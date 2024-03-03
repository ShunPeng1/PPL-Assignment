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
        return f"Environtment({self.scope})"

class ExprParam: 
    def __init__(self, kind : Kind, isRHS : bool = False, isDeclared : bool = False, inferredType : Type = None, inferredSymbol : Symbol = None) -> None:
        self.kind = kind
        self.isRHS = isRHS
        self.isDeclared = isDeclared
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
    def __init__(self, currentFunctionSymbol : FunctionSymbol = None, insideLoopCount : int = 0) -> None:
        if currentFunctionSymbol is None:
            currentFunctionSymbol = None
        self.currentFunctionSymbol = currentFunctionSymbol
        self.insideLoopCount = 0
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


    def checkRedeclared(self, kind : Function | Variable | Parameter, name: str, lst : Scope):
        print("checkRedeclared: ", kind, name, lst)

        symbols = lst.symbols
        symbol = self.lookup(name, symbols, getName)
        if symbol:
            raise Redeclared(kind, name)

        return None # No symbol found

    
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
        
    def checkFunctionDefined(self):
        globalSymbols = self.envi[0].symbols

        for symbol in globalSymbols:
            if type(symbol) == FunctionSymbol and symbol.body is None:
                raise NoDefinition(symbol.name)


    def getSymbol(self, name : str, isOnlyLastScope : bool, envi : Envi) -> Symbol:
        print("getSymbol: ", name, envi)

        if isOnlyLastScope:
            return self.lookup(name, envi.getLast().symbols, getName)

        for i in range(len(envi) - 1, -1, -1): # from current scope to global scope
            print("checkDeclared Scope: ", i, envi[i])
            symbols = envi[i].symbols # list of Symbol in scope
           
            for symbol in symbols:
                if name == getName(symbol):
                    return symbol

        return None # No symbol found


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

        
        # Check for function defined
        self.checkFunctionDefined()
        
        # Check for entry point
        self.checkEntry()

        self.envi.pop()

        return []

    def visitVarDecl(self, ast : VarDecl, param : tuple[Envi, VarDeclParam]):
        print("visitVarDecl: ", ast)

        (envi, varDeclParam) = param
        name = ast.name.name
        self.visit(ast.name, (envi, ExprParam(varDeclParam.kind, False, False)))
        
        current_scope = envi.getLast()
        
        # Visit variable type
        if ast.modifier == "var":
            varInitType = self.visit(ast.varInit, (envi, ExprParam(Identifier, True, True))) if ast.varInit else None
            
            if varInitType is None:
                raise TypeCannotBeInferred(ast)
            
            current_scope.define(VariableSymbol(name, varInitType))
        
        elif ast.modifier == "dynamic":  
            varSymbol = VariableSymbol(name, None)  
            if ast.varInit:
                varInitType = self.visit(ast.varInit, (envi, ExprParam(Variable(), True, True)))
                
                if varInitType is None:
                    raise TypeCannotBeInferred(ast)
                
                varSymbol = VariableSymbol(name, varInitType)
                
            current_scope.define(varSymbol)

        else: # no modifier
            varType = self.visit(ast.varType, (envi, None))
            
            symbol = VariableSymbol(name, varType)
            
            if ast.varInit:
                varInitType = self.visit(ast.varInit, (envi, ExprParam(Variable(), True, True, varType, symbol)))
                if type(varType) != type(varInitType):
                    raise TypeMismatchInStatement(ast)
            
            current_scope.define(symbol)
            return symbol
    
    def visitFuncDecl(self, ast : FuncDecl, param : tuple[Envi, None]):
        print(ast)

        (envi, _) = param

        # Get function symbol
        name = ast.name.name
        functionSymbol = self.getSymbol(name, True, envi)
        self.visit(ast.name, (envi, ExprParam(Function(), False, functionSymbol is not None)))
        
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

        def visitFuncBody(functionSymbol : FunctionSymbol = None):
            stmtParam = StmtParam(functionSymbol, 0)
            body = self.visit(ast.body, (envi, stmtParam)) if ast.body else None # declare only or implement function
            stmtParam.isInsideFunction = False
            return body

        
        if functionSymbol is None: # first declaration of function 
            
            functionSymbol = FunctionSymbol(name, None, [], None) # TODO : return type of function
        
            # Visit function parameters and body
            parameters = visitFuncParam()
            functionSymbol.param = parameters
            body = visitFuncBody(functionSymbol)
            functionSymbol.body = body
        
            # Add function to current scope
            envi.getLast().define(functionSymbol)
        
            return functionSymbol
    
        elif type(functionSymbol) == FunctionSymbol: # implement the body function
            
            if ast.body is None:
                raise Redeclared(Function(), name) # redeclared a declared-only function

            # Check for redeclared parameters
            parameters = visitFuncParam()

            # Create lists of parameter types
            function_param_types = list(map(lambda param: type(param.type), functionSymbol.param))
            parameters_types = list(map(lambda param: type(param.type), parameters))

            # Compare the lists of parameter types
            if function_param_types != parameters_types:
                raise Redeclared(Function(), name)

            # Already Have a function declared the body 
            if functionSymbol.body :
                raise Redeclared(Function(), name)
            elif ast.body is None : # already have a declared-only function and redeclared with no body
                raise Redeclared(Function(), name)

            # Visit function body
            body = visitFuncBody(functionSymbol)
            functionSymbol.body = body

            return functionSymbol
    
        else:
            raise Redeclared(Function(), name)

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
            operandParam = ExprParam(Variable(), True, True, inferredOperandType)

        left = self.visit(ast.left, (envi, operandParam))
        right = self.visit(ast.right, (envi, operandParam))
        

        if type(right) != type(inferredOperandType) or type(left) != type(inferredOperandType):
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
            operandParam = ExprParam(Variable(), True, True, inferredOperandType)
        expr = self.visit(ast.operand, (envi, operandParam))
        
        if type(expr) != type(inferredOperandType):
            raise TypeMismatchInExpression(ast)

        return inferredReturnType # No type can be inferred

    
    def visitCallExpr(self, ast, param : tuple[Envi, ExprParam]):
        print("Call Stmt: ",ast)

        (envi, exprParam) = param

        name = ast.name.name
        self.visit(ast.name, (envi, ExprParam(Function(), True, True)))
        symbol = self.getSymbol(name, False, envi)

        if symbol is None:
            raise Undeclared(Function(), ast.name)

        if type(symbol) != FunctionSymbol:
            raise TypeMismatchInExpression(ast)

        if len(ast.args) != len(symbol.param):
            raise TypeMismatchInExpression(ast)

        for i in range(len(ast.args)):
            symbolParamType = symbol.param[i].type
            callParamType = self.visit(ast.args[i], (envi, ExprParam(Variable(), True, True, symbolParamType, symbol.param[i])))
            if type(callParamType) != type(symbolParamType):
                raise TypeMismatchInExpression(ast)

        if symbol.body is None: # function declared-only
            symbol.type = exprParam.inferredType
        elif type(symbol.type) != exprParam.inferredType: # this must be a void function
            raise TypeMismatchInExpression(ast)    
            
        return symbol.type # TODO : return of a statement


    
    
    def visitId(self, ast : Id, param : tuple[Envi, ExprParam]):
        print("Visit Id: " , ast, param)
        (envi, exprParam) = param
        if type(exprParam) == ExprParam:
            if exprParam.isRHS:
                symbol = self.checkDeclared(Identifier(), ast.name, envi)
                
                if symbol.type :                  
                    return symbol.type
                elif exprParam.inferredType : # Inferred type
                    symbol.type = exprParam.inferredType
                    return symbol.type
                else :
                    return None # No type can be inferred, will raise error in parent node
        
            else : # LHS
                if exprParam.isDeclared:
                    symbol = self.checkDeclared(Identifier(), ast.name, envi)
                    return symbol.type
                else : # not declared
                    self.checkRedeclared(exprParam.kind, ast.name, envi.getLast())
                    return None # No type can be inferred, will raise error in parent node

        else:
            return ast.name

    
    def visitArrayCell(self, ast : ArrayCell, param):
        pass

    
    def visitBlock(self, ast : Block, param : tuple[Envi, StmtParam]):
        print("Visit Block: ", ast)
        
        (envi, stmtParam) = param

        envi.append(Scope())

        for stmt in ast.stmt:
            if type(stmt) == VarDecl:
                self.visit(stmt, (envi, VarDeclParam(Variable(), len(self.envi)-1)))
            else:
                self.visit(stmt, (envi, stmtParam))

        envi.pop()


        return True # TODO : return of a statement

    
    def visitIf(self, ast : If, param : tuple[Envi, StmtParam]):
        print("Visit If: ", ast)

        (envi, stmtParam) = param

        ifConditionType = self.visit(ast.expr, (envi, ExprParam(Variable(), True, True, BoolType())))

        if type(ifConditionType) != BoolType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.thenStmt, (envi, stmtParam))

        for (elifExpr, elifStmt) in ast.elifStmt:
            elifConditionType = self.visit(elifExpr, (envi, ExprParam(Variable(), True, True, BoolType())))
            
            if type(elifConditionType) != BoolType:
                raise TypeMismatchInStatement(ast)

            self.visit(elifStmt, (envi, stmtParam))
        
        if ast.elseStmt:
            self.visit(ast.elseStmt, (envi, stmtParam))

        return True # TODO : return of a statement

    
    def visitFor(self, ast : For, param):
        print("Visit For: ", ast)

        (envi, stmtParam) = param

        # Copy from visitAssign        
        lhsType = self.visit(ast.name, (envi, ExprParam(Variable(), False, True)))
        symbol = self.getSymbol(ast.name.name, False, envi)

        if lhsType: # LHS is declared and has type
            rhsType = self.visit(ast.updExpr, (envi, ExprParam(Variable(), True, True, lhsType, symbol)))

            if type(lhsType) != type(rhsType):
                raise TypeMismatchInStatement(ast)
        else: # LHS first use
            rhsType = self.visit(ast.updExpr, (envi, ExprParam(Variable(), True, True, None, symbol)))
            
            if rhsType is None:
                raise TypeCannotBeInferred(ast)

            symbol.type = rhsType

        # Visit condition of for loop
        condType = self.visit(ast.condExpr, (envi, ExprParam(Variable(), True, True, BoolType())))
        if type(condType) != BoolType:
            raise TypeMismatchInStatement(ast)
        
        # Visit body of for loop
        stmtParam.insideLoopCount += 1
        self.visit(ast.body, (envi, stmtParam))
        stmtParam.insideLoopCount -= 1

        return True # TODO : return of a statement

    
    def visitContinue(self, ast : Continue, param : tuple[Envi, StmtParam]):
        print("Visit Continue: ", ast)

        (envi, stmtParam) = param

        if stmtParam.insideLoopCount == 0:
            raise MustInLoop(ast)
        
        return True # TODO : return of a statement

    
    def visitBreak(self, ast : Break, param):
        print("Visit Break: ", ast)

        (envi, stmtParam) = param

        if stmtParam.insideLoopCount == 0:
            raise MustInLoop(ast)

        return True # TODO : return of a statement
    
    def visitReturn(self, ast : Return, param : tuple[Envi, StmtParam]):
        
        (envi, stmtParam) = param



        if ast.expr:
            return self.visit(ast.expr, param)

        return VoidType() 

    
    def visitAssign(self, ast : Assign, param : tuple[Envi, StmtParam]):
        
        (envi, stmtParam) = param

        lhsType = self.visit(ast.lhs, (envi, ExprParam(Variable(), False, True)))
        symbol = self.getSymbol(ast.lhs.name, False, envi)

        if lhsType: # LHS is declared and has type
            rhsType = self.visit(ast.rhs, (envi, ExprParam(Variable(), True, True, lhsType, symbol)))

            if type(lhsType) != type(rhsType):
                raise TypeMismatchInStatement(ast)
        else: # LHS first use
            rhsType = self.visit(ast.rhs, (envi, ExprParam(Variable(), True, True, None, symbol)))
            
            if rhsType is None:
                raise TypeCannotBeInferred(ast)

            symbol.type = rhsType

        
        return True # TODO : return of a statement

    
    def visitCallStmt(self, ast : CallStmt, param : tuple[Envi, StmtParam]):
        print("Call Stmt: ",ast)

        (envi, stmtParam) = param

        name = ast.name.name
        self.visit(ast.name, (envi, ExprParam(Function(), True, True)))
        symbol = self.getSymbol(name, False, envi)

        if symbol is None:
            raise Undeclared(Function(), ast.name)

        if type(symbol) != FunctionSymbol:
            raise TypeMismatchInStatement(ast)

        if len(ast.args) != len(symbol.param):
            raise TypeMismatchInStatement(ast)

        for i in range(len(ast.args)):
            symbolParamType = symbol.param[i].type
            callParamType = self.visit(ast.args[i], (envi, ExprParam(Variable(), True, True, symbolParamType, symbol.param[i])))
            if type(callParamType) != type(symbolParamType):
                raise TypeMismatchInStatement(ast)

        if symbol.body is None: # function declared-only
            symbol.type = VoidType()
        elif type(symbol.type) != VoidType: # this must be a void function
            raise TypeMismatchInStatement(ast)    
            
        return True # TODO : return of a statement


    
    def visitNumberLiteral(self, ast : NumberLiteral, param):
        return NumberType()

    
    def visitBooleanLiteral(self, ast : BooleanLiteral, param):
        return BoolType()

    
    def visitStringLiteral(self, ast : StringLiteral, param):
        return StringType()

    
    def visitArrayLiteral(self, ast : ArrayLiteral, param):
        pass

