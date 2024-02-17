from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

# Student : Banh Tan Thuan
# Student ID : 2153011
# Class : CC03

class ASTGeneration(ZCodeVisitor):
    
    # program						: newline_list? declaration_list newline_list? EOF;
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
       #print("Program ", ctx.declaration_list())
        program = Program(self.visit(ctx.declaration_list()))
        return program

    
    # declaration_list			: declaration declaration_list // Recursive
	#						    | declaration; // At least one declaration
    def visitDeclaration_list(self, ctx:ZCodeParser.Declaration_listContext):
        if ctx.declaration_list():
            
            return [self.visit(ctx.declaration())] + self.visit(ctx.declaration_list())
        else:
            return [self.visit(ctx.declaration())]
        
        

    # declaration					: function_declaration newline_list?
    #   							| variable_declaration_statement newline_list;     
    def visitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        if ctx.function_declaration():
            return self.visit(ctx.function_declaration())
        elif ctx.variable_declaration_statement():
            return self.visit(ctx.variable_declaration_statement())
        else :
            return None
        
    
    # local_statement_single		: newline_list? local_statement newline_list?;
    def visitLocal_statement_single(self, ctx:ZCodeParser.Local_statement_singleContext):
       #print("Local Statement Single ", ctx.local_statement())
        return self.visit(ctx.local_statement())

    # local_statement_list		    : (newline_list|local_statement) local_statement_list // Recursive
	#	        					| ; // Empty statement list
    def visitLocal_statement_list(self, ctx:ZCodeParser.Local_statement_listContext):
       #print("Local Statement List ", ctx.local_statement(), ctx.local_statement_list())
        
        if ctx.local_statement() and ctx.local_statement_list():
            return [self.visit(ctx.local_statement())] + self.visit(ctx.local_statement_list())
        elif ctx.local_statement_list():
            return self.visit(ctx.local_statement_list())
        elif ctx.local_statement():
            return [self.visit(ctx.local_statement())]
        else:
            return []

    # local_statement				: variable_declaration_statement NEWLINE
	#       						| if_statement 
	#       						| function_call_statement NEWLINE
	#       						| for_statement 
	#       						| break_statement NEWLINE
	#       						| continue_statement NEWLINE
	#       						| block_statement
	#       						| assignment_statement NEWLINE
	#       						| return_statement NEWLINE;
    def visitLocal_statement(self, ctx:ZCodeParser.Local_statementContext):
        if ctx.variable_declaration_statement():
            return self.visit(ctx.variable_declaration_statement())
        elif ctx.if_statement():
            return self.visit(ctx.if_statement())
        elif ctx.function_call_statement():
            return self.visit(ctx.function_call_statement())
        elif ctx.for_statement():
            return self.visit(ctx.for_statement())
        elif ctx.break_statement():
            return self.visit(ctx.break_statement())
        elif ctx.continue_statement():
            return self.visit(ctx.continue_statement())
        elif ctx.block_statement():
            return self.visit(ctx.block_statement())
        elif ctx.assignment_statement():
            return self.visit(ctx.assignment_statement())
        elif ctx.return_statement():
            return self.visit(ctx.return_statement())
        else :
            return None


    # Visit a parse tree produced by ZCodeParser#newline_list.
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return None


    # Visit a parse tree produced by ZCodeParser#newline.
    def visitNewline(self, ctx:ZCodeParser.NewlineContext):
        return None


    # block_statement				: BEGIN newline_list local_statement_list END newline_list ;
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
       #print("Block Statement ", ctx.local_statement_list())
        block = Block(self.visit(ctx.local_statement_list()))
       #print("Block Statement ", block)
        return block

    # variable_declaration_statement	: basic_variable_declaration | array_declaration ;
    def visitVariable_declaration_statement(self, ctx:ZCodeParser.Variable_declaration_statementContext):
        if ctx.basic_variable_declaration():
            return self.visit(ctx.basic_variable_declaration())
        elif ctx.array_declaration():
            return self.visit(ctx.array_declaration())
        else :
            return None


    # basic_variable_declaration	: VAR IDENTIFIER ASSIGN expression // Must have initial value
	#	        					| (basic_type | DYNAMIC) IDENTIFIER (ASSIGN expression)?;
    def visitBasic_variable_declaration(self, ctx:ZCodeParser.Basic_variable_declarationContext):
        expression = self.visit(ctx.expression()) if ctx.expression() else None
        type = self.visit(ctx.basic_type()) if ctx.basic_type() else None
        id = Id(ctx.IDENTIFIER().getText())
        
        #print("Basic Variable Declaration ", ctx.expression(), expression, ctx.basic_type(), id)

        modifier = str
        if ctx.DYNAMIC():
            modifier = ctx.DYNAMIC().getText()
        elif ctx.VAR():
            modifier = ctx.VAR().getText()
        else :
            modifier = None
        
        return VarDecl(id, type, modifier, expression)
        

    # basic_type					: (NUMBER_TYPE | STRING_TYPE | BOOLEAN_TYPE) ;
    def visitBasic_type(self, ctx:ZCodeParser.Basic_typeContext):
        if ctx.NUMBER_TYPE():
            return NumberType()
        elif ctx.STRING_TYPE():
            return StringType()
        elif ctx.BOOLEAN_TYPE():
            return BoolType()
        else :
            return None


    # array_declaration			: basic_type IDENTIFIER array_dimension (ASSIGN expression)?;
    def visitArray_declaration(self, ctx:ZCodeParser.Array_declarationContext):
        type = self.visit(ctx.basic_type())
        id = Id(ctx.IDENTIFIER().getText())
        dimension = self.visit(ctx.array_dimension())

        arrayType = ArrayType(dimension, type)
        
        value = self.visit(ctx.expression()) if ctx.expression() else None
        
        return VarDecl(id, arrayType, None, value)
        

    # array_dimension 			: LBRACK array_dimension_list RBRACK;
    def visitArray_dimension(self, ctx:ZCodeParser.Array_dimensionContext):
        return self.visit(ctx.array_dimension_list())
        

    # array_dimension_list 		: number_literal COMMA array_dimension_list // Recursive
	#   						| number_literal;
    def visitArray_dimension_list(self, ctx:ZCodeParser.Array_dimension_listContext):
        size = float(self.visit(ctx.number_literal()).value)

        if ctx.array_dimension_list():
            return [size] + self.visit(ctx.array_dimension_list())
        else:
            return [size]


    # assignment_statement		: IDENTIFIER element_expression? ASSIGN expression;
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        lhs = Expr
        id = Id(ctx.IDENTIFIER().getText())
        
        if ctx.element_expression():
            lhs = ArrayCell(id, self.visit(ctx.element_expression()))
        else:
            lhs = id

        expression = self.visit(ctx.expression())

        return Assign(lhs, expression)

    # function_declaration		: FUNC IDENTIFIER LPAREN parameter_part_recursive? RPAREN function_body ; // Declaration onlu or body definition might be empty
    def visitFunction_declaration(self, ctx:ZCodeParser.Function_declarationContext):
       #print("Function Declaration ", ctx.IDENTIFIER(), ctx.parameter_part_recursive(), ctx.function_body())

        id = Id(ctx.IDENTIFIER().getText())
        parameter = self.visit(ctx.parameter_part_recursive()) if ctx.parameter_part_recursive() else []
        body = self.visit(ctx.function_body()) if ctx.function_body() else None
        
        return FuncDecl(id, parameter, body)

    # function_body			   	    : newline_list? return_statement NEWLINE
	#	    				    	| newline_list? block_statement
	#		    		    		| newline;
    def visitFunction_body(self, ctx:ZCodeParser.Function_bodyContext):
       #print("Function Body ", ctx.return_statement(), ctx.block_statement(), ctx.newline())
        if ctx.return_statement():
            return self.visit(ctx.return_statement())
        elif ctx.block_statement():
            return self.visit(ctx.block_statement())
        else :
            return None

    # return_statement		    	: RETURN expression?;
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        expression = self.visit(ctx.expression()) if ctx.expression() else None
        return Return(expression)

    # parameter_part_recursive      : parameter_declaration COMMA parameter_part_recursive // Recursive
	#                               | parameter_declaration;
    def visitParameter_part_recursive(self, ctx:ZCodeParser.Parameter_part_recursiveContext):
        if ctx.parameter_part_recursive():
            return [self.visit(ctx.parameter_declaration())] + self.visit(ctx.parameter_part_recursive())
        else:
            return [self.visit(ctx.parameter_declaration())]

    # parameter_declaration	    	: basic_parameter_declaration
	#   		    				| array_parameter_declaration;
    def visitParameter_declaration(self, ctx:ZCodeParser.Parameter_declarationContext):
        if ctx.basic_parameter_declaration():
            return self.visit(ctx.basic_parameter_declaration())
        elif ctx.array_parameter_declaration():
            return self.visit(ctx.array_parameter_declaration())
        else :
            return None

    # basic_parameter_declaration	: basic_type IDENTIFIER;
    def visitBasic_parameter_declaration(self, ctx:ZCodeParser.Basic_parameter_declarationContext):
        type = self.visit(ctx.basic_type())
        id = Id(ctx.IDENTIFIER().getText())

       #print("Basic Parameter Declaration ", ctx.basic_type(), ctx.IDENTIFIER())

        return VarDecl(id, type, None, None)

    # array_parameter_declaration	: basic_type IDENTIFIER array_dimension;
    def visitArray_parameter_declaration(self, ctx:ZCodeParser.Array_parameter_declarationContext):
       #print("Array Parameter Declaration ", ctx.basic_type(), ctx.IDENTIFIER(), ctx.array_dimension())

        type = self.visit(ctx.basic_type())
        id = Id(ctx.IDENTIFIER().getText())
        dimension = self.visit(ctx.array_dimension())
        arrayType = ArrayType(dimension, type)


        return VarDecl(id, arrayType, None, None)

    # if_statement				: IF branch_condition branch_body 
	#							(elif_recursive_statement)?
	#							(else_statement)? ;
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
       #print("If Statement ", ctx.branch_condition(), ctx.branch_body(), ctx.elif_recursive_statement(), ctx.else_statement())

        condition = self.visit(ctx.branch_condition())
        body = self.visit(ctx.branch_body())
        elifStmt = self.visit(ctx.elif_recursive_statement()) if ctx.elif_recursive_statement() else []
        elseStmt = self.visit(ctx.else_statement()) if ctx.else_statement() else None

        if_statement = If(condition, body, elifStmt, elseStmt) ## TODO : Check again
       #print("If Statement ", condition, body, elifStmt, elseStmt)
       #print("If Statement ", if_statement)
        return if_statement

    # elif_recursive_statement	: elif_statement elif_recursive_statement // Recursive
	#   						| elif_statement;
    def visitElif_recursive_statement(self, ctx:ZCodeParser.Elif_recursive_statementContext):
        if ctx.elif_recursive_statement():
            return [self.visit(ctx.elif_statement())] + self.visit(ctx.elif_recursive_statement())
        else:
            return [self.visit(ctx.elif_statement())]

    # elif_statement				: ELIF branch_condition branch_body;
    def visitElif_statement(self, ctx:ZCodeParser.Elif_statementContext):
        condition = self.visit(ctx.branch_condition())
        body = self.visit(ctx.branch_body())

        return (condition, body)

    # else_statement				: ELSE branch_body;
    def visitElse_statement(self, ctx:ZCodeParser.Else_statementContext):
       #print("Else Statement ", ctx.branch_body())
        return self.visit(ctx.branch_body())

    # branch_condition		    	: LPAREN expression RPAREN;
    def visitBranch_condition(self, ctx:ZCodeParser.Branch_conditionContext):
        return self.visit(ctx.expression())

    # branch_body					: local_statement_single;
    def visitBranch_body(self, ctx:ZCodeParser.Branch_bodyContext):
       #print("Branch Body ", ctx.local_statement_single())
        return self.visit(ctx.local_statement_single())

    # function_call_statement		: IDENTIFIER LPAREN argument_part? RPAREN ;
    def visitFunction_call_statement(self, ctx:ZCodeParser.Function_call_statementContext):
        id = Id(ctx.IDENTIFIER().getText())
        argument = self.visit(ctx.argument_part()) if ctx.argument_part() else []

        return CallStmt(id, argument)

    # function_call_expression	: IDENTIFIER LPAREN argument_part? RPAREN ;
    def visitFunction_call_expression(self, ctx:ZCodeParser.Function_call_expressionContext):
        id = Id(ctx.IDENTIFIER().getText())
        argument = self.visit(ctx.argument_part()) if ctx.argument_part() else []

        return CallExpr(id, argument)

    # argument_part		    		: expression COMMA argument_part // Recursive
	#   				    		| expression;
    def visitArgument_part(self, ctx:ZCodeParser.Argument_partContext):
        if ctx.argument_part():
            return [self.visit(ctx.expression())] + self.visit(ctx.argument_part())
        else:
            return [self.visit(ctx.expression())]

    # for_statement				: FOR IDENTIFIER UNTIL expression BY expression loop_body;
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        id = Id(ctx.IDENTIFIER().getText())
        condition = self.visit(ctx.expression(0))
        update = self.visit(ctx.expression(1))
        body = self.visit(ctx.loop_body())

        return For(id, condition, update, body)

    # loop_body					: local_statement_single;
    def visitLoop_body(self, ctx:ZCodeParser.Loop_bodyContext):
        return self.visit(ctx.local_statement_single())

    # break_statement				: BREAK;
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return Break()

    # continue_statement			: CONTINUE;
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return Continue()

    # expression 					: string_expression; // Highest precedence
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visit(ctx.string_expression())


    # string_expression 			: relational_expression CONCATE relational_expression // Binary Infix None Associative
	#       						| relational_expression; // Next precedence
    def visitString_expression(self, ctx:ZCodeParser.String_expressionContext):
       #print("String Expression ", ctx.CONCATE(), ctx.relational_expression())
        if ctx.CONCATE():
            left = self.visit(ctx.relational_expression(0))
            right = self.visit(ctx.relational_expression(1))
            op = ctx.CONCATE().getText()
            return BinaryOp(op, left, right)    
        else:
            return self.visit(ctx.relational_expression(0))


    # relational_expression	    	: logical_expression relational_operator logical_expression // Binary Infix None Associative
	#   						    | logical_expression; // Next precedence
    def visitRelational_expression(self, ctx:ZCodeParser.Relational_expressionContext):
       #print("Relational Expression ", ctx.relational_operator(), ctx.logical_expression())
        if ctx.relational_operator():
            left = self.visit(ctx.logical_expression(0))
            right = self.visit(ctx.logical_expression(1))
            op = self.visit(ctx.relational_operator())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.logical_expression(0))
        

    # logical_expression			: logical_expression logic_operator adding_expression // Binary Infix Left Associative
	#       						| adding_expression; // Next precedence
    def visitLogical_expression(self, ctx:ZCodeParser.Logical_expressionContext):
       #print("Logical Expression ", ctx.logic_operator(), ctx.adding_expression())
        if ctx.logic_operator():
            left = self.visit(ctx.logical_expression())
            right = self.visit(ctx.adding_expression())
            op = self.visit(ctx.logic_operator())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.adding_expression())


    # adding_expression			: adding_expression additive_operator multiplying_expression // Binary Infix Left Associative
	#   						| multiplying_expression; // Next precedence
    def visitAdding_expression(self, ctx:ZCodeParser.Adding_expressionContext):
       #print("Adding Expression ", ctx.additive_operator(), ctx.multiplying_expression())
        if ctx.additive_operator():
            left = self.visit(ctx.adding_expression())
            right = self.visit(ctx.multiplying_expression())
            op = self.visit(ctx.additive_operator())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.multiplying_expression())
        

    # multiplying_expression		: multiplying_expression multiplicative_operator negation_expression // Binary Infix Left Associative
	#       						| negation_expression; // Next precedence
    def visitMultiplying_expression(self, ctx:ZCodeParser.Multiplying_expressionContext):
       #print("Multiplying Expression ", ctx.multiplicative_operator(), ctx.negation_expression())
        if ctx.multiplicative_operator():
            left = self.visit(ctx.multiplying_expression())
            right = self.visit(ctx.negation_expression())
            op = self.visit(ctx.multiplicative_operator())
            return BinaryOp(op, left, right)
        else:
            return self.visit(ctx.negation_expression())
        

    # negation_expression			: NOT negation_expression // Unary Prefix Right Associative
	#       						| sign_expression; // Next precedence
    def visitNegation_expression(self, ctx:ZCodeParser.Negation_expressionContext):
       #print("Negation Expression ", ctx.NOT(), ctx.sign_expression())
        if ctx.NOT():
            operand = self.visit(ctx.negation_expression())
            op = ctx.NOT().getText()
            return UnaryOp(op, operand)
        else:
            return self.visit(ctx.sign_expression())
        

    # sign_expression				: additive_operator sign_expression // Unary Prefix Right Associative
	#       						| parenthesis_expression; // Next precedence
    def visitSign_expression(self, ctx:ZCodeParser.Sign_expressionContext):
       #print("Sign Expression ", ctx.MINUS(), ctx.parenthesis_expression())
        if ctx.MINUS():
            operand = self.visit(ctx.sign_expression())
            op = ctx.MINUS().getText()
            return UnaryOp(op, operand)
        else:
            return self.visit(ctx.parenthesis_expression())

    # parenthesis_expression		: LPAREN expression RPAREN // Parenthesis
	#       						| operand; // Next precedence
    def visitParenthesis_expression(self, ctx:ZCodeParser.Parenthesis_expressionContext):
       #print("Parenthesis Expression ", ctx.expression(), ctx.operand())
        if ctx.expression():
            return self.visit(ctx.expression())
        else:
            return self.visit(ctx.operand())

    # operand						: literal 
	#	    		    			| function_call_expression 
	#		        				| IDENTIFIER 
	#					        	| array_literal;
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
       #print("Operand ", ctx.literal(), ctx.function_call_expression(), ctx.IDENTIFIER(), ctx.array_literal())
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.function_call_expression():
            return self.visit(ctx.function_call_expression())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.array_literal():
            return self.visit(ctx.array_literal())
        else :
            return None

    # array_literal 				: (function_call_statement | IDENTIFIER)? element_expression ; // Unary Postfix Left Associative
    # TODO : Check again
    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        arr = Expr
        value = self.visit(ctx.element_expression())

        if ctx.function_call_expression():
            arr = self.visit(ctx.function_call_expression())
            return ArrayCell(arr, value)
        elif ctx.IDENTIFIER():
            arr = Id(ctx.IDENTIFIER().getText())
            return ArrayCell(arr, value)
        else:
            return ArrayLiteral(value)
            
        
    # element_expression			: LBRACK index_operator RBRACK; 
    def visitElement_expression(self, ctx:ZCodeParser.Element_expressionContext):
        return self.visit(ctx.index_operator())

    # index_operator				: expression COMMA index_operator // Recursive
	#       						| expression;
    def visitIndex_operator(self, ctx:ZCodeParser.Index_operatorContext):
        if ctx.index_operator():
            return [self.visit(ctx.expression())] + self.visit(ctx.index_operator())
        else:
            return [self.visit(ctx.expression())]

    # relational_operator 		: LT | LE | GT | GE | EQUAL | NOT_EQUAL | STRING_EQUAL;
    def visitRelational_operator(self, ctx:ZCodeParser.Relational_operatorContext):
        if ctx.LT():
            return ctx.LT().getText()
        elif ctx.LE():
            return ctx.LE().getText()
        elif ctx.GT():
            return ctx.GT().getText()
        elif ctx.GE():
            return ctx.GE().getText()
        elif ctx.EQUAL():
            return ctx.EQUAL().getText()
        elif ctx.NOT_EQUAL():
            return ctx.NOT_EQUAL().getText()
        elif ctx.STRING_EQUAL():
            return ctx.STRING_EQUAL().getText()
        else :
            return None


    # additive_operator 			: PLUS | MINUS ;
    def visitAdditive_operator(self, ctx:ZCodeParser.Additive_operatorContext):
        if ctx.PLUS():
            return ctx.PLUS().getText()
        elif ctx.MINUS():
            return ctx.MINUS().getText()
        else :
            return None

    # multiplicative_operator		: MULTIPLY | DIVIDE | MOD ;
    def visitMultiplicative_operator(self, ctx:ZCodeParser.Multiplicative_operatorContext):
        if ctx.MULTIPLY():
            return ctx.MULTIPLY().getText()
        elif ctx.DIVIDE():
            return ctx.DIVIDE().getText()
        elif ctx.MOD():
            return ctx.MOD().getText()
        else :
            return None

    # logic_operator 				: AND | OR ;
    def visitLogic_operator(self, ctx:ZCodeParser.Logic_operatorContext):
        if ctx.AND():
            return ctx.AND().getText()
        elif ctx.OR():
            return ctx.OR().getText()
        else :
            return None

    # literal						: NUMBER_LIT | BOOLEAN_LIT | STRING_LIT;
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
       #print("Literal ", ctx.NUMBER_LIT(), ctx.BOOLEAN_LIT(), ctx.STRING_LIT())
        if ctx.NUMBER_LIT():
            return NumberLiteral(float(ctx.NUMBER_LIT().getText())) # NumLit(1.0) 
        elif ctx.BOOLEAN_LIT():
            return BooleanLiteral(ctx.BOOLEAN_LIT().getText() == "true")
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        else :
            return None

    # string_literal 				: STRING_LIT ;
    def visitString_literal(self, ctx:ZCodeParser.String_literalContext):
        return StringLiteral(ctx.STRING_LIT().getText())


    # number_literal 				: NUMBER_LIT ;
    def visitNumber_literal(self, ctx:ZCodeParser.Number_literalContext):
       #print("Number Literal ", ctx.NUMBER_LIT(), ctx.NUMBER_LIT().getText())
        return NumberLiteral(ctx.NUMBER_LIT().getText())


    # boolean_literal 			: BOOLEAN_LIT ;
    def visitBoolean_literal(self, ctx:ZCodeParser.Boolean_literalContext):
        return BooleanLiteral(ctx.BOOLEAN_LIT().getText())
