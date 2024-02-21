from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class Symbol:
    def __init__(self, name : str):
        self.name = name

def getName(symbol : Symbol):
    return symbol.name    

class VariableSymbol(Symbol):
    def __init__(self, name : str, type : Type = None):
        self.name = name
        self.type = type

    def __str__(self):
        return f"VariableSymbol({self.name}, {self.type})"

class FunctionSymbol(Symbol):
    def __init__(self, name: str, returnType: Type = None, param: list[VariableSymbol] = [], body:Stmt =None):
        self.name = name
        self.returnType = returnType
        self.param = param
        self.body = body

    def __str__(self):
        return f"FunctionSymbol({self.name}, {self.returnType}, [{', '.join(str(i) for i in self.param)}], {self.body})"

class Scope:
    def __init__(self, symbols: list[Symbol] = [Symbol]):
        self.symbols = symbols # list of Symbol

    def define(self, symbol : Symbol):
        self.symbols.append(symbol)

    def __str__(self) -> str:
        return f"Scope([{', '.join(str(i) for i in self.symbols)}])"


class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast
        self.envi = [Scope] # stack of Scope

        global_scope = Scope([
            FunctionSymbol("readNumber", NumberType),
            FunctionSymbol("readString", StringType),
            FunctionSymbol("readBool", BoolType),

            FunctionSymbol("writeNumber", VoidType, [VariableSymbol("n", NumberType)]),
            FunctionSymbol("writeString", VoidType, [VariableSymbol("s", StringType)]),
            FunctionSymbol("writeBool", VoidType, [VariableSymbol("b", BoolType)])
        ])

        self.envi.append(global_scope) # global scope

        print("StaticChecker: ", ast)

    def checkRedeclared(self, kind : Kind, name: str, lst : Scope):
        print("checkRedeclared: ", kind, id, lst)

        symbols = lst.symbols
        if self.lookup(name, symbols, getName):
            raise Redeclared(kind, name)
        return False
    
    def checkEntry(self, name : str, lst : Scope):
        print("checkEntry: ", id, lst)
        symbols = lst.symbols

        if not self.lookup(id, symbols, getName):
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
        self.checkEntry("main", self.envi[-1])
        
        self.envi.pop()

    def visitVarDecl(self, ast, param):
        print(ast)

        name = self.visit(ast.name, None)
        varInit = self.visit(ast.varInit, None) if ast.varInit else None

        if self.checkRedeclared(Variable(), name, self.envi[-1]):
            return

        
        # Visit variable type
        if ast.modifier == "var":
            pass
        elif ast.modifier == "dynamic":
            pass
        else:
            pass

        # Add variable to current scope
        self.envi[-1].define(VariableSymbol(name, ast.varType))
    
    def visitFuncDecl(self, ast, param):
        print(ast)
        name = self.visit(ast.name, None)
        
        if self.checkRedeclared(Function(), name, self.envi[-1]):
            return
        
        if ast.param:
            self.envi.append(Scope()) # 
            for param in ast.param:
                self.visit(param, None)
            
            self.envi.pop()
        
        # Add function to current scope
        self.envi[-1].define(FunctionSymbol(name, None, [], ast.body))
    
    def visitNumberType(self, ast, param):
        return NumberType()
        
    
    def visitBoolType(self, ast, param):
        return BoolType()

    
    def visitStringType(self, ast, param):
        return StringType()

    
    def visitArrayType(self, ast, param):
        return ArrayType(ast.size, ast.eleType)

    
    def visitBinaryOp(self, ast, param):
        pass

    
    def visitUnaryOp(self, ast, param):
        pass

    
    def visitCallExpr(self, ast, param):
        pass

    
    def visitId(self, ast, param):
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
        pass

    
    def visitBooleanLiteral(self, ast, param):
        pass

    
    def visitStringLiteral(self, ast, param):
        pass

    
    def visitArrayLiteral(self, ast, param):
        pass

