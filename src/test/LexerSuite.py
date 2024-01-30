import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_2513011100(self):
		self.assertTrue(TestLexer.test('''## kBPdja6 np''', '''<EOF>''', 2513011100))

	def test_2513011101(self):
		self.assertTrue(TestLexer.test("y", "y,<EOF>", 2513011101))

	def test_2513011102(self):
		self.assertTrue(TestLexer.test("3eRTfIKA", "3,eRTfIKA,<EOF>", 2513011102))

	def test_2513011103(self):
		self.assertTrue(TestLexer.test('''## 1t6gJMTa_pE;C$e!/(''', '''<EOF>''', 2513011103))

	def test_2513011104(self):
		self.assertTrue(TestLexer.test("1E+99", "1E+99,<EOF>", 2513011104))

	def test_2513011105(self):
		self.assertTrue(TestLexer.test('''## e4_J[gY''', '''<EOF>''', 2513011105))

	def test_2513011106(self):
		self.assertTrue(TestLexer.test('''"\\a'""''', '''Illegal Escape In String: \\a''', 2513011106))

	def test_2513011107(self):
		self.assertTrue(TestLexer.test("89", "89,<EOF>", 2513011107))

	def test_2513011108(self):
		self.assertTrue(TestLexer.test('''## k?''', '''<EOF>''', 2513011108))

	def test_2513011109(self):
		self.assertTrue(TestLexer.test("FQRtKc", "FQRtKc,<EOF>", 2513011109))

	def test_2513011110(self):
		self.assertTrue(TestLexer.test('''## rDX]&xsDUC''', '''<EOF>''', 2513011110))

	def test_2513011111(self):
		self.assertTrue(TestLexer.test('''## S''', '''<EOF>''', 2513011111))

	def test_2513011112(self):
		self.assertTrue(TestLexer.test('''## Z[fR )YG''', '''<EOF>''', 2513011112))

	def test_2513011113(self):
		self.assertTrue(TestLexer.test('''"
M'""''', '''Unclosed String: ''', 2513011113))

	def test_2513011114(self):
		self.assertTrue(TestLexer.test("T", "T,<EOF>", 2513011114))

	def test_2513011115(self):
		self.assertTrue(TestLexer.test("63", "63,<EOF>", 2513011115))

	def test_2513011116(self):
		self.assertTrue(TestLexer.test("WI&", "WI,Error Token &", 2513011116))

	def test_2513011117(self):
		self.assertTrue(TestLexer.test("2.270e+52", "2.270e+52,<EOF>", 2513011117))

	def test_2513011118(self):
		self.assertTrue(TestLexer.test("Yebhg", "Yebhg,<EOF>", 2513011118))

	def test_2513011119(self):
		self.assertTrue(TestLexer.test("jZ", "jZ,<EOF>", 2513011119))

	def test_2513011120(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011120))

	def test_2513011121(self):
		self.assertTrue(TestLexer.test("Rh#bXT", "Rh,Error Token #", 2513011121))

	def test_2513011122(self):
		self.assertTrue(TestLexer.test("w1m", "w1m,<EOF>", 2513011122))

	def test_2513011123(self):
		self.assertTrue(TestLexer.test('''"\\wJ'"> "''', '''Illegal Escape In String: \\w''', 2513011123))

	def test_2513011124(self):
		self.assertTrue(TestLexer.test('''"\\z~'"'"Hb"''', '''Illegal Escape In String: \\z''', 2513011124))

	def test_2513011125(self):
		self.assertTrue(TestLexer.test("1fHEPY", "1,fHEPY,<EOF>", 2513011125))

	def test_2513011126(self):
		self.assertTrue(TestLexer.test('''## |}OP6a)''', '''<EOF>''', 2513011126))

	def test_2513011127(self):
		self.assertTrue(TestLexer.test('''## .)=e7f}j''', '''<EOF>''', 2513011127))

	def test_2513011128(self):
		self.assertTrue(TestLexer.test('''## MA0m40DoQ`FT I''', '''<EOF>''', 2513011128))

	def test_2513011129(self):
		self.assertTrue(TestLexer.test('''## !Bh+QB1N''', '''<EOF>''', 2513011129))

	def test_2513011130(self):
		self.assertTrue(TestLexer.test("c_BD^lGX", "c_BD,Error Token ^", 2513011130))

	def test_2513011131(self):
		self.assertTrue(TestLexer.test("T&cPZccPf", "T,Error Token &", 2513011131))

	def test_2513011132(self):
		self.assertTrue(TestLexer.test("4E-71", "4E-71,<EOF>", 2513011132))

	def test_2513011133(self):
		self.assertTrue(TestLexer.test("165", "165,<EOF>", 2513011133))

	def test_2513011134(self):
		self.assertTrue(TestLexer.test("xCu", "xCu,<EOF>", 2513011134))

	def test_2513011135(self):
		self.assertTrue(TestLexer.test('''## =})kp;x(d]6''', '''<EOF>''', 2513011135))

	def test_2513011136(self):
		self.assertTrue(TestLexer.test("napGYzwZpE", "napGYzwZpE,<EOF>", 2513011136))

	def test_2513011137(self):
		self.assertTrue(TestLexer.test("Ok0l", "Ok0l,<EOF>", 2513011137))

	def test_2513011138(self):
		self.assertTrue(TestLexer.test('''"'"'" ''', '''Unclosed String: '"'" ''', 2513011138))

	def test_2513011139(self):
		self.assertTrue(TestLexer.test("8rgadwl", "8,rgadwl,<EOF>", 2513011139))

	def test_2513011140(self):
		self.assertTrue(TestLexer.test("27", "27,<EOF>", 2513011140))

	def test_2513011141(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 2513011141))

	def test_2513011142(self):
		self.assertTrue(TestLexer.test('''"<- ''', '''Unclosed String: <- ''', 2513011142))

	def test_2513011143(self):
		self.assertTrue(TestLexer.test("4.974", "4.974,<EOF>", 2513011143))

	def test_2513011144(self):
		self.assertTrue(TestLexer.test("kNmk", "kNmk,<EOF>", 2513011144))

	def test_2513011145(self):
		self.assertTrue(TestLexer.test('''## TSU''', '''<EOF>''', 2513011145))

	def test_2513011146(self):
		self.assertTrue(TestLexer.test("745e+47", "745e+47,<EOF>", 2513011146))

	def test_2513011147(self):
		self.assertTrue(TestLexer.test('''## B9j%k#5Cy;I4''', '''<EOF>''', 2513011147))

	def test_2513011148(self):
		self.assertTrue(TestLexer.test("l8Kd@&Cm_", "l8Kd,Error Token @", 2513011148))

	def test_2513011149(self):
		self.assertTrue(TestLexer.test("Q&BFOF", "Q,Error Token &", 2513011149))

	def test_2513011150(self):
		self.assertTrue(TestLexer.test("fNA_JU5R", "fNA_JU5R,<EOF>", 2513011150))

	def test_2513011151(self):
		self.assertTrue(TestLexer.test('''## 1Z0>m"''', '''<EOF>''', 2513011151))

	def test_2513011152(self):
		self.assertTrue(TestLexer.test("3E+48", "3E+48,<EOF>", 2513011152))

	def test_2513011153(self):
		self.assertTrue(TestLexer.test('''"
('"c6"''', '''Unclosed String: ''', 2513011153))

	def test_2513011154(self):
		self.assertTrue(TestLexer.test('''"="''', '''=,<EOF>''', 2513011154))

	def test_2513011155(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011155))

	def test_2513011156(self):
		self.assertTrue(TestLexer.test("50e65", "50e65,<EOF>", 2513011156))

	def test_2513011157(self):
		self.assertTrue(TestLexer.test('''## LPu#1gA''', '''<EOF>''', 2513011157))

	def test_2513011158(self):
		self.assertTrue(TestLexer.test("1.801", "1.801,<EOF>", 2513011158))

	def test_2513011159(self):
		self.assertTrue(TestLexer.test('''"aS ''', '''Unclosed String: aS ''', 2513011159))

	def test_2513011160(self):
		self.assertTrue(TestLexer.test('''"\\y&"''', '''Illegal Escape In String: \\y''', 2513011160))

	def test_2513011161(self):
		self.assertTrue(TestLexer.test('''"\\z'"'"pf'""''', '''Illegal Escape In String: \\z''', 2513011161))

	def test_2513011162(self):
		self.assertTrue(TestLexer.test('''## 1`{''', '''<EOF>''', 2513011162))

	def test_2513011163(self):
		self.assertTrue(TestLexer.test("379E-06", "379E-06,<EOF>", 2513011163))

	def test_2513011164(self):
		self.assertTrue(TestLexer.test("v", "v,<EOF>", 2513011164))

	def test_2513011165(self):
		self.assertTrue(TestLexer.test('''"'"'"'" ''', '''Unclosed String: '"'"'" ''', 2513011165))

	def test_2513011166(self):
		self.assertTrue(TestLexer.test('''## nYM(B|Tk''', '''<EOF>''', 2513011166))

	def test_2513011167(self):
		self.assertTrue(TestLexer.test('''"'"u'"$l"''', '''\'"u'"$l,<EOF>''', 2513011167))

	def test_2513011168(self):
		self.assertTrue(TestLexer.test("746.490e59", "746.490e59,<EOF>", 2513011168))

	def test_2513011169(self):
		self.assertTrue(TestLexer.test("4.413", "4.413,<EOF>", 2513011169))

	def test_2513011170(self):
		self.assertTrue(TestLexer.test("2gst5i", "2,gst5i,<EOF>", 2513011170))

	def test_2513011171(self):
		self.assertTrue(TestLexer.test("150.194", "150.194,<EOF>", 2513011171))

	def test_2513011172(self):
		self.assertTrue(TestLexer.test("64.641", "64.641,<EOF>", 2513011172))

	def test_2513011173(self):
		self.assertTrue(TestLexer.test("54", "54,<EOF>", 2513011173))

	def test_2513011174(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011174))

	def test_2513011175(self):
		self.assertTrue(TestLexer.test("#sznPm#", "Error Token #", 2513011175))

	def test_2513011176(self):
		self.assertTrue(TestLexer.test('''## )|8KVjC?f#Q''', '''<EOF>''', 2513011176))

	def test_2513011177(self):
		self.assertTrue(TestLexer.test('''"'"7\\s'"'"0"''', '''Illegal Escape In String: '"7\\s''', 2513011177))

	def test_2513011178(self):
		self.assertTrue(TestLexer.test('''"
'"'""''', '''Unclosed String: ''', 2513011178))

	def test_2513011179(self):
		self.assertTrue(TestLexer.test('''## %M;bTL,zon["I3.]WxT<''', '''<EOF>''', 2513011179))

	def test_2513011180(self):
		self.assertTrue(TestLexer.test('''## fxVqrl~''', '''<EOF>''', 2513011180))

	def test_2513011181(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011181))

	def test_2513011182(self):
		self.assertTrue(TestLexer.test('''## X''', '''<EOF>''', 2513011182))

	def test_2513011183(self):
		self.assertTrue(TestLexer.test("65.082e69", "65.082e69,<EOF>", 2513011183))

	def test_2513011184(self):
		self.assertTrue(TestLexer.test('''## <IAcyr''', '''<EOF>''', 2513011184))

	def test_2513011185(self):
		self.assertTrue(TestLexer.test('''"\\vE"''', '''Illegal Escape In String: \\v''', 2513011185))

	def test_2513011186(self):
		self.assertTrue(TestLexer.test("459.196E65", "459.196E65,<EOF>", 2513011186))

	def test_2513011187(self):
		self.assertTrue(TestLexer.test("$", "Error Token $", 2513011187))

	def test_2513011188(self):
		self.assertTrue(TestLexer.test('''## bx^EbL''', '''<EOF>''', 2513011188))

	def test_2513011189(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011189))

	def test_2513011190(self):
		self.assertTrue(TestLexer.test('''## ^3yDpp]n0''', '''<EOF>''', 2513011190))

	def test_2513011191(self):
		self.assertTrue(TestLexer.test("bX1t", "bX1t,<EOF>", 2513011191))

	def test_2513011192(self):
		self.assertTrue(TestLexer.test('''## P16UB^5I''', '''<EOF>''', 2513011192))

	def test_2513011193(self):
		self.assertTrue(TestLexer.test('''"'"W'" ''', '''Unclosed String: '"W'" ''', 2513011193))

	def test_2513011194(self):
		self.assertTrue(TestLexer.test("839.075E+00", "839.075E+00,<EOF>", 2513011194))

	def test_2513011195(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 2513011195))

	def test_2513011196(self):
		self.assertTrue(TestLexer.test('''"'"h\\u'"'""''', '''Illegal Escape In String: '"h\\u''', 2513011196))

	def test_2513011197(self):
		self.assertTrue(TestLexer.test("Wt4z$4F", "Wt4z,Error Token $", 2513011197))

	def test_2513011198(self):
		self.assertTrue(TestLexer.test("B^J3zBgN", "B,Error Token ^", 2513011198))

	def test_2513011199(self):
		self.assertTrue(TestLexer.test('''## e;V0eRKXa&#m^OC/''', '''<EOF>''', 2513011199))
