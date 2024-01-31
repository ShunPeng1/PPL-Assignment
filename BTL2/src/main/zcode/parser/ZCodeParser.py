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
        buf.write("\u01bf\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\5\2t\n")
        buf.write("\2\3\2\3\2\5\2x\n\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0080")
        buf.write("\n\3\3\4\3\4\5\4\u0084\n\4\3\4\3\4\3\4\5\4\u0089\n\4\3")
        buf.write("\5\5\5\u008c\n\5\3\5\3\5\5\5\u0090\n\5\3\6\3\6\5\6\u0094")
        buf.write("\n\6\3\6\3\6\3\6\5\6\u0099\n\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\5\7\u00b0\n\7\3\b\3\b\3\b\3\b\5\b\u00b6\n\b\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\5\13\u00c2\n\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00ca\n\f\3\f\3\f\3\f\5\f")
        buf.write("\u00cf\n\f\5\f\u00d1\n\f\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\5\16\u00da\n\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u00e5\n\20\3\21\3\21\5\21\u00e9\n\21\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u00f2\n\22\3\22")
        buf.write("\3\22\3\22\3\23\5\23\u00f8\n\23\3\23\3\23\3\23\3\23\5")
        buf.write("\23\u00fe\n\23\3\23\3\23\5\23\u0102\n\23\3\24\3\24\5\24")
        buf.write("\u0106\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u010d\n\25\3")
        buf.write("\26\3\26\5\26\u0111\n\26\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\5\31\u011e\n\31\3\31\5\31\u0121")
        buf.write("\n\31\3\32\3\32\3\32\3\32\5\32\u0127\n\32\3\33\3\33\3")
        buf.write("\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3\37\5\37\u0139\n\37\3\37\3\37\3 \3 \3 \3 ")
        buf.write("\3 \5 \u0142\n \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3#\3#")
        buf.write("\3$\3$\3%\3%\3&\3&\3&\3&\3&\5&\u0159\n&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\5\'\u0160\n\'\3(\3(\3(\3(\3(\3(\3(\7(\u0169\n(")
        buf.write("\f(\16(\u016c\13(\3)\3)\3)\3)\3)\3)\3)\7)\u0175\n)\f)")
        buf.write("\16)\u0178\13)\3*\3*\3*\3*\3*\3*\3*\7*\u0181\n*\f*\16")
        buf.write("*\u0184\13*\3+\3+\3+\5+\u0189\n+\3,\3,\3,\3,\5,\u018f")
        buf.write("\n,\3-\3-\3-\3-\3-\5-\u0196\n-\3.\3.\3.\3.\5.\u019c\n")
        buf.write(".\3/\3/\5/\u01a0\n/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\5\61\u01ad\n\61\3\62\3\62\3\63\3\63\3")
        buf.write("\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\39")
        buf.write("\2\5NPR:\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write("*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnp\2\b\3\2")
        buf.write("\3\5\4\2%*,,\3\2\35\36\3\2\37!\3\2#$\3\2.\60\2\u01ba\2")
        buf.write("s\3\2\2\2\4\177\3\2\2\2\6\u0088\3\2\2\2\b\u008b\3\2\2")
        buf.write("\2\n\u0098\3\2\2\2\f\u00af\3\2\2\2\16\u00b5\3\2\2\2\20")
        buf.write("\u00b7\3\2\2\2\22\u00b9\3\2\2\2\24\u00c1\3\2\2\2\26\u00d0")
        buf.write("\3\2\2\2\30\u00d2\3\2\2\2\32\u00d4\3\2\2\2\34\u00db\3")
        buf.write("\2\2\2\36\u00e4\3\2\2\2 \u00e6\3\2\2\2\"\u00ed\3\2\2\2")
        buf.write("$\u0101\3\2\2\2&\u0103\3\2\2\2(\u010c\3\2\2\2*\u0110\3")
        buf.write("\2\2\2,\u0112\3\2\2\2.\u0115\3\2\2\2\60\u0119\3\2\2\2")
        buf.write("\62\u0126\3\2\2\2\64\u0128\3\2\2\2\66\u012c\3\2\2\28\u012f")
        buf.write("\3\2\2\2:\u0133\3\2\2\2<\u0135\3\2\2\2>\u0141\3\2\2\2")
        buf.write("@\u0143\3\2\2\2B\u014b\3\2\2\2D\u014d\3\2\2\2F\u014f\3")
        buf.write("\2\2\2H\u0151\3\2\2\2J\u0158\3\2\2\2L\u015f\3\2\2\2N\u0161")
        buf.write("\3\2\2\2P\u016d\3\2\2\2R\u0179\3\2\2\2T\u0188\3\2\2\2")
        buf.write("V\u018e\3\2\2\2X\u0195\3\2\2\2Z\u019b\3\2\2\2\\\u019f")
        buf.write("\3\2\2\2^\u01a3\3\2\2\2`\u01ac\3\2\2\2b\u01ae\3\2\2\2")
        buf.write("d\u01b0\3\2\2\2f\u01b2\3\2\2\2h\u01b4\3\2\2\2j\u01b6\3")
        buf.write("\2\2\2l\u01b8\3\2\2\2n\u01ba\3\2\2\2p\u01bc\3\2\2\2rt")
        buf.write("\5\16\b\2sr\3\2\2\2st\3\2\2\2tu\3\2\2\2uw\5\4\3\2vx\5")
        buf.write("\16\b\2wv\3\2\2\2wx\3\2\2\2xy\3\2\2\2yz\7\2\2\3z\3\3\2")
        buf.write("\2\2{|\5\6\4\2|}\5\4\3\2}\u0080\3\2\2\2~\u0080\5\6\4\2")
        buf.write("\177{\3\2\2\2\177~\3\2\2\2\u0080\5\3\2\2\2\u0081\u0083")
        buf.write("\5\"\22\2\u0082\u0084\5\16\b\2\u0083\u0082\3\2\2\2\u0083")
        buf.write("\u0084\3\2\2\2\u0084\u0089\3\2\2\2\u0085\u0086\5\24\13")
        buf.write("\2\u0086\u0087\5\16\b\2\u0087\u0089\3\2\2\2\u0088\u0081")
        buf.write("\3\2\2\2\u0088\u0085\3\2\2\2\u0089\7\3\2\2\2\u008a\u008c")
        buf.write("\5\16\b\2\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2\2\u008c")
        buf.write("\u008d\3\2\2\2\u008d\u008f\5\f\7\2\u008e\u0090\5\16\b")
        buf.write("\2\u008f\u008e\3\2\2\2\u008f\u0090\3\2\2\2\u0090\t\3\2")
        buf.write("\2\2\u0091\u0094\5\16\b\2\u0092\u0094\5\f\7\2\u0093\u0091")
        buf.write("\3\2\2\2\u0093\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\u0096\5\n\6\2\u0096\u0099\3\2\2\2\u0097\u0099\3\2\2\2")
        buf.write("\u0098\u0093\3\2\2\2\u0098\u0097\3\2\2\2\u0099\13\3\2")
        buf.write("\2\2\u009a\u009b\5\24\13\2\u009b\u009c\7\t\2\2\u009c\u00b0")
        buf.write("\3\2\2\2\u009d\u00b0\5\60\31\2\u009e\u009f\5<\37\2\u009f")
        buf.write("\u00a0\7\t\2\2\u00a0\u00b0\3\2\2\2\u00a1\u00b0\5@!\2\u00a2")
        buf.write("\u00a3\5D#\2\u00a3\u00a4\7\t\2\2\u00a4\u00b0\3\2\2\2\u00a5")
        buf.write("\u00a6\5F$\2\u00a6\u00a7\7\t\2\2\u00a7\u00b0\3\2\2\2\u00a8")
        buf.write("\u00b0\5\22\n\2\u00a9\u00aa\5 \21\2\u00aa\u00ab\7\t\2")
        buf.write("\2\u00ab\u00b0\3\2\2\2\u00ac\u00ad\5&\24\2\u00ad\u00ae")
        buf.write("\7\t\2\2\u00ae\u00b0\3\2\2\2\u00af\u009a\3\2\2\2\u00af")
        buf.write("\u009d\3\2\2\2\u00af\u009e\3\2\2\2\u00af\u00a1\3\2\2\2")
        buf.write("\u00af\u00a2\3\2\2\2\u00af\u00a5\3\2\2\2\u00af\u00a8\3")
        buf.write("\2\2\2\u00af\u00a9\3\2\2\2\u00af\u00ac\3\2\2\2\u00b0\r")
        buf.write("\3\2\2\2\u00b1\u00b2\5\20\t\2\u00b2\u00b3\5\16\b\2\u00b3")
        buf.write("\u00b6\3\2\2\2\u00b4\u00b6\5\20\t\2\u00b5\u00b1\3\2\2")
        buf.write("\2\u00b5\u00b4\3\2\2\2\u00b6\17\3\2\2\2\u00b7\u00b8\7")
        buf.write("\t\2\2\u00b8\21\3\2\2\2\u00b9\u00ba\7\13\2\2\u00ba\u00bb")
        buf.write("\5\16\b\2\u00bb\u00bc\5\n\6\2\u00bc\u00bd\7\f\2\2\u00bd")
        buf.write("\u00be\5\16\b\2\u00be\23\3\2\2\2\u00bf\u00c2\5\26\f\2")
        buf.write("\u00c0\u00c2\5\32\16\2\u00c1\u00bf\3\2\2\2\u00c1\u00c0")
        buf.write("\3\2\2\2\u00c2\25\3\2\2\2\u00c3\u00c4\7\6\2\2\u00c4\u00c5")
        buf.write("\7-\2\2\u00c5\u00c6\7\27\2\2\u00c6\u00d1\5H%\2\u00c7\u00ca")
        buf.write("\5\30\r\2\u00c8\u00ca\7\7\2\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write("\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00ce\7-\2\2")
        buf.write("\u00cc\u00cd\7\27\2\2\u00cd\u00cf\5H%\2\u00ce\u00cc\3")
        buf.write("\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0\u00c3")
        buf.write("\3\2\2\2\u00d0\u00c9\3\2\2\2\u00d1\27\3\2\2\2\u00d2\u00d3")
        buf.write("\t\2\2\2\u00d3\31\3\2\2\2\u00d4\u00d5\5\30\r\2\u00d5\u00d6")
        buf.write("\7-\2\2\u00d6\u00d9\5\34\17\2\u00d7\u00d8\7\27\2\2\u00d8")
        buf.write("\u00da\5H%\2\u00d9\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\33\3\2\2\2\u00db\u00dc\7\32\2\2\u00dc\u00dd\5\36\20\2")
        buf.write("\u00dd\u00de\7\33\2\2\u00de\35\3\2\2\2\u00df\u00e0\5n")
        buf.write("8\2\u00e0\u00e1\7\34\2\2\u00e1\u00e2\5\36\20\2\u00e2\u00e5")
        buf.write("\3\2\2\2\u00e3\u00e5\5n8\2\u00e4\u00df\3\2\2\2\u00e4\u00e3")
        buf.write("\3\2\2\2\u00e5\37\3\2\2\2\u00e6\u00e8\7-\2\2\u00e7\u00e9")
        buf.write("\5^\60\2\u00e8\u00e7\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea\u00eb\7\27\2\2\u00eb\u00ec\5H%\2")
        buf.write("\u00ec!\3\2\2\2\u00ed\u00ee\7\r\2\2\u00ee\u00ef\7-\2\2")
        buf.write("\u00ef\u00f1\7\30\2\2\u00f0\u00f2\5(\25\2\u00f1\u00f0")
        buf.write("\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write("\u00f4\7\31\2\2\u00f4\u00f5\5$\23\2\u00f5#\3\2\2\2\u00f6")
        buf.write("\u00f8\5\16\b\2\u00f7\u00f6\3\2\2\2\u00f7\u00f8\3\2\2")
        buf.write("\2\u00f8\u00f9\3\2\2\2\u00f9\u00fa\5&\24\2\u00fa\u00fb")
        buf.write("\7\t\2\2\u00fb\u0102\3\2\2\2\u00fc\u00fe\5\16\b\2\u00fd")
        buf.write("\u00fc\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\3\2\2\2")
        buf.write("\u00ff\u0102\5\22\n\2\u0100\u0102\5\20\t\2\u0101\u00f7")
        buf.write("\3\2\2\2\u0101\u00fd\3\2\2\2\u0101\u0100\3\2\2\2\u0102")
        buf.write("%\3\2\2\2\u0103\u0105\7\16\2\2\u0104\u0106\5H%\2\u0105")
        buf.write("\u0104\3\2\2\2\u0105\u0106\3\2\2\2\u0106\'\3\2\2\2\u0107")
        buf.write("\u0108\5*\26\2\u0108\u0109\7\34\2\2\u0109\u010a\5(\25")
        buf.write("\2\u010a\u010d\3\2\2\2\u010b\u010d\5*\26\2\u010c\u0107")
        buf.write("\3\2\2\2\u010c\u010b\3\2\2\2\u010d)\3\2\2\2\u010e\u0111")
        buf.write("\5,\27\2\u010f\u0111\5.\30\2\u0110\u010e\3\2\2\2\u0110")
        buf.write("\u010f\3\2\2\2\u0111+\3\2\2\2\u0112\u0113\5\30\r\2\u0113")
        buf.write("\u0114\7-\2\2\u0114-\3\2\2\2\u0115\u0116\5\30\r\2\u0116")
        buf.write("\u0117\7-\2\2\u0117\u0118\5\34\17\2\u0118/\3\2\2\2\u0119")
        buf.write("\u011a\7\17\2\2\u011a\u011b\58\35\2\u011b\u011d\5:\36")
        buf.write("\2\u011c\u011e\5\62\32\2\u011d\u011c\3\2\2\2\u011d\u011e")
        buf.write("\3\2\2\2\u011e\u0120\3\2\2\2\u011f\u0121\5\66\34\2\u0120")
        buf.write("\u011f\3\2\2\2\u0120\u0121\3\2\2\2\u0121\61\3\2\2\2\u0122")
        buf.write("\u0123\5\64\33\2\u0123\u0124\5\62\32\2\u0124\u0127\3\2")
        buf.write("\2\2\u0125\u0127\5\64\33\2\u0126\u0122\3\2\2\2\u0126\u0125")
        buf.write("\3\2\2\2\u0127\63\3\2\2\2\u0128\u0129\7\21\2\2\u0129\u012a")
        buf.write("\58\35\2\u012a\u012b\5:\36\2\u012b\65\3\2\2\2\u012c\u012d")
        buf.write("\7\20\2\2\u012d\u012e\5:\36\2\u012e\67\3\2\2\2\u012f\u0130")
        buf.write("\7\30\2\2\u0130\u0131\5H%\2\u0131\u0132\7\31\2\2\u0132")
        buf.write("9\3\2\2\2\u0133\u0134\5\b\5\2\u0134;\3\2\2\2\u0135\u0136")
        buf.write("\7-\2\2\u0136\u0138\7\30\2\2\u0137\u0139\5> \2\u0138\u0137")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\u013b\7\31\2\2\u013b=\3\2\2\2\u013c\u013d\5H%\2\u013d")
        buf.write("\u013e\7\34\2\2\u013e\u013f\5> \2\u013f\u0142\3\2\2\2")
        buf.write("\u0140\u0142\5H%\2\u0141\u013c\3\2\2\2\u0141\u0140\3\2")
        buf.write("\2\2\u0142?\3\2\2\2\u0143\u0144\7\22\2\2\u0144\u0145\7")
        buf.write("-\2\2\u0145\u0146\7\23\2\2\u0146\u0147\5H%\2\u0147\u0148")
        buf.write("\7\24\2\2\u0148\u0149\5H%\2\u0149\u014a\5B\"\2\u014aA")
        buf.write("\3\2\2\2\u014b\u014c\5\b\5\2\u014cC\3\2\2\2\u014d\u014e")
        buf.write("\7\25\2\2\u014eE\3\2\2\2\u014f\u0150\7\26\2\2\u0150G\3")
        buf.write("\2\2\2\u0151\u0152\5J&\2\u0152I\3\2\2\2\u0153\u0154\5")
        buf.write("L\'\2\u0154\u0155\7+\2\2\u0155\u0156\5L\'\2\u0156\u0159")
        buf.write("\3\2\2\2\u0157\u0159\5L\'\2\u0158\u0153\3\2\2\2\u0158")
        buf.write("\u0157\3\2\2\2\u0159K\3\2\2\2\u015a\u015b\5N(\2\u015b")
        buf.write("\u015c\5b\62\2\u015c\u015d\5N(\2\u015d\u0160\3\2\2\2\u015e")
        buf.write("\u0160\5N(\2\u015f\u015a\3\2\2\2\u015f\u015e\3\2\2\2\u0160")
        buf.write("M\3\2\2\2\u0161\u0162\b(\1\2\u0162\u0163\5P)\2\u0163\u016a")
        buf.write("\3\2\2\2\u0164\u0165\f\4\2\2\u0165\u0166\5h\65\2\u0166")
        buf.write("\u0167\5P)\2\u0167\u0169\3\2\2\2\u0168\u0164\3\2\2\2\u0169")
        buf.write("\u016c\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2")
        buf.write("\u016bO\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u016e\b)\1\2")
        buf.write("\u016e\u016f\5R*\2\u016f\u0176\3\2\2\2\u0170\u0171\f\4")
        buf.write("\2\2\u0171\u0172\5d\63\2\u0172\u0173\5R*\2\u0173\u0175")
        buf.write("\3\2\2\2\u0174\u0170\3\2\2\2\u0175\u0178\3\2\2\2\u0176")
        buf.write("\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177Q\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0179\u017a\b*\1\2\u017a\u017b\5T+\2\u017b")
        buf.write("\u0182\3\2\2\2\u017c\u017d\f\4\2\2\u017d\u017e\5f\64\2")
        buf.write("\u017e\u017f\5T+\2\u017f\u0181\3\2\2\2\u0180\u017c\3\2")
        buf.write("\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183")
        buf.write("\3\2\2\2\u0183S\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186")
        buf.write("\7\"\2\2\u0186\u0189\5T+\2\u0187\u0189\5V,\2\u0188\u0185")
        buf.write("\3\2\2\2\u0188\u0187\3\2\2\2\u0189U\3\2\2\2\u018a\u018b")
        buf.write("\5d\63\2\u018b\u018c\5V,\2\u018c\u018f\3\2\2\2\u018d\u018f")
        buf.write("\5X-\2\u018e\u018a\3\2\2\2\u018e\u018d\3\2\2\2\u018fW")
        buf.write("\3\2\2\2\u0190\u0191\7\30\2\2\u0191\u0192\5H%\2\u0192")
        buf.write("\u0193\7\31\2\2\u0193\u0196\3\2\2\2\u0194\u0196\5Z.\2")
        buf.write("\u0195\u0190\3\2\2\2\u0195\u0194\3\2\2\2\u0196Y\3\2\2")
        buf.write("\2\u0197\u019c\5j\66\2\u0198\u019c\5<\37\2\u0199\u019c")
        buf.write("\7-\2\2\u019a\u019c\5\\/\2\u019b\u0197\3\2\2\2\u019b\u0198")
        buf.write("\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019a\3\2\2\2\u019c")
        buf.write("[\3\2\2\2\u019d\u01a0\5<\37\2\u019e\u01a0\7-\2\2\u019f")
        buf.write("\u019d\3\2\2\2\u019f\u019e\3\2\2\2\u019f\u01a0\3\2\2\2")
        buf.write("\u01a0\u01a1\3\2\2\2\u01a1\u01a2\5^\60\2\u01a2]\3\2\2")
        buf.write("\2\u01a3\u01a4\7\32\2\2\u01a4\u01a5\5`\61\2\u01a5\u01a6")
        buf.write("\7\33\2\2\u01a6_\3\2\2\2\u01a7\u01a8\5H%\2\u01a8\u01a9")
        buf.write("\7\34\2\2\u01a9\u01aa\5`\61\2\u01aa\u01ad\3\2\2\2\u01ab")
        buf.write("\u01ad\5H%\2\u01ac\u01a7\3\2\2\2\u01ac\u01ab\3\2\2\2\u01ad")
        buf.write("a\3\2\2\2\u01ae\u01af\t\3\2\2\u01afc\3\2\2\2\u01b0\u01b1")
        buf.write("\t\4\2\2\u01b1e\3\2\2\2\u01b2\u01b3\t\5\2\2\u01b3g\3\2")
        buf.write("\2\2\u01b4\u01b5\t\6\2\2\u01b5i\3\2\2\2\u01b6\u01b7\t")
        buf.write("\7\2\2\u01b7k\3\2\2\2\u01b8\u01b9\7\60\2\2\u01b9m\3\2")
        buf.write("\2\2\u01ba\u01bb\7.\2\2\u01bbo\3\2\2\2\u01bc\u01bd\7/")
        buf.write("\2\2\u01bdq\3\2\2\2+sw\177\u0083\u0088\u008b\u008f\u0093")
        buf.write("\u0098\u00af\u00b5\u00c1\u00c9\u00ce\u00d0\u00d9\u00e4")
        buf.write("\u00e8\u00f1\u00f7\u00fd\u0101\u0105\u010c\u0110\u011d")
        buf.write("\u0120\u0126\u0138\u0141\u0158\u015f\u016a\u0176\u0182")
        buf.write("\u0188\u018e\u0195\u019b\u019f\u01ac")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'number'", "'bool'", "'string'", "'var'", 
                     "'dynamic'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'begin'", "'end'", "'func'", "'return'", "'if'", "'else'", 
                     "'elif'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'<-'", "'('", "')'", "'['", "']'", "','", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", "'='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'...'", "'=='" ]

    symbolicNames = [ "<INVALID>", "NUMBER_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", 
                      "VAR", "DYNAMIC", "COMMENT", "NEWLINE", "WHITESPACE", 
                      "BEGIN", "END", "FUNC", "RETURN", "IF", "ELSE", "ELIF", 
                      "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "ASSIGN", 
                      "LPAREN", "RPAREN", "LBRACK", "RBRACK", "COMMA", "PLUS", 
                      "MINUS", "MULTIPLY", "DIVIDE", "MOD", "NOT", "AND", 
                      "OR", "EQUAL", "NOT_EQUAL", "LT", "LE", "GT", "GE", 
                      "CONCATE", "STRING_EQUAL", "IDENTIFIER", "NUMBER_LIT", 
                      "BOOLEAN_LIT", "STRING_LIT", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declaration_list = 1
    RULE_declaration = 2
    RULE_local_statement_single = 3
    RULE_local_statement_list = 4
    RULE_local_statement = 5
    RULE_newline_list = 6
    RULE_newline = 7
    RULE_block_statement = 8
    RULE_variable_declaration_statement = 9
    RULE_basic_variable_declaration = 10
    RULE_basic_type = 11
    RULE_array_declaration = 12
    RULE_array_dimension = 13
    RULE_array_dimension_list = 14
    RULE_assignment_statement = 15
    RULE_function_declaration = 16
    RULE_function_body = 17
    RULE_return_statement = 18
    RULE_parameter_part_recursive = 19
    RULE_parameter_declaration = 20
    RULE_basic_parameter_declaration = 21
    RULE_array_parameter_declaration = 22
    RULE_if_statement = 23
    RULE_elif_recursive_statement = 24
    RULE_elif_statement = 25
    RULE_else_statement = 26
    RULE_branch_condition = 27
    RULE_branch_body = 28
    RULE_function_call_statement = 29
    RULE_argument_part = 30
    RULE_for_statement = 31
    RULE_loop_body = 32
    RULE_break_statement = 33
    RULE_continue_statement = 34
    RULE_expression = 35
    RULE_string_expression = 36
    RULE_relational_expression = 37
    RULE_logical_expression = 38
    RULE_adding_expression = 39
    RULE_multiplying_expression = 40
    RULE_negation_expression = 41
    RULE_sign_expression = 42
    RULE_parenthesis_expression = 43
    RULE_operand = 44
    RULE_array_literal = 45
    RULE_element_expression = 46
    RULE_index_operator = 47
    RULE_relational_operator = 48
    RULE_additive_operator = 49
    RULE_multiplicative_operator = 50
    RULE_logic_operator = 51
    RULE_literal = 52
    RULE_string_literal = 53
    RULE_number_literal = 54
    RULE_boolean_literal = 55

    ruleNames =  [ "program", "declaration_list", "declaration", "local_statement_single", 
                   "local_statement_list", "local_statement", "newline_list", 
                   "newline", "block_statement", "variable_declaration_statement", 
                   "basic_variable_declaration", "basic_type", "array_declaration", 
                   "array_dimension", "array_dimension_list", "assignment_statement", 
                   "function_declaration", "function_body", "return_statement", 
                   "parameter_part_recursive", "parameter_declaration", 
                   "basic_parameter_declaration", "array_parameter_declaration", 
                   "if_statement", "elif_recursive_statement", "elif_statement", 
                   "else_statement", "branch_condition", "branch_body", 
                   "function_call_statement", "argument_part", "for_statement", 
                   "loop_body", "break_statement", "continue_statement", 
                   "expression", "string_expression", "relational_expression", 
                   "logical_expression", "adding_expression", "multiplying_expression", 
                   "negation_expression", "sign_expression", "parenthesis_expression", 
                   "operand", "array_literal", "element_expression", "index_operator", 
                   "relational_operator", "additive_operator", "multiplicative_operator", 
                   "logic_operator", "literal", "string_literal", "number_literal", 
                   "boolean_literal" ]

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
    FUNC=11
    RETURN=12
    IF=13
    ELSE=14
    ELIF=15
    FOR=16
    UNTIL=17
    BY=18
    BREAK=19
    CONTINUE=20
    ASSIGN=21
    LPAREN=22
    RPAREN=23
    LBRACK=24
    RBRACK=25
    COMMA=26
    PLUS=27
    MINUS=28
    MULTIPLY=29
    DIVIDE=30
    MOD=31
    NOT=32
    AND=33
    OR=34
    EQUAL=35
    NOT_EQUAL=36
    LT=37
    LE=38
    GT=39
    GE=40
    CONCATE=41
    STRING_EQUAL=42
    IDENTIFIER=43
    NUMBER_LIT=44
    BOOLEAN_LIT=45
    STRING_LIT=46
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

        def declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


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
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 112
                self.newline_list()


            self.state = 115
            self.declaration_list()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 116
                self.newline_list()


            self.state = 119
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationContext,0)


        def declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_list" ):
                return visitor.visitDeclaration_list(self)
            else:
                return visitor.visitChildren(self)




    def declaration_list(self):

        localctx = ZCodeParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration_list)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.declaration()
                self.state = 122
                self.declaration_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Function_declarationContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def variable_declaration_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declaration_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.function_declaration()
                self.state = 129
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 128
                    self.newline_list()


                pass
            elif token in [ZCodeParser.NUMBER_TYPE, ZCodeParser.BOOLEAN_TYPE, ZCodeParser.STRING_TYPE, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.variable_declaration_statement()
                self.state = 132
                self.newline_list()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_statement_singleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statementContext,0)


        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_local_statement_single

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_statement_single" ):
                return visitor.visitLocal_statement_single(self)
            else:
                return visitor.visitChildren(self)




    def local_statement_single(self):

        localctx = ZCodeParser.Local_statement_singleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_local_statement_single)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 136
                self.newline_list()


            self.state = 139
            self.local_statement()
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 140
                self.newline_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statement_listContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def local_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_local_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_statement_list" ):
                return visitor.visitLocal_statement_list(self)
            else:
                return visitor.visitChildren(self)




    def local_statement_list(self):

        localctx = ZCodeParser.Local_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_local_statement_list)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_TYPE, ZCodeParser.BOOLEAN_TYPE, ZCodeParser.STRING_TYPE, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.NEWLINE, ZCodeParser.BEGIN, ZCodeParser.RETURN, ZCodeParser.IF, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NEWLINE]:
                    self.state = 143
                    self.newline_list()
                    pass
                elif token in [ZCodeParser.NUMBER_TYPE, ZCodeParser.BOOLEAN_TYPE, ZCodeParser.STRING_TYPE, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BEGIN, ZCodeParser.RETURN, ZCodeParser.IF, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IDENTIFIER]:
                    self.state = 144
                    self.local_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 147
                self.local_statement_list()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declaration_statementContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def function_call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_local_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_statement" ):
                return visitor.visitLocal_statement(self)
            else:
                return visitor.visitChildren(self)




    def local_statement(self):

        localctx = ZCodeParser.Local_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_local_statement)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.variable_declaration_statement()
                self.state = 153
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.function_call_statement()
                self.state = 157
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 159
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 160
                self.break_statement()
                self.state = 161
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 163
                self.continue_statement()
                self.state = 164
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 166
                self.block_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 167
                self.assignment_statement()
                self.state = 168
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 170
                self.return_statement()
                self.state = 171
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_list" ):
                return visitor.visitNewline_list(self)
            else:
                return visitor.visitChildren(self)




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_newline_list)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.newline()
                self.state = 176
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.newline()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_newline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline" ):
                return visitor.visitNewline(self)
            else:
                return visitor.visitChildren(self)




    def newline(self):

        localctx = ZCodeParser.NewlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def local_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statement_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(ZCodeParser.BEGIN)
            self.state = 184
            self.newline_list()
            self.state = 185
            self.local_statement_list()
            self.state = 186
            self.match(ZCodeParser.END)
            self.state = 187
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_variable_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Basic_variable_declarationContext,0)


        def array_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Array_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_declaration_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration_statement" ):
                return visitor.visitVariable_declaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration_statement(self):

        localctx = ZCodeParser.Variable_declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_variable_declaration_statement)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.basic_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.array_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def basic_type(self):
            return self.getTypedRuleContext(ZCodeParser.Basic_typeContext,0)


        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_basic_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_variable_declaration" ):
                return visitor.visitBasic_variable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def basic_variable_declaration(self):

        localctx = ZCodeParser.Basic_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_basic_variable_declaration)
        self._la = 0 # Token type
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(ZCodeParser.VAR)
                self.state = 194
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 195
                self.match(ZCodeParser.ASSIGN)
                self.state = 196
                self.expression()
                pass
            elif token in [ZCodeParser.NUMBER_TYPE, ZCodeParser.BOOLEAN_TYPE, ZCodeParser.STRING_TYPE, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NUMBER_TYPE, ZCodeParser.BOOLEAN_TYPE, ZCodeParser.STRING_TYPE]:
                    self.state = 197
                    self.basic_type()
                    pass
                elif token in [ZCodeParser.DYNAMIC]:
                    self.state = 198
                    self.match(ZCodeParser.DYNAMIC)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 201
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 202
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 203
                    self.expression()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_TYPE(self):
            return self.getToken(ZCodeParser.NUMBER_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(ZCodeParser.STRING_TYPE, 0)

        def BOOLEAN_TYPE(self):
            return self.getToken(ZCodeParser.BOOLEAN_TYPE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_basic_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_type" ):
                return visitor.visitBasic_type(self)
            else:
                return visitor.visitChildren(self)




    def basic_type(self):

        localctx = ZCodeParser.Basic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_basic_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER_TYPE) | (1 << ZCodeParser.BOOLEAN_TYPE) | (1 << ZCodeParser.STRING_TYPE))) != 0)):
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


    class Array_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_type(self):
            return self.getTypedRuleContext(ZCodeParser.Basic_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_dimension(self):
            return self.getTypedRuleContext(ZCodeParser.Array_dimensionContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declaration" ):
                return visitor.visitArray_declaration(self)
            else:
                return visitor.visitChildren(self)




    def array_declaration(self):

        localctx = ZCodeParser.Array_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.basic_type()
            self.state = 211
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 212
            self.array_dimension()
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 213
                self.match(ZCodeParser.ASSIGN)
                self.state = 214
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_dimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def array_dimension_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_dimension_listContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_dimension" ):
                return visitor.visitArray_dimension(self)
            else:
                return visitor.visitChildren(self)




    def array_dimension(self):

        localctx = ZCodeParser.Array_dimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_array_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(ZCodeParser.LBRACK)
            self.state = 218
            self.array_dimension_list()
            self.state = 219
            self.match(ZCodeParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_dimension_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Number_literalContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def array_dimension_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_dimension_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_dimension_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_dimension_list" ):
                return visitor.visitArray_dimension_list(self)
            else:
                return visitor.visitChildren(self)




    def array_dimension_list(self):

        localctx = ZCodeParser.Array_dimension_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_dimension_list)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.number_literal()
                self.state = 222
                self.match(ZCodeParser.COMMA)
                self.state = 223
                self.array_dimension_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.number_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def element_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Element_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assignment_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.LBRACK:
                self.state = 229
                self.element_expression()


            self.state = 232
            self.match(ZCodeParser.ASSIGN)
            self.state = 233
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def function_body(self):
            return self.getTypedRuleContext(ZCodeParser.Function_bodyContext,0)


        def parameter_part_recursive(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_part_recursiveContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = ZCodeParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(ZCodeParser.FUNC)
            self.state = 236
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 237
            self.match(ZCodeParser.LPAREN)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER_TYPE) | (1 << ZCodeParser.BOOLEAN_TYPE) | (1 << ZCodeParser.STRING_TYPE))) != 0):
                self.state = 238
                self.parameter_part_recursive()


            self.state = 241
            self.match(ZCodeParser.RPAREN)
            self.state = 242
            self.function_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def newline(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_body" ):
                return visitor.visitFunction_body(self)
            else:
                return visitor.visitChildren(self)




    def function_body(self):

        localctx = ZCodeParser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_function_body)
        self._la = 0 # Token type
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 244
                    self.newline_list()


                self.state = 247
                self.return_statement()
                self.state = 248
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 250
                    self.newline_list()


                self.state = 253
                self.block_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
                self.newline()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(ZCodeParser.RETURN)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.LBRACK) | (1 << ZCodeParser.PLUS) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.BOOLEAN_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 258
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_part_recursiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_declarationContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def parameter_part_recursive(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_part_recursiveContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_part_recursive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_part_recursive" ):
                return visitor.visitParameter_part_recursive(self)
            else:
                return visitor.visitChildren(self)




    def parameter_part_recursive(self):

        localctx = ZCodeParser.Parameter_part_recursiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parameter_part_recursive)
        try:
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.parameter_declaration()
                self.state = 262
                self.match(ZCodeParser.COMMA)
                self.state = 263
                self.parameter_part_recursive()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.parameter_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_parameter_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Basic_parameter_declarationContext,0)


        def array_parameter_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Array_parameter_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_declaration" ):
                return visitor.visitParameter_declaration(self)
            else:
                return visitor.visitChildren(self)




    def parameter_declaration(self):

        localctx = ZCodeParser.Parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_parameter_declaration)
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.basic_parameter_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.array_parameter_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_parameter_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_type(self):
            return self.getTypedRuleContext(ZCodeParser.Basic_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_basic_parameter_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_parameter_declaration" ):
                return visitor.visitBasic_parameter_declaration(self)
            else:
                return visitor.visitChildren(self)




    def basic_parameter_declaration(self):

        localctx = ZCodeParser.Basic_parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_basic_parameter_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.basic_type()
            self.state = 273
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_parameter_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_type(self):
            return self.getTypedRuleContext(ZCodeParser.Basic_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_dimension(self):
            return self.getTypedRuleContext(ZCodeParser.Array_dimensionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_parameter_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_parameter_declaration" ):
                return visitor.visitArray_parameter_declaration(self)
            else:
                return visitor.visitChildren(self)




    def array_parameter_declaration(self):

        localctx = ZCodeParser.Array_parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_array_parameter_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.basic_type()
            self.state = 276
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 277
            self.array_dimension()
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

        def branch_condition(self):
            return self.getTypedRuleContext(ZCodeParser.Branch_conditionContext,0)


        def branch_body(self):
            return self.getTypedRuleContext(ZCodeParser.Branch_bodyContext,0)


        def elif_recursive_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_recursive_statementContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Else_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(ZCodeParser.IF)
            self.state = 280
            self.branch_condition()
            self.state = 281
            self.branch_body()
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 282
                self.elif_recursive_statement()


            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 285
                self.else_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_recursive_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statementContext,0)


        def elif_recursive_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_recursive_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_recursive_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_recursive_statement" ):
                return visitor.visitElif_recursive_statement(self)
            else:
                return visitor.visitChildren(self)




    def elif_recursive_statement(self):

        localctx = ZCodeParser.Elif_recursive_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elif_recursive_statement)
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.elif_statement()
                self.state = 289
                self.elif_recursive_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.elif_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def branch_condition(self):
            return self.getTypedRuleContext(ZCodeParser.Branch_conditionContext,0)


        def branch_body(self):
            return self.getTypedRuleContext(ZCodeParser.Branch_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_statement" ):
                return visitor.visitElif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elif_statement(self):

        localctx = ZCodeParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(ZCodeParser.ELIF)
            self.state = 295
            self.branch_condition()
            self.state = 296
            self.branch_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def branch_body(self):
            return self.getTypedRuleContext(ZCodeParser.Branch_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = ZCodeParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(ZCodeParser.ELSE)
            self.state = 299
            self.branch_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Branch_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_branch_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBranch_condition" ):
                return visitor.visitBranch_condition(self)
            else:
                return visitor.visitChildren(self)




    def branch_condition(self):

        localctx = ZCodeParser.Branch_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_branch_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(ZCodeParser.LPAREN)
            self.state = 302
            self.expression()
            self.state = 303
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Branch_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_statement_single(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statement_singleContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_branch_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBranch_body" ):
                return visitor.visitBranch_body(self)
            else:
                return visitor.visitChildren(self)




    def branch_body(self):

        localctx = ZCodeParser.Branch_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_branch_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.local_statement_single()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_statementContext(ParserRuleContext):
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

        def argument_part(self):
            return self.getTypedRuleContext(ZCodeParser.Argument_partContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_statement" ):
                return visitor.visitFunction_call_statement(self)
            else:
                return visitor.visitChildren(self)




    def function_call_statement(self):

        localctx = ZCodeParser.Function_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_function_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 308
            self.match(ZCodeParser.LPAREN)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.LBRACK) | (1 << ZCodeParser.PLUS) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.BOOLEAN_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 309
                self.argument_part()


            self.state = 312
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def argument_part(self):
            return self.getTypedRuleContext(ZCodeParser.Argument_partContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argument_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_part" ):
                return visitor.visitArgument_part(self)
            else:
                return visitor.visitChildren(self)




    def argument_part(self):

        localctx = ZCodeParser.Argument_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_argument_part)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.expression()
                self.state = 315
                self.match(ZCodeParser.COMMA)
                self.state = 316
                self.argument_part()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def loop_body(self):
            return self.getTypedRuleContext(ZCodeParser.Loop_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(ZCodeParser.FOR)
            self.state = 322
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 323
            self.match(ZCodeParser.UNTIL)
            self.state = 324
            self.expression()
            self.state = 325
            self.match(ZCodeParser.BY)
            self.state = 326
            self.expression()
            self.state = 327
            self.loop_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_statement_single(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statement_singleContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_loop_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_body" ):
                return visitor.visitLoop_body(self)
            else:
                return visitor.visitChildren(self)




    def loop_body(self):

        localctx = ZCodeParser.Loop_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_loop_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.local_statement_single()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(ZCodeParser.CONTINUE)
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

        def string_expression(self):
            return self.getTypedRuleContext(ZCodeParser.String_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.string_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Relational_expressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Relational_expressionContext,i)


        def CONCATE(self):
            return self.getToken(ZCodeParser.CONCATE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_string_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_expression" ):
                return visitor.visitString_expression(self)
            else:
                return visitor.visitChildren(self)




    def string_expression(self):

        localctx = ZCodeParser.String_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_string_expression)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.relational_expression()
                self.state = 338
                self.match(ZCodeParser.CONCATE)
                self.state = 339
                self.relational_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.relational_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Logical_expressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Logical_expressionContext,i)


        def relational_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Relational_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_relational_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expression" ):
                return visitor.visitRelational_expression(self)
            else:
                return visitor.visitChildren(self)




    def relational_expression(self):

        localctx = ZCodeParser.Relational_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_relational_expression)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.logical_expression(0)
                self.state = 345
                self.relational_operator()
                self.state = 346
                self.logical_expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.logical_expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Adding_expressionContext,0)


        def logical_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Logical_expressionContext,0)


        def logic_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Logic_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_logical_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expression" ):
                return visitor.visitLogical_expression(self)
            else:
                return visitor.visitChildren(self)



    def logical_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Logical_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_logical_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.adding_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 360
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 354
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 355
                    self.logic_operator()
                    self.state = 356
                    self.adding_expression(0) 
                self.state = 362
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Adding_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Multiplying_expressionContext,0)


        def adding_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Adding_expressionContext,0)


        def additive_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Additive_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_adding_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_expression" ):
                return visitor.visitAdding_expression(self)
            else:
                return visitor.visitChildren(self)



    def adding_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Adding_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_adding_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.multiplying_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 372
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Adding_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expression)
                    self.state = 366
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 367
                    self.additive_operator()
                    self.state = 368
                    self.multiplying_expression(0) 
                self.state = 374
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negation_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Negation_expressionContext,0)


        def multiplying_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Multiplying_expressionContext,0)


        def multiplicative_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Multiplicative_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_multiplying_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_expression" ):
                return visitor.visitMultiplying_expression(self)
            else:
                return visitor.visitChildren(self)



    def multiplying_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Multiplying_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_multiplying_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.negation_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Multiplying_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
                    self.state = 378
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 379
                    self.multiplicative_operator()
                    self.state = 380
                    self.negation_expression() 
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Negation_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def negation_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Negation_expressionContext,0)


        def sign_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_negation_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegation_expression" ):
                return visitor.visitNegation_expression(self)
            else:
                return visitor.visitChildren(self)




    def negation_expression(self):

        localctx = ZCodeParser.Negation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_negation_expression)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(ZCodeParser.NOT)
                self.state = 388
                self.negation_expression()
                pass
            elif token in [ZCodeParser.LPAREN, ZCodeParser.LBRACK, ZCodeParser.PLUS, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.BOOLEAN_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.sign_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Additive_operatorContext,0)


        def sign_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_expressionContext,0)


        def parenthesis_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Parenthesis_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expression" ):
                return visitor.visitSign_expression(self)
            else:
                return visitor.visitChildren(self)




    def sign_expression(self):

        localctx = ZCodeParser.Sign_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_sign_expression)
        try:
            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.PLUS, ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.additive_operator()
                self.state = 393
                self.sign_expression()
                pass
            elif token in [ZCodeParser.LPAREN, ZCodeParser.LBRACK, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.BOOLEAN_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.parenthesis_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parenthesis_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parenthesis_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis_expression" ):
                return visitor.visitParenthesis_expression(self)
            else:
                return visitor.visitChildren(self)




    def parenthesis_expression(self):

        localctx = ZCodeParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_parenthesis_expression)
        try:
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(ZCodeParser.LPAREN)
                self.state = 399
                self.expression()
                self.state = 400
                self.match(ZCodeParser.RPAREN)
                pass
            elif token in [ZCodeParser.LBRACK, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.BOOLEAN_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def function_call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_statementContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_operand)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.function_call_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 407
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 408
                self.array_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Element_expressionContext,0)


        def function_call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_statementContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 411
                self.function_call_statement()

            elif la_ == 2:
                self.state = 412
                self.match(ZCodeParser.IDENTIFIER)


            self.state = 415
            self.element_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_element_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expression" ):
                return visitor.visitElement_expression(self)
            else:
                return visitor.visitChildren(self)




    def element_expression(self):

        localctx = ZCodeParser.Element_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_element_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(ZCodeParser.LBRACK)
            self.state = 418
            self.index_operator()
            self.state = 419
            self.match(ZCodeParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = ZCodeParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_index_operator)
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.expression()
                self.state = 422
                self.match(ZCodeParser.COMMA)
                self.state = 423
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.expression()
                pass


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

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def STRING_EQUAL(self):
            return self.getToken(ZCodeParser.STRING_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relational_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_operator" ):
                return visitor.visitRelational_operator(self)
            else:
                return visitor.visitChildren(self)




    def relational_operator(self):

        localctx = ZCodeParser.Relational_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GE) | (1 << ZCodeParser.STRING_EQUAL))) != 0)):
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


    class Additive_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_additive_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive_operator" ):
                return visitor.visitAdditive_operator(self)
            else:
                return visitor.visitChildren(self)




    def additive_operator(self):

        localctx = ZCodeParser.Additive_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_additive_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
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


    class Multiplicative_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTIPLY(self):
            return self.getToken(ZCodeParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(ZCodeParser.DIVIDE, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_multiplicative_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative_operator" ):
                return visitor.visitMultiplicative_operator(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative_operator(self):

        localctx = ZCodeParser.Multiplicative_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_multiplicative_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULTIPLY) | (1 << ZCodeParser.DIVIDE) | (1 << ZCodeParser.MOD))) != 0)):
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


    class Logic_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logic_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_operator" ):
                return visitor.visitLogic_operator(self)
            else:
                return visitor.visitChildren(self)




    def logic_operator(self):

        localctx = ZCodeParser.Logic_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_logic_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(ZCodeParser.BOOLEAN_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.BOOLEAN_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0)):
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


    class String_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_string_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_literal" ):
                return visitor.visitString_literal(self)
            else:
                return visitor.visitChildren(self)




    def string_literal(self):

        localctx = ZCodeParser.String_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(ZCodeParser.STRING_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_number_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_literal" ):
                return visitor.visitNumber_literal(self)
            else:
                return visitor.visitChildren(self)




    def number_literal(self):

        localctx = ZCodeParser.Number_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_number_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(ZCodeParser.NUMBER_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN_LIT(self):
            return self.getToken(ZCodeParser.BOOLEAN_LIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_boolean_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_literal" ):
                return visitor.visitBoolean_literal(self)
            else:
                return visitor.visitChildren(self)




    def boolean_literal(self):

        localctx = ZCodeParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_boolean_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(ZCodeParser.BOOLEAN_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[38] = self.logical_expression_sempred
        self._predicates[39] = self.adding_expression_sempred
        self._predicates[40] = self.multiplying_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def adding_expression_sempred(self, localctx:Adding_expressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expression_sempred(self, localctx:Multiplying_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




