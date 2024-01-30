import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_100(self):
		self.assertTrue(TestLexer.test('''## j_=a2fN8z!*hs''', '''## j_=a2fN8z!*hs,<EOF>''', 100))

	def test_101(self):
		self.assertTrue(TestLexer.test("8hUuNaO", "8,hUuNaO,<EOF>", 101))

	def test_102(self):
		self.assertTrue(TestLexer.test("104E01", "104E01,<EOF>", 102))

	def test_103(self):
		self.assertTrue(TestLexer.test("2.623e03", "2.623e03,<EOF>", 103))

	def test_104(self):
		self.assertTrue(TestLexer.test("249", "249,<EOF>", 104))

	def test_105(self):
		self.assertTrue(TestLexer.test("9.791E+24", "9.791E+24,<EOF>", 105))

	def test_106(self):
		self.assertTrue(TestLexer.test('''## O#7''', '''## O#7,<EOF>''', 106))

	def test_107(self):
		self.assertTrue(TestLexer.test("55E+71", "55E+71,<EOF>", 107))

	def test_108(self):
		self.assertTrue(TestLexer.test('''"
'"'""''', '''Unclosed String: ''', 108))

	def test_109(self):
		self.assertTrue(TestLexer.test('''"'"W*e'""''', '''\'"W*e'",<EOF>''', 109))

	def test_110(self):
		self.assertTrue(TestLexer.test("JM25", "JM25,<EOF>", 110))

	def test_111(self):
		self.assertTrue(TestLexer.test('''"[)?'"x ''', '''Unclosed String: [)?'"x ''', 111))

	def test_112(self):
		self.assertTrue(TestLexer.test('''## RTK!yHl^!Lo&^+S6kiD''', '''## RTK!yHl^!Lo&^+S6kiD,<EOF>''', 112))

	def test_113(self):
		self.assertTrue(TestLexer.test("438.032", "438.032,<EOF>", 113))

	def test_114(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 114))

	def test_115(self):
		self.assertTrue(TestLexer.test("67.963E42", "67.963E42,<EOF>", 115))

	def test_116(self):
		self.assertTrue(TestLexer.test('''"\\g'""''', '''Illegal Escape In String: \\g''', 116))

	def test_117(self):
		self.assertTrue(TestLexer.test('''"u'"6d"''', '''u'"6d,<EOF>''', 117))

	def test_118(self):
		self.assertTrue(TestLexer.test('''## 0op''', '''## 0op,<EOF>''', 118))

	def test_119(self):
		self.assertTrue(TestLexer.test("hmK$", "hmK,Error Token $", 119))

	def test_120(self):
		self.assertTrue(TestLexer.test("72.067", "72.067,<EOF>", 120))

	def test_121(self):
		self.assertTrue(TestLexer.test('''"'"'"\\u-?"''', '''Illegal Escape In String: '"'"\\u''', 121))

	def test_122(self):
		self.assertTrue(TestLexer.test('''## k]Uem>=s-+Zi[xfKk6&''', '''## k]Uem>=s-+Zi[xfKk6&,<EOF>''', 122))

	def test_123(self):
		self.assertTrue(TestLexer.test("5.835E66", "5.835E66,<EOF>", 123))

	def test_124(self):
		self.assertTrue(TestLexer.test('''"'")N\\s'""''', '''Illegal Escape In String: '")N\\s''', 124))

	def test_125(self):
		self.assertTrue(TestLexer.test("aGzwMK5LI", "aGzwMK5LI,<EOF>", 125))

	def test_126(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 126))

	def test_127(self):
		self.assertTrue(TestLexer.test('''## Q[UesY4hM%gH+B2{gbm''', '''## Q[UesY4hM%gH+B2{gbm,<EOF>''', 127))

	def test_128(self):
		self.assertTrue(TestLexer.test("628.436E76", "628.436E76,<EOF>", 128))

	def test_129(self):
		self.assertTrue(TestLexer.test('''## R"3/''', '''## R"3/,<EOF>''', 129))

	def test_130(self):
		self.assertTrue(TestLexer.test("9.990", "9.990,<EOF>", 130))

	def test_131(self):
		self.assertTrue(TestLexer.test('''## q~H%#WrWi:''', '''## q~H%#WrWi:,<EOF>''', 131))

	def test_132(self):
		self.assertTrue(TestLexer.test('''## 2tE3yci{#Lu''', '''## 2tE3yci{#Lu,<EOF>''', 132))

	def test_133(self):
		self.assertTrue(TestLexer.test("7", "7,<EOF>", 133))

	def test_134(self):
		self.assertTrue(TestLexer.test('''## q''', '''## q,<EOF>''', 134))

	def test_135(self):
		self.assertTrue(TestLexer.test("550.500E64", "550.500E64,<EOF>", 135))

	def test_136(self):
		self.assertTrue(TestLexer.test('''"'"^'""''', '''\'"^'",<EOF>''', 136))

	def test_137(self):
		self.assertTrue(TestLexer.test("xl2hgkIK", "xl2hgkIK,<EOF>", 137))

	def test_138(self):
		self.assertTrue(TestLexer.test('''## |{{i>XtA''', '''## |{{i>XtA,<EOF>''', 138))

	def test_139(self):
		self.assertTrue(TestLexer.test('''"'"'"!C'""''', '''\'"'"!C'",<EOF>''', 139))

	def test_140(self):
		self.assertTrue(TestLexer.test("55E31", "55E31,<EOF>", 140))

	def test_141(self):
		self.assertTrue(TestLexer.test('''"L%'"="''', '''L%'"=,<EOF>''', 141))

	def test_142(self):
		self.assertTrue(TestLexer.test('''## Om*V_|[eq+''', '''## Om*V_|[eq+,<EOF>''', 142))

	def test_143(self):
		self.assertTrue(TestLexer.test("8.153", "8.153,<EOF>", 143))

	def test_144(self):
		self.assertTrue(TestLexer.test("A^6", "A,Error Token ^", 144))

	def test_145(self):
		self.assertTrue(TestLexer.test("357.132", "357.132,<EOF>", 145))

	def test_146(self):
		self.assertTrue(TestLexer.test("eG_", "eG_,<EOF>", 146))

	def test_147(self):
		self.assertTrue(TestLexer.test("676.400E50", "676.400E50,<EOF>", 147))

	def test_148(self):
		self.assertTrue(TestLexer.test("g1xF", "g1xF,<EOF>", 148))

	def test_149(self):
		self.assertTrue(TestLexer.test('''"zm\\o@'""''', '''Illegal Escape In String: zm\\o''', 149))

	def test_150(self):
		self.assertTrue(TestLexer.test('''"
'""''', '''Unclosed String: ''', 150))

	def test_151(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 151))

	def test_152(self):
		self.assertTrue(TestLexer.test("869.532", "869.532,<EOF>", 152))

	def test_153(self):
		self.assertTrue(TestLexer.test("6bXW$dY0", "6,bXW,Error Token $", 153))

	def test_154(self):
		self.assertTrue(TestLexer.test("9wA^2keW", "9,wA,Error Token ^", 154))

	def test_155(self):
		self.assertTrue(TestLexer.test('''## 8xfeeX6ag"A+s''', '''## 8xfeeX6ag"A+s,<EOF>''', 155))

	def test_156(self):
		self.assertTrue(TestLexer.test("QBsxVvmSZ", "QBsxVvmSZ,<EOF>", 156))

	def test_157(self):
		self.assertTrue(TestLexer.test('''"R'""''', '''R'",<EOF>''', 157))

	def test_158(self):
		self.assertTrue(TestLexer.test('''## |)d^ ]5-:hJ_=AoZ$ut''', '''## |)d^ ]5-:hJ_=AoZ$ut,<EOF>''', 158))

	def test_159(self):
		self.assertTrue(TestLexer.test("58E+89", "58E+89,<EOF>", 159))

	def test_160(self):
		self.assertTrue(TestLexer.test('''## S#?0x>2PX$<n~=ym''', '''## S#?0x>2PX$<n~=ym,<EOF>''', 160))

	def test_161(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 161))

	def test_162(self):
		self.assertTrue(TestLexer.test('''## [QSez8e.T''', '''## [QSez8e.T,<EOF>''', 162))

	def test_163(self):
		self.assertTrue(TestLexer.test('''"0'""''', '''0'",<EOF>''', 163))

	def test_164(self):
		self.assertTrue(TestLexer.test('''## bFnSZ+g3ks0_T!0<Es''', '''## bFnSZ+g3ks0_T!0<Es,<EOF>''', 164))

	def test_165(self):
		self.assertTrue(TestLexer.test("34.338", "34.338,<EOF>", 165))

	def test_166(self):
		self.assertTrue(TestLexer.test("41E30", "41E30,<EOF>", 166))

	def test_167(self):
		self.assertTrue(TestLexer.test("21.811", "21.811,<EOF>", 167))

	def test_168(self):
		self.assertTrue(TestLexer.test('''"'"\\w~"''', '''Illegal Escape In String: '"\\w''', 168))

	def test_169(self):
		self.assertTrue(TestLexer.test('''"TC
t'""''', '''Unclosed String: TC''', 169))

	def test_170(self):
		self.assertTrue(TestLexer.test('''"8f'"\\gs1"''', '''Illegal Escape In String: 8f'"\\g''', 170))

	def test_171(self):
		self.assertTrue(TestLexer.test("19.655E77", "19.655E77,<EOF>", 171))

	def test_172(self):
		self.assertTrue(TestLexer.test('''## aNiZp:"oO9c3}''', '''## aNiZp:"oO9c3},<EOF>''', 172))

	def test_173(self):
		self.assertTrue(TestLexer.test("Mc&", "Mc,Error Token &", 173))

	def test_174(self):
		self.assertTrue(TestLexer.test('''"\\c'"Y'"'""''', '''Illegal Escape In String: \\c''', 174))

	def test_175(self):
		self.assertTrue(TestLexer.test("V6mmJpAht", "V6mmJpAht,<EOF>", 175))

	def test_176(self):
		self.assertTrue(TestLexer.test("kBzwb", "kBzwb,<EOF>", 176))

	def test_177(self):
		self.assertTrue(TestLexer.test('''"'"
'"'"'"|"''', '''Unclosed String: '"''', 177))

	def test_178(self):
		self.assertTrue(TestLexer.test("#G", "Error Token #", 178))

	def test_179(self):
		self.assertTrue(TestLexer.test('''## ,PGKG''', '''## ,PGKG,<EOF>''', 179))

	def test_180(self):
		self.assertTrue(TestLexer.test('''## <>YT:|,''', '''## <>YT:|,,<EOF>''', 180))

	def test_181(self):
		self.assertTrue(TestLexer.test("980", "980,<EOF>", 181))

	def test_182(self):
		self.assertTrue(TestLexer.test('''"3_\\ed'":"''', '''Illegal Escape In String: 3_\\e''', 182))

	def test_183(self):
		self.assertTrue(TestLexer.test("G9ZP", "G9ZP,<EOF>", 183))

	def test_184(self):
		self.assertTrue(TestLexer.test("1.927E-26", "1.927E-26,<EOF>", 184))

	def test_185(self):
		self.assertTrue(TestLexer.test("CcKbUbhj", "CcKbUbhj,<EOF>", 185))

	def test_186(self):
		self.assertTrue(TestLexer.test('''"'"\\m]"''', '''Illegal Escape In String: '"\\m''', 186))

	def test_187(self):
		self.assertTrue(TestLexer.test('''"Z['"'"'" ''', '''Unclosed String: Z['"'"'" ''', 187))

	def test_188(self):
		self.assertTrue(TestLexer.test("0E61", "0E61,<EOF>", 188))

	def test_189(self):
		self.assertTrue(TestLexer.test('''## =l<dg3BXH:qH.xRN,6''', '''## =l<dg3BXH:qH.xRN,6,<EOF>''', 189))

	def test_190(self):
		self.assertTrue(TestLexer.test('''## w@UFaxnb}>e@VxHTo"z[''', '''## w@UFaxnb}>e@VxHTo"z[,<EOF>''', 190))

	def test_191(self):
		self.assertTrue(TestLexer.test("59E-87", "59E-87,<EOF>", 191))

	def test_192(self):
		self.assertTrue(TestLexer.test('''## 9r$NKw(hL2elC''', '''## 9r$NKw(hL2elC,<EOF>''', 192))

	def test_193(self):
		self.assertTrue(TestLexer.test('''"
p ''', '''Unclosed String: ''', 193))

	def test_194(self):
		self.assertTrue(TestLexer.test("#m2JS@Z_n", "Error Token #", 194))

	def test_195(self):
		self.assertTrue(TestLexer.test("rqsg1a", "rqsg1a,<EOF>", 195))

	def test_196(self):
		self.assertTrue(TestLexer.test('''## i''', '''## i,<EOF>''', 196))

	def test_197(self):
		self.assertTrue(TestLexer.test('''"cd'""''', '''cd'",<EOF>''', 197))

	def test_198(self):
		self.assertTrue(TestLexer.test('''## U1DdQB_3TOhJ0)^uG*94''', '''## U1DdQB_3TOhJ0)^uG*94,<EOF>''', 198))

	def test_199(self):
		self.assertTrue(TestLexer.test('''"'"'"'" ''', '''Unclosed String: '"'"'" ''', 199))
