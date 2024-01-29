# Generated from ./main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62")
        buf.write("\u0172\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\7\7\u0091\n\7\f\7\16\7\u0094\13\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\5\b\u009d\n\b\3\b\3\b\3\t\6\t\u00a2\n\t\r")
        buf.write("\t\16\t\u00a3\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3,\3,\7,")
        buf.write("\u0121\n,\f,\16,\u0124\13,\3-\3-\5-\u0128\n-\3-\5-\u012b")
        buf.write("\n-\3.\6.\u012e\n.\r.\16.\u012f\3/\3/\7/\u0134\n/\f/\16")
        buf.write("/\u0137\13/\3\60\3\60\5\60\u013b\n\60\3\60\6\60\u013e")
        buf.write("\n\60\r\60\16\60\u013f\3\61\3\61\5\61\u0144\n\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\7\64\u0157\n\64\f\64\16\64\u015a")
        buf.write("\13\64\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\7\66\u0169\n\66\f\66\16\66\u016c\13")
        buf.write("\66\3\66\5\66\u016f\n\66\3\66\3\66\2\2\67\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("\2]\2_\2a/c\2e\2g\60i\61k\62\3\2\16\4\2\f\f\16\17\4\2")
        buf.write("\f\f\17\17\5\2\n\13\16\17\"\"\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\3\2\62;\4\2GGgg\4\2--//\7\2\f\f\17\17$$))^^\t\2))^")
        buf.write("^ddhhppttvv\7\2\n\13\16\16$$))^^\3\3$$\2\u017f\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2a\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\3m\3\2\2\2\5t\3\2\2\2\7y\3\2\2\2\t")
        buf.write("\u0080\3\2\2\2\13\u0084\3\2\2\2\r\u008c\3\2\2\2\17\u009c")
        buf.write("\3\2\2\2\21\u00a1\3\2\2\2\23\u00a7\3\2\2\2\25\u00ad\3")
        buf.write("\2\2\2\27\u00b1\3\2\2\2\31\u00b6\3\2\2\2\33\u00bd\3\2")
        buf.write("\2\2\35\u00c0\3\2\2\2\37\u00c5\3\2\2\2!\u00ca\3\2\2\2")
        buf.write("#\u00ce\3\2\2\2%\u00d4\3\2\2\2\'\u00d7\3\2\2\2)\u00dd")
        buf.write("\3\2\2\2+\u00e6\3\2\2\2-\u00e9\3\2\2\2/\u00eb\3\2\2\2")
        buf.write("\61\u00ed\3\2\2\2\63\u00ef\3\2\2\2\65\u00f1\3\2\2\2\67")
        buf.write("\u00f3\3\2\2\29\u00f5\3\2\2\2;\u00f7\3\2\2\2=\u00f9\3")
        buf.write("\2\2\2?\u00fb\3\2\2\2A\u00fd\3\2\2\2C\u0101\3\2\2\2E\u0105")
        buf.write("\3\2\2\2G\u0108\3\2\2\2I\u010a\3\2\2\2K\u010d\3\2\2\2")
        buf.write("M\u010f\3\2\2\2O\u0112\3\2\2\2Q\u0114\3\2\2\2S\u0117\3")
        buf.write("\2\2\2U\u011b\3\2\2\2W\u011e\3\2\2\2Y\u0125\3\2\2\2[\u012d")
        buf.write("\3\2\2\2]\u0131\3\2\2\2_\u0138\3\2\2\2a\u0143\3\2\2\2")
        buf.write("c\u0145\3\2\2\2e\u014a\3\2\2\2g\u0150\3\2\2\2i\u015e\3")
        buf.write("\2\2\2k\u0161\3\2\2\2mn\7p\2\2no\7w\2\2op\7o\2\2pq\7d")
        buf.write("\2\2qr\7g\2\2rs\7t\2\2s\4\3\2\2\2tu\7d\2\2uv\7q\2\2vw")
        buf.write("\7q\2\2wx\7n\2\2x\6\3\2\2\2yz\7u\2\2z{\7v\2\2{|\7t\2\2")
        buf.write("|}\7k\2\2}~\7p\2\2~\177\7i\2\2\177\b\3\2\2\2\u0080\u0081")
        buf.write("\7x\2\2\u0081\u0082\7c\2\2\u0082\u0083\7t\2\2\u0083\n")
        buf.write("\3\2\2\2\u0084\u0085\7f\2\2\u0085\u0086\7{\2\2\u0086\u0087")
        buf.write("\7p\2\2\u0087\u0088\7c\2\2\u0088\u0089\7o\2\2\u0089\u008a")
        buf.write("\7k\2\2\u008a\u008b\7e\2\2\u008b\f\3\2\2\2\u008c\u008d")
        buf.write("\7%\2\2\u008d\u008e\7%\2\2\u008e\u0092\3\2\2\2\u008f\u0091")
        buf.write("\n\2\2\2\u0090\u008f\3\2\2\2\u0091\u0094\3\2\2\2\u0092")
        buf.write("\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0095\3\2\2\2")
        buf.write("\u0094\u0092\3\2\2\2\u0095\u0096\b\7\2\2\u0096\16\3\2")
        buf.write("\2\2\u0097\u0098\7\17\2\2\u0098\u009d\7\f\2\2\u0099\u009a")
        buf.write("\7\f\2\2\u009a\u009d\7\17\2\2\u009b\u009d\t\3\2\2\u009c")
        buf.write("\u0097\3\2\2\2\u009c\u0099\3\2\2\2\u009c\u009b\3\2\2\2")
        buf.write("\u009d\u009e\3\2\2\2\u009e\u009f\b\b\3\2\u009f\20\3\2")
        buf.write("\2\2\u00a0\u00a2\t\4\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\u00a6\b\t\2\2\u00a6\22\3\2\2\2\u00a7")
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
        buf.write("\u00e7\7>\2\2\u00e7\u00e8\7/\2\2\u00e8,\3\2\2\2\u00e9")
        buf.write("\u00ea\7*\2\2\u00ea.\3\2\2\2\u00eb\u00ec\7+\2\2\u00ec")
        buf.write("\60\3\2\2\2\u00ed\u00ee\7]\2\2\u00ee\62\3\2\2\2\u00ef")
        buf.write("\u00f0\7_\2\2\u00f0\64\3\2\2\2\u00f1\u00f2\7.\2\2\u00f2")
        buf.write("\66\3\2\2\2\u00f3\u00f4\7-\2\2\u00f48\3\2\2\2\u00f5\u00f6")
        buf.write("\7/\2\2\u00f6:\3\2\2\2\u00f7\u00f8\7,\2\2\u00f8<\3\2\2")
        buf.write("\2\u00f9\u00fa\7\61\2\2\u00fa>\3\2\2\2\u00fb\u00fc\7\'")
        buf.write("\2\2\u00fc@\3\2\2\2\u00fd\u00fe\7p\2\2\u00fe\u00ff\7q")
        buf.write("\2\2\u00ff\u0100\7v\2\2\u0100B\3\2\2\2\u0101\u0102\7c")
        buf.write("\2\2\u0102\u0103\7p\2\2\u0103\u0104\7f\2\2\u0104D\3\2")
        buf.write("\2\2\u0105\u0106\7q\2\2\u0106\u0107\7t\2\2\u0107F\3\2")
        buf.write("\2\2\u0108\u0109\7?\2\2\u0109H\3\2\2\2\u010a\u010b\7#")
        buf.write("\2\2\u010b\u010c\7?\2\2\u010cJ\3\2\2\2\u010d\u010e\7>")
        buf.write("\2\2\u010eL\3\2\2\2\u010f\u0110\7>\2\2\u0110\u0111\7?")
        buf.write("\2\2\u0111N\3\2\2\2\u0112\u0113\7@\2\2\u0113P\3\2\2\2")
        buf.write("\u0114\u0115\7@\2\2\u0115\u0116\7?\2\2\u0116R\3\2\2\2")
        buf.write("\u0117\u0118\7\60\2\2\u0118\u0119\7\60\2\2\u0119\u011a")
        buf.write("\7\60\2\2\u011aT\3\2\2\2\u011b\u011c\7?\2\2\u011c\u011d")
        buf.write("\7?\2\2\u011dV\3\2\2\2\u011e\u0122\t\5\2\2\u011f\u0121")
        buf.write("\t\6\2\2\u0120\u011f\3\2\2\2\u0121\u0124\3\2\2\2\u0122")
        buf.write("\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123X\3\2\2\2\u0124")
        buf.write("\u0122\3\2\2\2\u0125\u0127\5[.\2\u0126\u0128\5]/\2\u0127")
        buf.write("\u0126\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012a\3\2\2\2")
        buf.write("\u0129\u012b\5_\60\2\u012a\u0129\3\2\2\2\u012a\u012b\3")
        buf.write("\2\2\2\u012bZ\3\2\2\2\u012c\u012e\t\7\2\2\u012d\u012c")
        buf.write("\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u012d\3\2\2\2\u012f")
        buf.write("\u0130\3\2\2\2\u0130\\\3\2\2\2\u0131\u0135\7\60\2\2\u0132")
        buf.write("\u0134\t\7\2\2\u0133\u0132\3\2\2\2\u0134\u0137\3\2\2\2")
        buf.write("\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136^\3\2\2")
        buf.write("\2\u0137\u0135\3\2\2\2\u0138\u013a\t\b\2\2\u0139\u013b")
        buf.write("\t\t\2\2\u013a\u0139\3\2\2\2\u013a\u013b\3\2\2\2\u013b")
        buf.write("\u013d\3\2\2\2\u013c\u013e\t\7\2\2\u013d\u013c\3\2\2\2")
        buf.write("\u013e\u013f\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3")
        buf.write("\2\2\2\u0140`\3\2\2\2\u0141\u0144\5c\62\2\u0142\u0144")
        buf.write("\5e\63\2\u0143\u0141\3\2\2\2\u0143\u0142\3\2\2\2\u0144")
        buf.write("b\3\2\2\2\u0145\u0146\7v\2\2\u0146\u0147\7t\2\2\u0147")
        buf.write("\u0148\7w\2\2\u0148\u0149\7g\2\2\u0149d\3\2\2\2\u014a")
        buf.write("\u014b\7h\2\2\u014b\u014c\7c\2\2\u014c\u014d\7n\2\2\u014d")
        buf.write("\u014e\7u\2\2\u014e\u014f\7g\2\2\u014ff\3\2\2\2\u0150")
        buf.write("\u0158\7$\2\2\u0151\u0157\n\n\2\2\u0152\u0153\7^\2\2\u0153")
        buf.write("\u0157\t\13\2\2\u0154\u0155\7)\2\2\u0155\u0157\7$\2\2")
        buf.write("\u0156\u0151\3\2\2\2\u0156\u0152\3\2\2\2\u0156\u0154\3")
        buf.write("\2\2\2\u0157\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159")
        buf.write("\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u0158\3\2\2\2\u015b")
        buf.write("\u015c\7$\2\2\u015c\u015d\b\64\4\2\u015dh\3\2\2\2\u015e")
        buf.write("\u015f\13\2\2\2\u015f\u0160\b\65\5\2\u0160j\3\2\2\2\u0161")
        buf.write("\u016a\7$\2\2\u0162\u0169\n\f\2\2\u0163\u0164\7^\2\2\u0164")
        buf.write("\u0169\t\13\2\2\u0165\u0166\7)\2\2\u0166\u0169\7$\2\2")
        buf.write("\u0167\u0169\t\3\2\2\u0168\u0162\3\2\2\2\u0168\u0163\3")
        buf.write("\2\2\2\u0168\u0165\3\2\2\2\u0168\u0167\3\2\2\2\u0169\u016c")
        buf.write("\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b")
        buf.write("\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u016f\t\r\2\2")
        buf.write("\u016e\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0171\b")
        buf.write("\66\6\2\u0171l\3\2\2\2\23\2\u0092\u009c\u00a3\u0122\u0127")
        buf.write("\u012a\u012f\u0135\u013a\u013f\u0143\u0156\u0158\u0168")
        buf.write("\u016a\u016e\7\b\2\2\3\b\2\3\64\3\3\65\4\3\66\5")
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
    ASSIGN = 21
    LPAREN = 22
    RPAREN = 23
    LBRACK = 24
    RBRACK = 25
    COMMA = 26
    PLUS = 27
    MINUS = 28
    MULTIPLY = 29
    DIVIDE = 30
    MOD = 31
    NOT = 32
    AND = 33
    OR = 34
    EQUAL = 35
    NOT_EQUAL = 36
    LT = 37
    LE = 38
    GT = 39
    GE = 40
    CONCATE = 41
    STRING_EQUAL = 42
    IDENTIFIER = 43
    NUMBER_LIT = 44
    BOOLEAN_LIT = 45
    STRING_LIT = 46
    ERROR_CHAR = 47
    UNCLOSE_STRING = 48

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
            "CONTINUE", "ASSIGN", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
            "COMMA", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MOD", "NOT", 
            "AND", "OR", "EQUAL", "NOT_EQUAL", "LT", "LE", "GT", "GE", "CONCATE", 
            "STRING_EQUAL", "IDENTIFIER", "NUMBER_LIT", "BOOLEAN_LIT", "STRING_LIT", 
            "ERROR_CHAR", "UNCLOSE_STRING" ]

    ruleNames = [ "NUMBER_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", "VAR", "DYNAMIC", 
                  "COMMENT", "NEWLINE", "WHITESPACE", "BEGIN", "END", "FUNC", 
                  "RETURN", "IF", "ELSE", "ELIF", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "ASSIGN", "LPAREN", "RPAREN", "LBRACK", 
                  "RBRACK", "COMMA", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                  "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LT", 
                  "LE", "GT", "GE", "CONCATE", "STRING_EQUAL", "IDENTIFIER", 
                  "NUMBER_LIT", "NUMBER_INTERGER", "NUMBER_DECIMAL", "NUMBER_EXPONENT", 
                  "BOOLEAN_LIT", "TRUE", "FALSE", "STRING_LIT", "ERROR_CHAR", 
                  "UNCLOSE_STRING" ]

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
            actions[50] = self.STRING_LIT_action 
            actions[51] = self.ERROR_CHAR_action 
            actions[52] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

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

     


