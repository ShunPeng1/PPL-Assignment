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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2$")
        buf.write("\u00e3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\7\3N\n\3\f\3\16\3Q\13\3\3\4\6\4T\n\4\r\4")
        buf.write("\16\4U\3\5\6\5Y\n\5\r\5\16\5Z\3\5\5\5^\n\5\3\5\7\5a\n")
        buf.write("\5\f\5\16\5d\13\5\3\5\3\5\5\5h\n\5\3\5\6\5k\n\5\r\5\16")
        buf.write("\5l\5\5o\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6z")
        buf.write("\n\6\3\7\3\7\7\7~\n\7\f\7\16\7\u0081\13\7\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\7\36\u00bf\n\36\f\36\16\36\u00c2\13\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\7\37\u00cb\n\37\f\37\16\37\u00ce")
        buf.write("\13\37\3\37\5\37\u00d1\n\37\3\37\3\37\3\37\3 \6 \u00d7")
        buf.write("\n \r \16 \u00d8\3 \3 \3!\3!\3!\3\"\3\"\3#\3#\3O\2$\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$\3\2\13\4\2\f")
        buf.write("\f\17\17\3\2\62;\4\2GGgg\4\2--//\3\2c|\4\2\62;c|\5\2\f")
        buf.write("\f\17\17$$\6\2\f\f\17\17$$))\5\2\13\f\17\17\"\"\2\u00f2")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\3G\3\2\2\2\5I\3\2\2\2")
        buf.write("\7S\3\2\2\2\tX\3\2\2\2\13y\3\2\2\2\r{\3\2\2\2\17\u0082")
        buf.write("\3\2\2\2\21\u0084\3\2\2\2\23\u0086\3\2\2\2\25\u0088\3")
        buf.write("\2\2\2\27\u008a\3\2\2\2\31\u008c\3\2\2\2\33\u008e\3\2")
        buf.write("\2\2\35\u0090\3\2\2\2\37\u0092\3\2\2\2!\u0094\3\2\2\2")
        buf.write("#\u0096\3\2\2\2%\u009a\3\2\2\2\'\u009e\3\2\2\2)\u00a1")
        buf.write("\3\2\2\2+\u00a3\3\2\2\2-\u00a6\3\2\2\2/\u00a9\3\2\2\2")
        buf.write("\61\u00ab\3\2\2\2\63\u00ae\3\2\2\2\65\u00b0\3\2\2\2\67")
        buf.write("\u00b3\3\2\2\29\u00b7\3\2\2\2;\u00ba\3\2\2\2=\u00c6\3")
        buf.write("\2\2\2?\u00d6\3\2\2\2A\u00dc\3\2\2\2C\u00df\3\2\2\2E\u00e1")
        buf.write("\3\2\2\2GH\5\t\5\2H\4\3\2\2\2IJ\7%\2\2JK\7%\2\2KO\3\2")
        buf.write("\2\2LN\13\2\2\2ML\3\2\2\2NQ\3\2\2\2OP\3\2\2\2OM\3\2\2")
        buf.write("\2P\6\3\2\2\2QO\3\2\2\2RT\t\2\2\2SR\3\2\2\2TU\3\2\2\2")
        buf.write("US\3\2\2\2UV\3\2\2\2V\b\3\2\2\2WY\t\3\2\2XW\3\2\2\2YZ")
        buf.write("\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[]\3\2\2\2\\^\7\60\2\2]\\")
        buf.write("\3\2\2\2]^\3\2\2\2^b\3\2\2\2_a\t\3\2\2`_\3\2\2\2ad\3\2")
        buf.write("\2\2b`\3\2\2\2bc\3\2\2\2cn\3\2\2\2db\3\2\2\2eg\t\4\2\2")
        buf.write("fh\t\5\2\2gf\3\2\2\2gh\3\2\2\2hj\3\2\2\2ik\t\3\2\2ji\3")
        buf.write("\2\2\2kl\3\2\2\2lj\3\2\2\2lm\3\2\2\2mo\3\2\2\2ne\3\2\2")
        buf.write("\2no\3\2\2\2o\n\3\2\2\2pq\7v\2\2qr\7t\2\2rs\7w\2\2sz\7")
        buf.write("g\2\2tu\7h\2\2uv\7c\2\2vw\7n\2\2wx\7u\2\2xz\7g\2\2yp\3")
        buf.write("\2\2\2yt\3\2\2\2z\f\3\2\2\2{\177\t\6\2\2|~\t\7\2\2}|\3")
        buf.write("\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080")
        buf.write("\16\3\2\2\2\u0081\177\3\2\2\2\u0082\u0083\7*\2\2\u0083")
        buf.write("\20\3\2\2\2\u0084\u0085\7+\2\2\u0085\22\3\2\2\2\u0086")
        buf.write("\u0087\7]\2\2\u0087\24\3\2\2\2\u0088\u0089\7_\2\2\u0089")
        buf.write("\26\3\2\2\2\u008a\u008b\7.\2\2\u008b\30\3\2\2\2\u008c")
        buf.write("\u008d\7-\2\2\u008d\32\3\2\2\2\u008e\u008f\7/\2\2\u008f")
        buf.write("\34\3\2\2\2\u0090\u0091\7,\2\2\u0091\36\3\2\2\2\u0092")
        buf.write("\u0093\7\61\2\2\u0093 \3\2\2\2\u0094\u0095\7\'\2\2\u0095")
        buf.write("\"\3\2\2\2\u0096\u0097\7p\2\2\u0097\u0098\7q\2\2\u0098")
        buf.write("\u0099\7v\2\2\u0099$\3\2\2\2\u009a\u009b\7c\2\2\u009b")
        buf.write("\u009c\7p\2\2\u009c\u009d\7f\2\2\u009d&\3\2\2\2\u009e")
        buf.write("\u009f\7q\2\2\u009f\u00a0\7t\2\2\u00a0(\3\2\2\2\u00a1")
        buf.write("\u00a2\7?\2\2\u00a2*\3\2\2\2\u00a3\u00a4\7>\2\2\u00a4")
        buf.write("\u00a5\7/\2\2\u00a5,\3\2\2\2\u00a6\u00a7\7#\2\2\u00a7")
        buf.write("\u00a8\7?\2\2\u00a8.\3\2\2\2\u00a9\u00aa\7>\2\2\u00aa")
        buf.write("\60\3\2\2\2\u00ab\u00ac\7>\2\2\u00ac\u00ad\7?\2\2\u00ad")
        buf.write("\62\3\2\2\2\u00ae\u00af\7@\2\2\u00af\64\3\2\2\2\u00b0")
        buf.write("\u00b1\7@\2\2\u00b1\u00b2\7?\2\2\u00b2\66\3\2\2\2\u00b3")
        buf.write("\u00b4\7\60\2\2\u00b4\u00b5\7\60\2\2\u00b5\u00b6\7\60")
        buf.write("\2\2\u00b68\3\2\2\2\u00b7\u00b8\7?\2\2\u00b8\u00b9\7?")
        buf.write("\2\2\u00b9:\3\2\2\2\u00ba\u00c0\7$\2\2\u00bb\u00bf\n\b")
        buf.write("\2\2\u00bc\u00bd\7^\2\2\u00bd\u00bf\13\2\2\2\u00be\u00bb")
        buf.write("\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2")
        buf.write("\u00c2\u00c0\3\2\2\2\u00c3\u00c4\7$\2\2\u00c4\u00c5\b")
        buf.write("\36\2\2\u00c5<\3\2\2\2\u00c6\u00cc\7$\2\2\u00c7\u00cb")
        buf.write("\n\t\2\2\u00c8\u00c9\7^\2\2\u00c9\u00cb\13\2\2\2\u00ca")
        buf.write("\u00c7\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00ce\3\2\2\2")
        buf.write("\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00d0\3")
        buf.write("\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d1\7\17\2\2\u00d0")
        buf.write("\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d2\u00d3\7\f\2\2\u00d3\u00d4\b\37\3\2\u00d4>\3\2\2")
        buf.write("\2\u00d5\u00d7\t\n\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00d8")
        buf.write("\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9")
        buf.write("\u00da\3\2\2\2\u00da\u00db\b \4\2\u00db@\3\2\2\2\u00dc")
        buf.write("\u00dd\13\2\2\2\u00dd\u00de\b!\5\2\u00deB\3\2\2\2\u00df")
        buf.write("\u00e0\13\2\2\2\u00e0D\3\2\2\2\u00e1\u00e2\13\2\2\2\u00e2")
        buf.write("F\3\2\2\2\23\2OUZ]bglny\177\u00be\u00c0\u00ca\u00cc\u00d0")
        buf.write("\u00d8\6\3\36\2\3\37\3\b\2\2\3!\4")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EXPRESSION = 1
    COMMENT = 2
    NEWLINE = 3
    NUMBER = 4
    BOOLEAN = 5
    IDENTIFIER = 6
    LPAREN = 7
    RPAREN = 8
    LBRACK = 9
    RBRACK = 10
    COMMA = 11
    PLUS = 12
    MINUS = 13
    MULTIPLY = 14
    DIVIDE = 15
    MOD = 16
    NOT = 17
    AND = 18
    OR = 19
    EQUAL = 20
    ASSIGN = 21
    NEQUAL = 22
    LT = 23
    LE = 24
    GT = 25
    GE = 26
    CONCATE = 27
    STRING_EQUAL = 28
    STRING = 29
    STRING_NEWLINE_ERROR = 30
    WS = 31
    ERROR_CHAR = 32
    UNCLOSE_STRING = 33
    ILLEGAL_ESCAPE = 34

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "','", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'not'", "'and'", "'or'", "'='", "'<-'", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'...'", "'=='" ]

    symbolicNames = [ "<INVALID>",
            "EXPRESSION", "COMMENT", "NEWLINE", "NUMBER", "BOOLEAN", "IDENTIFIER", 
            "LPAREN", "RPAREN", "LBRACK", "RBRACK", "COMMA", "PLUS", "MINUS", 
            "MULTIPLY", "DIVIDE", "MOD", "NOT", "AND", "OR", "EQUAL", "ASSIGN", 
            "NEQUAL", "LT", "LE", "GT", "GE", "CONCATE", "STRING_EQUAL", 
            "STRING", "STRING_NEWLINE_ERROR", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "EXPRESSION", "COMMENT", "NEWLINE", "NUMBER", "BOOLEAN", 
                  "IDENTIFIER", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
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
            actions[28] = self.STRING_action 
            actions[29] = self.STRING_NEWLINE_ERROR_action 
            actions[31] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                // Custom code to handle the string token
                // You can access the matched text with getText() method

     

    def STRING_NEWLINE_ERROR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                // Custom code to handle the error
                // You can print an error message or throw an exception
                throw new RuntimeException("Newline character found within a string");

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     


