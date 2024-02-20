from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class VariableSymbol:
    def __init__(self, name : str, type : Type = None):
        self.name = name
        self.type = type


class FunctionSymbol:
    def __init__(self, name: str, returnType: Type = None, param: list[VariableSymbol] = None, body:Stmt =None):
        self.name = name
        self.returnType = returnType
        self.param = param
        self.body = body

class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast
        self.envi = []

    def visitProgram(self, ast, param):
        print(ast)
        
        

    
    def visitVarDecl(self, ast, param):
        pass

    
    def visitFuncDecl(self, ast, param):
        pass

    
    def visitNumberType(self, ast, param):
        pass

    
    def visitBoolType(self, ast, param):
        pass

    
    def visitStringType(self, ast, param):
        pass

    
    def visitArrayType(self, ast, param):
        pass

    
    def visitBinaryOp(self, ast, param):
        pass

    
    def visitUnaryOp(self, ast, param):
        pass

    
    def visitCallExpr(self, ast, param):
        pass

    
    def visitId(self, ast, param):
        pass

    
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

