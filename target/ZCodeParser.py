# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63")
        buf.write("8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\7\3\36\n\3\f\3\16\3!\13\3\5\3#\n\3\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\5\4\2\27\27")
        buf.write("\61\61\3\2).\3\2\30\31\2\63\2\25\3\2\2\2\4\30\3\2\2\2")
        buf.write("\6&\3\2\2\2\b(\3\2\2\2\n,\3\2\2\2\f\63\3\2\2\2\16\65\3")
        buf.write("\2\2\2\20\21\5\6\4\2\21\22\7\t\2\2\22\24\3\2\2\2\23\20")
        buf.write("\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26")
        buf.write("\3\3\2\2\2\27\25\3\2\2\2\30\31\7\26\2\2\31\"\7\34\2\2")
        buf.write("\32\37\5\6\4\2\33\34\7 \2\2\34\36\5\6\4\2\35\33\3\2\2")
        buf.write("\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 #\3\2\2\2!\37")
        buf.write("\3\2\2\2\"\32\3\2\2\2\"#\3\2\2\2#$\3\2\2\2$%\7\35\2\2")
        buf.write("%\5\3\2\2\2&\'\t\2\2\2\'\7\3\2\2\2()\5\6\4\2)*\5\f\7\2")
        buf.write("*+\5\6\4\2+\t\3\2\2\2,-\7\16\2\2-.\5\6\4\2./\5\f\7\2/")
        buf.write("\60\5\6\4\2\60\61\7\r\2\2\61\62\5\16\b\2\62\13\3\2\2\2")
        buf.write("\63\64\t\3\2\2\64\r\3\2\2\2\65\66\t\4\2\2\66\17\3\2\2")
        buf.write("\2\5\25\37\"")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'number'", "'bool'", "'string'", "'var'", 
                     "'dynamic'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'begin'", "'end'", "'return'", "'if'", "'else'", "'elif'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "<INVALID>", "<INVALID>", "'true'", "'false'", "<INVALID>", 
                     "'<-'", "'('", "')'", "'['", "']'", "','", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", "'='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'...'", "'=='" ]

    symbolicNames = [ "<INVALID>", "NUMBER_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", 
                      "VAR", "DYNAMIC", "COMMENT", "NEWLINE", "WHITESPACE", 
                      "BEGIN", "END", "RETURN", "IF", "ELSE", "ELIF", "FOR", 
                      "UNTIL", "BY", "BREAK", "CONTINUE", "IDENTIFIER", 
                      "NUMBER_LIT", "TRUE", "FALSE", "STRING_LIT", "ASSIGNMENT", 
                      "LPAREN", "RPAREN", "LBRACK", "RBRACK", "COMMA", "PLUS", 
                      "MINUS", "MULTIPLY", "DIVIDE", "MOD", "NOT", "AND", 
                      "OR", "EQUAL", "NEQUAL", "LT", "LE", "GT", "GE", "CONCATE", 
                      "STRING_EQUAL", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_function = 1
    RULE_expression = 2
    RULE_boolean_expression = 3
    RULE_if_statement = 4
    RULE_relational_operator = 5
    RULE_boolean_value = 6

    ruleNames =  [ "program", "function", "expression", "boolean_expression", 
                   "if_statement", "relational_operator", "boolean_value" ]

    EOF = Token.EOF
    NUMBER_TYPE=1
    BOOLEAN_TYPE=2
    STRING_TYPE=3
    VAR=4
    DYNAMIC=5
    COMMENT=6
    NEWLINE=7
    WHITESPACE=8
    BEGIN=9
    END=10
    RETURN=11
    IF=12
    ELSE=13
    ELIF=14
    FOR=15
    UNTIL=16
    BY=17
    BREAK=18
    CONTINUE=19
    IDENTIFIER=20
    NUMBER_LIT=21
    TRUE=22
    FALSE=23
    STRING_LIT=24
    ASSIGNMENT=25
    LPAREN=26
    RPAREN=27
    LBRACK=28
    RBRACK=29
    COMMA=30
    PLUS=31
    MINUS=32
    MULTIPLY=33
    DIVIDE=34
    MOD=35
    NOT=36
    AND=37
    OR=38
    EQUAL=39
    NEQUAL=40
    LT=41
    LE=42
    GT=43
    GE=44
    CONCATE=45
    STRING_EQUAL=46
    ERROR_CHAR=47
    UNCLOSE_STRING=48
    ILLEGAL_ESCAPE=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NUMBER_LIT or _la==ZCodeParser.ERROR_CHAR:
                self.state = 14
                self.expression()
                self.state = 15
                self.match(ZCodeParser.NEWLINE)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMA)
            else:
                return self.getToken(ZCodeParser.COMMA, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 23
            self.match(ZCodeParser.LPAREN)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NUMBER_LIT or _la==ZCodeParser.ERROR_CHAR:
                self.state = 24
                self.expression()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.COMMA:
                    self.state = 25
                    self.match(ZCodeParser.COMMA)
                    self.state = 26
                    self.expression()
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 34
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def ERROR_CHAR(self):
            return self.getToken(ZCodeParser.ERROR_CHAR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.NUMBER_LIT or _la==ZCodeParser.ERROR_CHAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def relational_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Relational_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_boolean_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_expression" ):
                return visitor.visitBoolean_expression(self)
            else:
                return visitor.visitChildren(self)




    def boolean_expression(self):

        localctx = ZCodeParser.Boolean_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_boolean_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.expression()
            self.state = 39
            self.relational_operator()
            self.state = 40
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def relational_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Relational_operatorContext,0)


        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def boolean_value(self):
            return self.getTypedRuleContext(ZCodeParser.Boolean_valueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(ZCodeParser.IF)
            self.state = 43
            self.expression()
            self.state = 44
            self.relational_operator()
            self.state = 45
            self.expression()
            self.state = 46
            self.match(ZCodeParser.RETURN)
            self.state = 47
            self.boolean_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def LE(self):
            return self.getToken(ZCodeParser.LE, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def GE(self):
            return self.getToken(ZCodeParser.GE, 0)

        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def NEQUAL(self):
            return self.getToken(ZCodeParser.NEQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relational_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_operator" ):
                return visitor.visitRelational_operator(self)
            else:
                return visitor.visitChildren(self)




    def relational_operator(self):

        localctx = ZCodeParser.Relational_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NEQUAL) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_boolean_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_value" ):
                return visitor.visitBoolean_value(self)
            else:
                return visitor.visitChildren(self)




    def boolean_value(self):

        localctx = ZCodeParser.Boolean_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_boolean_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.TRUE or _la==ZCodeParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





