from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):

        
    
    # program						: newline_list? declaration_list newline_list? EOF;
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.declaration_list()))

    
    # declaration_list			: declaration declaration_list // Recursive
	#						    | declaration; // At least one declaration
    def visitDeclaration_list(self, ctx:ZCodeParser.Declaration_listContext):
        if ctx.declaration_list():
            
            return [self.visit(ctx.declaration())] + self.visit(ctx.declaration_list())
        else:
            return [self.visit(ctx.declaration())]
        
        

    # declaration					: function_declaration_statement newline_list?
    #   							| variable_declaration_statement newline_list;     
    def visitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        if ctx.function_declaration_statement():
            return self.visit(ctx.function_declaration_statement())
        elif ctx.variable_declaration_statement():
            return self.visit(ctx.variable_declaration_statement())
        else :
            return None
        
        

    
    # local_statement_single		: newline_list? local_statement newline_list?;
    def visitLocal_statement_single(self, ctx:ZCodeParser.Local_statement_singleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#local_statement_list.
    def visitLocal_statement_list(self, ctx:ZCodeParser.Local_statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#local_statement.
    def visitLocal_statement(self, ctx:ZCodeParser.Local_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_list.
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline.
    def visitNewline(self, ctx:ZCodeParser.NewlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_statement.
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return self.visitChildren(ctx)


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
        
        return VarDecl(id, type, None, expression)
        

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


    # array_declaration			: basic_type IDENTIFIER array_dimension (ASSIGN array_value)?;
    def visitArray_declaration(self, ctx:ZCodeParser.Array_declarationContext):
        type = self.visit(ctx.basic_type())
        id = Id(ctx.IDENTIFIER().getText())
        dimension = self.visit(ctx.array_dimension())

        arrayType = ArrayType(dimension, type)
        
        value = self.visit(ctx.array_value()) if ctx.array_value() else None
        
        return VarDecl(id, arrayType, None, value)
        

    # array_dimension 			: LBRACK array_dimension_list RBRACK;
    def visitArray_dimension(self, ctx:ZCodeParser.Array_dimensionContext):
        return self.visit(ctx.array_dimension_list())
        

    # array_dimension_list 		: number_literal COMMA array_dimension_list // Recursive
	#   						| number_literal;
    def visitArray_dimension_list(self, ctx:ZCodeParser.Array_dimension_listContext):
        if ctx.array_dimension_list():
            return [self.visit(ctx.number_literal())] + self.visit(ctx.array_dimension_list())
        else:
            return [self.visit(ctx.number_literal())]


    # array_value				: LBRACK array_value_expression_list RBRACK
	#				    		| expression ;
    def visitArray_value(self, ctx:ZCodeParser.Array_valueContext):
        return self.visitChildren(ctx) ## TODO


    # Visit a parse tree produced by ZCodeParser#array_value_expression_list.
    def visitArray_value_expression_list(self, ctx:ZCodeParser.Array_value_expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignment_statement.
    def visitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#basic_variable_assignment.
    def visitBasic_variable_assignment(self, ctx:ZCodeParser.Basic_variable_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_assignment.
    def visitArray_assignment(self, ctx:ZCodeParser.Array_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_declaration_statement.
    def visitFunction_declaration_statement(self, ctx:ZCodeParser.Function_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_body.
    def visitFunction_body(self, ctx:ZCodeParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_statement.
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter_part_recursive.
    def visitParameter_part_recursive(self, ctx:ZCodeParser.Parameter_part_recursiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter_declaration_statement.
    def visitParameter_declaration_statement(self, ctx:ZCodeParser.Parameter_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#basic_parameter_declaration.
    def visitBasic_parameter_declaration(self, ctx:ZCodeParser.Basic_parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_parameter_declaration.
    def visitArray_parameter_declaration(self, ctx:ZCodeParser.Array_parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_statement.
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_recursive_statement.
    def visitElif_recursive_statement(self, ctx:ZCodeParser.Elif_recursive_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_statement.
    def visitElif_statement(self, ctx:ZCodeParser.Elif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_statement.
    def visitElse_statement(self, ctx:ZCodeParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#branch_condition.
    def visitBranch_condition(self, ctx:ZCodeParser.Branch_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#branch_body.
    def visitBranch_body(self, ctx:ZCodeParser.Branch_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_call_statement.
    def visitFunction_call_statement(self, ctx:ZCodeParser.Function_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argument_part.
    def visitArgument_part(self, ctx:ZCodeParser.Argument_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_statement.
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#loop_body.
    def visitLoop_body(self, ctx:ZCodeParser.Loop_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_statement.
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_statement.
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#string_expression.
    def visitString_expression(self, ctx:ZCodeParser.String_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relational_expression.
    def visitRelational_expression(self, ctx:ZCodeParser.Relational_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logical_expression.
    def visitLogical_expression(self, ctx:ZCodeParser.Logical_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#adding_expression.
    def visitAdding_expression(self, ctx:ZCodeParser.Adding_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multiplying_expression.
    def visitMultiplying_expression(self, ctx:ZCodeParser.Multiplying_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#negation_expression.
    def visitNegation_expression(self, ctx:ZCodeParser.Negation_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sign_expression.
    def visitSign_expression(self, ctx:ZCodeParser.Sign_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parenthesis_expression.
    def visitParenthesis_expression(self, ctx:ZCodeParser.Parenthesis_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_literal.
    def visitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_access.
    def visitArray_access(self, ctx:ZCodeParser.Array_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_index_access.
    def visitArray_index_access(self, ctx:ZCodeParser.Array_index_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relational_operator.
    def visitRelational_operator(self, ctx:ZCodeParser.Relational_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#additive_operator.
    def visitAdditive_operator(self, ctx:ZCodeParser.Additive_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multiplicative_operator.
    def visitMultiplicative_operator(self, ctx:ZCodeParser.Multiplicative_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logic_operator.
    def visitLogic_operator(self, ctx:ZCodeParser.Logic_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#string_literal.
    def visitString_literal(self, ctx:ZCodeParser.String_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#number_literal.
    def visitNumber_literal(self, ctx:ZCodeParser.Number_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#boolean_literal.
    def visitBoolean_literal(self, ctx:ZCodeParser.Boolean_literalContext):
        return self.visitChildren(ctx)
    
