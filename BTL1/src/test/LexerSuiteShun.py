import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_2513011100(self):
		self.assertTrue(TestLexer.test('''".'"t0"''', '''.'"t0,<EOF>''', 2513011100))

	def test_2513011101(self):
		self.assertTrue(TestLexer.test('''## @o0~zp[b0cVjp''', '''<EOF>''', 2513011101))

	def test_2513011102(self):
		self.assertTrue(TestLexer.test("P_fXZFt1S", "P_fXZFt1S,<EOF>", 2513011102))

	def test_2513011103(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011103))

	def test_2513011104(self):
		self.assertTrue(TestLexer.test('''## Xv&$^/''', '''<EOF>''', 2513011104))

	def test_2513011105(self):
		self.assertTrue(TestLexer.test('''"'"
'"'"'"`"''', '''Unclosed String: '"''', 2513011105))

	def test_2513011106(self):
		self.assertTrue(TestLexer.test("412", "412,<EOF>", 2513011106))

	def test_2513011107(self):
		self.assertTrue(TestLexer.test("4", "4,<EOF>", 2513011107))

	def test_2513011108(self):
		self.assertTrue(TestLexer.test('''"'"1
r'"'""''', '''Unclosed String: '"1''', 2513011108))

	def test_2513011109(self):
		self.assertTrue(TestLexer.test("7", "7,<EOF>", 2513011109))

	def test_2513011110(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011110))

	def test_2513011111(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011111))

	def test_2513011112(self):
		self.assertTrue(TestLexer.test("7", "7,<EOF>", 2513011112))

	def test_2513011113(self):
		self.assertTrue(TestLexer.test("6", "6,<EOF>", 2513011113))

	def test_2513011114(self):
		self.assertTrue(TestLexer.test('''"\\a	F"''', '''Illegal Escape In String: \\a''', 2513011114))

	def test_2513011115(self):
		self.assertTrue(TestLexer.test('''## f}qUH{Am,nev+<=(=Nt''', '''<EOF>''', 2513011115))

	def test_2513011116(self):
		self.assertTrue(TestLexer.test("O", "O,<EOF>", 2513011116))

	def test_2513011117(self):
		self.assertTrue(TestLexer.test('''## @z-*6r2HyYQp5N1{4D8f''', '''<EOF>''', 2513011117))

	def test_2513011118(self):
		self.assertTrue(TestLexer.test('''"\\u'""''', '''Illegal Escape In String: \\u''', 2513011118))

	def test_2513011119(self):
		self.assertTrue(TestLexer.test("86e-64", "86e-64,<EOF>", 2513011119))

	def test_2513011120(self):
		self.assertTrue(TestLexer.test("H", "H,<EOF>", 2513011120))

	def test_2513011121(self):
		self.assertTrue(TestLexer.test("bz", "bz,<EOF>", 2513011121))

	def test_2513011122(self):
		self.assertTrue(TestLexer.test('''## #9Fe*JvlzzM1nB3+ `|A''', '''<EOF>''', 2513011122))

	def test_2513011123(self):
		self.assertTrue(TestLexer.test('''"='"'"\\js"''', '''Illegal Escape In String: ='"'"\\j''', 2513011123))

	def test_2513011124(self):
		self.assertTrue(TestLexer.test("9@Y", "9,Error Token @", 2513011124))

	def test_2513011125(self):
		self.assertTrue(TestLexer.test("gxLa1Fa8", "gxLa1Fa8,<EOF>", 2513011125))

	def test_2513011126(self):
		self.assertTrue(TestLexer.test('''"'"Ia"''', '''\'"Ia,<EOF>''', 2513011126))

	def test_2513011127(self):
		self.assertTrue(TestLexer.test('''## XGZx05=tXQI78j{TE-''', '''<EOF>''', 2513011127))

	def test_2513011128(self):
		self.assertTrue(TestLexer.test("7ONXf0u", "7,ONXf0u,<EOF>", 2513011128))

	def test_2513011129(self):
		self.assertTrue(TestLexer.test("S9LFP56dLg", "S9LFP56dLg,<EOF>", 2513011129))

	def test_2513011130(self):
		self.assertTrue(TestLexer.test("3.391e-14", "3.391e-14,<EOF>", 2513011130))

	def test_2513011131(self):
		self.assertTrue(TestLexer.test("32", "32,<EOF>", 2513011131))

	def test_2513011132(self):
		self.assertTrue(TestLexer.test('''## uf4PmO7M?Q''', '''<EOF>''', 2513011132))

	def test_2513011133(self):
		self.assertTrue(TestLexer.test("1LwCtY", "1,LwCtY,<EOF>", 2513011133))

	def test_2513011134(self):
		self.assertTrue(TestLexer.test('''## a''', '''<EOF>''', 2513011134))

	def test_2513011135(self):
		self.assertTrue(TestLexer.test("6e+89", "6e+89,<EOF>", 2513011135))

	def test_2513011136(self):
		self.assertTrue(TestLexer.test('''##  pVn+pgqyOD Q+-jAC-''', '''<EOF>''', 2513011136))

	def test_2513011137(self):
		self.assertTrue(TestLexer.test('''##  O5ln*|P&q{]=k''', '''<EOF>''', 2513011137))

	def test_2513011138(self):
		self.assertTrue(TestLexer.test("q6&", "q6,Error Token &", 2513011138))

	def test_2513011139(self):
		self.assertTrue(TestLexer.test("mE", "mE,<EOF>", 2513011139))

	def test_2513011140(self):
		self.assertTrue(TestLexer.test("LWgIW", "LWgIW,<EOF>", 2513011140))

	def test_2513011141(self):
		self.assertTrue(TestLexer.test('''## #mg''', '''<EOF>''', 2513011141))

	def test_2513011142(self):
		self.assertTrue(TestLexer.test('''## :01g''', '''<EOF>''', 2513011142))

	def test_2513011143(self):
		self.assertTrue(TestLexer.test('''"
'"j"''', '''Unclosed String: ''', 2513011143))

	def test_2513011144(self):
		self.assertTrue(TestLexer.test("Ub2KE#gDFd", "Ub2KE,Error Token #", 2513011144))

	def test_2513011145(self):
		self.assertTrue(TestLexer.test('''## rZ-!fF''', '''<EOF>''', 2513011145))

	def test_2513011146(self):
		self.assertTrue(TestLexer.test('''## >z23U''', '''<EOF>''', 2513011146))

	def test_2513011147(self):
		self.assertTrue(TestLexer.test("Z5uo", "Z5uo,<EOF>", 2513011147))

	def test_2513011148(self):
		self.assertTrue(TestLexer.test("6.223", "6.223,<EOF>", 2513011148))

	def test_2513011149(self):
		self.assertTrue(TestLexer.test("wSrw", "wSrw,<EOF>", 2513011149))

	def test_2513011150(self):
		self.assertTrue(TestLexer.test('''")'"- ''', '''Unclosed String: )'"- ''', 2513011150))

	def test_2513011151(self):
		self.assertTrue(TestLexer.test("ukl3$f9D", "ukl3,Error Token $", 2513011151))

	def test_2513011152(self):
		self.assertTrue(TestLexer.test('''## c9`EQ<Bvc''', '''<EOF>''', 2513011152))

	def test_2513011153(self):
		self.assertTrue(TestLexer.test("92", "92,<EOF>", 2513011153))

	def test_2513011154(self):
		self.assertTrue(TestLexer.test('''## P''', '''<EOF>''', 2513011154))

	def test_2513011155(self):
		self.assertTrue(TestLexer.test("25e+34", "25e+34,<EOF>", 2513011155))

	def test_2513011156(self):
		self.assertTrue(TestLexer.test('''"3q'"\\g'""''', '''Illegal Escape In String: 3q'"\\g''', 2513011156))

	def test_2513011157(self):
		self.assertTrue(TestLexer.test("39E07", "39E07,<EOF>", 2513011157))

	def test_2513011158(self):
		self.assertTrue(TestLexer.test('''"\\k/"''', '''Illegal Escape In String: \\k''', 2513011158))

	def test_2513011159(self):
		self.assertTrue(TestLexer.test("3.188", "3.188,<EOF>", 2513011159))

	def test_2513011160(self):
		self.assertTrue(TestLexer.test("96sd", "96,sd,<EOF>", 2513011160))

	def test_2513011161(self):
		self.assertTrue(TestLexer.test("TfY6ts", "TfY6ts,<EOF>", 2513011161))

	def test_2513011162(self):
		self.assertTrue(TestLexer.test("2E-24", "2E-24,<EOF>", 2513011162))

	def test_2513011163(self):
		self.assertTrue(TestLexer.test("74e96", "74e96,<EOF>", 2513011163))

	def test_2513011164(self):
		self.assertTrue(TestLexer.test("P4HWI8EMQ", "P4HWI8EMQ,<EOF>", 2513011164))

	def test_2513011165(self):
		self.assertTrue(TestLexer.test("4hpb326s", "4,hpb326s,<EOF>", 2513011165))

	def test_2513011166(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011166))

	def test_2513011167(self):
		self.assertTrue(TestLexer.test('''## h)v$XnzWo1!<''', '''<EOF>''', 2513011167))

	def test_2513011168(self):
		self.assertTrue(TestLexer.test('''## )''', '''<EOF>''', 2513011168))

	def test_2513011169(self):
		self.assertTrue(TestLexer.test("p#u0k", "p,Error Token #", 2513011169))

	def test_2513011170(self):
		self.assertTrue(TestLexer.test("w2HFa", "w2HFa,<EOF>", 2513011170))

	def test_2513011171(self):
		self.assertTrue(TestLexer.test("602e+66", "602e+66,<EOF>", 2513011171))

	def test_2513011172(self):
		self.assertTrue(TestLexer.test("3mPcOF", "3,mPcOF,<EOF>", 2513011172))

	def test_2513011173(self):
		self.assertTrue(TestLexer.test("24e+37", "24e+37,<EOF>", 2513011173))

	def test_2513011174(self):
		self.assertTrue(TestLexer.test('''"'"'"\\v'""''', '''Illegal Escape In String: '"'"\\v''', 2513011174))

	def test_2513011175(self):
		self.assertTrue(TestLexer.test('''"('""''', '''('",<EOF>''', 2513011175))

	def test_2513011176(self):
		self.assertTrue(TestLexer.test("37", "37,<EOF>", 2513011176))

	def test_2513011177(self):
		self.assertTrue(TestLexer.test("HyqSwSO", "HyqSwSO,<EOF>", 2513011177))

	def test_2513011178(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 2513011178))

	def test_2513011179(self):
		self.assertTrue(TestLexer.test('''## VGl>eX#N`F-7N^**O''', '''<EOF>''', 2513011179))

	def test_2513011180(self):
		self.assertTrue(TestLexer.test("kFGZ", "kFGZ,<EOF>", 2513011180))

	def test_2513011181(self):
		self.assertTrue(TestLexer.test("9E-55", "9E-55,<EOF>", 2513011181))

	def test_2513011182(self):
		self.assertTrue(TestLexer.test("920", "920,<EOF>", 2513011182))

	def test_2513011183(self):
		self.assertTrue(TestLexer.test("55", "55,<EOF>", 2513011183))

	def test_2513011184(self):
		self.assertTrue(TestLexer.test("675.554E-50", "675.554E-50,<EOF>", 2513011184))

	def test_2513011185(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011185))

	def test_2513011186(self):
		self.assertTrue(TestLexer.test('''## f{_RE''', '''<EOF>''', 2513011186))

	def test_2513011187(self):
		self.assertTrue(TestLexer.test("Pon", "Pon,<EOF>", 2513011187))

	def test_2513011188(self):
		self.assertTrue(TestLexer.test('''"'"
'""''', '''Unclosed String: '"''', 2513011188))

	def test_2513011189(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011189))

	def test_2513011190(self):
		self.assertTrue(TestLexer.test("8.770", "8.770,<EOF>", 2513011190))

	def test_2513011191(self):
		self.assertTrue(TestLexer.test("1.881", "1.881,<EOF>", 2513011191))

	def test_2513011192(self):
		self.assertTrue(TestLexer.test("5.675", "5.675,<EOF>", 2513011192))

	def test_2513011193(self):
		self.assertTrue(TestLexer.test("^1bHNbTo", "Error Token ^", 2513011193))

	def test_2513011194(self):
		self.assertTrue(TestLexer.test('''"'"('"\\y'"G"''', '''Illegal Escape In String: '"('"\\y''', 2513011194))

	def test_2513011195(self):
		self.assertTrue(TestLexer.test("kLpe_3", "kLpe_3,<EOF>", 2513011195))

	def test_2513011196(self):
		self.assertTrue(TestLexer.test('''## uA(tceLc''', '''<EOF>''', 2513011196))

	def test_2513011197(self):
		self.assertTrue(TestLexer.test('''## 6QquO*kC;@}z''', '''<EOF>''', 2513011197))

	def test_2513011198(self):
		self.assertTrue(TestLexer.test('''"
'"H'""''', '''Unclosed String: ''', 2513011198))

	def test_2513011199(self):
		self.assertTrue(TestLexer.test('''"KQAF'""''', '''KQAF'",<EOF>''', 2513011199))
