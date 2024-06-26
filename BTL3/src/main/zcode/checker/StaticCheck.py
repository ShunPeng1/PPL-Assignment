from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

from typing import List, Union, Tuple

# Student : Banh Tan Thuan
# Student ID : 2153011
# Class : CC03


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


class FunctionSymbol(Symbol):
    def __init__(self, name: str, type: Type = None, param: List[VariableSymbol] = None, body:Stmt =None):
        self.name = name
        self.type = type # return type of function
        
        if param is None:
            param = []
        self.param = param
        self.body = body


class Scope:
    def __init__(self, symbols = None):
        self.symbols = symbols if symbols is not None else []  # Initialize as empty list if None is provided
    
    def define(self, symbol : Symbol):
        self.symbols.append(symbol)
        
    
    def checkRedeclared(self, kind : Union[Function, Variable, Parameter], name: str):
        #print("checkRedeclared: ", kind, name, lst)
        
        symbolKind = FunctionSymbol if type(kind) == Function else VariableSymbol
       
        for symbol in self.symbols:
            if name == getName(symbol) and type(symbol) == symbolKind :
                raise Redeclared(kind, name)

        return None # No symbol found


class Envi:
    def __init__(self, scope : None):
        if scope is None:
            scope = []
        self.scope : List[Scope] = scope

    def append(self, scope : Scope):
        self.scope.append(scope)

    def pop(self):
        self.scope.pop()

    def getLast(self) -> Scope:
        return self.scope[-1]

    
    def checkDeclared(self, kind : Kind, name : str) -> Symbol:
        #print("checkDeclared: ", kind, name, envi)
        
        symbolKind = FunctionSymbol if type(kind) == Function else VariableSymbol

        for i in range(len(self.scope) - 1, -1, -1): # from current scope to global scope
            #print("checkDeclared Scope: ", i, envi[i])
            symbols = self.scope[i].symbols # list of Symbol in scope
           
            for symbol in symbols:
                if name == getName(symbol) and type(symbol) == symbolKind :
                    return symbol

        kind = kind if type(kind) == Function else Identifier()        
        raise Undeclared(kind, name)

    def getSymbol(self,kind : Kind, lhs : Union[Id , ArrayCell] , isOnlyLastScope : bool) -> Symbol:
        #print("getSymbol: ", lhs, envi)

        name = ""
        if type(lhs) == Id:
            name = lhs.name
        elif type(lhs) == ArrayCell:
            name = lhs.arr.name

        symbolKind = FunctionSymbol if type(kind) == Function else VariableSymbol

        if isOnlyLastScope:
            symbols = self.scope[-1].symbols # list of Symbol in scope last scope
           
            for symbol in symbols:
                if name == getName(symbol) and type(symbol) == symbolKind :
                    return symbol
        
        for i in range(len(self.scope) - 1, -1, -1): # from current scope to global scope
            #print("checkDeclared Scope: ", i, envi[i])
            symbols = self.scope[i].symbols # list of Symbol in scope
           
            for symbol in symbols:
                if name == getName(symbol) and type(symbol) == symbolKind :
                    return symbol

        return None # No symbol found
    

    def __getitem__(self, index : int):
        return self.scope[index]

    def __setitem__(self, index, value : Scope):
        self.scope[index] = value
    
    def __len__(self):
        return len(self.scope)

class ExprParam: 
    def __init__(self, kind : Kind, isRHS : bool = False, isDeclared : bool = False, inferredType : Type = None) -> None:
        self.kind = kind
        self.isRHS = isRHS
        self.isDeclared = isDeclared
        self.inferredType = inferredType


class VarDeclParam:
    def __init__(self, kind : Kind, scopeIndex : int) -> None:
        self.kind = kind
        self.scopeIndex = scopeIndex


class StmtParam:
    def __init__(self, currentFunctionSymbol : FunctionSymbol = None, insideLoopCount : int = 0) -> None:
        if currentFunctionSymbol is None:
            currentFunctionSymbol = None
        self.currentFunctionSymbol = currentFunctionSymbol
        self.insideLoopCount = 0
        pass
       
        
class UninferableType(Type):
    pass
    
class MismatchType(Type):
    pass

class UndeclaredType(Type):
    pass

def compareType(type1 : Type, type2 : Type) -> bool:
    #print("compareType: ", type1, type2)
    
    if type(type1) != type(type2): # type of value is different from inferred type
        return False # Type cannot be inferred, will raise error in parent node
            
    if type(type1) == ArrayType and type(type2) == ArrayType: # the value is an array type
        return compareArraySize(type1.size, type2.size) and compareType(type1.eleType, type2.eleType)

    return True
    
def compareArraySize(size1 : List[int], size2 : List[int]) -> bool:
    if len(size1) != len(size2):
        return False
    for i in range(len(size1)):
        if size1[i] != size2[i]:
            return False
    return True

class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast
        

    def checkEntry(self):
        #print("checkEntry: ", self.envi[0].symbols)

        globalSymbols = self.envi[0].symbols

        isFound = False
        for symbol in globalSymbols:
            if type(symbol) == FunctionSymbol and symbol.name == "main" and symbol.param == [] and type(symbol.type) == VoidType :#TODO : and symbol.type == VoidType:
                isFound = True
                
        if not isFound:
            raise NoEntryPoint()
        
    def checkFunctionDefined(self):
        globalSymbols = self.envi[0].symbols

        for symbol in globalSymbols:
            if type(symbol) == FunctionSymbol and symbol.body is None:
                raise NoDefinition(symbol.name)


    def check(self):
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

        return self.visit(self.ast, self.envi)


    def visitProgram(self, ast : Program, param : Envi):
        #print(ast)

        envi = param

        # Visit all declaration in program
        for decl in ast.decl:
            if type(decl) == VarDecl:
                self.visit(decl, (envi, VarDeclParam(Variable(), len(envi)-1)))
            elif type(decl) == FuncDecl:
                self.visit(decl, (envi, None))

        
        # Check for function defined
        self.checkFunctionDefined()
        
        # Check for entry point
        self.checkEntry()

        envi.pop()

        return 
        

    def visitVarDecl(self, ast : VarDecl, param : Tuple[Envi, VarDeclParam]):
        #print("visitVarDecl: ", ast)

        (envi, varDeclParam) = param
        name = ast.name.name
        self.visit(ast.name, (envi, ExprParam(varDeclParam.kind, False, False)))
        
        current_scope = envi.getLast()
        varSymbol = VariableSymbol(name, UndeclaredType())
        current_scope.define(varSymbol)
        
        # Visit variable type
        if ast.modifier == "dynamic":
            if ast.varInit:
                varInitType = self.visit(ast.varInit, (envi, ExprParam(Variable(), True, True))) if ast.varInit else None
                
                if type(varInitType) == UninferableType:
                    raise TypeCannotBeInferred(ast)
                
                varSymbol.type = varInitType
            else:
                varSymbol.type = None
        
        elif ast.modifier == "var":  
            varInitType = self.visit(ast.varInit, (envi, ExprParam(Identifier(), True, True))) 

            if type(varInitType) == UninferableType:
                raise TypeCannotBeInferred(ast)    
            
            varSymbol.type = varInitType
            

        else: # no modifier
            varType = self.visit(ast.varType, (envi, None))

            
            if ast.varInit:
                varInitType = self.visit(ast.varInit, (envi, ExprParam(Variable(), True, True, varType)))
                
                if type(varInitType) == UninferableType:
                    raise TypeCannotBeInferred(ast)

                #if type(varType) != type(varInitType):
                if compareType(varType, varInitType) == False:
                    raise TypeMismatchInStatement(ast)
            
            varSymbol.type = varType
            return varSymbol
    
    def visitFuncDecl(self, ast : FuncDecl, param : Tuple[Envi, None]):
        #print("FuncDecl: ",ast)

        (envi, _) = param

        # Get function symbol
        functionSymbol = envi.getSymbol(Function(), ast.name, True)
        name = ast.name.name
        isDeclared = functionSymbol is not None

        self.visit(ast.name, (envi, ExprParam(Function(), False, isDeclared))) # visit function name, check functionSymbol have declared or not
        
        def visitFuncParam():
            parameters = []

            #print(len(envi),envi.getLast())
            envi.append(Scope()) # new scope for function parameters

            if ast.param:
                for astParam in ast.param:
                    parameterSymbol = self.visit(astParam, (envi, VarDeclParam(Parameter(), len(envi)-1)))
                    parameters.append(parameterSymbol)
                
                #print(len(envi),envi.getLast())
            return parameters

        def visitFuncBody(functionSymbol : FunctionSymbol = None):
            stmtParam = StmtParam(functionSymbol, 0)
            body = self.visit(ast.body, (envi, stmtParam)) if ast.body else None # declare only or implement function
            
            if body: # function has body so it must have a type
                if functionSymbol.type is None:
                    functionSymbol.type = VoidType()
            
            
            stmtParam.currentFunctionSymbol = None # pop the scope of function 
            envi.pop() # pop the scope of function parameters

            return body

        
        if functionSymbol is None: # first declaration of function 
            
            functionSymbol = FunctionSymbol(name, None, [], None) # TODO : return type of function

            # Add function to current scope, add it soon because of recursive call
            envi.getLast().define(functionSymbol) 

            # Visit function parameters and body
            parameters = visitFuncParam()
            functionSymbol.param = parameters
            body = visitFuncBody(functionSymbol)
            functionSymbol.body = body
        
        
            return functionSymbol
    
        elif type(functionSymbol) == FunctionSymbol: # implement the body function
            
            if ast.body is None:
                raise Redeclared(Function(), name) # redeclared a declared-only function

            # Check for redeclared parameters
            parameters = visitFuncParam()

            # Create lists of parameter types
            #function_param_types = list(map(lambda param: type(param.type), functionSymbol.param))
            #parameters_types = list(map(lambda param: type(param.type), parameters))

            # Compare the lists of parameter types
            #if function_param_types != parameters_types:
            #    raise Redeclared(Function(), name)


            function_param_types = list(map(lambda param: param.type, functionSymbol.param))
            parameters_types = list(map(lambda param: param.type, parameters))

            if len(function_param_types) != len(parameters_types):
                raise Redeclared(Function(), name)

            for i in range(len(function_param_types)):
                if compareType(function_param_types[i], parameters_types[i]) == False:
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

    
    def visitBinaryOp(self, ast : BinaryOp, param : Tuple[Envi, ExprParam]):
        #print("Binary Op: ", ast, param)
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
        
        if type(left) is UninferableType or type(right) is UninferableType:
            return UninferableType() # Type cannot be inferred, will raise error in parent node

        #if type(right) != type(inferredOperandType) or type(left) != type(inferredOperandType):
        if compareType(left, inferredOperandType) == False or compareType(right, inferredOperandType) == False:
            raise TypeMismatchInExpression(ast)

        #print("Binary Op Type: ", left, right, inferredReturnType)
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
            operandParam = ExprParam(Variable(), True, True, inferredOperandType)
        
        exprType = self.visit(ast.operand, (envi, operandParam))
        
        if type(exprType) is UninferableType:
            return UninferableType() # Type cannot be inferred, will raise error in parent node

        #if type(expr) != type(inferredOperandType):
        if compareType(exprType, inferredOperandType) == False:
            raise TypeMismatchInExpression(ast)

        return inferredReturnType # No type can be inferred

    
    def visitCallExpr(self, ast : CallExpr, param : Tuple[Envi, ExprParam]):
        #print("Call Expr: ",ast, param[1])

        (envi, exprParam) = param

        self.visit(ast.name, (envi, ExprParam(Function(), True, True)))
        functionSymbol = envi.getSymbol(Function(),ast.name, False)

        if functionSymbol is None:
            raise Undeclared(Function(), ast.name)

        if type(functionSymbol) != FunctionSymbol:
            raise TypeMismatchInExpression(ast)

        if len(ast.args) != len(functionSymbol.param):
            raise TypeMismatchInExpression(ast)

        for i in range(len(ast.args)):
            symbolParamType = functionSymbol.param[i].type
            callParamType = self.visit(ast.args[i], (envi, ExprParam(Variable(), True, True, symbolParamType)))
            
            if compareType(callParamType, symbolParamType) == False:
                raise TypeMismatchInExpression(ast)
                    
            

        if functionSymbol.type is None: # function with not yet assigned type
            if exprParam.inferredType:
                functionSymbol.type = exprParam.inferredType
            else:
                #return None
                return UninferableType() # Will raise error in parent node

        else: # function declared and have the return type
            #if exprParam.inferredType and type(functionSymbol.type) != type(exprParam.inferredType): # inferred type is different from declared type and exist
            if exprParam.inferredType and compareType(functionSymbol.type, exprParam.inferredType) == False: # inferred type is different from declared type and exist
                return MismatchType() # Will raise error in parent node
                #return None # Will raise error in parent node
            
        return functionSymbol.type 


    
    
    def visitId(self, ast : Id, param : Tuple[Envi, ExprParam]):
        #print("Visit Id: " , ast, param)
        (envi, exprParam) = param
        if type(exprParam) == ExprParam:
            if exprParam.isRHS:
                symbol = envi.checkDeclared(exprParam.kind, ast.name)
                
                if symbol.type:
                    if type(symbol.type) == UndeclaredType:
                        
                        raise Undeclared(Identifier(), ast.name)                  
                    return symbol.type
                elif exprParam.inferredType : # No type in symbol yet so inferred type
                    symbol.type = exprParam.inferredType
                    return symbol.type
                else :
                    return UninferableType() # No type can be inferred, will raise error in parent node
        
            else : # LHS
                if exprParam.isDeclared:
                    symbol = envi.checkDeclared(exprParam.kind, ast.name)
                    return symbol.type
                else : # not declared
                    envi.getLast().checkRedeclared(exprParam.kind, ast.name)
                    return UninferableType() # No type can be inferred, will raise error in parent node

        else:
            return ast.name

    
    def visitArrayCell(self, ast : ArrayCell, param : Tuple[Envi, ExprParam]):
        #print("Array Cell: ", ast, param)

        (envi, exprParam) = param

        arrType = self.visit(ast.arr, (envi, ExprParam(Variable(), exprParam.isRHS, exprParam.isDeclared, None))) # visit array type
        
        #print("Array Cell Type: ", arrType, exprParam.isRHS, exprParam.isDeclared, exprParam.inferredType, len(ast.idx))
        if arrType is None or type(arrType) == UninferableType: # arrType type is None cannot know if ArrayCell a[1,2,3] is array of [?,?,?] size
            return UninferableType() # Type cannot be inferred, will raise error in parent node

        if type(arrType) != ArrayType:
            raise TypeMismatchInExpression(ast) # arrType is not an array type

        if len(ast.idx) > len(arrType.size): # index out of range
            raise TypeMismatchInExpression(ast)

        innerType = ArrayType(arrType.size, arrType.eleType) # copy of array type       
        for i in range(len(ast.idx)):
            idx = ast.idx[i]
            idxType = self.visit(idx, (envi, ExprParam(Variable(), True, True, NumberType())))

            if type(idxType) != NumberType:
                raise TypeMismatchInExpression(ast)

            if len(innerType.size) > 1: # inner type of the array is the array (a[3,2] inner is a[2])
                innerType.size = innerType.size[1:]
            else : # inner type of the array is the element type 
                innerType = innerType.eleType

        #print("Array Cell Inner Type: ", innerType)
        return innerType # return type of array cell        
        

    
    def visitBlock(self, ast : Block, param : Tuple[Envi, StmtParam]):
        #print("Visit Block: ", ast)
        
        (envi, stmtParam) = param

        envi.append(Scope())

        for stmt in ast.stmt:
            if type(stmt) == VarDecl:
                self.visit(stmt, (envi, VarDeclParam(Variable(), len(self.envi)-1)))
            else:
                self.visit(stmt, (envi, stmtParam))

        envi.pop()


        return ast # TODO : return of a statement

    
    def visitIf(self, ast : If, param : Tuple[Envi, StmtParam]):
        #print("Visit If: ", ast)

        (envi, stmtParam) = param

        ifConditionType = self.visit(ast.expr, (envi, ExprParam(Variable(), True, True, BoolType())))

        if type(ifConditionType) != BoolType or type(ifConditionType) == MismatchType:
            raise TypeMismatchInStatement(ast)
            
        
        if type(ast.thenStmt) == VarDecl:
            self.visit(ast.thenStmt, (envi, VarDeclParam(Variable(), len(self.envi)-1))) 
        else:
            self.visit(ast.thenStmt, (envi, stmtParam))

        for (elifExpr, elifStmt) in ast.elifStmt:
            elifConditionType = self.visit(elifExpr, (envi, ExprParam(Variable(), True, True, BoolType())))
            
            if type(elifConditionType) != BoolType:
                raise TypeMismatchInStatement(ast)

            if type(elifStmt) == VarDecl:
                self.visit(elifStmt, (envi, VarDeclParam(Variable(), len(self.envi)-1))) 
            else:
                self.visit(elifStmt, (envi, stmtParam))
                
        
        if ast.elseStmt:
            if type(ast.elseStmt) == VarDecl:
                self.visit(ast.elseStmt, (envi, VarDeclParam(Variable(), len(self.envi)-1))) 
            else:
                self.visit(ast.elseStmt, (envi, stmtParam))
    

        return ast # TODO : return of a statement

    
    def visitFor(self, ast : For, param : Tuple[Envi, StmtParam]):
        #print("Visit For: ", ast)

        (envi, stmtParam) = param
    
        lhsType = self.visit(ast.name, (envi, ExprParam(Variable(), False, True, NumberType())))
        symbol = envi.getSymbol(Variable(), ast.name, False)
        updType = self.visit(ast.updExpr, (envi, ExprParam(Variable(), True, True, NumberType())))

        
        if lhsType is None: # LHS first use so infer type
            lhsType = NumberType()
            symbol.type = lhsType

        if type(lhsType) != NumberType or type(updType) != NumberType:
                raise TypeMismatchInStatement(ast)
            
        if type(updType) == UninferableType or type(lhsType) == UninferableType:
            raise TypeCannotBeInferred(ast)
        
        if type(lhsType) == MismatchType or type(updType) == MismatchType:
            raise TypeMismatchInStatement(ast)
        
            

        # Visit condition of for loop
        condType = self.visit(ast.condExpr, (envi, ExprParam(Variable(), True, True, BoolType())))
        if type(condType) != BoolType or type(condType) == MismatchType:
            raise TypeMismatchInStatement(ast)
        
        if type(condType) == UninferableType:
            raise TypeCannotBeInferred(ast)
        
        # Visit body of for loop
        stmtParam.insideLoopCount += 1
        
        if type(ast.body) == VarDecl:
            self.visit(ast.body, (envi, VarDeclParam(Variable(), len(self.envi)-1))) 
        else:
            self.visit(ast.body, (envi, stmtParam))

        stmtParam.insideLoopCount -= 1

        return ast # TODO : return of a statement

    
    def visitContinue(self, ast : Continue, param : Tuple[Envi, StmtParam]):
        #print("Visit Continue: ", ast)

        (envi, stmtParam) = param

        if stmtParam.insideLoopCount == 0:
            raise MustInLoop(ast)
        
        return ast # TODO : return of a statement

    
    def visitBreak(self, ast : Break, param : Tuple[Envi, StmtParam]):
        #print("Visit Break: ", ast)

        (envi, stmtParam) = param

        if stmtParam.insideLoopCount == 0:
            raise MustInLoop(ast)

        return ast # TODO : return of a statement
    
    def visitReturn(self, ast : Return, param : Tuple[Envi, StmtParam]):
        
        (envi, stmtParam) = param

        if stmtParam.currentFunctionSymbol.type is None: # function type is not declared
            if ast.expr:
                returnType = self.visit(ast.expr, (envi, ExprParam(Variable(), True, True, stmtParam.currentFunctionSymbol.type)))
                
                if type(returnType) == UninferableType:
                    raise TypeCannotBeInferred(ast)
                
                stmtParam.currentFunctionSymbol.type = returnType

            else:
                stmtParam.currentFunctionSymbol.type = VoidType()
        
        else: # function type is declared
            if ast.expr:
                returnType = self.visit(ast.expr, (envi, ExprParam(Variable(), True, True, stmtParam.currentFunctionSymbol.type)))
                
                #if type(returnType) != type(stmtParam.currentFunctionSymbol.type):
                if compareType(returnType, stmtParam.currentFunctionSymbol.type) == False:
                    raise TypeMismatchInStatement(ast)
            else:
                if type(stmtParam.currentFunctionSymbol.type) != VoidType:
                    raise TypeMismatchInStatement(ast)

        
        return ast # TODO : return of a statement


    
    def visitAssign(self, ast : Assign, param : Tuple[Envi, StmtParam]):
        #print("Assign: ", ast)
        (envi, stmtParam) = param

        lhsType = self.visit(ast.lhs, (envi, ExprParam(Variable(), False, True)))
        symbol = envi.getSymbol(Variable(),ast.lhs, False)

        if lhsType: # LHS is declared and has type
            rhsType = self.visit(ast.rhs, (envi, ExprParam(Variable(), True, True, lhsType)))

            #print("Assign LHS Type1: ", lhsType, rhsType)

            if type(rhsType) == UninferableType or type(lhsType) == UninferableType:
                raise TypeCannotBeInferred(ast)

            #if type(lhsType) != type(rhsType):
            if compareType(lhsType, rhsType) == False:
                raise TypeMismatchInStatement(ast)
            
        else: # LHS first use
            rhsType = self.visit(ast.rhs, (envi, ExprParam(Variable(), True, True)))
            
            #print("Assign LHS Type2: ", lhsType, rhsType)

            if type(rhsType) == UninferableType:
                raise TypeCannotBeInferred(ast)
            
            if type(rhsType) == MismatchType:
                raise TypeMismatchInStatement(ast)
            
            if symbol.type is not None and compareType(symbol.type, rhsType) == False:
                raise TypeMismatchInStatement(ast)
            

            symbol.type = rhsType

        
        return ast # TODO : return of a statement

    
    def visitCallStmt(self, ast : CallStmt, param : Tuple[Envi, StmtParam]):
        #print("Call Stmt: ",ast)

        (envi, stmtParam) = param

        self.visit(ast.name, (envi, ExprParam(Function(), True, True)))
        functionSymbol = envi.getSymbol(Function(),ast.name, False)

        if functionSymbol is None:
            raise Undeclared(Function(), ast.name)

        if type(functionSymbol) != FunctionSymbol:
            raise TypeMismatchInStatement(ast)

        if len(ast.args) != len(functionSymbol.param):
            raise TypeMismatchInStatement(ast)

        for i in range(len(ast.args)):
            symbolParamType = functionSymbol.param[i].type
            callParamType = self.visit(ast.args[i], (envi, ExprParam(Variable(), True, True, symbolParamType)))
            
            if compareType(callParamType, symbolParamType) == False:
                raise TypeMismatchInStatement(ast)
            

        if functionSymbol.type is None: # function declared-only
            functionSymbol.type = VoidType()
        elif type(functionSymbol.type) != VoidType: # this must be a void function
            raise TypeMismatchInStatement(ast)    
           
        return ast # TODO : return of a statement


    
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
        
        inferredType = exprParam.inferredType
        if inferredType: 
            if type(inferredType) != ArrayType: # inferred type is not an array
                for i in range(0,len(ast.value)):
                    value = ast.value[i]
                    valueType = self.visit(value, (envi, ExprParam(Variable(), True, True, None)))
                    
                    #print("Array Literal Value Type: ", valueType, innerType)
                    if type(valueType) == UninferableType:
                        return UninferableType()


                return MismatchType() # TODO : check again and raise error
                
            # Check for size of array
            #print("Array Literal Inferred Type: ", inferredType.size, len(ast.value), inferredType.eleType, len(inferredType.size) > 0, inferredType.size[0] != len(ast.value))
            if len(inferredType.size) > 0:
                if (inferredType.size[0] != len(ast.value)):
                    return MismatchType() # Type cannot be inferred, will raise error in parent node

            # Get inner type of array
            innerType = ArrayType(inferredType.size, inferredType.eleType) # copy of array type
                
            if len(inferredType.size) <= 1:
                innerType = inferredType.eleType
            else :
                innerType = ArrayType( inferredType.size[1:] , inferredType.eleType)

            #firstType = self.visit(ast.value[0], (envi, ExprParam(Variable(), True, True, innerType)))
            #if compareType(firstType, innerType) == False:
            #    return MismatchType() # Not the same type as first will raise error in the parent node

            # Check for type of each value in array
            for i in range(0,len(ast.value)):
                value = ast.value[i]
                valueType = self.visit(value, (envi, ExprParam(Variable(), True, True, innerType)))
                
                #print("Array Literal Value Type: ", valueType, innerType)
                if type(valueType) == UninferableType:
                    return UninferableType()

                if compareType(valueType, innerType) == False:
                    #return MismatchType()
                    raise TypeMismatchInExpression(ast) # Not the same type as first will raise error in the current node

            return ArrayType(inferredType.size , inferredType.eleType)


        else : # No inferred type
            
            firstType = None            
            for value in ast.value:
                firstType = self.visit(value, (envi, ExprParam(Variable(), True, True, None)))

                if (firstType and type(firstType) != UninferableType):
                    break
            
            #print("Array Literal First Type: ", firstType)
            if firstType is None or type(firstType) == UninferableType:
                return UninferableType() # TODO : check again and raise error
            
            # Check for type of each value in array
            for value in ast.value:
                valueType = self.visit(value, (envi, ExprParam(Variable(), True, True, firstType)))
                
                if type(valueType) == UninferableType:
                    return UninferableType()

                #print("Array Literal Value Type: ", valueType, firstType)
                if compareType(valueType, firstType) == False:
                    raise TypeMismatchInExpression(ast)
                

            if type(firstType) == ArrayType: # the first element is an array type
                return ArrayType([len(ast.value)] + firstType.size, firstType.eleType)
            
            else: # inferred type is not an array, maybe NumberType, StringType, BoolType, VoidType
                return ArrayType([len(ast.value)], firstType)

