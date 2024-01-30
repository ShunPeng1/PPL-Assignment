import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_100(self):
		self.assertTrue(TestLexer.test("83.840", "83.840,<EOF>", 100))

	def test_101(self):
		self.assertTrue(TestLexer.test("cNknj#0", "cNknj,Error Token #", 101))

	def test_102(self):
		self.assertTrue(TestLexer.test('''## XH 0T{@*^/oUN4bF1.''', '''## XH 0T{@*^/oUN4bF1.,<EOF>''', 102))

	def test_103(self):
		self.assertTrue(TestLexer.test('''## }. QE$j''', '''## }. QE$j,<EOF>''', 103))

	def test_104(self):
		self.assertTrue(TestLexer.test('''## AdqkSX>-Ogl''', '''## AdqkSX>-Ogl,<EOF>''', 104))

	def test_105(self):
		self.assertTrue(TestLexer.test("DpBST", "DpBST,<EOF>", 105))

	def test_106(self):
		self.assertTrue(TestLexer.test('''## 5Aa4qH<%-NBgc''', '''## 5Aa4qH<%-NBgc,<EOF>''', 106))

	def test_107(self):
		self.assertTrue(TestLexer.test("15RO$d", "15,RO,Error Token $", 107))

	def test_108(self):
		self.assertTrue(TestLexer.test("45.110", "45.110,<EOF>", 108))

	def test_109(self):
		self.assertTrue(TestLexer.test('''## _]K!s=4.]5"`#}ThG''', '''## _]K!s=4.]5"`#}ThG,<EOF>''', 109))

	def test_110(self):
		self.assertTrue(TestLexer.test("uxoGk", "uxoGk,<EOF>", 110))

	def test_111(self):
		self.assertTrue(TestLexer.test("50E-13", "50E-13,<EOF>", 111))

	def test_112(self):
		self.assertTrue(TestLexer.test("Yee@foy", "Yee,Error Token @", 112))

	def test_113(self):
		self.assertTrue(TestLexer.test("4.409", "4.409,<EOF>", 113))

	def test_114(self):
		self.assertTrue(TestLexer.test("RRKFMRgs", "RRKFMRgs,<EOF>", 114))

	def test_115(self):
		self.assertTrue(TestLexer.test("540.025e+18", "540.025e+18,<EOF>", 115))

	def test_116(self):
		self.assertTrue(TestLexer.test("83", "83,<EOF>", 116))

	def test_117(self):
		self.assertTrue(TestLexer.test('''## Xsu5z3[ht.J$E)tT''', '''## Xsu5z3[ht.J$E)tT,<EOF>''', 117))

	def test_118(self):
		self.assertTrue(TestLexer.test('''"'"^=~n ''', '''Unclosed String: '"^=~n ''', 118))

	def test_119(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 119))

	def test_120(self):
		self.assertTrue(TestLexer.test('''## r/76a,hh+AFN&-*sX_=R''', '''## r/76a,hh+AFN&-*sX_=R,<EOF>''', 120))

	def test_121(self):
		self.assertTrue(TestLexer.test('''## 1Cs-''', '''## 1Cs-,<EOF>''', 121))

	def test_122(self):
		self.assertTrue(TestLexer.test("dOX", "dOX,<EOF>", 122))

	def test_123(self):
		self.assertTrue(TestLexer.test("50e-66", "50e-66,<EOF>", 123))

	def test_124(self):
		self.assertTrue(TestLexer.test("SjA", "SjA,<EOF>", 124))

	def test_125(self):
		self.assertTrue(TestLexer.test("451.039", "451.039,<EOF>", 125))

	def test_126(self):
		self.assertTrue(TestLexer.test("b1#ZEPH", "b1,Error Token #", 126))

	def test_127(self):
		self.assertTrue(TestLexer.test("18.459", "18.459,<EOF>", 127))

	def test_128(self):
		self.assertTrue(TestLexer.test('''## Bw{CD`Q''', '''## Bw{CD`Q,<EOF>''', 128))

	def test_129(self):
		self.assertTrue(TestLexer.test('''## akLE''', '''## akLE,<EOF>''', 129))

	def test_130(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 130))

	def test_131(self):
		self.assertTrue(TestLexer.test("2.032", "2.032,<EOF>", 131))

	def test_132(self):
		self.assertTrue(TestLexer.test("555e+60", "555e+60,<EOF>", 132))

	def test_133(self):
		self.assertTrue(TestLexer.test("6AH&s3", "6,AH,Error Token &", 133))

	def test_134(self):
		self.assertTrue(TestLexer.test('''"\\ae"''', '''Illegal Escape In String: \\a''', 134))

	def test_135(self):
		self.assertTrue(TestLexer.test('''"i'"\\hO"''', '''Illegal Escape In String: i'"\\h''', 135))

	def test_136(self):
		self.assertTrue(TestLexer.test("Dfj0jKSUG", "Dfj0jKSUG,<EOF>", 136))

	def test_137(self):
		self.assertTrue(TestLexer.test('''"r\\c'""''', '''Illegal Escape In String: r\\c''', 137))

	def test_138(self):
		self.assertTrue(TestLexer.test('''"'"'"'" ''', '''Unclosed String: '"'"'" ''', 138))

	def test_139(self):
		self.assertTrue(TestLexer.test("df4Ro864D6", "df4Ro864D6,<EOF>", 139))

	def test_140(self):
		self.assertTrue(TestLexer.test("8.139", "8.139,<EOF>", 140))

	def test_141(self):
		self.assertTrue(TestLexer.test('''"'"j
Z/'""''', '''Unclosed String: '"j''', 141))

	def test_142(self):
		self.assertTrue(TestLexer.test("1qCkB", "1,qCkB,<EOF>", 142))

	def test_143(self):
		self.assertTrue(TestLexer.test('''"'"r'""''', '''\'"r'",<EOF>''', 143))

	def test_144(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 144))

	def test_145(self):
		self.assertTrue(TestLexer.test("5E91", "5E91,<EOF>", 145))

	def test_146(self):
		self.assertTrue(TestLexer.test("7.921E+66", "7.921E+66,<EOF>", 146))

	def test_147(self):
		self.assertTrue(TestLexer.test("95.454e61", "95.454e61,<EOF>", 147))

	def test_148(self):
		self.assertTrue(TestLexer.test('''"2y'"X ''', '''Unclosed String: 2y'"X ''', 148))

	def test_149(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 149))

	def test_150(self):
		self.assertTrue(TestLexer.test("bmG0BqVo", "bmG0BqVo,<EOF>", 150))

	def test_151(self):
		self.assertTrue(TestLexer.test("4.032", "4.032,<EOF>", 151))

	def test_152(self):
		self.assertTrue(TestLexer.test("Zg8grv$h", "Zg8grv,Error Token $", 152))

	def test_153(self):
		self.assertTrue(TestLexer.test('''## D.3I92RZ| SLFQ!0z aO''', '''## D.3I92RZ| SLFQ!0z aO,<EOF>''', 153))

	def test_154(self):
		self.assertTrue(TestLexer.test('''"'"'"'"2A ''', '''Unclosed String: '"'"'"2A ''', 154))

	def test_155(self):
		self.assertTrue(TestLexer.test('''## 2RNU.0.qsYaOv''', '''## 2RNU.0.qsYaOv,<EOF>''', 155))

	def test_156(self):
		self.assertTrue(TestLexer.test("l_HREBm5d", "l_HREBm5d,<EOF>", 156))

	def test_157(self):
		self.assertTrue(TestLexer.test("IMzp", "IMzp,<EOF>", 157))

	def test_158(self):
		self.assertTrue(TestLexer.test("dm^G", "dm,Error Token ^", 158))

	def test_159(self):
		self.assertTrue(TestLexer.test("waQV&MSX6u", "waQV,Error Token &", 159))

	def test_160(self):
		self.assertTrue(TestLexer.test('''"'"\\q'"'""''', '''Illegal Escape In String: '"\\q''', 160))

	def test_161(self):
		self.assertTrue(TestLexer.test("TEk2LUij", "TEk2LUij,<EOF>", 161))

	def test_162(self):
		self.assertTrue(TestLexer.test("bKFKNfa", "bKFKNfa,<EOF>", 162))

	def test_163(self):
		self.assertTrue(TestLexer.test('''## {4''', '''## {4,<EOF>''', 163))

	def test_164(self):
		self.assertTrue(TestLexer.test('''## OYT''', '''## OYT,<EOF>''', 164))

	def test_165(self):
		self.assertTrue(TestLexer.test('''">\\hQ'"'""''', '''Illegal Escape In String: >\\h''', 165))

	def test_166(self):
		self.assertTrue(TestLexer.test('''## 2PqO1EGL>''', '''## 2PqO1EGL>,<EOF>''', 166))

	def test_167(self):
		self.assertTrue(TestLexer.test('''## ${7''', '''## ${7,<EOF>''', 167))

	def test_168(self):
		self.assertTrue(TestLexer.test('''"D"''', '''D,<EOF>''', 168))

	def test_169(self):
		self.assertTrue(TestLexer.test("43.833", "43.833,<EOF>", 169))

	def test_170(self):
		self.assertTrue(TestLexer.test("V9PXE_WCYo", "V9PXE_WCYo,<EOF>", 170))

	def test_171(self):
		self.assertTrue(TestLexer.test("LMTZ@1lC", "LMTZ,Error Token @", 171))

	def test_172(self):
		self.assertTrue(TestLexer.test("258", "258,<EOF>", 172))

	def test_173(self):
		self.assertTrue(TestLexer.test("163.709", "163.709,<EOF>", 173))

	def test_174(self):
		self.assertTrue(TestLexer.test("3", "3,<EOF>", 174))

	def test_175(self):
		self.assertTrue(TestLexer.test('''## 4#.z~u?R%''', '''## 4#.z~u?R%,<EOF>''', 175))

	def test_176(self):
		self.assertTrue(TestLexer.test('''## &~`''', '''## &~`,<EOF>''', 176))

	def test_177(self):
		self.assertTrue(TestLexer.test('''## yfIS8 2?:?4a6iR''', '''## yfIS8 2?:?4a6iR,<EOF>''', 177))

	def test_178(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 178))

	def test_179(self):
		self.assertTrue(TestLexer.test('''"\\s,)"''', '''Illegal Escape In String: \\s''', 179))

	def test_180(self):
		self.assertTrue(TestLexer.test("41e+35", "41e+35,<EOF>", 180))

	def test_181(self):
		self.assertTrue(TestLexer.test('''"4'"9+"''', '''4'"9+,<EOF>''', 181))

	def test_182(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 182))

	def test_183(self):
		self.assertTrue(TestLexer.test("kTXZkZr", "kTXZkZr,<EOF>", 183))

	def test_184(self):
		self.assertTrue(TestLexer.test('''## 2ay;N(3Y!''', '''## 2ay;N(3Y!,<EOF>''', 184))

	def test_185(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''Unclosed String: '" ''', 185))

	def test_186(self):
		self.assertTrue(TestLexer.test("54.711e48", "54.711e48,<EOF>", 186))

	def test_187(self):
		self.assertTrue(TestLexer.test('''## 5=K4CjnX/s''', '''## 5=K4CjnX/s,<EOF>''', 187))

	def test_188(self):
		self.assertTrue(TestLexer.test('''## RxV-(Qtiz^Z%Kf.$*''', '''## RxV-(Qtiz^Z%Kf.$*,<EOF>''', 188))

	def test_189(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 189))

	def test_190(self):
		self.assertTrue(TestLexer.test('''## #U^jqX/4o`ceG)''', '''## #U^jqX/4o`ceG),<EOF>''', 190))

	def test_191(self):
		self.assertTrue(TestLexer.test('''## S''', '''## S,<EOF>''', 191))

	def test_192(self):
		self.assertTrue(TestLexer.test("3.752", "3.752,<EOF>", 192))

	def test_193(self):
		self.assertTrue(TestLexer.test("v76", "v76,<EOF>", 193))

	def test_194(self):
		self.assertTrue(TestLexer.test('''## ,B8Bw_%Dz''', '''## ,B8Bw_%Dz,<EOF>''', 194))

	def test_195(self):
		self.assertTrue(TestLexer.test('''## WkL)5,wA8P=X3 z>u[.=''', '''## WkL)5,wA8P=X3 z>u[.=,<EOF>''', 195))

	def test_196(self):
		self.assertTrue(TestLexer.test("640e+68", "640e+68,<EOF>", 196))

	def test_197(self):
		self.assertTrue(TestLexer.test('''## AU;_xt''', '''## AU;_xt,<EOF>''', 197))

	def test_198(self):
		self.assertTrue(TestLexer.test('''## sfF9Wg|Nfw''', '''## sfF9Wg|Nfw,<EOF>''', 198))

	def test_199(self):
		self.assertTrue(TestLexer.test("arUakw99e", "arUakw99e,<EOF>", 199))

	def test_200(self):
		self.assertTrue(TestLexer.test('''"'"\\lM
"''', '''Illegal Escape In String: '"\\l''', 200))

	def test_201(self):
		self.assertTrue(TestLexer.test('''## ?&`O^SH''', '''## ?&`O^SH,<EOF>''', 201))

	def test_202(self):
		self.assertTrue(TestLexer.test("8.196", "8.196,<EOF>", 202))

	def test_203(self):
		self.assertTrue(TestLexer.test("JVnzdi", "JVnzdi,<EOF>", 203))

	def test_204(self):
		self.assertTrue(TestLexer.test('''"x ''', '''Unclosed String: x ''', 204))

	def test_205(self):
		self.assertTrue(TestLexer.test("5.650", "5.650,<EOF>", 205))

	def test_206(self):
		self.assertTrue(TestLexer.test('''"FnQ'""''', '''FnQ'",<EOF>''', 206))

	def test_207(self):
		self.assertTrue(TestLexer.test("18.018", "18.018,<EOF>", 207))

	def test_208(self):
		self.assertTrue(TestLexer.test('''## fIx$pk/kL2u%!NE''', '''## fIx$pk/kL2u%!NE,<EOF>''', 208))

	def test_209(self):
		self.assertTrue(TestLexer.test("6", "6,<EOF>", 209))

	def test_210(self):
		self.assertTrue(TestLexer.test("76", "76,<EOF>", 210))

	def test_211(self):
		self.assertTrue(TestLexer.test("3E93", "3E93,<EOF>", 211))

	def test_212(self):
		self.assertTrue(TestLexer.test('''## C.8ILAUI''', '''## C.8ILAUI,<EOF>''', 212))

	def test_213(self):
		self.assertTrue(TestLexer.test('''## O8ijd49b/%1S''', '''## O8ijd49b/%1S,<EOF>''', 213))

	def test_214(self):
		self.assertTrue(TestLexer.test("58e36", "58e36,<EOF>", 214))

	def test_215(self):
		self.assertTrue(TestLexer.test('''## :d9Uw ''', '''## :d9Uw ,<EOF>''', 215))

	def test_216(self):
		self.assertTrue(TestLexer.test("6.032e+82", "6.032e+82,<EOF>", 216))

	def test_217(self):
		self.assertTrue(TestLexer.test("uZnp", "uZnp,<EOF>", 217))

	def test_218(self):
		self.assertTrue(TestLexer.test("49.825E15", "49.825E15,<EOF>", 218))

	def test_219(self):
		self.assertTrue(TestLexer.test("865E-95", "865E-95,<EOF>", 219))

	def test_220(self):
		self.assertTrue(TestLexer.test('''## Bz''', '''## Bz,<EOF>''', 220))

	def test_221(self):
		self.assertTrue(TestLexer.test("4.607", "4.607,<EOF>", 221))

	def test_222(self):
		self.assertTrue(TestLexer.test('''## 1nkvb|''', '''## 1nkvb|,<EOF>''', 222))

	def test_223(self):
		self.assertTrue(TestLexer.test("96.850", "96.850,<EOF>", 223))

	def test_224(self):
		self.assertTrue(TestLexer.test("72.590", "72.590,<EOF>", 224))

	def test_225(self):
		self.assertTrue(TestLexer.test('''## D e=TN7ss!07N,''', '''## D e=TN7ss!07N,,<EOF>''', 225))

	def test_226(self):
		self.assertTrue(TestLexer.test('''## rJ^u01%+jc^pp?w;''', '''## rJ^u01%+jc^pp?w;,<EOF>''', 226))

	def test_227(self):
		self.assertTrue(TestLexer.test('''##  ;KbW(ORm@ >~s;''', '''##  ;KbW(ORm@ >~s;,<EOF>''', 227))

	def test_228(self):
		self.assertTrue(TestLexer.test('''## 4?OkKg0Ie+fx3u3?''', '''## 4?OkKg0Ie+fx3u3?,<EOF>''', 228))

	def test_229(self):
		self.assertTrue(TestLexer.test('''## h/]''', '''## h/],<EOF>''', 229))

	def test_230(self):
		self.assertTrue(TestLexer.test("6", "6,<EOF>", 230))

	def test_231(self):
		self.assertTrue(TestLexer.test('''## wrqLx''', '''## wrqLx,<EOF>''', 231))

	def test_232(self):
		self.assertTrue(TestLexer.test("u5wc", "u5wc,<EOF>", 232))

	def test_233(self):
		self.assertTrue(TestLexer.test('''"'"'"'"'"'" ''', '''Unclosed String: '"'"'"'"'" ''', 233))

	def test_234(self):
		self.assertTrue(TestLexer.test('''## 9/VbawM!#1N=3M=lloKI''', '''## 9/VbawM!#1N=3M=lloKI,<EOF>''', 234))

	def test_235(self):
		self.assertTrue(TestLexer.test("WPCICLv7E7", "WPCICLv7E7,<EOF>", 235))

	def test_236(self):
		self.assertTrue(TestLexer.test('''## g]#3HzY|6''', '''## g]#3HzY|6,<EOF>''', 236))

	def test_237(self):
		self.assertTrue(TestLexer.test("Pmxc&", "Pmxc,Error Token &", 237))

	def test_238(self):
		self.assertTrue(TestLexer.test('''## Pi7N!j@g0Fh1(C,2''', '''## Pi7N!j@g0Fh1(C,2,<EOF>''', 238))

	def test_239(self):
		self.assertTrue(TestLexer.test("594.298e+04", "594.298e+04,<EOF>", 239))

	def test_240(self):
		self.assertTrue(TestLexer.test("s_RrT", "s_RrT,<EOF>", 240))

	def test_241(self):
		self.assertTrue(TestLexer.test("1", "1,<EOF>", 241))

	def test_242(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 242))

	def test_243(self):
		self.assertTrue(TestLexer.test("6.995", "6.995,<EOF>", 243))

	def test_244(self):
		self.assertTrue(TestLexer.test("372", "372,<EOF>", 244))

	def test_245(self):
		self.assertTrue(TestLexer.test("8.826e+62", "8.826e+62,<EOF>", 245))

	def test_246(self):
		self.assertTrue(TestLexer.test('''"'"\\y'"'""''', '''Illegal Escape In String: '"\\y''', 246))

	def test_247(self):
		self.assertTrue(TestLexer.test("#b", "Error Token #", 247))

	def test_248(self):
		self.assertTrue(TestLexer.test('''## p.jA89X''', '''## p.jA89X,<EOF>''', 248))

	def test_249(self):
		self.assertTrue(TestLexer.test('''## @le''', '''## @le,<EOF>''', 249))

	def test_250(self):
		self.assertTrue(TestLexer.test("VDA", "VDA,<EOF>", 250))

	def test_251(self):
		self.assertTrue(TestLexer.test('''"S\\a'""''', '''Illegal Escape In String: S\\a''', 251))

	def test_252(self):
		self.assertTrue(TestLexer.test("$H", "Error Token $", 252))

	def test_253(self):
		self.assertTrue(TestLexer.test("__B", "__B,<EOF>", 253))

	def test_254(self):
		self.assertTrue(TestLexer.test("Jd", "Jd,<EOF>", 254))

	def test_255(self):
		self.assertTrue(TestLexer.test("20E-10", "20E-10,<EOF>", 255))

	def test_256(self):
		self.assertTrue(TestLexer.test("VGWKGUXa", "VGWKGUXa,<EOF>", 256))

	def test_257(self):
		self.assertTrue(TestLexer.test('''## bm!%-X wFp_7;=`''', '''## bm!%-X wFp_7;=`,<EOF>''', 257))

	def test_258(self):
		self.assertTrue(TestLexer.test("N", "N,<EOF>", 258))

	def test_259(self):
		self.assertTrue(TestLexer.test("147.571E+40", "147.571E+40,<EOF>", 259))

	def test_260(self):
		self.assertTrue(TestLexer.test('''## @@cj''', '''## @@cj,<EOF>''', 260))

	def test_261(self):
		self.assertTrue(TestLexer.test('''## K`Nc[e(pY<[d5[9=,f''', '''## K`Nc[e(pY<[d5[9=,f,<EOF>''', 261))

	def test_262(self):
		self.assertTrue(TestLexer.test('''"
O."''', '''Unclosed String: ''', 262))

	def test_263(self):
		self.assertTrue(TestLexer.test('''## e N;nI''', '''## e N;nI,<EOF>''', 263))

	def test_264(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 264))

	def test_265(self):
		self.assertTrue(TestLexer.test("580.384", "580.384,<EOF>", 265))

	def test_266(self):
		self.assertTrue(TestLexer.test("&jv&0^h", "Error Token &", 266))

	def test_267(self):
		self.assertTrue(TestLexer.test("79.817", "79.817,<EOF>", 267))

	def test_268(self):
		self.assertTrue(TestLexer.test('''## /''', '''## /,<EOF>''', 268))

	def test_269(self):
		self.assertTrue(TestLexer.test('''## t''', '''## t,<EOF>''', 269))

	def test_270(self):
		self.assertTrue(TestLexer.test("5.885E+25", "5.885E+25,<EOF>", 270))

	def test_271(self):
		self.assertTrue(TestLexer.test('''"'"\\d2Cdw"''', '''Illegal Escape In String: '"\\d''', 271))

	def test_272(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 272))

	def test_273(self):
		self.assertTrue(TestLexer.test('''## Z(Zv''', '''## Z(Zv,<EOF>''', 273))

	def test_274(self):
		self.assertTrue(TestLexer.test('''## |TPxG~V+[&ST2hnFap''', '''## |TPxG~V+[&ST2hnFap,<EOF>''', 274))

	def test_275(self):
		self.assertTrue(TestLexer.test('''## FPhE#|l97''', '''## FPhE#|l97,<EOF>''', 275))

	def test_276(self):
		self.assertTrue(TestLexer.test("1.847e-10", "1.847e-10,<EOF>", 276))

	def test_277(self):
		self.assertTrue(TestLexer.test("7e+15", "7e+15,<EOF>", 277))

	def test_278(self):
		self.assertTrue(TestLexer.test("5kFSbU_", "5,kFSbU_,<EOF>", 278))

	def test_279(self):
		self.assertTrue(TestLexer.test('''## `kS0j8[F13LpTV>MI''', '''## `kS0j8[F13LpTV>MI,<EOF>''', 279))

	def test_280(self):
		self.assertTrue(TestLexer.test("^&jbg", "Error Token ^", 280))

	def test_281(self):
		self.assertTrue(TestLexer.test('''"\\u%'"'"'""''', '''Illegal Escape In String: \\u''', 281))

	def test_282(self):
		self.assertTrue(TestLexer.test("296.665e-76", "296.665e-76,<EOF>", 282))

	def test_283(self):
		self.assertTrue(TestLexer.test('''## i[%r4?a&t''', '''## i[%r4?a&t,<EOF>''', 283))

	def test_284(self):
		self.assertTrue(TestLexer.test("23", "23,<EOF>", 284))

	def test_285(self):
		self.assertTrue(TestLexer.test('''"
'""''', '''Unclosed String: ''', 285))

	def test_286(self):
		self.assertTrue(TestLexer.test("48", "48,<EOF>", 286))

	def test_287(self):
		self.assertTrue(TestLexer.test("6", "6,<EOF>", 287))

	def test_288(self):
		self.assertTrue(TestLexer.test('''## S]_H24''', '''## S]_H24,<EOF>''', 288))

	def test_289(self):
		self.assertTrue(TestLexer.test('''## `^B:n^q3Cf<''', '''## `^B:n^q3Cf<,<EOF>''', 289))

	def test_290(self):
		self.assertTrue(TestLexer.test('''"\\p'"'"%'"'""''', '''Illegal Escape In String: \\p''', 290))

	def test_291(self):
		self.assertTrue(TestLexer.test('''## 3[,@xdS^''', '''## 3[,@xdS^,<EOF>''', 291))

	def test_292(self):
		self.assertTrue(TestLexer.test("90E+00", "90E+00,<EOF>", 292))

	def test_293(self):
		self.assertTrue(TestLexer.test('''## CsuesOMCe~j?''', '''## CsuesOMCe~j?,<EOF>''', 293))

	def test_294(self):
		self.assertTrue(TestLexer.test('''"'"5AI"''', '''\'"5AI,<EOF>''', 294))

	def test_295(self):
		self.assertTrue(TestLexer.test("9.556", "9.556,<EOF>", 295))

	def test_296(self):
		self.assertTrue(TestLexer.test('''"'"\\i'"'"D'""''', '''Illegal Escape In String: '"\\i''', 296))

	def test_297(self):
		self.assertTrue(TestLexer.test("437.684e+83", "437.684e+83,<EOF>", 297))

	def test_298(self):
		self.assertTrue(TestLexer.test("226.192E44", "226.192E44,<EOF>", 298))

	def test_299(self):
		self.assertTrue(TestLexer.test('''## .-''', '''## .-,<EOF>''', 299))

	def test_300(self):
		self.assertTrue(TestLexer.test('''## R''', '''## R,<EOF>''', 300))

	def test_301(self):
		self.assertTrue(TestLexer.test("zi", "zi,<EOF>", 301))

	def test_302(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 302))

	def test_303(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 303))

	def test_304(self):
		self.assertTrue(TestLexer.test('''"W\\d'""''', '''Illegal Escape In String: W\\d''', 304))

	def test_305(self):
		self.assertTrue(TestLexer.test('''## @;''', '''## @;,<EOF>''', 305))

	def test_306(self):
		self.assertTrue(TestLexer.test('''## ,''', '''## ,,<EOF>''', 306))

	def test_307(self):
		self.assertTrue(TestLexer.test('''"r'"'"'""''', '''r'"'"'",<EOF>''', 307))

	def test_308(self):
		self.assertTrue(TestLexer.test("70.494", "70.494,<EOF>", 308))

	def test_309(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 309))

	def test_310(self):
		self.assertTrue(TestLexer.test('''## i?@H,?NKL3jlvZ`''', '''## i?@H,?NKL3jlvZ`,<EOF>''', 310))

	def test_311(self):
		self.assertTrue(TestLexer.test("0.462", "0.462,<EOF>", 311))

	def test_312(self):
		self.assertTrue(TestLexer.test('''"S'"
'"O'""''', '''Unclosed String: S'"''', 312))

	def test_313(self):
		self.assertTrue(TestLexer.test("SL2D", "SL2D,<EOF>", 313))

	def test_314(self):
		self.assertTrue(TestLexer.test('''"'"'"='"\\u'""''', '''Illegal Escape In String: '"'"='"\\u''', 314))

	def test_315(self):
		self.assertTrue(TestLexer.test("50", "50,<EOF>", 315))

	def test_316(self):
		self.assertTrue(TestLexer.test("852.427e-48", "852.427e-48,<EOF>", 316))

	def test_317(self):
		self.assertTrue(TestLexer.test('''"$'"a'"'""''', '''$'"a'"'",<EOF>''', 317))

	def test_318(self):
		self.assertTrue(TestLexer.test("xIWqhI6o", "xIWqhI6o,<EOF>", 318))

	def test_319(self):
		self.assertTrue(TestLexer.test("f4NsX28k", "f4NsX28k,<EOF>", 319))

	def test_320(self):
		self.assertTrue(TestLexer.test("X8", "X8,<EOF>", 320))

	def test_321(self):
		self.assertTrue(TestLexer.test("35.365", "35.365,<EOF>", 321))

	def test_322(self):
		self.assertTrue(TestLexer.test("9tmLZnOX", "9,tmLZnOX,<EOF>", 322))

	def test_323(self):
		self.assertTrue(TestLexer.test('''## :^5mk9c( <UBA^&+''', '''## :^5mk9c( <UBA^&+,<EOF>''', 323))

	def test_324(self):
		self.assertTrue(TestLexer.test("662", "662,<EOF>", 324))

	def test_325(self):
		self.assertTrue(TestLexer.test('''".''"6"''', '''Illegal Escape In String: .''''', 325))

	def test_326(self):
		self.assertTrue(TestLexer.test('''## c5nq)~m55j/@7Fl8WU''', '''## c5nq)~m55j/@7Fl8WU,<EOF>''', 326))

	def test_327(self):
		self.assertTrue(TestLexer.test('''## Ib,3joAK''', '''## Ib,3joAK,<EOF>''', 327))

	def test_328(self):
		self.assertTrue(TestLexer.test('''"vi
'"'"'""''', '''Unclosed String: vi''', 328))

	def test_329(self):
		self.assertTrue(TestLexer.test("YFV", "YFV,<EOF>", 329))

	def test_330(self):
		self.assertTrue(TestLexer.test('''## LwNifOoOB5<#Ea/''', '''## LwNifOoOB5<#Ea/,<EOF>''', 330))

	def test_331(self):
		self.assertTrue(TestLexer.test("u#^0@U6W", "u,Error Token #", 331))

	def test_332(self):
		self.assertTrue(TestLexer.test('''## VI@i(V[&r}Ee''', '''## VI@i(V[&r}Ee,<EOF>''', 332))

	def test_333(self):
		self.assertTrue(TestLexer.test('''"'"'"'" ''', '''Unclosed String: '"'"'" ''', 333))

	def test_334(self):
		self.assertTrue(TestLexer.test('''## )KC9b6L&rrJ=cK''', '''## )KC9b6L&rrJ=cK,<EOF>''', 334))

	def test_335(self):
		self.assertTrue(TestLexer.test("94.331", "94.331,<EOF>", 335))

	def test_336(self):
		self.assertTrue(TestLexer.test("cdKFC", "cdKFC,<EOF>", 336))

	def test_337(self):
		self.assertTrue(TestLexer.test("U", "U,<EOF>", 337))

	def test_338(self):
		self.assertTrue(TestLexer.test("801E-02", "801E-02,<EOF>", 338))

	def test_339(self):
		self.assertTrue(TestLexer.test("714", "714,<EOF>", 339))

	def test_340(self):
		self.assertTrue(TestLexer.test("0.634", "0.634,<EOF>", 340))

	def test_341(self):
		self.assertTrue(TestLexer.test('''"'"\\l'"&"''', '''Illegal Escape In String: '"\\l''', 341))

	def test_342(self):
		self.assertTrue(TestLexer.test("VqU$RV", "VqU,Error Token $", 342))

	def test_343(self):
		self.assertTrue(TestLexer.test('''## y.3R)uV%s:DTDg''', '''## y.3R)uV%s:DTDg,<EOF>''', 343))

	def test_344(self):
		self.assertTrue(TestLexer.test("1.516", "1.516,<EOF>", 344))

	def test_345(self):
		self.assertTrue(TestLexer.test("9E65", "9E65,<EOF>", 345))

	def test_346(self):
		self.assertTrue(TestLexer.test('''"'"3'"\\l'""''', '''Illegal Escape In String: '"3'"\\l''', 346))

	def test_347(self):
		self.assertTrue(TestLexer.test("98e+71", "98e+71,<EOF>", 347))

	def test_348(self):
		self.assertTrue(TestLexer.test("U", "U,<EOF>", 348))

	def test_349(self):
		self.assertTrue(TestLexer.test("975E-91", "975E-91,<EOF>", 349))

	def test_350(self):
		self.assertTrue(TestLexer.test("2.166E14", "2.166E14,<EOF>", 350))

	def test_351(self):
		self.assertTrue(TestLexer.test('''## <N[G4Xa''', '''## <N[G4Xa,<EOF>''', 351))

	def test_352(self):
		self.assertTrue(TestLexer.test("W1pgM", "W1pgM,<EOF>", 352))

	def test_353(self):
		self.assertTrue(TestLexer.test("1BM9qc", "1,BM9qc,<EOF>", 353))

	def test_354(self):
		self.assertTrue(TestLexer.test("#4x2TjMfJ_", "Error Token #", 354))

	def test_355(self):
		self.assertTrue(TestLexer.test('''"'"\\o'"
"''', '''Illegal Escape In String: '"\\o''', 355))

	def test_356(self):
		self.assertTrue(TestLexer.test('''"
z'"'"'""''', '''Unclosed String: ''', 356))

	def test_357(self):
		self.assertTrue(TestLexer.test('''"_"''', '''Unclosed String: ''', 357))

	def test_358(self):
		self.assertTrue(TestLexer.test('''## *(34X`Ke@P<+''', '''## *(34X`Ke@P<+,<EOF>''', 358))

	def test_359(self):
		self.assertTrue(TestLexer.test("t", "t,<EOF>", 359))

	def test_360(self):
		self.assertTrue(TestLexer.test("_GjgH", "_GjgH,<EOF>", 360))

	def test_361(self):
		self.assertTrue(TestLexer.test("101.417e-93", "101.417e-93,<EOF>", 361))

	def test_362(self):
		self.assertTrue(TestLexer.test('''## PNDP^!v5O<hF4F?kEB''', '''## PNDP^!v5O<hF4F?kEB,<EOF>''', 362))

	def test_363(self):
		self.assertTrue(TestLexer.test("4", "4,<EOF>", 363))

	def test_364(self):
		self.assertTrue(TestLexer.test('''"'"\\a'""''', '''Illegal Escape In String: '"\\a''', 364))

	def test_365(self):
		self.assertTrue(TestLexer.test('''## )1BM}CF9V<pIKXzgy ]s''', '''## )1BM}CF9V<pIKXzgy ]s,<EOF>''', 365))

	def test_366(self):
		self.assertTrue(TestLexer.test("FFBJyY", "FFBJyY,<EOF>", 366))

	def test_367(self):
		self.assertTrue(TestLexer.test("T", "T,<EOF>", 367))

	def test_368(self):
		self.assertTrue(TestLexer.test("yG", "yG,<EOF>", 368))

	def test_369(self):
		self.assertTrue(TestLexer.test('''## `p''', '''## `p,<EOF>''', 369))

	def test_370(self):
		self.assertTrue(TestLexer.test('''## _+hOJ!}K*a_m;wtA:3<t''', '''## _+hOJ!}K*a_m;wtA:3<t,<EOF>''', 370))

	def test_371(self):
		self.assertTrue(TestLexer.test('''## S P6jh@a#dzwHU]5''', '''## S P6jh@a#dzwHU]5,<EOF>''', 371))

	def test_372(self):
		self.assertTrue(TestLexer.test("OB$s", "OB,Error Token $", 372))

	def test_373(self):
		self.assertTrue(TestLexer.test('''## yZ!;X<S,,I''', '''## yZ!;X<S,,I,<EOF>''', 373))

	def test_374(self):
		self.assertTrue(TestLexer.test("65", "65,<EOF>", 374))

	def test_375(self):
		self.assertTrue(TestLexer.test('''"\\v'""''', '''Illegal Escape In String: \\v''', 375))

	def test_376(self):
		self.assertTrue(TestLexer.test("A3WXZeyX", "A3WXZeyX,<EOF>", 376))

	def test_377(self):
		self.assertTrue(TestLexer.test('''"n'"'"\\y'""''', '''Illegal Escape In String: n'"'"\\y''', 377))

	def test_378(self):
		self.assertTrue(TestLexer.test('''"\\x'"'""''', '''Illegal Escape In String: \\x''', 378))

	def test_379(self):
		self.assertTrue(TestLexer.test("84.559", "84.559,<EOF>", 379))

	def test_380(self):
		self.assertTrue(TestLexer.test('''## 0q:^u]O.tz+&@p?''', '''## 0q:^u]O.tz+&@p?,<EOF>''', 380))

	def test_381(self):
		self.assertTrue(TestLexer.test("8.862", "8.862,<EOF>", 381))

	def test_382(self):
		self.assertTrue(TestLexer.test("V3n^W9vC", "V3n,Error Token ^", 382))

	def test_383(self):
		self.assertTrue(TestLexer.test("#MfD6LFeO", "Error Token #", 383))

	def test_384(self):
		self.assertTrue(TestLexer.test("ziJY5", "ziJY5,<EOF>", 384))

	def test_385(self):
		self.assertTrue(TestLexer.test("_F7&Xaw", "_F7,Error Token &", 385))

	def test_386(self):
		self.assertTrue(TestLexer.test('''## K?vvqk?dAh$7""B''', '''## K?vvqk?dAh$7""B,<EOF>''', 386))

	def test_387(self):
		self.assertTrue(TestLexer.test("r7_", "r7_,<EOF>", 387))

	def test_388(self):
		self.assertTrue(TestLexer.test("FpPZ", "FpPZ,<EOF>", 388))

	def test_389(self):
		self.assertTrue(TestLexer.test("a8hO", "a8hO,<EOF>", 389))

	def test_390(self):
		self.assertTrue(TestLexer.test('''"66'"2 ''', '''Unclosed String: 66'"2 ''', 390))

	def test_391(self):
		self.assertTrue(TestLexer.test("RajdEQoy05", "RajdEQoy05,<EOF>", 391))

	def test_392(self):
		self.assertTrue(TestLexer.test("302.092E-41", "302.092E-41,<EOF>", 392))

	def test_393(self):
		self.assertTrue(TestLexer.test("582.024E-84", "582.024E-84,<EOF>", 393))

	def test_394(self):
		self.assertTrue(TestLexer.test("57e-10", "57e-10,<EOF>", 394))

	def test_395(self):
		self.assertTrue(TestLexer.test("0.698", "0.698,<EOF>", 395))

	def test_396(self):
		self.assertTrue(TestLexer.test('''## h(q|<W-fJ_:^}~Jfx''', '''## h(q|<W-fJ_:^}~Jfx,<EOF>''', 396))

	def test_397(self):
		self.assertTrue(TestLexer.test("508", "508,<EOF>", 397))

	def test_398(self):
		self.assertTrue(TestLexer.test('''"I/\\kn'"K"''', '''Illegal Escape In String: I/\\k''', 398))

	def test_399(self):
		self.assertTrue(TestLexer.test('''"p"''', '''p,<EOF>''', 399))

	def test_400(self):
		self.assertTrue(TestLexer.test('''## =~.<[PWC6v''', '''## =~.<[PWC6v,<EOF>''', 400))

	def test_401(self):
		self.assertTrue(TestLexer.test("1e30", "1e30,<EOF>", 401))

	def test_402(self):
		self.assertTrue(TestLexer.test('''"g"''', '''g,<EOF>''', 402))

	def test_403(self):
		self.assertTrue(TestLexer.test("q", "q,<EOF>", 403))

	def test_404(self):
		self.assertTrue(TestLexer.test('''## E''', '''## E,<EOF>''', 404))

	def test_405(self):
		self.assertTrue(TestLexer.test("Q^", "Q,Error Token ^", 405))

	def test_406(self):
		self.assertTrue(TestLexer.test('''## d`$ix_7nrYk[''', '''## d`$ix_7nrYk[,<EOF>''', 406))

	def test_407(self):
		self.assertTrue(TestLexer.test("554.752E-73", "554.752E-73,<EOF>", 407))

	def test_408(self):
		self.assertTrue(TestLexer.test("E", "E,<EOF>", 408))

	def test_409(self):
		self.assertTrue(TestLexer.test("ayXa9ScWn", "ayXa9ScWn,<EOF>", 409))

	def test_410(self):
		self.assertTrue(TestLexer.test('''"\\s4DS'"'""''', '''Illegal Escape In String: \\s''', 410))

	def test_411(self):
		self.assertTrue(TestLexer.test("x7mrDY", "x7mrDY,<EOF>", 411))

	def test_412(self):
		self.assertTrue(TestLexer.test('''## sz<^!pUMc''', '''## sz<^!pUMc,<EOF>''', 412))

	def test_413(self):
		self.assertTrue(TestLexer.test('''"'"'"("''', '''\'"'"(,<EOF>''', 413))

	def test_414(self):
		self.assertTrue(TestLexer.test('''## ??i[IrI''', '''## ??i[IrI,<EOF>''', 414))

	def test_415(self):
		self.assertTrue(TestLexer.test("t", "t,<EOF>", 415))

	def test_416(self):
		self.assertTrue(TestLexer.test('''"g"''', '''g,<EOF>''', 416))

	def test_417(self):
		self.assertTrue(TestLexer.test("8.584e-58", "8.584e-58,<EOF>", 417))

	def test_418(self):
		self.assertTrue(TestLexer.test('''"- ''', '''Unclosed String: - ''', 418))

	def test_419(self):
		self.assertTrue(TestLexer.test('''"3'" ''', '''Unclosed String: 3'" ''', 419))

	def test_420(self):
		self.assertTrue(TestLexer.test("10e86", "10e86,<EOF>", 420))

	def test_421(self):
		self.assertTrue(TestLexer.test("Fs36", "Fs36,<EOF>", 421))

	def test_422(self):
		self.assertTrue(TestLexer.test("03dF&", "03,dF,Error Token &", 422))

	def test_423(self):
		self.assertTrue(TestLexer.test('''"s\\ax,"''', '''Illegal Escape In String: s\\a''', 423))

	def test_424(self):
		self.assertTrue(TestLexer.test("c&Rs54CB", "c,Error Token &", 424))

	def test_425(self):
		self.assertTrue(TestLexer.test('''"'"aj"''', '''\'"aj,<EOF>''', 425))

	def test_426(self):
		self.assertTrue(TestLexer.test("98.254", "98.254,<EOF>", 426))

	def test_427(self):
		self.assertTrue(TestLexer.test('''## ky$''', '''## ky$,<EOF>''', 427))

	def test_428(self):
		self.assertTrue(TestLexer.test("9.433", "9.433,<EOF>", 428))

	def test_429(self):
		self.assertTrue(TestLexer.test("kdTG", "kdTG,<EOF>", 429))

	def test_430(self):
		self.assertTrue(TestLexer.test("43.741E+59", "43.741E+59,<EOF>", 430))

	def test_431(self):
		self.assertTrue(TestLexer.test('''## etd''', '''## etd,<EOF>''', 431))

	def test_432(self):
		self.assertTrue(TestLexer.test('''"'"
'"'""''', '''Unclosed String: '"''', 432))

	def test_433(self):
		self.assertTrue(TestLexer.test('''## FuIv!e''', '''## FuIv!e,<EOF>''', 433))

	def test_434(self):
		self.assertTrue(TestLexer.test("6.466E+18", "6.466E+18,<EOF>", 434))

	def test_435(self):
		self.assertTrue(TestLexer.test('''## K`h$o8/mDSgSlFP_a''', '''## K`h$o8/mDSgSlFP_a,<EOF>''', 435))

	def test_436(self):
		self.assertTrue(TestLexer.test('''"5'"'"'"D"''', '''5'"'"'"D,<EOF>''', 436))

	def test_437(self):
		self.assertTrue(TestLexer.test("JUt_", "JUt_,<EOF>", 437))

	def test_438(self):
		self.assertTrue(TestLexer.test("q3kCR4q5I", "q3kCR4q5I,<EOF>", 438))

	def test_439(self):
		self.assertTrue(TestLexer.test("406.355", "406.355,<EOF>", 439))

	def test_440(self):
		self.assertTrue(TestLexer.test("yIXrxO", "yIXrxO,<EOF>", 440))

	def test_441(self):
		self.assertTrue(TestLexer.test('''## yXH0QjKOm5Su&Z&~iJP''', '''## yXH0QjKOm5Su&Z&~iJP,<EOF>''', 441))

	def test_442(self):
		self.assertTrue(TestLexer.test("j1R^jP", "j1R,Error Token ^", 442))

	def test_443(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 443))

	def test_444(self):
		self.assertTrue(TestLexer.test("74aM&7uO_5", "74,aM,Error Token &", 444))

	def test_445(self):
		self.assertTrue(TestLexer.test("c0^o^au5z", "c0,Error Token ^", 445))

	def test_446(self):
		self.assertTrue(TestLexer.test('''## {*h&#}''', '''## {*h&#},<EOF>''', 446))

	def test_447(self):
		self.assertTrue(TestLexer.test("q", "q,<EOF>", 447))

	def test_448(self):
		self.assertTrue(TestLexer.test('''## D_4y=wzVdu1|Vo(%P|''', '''## D_4y=wzVdu1|Vo(%P|,<EOF>''', 448))

	def test_449(self):
		self.assertTrue(TestLexer.test('''## HgZZn/_NY,r)!]4f||U''', '''## HgZZn/_NY,r)!]4f||U,<EOF>''', 449))

	def test_450(self):
		self.assertTrue(TestLexer.test("896", "896,<EOF>", 450))

	def test_451(self):
		self.assertTrue(TestLexer.test('''## E<WQb* 9GkHyg=5_''', '''## E<WQb* 9GkHyg=5_,<EOF>''', 451))

	def test_452(self):
		self.assertTrue(TestLexer.test("8E+05", "8E+05,<EOF>", 452))

	def test_453(self):
		self.assertTrue(TestLexer.test('''## GQ0|NIZhwpHi''', '''## GQ0|NIZhwpHi,<EOF>''', 453))

	def test_454(self):
		self.assertTrue(TestLexer.test("gb89SoF", "gb89SoF,<EOF>", 454))

	def test_455(self):
		self.assertTrue(TestLexer.test("#EpeVGo", "Error Token #", 455))

	def test_456(self):
		self.assertTrue(TestLexer.test("Rk", "Rk,<EOF>", 456))

	def test_457(self):
		self.assertTrue(TestLexer.test("iIUB&JDhAo", "iIUB,Error Token &", 457))

	def test_458(self):
		self.assertTrue(TestLexer.test("su3", "su3,<EOF>", 458))

	def test_459(self):
		self.assertTrue(TestLexer.test("em443", "em443,<EOF>", 459))

	def test_460(self):
		self.assertTrue(TestLexer.test("95.415E+38", "95.415E+38,<EOF>", 460))

	def test_461(self):
		self.assertTrue(TestLexer.test("4", "4,<EOF>", 461))

	def test_462(self):
		self.assertTrue(TestLexer.test('''"
N"''', '''Unclosed String: ''', 462))

	def test_463(self):
		self.assertTrue(TestLexer.test('''"TA2'"F ''', '''Unclosed String: TA2'"F ''', 463))

	def test_464(self):
		self.assertTrue(TestLexer.test('''## 5TAnrK:f''', '''## 5TAnrK:f,<EOF>''', 464))

	def test_465(self):
		self.assertTrue(TestLexer.test("@sLk#VP", "Error Token @", 465))

	def test_466(self):
		self.assertTrue(TestLexer.test("jZ93", "jZ93,<EOF>", 466))

	def test_467(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 467))

	def test_468(self):
		self.assertTrue(TestLexer.test('''"\\o'"'"W'""''', '''Illegal Escape In String: \\o''', 468))

	def test_469(self):
		self.assertTrue(TestLexer.test("594.462e-15", "594.462e-15,<EOF>", 469))

	def test_470(self):
		self.assertTrue(TestLexer.test("sSzp$jGJDE", "sSzp,Error Token $", 470))

	def test_471(self):
		self.assertTrue(TestLexer.test("88.059", "88.059,<EOF>", 471))

	def test_472(self):
		self.assertTrue(TestLexer.test('''"r'"'""''', '''r'"'",<EOF>''', 472))

	def test_473(self):
		self.assertTrue(TestLexer.test('''"
Pi"''', '''Unclosed String: ''', 473))

	def test_474(self):
		self.assertTrue(TestLexer.test('''## sM"/[Ef!sYfoUAc.=''', '''## sM"/[Ef!sYfoUAc.=,<EOF>''', 474))

	def test_475(self):
		self.assertTrue(TestLexer.test("D_eoky", "D_eoky,<EOF>", 475))

	def test_476(self):
		self.assertTrue(TestLexer.test('''## 9@{VD#$yA.!|Q4f''', '''## 9@{VD#$yA.!|Q4f,<EOF>''', 476))

	def test_477(self):
		self.assertTrue(TestLexer.test("5.147e+51", "5.147e+51,<EOF>", 477))

	def test_478(self):
		self.assertTrue(TestLexer.test("2.497e+08", "2.497e+08,<EOF>", 478))

	def test_479(self):
		self.assertTrue(TestLexer.test("V@", "V,Error Token @", 479))

	def test_480(self):
		self.assertTrue(TestLexer.test('''## d''', '''## d,<EOF>''', 480))

	def test_481(self):
		self.assertTrue(TestLexer.test("mNYze^", "mNYze,Error Token ^", 481))

	def test_482(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 482))

	def test_483(self):
		self.assertTrue(TestLexer.test("vnWaj^", "vnWaj,Error Token ^", 483))

	def test_484(self):
		self.assertTrue(TestLexer.test('''"
#Es'"'""''', '''Unclosed String: ''', 484))

	def test_485(self):
		self.assertTrue(TestLexer.test("17.626", "17.626,<EOF>", 485))

	def test_486(self):
		self.assertTrue(TestLexer.test("uQZ0wVDK", "uQZ0wVDK,<EOF>", 486))

	def test_487(self):
		self.assertTrue(TestLexer.test("755.585", "755.585,<EOF>", 487))

	def test_488(self):
		self.assertTrue(TestLexer.test('''"7R'""''', '''7R'",<EOF>''', 488))

	def test_489(self):
		self.assertTrue(TestLexer.test("RMm4z$7S", "RMm4z,Error Token $", 489))

	def test_490(self):
		self.assertTrue(TestLexer.test('''"'"'"'"}'" ''', '''Unclosed String: '"'"'"}'" ''', 490))

	def test_491(self):
		self.assertTrue(TestLexer.test('''")'"'"'"\\z'""''', '''Illegal Escape In String: )'"'"'"\\z''', 491))

	def test_492(self):
		self.assertTrue(TestLexer.test("z", "z,<EOF>", 492))

	def test_493(self):
		self.assertTrue(TestLexer.test('''## oW9u&&s,g5~Y''', '''## oW9u&&s,g5~Y,<EOF>''', 493))

	def test_494(self):
		self.assertTrue(TestLexer.test("121", "121,<EOF>", 494))

	def test_495(self):
		self.assertTrue(TestLexer.test("V^X#&ANp@", "V,Error Token ^", 495))

	def test_496(self):
		self.assertTrue(TestLexer.test("L4", "L4,<EOF>", 496))

	def test_497(self):
		self.assertTrue(TestLexer.test('''## u6ok a}I''', '''## u6ok a}I,<EOF>''', 497))

	def test_498(self):
		self.assertTrue(TestLexer.test('''"'"'"'"\\oO"''', '''Illegal Escape In String: '"'"'"\\o''', 498))

	def test_499(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 499))

	def test_500(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 500))

	def test_501(self):
		self.assertTrue(TestLexer.test('''"'"K'"'"'""''', '''\'"K'"'"'",<EOF>''', 501))

	def test_502(self):
		self.assertTrue(TestLexer.test('''## P%+nHqM|o{2ITW6wiW''', '''## P%+nHqM|o{2ITW6wiW,<EOF>''', 502))

	def test_503(self):
		self.assertTrue(TestLexer.test("95.438e35", "95.438e35,<EOF>", 503))

	def test_504(self):
		self.assertTrue(TestLexer.test("^t", "Error Token ^", 504))

	def test_505(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 505))

	def test_506(self):
		self.assertTrue(TestLexer.test('''## |MbPL''', '''## |MbPL,<EOF>''', 506))

	def test_507(self):
		self.assertTrue(TestLexer.test("28E+45", "28E+45,<EOF>", 507))

	def test_508(self):
		self.assertTrue(TestLexer.test("102.478", "102.478,<EOF>", 508))

	def test_509(self):
		self.assertTrue(TestLexer.test("UwGO", "UwGO,<EOF>", 509))

	def test_510(self):
		self.assertTrue(TestLexer.test("5.283E-20", "5.283E-20,<EOF>", 510))

	def test_511(self):
		self.assertTrue(TestLexer.test("411e40", "411e40,<EOF>", 511))

	def test_512(self):
		self.assertTrue(TestLexer.test("9FEDNi0^", "9,FEDNi0,Error Token ^", 512))

	def test_513(self):
		self.assertTrue(TestLexer.test('''"'"'"o'""''', '''\'"'"o'",<EOF>''', 513))

	def test_514(self):
		self.assertTrue(TestLexer.test("__0KVH@", "__0KVH,Error Token @", 514))

	def test_515(self):
		self.assertTrue(TestLexer.test("520", "520,<EOF>", 515))

	def test_516(self):
		self.assertTrue(TestLexer.test('''## 9)0KL+yxoiAQ6)i''', '''## 9)0KL+yxoiAQ6)i,<EOF>''', 516))

	def test_517(self):
		self.assertTrue(TestLexer.test("6.111e+31", "6.111e+31,<EOF>", 517))

	def test_518(self):
		self.assertTrue(TestLexer.test('''## Bs.b)CF''', '''## Bs.b)CF,<EOF>''', 518))

	def test_519(self):
		self.assertTrue(TestLexer.test("29.560", "29.560,<EOF>", 519))

	def test_520(self):
		self.assertTrue(TestLexer.test('''## -A*li''', '''## -A*li,<EOF>''', 520))

	def test_521(self):
		self.assertTrue(TestLexer.test("VAtsK0K1", "VAtsK0K1,<EOF>", 521))

	def test_522(self):
		self.assertTrue(TestLexer.test("6Aw#u^wQs", "6,Aw,Error Token #", 522))

	def test_523(self):
		self.assertTrue(TestLexer.test('''## *y E=]hEE6-4,w''', '''## *y E=]hEE6-4,w,<EOF>''', 523))

	def test_524(self):
		self.assertTrue(TestLexer.test("Se", "Se,<EOF>", 524))

	def test_525(self):
		self.assertTrue(TestLexer.test('''"'"\\i
%"''', '''Illegal Escape In String: '"\\i''', 525))

	def test_526(self):
		self.assertTrue(TestLexer.test('''## *z45ofQ7)Dfjj+SW''', '''## *z45ofQ7)Dfjj+SW,<EOF>''', 526))

	def test_527(self):
		self.assertTrue(TestLexer.test("5.707e48", "5.707e48,<EOF>", 527))

	def test_528(self):
		self.assertTrue(TestLexer.test('''"Tw'"b1"''', '''Tw'"b1,<EOF>''', 528))

	def test_529(self):
		self.assertTrue(TestLexer.test('''## `aX"ZXX">o+)+oe=YQjx''', '''## `aX"ZXX">o+)+oe=YQjx,<EOF>''', 529))

	def test_530(self):
		self.assertTrue(TestLexer.test("8E28", "8E28,<EOF>", 530))

	def test_531(self):
		self.assertTrue(TestLexer.test("54E-18", "54E-18,<EOF>", 531))

	def test_532(self):
		self.assertTrue(TestLexer.test("2.020", "2.020,<EOF>", 532))

	def test_533(self):
		self.assertTrue(TestLexer.test('''"h\\e'""''', '''Illegal Escape In String: h\\e''', 533))

	def test_534(self):
		self.assertTrue(TestLexer.test("Ng0hMa", "Ng0hMa,<EOF>", 534))

	def test_535(self):
		self.assertTrue(TestLexer.test("cu1u6e", "cu1u6e,<EOF>", 535))

	def test_536(self):
		self.assertTrue(TestLexer.test('''## -ea-doyxa2k6''', '''## -ea-doyxa2k6,<EOF>''', 536))

	def test_537(self):
		self.assertTrue(TestLexer.test('''## T!.63S}*n1p|[c:"{ +F''', '''## T!.63S}*n1p|[c:"{ +F,<EOF>''', 537))

	def test_538(self):
		self.assertTrue(TestLexer.test("HiV", "HiV,<EOF>", 538))

	def test_539(self):
		self.assertTrue(TestLexer.test('''"S
y"''', '''Unclosed String: S''', 539))

	def test_540(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 540))

	def test_541(self):
		self.assertTrue(TestLexer.test("9.447", "9.447,<EOF>", 541))

	def test_542(self):
		self.assertTrue(TestLexer.test("JqteO", "JqteO,<EOF>", 542))

	def test_543(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 543))

	def test_544(self):
		self.assertTrue(TestLexer.test("#Y&HC9", "Error Token #", 544))

	def test_545(self):
		self.assertTrue(TestLexer.test("58", "58,<EOF>", 545))

	def test_546(self):
		self.assertTrue(TestLexer.test('''## ?b]9i]7/>oSW"I''', '''## ?b]9i]7/>oSW"I,<EOF>''', 546))

	def test_547(self):
		self.assertTrue(TestLexer.test("qrnj#O5zT", "qrnj,Error Token #", 547))

	def test_548(self):
		self.assertTrue(TestLexer.test("Mbi", "Mbi,<EOF>", 548))

	def test_549(self):
		self.assertTrue(TestLexer.test("eU", "eU,<EOF>", 549))

	def test_550(self):
		self.assertTrue(TestLexer.test("9", "9,<EOF>", 550))

	def test_551(self):
		self.assertTrue(TestLexer.test("U9DPSEtA4", "U9DPSEtA4,<EOF>", 551))

	def test_552(self):
		self.assertTrue(TestLexer.test("EH7", "EH7,<EOF>", 552))

	def test_553(self):
		self.assertTrue(TestLexer.test('''## (cHQ}SrD+`&}SF7''', '''## (cHQ}SrD+`&}SF7,<EOF>''', 553))

	def test_554(self):
		self.assertTrue(TestLexer.test('''"%'""''', '''%'",<EOF>''', 554))

	def test_555(self):
		self.assertTrue(TestLexer.test('''## v"''', '''## v",<EOF>''', 555))

	def test_556(self):
		self.assertTrue(TestLexer.test("cc2e228f5V", "cc2e228f5V,<EOF>", 556))

	def test_557(self):
		self.assertTrue(TestLexer.test('''"Iu"''', '''Iu,<EOF>''', 557))

	def test_558(self):
		self.assertTrue(TestLexer.test('''## UCyg,9}''', '''## UCyg,9},<EOF>''', 558))

	def test_559(self):
		self.assertTrue(TestLexer.test("8sQRx$T", "8,sQRx,Error Token $", 559))

	def test_560(self):
		self.assertTrue(TestLexer.test("eK5aUGN0p", "eK5aUGN0p,<EOF>", 560))

	def test_561(self):
		self.assertTrue(TestLexer.test('''">\\p'"{'"*"''', '''Illegal Escape In String: >\\p''', 561))

	def test_562(self):
		self.assertTrue(TestLexer.test("2e79", "2e79,<EOF>", 562))

	def test_563(self):
		self.assertTrue(TestLexer.test('''"'"U ''', '''Unclosed String: '"U ''', 563))

	def test_564(self):
		self.assertTrue(TestLexer.test('''## &(9#]V^''', '''## &(9#]V^,<EOF>''', 564))

	def test_565(self):
		self.assertTrue(TestLexer.test('''## Fiqd90MY};Q=7@jlA/uR''', '''## Fiqd90MY};Q=7@jlA/uR,<EOF>''', 565))

	def test_566(self):
		self.assertTrue(TestLexer.test('''"'"'"'""''', '''\'"'"'",<EOF>''', 566))

	def test_567(self):
		self.assertTrue(TestLexer.test('''## etgoc.Tru)5i9{?''', '''## etgoc.Tru)5i9{?,<EOF>''', 567))

	def test_568(self):
		self.assertTrue(TestLexer.test('''## ~Lq<OEd}z"Zb7Mn+tL<''', '''## ~Lq<OEd}z"Zb7Mn+tL<,<EOF>''', 568))

	def test_569(self):
		self.assertTrue(TestLexer.test('''## Ya2<`~~%9*kP1$M)''', '''## Ya2<`~~%9*kP1$M),<EOF>''', 569))

	def test_570(self):
		self.assertTrue(TestLexer.test("s3dccp", "s3dccp,<EOF>", 570))

	def test_571(self):
		self.assertTrue(TestLexer.test('''## h|}Xq%qK7j&:jQv(Q''', '''## h|}Xq%qK7j&:jQv(Q,<EOF>''', 571))

	def test_572(self):
		self.assertTrue(TestLexer.test("7", "7,<EOF>", 572))

	def test_573(self):
		self.assertTrue(TestLexer.test("60.258e-54", "60.258e-54,<EOF>", 573))

	def test_574(self):
		self.assertTrue(TestLexer.test("aOgizpXN", "aOgizpXN,<EOF>", 574))

	def test_575(self):
		self.assertTrue(TestLexer.test('''## P&yY`''', '''## P&yY`,<EOF>''', 575))

	def test_576(self):
		self.assertTrue(TestLexer.test('''## lB''', '''## lB,<EOF>''', 576))

	def test_577(self):
		self.assertTrue(TestLexer.test("462.846E12", "462.846E12,<EOF>", 577))

	def test_578(self):
		self.assertTrue(TestLexer.test("_c6A6OR6a", "_c6A6OR6a,<EOF>", 578))

	def test_579(self):
		self.assertTrue(TestLexer.test("8.754E+42", "8.754E+42,<EOF>", 579))

	def test_580(self):
		self.assertTrue(TestLexer.test("831.304E06", "831.304E06,<EOF>", 580))

	def test_581(self):
		self.assertTrue(TestLexer.test("z0a", "z0a,<EOF>", 581))

	def test_582(self):
		self.assertTrue(TestLexer.test('''## W45''', '''## W45,<EOF>''', 582))

	def test_583(self):
		self.assertTrue(TestLexer.test('''## s+J>''', '''## s+J>,<EOF>''', 583))

	def test_584(self):
		self.assertTrue(TestLexer.test('''"-\\z'""''', '''Illegal Escape In String: -\\z''', 584))

	def test_585(self):
		self.assertTrue(TestLexer.test("B$IVFC$H", "B,Error Token $", 585))

	def test_586(self):
		self.assertTrue(TestLexer.test('''"L'"
'"'"|"''', '''Unclosed String: L'"''', 586))

	def test_587(self):
		self.assertTrue(TestLexer.test("237", "237,<EOF>", 587))

	def test_588(self):
		self.assertTrue(TestLexer.test("U^EQ", "U,Error Token ^", 588))

	def test_589(self):
		self.assertTrue(TestLexer.test("1BlnR6v", "1,BlnR6v,<EOF>", 589))

	def test_590(self):
		self.assertTrue(TestLexer.test("80", "80,<EOF>", 590))

	def test_591(self):
		self.assertTrue(TestLexer.test("883E-99", "883E-99,<EOF>", 591))

	def test_592(self):
		self.assertTrue(TestLexer.test('''"0uAK'" ''', '''Unclosed String: 0uAK'" ''', 592))

	def test_593(self):
		self.assertTrue(TestLexer.test("f", "f,<EOF>", 593))

	def test_594(self):
		self.assertTrue(TestLexer.test('''## 5>ASqVln`x)ID%cUV''', '''## 5>ASqVln`x)ID%cUV,<EOF>''', 594))

	def test_595(self):
		self.assertTrue(TestLexer.test('''"
G'"<'""''', '''Unclosed String: ''', 595))

	def test_596(self):
		self.assertTrue(TestLexer.test('''"v
'"2="''', '''Unclosed String: v''', 596))

	def test_597(self):
		self.assertTrue(TestLexer.test("7ENF", "7,ENF,<EOF>", 597))

	def test_598(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 598))

	def test_599(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 599))
