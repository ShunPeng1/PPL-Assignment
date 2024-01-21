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
        buf.write("\u01e4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\3\2\5\2z\n\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0082")
        buf.write("\n\3\3\4\3\4\3\4\5\4\u0087\n\4\3\5\3\5\3\5\3\5\5\5\u008d")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0099")
        buf.write("\n\6\3\7\3\7\3\7\3\7\5\7\u009f\n\7\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\5\n\u00ab\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00b5\n\13\3\13\3\13\3\13\5")
        buf.write("\13\u00ba\n\13\5\13\u00bc\n\13\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u00c5\n\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00d0\n\17\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\5\20\u00d9\n\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u00e5\n\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\5\22\u00ed\n\22\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\5\25\u00fb\n\25\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u0101\n\25\5\25\u0103\n\25\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u0109\n\26\3\27\3\27\3\27\3\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\5\30\u0114\n\30\3\31\3\31\5\31")
        buf.write("\u0118\n\31\3\32\3\32\5\32\u011c\n\32\3\32\3\32\3\33\3")
        buf.write("\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u0128\n\34\3\34")
        buf.write("\5\34\u012b\n\34\3\35\3\35\3\35\3\35\5\35\u0131\n\35\3")
        buf.write("\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \5")
        buf.write(" \u0140\n \3!\3!\3!\5!\u0145\n!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\3\"\5\"\u014e\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3")
        buf.write("$\3$\3$\5$\u015e\n$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3")
        buf.write("(\3(\3(\5(\u016d\n(\3)\3)\3)\3)\3)\5)\u0174\n)\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\7*\u017d\n*\f*\16*\u0180\13*\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\7+\u0189\n+\f+\16+\u018c\13+\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\7,\u0195\n,\f,\16,\u0198\13,\3-\3-\3-\5-\u019d")
        buf.write("\n-\3.\3.\3.\3.\5.\u01a3\n.\3/\5/\u01a6\n/\3/\3/\5/\u01aa")
        buf.write("\n/\3\60\3\60\3\60\3\60\5\60\u01b0\n\60\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\7\61\u01bc\n\61\f")
        buf.write("\61\16\61\u01bf\13\61\3\62\3\62\3\62\3\62\3\62\5\62\u01c6")
        buf.write("\n\62\3\63\3\63\3\63\5\63\u01cb\n\63\3\64\3\64\3\64\3")
        buf.write("\64\3\64\5\64\u01d2\n\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\38\38\39\39\3:\3:\3;\3;\3<\3<\3<\2\6RTV`=\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@")
        buf.write("BDFHJLNPRTVXZ\\^`bdfhjlnprtv\2\t\3\2\b\t\3\2\3\5\4\2%")
        buf.write("*,,\3\2\35\36\3\2\37!\3\2#$\3\2.\60\2\u01e0\2y\3\2\2\2")
        buf.write("\4\u0081\3\2\2\2\6\u0086\3\2\2\2\b\u008c\3\2\2\2\n\u0098")
        buf.write("\3\2\2\2\f\u009e\3\2\2\2\16\u00a0\3\2\2\2\20\u00a2\3\2")
        buf.write("\2\2\22\u00aa\3\2\2\2\24\u00bb\3\2\2\2\26\u00bd\3\2\2")
        buf.write("\2\30\u00bf\3\2\2\2\32\u00c6\3\2\2\2\34\u00cf\3\2\2\2")
        buf.write("\36\u00d8\3\2\2\2 \u00e4\3\2\2\2\"\u00ec\3\2\2\2$\u00ee")
        buf.write("\3\2\2\2&\u00f2\3\2\2\2(\u00f6\3\2\2\2*\u0108\3\2\2\2")
        buf.write(",\u010a\3\2\2\2.\u0113\3\2\2\2\60\u0117\3\2\2\2\62\u011b")
        buf.write("\3\2\2\2\64\u011f\3\2\2\2\66\u0123\3\2\2\28\u0130\3\2")
        buf.write("\2\2:\u0132\3\2\2\2<\u0136\3\2\2\2>\u013f\3\2\2\2@\u0141")
        buf.write("\3\2\2\2B\u014d\3\2\2\2D\u014f\3\2\2\2F\u015d\3\2\2\2")
        buf.write("H\u015f\3\2\2\2J\u0162\3\2\2\2L\u0165\3\2\2\2N\u016c\3")
        buf.write("\2\2\2P\u0173\3\2\2\2R\u0175\3\2\2\2T\u0181\3\2\2\2V\u018d")
        buf.write("\3\2\2\2X\u019c\3\2\2\2Z\u01a2\3\2\2\2\\\u01a9\3\2\2\2")
        buf.write("^\u01af\3\2\2\2`\u01b1\3\2\2\2b\u01c5\3\2\2\2d\u01ca\3")
        buf.write("\2\2\2f\u01d1\3\2\2\2h\u01d3\3\2\2\2j\u01d5\3\2\2\2l\u01d7")
        buf.write("\3\2\2\2n\u01d9\3\2\2\2p\u01db\3\2\2\2r\u01dd\3\2\2\2")
        buf.write("t\u01df\3\2\2\2v\u01e1\3\2\2\2xz\5\4\3\2yx\3\2\2\2yz\3")
        buf.write("\2\2\2z{\3\2\2\2{|\7\2\2\3|\3\3\2\2\2}~\5\6\4\2~\177\5")
        buf.write("\4\3\2\177\u0082\3\2\2\2\u0080\u0082\5\6\4\2\u0081}\3")
        buf.write("\2\2\2\u0081\u0080\3\2\2\2\u0082\5\3\2\2\2\u0083\u0087")
        buf.write("\5(\25\2\u0084\u0087\5\22\n\2\u0085\u0087\5\f\7\2\u0086")
        buf.write("\u0083\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2")
        buf.write("\u0087\7\3\2\2\2\u0088\u0089\5\n\6\2\u0089\u008a\5\b\5")
        buf.write("\2\u008a\u008d\3\2\2\2\u008b\u008d\5\n\6\2\u008c\u0088")
        buf.write("\3\2\2\2\u008c\u008b\3\2\2\2\u008d\t\3\2\2\2\u008e\u0099")
        buf.write("\5\22\n\2\u008f\u0099\5\66\34\2\u0090\u0099\5@!\2\u0091")
        buf.write("\u0099\5D#\2\u0092\u0099\5H%\2\u0093\u0099\5J&\2\u0094")
        buf.write("\u0099\5\20\t\2\u0095\u0099\5\"\22\2\u0096\u0099\5,\27")
        buf.write("\2\u0097\u0099\5\f\7\2\u0098\u008e\3\2\2\2\u0098\u008f")
        buf.write("\3\2\2\2\u0098\u0090\3\2\2\2\u0098\u0091\3\2\2\2\u0098")
        buf.write("\u0092\3\2\2\2\u0098\u0093\3\2\2\2\u0098\u0094\3\2\2\2")
        buf.write("\u0098\u0095\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0097\3")
        buf.write("\2\2\2\u0099\13\3\2\2\2\u009a\u009b\5\16\b\2\u009b\u009c")
        buf.write("\5\f\7\2\u009c\u009f\3\2\2\2\u009d\u009f\5\16\b\2\u009e")
        buf.write("\u009a\3\2\2\2\u009e\u009d\3\2\2\2\u009f\r\3\2\2\2\u00a0")
        buf.write("\u00a1\t\2\2\2\u00a1\17\3\2\2\2\u00a2\u00a3\7\13\2\2\u00a3")
        buf.write("\u00a4\7\t\2\2\u00a4\u00a5\5\b\5\2\u00a5\u00a6\7\f\2\2")
        buf.write("\u00a6\u00a7\7\t\2\2\u00a7\21\3\2\2\2\u00a8\u00ab\5\24")
        buf.write("\13\2\u00a9\u00ab\5\30\r\2\u00aa\u00a8\3\2\2\2\u00aa\u00a9")
        buf.write("\3\2\2\2\u00ab\23\3\2\2\2\u00ac\u00ad\7\6\2\2\u00ad\u00ae")
        buf.write("\7-\2\2\u00ae\u00af\7\27\2\2\u00af\u00b0\5L\'\2\u00b0")
        buf.write("\u00b1\7\t\2\2\u00b1\u00bc\3\2\2\2\u00b2\u00b5\5\26\f")
        buf.write("\2\u00b3\u00b5\7\7\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b3")
        buf.write("\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b9\7-\2\2\u00b7")
        buf.write("\u00b8\7\27\2\2\u00b8\u00ba\5L\'\2\u00b9\u00b7\3\2\2\2")
        buf.write("\u00b9\u00ba\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00ac\3")
        buf.write("\2\2\2\u00bb\u00b4\3\2\2\2\u00bc\25\3\2\2\2\u00bd\u00be")
        buf.write("\t\3\2\2\u00be\27\3\2\2\2\u00bf\u00c0\5\26\f\2\u00c0\u00c1")
        buf.write("\7-\2\2\u00c1\u00c4\5\32\16\2\u00c2\u00c3\7\27\2\2\u00c3")
        buf.write("\u00c5\5\36\20\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2")
        buf.write("\2\u00c5\31\3\2\2\2\u00c6\u00c7\7\32\2\2\u00c7\u00c8\5")
        buf.write("\34\17\2\u00c8\u00c9\7\33\2\2\u00c9\33\3\2\2\2\u00ca\u00cb")
        buf.write("\5t;\2\u00cb\u00cc\7\34\2\2\u00cc\u00cd\5\34\17\2\u00cd")
        buf.write("\u00d0\3\2\2\2\u00ce\u00d0\5t;\2\u00cf\u00ca\3\2\2\2\u00cf")
        buf.write("\u00ce\3\2\2\2\u00d0\35\3\2\2\2\u00d1\u00d2\7\32\2\2\u00d2")
        buf.write("\u00d3\5 \21\2\u00d3\u00d4\7\33\2\2\u00d4\u00d9\3\2\2")
        buf.write("\2\u00d5\u00d6\7\32\2\2\u00d6\u00d9\7\33\2\2\u00d7\u00d9")
        buf.write("\5L\'\2\u00d8\u00d1\3\2\2\2\u00d8\u00d5\3\2\2\2\u00d8")
        buf.write("\u00d7\3\2\2\2\u00d9\37\3\2\2\2\u00da\u00db\5L\'\2\u00db")
        buf.write("\u00dc\7\34\2\2\u00dc\u00dd\5 \21\2\u00dd\u00e5\3\2\2")
        buf.write("\2\u00de\u00df\5\36\20\2\u00df\u00e0\7\34\2\2\u00e0\u00e1")
        buf.write("\5\36\20\2\u00e1\u00e5\3\2\2\2\u00e2\u00e5\5\36\20\2\u00e3")
        buf.write("\u00e5\5L\'\2\u00e4\u00da\3\2\2\2\u00e4\u00de\3\2\2\2")
        buf.write("\u00e4\u00e2\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e5!\3\2\2")
        buf.write("\2\u00e6\u00e7\5$\23\2\u00e7\u00e8\7\t\2\2\u00e8\u00ed")
        buf.write("\3\2\2\2\u00e9\u00ea\5&\24\2\u00ea\u00eb\7\t\2\2\u00eb")
        buf.write("\u00ed\3\2\2\2\u00ec\u00e6\3\2\2\2\u00ec\u00e9\3\2\2\2")
        buf.write("\u00ed#\3\2\2\2\u00ee\u00ef\7-\2\2\u00ef\u00f0\7\27\2")
        buf.write("\2\u00f0\u00f1\5L\'\2\u00f1%\3\2\2\2\u00f2\u00f3\5^\60")
        buf.write("\2\u00f3\u00f4\7\27\2\2\u00f4\u00f5\5L\'\2\u00f5\'\3\2")
        buf.write("\2\2\u00f6\u00f7\7\r\2\2\u00f7\u00f8\7-\2\2\u00f8\u00fa")
        buf.write("\7\30\2\2\u00f9\u00fb\5.\30\2\u00fa\u00f9\3\2\2\2\u00fa")
        buf.write("\u00fb\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\7\31\2")
        buf.write("\2\u00fd\u0102\7\t\2\2\u00fe\u0100\5*\26\2\u00ff\u0101")
        buf.write("\7\t\2\2\u0100\u00ff\3\2\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write("\u0103\3\2\2\2\u0102\u00fe\3\2\2\2\u0102\u0103\3\2\2\2")
        buf.write("\u0103)\3\2\2\2\u0104\u0109\5\n\6\2\u0105\u0106\5\f\7")
        buf.write("\2\u0106\u0107\5\20\t\2\u0107\u0109\3\2\2\2\u0108\u0104")
        buf.write("\3\2\2\2\u0108\u0105\3\2\2\2\u0109+\3\2\2\2\u010a\u010b")
        buf.write("\7\16\2\2\u010b\u010c\5L\'\2\u010c\u010d\7\t\2\2\u010d")
        buf.write("-\3\2\2\2\u010e\u010f\5\60\31\2\u010f\u0110\7\34\2\2\u0110")
        buf.write("\u0111\5.\30\2\u0111\u0114\3\2\2\2\u0112\u0114\5\60\31")
        buf.write("\2\u0113\u010e\3\2\2\2\u0113\u0112\3\2\2\2\u0114/\3\2")
        buf.write("\2\2\u0115\u0118\5\62\32\2\u0116\u0118\5\64\33\2\u0117")
        buf.write("\u0115\3\2\2\2\u0117\u0116\3\2\2\2\u0118\61\3\2\2\2\u0119")
        buf.write("\u011c\7\7\2\2\u011a\u011c\5\26\f\2\u011b\u0119\3\2\2")
        buf.write("\2\u011b\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e")
        buf.write("\7-\2\2\u011e\63\3\2\2\2\u011f\u0120\5\26\f\2\u0120\u0121")
        buf.write("\7-\2\2\u0121\u0122\5\32\16\2\u0122\65\3\2\2\2\u0123\u0124")
        buf.write("\7\17\2\2\u0124\u0125\5L\'\2\u0125\u0127\5> \2\u0126\u0128")
        buf.write("\58\35\2\u0127\u0126\3\2\2\2\u0127\u0128\3\2\2\2\u0128")
        buf.write("\u012a\3\2\2\2\u0129\u012b\5<\37\2\u012a\u0129\3\2\2\2")
        buf.write("\u012a\u012b\3\2\2\2\u012b\67\3\2\2\2\u012c\u012d\5:\36")
        buf.write("\2\u012d\u012e\58\35\2\u012e\u0131\3\2\2\2\u012f\u0131")
        buf.write("\5:\36\2\u0130\u012c\3\2\2\2\u0130\u012f\3\2\2\2\u0131")
        buf.write("9\3\2\2\2\u0132\u0133\7\21\2\2\u0133\u0134\5L\'\2\u0134")
        buf.write("\u0135\5> \2\u0135;\3\2\2\2\u0136\u0137\7\20\2\2\u0137")
        buf.write("\u0138\5> \2\u0138=\3\2\2\2\u0139\u013a\5\f\7\2\u013a")
        buf.write("\u013b\5\20\t\2\u013b\u0140\3\2\2\2\u013c\u013d\5\f\7")
        buf.write("\2\u013d\u013e\5\n\6\2\u013e\u0140\3\2\2\2\u013f\u0139")
        buf.write("\3\2\2\2\u013f\u013c\3\2\2\2\u0140?\3\2\2\2\u0141\u0142")
        buf.write("\7-\2\2\u0142\u0144\7\30\2\2\u0143\u0145\5B\"\2\u0144")
        buf.write("\u0143\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146\3\2\2\2")
        buf.write("\u0146\u0147\7\31\2\2\u0147A\3\2\2\2\u0148\u0149\5L\'")
        buf.write("\2\u0149\u014a\7\34\2\2\u014a\u014b\5B\"\2\u014b\u014e")
        buf.write("\3\2\2\2\u014c\u014e\5L\'\2\u014d\u0148\3\2\2\2\u014d")
        buf.write("\u014c\3\2\2\2\u014eC\3\2\2\2\u014f\u0150\7\22\2\2\u0150")
        buf.write("\u0151\7-\2\2\u0151\u0152\7\23\2\2\u0152\u0153\5L\'\2")
        buf.write("\u0153\u0154\7\24\2\2\u0154\u0155\5L\'\2\u0155\u0156\5")
        buf.write("F$\2\u0156E\3\2\2\2\u0157\u0158\5\f\7\2\u0158\u0159\5")
        buf.write("\20\t\2\u0159\u015e\3\2\2\2\u015a\u015b\5\f\7\2\u015b")
        buf.write("\u015c\5\n\6\2\u015c\u015e\3\2\2\2\u015d\u0157\3\2\2\2")
        buf.write("\u015d\u015a\3\2\2\2\u015eG\3\2\2\2\u015f\u0160\7\25\2")
        buf.write("\2\u0160\u0161\7\t\2\2\u0161I\3\2\2\2\u0162\u0163\7\26")
        buf.write("\2\2\u0163\u0164\7\t\2\2\u0164K\3\2\2\2\u0165\u0166\5")
        buf.write("N(\2\u0166M\3\2\2\2\u0167\u0168\5P)\2\u0168\u0169\7+\2")
        buf.write("\2\u0169\u016a\5P)\2\u016a\u016d\3\2\2\2\u016b\u016d\5")
        buf.write("P)\2\u016c\u0167\3\2\2\2\u016c\u016b\3\2\2\2\u016dO\3")
        buf.write("\2\2\2\u016e\u016f\5R*\2\u016f\u0170\5h\65\2\u0170\u0171")
        buf.write("\5R*\2\u0171\u0174\3\2\2\2\u0172\u0174\5R*\2\u0173\u016e")
        buf.write("\3\2\2\2\u0173\u0172\3\2\2\2\u0174Q\3\2\2\2\u0175\u0176")
        buf.write("\b*\1\2\u0176\u0177\5T+\2\u0177\u017e\3\2\2\2\u0178\u0179")
        buf.write("\f\4\2\2\u0179\u017a\5n8\2\u017a\u017b\5T+\2\u017b\u017d")
        buf.write("\3\2\2\2\u017c\u0178\3\2\2\2\u017d\u0180\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017fS\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0181\u0182\b+\1\2\u0182\u0183\5V,\2\u0183")
        buf.write("\u018a\3\2\2\2\u0184\u0185\f\4\2\2\u0185\u0186\5j\66\2")
        buf.write("\u0186\u0187\5V,\2\u0187\u0189\3\2\2\2\u0188\u0184\3\2")
        buf.write("\2\2\u0189\u018c\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b")
        buf.write("\3\2\2\2\u018bU\3\2\2\2\u018c\u018a\3\2\2\2\u018d\u018e")
        buf.write("\b,\1\2\u018e\u018f\5X-\2\u018f\u0196\3\2\2\2\u0190\u0191")
        buf.write("\f\4\2\2\u0191\u0192\5l\67\2\u0192\u0193\5X-\2\u0193\u0195")
        buf.write("\3\2\2\2\u0194\u0190\3\2\2\2\u0195\u0198\3\2\2\2\u0196")
        buf.write("\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197W\3\2\2\2\u0198")
        buf.write("\u0196\3\2\2\2\u0199\u019a\7\"\2\2\u019a\u019d\5X-\2\u019b")
        buf.write("\u019d\5Z.\2\u019c\u0199\3\2\2\2\u019c\u019b\3\2\2\2\u019d")
        buf.write("Y\3\2\2\2\u019e\u019f\5j\66\2\u019f\u01a0\5Z.\2\u01a0")
        buf.write("\u01a3\3\2\2\2\u01a1\u01a3\5\\/\2\u01a2\u019e\3\2\2\2")
        buf.write("\u01a2\u01a1\3\2\2\2\u01a3[\3\2\2\2\u01a4\u01a6\5d\63")
        buf.write("\2\u01a5\u01a4\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7")
        buf.write("\3\2\2\2\u01a7\u01aa\5`\61\2\u01a8\u01aa\5b\62\2\u01a9")
        buf.write("\u01a5\3\2\2\2\u01a9\u01a8\3\2\2\2\u01aa]\3\2\2\2\u01ab")
        buf.write("\u01ac\5d\63\2\u01ac\u01ad\5`\61\2\u01ad\u01b0\3\2\2\2")
        buf.write("\u01ae\u01b0\5b\62\2\u01af\u01ab\3\2\2\2\u01af\u01ae\3")
        buf.write("\2\2\2\u01b0_\3\2\2\2\u01b1\u01b2\b\61\1\2\u01b2\u01b3")
        buf.write("\7\32\2\2\u01b3\u01b4\5f\64\2\u01b4\u01b5\7\33\2\2\u01b5")
        buf.write("\u01bd\3\2\2\2\u01b6\u01b7\f\4\2\2\u01b7\u01b8\7\32\2")
        buf.write("\2\u01b8\u01b9\5f\64\2\u01b9\u01ba\7\33\2\2\u01ba\u01bc")
        buf.write("\3\2\2\2\u01bb\u01b6\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01bea\3\2\2\2\u01bf")
        buf.write("\u01bd\3\2\2\2\u01c0\u01c1\7\30\2\2\u01c1\u01c2\5L\'\2")
        buf.write("\u01c2\u01c3\7\31\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c6")
        buf.write("\5d\63\2\u01c5\u01c0\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6")
        buf.write("c\3\2\2\2\u01c7\u01cb\5p9\2\u01c8\u01cb\5@!\2\u01c9\u01cb")
        buf.write("\7-\2\2\u01ca\u01c7\3\2\2\2\u01ca\u01c8\3\2\2\2\u01ca")
        buf.write("\u01c9\3\2\2\2\u01cbe\3\2\2\2\u01cc\u01cd\5L\'\2\u01cd")
        buf.write("\u01ce\7\34\2\2\u01ce\u01cf\5f\64\2\u01cf\u01d2\3\2\2")
        buf.write("\2\u01d0\u01d2\5L\'\2\u01d1\u01cc\3\2\2\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d2g\3\2\2\2\u01d3\u01d4\t\4\2\2\u01d4i\3\2")
        buf.write("\2\2\u01d5\u01d6\t\5\2\2\u01d6k\3\2\2\2\u01d7\u01d8\t")
        buf.write("\6\2\2\u01d8m\3\2\2\2\u01d9\u01da\t\7\2\2\u01dao\3\2\2")
        buf.write("\2\u01db\u01dc\t\b\2\2\u01dcq\3\2\2\2\u01dd\u01de\7\60")
        buf.write("\2\2\u01des\3\2\2\2\u01df\u01e0\7.\2\2\u01e0u\3\2\2\2")
        buf.write("\u01e1\u01e2\7/\2\2\u01e2w\3\2\2\2-y\u0081\u0086\u008c")
        buf.write("\u0098\u009e\u00aa\u00b4\u00b9\u00bb\u00c4\u00cf\u00d8")
        buf.write("\u00e4\u00ec\u00fa\u0100\u0102\u0108\u0113\u0117\u011b")
        buf.write("\u0127\u012a\u0130\u013f\u0144\u014d\u015d\u016c\u0173")
        buf.write("\u017e\u018a\u0196\u019c\u01a2\u01a5\u01a9\u01af\u01bd")
        buf.write("\u01c5\u01ca\u01d1")
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
    RULE_local_statement_list = 3
    RULE_local_statement = 4
    RULE_ignore_statement_list = 5
    RULE_ignore_statement = 6
    RULE_block_statement = 7
    RULE_variable_declaration_statement = 8
    RULE_basic_variable_declaration = 9
    RULE_basic_type = 10
    RULE_array_declaration = 11
    RULE_array_dimension = 12
    RULE_array_dimension_list = 13
    RULE_array_value = 14
    RULE_array_value_expression_list = 15
    RULE_assignment_statement = 16
    RULE_basic_variable_assignment = 17
    RULE_array_assignment = 18
    RULE_function_declaration_statement = 19
    RULE_function_body = 20
    RULE_return_statement = 21
    RULE_parameter_part_recursive = 22
    RULE_parameter_declaration_statement = 23
    RULE_basic_parameter_declaration = 24
    RULE_array_parameter_declaration = 25
    RULE_if_statement = 26
    RULE_elif_recursive_statement = 27
    RULE_elif_statement = 28
    RULE_else_statement = 29
    RULE_branch_body = 30
    RULE_function_call_statement = 31
    RULE_argument_part = 32
    RULE_for_statement = 33
    RULE_loop_body = 34
    RULE_break_statement = 35
    RULE_continue_statement = 36
    RULE_expression = 37
    RULE_string_expression = 38
    RULE_relational_expression = 39
    RULE_logical_expression = 40
    RULE_adding_expression = 41
    RULE_multiplying_expression = 42
    RULE_negation_expression = 43
    RULE_sign_expression = 44
    RULE_element_expression = 45
    RULE_element_force_expression = 46
    RULE_index_expression = 47
    RULE_parenthesis_expression = 48
    RULE_operand = 49
    RULE_array_index_access = 50
    RULE_relational_operator = 51
    RULE_additive_operator = 52
    RULE_multiplicative_operator = 53
    RULE_logic_operator = 54
    RULE_literal = 55
    RULE_string_literal = 56
    RULE_number_literal = 57
    RULE_boolean_literal = 58

    ruleNames =  [ "program", "declaration_list", "declaration", "local_statement_list", 
                   "local_statement", "ignore_statement_list", "ignore_statement", 
                   "block_statement", "variable_declaration_statement", 
                   "basic_variable_declaration", "basic_type", "array_declaration", 
                   "array_dimension", "array_dimension_list", "array_value", 
                   "array_value_expression_list", "assignment_statement", 
                   "basic_variable_assignment", "array_assignment", "function_declaration_statement", 
                   "function_body", "return_statement", "parameter_part_recursive", 
                   "parameter_declaration_statement", "basic_parameter_declaration", 
                   "array_parameter_declaration", "if_statement", "elif_recursive_statement", 
                   "elif_statement", "else_statement", "branch_body", "function_call_statement", 
                   "argument_part", "for_statement", "loop_body", "break_statement", 
                   "continue_statement", "expression", "string_expression", 
                   "relational_expression", "logical_expression", "adding_expression", 
                   "multiplying_expression", "negation_expression", "sign_expression", 
                   "element_expression", "element_force_expression", "index_expression", 
                   "parenthesis_expression", "operand", "array_index_access", 
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

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_listContext,0)


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
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER_TYPE) | (1 << ZCodeParser.BOOLEAN_TYPE) | (1 << ZCodeParser.STRING_TYPE) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.COMMENT) | (1 << ZCodeParser.NEWLINE) | (1 << ZCodeParser.FUNC))) != 0):
                self.state = 118
                self.declaration_list()


            self.state = 121
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
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.declaration()
                self.state = 124
                self.declaration_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
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

        def function_declaration_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Function_declaration_statementContext,0)


        def variable_declaration_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declaration_statementContext,0)


        def ignore_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Ignore_statement_listContext,0)


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
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.function_declaration_statement()
                pass
            elif token in [ZCodeParser.NUMBER_TYPE, ZCodeParser.BOOLEAN_TYPE, ZCodeParser.STRING_TYPE, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.variable_declaration_statement()
                pass
            elif token in [ZCodeParser.COMMENT, ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.ignore_statement_list()
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


    class Local_statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statementContext,0)


        def local_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_local_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_statement_list" ):
                return visitor.visitLocal_statement_list(self)
            else:
                return visitor.visitChildren(self)




    def local_statement_list(self):

        localctx = ZCodeParser.Local_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_local_statement_list)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.local_statement()
                self.state = 135
                self.local_statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.local_statement()
                pass


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


        def ignore_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Ignore_statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_local_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocal_statement" ):
                return visitor.visitLocal_statement(self)
            else:
                return visitor.visitChildren(self)




    def local_statement(self):

        localctx = ZCodeParser.Local_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_local_statement)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.variable_declaration_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.function_call_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 144
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 145
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 146
                self.block_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 147
                self.assignment_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 148
                self.return_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 149
                self.ignore_statement_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ignore_statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ignore_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Ignore_statementContext,0)


        def ignore_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Ignore_statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore_statement_list" ):
                return visitor.visitIgnore_statement_list(self)
            else:
                return visitor.visitChildren(self)




    def ignore_statement_list(self):

        localctx = ZCodeParser.Ignore_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ignore_statement_list)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.ignore_statement()
                self.state = 153
                self.ignore_statement_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.ignore_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ignore_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(ZCodeParser.COMMENT, 0)

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore_statement" ):
                return visitor.visitIgnore_statement(self)
            else:
                return visitor.visitChildren(self)




    def ignore_statement(self):

        localctx = ZCodeParser.Ignore_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ignore_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.COMMENT or _la==ZCodeParser.NEWLINE):
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


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

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
        self.enterRule(localctx, 14, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(ZCodeParser.BEGIN)
            self.state = 161
            self.match(ZCodeParser.NEWLINE)
            self.state = 162
            self.local_statement_list()
            self.state = 163
            self.match(ZCodeParser.END)
            self.state = 164
            self.match(ZCodeParser.NEWLINE)
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
        self.enterRule(localctx, 16, self.RULE_variable_declaration_statement)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.basic_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
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


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

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
        self.enterRule(localctx, 18, self.RULE_basic_variable_declaration)
        self._la = 0 # Token type
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.match(ZCodeParser.VAR)
                self.state = 171
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 172
                self.match(ZCodeParser.ASSIGN)
                self.state = 173
                self.expression()
                self.state = 174
                self.match(ZCodeParser.NEWLINE)
                pass
            elif token in [ZCodeParser.NUMBER_TYPE, ZCodeParser.BOOLEAN_TYPE, ZCodeParser.STRING_TYPE, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.NUMBER_TYPE, ZCodeParser.BOOLEAN_TYPE, ZCodeParser.STRING_TYPE]:
                    self.state = 176
                    self.basic_type()
                    pass
                elif token in [ZCodeParser.DYNAMIC]:
                    self.state = 177
                    self.match(ZCodeParser.DYNAMIC)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 180
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 181
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 182
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
        self.enterRule(localctx, 20, self.RULE_basic_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
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

        def array_value(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valueContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declaration" ):
                return visitor.visitArray_declaration(self)
            else:
                return visitor.visitChildren(self)




    def array_declaration(self):

        localctx = ZCodeParser.Array_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.basic_type()
            self.state = 190
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 191
            self.array_dimension()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 192
                self.match(ZCodeParser.ASSIGN)
                self.state = 193
                self.array_value()


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
        self.enterRule(localctx, 24, self.RULE_array_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(ZCodeParser.LBRACK)
            self.state = 197
            self.array_dimension_list()
            self.state = 198
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
        self.enterRule(localctx, 26, self.RULE_array_dimension_list)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.number_literal()
                self.state = 201
                self.match(ZCodeParser.COMMA)
                self.state = 202
                self.array_dimension_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.number_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def array_value_expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_value_expression_listContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value" ):
                return visitor.visitArray_value(self)
            else:
                return visitor.visitChildren(self)




    def array_value(self):

        localctx = ZCodeParser.Array_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_value)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.match(ZCodeParser.LBRACK)
                self.state = 208
                self.array_value_expression_list()
                self.state = 209
                self.match(ZCodeParser.RBRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(ZCodeParser.LBRACK)
                self.state = 212
                self.match(ZCodeParser.RBRACK)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 213
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_value_expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def array_value_expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_value_expression_listContext,0)


        def array_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Array_valueContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Array_valueContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value_expression_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value_expression_list" ):
                return visitor.visitArray_value_expression_list(self)
            else:
                return visitor.visitChildren(self)




    def array_value_expression_list(self):

        localctx = ZCodeParser.Array_value_expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_array_value_expression_list)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.expression()
                self.state = 217
                self.match(ZCodeParser.COMMA)
                self.state = 218
                self.array_value_expression_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.array_value()
                self.state = 221
                self.match(ZCodeParser.COMMA)
                self.state = 222
                self.array_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 224
                self.array_value()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 225
                self.expression()
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

        def basic_variable_assignment(self):
            return self.getTypedRuleContext(ZCodeParser.Basic_variable_assignmentContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def array_assignment(self):
            return self.getTypedRuleContext(ZCodeParser.Array_assignmentContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assignment_statement)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.basic_variable_assignment()
                self.state = 229
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.array_assignment()
                self.state = 232
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_variable_assignmentContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_basic_variable_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_variable_assignment" ):
                return visitor.visitBasic_variable_assignment(self)
            else:
                return visitor.visitChildren(self)




    def basic_variable_assignment(self):

        localctx = ZCodeParser.Basic_variable_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_basic_variable_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 237
            self.match(ZCodeParser.ASSIGN)
            self.state = 238
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_force_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Element_force_expressionContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_assignment" ):
                return visitor.visitArray_assignment(self)
            else:
                return visitor.visitChildren(self)




    def array_assignment(self):

        localctx = ZCodeParser.Array_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_array_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.element_force_expression()
            self.state = 241
            self.match(ZCodeParser.ASSIGN)
            self.state = 242
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declaration_statementContext(ParserRuleContext):
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

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def parameter_part_recursive(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_part_recursiveContext,0)


        def function_body(self):
            return self.getTypedRuleContext(ZCodeParser.Function_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_declaration_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration_statement" ):
                return visitor.visitFunction_declaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration_statement(self):

        localctx = ZCodeParser.Function_declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_function_declaration_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(ZCodeParser.FUNC)
            self.state = 245
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 246
            self.match(ZCodeParser.LPAREN)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER_TYPE) | (1 << ZCodeParser.BOOLEAN_TYPE) | (1 << ZCodeParser.STRING_TYPE) | (1 << ZCodeParser.DYNAMIC))) != 0):
                self.state = 247
                self.parameter_part_recursive()


            self.state = 250
            self.match(ZCodeParser.RPAREN)
            self.state = 251
            self.match(ZCodeParser.NEWLINE)
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 252
                self.function_body()
                self.state = 254
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 253
                    self.match(ZCodeParser.NEWLINE)




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

        def local_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statementContext,0)


        def ignore_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Ignore_statement_listContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_body" ):
                return visitor.visitFunction_body(self)
            else:
                return visitor.visitChildren(self)




    def function_body(self):

        localctx = ZCodeParser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_function_body)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.local_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.ignore_statement_list()
                self.state = 260
                self.block_statement()
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


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(ZCodeParser.RETURN)
            self.state = 265
            self.expression()
            self.state = 266
            self.match(ZCodeParser.NEWLINE)
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

        def parameter_declaration_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_declaration_statementContext,0)


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
        self.enterRule(localctx, 44, self.RULE_parameter_part_recursive)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.parameter_declaration_statement()
                self.state = 269
                self.match(ZCodeParser.COMMA)
                self.state = 270
                self.parameter_part_recursive()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.parameter_declaration_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_parameter_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Basic_parameter_declarationContext,0)


        def array_parameter_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Array_parameter_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_declaration_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_declaration_statement" ):
                return visitor.visitParameter_declaration_statement(self)
            else:
                return visitor.visitChildren(self)




    def parameter_declaration_statement(self):

        localctx = ZCodeParser.Parameter_declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_parameter_declaration_statement)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.basic_parameter_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
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

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def basic_type(self):
            return self.getTypedRuleContext(ZCodeParser.Basic_typeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_basic_parameter_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_parameter_declaration" ):
                return visitor.visitBasic_parameter_declaration(self)
            else:
                return visitor.visitChildren(self)




    def basic_parameter_declaration(self):

        localctx = ZCodeParser.Basic_parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_basic_parameter_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.DYNAMIC]:
                self.state = 279
                self.match(ZCodeParser.DYNAMIC)
                pass
            elif token in [ZCodeParser.NUMBER_TYPE, ZCodeParser.BOOLEAN_TYPE, ZCodeParser.STRING_TYPE]:
                self.state = 280
                self.basic_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 283
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
        self.enterRule(localctx, 50, self.RULE_array_parameter_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.basic_type()
            self.state = 286
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 287
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

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


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
        self.enterRule(localctx, 52, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(ZCodeParser.IF)
            self.state = 290
            self.expression()
            self.state = 291
            self.branch_body()
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 292
                self.elif_recursive_statement()


            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 295
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
        self.enterRule(localctx, 54, self.RULE_elif_recursive_statement)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.elif_statement()
                self.state = 299
                self.elif_recursive_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
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

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


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
        self.enterRule(localctx, 56, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(ZCodeParser.ELIF)
            self.state = 305
            self.expression()
            self.state = 306
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
        self.enterRule(localctx, 58, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(ZCodeParser.ELSE)
            self.state = 309
            self.branch_body()
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

        def ignore_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Ignore_statement_listContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def local_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_branch_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBranch_body" ):
                return visitor.visitBranch_body(self)
            else:
                return visitor.visitChildren(self)




    def branch_body(self):

        localctx = ZCodeParser.Branch_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_branch_body)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.ignore_statement_list()
                self.state = 312
                self.block_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.ignore_statement_list()
                self.state = 315
                self.local_statement()
                pass


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
        self.enterRule(localctx, 62, self.RULE_function_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 320
            self.match(ZCodeParser.LPAREN)
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.LPAREN) | (1 << ZCodeParser.LBRACK) | (1 << ZCodeParser.PLUS) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.BOOLEAN_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 321
                self.argument_part()


            self.state = 324
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
        self.enterRule(localctx, 64, self.RULE_argument_part)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.expression()
                self.state = 327
                self.match(ZCodeParser.COMMA)
                self.state = 328
                self.argument_part()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
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
        self.enterRule(localctx, 66, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(ZCodeParser.FOR)
            self.state = 334
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 335
            self.match(ZCodeParser.UNTIL)
            self.state = 336
            self.expression()
            self.state = 337
            self.match(ZCodeParser.BY)
            self.state = 338
            self.expression()
            self.state = 339
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

        def ignore_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Ignore_statement_listContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def local_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_loop_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_body" ):
                return visitor.visitLoop_body(self)
            else:
                return visitor.visitChildren(self)




    def loop_body(self):

        localctx = ZCodeParser.Loop_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_loop_body)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.ignore_statement_list()
                self.state = 342
                self.block_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.ignore_statement_list()
                self.state = 345
                self.local_statement()
                pass


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

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(ZCodeParser.BREAK)
            self.state = 350
            self.match(ZCodeParser.NEWLINE)
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

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(ZCodeParser.CONTINUE)
            self.state = 353
            self.match(ZCodeParser.NEWLINE)
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
        self.enterRule(localctx, 74, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
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
        self.enterRule(localctx, 76, self.RULE_string_expression)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.relational_expression()
                self.state = 358
                self.match(ZCodeParser.CONCATE)
                self.state = 359
                self.relational_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
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
        self.enterRule(localctx, 78, self.RULE_relational_expression)
        try:
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.logical_expression(0)
                self.state = 365
                self.relational_operator()
                self.state = 366
                self.logical_expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_logical_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.adding_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 380
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 374
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 375
                    self.logic_operator()
                    self.state = 376
                    self.adding_expression(0) 
                self.state = 382
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_adding_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.multiplying_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 392
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Adding_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expression)
                    self.state = 386
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 387
                    self.additive_operator()
                    self.state = 388
                    self.multiplying_expression(0) 
                self.state = 394
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_multiplying_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.negation_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 404
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Multiplying_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
                    self.state = 398
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 399
                    self.multiplicative_operator()
                    self.state = 400
                    self.negation_expression() 
                self.state = 406
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        self.enterRule(localctx, 86, self.RULE_negation_expression)
        try:
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(ZCodeParser.NOT)
                self.state = 408
                self.negation_expression()
                pass
            elif token in [ZCodeParser.LPAREN, ZCodeParser.LBRACK, ZCodeParser.PLUS, ZCodeParser.MINUS, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.BOOLEAN_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
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


        def element_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Element_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expression" ):
                return visitor.visitSign_expression(self)
            else:
                return visitor.visitChildren(self)




    def sign_expression(self):

        localctx = ZCodeParser.Sign_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_sign_expression)
        try:
            self.state = 416
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.PLUS, ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.additive_operator()
                self.state = 413
                self.sign_expression()
                pass
            elif token in [ZCodeParser.LPAREN, ZCodeParser.LBRACK, ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.BOOLEAN_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.element_expression()
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


    class Element_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Index_expressionContext,0)


        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def parenthesis_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Parenthesis_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_element_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expression" ):
                return visitor.visitElement_expression(self)
            else:
                return visitor.visitChildren(self)




    def element_expression(self):

        localctx = ZCodeParser.Element_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_element_expression)
        self._la = 0 # Token type
        try:
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.IDENTIFIER) | (1 << ZCodeParser.NUMBER_LIT) | (1 << ZCodeParser.BOOLEAN_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                    self.state = 418
                    self.operand()


                self.state = 421
                self.index_expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.parenthesis_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_force_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def index_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Index_expressionContext,0)


        def parenthesis_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Parenthesis_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_element_force_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_force_expression" ):
                return visitor.visitElement_force_expression(self)
            else:
                return visitor.visitChildren(self)




    def element_force_expression(self):

        localctx = ZCodeParser.Element_force_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_element_force_expression)
        try:
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.operand()
                self.state = 426
                self.index_expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.parenthesis_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def array_index_access(self):
            return self.getTypedRuleContext(ZCodeParser.Array_index_accessContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def index_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Index_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expression" ):
                return visitor.visitIndex_expression(self)
            else:
                return visitor.visitChildren(self)



    def index_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Index_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_index_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(ZCodeParser.LBRACK)
            self.state = 433
            self.array_index_access()
            self.state = 434
            self.match(ZCodeParser.RBRACK)
            self._ctx.stop = self._input.LT(-1)
            self.state = 443
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Index_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_expression)
                    self.state = 436
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 437
                    self.match(ZCodeParser.LBRACK)
                    self.state = 438
                    self.array_index_access()
                    self.state = 439
                    self.match(ZCodeParser.RBRACK) 
                self.state = 445
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 96, self.RULE_parenthesis_expression)
        try:
            self.state = 451
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.match(ZCodeParser.LPAREN)
                self.state = 447
                self.expression()
                self.state = 448
                self.match(ZCodeParser.RPAREN)
                pass
            elif token in [ZCodeParser.IDENTIFIER, ZCodeParser.NUMBER_LIT, ZCodeParser.BOOLEAN_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_operand)
        try:
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.function_call_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 455
                self.match(ZCodeParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_index_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def array_index_access(self):
            return self.getTypedRuleContext(ZCodeParser.Array_index_accessContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_index_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_index_access" ):
                return visitor.visitArray_index_access(self)
            else:
                return visitor.visitChildren(self)




    def array_index_access(self):

        localctx = ZCodeParser.Array_index_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_array_index_access)
        try:
            self.state = 463
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.expression()
                self.state = 459
                self.match(ZCodeParser.COMMA)
                self.state = 460
                self.array_index_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
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
        self.enterRule(localctx, 102, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
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
        self.enterRule(localctx, 104, self.RULE_additive_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
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
        self.enterRule(localctx, 106, self.RULE_multiplicative_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
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
        self.enterRule(localctx, 108, self.RULE_logic_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
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
        self.enterRule(localctx, 110, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
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
        self.enterRule(localctx, 112, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
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
        self.enterRule(localctx, 114, self.RULE_number_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
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
        self.enterRule(localctx, 116, self.RULE_boolean_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
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
        self._predicates[40] = self.logical_expression_sempred
        self._predicates[41] = self.adding_expression_sempred
        self._predicates[42] = self.multiplying_expression_sempred
        self._predicates[47] = self.index_expression_sempred
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
         

    def index_expression_sempred(self, localctx:Index_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




