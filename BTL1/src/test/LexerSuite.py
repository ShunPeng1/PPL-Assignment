import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_2513011100(self):
		self.assertTrue(TestLexer.test("L", "L,<EOF>", 2513011100))

	def test_2513011101(self):
		self.assertTrue(TestLexer.test('''## %CEBl85m+5I''', '''<EOF>''', 2513011101))

	def test_2513011102(self):
		self.assertTrue(TestLexer.test('''"Oc ''', '''Unclosed String: Oc ''', 2513011102))

	def test_2513011103(self):
		self.assertTrue(TestLexer.test('''"\\m'""''', '''Illegal Escape In String: \\m''', 2513011103))

	def test_2513011104(self):
		self.assertTrue(TestLexer.test("7.482", "7.482,<EOF>", 2513011104))

	def test_2513011105(self):
		self.assertTrue(TestLexer.test('''"G"''', '''G,<EOF>''', 2513011105))

	def test_2513011106(self):
		self.assertTrue(TestLexer.test("@8@AI", "Error Token @", 2513011106))

	def test_2513011107(self):
		self.assertTrue(TestLexer.test("aQvgPyza", "aQvgPyza,<EOF>", 2513011107))

	def test_2513011108(self):
		self.assertTrue(TestLexer.test("6.439", "6.439,<EOF>", 2513011108))

	def test_2513011109(self):
		self.assertTrue(TestLexer.test("vxVMOpS^Aw", "vxVMOpS,Error Token ^", 2513011109))

	def test_2513011110(self):
		self.assertTrue(TestLexer.test("EYw", "EYw,<EOF>", 2513011110))

	def test_2513011111(self):
		self.assertTrue(TestLexer.test("92.913e+41", "92.913e+41,<EOF>", 2513011111))

	def test_2513011112(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011112))

	def test_2513011113(self):
		self.assertTrue(TestLexer.test('''"w'""''', '''w'",<EOF>''', 2513011113))

	def test_2513011114(self):
		self.assertTrue(TestLexer.test("105.165", "105.165,<EOF>", 2513011114))

	def test_2513011115(self):
		self.assertTrue(TestLexer.test('''## f<A[?Z#|xz{&=+~''', '''<EOF>''', 2513011115))

	def test_2513011116(self):
		self.assertTrue(TestLexer.test("KNQ@D", "KNQ,Error Token @", 2513011116))

	def test_2513011117(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011117))

	def test_2513011118(self):
		self.assertTrue(TestLexer.test("80.158e+31", "80.158e+31,<EOF>", 2513011118))

	def test_2513011119(self):
		self.assertTrue(TestLexer.test("55.053e-90", "55.053e-90,<EOF>", 2513011119))

	def test_2513011120(self):
		self.assertTrue(TestLexer.test('''## gA''', '''<EOF>''', 2513011120))

	def test_2513011121(self):
		self.assertTrue(TestLexer.test('''"'"'"r"''', '''\'"'"r,<EOF>''', 2513011121))

	def test_2513011122(self):
		self.assertTrue(TestLexer.test("^NPZ", "Error Token ^", 2513011122))

	def test_2513011123(self):
		self.assertTrue(TestLexer.test("125e01", "125e01,<EOF>", 2513011123))

	def test_2513011124(self):
		self.assertTrue(TestLexer.test("P", "P,<EOF>", 2513011124))

	def test_2513011125(self):
		self.assertTrue(TestLexer.test("893.829E+24", "893.829E+24,<EOF>", 2513011125))

	def test_2513011126(self):
		self.assertTrue(TestLexer.test("10.906e-81", "10.906e-81,<EOF>", 2513011126))

	def test_2513011127(self):
		self.assertTrue(TestLexer.test("6.463", "6.463,<EOF>", 2513011127))

	def test_2513011128(self):
		self.assertTrue(TestLexer.test('''## wJS"H6]|''', '''<EOF>''', 2513011128))

	def test_2513011129(self):
		self.assertTrue(TestLexer.test('''## GIf^:R.XUJ8%<laDu?AO''', '''<EOF>''', 2513011129))

	def test_2513011130(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011130))

	def test_2513011131(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 2513011131))

	def test_2513011132(self):
		self.assertTrue(TestLexer.test('''"\\y'""''', '''Illegal Escape In String: \\y''', 2513011132))

	def test_2513011133(self):
		self.assertTrue(TestLexer.test('''"\\z'""''', '''Illegal Escape In String: \\z''', 2513011133))

	def test_2513011134(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011134))

	def test_2513011135(self):
		self.assertTrue(TestLexer.test('''## .aQ!t''', '''<EOF>''', 2513011135))

	def test_2513011136(self):
		self.assertTrue(TestLexer.test("#H", "Error Token #", 2513011136))

	def test_2513011137(self):
		self.assertTrue(TestLexer.test("WJP", "WJP,<EOF>", 2513011137))

	def test_2513011138(self):
		self.assertTrue(TestLexer.test("l0&Rp", "l0,Error Token &", 2513011138))

	def test_2513011139(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011139))

	def test_2513011140(self):
		self.assertTrue(TestLexer.test('''"'"'"'"'""''', '''\'"'"'"'",<EOF>''', 2513011140))

	def test_2513011141(self):
		self.assertTrue(TestLexer.test('''## mM''', '''<EOF>''', 2513011141))

	def test_2513011142(self):
		self.assertTrue(TestLexer.test('''"	4vL'""''', '''	4vL'",<EOF>''', 2513011142))

	def test_2513011143(self):
		self.assertTrue(TestLexer.test('''## o*>NN^w]Lzo#''', '''<EOF>''', 2513011143))

	def test_2513011144(self):
		self.assertTrue(TestLexer.test('''## <LA:}si''', '''<EOF>''', 2513011144))

	def test_2513011145(self):
		self.assertTrue(TestLexer.test("267&bQlJV", "267,Error Token &", 2513011145))

	def test_2513011146(self):
		self.assertTrue(TestLexer.test('''## g#Xy69r''', '''<EOF>''', 2513011146))

	def test_2513011147(self):
		self.assertTrue(TestLexer.test("6.032", "6.032,<EOF>", 2513011147))

	def test_2513011148(self):
		self.assertTrue(TestLexer.test("95.034", "95.034,<EOF>", 2513011148))

	def test_2513011149(self):
		self.assertTrue(TestLexer.test("27.069E88", "27.069E88,<EOF>", 2513011149))

	def test_2513011150(self):
		self.assertTrue(TestLexer.test("45.248", "45.248,<EOF>", 2513011150))

	def test_2513011151(self):
		self.assertTrue(TestLexer.test('''## >`''', '''<EOF>''', 2513011151))

	def test_2513011152(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011152))

	def test_2513011153(self):
		self.assertTrue(TestLexer.test('''## WN$"ipIH:uo[YQs''', '''<EOF>''', 2513011153))

	def test_2513011154(self):
		self.assertTrue(TestLexer.test("5BtVsMYvs", "5,BtVsMYvs,<EOF>", 2513011154))

	def test_2513011155(self):
		self.assertTrue(TestLexer.test('''## z<K-H''', '''<EOF>''', 2513011155))

	def test_2513011156(self):
		self.assertTrue(TestLexer.test("143", "143,<EOF>", 2513011156))

	def test_2513011157(self):
		self.assertTrue(TestLexer.test('''## ,''', '''<EOF>''', 2513011157))

	def test_2513011158(self):
		self.assertTrue(TestLexer.test("56e+55", "56e+55,<EOF>", 2513011158))

	def test_2513011159(self):
		self.assertTrue(TestLexer.test('''## {t1_YNdj#t% cV](^=~w''', '''<EOF>''', 2513011159))

	def test_2513011160(self):
		self.assertTrue(TestLexer.test('''## .>Gf!pD&>`ZuZlt~bP7''', '''<EOF>''', 2513011160))

	def test_2513011161(self):
		self.assertTrue(TestLexer.test("4o3fYu", "4,o3fYu,<EOF>", 2513011161))

	def test_2513011162(self):
		self.assertTrue(TestLexer.test('''## ;KL=9q`]Cp r:''', '''<EOF>''', 2513011162))

	def test_2513011163(self):
		self.assertTrue(TestLexer.test('''"\\u'"+5'"'""''', '''Illegal Escape In String: \\u''', 2513011163))

	def test_2513011164(self):
		self.assertTrue(TestLexer.test('''"c\\w'"K"''', '''Illegal Escape In String: c\\w''', 2513011164))

	def test_2513011165(self):
		self.assertTrue(TestLexer.test("4s", "4,s,<EOF>", 2513011165))

	def test_2513011166(self):
		self.assertTrue(TestLexer.test('''")\\p'"'"a"''', '''Illegal Escape In String: )\\p''', 2513011166))

	def test_2513011167(self):
		self.assertTrue(TestLexer.test('''"
q'""''', '''Unclosed String: ''', 2513011167))

	def test_2513011168(self):
		self.assertTrue(TestLexer.test("5.202e+38", "5.202e+38,<EOF>", 2513011168))

	def test_2513011169(self):
		self.assertTrue(TestLexer.test("6j$", "6,j,Error Token $", 2513011169))

	def test_2513011170(self):
		self.assertTrue(TestLexer.test('''##  wS5A&Ht%XManAji/2K,''', '''<EOF>''', 2513011170))

	def test_2513011171(self):
		self.assertTrue(TestLexer.test("eXcbu3", "eXcbu3,<EOF>", 2513011171))

	def test_2513011172(self):
		self.assertTrue(TestLexer.test('''"'"Y'"\\du'""''', '''Illegal Escape In String: '"Y'"\\d''', 2513011172))

	def test_2513011173(self):
		self.assertTrue(TestLexer.test('''## o"<;%,2+I_{sPn5''', '''<EOF>''', 2513011173))

	def test_2513011174(self):
		self.assertTrue(TestLexer.test('''"'"\\o'""''', '''Illegal Escape In String: '"\\o''', 2513011174))

	def test_2513011175(self):
		self.assertTrue(TestLexer.test('''"|gX8"''', '''|gX8,<EOF>''', 2513011175))

	def test_2513011176(self):
		self.assertTrue(TestLexer.test('''## woi3j,X9uEh(n''', '''<EOF>''', 2513011176))

	def test_2513011177(self):
		self.assertTrue(TestLexer.test("fbx", "fbx,<EOF>", 2513011177))

	def test_2513011178(self):
		self.assertTrue(TestLexer.test('''## lG-5dpWU''', '''<EOF>''', 2513011178))

	def test_2513011179(self):
		self.assertTrue(TestLexer.test("9.419e+30", "9.419e+30,<EOF>", 2513011179))

	def test_2513011180(self):
		self.assertTrue(TestLexer.test("36.916E+82", "36.916E+82,<EOF>", 2513011180))

	def test_2513011181(self):
		self.assertTrue(TestLexer.test('''## YX#TfDF>Ynjd!u2B''', '''<EOF>''', 2513011181))

	def test_2513011182(self):
		self.assertTrue(TestLexer.test('''"QuT'""''', '''QuT'",<EOF>''', 2513011182))

	def test_2513011183(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 2513011183))

	def test_2513011184(self):
		self.assertTrue(TestLexer.test('''"'"'"2'""''', '''\'"'"2'",<EOF>''', 2513011184))

	def test_2513011185(self):
		self.assertTrue(TestLexer.test('''## [.mvIiO3=%)P08tbKVF''', '''<EOF>''', 2513011185))

	def test_2513011186(self):
		self.assertTrue(TestLexer.test('''## WW_+1Sf>''', '''<EOF>''', 2513011186))

	def test_2513011187(self):
		self.assertTrue(TestLexer.test('''"'"'"
'"'""''', '''Unclosed String: '"'"''', 2513011187))

	def test_2513011188(self):
		self.assertTrue(TestLexer.test("864.679", "864.679,<EOF>", 2513011188))

	def test_2513011189(self):
		self.assertTrue(TestLexer.test('''"'"
'"E
"''', '''Unclosed String: '"''', 2513011189))

	def test_2513011190(self):
		self.assertTrue(TestLexer.test("#A_FRp", "Error Token #", 2513011190))

	def test_2513011191(self):
		self.assertTrue(TestLexer.test('''"f'" ''', '''Unclosed String: f'" ''', 2513011191))

	def test_2513011192(self):
		self.assertTrue(TestLexer.test('''"\\j'""''', '''Illegal Escape In String: \\j''', 2513011192))

	def test_2513011193(self):
		self.assertTrue(TestLexer.test('''## xBK{RF?g&9q9}3bU''', '''<EOF>''', 2513011193))

	def test_2513011194(self):
		self.assertTrue(TestLexer.test("62.505e56", "62.505e56,<EOF>", 2513011194))

	def test_2513011195(self):
		self.assertTrue(TestLexer.test('''"'"qN'"'" ''', '''Unclosed String: '"qN'"'" ''', 2513011195))

	def test_2513011196(self):
		self.assertTrue(TestLexer.test("JAc_PK", "JAc_PK,<EOF>", 2513011196))

	def test_2513011197(self):
		self.assertTrue(TestLexer.test('''"'"'"'""''', '''\'"'"'",<EOF>''', 2513011197))

	def test_2513011198(self):
		self.assertTrue(TestLexer.test("8.919", "8.919,<EOF>", 2513011198))

	def test_2513011199(self):
		self.assertTrue(TestLexer.test('''## krVzaG`OJp;~''', '''<EOF>''', 2513011199))
