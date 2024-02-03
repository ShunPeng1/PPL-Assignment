import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_2513011100(self):
		self.assertTrue(TestLexer.test('''## 4>;1]U0`u%Np3&''', '''<EOF>''', 2513011100))

	def test_2513011101(self):
		self.assertTrue(TestLexer.test('''"?M80'" ''', '''Unclosed String: ?M80'" ''', 2513011101))

	def test_2513011102(self):
		self.assertTrue(TestLexer.test("UI3X", "UI3X,<EOF>", 2513011102))

	def test_2513011103(self):
		self.assertTrue(TestLexer.test("53E+28", "53E+28,<EOF>", 2513011103))

	def test_2513011104(self):
		self.assertTrue(TestLexer.test('''## c502RE?t%5X ''', '''<EOF>''', 2513011104))

	def test_2513011105(self):
		self.assertTrue(TestLexer.test("P", "P,<EOF>", 2513011105))

	def test_2513011106(self):
		self.assertTrue(TestLexer.test("cf", "cf,<EOF>", 2513011106))

	def test_2513011107(self):
		self.assertTrue(TestLexer.test("0e+27", "0e+27,<EOF>", 2513011107))

	def test_2513011108(self):
		self.assertTrue(TestLexer.test('''"K5'""''', '''K5'",<EOF>''', 2513011108))

	def test_2513011109(self):
		self.assertTrue(TestLexer.test("ipg^", "ipg,Error Token ^", 2513011109))

	def test_2513011110(self):
		self.assertTrue(TestLexer.test('''## u2u{s}C|4oO&#a''', '''<EOF>''', 2513011110))

	def test_2513011111(self):
		self.assertTrue(TestLexer.test("87.399", "87.399,<EOF>", 2513011111))

	def test_2513011112(self):
		self.assertTrue(TestLexer.test('''"4 ''', '''Unclosed String: 4 ''', 2513011112))

	def test_2513011113(self):
		self.assertTrue(TestLexer.test('''## l|/4?okrW''', '''<EOF>''', 2513011113))

	def test_2513011114(self):
		self.assertTrue(TestLexer.test("jOxX_TxyO", "jOxX_TxyO,<EOF>", 2513011114))

	def test_2513011115(self):
		self.assertTrue(TestLexer.test("0cJvoz", "0,cJvoz,<EOF>", 2513011115))

	def test_2513011116(self):
		self.assertTrue(TestLexer.test('''## )''', '''<EOF>''', 2513011116))

	def test_2513011117(self):
		self.assertTrue(TestLexer.test("3e-59", "3e-59,<EOF>", 2513011117))

	def test_2513011118(self):
		self.assertTrue(TestLexer.test("U8", "U8,<EOF>", 2513011118))

	def test_2513011119(self):
		self.assertTrue(TestLexer.test("rk9H", "rk9H,<EOF>", 2513011119))

	def test_2513011120(self):
		self.assertTrue(TestLexer.test('''"'"xF'""''', '''\'"xF'",<EOF>''', 2513011120))

	def test_2513011121(self):
		self.assertTrue(TestLexer.test('''"T[j'""''', '''T[j'",<EOF>''', 2513011121))

	def test_2513011122(self):
		self.assertTrue(TestLexer.test('''"'"\\k'""''', '''Illegal Escape In String: '"\\k''', 2513011122))

	def test_2513011123(self):
		self.assertTrue(TestLexer.test('''## xXGs:%R{MPp{n+u''', '''<EOF>''', 2513011123))

	def test_2513011124(self):
		self.assertTrue(TestLexer.test('''## k/y/(I;xU''', '''<EOF>''', 2513011124))

	def test_2513011125(self):
		self.assertTrue(TestLexer.test('''## ELnk!@kb''', '''<EOF>''', 2513011125))

	def test_2513011126(self):
		self.assertTrue(TestLexer.test("Bj7AaS4ZBW", "Bj7AaS4ZBW,<EOF>", 2513011126))

	def test_2513011127(self):
		self.assertTrue(TestLexer.test("tPu#", "tPu,Error Token #", 2513011127))

	def test_2513011128(self):
		self.assertTrue(TestLexer.test('''## )y7J,`Y>nv%^@#`SQ''', '''<EOF>''', 2513011128))

	def test_2513011129(self):
		self.assertTrue(TestLexer.test("fbHzZ3", "fbHzZ3,<EOF>", 2513011129))

	def test_2513011130(self):
		self.assertTrue(TestLexer.test("1qXJInejjX", "1,qXJInejjX,<EOF>", 2513011130))

	def test_2513011131(self):
		self.assertTrue(TestLexer.test('''## Ai>Z*''', '''<EOF>''', 2513011131))

	def test_2513011132(self):
		self.assertTrue(TestLexer.test("385.104", "385.104,<EOF>", 2513011132))

	def test_2513011133(self):
		self.assertTrue(TestLexer.test('''"'"'"'"	'""''', '''\'"'"'"	'",<EOF>''', 2513011133))

	def test_2513011134(self):
		self.assertTrue(TestLexer.test('''"hS'"O ''', '''Unclosed String: hS'"O ''', 2513011134))

	def test_2513011135(self):
		self.assertTrue(TestLexer.test("YUBlU", "YUBlU,<EOF>", 2513011135))

	def test_2513011136(self):
		self.assertTrue(TestLexer.test('''## 9vU)s''', '''<EOF>''', 2513011136))

	def test_2513011137(self):
		self.assertTrue(TestLexer.test('''"'"'"'"'"G"''', '''\'"'"'"'"G,<EOF>''', 2513011137))

	def test_2513011138(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 2513011138))

	def test_2513011139(self):
		self.assertTrue(TestLexer.test('''"0"''', '''0,<EOF>''', 2513011139))

	def test_2513011140(self):
		self.assertTrue(TestLexer.test("be", "be,<EOF>", 2513011140))

	def test_2513011141(self):
		self.assertTrue(TestLexer.test("4", "4,<EOF>", 2513011141))

	def test_2513011142(self):
		self.assertTrue(TestLexer.test("OSbd", "OSbd,<EOF>", 2513011142))

	def test_2513011143(self):
		self.assertTrue(TestLexer.test('''"'"'"f\\j*"''', '''Illegal Escape In String: '"'"f\\j''', 2513011143))

	def test_2513011144(self):
		self.assertTrue(TestLexer.test('''## bp?m''', '''<EOF>''', 2513011144))

	def test_2513011145(self):
		self.assertTrue(TestLexer.test("4e01", "4e01,<EOF>", 2513011145))

	def test_2513011146(self):
		self.assertTrue(TestLexer.test("i", "i,<EOF>", 2513011146))

	def test_2513011147(self):
		self.assertTrue(TestLexer.test("81", "81,<EOF>", 2513011147))

	def test_2513011148(self):
		self.assertTrue(TestLexer.test('''## qU5;7Z^vxV''', '''<EOF>''', 2513011148))

	def test_2513011149(self):
		self.assertTrue(TestLexer.test("4", "4,<EOF>", 2513011149))

	def test_2513011150(self):
		self.assertTrue(TestLexer.test('''## whg;kL''', '''<EOF>''', 2513011150))

	def test_2513011151(self):
		self.assertTrue(TestLexer.test('''## 0ZL$|EOZAdYs!ZwL''', '''<EOF>''', 2513011151))

	def test_2513011152(self):
		self.assertTrue(TestLexer.test("39.809", "39.809,<EOF>", 2513011152))

	def test_2513011153(self):
		self.assertTrue(TestLexer.test('''## qj[zpy45nV_Y`O%_''', '''<EOF>''', 2513011153))

	def test_2513011154(self):
		self.assertTrue(TestLexer.test("255.193E-30", "255.193E-30,<EOF>", 2513011154))

	def test_2513011155(self):
		self.assertTrue(TestLexer.test('''## 0H;Akre29f"SA''', '''<EOF>''', 2513011155))

	def test_2513011156(self):
		self.assertTrue(TestLexer.test("9E82", "9E82,<EOF>", 2513011156))

	def test_2513011157(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011157))

	def test_2513011158(self):
		self.assertTrue(TestLexer.test("3.791E84", "3.791E84,<EOF>", 2513011158))

	def test_2513011159(self):
		self.assertTrue(TestLexer.test('''"n\\jb'"'""''', '''Illegal Escape In String: n\\j''', 2513011159))

	def test_2513011160(self):
		self.assertTrue(TestLexer.test('''## ?Ep+q4m*2"4tCR%''', '''<EOF>''', 2513011160))

	def test_2513011161(self):
		self.assertTrue(TestLexer.test("508.336", "508.336,<EOF>", 2513011161))

	def test_2513011162(self):
		self.assertTrue(TestLexer.test('''## +x]$L''', '''<EOF>''', 2513011162))

	def test_2513011163(self):
		self.assertTrue(TestLexer.test('''## lm2*sEnf,''', '''<EOF>''', 2513011163))

	def test_2513011164(self):
		self.assertTrue(TestLexer.test('''## (EilP''', '''<EOF>''', 2513011164))

	def test_2513011165(self):
		self.assertTrue(TestLexer.test("4e+21", "4e+21,<EOF>", 2513011165))

	def test_2513011166(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 2513011166))

	def test_2513011167(self):
		self.assertTrue(TestLexer.test('''"b
'""''', '''Unclosed String: b''', 2513011167))

	def test_2513011168(self):
		self.assertTrue(TestLexer.test("S", "S,<EOF>", 2513011168))

	def test_2513011169(self):
		self.assertTrue(TestLexer.test("634.308", "634.308,<EOF>", 2513011169))

	def test_2513011170(self):
		self.assertTrue(TestLexer.test("pVKhsT", "pVKhsT,<EOF>", 2513011170))

	def test_2513011171(self):
		self.assertTrue(TestLexer.test('''## -T2d?''', '''<EOF>''', 2513011171))

	def test_2513011172(self):
		self.assertTrue(TestLexer.test("o", "o,<EOF>", 2513011172))

	def test_2513011173(self):
		self.assertTrue(TestLexer.test("6.324", "6.324,<EOF>", 2513011173))

	def test_2513011174(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011174))

	def test_2513011175(self):
		self.assertTrue(TestLexer.test('''"\\e
D'"'"'""''', '''Illegal Escape In String: \\e''', 2513011175))

	def test_2513011176(self):
		self.assertTrue(TestLexer.test("79", "79,<EOF>", 2513011176))

	def test_2513011177(self):
		self.assertTrue(TestLexer.test("E", "E,<EOF>", 2513011177))

	def test_2513011178(self):
		self.assertTrue(TestLexer.test("$50zpr9x", "Error Token $", 2513011178))

	def test_2513011179(self):
		self.assertTrue(TestLexer.test('''"\\wg"''', '''Illegal Escape In String: \\w''', 2513011179))

	def test_2513011180(self):
		self.assertTrue(TestLexer.test("3.009", "3.009,<EOF>", 2513011180))

	def test_2513011181(self):
		self.assertTrue(TestLexer.test('''"S ''', '''Unclosed String: S ''', 2513011181))

	def test_2513011182(self):
		self.assertTrue(TestLexer.test("YeFR2R8b_x", "YeFR2R8b_x,<EOF>", 2513011182))

	def test_2513011183(self):
		self.assertTrue(TestLexer.test('''## kpg&4%X`8''', '''<EOF>''', 2513011183))

	def test_2513011184(self):
		self.assertTrue(TestLexer.test('''## 2,6]''', '''<EOF>''', 2513011184))

	def test_2513011185(self):
		self.assertTrue(TestLexer.test("N_yw0$", "N_yw0,Error Token $", 2513011185))

	def test_2513011186(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 2513011186))

	def test_2513011187(self):
		self.assertTrue(TestLexer.test("@de", "Error Token @", 2513011187))

	def test_2513011188(self):
		self.assertTrue(TestLexer.test('''">N\\oM"''', '''Illegal Escape In String: >N\\o''', 2513011188))

	def test_2513011189(self):
		self.assertTrue(TestLexer.test('''## AXxH.[(zr3N>dx+z[d><''', '''<EOF>''', 2513011189))

	def test_2513011190(self):
		self.assertTrue(TestLexer.test("348", "348,<EOF>", 2513011190))

	def test_2513011191(self):
		self.assertTrue(TestLexer.test('''## /mUQq)#o&FJ''', '''<EOF>''', 2513011191))

	def test_2513011192(self):
		self.assertTrue(TestLexer.test("232.137", "232.137,<EOF>", 2513011192))

	def test_2513011193(self):
		self.assertTrue(TestLexer.test("6CC", "6,CC,<EOF>", 2513011193))

	def test_2513011194(self):
		self.assertTrue(TestLexer.test('''## NP''', '''<EOF>''', 2513011194))

	def test_2513011195(self):
		self.assertTrue(TestLexer.test('''## nIQ^`^20#''', '''<EOF>''', 2513011195))

	def test_2513011196(self):
		self.assertTrue(TestLexer.test('''## eJwDy}rHjT>EIe5''', '''<EOF>''', 2513011196))

	def test_2513011197(self):
		self.assertTrue(TestLexer.test("lgE", "lgE,<EOF>", 2513011197))

	def test_2513011198(self):
		self.assertTrue(TestLexer.test('''## tLivoq}7m!''', '''<EOF>''', 2513011198))

	def test_2513011199(self):
		self.assertTrue(TestLexer.test("511E+35", "511E+35,<EOF>", 2513011199))
