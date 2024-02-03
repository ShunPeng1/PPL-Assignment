import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_2513011100(self):
		self.assertTrue(TestLexer.test('''## m<(mQF]XzeXU''', '''<EOF>''', 2513011100))

	def test_2513011101(self):
		self.assertTrue(TestLexer.test('''"'"h"''', '''\'"h,<EOF>''', 2513011101))

	def test_2513011102(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 2513011102))

	def test_2513011103(self):
		self.assertTrue(TestLexer.test("0C2DDRaGH", "0,C2DDRaGH,<EOF>", 2513011103))

	def test_2513011104(self):
		self.assertTrue(TestLexer.test('''## Cbt''', '''<EOF>''', 2513011104))

	def test_2513011105(self):
		self.assertTrue(TestLexer.test('''## )4Ig''', '''<EOF>''', 2513011105))

	def test_2513011106(self):
		self.assertTrue(TestLexer.test("_5^WPhT", "_5,Error Token ^", 2513011106))

	def test_2513011107(self):
		self.assertTrue(TestLexer.test("9.408", "9.408,<EOF>", 2513011107))

	def test_2513011108(self):
		self.assertTrue(TestLexer.test('''"'"\\h."''', '''Illegal Escape In String: '"\\h''', 2513011108))

	def test_2513011109(self):
		self.assertTrue(TestLexer.test("7", "7,<EOF>", 2513011109))

	def test_2513011110(self):
		self.assertTrue(TestLexer.test('''## OC;Jd`P^''', '''<EOF>''', 2513011110))

	def test_2513011111(self):
		self.assertTrue(TestLexer.test('''## 0s5_yJ=XA{Pd''', '''<EOF>''', 2513011111))

	def test_2513011112(self):
		self.assertTrue(TestLexer.test('''## `zW>TRO''', '''<EOF>''', 2513011112))

	def test_2513011113(self):
		self.assertTrue(TestLexer.test("54", "54,<EOF>", 2513011113))

	def test_2513011114(self):
		self.assertTrue(TestLexer.test('''"fn'"'""''', '''fn'"'",<EOF>''', 2513011114))

	def test_2513011115(self):
		self.assertTrue(TestLexer.test('''"P'"'"~ ''', '''Unclosed String: P'"'"~ ''', 2513011115))

	def test_2513011116(self):
		self.assertTrue(TestLexer.test('''## (~V/E''', '''<EOF>''', 2513011116))

	def test_2513011117(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 2513011117))

	def test_2513011118(self):
		self.assertTrue(TestLexer.test("24", "24,<EOF>", 2513011118))

	def test_2513011119(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011119))

	def test_2513011120(self):
		self.assertTrue(TestLexer.test('''## shm|Xb''', '''<EOF>''', 2513011120))

	def test_2513011121(self):
		self.assertTrue(TestLexer.test("4.806E+05", "4.806E+05,<EOF>", 2513011121))

	def test_2513011122(self):
		self.assertTrue(TestLexer.test('''"'"F"''', '''\'"F,<EOF>''', 2513011122))

	def test_2513011123(self):
		self.assertTrue(TestLexer.test("5E-94", "5E-94,<EOF>", 2513011123))

	def test_2513011124(self):
		self.assertTrue(TestLexer.test("z", "z,<EOF>", 2513011124))

	def test_2513011125(self):
		self.assertTrue(TestLexer.test('''"m}"''', '''m},<EOF>''', 2513011125))

	def test_2513011126(self):
		self.assertTrue(TestLexer.test('''## q''', '''<EOF>''', 2513011126))

	def test_2513011127(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 2513011127))

	def test_2513011128(self):
		self.assertTrue(TestLexer.test('''"
D"''', '''Unclosed String: ''', 2513011128))

	def test_2513011129(self):
		self.assertTrue(TestLexer.test('''## m''', '''<EOF>''', 2513011129))

	def test_2513011130(self):
		self.assertTrue(TestLexer.test("9", "9,<EOF>", 2513011130))

	def test_2513011131(self):
		self.assertTrue(TestLexer.test("207.919", "207.919,<EOF>", 2513011131))

	def test_2513011132(self):
		self.assertTrue(TestLexer.test("V9Kc05Hj", "V9Kc05Hj,<EOF>", 2513011132))

	def test_2513011133(self):
		self.assertTrue(TestLexer.test("bZKSfpdupX", "bZKSfpdupX,<EOF>", 2513011133))

	def test_2513011134(self):
		self.assertTrue(TestLexer.test('''## z.->#cU''', '''<EOF>''', 2513011134))

	def test_2513011135(self):
		self.assertTrue(TestLexer.test('''## 51ft](=F''', '''<EOF>''', 2513011135))

	def test_2513011136(self):
		self.assertTrue(TestLexer.test('''## 8]ZfF-gII/&''', '''<EOF>''', 2513011136))

	def test_2513011137(self):
		self.assertTrue(TestLexer.test('''"e|TU%"''', '''e|TU%,<EOF>''', 2513011137))

	def test_2513011138(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 2513011138))

	def test_2513011139(self):
		self.assertTrue(TestLexer.test('''## @Cp''', '''<EOF>''', 2513011139))

	def test_2513011140(self):
		self.assertTrue(TestLexer.test('''## u+;c6HD}-/~N:x''', '''<EOF>''', 2513011140))

	def test_2513011141(self):
		self.assertTrue(TestLexer.test("0.530e-92", "0.530e-92,<EOF>", 2513011141))

	def test_2513011142(self):
		self.assertTrue(TestLexer.test("4#q@XO", "4,Error Token #", 2513011142))

	def test_2513011143(self):
		self.assertTrue(TestLexer.test("tt5LhOLM", "tt5LhOLM,<EOF>", 2513011143))

	def test_2513011144(self):
		self.assertTrue(TestLexer.test("j9", "j9,<EOF>", 2513011144))

	def test_2513011145(self):
		self.assertTrue(TestLexer.test("C2Y", "C2Y,<EOF>", 2513011145))

	def test_2513011146(self):
		self.assertTrue(TestLexer.test("CvRAhs6a", "CvRAhs6a,<EOF>", 2513011146))

	def test_2513011147(self):
		self.assertTrue(TestLexer.test('''"\\l'""''', '''Illegal Escape In String: \\l''', 2513011147))

	def test_2513011148(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011148))

	def test_2513011149(self):
		self.assertTrue(TestLexer.test('''"w ''', '''Unclosed String: w ''', 2513011149))

	def test_2513011150(self):
		self.assertTrue(TestLexer.test('''## ~g)`^}f 5ACHd''', '''<EOF>''', 2513011150))

	def test_2513011151(self):
		self.assertTrue(TestLexer.test("QndfRnLku_", "QndfRnLku_,<EOF>", 2513011151))

	def test_2513011152(self):
		self.assertTrue(TestLexer.test('''"P'"c'" ''', '''Unclosed String: P'"c'" ''', 2513011152))

	def test_2513011153(self):
		self.assertTrue(TestLexer.test('''## Pct[''', '''<EOF>''', 2513011153))

	def test_2513011154(self):
		self.assertTrue(TestLexer.test("Lhp0I", "Lhp0I,<EOF>", 2513011154))

	def test_2513011155(self):
		self.assertTrue(TestLexer.test('''## u2O0xHHPuNmFcd''', '''<EOF>''', 2513011155))

	def test_2513011156(self):
		self.assertTrue(TestLexer.test('''"'"s'"'"
)"''', '''Unclosed String: '"s'"'"''', 2513011156))

	def test_2513011157(self):
		self.assertTrue(TestLexer.test("pOlQuj", "pOlQuj,<EOF>", 2513011157))

	def test_2513011158(self):
		self.assertTrue(TestLexer.test("a", "a,<EOF>", 2513011158))

	def test_2513011159(self):
		self.assertTrue(TestLexer.test("1.675", "1.675,<EOF>", 2513011159))

	def test_2513011160(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 2513011160))

	def test_2513011161(self):
		self.assertTrue(TestLexer.test('''## Zo88m;RHd~XT|.9S`:=,''', '''<EOF>''', 2513011161))

	def test_2513011162(self):
		self.assertTrue(TestLexer.test('''## ;qx;46Y3.''', '''<EOF>''', 2513011162))

	def test_2513011163(self):
		self.assertTrue(TestLexer.test("YpVvuF", "YpVvuF,<EOF>", 2513011163))

	def test_2513011164(self):
		self.assertTrue(TestLexer.test('''"(
0"''', '''Unclosed String: (''', 2513011164))

	def test_2513011165(self):
		self.assertTrue(TestLexer.test("V4cs", "V4cs,<EOF>", 2513011165))

	def test_2513011166(self):
		self.assertTrue(TestLexer.test('''"TW,7'" ''', '''Unclosed String: TW,7'" ''', 2513011166))

	def test_2513011167(self):
		self.assertTrue(TestLexer.test("92.633", "92.633,<EOF>", 2513011167))

	def test_2513011168(self):
		self.assertTrue(TestLexer.test('''"<\\e'""''', '''Illegal Escape In String: <\\e''', 2513011168))

	def test_2513011169(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011169))

	def test_2513011170(self):
		self.assertTrue(TestLexer.test("Zer2pxw", "Zer2pxw,<EOF>", 2513011170))

	def test_2513011171(self):
		self.assertTrue(TestLexer.test("B0ekbX", "B0ekbX,<EOF>", 2513011171))

	def test_2513011172(self):
		self.assertTrue(TestLexer.test('''## xV''', '''<EOF>''', 2513011172))

	def test_2513011173(self):
		self.assertTrue(TestLexer.test("IM", "IM,<EOF>", 2513011173))

	def test_2513011174(self):
		self.assertTrue(TestLexer.test("1", "1,<EOF>", 2513011174))

	def test_2513011175(self):
		self.assertTrue(TestLexer.test("A", "A,<EOF>", 2513011175))

	def test_2513011176(self):
		self.assertTrue(TestLexer.test("43", "43,<EOF>", 2513011176))

	def test_2513011177(self):
		self.assertTrue(TestLexer.test('''"'"'"
_v'""''', '''Unclosed String: '"'"''', 2513011177))

	def test_2513011178(self):
		self.assertTrue(TestLexer.test("0.924", "0.924,<EOF>", 2513011178))

	def test_2513011179(self):
		self.assertTrue(TestLexer.test("68", "68,<EOF>", 2513011179))

	def test_2513011180(self):
		self.assertTrue(TestLexer.test('''"r'"'"'""''', '''r'"'"'",<EOF>''', 2513011180))

	def test_2513011181(self):
		self.assertTrue(TestLexer.test('''## E{d(n(6PTHh$HD&''', '''<EOF>''', 2513011181))

	def test_2513011182(self):
		self.assertTrue(TestLexer.test("L9cC@", "L9cC,Error Token @", 2513011182))

	def test_2513011183(self):
		self.assertTrue(TestLexer.test("59.711e-90", "59.711e-90,<EOF>", 2513011183))

	def test_2513011184(self):
		self.assertTrue(TestLexer.test('''## vWQ;^M!lNbe5Q})-w''', '''<EOF>''', 2513011184))

	def test_2513011185(self):
		self.assertTrue(TestLexer.test('''"'"O\\i'"'"U"''', '''Illegal Escape In String: '"O\\i''', 2513011185))

	def test_2513011186(self):
		self.assertTrue(TestLexer.test('''## S5y&(*C5%''', '''<EOF>''', 2513011186))

	def test_2513011187(self):
		self.assertTrue(TestLexer.test('''">'""''', '''>'",<EOF>''', 2513011187))

	def test_2513011188(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''Unclosed String: '" ''', 2513011188))

	def test_2513011189(self):
		self.assertTrue(TestLexer.test("cVqEt_", "cVqEt_,<EOF>", 2513011189))

	def test_2513011190(self):
		self.assertTrue(TestLexer.test('''"'"tw ''', '''Unclosed String: '"tw ''', 2513011190))

	def test_2513011191(self):
		self.assertTrue(TestLexer.test("K", "K,<EOF>", 2513011191))

	def test_2513011192(self):
		self.assertTrue(TestLexer.test('''## <P/y/Yo1<)B;M]mjEywv''', '''<EOF>''', 2513011192))

	def test_2513011193(self):
		self.assertTrue(TestLexer.test("Ggv", "Ggv,<EOF>", 2513011193))

	def test_2513011194(self):
		self.assertTrue(TestLexer.test("HMQr60v9HO", "HMQr60v9HO,<EOF>", 2513011194))

	def test_2513011195(self):
		self.assertTrue(TestLexer.test('''"%
'""''', '''Unclosed String: %''', 2513011195))

	def test_2513011196(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 2513011196))

	def test_2513011197(self):
		self.assertTrue(TestLexer.test('''"\\pY"''', '''Illegal Escape In String: \\p''', 2513011197))

	def test_2513011198(self):
		self.assertTrue(TestLexer.test('''"'">s
1"''', '''Unclosed String: '">s''', 2513011198))

	def test_2513011199(self):
		self.assertTrue(TestLexer.test('''## qr+wGP/(|%;LaSZcj''', '''<EOF>''', 2513011199))
