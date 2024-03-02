from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class Symbol:
    def __init__(self, name : str, type : Type = None):
        self.name = name
        self.type = type

def getName(symbol : Symbol):
    return symbol.name    

class VariableSymbol(Symbol):
    def __init__(self, name : str, type : Type = None):
        self.name = name
        self.type = type

    def __str__(self):
        return f"VariableSymbol({self.name}, {self.type})"

class FunctionSymbol(Symbol):
    def __init__(self, name: str, type: Type = None, param: list[VariableSymbol] = [], body:Stmt =None):
        self.name = name
        self.type = type # return type of function
        self.param = param
        self.body = body

    def __str__(self):
        return f"FunctionSymbol({self.name}, {self.type}, [{', '.join(str(i) for i in self.param)}], {self.body})"

class Scope:
    def __init__(self, symbols = None):
        self.symbols = symbols if symbols is not None else []  # Initialize as empty list if None is provided
    def define(self, symbol : Symbol):
        self.symbols.append(symbol)

    def __str__(self) -> str:
        return f"Scope([{', '.join(str(i) for i in self.symbols)}])"

class Envi:
    def __init__(self, scope : None):
        if scope is None:
            scope = []
        self.scope : list[Scope] = scope
        self.functionScopeCount = 0
        self.isInsideLoop = 0

    def append(self, scope : Scope):
        self.scope.append(scope)

    def pop(self):
        self.scope.pop()

    def getLast(self) -> Scope:
        return self.scope[-1]

    def __getitem__(self, index : int):
        return self.scope[index]

    def __setitem__(self, index, value : Scope):
        self.scope[index] = value
    
    def __len__(self):
        return len(self.scope)

    def __str__(self) -> str:
        return f"Environtment({self.scope}, {self.isInsideFunction}, {self.isInsideLoop})"

class ExprParam: 
    def __init__(self, kind : Kind, isDeclared : bool = False,  inferredType : Type = None, inferredSymbol : Symbol = None) -> None:
        self.kind = kind
        self.isRHS = isDeclared
        self.inferredType = inferredType
        self.inferedSymbol = inferredSymbol

    def __str__(self) -> str:
        return f"IdParam({self.kind}, {self.scopeIndex}, {self.isRHS}, {self.inferredType})"

class VarDeclParam:
    def __init__(self, kind : Kind, scopeIndex : int) -> None:
        self.kind = kind
        self.scopeIndex = scopeIndex

    def __str__(self) -> str:
        return f"VarDeclParam({self.kind}, {self.scopeIndex})"

class StmtParam:
    def __init__(self):
        pass
       
        
    def __str__(self) -> str:
        pass
        
class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast
        self.envi : Envi = Envi([]) # global scope

        global_scope = Scope([ # global scope built-in functions
            FunctionSymbol("readNumber", NumberType(), [], Stmt()),
            FunctionSymbol("readString", StringType(), [], Stmt()),
            FunctionSymbol("readBool", BoolType(), [], Stmt()),

            FunctionSymbol("writeNumber", VoidType(), [VariableSymbol("n", NumberType())], Stmt()),
            FunctionSymbol("writeString", VoidType(), [VariableSymbol("s", StringType())], Stmt()),
            FunctionSymbol("writeBool", VoidType(), [VariableSymbol("b", BoolType())], Stmt())
        ])


        self.envi.append(global_scope) # global scope


    def checkRedeclaredVariable(self, kind : Kind, name: str, lst : Scope):
        print("checkRedeclared: ", kind, name, lst)

        symbols = lst.symbols
        if self.lookup(name, symbols, getName):
            raise Redeclared(kind, name)

    def checkRedeclaredFunction(self, name: str, lst : Scope) -> FunctionSymbol:
        print("checkRedeclaredFunction: ", name, lst)

        symbols = lst.symbols
        funcSymbol = self.lookup(name, symbols, getName)
        
        if funcSymbol is None:
            return None
        
        if type(funcSymbol) == FunctionSymbol:
            if funcSymbol.body:
                raise Redeclared(Function(), name)
            else :
                return funcSymbol
            
        raise Redeclared(Function(), name)     

    
    def checkDeclared(self, kind : Kind, name : str, envi : Envi) -> Symbol:
        #print("checkDeclared: ", name, lst)
        
        for i in range(len(envi) - 1, -1, -1): # from current scope to global scope
            print("checkDeclared Scope: ", i, envi[i])
            symbols = envi[i].symbols # list of Symbol in scope
           
            for symbol in symbols:
                if name == getName(symbol):
                    return symbol
                
        raise Undeclared(kind, name)
    

    def checkEntry(self):
        print("checkEntry: ", self.envi[0].symbols)

        globalSymbols = self.envi[0].symbols

        isFound = False
        for symbol in globalSymbols:
            if type(symbol) == FunctionSymbol and symbol.name == "main" and symbol.param == [] :#TODO : and symbol.type == VoidType:
                isFound = True
                
        if not isFound:
            raise NoEntryPoint()
        

    def check(self):
        return self.visit(self.ast, self.envi)


    def visitProgram(self, ast : Program, param):
        print(ast)

        # Visit all declaration in program
        for decl in ast.decl:
            if type(decl) == VarDecl:
                self.visit(decl, (self.envi, VarDeclParam(Variable(), len(self.envi)-1)))
            elif type(decl) == FuncDecl:
                self.visit(decl, (self.envi, None))

        # Check for entry point
        self.checkEntry()
        
        self.envi.pop()

        return []

    def visitVarDecl(self, ast : VarDecl, param : tuple[Envi, VarDeclParam]):
        print("visitVarDecl: ", ast)

        (envi, varDeclParam) = param
        name = self.visit(ast.name, (envi, None))

        # Check for redeclared variable
        if varDeclParam:
            self.checkRedeclaredVariable(varDeclParam.kind, name, envi.getLast())
        
        current_scope = envi.getLast()
        
        # Visit variable type
        if ast.modifier == "var":
            varInitType = self.visit(ast.varInit, (envi, None)) if ast.varInit else None
            
            if varInitType is None:
                raise TypeCannotBeInferred(ast)
            
            current_scope.define(VariableSymbol(name, varInitType))
        
        elif ast.modifier == "dynamic":    
            varInitType = self.visit(ast.varInit, (envi, None)) if ast.varInit else None
            current_scope.define(VariableSymbol(name, ast.varType))


        else: # no modifier
            varType = self.visit(ast.varType, (envi, None))
            
            symbol = VariableSymbol(name, varType)
            
            if ast.varInit:
                varInitType = self.visit(ast.varInit, (envi, ExprParam(Variable(), True, varType, symbol)))
                if type(varType) != type(varInitType):
                    raise TypeMismatchInStatement(ast)
            
            envi.getLast().define(symbol)
            return symbol
    
    def visitFuncDecl(self, ast : FuncDecl, param : tuple[Envi, None]):
        print(ast)

        (envi, _) = param
        name = self.visit(ast.name, (envi, None))
        
        def visitFuncParam():
            parameters = []
            if ast.param:
                envi.append(Scope()) # new scope for function parameters
                for astParam in ast.param:
                    parameterSymbol = self.visit(astParam, (envi, VarDeclParam(Parameter(), len(envi)-1)))
                    parameters.append(parameterSymbol)
                
                envi.pop()
                print(len(envi),envi.getLast())
            return parameters

        def visitFuncBody():
            envi.functionScopeCount += 1
            body = self.visit(ast.body, (envi, None)) if ast.body else None # declare only or implement function
            envi.functionScopeCount -= 1
            return body

        # Check for redeclared function
        function = self.checkRedeclaredFunction(name, envi.getLast())

        if function is None: # first declaration of function 

            parameters = visitFuncParam()
            body = visitFuncBody()

            functionSymbol = FunctionSymbol(name, None, parameters, body) # TODO : return type of function
        
            # Add function to current scope
            envi.getLast().define(functionSymbol)
        
            return functionSymbol
    
        else: # implement the body function
            
            if ast.body is None:
                raise Redeclared(Function(), name) # redeclared a declared-only function

            # Check for redeclared parameters
            parameters = visitFuncParam()

            # Create lists of parameter types
            function_param_types = list(map(lambda param: type(param.type), function.param))
            parameters_types = list(map(lambda param: type(param.type), parameters))

            # Compare the lists of parameter types
            if function_param_types != parameters_types:
                raise Redeclared(Function(), name)

            # Already Have a function declared the body or the body supposed to have is None
            if function.body or ast.body is None:
                raise Redeclared(Function(), name)

            # Visit function body
            body = visitFuncBody()
            function.body = body


            return function


    def visitNumberType(self, ast : NumberType, param):
        return NumberType()
        
    
    def visitBoolType(self, ast : BoolType, param):
        return BoolType()

    
    def visitStringType(self, ast : StringType, param):
        return StringType()

    
    def visitArrayType(self, ast : ArrayType, param):
        return ArrayType(ast.size, ast.eleType)

    
    def visitBinaryOp(self, ast : BinaryOp, param : tuple[Envi, ExprParam]):
        
        (envi, exprParam) = param

        inferredOperandType = None
        inferredReturnType = None

        if ast.op in ['+', '-', '*', '/', '%']:
            inferredOperandType = NumberType()
            inferredReturnType = NumberType()
           
        
        if ast.op in ['>', '>=', '<', '<=', '=', '!=']:
            inferredOperandType = NumberType()
            inferredReturnType = BoolType()
            
        if ast.op in ['and', 'or']:
            inferredOperandType = BoolType()
            inferredReturnType = BoolType()
            
        if ast.op in ['...']:
            inferredOperandType = StringType()
            inferredReturnType = StringType()
            
        if ast.op in ['==']:
            inferredOperandType = StringType()
            inferredReturnType = BoolType()

        operandParam = None
        if exprParam:
            operandParam = ExprParam(Variable(), exprParam.isRHS, inferredOperandType)

        left = self.visit(ast.left, (envi, operandParam))
        right = self.visit(ast.right, (envi, operandParam))
        

        if type(left) != type(right) or type(left) != type(inferredOperandType):
            raise TypeMismatchInExpression(ast)

        return inferredReturnType # return type of binary operation

    
    def visitUnaryOp(self, ast : UnaryOp, param : tuple[Envi, ExprParam]):
        (envi, exprParam) = param

        inferredOperandType = None
        inferredReturnType = None

        if ast.op in ['-']:
            inferredOperandType = NumberType()
            inferredReturnType = NumberType()
        
        if ast.op in ['not']:
            inferredOperandType = BoolType()
            inferredReturnType = BoolType()

        operandParam = None
        if exprParam:
            operandParam = ExprParam(Variable(), exprParam.isRHS , inferredOperandType)
        expr = self.visit(ast.operand, (envi, operandParam))
        
        if type(expr) != type(inferredOperandType):
            raise TypeMismatchInExpression(ast)

        return inferredReturnType # No type can be inferred

    
    def visitCallExpr(self, ast, param):
        pass

    
    
    def visitId(self, ast : Id, param : tuple[Envi, ExprParam]):
        print("Visit Id: " , ast, param)
        (envi, exprParam) = param
        if type(exprParam) == ExprParam:
            if exprParam.isRHS:
                symbol = self.checkDeclared(Identifier(), ast.name, envi)
                
                print("Visit Id Found: ", symbol)
                return symbol.type
        
        else:
            return ast.name

    
    def visitArrayCell(self, ast : ArrayCell, param):
        pass

    
    def visitBlock(self, ast : Block, param):
        return True # TODO : return type of block

    
    def visitIf(self, ast : If, param):
        return True # TODO : return type of block

    
    def visitFor(self, ast : For, param):



        return True # TODO : return type of block

    
    def visitContinue(self, ast : Continue, param):
        return True # TODO : return type of block

    
    def visitBreak(self, ast : Break, param):
        return True # TODO : return type of block

    
    def visitReturn(self, ast : Return, param : tuple[Envi, StmtParam]):
        
        (envi, stmtParam) = param
        if envi.functionScopeCount == 0:
            raise ReturnNotInFunction()

        if ast.expr:
            return self.visit(ast.expr, param)

        return VoidType() 

    
    def visitAssign(self, ast : Assign, param):
        return True # TODO : return type of block

    
    def visitCallStmt(self, ast : CallStmt, param):
        print("Call Stmt: ",ast)
        return True # TODO : return type of block


    
    def visitNumberLiteral(self, ast : NumberLiteral, param):
        return NumberType()

    
    def visitBooleanLiteral(self, ast : BooleanLiteral, param):
        return BoolType()

    
    def visitStringLiteral(self, ast : StringLiteral, param):
        return StringType()

    
    def visitArrayLiteral(self, ast : ArrayLiteral, param):
        pass

