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
    

class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast
        self.envi : list[Scope] = [] # stack of Scope

        global_scope = Scope([ # global scope built-in functions
            FunctionSymbol("readNumber", NumberType()),
            FunctionSymbol("readString", StringType()),
            FunctionSymbol("readBool", BoolType()),

            FunctionSymbol("writeNumber", VoidType(), [VariableSymbol("n", NumberType())]),
            FunctionSymbol("writeString", VoidType(), [VariableSymbol("s", StringType())]),
            FunctionSymbol("writeBool", VoidType(), [VariableSymbol("b", BoolType())])
        ])

        self.envi.append(global_scope) # global scope


    def checkRedeclared(self, kind : Kind, name: str, lst : Scope):
        print("checkRedeclared: ", kind, name, lst)

        symbols = lst.symbols
        if self.lookup(name, symbols, getName):
            raise Redeclared(kind, name)

    
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
        lst = self.envi[0]        
        symbols = lst.symbols

        if not self.lookup("main", symbols, getName):
            raise NoEntryPoint()
        return False
        

    def check(self):
        return self.visit(self.ast, None)


    def visitProgram(self, ast, param):
        print(ast)

        # Visit all declaration in program
        for decl in ast.decl:
            self.visit(decl, None)

        # Check for entry point
        self.checkEntry()
        
        self.envi.pop()

        return []

    def visitVarDecl(self, ast, param):
        print("visitVarDecl: ", ast)

        name = self.visit(ast.name, None)

        # Check for redeclared variable
        self.checkRedeclared(Variable(), name, self.envi[-1])
        
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


    
    def visitFuncDecl(self, ast, param):
        print(ast)

        name = self.visit(ast.name, None)
        
        # Check for redeclared function
        self.checkRedeclared(Function(), name, self.envi[-1])
        
        parameters = []
        if ast.param:
            self.envi.append(Scope()) # new scope for function parameters
            for astParam in ast.param:
                parameterSymbol = self.visit(astParam, None)
                parameters.append(parameterSymbol)
            
            self.envi.pop()
        
        body = self.visit(ast.body, None) if ast.body else None
        functionSymbol = FunctionSymbol(name, None, parameters, body)
        
        # Add function to current scope
        self.envi[-1].define(functionSymbol)
        
        return functionSymbol
    
    def visitNumberType(self, ast, param):
        return NumberType()
        
    
    def visitBoolType(self, ast, param):
        return BoolType()

    
    def visitStringType(self, ast, param):
        return StringType()

    
    def visitArrayType(self, ast, param):
        return ArrayType(ast.size, ast.eleType)

    
    def visitBinaryOp(self, ast, param):
        left = self.visit(ast.left, param)
        right = self.visit(ast.right, param)

        if ast.op in ['+', '-', '*', '/', '%']:
            if isinstance(left, NumberType) and isinstance(right, NumberType):
                return NumberType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['>', '>=', '<', '<=', '=', '!=']:
            if isinstance(left, NumberType) and isinstance(right, NumberType):
                return BoolType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['and', 'or']:
            if isinstance(left, BoolType) and isinstance(right, BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['...']:
            if isinstance(left, StringType) and isinstance(right, StringType):
                return StringType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['==']:
            if isinstance(left, StringType) and isinstance(right, StringType):
                return BoolType()
            raise TypeMismatchInExpression(ast)

        return None # No type can be inferred

    
    def visitUnaryOp(self, ast, param):
        expr = self.visit(ast.operand, param)

        if ast.op in ['-']:
            if isinstance(expr, NumberType):
                return NumberType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['not']:
            if isinstance(expr, BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)

        return None # No type can be inferred

    
    def visitCallExpr(self, ast, param):
        pass

    
    
    def visitId(self, ast, param):
        print("Visit Id: " , ast, param)
        if isinstance(param, ExprParam):
            if param.isDeclared:
                symbol = self.checkDeclared(Identifier(), ast.name, param.scopeIndex)
                
                print("Visit Id Found: ", symbol)
                return symbol.type
        
        else:
            return ast.name

    
    def visitArrayCell(self, ast, param):
        pass

    
    def visitBlock(self, ast, param):
        pass

    
    def visitIf(self, ast, param):
        pass

    
    def visitFor(self, ast, param):
        pass

    
    def visitContinue(self, ast, param):
        pass

    
    def visitBreak(self, ast, param):
        pass

    
    def visitReturn(self, ast, param):
        pass

    
    def visitAssign(self, ast, param):
        pass

    
    def visitCallStmt(self, ast, param):
        pass

    
    def visitNumberLiteral(self, ast, param):
        return NumberType()

    
    def visitBooleanLiteral(self, ast, param):
        return BoolType()

    
    def visitStringLiteral(self, ast, param):
        return StringType()

    
    def visitArrayLiteral(self, ast, param):
        pass

