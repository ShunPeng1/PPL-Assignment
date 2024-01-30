import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_100(self):
		self.assertTrue(TestLexer.test("dW", "dW,<EOF>", 100))

	def test_101(self):
		self.assertTrue(TestLexer.test("661.041", "661.041,<EOF>", 101))

	def test_102(self):
		self.assertTrue(TestLexer.test("y", "y,<EOF>", 102))

	def test_103(self):
		self.assertTrue(TestLexer.test('''"\\s'"fS"''', '''Illegal Escape In String: \\s''', 103))

	def test_104(self):
		self.assertTrue(TestLexer.test("mG4Dcg", "mG4Dcg,<EOF>", 104))

	def test_105(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 105))

	def test_106(self):
		self.assertTrue(TestLexer.test('''## &sas favQIw0h[$G$-S''', '''<EOF>''', 106))

	def test_107(self):
		self.assertTrue(TestLexer.test("424E+70", "424E+70,<EOF>", 107))

	def test_108(self):
		self.assertTrue(TestLexer.test("0.614E-88", "0.614E-88,<EOF>", 108))

	def test_109(self):
		self.assertTrue(TestLexer.test('''## _=N6?vO?J,Y(y<1m-lI''', '''<EOF>''', 109))

	def test_110(self):
		self.assertTrue(TestLexer.test('''## QC''', '''<EOF>''', 110))

	def test_111(self):
		self.assertTrue(TestLexer.test('''## 32sC[GOOAY''', '''<EOF>''', 111))

	def test_112(self):
		self.assertTrue(TestLexer.test('''"'"mq
'"W"''', '''Unclosed String: '"mq
''', 112))

	def test_113(self):
		self.assertTrue(TestLexer.test("51.495E+29", "51.495E+29,<EOF>", 113))

	def test_114(self):
		self.assertTrue(TestLexer.test('''"'"'"'""''', '''\'"'"'",<EOF>''', 114))

	def test_115(self):
		self.assertTrue(TestLexer.test("aq", "aq,<EOF>", 115))

	def test_116(self):
		self.assertTrue(TestLexer.test("CrWhRe", "CrWhRe,<EOF>", 116))

	def test_117(self):
		self.assertTrue(TestLexer.test('''## qWT%uw''', '''<EOF>''', 117))

	def test_118(self):
		self.assertTrue(TestLexer.test("#JK_o", "Error Token #", 118))

	def test_119(self):
		self.assertTrue(TestLexer.test("7.219", "7.219,<EOF>", 119))

	def test_120(self):
		self.assertTrue(TestLexer.test('''## 4sgU.x<.6C''', '''<EOF>''', 120))

	def test_121(self):
		self.assertTrue(TestLexer.test("80E+16", "80E+16,<EOF>", 121))

	def test_122(self):
		self.assertTrue(TestLexer.test("5.822e+51", "5.822e+51,<EOF>", 122))

	def test_123(self):
		self.assertTrue(TestLexer.test('''## v''', '''<EOF>''', 123))

	def test_124(self):
		self.assertTrue(TestLexer.test('''## s>UP2g?n%%rT8wp^6b b''', '''<EOF>''', 124))

	def test_125(self):
		self.assertTrue(TestLexer.test("893.717", "893.717,<EOF>", 125))

	def test_126(self):
		self.assertTrue(TestLexer.test("XG", "XG,<EOF>", 126))

	def test_127(self):
		self.assertTrue(TestLexer.test("61E+69", "61E+69,<EOF>", 127))

	def test_128(self):
		self.assertTrue(TestLexer.test("5.914", "5.914,<EOF>", 128))

	def test_129(self):
		self.assertTrue(TestLexer.test('''"'"'"C| ''', '''Unclosed String: '"'"C| ''', 129))

	def test_130(self):
		self.assertTrue(TestLexer.test("31.527", "31.527,<EOF>", 130))

	def test_131(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 131))

	def test_132(self):
		self.assertTrue(TestLexer.test("eIk3", "eIk3,<EOF>", 132))

	def test_133(self):
		self.assertTrue(TestLexer.test("I8^mH5", "I8,Error Token ^", 133))

	def test_134(self):
		self.assertTrue(TestLexer.test("D6k3", "D6k3,<EOF>", 134))

	def test_135(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 135))

	def test_136(self):
		self.assertTrue(TestLexer.test("mA#4BuLM", "mA,Error Token #", 136))

	def test_137(self):
		self.assertTrue(TestLexer.test('''## Imr^D1d;Ej[Kjk2r-J''', '''<EOF>''', 137))

	def test_138(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 138))

	def test_139(self):
		self.assertTrue(TestLexer.test("PDUdw7NO", "PDUdw7NO,<EOF>", 139))

	def test_140(self):
		self.assertTrue(TestLexer.test('''## gGh9&d"8l{BSI''', '''<EOF>''', 140))

	def test_141(self):
		self.assertTrue(TestLexer.test("om", "om,<EOF>", 141))

	def test_142(self):
		self.assertTrue(TestLexer.test("@", "Error Token @", 142))

	def test_143(self):
		self.assertTrue(TestLexer.test("7E57", "7E57,<EOF>", 143))

	def test_144(self):
		self.assertTrue(TestLexer.test('''## !![-cc{QH8"v!`] :k''', '''<EOF>''', 144))

	def test_145(self):
		self.assertTrue(TestLexer.test("45e+51", "45e+51,<EOF>", 145))

	def test_146(self):
		self.assertTrue(TestLexer.test("625.090E+01", "625.090E+01,<EOF>", 146))

	def test_147(self):
		self.assertTrue(TestLexer.test("315e+98", "315e+98,<EOF>", 147))

	def test_148(self):
		self.assertTrue(TestLexer.test('''## Z @v7j''', '''<EOF>''', 148))

	def test_149(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 149))

	def test_150(self):
		self.assertTrue(TestLexer.test('''"'"\\y'"'"''', '''Illegal Escape In String: '"\\y''', 150))

	def test_151(self):
		self.assertTrue(TestLexer.test('''":&'"o"''', ''':&'"o,<EOF>''', 151))

	def test_152(self):
		self.assertTrue(TestLexer.test('''## Lc,9 o3|V''', '''<EOF>''', 152))

	def test_153(self):
		self.assertTrue(TestLexer.test('''"<s'"B ''', '''Unclosed String: <s'"B ''', 153))

	def test_154(self):
		self.assertTrue(TestLexer.test("3", "3,<EOF>", 154))

	def test_155(self):
		self.assertTrue(TestLexer.test("LaKUlO", "LaKUlO,<EOF>", 155))

	def test_156(self):
		self.assertTrue(TestLexer.test('''## :Z(JvloG${''', '''<EOF>''', 156))

	def test_157(self):
		self.assertTrue(TestLexer.test("78ytr@ekcp", "78,ytr,Error Token @", 157))

	def test_158(self):
		self.assertTrue(TestLexer.test("990.586e41", "990.586e41,<EOF>", 158))

	def test_159(self):
		self.assertTrue(TestLexer.test('''## [3XxNUFlTf33.V^Jed8''', '''<EOF>''', 159))

	def test_160(self):
		self.assertTrue(TestLexer.test('''## q@v~z97n=UN>x$63W|?o''', '''<EOF>''', 160))

	def test_161(self):
		self.assertTrue(TestLexer.test("8Y#", "8,Y,Error Token #", 161))

	def test_162(self):
		self.assertTrue(TestLexer.test('''"xX'"'"'""''', '''xX'"'"'",<EOF>''', 162))

	def test_163(self):
		self.assertTrue(TestLexer.test('''"\\h'"1u"''', '''Illegal Escape In String: \\h''', 163))

	def test_164(self):
		self.assertTrue(TestLexer.test('''"'"'"|F"''', '''\'"'"|F,<EOF>''', 164))

	def test_165(self):
		self.assertTrue(TestLexer.test("33.313E72", "33.313E72,<EOF>", 165))

	def test_166(self):
		self.assertTrue(TestLexer.test('''## KP_+zM%XmN|''', '''<EOF>''', 166))

	def test_167(self):
		self.assertTrue(TestLexer.test('''"'"
T'"!"''', '''Unclosed String: '"
''', 167))

	def test_168(self):
		self.assertTrue(TestLexer.test('''## dty_A^8L#vu`''', '''<EOF>''', 168))

	def test_169(self):
		self.assertTrue(TestLexer.test('''"\\p'"7f"''', '''Illegal Escape In String: \\p''', 169))

	def test_170(self):
		self.assertTrue(TestLexer.test("J5de", "J5de,<EOF>", 170))

	def test_171(self):
		self.assertTrue(TestLexer.test('''## )9-''', '''<EOF>''', 171))

	def test_172(self):
		self.assertTrue(TestLexer.test('''## [''', '''<EOF>''', 172))

	def test_173(self):
		self.assertTrue(TestLexer.test("57e-79", "57e-79,<EOF>", 173))

	def test_174(self):
		self.assertTrue(TestLexer.test("40e-55", "40e-55,<EOF>", 174))

	def test_175(self):
		self.assertTrue(TestLexer.test("438e-08", "438e-08,<EOF>", 175))

	def test_176(self):
		self.assertTrue(TestLexer.test('''## ^J''', '''<EOF>''', 176))

	def test_177(self):
		self.assertTrue(TestLexer.test('''"'"G ''', '''Unclosed String: '"G ''', 177))

	def test_178(self):
		self.assertTrue(TestLexer.test("j^P78Y", "j,Error Token ^", 178))

	def test_179(self):
		self.assertTrue(TestLexer.test('''"=\\v'"'""''', '''Illegal Escape In String: =\\v''', 179))

	def test_180(self):
		self.assertTrue(TestLexer.test("7.660", "7.660,<EOF>", 180))

	def test_181(self):
		self.assertTrue(TestLexer.test('''";'"'"/'" ''', '''Unclosed String: ;'"'"/'" ''', 181))

	def test_182(self):
		self.assertTrue(TestLexer.test('''"\\qn-'"'""''', '''Illegal Escape In String: \\q''', 182))

	def test_183(self):
		self.assertTrue(TestLexer.test('''## ~+#vw0''', '''<EOF>''', 183))

	def test_184(self):
		self.assertTrue(TestLexer.test("P^xwkXpsM", "P,Error Token ^", 184))

	def test_185(self):
		self.assertTrue(TestLexer.test('''"'"
W'"vr"''', '''Unclosed String: '"
''', 185))

	def test_186(self):
		self.assertTrue(TestLexer.test("Q^tCPI3yaT", "Q,Error Token ^", 186))

	def test_187(self):
		self.assertTrue(TestLexer.test('''## , sdQb{=n857G`''', '''<EOF>''', 187))

	def test_188(self):
		self.assertTrue(TestLexer.test("jh2F2l", "jh2F2l,<EOF>", 188))

	def test_189(self):
		self.assertTrue(TestLexer.test('''## .>p9S%nnFGtwSIR:E8(4''', '''<EOF>''', 189))

	def test_190(self):
		self.assertTrue(TestLexer.test('''## dOkwNTxf;=Tl8/wYNS''', '''<EOF>''', 190))

	def test_191(self):
		self.assertTrue(TestLexer.test('''"c"''', '''c,<EOF>''', 191))

	def test_192(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 192))

	def test_193(self):
		self.assertTrue(TestLexer.test('''## F''', '''<EOF>''', 193))

	def test_194(self):
		self.assertTrue(TestLexer.test('''## er=K*HjIk}uvy*''', '''<EOF>''', 194))

	def test_195(self):
		self.assertTrue(TestLexer.test("8nzvXDplc", "8,nzvXDplc,<EOF>", 195))

	def test_196(self):
		self.assertTrue(TestLexer.test("0yS", "0,yS,<EOF>", 196))

	def test_197(self):
		self.assertTrue(TestLexer.test("lmC$c1", "lmC,Error Token $", 197))

	def test_198(self):
		self.assertTrue(TestLexer.test('''"3'""''', '''3'",<EOF>''', 198))

	def test_199(self):
		self.assertTrue(TestLexer.test("$Um5DlW", "Error Token $", 199))

	def test_200(self):
		self.assertTrue(TestLexer.test("kZwy569", "kZwy569,<EOF>", 200))

	def test_201(self):
		self.assertTrue(TestLexer.test("3.468", "3.468,<EOF>", 201))

	def test_202(self):
		self.assertTrue(TestLexer.test("1.428e28", "1.428e28,<EOF>", 202))

	def test_203(self):
		self.assertTrue(TestLexer.test('''## !U+3.S`Y(jSVKv>"''', '''<EOF>''', 203))

	def test_204(self):
		self.assertTrue(TestLexer.test('''"\\x'"'""''', '''Illegal Escape In String: \\x''', 204))

	def test_205(self):
		self.assertTrue(TestLexer.test("80VjiJjuV", "80,VjiJjuV,<EOF>", 205))

	def test_206(self):
		self.assertTrue(TestLexer.test("56", "56,<EOF>", 206))

	def test_207(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 207))

	def test_208(self):
		self.assertTrue(TestLexer.test("U9", "U9,<EOF>", 208))

	def test_209(self):
		self.assertTrue(TestLexer.test("6.089", "6.089,<EOF>", 209))

	def test_210(self):
		self.assertTrue(TestLexer.test('''"\\q'"t '""''', '''Illegal Escape In String: \\q''', 210))

	def test_211(self):
		self.assertTrue(TestLexer.test('''## Tq9#q0f<''', '''<EOF>''', 211))

	def test_212(self):
		self.assertTrue(TestLexer.test("617.662", "617.662,<EOF>", 212))

	def test_213(self):
		self.assertTrue(TestLexer.test('''"'"@JD"''', '''\'"@JD,<EOF>''', 213))

	def test_214(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 214))

	def test_215(self):
		self.assertTrue(TestLexer.test("tsiG_Sx", "tsiG_Sx,<EOF>", 215))

	def test_216(self):
		self.assertTrue(TestLexer.test('''## hS''', '''<EOF>''', 216))

	def test_217(self):
		self.assertTrue(TestLexer.test('''"&O!'", ''', '''Unclosed String: &O!'", ''', 217))

	def test_218(self):
		self.assertTrue(TestLexer.test('''## n''', '''<EOF>''', 218))

	def test_219(self):
		self.assertTrue(TestLexer.test("A95Is", "A95Is,<EOF>", 219))

	def test_220(self):
		self.assertTrue(TestLexer.test("8.146E-59", "8.146E-59,<EOF>", 220))

	def test_221(self):
		self.assertTrue(TestLexer.test('''## jfiOHR6QE''', '''<EOF>''', 221))

	def test_222(self):
		self.assertTrue(TestLexer.test("18E-86", "18E-86,<EOF>", 222))

	def test_223(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 223))

	def test_224(self):
		self.assertTrue(TestLexer.test('''"X\\z'"'"'""''', '''Illegal Escape In String: X\\z''', 224))

	def test_225(self):
		self.assertTrue(TestLexer.test("DObzbvIY", "DObzbvIY,<EOF>", 225))

	def test_226(self):
		self.assertTrue(TestLexer.test("nI2", "nI2,<EOF>", 226))

	def test_227(self):
		self.assertTrue(TestLexer.test("ww", "ww,<EOF>", 227))

	def test_228(self):
		self.assertTrue(TestLexer.test("HUPQQW", "HUPQQW,<EOF>", 228))

	def test_229(self):
		self.assertTrue(TestLexer.test("558e59", "558e59,<EOF>", 229))

	def test_230(self):
		self.assertTrue(TestLexer.test("6E-22", "6E-22,<EOF>", 230))

	def test_231(self):
		self.assertTrue(TestLexer.test("6E00", "6E00,<EOF>", 231))

	def test_232(self):
		self.assertTrue(TestLexer.test("hYFVMd", "hYFVMd,<EOF>", 232))

	def test_233(self):
		self.assertTrue(TestLexer.test("179", "179,<EOF>", 233))

	def test_234(self):
		self.assertTrue(TestLexer.test('''"\\czBW,"''', '''Illegal Escape In String: \\c''', 234))

	def test_235(self):
		self.assertTrue(TestLexer.test('''## EPpBAEr0:9$=T`%hUU''', '''<EOF>''', 235))

	def test_236(self):
		self.assertTrue(TestLexer.test('''"ezV_\\u<"''', '''Illegal Escape In String: ezV_\\u''', 236))

	def test_237(self):
		self.assertTrue(TestLexer.test("26e+28", "26e+28,<EOF>", 237))

	def test_238(self):
		self.assertTrue(TestLexer.test('''## "@%0Loq}''', '''<EOF>''', 238))

	def test_239(self):
		self.assertTrue(TestLexer.test("ux&", "ux,Error Token &", 239))

	def test_240(self):
		self.assertTrue(TestLexer.test("1", "1,<EOF>", 240))

	def test_241(self):
		self.assertTrue(TestLexer.test('''## 3K_f0JS|-@fG%!{''', '''<EOF>''', 241))

	def test_242(self):
		self.assertTrue(TestLexer.test('''"8'" ''', '''Unclosed String: 8'" ''', 242))

	def test_243(self):
		self.assertTrue(TestLexer.test("blQ^OVz&_", "blQ,Error Token ^", 243))

	def test_244(self):
		self.assertTrue(TestLexer.test("1", "1,<EOF>", 244))

	def test_245(self):
		self.assertTrue(TestLexer.test("1.822E05", "1.822E05,<EOF>", 245))

	def test_246(self):
		self.assertTrue(TestLexer.test('''## jKH#sD5B:.''', '''<EOF>''', 246))

	def test_247(self):
		self.assertTrue(TestLexer.test("3.841", "3.841,<EOF>", 247))

	def test_248(self):
		self.assertTrue(TestLexer.test("Y$", "Y,Error Token $", 248))

	def test_249(self):
		self.assertTrue(TestLexer.test('''"d ''', '''Unclosed String: d ''', 249))

	def test_250(self):
		self.assertTrue(TestLexer.test('''"'"'"'"z"''', '''\'"'"'"z,<EOF>''', 250))

	def test_251(self):
		self.assertTrue(TestLexer.test("V", "V,<EOF>", 251))

	def test_252(self):
		self.assertTrue(TestLexer.test('''## }''', '''<EOF>''', 252))

	def test_253(self):
		self.assertTrue(TestLexer.test("7.193", "7.193,<EOF>", 253))

	def test_254(self):
		self.assertTrue(TestLexer.test('''"\\h '"sU"''', '''Illegal Escape In String: \\h''', 254))

	def test_255(self):
		self.assertTrue(TestLexer.test("5.329e+41", "5.329e+41,<EOF>", 255))

	def test_256(self):
		self.assertTrue(TestLexer.test('''"'"'"'" ''', '''Unclosed String: '"'"'" ''', 256))

	def test_257(self):
		self.assertTrue(TestLexer.test('''"'"a/\\i'"'""''', '''Illegal Escape In String: '"a/\\i''', 257))

	def test_258(self):
		self.assertTrue(TestLexer.test("@ZsK", "Error Token @", 258))

	def test_259(self):
		self.assertTrue(TestLexer.test('''"'"'"'"'"'" ''', '''Unclosed String: '"'"'"'"'" ''', 259))

	def test_260(self):
		self.assertTrue(TestLexer.test('''"pP(n
'""''', '''Unclosed String: pP(n
''', 260))

	def test_261(self):
		self.assertTrue(TestLexer.test("328", "328,<EOF>", 261))

	def test_262(self):
		self.assertTrue(TestLexer.test('''## 0VCd?J''', '''<EOF>''', 262))

	def test_263(self):
		self.assertTrue(TestLexer.test('''"'"'"
'"'"'""''', '''Unclosed String: '"'"
''', 263))

	def test_264(self):
		self.assertTrue(TestLexer.test("G4SG", "G4SG,<EOF>", 264))

	def test_265(self):
		self.assertTrue(TestLexer.test("39", "39,<EOF>", 265))

	def test_266(self):
		self.assertTrue(TestLexer.test("411e45", "411e45,<EOF>", 266))

	def test_267(self):
		self.assertTrue(TestLexer.test('''"K'"C@"''', '''K'"C@,<EOF>''', 267))

	def test_268(self):
		self.assertTrue(TestLexer.test("M&T$P8UcI1", "M,Error Token &", 268))

	def test_269(self):
		self.assertTrue(TestLexer.test('''## <>m?`1''', '''<EOF>''', 269))

	def test_270(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 270))

	def test_271(self):
		self.assertTrue(TestLexer.test("373", "373,<EOF>", 271))

	def test_272(self):
		self.assertTrue(TestLexer.test('''## ~R''', '''<EOF>''', 272))

	def test_273(self):
		self.assertTrue(TestLexer.test('''## u6&!~R`,x>{*oA-H8FKA''', '''<EOF>''', 273))

	def test_274(self):
		self.assertTrue(TestLexer.test('''## j:M{M(I4@+>RlO|uU''', '''<EOF>''', 274))

	def test_275(self):
		self.assertTrue(TestLexer.test('''## XG.KgfK=;>L! ];+''', '''<EOF>''', 275))

	def test_276(self):
		self.assertTrue(TestLexer.test("wp", "wp,<EOF>", 276))

	def test_277(self):
		self.assertTrue(TestLexer.test('''## AOz/HGTE=Wr~ Re''', '''<EOF>''', 277))

	def test_278(self):
		self.assertTrue(TestLexer.test("721", "721,<EOF>", 278))

	def test_279(self):
		self.assertTrue(TestLexer.test('''## {%;V/;)"B''', '''<EOF>''', 279))

	def test_280(self):
		self.assertTrue(TestLexer.test("piu_#W5F", "piu_,Error Token #", 280))

	def test_281(self):
		self.assertTrue(TestLexer.test("sH^z", "sH,Error Token ^", 281))

	def test_282(self):
		self.assertTrue(TestLexer.test("0wLVuWiw", "0,wLVuWiw,<EOF>", 282))

	def test_283(self):
		self.assertTrue(TestLexer.test('''"  ''', '''Unclosed String:   ''', 283))

	def test_284(self):
		self.assertTrue(TestLexer.test("7.635e04", "7.635e04,<EOF>", 284))

	def test_285(self):
		self.assertTrue(TestLexer.test("9.001E82", "9.001E82,<EOF>", 285))

	def test_286(self):
		self.assertTrue(TestLexer.test('''"'"d ''', '''Unclosed String: '"d ''', 286))

	def test_287(self):
		self.assertTrue(TestLexer.test("413", "413,<EOF>", 287))

	def test_288(self):
		self.assertTrue(TestLexer.test("96", "96,<EOF>", 288))

	def test_289(self):
		self.assertTrue(TestLexer.test("a", "a,<EOF>", 289))

	def test_290(self):
		self.assertTrue(TestLexer.test("201e+04", "201e+04,<EOF>", 290))

	def test_291(self):
		self.assertTrue(TestLexer.test("532e77", "532e77,<EOF>", 291))

	def test_292(self):
		self.assertTrue(TestLexer.test('''"'"z'""''', '''\'"z'",<EOF>''', 292))

	def test_293(self):
		self.assertTrue(TestLexer.test('''## L)[*=O>-oS>>%p[#3''', '''<EOF>''', 293))

	def test_294(self):
		self.assertTrue(TestLexer.test("lCyv", "lCyv,<EOF>", 294))

	def test_295(self):
		self.assertTrue(TestLexer.test("JbD7", "JbD7,<EOF>", 295))

	def test_296(self):
		self.assertTrue(TestLexer.test('''"\\p'"'"'")'""''', '''Illegal Escape In String: \\p''', 296))

	def test_297(self):
		self.assertTrue(TestLexer.test("35.251", "35.251,<EOF>", 297))

	def test_298(self):
		self.assertTrue(TestLexer.test('''## .T%p''', '''<EOF>''', 298))

	def test_299(self):
		self.assertTrue(TestLexer.test("4f@o", "4,f,Error Token @", 299))

	def test_300(self):
		self.assertTrue(TestLexer.test("QM2X", "QM2X,<EOF>", 300))

	def test_301(self):
		self.assertTrue(TestLexer.test("FsnJ^u@", "FsnJ,Error Token ^", 301))

	def test_302(self):
		self.assertTrue(TestLexer.test('''"@\\ol'""''', '''Illegal Escape In String: @\\o''', 302))

	def test_303(self):
		self.assertTrue(TestLexer.test('''## ZX''', '''<EOF>''', 303))

	def test_304(self):
		self.assertTrue(TestLexer.test("H^Q#XB^", "H,Error Token ^", 304))

	def test_305(self):
		self.assertTrue(TestLexer.test('''## H]LnERJO!d;y/""''', '''<EOF>''', 305))

	def test_306(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 306))

	def test_307(self):
		self.assertTrue(TestLexer.test("7", "7,<EOF>", 307))

	def test_308(self):
		self.assertTrue(TestLexer.test("803.641E-41", "803.641E-41,<EOF>", 308))

	def test_309(self):
		self.assertTrue(TestLexer.test('''".T\\g9'""''', '''Illegal Escape In String: .T\\g''', 309))

	def test_310(self):
		self.assertTrue(TestLexer.test('''## 7sUs@/otJ3!fTH''', '''<EOF>''', 310))

	def test_311(self):
		self.assertTrue(TestLexer.test("xYxe61vDA", "xYxe61vDA,<EOF>", 311))

	def test_312(self):
		self.assertTrue(TestLexer.test('''") B"''', ''') B,<EOF>''', 312))

	def test_313(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''Unclosed String: '" ''', 313))

	def test_314(self):
		self.assertTrue(TestLexer.test('''## R$O1v''', '''<EOF>''', 314))

	def test_315(self):
		self.assertTrue(TestLexer.test('''"\\zY'"'""''', '''Illegal Escape In String: \\z''', 315))

	def test_316(self):
		self.assertTrue(TestLexer.test('''## *nD/QqU&U''', '''<EOF>''', 316))

	def test_317(self):
		self.assertTrue(TestLexer.test('''"'"'"'"'"g ''', '''Unclosed String: '"'"'"'"g ''', 317))

	def test_318(self):
		self.assertTrue(TestLexer.test("Vby", "Vby,<EOF>", 318))

	def test_319(self):
		self.assertTrue(TestLexer.test("3.402e70", "3.402e70,<EOF>", 319))

	def test_320(self):
		self.assertTrue(TestLexer.test('''## #mC-''', '''<EOF>''', 320))

	def test_321(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 321))

	def test_322(self):
		self.assertTrue(TestLexer.test('''"'"{'""''', '''\'"{'",<EOF>''', 322))

	def test_323(self):
		self.assertTrue(TestLexer.test("95.690E22", "95.690E22,<EOF>", 323))

	def test_324(self):
		self.assertTrue(TestLexer.test('''## A0C=H_5@0E&''', '''<EOF>''', 324))

	def test_325(self):
		self.assertTrue(TestLexer.test('''## ORG''', '''<EOF>''', 325))

	def test_326(self):
		self.assertTrue(TestLexer.test("4E54", "4E54,<EOF>", 326))

	def test_327(self):
		self.assertTrue(TestLexer.test("f0pVBs", "f0pVBs,<EOF>", 327))

	def test_328(self):
		self.assertTrue(TestLexer.test('''"*\\y "''', '''Illegal Escape In String: *\\y''', 328))

	def test_329(self):
		self.assertTrue(TestLexer.test('''"M"''', '''M,<EOF>''', 329))

	def test_330(self):
		self.assertTrue(TestLexer.test('''## w;5''', '''<EOF>''', 330))

	def test_331(self):
		self.assertTrue(TestLexer.test('''"@x'"'" ''', '''Unclosed String: @x'"'" ''', 331))

	def test_332(self):
		self.assertTrue(TestLexer.test("q", "q,<EOF>", 332))

	def test_333(self):
		self.assertTrue(TestLexer.test('''"'"	"''', '''\'"	,<EOF>''', 333))

	def test_334(self):
		self.assertTrue(TestLexer.test("38p5", "38,p5,<EOF>", 334))

	def test_335(self):
		self.assertTrue(TestLexer.test("Tk3", "Tk3,<EOF>", 335))

	def test_336(self):
		self.assertTrue(TestLexer.test("4uvfTDyBIt", "4,uvfTDyBIt,<EOF>", 336))

	def test_337(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 337))

	def test_338(self):
		self.assertTrue(TestLexer.test('''"'";'" ''', '''Unclosed String: '";'" ''', 338))

	def test_339(self):
		self.assertTrue(TestLexer.test("TvAx", "TvAx,<EOF>", 339))

	def test_340(self):
		self.assertTrue(TestLexer.test('''## wr?jl~N''', '''<EOF>''', 340))

	def test_341(self):
		self.assertTrue(TestLexer.test('''"DQk'""''', '''DQk'",<EOF>''', 341))

	def test_342(self):
		self.assertTrue(TestLexer.test("345", "345,<EOF>", 342))

	def test_343(self):
		self.assertTrue(TestLexer.test("6.038", "6.038,<EOF>", 343))

	def test_344(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 344))

	def test_345(self):
		self.assertTrue(TestLexer.test("194", "194,<EOF>", 345))

	def test_346(self):
		self.assertTrue(TestLexer.test("Vw8&OloVL0", "Vw8,Error Token &", 346))

	def test_347(self):
		self.assertTrue(TestLexer.test("99.702", "99.702,<EOF>", 347))

	def test_348(self):
		self.assertTrue(TestLexer.test('''"'"\\q>"''', '''Illegal Escape In String: '"\\q''', 348))

	def test_349(self):
		self.assertTrue(TestLexer.test('''"\\uA'""''', '''Illegal Escape In String: \\u''', 349))

	def test_350(self):
		self.assertTrue(TestLexer.test("#uTgPjhsW", "Error Token #", 350))

	def test_351(self):
		self.assertTrue(TestLexer.test('''"
2"''', '''Unclosed String: 
''', 351))

	def test_352(self):
		self.assertTrue(TestLexer.test("528.672E-92", "528.672E-92,<EOF>", 352))

	def test_353(self):
		self.assertTrue(TestLexer.test("5.300", "5.300,<EOF>", 353))

	def test_354(self):
		self.assertTrue(TestLexer.test('''"\\z0V"''', '''Illegal Escape In String: \\z''', 354))

	def test_355(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 355))

	def test_356(self):
		self.assertTrue(TestLexer.test("14e87", "14e87,<EOF>", 356))

	def test_357(self):
		self.assertTrue(TestLexer.test('''"mV'""''', '''mV'",<EOF>''', 357))

	def test_358(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 358))

	def test_359(self):
		self.assertTrue(TestLexer.test("411e35", "411e35,<EOF>", 359))

	def test_360(self):
		self.assertTrue(TestLexer.test('''"BL\\u
'""''', '''Illegal Escape In String: BL\\u''', 360))

	def test_361(self):
		self.assertTrue(TestLexer.test("h", "h,<EOF>", 361))

	def test_362(self):
		self.assertTrue(TestLexer.test("6", "6,<EOF>", 362))

	def test_363(self):
		self.assertTrue(TestLexer.test('''"'"% ''', '''Unclosed String: '"% ''', 363))

	def test_364(self):
		self.assertTrue(TestLexer.test("PBfIs", "PBfIs,<EOF>", 364))

	def test_365(self):
		self.assertTrue(TestLexer.test('''## =?tujoV4Ti@y''', '''<EOF>''', 365))

	def test_366(self):
		self.assertTrue(TestLexer.test("18", "18,<EOF>", 366))

	def test_367(self):
		self.assertTrue(TestLexer.test("2d2CBm", "2,d2CBm,<EOF>", 367))

	def test_368(self):
		self.assertTrue(TestLexer.test('''"'"ZH' ''', '''Unclosed String: '"ZH' ''', 368))

	def test_369(self):
		self.assertTrue(TestLexer.test('''## |hJ_=EX6''', '''<EOF>''', 369))

	def test_370(self):
		self.assertTrue(TestLexer.test("_o", "_o,<EOF>", 370))

	def test_371(self):
		self.assertTrue(TestLexer.test('''## m1)}X.ZM<S&+"''', '''<EOF>''', 371))

	def test_372(self):
		self.assertTrue(TestLexer.test('''## *Bl@an7*6''', '''<EOF>''', 372))

	def test_373(self):
		self.assertTrue(TestLexer.test('''## I~FTjrP^''', '''<EOF>''', 373))

	def test_374(self):
		self.assertTrue(TestLexer.test('''"M'"\\p0"''', '''Illegal Escape In String: M'"\\p''', 374))

	def test_375(self):
		self.assertTrue(TestLexer.test("24.749e24", "24.749e24,<EOF>", 375))

	def test_376(self):
		self.assertTrue(TestLexer.test('''"f'"''""''', '''f'"''",<EOF>''', 376))

	def test_377(self):
		self.assertTrue(TestLexer.test("J8n", "J8n,<EOF>", 377))

	def test_378(self):
		self.assertTrue(TestLexer.test("OjT", "OjT,<EOF>", 378))

	def test_379(self):
		self.assertTrue(TestLexer.test('''## +ZsXEJ8hmiy!Z&v''', '''<EOF>''', 379))

	def test_380(self):
		self.assertTrue(TestLexer.test('''"L\\y*"''', '''Illegal Escape In String: L\\y''', 380))

	def test_381(self):
		self.assertTrue(TestLexer.test("n^P", "n,Error Token ^", 381))

	def test_382(self):
		self.assertTrue(TestLexer.test("8JvrliS", "8,JvrliS,<EOF>", 382))

	def test_383(self):
		self.assertTrue(TestLexer.test("q", "q,<EOF>", 383))

	def test_384(self):
		self.assertTrue(TestLexer.test('''## /J8F7)~rY_x''', '''<EOF>''', 384))

	def test_385(self):
		self.assertTrue(TestLexer.test("$#pJ@IEZXi", "Error Token $", 385))

	def test_386(self):
		self.assertTrue(TestLexer.test("5.561", "5.561,<EOF>", 386))

	def test_387(self):
		self.assertTrue(TestLexer.test('''"'"{'"'" ''', '''Unclosed String: '"{'"'" ''', 387))

	def test_388(self):
		self.assertTrue(TestLexer.test('''## PDv}2".Y%@mU>bh_,jY''', '''<EOF>''', 388))

	def test_389(self):
		self.assertTrue(TestLexer.test("0x9SyuW", "0,x9SyuW,<EOF>", 389))

	def test_390(self):
		self.assertTrue(TestLexer.test('''"'"'"
?'""''', '''Unclosed String: '"'"
''', 390))

	def test_391(self):
		self.assertTrue(TestLexer.test("7FDa", "7,FDa,<EOF>", 391))

	def test_392(self):
		self.assertTrue(TestLexer.test('''"'"'"'"&"''', '''\'"'"'"&,<EOF>''', 392))

	def test_393(self):
		self.assertTrue(TestLexer.test('''## j^Q|<9Jyn''', '''<EOF>''', 393))

	def test_394(self):
		self.assertTrue(TestLexer.test('''"\\d'"'""''', '''Illegal Escape In String: \\d''', 394))

	def test_395(self):
		self.assertTrue(TestLexer.test('''"K"''', '''K,<EOF>''', 395))

	def test_396(self):
		self.assertTrue(TestLexer.test("ya9UJg", "ya9UJg,<EOF>", 396))

	def test_397(self):
		self.assertTrue(TestLexer.test("L@D", "L,Error Token @", 397))

	def test_398(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 398))

	def test_399(self):
		self.assertTrue(TestLexer.test('''"'"'"F"''', '''\'"'"F,<EOF>''', 399))

	def test_400(self):
		self.assertTrue(TestLexer.test("LM5Coms9", "LM5Coms9,<EOF>", 400))

	def test_401(self):
		self.assertTrue(TestLexer.test("BwRvM&", "BwRvM,Error Token &", 401))

	def test_402(self):
		self.assertTrue(TestLexer.test('''"'"\\x'"'"M"''', '''Illegal Escape In String: '"\\x''', 402))

	def test_403(self):
		self.assertTrue(TestLexer.test("A&f", "A,Error Token &", 403))

	def test_404(self):
		self.assertTrue(TestLexer.test("208.800E49", "208.800E49,<EOF>", 404))

	def test_405(self):
		self.assertTrue(TestLexer.test('''## tlZ5op4~N9LNq''', '''<EOF>''', 405))

	def test_406(self):
		self.assertTrue(TestLexer.test('''"
''""''', '''Unclosed String: 
''', 406))

	def test_407(self):
		self.assertTrue(TestLexer.test("974.100e17", "974.100e17,<EOF>", 407))

	def test_408(self):
		self.assertTrue(TestLexer.test("54", "54,<EOF>", 408))

	def test_409(self):
		self.assertTrue(TestLexer.test('''## ~@KYcpB4O;W=&QV%K6G''', '''<EOF>''', 409))

	def test_410(self):
		self.assertTrue(TestLexer.test("w#finEl", "w,Error Token #", 410))

	def test_411(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 411))

	def test_412(self):
		self.assertTrue(TestLexer.test("7.596e+82", "7.596e+82,<EOF>", 412))

	def test_413(self):
		self.assertTrue(TestLexer.test('''"{s'"'""''', '''{s'"'",<EOF>''', 413))

	def test_414(self):
		self.assertTrue(TestLexer.test('''## 0nWcDE;HBSUY7@6''', '''<EOF>''', 414))

	def test_415(self):
		self.assertTrue(TestLexer.test('''## K1<qbL9Hn|%''', '''<EOF>''', 415))

	def test_416(self):
		self.assertTrue(TestLexer.test('''## m&LDUl4{4]!d,/f<o{a''', '''<EOF>''', 416))

	def test_417(self):
		self.assertTrue(TestLexer.test('''"Kh'"'""''', '''Kh'"'",<EOF>''', 417))

	def test_418(self):
		self.assertTrue(TestLexer.test('''"Z ''', '''Unclosed String: Z ''', 418))

	def test_419(self):
		self.assertTrue(TestLexer.test('''## H {m''', '''<EOF>''', 419))

	def test_420(self):
		self.assertTrue(TestLexer.test("bm1tz5h", "bm1tz5h,<EOF>", 420))

	def test_421(self):
		self.assertTrue(TestLexer.test('''"G'"'"'"'" ''', '''Unclosed String: G'"'"'"'" ''', 421))

	def test_422(self):
		self.assertTrue(TestLexer.test("Km", "Km,<EOF>", 422))

	def test_423(self):
		self.assertTrue(TestLexer.test('''")\\u'"'"'""''', '''Illegal Escape In String: )\\u''', 423))

	def test_424(self):
		self.assertTrue(TestLexer.test("3.746E54", "3.746E54,<EOF>", 424))

	def test_425(self):
		self.assertTrue(TestLexer.test("DG6U#Qqg", "DG6U,Error Token #", 425))

	def test_426(self):
		self.assertTrue(TestLexer.test('''"'"z'"'""''', '''\'"z'"'",<EOF>''', 426))

	def test_427(self):
		self.assertTrue(TestLexer.test("1E75", "1E75,<EOF>", 427))

	def test_428(self):
		self.assertTrue(TestLexer.test('''"'"'"'"'"'""''', '''\'"'"'"'"'",<EOF>''', 428))

	def test_429(self):
		self.assertTrue(TestLexer.test("4.513E01", "4.513E01,<EOF>", 429))

	def test_430(self):
		self.assertTrue(TestLexer.test('''## `mF>6N%1u''', '''<EOF>''', 430))

	def test_431(self):
		self.assertTrue(TestLexer.test('''## gs''', '''<EOF>''', 431))

	def test_432(self):
		self.assertTrue(TestLexer.test("GK5id3YR", "GK5id3YR,<EOF>", 432))

	def test_433(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 433))

	def test_434(self):
		self.assertTrue(TestLexer.test("RU0eEf", "RU0eEf,<EOF>", 434))

	def test_435(self):
		self.assertTrue(TestLexer.test('''"'"'" ''', '''Unclosed String: '"'" ''', 435))

	def test_436(self):
		self.assertTrue(TestLexer.test('''"\\c'""''', '''Illegal Escape In String: \\c''', 436))

	def test_437(self):
		self.assertTrue(TestLexer.test('''## U[''', '''<EOF>''', 437))

	def test_438(self):
		self.assertTrue(TestLexer.test("758E+48", "758E+48,<EOF>", 438))

	def test_439(self):
		self.assertTrue(TestLexer.test("kzlU", "kzlU,<EOF>", 439))

	def test_440(self):
		self.assertTrue(TestLexer.test("s", "s,<EOF>", 440))

	def test_441(self):
		self.assertTrue(TestLexer.test('''"\\dM"''', '''Illegal Escape In String: \\d''', 441))

	def test_442(self):
		self.assertTrue(TestLexer.test("H5GNtSqY", "H5GNtSqY,<EOF>", 442))

	def test_443(self):
		self.assertTrue(TestLexer.test("YoICm22bpb", "YoICm22bpb,<EOF>", 443))

	def test_444(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 444))

	def test_445(self):
		self.assertTrue(TestLexer.test('''## ^vp''', '''<EOF>''', 445))

	def test_446(self):
		self.assertTrue(TestLexer.test("h", "h,<EOF>", 446))

	def test_447(self):
		self.assertTrue(TestLexer.test("7.873e+73", "7.873e+73,<EOF>", 447))

	def test_448(self):
		self.assertTrue(TestLexer.test('''")	 ''', '''Unclosed String: )	 ''', 448))

	def test_449(self):
		self.assertTrue(TestLexer.test("730", "730,<EOF>", 449))

	def test_450(self):
		self.assertTrue(TestLexer.test("Kgg", "Kgg,<EOF>", 450))

	def test_451(self):
		self.assertTrue(TestLexer.test("83.191", "83.191,<EOF>", 451))

	def test_452(self):
		self.assertTrue(TestLexer.test('''## L)qDsd8[!B=7w>ns(%Um''', '''<EOF>''', 452))

	def test_453(self):
		self.assertTrue(TestLexer.test('''"
@"''', '''Unclosed String: 
''', 453))

	def test_454(self):
		self.assertTrue(TestLexer.test("ouxcZ54B8", "ouxcZ54B8,<EOF>", 454))

	def test_455(self):
		self.assertTrue(TestLexer.test("1E+04", "1E+04,<EOF>", 455))

	def test_456(self):
		self.assertTrue(TestLexer.test("426.293E+57", "426.293E+57,<EOF>", 456))

	def test_457(self):
		self.assertTrue(TestLexer.test('''"_'"\\ee'"'""''', '''Illegal Escape In String: _'"\\e''', 457))

	def test_458(self):
		self.assertTrue(TestLexer.test("4E-81", "4E-81,<EOF>", 458))

	def test_459(self):
		self.assertTrue(TestLexer.test('''## S%&"0=eSo4d''', '''<EOF>''', 459))

	def test_460(self):
		self.assertTrue(TestLexer.test("dIQ8f", "dIQ8f,<EOF>", 460))

	def test_461(self):
		self.assertTrue(TestLexer.test('''## b;Z''', '''<EOF>''', 461))
												
	def test_462(self):
		self.assertTrue(TestLexer.test("2e+87", "2e+87,<EOF>", 462))

	def test_463(self):
		self.assertTrue(TestLexer.test('''"
'"G'"O"''', '''Unclosed String: 
''', 463))

	def test_464(self):
		self.assertTrue(TestLexer.test("m", "m,<EOF>", 464))

	def test_465(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 465))

	def test_466(self):
		self.assertTrue(TestLexer.test("6", "6,<EOF>", 466))

	def test_467(self):
		self.assertTrue(TestLexer.test('''## k6}GLP!{oj''', '''<EOF>''', 467))

	def test_468(self):
		self.assertTrue(TestLexer.test('''## ~"_&_#cTpThJvw%`0L"''', '''<EOF>''', 468))

	def test_469(self):
		self.assertTrue(TestLexer.test('''"\\x'"a"''', '''Illegal Escape In String: \\x''', 469))

	def test_470(self):
		self.assertTrue(TestLexer.test('''## 4(B)[''', '''<EOF>''', 470))

	def test_471(self):
		self.assertTrue(TestLexer.test('''## sPK}&qy''', '''<EOF>''', 471))

	def test_472(self):
		self.assertTrue(TestLexer.test("87.896", "87.896,<EOF>", 472))

	def test_473(self):
		self.assertTrue(TestLexer.test('''"'"P\\g'"'""''', '''Illegal Escape In String: '"P\\g''', 473))

	def test_474(self):
		self.assertTrue(TestLexer.test('''## RxHZeitcg%-mwl''', '''<EOF>''', 474))

	def test_475(self):
		self.assertTrue(TestLexer.test('''## bv,AY~81jV4sMRh/p7''', '''<EOF>''', 475))

	def test_476(self):
		self.assertTrue(TestLexer.test("_B", "_B,<EOF>", 476))

	def test_477(self):
		self.assertTrue(TestLexer.test("2.966", "2.966,<EOF>", 477))

	def test_478(self):
		self.assertTrue(TestLexer.test('''"[h( ''', '''Unclosed String: [h( ''', 478))

	def test_479(self):
		self.assertTrue(TestLexer.test("Axn_IVSBX", "Axn_IVSBX,<EOF>", 479))

	def test_480(self):
		self.assertTrue(TestLexer.test("12", "12,<EOF>", 480))

	def test_481(self):
		self.assertTrue(TestLexer.test("59.774e+84", "59.774e+84,<EOF>", 481))

	def test_482(self):
		self.assertTrue(TestLexer.test('''## eISP_{jI_KI[`-CQ6 :9''', '''<EOF>''', 482))

	def test_483(self):
		self.assertTrue(TestLexer.test("bR", "bR,<EOF>", 483))

	def test_484(self):
		self.assertTrue(TestLexer.test('''"W'"'""''', '''W'"'",<EOF>''', 484))

	def test_485(self):
		self.assertTrue(TestLexer.test('''"'"'"\\d'"I-"''', '''Illegal Escape In String: '"'"\\d''', 485))

	def test_486(self):
		self.assertTrue(TestLexer.test('''## +''', '''<EOF>''', 486))

	def test_487(self):
		self.assertTrue(TestLexer.test('''"\\c6"''', '''Illegal Escape In String: \\c''', 487))

	def test_488(self):
		self.assertTrue(TestLexer.test('''"'"R'"'""''', '''\'"R'"'",<EOF>''', 488))

	def test_489(self):
		self.assertTrue(TestLexer.test('''## ,$2`IR''', '''<EOF>''', 489))

	def test_490(self):
		self.assertTrue(TestLexer.test("4ZW&5hNh4m", "4,ZW,Error Token &", 490))

	def test_491(self):
		self.assertTrue(TestLexer.test('''"S'"'"|"''', '''S'"'"|,<EOF>''', 491))

	def test_492(self):
		self.assertTrue(TestLexer.test("4.680", "4.680,<EOF>", 492))

	def test_493(self):
		self.assertTrue(TestLexer.test('''## `a0/ds>7*Q{GIi''', '''<EOF>''', 493))

	def test_494(self):
		self.assertTrue(TestLexer.test("uf5n", "uf5n,<EOF>", 494))

	def test_495(self):
		self.assertTrue(TestLexer.test('''## :1a]Idn''', '''<EOF>''', 495))

	def test_496(self):
		self.assertTrue(TestLexer.test("95", "95,<EOF>", 496))

	def test_497(self):
		self.assertTrue(TestLexer.test("46E+37", "46E+37,<EOF>", 497))

	def test_498(self):
		self.assertTrue(TestLexer.test("51.081", "51.081,<EOF>", 498))

	def test_499(self):
		self.assertTrue(TestLexer.test("Y8Nys", "Y8Nys,<EOF>", 499))

	def test_500(self):
		self.assertTrue(TestLexer.test('''"'"'" ''', '''Unclosed String: '"'" ''', 500))

	def test_501(self):
		self.assertTrue(TestLexer.test("VCVa", "VCVa,<EOF>", 501))

	def test_502(self):
		self.assertTrue(TestLexer.test("zNq3tp#E", "zNq3tp,Error Token #", 502))

	def test_503(self):
		self.assertTrue(TestLexer.test('''## rWegx|.&-p~Z5''', '''<EOF>''', 503))

	def test_504(self):
		self.assertTrue(TestLexer.test("991", "991,<EOF>", 504))

	def test_505(self):
		self.assertTrue(TestLexer.test('''## wDU5zKr|-rK&Ywm{''', '''<EOF>''', 505))

	def test_506(self):
		self.assertTrue(TestLexer.test("2g@r2sw", "2,g,Error Token @", 506))

	def test_507(self):
		self.assertTrue(TestLexer.test("E", "E,<EOF>", 507))

	def test_508(self):
		self.assertTrue(TestLexer.test("7.099E99", "7.099E99,<EOF>", 508))

	def test_509(self):
		self.assertTrue(TestLexer.test('''## ji}H|F#(p''', '''<EOF>''', 509))

	def test_510(self):
		self.assertTrue(TestLexer.test("1.259", "1.259,<EOF>", 510))

	def test_511(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 511))

	def test_512(self):
		self.assertTrue(TestLexer.test('''"\\v>u'"+"''', '''Illegal Escape In String: \\v''', 512))

	def test_513(self):
		self.assertTrue(TestLexer.test("960E+58", "960E+58,<EOF>", 513))

	def test_514(self):
		self.assertTrue(TestLexer.test('''"S'"\\s'"'""''', '''Illegal Escape In String: S'"\\s''', 514))

	def test_515(self):
		self.assertTrue(TestLexer.test("88", "88,<EOF>", 515))

	def test_516(self):
		self.assertTrue(TestLexer.test('''"q\\y'"Z<"''', '''Illegal Escape In String: q\\y''', 516))

	def test_517(self):
		self.assertTrue(TestLexer.test("_z3", "_z3,<EOF>", 517))

	def test_518(self):
		self.assertTrue(TestLexer.test("rqC", "rqC,<EOF>", 518))

	def test_519(self):
		self.assertTrue(TestLexer.test("7", "7,<EOF>", 519))

	def test_520(self):
		self.assertTrue(TestLexer.test("7.920E-47", "7.920E-47,<EOF>", 520))

	def test_521(self):
		self.assertTrue(TestLexer.test('''"\\zM:"''', '''Illegal Escape In String: \\z''', 521))

	def test_522(self):
		self.assertTrue(TestLexer.test('''## HB|YM ?1T''', '''<EOF>''', 522))

	def test_523(self):
		self.assertTrue(TestLexer.test("394E-21", "394E-21,<EOF>", 523))

	def test_524(self):
		self.assertTrue(TestLexer.test("2.224e+48", "2.224e+48,<EOF>", 524))

	def test_525(self):
		self.assertTrue(TestLexer.test('''## >''', '''<EOF>''', 525))

	def test_526(self):
		self.assertTrue(TestLexer.test("I", "I,<EOF>", 526))

	def test_527(self):
		self.assertTrue(TestLexer.test('''## IH1Mpcr-8*]R,MJu''', '''<EOF>''', 527))

	def test_528(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''Unclosed String: '" ''', 528))

	def test_529(self):
		self.assertTrue(TestLexer.test("72", "72,<EOF>", 529))

	def test_530(self):
		self.assertTrue(TestLexer.test('''"mU'""''', '''mU'",<EOF>''', 530))

	def test_531(self):
		self.assertTrue(TestLexer.test('''## #NK0gRT^_6NMz<c2?)''', '''<EOF>''', 531))

	def test_532(self):
		self.assertTrue(TestLexer.test('''"%\\jI'"nt"''', '''Illegal Escape In String: %\\j''', 532))

	def test_533(self):
		self.assertTrue(TestLexer.test('''"\\l'"'"'""''', '''Illegal Escape In String: \\l''', 533))

	def test_534(self):
		self.assertTrue(TestLexer.test('''## `?/d[:''', '''<EOF>''', 534))

	def test_535(self):
		self.assertTrue(TestLexer.test('''"'"'"'"E"''', '''\'"'"'"E,<EOF>''', 535))

	def test_536(self):
		self.assertTrue(TestLexer.test("2e18", "2e18,<EOF>", 536))

	def test_537(self):
		self.assertTrue(TestLexer.test('''## 9aAVC7?0[T#@3HBnV}i''', '''<EOF>''', 537))

	def test_538(self):
		self.assertTrue(TestLexer.test('''## %x9&N|FVq}]ov''', '''<EOF>''', 538))

	def test_539(self):
		self.assertTrue(TestLexer.test('''## "N$:-w{zh4xKu2&[[I''', '''<EOF>''', 539))

	def test_540(self):
		self.assertTrue(TestLexer.test("6u_UKFSDf", "6,u_UKFSDf,<EOF>", 540))

	def test_541(self):
		self.assertTrue(TestLexer.test("iGf", "iGf,<EOF>", 541))

	def test_542(self):
		self.assertTrue(TestLexer.test("cZni$rnLMM", "cZni,Error Token $", 542))

	def test_543(self):
		self.assertTrue(TestLexer.test('''## #n@a0f-xy>D,DD''', '''<EOF>''', 543))

	def test_544(self):
		self.assertTrue(TestLexer.test("410", "410,<EOF>", 544))

	def test_545(self):
		self.assertTrue(TestLexer.test('''## O<7gL[D-v7eQ''', '''<EOF>''', 545))

	def test_546(self):
		self.assertTrue(TestLexer.test("b@", "b,Error Token @", 546))

	def test_547(self):
		self.assertTrue(TestLexer.test("9M_ev", "9,M_ev,<EOF>", 547))

	def test_548(self):
		self.assertTrue(TestLexer.test('''"X'":"''', '''X'":,<EOF>''', 548))

	def test_549(self):
		self.assertTrue(TestLexer.test("BQfyofiw", "BQfyofiw,<EOF>", 549))

	def test_550(self):
		self.assertTrue(TestLexer.test('''## qd{&Soi[<zuGbb''', '''<EOF>''', 550))

	def test_551(self):
		self.assertTrue(TestLexer.test("93.438", "93.438,<EOF>", 551))

	def test_552(self):
		self.assertTrue(TestLexer.test('''"'"_4\\iTY"''', '''Illegal Escape In String: '"_4\\i''', 552))

	def test_553(self):
		self.assertTrue(TestLexer.test("901.149e02", "901.149e02,<EOF>", 553))

	def test_554(self):
		self.assertTrue(TestLexer.test('''## #Qp&NOi F''', '''<EOF>''', 554))

	def test_555(self):
		self.assertTrue(TestLexer.test("U", "U,<EOF>", 555))

	def test_556(self):
		self.assertTrue(TestLexer.test("78.350e+84", "78.350e+84,<EOF>", 556))

	def test_557(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 557))

	def test_558(self):
		self.assertTrue(TestLexer.test("Pbu", "Pbu,<EOF>", 558))

	def test_559(self):
		self.assertTrue(TestLexer.test("94.779", "94.779,<EOF>", 559))

	def test_560(self):
		self.assertTrue(TestLexer.test("l9COtDy797", "l9COtDy797,<EOF>", 560))

	def test_561(self):
		self.assertTrue(TestLexer.test('''"'"
'"'"\\q'""''', '''Unclosed String: '"
''', 561))

	def test_562(self):
		self.assertTrue(TestLexer.test("435.564", "435.564,<EOF>", 562))

	def test_563(self):
		self.assertTrue(TestLexer.test('''## BO''', '''<EOF>''', 563))

	def test_564(self):
		self.assertTrue(TestLexer.test('''## _3U''', '''<EOF>''', 564))

	def test_565(self):
		self.assertTrue(TestLexer.test("375.689", "375.689,<EOF>", 565))

	def test_566(self):
		self.assertTrue(TestLexer.test("U05m", "U05m,<EOF>", 566))

	def test_567(self):
		self.assertTrue(TestLexer.test('''"'"'"'"Q"''', '''\'"'"'"Q,<EOF>''', 567))

	def test_568(self):
		self.assertTrue(TestLexer.test('''## G7;z:hI"''', '''<EOF>''', 568))

	def test_569(self):
		self.assertTrue(TestLexer.test("kozz6E", "kozz6E,<EOF>", 569))

	def test_570(self):
		self.assertTrue(TestLexer.test('''"'"\\x'""''', '''Illegal Escape In String: '"\\x''', 570))

	def test_571(self):
		self.assertTrue(TestLexer.test("43E-71", "43E-71,<EOF>", 571))

	def test_572(self):
		self.assertTrue(TestLexer.test('''## )(x-Vb-x(''', '''<EOF>''', 572))

	def test_573(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 573))

	def test_574(self):
		self.assertTrue(TestLexer.test('''## [i^wdgjK[W''', '''<EOF>''', 574))

	def test_575(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 575))

	def test_576(self):
		self.assertTrue(TestLexer.test('''"]'"\\dG"''', '''Illegal Escape In String: ]'"\\d''', 576))

	def test_577(self):
		self.assertTrue(TestLexer.test('''## <jsPbNf|^@`ZTbGQKnO(''', '''<EOF>''', 577))

	def test_578(self):
		self.assertTrue(TestLexer.test('''## kr*`{''', '''<EOF>''', 578))

	def test_579(self):
		self.assertTrue(TestLexer.test("3", "3,<EOF>", 579))

	def test_580(self):
		self.assertTrue(TestLexer.test("1sXgem^@Pa", "1,sXgem,Error Token ^", 580))

	def test_581(self):
		self.assertTrue(TestLexer.test("vrFVFWM", "vrFVFWM,<EOF>", 581))

	def test_582(self):
		self.assertTrue(TestLexer.test('''"'"CrH"''', '''\'"CrH,<EOF>''', 582))

	def test_583(self):
		self.assertTrue(TestLexer.test('''"\\zO'"'""''', '''Illegal Escape In String: \\z''', 583))

	def test_584(self):
		self.assertTrue(TestLexer.test('''"'T ''', '''Unclosed String: 'T ''', 584))

	def test_585(self):
		self.assertTrue(TestLexer.test("61e61", "61e61,<EOF>", 585))

	def test_586(self):
		self.assertTrue(TestLexer.test("_TUZB&", "_TUZB,Error Token &", 586))

	def test_587(self):
		self.assertTrue(TestLexer.test('''"'"'" ''', '''Unclosed String: '"'" ''', 587))

	def test_588(self):
		self.assertTrue(TestLexer.test("s2RMkbG", "s2RMkbG,<EOF>", 588))

	def test_589(self):
		self.assertTrue(TestLexer.test('''## B% %''', '''<EOF>''', 589))

	def test_590(self):
		self.assertTrue(TestLexer.test("6urtQq3", "6,urtQq3,<EOF>", 590))

	def test_591(self):
		self.assertTrue(TestLexer.test('''"uk'"'"'""''', '''uk'"'"'",<EOF>''', 591))

	def test_592(self):
		self.assertTrue(TestLexer.test('''## ;z*.bL8n[3W''', '''<EOF>''', 592))

	def test_593(self):
		self.assertTrue(TestLexer.test('''"'"'"'"\\zE'""''', '''Illegal Escape In String: '"'"'"\\z''', 593))

	def test_594(self):
		self.assertTrue(TestLexer.test("8.962E+97", "8.962E+97,<EOF>", 594))

	def test_595(self):
		self.assertTrue(TestLexer.test('''## ca''', '''<EOF>''', 595))

	def test_596(self):
		self.assertTrue(TestLexer.test("5.090", "5.090,<EOF>", 596))

	def test_597(self):
		self.assertTrue(TestLexer.test("99.148", "99.148,<EOF>", 597))

	def test_598(self):
		self.assertTrue(TestLexer.test('''## )|W5dJI041GEkJ[3Py''', '''<EOF>''', 598))

	def test_599(self):
		self.assertTrue(TestLexer.test('''## *b V5''', '''<EOF>''', 599))
