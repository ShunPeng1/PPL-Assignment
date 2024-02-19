import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_2513011100(self):
		self.assertTrue(TestLexer.test('''"\\w`'"1B"''', '''Illegal Escape In String: \\w''', 2513011100))

	def test_2513011101(self):
		self.assertTrue(TestLexer.test('''## nLvNM?>b''', '''<EOF>''', 2513011101))

	def test_2513011102(self):
		self.assertTrue(TestLexer.test('''"w ''', '''Unclosed String: w ''', 2513011102))

	def test_2513011103(self):
		self.assertTrue(TestLexer.test("278.162", "278.162,<EOF>", 2513011103))

	def test_2513011104(self):
		self.assertTrue(TestLexer.test('''## }?g2iC~vH@GpppM^"''', '''<EOF>''', 2513011104))

	def test_2513011105(self):
		self.assertTrue(TestLexer.test("7.362E+38", "7.362E+38,<EOF>", 2513011105))

	def test_2513011106(self):
		self.assertTrue(TestLexer.test('''## u4W/wT*@5KYB`a3''', '''<EOF>''', 2513011106))

	def test_2513011107(self):
		self.assertTrue(TestLexer.test('''"S/K"''', '''S/K,<EOF>''', 2513011107))

	def test_2513011108(self):
		self.assertTrue(TestLexer.test("DuxWCXp$Up", "DuxWCXp,Error Token $", 2513011108))

	def test_2513011109(self):
		self.assertTrue(TestLexer.test("u", "u,<EOF>", 2513011109))

	def test_2513011110(self):
		self.assertTrue(TestLexer.test('''## HSsO!~t$Eh''', '''<EOF>''', 2513011110))

	def test_2513011111(self):
		self.assertTrue(TestLexer.test("U4f2agU", "U4f2agU,<EOF>", 2513011111))

	def test_2513011112(self):
		self.assertTrue(TestLexer.test('''"'"'"C'"'" ''', '''Unclosed String: '"'"C'"'" ''', 2513011112))

	def test_2513011113(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 2513011113))

	def test_2513011114(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 2513011114))

	def test_2513011115(self):
		self.assertTrue(TestLexer.test("6.772E+99", "6.772E+99,<EOF>", 2513011115))

	def test_2513011116(self):
		self.assertTrue(TestLexer.test("595e+38", "595e+38,<EOF>", 2513011116))

	def test_2513011117(self):
		self.assertTrue(TestLexer.test("554.573", "554.573,<EOF>", 2513011117))

	def test_2513011118(self):
		self.assertTrue(TestLexer.test('''## fO5|oQ|j|5ZWP%E>pK9@''', '''<EOF>''', 2513011118))

	def test_2513011119(self):
		self.assertTrue(TestLexer.test("##YI6jBT4", "<EOF>", 2513011119))

	def test_2513011120(self):
		self.assertTrue(TestLexer.test('''## %<DEq(#/L~G.FFc''', '''<EOF>''', 2513011120))

	def test_2513011121(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011121))

	def test_2513011122(self):
		self.assertTrue(TestLexer.test("991", "991,<EOF>", 2513011122))

	def test_2513011123(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 2513011123))

	def test_2513011124(self):
		self.assertTrue(TestLexer.test("Z6$z&i_UlF", "Z6,Error Token $", 2513011124))

	def test_2513011125(self):
		self.assertTrue(TestLexer.test('''"/:'"'"b"''', '''/:'"'"b,<EOF>''', 2513011125))

	def test_2513011126(self):
		self.assertTrue(TestLexer.test('''## !ZRA2#tUEn@Yu7o''', '''<EOF>''', 2513011126))

	def test_2513011127(self):
		self.assertTrue(TestLexer.test("w6C#yYqe", "w6C,Error Token #", 2513011127))

	def test_2513011128(self):
		self.assertTrue(TestLexer.test("644.622e09", "644.622e09,<EOF>", 2513011128))

	def test_2513011129(self):
		self.assertTrue(TestLexer.test('''## OmV/z''', '''<EOF>''', 2513011129))

	def test_2513011130(self):
		self.assertTrue(TestLexer.test('''## HnvlPI<._Y!m,Qfk''', '''<EOF>''', 2513011130))

	def test_2513011131(self):
		self.assertTrue(TestLexer.test("#1_NC4", "Error Token #", 2513011131))

	def test_2513011132(self):
		self.assertTrue(TestLexer.test("4.107", "4.107,<EOF>", 2513011132))

	def test_2513011133(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 2513011133))

	def test_2513011134(self):
		self.assertTrue(TestLexer.test("453", "453,<EOF>", 2513011134))

	def test_2513011135(self):
		self.assertTrue(TestLexer.test("72", "72,<EOF>", 2513011135))

	def test_2513011136(self):
		self.assertTrue(TestLexer.test('''## B_w*eTo!&Rd*gp!ZSa''', '''<EOF>''', 2513011136))

	def test_2513011137(self):
		self.assertTrue(TestLexer.test("a9", "a9,<EOF>", 2513011137))

	def test_2513011138(self):
		self.assertTrue(TestLexer.test("by", "by,<EOF>", 2513011138))

	def test_2513011139(self):
		self.assertTrue(TestLexer.test('''"
M"''', '''Unclosed String: ''', 2513011139))

	def test_2513011140(self):
		self.assertTrue(TestLexer.test("44.103", "44.103,<EOF>", 2513011140))

	def test_2513011141(self):
		self.assertTrue(TestLexer.test("86", "86,<EOF>", 2513011141))

	def test_2513011142(self):
		self.assertTrue(TestLexer.test('''## |/2/{7j)ojQW''', '''<EOF>''', 2513011142))

	def test_2513011143(self):
		self.assertTrue(TestLexer.test('''## {]''', '''<EOF>''', 2513011143))

	def test_2513011144(self):
		self.assertTrue(TestLexer.test("cMvz", "cMvz,<EOF>", 2513011144))

	def test_2513011145(self):
		self.assertTrue(TestLexer.test('''"'"z'"'""''', '''\'"z'"'",<EOF>''', 2513011145))

	def test_2513011146(self):
		self.assertTrue(TestLexer.test('''"m'""''', '''m'",<EOF>''', 2513011146))

	def test_2513011147(self):
		self.assertTrue(TestLexer.test("plfghPo", "plfghPo,<EOF>", 2513011147))

	def test_2513011148(self):
		self.assertTrue(TestLexer.test("D3W0lPk", "D3W0lPk,<EOF>", 2513011148))

	def test_2513011149(self):
		self.assertTrue(TestLexer.test('''## A;Bo,eiu''', '''<EOF>''', 2513011149))

	def test_2513011150(self):
		self.assertTrue(TestLexer.test("AuNNk^C$9C", "AuNNk,Error Token ^", 2513011150))

	def test_2513011151(self):
		self.assertTrue(TestLexer.test("JL&K#s2", "JL,Error Token &", 2513011151))

	def test_2513011152(self):
		self.assertTrue(TestLexer.test('''## 9bP_b5O''', '''<EOF>''', 2513011152))

	def test_2513011153(self):
		self.assertTrue(TestLexer.test("8.744", "8.744,<EOF>", 2513011153))

	def test_2513011154(self):
		self.assertTrue(TestLexer.test("0.077", "0.077,<EOF>", 2513011154))

	def test_2513011155(self):
		self.assertTrue(TestLexer.test('''## :H*4n<N}t>''', '''<EOF>''', 2513011155))

	def test_2513011156(self):
		self.assertTrue(TestLexer.test("294", "294,<EOF>", 2513011156))

	def test_2513011157(self):
		self.assertTrue(TestLexer.test('''## 7v$1EFEH[/FO;''', '''<EOF>''', 2513011157))

	def test_2513011158(self):
		self.assertTrue(TestLexer.test("cgX", "cgX,<EOF>", 2513011158))

	def test_2513011159(self):
		self.assertTrue(TestLexer.test("5", "5,<EOF>", 2513011159))

	def test_2513011160(self):
		self.assertTrue(TestLexer.test("13", "13,<EOF>", 2513011160))

	def test_2513011161(self):
		self.assertTrue(TestLexer.test("AfW", "AfW,<EOF>", 2513011161))

	def test_2513011162(self):
		self.assertTrue(TestLexer.test("4.010E+37", "4.010E+37,<EOF>", 2513011162))

	def test_2513011163(self):
		self.assertTrue(TestLexer.test('''## &IRX}r2b!TzW''', '''<EOF>''', 2513011163))

	def test_2513011164(self):
		self.assertTrue(TestLexer.test('''## :qInZpq>nq{X}R''', '''<EOF>''', 2513011164))

	def test_2513011165(self):
		self.assertTrue(TestLexer.test("111E58", "111E58,<EOF>", 2513011165))

	def test_2513011166(self):
		self.assertTrue(TestLexer.test('''## !idm!R,lP>q^''', '''<EOF>''', 2513011166))

	def test_2513011167(self):
		self.assertTrue(TestLexer.test('''"'"K\\gE"''', '''Illegal Escape In String: '"K\\g''', 2513011167))

	def test_2513011168(self):
		self.assertTrue(TestLexer.test('''## 1A-F9z"i''', '''<EOF>''', 2513011168))

	def test_2513011169(self):
		self.assertTrue(TestLexer.test("AhDFd", "AhDFd,<EOF>", 2513011169))

	def test_2513011170(self):
		self.assertTrue(TestLexer.test("5wju$QAj", "5,wju,Error Token $", 2513011170))

	def test_2513011171(self):
		self.assertTrue(TestLexer.test("600.204e+09", "600.204e+09,<EOF>", 2513011171))

	def test_2513011172(self):
		self.assertTrue(TestLexer.test("hsWneLSShY", "hsWneLSShY,<EOF>", 2513011172))

	def test_2513011173(self):
		self.assertTrue(TestLexer.test('''## {R9O"m>14s''', '''<EOF>''', 2513011173))

	def test_2513011174(self):
		self.assertTrue(TestLexer.test("75.265E-70", "75.265E-70,<EOF>", 2513011174))

	def test_2513011175(self):
		self.assertTrue(TestLexer.test('''## /8pJ07TbOPl''', '''<EOF>''', 2513011175))

	def test_2513011176(self):
		self.assertTrue(TestLexer.test('''## <to`&.@i~fu]Zv8DMsHb''', '''<EOF>''', 2513011176))

	def test_2513011177(self):
		self.assertTrue(TestLexer.test("hg1TMKnYwL", "hg1TMKnYwL,<EOF>", 2513011177))

	def test_2513011178(self):
		self.assertTrue(TestLexer.test("l6z9n", "l6z9n,<EOF>", 2513011178))

	def test_2513011179(self):
		self.assertTrue(TestLexer.test("mg", "mg,<EOF>", 2513011179))

	def test_2513011180(self):
		self.assertTrue(TestLexer.test("586", "586,<EOF>", 2513011180))

	def test_2513011181(self):
		self.assertTrue(TestLexer.test('''"2'"'"'""''', '''2'"'"'",<EOF>''', 2513011181))

	def test_2513011182(self):
		self.assertTrue(TestLexer.test('''## %{Mi|$NvNz>LSp<dMQ''', '''<EOF>''', 2513011182))

	def test_2513011183(self):
		self.assertTrue(TestLexer.test('''## 1UF`.fGK''', '''<EOF>''', 2513011183))

	def test_2513011184(self):
		self.assertTrue(TestLexer.test('''## YO27;ne8z`/ljTmEb''', '''<EOF>''', 2513011184))

	def test_2513011185(self):
		self.assertTrue(TestLexer.test('''## 1a##yf''', '''<EOF>''', 2513011185))

	def test_2513011186(self):
		self.assertTrue(TestLexer.test("8E-49", "8E-49,<EOF>", 2513011186))

	def test_2513011187(self):
		self.assertTrue(TestLexer.test('''## :D OZW@]C]JL-_V7<Ty8''', '''<EOF>''', 2513011187))

	def test_2513011188(self):
		self.assertTrue(TestLexer.test("77j", "77,j,<EOF>", 2513011188))

	def test_2513011189(self):
		self.assertTrue(TestLexer.test('''"'".SG"''', '''\'".SG,<EOF>''', 2513011189))

	def test_2513011190(self):
		self.assertTrue(TestLexer.test('''## Z?.Bih''', '''<EOF>''', 2513011190))

	def test_2513011191(self):
		self.assertTrue(TestLexer.test("645.692", "645.692,<EOF>", 2513011191))

	def test_2513011192(self):
		self.assertTrue(TestLexer.test("XIRC$", "XIRC,Error Token $", 2513011192))

	def test_2513011193(self):
		self.assertTrue(TestLexer.test("29e+25", "29e+25,<EOF>", 2513011193))

	def test_2513011194(self):
		self.assertTrue(TestLexer.test("146.778", "146.778,<EOF>", 2513011194))

	def test_2513011195(self):
		self.assertTrue(TestLexer.test('''## L1`"u5,"Wax}P(sCtG''', '''<EOF>''', 2513011195))

	def test_2513011196(self):
		self.assertTrue(TestLexer.test("678.958E-88", "678.958E-88,<EOF>", 2513011196))

	def test_2513011197(self):
		self.assertTrue(TestLexer.test('''"\\k'""''', '''Illegal Escape In String: \\k''', 2513011197))

	def test_2513011198(self):
		self.assertTrue(TestLexer.test('''## !QL,?$r><F<^$anfBc''', '''<EOF>''', 2513011198))

	def test_2513011199(self):
		self.assertTrue(TestLexer.test('''## $!JW:9na`D6DfYHD]A''', '''<EOF>''', 2513011199))
