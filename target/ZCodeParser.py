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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3$")
        buf.write("\f\4\2\t\2\3\2\3\2\7\2\7\n\2\f\2\16\2\n\13\2\3\2\2\2\3")
        buf.write("\2\2\2\2\13\2\b\3\2\2\2\4\5\7\3\2\2\5\7\7\5\2\2\6\4\3")
        buf.write("\2\2\2\7\n\3\2\2\2\b\6\3\2\2\2\b\t\3\2\2\2\t\3\3\2\2\2")
        buf.write("\n\b\3\2\2\2\3\b")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'", "','", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'not'", "'and'", "'or'", "'='", "'<-'", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'...'", "'=='" ]

    symbolicNames = [ "<INVALID>", "EXPRESSION", "COMMENT", "NEWLINE", "NUMBER", 
                      "BOOLEAN", "IDENTIFIER", "LPAREN", "RPAREN", "LBRACK", 
                      "RBRACK", "COMMA", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                      "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NEQUAL", 
                      "LT", "LE", "GT", "GE", "CONCATE", "STRING_EQUAL", 
                      "STRING", "STRING_NEWLINE_ERROR", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    EXPRESSION=1
    COMMENT=2
    NEWLINE=3
    NUMBER=4
    BOOLEAN=5
    IDENTIFIER=6
    LPAREN=7
    RPAREN=8
    LBRACK=9
    RBRACK=10
    COMMA=11
    PLUS=12
    MINUS=13
    MULTIPLY=14
    DIVIDE=15
    MOD=16
    NOT=17
    AND=18
    OR=19
    EQUAL=20
    ASSIGN=21
    NEQUAL=22
    LT=23
    LE=24
    GT=25
    GE=26
    CONCATE=27
    STRING_EQUAL=28
    STRING=29
    STRING_NEWLINE_ERROR=30
    WS=31
    ERROR_CHAR=32
    UNCLOSE_STRING=33
    ILLEGAL_ESCAPE=34

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

        def EXPRESSION(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.EXPRESSION)
            else:
                return self.getToken(ZCodeParser.EXPRESSION, i)

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
            self.state = 6
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.EXPRESSION:
                self.state = 2
                self.match(ZCodeParser.EXPRESSION)
                self.state = 3
                self.match(ZCodeParser.NEWLINE)
                self.state = 8
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





