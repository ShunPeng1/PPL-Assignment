import math
from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *

from typing import List, Union, Tuple


## Make missing classes

class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value

class ClassType (Type):
    def __init__(self, ctype):
        self.classname = ctype # ClassType

class Instance:
    def __init__(self):
        pass

class ClassName(Val):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"ClassName({self.name})"

class ClassDecl (Decl):
    def __init__(self, classname : ClassName, memlist : list[Decl]):
        self.classname : ClassName = classname # Id
        self.memlist : list[Decl] = memlist # list of Decl

    def accept(self, visitor, param):
        return visitor.visitClassDecl(self, param)
    
    def __str__(self):
        memlist_str = ', '.join(str(mem) for mem in self.memlist)
        return f"ClassDecl({self.classname}, [{memlist_str}] )"

class MethodType(Type):
    def __init__(self, partype : list[Type], rettype):
        self.partype = partype # list of Type
        self.rettype = rettype # Type

    def __str__(self):
        partype_str = ', '.join(str(i) for i in self.partype)
        return f"MethodType([{partype_str}], {self.rettype})"


class AttributeDecl(Decl):
    def __init__(self, isStatic, name, varType, varInit):
        self.isStatic = isStatic
        self.name = name # Id
        self.varType = varType
        self.varInit = varInit # Assign (if isStatic) or Expr

    def accept(self, visitor, param):
        return visitor.visitAttributeDecl(self, param)

    def __str__(self):
        return f"AttributeDecl({self.name}, {self.varType}, {self.varInit})"
        

class MethodDecl(Decl):
    # instance: Instance
    # name: Id
    # param: list[AttributeDecl]
    # returnType: Type
    # body: Block

    def __init__(self, instance, name, param : list[AttributeDecl], returnType, body):
        self.instance = instance # Not used but keep for consistency
        self.name = name # Id
        self.param = param # list of AttributeDecl
        self.returnType = returnType # Type
        self.body = body # Block

    def accept(self, visitor, param):
        return visitor.visitMethodDecl(self, param)

    def __str__(self):
        return f"MethodDecl({self.name}, {self.param}, {self.returnType}, {self.body})"


class Symbol:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Symbol({self.name})"

class VariableSymbol(Symbol):
    def __init__(self, name : str, type : Type = None, idx = 0, isStatic : bool = False, astAttributeDecl : AttributeDecl = None):
        self.name = name
        self.type = type
        self.idx = idx
        self.isStatic = isStatic
        self.astAttributeDecl = astAttributeDecl

    def __str__(self):
        return f"VariableSymbol({self.name}, {self.type}. {self.idx}, {self.isStatic})"


class FunctionSymbol(Symbol):
    def __init__(self, name, methodType = MethodType([],None), className : ClassName = None, param : list[AttributeDecl] = None, body = None, astMethodDecl : MethodDecl=None):
        self.name = name
        self.methodType : MethodType = methodType  # MethodType
        if param is None:
            param = []
        self.param = param

        self.body = body
        self.className = className
        
        self.astMethodDecl = astMethodDecl

    def __str__(self):
        paramStr = ', '.join(str(i) for i in self.param)
        return f"FunctionSymbol({self.name}, {self.methodType}, [{paramStr}], {self.className}, {self.astMethodDecl})"

   
class SubBody():
    def __init__(self, frame : Frame, sym : list[Symbol], isParam = False):
        self.frame : Frame = frame
        self.sym : list[Symbol] = sym # list of Symbol
        self.isParam : bool = isParam

    def __str__(self):
        return f"SubBody([{', '.join(str(i) for i in self.sym)}])"


class Access():
    def __init__(self,  frame : Frame, sym : list[Symbol], isLeft):
        self.frame : Frame = frame
        self.sym : list[Symbol] = sym # list of Symbol
        self.isLeft = isLeft

    def __str__(self):
        return f"Access({self.frame}, [{', '.join(str(i) for i in self.sym)}], {self.isLeft})"


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
        self.scopes : List[Scope] = scope
        self.itr = len(scope)-1

    def append(self, scope : Scope):
        self.scopes.append(scope)

    def pop(self):
        self.scopes.pop()

    def next_iterator(self):
        if self.itr < len(self.scopes) - 1:
            self.itr += 1
        return self.scopes[self.itr]
        
    def previous_iterator(self):
        if self.itr > 0:
            self.itr -= 1
        return self.scopes[self.itr] 

    def getFirst(self) -> Scope:
        return self.scopes[0]

    def getLast(self) -> Scope:
        return self.scopes[-1]

    def __getitem__(self, index : int):
        return self.scopes[index]

    def __setitem__(self, index, value : Scope):
        self.scopes[index] = value
    
    def __len__(self):
        return len(self.scopes)

    def __str__(self) -> str:
        return f"Environtment({self.scopes})"


class ExprParam: 
    def __init__(self, isRHS : bool = False, isDeclared : bool = False, inferredType : Type = None) -> None:
        self.isRHS = isRHS
        self.isDeclared = isDeclared
        self.inferredType = inferredType

    def __str__(self) -> str:
        return f"IdParam({self.isRHS}, {self.inferredType})"



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
        return [
            FunctionSymbol("readNumber", MethodType([], NumberType()), currClassName),
            FunctionSymbol("readString", MethodType([], StringType()), currClassName),
            FunctionSymbol("readBool", MethodType([], BoolType()), currClassName),
            FunctionSymbol("writeNumber", MethodType([NumberType()], VoidType()), currClassName),
            FunctionSymbol("writeString", MethodType([StringType()], VoidType()), currClassName),
            FunctionSymbol("writeBool", MethodType([BoolType()], VoidType()), currClassName),
        ]
    

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        global_envi = self.init()
        print("Global Envi: ", global_envi)
        java_ast_visitor = AstConvertToJavaAstVisitor(ast, Envi([Scope(global_envi)]) )
        java_ast = java_ast_visitor.visit(ast, None)
        print("Java AST: ", java_ast)
        gc = CodeGenVisitor(java_ast, global_envi, path)
        gc.visit(java_ast, global_envi)




def getName(symbol : Symbol) -> str:
    return symbol.name

EMIT_SEPARATOR : str = "@@@" 

class AstConvertToJavaAstVisitor(BaseVisitor):
    def __init__(self, astTree,env):
        self.astTree = astTree
        self.env = env
        self.className = ClassName("ZCodeClass")
    
        

    def lookup(self, name : str, symbols : list[Symbol], getName) -> Symbol:
        for symbol in symbols:
            if name == getName(symbol):
                return symbol
        return None

    def getSymbol(self, lhs : Union[Id , ArrayCell] , isOnlyLastScope : bool, envi : Envi) -> Symbol:
        #print("getSymbol: ", lhs, envi)

        name = ""
        if type(lhs) == Id:
            name = lhs.name
        elif type(lhs) == ArrayCell:
            name = lhs.arr.name


        if isOnlyLastScope:
            return self.lookup(name, envi.getLast().symbols, getName)

        for i in range(len(envi) - 1, -1, -1): # from current scope to global scope
            #print("checkDeclared Scope: ", i, envi[i])
            symbols = envi[i].symbols # list of Symbol in scope
           
            for symbol in symbols:
                if name == getName(symbol):
                    return symbol

        return None # No symbol found

    def visitProgram(self, ast : Program, c):
        result = []
        for i in range(len(ast.decl)):
            decl = self.visit(ast.decl[i], (self.env, None))
            if decl:
                result.append(decl)
        return ClassDecl(self.className, result)

    def visitVarDecl(self, ast : VarDecl, param : tuple[Envi, None]):
        
        (envi, varDeclParam) = param
        name = ast.name.name
        self.visit(ast.name, (envi, ExprParam(False, False)))
        
        isStatic = len(envi.scopes) == 1
        current_scope = envi.getLast()
        
        # Visit variable type
        if ast.modifier == "var":
            varInitType = self.visit(ast.varInit, (envi, ExprParam(True, True))) 
            
            attributeDecl = None
            if isStatic:
                varInit = Assign(ast.name, ast.varInit) if ast.varInit else None
                attributeDecl = AttributeDecl(isStatic, ast.name, varInitType, varInit)
            else:
                attributeDecl = AttributeDecl(isStatic, ast.name, varInitType, ast.varInit)

            varSymbol = VariableSymbol(name, varInitType, 0, isStatic, attributeDecl)

            current_scope.define(varSymbol)
            return attributeDecl
            
        elif ast.modifier == "dynamic":  
            varSymbol = VariableSymbol(name, None)  
            if ast.varInit:
                varInitType = self.visit(ast.varInit, (envi, ExprParam(True, True))) if ast.varInit else None
                varSymbol = VariableSymbol(name, varInitType, 0, isStatic)
                

            attributeDecl = None
            if isStatic:
                varInit = Assign(ast.name, ast.varInit) if ast.varInit else None
                attributeDecl = AttributeDecl(isStatic, ast.name, varSymbol.type, varInit)
            else:
                attributeDecl = AttributeDecl(isStatic, ast.name, varSymbol.type, ast.varInit)
                
            varSymbol.astAttributeDecl = attributeDecl
            current_scope.define(varSymbol)
            return attributeDecl
        
        else: # no modifier
            varType = self.visit(ast.varType, (envi, None))
            
            varSymbol = VariableSymbol(name, varType, 0, isStatic)
            
            attributeDecl = None
            if isStatic:
                varInit = Assign(ast.name, ast.varInit) if ast.varInit else None
                attributeDecl = AttributeDecl(isStatic, ast.name, varType, varInit)
            else:
                attributeDecl = AttributeDecl(isStatic, ast.name, varType, ast.varInit)
              
            varSymbol.astAttributeDecl = attributeDecl
            current_scope.define(varSymbol)
            return attributeDecl

        

    def visitFuncDecl(self, ast : FuncDecl, param : tuple[Envi,None]):
        print("VisitFuncDecl: ",ast, param)
        
        (envi, _) = param

        # Get function symbol
        functionSymbol = self.getSymbol(ast.name, True, envi)
        name = ast.name.name
        isDeclared = functionSymbol is not None

        self.visit(ast.name, (envi, ExprParam(False, isDeclared))) # visit function name, check functionSymbol have declared or not
        
        def visitFuncParamAndBody(functionSymbol : FunctionSymbol):
            
            parameters : list[AttributeDecl] = []

            envi.append(Scope()) # new scope for function parameters

            if ast.param:
                for i in range(0,len(ast.param)):
                    paramDecl = ast.param[i]
                    paramAttributeDecl = self.visit(paramDecl, (envi, None))
                    parameters.append(paramAttributeDecl)
                
                #print(len(envi),envi.getLast())
            
            # Add function Symbol before visit body for recursive
            functionSymbol.param = parameters

            # Add method type only knowing the parameters
            methodType = MethodType([x.varType for x in parameters],None)
            functionSymbol.methodType = methodType
            
            stmtParam = StmtParam(functionSymbol, 0)
            body = self.visit(ast.body, (envi, stmtParam)) if ast.body else None # declare only or implement function
            
            if body: # function has body so it must have a type
                if functionSymbol.methodType.rettype is None:
                    methodType.rettype = VoidType()
                else:
                    methodType.rettype = functionSymbol.methodType.rettype 
                print("Function Body JAVA: ", functionSymbol )

            # Add method type to function symbol after visit body
            functionSymbol.methodType = methodType
            functionSymbol.body = body

            stmtParam.currentFunctionSymbol = None # pop the scope of function 
            envi.pop() # pop the scope of function parameters

        
        if functionSymbol is None: # first declaration of function 
            methodDecl = MethodDecl(Instance(), ast.name, None, None , None)
            
            functionSymbol = FunctionSymbol(name, MethodType([],None), self.className, None, None, methodDecl) # TODO : return type of function

            # Add function to current scope, add it soon because of recursive call
            envi.getLast().define(functionSymbol) 

            # Visit function parameters and body
            visitFuncParamAndBody(functionSymbol)
            
            methodDecl.param = functionSymbol.param
            methodDecl.returnType = functionSymbol.methodType.rettype
            methodDecl.body = functionSymbol.body

            print("Function Symbol JAVA: ", functionSymbol, methodDecl)
        
            return methodDecl

    
        elif type(functionSymbol) == FunctionSymbol: # implement the body function
            
            # Check for redeclared parameters
            visitFuncParamAndBody(functionSymbol)

            methodDecl = functionSymbol.astMethodDecl
            methodDecl.param = functionSymbol.param
            methodDecl.body = functionSymbol.body
            
            functionSymbol.astMethodDecl = methodDecl # update astMethodDecl
            
            return None # no need to return method declaration
    
        else:
            pass # Solved in StaticChecker
        

    def visitNumberType(self, ast : NumberType, param):
        return NumberType()
    
    def visitBoolType(self, ast : BoolType, param):
        return BoolType()

    def visitStringType(self, ast : StringType, param):
        return StringType()
    
    def visitArrayType(self, ast : ArrayType, param):
        return ArrayType(ast.size, ast.eleType)
    
    def visitBinaryOp(self, ast : BinaryOp, param : Tuple[Envi, ExprParam]):
        
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
            operandParam = ExprParam(True, True, inferredOperandType)

        left = self.visit(ast.left, (envi, operandParam))
        right = self.visit(ast.right, (envi, operandParam))
        
        
        return inferredReturnType # return type of binary operation

    
    def visitUnaryOp(self, ast : UnaryOp, param : Tuple[Envi, ExprParam]):
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
            operandParam = ExprParam( True, True, inferredOperandType)
        
        exprType = self.visit(ast.operand, (envi, operandParam))
        
        return inferredReturnType # return type of unary operation

    def visitCallExpr(self, ast : CallExpr, param : Tuple[Envi, ExprParam]):
        #print("Call Expr: ",ast, param[1])

        (envi, exprParam) = param

        self.visit(ast.name, (envi, ExprParam( True, True)))
        functionSymbol : FunctionSymbol = self.getSymbol(ast.name, False, envi)

        print("Call Expr:", len(ast.args), functionSymbol)
        for i in range(len(ast.args)):
            symbolParamType = functionSymbol.param[i].varType
            callParamType = self.visit(ast.args[i], (envi, ExprParam(True, True, symbolParamType)))
            

        if functionSymbol.methodType.rettype is None: # function with not yet assigned type
            if exprParam.inferredType:
                functionSymbol.methodType.rettype = exprParam.inferredType
        
        if functionSymbol.astMethodDecl: # Update return type of method declaration
            if exprParam.inferredType:
                functionSymbol.astMethodDecl.returnType = exprParam.inferredType
            
        return functionSymbol.methodType.rettype
    
    def visitId(self, ast : Id, param : Tuple[Envi, ExprParam]):
        #print("Visit Id: " , ast, param)
        (envi, exprParam) = param
        if type(exprParam) == ExprParam:
            if exprParam.isRHS:
                symbol = self.getSymbol(ast, False, envi)
                
                if type(symbol) is VariableSymbol :
                    if symbol.type :                  
                        return symbol.type
                    elif exprParam.inferredType : # No type in symbol yet so inferred type
                        symbol.type = exprParam.inferredType
                        symbol.astAttributeDecl.varType = exprParam.inferredType # update type of attribute declaration

                        return symbol.type
                elif type(symbol) is FunctionSymbol:
                    if symbol.methodType.rettype:
                        return symbol.methodType.rettype
                    elif exprParam.inferredType:
                        symbol.methodType.rettype = exprParam.inferredType
                        symbol.astMethodDecl.returnType = exprParam.inferredType # update return type of method declaration
                        return symbol.methodType.rettype
                    
                
            else : # LHS
                if exprParam.isDeclared:
                    symbol = self.getSymbol(ast, False, envi)
                    if type(symbol) is VariableSymbol :
                        return symbol.type
                    elif type(symbol) is FunctionSymbol:
                        return symbol.methodType.rettype
        else:
            raise Exception("Id not found in enviroment")


    def visitArrayCell(self, ast : ArrayCell, param : Tuple[Envi, ExprParam]):
        #print("Array Cell: ", ast, param)

        (envi, exprParam) = param

        arrType : ArrayType = self.visit(ast.arr, (envi, ExprParam(exprParam.isRHS, exprParam.isDeclared, None))) # visit array type
        
        #print("Array Cell Type: ", arrType, exprParam.isRHS, exprParam.isDeclared, exprParam.inferredType, len(ast.idx))
        
        innerType = ArrayType(arrType.size, arrType.eleType) # copy of array type       
        for i in range(len(ast.idx)):
            idx = ast.idx[i]
            idxType = self.visit(idx, (envi, ExprParam(True, True, NumberType())))

            if len(innerType.size) > 1: # inner type of the array is the array (a[3,2] inner is a[2])
                innerType.size = innerType.size[1:]
            else : # inner type of the array is the element type 
                innerType = innerType.eleType

        #print("Array Cell Inner Type: ", innerType)
        return innerType # return type of array cell        
        

    def visitBlock(self, ast : Block, param : tuple[Envi,StmtParam]):
        
        (envi, stmtParam) = param

        envi.append(Scope())

        stmts = []
        i = 0
        for stmt in ast.stmt:
            if type(stmt) == VarDecl:
                stmts = stmts + [self.visit(stmt, (envi, stmtParam))]
                i += 1
            else:
                stmts = stmts + [self.visit(stmt, (envi, stmtParam))]

        envi.pop()
        stmtStr = ', '.join(str(stmt) for stmt in stmts)
        print("visitBlockJava: ", stmtStr)
        return Block(stmts) 

    def visitIf(self, ast : If, param : Tuple[Envi, StmtParam]):
        #print("Visit If: ", ast)

        (envi, stmtParam) = param

        ifConditionType = self.visit(ast.expr, (envi, ExprParam(True, True, BoolType())))
        
        
        thenStmt = self.visit(ast.thenStmt, (envi, stmtParam)) 

        elifListTuple = []
        for (elifExpr, elifStmt) in ast.elifStmt:
            elifConditionType = self.visit(elifExpr, (envi, ExprParam( True, True, BoolType())))

            elifListTuple.append((elifExpr, self.visit(elifStmt, (envi, stmtParam))))
        
        elseStmt = None
        if ast.elseStmt:
            elseStmt = self.visit(ast.elseStmt, (envi, stmtParam))

        return If(ast.expr, thenStmt, elifListTuple, elseStmt)

    
    def visitFor(self, ast : For, param):
        #print("Visit For: ", ast)

        (envi, stmtParam) = param
    
        lhsType = self.visit(ast.name, (envi, ExprParam(False, True, NumberType())))
        symbol : VariableSymbol = self.getSymbol(ast.name, False, envi)
        updType = self.visit(ast.updExpr, (envi, ExprParam(True, True, NumberType())))

        
        if lhsType is None: # LHS first use so infer type
            lhsType = NumberType()
            symbol.type = lhsType
            symbol.astAttributeDecl.varType = lhsType # update type of attribute declaration
        
            
        # Visit condition of for loop
        condType = self.visit(ast.condExpr, (envi, ExprParam(True, True, BoolType())))
       
        
        # Visit body of for loop
        
        body = self.visit(ast.body, (envi, stmtParam))
        
        return For(ast.name, ast.condExpr, ast.updExpr, body)

    
    def visitContinue(self, ast : Continue, param : Tuple[Envi, StmtParam]):
        #print("Visit Continue: ", ast)
        (envi, stmtParam) = param

        return ast

    
    def visitBreak(self, ast : Break, param):
        #print("Visit Break: ", ast)
        (envi, stmtParam) = param

        return ast
    
    def visitReturn(self, ast : Return, param : Tuple[Envi, StmtParam]):
        
        (envi, stmtParam) = param

        if stmtParam.currentFunctionSymbol.astMethodDecl.returnType is None: # function type is not declared
            if ast.expr:
                returnType = self.visit(ast.expr, (envi, ExprParam(True, True, stmtParam.currentFunctionSymbol.methodType.rettype)))
            
                stmtParam.currentFunctionSymbol.methodType.rettype = returnType
                stmtParam.currentFunctionSymbol.astMethodDecl.returnType = returnType # update return type of method declaration
                
                print("Return Type JAVA : ", returnType, stmtParam.currentFunctionSymbol)
            else:
                stmtParam.currentFunctionSymbol.methodType.rettype = VoidType()
                stmtParam.currentFunctionSymbol.astMethodDecl.returnType = VoidType() # update return type of method declaration
        
        else: # function type is declared
            if ast.expr:
                returnType = self.visit(ast.expr, (envi, ExprParam(True, True, stmtParam.currentFunctionSymbol.methodType.rettype)))
                
                
        
        return ast


    
    def visitAssign(self, ast : Assign, param : Tuple[Envi, StmtParam]):
        
        (envi, stmtParam) = param

        lhsType = self.visit(ast.lhs, (envi, ExprParam( False, True)))
        symbol : VariableSymbol = self.getSymbol(ast.lhs, False, envi)

        if lhsType: # LHS is declared and has type
            rhsType = self.visit(ast.rhs, (envi, ExprParam( True, True, lhsType)))

        else: # LHS first use
            rhsType = self.visit(ast.rhs, (envi, ExprParam( True, True)))
            
            symbol.type = rhsType
            symbol.astAttributeDecl.varType = rhsType # update type of attribute declaration

        return ast

    
    def visitCallStmt(self, ast : CallStmt, param : Tuple[Envi, StmtParam]):
        #print("Call Stmt: ",ast, )

        (envi, stmtParam) = param

        self.visit(ast.name, (envi, ExprParam( True, True)))
        functionSymbol : FunctionSymbol = self.getSymbol(ast.name, False, envi)
        
        print("Call Stmt: ",ast, functionSymbol, len(ast.args))

        for i in range(len(ast.args)):
            symbolParamType = functionSymbol.methodType.partype[i]
            callParamType = self.visit(ast.args[i], (envi, ExprParam( True, True, symbolParamType)))

        if functionSymbol.methodType.rettype is None: # function declared-only
            functionSymbol.methodType.rettype = VoidType()

        if functionSymbol.astMethodDecl:
            functionSymbol.astMethodDecl.returnType = VoidType() # update return type of method declaration
          
        return ast


    
    def visitNumberLiteral(self, ast : NumberLiteral, param):
        #print("Number Literal: ", ast)
        return NumberType()

    
    def visitBooleanLiteral(self, ast : BooleanLiteral, param):
        return BoolType()

    
    def visitStringLiteral(self, ast : StringLiteral, param):
        return StringType()

    
    def visitArrayLiteral(self, ast : ArrayLiteral, param : Tuple[Envi, ExprParam]):
        #print("Array Literal: ", ast)

        (envi, exprParam) = param

        if len(ast.value) == 0:
            return ArrayType([0], None)
        
        inferredType : ArrayType = exprParam.inferredType
        if inferredType: 
             
            #print("Array Literal Inferred Type: ", inferredType.size, len(ast.value), inferredType.eleType, len(inferredType.size) > 0, inferredType.size[0] != len(ast.value))
            
            # Get inner type of array
            innerType = ArrayType(inferredType.size, inferredType.eleType) # copy of array type
                
            if len(inferredType.size) <= 1:
                innerType = inferredType.eleType
            else :
                innerType = ArrayType( inferredType.size[1:] , inferredType.eleType)

            # Check for type of each value in array
            for value in ast.value:
                valueType = self.visit(value, (envi, ExprParam( True, True, innerType)))
                

            return ArrayType(inferredType.size , inferredType.eleType)


        else : # No inferred type
            
            firstType = None            
            for value in ast.value:
                firstType = self.visit(value, (envi, ExprParam(True, True, None)))

            
            # Check for type of each value in array
            for value in ast.value:
                valueType = self.visit(value, (envi, ExprParam(True, True, firstType)))
                
                
            if type(firstType) == ArrayType: # the first element is an array type
                return ArrayType([len(ast.value)] + firstType.size, firstType.eleType)
            
            else: # inferred type is not an array, maybe NumberType, StringType, BoolType, VoidType
                return ArrayType([len(ast.value)], firstType)



class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env : Envi, path):
        self.astTree = astTree
        self.env : Envi = env
        self.path = path
    
    def visitClassDecl(self, ast : ClassDecl, globalEnvi : List[FunctionSymbol]):
        print("VisitClassDecl: ",ast, globalEnvi)

        self.className = ast.classname.name
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(
            self.className, "java.lang.Object"))

        
        # generate static variable
        for decl in ast.memlist:   
            if type(decl) == AttributeDecl:
                
                symbol =  self.visit(decl, SubBody(None, globalEnvi))  
                globalEnvi.append(symbol)

        # generate static function
        for decl in ast.memlist:   
            if type(decl) == MethodDecl:            
                symbol =  self.visit(decl, SubBody(None, globalEnvi))
                
                globalEnvi.append(symbol)  
            
        # generate static constructor
                
        staticAttributeAssign = []
        
        for decl in ast.memlist:
            if type(decl) == AttributeDecl and decl.isStatic:
                assignStmt = decl.varInit if type(decl.varInit) == Assign else Assign(decl.name, self.getDefaultValue(decl.varType))
                staticAttributeAssign.append(assignStmt)

        self.genMETHOD(MethodDecl(Instance(), Id("<clinit>"), list(), VoidType(), Block(staticAttributeAssign)), globalEnvi, Frame("<clinit>", VoidType()))

        
        # generate default constructor
        self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(), None, Block([])), globalEnvi, Frame("<init>", VoidType()))
        self.emit.emitEPILOG()

        return globalEnvi

    def genMETHOD(self, consdecl : MethodDecl, o : list[Symbol], frame : Frame):
        print("genMETHOD: ",consdecl, o, frame)

        # Check if the method is a constructor or the main method
        isConstructor = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType

        # Set the return type based on whether the method is a constructor
        returnType = VoidType() if isConstructor else consdecl.returnType

        # Set the method name based on whether the method is a constructor
        methodName = "<init>" if isConstructor else consdecl.name.name

        # Set the input types based on whether the method is the main method
        intype = [ArrayType([0], StringType())] if isMain else list(map(lambda x: x.varType, consdecl.param))

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
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([0], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            local = reduce(lambda env, ele: SubBody(frame, env.sym + [self.visit(ele, env)], True), consdecl.param, SubBody(frame, [], True))
            glenv = glenv + local.sym

        # Get the method body
        body = consdecl.body

        # Generate the start label for the method
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isConstructor:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.visit(body, SubBody(frame, glenv))

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
        print("VisitMethodDecl: ", ast)

        frame = Frame(ast.name, ast.returnType)
        functionSymbol = FunctionSymbol(ast.name.name, MethodType([x.varType for x in ast.param], ast.returnType), ClassName(self.className))
        #o.sym.append(functionSymbol)
        
        self.genMETHOD(ast, o.sym, frame)
        return functionSymbol

    def getDefaultValue(self, varType : Type):
        print("Get Default Value: ", varType)
        if type(varType) == NumberType:
            return NumberLiteral(0.0)
        elif type(varType) == BoolType:
            return BooleanLiteral(False)
        elif type(varType) == StringType:
            return StringLiteral("")
        elif type(varType) == ArrayType:
            print("Get Default Value Array: ", varType.size, varType.eleType)
            if len(varType.size) == 1:
                return ArrayLiteral([self.getDefaultValue(varType.eleType) for i in range(int(varType.size[0]))])
            else:
                return ArrayLiteral([self.getDefaultValue(ArrayType(varType.size[1:], varType.eleType)) for i in range(int(varType.size[0]))])
            
 
    def visitAttributeDecl(self, ast : AttributeDecl, o : SubBody):
        print("visitAttributeDecl: ", ast)

        isStatic = ast.isStatic
        isParam = o.isParam
        variableSymbol = None
        if isStatic: # static variable
            self.emit.printout(self.emit.emitATTRIBUTE(ast.name.name, ast.varType, False, None))
            variableSymbol = VariableSymbol(ast.name.name, ast.varType, 0, isStatic, ast)
            #o.sym.append(variableSymbol)
            
            # Ignore the initial value of the static variable because it will be initialized in the static constructor

        else: # local variable
            idx = o.frame.getNewIndex()
            variableSymbol = VariableSymbol(ast.name.name, ast.varType, idx, isStatic, ast)
            self.emit.printout(self.emit.emitVAR(idx, ast.name.name, ast.varType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
            
            if isParam:
                return variableSymbol # Not generate initial for parameter
            
            if ast.varInit is None : # No initial value
                #o.sym.append(variableSymbol)
                ast.varInit = self.getDefaultValue(ast.varType)

            initEmit, initType = self.visit(ast.varInit, Access(o.frame, o.sym, False))
            self.emit.printout(initEmit)
            #self.emit.printout(self.emit.emitPUSHCONST(idx, ast.varType, o.frame))
            
            self.emit.printout(self.emit.emitWRITEVAR(ast.name.name, ast.varType, idx, o.frame))

            #o.sym.append(variableSymbol)

        
        return variableSymbol


    def visitBlock(self, ast : Block, o : SubBody):
        print("VisitBlock: ",ast)

        o.frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame))

        blockSymbols = []
        for stmt in ast.stmt:
            stmtReturn = self.visit(stmt, o)
            if type(stmtReturn) == FunctionSymbol or type(stmtReturn) == VariableSymbol:
                o.sym.append(stmtReturn)
                blockSymbols.append(stmtReturn)

        for symbol in blockSymbols:
            o.sym.pop() # remove the symbol from the symbol table
        
        
        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))
        o.frame.exitScope()
        return


    def visitIf(self, ast : If, o : SubBody):
        print("VisitIf: ")

        ifFalseLabel = o.frame.getNewLabel()
        endLabel = o.frame.getNewLabel()

        exprEmit, exprType = self.visit(ast.expr, Access(o.frame, o.sym, False))
        self.emit.printout(exprEmit)

        # If the condition is false, jump to the elif statement
        self.emit.printout(self.emit.emitIFFALSE(ifFalseLabel, o.frame))
        self.visit(ast.thenStmt, o)
        self.emit.printout(self.emit.emitGOTO(endLabel, o.frame))
        self.emit.printout(self.emit.emitLABEL(ifFalseLabel, o.frame))

        for (elifExpr, elifStmt) in ast.elifStmt:
            elifFalseLabel = o.frame.getNewLabel()
            elifExprEmit, elifExprType = self.visit(elifExpr, Access(o.frame, o.sym, False))
            self.emit.printout(elifExprEmit)

            # If the condition is false, jump to the next condition
            self.emit.printout(self.emit.emitIFFALSE(elifFalseLabel, o.frame))
            self.visit(elifStmt, o)
            self.emit.printout(self.emit.emitGOTO(endLabel, o.frame))
            self.emit.printout(self.emit.emitLABEL(elifFalseLabel, o.frame))

        if ast.elseStmt: # else statement
            self.visit(ast.elseStmt, o)

        self.emit.printout(self.emit.emitLABEL(endLabel, o.frame))
        
        ## Empty Label at the end of if statement fix
        self.emit.printout(self.emit.emitPUSHFCONST("0.0",o.frame))
        self.emit.printout(self.emit.emitPOP(o.frame))

        return ast


    def visitFor(self, ast : For, o : SubBody):
        print("VisitFor: ")

        o.frame.enterLoop()

        continueLabel = o.frame.getContinueLabel()
        breakLabel = o.frame.getBreakLabel()
        conditionLabel = o.frame.getNewLabel()


        # Declare the loop variable
        incrementIndex = o.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(incrementIndex, "until", NumberType(), o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
        untilSymbol = VariableSymbol("until", NumberType(), incrementIndex, False, None)
        o.sym.append(untilSymbol)

        incrementAssign = Assign(Id("until"), ast.updExpr)
        self.visit(incrementAssign, SubBody(o.frame, o.sym))
        

        # Initialize the loop variable
        iterationIndex = o.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(iterationIndex, "for", NumberType(), o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
        forSymbol = VariableSymbol("for", NumberType(), iterationIndex, False, None)
        o.sym.append(forSymbol)

        iterationIndexAssign = Assign(Id("for"), ast.name)
        self.visit(iterationIndexAssign, SubBody(o.frame, o.sym))

        initEmit, initType = self.visit(ast.name, Access(o.frame, o.sym, False))

        # Visit the condition of the loop
        self.emit.printout(self.emit.emitLABEL(conditionLabel, o.frame))
        condEmit, condType = self.visit(ast.condExpr, Access(o.frame, o.sym, False))
        self.emit.printout(condEmit)

        self.emit.printout(self.emit.emitIFTRUE(breakLabel, o.frame))

        # Visit the body of the loop
        self.visit(ast.body, o)

        self.emit.printout(self.emit.emitLABEL(continueLabel, o.frame))

        # Update the loop variable
        updateExpr = Assign(ast.name, BinaryOp("+", ast.name, Id("until")))
        self.visit(updateExpr, SubBody(o.frame, o.sym))

        self.emit.printout(self.emit.emitGOTO(conditionLabel, o.frame))

        
        self.emit.printout(self.emit.emitLABEL(breakLabel, o.frame))

        revertAssign = Assign(ast.name, Id("for"))
        self.visit(revertAssign, SubBody(o.frame, o.sym))
        o.sym.remove(forSymbol)
        o.sym.remove(untilSymbol)


        # Exit the loop
        o.frame.exitLoop()



        return ast


    def visitContinue(self, ast : Continue, o : SubBody):
        print("VisitContinue: ")

        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))
        return ast
    

    def visitBreak(self, ast : Break, o : SubBody):
        print("VisitBreak: ")

        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
        return ast

    def visitReturn(self, ast : Return, o : SubBody):
        print("VisitReturn: ")

        if ast.expr:
            returnEmit, returnType = self.visit(ast.expr, Access(o.frame, o.sym, False))
            self.emit.printout(returnEmit)
            self.emit.printout(self.emit.emitRETURN(returnType, o.frame))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), o.frame))
        return ast
    

    def visitAssign(self, ast : Assign, o : SubBody):

        
        if type(ast.lhs) == ArrayCell:
            o.frame.push()
            o.frame.push()

            assignEmit, assignType = self.visit(ast.rhs, Access(o.frame, o.sym, False))
            
            o.frame.pop()
            o.frame.pop()

            leftEmit , leftType = self.visit(ast.lhs, Access(o.frame, o.sym, True))
            print("visitAssign: ", ast, assignEmit, assignType, leftEmit, leftType)
        
            innerEmit, arrEmit = leftEmit.split(EMIT_SEPARATOR)
            
            self.emit.printout(innerEmit)
            self.emit.printout(assignEmit)
            self.emit.printout(arrEmit)
        else:
            
            assignEmit, assignType = self.visit(ast.rhs, Access(o.frame, o.sym, False))
        
            leftEmit , leftType = self.visit(ast.lhs, Access(o.frame, o.sym, True))

            self.emit.printout(assignEmit)
            self.emit.printout(leftEmit)

        return assignEmit, assignType


    def visitUnaryOp(self, ast : UnaryOp, o : Access):
        exprEmit, exprType = self.visit(ast.operand, o)
        if ast.op == "-":
            return exprEmit + self.emit.emitNEGOP(exprType, o.frame), exprType
        elif ast.op == "not":
            return exprEmit + self.emit.emitNOT(exprType, o.frame), exprType
        else:
            pass


    def visitBinaryOp(self, ast : BinaryOp, o : Access):
        leftEmit, leftType = self.visit(ast.left, o)
        rightEmit, rightType = self.visit(ast.right, o)
        
        if ast.op == "+":
            return leftEmit + rightEmit + self.emit.emitADDOP(ast.op, leftType, o.frame), leftType
        elif ast.op == "-":
            return leftEmit + rightEmit + self.emit.emitADDOP(ast.op, leftType, o.frame), leftType
        elif ast.op == "*":
            return leftEmit + rightEmit + self.emit.emitMULOP(ast.op, leftType, o.frame), leftType
        elif ast.op == "/":
            return leftEmit + rightEmit + self.emit.emitMULOP(ast.op, leftType, o.frame), leftType
        elif ast.op == "%":
            return leftEmit + rightEmit + self.emit.emitMOD(o.frame), leftType
        
        elif ast.op == ">":
            return leftEmit + rightEmit + self.emit.emitREOP(ast.op, leftType, o.frame), BoolType()
        elif ast.op == ">=":
            return leftEmit + rightEmit + self.emit.emitREOP(ast.op, leftType, o.frame), BoolType()
        elif ast.op == "<":
            return leftEmit + rightEmit + self.emit.emitREOP(ast.op, leftType, o.frame), BoolType()
        elif ast.op == "<=":
            return leftEmit + rightEmit + self.emit.emitREOP(ast.op, leftType, o.frame), BoolType()
        elif ast.op == "=":
            return leftEmit + rightEmit + self.emit.emitREOP(ast.op, leftType, o.frame), BoolType()
        elif ast.op == "!=":
            return leftEmit + rightEmit + self.emit.emitREOP(ast.op, leftType, o.frame), BoolType()
        
        elif ast.op == "and":
            return leftEmit + rightEmit + self.emit.emitANDOP(o.frame), BoolType()
        elif ast.op == "or":
            return leftEmit + rightEmit + self.emit.emitOROP(o.frame), BoolType()
        
        elif ast.op == "...":
            return leftEmit + rightEmit + self.emit.emitConcatStrings(o.frame), StringType()
        elif ast.op == "==":
            return leftEmit + rightEmit + self.emit.emitCompareStrings(o.frame), BoolType()
        
        else:
            pass

    def visitCallStmt(self, ast : CallStmt, o : SubBody):
        print("VisitCallStmt: ", ast)
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        #functionSymbol : FunctionSymbol = next(filter(lambda x: ast.name.name == x.name, nenv), None)
        filtered_symbols = list(filter(lambda x: ast.name.name == x.name, nenv))
        functionSymbol : FunctionSymbol = filtered_symbols[-1] if filtered_symbols else None
        
        className = functionSymbol.className.name
        methodType = functionSymbol.methodType
        in_ = ("", list()) # Tuple of emit string and list of types
        
        # Visit arguments
        for x in ast.args:
            str1, typ1 = self.visit(x, Access(frame, nenv, False))
            in_ = (in_[0] + str1, in_[1] + [typ1]) # Concatenate emit string and append type
        

        self.emit.printout(in_[0])
        print("CallStmt: ",self.emit.buff)
        self.emit.printout(self.emit.emitINVOKESTATIC(
            className + "/" + ast.name.name, methodType, frame))

    
    def visitCallExpr(self, ast : CallExpr, o : Access):
        print("VisitCallExpr: ",ast)
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        #functionSymbol : FunctionSymbol = next(filter(lambda x: ast.name.name == x.name, nenv), None)
        filtered_symbols = list(filter(lambda x: ast.name.name == x.name, nenv))
        functionSymbol : FunctionSymbol = filtered_symbols[-1] if filtered_symbols else None
        
        className = functionSymbol.className.name
        methodType = functionSymbol.methodType
        in_ = ("", list()) # Tuple of emit string and list of types
        
        # Visit arguments
        for x in ast.args:
            str1, typ1 = self.visit(x, Access(frame, nenv, False))
            in_ = (in_[0] + str1, in_[1] + [typ1] ) # Concatenate emit string and append type
        
        print("CallExpr: ",in_[0], self.emit.buff)
            
        emitStr = in_[0] + self.emit.emitINVOKESTATIC(className + "/" + ast.name.name, methodType, frame)
        
        return emitStr, methodType.rettype

    
    def visitId(self, ast : Id, param : Access):
        print("VisitId: ",ast,param)
        
        ctxt = param
        frame = ctxt.frame
        nenv = ctxt.sym
        #symbol : VariableSymbol = next(filter(lambda x: ast.name == x.name, nenv), None) 
        
        filtered_symbols = list(filter(lambda x: ast.name == x.name, nenv))
        symbol : VariableSymbol = filtered_symbols[-1] if filtered_symbols else None
        
        isStatic = symbol.isStatic
        idx = symbol.idx
        typ = symbol.type


        if isStatic:
            if param.isLeft:
                return self.emit.emitPUTSTATIC(self.className+"/"+ast.name, typ, frame), typ
            else:
                return self.emit.emitGETSTATIC(self.className+"/"+ast.name, typ, frame), typ
        else:
            if param.isLeft :
                return self.emit.emitWRITEVAR(ast.name, typ, idx, frame), typ
            else :
                return self.emit.emitREADVAR(ast.name, typ, idx, frame), typ

    
    def visitArrayCell(self, ast : ArrayCell, o : Access):
        print("VisitArrayCell: ",ast)

        frame = o.frame
        nenv = o.sym
        arrType = None
        innerType = None

        if o.isLeft: 
                        
            innerEmit , innerType = self.visit(ast.arr, Access(frame, nenv, False)) 
            

            # Visit and Load the index of the array
            for i in range(0,len(ast.idx)):
                idxEmit, idxType = self.visit(ast.idx[i], Access(frame, nenv, False)) 
                
                innerEmit += idxEmit + self.emit.emitF2I(frame)
                
                # Get the inner type of the array
                innerType = ArrayType(innerType.size[1:], innerType.eleType) if ( 1 < len(innerType.size)) else innerType.eleType
                    
                if i + 1 < len(ast.idx):
                    
                    # idxType is always NumberType (Float), innerType is the type of the inner array
                    innerEmit += self.emit.emitALOAD(innerType, frame)
                    
            
            arrEmit = self.emit.emitASTORE(innerType, frame) 
            
            return innerEmit + EMIT_SEPARATOR + arrEmit, innerType

        else : # isRight
            arrEmit, arrType = self.visit(ast.arr, Access(frame, nenv, False))

            if type(arrType) != ArrayType:
                return arrEmit, arrType # TODO : Error
            
            innerType = arrType

            # Visit and Load the index of the array
            for i in range(0,len(ast.idx)):
                idxEmit, idxType = self.visit(ast.idx[i], Access(frame, nenv, False)) 
                
                # Get the inner type of the array
                innerType = ArrayType(arrType.size[i+1:], arrType.eleType) if (i + 1 < len(arrType.size)) else arrType.eleType
                
                # idxType is always NumberType (Float), innerType is the type of the inner array
                arrEmit += idxEmit + self.emit.emitF2I(frame)
                arrEmit += self.emit.emitALOAD(innerType, frame)
                
            return arrEmit, innerType

    
            
    

            
    def visitNumberLiteral(self, ast : NumberLiteral, o : Access):
        value = ast.value
        if isinstance(value, float):
            # Calculate the number of decimal places required
            decimal_places = abs(int(math.floor(math.log10(abs(value)))))
            # Convert the float to a string in decimal notation with the calculated number of decimal places
            print("VisitNumberLiteral: ",value, "{:.{}f}".format(value, decimal_places))
            value = "{:.{}f}".format(value, decimal_places)
        
        return self.emit.emitPUSHFCONST(value, o.frame), NumberType()

    def visitBooleanLiteral(self, ast : BooleanLiteral, o : Access):
        return self.emit.emitPUSHICONST(str(ast.value).lower(), o.frame), BoolType()

    def visitStringLiteral(self, ast : StringLiteral, o : Access):
        print("VisitStringLiteral: ")
        escaped_value = ast.value.replace('"', '\\"')
        return self.emit.emitPUSHCONST(escaped_value, StringType(), o.frame), StringType()

    def visitArrayLiteral(self, ast : ArrayLiteral, param : Access):
        print("VisitArrayLiteral: ",ast)

        ctxt = param
        frame = ctxt.frame
        nenv = ctxt.sym
        eleType = None
    
        valueTypes = []
        size = [len(ast.value)]
        emitStr = ""
        
        frame.push() # Mock the array reference

        for i in range(0,len(ast.value)):
            valueExpr = ast.value[i]

            # Duplicate the array reference
            emitStr += self.emit.emitDUP(frame)

            # Insert the index of the element
            emitStr += self.emit.emitPUSHICONST(i, frame)

            # Visit the value of the element            
            valueEmit, valueType = self.visit(valueExpr, Access(frame, nenv, False))
            emitStr += valueEmit

            emitStr += self.emit.emitASTORE(valueType, frame)

            valueTypes.append(valueType)

        frame.pop() # Pop the array reference
        
        eleType = valueTypes[0]

        if type(eleType) == ArrayType:
            size = [len(ast.value)] + eleType.size
            eleType = eleType.eleType

        arrayType = ArrayType(size, eleType)

        emitStr = self.emit.emitPUSHCONST(str(len(ast.value)), arrayType, frame) + emitStr # The in the array is empty

        return emitStr, arrayType
    

    