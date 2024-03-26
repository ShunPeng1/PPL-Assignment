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
    def __init__(self, partype, rettype):
        self.partype = partype # list of Type
        self.rettype = rettype # Type

    def __str__(self):
        partype_str = ', '.join(str(i) for i in self.partype)
        return f"MethodType([{partype_str}], {self.rettype})"


class MethodDecl(Decl):
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

    def accept(self, visitor, param):
        return visitor.visitMethodDecl(self, param)

    def __str__(self):
        return f"MethodDecl({self.name}, {self.param}, {self.returnType}, {self.body})"

class AttributeDecl(Decl):
    def __init__(self, isStatic, name, varType, idx, varInit):
        self.isStatic = isStatic
        self.name = name # Id
        self.varType = varType
        self.idx = idx
        self.varInit = varInit # Block

    def accept(self, visitor, param):
        return visitor.visitAttributeDecl(self, param)

    def __str__(self):
        return f"AttributeDecl({self.name}, {self.idx}, {self.varType}, {self.varInit})"
        

class Symbol:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Symbol({self.name})"

class VariableSymbol(Symbol):
    def __init__(self, name : str, type : Type = None, idx = 0, isStatic : bool = False, astVarDecl : VarDecl = None):
        self.name = name
        self.type = type
        self.idx = idx
        self.isStatic = isStatic
        self.astVarDecl = astVarDecl

    def __str__(self):
        return f"VariableSymbol({self.name}, {self.type})"


class FunctionSymbol(Symbol):
    def __init__(self, name, methodType = MethodType([],None), className : ClassName = None, param : list[VariableSymbol] = None, body = None, astFuncDecl=None):
        self.name = name
        self.methodType : MethodType = methodType  # MethodType
        if param is None:
            param = []
        self.param = param

        self.body = body
        self.astFuncDecl = astFuncDecl
        self.className = className

    def __str__(self):
        return f"FunctionSymbol({self.name}, {self.methodType})"

   
class SubBody():
    def __init__(self, frame : Frame, sym : list[Symbol]):
        self.frame : Frame = frame
        self.sym : list[Symbol] = sym # list of Symbol

    def __str__(self):
        return f"SubBody([{', '.join(str(i) for i in self.sym)}])"


class Access():
    def __init__(self,  frame : Frame, sym : list[Symbol], isLeft, isDeclared=False):
        self.frame : Frame = frame
        self.sym : list[Symbol] = sym # list of Symbol
        self.isLeft = isLeft
        self.isDeclared = isDeclared


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
        print("getSymbol: ", lhs, envi)

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
            result.append(self.visit(ast.decl[i], (self.env, VarDeclParam(True, i))))
        return ClassDecl(self.className, result)

    def visitVarDecl(self, ast : VarDecl, param : tuple[Envi,VarDeclParam]):
        
        (envi, varDeclParam) = param
        name = ast.name.name
        self.visit(ast.name, (envi, ExprParam(False, False)))
        
        current_scope = envi.getLast()
        
        # Visit variable type
        if ast.modifier == "var":
            varInitType = self.visit(ast.varInit, (envi, ExprParam(True, True))) 
            varSymbol = VariableSymbol(name, varInitType, varDeclParam.index, varDeclParam.isStatic, ast)
            attributeDecl = AttributeDecl(varDeclParam.isStatic, ast.name, varInitType, varDeclParam.index, ast.varInit)
            
            current_scope.define(varSymbol)
            return attributeDecl
            
        elif ast.modifier == "dynamic":  
            varSymbol = VariableSymbol(name, None)  
            if ast.varInit:
                varInitType = self.visit(ast.varInit, (envi, ExprParam(True, True))) if ast.varInit else None
                varSymbol = VariableSymbol(name, varInitType, varDeclParam.index, varDeclParam.isStatic, ast)
                
            attributeDecl = AttributeDecl(varDeclParam.isStatic, ast.name, varSymbol.type, varDeclParam.index, ast.varInit)
            
            current_scope.define(varSymbol)
            return attributeDecl
        
        else: # no modifier
            varType = self.visit(ast.varType, (envi, None))
            
            varSymbol = VariableSymbol(name, varType, varDeclParam.index, varDeclParam.isStatic, ast)
            attributeDecl = AttributeDecl(varDeclParam.isStatic, ast.name, varType, varDeclParam.index, ast.varInit)

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
            parameters : list[VariableSymbol] = []

            #print(len(envi),envi.getLast())
            envi.append(Scope()) # new scope for function parameters

            if ast.param:
                for i in range(0,len(ast.param)):
                    astParam = ast.param[i]
                    parameterSymbol = self.visit(astParam, (envi, VarDeclParam(False , i)))
                    parameters.append(parameterSymbol)
                
                #print(len(envi),envi.getLast())
            

            stmtParam = StmtParam(functionSymbol, 0)
            body = self.visit(ast.body, (envi, stmtParam)) if ast.body else None # declare only or implement function
            
            if body: # function has body so it must have a type
                if functionSymbol.methodType is None:
                    functionSymbol.methodType = MethodType([x.type for x in parameters],None)
                
                if functionSymbol.methodType.rettype is None:
                    functionSymbol.methodType = MethodType([x.type for x in parameters],VoidType()) 
                else:
                    functionSymbol.methodType = MethodType([x.type for x in parameters],functionSymbol.methodType.rettype)
            else:
                functionSymbol.methodType = MethodType([x.type for x in parameters],None)

            functionSymbol.param = parameters
            functionSymbol.body = body

            stmtParam.currentFunctionSymbol = None # pop the scope of function 
            envi.pop() # pop the scope of function parameters

        
        if functionSymbol is None: # first declaration of function 
            
            functionSymbol = FunctionSymbol(name, MethodType([],None), self.className, [], None, ast) # TODO : return type of function

            # Add function to current scope, add it soon because of recursive call
            envi.getLast().define(functionSymbol) 

            # Visit function parameters and body
            visitFuncParamAndBody(functionSymbol)
        
            return MethodDecl(Instance(), ast.name , functionSymbol.param, functionSymbol.methodType.rettype , functionSymbol.body) if functionSymbol.body else None

    
        elif type(functionSymbol) == FunctionSymbol: # implement the body function
        
            # Check for redeclared parameters
            visitFuncParamAndBody(functionSymbol)

            return MethodDecl(Instance(), functionSymbol.name, functionSymbol.param, functionSymbol.methodType.rettype , functionSymbol.body)
    
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
        
        return inferredReturnType # No type can be inferred

    def visitCallExpr(self, ast : CallExpr, param : Tuple[Envi, ExprParam]):
        #print("Call Expr: ",ast, param[1])

        (envi, exprParam) = param

        self.visit(ast.name, (envi, ExprParam( True, True)))
        functionSymbol : FunctionSymbol = self.getSymbol(ast.name, False, envi)


        for i in range(len(ast.args)):
            symbolParamType = functionSymbol.param[i].type
            callParamType = self.visit(ast.args[i], (envi, ExprParam(True, True, symbolParamType)))
            

        if functionSymbol.methodType.rettype is None: # function with not yet assigned type
            if exprParam.inferredType:
                functionSymbol.methodType.rettype = exprParam.inferredType
            
            
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
                        return symbol.type
                elif type(symbol) is FunctionSymbol:
                    if symbol.methodType.rettype:
                        return symbol.methodType.rettype
                    elif exprParam.inferredType:
                        symbol.methodType.rettype = exprParam.inferredType
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
                stmts = stmts + [self.visit(stmt, (envi, VarDeclParam(False, i)))]
                i += 1
            else:
                stmts = stmts + [self.visit(stmt, (envi, stmtParam))]

        envi.pop()

        return Block(stmts) 

    def visitIf(self, ast : If, param : Tuple[Envi, StmtParam]):
        #print("Visit If: ", ast)

        (envi, stmtParam) = param

        ifConditionType = self.visit(ast.expr, (envi, ExprParam(True, True, BoolType())))
        
        self.visit(ast.thenStmt, (envi, stmtParam))

        for (elifExpr, elifStmt) in ast.elifStmt:
            elifConditionType = self.visit(elifExpr, (envi, ExprParam( True, True, BoolType())))

            self.visit(elifStmt, (envi, stmtParam))
        
        if ast.elseStmt:
            self.visit(ast.elseStmt, (envi, stmtParam))

        return ast

    
    def visitFor(self, ast : For, param):
        #print("Visit For: ", ast)

        (envi, stmtParam) = param
    
        lhsType = self.visit(ast.name, (envi, ExprParam(False, True, NumberType())))
        symbol : VariableSymbol = self.getSymbol(ast.name, False, envi)
        updType = self.visit(ast.updExpr, (envi, ExprParam(True, True, NumberType())))

        
        if lhsType is None: # LHS first use so infer type
            lhsType = NumberType()
            symbol.type = lhsType
        
            
        # Visit condition of for loop
        condType = self.visit(ast.condExpr, (envi, ExprParam(True, True, BoolType())))
       
        
        # Visit body of for loop
        
        self.visit(ast.body, (envi, stmtParam))
        
        return ast

    
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

        if stmtParam.currentFunctionSymbol.methodType.rettype is None: # function type is not declared
            if ast.expr:
                returnType = self.visit(ast.expr, (envi, ExprParam(True, True, stmtParam.currentFunctionSymbol.methodType.rettype)))
            
                
                stmtParam.currentFunctionSymbol.methodType.rettype = returnType

            else:
                stmtParam.currentFunctionSymbol.methodType.rettype = VoidType()
        
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
            return ArrayType(0, None)
        
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

        # generate class static init
        staticAttributeDecl = list(filter(lambda x: type(x) == AttributeDecl and x.isStatic, ast.memlist))

        self.genMETHOD(MethodDecl(Instance(), Id("<clinit>"), list(), VoidType(), Block(staticAttributeDecl)), globalEnvi, Frame("<clinit>", VoidType()))

        # generate static classes
        for symbol in ast.memlist:
            if type(symbol) == MethodDecl:
                self.visit(symbol, SubBody(None, globalEnvi))
            
            
        
        # generate default constructor
        self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(
        ), None, Block([])), globalEnvi, Frame("<init>", VoidType()))
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
        print("VisitMethodDecl: ",ast, o)

        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        functionSymbol = FunctionSymbol(ast.name, MethodType([x.typ for x in ast.param], ast.returnType), ClassName(self.className))
        o.sym.append(functionSymbol)
        return functionSymbol

    
    def visitAttributeDecl(self, ast : AttributeDecl, o : SubBody):
        print("visitAttributeDecl: ",ast, o)

        isStatic = ast.isStatic
        variableSymbol = None
        if isStatic: # static variable
            self.emit.printout(self.emit.emitATTRIBUTE(ast.name.name, ast.varType, False, None))
            variableSymbol = VariableSymbol(ast.name.name, ast.varType, 0, isStatic, ast)

        else: # local variable
            idx = o.frame.getNewIndex()
            variableSymbol = VariableSymbol(ast.name.name, ast.varType, idx, isStatic, ast)
        

        initEmit, initType = self.visit(ast.varInit, Access(o.frame, o.sym, False, False))
        self.emit.printout(initEmit)
        #self.emit.printout(self.emit.emitPUSHCONST(idx, ast.varType, o.frame))
        
        o.sym.append(variableSymbol)

        leftEmit, leftType = self.visit(ast.name, Access(o.frame, o.sym, True, False))
        self.emit.printout(leftEmit)
        
        return variableSymbol
    

    def visitNumberType(self, ast, param):
        pass

    def visitBoolType(self, ast, param):
        pass

    def visitStringType(self, ast, param):
        pass

    def visitArrayType(self, ast, param):
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
        print("VisitCallStmt: ",ast, o)
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        functionSymbol : FunctionSymbol = next(filter(lambda x: ast.name.name == x.name, nenv), None)
        className = functionSymbol.className.name
        methodType = functionSymbol.methodType
        in_ = ("", list()) # Tuple of emit string and list of types
        
        # Visit arguments
        for x in ast.args:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1)) # Concatenate emit string and append type
        

        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            className + "/" + ast.name.name, methodType, frame))

    
    def visitCallExpr(self, ast : CallExpr, o : Access):
        print("VisitCallExpr: ",ast, o)
        print("VisitCallStmt: ",ast, o)
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        functionSymbol : FunctionSymbol = next(filter(lambda x: ast.name.name == x.name, nenv), None)
        className = functionSymbol.className.name
        methodType = functionSymbol.methodType
        in_ = ("", list()) # Tuple of emit string and list of types
        
        # Visit arguments
        for x in ast.args:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1)) # Concatenate emit string and append type
        

        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            className + "/" + ast.name.name, methodType, frame))
        
        return in_[0], methodType.rettype

    
    def visitId(self, ast : Id, param : Access):
        print("VisitId: ",ast, param)
        
        ctxt = param
        frame = ctxt.frame
        nenv = ctxt.sym
        symbol : VariableSymbol = next(filter(lambda x: ast.name == x.name, nenv), None)
        idx = symbol.idx
        typ = symbol.type
        
        if symbol.isStatic:
            if param.isLeft:
                return self.emit.emitPUTSTATIC(ast.name, typ, frame), typ
            else:
                return self.emit.emitGETSTATIC(ast.name, typ, frame), typ
        else:
            if param.isLeft :
                return self.emit.emitWRITEVAR(ast.name, typ, idx, frame), typ
            else :
                return self.emit.emitREADVAR(ast.name, typ, idx, frame), typ

       
            
    def visitNumberLiteral(self, ast : NumberLiteral, o : Access):
        return self.emit.emitPUSHFCONST(ast.value, o.frame), NumberType()

    def visitBooleanLiteral(self, ast : BooleanLiteral, o : Access):
        return self.emit.emitPUSHICONST(str(ast.value).lower(), o.frame), BoolType()

    def visitStringLiteral(self, ast : StringLiteral, o : Access):
        print("VisitStringLiteral: ",ast, o)
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()

    def visitArrayLiteral(self, ast, param):
        pass
