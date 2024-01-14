# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2%")
        buf.write("\u00f2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\7\3R\n\3\f\3\16\3U\13\3\5\3")
        buf.write("W\n\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4_\n\4\f\4\16\4b\13\4")
        buf.write("\3\5\6\5e\n\5\r\5\16\5f\3\6\3\6\7\6k\n\6\f\6\16\6n\13")
        buf.write("\6\3\7\6\7q\n\7\r\7\16\7r\3\7\5\7v\n\7\3\7\7\7y\n\7\f")
        buf.write("\7\16\7|\13\7\3\7\3\7\5\7\u0080\n\7\3\7\6\7\u0083\n\7")
        buf.write("\r\7\16\7\u0084\5\7\u0087\n\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\5\b\u0092\n\b\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\7\37\u00d0")
        buf.write("\n\37\f\37\16\37\u00d3\13\37\3\37\3\37\3 \3 \3 \3 \7 ")
        buf.write("\u00db\n \f \16 \u00de\13 \3 \5 \u00e1\n \3 \3 \3!\6!")
        buf.write("\u00e6\n!\r!\16!\u00e7\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("`\2%\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%\3\2")
        buf.write("\13\4\2\f\f\17\17\3\2c|\4\2\62;c|\3\2\62;\4\2GGgg\4\2")
        buf.write("--//\5\2\f\f\17\17$$\6\2\f\f\17\17$$))\5\2\13\f\17\17")
        buf.write("\"\"\2\u0103\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\3I\3\2\2\2\5K\3\2\2\2\7Z\3\2\2\2\td\3\2\2\2\13h\3\2")
        buf.write("\2\2\rp\3\2\2\2\17\u0091\3\2\2\2\21\u0093\3\2\2\2\23\u0095")
        buf.write("\3\2\2\2\25\u0097\3\2\2\2\27\u0099\3\2\2\2\31\u009b\3")
        buf.write("\2\2\2\33\u009d\3\2\2\2\35\u009f\3\2\2\2\37\u00a1\3\2")
        buf.write("\2\2!\u00a3\3\2\2\2#\u00a5\3\2\2\2%\u00a7\3\2\2\2\'\u00ab")
        buf.write("\3\2\2\2)\u00af\3\2\2\2+\u00b2\3\2\2\2-\u00b4\3\2\2\2")
        buf.write("/\u00b7\3\2\2\2\61\u00ba\3\2\2\2\63\u00bc\3\2\2\2\65\u00bf")
        buf.write("\3\2\2\2\67\u00c1\3\2\2\29\u00c4\3\2\2\2;\u00c8\3\2\2")
        buf.write("\2=\u00cb\3\2\2\2?\u00d6\3\2\2\2A\u00e5\3\2\2\2C\u00eb")
        buf.write("\3\2\2\2E\u00ee\3\2\2\2G\u00f0\3\2\2\2IJ\5\r\7\2J\4\3")
        buf.write("\2\2\2KL\5\13\6\2LV\5\21\t\2MS\5\3\2\2NO\5\31\r\2OP\5")
        buf.write("\3\2\2PR\3\2\2\2QN\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2")
        buf.write("\2TW\3\2\2\2US\3\2\2\2VM\3\2\2\2VW\3\2\2\2WX\3\2\2\2X")
        buf.write("Y\5\23\n\2Y\6\3\2\2\2Z[\7%\2\2[\\\7%\2\2\\`\3\2\2\2]_")
        buf.write("\13\2\2\2^]\3\2\2\2_b\3\2\2\2`a\3\2\2\2`^\3\2\2\2a\b\3")
        buf.write("\2\2\2b`\3\2\2\2ce\t\2\2\2dc\3\2\2\2ef\3\2\2\2fd\3\2\2")
        buf.write("\2fg\3\2\2\2g\n\3\2\2\2hl\t\3\2\2ik\t\4\2\2ji\3\2\2\2")
        buf.write("kn\3\2\2\2lj\3\2\2\2lm\3\2\2\2m\f\3\2\2\2nl\3\2\2\2oq")
        buf.write("\t\5\2\2po\3\2\2\2qr\3\2\2\2rp\3\2\2\2rs\3\2\2\2su\3\2")
        buf.write("\2\2tv\7\60\2\2ut\3\2\2\2uv\3\2\2\2vz\3\2\2\2wy\t\5\2")
        buf.write("\2xw\3\2\2\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{\u0086\3\2")
        buf.write("\2\2|z\3\2\2\2}\177\t\6\2\2~\u0080\t\7\2\2\177~\3\2\2")
        buf.write("\2\177\u0080\3\2\2\2\u0080\u0082\3\2\2\2\u0081\u0083\t")
        buf.write("\5\2\2\u0082\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0082")
        buf.write("\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0087\3\2\2\2\u0086")
        buf.write("}\3\2\2\2\u0086\u0087\3\2\2\2\u0087\16\3\2\2\2\u0088\u0089")
        buf.write("\7v\2\2\u0089\u008a\7t\2\2\u008a\u008b\7w\2\2\u008b\u0092")
        buf.write("\7g\2\2\u008c\u008d\7h\2\2\u008d\u008e\7c\2\2\u008e\u008f")
        buf.write("\7n\2\2\u008f\u0090\7u\2\2\u0090\u0092\7g\2\2\u0091\u0088")
        buf.write("\3\2\2\2\u0091\u008c\3\2\2\2\u0092\20\3\2\2\2\u0093\u0094")
        buf.write("\7*\2\2\u0094\22\3\2\2\2\u0095\u0096\7+\2\2\u0096\24\3")
        buf.write("\2\2\2\u0097\u0098\7]\2\2\u0098\26\3\2\2\2\u0099\u009a")
        buf.write("\7_\2\2\u009a\30\3\2\2\2\u009b\u009c\7.\2\2\u009c\32\3")
        buf.write("\2\2\2\u009d\u009e\7-\2\2\u009e\34\3\2\2\2\u009f\u00a0")
        buf.write("\7/\2\2\u00a0\36\3\2\2\2\u00a1\u00a2\7,\2\2\u00a2 \3\2")
        buf.write("\2\2\u00a3\u00a4\7\61\2\2\u00a4\"\3\2\2\2\u00a5\u00a6")
        buf.write("\7\'\2\2\u00a6$\3\2\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9")
        buf.write("\7q\2\2\u00a9\u00aa\7v\2\2\u00aa&\3\2\2\2\u00ab\u00ac")
        buf.write("\7c\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae\7f\2\2\u00ae(\3")
        buf.write("\2\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1\7t\2\2\u00b1*\3")
        buf.write("\2\2\2\u00b2\u00b3\7?\2\2\u00b3,\3\2\2\2\u00b4\u00b5\7")
        buf.write(">\2\2\u00b5\u00b6\7/\2\2\u00b6.\3\2\2\2\u00b7\u00b8\7")
        buf.write("#\2\2\u00b8\u00b9\7?\2\2\u00b9\60\3\2\2\2\u00ba\u00bb")
        buf.write("\7>\2\2\u00bb\62\3\2\2\2\u00bc\u00bd\7>\2\2\u00bd\u00be")
        buf.write("\7?\2\2\u00be\64\3\2\2\2\u00bf\u00c0\7@\2\2\u00c0\66\3")
        buf.write("\2\2\2\u00c1\u00c2\7@\2\2\u00c2\u00c3\7?\2\2\u00c38\3")
        buf.write("\2\2\2\u00c4\u00c5\7\60\2\2\u00c5\u00c6\7\60\2\2\u00c6")
        buf.write("\u00c7\7\60\2\2\u00c7:\3\2\2\2\u00c8\u00c9\7?\2\2\u00c9")
        buf.write("\u00ca\7?\2\2\u00ca<\3\2\2\2\u00cb\u00d1\7$\2\2\u00cc")
        buf.write("\u00d0\n\b\2\2\u00cd\u00ce\7^\2\2\u00ce\u00d0\13\2\2\2")
        buf.write("\u00cf\u00cc\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d3\3")
        buf.write("\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d4")
        buf.write("\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d5\7$\2\2\u00d5")
        buf.write(">\3\2\2\2\u00d6\u00dc\7$\2\2\u00d7\u00db\n\t\2\2\u00d8")
        buf.write("\u00d9\7^\2\2\u00d9\u00db\13\2\2\2\u00da\u00d7\3\2\2\2")
        buf.write("\u00da\u00d8\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3")
        buf.write("\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00df\u00e1\7\17\2\2\u00e0\u00df\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\7\f\2\2")
        buf.write("\u00e3@\3\2\2\2\u00e4\u00e6\t\n\2\2\u00e5\u00e4\3\2\2")
        buf.write("\2\u00e6\u00e7\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8")
        buf.write("\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\b!\2\2\u00ea")
        buf.write("B\3\2\2\2\u00eb\u00ec\13\2\2\2\u00ec\u00ed\b\"\3\2\u00ed")
        buf.write("D\3\2\2\2\u00ee\u00ef\13\2\2\2\u00efF\3\2\2\2\u00f0\u00f1")
        buf.write("\13\2\2\2\u00f1H\3\2\2\2\25\2SV`flruz\177\u0084\u0086")
        buf.write("\u0091\u00cf\u00d1\u00da\u00dc\u00e0\u00e7\4\b\2\2\3\"")
        buf.write("\2")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EXPRESSION = 1
    FUNCTION = 2
    COMMENT = 3
    NEWLINE = 4
    IDENTIFIER = 5
    NUMBER = 6
    BOOLEAN = 7
    LPAREN = 8
    RPAREN = 9
    LBRACK = 10
    RBRACK = 11
    COMMA = 12
    PLUS = 13
    MINUS = 14
    MULTIPLY = 15
    DIVIDE = 16
    MOD = 17
    NOT = 18
    AND = 19
    OR = 20
    EQUAL = 21
    ASSIGN = 22
    NEQUAL = 23
    LT = 24
    LE = 25
    GT = 26
    GE = 27
    CONCATE = 28
    STRING_EQUAL = 29
    STRING = 30
    STRING_NEWLINE_ERROR = 31
    WS = 32
    ERROR_CHAR = 33
    UNCLOSE_STRING = 34
    ILLEGAL_ESCAPE = 35

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "','", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'not'", "'and'", "'or'", "'='", "'<-'", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'...'", "'=='" ]

    symbolicNames = [ "<INVALID>",
            "EXPRESSION", "FUNCTION", "COMMENT", "NEWLINE", "IDENTIFIER", 
            "NUMBER", "BOOLEAN", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
            "COMMA", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MOD", "NOT", 
            "AND", "OR", "EQUAL", "ASSIGN", "NEQUAL", "LT", "LE", "GT", 
            "GE", "CONCATE", "STRING_EQUAL", "STRING", "STRING_NEWLINE_ERROR", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "EXPRESSION", "FUNCTION", "COMMENT", "NEWLINE", "IDENTIFIER", 
                  "NUMBER", "BOOLEAN", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
                  "COMMA", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MOD", 
                  "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NEQUAL", "LT", 
                  "LE", "GT", "GE", "CONCATE", "STRING_EQUAL", "STRING", 
                  "STRING_NEWLINE_ERROR", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[32] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


