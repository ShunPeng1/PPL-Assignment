# Generated from c:/Users/PC/Downloads/PPL/PPL Assignment/BTL4/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#declaration_list.
    def enterDeclaration_list(self, ctx:ZCodeParser.Declaration_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#declaration_list.
    def exitDeclaration_list(self, ctx:ZCodeParser.Declaration_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#declaration.
    def enterDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#declaration.
    def exitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#local_statement_single.
    def enterLocal_statement_single(self, ctx:ZCodeParser.Local_statement_singleContext):
        pass

    # Exit a parse tree produced by ZCodeParser#local_statement_single.
    def exitLocal_statement_single(self, ctx:ZCodeParser.Local_statement_singleContext):
        pass


    # Enter a parse tree produced by ZCodeParser#local_statement_list.
    def enterLocal_statement_list(self, ctx:ZCodeParser.Local_statement_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#local_statement_list.
    def exitLocal_statement_list(self, ctx:ZCodeParser.Local_statement_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#local_statement.
    def enterLocal_statement(self, ctx:ZCodeParser.Local_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#local_statement.
    def exitLocal_statement(self, ctx:ZCodeParser.Local_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#newline_list.
    def enterNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#newline_list.
    def exitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#newline.
    def enterNewline(self, ctx:ZCodeParser.NewlineContext):
        pass

    # Exit a parse tree produced by ZCodeParser#newline.
    def exitNewline(self, ctx:ZCodeParser.NewlineContext):
        pass


    # Enter a parse tree produced by ZCodeParser#block_statement.
    def enterBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#block_statement.
    def exitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#variable_declaration_statement.
    def enterVariable_declaration_statement(self, ctx:ZCodeParser.Variable_declaration_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#variable_declaration_statement.
    def exitVariable_declaration_statement(self, ctx:ZCodeParser.Variable_declaration_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#basic_variable_declaration.
    def enterBasic_variable_declaration(self, ctx:ZCodeParser.Basic_variable_declarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#basic_variable_declaration.
    def exitBasic_variable_declaration(self, ctx:ZCodeParser.Basic_variable_declarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#basic_type.
    def enterBasic_type(self, ctx:ZCodeParser.Basic_typeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#basic_type.
    def exitBasic_type(self, ctx:ZCodeParser.Basic_typeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_declaration.
    def enterArray_declaration(self, ctx:ZCodeParser.Array_declarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_declaration.
    def exitArray_declaration(self, ctx:ZCodeParser.Array_declarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_dimension.
    def enterArray_dimension(self, ctx:ZCodeParser.Array_dimensionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_dimension.
    def exitArray_dimension(self, ctx:ZCodeParser.Array_dimensionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_dimension_list.
    def enterArray_dimension_list(self, ctx:ZCodeParser.Array_dimension_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_dimension_list.
    def exitArray_dimension_list(self, ctx:ZCodeParser.Array_dimension_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignment_statement.
    def enterAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignment_statement.
    def exitAssignment_statement(self, ctx:ZCodeParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#function_declaration.
    def enterFunction_declaration(self, ctx:ZCodeParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#function_declaration.
    def exitFunction_declaration(self, ctx:ZCodeParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#function_body.
    def enterFunction_body(self, ctx:ZCodeParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#function_body.
    def exitFunction_body(self, ctx:ZCodeParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#return_statement.
    def enterReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#return_statement.
    def exitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#parameter_part_recursive.
    def enterParameter_part_recursive(self, ctx:ZCodeParser.Parameter_part_recursiveContext):
        pass

    # Exit a parse tree produced by ZCodeParser#parameter_part_recursive.
    def exitParameter_part_recursive(self, ctx:ZCodeParser.Parameter_part_recursiveContext):
        pass


    # Enter a parse tree produced by ZCodeParser#parameter_declaration.
    def enterParameter_declaration(self, ctx:ZCodeParser.Parameter_declarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#parameter_declaration.
    def exitParameter_declaration(self, ctx:ZCodeParser.Parameter_declarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#basic_parameter_declaration.
    def enterBasic_parameter_declaration(self, ctx:ZCodeParser.Basic_parameter_declarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#basic_parameter_declaration.
    def exitBasic_parameter_declaration(self, ctx:ZCodeParser.Basic_parameter_declarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_parameter_declaration.
    def enterArray_parameter_declaration(self, ctx:ZCodeParser.Array_parameter_declarationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_parameter_declaration.
    def exitArray_parameter_declaration(self, ctx:ZCodeParser.Array_parameter_declarationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#if_statement.
    def enterIf_statement(self, ctx:ZCodeParser.If_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#if_statement.
    def exitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elif_recursive_statement.
    def enterElif_recursive_statement(self, ctx:ZCodeParser.Elif_recursive_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elif_recursive_statement.
    def exitElif_recursive_statement(self, ctx:ZCodeParser.Elif_recursive_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elif_statement.
    def enterElif_statement(self, ctx:ZCodeParser.Elif_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elif_statement.
    def exitElif_statement(self, ctx:ZCodeParser.Elif_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#else_statement.
    def enterElse_statement(self, ctx:ZCodeParser.Else_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#else_statement.
    def exitElse_statement(self, ctx:ZCodeParser.Else_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#branch_condition.
    def enterBranch_condition(self, ctx:ZCodeParser.Branch_conditionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#branch_condition.
    def exitBranch_condition(self, ctx:ZCodeParser.Branch_conditionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#branch_body.
    def enterBranch_body(self, ctx:ZCodeParser.Branch_bodyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#branch_body.
    def exitBranch_body(self, ctx:ZCodeParser.Branch_bodyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#function_call_statement.
    def enterFunction_call_statement(self, ctx:ZCodeParser.Function_call_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#function_call_statement.
    def exitFunction_call_statement(self, ctx:ZCodeParser.Function_call_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#function_call_expression.
    def enterFunction_call_expression(self, ctx:ZCodeParser.Function_call_expressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#function_call_expression.
    def exitFunction_call_expression(self, ctx:ZCodeParser.Function_call_expressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#argument_part.
    def enterArgument_part(self, ctx:ZCodeParser.Argument_partContext):
        pass

    # Exit a parse tree produced by ZCodeParser#argument_part.
    def exitArgument_part(self, ctx:ZCodeParser.Argument_partContext):
        pass


    # Enter a parse tree produced by ZCodeParser#for_statement.
    def enterFor_statement(self, ctx:ZCodeParser.For_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#for_statement.
    def exitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#loop_body.
    def enterLoop_body(self, ctx:ZCodeParser.Loop_bodyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#loop_body.
    def exitLoop_body(self, ctx:ZCodeParser.Loop_bodyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#break_statement.
    def enterBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#break_statement.
    def exitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#continue_statement.
    def enterContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#continue_statement.
    def exitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression.
    def enterExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expression.
    def exitExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#string_expression.
    def enterString_expression(self, ctx:ZCodeParser.String_expressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#string_expression.
    def exitString_expression(self, ctx:ZCodeParser.String_expressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#relational_expression.
    def enterRelational_expression(self, ctx:ZCodeParser.Relational_expressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#relational_expression.
    def exitRelational_expression(self, ctx:ZCodeParser.Relational_expressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#logical_expression.
    def enterLogical_expression(self, ctx:ZCodeParser.Logical_expressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#logical_expression.
    def exitLogical_expression(self, ctx:ZCodeParser.Logical_expressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#adding_expression.
    def enterAdding_expression(self, ctx:ZCodeParser.Adding_expressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#adding_expression.
    def exitAdding_expression(self, ctx:ZCodeParser.Adding_expressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#multiplying_expression.
    def enterMultiplying_expression(self, ctx:ZCodeParser.Multiplying_expressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#multiplying_expression.
    def exitMultiplying_expression(self, ctx:ZCodeParser.Multiplying_expressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#negation_expression.
    def enterNegation_expression(self, ctx:ZCodeParser.Negation_expressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#negation_expression.
    def exitNegation_expression(self, ctx:ZCodeParser.Negation_expressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#sign_expression.
    def enterSign_expression(self, ctx:ZCodeParser.Sign_expressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#sign_expression.
    def exitSign_expression(self, ctx:ZCodeParser.Sign_expressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#parenthesis_expression.
    def enterParenthesis_expression(self, ctx:ZCodeParser.Parenthesis_expressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#parenthesis_expression.
    def exitParenthesis_expression(self, ctx:ZCodeParser.Parenthesis_expressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#operand.
    def enterOperand(self, ctx:ZCodeParser.OperandContext):
        pass

    # Exit a parse tree produced by ZCodeParser#operand.
    def exitOperand(self, ctx:ZCodeParser.OperandContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_literal.
    def enterArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_literal.
    def exitArray_literal(self, ctx:ZCodeParser.Array_literalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#element_expression.
    def enterElement_expression(self, ctx:ZCodeParser.Element_expressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#element_expression.
    def exitElement_expression(self, ctx:ZCodeParser.Element_expressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#index_operator.
    def enterIndex_operator(self, ctx:ZCodeParser.Index_operatorContext):
        pass

    # Exit a parse tree produced by ZCodeParser#index_operator.
    def exitIndex_operator(self, ctx:ZCodeParser.Index_operatorContext):
        pass


    # Enter a parse tree produced by ZCodeParser#relational_operator.
    def enterRelational_operator(self, ctx:ZCodeParser.Relational_operatorContext):
        pass

    # Exit a parse tree produced by ZCodeParser#relational_operator.
    def exitRelational_operator(self, ctx:ZCodeParser.Relational_operatorContext):
        pass


    # Enter a parse tree produced by ZCodeParser#additive_operator.
    def enterAdditive_operator(self, ctx:ZCodeParser.Additive_operatorContext):
        pass

    # Exit a parse tree produced by ZCodeParser#additive_operator.
    def exitAdditive_operator(self, ctx:ZCodeParser.Additive_operatorContext):
        pass


    # Enter a parse tree produced by ZCodeParser#multiplicative_operator.
    def enterMultiplicative_operator(self, ctx:ZCodeParser.Multiplicative_operatorContext):
        pass

    # Exit a parse tree produced by ZCodeParser#multiplicative_operator.
    def exitMultiplicative_operator(self, ctx:ZCodeParser.Multiplicative_operatorContext):
        pass


    # Enter a parse tree produced by ZCodeParser#logic_operator.
    def enterLogic_operator(self, ctx:ZCodeParser.Logic_operatorContext):
        pass

    # Exit a parse tree produced by ZCodeParser#logic_operator.
    def exitLogic_operator(self, ctx:ZCodeParser.Logic_operatorContext):
        pass


    # Enter a parse tree produced by ZCodeParser#literal.
    def enterLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass

    # Exit a parse tree produced by ZCodeParser#literal.
    def exitLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass


    # Enter a parse tree produced by ZCodeParser#string_literal.
    def enterString_literal(self, ctx:ZCodeParser.String_literalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#string_literal.
    def exitString_literal(self, ctx:ZCodeParser.String_literalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#number_literal.
    def enterNumber_literal(self, ctx:ZCodeParser.Number_literalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#number_literal.
    def exitNumber_literal(self, ctx:ZCodeParser.Number_literalContext):
        pass


    # Enter a parse tree produced by ZCodeParser#boolean_literal.
    def enterBoolean_literal(self, ctx:ZCodeParser.Boolean_literalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#boolean_literal.
    def exitBoolean_literal(self, ctx:ZCodeParser.Boolean_literalContext):
        pass



del ZCodeParser