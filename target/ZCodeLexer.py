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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0172\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7\u008f")
        buf.write("\n\7\f\7\16\7\u0092\13\7\3\b\6\b\u0095\n\b\r\b\16\b\u0096")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\t\u00a0\n\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\7\25\u00de\n\25\f\25\16\25\u00e1\13\25\3\26\3\26\5\26")
        buf.write("\u00e5\n\26\3\26\5\26\u00e8\n\26\3\27\6\27\u00eb\n\27")
        buf.write("\r\27\16\27\u00ec\3\30\3\30\7\30\u00f1\n\30\f\30\16\30")
        buf.write("\u00f4\13\30\3\31\3\31\5\31\u00f8\n\31\3\31\6\31\u00fb")
        buf.write("\n\31\r\31\16\31\u00fc\3\32\3\32\3\32\3\32\3\32\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\7\34\u0110\n\34\f\34\16\34\u0113\13\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\7\64\u015a\n")
        buf.write("\64\f\64\16\64\u015d\13\64\3\64\5\64\u0160\n\64\3\64\3")
        buf.write("\64\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u016a\n\65\f\65")
        buf.write("\16\65\u016d\13\65\3\65\3\65\3\65\3\65\2\2\66\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\2/\2\61\2\63\30")
        buf.write("\65\31\67\329\33;\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U")
        buf.write(")W*Y+[,]-_.a/c\60e\61g\62i\63\3\2\17\4\2\f\f\16\17\5\2")
        buf.write("\n\f\16\17\"\"\4\2\f\f\17\17\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\3\2\62;\4\2GGgg\4\2--//\7\2\f\f\17\17$$))^^\t\2))^^")
        buf.write("ddhhppttvv\5\2$$))^^\3\3$$\6\2\f\f\17\17$$))\2\u0183\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2\63\3\2\2")
        buf.write("\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=")
        buf.write("\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2")
        buf.write("G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2")
        buf.write("\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2")
        buf.write("\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2")
        buf.write("\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\3k\3\2\2\2\5r\3")
        buf.write("\2\2\2\7w\3\2\2\2\t~\3\2\2\2\13\u0082\3\2\2\2\r\u008a")
        buf.write("\3\2\2\2\17\u0094\3\2\2\2\21\u009f\3\2\2\2\23\u00a1\3")
        buf.write("\2\2\2\25\u00a7\3\2\2\2\27\u00ab\3\2\2\2\31\u00b2\3\2")
        buf.write("\2\2\33\u00b5\3\2\2\2\35\u00ba\3\2\2\2\37\u00bf\3\2\2")
        buf.write("\2!\u00c3\3\2\2\2#\u00c9\3\2\2\2%\u00cc\3\2\2\2\'\u00d2")
        buf.write("\3\2\2\2)\u00db\3\2\2\2+\u00e2\3\2\2\2-\u00ea\3\2\2\2")
        buf.write("/\u00ee\3\2\2\2\61\u00f5\3\2\2\2\63\u00fe\3\2\2\2\65\u0103")
        buf.write("\3\2\2\2\67\u0109\3\2\2\29\u0117\3\2\2\2;\u011a\3\2\2")
        buf.write("\2=\u011c\3\2\2\2?\u011e\3\2\2\2A\u0120\3\2\2\2C\u0122")
        buf.write("\3\2\2\2E\u0124\3\2\2\2G\u0126\3\2\2\2I\u0128\3\2\2\2")
        buf.write("K\u012a\3\2\2\2M\u012c\3\2\2\2O\u012e\3\2\2\2Q\u0132\3")
        buf.write("\2\2\2S\u0136\3\2\2\2U\u0139\3\2\2\2W\u013b\3\2\2\2Y\u013e")
        buf.write("\3\2\2\2[\u0140\3\2\2\2]\u0143\3\2\2\2_\u0145\3\2\2\2")
        buf.write("a\u0148\3\2\2\2c\u014c\3\2\2\2e\u014f\3\2\2\2g\u0152\3")
        buf.write("\2\2\2i\u0163\3\2\2\2kl\7p\2\2lm\7w\2\2mn\7o\2\2no\7d")
        buf.write("\2\2op\7g\2\2pq\7t\2\2q\4\3\2\2\2rs\7d\2\2st\7q\2\2tu")
        buf.write("\7q\2\2uv\7n\2\2v\6\3\2\2\2wx\7u\2\2xy\7v\2\2yz\7t\2\2")
        buf.write("z{\7k\2\2{|\7p\2\2|}\7i\2\2}\b\3\2\2\2~\177\7x\2\2\177")
        buf.write("\u0080\7c\2\2\u0080\u0081\7t\2\2\u0081\n\3\2\2\2\u0082")
        buf.write("\u0083\7f\2\2\u0083\u0084\7{\2\2\u0084\u0085\7p\2\2\u0085")
        buf.write("\u0086\7c\2\2\u0086\u0087\7o\2\2\u0087\u0088\7k\2\2\u0088")
        buf.write("\u0089\7e\2\2\u0089\f\3\2\2\2\u008a\u008b\7%\2\2\u008b")
        buf.write("\u008c\7%\2\2\u008c\u0090\3\2\2\2\u008d\u008f\n\2\2\2")
        buf.write("\u008e\u008d\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3")
        buf.write("\2\2\2\u0090\u0091\3\2\2\2\u0091\16\3\2\2\2\u0092\u0090")
        buf.write("\3\2\2\2\u0093\u0095\t\3\2\2\u0094\u0093\3\2\2\2\u0095")
        buf.write("\u0096\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\u0098\3\2\2\2\u0098\u0099\b\b\2\2\u0099\20\3\2")
        buf.write("\2\2\u009a\u009b\7\17\2\2\u009b\u00a0\7\f\2\2\u009c\u009d")
        buf.write("\7\f\2\2\u009d\u00a0\7\17\2\2\u009e\u00a0\t\4\2\2\u009f")
        buf.write("\u009a\3\2\2\2\u009f\u009c\3\2\2\2\u009f\u009e\3\2\2\2")
        buf.write("\u00a0\22\3\2\2\2\u00a1\u00a2\7d\2\2\u00a2\u00a3\7g\2")
        buf.write("\2\u00a3\u00a4\7i\2\2\u00a4\u00a5\7k\2\2\u00a5\u00a6\7")
        buf.write("p\2\2\u00a6\24\3\2\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9")
        buf.write("\7p\2\2\u00a9\u00aa\7f\2\2\u00aa\26\3\2\2\2\u00ab\u00ac")
        buf.write("\7t\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af")
        buf.write("\7w\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1\7p\2\2\u00b1\30")
        buf.write("\3\2\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4\7h\2\2\u00b4\32")
        buf.write("\3\2\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7n\2\2\u00b7\u00b8")
        buf.write("\7u\2\2\u00b8\u00b9\7g\2\2\u00b9\34\3\2\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\u00bc\7n\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be")
        buf.write("\7h\2\2\u00be\36\3\2\2\2\u00bf\u00c0\7h\2\2\u00c0\u00c1")
        buf.write("\7q\2\2\u00c1\u00c2\7t\2\2\u00c2 \3\2\2\2\u00c3\u00c4")
        buf.write("\7w\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7")
        buf.write("\7k\2\2\u00c7\u00c8\7n\2\2\u00c8\"\3\2\2\2\u00c9\u00ca")
        buf.write("\7d\2\2\u00ca\u00cb\7{\2\2\u00cb$\3\2\2\2\u00cc\u00cd")
        buf.write("\7d\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0")
        buf.write("\7c\2\2\u00d0\u00d1\7m\2\2\u00d1&\3\2\2\2\u00d2\u00d3")
        buf.write("\7e\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6")
        buf.write("\7v\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9")
        buf.write("\7w\2\2\u00d9\u00da\7g\2\2\u00da(\3\2\2\2\u00db\u00df")
        buf.write("\t\5\2\2\u00dc\u00de\t\6\2\2\u00dd\u00dc\3\2\2\2\u00de")
        buf.write("\u00e1\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0*\3\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e4\5-\27")
        buf.write("\2\u00e3\u00e5\5/\30\2\u00e4\u00e3\3\2\2\2\u00e4\u00e5")
        buf.write("\3\2\2\2\u00e5\u00e7\3\2\2\2\u00e6\u00e8\5\61\31\2\u00e7")
        buf.write("\u00e6\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8,\3\2\2\2\u00e9")
        buf.write("\u00eb\t\7\2\2\u00ea\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write("\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed.\3\2\2")
        buf.write("\2\u00ee\u00f2\7\60\2\2\u00ef\u00f1\t\7\2\2\u00f0\u00ef")
        buf.write("\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2")
        buf.write("\u00f3\3\2\2\2\u00f3\60\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5")
        buf.write("\u00f7\t\b\2\2\u00f6\u00f8\t\t\2\2\u00f7\u00f6\3\2\2\2")
        buf.write("\u00f7\u00f8\3\2\2\2\u00f8\u00fa\3\2\2\2\u00f9\u00fb\t")
        buf.write("\7\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fa")
        buf.write("\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\62\3\2\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff\u0100\7t\2\2\u0100\u0101\7w\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102\64\3\2\2\2\u0103\u0104\7h\2\2\u0104\u0105")
        buf.write("\7c\2\2\u0105\u0106\7n\2\2\u0106\u0107\7u\2\2\u0107\u0108")
        buf.write("\7g\2\2\u0108\66\3\2\2\2\u0109\u0111\7$\2\2\u010a\u0110")
        buf.write("\n\n\2\2\u010b\u010c\7^\2\2\u010c\u0110\t\13\2\2\u010d")
        buf.write("\u010e\7)\2\2\u010e\u0110\7$\2\2\u010f\u010a\3\2\2\2\u010f")
        buf.write("\u010b\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0113\3\2\2\2")
        buf.write("\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0114\3")
        buf.write("\2\2\2\u0113\u0111\3\2\2\2\u0114\u0115\7$\2\2\u0115\u0116")
        buf.write("\b\34\3\2\u01168\3\2\2\2\u0117\u0118\7>\2\2\u0118\u0119")
        buf.write("\7/\2\2\u0119:\3\2\2\2\u011a\u011b\7*\2\2\u011b<\3\2\2")
        buf.write("\2\u011c\u011d\7+\2\2\u011d>\3\2\2\2\u011e\u011f\7]\2")
        buf.write("\2\u011f@\3\2\2\2\u0120\u0121\7_\2\2\u0121B\3\2\2\2\u0122")
        buf.write("\u0123\7.\2\2\u0123D\3\2\2\2\u0124\u0125\7-\2\2\u0125")
        buf.write("F\3\2\2\2\u0126\u0127\7/\2\2\u0127H\3\2\2\2\u0128\u0129")
        buf.write("\7,\2\2\u0129J\3\2\2\2\u012a\u012b\7\61\2\2\u012bL\3\2")
        buf.write("\2\2\u012c\u012d\7\'\2\2\u012dN\3\2\2\2\u012e\u012f\7")
        buf.write("p\2\2\u012f\u0130\7q\2\2\u0130\u0131\7v\2\2\u0131P\3\2")
        buf.write("\2\2\u0132\u0133\7c\2\2\u0133\u0134\7p\2\2\u0134\u0135")
        buf.write("\7f\2\2\u0135R\3\2\2\2\u0136\u0137\7q\2\2\u0137\u0138")
        buf.write("\7t\2\2\u0138T\3\2\2\2\u0139\u013a\7?\2\2\u013aV\3\2\2")
        buf.write("\2\u013b\u013c\7#\2\2\u013c\u013d\7?\2\2\u013dX\3\2\2")
        buf.write("\2\u013e\u013f\7>\2\2\u013fZ\3\2\2\2\u0140\u0141\7>\2")
        buf.write("\2\u0141\u0142\7?\2\2\u0142\\\3\2\2\2\u0143\u0144\7@\2")
        buf.write("\2\u0144^\3\2\2\2\u0145\u0146\7@\2\2\u0146\u0147\7?\2")
        buf.write("\2\u0147`\3\2\2\2\u0148\u0149\7\60\2\2\u0149\u014a\7\60")
        buf.write("\2\2\u014a\u014b\7\60\2\2\u014bb\3\2\2\2\u014c\u014d\7")
        buf.write("?\2\2\u014d\u014e\7?\2\2\u014ed\3\2\2\2\u014f\u0150\13")
        buf.write("\2\2\2\u0150\u0151\b\63\4\2\u0151f\3\2\2\2\u0152\u015b")
        buf.write("\7$\2\2\u0153\u015a\n\f\2\2\u0154\u0155\7^\2\2\u0155\u015a")
        buf.write("\t\13\2\2\u0156\u0157\7)\2\2\u0157\u015a\7$\2\2\u0158")
        buf.write("\u015a\t\4\2\2\u0159\u0153\3\2\2\2\u0159\u0154\3\2\2\2")
        buf.write("\u0159\u0156\3\2\2\2\u0159\u0158\3\2\2\2\u015a\u015d\3")
        buf.write("\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015f")
        buf.write("\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u0160\t\r\2\2\u015f")
        buf.write("\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0162\b\64\5")
        buf.write("\2\u0162h\3\2\2\2\u0163\u016b\7$\2\2\u0164\u016a\n\16")
        buf.write("\2\2\u0165\u0166\7^\2\2\u0166\u016a\t\13\2\2\u0167\u0168")
        buf.write("\7)\2\2\u0168\u016a\7$\2\2\u0169\u0164\3\2\2\2\u0169\u0165")
        buf.write("\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016d\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016e\3\2\2\2")
        buf.write("\u016d\u016b\3\2\2\2\u016e\u016f\7^\2\2\u016f\u0170\n")
        buf.write("\13\2\2\u0170\u0171\b\65\6\2\u0171j\3\2\2\2\24\2\u0090")
        buf.write("\u0096\u009f\u00df\u00e4\u00e7\u00ec\u00f2\u00f7\u00fc")
        buf.write("\u010f\u0111\u0159\u015b\u015f\u0169\u016b\7\b\2\2\3\34")
        buf.write("\2\3\63\3\3\64\4\3\65\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER_TYPE = 1
    BOOLEAN_TYPE = 2
    STRING_TYPE = 3
    VAR = 4
    DYNAMIC = 5
    COMMENT = 6
    WHITESPACE = 7
    NEWLINE = 8
    BEGIN = 9
    END = 10
    RETURN = 11
    IF = 12
    ELSE = 13
    ELIF = 14
    FOR = 15
    UNTIL = 16
    BY = 17
    BREAK = 18
    CONTINUE = 19
    IDENTIFIER = 20
    NUMBER_LIT = 21
    TRUE = 22
    FALSE = 23
    STRING_LIT = 24
    ASSIGNMENT = 25
    LPAREN = 26
    RPAREN = 27
    LBRACK = 28
    RBRACK = 29
    COMMA = 30
    PLUS = 31
    MINUS = 32
    MULTIPLY = 33
    DIVIDE = 34
    MOD = 35
    NOT = 36
    AND = 37
    OR = 38
    EQUAL = 39
    NEQUAL = 40
    LT = 41
    LE = 42
    GT = 43
    GE = 44
    CONCATE = 45
    STRING_EQUAL = 46
    ERROR_CHAR = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'number'", "'bool'", "'string'", "'var'", "'dynamic'", "'begin'", 
            "'end'", "'return'", "'if'", "'else'", "'elif'", "'for'", "'until'", 
            "'by'", "'break'", "'continue'", "'true'", "'false'", "'<-'", 
            "'('", "')'", "'['", "']'", "','", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'not'", "'and'", "'or'", "'='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'...'", "'=='" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", "VAR", "DYNAMIC", 
            "COMMENT", "WHITESPACE", "NEWLINE", "BEGIN", "END", "RETURN", 
            "IF", "ELSE", "ELIF", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IDENTIFIER", "NUMBER_LIT", "TRUE", "FALSE", "STRING_LIT", "ASSIGNMENT", 
            "LPAREN", "RPAREN", "LBRACK", "RBRACK", "COMMA", "PLUS", "MINUS", 
            "MULTIPLY", "DIVIDE", "MOD", "NOT", "AND", "OR", "EQUAL", "NEQUAL", 
            "LT", "LE", "GT", "GE", "CONCATE", "STRING_EQUAL", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "NUMBER_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", "VAR", "DYNAMIC", 
                  "COMMENT", "WHITESPACE", "NEWLINE", "BEGIN", "END", "RETURN", 
                  "IF", "ELSE", "ELIF", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                  "IDENTIFIER", "NUMBER_LIT", "NUMBER_INTERGER", "NUMBER_DECIMAL", 
                  "NUMBER_EXPONENT", "TRUE", "FALSE", "STRING_LIT", "ASSIGNMENT", 
                  "LPAREN", "RPAREN", "LBRACK", "RBRACK", "COMMA", "PLUS", 
                  "MINUS", "MULTIPLY", "DIVIDE", "MOD", "NOT", "AND", "OR", 
                  "EQUAL", "NEQUAL", "LT", "LE", "GT", "GE", "CONCATE", 
                  "STRING_EQUAL", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[26] = self.STRING_LIT_action 
            actions[49] = self.ERROR_CHAR_action 
            actions[50] = self.UNCLOSE_STRING_action 
            actions[51] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1];
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            newlineIndex = self.text.find('\r\n') 
            raise UncloseString(self.text[1:newlineIndex] if newlineIndex != -1 else self.text[1:]) # if end with \n else end with EOF

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            raise IllegalEscape(self.text[1:-1])

     


