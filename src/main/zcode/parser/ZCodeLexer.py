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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u018b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\7\3\7\3\7\3\7\7\7\u0093\n\7\f\7\16\7\u0096\13\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\5\b\u009f\n\b\3\b\3\b\3\t\6\t\u00a4")
        buf.write("\n\t\r\t\16\t\u00a5\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3")
        buf.write("%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\7,\u0123\n,\f,\16,\u0126\13,\3-\3-\5-\u012a\n")
        buf.write("-\3-\5-\u012d\n-\3.\6.\u0130\n.\r.\16.\u0131\3/\3/\7/")
        buf.write("\u0136\n/\f/\16/\u0139\13/\3\60\3\60\5\60\u013d\n\60\3")
        buf.write("\60\6\60\u0140\n\60\r\60\16\60\u0141\3\61\3\61\5\61\u0146")
        buf.write("\n\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u0159\n\64\7")
        buf.write("\64\u015b\n\64\f\64\16\64\u015e\13\64\3\64\3\64\3\64\3")
        buf.write("\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u016c")
        buf.write("\n\66\3\66\7\66\u016f\n\66\f\66\16\66\u0172\13\66\3\66")
        buf.write("\5\66\u0175\n\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3")
        buf.write("\67\3\67\5\67\u0180\n\67\7\67\u0182\n\67\f\67\16\67\u0185")
        buf.write("\13\67\3\67\5\67\u0188\n\67\3\67\3\67\2\28\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("\2]\2_\2a/c\2e\2g\60i\61k\62m\63\3\2\24\4\2\f\f\16\17")
        buf.write("\5\2\n\13\16\16\"\"\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;")
        buf.write("\4\2GGgg\4\2--//\7\2\f\f\17\17$$))^^\3\2^^\t\2))^^ddh")
        buf.write("hppttvv\3\2))\5\2\f\f\17\17^^\7\2\n\n\16\16$$))^^\5\2")
        buf.write("\n\n\16\16^^\4\2\f\f\17\17\3\3$$\5\2$$))^^\4\2\n\n\16")
        buf.write("\16\2\u019f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2a\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\3o")
        buf.write("\3\2\2\2\5v\3\2\2\2\7{\3\2\2\2\t\u0082\3\2\2\2\13\u0086")
        buf.write("\3\2\2\2\r\u008e\3\2\2\2\17\u009e\3\2\2\2\21\u00a3\3\2")
        buf.write("\2\2\23\u00a9\3\2\2\2\25\u00af\3\2\2\2\27\u00b3\3\2\2")
        buf.write("\2\31\u00b8\3\2\2\2\33\u00bf\3\2\2\2\35\u00c2\3\2\2\2")
        buf.write("\37\u00c7\3\2\2\2!\u00cc\3\2\2\2#\u00d0\3\2\2\2%\u00d6")
        buf.write("\3\2\2\2\'\u00d9\3\2\2\2)\u00df\3\2\2\2+\u00e8\3\2\2\2")
        buf.write("-\u00eb\3\2\2\2/\u00ed\3\2\2\2\61\u00ef\3\2\2\2\63\u00f1")
        buf.write("\3\2\2\2\65\u00f3\3\2\2\2\67\u00f5\3\2\2\29\u00f7\3\2")
        buf.write("\2\2;\u00f9\3\2\2\2=\u00fb\3\2\2\2?\u00fd\3\2\2\2A\u00ff")
        buf.write("\3\2\2\2C\u0103\3\2\2\2E\u0107\3\2\2\2G\u010a\3\2\2\2")
        buf.write("I\u010c\3\2\2\2K\u010f\3\2\2\2M\u0111\3\2\2\2O\u0114\3")
        buf.write("\2\2\2Q\u0116\3\2\2\2S\u0119\3\2\2\2U\u011d\3\2\2\2W\u0120")
        buf.write("\3\2\2\2Y\u0127\3\2\2\2[\u012f\3\2\2\2]\u0133\3\2\2\2")
        buf.write("_\u013a\3\2\2\2a\u0145\3\2\2\2c\u0147\3\2\2\2e\u014c\3")
        buf.write("\2\2\2g\u0152\3\2\2\2i\u0162\3\2\2\2k\u0165\3\2\2\2m\u0178")
        buf.write("\3\2\2\2op\7p\2\2pq\7w\2\2qr\7o\2\2rs\7d\2\2st\7g\2\2")
        buf.write("tu\7t\2\2u\4\3\2\2\2vw\7d\2\2wx\7q\2\2xy\7q\2\2yz\7n\2")
        buf.write("\2z\6\3\2\2\2{|\7u\2\2|}\7v\2\2}~\7t\2\2~\177\7k\2\2\177")
        buf.write("\u0080\7p\2\2\u0080\u0081\7i\2\2\u0081\b\3\2\2\2\u0082")
        buf.write("\u0083\7x\2\2\u0083\u0084\7c\2\2\u0084\u0085\7t\2\2\u0085")
        buf.write("\n\3\2\2\2\u0086\u0087\7f\2\2\u0087\u0088\7{\2\2\u0088")
        buf.write("\u0089\7p\2\2\u0089\u008a\7c\2\2\u008a\u008b\7o\2\2\u008b")
        buf.write("\u008c\7k\2\2\u008c\u008d\7e\2\2\u008d\f\3\2\2\2\u008e")
        buf.write("\u008f\7%\2\2\u008f\u0090\7%\2\2\u0090\u0094\3\2\2\2\u0091")
        buf.write("\u0093\n\2\2\2\u0092\u0091\3\2\2\2\u0093\u0096\3\2\2\2")
        buf.write("\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0097\3")
        buf.write("\2\2\2\u0096\u0094\3\2\2\2\u0097\u0098\b\7\2\2\u0098\16")
        buf.write("\3\2\2\2\u0099\u009a\7\17\2\2\u009a\u009f\7\f\2\2\u009b")
        buf.write("\u009c\7\f\2\2\u009c\u009f\7\17\2\2\u009d\u009f\7\f\2")
        buf.write("\2\u009e\u0099\3\2\2\2\u009e\u009b\3\2\2\2\u009e\u009d")
        buf.write("\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\b\b\3\2\u00a1")
        buf.write("\20\3\2\2\2\u00a2\u00a4\t\3\2\2\u00a3\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2")
        buf.write("\u00a6\u00a7\3\2\2\2\u00a7\u00a8\b\t\2\2\u00a8\22\3\2")
        buf.write("\2\2\u00a9\u00aa\7d\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac")
        buf.write("\7i\2\2\u00ac\u00ad\7k\2\2\u00ad\u00ae\7p\2\2\u00ae\24")
        buf.write("\3\2\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2")
        buf.write("\7f\2\2\u00b2\26\3\2\2\2\u00b3\u00b4\7h\2\2\u00b4\u00b5")
        buf.write("\7w\2\2\u00b5\u00b6\7p\2\2\u00b6\u00b7\7e\2\2\u00b7\30")
        buf.write("\3\2\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb")
        buf.write("\7v\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be")
        buf.write("\7p\2\2\u00be\32\3\2\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1")
        buf.write("\7h\2\2\u00c1\34\3\2\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4")
        buf.write("\7n\2\2\u00c4\u00c5\7u\2\2\u00c5\u00c6\7g\2\2\u00c6\36")
        buf.write("\3\2\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca")
        buf.write("\7k\2\2\u00ca\u00cb\7h\2\2\u00cb \3\2\2\2\u00cc\u00cd")
        buf.write("\7h\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7t\2\2\u00cf\"")
        buf.write("\3\2\2\2\u00d0\u00d1\7w\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3")
        buf.write("\7v\2\2\u00d3\u00d4\7k\2\2\u00d4\u00d5\7n\2\2\u00d5$\3")
        buf.write("\2\2\2\u00d6\u00d7\7d\2\2\u00d7\u00d8\7{\2\2\u00d8&\3")
        buf.write("\2\2\2\u00d9\u00da\7d\2\2\u00da\u00db\7t\2\2\u00db\u00dc")
        buf.write("\7g\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de\7m\2\2\u00de(\3")
        buf.write("\2\2\2\u00df\u00e0\7e\2\2\u00e0\u00e1\7q\2\2\u00e1\u00e2")
        buf.write("\7p\2\2\u00e2\u00e3\7v\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5")
        buf.write("\7p\2\2\u00e5\u00e6\7w\2\2\u00e6\u00e7\7g\2\2\u00e7*\3")
        buf.write("\2\2\2\u00e8\u00e9\7>\2\2\u00e9\u00ea\7/\2\2\u00ea,\3")
        buf.write("\2\2\2\u00eb\u00ec\7*\2\2\u00ec.\3\2\2\2\u00ed\u00ee\7")
        buf.write("+\2\2\u00ee\60\3\2\2\2\u00ef\u00f0\7]\2\2\u00f0\62\3\2")
        buf.write("\2\2\u00f1\u00f2\7_\2\2\u00f2\64\3\2\2\2\u00f3\u00f4\7")
        buf.write(".\2\2\u00f4\66\3\2\2\2\u00f5\u00f6\7-\2\2\u00f68\3\2\2")
        buf.write("\2\u00f7\u00f8\7/\2\2\u00f8:\3\2\2\2\u00f9\u00fa\7,\2")
        buf.write("\2\u00fa<\3\2\2\2\u00fb\u00fc\7\61\2\2\u00fc>\3\2\2\2")
        buf.write("\u00fd\u00fe\7\'\2\2\u00fe@\3\2\2\2\u00ff\u0100\7p\2\2")
        buf.write("\u0100\u0101\7q\2\2\u0101\u0102\7v\2\2\u0102B\3\2\2\2")
        buf.write("\u0103\u0104\7c\2\2\u0104\u0105\7p\2\2\u0105\u0106\7f")
        buf.write("\2\2\u0106D\3\2\2\2\u0107\u0108\7q\2\2\u0108\u0109\7t")
        buf.write("\2\2\u0109F\3\2\2\2\u010a\u010b\7?\2\2\u010bH\3\2\2\2")
        buf.write("\u010c\u010d\7#\2\2\u010d\u010e\7?\2\2\u010eJ\3\2\2\2")
        buf.write("\u010f\u0110\7>\2\2\u0110L\3\2\2\2\u0111\u0112\7>\2\2")
        buf.write("\u0112\u0113\7?\2\2\u0113N\3\2\2\2\u0114\u0115\7@\2\2")
        buf.write("\u0115P\3\2\2\2\u0116\u0117\7@\2\2\u0117\u0118\7?\2\2")
        buf.write("\u0118R\3\2\2\2\u0119\u011a\7\60\2\2\u011a\u011b\7\60")
        buf.write("\2\2\u011b\u011c\7\60\2\2\u011cT\3\2\2\2\u011d\u011e\7")
        buf.write("?\2\2\u011e\u011f\7?\2\2\u011fV\3\2\2\2\u0120\u0124\t")
        buf.write("\4\2\2\u0121\u0123\t\5\2\2\u0122\u0121\3\2\2\2\u0123\u0126")
        buf.write("\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125")
        buf.write("X\3\2\2\2\u0126\u0124\3\2\2\2\u0127\u0129\5[.\2\u0128")
        buf.write("\u012a\5]/\2\u0129\u0128\3\2\2\2\u0129\u012a\3\2\2\2\u012a")
        buf.write("\u012c\3\2\2\2\u012b\u012d\5_\60\2\u012c\u012b\3\2\2\2")
        buf.write("\u012c\u012d\3\2\2\2\u012dZ\3\2\2\2\u012e\u0130\t\6\2")
        buf.write("\2\u012f\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u012f")
        buf.write("\3\2\2\2\u0131\u0132\3\2\2\2\u0132\\\3\2\2\2\u0133\u0137")
        buf.write("\7\60\2\2\u0134\u0136\t\6\2\2\u0135\u0134\3\2\2\2\u0136")
        buf.write("\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2")
        buf.write("\u0138^\3\2\2\2\u0139\u0137\3\2\2\2\u013a\u013c\t\7\2")
        buf.write("\2\u013b\u013d\t\b\2\2\u013c\u013b\3\2\2\2\u013c\u013d")
        buf.write("\3\2\2\2\u013d\u013f\3\2\2\2\u013e\u0140\t\6\2\2\u013f")
        buf.write("\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u013f\3\2\2\2")
        buf.write("\u0141\u0142\3\2\2\2\u0142`\3\2\2\2\u0143\u0146\5c\62")
        buf.write("\2\u0144\u0146\5e\63\2\u0145\u0143\3\2\2\2\u0145\u0144")
        buf.write("\3\2\2\2\u0146b\3\2\2\2\u0147\u0148\7v\2\2\u0148\u0149")
        buf.write("\7t\2\2\u0149\u014a\7w\2\2\u014a\u014b\7g\2\2\u014bd\3")
        buf.write("\2\2\2\u014c\u014d\7h\2\2\u014d\u014e\7c\2\2\u014e\u014f")
        buf.write("\7n\2\2\u014f\u0150\7u\2\2\u0150\u0151\7g\2\2\u0151f\3")
        buf.write("\2\2\2\u0152\u015c\7$\2\2\u0153\u015b\n\t\2\2\u0154\u0155")
        buf.write("\t\n\2\2\u0155\u015b\t\13\2\2\u0156\u0158\t\f\2\2\u0157")
        buf.write("\u0159\n\r\2\2\u0158\u0157\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159\u015b\3\2\2\2\u015a\u0153\3\2\2\2\u015a\u0154\3")
        buf.write("\2\2\2\u015a\u0156\3\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a")
        buf.write("\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015f\3\2\2\2\u015e")
        buf.write("\u015c\3\2\2\2\u015f\u0160\7$\2\2\u0160\u0161\b\64\4\2")
        buf.write("\u0161h\3\2\2\2\u0162\u0163\13\2\2\2\u0163\u0164\b\65")
        buf.write("\5\2\u0164j\3\2\2\2\u0165\u0170\7$\2\2\u0166\u016f\n\16")
        buf.write("\2\2\u0167\u0168\t\n\2\2\u0168\u016f\t\13\2\2\u0169\u016b")
        buf.write("\t\f\2\2\u016a\u016c\n\17\2\2\u016b\u016a\3\2\2\2\u016b")
        buf.write("\u016c\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016f\t\20\2")
        buf.write("\2\u016e\u0166\3\2\2\2\u016e\u0167\3\2\2\2\u016e\u0169")
        buf.write("\3\2\2\2\u016e\u016d\3\2\2\2\u016f\u0172\3\2\2\2\u0170")
        buf.write("\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0174\3\2\2\2")
        buf.write("\u0172\u0170\3\2\2\2\u0173\u0175\t\21\2\2\u0174\u0173")
        buf.write("\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\b\66\6\2\u0177")
        buf.write("l\3\2\2\2\u0178\u0183\7$\2\2\u0179\u0182\n\22\2\2\u017a")
        buf.write("\u0182\t\23\2\2\u017b\u017c\t\n\2\2\u017c\u0182\13\2\2")
        buf.write("\2\u017d\u017f\t\f\2\2\u017e\u0180\n\17\2\2\u017f\u017e")
        buf.write("\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0182\3\2\2\2\u0181")
        buf.write("\u0179\3\2\2\2\u0181\u017a\3\2\2\2\u0181\u017b\3\2\2\2")
        buf.write("\u0181\u017d\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181\3")
        buf.write("\2\2\2\u0183\u0184\3\2\2\2\u0184\u0187\3\2\2\2\u0185\u0183")
        buf.write("\3\2\2\2\u0186\u0188\t\21\2\2\u0187\u0186\3\2\2\2\u0188")
        buf.write("\u0189\3\2\2\2\u0189\u018a\b\67\7\2\u018an\3\2\2\2\31")
        buf.write("\2\u0094\u009e\u00a5\u0124\u0129\u012c\u0131\u0137\u013c")
        buf.write("\u0141\u0145\u0158\u015a\u015c\u016b\u016e\u0170\u0174")
        buf.write("\u017f\u0181\u0183\u0187\b\b\2\2\3\b\2\3\64\3\3\65\4\3")
        buf.write("\66\5\3\67\6")
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
            "CONTINUE", "ASSIGN", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
            "COMMA", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MOD", "NOT", 
            "AND", "OR", "EQUAL", "NOT_EQUAL", "LT", "LE", "GT", "GE", "CONCATE", 
            "STRING_EQUAL", "IDENTIFIER", "NUMBER_LIT", "BOOLEAN_LIT", "STRING_LIT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "NUMBER_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", "VAR", "DYNAMIC", 
                  "COMMENT", "NEWLINE", "WHITESPACE", "BEGIN", "END", "FUNC", 
                  "RETURN", "IF", "ELSE", "ELIF", "FOR", "UNTIL", "BY", 
                  "BREAK", "CONTINUE", "ASSIGN", "LPAREN", "RPAREN", "LBRACK", 
                  "RBRACK", "COMMA", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", 
                  "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LT", 
                  "LE", "GT", "GE", "CONCATE", "STRING_EQUAL", "IDENTIFIER", 
                  "NUMBER_LIT", "NUMBER_INTERGER", "NUMBER_DECIMAL", "NUMBER_EXPONENT", 
                  "BOOLEAN_LIT", "TRUE", "FALSE", "STRING_LIT", "ERROR_CHAR", 
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
            actions[50] = self.STRING_LIT_action 
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

            self.text = self.text.replace('\r', '')

     

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

            import re
            import math

            match1 = re.search(r'[^\\]\\[^\\nrtbf]', self.text)
            match2 = re.search(r'[\f\b]', self.text)
            #match3 = re.search(r'\'[^"]', self.text)

            end_indices = []

            if match1:
                end_index1 = match1.start() + 3  # +2 to include the escape character itself
                end_indices.append(end_index1)
                print("Case 1", end_index1)
            if match2:
                end_index2 = match2.start() + 1  # +1 to include the escape character itself
                end_indices.append(end_index2)
                print("Case 2", end_index2)
            #if match3:
            #    end_index3 = match3.start() + 2  # +1 to include the escape character itself
            #    end_indices.append(end_index3)
            #    print("Case 3", end_index3)

            if end_indices:
                end_index = min(end_indices)
            else:
                end_index = -1
                print("Case 4", end_index)

            print("Original text: ", self.text)
            raise IllegalEscape(self.text[1:end_index])
            		

     


