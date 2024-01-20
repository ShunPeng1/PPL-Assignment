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
        buf.write("\u0186\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\7\7\u0093\n\7\f\7\16\7\u0096\13\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\5\b\u009d\n\b\3\b\3\b\3\t\6\t\u00a2\n\t")
        buf.write("\r\t\16\t\u00a3\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\7\26\u00e9\n\26\f\26\16\26\u00ec\13\26\3\27\3\27")
        buf.write("\5\27\u00f0\n\27\3\27\5\27\u00f3\n\27\3\30\6\30\u00f6")
        buf.write("\n\30\r\30\16\30\u00f7\3\31\3\31\7\31\u00fc\n\31\f\31")
        buf.write("\16\31\u00ff\13\31\3\32\3\32\5\32\u0103\n\32\3\32\6\32")
        buf.write("\u0106\n\32\r\32\16\32\u0107\3\33\3\33\5\33\u010c\n\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u011f\n\36\f\36\16")
        buf.write("\36\u0122\13\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)")
        buf.write("\3)\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\7\66\u0169\n\66\f\66\16\66\u016c")
        buf.write("\13\66\3\66\5\66\u016f\n\66\3\66\3\66\3\67\3\67\3\67\3")
        buf.write("\67\3\67\3\67\7\67\u0179\n\67\f\67\16\67\u017c\13\67\3")
        buf.write("\67\3\67\3\67\3\67\3\67\5\67\u0183\n\67\3\67\3\67\2\2")
        buf.write("8\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\2")
        buf.write("\61\2\63\2\65\31\67\29\2;\32=\33?\34A\35C\36E\37G I!K")
        buf.write("\"M#O$Q%S&U\'W(Y)[*]+_,a-c.e/g\60i\61k\62m\63\3\2\21\4")
        buf.write("\2\f\f\16\17\4\2\f\f\17\17\5\2\n\13\16\17\"\"\5\2C\\a")
        buf.write("ac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\4\2--//\7\2\f\f\17")
        buf.write("\17$$))^^\t\2))^^ddhhppttvv\7\2\n\13\16\16$$))^^\3\3$")
        buf.write("$\5\2$$))^^\4\2\n\13\16\16\3\2$$\2\u0198\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2\65\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\3o\3\2\2\2\5v\3\2\2\2\7{\3\2\2\2\t")
        buf.write("\u0082\3\2\2\2\13\u0086\3\2\2\2\r\u008e\3\2\2\2\17\u009c")
        buf.write("\3\2\2\2\21\u00a1\3\2\2\2\23\u00a7\3\2\2\2\25\u00ad\3")
        buf.write("\2\2\2\27\u00b1\3\2\2\2\31\u00b6\3\2\2\2\33\u00bd\3\2")
        buf.write("\2\2\35\u00c0\3\2\2\2\37\u00c5\3\2\2\2!\u00ca\3\2\2\2")
        buf.write("#\u00ce\3\2\2\2%\u00d4\3\2\2\2\'\u00d7\3\2\2\2)\u00dd")
        buf.write("\3\2\2\2+\u00e6\3\2\2\2-\u00ed\3\2\2\2/\u00f5\3\2\2\2")
        buf.write("\61\u00f9\3\2\2\2\63\u0100\3\2\2\2\65\u010b\3\2\2\2\67")
        buf.write("\u010d\3\2\2\29\u0112\3\2\2\2;\u0118\3\2\2\2=\u0126\3")
        buf.write("\2\2\2?\u0129\3\2\2\2A\u012b\3\2\2\2C\u012d\3\2\2\2E\u012f")
        buf.write("\3\2\2\2G\u0131\3\2\2\2I\u0133\3\2\2\2K\u0135\3\2\2\2")
        buf.write("M\u0137\3\2\2\2O\u0139\3\2\2\2Q\u013b\3\2\2\2S\u013d\3")
        buf.write("\2\2\2U\u0141\3\2\2\2W\u0145\3\2\2\2Y\u0148\3\2\2\2[\u014a")
        buf.write("\3\2\2\2]\u014d\3\2\2\2_\u014f\3\2\2\2a\u0152\3\2\2\2")
        buf.write("c\u0154\3\2\2\2e\u0157\3\2\2\2g\u015b\3\2\2\2i\u015e\3")
        buf.write("\2\2\2k\u0161\3\2\2\2m\u0172\3\2\2\2op\7p\2\2pq\7w\2\2")
        buf.write("qr\7o\2\2rs\7d\2\2st\7g\2\2tu\7t\2\2u\4\3\2\2\2vw\7d\2")
        buf.write("\2wx\7q\2\2xy\7q\2\2yz\7n\2\2z\6\3\2\2\2{|\7u\2\2|}\7")
        buf.write("v\2\2}~\7t\2\2~\177\7k\2\2\177\u0080\7p\2\2\u0080\u0081")
        buf.write("\7i\2\2\u0081\b\3\2\2\2\u0082\u0083\7x\2\2\u0083\u0084")
        buf.write("\7c\2\2\u0084\u0085\7t\2\2\u0085\n\3\2\2\2\u0086\u0087")
        buf.write("\7f\2\2\u0087\u0088\7{\2\2\u0088\u0089\7p\2\2\u0089\u008a")
        buf.write("\7c\2\2\u008a\u008b\7o\2\2\u008b\u008c\7k\2\2\u008c\u008d")
        buf.write("\7e\2\2\u008d\f\3\2\2\2\u008e\u008f\7%\2\2\u008f\u0090")
        buf.write("\7%\2\2\u0090\u0094\3\2\2\2\u0091\u0093\n\2\2\2\u0092")
        buf.write("\u0091\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092\3\2\2\2")
        buf.write("\u0094\u0095\3\2\2\2\u0095\16\3\2\2\2\u0096\u0094\3\2")
        buf.write("\2\2\u0097\u0098\7\17\2\2\u0098\u009d\7\f\2\2\u0099\u009a")
        buf.write("\7\f\2\2\u009a\u009d\7\17\2\2\u009b\u009d\t\3\2\2\u009c")
        buf.write("\u0097\3\2\2\2\u009c\u0099\3\2\2\2\u009c\u009b\3\2\2\2")
        buf.write("\u009d\u009e\3\2\2\2\u009e\u009f\b\b\2\2\u009f\20\3\2")
        buf.write("\2\2\u00a0\u00a2\t\4\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\u00a6\b\t\3\2\u00a6\22\3\2\2\2\u00a7")
        buf.write("\u00a8\7d\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7i\2\2\u00aa")
        buf.write("\u00ab\7k\2\2\u00ab\u00ac\7p\2\2\u00ac\24\3\2\2\2\u00ad")
        buf.write("\u00ae\7g\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7f\2\2\u00b0")
        buf.write("\26\3\2\2\2\u00b1\u00b2\7h\2\2\u00b2\u00b3\7w\2\2\u00b3")
        buf.write("\u00b4\7p\2\2\u00b4\u00b5\7e\2\2\u00b5\30\3\2\2\2\u00b6")
        buf.write("\u00b7\7t\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9\7v\2\2\u00b9")
        buf.write("\u00ba\7w\2\2\u00ba\u00bb\7t\2\2\u00bb\u00bc\7p\2\2\u00bc")
        buf.write("\32\3\2\2\2\u00bd\u00be\7k\2\2\u00be\u00bf\7h\2\2\u00bf")
        buf.write("\34\3\2\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7n\2\2\u00c2")
        buf.write("\u00c3\7u\2\2\u00c3\u00c4\7g\2\2\u00c4\36\3\2\2\2\u00c5")
        buf.write("\u00c6\7g\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8\7k\2\2\u00c8")
        buf.write("\u00c9\7h\2\2\u00c9 \3\2\2\2\u00ca\u00cb\7h\2\2\u00cb")
        buf.write("\u00cc\7q\2\2\u00cc\u00cd\7t\2\2\u00cd\"\3\2\2\2\u00ce")
        buf.write("\u00cf\7w\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7v\2\2\u00d1")
        buf.write("\u00d2\7k\2\2\u00d2\u00d3\7n\2\2\u00d3$\3\2\2\2\u00d4")
        buf.write("\u00d5\7d\2\2\u00d5\u00d6\7{\2\2\u00d6&\3\2\2\2\u00d7")
        buf.write("\u00d8\7d\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7g\2\2\u00da")
        buf.write("\u00db\7c\2\2\u00db\u00dc\7m\2\2\u00dc(\3\2\2\2\u00dd")
        buf.write("\u00de\7e\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7p\2\2\u00e0")
        buf.write("\u00e1\7v\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3")
        buf.write("\u00e4\7w\2\2\u00e4\u00e5\7g\2\2\u00e5*\3\2\2\2\u00e6")
        buf.write("\u00ea\t\5\2\2\u00e7\u00e9\t\6\2\2\u00e8\u00e7\3\2\2\2")
        buf.write("\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3")
        buf.write("\2\2\2\u00eb,\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00ef")
        buf.write("\5/\30\2\u00ee\u00f0\5\61\31\2\u00ef\u00ee\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00f3\5\63\32")
        buf.write("\2\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3.\3\2")
        buf.write("\2\2\u00f4\u00f6\t\7\2\2\u00f5\u00f4\3\2\2\2\u00f6\u00f7")
        buf.write("\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8")
        buf.write("\60\3\2\2\2\u00f9\u00fd\7\60\2\2\u00fa\u00fc\t\7\2\2\u00fb")
        buf.write("\u00fa\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2")
        buf.write("\u00fd\u00fe\3\2\2\2\u00fe\62\3\2\2\2\u00ff\u00fd\3\2")
        buf.write("\2\2\u0100\u0102\t\b\2\2\u0101\u0103\t\t\2\2\u0102\u0101")
        buf.write("\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0105\3\2\2\2\u0104")
        buf.write("\u0106\t\7\2\2\u0105\u0104\3\2\2\2\u0106\u0107\3\2\2\2")
        buf.write("\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\64\3\2")
        buf.write("\2\2\u0109\u010c\5\67\34\2\u010a\u010c\59\35\2\u010b\u0109")
        buf.write("\3\2\2\2\u010b\u010a\3\2\2\2\u010c\66\3\2\2\2\u010d\u010e")
        buf.write("\7v\2\2\u010e\u010f\7t\2\2\u010f\u0110\7w\2\2\u0110\u0111")
        buf.write("\7g\2\2\u01118\3\2\2\2\u0112\u0113\7h\2\2\u0113\u0114")
        buf.write("\7c\2\2\u0114\u0115\7n\2\2\u0115\u0116\7u\2\2\u0116\u0117")
        buf.write("\7g\2\2\u0117:\3\2\2\2\u0118\u0120\7$\2\2\u0119\u011f")
        buf.write("\n\n\2\2\u011a\u011b\7^\2\2\u011b\u011f\t\13\2\2\u011c")
        buf.write("\u011d\7)\2\2\u011d\u011f\7$\2\2\u011e\u0119\3\2\2\2\u011e")
        buf.write("\u011a\3\2\2\2\u011e\u011c\3\2\2\2\u011f\u0122\3\2\2\2")
        buf.write("\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0123\3")
        buf.write("\2\2\2\u0122\u0120\3\2\2\2\u0123\u0124\7$\2\2\u0124\u0125")
        buf.write("\b\36\4\2\u0125<\3\2\2\2\u0126\u0127\7>\2\2\u0127\u0128")
        buf.write("\7/\2\2\u0128>\3\2\2\2\u0129\u012a\7*\2\2\u012a@\3\2\2")
        buf.write("\2\u012b\u012c\7+\2\2\u012cB\3\2\2\2\u012d\u012e\7]\2")
        buf.write("\2\u012eD\3\2\2\2\u012f\u0130\7_\2\2\u0130F\3\2\2\2\u0131")
        buf.write("\u0132\7.\2\2\u0132H\3\2\2\2\u0133\u0134\7-\2\2\u0134")
        buf.write("J\3\2\2\2\u0135\u0136\7/\2\2\u0136L\3\2\2\2\u0137\u0138")
        buf.write("\7,\2\2\u0138N\3\2\2\2\u0139\u013a\7\61\2\2\u013aP\3\2")
        buf.write("\2\2\u013b\u013c\7\'\2\2\u013cR\3\2\2\2\u013d\u013e\7")
        buf.write("p\2\2\u013e\u013f\7q\2\2\u013f\u0140\7v\2\2\u0140T\3\2")
        buf.write("\2\2\u0141\u0142\7c\2\2\u0142\u0143\7p\2\2\u0143\u0144")
        buf.write("\7f\2\2\u0144V\3\2\2\2\u0145\u0146\7q\2\2\u0146\u0147")
        buf.write("\7t\2\2\u0147X\3\2\2\2\u0148\u0149\7?\2\2\u0149Z\3\2\2")
        buf.write("\2\u014a\u014b\7#\2\2\u014b\u014c\7?\2\2\u014c\\\3\2\2")
        buf.write("\2\u014d\u014e\7>\2\2\u014e^\3\2\2\2\u014f\u0150\7>\2")
        buf.write("\2\u0150\u0151\7?\2\2\u0151`\3\2\2\2\u0152\u0153\7@\2")
        buf.write("\2\u0153b\3\2\2\2\u0154\u0155\7@\2\2\u0155\u0156\7?\2")
        buf.write("\2\u0156d\3\2\2\2\u0157\u0158\7\60\2\2\u0158\u0159\7\60")
        buf.write("\2\2\u0159\u015a\7\60\2\2\u015af\3\2\2\2\u015b\u015c\7")
        buf.write("?\2\2\u015c\u015d\7?\2\2\u015dh\3\2\2\2\u015e\u015f\13")
        buf.write("\2\2\2\u015f\u0160\b\65\5\2\u0160j\3\2\2\2\u0161\u016a")
        buf.write("\7$\2\2\u0162\u0169\n\f\2\2\u0163\u0164\7^\2\2\u0164\u0169")
        buf.write("\t\13\2\2\u0165\u0166\7)\2\2\u0166\u0169\7$\2\2\u0167")
        buf.write("\u0169\t\3\2\2\u0168\u0162\3\2\2\2\u0168\u0163\3\2\2\2")
        buf.write("\u0168\u0165\3\2\2\2\u0168\u0167\3\2\2\2\u0169\u016c\3")
        buf.write("\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016e")
        buf.write("\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u016f\t\r\2\2\u016e")
        buf.write("\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0171\b\66\6")
        buf.write("\2\u0171l\3\2\2\2\u0172\u017a\7$\2\2\u0173\u0179\n\16")
        buf.write("\2\2\u0174\u0175\7^\2\2\u0175\u0179\t\13\2\2\u0176\u0177")
        buf.write("\7)\2\2\u0177\u0179\7$\2\2\u0178\u0173\3\2\2\2\u0178\u0174")
        buf.write("\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017c\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u0182\3\2\2\2")
        buf.write("\u017c\u017a\3\2\2\2\u017d\u017e\7^\2\2\u017e\u0183\n")
        buf.write("\13\2\2\u017f\u0183\t\17\2\2\u0180\u0181\7)\2\2\u0181")
        buf.write("\u0183\n\20\2\2\u0182\u017d\3\2\2\2\u0182\u017f\3\2\2")
        buf.write("\2\u0182\u0180\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185")
        buf.write("\b\67\7\2\u0185n\3\2\2\2\26\2\u0094\u009c\u00a3\u00ea")
        buf.write("\u00ef\u00f2\u00f7\u00fd\u0102\u0107\u010b\u011e\u0120")
        buf.write("\u0168\u016a\u016e\u0178\u017a\u0182\b\3\b\2\b\2\2\3\36")
        buf.write("\3\3\65\4\3\66\5\3\67\6")
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
    FUNC = 11
    RETURN = 12
    IF = 13
    ELSE = 14
    ELIF = 15
    FOR = 16
    UNTIL = 17
    BY = 18
    BREAK = 19
    CONTINUE = 20
    IDENTIFIER = 21
    NUMBER_LIT = 22
    BOOLEAN_LIT = 23
    STRING_LIT = 24
    ASSIGN = 25
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
    NOT_EQUAL = 40
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
            "'end'", "'func'", "'return'", "'if'", "'else'", "'elif'", "'for'", 
            "'until'", "'by'", "'break'", "'continue'", "'<-'", "'('", "')'", 
            "'['", "']'", "','", "'+'", "'-'", "'*'", "'/'", "'%'", "'not'", 
            "'and'", "'or'", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", "VAR", "DYNAMIC", 
            "COMMENT", "NEWLINE", "WHITESPACE", "BEGIN", "END", "FUNC", 
            "RETURN", "IF", "ELSE", "ELIF", "FOR", "UNTIL", "BY", "BREAK", 
            "CONTINUE", "IDENTIFIER", "NUMBER_LIT", "BOOLEAN_LIT", "STRING_LIT", 
            "ASSIGN", "LPAREN", "RPAREN", "LBRACK", "RBRACK", "COMMA", "PLUS", 
            "MINUS", "MULTIPLY", "DIVIDE", "MOD", "NOT", "AND", "OR", "EQUAL", 
            "NOT_EQUAL", "LT", "LE", "GT", "GE", "CONCATE", "STRING_EQUAL", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "NUMBER_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", "VAR", "DYNAMIC", 
                  "COMMENT", "NEWLINE", "WHITESPACE", "BEGIN", "END", "FUNC", 
                  "RETURN", "IF", "ELSE", "ELIF", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "IDENTIFIER", "NUMBER_LIT", "NUMBER_INTERGER", 
                  "NUMBER_DECIMAL", "NUMBER_EXPONENT", "BOOLEAN_LIT", "TRUE", 
                  "FALSE", "STRING_LIT", "ASSIGN", "LPAREN", "RPAREN", "LBRACK", 
                  "RBRACK", "COMMA", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                  "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LT", 
                  "LE", "GT", "GE", "CONCATE", "STRING_EQUAL", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[28] = self.STRING_LIT_action 
            actions[51] = self.ERROR_CHAR_action 
            actions[52] = self.UNCLOSE_STRING_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
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

            self.text = self.text[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            raise ErrorToken(self.text)

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            newlineIndex = self.text.find('\r\n') 
            raise UncloseString(self.text[1:newlineIndex] if newlineIndex != -1 else self.text[1:]) # if end with \n else end with EOF

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            raise IllegalEscape(self.text[1:])

     


