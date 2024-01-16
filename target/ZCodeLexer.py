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
        buf.write("\u0176\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\n\7\f\7\16\7\u0092\13\7\3\b\3\b\3\b\3\b\3\b\6\b\u0099")
        buf.write("\n\b\r\b\16\b\u009a\3\b\3\b\3\t\6\t\u00a0\n\t\r\t\16\t")
        buf.write("\u00a1\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\7\25\u00e2\n\25\f\25\16\25\u00e5")
        buf.write("\13\25\3\26\3\26\5\26\u00e9\n\26\3\26\5\26\u00ec\n\26")
        buf.write("\3\27\6\27\u00ef\n\27\r\27\16\27\u00f0\3\30\3\30\7\30")
        buf.write("\u00f5\n\30\f\30\16\30\u00f8\13\30\3\31\3\31\5\31\u00fc")
        buf.write("\n\31\3\31\6\31\u00ff\n\31\r\31\16\31\u0100\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\7\34\u0114\n\34\f\34\16\34\u0117")
        buf.write("\13\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3")
        buf.write("\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-")
        buf.write("\3-\3.\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\7\64\u015e\n\64\f\64\16\64\u0161\13\64\3\64")
        buf.write("\5\64\u0164\n\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3")
        buf.write("\65\7\65\u016e\n\65\f\65\16\65\u0171\13\65\3\65\3\65\3")
        buf.write("\65\3\65\3\u009a\2\66\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\2/\2\61\2\63\30\65\31\67\329\33;\34=\35")
        buf.write("?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62")
        buf.write("i\63\3\2\17\4\2\f\f\16\17\4\2\f\f\17\17\5\2\n\f\16\17")
        buf.write("\"\"\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--/")
        buf.write("/\7\2\f\f\17\17$$))^^\t\2))^^ddhhppttvv\5\2$$))^^\3\3")
        buf.write("$$\6\2\f\f\17\17$$))\2\u0188\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\3k\3\2\2\2\5r\3\2\2\2\7w\3\2\2\2\t~\3\2\2\2")
        buf.write("\13\u0082\3\2\2\2\r\u008a\3\2\2\2\17\u0098\3\2\2\2\21")
        buf.write("\u009f\3\2\2\2\23\u00a5\3\2\2\2\25\u00ab\3\2\2\2\27\u00af")
        buf.write("\3\2\2\2\31\u00b6\3\2\2\2\33\u00b9\3\2\2\2\35\u00be\3")
        buf.write("\2\2\2\37\u00c3\3\2\2\2!\u00c7\3\2\2\2#\u00cd\3\2\2\2")
        buf.write("%\u00d0\3\2\2\2\'\u00d6\3\2\2\2)\u00df\3\2\2\2+\u00e6")
        buf.write("\3\2\2\2-\u00ee\3\2\2\2/\u00f2\3\2\2\2\61\u00f9\3\2\2")
        buf.write("\2\63\u0102\3\2\2\2\65\u0107\3\2\2\2\67\u010d\3\2\2\2")
        buf.write("9\u011b\3\2\2\2;\u011e\3\2\2\2=\u0120\3\2\2\2?\u0122\3")
        buf.write("\2\2\2A\u0124\3\2\2\2C\u0126\3\2\2\2E\u0128\3\2\2\2G\u012a")
        buf.write("\3\2\2\2I\u012c\3\2\2\2K\u012e\3\2\2\2M\u0130\3\2\2\2")
        buf.write("O\u0132\3\2\2\2Q\u0136\3\2\2\2S\u013a\3\2\2\2U\u013d\3")
        buf.write("\2\2\2W\u013f\3\2\2\2Y\u0142\3\2\2\2[\u0144\3\2\2\2]\u0147")
        buf.write("\3\2\2\2_\u0149\3\2\2\2a\u014c\3\2\2\2c\u0150\3\2\2\2")
        buf.write("e\u0153\3\2\2\2g\u0156\3\2\2\2i\u0167\3\2\2\2kl\7p\2\2")
        buf.write("lm\7w\2\2mn\7o\2\2no\7d\2\2op\7g\2\2pq\7t\2\2q\4\3\2\2")
        buf.write("\2rs\7d\2\2st\7q\2\2tu\7q\2\2uv\7n\2\2v\6\3\2\2\2wx\7")
        buf.write("u\2\2xy\7v\2\2yz\7t\2\2z{\7k\2\2{|\7p\2\2|}\7i\2\2}\b")
        buf.write("\3\2\2\2~\177\7x\2\2\177\u0080\7c\2\2\u0080\u0081\7t\2")
        buf.write("\2\u0081\n\3\2\2\2\u0082\u0083\7f\2\2\u0083\u0084\7{\2")
        buf.write("\2\u0084\u0085\7p\2\2\u0085\u0086\7c\2\2\u0086\u0087\7")
        buf.write("o\2\2\u0087\u0088\7k\2\2\u0088\u0089\7e\2\2\u0089\f\3")
        buf.write("\2\2\2\u008a\u008b\7%\2\2\u008b\u008c\7%\2\2\u008c\u0090")
        buf.write("\3\2\2\2\u008d\u008f\n\2\2\2\u008e\u008d\3\2\2\2\u008f")
        buf.write("\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2")
        buf.write("\u0091\16\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0094\7\17")
        buf.write("\2\2\u0094\u0099\7\f\2\2\u0095\u0096\7\f\2\2\u0096\u0099")
        buf.write("\7\17\2\2\u0097\u0099\t\3\2\2\u0098\u0093\3\2\2\2\u0098")
        buf.write("\u0095\3\2\2\2\u0098\u0097\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u009b\3\2\2\2\u009a\u0098\3\2\2\2\u009b\u009c\3")
        buf.write("\2\2\2\u009c\u009d\b\b\2\2\u009d\20\3\2\2\2\u009e\u00a0")
        buf.write("\t\4\2\2\u009f\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\u00a4\b\t\3\2\u00a4\22\3\2\2\2\u00a5\u00a6\7d\2")
        buf.write("\2\u00a6\u00a7\7g\2\2\u00a7\u00a8\7i\2\2\u00a8\u00a9\7")
        buf.write("k\2\2\u00a9\u00aa\7p\2\2\u00aa\24\3\2\2\2\u00ab\u00ac")
        buf.write("\7g\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae\7f\2\2\u00ae\26")
        buf.write("\3\2\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2")
        buf.write("\7v\2\2\u00b2\u00b3\7w\2\2\u00b3\u00b4\7t\2\2\u00b4\u00b5")
        buf.write("\7p\2\2\u00b5\30\3\2\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8")
        buf.write("\7h\2\2\u00b8\32\3\2\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb")
        buf.write("\7n\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd\7g\2\2\u00bd\34")
        buf.write("\3\2\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0\7n\2\2\u00c0\u00c1")
        buf.write("\7k\2\2\u00c1\u00c2\7h\2\2\u00c2\36\3\2\2\2\u00c3\u00c4")
        buf.write("\7h\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7t\2\2\u00c6 \3")
        buf.write("\2\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca")
        buf.write("\7v\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7n\2\2\u00cc\"")
        buf.write("\3\2\2\2\u00cd\u00ce\7d\2\2\u00ce\u00cf\7{\2\2\u00cf$")
        buf.write("\3\2\2\2\u00d0\u00d1\7d\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3")
        buf.write("\7g\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7m\2\2\u00d5&\3")
        buf.write("\2\2\2\u00d6\u00d7\7e\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9")
        buf.write("\7p\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7k\2\2\u00db\u00dc")
        buf.write("\7p\2\2\u00dc\u00dd\7w\2\2\u00dd\u00de\7g\2\2\u00de(\3")
        buf.write("\2\2\2\u00df\u00e3\t\5\2\2\u00e0\u00e2\t\6\2\2\u00e1\u00e0")
        buf.write("\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3")
        buf.write("\u00e4\3\2\2\2\u00e4*\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6")
        buf.write("\u00e8\5-\27\2\u00e7\u00e9\5/\30\2\u00e8\u00e7\3\2\2\2")
        buf.write("\u00e8\u00e9\3\2\2\2\u00e9\u00eb\3\2\2\2\u00ea\u00ec\5")
        buf.write("\61\31\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec")
        buf.write(",\3\2\2\2\u00ed\u00ef\t\7\2\2\u00ee\u00ed\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2")
        buf.write("\u00f1.\3\2\2\2\u00f2\u00f6\7\60\2\2\u00f3\u00f5\t\7\2")
        buf.write("\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f4")
        buf.write("\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\60\3\2\2\2\u00f8\u00f6")
        buf.write("\3\2\2\2\u00f9\u00fb\t\b\2\2\u00fa\u00fc\t\t\2\2\u00fb")
        buf.write("\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fe\3\2\2\2")
        buf.write("\u00fd\u00ff\t\7\2\2\u00fe\u00fd\3\2\2\2\u00ff\u0100\3")
        buf.write("\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101\62")
        buf.write("\3\2\2\2\u0102\u0103\7v\2\2\u0103\u0104\7t\2\2\u0104\u0105")
        buf.write("\7w\2\2\u0105\u0106\7g\2\2\u0106\64\3\2\2\2\u0107\u0108")
        buf.write("\7h\2\2\u0108\u0109\7c\2\2\u0109\u010a\7n\2\2\u010a\u010b")
        buf.write("\7u\2\2\u010b\u010c\7g\2\2\u010c\66\3\2\2\2\u010d\u0115")
        buf.write("\7$\2\2\u010e\u0114\n\n\2\2\u010f\u0110\7^\2\2\u0110\u0114")
        buf.write("\t\13\2\2\u0111\u0112\7)\2\2\u0112\u0114\7$\2\2\u0113")
        buf.write("\u010e\3\2\2\2\u0113\u010f\3\2\2\2\u0113\u0111\3\2\2\2")
        buf.write("\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3")
        buf.write("\2\2\2\u0116\u0118\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119")
        buf.write("\7$\2\2\u0119\u011a\b\34\4\2\u011a8\3\2\2\2\u011b\u011c")
        buf.write("\7>\2\2\u011c\u011d\7/\2\2\u011d:\3\2\2\2\u011e\u011f")
        buf.write("\7*\2\2\u011f<\3\2\2\2\u0120\u0121\7+\2\2\u0121>\3\2\2")
        buf.write("\2\u0122\u0123\7]\2\2\u0123@\3\2\2\2\u0124\u0125\7_\2")
        buf.write("\2\u0125B\3\2\2\2\u0126\u0127\7.\2\2\u0127D\3\2\2\2\u0128")
        buf.write("\u0129\7-\2\2\u0129F\3\2\2\2\u012a\u012b\7/\2\2\u012b")
        buf.write("H\3\2\2\2\u012c\u012d\7,\2\2\u012dJ\3\2\2\2\u012e\u012f")
        buf.write("\7\61\2\2\u012fL\3\2\2\2\u0130\u0131\7\'\2\2\u0131N\3")
        buf.write("\2\2\2\u0132\u0133\7p\2\2\u0133\u0134\7q\2\2\u0134\u0135")
        buf.write("\7v\2\2\u0135P\3\2\2\2\u0136\u0137\7c\2\2\u0137\u0138")
        buf.write("\7p\2\2\u0138\u0139\7f\2\2\u0139R\3\2\2\2\u013a\u013b")
        buf.write("\7q\2\2\u013b\u013c\7t\2\2\u013cT\3\2\2\2\u013d\u013e")
        buf.write("\7?\2\2\u013eV\3\2\2\2\u013f\u0140\7#\2\2\u0140\u0141")
        buf.write("\7?\2\2\u0141X\3\2\2\2\u0142\u0143\7>\2\2\u0143Z\3\2\2")
        buf.write("\2\u0144\u0145\7>\2\2\u0145\u0146\7?\2\2\u0146\\\3\2\2")
        buf.write("\2\u0147\u0148\7@\2\2\u0148^\3\2\2\2\u0149\u014a\7@\2")
        buf.write("\2\u014a\u014b\7?\2\2\u014b`\3\2\2\2\u014c\u014d\7\60")
        buf.write("\2\2\u014d\u014e\7\60\2\2\u014e\u014f\7\60\2\2\u014fb")
        buf.write("\3\2\2\2\u0150\u0151\7?\2\2\u0151\u0152\7?\2\2\u0152d")
        buf.write("\3\2\2\2\u0153\u0154\13\2\2\2\u0154\u0155\b\63\5\2\u0155")
        buf.write("f\3\2\2\2\u0156\u015f\7$\2\2\u0157\u015e\n\f\2\2\u0158")
        buf.write("\u0159\7^\2\2\u0159\u015e\t\13\2\2\u015a\u015b\7)\2\2")
        buf.write("\u015b\u015e\7$\2\2\u015c\u015e\t\3\2\2\u015d\u0157\3")
        buf.write("\2\2\2\u015d\u0158\3\2\2\2\u015d\u015a\3\2\2\2\u015d\u015c")
        buf.write("\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d\3\2\2\2\u015f")
        buf.write("\u0160\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u015f\3\2\2\2")
        buf.write("\u0162\u0164\t\r\2\2\u0163\u0162\3\2\2\2\u0164\u0165\3")
        buf.write("\2\2\2\u0165\u0166\b\64\6\2\u0166h\3\2\2\2\u0167\u016f")
        buf.write("\7$\2\2\u0168\u016e\n\16\2\2\u0169\u016a\7^\2\2\u016a")
        buf.write("\u016e\t\13\2\2\u016b\u016c\7)\2\2\u016c\u016e\7$\2\2")
        buf.write("\u016d\u0168\3\2\2\2\u016d\u0169\3\2\2\2\u016d\u016b\3")
        buf.write("\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170")
        buf.write("\3\2\2\2\u0170\u0172\3\2\2\2\u0171\u016f\3\2\2\2\u0172")
        buf.write("\u0173\7^\2\2\u0173\u0174\n\13\2\2\u0174\u0175\b\65\7")
        buf.write("\2\u0175j\3\2\2\2\25\2\u0090\u0098\u009a\u00a1\u00e3\u00e8")
        buf.write("\u00eb\u00f0\u00f6\u00fb\u0100\u0113\u0115\u015d\u015f")
        buf.write("\u0163\u016d\u016f\b\3\b\2\b\2\2\3\34\3\3\63\4\3\64\5")
        buf.write("\3\65\6")
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
    NEWLINE = 7
    WHITESPACE = 8
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
            "COMMENT", "NEWLINE", "WHITESPACE", "BEGIN", "END", "RETURN", 
            "IF", "ELSE", "ELIF", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IDENTIFIER", "NUMBER_LIT", "TRUE", "FALSE", "STRING_LIT", "ASSIGNMENT", 
            "LPAREN", "RPAREN", "LBRACK", "RBRACK", "COMMA", "PLUS", "MINUS", 
            "MULTIPLY", "DIVIDE", "MOD", "NOT", "AND", "OR", "EQUAL", "NEQUAL", 
            "LT", "LE", "GT", "GE", "CONCATE", "STRING_EQUAL", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "NUMBER_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", "VAR", "DYNAMIC", 
                  "COMMENT", "NEWLINE", "WHITESPACE", "BEGIN", "END", "RETURN", 
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
            actions[6] = self.NEWLINE_action 
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


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            print("NEWLINE")
            self.text = self.text.replace('\r\n', '\n')

     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:-1];
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            newlineIndex = self.text.find('\r\n') 
            raise UncloseString(self.text[1:newlineIndex] if newlineIndex != -1 else self.text[1:]) # if end with \n else end with EOF

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            raise IllegalEscape(self.text[1:-1])

     


