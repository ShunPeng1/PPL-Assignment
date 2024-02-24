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
    def __init__(self, symbols: list[Symbol] = []):
        self.symbols = symbols # list of Symbol

    def define(self, symbol : Symbol):
        self.symbols.append(symbol)

    def __str__(self) -> str:
        return f"Scope([{', '.join(str(i) for i in self.symbols)}])"

class ExprParam: 
    def __init__(self, kind : Kind, scopeIndex : int, isDeclared : bool = False) -> None:
        self.kind = kind
        self.scopeIndex = scopeIndex
        self.isDeclared = isDeclared

    def __str__(self) -> str:
        return f"IdParam({self.kind}, {self.scopeIndex}, {self.isDeclared})"

class VarDeclParam:
    def __init__(self, kind : Kind, scopeIndex : int) -> None:
        self.kind = kind
        self.scopeIndex = scopeIndex

    def __str__(self) -> str:
        return f"VarDeclParam({self.kind}, {self.scopeIndex})"

class StmtParam:
    def __init__(self, isInFunction = False, isInLoop = False) -> None:
        self.isInFunction = isInFunction
        self.isInLoop = isInLoop
        
    def __str__(self) -> str:
        return f"StmtParam({self.isInFunction}, {self.isInLoop})"

class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast
        self.envi : list[Scope] = [] # stack of Scope

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
        
        if funcSymbol == None:
            return None
        
        if type(funcSymbol) == FunctionSymbol:
            if funcSymbol.body == None:
                return funcSymbol
         
        raise Redeclared(FunctionSymbol(), name)
    
    def checkDeclared(self, kind : Kind, name : str, current_scope_index : int) -> Symbol:
        #print("checkDeclared: ", name, lst)
        
        for i in range(current_scope_index, -1, -1): # from current scope to global scope
            print("checkDeclared Scope: ", i, self.envi[i])
            symbols = self.envi[i].symbols # list of Symbol in scope
           
            for symbol in symbols:
                if name == getName(symbol):
                    return symbol
                
        raise Undeclared(kind, name)
    

    def checkEntry(self):
        print("checkEntry: ")

        globalSymbols = self.envi[0].symbols

        isFound = False
        for symbol in globalSymbols:
            if type(symbol) == FunctionSymbol and symbol.name == "main" and symbol.param == [] and symbol.type == VoidType:
                isFound = True
                
        if not isFound:
            raise NoEntryPoint()
        

    def check(self):
        return self.visit(self.ast, None)


    def visitProgram(self, ast : Program, param):
        print(ast)

        # Visit all declaration in program
        for decl in ast.decl:
            if type(decl) == VarDecl:
                self.visit(decl, VarDeclParam(Variable(), len(self.envi)-1))
            elif type(decl) == FuncDecl:
                self.visit(decl, None)

        # Check for entry point
        self.checkEntry()
        
        self.envi.pop()

        return []

    def visitVarDecl(self, ast : VarDecl, param : VarDeclParam):
        print("visitVarDecl: ", ast)

        name = self.visit(ast.name, None)

        # Check for redeclared variable
        if param:
            self.checkRedeclaredVariable(param.kind, name, self.envi[-1])
        
        current_scope = self.envi[-1]
        current_scope_index = len(self.envi) - 1
        
        # Visit variable type
        if ast.modifier == "var":
            varInitType = self.visit(ast.varInit, None) if ast.varInit else None
            current_scope.define(VariableSymbol(name, ast.varType))
        
        elif ast.modifier == "dynamic":    
            varInitType = self.visit(ast.varInit, None) if ast.varInit else None
            current_scope.define(VariableSymbol(name, ast.varType))


        else: # no modifier
            varType = self.visit(ast.varType, None)
            if ast.varInit:
                varInitType = self.visit(ast.varInit, ExprParam(Variable(), current_scope_index, True))
                if type(varType) != type(varInitType):
                    raise TypeMismatchInStatement(ast)

            symbol = VariableSymbol(name, varType)
            
            self.envi[-1].define(symbol)
            return symbol


    
    def visitFuncDecl(self, ast : FuncDecl, param):
        print(ast)

        name = self.visit(ast.name, None)
        
        # Check for redeclared function
        function = self.checkRedeclaredFunction(name, self.envi[-1])

        if function == None: # first declaration of function 

            parameters = []
            if ast.param:
                self.envi.append(Scope()) # new scope for function parameters
                for astParam in ast.param:
                    parameterSymbol = self.visit(astParam, VarDeclParam(Parameter(), len(self.envi)-1))
                    parameters.append(parameterSymbol)
                
                self.envi.pop()
            
            body = self.visit(ast.body, None) if ast.body else None # declare only or implement function
            functionSymbol = FunctionSymbol(name, None, parameters, body) # TODO : return type of function
        
            # Add function to current scope
            self.envi[-1].define(functionSymbol)
        
            return functionSymbol
    
        else: # implement the body function
            
            body = self.visit(ast.body, None)
            if body == None:
                raise Redeclared(Function(), name) # redeclared a declared-only function

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

    
    def visitBinaryOp(self, ast : BinaryOp, param):
        left = self.visit(ast.left, param)
        right = self.visit(ast.right, param)

        if ast.op in ['+', '-', '*', '/', '%']:
            if (type(left) == NumberType) and (type(right)== NumberType):
                return NumberType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['>', '>=', '<', '<=', '=', '!=']:
            if (type(left) == NumberType) and (type(right)== NumberType):    return BoolType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['and', 'or']:
            if (type(left) == BoolType) and (type(right) == BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['...']:
            if (type(left) == StringType) and (type(right) == StringType):
                return StringType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['==']:
            if (type(left) == StringType) and (type(right) == StringType):
                return BoolType()
            raise TypeMismatchInExpression(ast)

        return None # No type can be inferred

    
    def visitUnaryOp(self, ast : UnaryOp, param):
        expr = self.visit(ast.operand, param)

        if ast.op in ['-']:
            if type(expr) == NumberType:
                return NumberType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['not']:
            if type(expr) == BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ast)

        return None # No type can be inferred

    
    def visitCallExpr(self, ast, param):
        pass

    
    
    def visitId(self, ast : Id, param):
        print("Visit Id: " , ast, param)
        if type(param) == ExprParam:
            if param.isDeclared:
                symbol = self.checkDeclared(Identifier(), ast.name, param.scopeIndex)
                
                print("Visit Id Found: ", symbol)
                return symbol.type
        
        else:
            return ast.name

    
    def visitArrayCell(self, ast : ArrayCell, param):
        pass

    
    def visitBlock(self, ast : Block, param):
        pass

    
    def visitIf(self, ast : If, param):
        pass

    
    def visitFor(self, ast : For, param):
        pass

    
    def visitContinue(self, ast : Continue, param):
        pass

    
    def visitBreak(self, ast : Break, param):
        pass

    
    def visitReturn(self, ast : Return, param):
        pass

    
    def visitAssign(self, ast : Assign, param):
        pass

    
    def visitCallStmt(self, ast : CallStmt, param):
        print("Call Stmt: ",ast)


    
    def visitNumberLiteral(self, ast : NumberLiteral, param):
        return NumberType()

    
    def visitBooleanLiteral(self, ast : BooleanLiteral, param):
        return BoolType()

    
    def visitStringLiteral(self, ast : StringLiteral, param):
        return StringType()

    
    def visitArrayLiteral(self, ast : ArrayLiteral, param):
        pass

