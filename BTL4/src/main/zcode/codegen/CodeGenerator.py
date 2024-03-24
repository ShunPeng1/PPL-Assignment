from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *

from typing import List, Union, Tuple


## Make missing classes



class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value

class ClassType (Type):
    def __init__(self, ctype):
        self.classname = ctype # Id

class Instance:
    def __init__(self):
        pass

class ClassName(Val):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"ClassName({self.value})"

class ClassDecl (Decl):
    def __init__(self, classname : ClassName, memlist : list[Decl]):
        self.classname : ClassName = classname # Id
        self.memlist : list[Decl] = memlist # list of Decl

    def __str__(self):
        memlist_str = ', '.join(str(mem) for mem in self.memlist)
        return f"ClassDecl({self.classname}, [{memlist_str}] )"

class MethodType(Type):
    def __init__(self, partype, rettype):
        self.partype = partype # list of Type
        self.rettype = rettype # Type

    def __str__(self):
        return f"MethodType({self.partype}, {self.rettype})"


class MethodDecl:
    # instance: Instance
    # name: Id
    # param: list[VarDecl]
    # returnType: Type
    # body: Block

    def __init__(self, instance, name, param, returnType, body):
        self.instance = instance # Not used but keep for consistency
        self.name = name # Id
        self.param = param # list of VarDecl
        self.returnType = returnType # Type
        self.body = body # Block

    def __str__(self):
        return f"MethodDecl({self.name}, {self.param}, {self.returnType}, {self.body})"

class Symbol:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Symbol({self.name})"

class VariableSymbol(Symbol):
    def __init__(self, name : str, type : Type = None, position = 0, isStatic : bool = False, astVarDecl : VarDecl = None):
        self.name = name
        self.type = type
        self.position = position
        self.isStatic = isStatic
        self.astVarDecl = astVarDecl

    def __str__(self):
        return f"VariableSymbol({self.name}, {self.type})"


class FunctionSymbol(Symbol):
    def __init__(self, name, methodType = MethodType([],None), param : list[VariableSymbol] = None, body = None, astFuncDecl=None, className : ClassName = None):
        self.name = name
        self.methodType : MethodType = methodType  # MethodType
        if param is None:
            param = []
        self.param = param

        self.body = body
        self.astFuncDecl = astFuncDecl

    def __str__(self):
        return f"FunctionSymbol({self.name}, {self.methodType})"

   
class SubBody():
    def __init__(self, frame : Frame, sym : list[FunctionSymbol]):
        self.frame : Frame = frame
        self.sym : list[FunctionSymbol] = sym # list of Symbol


class Scope:
    def __init__(self, symbols = None):
        self.symbols = symbols if symbols is not None else []  # Initialize as empty list if None is provided
    
    def define(self, symbol : FunctionSymbol):
        self.symbols.append(symbol)

    def __str__(self) -> str:
        return f"Scope([{', '.join(str(i) for i in self.symbols)}])"

class Envi:
    def __init__(self, scope : None):
        if scope is None:
            scope = []
        self.scope : List[Scope] = scope
        self.itr = len(scope)-1

    def append(self, scope : Scope):
        self.scope.append(scope)

    def pop(self):
        self.scope.pop()

    def next_iterator(self):
        if self.itr < len(self.scope) - 1:
            self.itr += 1
        return self.scope[self.itr]
        
    def previous_iterator(self):
        if self.itr > 0:
            self.itr -= 1
        return self.scope[self.itr] 

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
    def __init__(self, isRHS : bool = False, isDeclared : bool = False, inferredType : Type = None) -> None:
        self.isRHS = isRHS
        self.isDeclared = isDeclared
        self.inferredType = inferredType

    def __str__(self) -> str:
        return f"IdParam({self.isRHS}, {self.inferredType})"

class VarDeclParam():
    def __init__(self, isStatic, index):
        self.isStatic = isStatic
        self.index = index


class StmtParam:
    def __init__(self, currentFunctionSymbol : FunctionSymbol = None, insideLoopCount : int = 0) -> None:
        if currentFunctionSymbol is None:
            currentFunctionSymbol = None
        self.currentFunctionSymbol = currentFunctionSymbol
        self.insideLoopCount = 0
        pass
       
        
    def __str__(self) -> str:
        pass

## End of missing classes

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        currClassName = ClassName(self.libName)
        return Envi([Scope([
            FunctionSymbol("readNumber", MethodType([], NumberType()), className= currClassName),
            FunctionSymbol("readString", MethodType([], StringType()), className= currClassName),
            FunctionSymbol("readBool", MethodType([], BoolType()), className= currClassName),
            FunctionSymbol("writeNumber", MethodType([NumberType()], VoidType()), className= currClassName),
            FunctionSymbol("writeString", MethodType([StringType()], VoidType()), className= currClassName),
            FunctionSymbol("writeBool", MethodType([BoolType()], VoidType()), className= currClassName),
        ])])
    

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        global_envi = self.init()
        print("Global Envi: ", global_envi)
        java_ast = AstConvertToJavaAstVisitor(ast, global_envi)
        print("Java AST: ", java_ast.visit(ast, None))
        gc = CodeGenVisitor(java_ast, global_envi, path)
        gc.visit(ast, None)











class AstConvertToJavaAstVisitor(BaseVisitor):
    def __init__(self, astTree,env):
        self.astTree = astTree
        self.env = env

    def visitProgram(self, ast : Program, c):
        
        return ClassDecl(ClassName("ZCode"),[self.visit(i, (self.env, None)) for i in ast.decl])
    
    def visitVarDecl(self, ast : VarDecl, param : tuple[Envi,None]):
        
        (envi, varDeclParam) = param
        name = ast.name.name
        self.visit(ast.name, (envi, ExprParam(False, False)))
        
        current_scope = envi.getLast()
        
        # Visit variable type
        if ast.modifier == "var":
            varInitType = self.visit(ast.varInit, (envi, ExprParam(True, True))) 
            
            current_scope.define(VariableSymbol(name, varInitType))
        
        elif ast.modifier == "dynamic":  
            varSymbol = VariableSymbol(name, None)  
            if ast.varInit:
                varInitType = self.visit(ast.varInit, (envi, ExprParam(True, True))) if ast.varInit else None
                varSymbol = VariableSymbol(name, varInitType)
                
            current_scope.define(varSymbol)

        else: # no modifier
            varType = self.visit(ast.varType, (envi, None))
            
            symbol = VariableSymbol(name, varType)
            
            if ast.varInit:
                varInitType = self.visit(ast.varInit, (envi, ExprParam(True, True, varType)))
            
            current_scope.define(symbol)
            return symbol
        

    def visitFuncDecl(self, ast : FuncDecl, param):
        print("VisitFuncDecl: ",ast, param)
        
        return Symbol(ast.name.name, MethodType([self.visit(x) for x in ast.param], ast.returnType), ClassName("MCClass"))
        
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

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path

    def visitProgram(self, ast : Program, c):
        
        [self.visit(i, c) for i in ast.decl]
        
        return c
    
    def visitVarDecl(self, ast : VarDecl, param):
        print("VisitVarDecl: ",ast, param)
        pass

    def visitFuncDecl(self, ast : FuncDecl, param):
        print("VisitFuncDecl: ",ast, param)
        
        return FunctionSymbol(ast.name.name, MethodType([self.visit(x) for x in ast.param], ast.returnType), ClassName("MCClass"))
        
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

    def visitClassDecl(self, ast : ClassDecl, c : list[FunctionSymbol]):
        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))
        
        # visit all methoddecl
        [self.visit(ele, SubBody(None, self.env))
         for ele in ast.memlist if type(ele) == MethodDecl]
        
        # generate default constructor
        self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(
        ), None, Block([])), c, Frame("<init>", VoidType()))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl : MethodDecl, o : list[FunctionSymbol], frame : Frame):
        # Check if the method is a constructor or the main method
        isConstructor = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType

        # Set the return type based on whether the method is a constructor
        returnType = VoidType() if isConstructor else consdecl.returnType

        # Set the method name based on whether the method is a constructor
        methodName = "<init>" if isConstructor else consdecl.name.name

        # Set the input types based on whether the method is the main method
        intype = [ArrayType(0, StringType())] if isMain else list(map(lambda x: x.typ, consdecl.param))

        # Create a method type object
        mtype = MethodType(intype, returnType)

        # Generate the method declaration code
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isConstructor, frame))

        # Enter a new scope
        frame.enterScope(True)

        # Initialize the global environment
        glenv = o

        # Generate code for parameter declarations
        if isConstructor:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(Id(self.className)), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            local = reduce(lambda env, ele: SubBody(frame, [self.visit(ele, env)]+env.sym), consdecl.param, SubBody(frame, []))
            glenv = local.sym+glenv

        # Get the method body
        body = consdecl.body

        # Generate the start label for the method
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isConstructor:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        # Generate the end label for the method
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        # Generate the return statement
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))

        # End the method
        self.emit.printout(self.emit.emitENDMETHOD(frame))

        # Exit the scope
        frame.exitScope()

    def visitMethodDecl(self, ast : MethodDecl, o : SubBody):
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        return FunctionSymbol(ast.name, MethodType([x.typ for x in ast.param], ast.returnType), ClassName(self.className))

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = next(filter(lambda x: ast.method.name == x.name, nenv), None)
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.method.name, ctype, frame))

    def visitNumberLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(ast.value, o.frame), NumberType()

    def visitBinaryOp(self, ast, o):
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        return e1c + e2c + self.emit.emitADDOP(ast.op, e1t, o.frame), e1t
