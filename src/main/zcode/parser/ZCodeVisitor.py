# Generated from ./main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declaration_list.
    def visitDeclaration_list(self, ctx:ZCodeParser.Declaration_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declaration.
    def visitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#local_statement_single.
    def visitLocal_statement_single(self, ctx:ZCodeParser.Local_statement_singleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#local_statement_multiple.
    def visitLocal_statement_multiple(self, ctx:ZCodeParser.Local_statement_multipleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#local_statement_list.
    def visitLocal_statement_list(self, ctx:ZCodeParser.Local_statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#local_statement.
    def visitLocal_statement(self, ctx:ZCodeParser.Local_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ignore_statement_list_inline.
    def visitIgnore_statement_list_inline(self, ctx:ZCodeParser.Ignore_statement_list_inlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ignore_statement_list.
    def visitIgnore_statement_list(self, ctx:ZCodeParser.Ignore_statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ignore_statement.
    def visitIgnore_statement(self, ctx:ZCodeParser.Ignore_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#comment_statement.
    def visitComment_statement(self, ctx:ZCodeParser.Comment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_statement.
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variable_declaration_statement.
    def visitVariable_declaration_statement(self, ctx:ZCodeParser.Variable_declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#basic_variable_declaration.
    def visitBasic_variable_declaration(self, ctx:ZCodeParser.Basic_variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#basic_type.
    def visitBasic_type(self, ctx:ZCodeParser.Basic_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_declaration.
    def visitArray_declaration(self, ctx:ZCodeParser.Array_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_dimension.
    def visitArray_dimension(self, ctx:ZCodeParser.Array_dimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_dimension_list.
    def visitArray_dimension_list(self, ctx:ZCodeParser.Array_dimension_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_value.
    def visitArray_value(self, ctx:ZCodeParser.Array_valueContext):
        return self.visitChildren(ctx)


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


    # Visit a parse tree produced by ZCodeParser#element_expression.
    def visitElement_expression(self, ctx:ZCodeParser.Element_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_expression.
    def visitIndex_expression(self, ctx:ZCodeParser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parenthesis_expression.
    def visitParenthesis_expression(self, ctx:ZCodeParser.Parenthesis_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operand.
    def visitOperand(self, ctx:ZCodeParser.OperandContext):
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



del ZCodeParser