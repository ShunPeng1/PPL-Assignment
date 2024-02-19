import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
	def test_21530115000(self):
		input = '''
func km0 (bool xp, number XZt[7.84,28.98,97.22], number EJX[27.22])	return [not sNj_("RcP", "i", "COEkI") * Sw]

func kVRW ()	return
number crI <- 4.48
number Ej[56.18,11.03]
number WJ8[63.4,86.75,69.43]
'''
		expect = '''Program([FuncDecl(Id(km0), [VarDecl(Id(xp), BoolType, None, None), VarDecl(Id(XZt), ArrayType([7.84, 28.98, 97.22], NumberType), None, None), VarDecl(Id(EJX), ArrayType([27.22], NumberType), None, None)], Return(ArrayLit(BinaryOp(*, UnaryOp(not, CallExpr(Id(sNj_), [StringLit(RcP), StringLit(i), StringLit(COEkI)])), Id(Sw))))), FuncDecl(Id(kVRW), [], Return()), VarDecl(Id(crI), NumberType, None, NumLit(4.48)), VarDecl(Id(Ej), ArrayType([56.18, 11.03], NumberType), None, None), VarDecl(Id(WJ8), ArrayType([63.4, 86.75, 69.43], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115000))

	def test_21530115001(self):
		input = '''
func YO (number HM[97.12])
	return
bool Y51b <- 6.34
'''
		expect = '''Program([FuncDecl(Id(YO), [VarDecl(Id(HM), ArrayType([97.12], NumberType), None, None)], Return()), VarDecl(Id(Y51b), BoolType, None, NumLit(6.34))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115001))

	def test_21530115002(self):
		input = '''
bool e87l
'''
		expect = '''Program([VarDecl(Id(e87l), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115002))

	def test_21530115003(self):
		input = '''
func Zhc (string kW[64.29,63.73,23.48], number NP[86.95,52.05,52.14])
	begin
		return 51.82
		HhB[shJy, 46.78, true] <- true
		number WjN[43.74]
	end

string egcG[73.73,77.84] <- 9.48
var S4 <- false
'''
		expect = '''Program([FuncDecl(Id(Zhc), [VarDecl(Id(kW), ArrayType([64.29, 63.73, 23.48], StringType), None, None), VarDecl(Id(NP), ArrayType([86.95, 52.05, 52.14], NumberType), None, None)], Block([Return(NumLit(51.82)), AssignStmt(ArrayCell(Id(HhB), [Id(shJy), NumLit(46.78), BooleanLit(True)]), BooleanLit(True)), VarDecl(Id(WjN), ArrayType([43.74], NumberType), None, None)])), VarDecl(Id(egcG), ArrayType([73.73, 77.84], StringType), None, NumLit(9.48)), VarDecl(Id(S4), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115003))

	def test_21530115004(self):
		input = '''
string Fi[42.98,66.32,90.57] <- "O"
number S6I[13.53]
'''
		expect = '''Program([VarDecl(Id(Fi), ArrayType([42.98, 66.32, 90.57], StringType), None, StringLit(O)), VarDecl(Id(S6I), ArrayType([13.53], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115004))

	def test_21530115005(self):
		input = '''
func Ff (bool aiYs, number j57)	return true
bool j7e[9.64] <- 20.89
func xaS (number LdRw[67.69], number BLq[6.94])
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(Ff), [VarDecl(Id(aiYs), BoolType, None, None), VarDecl(Id(j57), NumberType, None, None)], Return(BooleanLit(True))), VarDecl(Id(j7e), ArrayType([9.64], BoolType), None, NumLit(20.89)), FuncDecl(Id(xaS), [VarDecl(Id(LdRw), ArrayType([67.69], NumberType), None, None), VarDecl(Id(BLq), ArrayType([6.94], NumberType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115005))

	def test_21530115006(self):
		input = '''
func sOb (bool MB3B[71.13,57.59,43.87], string qGX[34.45,71.2])	return

bool Fco <- U4qW
dynamic Red
func lNk (string ZPac[39.3,62.99,73.41], number TwLx)	return false
func CMrX (number al)	begin
		return
		lTh()
	end

'''
		expect = '''Program([FuncDecl(Id(sOb), [VarDecl(Id(MB3B), ArrayType([71.13, 57.59, 43.87], BoolType), None, None), VarDecl(Id(qGX), ArrayType([34.45, 71.2], StringType), None, None)], Return()), VarDecl(Id(Fco), BoolType, None, Id(U4qW)), VarDecl(Id(Red), None, dynamic, None), FuncDecl(Id(lNk), [VarDecl(Id(ZPac), ArrayType([39.3, 62.99, 73.41], StringType), None, None), VarDecl(Id(TwLx), NumberType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(CMrX), [VarDecl(Id(al), NumberType, None, None)], Block([Return(), CallStmt(Id(lTh), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115006))

	def test_21530115007(self):
		input = '''
func S0Gy ()	return "Fd"
bool pO
func hDm (number u0, bool fk)	begin
		for lG until true by "Fu"
			for xuW until false by "kMWL"
				begin
					Uhl <- KlN
					break
					SST <- gdt
				end
		var oid <- false
	end

func LZ (string ED[73.19,88.3,81.54])	return "WR"
'''
		expect = '''Program([FuncDecl(Id(S0Gy), [], Return(StringLit(Fd))), VarDecl(Id(pO), BoolType, None, None), FuncDecl(Id(hDm), [VarDecl(Id(u0), NumberType, None, None), VarDecl(Id(fk), BoolType, None, None)], Block([For(Id(lG), BooleanLit(True), StringLit(Fu), For(Id(xuW), BooleanLit(False), StringLit(kMWL), Block([AssignStmt(Id(Uhl), Id(KlN)), Break, AssignStmt(Id(SST), Id(gdt))]))), VarDecl(Id(oid), None, var, BooleanLit(False))])), FuncDecl(Id(LZ), [VarDecl(Id(ED), ArrayType([73.19, 88.3, 81.54], StringType), None, None)], Return(StringLit(WR)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115007))

	def test_21530115008(self):
		input = '''
bool YE <- Un
func nCgs (string Hmn, number T1[19.51,28.24])	return false
number M5
func fP (string cD1a, number yqL, string bDP2)
	return
'''
		expect = '''Program([VarDecl(Id(YE), BoolType, None, Id(Un)), FuncDecl(Id(nCgs), [VarDecl(Id(Hmn), StringType, None, None), VarDecl(Id(T1), ArrayType([19.51, 28.24], NumberType), None, None)], Return(BooleanLit(False))), VarDecl(Id(M5), NumberType, None, None), FuncDecl(Id(fP), [VarDecl(Id(cD1a), StringType, None, None), VarDecl(Id(yqL), NumberType, None, None), VarDecl(Id(bDP2), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115008))

	def test_21530115009(self):
		input = '''
number NZb[65.51,70.83] <- pB_
'''
		expect = '''Program([VarDecl(Id(NZb), ArrayType([65.51, 70.83], NumberType), None, Id(pB_))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115009))

	def test_21530115010(self):
		input = '''
number Q6[21.16,13.3,15.06] <- 43.92
string jvo[69.73]
func iW (number jR9)
	begin
	end
'''
		expect = '''Program([VarDecl(Id(Q6), ArrayType([21.16, 13.3, 15.06], NumberType), None, NumLit(43.92)), VarDecl(Id(jvo), ArrayType([69.73], StringType), None, None), FuncDecl(Id(iW), [VarDecl(Id(jR9), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115010))

	def test_21530115011(self):
		input = '''
func ZC_l (bool vIPn[53.42], number EX1[88.89,71.53])
	return
bool LNz[16.59]
number Wj
func QQoU (bool DOZ9, bool Eq[97.67], string z8c)	return
'''
		expect = '''Program([FuncDecl(Id(ZC_l), [VarDecl(Id(vIPn), ArrayType([53.42], BoolType), None, None), VarDecl(Id(EX1), ArrayType([88.89, 71.53], NumberType), None, None)], Return()), VarDecl(Id(LNz), ArrayType([16.59], BoolType), None, None), VarDecl(Id(Wj), NumberType, None, None), FuncDecl(Id(QQoU), [VarDecl(Id(DOZ9), BoolType, None, None), VarDecl(Id(Eq), ArrayType([97.67], BoolType), None, None), VarDecl(Id(z8c), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115011))

	def test_21530115012(self):
		input = '''
bool Wx
bool ab9g[96.79,63.96,77.32] <- 96.42
func VlPo (bool zKnb, string pf[55.03,67.6,23.43])	return "PnN"
'''
		expect = '''Program([VarDecl(Id(Wx), BoolType, None, None), VarDecl(Id(ab9g), ArrayType([96.79, 63.96, 77.32], BoolType), None, NumLit(96.42)), FuncDecl(Id(VlPo), [VarDecl(Id(zKnb), BoolType, None, None), VarDecl(Id(pf), ArrayType([55.03, 67.6, 23.43], StringType), None, None)], Return(StringLit(PnN)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115012))

	def test_21530115013(self):
		input = '''
func jLc (number nvMJ, number D8LH[31.24,27.21,97.92])	begin
		u5IH[false, s1p] <- HJw
	end
func gtP ()
	return

func p5 ()
	return AR

bool Jfx[6.09]
'''
		expect = '''Program([FuncDecl(Id(jLc), [VarDecl(Id(nvMJ), NumberType, None, None), VarDecl(Id(D8LH), ArrayType([31.24, 27.21, 97.92], NumberType), None, None)], Block([AssignStmt(ArrayCell(Id(u5IH), [BooleanLit(False), Id(s1p)]), Id(HJw))])), FuncDecl(Id(gtP), [], Return()), FuncDecl(Id(p5), [], Return(Id(AR))), VarDecl(Id(Jfx), ArrayType([6.09], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115013))

	def test_21530115014(self):
		input = '''
number VrZ[55.49] <- "vj"
func Zjo ()	return
number ayMS <- "FTH"
func Hzb (number JFgp, number ORgG[35.28,77.1,0.17])	return

bool qf
'''
		expect = '''Program([VarDecl(Id(VrZ), ArrayType([55.49], NumberType), None, StringLit(vj)), FuncDecl(Id(Zjo), [], Return()), VarDecl(Id(ayMS), NumberType, None, StringLit(FTH)), FuncDecl(Id(Hzb), [VarDecl(Id(JFgp), NumberType, None, None), VarDecl(Id(ORgG), ArrayType([35.28, 77.1, 0.17], NumberType), None, None)], Return()), VarDecl(Id(qf), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115014))

	def test_21530115015(self):
		input = '''
number e7iG[2.08,58.16,72.59]
'''
		expect = '''Program([VarDecl(Id(e7iG), ArrayType([2.08, 58.16, 72.59], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115015))

	def test_21530115016(self):
		input = '''
func ps (bool fkuD, string TpRX[86.93], bool Gf)	return 30.95

string cg[18.65,98.78] <- "hZdzk"
'''
		expect = '''Program([FuncDecl(Id(ps), [VarDecl(Id(fkuD), BoolType, None, None), VarDecl(Id(TpRX), ArrayType([86.93], StringType), None, None), VarDecl(Id(Gf), BoolType, None, None)], Return(NumLit(30.95))), VarDecl(Id(cg), ArrayType([18.65, 98.78], StringType), None, StringLit(hZdzk))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115016))

	def test_21530115017(self):
		input = '''
func Rv ()	return

'''
		expect = '''Program([FuncDecl(Id(Rv), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115017))

	def test_21530115018(self):
		input = '''
func dMS (bool d9b, string Kx, number sI_)	return
bool uNvC <- 62.27
'''
		expect = '''Program([FuncDecl(Id(dMS), [VarDecl(Id(d9b), BoolType, None, None), VarDecl(Id(Kx), StringType, None, None), VarDecl(Id(sI_), NumberType, None, None)], Return()), VarDecl(Id(uNvC), BoolType, None, NumLit(62.27))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115018))

	def test_21530115019(self):
		input = '''
func Ab (bool hJ, number YOsG, number UcYR)
	begin
	end
number SjQ[43.21,13.83]
func AcXX (string zNN, number psOw[34.47], number LSTO)	begin
		string ox[48.62,60.28]
	end

number fRL5 <- mQ
bool omD[73.53] <- kShL
'''
		expect = '''Program([FuncDecl(Id(Ab), [VarDecl(Id(hJ), BoolType, None, None), VarDecl(Id(YOsG), NumberType, None, None), VarDecl(Id(UcYR), NumberType, None, None)], Block([])), VarDecl(Id(SjQ), ArrayType([43.21, 13.83], NumberType), None, None), FuncDecl(Id(AcXX), [VarDecl(Id(zNN), StringType, None, None), VarDecl(Id(psOw), ArrayType([34.47], NumberType), None, None), VarDecl(Id(LSTO), NumberType, None, None)], Block([VarDecl(Id(ox), ArrayType([48.62, 60.28], StringType), None, None)])), VarDecl(Id(fRL5), NumberType, None, Id(mQ)), VarDecl(Id(omD), ArrayType([73.53], BoolType), None, Id(kShL))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115019))

	def test_21530115020(self):
		input = '''
bool Wef <- gw
func axxh (string sGV, string azx[51.18,98.09,29.29], number Qlh[73.63,90.52])	begin
		number Ok[16.46,23.03]
		for xJ4Y until true by true
			continue
		Yrj[5.93, true] <- 54.0
	end

string gt[73.86,23.34,37.12] <- xYzK
func w2 (number yHfP)
	begin
	end

'''
		expect = '''Program([VarDecl(Id(Wef), BoolType, None, Id(gw)), FuncDecl(Id(axxh), [VarDecl(Id(sGV), StringType, None, None), VarDecl(Id(azx), ArrayType([51.18, 98.09, 29.29], StringType), None, None), VarDecl(Id(Qlh), ArrayType([73.63, 90.52], NumberType), None, None)], Block([VarDecl(Id(Ok), ArrayType([16.46, 23.03], NumberType), None, None), For(Id(xJ4Y), BooleanLit(True), BooleanLit(True), Continue), AssignStmt(ArrayCell(Id(Yrj), [NumLit(5.93), BooleanLit(True)]), NumLit(54.0))])), VarDecl(Id(gt), ArrayType([73.86, 23.34, 37.12], StringType), None, Id(xYzK)), FuncDecl(Id(w2), [VarDecl(Id(yHfP), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115020))

	def test_21530115021(self):
		input = '''
func GwN (number iZwJ[17.19,5.46,49.17], string eWlp, bool A5Ei[38.9,55.83,94.63])
	return n5
'''
		expect = '''Program([FuncDecl(Id(GwN), [VarDecl(Id(iZwJ), ArrayType([17.19, 5.46, 49.17], NumberType), None, None), VarDecl(Id(eWlp), StringType, None, None), VarDecl(Id(A5Ei), ArrayType([38.9, 55.83, 94.63], BoolType), None, None)], Return(Id(n5)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115021))

	def test_21530115022(self):
		input = '''
number z58T
func FOgC ()	return 12.46
'''
		expect = '''Program([VarDecl(Id(z58T), NumberType, None, None), FuncDecl(Id(FOgC), [], Return(NumLit(12.46)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115022))

	def test_21530115023(self):
		input = '''
func hp (number Vfcg, number U0Z, number BtX8)
	return

number VJd
'''
		expect = '''Program([FuncDecl(Id(hp), [VarDecl(Id(Vfcg), NumberType, None, None), VarDecl(Id(U0Z), NumberType, None, None), VarDecl(Id(BtX8), NumberType, None, None)], Return()), VarDecl(Id(VJd), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115023))

	def test_21530115024(self):
		input = '''
dynamic u3
'''
		expect = '''Program([VarDecl(Id(u3), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115024))

	def test_21530115025(self):
		input = '''
func Sgsx (string vPwG[0.71,22.51,53.84])
	return "D"
func KX ()	return

bool Eu[49.03,31.39] <- 50.94
'''
		expect = '''Program([FuncDecl(Id(Sgsx), [VarDecl(Id(vPwG), ArrayType([0.71, 22.51, 53.84], StringType), None, None)], Return(StringLit(D))), FuncDecl(Id(KX), [], Return()), VarDecl(Id(Eu), ArrayType([49.03, 31.39], BoolType), None, NumLit(50.94))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115025))

	def test_21530115026(self):
		input = '''
bool NG <- false
number No[53.05,52.64,63.95]
string lk[91.15,28.27,86.96]
func WiMY (bool FoQU[88.46,18.35], bool Ds[23.36,48.89], number fL[98.46,20.66,83.79])
	return

func yM (number jzK[66.87,17.3], bool BMl[1.45])
	begin
		break
	end

'''
		expect = '''Program([VarDecl(Id(NG), BoolType, None, BooleanLit(False)), VarDecl(Id(No), ArrayType([53.05, 52.64, 63.95], NumberType), None, None), VarDecl(Id(lk), ArrayType([91.15, 28.27, 86.96], StringType), None, None), FuncDecl(Id(WiMY), [VarDecl(Id(FoQU), ArrayType([88.46, 18.35], BoolType), None, None), VarDecl(Id(Ds), ArrayType([23.36, 48.89], BoolType), None, None), VarDecl(Id(fL), ArrayType([98.46, 20.66, 83.79], NumberType), None, None)], Return()), FuncDecl(Id(yM), [VarDecl(Id(jzK), ArrayType([66.87, 17.3], NumberType), None, None), VarDecl(Id(BMl), ArrayType([1.45], BoolType), None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115026))

	def test_21530115027(self):
		input = '''
bool KDC[33.75] <- false
'''
		expect = '''Program([VarDecl(Id(KDC), ArrayType([33.75], BoolType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115027))

	def test_21530115028(self):
		input = '''
func mPK ()	return true

func kQXt ()	return
var VkK7 <- false
func lg7Z ()
	return
'''
		expect = '''Program([FuncDecl(Id(mPK), [], Return(BooleanLit(True))), FuncDecl(Id(kQXt), [], Return()), VarDecl(Id(VkK7), None, var, BooleanLit(False)), FuncDecl(Id(lg7Z), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115028))

	def test_21530115029(self):
		input = '''
number g7[80.54,98.53,52.46]
func TB (number QGA, bool fZ3)
	return
func Jnt (string Hl, number Y8w[55.85,41.45])	return
func KKV ()
	return
func RIEu ()
	return 9.55

'''
		expect = '''Program([VarDecl(Id(g7), ArrayType([80.54, 98.53, 52.46], NumberType), None, None), FuncDecl(Id(TB), [VarDecl(Id(QGA), NumberType, None, None), VarDecl(Id(fZ3), BoolType, None, None)], Return()), FuncDecl(Id(Jnt), [VarDecl(Id(Hl), StringType, None, None), VarDecl(Id(Y8w), ArrayType([55.85, 41.45], NumberType), None, None)], Return()), FuncDecl(Id(KKV), [], Return()), FuncDecl(Id(RIEu), [], Return(NumLit(9.55)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115029))

	def test_21530115030(self):
		input = '''
func ds ()
	return
func VV ()
	return false
'''
		expect = '''Program([FuncDecl(Id(ds), [], Return()), FuncDecl(Id(VV), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115030))

	def test_21530115031(self):
		input = '''
string W70[97.16,51.72,99.77]
number q6BZ[65.63,25.69,47.39] <- 96.17
string vKZ[78.21,42.32]
func a9y (number kV, string Fr)
	return 38.47

'''
		expect = '''Program([VarDecl(Id(W70), ArrayType([97.16, 51.72, 99.77], StringType), None, None), VarDecl(Id(q6BZ), ArrayType([65.63, 25.69, 47.39], NumberType), None, NumLit(96.17)), VarDecl(Id(vKZ), ArrayType([78.21, 42.32], StringType), None, None), FuncDecl(Id(a9y), [VarDecl(Id(kV), NumberType, None, None), VarDecl(Id(Fr), StringType, None, None)], Return(NumLit(38.47)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115031))

	def test_21530115032(self):
		input = '''
func sI (bool SMbT[17.39], bool o1[7.3,75.65], number Kwl[6.73])	return 90.83

'''
		expect = '''Program([FuncDecl(Id(sI), [VarDecl(Id(SMbT), ArrayType([17.39], BoolType), None, None), VarDecl(Id(o1), ArrayType([7.3, 75.65], BoolType), None, None), VarDecl(Id(Kwl), ArrayType([6.73], NumberType), None, None)], Return(NumLit(90.83)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115032))

	def test_21530115033(self):
		input = '''
number Qb[39.34]
'''
		expect = '''Program([VarDecl(Id(Qb), ArrayType([39.34], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115033))

	def test_21530115034(self):
		input = '''
string Lvdb[21.78] <- 27.7
bool Hs[56.35,70.85]
number Fq5[40.18] <- "hUrtC"
var z_H <- false
func iIv (bool xJ6[51.03,52.47,64.44], bool obXY)	return

'''
		expect = '''Program([VarDecl(Id(Lvdb), ArrayType([21.78], StringType), None, NumLit(27.7)), VarDecl(Id(Hs), ArrayType([56.35, 70.85], BoolType), None, None), VarDecl(Id(Fq5), ArrayType([40.18], NumberType), None, StringLit(hUrtC)), VarDecl(Id(z_H), None, var, BooleanLit(False)), FuncDecl(Id(iIv), [VarDecl(Id(xJ6), ArrayType([51.03, 52.47, 64.44], BoolType), None, None), VarDecl(Id(obXY), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115034))

	def test_21530115035(self):
		input = '''
bool dn[24.71,49.99]
dynamic h4m5 <- true
func pbz (string NYGl)	begin
		for hQyo until false by zc
			h7(KaR8, 68.36, true)
	end
func YjN (number aC[77.63])
	return
func IC (number Wb, string fSa)
	return 14.71

'''
		expect = '''Program([VarDecl(Id(dn), ArrayType([24.71, 49.99], BoolType), None, None), VarDecl(Id(h4m5), None, dynamic, BooleanLit(True)), FuncDecl(Id(pbz), [VarDecl(Id(NYGl), StringType, None, None)], Block([For(Id(hQyo), BooleanLit(False), Id(zc), CallStmt(Id(h7), [Id(KaR8), NumLit(68.36), BooleanLit(True)]))])), FuncDecl(Id(YjN), [VarDecl(Id(aC), ArrayType([77.63], NumberType), None, None)], Return()), FuncDecl(Id(IC), [VarDecl(Id(Wb), NumberType, None, None), VarDecl(Id(fSa), StringType, None, None)], Return(NumLit(14.71)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115035))

	def test_21530115036(self):
		input = '''
number Wq[19.04,8.0,50.72]
number bO <- "XkK"
bool Uwi8[52.25,8.35]
func Ltex ()
	return "Kwev"
func VB (number WtEu)
	return
'''
		expect = '''Program([VarDecl(Id(Wq), ArrayType([19.04, 8.0, 50.72], NumberType), None, None), VarDecl(Id(bO), NumberType, None, StringLit(XkK)), VarDecl(Id(Uwi8), ArrayType([52.25, 8.35], BoolType), None, None), FuncDecl(Id(Ltex), [], Return(StringLit(Kwev))), FuncDecl(Id(VB), [VarDecl(Id(WtEu), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115036))

	def test_21530115037(self):
		input = '''
func tO (string MO4[94.76,0.49], string Yc2q[29.56,65.13,31.95], number T1dV)	return kjY
'''
		expect = '''Program([FuncDecl(Id(tO), [VarDecl(Id(MO4), ArrayType([94.76, 0.49], StringType), None, None), VarDecl(Id(Yc2q), ArrayType([29.56, 65.13, 31.95], StringType), None, None), VarDecl(Id(T1dV), NumberType, None, None)], Return(Id(kjY)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115037))

	def test_21530115038(self):
		input = '''
bool gRS5[16.14,99.34] <- YkZ5
func IS (number C7jd)	return
string UzQE <- px
'''
		expect = '''Program([VarDecl(Id(gRS5), ArrayType([16.14, 99.34], BoolType), None, Id(YkZ5)), FuncDecl(Id(IS), [VarDecl(Id(C7jd), NumberType, None, None)], Return()), VarDecl(Id(UzQE), StringType, None, Id(px))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115038))

	def test_21530115039(self):
		input = '''
bool Rfjc[49.86,74.87]
string DP[96.86] <- IRU
func IO ()
	return 72.53
func eNn (bool CL, bool sr[40.51,8.74,84.23], bool vCd[9.7,36.26,99.24])	return "mzmtC"

bool W3S6[68.07]
'''
		expect = '''Program([VarDecl(Id(Rfjc), ArrayType([49.86, 74.87], BoolType), None, None), VarDecl(Id(DP), ArrayType([96.86], StringType), None, Id(IRU)), FuncDecl(Id(IO), [], Return(NumLit(72.53))), FuncDecl(Id(eNn), [VarDecl(Id(CL), BoolType, None, None), VarDecl(Id(sr), ArrayType([40.51, 8.74, 84.23], BoolType), None, None), VarDecl(Id(vCd), ArrayType([9.7, 36.26, 99.24], BoolType), None, None)], Return(StringLit(mzmtC))), VarDecl(Id(W3S6), ArrayType([68.07], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115039))

	def test_21530115040(self):
		input = '''
func qx (bool P3, number VRy, number AO[99.25])	return 6.68
func RiuD (number Hmbz, string B9d7[37.04,35.32,0.92], string ZP)	return

func mUDU (number egqr[61.18])
	return true

'''
		expect = '''Program([FuncDecl(Id(qx), [VarDecl(Id(P3), BoolType, None, None), VarDecl(Id(VRy), NumberType, None, None), VarDecl(Id(AO), ArrayType([99.25], NumberType), None, None)], Return(NumLit(6.68))), FuncDecl(Id(RiuD), [VarDecl(Id(Hmbz), NumberType, None, None), VarDecl(Id(B9d7), ArrayType([37.04, 35.32, 0.92], StringType), None, None), VarDecl(Id(ZP), StringType, None, None)], Return()), FuncDecl(Id(mUDU), [VarDecl(Id(egqr), ArrayType([61.18], NumberType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115040))

	def test_21530115041(self):
		input = '''
bool rZZ_ <- "Fo"
'''
		expect = '''Program([VarDecl(Id(rZZ_), BoolType, None, StringLit(Fo))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115041))

	def test_21530115042(self):
		input = '''
string crA5[21.91] <- qxW
string Dzv <- true
func pP (string SqpL[51.63,27.62], bool g1)
	begin
		AA("oMmz", "J")
		begin
			gn()
			return "GfCG"
		end
		var iGz <- 27.34
	end
var TS <- 47.8
'''
		expect = '''Program([VarDecl(Id(crA5), ArrayType([21.91], StringType), None, Id(qxW)), VarDecl(Id(Dzv), StringType, None, BooleanLit(True)), FuncDecl(Id(pP), [VarDecl(Id(SqpL), ArrayType([51.63, 27.62], StringType), None, None), VarDecl(Id(g1), BoolType, None, None)], Block([CallStmt(Id(AA), [StringLit(oMmz), StringLit(J)]), Block([CallStmt(Id(gn), []), Return(StringLit(GfCG))]), VarDecl(Id(iGz), None, var, NumLit(27.34))])), VarDecl(Id(TS), None, var, NumLit(47.8))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115042))

	def test_21530115043(self):
		input = '''
func flhM ()	begin
		continue
		wxE()
		continue
	end
func Iw_ ()
	return 13.86
var oLn <- piP
'''
		expect = '''Program([FuncDecl(Id(flhM), [], Block([Continue, CallStmt(Id(wxE), []), Continue])), FuncDecl(Id(Iw_), [], Return(NumLit(13.86))), VarDecl(Id(oLn), None, var, Id(piP))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115043))

	def test_21530115044(self):
		input = '''
func rZ5 (number ssq[79.26,77.21], number srCQ[36.85], string BEM[77.82])
	begin
		break
	end

func SwL ()	return "mVqP"

func yv (string PfTM)
	return
'''
		expect = '''Program([FuncDecl(Id(rZ5), [VarDecl(Id(ssq), ArrayType([79.26, 77.21], NumberType), None, None), VarDecl(Id(srCQ), ArrayType([36.85], NumberType), None, None), VarDecl(Id(BEM), ArrayType([77.82], StringType), None, None)], Block([Break])), FuncDecl(Id(SwL), [], Return(StringLit(mVqP))), FuncDecl(Id(yv), [VarDecl(Id(PfTM), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115044))

	def test_21530115045(self):
		input = '''
func lz ()	begin
		begin
			begin
			end
			jtj <- false
			continue
		end
		begin
			if (6.91)
			for DA7 until 4.53 by false
				break
		end
		MBF2(true)
	end

func Ta8M ()
	return
bool L3M[31.67,74.26,6.64] <- true
bool jxe[95.75,2.82,45.02] <- false
var I9g <- gBG
'''
		expect = '''Program([FuncDecl(Id(lz), [], Block([Block([Block([]), AssignStmt(Id(jtj), BooleanLit(False)), Continue]), Block([If(NumLit(6.91), For(Id(DA7), NumLit(4.53), BooleanLit(False), Break)), [], None]), CallStmt(Id(MBF2), [BooleanLit(True)])])), FuncDecl(Id(Ta8M), [], Return()), VarDecl(Id(L3M), ArrayType([31.67, 74.26, 6.64], BoolType), None, BooleanLit(True)), VarDecl(Id(jxe), ArrayType([95.75, 2.82, 45.02], BoolType), None, BooleanLit(False)), VarDecl(Id(I9g), None, var, Id(gBG))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115045))

	def test_21530115046(self):
		input = '''
number FT8[16.8,14.07,55.61]
string nO[1.57,13.32] <- 88.43
'''
		expect = '''Program([VarDecl(Id(FT8), ArrayType([16.8, 14.07, 55.61], NumberType), None, None), VarDecl(Id(nO), ArrayType([1.57, 13.32], StringType), None, NumLit(88.43))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115046))

	def test_21530115047(self):
		input = '''
string aAlD
var Ca <- false
func EJo (number xzF[17.44,61.71,92.29], string PoS)	return "sAsw"

'''
		expect = '''Program([VarDecl(Id(aAlD), StringType, None, None), VarDecl(Id(Ca), None, var, BooleanLit(False)), FuncDecl(Id(EJo), [VarDecl(Id(xzF), ArrayType([17.44, 61.71, 92.29], NumberType), None, None), VarDecl(Id(PoS), StringType, None, None)], Return(StringLit(sAsw)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115047))

	def test_21530115048(self):
		input = '''
func KHlW (bool wf3[89.63], string Dcb, number sQd)
	return

'''
		expect = '''Program([FuncDecl(Id(KHlW), [VarDecl(Id(wf3), ArrayType([89.63], BoolType), None, None), VarDecl(Id(Dcb), StringType, None, None), VarDecl(Id(sQd), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115048))

	def test_21530115049(self):
		input = '''
number ox
'''
		expect = '''Program([VarDecl(Id(ox), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115049))

	def test_21530115050(self):
		input = '''
func Lsf (string BTpS, string SKN)	begin
		break
		qs[0.18, "yeDVN"] <- h5N
		jFO <- false
	end
'''
		expect = '''Program([FuncDecl(Id(Lsf), [VarDecl(Id(BTpS), StringType, None, None), VarDecl(Id(SKN), StringType, None, None)], Block([Break, AssignStmt(ArrayCell(Id(qs), [NumLit(0.18), StringLit(yeDVN)]), Id(h5N)), AssignStmt(Id(jFO), BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115050))

	def test_21530115051(self):
		input = '''
dynamic gk <- P1_d
func PHL (string Ual[7.61,45.39], number fk60, bool mU)	return true
func rM ()	begin
		asO <- 95.5
	end

'''
		expect = '''Program([VarDecl(Id(gk), None, dynamic, Id(P1_d)), FuncDecl(Id(PHL), [VarDecl(Id(Ual), ArrayType([7.61, 45.39], StringType), None, None), VarDecl(Id(fk60), NumberType, None, None), VarDecl(Id(mU), BoolType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(rM), [], Block([AssignStmt(Id(asO), NumLit(95.5))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115051))

	def test_21530115052(self):
		input = '''
number NP0B
bool Nf <- 20.77
'''
		expect = '''Program([VarDecl(Id(NP0B), NumberType, None, None), VarDecl(Id(Nf), BoolType, None, NumLit(20.77))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115052))

	def test_21530115053(self):
		input = '''
func chOG (bool K9Z, number o_sa)
	begin
	end
dynamic Ol_ <- false
bool nK5E[57.89]
func Ck (string jsW)
	return

func lmAL ()	return

'''
		expect = '''Program([FuncDecl(Id(chOG), [VarDecl(Id(K9Z), BoolType, None, None), VarDecl(Id(o_sa), NumberType, None, None)], Block([])), VarDecl(Id(Ol_), None, dynamic, BooleanLit(False)), VarDecl(Id(nK5E), ArrayType([57.89], BoolType), None, None), FuncDecl(Id(Ck), [VarDecl(Id(jsW), StringType, None, None)], Return()), FuncDecl(Id(lmAL), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115053))

	def test_21530115054(self):
		input = '''
bool QFD[1.79,49.54] <- 93.06
number U3 <- 92.56
number p0XZ[72.68,46.33,29.71] <- TU
func cD ()	begin
		break
		continue
	end
'''
		expect = '''Program([VarDecl(Id(QFD), ArrayType([1.79, 49.54], BoolType), None, NumLit(93.06)), VarDecl(Id(U3), NumberType, None, NumLit(92.56)), VarDecl(Id(p0XZ), ArrayType([72.68, 46.33, 29.71], NumberType), None, Id(TU)), FuncDecl(Id(cD), [], Block([Break, Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115054))

	def test_21530115055(self):
		input = '''
func Rktj (bool B4bp, number vNb, string wS)
	begin
		return
		begin
			for O7h until wdu by "UZE"
				begin
					CFK <- true
					return true
					return
				end
			if ("IyCCx") break
			elif (AT)
			for BGg8 until 77.43 by "ccZN"
				break
			elif (Pu)
			if (true)
			begin
				return
				begin
					return 38.17
				end
				for FRg until "nPv" by 2.46
					return
			end
			elif (true)
			break
			elif (false) return
			elif (I0) break
		end
		for lAn until 25.51 by "j"
			begin
				continue
				continue
			end
	end

bool IL[29.77,72.66] <- true
dynamic Jzk <- true
'''
		expect = '''Program([FuncDecl(Id(Rktj), [VarDecl(Id(B4bp), BoolType, None, None), VarDecl(Id(vNb), NumberType, None, None), VarDecl(Id(wS), StringType, None, None)], Block([Return(), Block([For(Id(O7h), Id(wdu), StringLit(UZE), Block([AssignStmt(Id(CFK), BooleanLit(True)), Return(BooleanLit(True)), Return()])), If(StringLit(IyCCx), Break), [(Id(AT), For(Id(BGg8), NumLit(77.43), StringLit(ccZN), Break)), (Id(Pu), If(BooleanLit(True), Block([Return(), Block([Return(NumLit(38.17))]), For(Id(FRg), StringLit(nPv), NumLit(2.46), Return())])), [(BooleanLit(True), Break), (BooleanLit(False), Return()), (Id(I0), Break)], None)], None]), For(Id(lAn), NumLit(25.51), StringLit(j), Block([Continue, Continue]))])), VarDecl(Id(IL), ArrayType([29.77, 72.66], BoolType), None, BooleanLit(True)), VarDecl(Id(Jzk), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115055))

	def test_21530115056(self):
		input = '''
func sZF (bool fPH[57.06,29.59,74.86])
	begin
	end
func N7c (string As)
	return
func lKfK (number nm)	return

func kQtZ (string vL[98.67], bool aP[73.3,68.04], string BRKB)	return true
bool Ia
'''
		expect = '''Program([FuncDecl(Id(sZF), [VarDecl(Id(fPH), ArrayType([57.06, 29.59, 74.86], BoolType), None, None)], Block([])), FuncDecl(Id(N7c), [VarDecl(Id(As), StringType, None, None)], Return()), FuncDecl(Id(lKfK), [VarDecl(Id(nm), NumberType, None, None)], Return()), FuncDecl(Id(kQtZ), [VarDecl(Id(vL), ArrayType([98.67], StringType), None, None), VarDecl(Id(aP), ArrayType([73.3, 68.04], BoolType), None, None), VarDecl(Id(BRKB), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(Ia), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115056))

	def test_21530115057(self):
		input = '''
string BC_[29.01,19.46]
func Qtu (number QRQ, number DzMB, string Pw0a[82.46])
	return false
'''
		expect = '''Program([VarDecl(Id(BC_), ArrayType([29.01, 19.46], StringType), None, None), FuncDecl(Id(Qtu), [VarDecl(Id(QRQ), NumberType, None, None), VarDecl(Id(DzMB), NumberType, None, None), VarDecl(Id(Pw0a), ArrayType([82.46], StringType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115057))

	def test_21530115058(self):
		input = '''
number OcrA[72.8,89.18,57.74] <- bQD
func hW ()	begin
		for dU until false by e9Bm
			if ("eds") for HQs until "HOH" by BMv
				begin
				end
			elif (Ppi)
			return
			elif (W_N)
			Dx4g[3.05] <- 44.1
		for katZ until true by 86.2
			dynamic Jf <- "ovA"
		break
	end

dynamic Ny <- true
func cBYr (number vK[12.21,29.37,71.3])	begin
		kIg(Z2, "lq", 98.64)
	end
func gE (bool Aa, string hDR5[66.03], bool TF)	begin
		continue
		if (21.89) begin
		end
		elif (98.46) continue
		elif (16.95) begin
			if ("tUg") vJ98()
			begin
				begin
				end
				break
			end
		end
		elif (false)
		for Tf7 until 8.59 by "DUzvy"
			return "rAhK"
		elif (true) return
		begin
			break
		end
	end
'''
		expect = '''Program([VarDecl(Id(OcrA), ArrayType([72.8, 89.18, 57.74], NumberType), None, Id(bQD)), FuncDecl(Id(hW), [], Block([For(Id(dU), BooleanLit(False), Id(e9Bm), If(StringLit(eds), For(Id(HQs), StringLit(HOH), Id(BMv), Block([]))), [(Id(Ppi), Return()), (Id(W_N), AssignStmt(ArrayCell(Id(Dx4g), [NumLit(3.05)]), NumLit(44.1)))], None), For(Id(katZ), BooleanLit(True), NumLit(86.2), VarDecl(Id(Jf), None, dynamic, StringLit(ovA))), Break])), VarDecl(Id(Ny), None, dynamic, BooleanLit(True)), FuncDecl(Id(cBYr), [VarDecl(Id(vK), ArrayType([12.21, 29.37, 71.3], NumberType), None, None)], Block([CallStmt(Id(kIg), [Id(Z2), StringLit(lq), NumLit(98.64)])])), FuncDecl(Id(gE), [VarDecl(Id(Aa), BoolType, None, None), VarDecl(Id(hDR5), ArrayType([66.03], StringType), None, None), VarDecl(Id(TF), BoolType, None, None)], Block([Continue, If(NumLit(21.89), Block([])), [(NumLit(98.46), Continue), (NumLit(16.95), Block([If(StringLit(tUg), CallStmt(Id(vJ98), [])), [], None, Block([Block([]), Break])])), (BooleanLit(False), For(Id(Tf7), NumLit(8.59), StringLit(DUzvy), Return(StringLit(rAhK)))), (BooleanLit(True), Return())], None, Block([Break])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115058))

	def test_21530115059(self):
		input = '''
func MPr (string cbmh[39.53,17.3,92.92], number ub, number tLj[70.77,48.72])	return

func mZm5 (string mT8G)	return "aRv"

'''
		expect = '''Program([FuncDecl(Id(MPr), [VarDecl(Id(cbmh), ArrayType([39.53, 17.3, 92.92], StringType), None, None), VarDecl(Id(ub), NumberType, None, None), VarDecl(Id(tLj), ArrayType([70.77, 48.72], NumberType), None, None)], Return()), FuncDecl(Id(mZm5), [VarDecl(Id(mT8G), StringType, None, None)], Return(StringLit(aRv)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115059))

	def test_21530115060(self):
		input = '''
func nS7v (number yc)
	return 90.25
func hll5 ()	begin
	end

number Qr3Y <- false
'''
		expect = '''Program([FuncDecl(Id(nS7v), [VarDecl(Id(yc), NumberType, None, None)], Return(NumLit(90.25))), FuncDecl(Id(hll5), [], Block([])), VarDecl(Id(Qr3Y), NumberType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115060))

	def test_21530115061(self):
		input = '''
func no7 (bool Xz[21.0])
	begin
		DG()
		jS()
		ab(PiOr)
	end
func iWUn (number t8, bool qD[94.96])
	return "JSxVY"

string MFYy[46.0,34.29] <- false
string zshV
string k0 <- "p"
'''
		expect = '''Program([FuncDecl(Id(no7), [VarDecl(Id(Xz), ArrayType([21.0], BoolType), None, None)], Block([CallStmt(Id(DG), []), CallStmt(Id(jS), []), CallStmt(Id(ab), [Id(PiOr)])])), FuncDecl(Id(iWUn), [VarDecl(Id(t8), NumberType, None, None), VarDecl(Id(qD), ArrayType([94.96], BoolType), None, None)], Return(StringLit(JSxVY))), VarDecl(Id(MFYy), ArrayType([46.0, 34.29], StringType), None, BooleanLit(False)), VarDecl(Id(zshV), StringType, None, None), VarDecl(Id(k0), StringType, None, StringLit(p))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115061))

	def test_21530115062(self):
		input = '''
number FMQ <- true
func AN (number Ia, string NZ, string zR[43.29])	return false
string pT <- "GAEOv"
func MfI ()
	begin
		begin
			return
			for kJ until true by 19.33
				begin
					bool HXDh[44.41,50.97,86.53] <- "VUHDI"
					yJH <- "oRgD"
				end
		end
		if ("DPSQ")
		break
		elif (Vfc1) ns3 <- "sOmk"
		else break
	end
'''
		expect = '''Program([VarDecl(Id(FMQ), NumberType, None, BooleanLit(True)), FuncDecl(Id(AN), [VarDecl(Id(Ia), NumberType, None, None), VarDecl(Id(NZ), StringType, None, None), VarDecl(Id(zR), ArrayType([43.29], StringType), None, None)], Return(BooleanLit(False))), VarDecl(Id(pT), StringType, None, StringLit(GAEOv)), FuncDecl(Id(MfI), [], Block([Block([Return(), For(Id(kJ), BooleanLit(True), NumLit(19.33), Block([VarDecl(Id(HXDh), ArrayType([44.41, 50.97, 86.53], BoolType), None, StringLit(VUHDI)), AssignStmt(Id(yJH), StringLit(oRgD))]))]), If(StringLit(DPSQ), Break), [(Id(Vfc1), AssignStmt(Id(ns3), StringLit(sOmk)))], Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115062))

	def test_21530115063(self):
		input = '''
string er
number e9wA
bool rAP <- zg
string v6tg[1.4] <- false
func ljn ()
	return 25.84

'''
		expect = '''Program([VarDecl(Id(er), StringType, None, None), VarDecl(Id(e9wA), NumberType, None, None), VarDecl(Id(rAP), BoolType, None, Id(zg)), VarDecl(Id(v6tg), ArrayType([1.4], StringType), None, BooleanLit(False)), FuncDecl(Id(ljn), [], Return(NumLit(25.84)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115063))

	def test_21530115064(self):
		input = '''
var AW <- HEzS
var x4 <- true
func LSyt (string RVht, bool LS)	begin
	end
dynamic Y0ys
func XkJE (number VVw, string LYZQ[34.2], bool Gf)	return
'''
		expect = '''Program([VarDecl(Id(AW), None, var, Id(HEzS)), VarDecl(Id(x4), None, var, BooleanLit(True)), FuncDecl(Id(LSyt), [VarDecl(Id(RVht), StringType, None, None), VarDecl(Id(LS), BoolType, None, None)], Block([])), VarDecl(Id(Y0ys), None, dynamic, None), FuncDecl(Id(XkJE), [VarDecl(Id(VVw), NumberType, None, None), VarDecl(Id(LYZQ), ArrayType([34.2], StringType), None, None), VarDecl(Id(Gf), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115064))

	def test_21530115065(self):
		input = '''
func Yfy (number c2, bool OGL[18.77])
	return 57.2
number pO[29.82,26.4,2.35]
'''
		expect = '''Program([FuncDecl(Id(Yfy), [VarDecl(Id(c2), NumberType, None, None), VarDecl(Id(OGL), ArrayType([18.77], BoolType), None, None)], Return(NumLit(57.2))), VarDecl(Id(pO), ArrayType([29.82, 26.4, 2.35], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115065))

	def test_21530115066(self):
		input = '''
func oR1 (string LO, bool HP_v)	return

'''
		expect = '''Program([FuncDecl(Id(oR1), [VarDecl(Id(LO), StringType, None, None), VarDecl(Id(HP_v), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115066))

	def test_21530115067(self):
		input = '''
func gTs (string FULh, bool ONF, number TY)
	begin
		ALgT[yx, true, "J"] <- "TbEWI"
	end
number bi <- m7T
func S4 ()	return

dynamic P7 <- l3E
func Tan ()	begin
		return false
		for CTm4 until "Q" by "gMjjN"
			begin
				break
				if ("Bsqp")
				if (true) for ZKKZ until Kp by false
					continue
				elif ("t") return "Hl"
				else continue
				elif ("DJxeR") begin
					AN(true)
					for mj until "vCmv" by "DukO"
						for ypC until 82.85 by "WlkqD"
							ug(fl, 41.09)
				end
				Q8()
			end
	end
'''
		expect = '''Program([FuncDecl(Id(gTs), [VarDecl(Id(FULh), StringType, None, None), VarDecl(Id(ONF), BoolType, None, None), VarDecl(Id(TY), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(ALgT), [Id(yx), BooleanLit(True), StringLit(J)]), StringLit(TbEWI))])), VarDecl(Id(bi), NumberType, None, Id(m7T)), FuncDecl(Id(S4), [], Return()), VarDecl(Id(P7), None, dynamic, Id(l3E)), FuncDecl(Id(Tan), [], Block([Return(BooleanLit(False)), For(Id(CTm4), StringLit(Q), StringLit(gMjjN), Block([Break, If(StringLit(Bsqp), If(BooleanLit(True), For(Id(ZKKZ), Id(Kp), BooleanLit(False), Continue)), [(StringLit(t), Return(StringLit(Hl)))], Continue), [(StringLit(DJxeR), Block([CallStmt(Id(AN), [BooleanLit(True)]), For(Id(mj), StringLit(vCmv), StringLit(DukO), For(Id(ypC), NumLit(82.85), StringLit(WlkqD), CallStmt(Id(ug), [Id(fl), NumLit(41.09)])))]))], None, CallStmt(Id(Q8), [])]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115067))

	def test_21530115068(self):
		input = '''
func t6J (string Md[81.24,11.1,26.03], string Vkx[60.85,46.52])	begin
		return "OjTUl"
		break
		number F7c <- "Kb"
	end

bool ZqDT[70.2,10.88] <- 39.66
'''
		expect = '''Program([FuncDecl(Id(t6J), [VarDecl(Id(Md), ArrayType([81.24, 11.1, 26.03], StringType), None, None), VarDecl(Id(Vkx), ArrayType([60.85, 46.52], StringType), None, None)], Block([Return(StringLit(OjTUl)), Break, VarDecl(Id(F7c), NumberType, None, StringLit(Kb))])), VarDecl(Id(ZqDT), ArrayType([70.2, 10.88], BoolType), None, NumLit(39.66))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115068))

	def test_21530115069(self):
		input = '''
func a6m (number KU[18.44])	begin
		var OQp2 <- "k"
	end
string a0[69.18,56.32,28.08] <- 54.83
'''
		expect = '''Program([FuncDecl(Id(a6m), [VarDecl(Id(KU), ArrayType([18.44], NumberType), None, None)], Block([VarDecl(Id(OQp2), None, var, StringLit(k))])), VarDecl(Id(a0), ArrayType([69.18, 56.32, 28.08], StringType), None, NumLit(54.83))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115069))

	def test_21530115070(self):
		input = '''
func zr (number AU[16.57,98.74], string Mt)
	return
bool KSc2 <- false
number yv
'''
		expect = '''Program([FuncDecl(Id(zr), [VarDecl(Id(AU), ArrayType([16.57, 98.74], NumberType), None, None), VarDecl(Id(Mt), StringType, None, None)], Return()), VarDecl(Id(KSc2), BoolType, None, BooleanLit(False)), VarDecl(Id(yv), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115070))

	def test_21530115071(self):
		input = '''
func ZxT ()	return "w"

string OO <- 25.46
func wax (number uZ[50.07,68.08])
	begin
		wLY()
	end

'''
		expect = '''Program([FuncDecl(Id(ZxT), [], Return(StringLit(w))), VarDecl(Id(OO), StringType, None, NumLit(25.46)), FuncDecl(Id(wax), [VarDecl(Id(uZ), ArrayType([50.07, 68.08], NumberType), None, None)], Block([CallStmt(Id(wLY), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115071))

	def test_21530115072(self):
		input = '''
number TZXo <- "JvYi"
func GFs6 (bool Bg, number ww[73.14], string lRtt)	return

func GXj8 (bool Nxqu, bool Ca9l, number ZY)	begin
		return false
	end

'''
		expect = '''Program([VarDecl(Id(TZXo), NumberType, None, StringLit(JvYi)), FuncDecl(Id(GFs6), [VarDecl(Id(Bg), BoolType, None, None), VarDecl(Id(ww), ArrayType([73.14], NumberType), None, None), VarDecl(Id(lRtt), StringType, None, None)], Return()), FuncDecl(Id(GXj8), [VarDecl(Id(Nxqu), BoolType, None, None), VarDecl(Id(Ca9l), BoolType, None, None), VarDecl(Id(ZY), NumberType, None, None)], Block([Return(BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115072))

	def test_21530115073(self):
		input = '''
func m3pJ (string d7OX[16.59])	begin
		return 45.35
		bool h7fJ
		begin
			return "SL"
			bool Pkf[66.36,53.12]
			var ky5 <- false
		end
	end
'''
		expect = '''Program([FuncDecl(Id(m3pJ), [VarDecl(Id(d7OX), ArrayType([16.59], StringType), None, None)], Block([Return(NumLit(45.35)), VarDecl(Id(h7fJ), BoolType, None, None), Block([Return(StringLit(SL)), VarDecl(Id(Pkf), ArrayType([66.36, 53.12], BoolType), None, None), VarDecl(Id(ky5), None, var, BooleanLit(False))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115073))

	def test_21530115074(self):
		input = '''
number eNEz[91.63] <- true
func eh (string DK[67.6])	return 24.77
var yDC5 <- 40.67
string MT_[89.45,34.31]
func wFr (number wE)	begin
		if (false) O11n[Omjv] <- 77.63
		elif ("bGr") if (61.64) number nve
		elif (95.81) return "y"
		elif ("NTkWy")
		return
		elif (false) dynamic Qia <- "rgnuk"
		elif (23.57)
		return
		elif (true) begin
			for M3 until false by w6
				var sPTL <- 23.74
		end
		elif (59.26)
		db6i["cuL"] <- "FFSM"
		else gw_ <- "GlK"
	end

'''
		expect = '''Program([VarDecl(Id(eNEz), ArrayType([91.63], NumberType), None, BooleanLit(True)), FuncDecl(Id(eh), [VarDecl(Id(DK), ArrayType([67.6], StringType), None, None)], Return(NumLit(24.77))), VarDecl(Id(yDC5), None, var, NumLit(40.67)), VarDecl(Id(MT_), ArrayType([89.45, 34.31], StringType), None, None), FuncDecl(Id(wFr), [VarDecl(Id(wE), NumberType, None, None)], Block([If(BooleanLit(False), AssignStmt(ArrayCell(Id(O11n), [Id(Omjv)]), NumLit(77.63))), [(StringLit(bGr), If(NumLit(61.64), VarDecl(Id(nve), NumberType, None, None)), [(NumLit(95.81), Return(StringLit(y))), (StringLit(NTkWy), Return()), (BooleanLit(False), VarDecl(Id(Qia), None, dynamic, StringLit(rgnuk))), (NumLit(23.57), Return()), (BooleanLit(True), Block([For(Id(M3), BooleanLit(False), Id(w6), VarDecl(Id(sPTL), None, var, NumLit(23.74)))])), (NumLit(59.26), AssignStmt(ArrayCell(Id(db6i), [StringLit(cuL)]), StringLit(FFSM)))], AssignStmt(Id(gw_), StringLit(GlK)))], None]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115074))

	def test_21530115075(self):
		input = '''
func sk (number ioM, number LSx)
	return QtsM

'''
		expect = '''Program([FuncDecl(Id(sk), [VarDecl(Id(ioM), NumberType, None, None), VarDecl(Id(LSx), NumberType, None, None)], Return(Id(QtsM)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115075))

	def test_21530115076(self):
		input = '''
number HJ[65.45]
func MK (bool oz1t[9.03], bool Xbtf[91.68])
	return

'''
		expect = '''Program([VarDecl(Id(HJ), ArrayType([65.45], NumberType), None, None), FuncDecl(Id(MK), [VarDecl(Id(oz1t), ArrayType([9.03], BoolType), None, None), VarDecl(Id(Xbtf), ArrayType([91.68], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115076))

	def test_21530115077(self):
		input = '''
func uTl4 (number fi0, string dVrh, bool WdmI)
	begin
		break
	end

bool bbv
func D90 ()
	return false
func GsCZ (bool xL)
	return

number xLt[62.92]
'''
		expect = '''Program([FuncDecl(Id(uTl4), [VarDecl(Id(fi0), NumberType, None, None), VarDecl(Id(dVrh), StringType, None, None), VarDecl(Id(WdmI), BoolType, None, None)], Block([Break])), VarDecl(Id(bbv), BoolType, None, None), FuncDecl(Id(D90), [], Return(BooleanLit(False))), FuncDecl(Id(GsCZ), [VarDecl(Id(xL), BoolType, None, None)], Return()), VarDecl(Id(xLt), ArrayType([62.92], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115077))

	def test_21530115078(self):
		input = '''
bool ffPw
func Ji (string X0, bool I1Ok)
	begin
		return
	end

var sS <- 23.23
func iV (string S3wr)	begin
		JFw8("LmLv", true)
	end

func Wfi (number ZZ[65.48,46.05,76.17])	return

'''
		expect = '''Program([VarDecl(Id(ffPw), BoolType, None, None), FuncDecl(Id(Ji), [VarDecl(Id(X0), StringType, None, None), VarDecl(Id(I1Ok), BoolType, None, None)], Block([Return()])), VarDecl(Id(sS), None, var, NumLit(23.23)), FuncDecl(Id(iV), [VarDecl(Id(S3wr), StringType, None, None)], Block([CallStmt(Id(JFw8), [StringLit(LmLv), BooleanLit(True)])])), FuncDecl(Id(Wfi), [VarDecl(Id(ZZ), ArrayType([65.48, 46.05, 76.17], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115078))

	def test_21530115079(self):
		input = '''
func Vb ()	begin
		YO(false, kXd)
		return FUMH
	end
bool No[29.01]
func Gk ()	return 72.27
'''
		expect = '''Program([FuncDecl(Id(Vb), [], Block([CallStmt(Id(YO), [BooleanLit(False), Id(kXd)]), Return(Id(FUMH))])), VarDecl(Id(No), ArrayType([29.01], BoolType), None, None), FuncDecl(Id(Gk), [], Return(NumLit(72.27)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115079))

	def test_21530115080(self):
		input = '''
func WY (bool gS[22.26,54.29], number eVN)
	return

func Qqz (bool No)	return true
'''
		expect = '''Program([FuncDecl(Id(WY), [VarDecl(Id(gS), ArrayType([22.26, 54.29], BoolType), None, None), VarDecl(Id(eVN), NumberType, None, None)], Return()), FuncDecl(Id(Qqz), [VarDecl(Id(No), BoolType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115080))

	def test_21530115081(self):
		input = '''
func OP (bool mM[84.93,92.53,6.11])	return

'''
		expect = '''Program([FuncDecl(Id(OP), [VarDecl(Id(mM), ArrayType([84.93, 92.53, 6.11], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115081))

	def test_21530115082(self):
		input = '''
bool x09V[49.73] <- "Nbke"
'''
		expect = '''Program([VarDecl(Id(x09V), ArrayType([49.73], BoolType), None, StringLit(Nbke))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115082))

	def test_21530115083(self):
		input = '''
string W8x8[69.37]
number CeAz[87.36,39.61]
bool VxH2[96.18,86.77] <- 33.2
'''
		expect = '''Program([VarDecl(Id(W8x8), ArrayType([69.37], StringType), None, None), VarDecl(Id(CeAz), ArrayType([87.36, 39.61], NumberType), None, None), VarDecl(Id(VxH2), ArrayType([96.18, 86.77], BoolType), None, NumLit(33.2))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115083))

	def test_21530115084(self):
		input = '''
bool jmq[91.43] <- gU
string FL
dynamic P4B
func giA (bool miwy[12.93,41.14,59.1], number jdKX[41.17,64.06], bool OY9)
	begin
		continue
		WZT <- true
	end

'''
		expect = '''Program([VarDecl(Id(jmq), ArrayType([91.43], BoolType), None, Id(gU)), VarDecl(Id(FL), StringType, None, None), VarDecl(Id(P4B), None, dynamic, None), FuncDecl(Id(giA), [VarDecl(Id(miwy), ArrayType([12.93, 41.14, 59.1], BoolType), None, None), VarDecl(Id(jdKX), ArrayType([41.17, 64.06], NumberType), None, None), VarDecl(Id(OY9), BoolType, None, None)], Block([Continue, AssignStmt(Id(WZT), BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115084))

	def test_21530115085(self):
		input = '''
func HQa ()	return

func X2aD (string Xq[51.0])
	return true
func uTyS (string ZXqS)	begin
	end

bool cAhI <- Byw
'''
		expect = '''Program([FuncDecl(Id(HQa), [], Return()), FuncDecl(Id(X2aD), [VarDecl(Id(Xq), ArrayType([51.0], StringType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(uTyS), [VarDecl(Id(ZXqS), StringType, None, None)], Block([])), VarDecl(Id(cAhI), BoolType, None, Id(Byw))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115085))

	def test_21530115086(self):
		input = '''
func CM (bool RF_[69.04,77.2], string od)
	return

func wlL8 (string wcHu[87.71], string M6T)
	return "i"
func Xr4 ()
	return
string d_1[69.62,71.32]
'''
		expect = '''Program([FuncDecl(Id(CM), [VarDecl(Id(RF_), ArrayType([69.04, 77.2], BoolType), None, None), VarDecl(Id(od), StringType, None, None)], Return()), FuncDecl(Id(wlL8), [VarDecl(Id(wcHu), ArrayType([87.71], StringType), None, None), VarDecl(Id(M6T), StringType, None, None)], Return(StringLit(i))), FuncDecl(Id(Xr4), [], Return()), VarDecl(Id(d_1), ArrayType([69.62, 71.32], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115086))

	def test_21530115087(self):
		input = '''
number bAYT[60.51,80.98]
string s2H
'''
		expect = '''Program([VarDecl(Id(bAYT), ArrayType([60.51, 80.98], NumberType), None, None), VarDecl(Id(s2H), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115087))

	def test_21530115088(self):
		input = '''
func Ki ()	begin
		begin
			return
			begin
				Dg[fHd, 1.95] <- 90.52
				return "hY"
				break
			end
			break
		end
		continue
		break
	end

number MFcA[94.8,0.81]
'''
		expect = '''Program([FuncDecl(Id(Ki), [], Block([Block([Return(), Block([AssignStmt(ArrayCell(Id(Dg), [Id(fHd), NumLit(1.95)]), NumLit(90.52)), Return(StringLit(hY)), Break]), Break]), Continue, Break])), VarDecl(Id(MFcA), ArrayType([94.8, 0.81], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115088))

	def test_21530115089(self):
		input = '''
number Gv[14.7,22.3]
func Ve (number O9Y, string rLXY[96.55,12.76])	begin
		continue
		break
	end

dynamic eN <- JH
func m2u (number AUB, string pt)
	return "be"

var jB1 <- false
'''
		expect = '''Program([VarDecl(Id(Gv), ArrayType([14.7, 22.3], NumberType), None, None), FuncDecl(Id(Ve), [VarDecl(Id(O9Y), NumberType, None, None), VarDecl(Id(rLXY), ArrayType([96.55, 12.76], StringType), None, None)], Block([Continue, Break])), VarDecl(Id(eN), None, dynamic, Id(JH)), FuncDecl(Id(m2u), [VarDecl(Id(AUB), NumberType, None, None), VarDecl(Id(pt), StringType, None, None)], Return(StringLit(be))), VarDecl(Id(jB1), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115089))

	def test_21530115090(self):
		input = '''
func aUOJ ()
	return true
'''
		expect = '''Program([FuncDecl(Id(aUOJ), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115090))

	def test_21530115091(self):
		input = '''
number E9CR <- false
func t2 (bool fVgi[90.33], bool jNOO, string TvbA)	return "PP"
'''
		expect = '''Program([VarDecl(Id(E9CR), NumberType, None, BooleanLit(False)), FuncDecl(Id(t2), [VarDecl(Id(fVgi), ArrayType([90.33], BoolType), None, None), VarDecl(Id(jNOO), BoolType, None, None), VarDecl(Id(TvbA), StringType, None, None)], Return(StringLit(PP)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115091))

	def test_21530115092(self):
		input = '''
string F5V
'''
		expect = '''Program([VarDecl(Id(F5V), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115092))

	def test_21530115093(self):
		input = '''
bool CcSx <- true
func iO ()
	return rv

number cWQ8
func Ijju (string zHs7, bool MiUO[55.99,63.93], string Vc1C[68.05])
	begin
		bool RSRt[77.09,90.09,4.17]
	end

'''
		expect = '''Program([VarDecl(Id(CcSx), BoolType, None, BooleanLit(True)), FuncDecl(Id(iO), [], Return(Id(rv))), VarDecl(Id(cWQ8), NumberType, None, None), FuncDecl(Id(Ijju), [VarDecl(Id(zHs7), StringType, None, None), VarDecl(Id(MiUO), ArrayType([55.99, 63.93], BoolType), None, None), VarDecl(Id(Vc1C), ArrayType([68.05], StringType), None, None)], Block([VarDecl(Id(RSRt), ArrayType([77.09, 90.09, 4.17], BoolType), None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115093))

	def test_21530115094(self):
		input = '''
number CAKD <- 20.17
'''
		expect = '''Program([VarDecl(Id(CAKD), NumberType, None, NumLit(20.17))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115094))

	def test_21530115095(self):
		input = '''
func FnCi (string Mux[81.46])	begin
	end

string ArWR[56.5,48.6] <- py
func Kc (string t9)
	begin
		break
		t7D["JZLpM"] <- "soWsG"
	end

'''
		expect = '''Program([FuncDecl(Id(FnCi), [VarDecl(Id(Mux), ArrayType([81.46], StringType), None, None)], Block([])), VarDecl(Id(ArWR), ArrayType([56.5, 48.6], StringType), None, Id(py)), FuncDecl(Id(Kc), [VarDecl(Id(t9), StringType, None, None)], Block([Break, AssignStmt(ArrayCell(Id(t7D), [StringLit(JZLpM)]), StringLit(soWsG))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115095))

	def test_21530115096(self):
		input = '''
bool wnYS <- 64.14
func EsMF (bool ihrt[11.6,4.94,2.6], number enG[71.47])
	return

bool u0yG[46.76]
number C506[60.89,38.22,40.24] <- false
string vn <- kpE
'''
		expect = '''Program([VarDecl(Id(wnYS), BoolType, None, NumLit(64.14)), FuncDecl(Id(EsMF), [VarDecl(Id(ihrt), ArrayType([11.6, 4.94, 2.6], BoolType), None, None), VarDecl(Id(enG), ArrayType([71.47], NumberType), None, None)], Return()), VarDecl(Id(u0yG), ArrayType([46.76], BoolType), None, None), VarDecl(Id(C506), ArrayType([60.89, 38.22, 40.24], NumberType), None, BooleanLit(False)), VarDecl(Id(vn), StringType, None, Id(kpE))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115096))

	def test_21530115097(self):
		input = '''
bool IG[32.88,19.69,87.82]
func yUdK ()
	return 37.12
'''
		expect = '''Program([VarDecl(Id(IG), ArrayType([32.88, 19.69, 87.82], BoolType), None, None), FuncDecl(Id(yUdK), [], Return(NumLit(37.12)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115097))

	def test_21530115098(self):
		input = '''
var KB <- true
bool ieP[78.12]
func A7ZC (bool H2, number ObG, bool Z0)
	return 73.65

bool BgeE[45.33]
dynamic q5
'''
		expect = '''Program([VarDecl(Id(KB), None, var, BooleanLit(True)), VarDecl(Id(ieP), ArrayType([78.12], BoolType), None, None), FuncDecl(Id(A7ZC), [VarDecl(Id(H2), BoolType, None, None), VarDecl(Id(ObG), NumberType, None, None), VarDecl(Id(Z0), BoolType, None, None)], Return(NumLit(73.65))), VarDecl(Id(BgeE), ArrayType([45.33], BoolType), None, None), VarDecl(Id(q5), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115098))

	def test_21530115099(self):
		input = '''
func yNua (number J3B, number DMAU, bool L7[43.34,55.63,39.97])	return

var lFO <- "zBKjC"
string C3Ch
bool xlY[99.48,14.5] <- true
'''
		expect = '''Program([FuncDecl(Id(yNua), [VarDecl(Id(J3B), NumberType, None, None), VarDecl(Id(DMAU), NumberType, None, None), VarDecl(Id(L7), ArrayType([43.34, 55.63, 39.97], BoolType), None, None)], Return()), VarDecl(Id(lFO), None, var, StringLit(zBKjC)), VarDecl(Id(C3Ch), StringType, None, None), VarDecl(Id(xlY), ArrayType([99.48, 14.5], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115099))

	def test_21530115100(self):
		input = '''
number KYG[98.33,60.62,8.43]
'''
		expect = '''Program([VarDecl(Id(KYG), ArrayType([98.33, 60.62, 8.43], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115100))

	def test_21530115101(self):
		input = '''
bool tC[29.98] <- "zUr"
number g3RD[61.77,1.48]
func CLCM ()	return

var kD <- true
'''
		expect = '''Program([VarDecl(Id(tC), ArrayType([29.98], BoolType), None, StringLit(zUr)), VarDecl(Id(g3RD), ArrayType([61.77, 1.48], NumberType), None, None), FuncDecl(Id(CLCM), [], Return()), VarDecl(Id(kD), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115101))

	def test_21530115102(self):
		input = '''
func xj (number e7fc[34.62,61.12,15.45], string Qv[60.13,49.88,30.14], string oMMA[54.33,41.01])
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(xj), [VarDecl(Id(e7fc), ArrayType([34.62, 61.12, 15.45], NumberType), None, None), VarDecl(Id(Qv), ArrayType([60.13, 49.88, 30.14], StringType), None, None), VarDecl(Id(oMMA), ArrayType([54.33, 41.01], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115102))

	def test_21530115103(self):
		input = '''
bool Svd <- true
func Zo8M ()
	return "TBY"

func yRK ()
	return true

func oj ()	return
func ZBUZ (number WON, number vL[6.74], number iFB)	return Qc
'''
		expect = '''Program([VarDecl(Id(Svd), BoolType, None, BooleanLit(True)), FuncDecl(Id(Zo8M), [], Return(StringLit(TBY))), FuncDecl(Id(yRK), [], Return(BooleanLit(True))), FuncDecl(Id(oj), [], Return()), FuncDecl(Id(ZBUZ), [VarDecl(Id(WON), NumberType, None, None), VarDecl(Id(vL), ArrayType([6.74], NumberType), None, None), VarDecl(Id(iFB), NumberType, None, None)], Return(Id(Qc)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115103))

	def test_21530115104(self):
		input = '''
number JWoq[30.89]
func XQW (bool YD9[49.07])	return
number EO5_[35.99,61.81,68.87] <- EYM
number jkmk <- false
bool JOh[90.31,36.7] <- "w"
'''
		expect = '''Program([VarDecl(Id(JWoq), ArrayType([30.89], NumberType), None, None), FuncDecl(Id(XQW), [VarDecl(Id(YD9), ArrayType([49.07], BoolType), None, None)], Return()), VarDecl(Id(EO5_), ArrayType([35.99, 61.81, 68.87], NumberType), None, Id(EYM)), VarDecl(Id(jkmk), NumberType, None, BooleanLit(False)), VarDecl(Id(JOh), ArrayType([90.31, 36.7], BoolType), None, StringLit(w))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115104))

	def test_21530115105(self):
		input = '''
number JBr[29.25,79.75,96.86]
'''
		expect = '''Program([VarDecl(Id(JBr), ArrayType([29.25, 79.75, 96.86], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115105))

	def test_21530115106(self):
		input = '''
func wdRs (number Jd4[47.8,22.35], string Tm8)	return

func xqF (number zs[47.69])	return 33.71
number jcGg[43.34]
dynamic EEzz <- "niy"
func F_ (number K3, bool GsK, number gqJ)
	return

'''
		expect = '''Program([FuncDecl(Id(wdRs), [VarDecl(Id(Jd4), ArrayType([47.8, 22.35], NumberType), None, None), VarDecl(Id(Tm8), StringType, None, None)], Return()), FuncDecl(Id(xqF), [VarDecl(Id(zs), ArrayType([47.69], NumberType), None, None)], Return(NumLit(33.71))), VarDecl(Id(jcGg), ArrayType([43.34], NumberType), None, None), VarDecl(Id(EEzz), None, dynamic, StringLit(niy)), FuncDecl(Id(F_), [VarDecl(Id(K3), NumberType, None, None), VarDecl(Id(GsK), BoolType, None, None), VarDecl(Id(gqJ), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115106))

	def test_21530115107(self):
		input = '''
dynamic ulsh
dynamic QT3L <- true
number uejx[16.52,4.7] <- false
string Qz[23.07,96.41]
number k0[52.93,44.45] <- 63.26
'''
		expect = '''Program([VarDecl(Id(ulsh), None, dynamic, None), VarDecl(Id(QT3L), None, dynamic, BooleanLit(True)), VarDecl(Id(uejx), ArrayType([16.52, 4.7], NumberType), None, BooleanLit(False)), VarDecl(Id(Qz), ArrayType([23.07, 96.41], StringType), None, None), VarDecl(Id(k0), ArrayType([52.93, 44.45], NumberType), None, NumLit(63.26))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115107))

	def test_21530115108(self):
		input = '''
func L1E ()
	begin
		GcXL[9.94, false, "cTK"] <- 83.09
		begin
			continue
			lsQJ(true, "mXYc", 11.4)
		end
		qg("JF")
	end

'''
		expect = '''Program([FuncDecl(Id(L1E), [], Block([AssignStmt(ArrayCell(Id(GcXL), [NumLit(9.94), BooleanLit(False), StringLit(cTK)]), NumLit(83.09)), Block([Continue, CallStmt(Id(lsQJ), [BooleanLit(True), StringLit(mXYc), NumLit(11.4)])]), CallStmt(Id(qg), [StringLit(JF)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115108))

	def test_21530115109(self):
		input = '''
func Qae5 ()	return Tm
'''
		expect = '''Program([FuncDecl(Id(Qae5), [], Return(Id(Tm)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115109))

	def test_21530115110(self):
		input = '''
number ylF[23.73,18.82] <- "CV"
'''
		expect = '''Program([VarDecl(Id(ylF), ArrayType([23.73, 18.82], NumberType), None, StringLit(CV))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115110))

	def test_21530115111(self):
		input = '''
number mm[61.9,18.13] <- false
func XPr1 (bool ZZk[86.51], number pBT, bool RY[30.57,66.24])	return false

func Mqyh ()
	return

'''
		expect = '''Program([VarDecl(Id(mm), ArrayType([61.9, 18.13], NumberType), None, BooleanLit(False)), FuncDecl(Id(XPr1), [VarDecl(Id(ZZk), ArrayType([86.51], BoolType), None, None), VarDecl(Id(pBT), NumberType, None, None), VarDecl(Id(RY), ArrayType([30.57, 66.24], BoolType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(Mqyh), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115111))

	def test_21530115112(self):
		input = '''
func kc (number NKV, number fi[19.78,83.65,92.18], bool rJe[34.39])
	return
bool JEk[23.58,93.91,22.65]
func S9 (number Szu, number fnDM)
	begin
		bool OUt[45.69] <- mvym
		begin
			for jB0Q until 33.01 by "uU"
				N4[vpb_, false] <- abC2
			continue
		end
		if (11.8)
		continue
		elif (xmf)
		return
	end

'''
		expect = '''Program([FuncDecl(Id(kc), [VarDecl(Id(NKV), NumberType, None, None), VarDecl(Id(fi), ArrayType([19.78, 83.65, 92.18], NumberType), None, None), VarDecl(Id(rJe), ArrayType([34.39], BoolType), None, None)], Return()), VarDecl(Id(JEk), ArrayType([23.58, 93.91, 22.65], BoolType), None, None), FuncDecl(Id(S9), [VarDecl(Id(Szu), NumberType, None, None), VarDecl(Id(fnDM), NumberType, None, None)], Block([VarDecl(Id(OUt), ArrayType([45.69], BoolType), None, Id(mvym)), Block([For(Id(jB0Q), NumLit(33.01), StringLit(uU), AssignStmt(ArrayCell(Id(N4), [Id(vpb_), BooleanLit(False)]), Id(abC2))), Continue]), If(NumLit(11.8), Continue), [(Id(xmf), Return())], None]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115112))

	def test_21530115113(self):
		input = '''
string kU <- "gARq"
var ubWF <- false
func wm ()
	return "Viik"
bool LL0 <- addD
'''
		expect = '''Program([VarDecl(Id(kU), StringType, None, StringLit(gARq)), VarDecl(Id(ubWF), None, var, BooleanLit(False)), FuncDecl(Id(wm), [], Return(StringLit(Viik))), VarDecl(Id(LL0), BoolType, None, Id(addD))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115113))

	def test_21530115114(self):
		input = '''
string UQx[6.35,69.67,75.65] <- true
func Za (bool fsYT[30.0], number Y1[34.96,2.89], number IO)	return true

func dQI (bool mw[65.82,80.26])	return 48.29
number wC <- true
func o0jg ()
	return

'''
		expect = '''Program([VarDecl(Id(UQx), ArrayType([6.35, 69.67, 75.65], StringType), None, BooleanLit(True)), FuncDecl(Id(Za), [VarDecl(Id(fsYT), ArrayType([30.0], BoolType), None, None), VarDecl(Id(Y1), ArrayType([34.96, 2.89], NumberType), None, None), VarDecl(Id(IO), NumberType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(dQI), [VarDecl(Id(mw), ArrayType([65.82, 80.26], BoolType), None, None)], Return(NumLit(48.29))), VarDecl(Id(wC), NumberType, None, BooleanLit(True)), FuncDecl(Id(o0jg), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115114))

	def test_21530115115(self):
		input = '''
func OwV (string oUMx[75.61,70.46,66.35], bool Se[74.39])	return

'''
		expect = '''Program([FuncDecl(Id(OwV), [VarDecl(Id(oUMx), ArrayType([75.61, 70.46, 66.35], StringType), None, None), VarDecl(Id(Se), ArrayType([74.39], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115115))

	def test_21530115116(self):
		input = '''
func YOhl (number g2[62.5], bool I7, string NZ)
	return

var u3 <- 10.07
func CJ (number ex, bool Yi, bool I3G9[4.18,3.09])	return

bool Kz[86.67,68.33] <- aS
func Y98 (number Hib, bool vHh)
	return

'''
		expect = '''Program([FuncDecl(Id(YOhl), [VarDecl(Id(g2), ArrayType([62.5], NumberType), None, None), VarDecl(Id(I7), BoolType, None, None), VarDecl(Id(NZ), StringType, None, None)], Return()), VarDecl(Id(u3), None, var, NumLit(10.07)), FuncDecl(Id(CJ), [VarDecl(Id(ex), NumberType, None, None), VarDecl(Id(Yi), BoolType, None, None), VarDecl(Id(I3G9), ArrayType([4.18, 3.09], BoolType), None, None)], Return()), VarDecl(Id(Kz), ArrayType([86.67, 68.33], BoolType), None, Id(aS)), FuncDecl(Id(Y98), [VarDecl(Id(Hib), NumberType, None, None), VarDecl(Id(vHh), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115116))

	def test_21530115117(self):
		input = '''
number gTy
func X0u0 (bool gTdL[20.57,82.33,95.17], string tGB)
	return

func hd ()
	begin
		continue
		break
		break
	end
number i4 <- nOw
func yIv (number p8bx, string ot)
	begin
	end
'''
		expect = '''Program([VarDecl(Id(gTy), NumberType, None, None), FuncDecl(Id(X0u0), [VarDecl(Id(gTdL), ArrayType([20.57, 82.33, 95.17], BoolType), None, None), VarDecl(Id(tGB), StringType, None, None)], Return()), FuncDecl(Id(hd), [], Block([Continue, Break, Break])), VarDecl(Id(i4), NumberType, None, Id(nOw)), FuncDecl(Id(yIv), [VarDecl(Id(p8bx), NumberType, None, None), VarDecl(Id(ot), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115117))

	def test_21530115118(self):
		input = '''
var yoP <- false
'''
		expect = '''Program([VarDecl(Id(yoP), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115118))

	def test_21530115119(self):
		input = '''
string X2R <- lum
string Ru[88.69]
dynamic Q9
'''
		expect = '''Program([VarDecl(Id(X2R), StringType, None, Id(lum)), VarDecl(Id(Ru), ArrayType([88.69], StringType), None, None), VarDecl(Id(Q9), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115119))

	def test_21530115120(self):
		input = '''
func XgoM (bool foS)	begin
	end
'''
		expect = '''Program([FuncDecl(Id(XgoM), [VarDecl(Id(foS), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115120))

	def test_21530115121(self):
		input = '''
var O_nq <- 41.18
func vq ()
	return

'''
		expect = '''Program([VarDecl(Id(O_nq), None, var, NumLit(41.18)), FuncDecl(Id(vq), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115121))

	def test_21530115122(self):
		input = '''
func cy12 ()	return

bool nB8w[6.3,27.06]
func yM (string piCk, string Bq7[86.27,95.12])
	begin
		break
	end
'''
		expect = '''Program([FuncDecl(Id(cy12), [], Return()), VarDecl(Id(nB8w), ArrayType([6.3, 27.06], BoolType), None, None), FuncDecl(Id(yM), [VarDecl(Id(piCk), StringType, None, None), VarDecl(Id(Bq7), ArrayType([86.27, 95.12], StringType), None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115122))

	def test_21530115123(self):
		input = '''
func sF (bool yAvx[30.4,20.7])
	return
func hdJ (number Cq[74.35,8.2,40.45], bool NVDs[0.81], bool mL[56.68,17.23,36.28])	begin
	end

number ID[97.1,39.27]
'''
		expect = '''Program([FuncDecl(Id(sF), [VarDecl(Id(yAvx), ArrayType([30.4, 20.7], BoolType), None, None)], Return()), FuncDecl(Id(hdJ), [VarDecl(Id(Cq), ArrayType([74.35, 8.2, 40.45], NumberType), None, None), VarDecl(Id(NVDs), ArrayType([0.81], BoolType), None, None), VarDecl(Id(mL), ArrayType([56.68, 17.23, 36.28], BoolType), None, None)], Block([])), VarDecl(Id(ID), ArrayType([97.1, 39.27], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115123))

	def test_21530115124(self):
		input = '''
func Kog (bool Rj, bool Kt8u, number M5jh[11.49,74.75,99.59])	return

'''
		expect = '''Program([FuncDecl(Id(Kog), [VarDecl(Id(Rj), BoolType, None, None), VarDecl(Id(Kt8u), BoolType, None, None), VarDecl(Id(M5jh), ArrayType([11.49, 74.75, 99.59], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115124))

	def test_21530115125(self):
		input = '''
func zM (number sdpE[87.8], string QvC, string wlL)
	return

var B2b <- 71.1
string vu
func zlO8 (string eYm)
	return

'''
		expect = '''Program([FuncDecl(Id(zM), [VarDecl(Id(sdpE), ArrayType([87.8], NumberType), None, None), VarDecl(Id(QvC), StringType, None, None), VarDecl(Id(wlL), StringType, None, None)], Return()), VarDecl(Id(B2b), None, var, NumLit(71.1)), VarDecl(Id(vu), StringType, None, None), FuncDecl(Id(zlO8), [VarDecl(Id(eYm), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115125))

	def test_21530115126(self):
		input = '''
func taag (bool uBb[24.29,46.84,41.18], string TRur[75.32,10.22], number b31)	return
'''
		expect = '''Program([FuncDecl(Id(taag), [VarDecl(Id(uBb), ArrayType([24.29, 46.84, 41.18], BoolType), None, None), VarDecl(Id(TRur), ArrayType([75.32, 10.22], StringType), None, None), VarDecl(Id(b31), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115126))

	def test_21530115127(self):
		input = '''
func kIVd (string knd[24.73], number EE, number r73)
	return "CtjZH"
func GI ()
	return false

func pQ ()
	return Wsb7
func DY ()	begin
		if (CrRY)
		for SN3v until "fmvV" by 74.6
			obk <- "gOj"
	end
bool rR9[47.83,9.04,7.3]
'''
		expect = '''Program([FuncDecl(Id(kIVd), [VarDecl(Id(knd), ArrayType([24.73], StringType), None, None), VarDecl(Id(EE), NumberType, None, None), VarDecl(Id(r73), NumberType, None, None)], Return(StringLit(CtjZH))), FuncDecl(Id(GI), [], Return(BooleanLit(False))), FuncDecl(Id(pQ), [], Return(Id(Wsb7))), FuncDecl(Id(DY), [], Block([If(Id(CrRY), For(Id(SN3v), StringLit(fmvV), NumLit(74.6), AssignStmt(Id(obk), StringLit(gOj)))), [], None])), VarDecl(Id(rR9), ArrayType([47.83, 9.04, 7.3], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115127))

	def test_21530115128(self):
		input = '''
var MAX <- "FLLT"
string aj[25.39]
string gg48 <- dq
func wYIN (number tGMj[44.94,97.29,54.27], string sm, number lEk[38.56,58.92])	return "H"
'''
		expect = '''Program([VarDecl(Id(MAX), None, var, StringLit(FLLT)), VarDecl(Id(aj), ArrayType([25.39], StringType), None, None), VarDecl(Id(gg48), StringType, None, Id(dq)), FuncDecl(Id(wYIN), [VarDecl(Id(tGMj), ArrayType([44.94, 97.29, 54.27], NumberType), None, None), VarDecl(Id(sm), StringType, None, None), VarDecl(Id(lEk), ArrayType([38.56, 58.92], NumberType), None, None)], Return(StringLit(H)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115128))

	def test_21530115129(self):
		input = '''
func h6vY ()	return "fMiek"

func hA (string GbZ[79.98])	return
number VLvs[39.23]
func MT (bool pid, bool fg)	return 50.35

bool tS <- Zkd
'''
		expect = '''Program([FuncDecl(Id(h6vY), [], Return(StringLit(fMiek))), FuncDecl(Id(hA), [VarDecl(Id(GbZ), ArrayType([79.98], StringType), None, None)], Return()), VarDecl(Id(VLvs), ArrayType([39.23], NumberType), None, None), FuncDecl(Id(MT), [VarDecl(Id(pid), BoolType, None, None), VarDecl(Id(fg), BoolType, None, None)], Return(NumLit(50.35))), VarDecl(Id(tS), BoolType, None, Id(Zkd))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115129))

	def test_21530115130(self):
		input = '''
bool fHf[18.3]
func EW1 (number wC[6.51], string JR, bool Wm8[13.44])
	return "wpX"
string EygN[39.54,28.79,60.06]
string ab[84.48,64.25,61.38]
'''
		expect = '''Program([VarDecl(Id(fHf), ArrayType([18.3], BoolType), None, None), FuncDecl(Id(EW1), [VarDecl(Id(wC), ArrayType([6.51], NumberType), None, None), VarDecl(Id(JR), StringType, None, None), VarDecl(Id(Wm8), ArrayType([13.44], BoolType), None, None)], Return(StringLit(wpX))), VarDecl(Id(EygN), ArrayType([39.54, 28.79, 60.06], StringType), None, None), VarDecl(Id(ab), ArrayType([84.48, 64.25, 61.38], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115130))

	def test_21530115131(self):
		input = '''
func z82 (string Bc, string Lb, bool p0_t[44.43])	begin
		if (14.69)
		begin
			eF(ok_, false, "e")
			if (20.58)
			begin
				continue
				bYE(true, "z", 26.94)
				for Fb3 until Qn by false
					string m9[54.38]
			end
			elif (29.14) continue
			elif (QX) ke_(iiw)
			elif (42.43)
			H8z("wEXE", 98.97, "av")
			elif ("MsxW") v7e[false, 7.4] <- "y"
			elif (false) Gy(73.87)
			for kms until "n" by false
				for JUt until Nm0 by true
					break
		end
		elif (k5) for Zv4X until "t" by 76.97
			break
		elif (Qff) continue
		bool CC[93.73,91.3,68.93]
	end
dynamic hJDI <- bh
string X5[28.4,13.45] <- "o"
'''
		expect = '''Program([FuncDecl(Id(z82), [VarDecl(Id(Bc), StringType, None, None), VarDecl(Id(Lb), StringType, None, None), VarDecl(Id(p0_t), ArrayType([44.43], BoolType), None, None)], Block([If(NumLit(14.69), Block([CallStmt(Id(eF), [Id(ok_), BooleanLit(False), StringLit(e)]), If(NumLit(20.58), Block([Continue, CallStmt(Id(bYE), [BooleanLit(True), StringLit(z), NumLit(26.94)]), For(Id(Fb3), Id(Qn), BooleanLit(False), VarDecl(Id(m9), ArrayType([54.38], StringType), None, None))])), [(NumLit(29.14), Continue), (Id(QX), CallStmt(Id(ke_), [Id(iiw)])), (NumLit(42.43), CallStmt(Id(H8z), [StringLit(wEXE), NumLit(98.97), StringLit(av)])), (StringLit(MsxW), AssignStmt(ArrayCell(Id(v7e), [BooleanLit(False), NumLit(7.4)]), StringLit(y))), (BooleanLit(False), CallStmt(Id(Gy), [NumLit(73.87)]))], None, For(Id(kms), StringLit(n), BooleanLit(False), For(Id(JUt), Id(Nm0), BooleanLit(True), Break))])), [(Id(k5), For(Id(Zv4X), StringLit(t), NumLit(76.97), Break)), (Id(Qff), Continue)], None, VarDecl(Id(CC), ArrayType([93.73, 91.3, 68.93], BoolType), None, None)])), VarDecl(Id(hJDI), None, dynamic, Id(bh)), VarDecl(Id(X5), ArrayType([28.4, 13.45], StringType), None, StringLit(o))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115131))

	def test_21530115132(self):
		input = '''
dynamic O57S
var MCgs <- XI
'''
		expect = '''Program([VarDecl(Id(O57S), None, dynamic, None), VarDecl(Id(MCgs), None, var, Id(XI))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115132))

	def test_21530115133(self):
		input = '''
var simZ <- false
'''
		expect = '''Program([VarDecl(Id(simZ), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115133))

	def test_21530115134(self):
		input = '''
func u1A (number cVP[70.22], string WI[23.39], string tF[53.53,43.12])
	return "vjJ"

number qK <- fq8
func eaY8 (number If, number ppBE)
	begin
		continue
	end
func dTo6 (string LK[80.53,80.74,49.69])	return 44.4

'''
		expect = '''Program([FuncDecl(Id(u1A), [VarDecl(Id(cVP), ArrayType([70.22], NumberType), None, None), VarDecl(Id(WI), ArrayType([23.39], StringType), None, None), VarDecl(Id(tF), ArrayType([53.53, 43.12], StringType), None, None)], Return(StringLit(vjJ))), VarDecl(Id(qK), NumberType, None, Id(fq8)), FuncDecl(Id(eaY8), [VarDecl(Id(If), NumberType, None, None), VarDecl(Id(ppBE), NumberType, None, None)], Block([Continue])), FuncDecl(Id(dTo6), [VarDecl(Id(LK), ArrayType([80.53, 80.74, 49.69], StringType), None, None)], Return(NumLit(44.4)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115134))

	def test_21530115135(self):
		input = '''
func DkSD (string US0e[11.88], bool K1[8.67], number NH_h)	begin
	end

'''
		expect = '''Program([FuncDecl(Id(DkSD), [VarDecl(Id(US0e), ArrayType([11.88], StringType), None, None), VarDecl(Id(K1), ArrayType([8.67], BoolType), None, None), VarDecl(Id(NH_h), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115135))

	def test_21530115136(self):
		input = '''
bool ubfQ <- 14.43
number hr[46.82,58.75,46.34] <- m4
func btS (bool DwW)
	return "eKjoT"

bool Rexu[87.18] <- MtN
'''
		expect = '''Program([VarDecl(Id(ubfQ), BoolType, None, NumLit(14.43)), VarDecl(Id(hr), ArrayType([46.82, 58.75, 46.34], NumberType), None, Id(m4)), FuncDecl(Id(btS), [VarDecl(Id(DwW), BoolType, None, None)], Return(StringLit(eKjoT))), VarDecl(Id(Rexu), ArrayType([87.18], BoolType), None, Id(MtN))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115136))

	def test_21530115137(self):
		input = '''
func kt (number JSgh[49.27,48.7,13.86])	return

string er[39.49,10.3,10.16]
dynamic nv
bool k9rW <- "yyOuR"
bool ak_[39.88,35.97]
'''
		expect = '''Program([FuncDecl(Id(kt), [VarDecl(Id(JSgh), ArrayType([49.27, 48.7, 13.86], NumberType), None, None)], Return()), VarDecl(Id(er), ArrayType([39.49, 10.3, 10.16], StringType), None, None), VarDecl(Id(nv), None, dynamic, None), VarDecl(Id(k9rW), BoolType, None, StringLit(yyOuR)), VarDecl(Id(ak_), ArrayType([39.88, 35.97], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115137))

	def test_21530115138(self):
		input = '''
func SzJ ()
	return 94.16
func n4 ()	begin
		for uS7q until 51.41 by "RKSFt"
			number gXFT[36.01,1.62,17.13]
		T3y()
		continue
	end

'''
		expect = '''Program([FuncDecl(Id(SzJ), [], Return(NumLit(94.16))), FuncDecl(Id(n4), [], Block([For(Id(uS7q), NumLit(51.41), StringLit(RKSFt), VarDecl(Id(gXFT), ArrayType([36.01, 1.62, 17.13], NumberType), None, None)), CallStmt(Id(T3y), []), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115138))

	def test_21530115139(self):
		input = '''
number GQqV
'''
		expect = '''Program([VarDecl(Id(GQqV), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115139))

	def test_21530115140(self):
		input = '''
func aMI (bool DJv[79.89], number TFYa)
	return
func S7 (bool ZBaU, bool vUg[92.53,35.3,47.0])	return 65.47

number HZkg[6.49]
'''
		expect = '''Program([FuncDecl(Id(aMI), [VarDecl(Id(DJv), ArrayType([79.89], BoolType), None, None), VarDecl(Id(TFYa), NumberType, None, None)], Return()), FuncDecl(Id(S7), [VarDecl(Id(ZBaU), BoolType, None, None), VarDecl(Id(vUg), ArrayType([92.53, 35.3, 47.0], BoolType), None, None)], Return(NumLit(65.47))), VarDecl(Id(HZkg), ArrayType([6.49], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115140))

	def test_21530115141(self):
		input = '''
bool bv
string Zac9 <- false
'''
		expect = '''Program([VarDecl(Id(bv), BoolType, None, None), VarDecl(Id(Zac9), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115141))

	def test_21530115142(self):
		input = '''
func Zc (bool UqFu[28.1], bool pmv[74.05], bool xKf[0.69,70.25,35.74])	return lv4

func r2eI ()	return "rJ"

func HT ()	return "jL"

'''
		expect = '''Program([FuncDecl(Id(Zc), [VarDecl(Id(UqFu), ArrayType([28.1], BoolType), None, None), VarDecl(Id(pmv), ArrayType([74.05], BoolType), None, None), VarDecl(Id(xKf), ArrayType([0.69, 70.25, 35.74], BoolType), None, None)], Return(Id(lv4))), FuncDecl(Id(r2eI), [], Return(StringLit(rJ))), FuncDecl(Id(HT), [], Return(StringLit(jL)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115142))

	def test_21530115143(self):
		input = '''
func YzL (number aNuA[79.67,63.29,47.76])
	return true
func aCLQ (number HT3, string XXt, bool WV5[76.66])
	return 22.42

number Fc[1.82,38.6]
func BM ()	begin
		for gZ until akC by "J"
			break
		begin
			if (23.62) begin
			end
		end
		break
	end
func SX (string uI[47.45,57.5])
	return PLh

'''
		expect = '''Program([FuncDecl(Id(YzL), [VarDecl(Id(aNuA), ArrayType([79.67, 63.29, 47.76], NumberType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(aCLQ), [VarDecl(Id(HT3), NumberType, None, None), VarDecl(Id(XXt), StringType, None, None), VarDecl(Id(WV5), ArrayType([76.66], BoolType), None, None)], Return(NumLit(22.42))), VarDecl(Id(Fc), ArrayType([1.82, 38.6], NumberType), None, None), FuncDecl(Id(BM), [], Block([For(Id(gZ), Id(akC), StringLit(J), Break), Block([If(NumLit(23.62), Block([])), [], None]), Break])), FuncDecl(Id(SX), [VarDecl(Id(uI), ArrayType([47.45, 57.5], StringType), None, None)], Return(Id(PLh)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115143))

	def test_21530115144(self):
		input = '''
func NTL (string U3Ue, string jEp)	return

number ERPl[97.69,63.29,78.16] <- 96.68
func Z1N (number V7u, string ejnV[24.13,29.47], string Uu[69.57])
	begin
		return "ZbL"
	end
func ZM (string CM[38.19,37.72])
	return

'''
		expect = '''Program([FuncDecl(Id(NTL), [VarDecl(Id(U3Ue), StringType, None, None), VarDecl(Id(jEp), StringType, None, None)], Return()), VarDecl(Id(ERPl), ArrayType([97.69, 63.29, 78.16], NumberType), None, NumLit(96.68)), FuncDecl(Id(Z1N), [VarDecl(Id(V7u), NumberType, None, None), VarDecl(Id(ejnV), ArrayType([24.13, 29.47], StringType), None, None), VarDecl(Id(Uu), ArrayType([69.57], StringType), None, None)], Block([Return(StringLit(ZbL))])), FuncDecl(Id(ZM), [VarDecl(Id(CM), ArrayType([38.19, 37.72], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115144))

	def test_21530115145(self):
		input = '''
var AmQE <- true
func MN (string pT3[77.95,14.9,35.72])	return

'''
		expect = '''Program([VarDecl(Id(AmQE), None, var, BooleanLit(True)), FuncDecl(Id(MN), [VarDecl(Id(pT3), ArrayType([77.95, 14.9, 35.72], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115145))

	def test_21530115146(self):
		input = '''
func zOAB (string Vc3[40.34,58.93], string OGis[89.76], string h6[83.08,33.41])
	return
'''
		expect = '''Program([FuncDecl(Id(zOAB), [VarDecl(Id(Vc3), ArrayType([40.34, 58.93], StringType), None, None), VarDecl(Id(OGis), ArrayType([89.76], StringType), None, None), VarDecl(Id(h6), ArrayType([83.08, 33.41], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115146))

	def test_21530115147(self):
		input = '''
func ZZ (bool xdUl)
	return G8e
func aoc (number a6K, string elZ, number Y0Y[51.28,77.88,95.37])
	return
func oHXx (bool YnU6[48.26,59.14], bool UTb[93.19,88.48], string Uo)	return false
'''
		expect = '''Program([FuncDecl(Id(ZZ), [VarDecl(Id(xdUl), BoolType, None, None)], Return(Id(G8e))), FuncDecl(Id(aoc), [VarDecl(Id(a6K), NumberType, None, None), VarDecl(Id(elZ), StringType, None, None), VarDecl(Id(Y0Y), ArrayType([51.28, 77.88, 95.37], NumberType), None, None)], Return()), FuncDecl(Id(oHXx), [VarDecl(Id(YnU6), ArrayType([48.26, 59.14], BoolType), None, None), VarDecl(Id(UTb), ArrayType([93.19, 88.48], BoolType), None, None), VarDecl(Id(Uo), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115147))

	def test_21530115148(self):
		input = '''
string BVxw[94.28,73.41,84.95]
func jeoY (string qM2, number h7_[47.72,94.56])
	begin
	end
number JCu[40.14,77.05] <- 21.26
func Xn4 ()	return

'''
		expect = '''Program([VarDecl(Id(BVxw), ArrayType([94.28, 73.41, 84.95], StringType), None, None), FuncDecl(Id(jeoY), [VarDecl(Id(qM2), StringType, None, None), VarDecl(Id(h7_), ArrayType([47.72, 94.56], NumberType), None, None)], Block([])), VarDecl(Id(JCu), ArrayType([40.14, 77.05], NumberType), None, NumLit(21.26)), FuncDecl(Id(Xn4), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115148))

	def test_21530115149(self):
		input = '''
func qusg (number e6)
	return iGM
func ZJT (bool EGcG, bool lL, number DlL[13.85])
	return
func rJKu (number a7wY[61.93], number H8W[62.36], string m2)
	begin
		dM <- fm7w
		return
		J1[M4, true] <- "in"
	end

number OKa <- false
var dJ <- hA
'''
		expect = '''Program([FuncDecl(Id(qusg), [VarDecl(Id(e6), NumberType, None, None)], Return(Id(iGM))), FuncDecl(Id(ZJT), [VarDecl(Id(EGcG), BoolType, None, None), VarDecl(Id(lL), BoolType, None, None), VarDecl(Id(DlL), ArrayType([13.85], NumberType), None, None)], Return()), FuncDecl(Id(rJKu), [VarDecl(Id(a7wY), ArrayType([61.93], NumberType), None, None), VarDecl(Id(H8W), ArrayType([62.36], NumberType), None, None), VarDecl(Id(m2), StringType, None, None)], Block([AssignStmt(Id(dM), Id(fm7w)), Return(), AssignStmt(ArrayCell(Id(J1), [Id(M4), BooleanLit(True)]), StringLit(in))])), VarDecl(Id(OKa), NumberType, None, BooleanLit(False)), VarDecl(Id(dJ), None, var, Id(hA))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115149))

	def test_21530115150(self):
		input = '''
func Ya (bool Ez[35.4,40.84], bool nvo)	return true

dynamic MYrR <- jN
'''
		expect = '''Program([FuncDecl(Id(Ya), [VarDecl(Id(Ez), ArrayType([35.4, 40.84], BoolType), None, None), VarDecl(Id(nvo), BoolType, None, None)], Return(BooleanLit(True))), VarDecl(Id(MYrR), None, dynamic, Id(jN))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115150))

	def test_21530115151(self):
		input = '''
var AcN <- 14.81
'''
		expect = '''Program([VarDecl(Id(AcN), None, var, NumLit(14.81))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115151))

	def test_21530115152(self):
		input = '''
string Ul
'''
		expect = '''Program([VarDecl(Id(Ul), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115152))

	def test_21530115153(self):
		input = '''
func F2 (number RlA[22.37,98.8], number g2g[92.5,40.53,17.35], number O1Z)	return

'''
		expect = '''Program([FuncDecl(Id(F2), [VarDecl(Id(RlA), ArrayType([22.37, 98.8], NumberType), None, None), VarDecl(Id(g2g), ArrayType([92.5, 40.53, 17.35], NumberType), None, None), VarDecl(Id(O1Z), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115153))

	def test_21530115154(self):
		input = '''
func r1 (bool QwNO, number eg[12.64,26.3])	return true

'''
		expect = '''Program([FuncDecl(Id(r1), [VarDecl(Id(QwNO), BoolType, None, None), VarDecl(Id(eg), ArrayType([12.64, 26.3], NumberType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115154))

	def test_21530115155(self):
		input = '''
number RibW
'''
		expect = '''Program([VarDecl(Id(RibW), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115155))

	def test_21530115156(self):
		input = '''
func tAZi (string DgYx[62.56,88.65], string vxwz[42.58])
	return "kE"

func L2 (number kl[43.66,65.23,51.92], bool QE, number yNoK[18.0,44.34,98.37])	return

'''
		expect = '''Program([FuncDecl(Id(tAZi), [VarDecl(Id(DgYx), ArrayType([62.56, 88.65], StringType), None, None), VarDecl(Id(vxwz), ArrayType([42.58], StringType), None, None)], Return(StringLit(kE))), FuncDecl(Id(L2), [VarDecl(Id(kl), ArrayType([43.66, 65.23, 51.92], NumberType), None, None), VarDecl(Id(QE), BoolType, None, None), VarDecl(Id(yNoK), ArrayType([18.0, 44.34, 98.37], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115156))

	def test_21530115157(self):
		input = '''
bool qyc
number GO
var oYc <- "JwQi"
func GTQ2 ()
	return

func bw (number Rfn[82.24], number CC[55.56])	return Kfi
'''
		expect = '''Program([VarDecl(Id(qyc), BoolType, None, None), VarDecl(Id(GO), NumberType, None, None), VarDecl(Id(oYc), None, var, StringLit(JwQi)), FuncDecl(Id(GTQ2), [], Return()), FuncDecl(Id(bw), [VarDecl(Id(Rfn), ArrayType([82.24], NumberType), None, None), VarDecl(Id(CC), ArrayType([55.56], NumberType), None, None)], Return(Id(Kfi)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115157))

	def test_21530115158(self):
		input = '''
func MKg0 ()
	return

dynamic aN_
bool OB[56.56,66.76,72.86] <- "U"
'''
		expect = '''Program([FuncDecl(Id(MKg0), [], Return()), VarDecl(Id(aN_), None, dynamic, None), VarDecl(Id(OB), ArrayType([56.56, 66.76, 72.86], BoolType), None, StringLit(U))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115158))

	def test_21530115159(self):
		input = '''
func P9Yd (string kgT, string HKm, bool ZC[76.15,88.63])	return

func voV (bool OQLd, bool j2[93.29])	return

func zHwm ()
	return uKg
'''
		expect = '''Program([FuncDecl(Id(P9Yd), [VarDecl(Id(kgT), StringType, None, None), VarDecl(Id(HKm), StringType, None, None), VarDecl(Id(ZC), ArrayType([76.15, 88.63], BoolType), None, None)], Return()), FuncDecl(Id(voV), [VarDecl(Id(OQLd), BoolType, None, None), VarDecl(Id(j2), ArrayType([93.29], BoolType), None, None)], Return()), FuncDecl(Id(zHwm), [], Return(Id(uKg)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115159))

	def test_21530115160(self):
		input = '''
func Qfz (string f2, string KW3, string vI9m)
	return true
'''
		expect = '''Program([FuncDecl(Id(Qfz), [VarDecl(Id(f2), StringType, None, None), VarDecl(Id(KW3), StringType, None, None), VarDecl(Id(vI9m), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115160))

	def test_21530115161(self):
		input = '''
func JJO_ (number wRao[64.77,33.46,49.93], bool gu)	return

func m1 (string Xac[17.22,1.76], bool WKe)	return "Dgn"
dynamic dBCI
func cy0o (bool rT)	return
bool jO[55.78,6.46,98.84] <- xan
'''
		expect = '''Program([FuncDecl(Id(JJO_), [VarDecl(Id(wRao), ArrayType([64.77, 33.46, 49.93], NumberType), None, None), VarDecl(Id(gu), BoolType, None, None)], Return()), FuncDecl(Id(m1), [VarDecl(Id(Xac), ArrayType([17.22, 1.76], StringType), None, None), VarDecl(Id(WKe), BoolType, None, None)], Return(StringLit(Dgn))), VarDecl(Id(dBCI), None, dynamic, None), FuncDecl(Id(cy0o), [VarDecl(Id(rT), BoolType, None, None)], Return()), VarDecl(Id(jO), ArrayType([55.78, 6.46, 98.84], BoolType), None, Id(xan))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115161))

	def test_21530115162(self):
		input = '''
func Ks (bool Xo)	begin
	end
func CedC (number amEI, number BYC[50.99,14.23])
	begin
		string Imfi[25.36] <- false
		V7 <- xf
	end

number XD6[93.87] <- 60.22
bool RF[83.67,67.59]
func Bw (string LRx)	return
'''
		expect = '''Program([FuncDecl(Id(Ks), [VarDecl(Id(Xo), BoolType, None, None)], Block([])), FuncDecl(Id(CedC), [VarDecl(Id(amEI), NumberType, None, None), VarDecl(Id(BYC), ArrayType([50.99, 14.23], NumberType), None, None)], Block([VarDecl(Id(Imfi), ArrayType([25.36], StringType), None, BooleanLit(False)), AssignStmt(Id(V7), Id(xf))])), VarDecl(Id(XD6), ArrayType([93.87], NumberType), None, NumLit(60.22)), VarDecl(Id(RF), ArrayType([83.67, 67.59], BoolType), None, None), FuncDecl(Id(Bw), [VarDecl(Id(LRx), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115162))

	def test_21530115163(self):
		input = '''
func B_t ()	return

func Vs (number vdw)
	return true
bool BFK[31.35,0.95]
'''
		expect = '''Program([FuncDecl(Id(B_t), [], Return()), FuncDecl(Id(Vs), [VarDecl(Id(vdw), NumberType, None, None)], Return(BooleanLit(True))), VarDecl(Id(BFK), ArrayType([31.35, 0.95], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115163))

	def test_21530115164(self):
		input = '''
func Uk (number r8fK[33.32,8.83,95.28], bool GVK[17.28,45.55,88.82], string dU[46.49])	return 9.97

number W4[2.54,91.53] <- Gn
number SRc6[98.64,62.63] <- "kT"
func Ky (string pyxL[48.05,9.57,27.3], string aOe, string NV)
	return "DgS"

func Pf5 ()
	begin
		nnaO(e4n)
		if (false)
		number mMYH[33.87,10.95] <- "A"
		elif ("Ix")
		JZp <- eGfi
	end

'''
		expect = '''Program([FuncDecl(Id(Uk), [VarDecl(Id(r8fK), ArrayType([33.32, 8.83, 95.28], NumberType), None, None), VarDecl(Id(GVK), ArrayType([17.28, 45.55, 88.82], BoolType), None, None), VarDecl(Id(dU), ArrayType([46.49], StringType), None, None)], Return(NumLit(9.97))), VarDecl(Id(W4), ArrayType([2.54, 91.53], NumberType), None, Id(Gn)), VarDecl(Id(SRc6), ArrayType([98.64, 62.63], NumberType), None, StringLit(kT)), FuncDecl(Id(Ky), [VarDecl(Id(pyxL), ArrayType([48.05, 9.57, 27.3], StringType), None, None), VarDecl(Id(aOe), StringType, None, None), VarDecl(Id(NV), StringType, None, None)], Return(StringLit(DgS))), FuncDecl(Id(Pf5), [], Block([CallStmt(Id(nnaO), [Id(e4n)]), If(BooleanLit(False), VarDecl(Id(mMYH), ArrayType([33.87, 10.95], NumberType), None, StringLit(A))), [(StringLit(Ix), AssignStmt(Id(JZp), Id(eGfi)))], None]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115164))

	def test_21530115165(self):
		input = '''
bool rG2
func BP7 (number wY_r, number vZ_, string SE[69.05,58.56,43.65])	return

func kMP1 (bool q24I[40.14])
	return
'''
		expect = '''Program([VarDecl(Id(rG2), BoolType, None, None), FuncDecl(Id(BP7), [VarDecl(Id(wY_r), NumberType, None, None), VarDecl(Id(vZ_), NumberType, None, None), VarDecl(Id(SE), ArrayType([69.05, 58.56, 43.65], StringType), None, None)], Return()), FuncDecl(Id(kMP1), [VarDecl(Id(q24I), ArrayType([40.14], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115165))

	def test_21530115166(self):
		input = '''
var Fz2 <- true
dynamic YB8 <- WLsr
'''
		expect = '''Program([VarDecl(Id(Fz2), None, var, BooleanLit(True)), VarDecl(Id(YB8), None, dynamic, Id(WLsr))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115166))

	def test_21530115167(self):
		input = '''
bool CQB[65.81]
func o2 (bool ksK, bool D_6[84.38,19.93], bool lSM[25.0])
	return nY
'''
		expect = '''Program([VarDecl(Id(CQB), ArrayType([65.81], BoolType), None, None), FuncDecl(Id(o2), [VarDecl(Id(ksK), BoolType, None, None), VarDecl(Id(D_6), ArrayType([84.38, 19.93], BoolType), None, None), VarDecl(Id(lSM), ArrayType([25.0], BoolType), None, None)], Return(Id(nY)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115167))

	def test_21530115168(self):
		input = '''
string AQ8[41.68]
dynamic NWPt <- 4.83
func VM (string NpB[46.78,43.3,35.78], bool U1Xb)	begin
	end
'''
		expect = '''Program([VarDecl(Id(AQ8), ArrayType([41.68], StringType), None, None), VarDecl(Id(NWPt), None, dynamic, NumLit(4.83)), FuncDecl(Id(VM), [VarDecl(Id(NpB), ArrayType([46.78, 43.3, 35.78], StringType), None, None), VarDecl(Id(U1Xb), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115168))

	def test_21530115169(self):
		input = '''
func Wm (string JE, bool A8)
	return "Bw"

'''
		expect = '''Program([FuncDecl(Id(Wm), [VarDecl(Id(JE), StringType, None, None), VarDecl(Id(A8), BoolType, None, None)], Return(StringLit(Bw)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115169))

	def test_21530115170(self):
		input = '''
func u2e (bool a6MK[66.6], bool mYf4)	begin
		if ("qeu") return 43.18
		elif (3.0) i4AB()
		elif ("XG")
		if (false) continue
		elif (true)
		continue
		elif (9.43)
		begin
			if (true)
			continue
			elif (57.45)
			break
			elif (false) continue
			elif ("Kzte") break
			else if (82.76) for Zqx6 until 71.74 by 0.48
				if (false)
				for Hn4 until 96.91 by CVR
					XR(false)
				elif (2.07)
				lG(false, yn)
				elif ("UJ")
				continue
				elif ("tZ")
				for iMlz until "bowJ" by 53.14
					VL(6.43, 21.41, true)
				elif (U4x9)
				continue
				elif (Dcv)
				begin
					return
				end
			elif (aJae)
			continue
			elif (false)
			begin
				string uGbX[30.16,55.82,41.77] <- true
				begin
				end
				return
			end
			else for gl until "Er" by whmF
				break
		end
		elif (qqON)
		continue
		elif (true) return
		break
	end

func lH (bool Zxl[61.31], bool MjC, string hGm[64.63])	return
'''
		expect = '''Program([FuncDecl(Id(u2e), [VarDecl(Id(a6MK), ArrayType([66.6], BoolType), None, None), VarDecl(Id(mYf4), BoolType, None, None)], Block([If(StringLit(qeu), Return(NumLit(43.18))), [(NumLit(3.0), CallStmt(Id(i4AB), [])), (StringLit(XG), If(BooleanLit(False), Continue), [(BooleanLit(True), Continue), (NumLit(9.43), Block([If(BooleanLit(True), Continue), [(NumLit(57.45), Break), (BooleanLit(False), Continue), (StringLit(Kzte), Break)], If(NumLit(82.76), For(Id(Zqx6), NumLit(71.74), NumLit(0.48), If(BooleanLit(False), For(Id(Hn4), NumLit(96.91), Id(CVR), CallStmt(Id(XR), [BooleanLit(False)]))), [(NumLit(2.07), CallStmt(Id(lG), [BooleanLit(False), Id(yn)])), (StringLit(UJ), Continue), (StringLit(tZ), For(Id(iMlz), StringLit(bowJ), NumLit(53.14), CallStmt(Id(VL), [NumLit(6.43), NumLit(21.41), BooleanLit(True)]))), (Id(U4x9), Continue), (Id(Dcv), Block([Return()])), (Id(aJae), Continue), (BooleanLit(False), Block([VarDecl(Id(uGbX), ArrayType([30.16, 55.82, 41.77], StringType), None, BooleanLit(True)), Block([]), Return()]))], For(Id(gl), StringLit(Er), Id(whmF), Break))), [], None])), (Id(qqON), Continue), (BooleanLit(True), Return())], None)], None, Break])), FuncDecl(Id(lH), [VarDecl(Id(Zxl), ArrayType([61.31], BoolType), None, None), VarDecl(Id(MjC), BoolType, None, None), VarDecl(Id(hGm), ArrayType([64.63], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115170))

	def test_21530115171(self):
		input = '''
func H9qw ()
	begin
		if (82.11) return
		else tAhb[false, true] <- "vg"
		begin
			if (20.32) for w9Z until false by 70.38
				pb()
			elif (a9)
			continue
			elif ("tx") return aJl
			elif (LwX) break
			else string yC
			break
			for nm until true by 41.06
				Hw <- thu
		end
		bool hMq8[28.54]
	end

func UN (string VU5, string Znxh[60.24], string Locx[74.92,48.63])
	return

string Fbuo[8.87] <- 23.14
func ZXnu (bool tRz, bool OX)	return

func UJr (number QH[15.63,63.78], string QuR[84.56], number WEb[20.15,49.06,25.16])
	return XLJ

'''
		expect = '''Program([FuncDecl(Id(H9qw), [], Block([If(NumLit(82.11), Return()), [], AssignStmt(ArrayCell(Id(tAhb), [BooleanLit(False), BooleanLit(True)]), StringLit(vg)), Block([If(NumLit(20.32), For(Id(w9Z), BooleanLit(False), NumLit(70.38), CallStmt(Id(pb), []))), [(Id(a9), Continue), (StringLit(tx), Return(Id(aJl))), (Id(LwX), Break)], VarDecl(Id(yC), StringType, None, None), Break, For(Id(nm), BooleanLit(True), NumLit(41.06), AssignStmt(Id(Hw), Id(thu)))]), VarDecl(Id(hMq8), ArrayType([28.54], BoolType), None, None)])), FuncDecl(Id(UN), [VarDecl(Id(VU5), StringType, None, None), VarDecl(Id(Znxh), ArrayType([60.24], StringType), None, None), VarDecl(Id(Locx), ArrayType([74.92, 48.63], StringType), None, None)], Return()), VarDecl(Id(Fbuo), ArrayType([8.87], StringType), None, NumLit(23.14)), FuncDecl(Id(ZXnu), [VarDecl(Id(tRz), BoolType, None, None), VarDecl(Id(OX), BoolType, None, None)], Return()), FuncDecl(Id(UJr), [VarDecl(Id(QH), ArrayType([15.63, 63.78], NumberType), None, None), VarDecl(Id(QuR), ArrayType([84.56], StringType), None, None), VarDecl(Id(WEb), ArrayType([20.15, 49.06, 25.16], NumberType), None, None)], Return(Id(XLJ)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115171))

	def test_21530115172(self):
		input = '''
func C0g ()	return
'''
		expect = '''Program([FuncDecl(Id(C0g), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115172))

	def test_21530115173(self):
		input = '''
func yely (string Vs[94.1])	return 30.63

func Ep (bool RKTI[28.12], string qHD[58.52], string R5D)	begin
	end

bool p_
string HWe
number wdN <- true
'''
		expect = '''Program([FuncDecl(Id(yely), [VarDecl(Id(Vs), ArrayType([94.1], StringType), None, None)], Return(NumLit(30.63))), FuncDecl(Id(Ep), [VarDecl(Id(RKTI), ArrayType([28.12], BoolType), None, None), VarDecl(Id(qHD), ArrayType([58.52], StringType), None, None), VarDecl(Id(R5D), StringType, None, None)], Block([])), VarDecl(Id(p_), BoolType, None, None), VarDecl(Id(HWe), StringType, None, None), VarDecl(Id(wdN), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115173))

	def test_21530115174(self):
		input = '''
func XSo (bool U6[68.0,61.7], string v3YE)
	begin
		if (Ms2)
		break
		elif (false) return "y"
		elif ("piznE")
		return
		elif (UG) if (Yflz) string LLi[38.72,95.35,59.97] <- "RG"
		elif (true)
		bool Amr[74.1,75.27]
		else dw("fA")
	end

func YFBg ()	return

'''
		expect = '''Program([FuncDecl(Id(XSo), [VarDecl(Id(U6), ArrayType([68.0, 61.7], BoolType), None, None), VarDecl(Id(v3YE), StringType, None, None)], Block([If(Id(Ms2), Break), [(BooleanLit(False), Return(StringLit(y))), (StringLit(piznE), Return()), (Id(UG), If(Id(Yflz), VarDecl(Id(LLi), ArrayType([38.72, 95.35, 59.97], StringType), None, StringLit(RG))), [(BooleanLit(True), VarDecl(Id(Amr), ArrayType([74.1, 75.27], BoolType), None, None))], CallStmt(Id(dw), [StringLit(fA)]))], None])), FuncDecl(Id(YFBg), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115174))

	def test_21530115175(self):
		input = '''
number fs7l[51.1,45.15,12.1]
func m5 ()	begin
		for zFE9 until 21.14 by xNGW
			continue
		begin
		end
		begin
			return
			begin
				return Mtxg
				begin
				end
			end
			for Fh until "rlH" by true
				for Sa until true by tnZn
					bool d7Or[91.65] <- 52.51
		end
	end
func fC_A ()
	begin
	end

number WR1r
func WdJd (string CjYj)
	return
'''
		expect = '''Program([VarDecl(Id(fs7l), ArrayType([51.1, 45.15, 12.1], NumberType), None, None), FuncDecl(Id(m5), [], Block([For(Id(zFE9), NumLit(21.14), Id(xNGW), Continue), Block([]), Block([Return(), Block([Return(Id(Mtxg)), Block([])]), For(Id(Fh), StringLit(rlH), BooleanLit(True), For(Id(Sa), BooleanLit(True), Id(tnZn), VarDecl(Id(d7Or), ArrayType([91.65], BoolType), None, NumLit(52.51))))])])), FuncDecl(Id(fC_A), [], Block([])), VarDecl(Id(WR1r), NumberType, None, None), FuncDecl(Id(WdJd), [VarDecl(Id(CjYj), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115175))

	def test_21530115176(self):
		input = '''
func As3 ()
	return
bool TIdC <- 39.74
func DSl (bool RCG[0.58,13.55], string Uu[52.22,12.81])
	return

'''
		expect = '''Program([FuncDecl(Id(As3), [], Return()), VarDecl(Id(TIdC), BoolType, None, NumLit(39.74)), FuncDecl(Id(DSl), [VarDecl(Id(RCG), ArrayType([0.58, 13.55], BoolType), None, None), VarDecl(Id(Uu), ArrayType([52.22, 12.81], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115176))

	def test_21530115177(self):
		input = '''
func uPY (bool kbh, bool ls[70.88,93.6])
	return
string dM <- "LhWl"
func HQd ()
	begin
	end

number PJNI[73.55,39.77,12.62] <- false
number qp <- "Xx"
'''
		expect = '''Program([FuncDecl(Id(uPY), [VarDecl(Id(kbh), BoolType, None, None), VarDecl(Id(ls), ArrayType([70.88, 93.6], BoolType), None, None)], Return()), VarDecl(Id(dM), StringType, None, StringLit(LhWl)), FuncDecl(Id(HQd), [], Block([])), VarDecl(Id(PJNI), ArrayType([73.55, 39.77, 12.62], NumberType), None, BooleanLit(False)), VarDecl(Id(qp), NumberType, None, StringLit(Xx))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115177))

	def test_21530115178(self):
		input = '''
bool RLB[56.77,91.99,42.01] <- 55.15
number YJ <- true
'''
		expect = '''Program([VarDecl(Id(RLB), ArrayType([56.77, 91.99, 42.01], BoolType), None, NumLit(55.15)), VarDecl(Id(YJ), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115178))

	def test_21530115179(self):
		input = '''
func vav ()	return
bool qKxc[22.25] <- "VRc"
string jG[75.06,51.32,30.44]
'''
		expect = '''Program([FuncDecl(Id(vav), [], Return()), VarDecl(Id(qKxc), ArrayType([22.25], BoolType), None, StringLit(VRc)), VarDecl(Id(jG), ArrayType([75.06, 51.32, 30.44], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115179))

	def test_21530115180(self):
		input = '''
func WRn8 (number aVM8, bool bmaT)	return
func uTQ (number F5c, string GQ2x[62.56,5.6], bool MWBm)	return

'''
		expect = '''Program([FuncDecl(Id(WRn8), [VarDecl(Id(aVM8), NumberType, None, None), VarDecl(Id(bmaT), BoolType, None, None)], Return()), FuncDecl(Id(uTQ), [VarDecl(Id(F5c), NumberType, None, None), VarDecl(Id(GQ2x), ArrayType([62.56, 5.6], StringType), None, None), VarDecl(Id(MWBm), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115180))

	def test_21530115181(self):
		input = '''
func X6GQ (string zGik[55.61], number YE, number lI3)	return true
func rp (bool NY[50.61,13.71])	return 74.58

dynamic xQF <- 88.87
func a7 ()
	return "caRlx"
'''
		expect = '''Program([FuncDecl(Id(X6GQ), [VarDecl(Id(zGik), ArrayType([55.61], StringType), None, None), VarDecl(Id(YE), NumberType, None, None), VarDecl(Id(lI3), NumberType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(rp), [VarDecl(Id(NY), ArrayType([50.61, 13.71], BoolType), None, None)], Return(NumLit(74.58))), VarDecl(Id(xQF), None, dynamic, NumLit(88.87)), FuncDecl(Id(a7), [], Return(StringLit(caRlx)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115181))

	def test_21530115182(self):
		input = '''
number KqDV[75.24,43.99] <- l6y0
bool FzXn[13.54] <- 16.77
bool qw[91.35] <- 51.9
func wN (number AZU, bool jqhf, number Hh[20.31])	return

'''
		expect = '''Program([VarDecl(Id(KqDV), ArrayType([75.24, 43.99], NumberType), None, Id(l6y0)), VarDecl(Id(FzXn), ArrayType([13.54], BoolType), None, NumLit(16.77)), VarDecl(Id(qw), ArrayType([91.35], BoolType), None, NumLit(51.9)), FuncDecl(Id(wN), [VarDecl(Id(AZU), NumberType, None, None), VarDecl(Id(jqhf), BoolType, None, None), VarDecl(Id(Hh), ArrayType([20.31], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115182))

	def test_21530115183(self):
		input = '''
func Hgi (string oIEF)
	return
string cl[26.75]
'''
		expect = '''Program([FuncDecl(Id(Hgi), [VarDecl(Id(oIEF), StringType, None, None)], Return()), VarDecl(Id(cl), ArrayType([26.75], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115183))

	def test_21530115184(self):
		input = '''
number XIfb[35.55] <- 98.37
func olJN ()	return

number Fp3[0.04]
'''
		expect = '''Program([VarDecl(Id(XIfb), ArrayType([35.55], NumberType), None, NumLit(98.37)), FuncDecl(Id(olJN), [], Return()), VarDecl(Id(Fp3), ArrayType([0.04], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115184))

	def test_21530115185(self):
		input = '''
string zU[4.26,18.68,28.22]
var gfj <- N5to
number xb[5.42,86.65,92.37] <- true
'''
		expect = '''Program([VarDecl(Id(zU), ArrayType([4.26, 18.68, 28.22], StringType), None, None), VarDecl(Id(gfj), None, var, Id(N5to)), VarDecl(Id(xb), ArrayType([5.42, 86.65, 92.37], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115185))

	def test_21530115186(self):
		input = '''
var E8w <- false
func Do1m ()
	begin
		break
	end
'''
		expect = '''Program([VarDecl(Id(E8w), None, var, BooleanLit(False)), FuncDecl(Id(Do1m), [], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115186))

	def test_21530115187(self):
		input = '''
bool Qg[70.92]
'''
		expect = '''Program([VarDecl(Id(Qg), ArrayType([70.92], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115187))

	def test_21530115188(self):
		input = '''
bool xaK[70.86,52.69]
string vP7[14.26]
func QMC8 ()
	return
func fRZz (string Eju[58.22,86.34,90.53])	begin
		begin
			for smMr until pz by false
				begin
					continue
					P0[true] <- v1X
				end
		end
	end
func vSyJ (number r7L7[55.51,86.84,36.98])
	begin
	end

'''
		expect = '''Program([VarDecl(Id(xaK), ArrayType([70.86, 52.69], BoolType), None, None), VarDecl(Id(vP7), ArrayType([14.26], StringType), None, None), FuncDecl(Id(QMC8), [], Return()), FuncDecl(Id(fRZz), [VarDecl(Id(Eju), ArrayType([58.22, 86.34, 90.53], StringType), None, None)], Block([Block([For(Id(smMr), Id(pz), BooleanLit(False), Block([Continue, AssignStmt(ArrayCell(Id(P0), [BooleanLit(True)]), Id(v1X))]))])])), FuncDecl(Id(vSyJ), [VarDecl(Id(r7L7), ArrayType([55.51, 86.84, 36.98], NumberType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115188))

	def test_21530115189(self):
		input = '''
bool gI4[11.48,82.6,25.28] <- "Spa"
func E2 ()	return true
'''
		expect = '''Program([VarDecl(Id(gI4), ArrayType([11.48, 82.6, 25.28], BoolType), None, StringLit(Spa)), FuncDecl(Id(E2), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115189))

	def test_21530115190(self):
		input = '''
func u4 (number hcu[84.79], string BOZ)	return

bool oM[62.61,57.43,99.17] <- 74.88
func w2M (bool qS[74.77])
	return u3F

'''
		expect = '''Program([FuncDecl(Id(u4), [VarDecl(Id(hcu), ArrayType([84.79], NumberType), None, None), VarDecl(Id(BOZ), StringType, None, None)], Return()), VarDecl(Id(oM), ArrayType([62.61, 57.43, 99.17], BoolType), None, NumLit(74.88)), FuncDecl(Id(w2M), [VarDecl(Id(qS), ArrayType([74.77], BoolType), None, None)], Return(Id(u3F)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115190))

	def test_21530115191(self):
		input = '''
string Uet[59.64] <- true
func fF (bool ej, bool dzKT, string AN[8.65,98.31])
	begin
		for isj until 70.19 by true
			if (y_N4)
			if ("RFgW") return 74.15
			elif ("ECHYX")
			return false
			elif ("vjJ") bool o9p[64.38,62.74,47.27] <- uK6
			elif ("oIXJC")
			break
			elif (87.34)
			if ("YCgo") begin
				break
				for SyY until 36.82 by false
					D82 <- "wZPga"
				rL0(LW)
			end
			elif (true)
			B9 <- false
			elif ("ynBPI") begin
				Vyy()
				for X5g until "IJyMk" by false
					break
			end
			elif (66.5) continue
			elif (false)
			tFe7(88.71)
			elif (Zc)
			if (Zu) var bTg <- 37.58
			elif (false)
			for cP3 until "qKrJf" by "crwG"
				return
			elif (AhVe)
			E8OG("yFV", 5.61)
			else MR8u[68.98, "YJTA", 33.41] <- "Fv"
			elif (50.97)
			return
			elif (87.2)
			K6E()
			elif ("JtY") break
		for rGFO until Jx by "kPK"
			cO1J <- true
		return
	end
number VkH <- "rjyp"
func Lh ()
	begin
	end

var PdM1 <- 75.65
'''
		expect = '''Program([VarDecl(Id(Uet), ArrayType([59.64], StringType), None, BooleanLit(True)), FuncDecl(Id(fF), [VarDecl(Id(ej), BoolType, None, None), VarDecl(Id(dzKT), BoolType, None, None), VarDecl(Id(AN), ArrayType([8.65, 98.31], StringType), None, None)], Block([For(Id(isj), NumLit(70.19), BooleanLit(True), If(Id(y_N4), If(StringLit(RFgW), Return(NumLit(74.15))), [(StringLit(ECHYX), Return(BooleanLit(False))), (StringLit(vjJ), VarDecl(Id(o9p), ArrayType([64.38, 62.74, 47.27], BoolType), None, Id(uK6))), (StringLit(oIXJC), Break), (NumLit(87.34), If(StringLit(YCgo), Block([Break, For(Id(SyY), NumLit(36.82), BooleanLit(False), AssignStmt(Id(D82), StringLit(wZPga))), CallStmt(Id(rL0), [Id(LW)])])), [(BooleanLit(True), AssignStmt(Id(B9), BooleanLit(False))), (StringLit(ynBPI), Block([CallStmt(Id(Vyy), []), For(Id(X5g), StringLit(IJyMk), BooleanLit(False), Break)])), (NumLit(66.5), Continue), (BooleanLit(False), CallStmt(Id(tFe7), [NumLit(88.71)])), (Id(Zc), If(Id(Zu), VarDecl(Id(bTg), None, var, NumLit(37.58))), [(BooleanLit(False), For(Id(cP3), StringLit(qKrJf), StringLit(crwG), Return())), (Id(AhVe), CallStmt(Id(E8OG), [StringLit(yFV), NumLit(5.61)]))], AssignStmt(ArrayCell(Id(MR8u), [NumLit(68.98), StringLit(YJTA), NumLit(33.41)]), StringLit(Fv))), (NumLit(50.97), Return()), (NumLit(87.2), CallStmt(Id(K6E), [])), (StringLit(JtY), Break)], None)], None), [], None), For(Id(rGFO), Id(Jx), StringLit(kPK), AssignStmt(Id(cO1J), BooleanLit(True))), Return()])), VarDecl(Id(VkH), NumberType, None, StringLit(rjyp)), FuncDecl(Id(Lh), [], Block([])), VarDecl(Id(PdM1), None, var, NumLit(75.65))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115191))

	def test_21530115192(self):
		input = '''
func ps08 ()
	return
number i4[48.31,65.23,23.39] <- "S"
func bj (string R2v, number pSGo)	begin
	end
func Ep ()
	return

'''
		expect = '''Program([FuncDecl(Id(ps08), [], Return()), VarDecl(Id(i4), ArrayType([48.31, 65.23, 23.39], NumberType), None, StringLit(S)), FuncDecl(Id(bj), [VarDecl(Id(R2v), StringType, None, None), VarDecl(Id(pSGo), NumberType, None, None)], Block([])), FuncDecl(Id(Ep), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115192))

	def test_21530115193(self):
		input = '''
func PcjO ()
	return
func MC (number hQT, string oD[55.3], string MeJ)
	begin
	end

number yyuN[2.46]
func e8BW ()
	return
'''
		expect = '''Program([FuncDecl(Id(PcjO), [], Return()), FuncDecl(Id(MC), [VarDecl(Id(hQT), NumberType, None, None), VarDecl(Id(oD), ArrayType([55.3], StringType), None, None), VarDecl(Id(MeJ), StringType, None, None)], Block([])), VarDecl(Id(yyuN), ArrayType([2.46], NumberType), None, None), FuncDecl(Id(e8BW), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115193))

	def test_21530115194(self):
		input = '''
func PQ (number gn[56.18], string d5[98.48,23.09,72.19], string qnY)	return "sNTX"
number FJBj <- true
'''
		expect = '''Program([FuncDecl(Id(PQ), [VarDecl(Id(gn), ArrayType([56.18], NumberType), None, None), VarDecl(Id(d5), ArrayType([98.48, 23.09, 72.19], StringType), None, None), VarDecl(Id(qnY), StringType, None, None)], Return(StringLit(sNTX))), VarDecl(Id(FJBj), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115194))

	def test_21530115195(self):
		input = '''
func tDT ()	return 18.74
func nrd (string Ou, bool PW[6.47])	return

number W7z <- 65.94
var QC <- 76.22
'''
		expect = '''Program([FuncDecl(Id(tDT), [], Return(NumLit(18.74))), FuncDecl(Id(nrd), [VarDecl(Id(Ou), StringType, None, None), VarDecl(Id(PW), ArrayType([6.47], BoolType), None, None)], Return()), VarDecl(Id(W7z), NumberType, None, NumLit(65.94)), VarDecl(Id(QC), None, var, NumLit(76.22))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115195))

	def test_21530115196(self):
		input = '''
number XjJX
var kz <- 97.63
bool nxd[8.34,60.55,37.36] <- 22.52
number OI[48.76,12.15] <- "Pf"
'''
		expect = '''Program([VarDecl(Id(XjJX), NumberType, None, None), VarDecl(Id(kz), None, var, NumLit(97.63)), VarDecl(Id(nxd), ArrayType([8.34, 60.55, 37.36], BoolType), None, NumLit(22.52)), VarDecl(Id(OI), ArrayType([48.76, 12.15], NumberType), None, StringLit(Pf))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115196))

	def test_21530115197(self):
		input = '''
func OA (number wcqo[65.95,92.75,97.3], string qZ_[28.96,41.94], bool lkPC)
	return "PQeh"

bool gik[88.61]
string hU[80.64,59.85,68.91]
number pZl[57.04] <- qqCI
'''
		expect = '''Program([FuncDecl(Id(OA), [VarDecl(Id(wcqo), ArrayType([65.95, 92.75, 97.3], NumberType), None, None), VarDecl(Id(qZ_), ArrayType([28.96, 41.94], StringType), None, None), VarDecl(Id(lkPC), BoolType, None, None)], Return(StringLit(PQeh))), VarDecl(Id(gik), ArrayType([88.61], BoolType), None, None), VarDecl(Id(hU), ArrayType([80.64, 59.85, 68.91], StringType), None, None), VarDecl(Id(pZl), ArrayType([57.04], NumberType), None, Id(qqCI))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115197))

	def test_21530115198(self):
		input = '''
dynamic MM
var P62 <- "A"
string ktDG[56.98,9.88,27.36] <- YF
var xO <- 53.06
'''
		expect = '''Program([VarDecl(Id(MM), None, dynamic, None), VarDecl(Id(P62), None, var, StringLit(A)), VarDecl(Id(ktDG), ArrayType([56.98, 9.88, 27.36], StringType), None, Id(YF)), VarDecl(Id(xO), None, var, NumLit(53.06))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115198))

	def test_21530115199(self):
		input = '''
string nT[74.86]
var MzAz <- Mq3
bool DAQ4[33.45,8.61]
string kAc[9.99]
string FT[61.73]
'''
		expect = '''Program([VarDecl(Id(nT), ArrayType([74.86], StringType), None, None), VarDecl(Id(MzAz), None, var, Id(Mq3)), VarDecl(Id(DAQ4), ArrayType([33.45, 8.61], BoolType), None, None), VarDecl(Id(kAc), ArrayType([9.99], StringType), None, None), VarDecl(Id(FT), ArrayType([61.73], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115199))

	def test_21530115200(self):
		input = '''
func BQ ()	return

func QP (string m3, bool wVPX[98.09,90.7,34.54], bool ki5r)	begin
		break
		continue
		continue
	end

number tH[28.1]
'''
		expect = '''Program([FuncDecl(Id(BQ), [], Return()), FuncDecl(Id(QP), [VarDecl(Id(m3), StringType, None, None), VarDecl(Id(wVPX), ArrayType([98.09, 90.7, 34.54], BoolType), None, None), VarDecl(Id(ki5r), BoolType, None, None)], Block([Break, Continue, Continue])), VarDecl(Id(tH), ArrayType([28.1], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115200))

	def test_21530115201(self):
		input = '''
func dP (string eRJ)	return

number R8 <- "mql"
bool Trb[96.32,37.9]
bool zYw[45.8,22.6]
func vh (string Qk[62.56], string po)	return

'''
		expect = '''Program([FuncDecl(Id(dP), [VarDecl(Id(eRJ), StringType, None, None)], Return()), VarDecl(Id(R8), NumberType, None, StringLit(mql)), VarDecl(Id(Trb), ArrayType([96.32, 37.9], BoolType), None, None), VarDecl(Id(zYw), ArrayType([45.8, 22.6], BoolType), None, None), FuncDecl(Id(vh), [VarDecl(Id(Qk), ArrayType([62.56], StringType), None, None), VarDecl(Id(po), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115201))

	def test_21530115202(self):
		input = '''
func Kcw (bool Mwx7[58.06,99.87], number YI, string nAe[81.71])
	begin
	end
func buA (number n8, bool uTo1, string rB9)
	return true
'''
		expect = '''Program([FuncDecl(Id(Kcw), [VarDecl(Id(Mwx7), ArrayType([58.06, 99.87], BoolType), None, None), VarDecl(Id(YI), NumberType, None, None), VarDecl(Id(nAe), ArrayType([81.71], StringType), None, None)], Block([])), FuncDecl(Id(buA), [VarDecl(Id(n8), NumberType, None, None), VarDecl(Id(uTo1), BoolType, None, None), VarDecl(Id(rB9), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115202))

	def test_21530115203(self):
		input = '''
var mcGt <- false
number ByzB[86.74,21.67,98.22]
func Fl ()
	begin
		if (Qa) for s_g until "mJk" by "K"
			for cc until 55.3 by "Svm"
				KnaC <- "GRp"
		elif ("WaTp") begin
			continue
			idMD <- 87.64
		end
		else if ("AVJPT")
		continue
		elif ("htgEI") yxrs <- A6
		elif (false)
		return
		elif (53.71)
		s7 <- "auUk"
		elif (39.99)
		oxH()
		elif ("uCeU") QTYj()
		else for OC7z until 41.14 by QZiR
			JjY7("Hgw", 25.74)
	end
number nRFL[95.85,82.07]
'''
		expect = '''Program([VarDecl(Id(mcGt), None, var, BooleanLit(False)), VarDecl(Id(ByzB), ArrayType([86.74, 21.67, 98.22], NumberType), None, None), FuncDecl(Id(Fl), [], Block([If(Id(Qa), For(Id(s_g), StringLit(mJk), StringLit(K), For(Id(cc), NumLit(55.3), StringLit(Svm), AssignStmt(Id(KnaC), StringLit(GRp))))), [(StringLit(WaTp), Block([Continue, AssignStmt(Id(idMD), NumLit(87.64))]))], If(StringLit(AVJPT), Continue), [(StringLit(htgEI), AssignStmt(Id(yxrs), Id(A6))), (BooleanLit(False), Return()), (NumLit(53.71), AssignStmt(Id(s7), StringLit(auUk))), (NumLit(39.99), CallStmt(Id(oxH), [])), (StringLit(uCeU), CallStmt(Id(QTYj), []))], For(Id(OC7z), NumLit(41.14), Id(QZiR), CallStmt(Id(JjY7), [StringLit(Hgw), NumLit(25.74)]))])), VarDecl(Id(nRFL), ArrayType([95.85, 82.07], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115203))

	def test_21530115204(self):
		input = '''
func FKWa (bool vYw, number AXU)	return "fWGAN"

'''
		expect = '''Program([FuncDecl(Id(FKWa), [VarDecl(Id(vYw), BoolType, None, None), VarDecl(Id(AXU), NumberType, None, None)], Return(StringLit(fWGAN)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115204))

	def test_21530115205(self):
		input = '''
func dkDg (bool Lbko, number PhQW[27.46,57.46,68.16], string OO5p[98.22,86.78])
	return
number KdV[25.98,99.87] <- true
func o6q (number bQS[35.18,57.97], bool MGt[55.2], number ZVU[75.99,60.61])	begin
		lJOK <- 93.08
		continue
	end
'''
		expect = '''Program([FuncDecl(Id(dkDg), [VarDecl(Id(Lbko), BoolType, None, None), VarDecl(Id(PhQW), ArrayType([27.46, 57.46, 68.16], NumberType), None, None), VarDecl(Id(OO5p), ArrayType([98.22, 86.78], StringType), None, None)], Return()), VarDecl(Id(KdV), ArrayType([25.98, 99.87], NumberType), None, BooleanLit(True)), FuncDecl(Id(o6q), [VarDecl(Id(bQS), ArrayType([35.18, 57.97], NumberType), None, None), VarDecl(Id(MGt), ArrayType([55.2], BoolType), None, None), VarDecl(Id(ZVU), ArrayType([75.99, 60.61], NumberType), None, None)], Block([AssignStmt(Id(lJOK), NumLit(93.08)), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115205))

	def test_21530115206(self):
		input = '''
func Djrk (string y2ob, number PX)	return
func mBu (number hU[37.27,9.23])	begin
		return yA
	end

number ZktB <- o7z
'''
		expect = '''Program([FuncDecl(Id(Djrk), [VarDecl(Id(y2ob), StringType, None, None), VarDecl(Id(PX), NumberType, None, None)], Return()), FuncDecl(Id(mBu), [VarDecl(Id(hU), ArrayType([37.27, 9.23], NumberType), None, None)], Block([Return(Id(yA))])), VarDecl(Id(ZktB), NumberType, None, Id(o7z))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115206))

	def test_21530115207(self):
		input = '''
string LAp
'''
		expect = '''Program([VarDecl(Id(LAp), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115207))

	def test_21530115208(self):
		input = '''
func bHGe (number zEwE[75.75], string o2)	return true

'''
		expect = '''Program([FuncDecl(Id(bHGe), [VarDecl(Id(zEwE), ArrayType([75.75], NumberType), None, None), VarDecl(Id(o2), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115208))

	def test_21530115209(self):
		input = '''
dynamic Sc <- true
func zq (bool IC32[46.64,34.31], number J2)	return UpNS

'''
		expect = '''Program([VarDecl(Id(Sc), None, dynamic, BooleanLit(True)), FuncDecl(Id(zq), [VarDecl(Id(IC32), ArrayType([46.64, 34.31], BoolType), None, None), VarDecl(Id(J2), NumberType, None, None)], Return(Id(UpNS)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115209))

	def test_21530115210(self):
		input = '''
func yX_8 (bool cyKo, bool MkD[57.49])
	begin
		break
	end
func W9D1 (number ToDF)
	return "QTamO"
'''
		expect = '''Program([FuncDecl(Id(yX_8), [VarDecl(Id(cyKo), BoolType, None, None), VarDecl(Id(MkD), ArrayType([57.49], BoolType), None, None)], Block([Break])), FuncDecl(Id(W9D1), [VarDecl(Id(ToDF), NumberType, None, None)], Return(StringLit(QTamO)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115210))

	def test_21530115211(self):
		input = '''
func p91 (bool od[64.43,94.94], bool DGtY[77.15,0.36])
	return
number bU[40.79]
number vtV
'''
		expect = '''Program([FuncDecl(Id(p91), [VarDecl(Id(od), ArrayType([64.43, 94.94], BoolType), None, None), VarDecl(Id(DGtY), ArrayType([77.15, 0.36], BoolType), None, None)], Return()), VarDecl(Id(bU), ArrayType([40.79], NumberType), None, None), VarDecl(Id(vtV), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115211))

	def test_21530115212(self):
		input = '''
func LT (number LwLy[56.4,70.16,37.84], string FdE8[33.68,14.0,63.25], bool mlI[93.36,59.83,80.99])	return
number VlqZ[65.26] <- "Eux"
func QSl (bool BT, number EVIH)
	return

number Qc[12.89,97.7] <- "FiaQ"
'''
		expect = '''Program([FuncDecl(Id(LT), [VarDecl(Id(LwLy), ArrayType([56.4, 70.16, 37.84], NumberType), None, None), VarDecl(Id(FdE8), ArrayType([33.68, 14.0, 63.25], StringType), None, None), VarDecl(Id(mlI), ArrayType([93.36, 59.83, 80.99], BoolType), None, None)], Return()), VarDecl(Id(VlqZ), ArrayType([65.26], NumberType), None, StringLit(Eux)), FuncDecl(Id(QSl), [VarDecl(Id(BT), BoolType, None, None), VarDecl(Id(EVIH), NumberType, None, None)], Return()), VarDecl(Id(Qc), ArrayType([12.89, 97.7], NumberType), None, StringLit(FiaQ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115212))

	def test_21530115213(self):
		input = '''
number Uui6 <- 1.39
func UPL (string Lve)
	begin
	end
func Ncvz (number iN6[56.96])	begin
	end

func xI (bool U41f, bool E3, bool NG)	return false
'''
		expect = '''Program([VarDecl(Id(Uui6), NumberType, None, NumLit(1.39)), FuncDecl(Id(UPL), [VarDecl(Id(Lve), StringType, None, None)], Block([])), FuncDecl(Id(Ncvz), [VarDecl(Id(iN6), ArrayType([56.96], NumberType), None, None)], Block([])), FuncDecl(Id(xI), [VarDecl(Id(U41f), BoolType, None, None), VarDecl(Id(E3), BoolType, None, None), VarDecl(Id(NG), BoolType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115213))

	def test_21530115214(self):
		input = '''
func i5 (bool rp)	return false
string CjW[89.29]
bool i_[57.18,80.21]
'''
		expect = '''Program([FuncDecl(Id(i5), [VarDecl(Id(rp), BoolType, None, None)], Return(BooleanLit(False))), VarDecl(Id(CjW), ArrayType([89.29], StringType), None, None), VarDecl(Id(i_), ArrayType([57.18, 80.21], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115214))

	def test_21530115215(self):
		input = '''
func f6 (string hS)
	return J2v
func MNUN ()
	return true
func zbZ (number YE[38.41,36.38,67.37])	return "pr"
'''
		expect = '''Program([FuncDecl(Id(f6), [VarDecl(Id(hS), StringType, None, None)], Return(Id(J2v))), FuncDecl(Id(MNUN), [], Return(BooleanLit(True))), FuncDecl(Id(zbZ), [VarDecl(Id(YE), ArrayType([38.41, 36.38, 67.37], NumberType), None, None)], Return(StringLit(pr)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115215))

	def test_21530115216(self):
		input = '''
func zh (string ml0j, number KYO[24.25,26.86])
	return
'''
		expect = '''Program([FuncDecl(Id(zh), [VarDecl(Id(ml0j), StringType, None, None), VarDecl(Id(KYO), ArrayType([24.25, 26.86], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115216))

	def test_21530115217(self):
		input = '''
number e0RE
bool Ks <- a3X
'''
		expect = '''Program([VarDecl(Id(e0RE), NumberType, None, None), VarDecl(Id(Ks), BoolType, None, Id(a3X))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115217))

	def test_21530115218(self):
		input = '''
func rg (number fQ, bool ym)	begin
		if (false)
		break
		return
		number mM[82.52,27.55,36.58]
	end

number ER[62.5]
func zM ()	begin
		sgrJ("pji", "LtV")
		if (53.87)
		for weR until "NBXXY" by false
			jOR2 <- VA
		elif (false)
		dD <- 42.95
	end
bool wVg[20.59] <- 22.49
string IS8 <- 25.08
'''
		expect = '''Program([FuncDecl(Id(rg), [VarDecl(Id(fQ), NumberType, None, None), VarDecl(Id(ym), BoolType, None, None)], Block([If(BooleanLit(False), Break), [], None, Return(), VarDecl(Id(mM), ArrayType([82.52, 27.55, 36.58], NumberType), None, None)])), VarDecl(Id(ER), ArrayType([62.5], NumberType), None, None), FuncDecl(Id(zM), [], Block([CallStmt(Id(sgrJ), [StringLit(pji), StringLit(LtV)]), If(NumLit(53.87), For(Id(weR), StringLit(NBXXY), BooleanLit(False), AssignStmt(Id(jOR2), Id(VA)))), [(BooleanLit(False), AssignStmt(Id(dD), NumLit(42.95)))], None])), VarDecl(Id(wVg), ArrayType([20.59], BoolType), None, NumLit(22.49)), VarDecl(Id(IS8), StringType, None, NumLit(25.08))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115218))

	def test_21530115219(self):
		input = '''
number vpiO[67.01,96.01,4.26]
func q8JT ()	begin
		O4E[AnKY] <- 83.15
	end

dynamic k_ <- "hjW"
'''
		expect = '''Program([VarDecl(Id(vpiO), ArrayType([67.01, 96.01, 4.26], NumberType), None, None), FuncDecl(Id(q8JT), [], Block([AssignStmt(ArrayCell(Id(O4E), [Id(AnKY)]), NumLit(83.15))])), VarDecl(Id(k_), None, dynamic, StringLit(hjW))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115219))

	def test_21530115220(self):
		input = '''
bool NB <- false
func TFL (number E7z[61.95], string to[44.29], string A_1l)	return

'''
		expect = '''Program([VarDecl(Id(NB), BoolType, None, BooleanLit(False)), FuncDecl(Id(TFL), [VarDecl(Id(E7z), ArrayType([61.95], NumberType), None, None), VarDecl(Id(to), ArrayType([44.29], StringType), None, None), VarDecl(Id(A_1l), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115220))

	def test_21530115221(self):
		input = '''
func quX (bool U3Nr)
	return 57.37

func kl_r (bool DJE, string q_1G[48.94,96.89,7.77])	begin
		BLn(59.8)
	end

dynamic D_ <- false
string TNNs[99.28,23.59]
number vBs[92.8,7.85,95.51]
'''
		expect = '''Program([FuncDecl(Id(quX), [VarDecl(Id(U3Nr), BoolType, None, None)], Return(NumLit(57.37))), FuncDecl(Id(kl_r), [VarDecl(Id(DJE), BoolType, None, None), VarDecl(Id(q_1G), ArrayType([48.94, 96.89, 7.77], StringType), None, None)], Block([CallStmt(Id(BLn), [NumLit(59.8)])])), VarDecl(Id(D_), None, dynamic, BooleanLit(False)), VarDecl(Id(TNNs), ArrayType([99.28, 23.59], StringType), None, None), VarDecl(Id(vBs), ArrayType([92.8, 7.85, 95.51], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115221))

	def test_21530115222(self):
		input = '''
string KR[61.78,54.11,48.68] <- "Sz"
func b_ (string u4iU[90.58,54.05,95.39])	return

bool uz[29.58,81.32] <- "yHL"
bool Dq[51.27] <- D4
'''
		expect = '''Program([VarDecl(Id(KR), ArrayType([61.78, 54.11, 48.68], StringType), None, StringLit(Sz)), FuncDecl(Id(b_), [VarDecl(Id(u4iU), ArrayType([90.58, 54.05, 95.39], StringType), None, None)], Return()), VarDecl(Id(uz), ArrayType([29.58, 81.32], BoolType), None, StringLit(yHL)), VarDecl(Id(Dq), ArrayType([51.27], BoolType), None, Id(D4))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115222))

	def test_21530115223(self):
		input = '''
dynamic I1nL <- true
'''
		expect = '''Program([VarDecl(Id(I1nL), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115223))

	def test_21530115224(self):
		input = '''
func Z_ (number RAT[6.75])
	begin
		begin
			begin
				break
				for Mu2V until "Ut" by 76.51
					for a0ag until hBis by 75.82
						break
				string zg[97.89,99.68]
			end
		end
		begin
			begin
			end
			for VhN until true by true
				if (5.31) begin
					string eRP
					for B9 until 20.69 by "O"
						return
					eAY[F4] <- guK0
				end
				elif (58.52) return
				elif (false)
				if (false) string oz[11.31]
				elif (false) L57[lQN4, 5.97, 65.35] <- oc
				else if (47.89)
				var da <- 84.84
				elif (true)
				return 13.62
				elif (19.92)
				begin
				end
				elif (false) begin
					number Pq
					return fZ
				end
				elif ("cDsrt")
				break
				elif (75.1) begin
					for myeU until true by true
						AF["og", U7] <- true
					if (true)
					for BVv until 53.64 by jdDo
						continue
					elif ("B") continue
					elif ("IT") for zNt until true by VET6
						number PW[11.42,63.45,16.0]
					elif ("NHoPe")
					if (true)
					g8R(Rk, false)
					elif (true) begin
						return true
						xol("XUAl")
						continue
					end
					elif (A8)
					return "oeQM"
					else continue
					elif ("eLUbz") continue
					string w3L[79.66] <- "SqHdu"
				end
				elif (BWu5) krJ(LF)
		end
	end
'''
		expect = '''Program([FuncDecl(Id(Z_), [VarDecl(Id(RAT), ArrayType([6.75], NumberType), None, None)], Block([Block([Block([Break, For(Id(Mu2V), StringLit(Ut), NumLit(76.51), For(Id(a0ag), Id(hBis), NumLit(75.82), Break)), VarDecl(Id(zg), ArrayType([97.89, 99.68], StringType), None, None)])]), Block([Block([]), For(Id(VhN), BooleanLit(True), BooleanLit(True), If(NumLit(5.31), Block([VarDecl(Id(eRP), StringType, None, None), For(Id(B9), NumLit(20.69), StringLit(O), Return()), AssignStmt(ArrayCell(Id(eAY), [Id(F4)]), Id(guK0))])), [(NumLit(58.52), Return()), (BooleanLit(False), If(BooleanLit(False), VarDecl(Id(oz), ArrayType([11.31], StringType), None, None)), [(BooleanLit(False), AssignStmt(ArrayCell(Id(L57), [Id(lQN4), NumLit(5.97), NumLit(65.35)]), Id(oc)))], If(NumLit(47.89), VarDecl(Id(da), None, var, NumLit(84.84))), [(BooleanLit(True), Return(NumLit(13.62))), (NumLit(19.92), Block([])), (BooleanLit(False), Block([VarDecl(Id(Pq), NumberType, None, None), Return(Id(fZ))])), (StringLit(cDsrt), Break), (NumLit(75.1), Block([For(Id(myeU), BooleanLit(True), BooleanLit(True), AssignStmt(ArrayCell(Id(AF), [StringLit(og), Id(U7)]), BooleanLit(True))), If(BooleanLit(True), For(Id(BVv), NumLit(53.64), Id(jdDo), Continue)), [(StringLit(B), Continue), (StringLit(IT), For(Id(zNt), BooleanLit(True), Id(VET6), VarDecl(Id(PW), ArrayType([11.42, 63.45, 16.0], NumberType), None, None))), (StringLit(NHoPe), If(BooleanLit(True), CallStmt(Id(g8R), [Id(Rk), BooleanLit(False)])), [(BooleanLit(True), Block([Return(BooleanLit(True)), CallStmt(Id(xol), [StringLit(XUAl)]), Continue])), (Id(A8), Return(StringLit(oeQM)))], Continue), (StringLit(eLUbz), Continue)], None, VarDecl(Id(w3L), ArrayType([79.66], StringType), None, StringLit(SqHdu))])), (Id(BWu5), CallStmt(Id(krJ), [Id(LF)]))], None)], None)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115224))

	def test_21530115225(self):
		input = '''
func tKPp ()	begin
		break
		string jp0D[86.21] <- Ms
	end

func bR5 (bool ni)
	return 8.71

func aK (bool rNb[51.93,73.07,50.09])	return true

'''
		expect = '''Program([FuncDecl(Id(tKPp), [], Block([Break, VarDecl(Id(jp0D), ArrayType([86.21], StringType), None, Id(Ms))])), FuncDecl(Id(bR5), [VarDecl(Id(ni), BoolType, None, None)], Return(NumLit(8.71))), FuncDecl(Id(aK), [VarDecl(Id(rNb), ArrayType([51.93, 73.07, 50.09], BoolType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115225))

	def test_21530115226(self):
		input = '''
string wyc
func oRAQ (bool vEw[88.01])
	return CY

number h3X <- 71.73
bool BH9H[11.25,93.5]
'''
		expect = '''Program([VarDecl(Id(wyc), StringType, None, None), FuncDecl(Id(oRAQ), [VarDecl(Id(vEw), ArrayType([88.01], BoolType), None, None)], Return(Id(CY))), VarDecl(Id(h3X), NumberType, None, NumLit(71.73)), VarDecl(Id(BH9H), ArrayType([11.25, 93.5], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115226))

	def test_21530115227(self):
		input = '''
bool qNd
func iN (number L1p)	return

string SVy4[41.3,73.33]
func EPzi (bool rHKs)
	begin
		begin
			break
			OI <- Ylk
			string Mzs0 <- MO
		end
		begin
		end
	end
'''
		expect = '''Program([VarDecl(Id(qNd), BoolType, None, None), FuncDecl(Id(iN), [VarDecl(Id(L1p), NumberType, None, None)], Return()), VarDecl(Id(SVy4), ArrayType([41.3, 73.33], StringType), None, None), FuncDecl(Id(EPzi), [VarDecl(Id(rHKs), BoolType, None, None)], Block([Block([Break, AssignStmt(Id(OI), Id(Ylk)), VarDecl(Id(Mzs0), StringType, None, Id(MO))]), Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115227))

	def test_21530115228(self):
		input = '''
func W6vI (string Y3m, string DK[76.23,62.09], number bDoG)
	return 2.76

func Pti (number O3LI[91.56,32.05,51.29])
	return y2Q
func hqA ()
	return b6t

'''
		expect = '''Program([FuncDecl(Id(W6vI), [VarDecl(Id(Y3m), StringType, None, None), VarDecl(Id(DK), ArrayType([76.23, 62.09], StringType), None, None), VarDecl(Id(bDoG), NumberType, None, None)], Return(NumLit(2.76))), FuncDecl(Id(Pti), [VarDecl(Id(O3LI), ArrayType([91.56, 32.05, 51.29], NumberType), None, None)], Return(Id(y2Q))), FuncDecl(Id(hqA), [], Return(Id(b6t)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115228))

	def test_21530115229(self):
		input = '''
func gkV7 (string zq, string Dysx[11.14], number NiD[58.28,20.74,1.92])	return false

func zG9 (number Zyw, number uid)
	return 67.19
'''
		expect = '''Program([FuncDecl(Id(gkV7), [VarDecl(Id(zq), StringType, None, None), VarDecl(Id(Dysx), ArrayType([11.14], StringType), None, None), VarDecl(Id(NiD), ArrayType([58.28, 20.74, 1.92], NumberType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(zG9), [VarDecl(Id(Zyw), NumberType, None, None), VarDecl(Id(uid), NumberType, None, None)], Return(NumLit(67.19)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115229))

	def test_21530115230(self):
		input = '''
bool xmYF[67.1,91.54]
func mk (bool Xdg, bool pyGk[60.68])
	begin
	end

'''
		expect = '''Program([VarDecl(Id(xmYF), ArrayType([67.1, 91.54], BoolType), None, None), FuncDecl(Id(mk), [VarDecl(Id(Xdg), BoolType, None, None), VarDecl(Id(pyGk), ArrayType([60.68], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115230))

	def test_21530115231(self):
		input = '''
string d1i[3.62]
bool wlI[25.56] <- "p"
string S9I[76.21]
'''
		expect = '''Program([VarDecl(Id(d1i), ArrayType([3.62], StringType), None, None), VarDecl(Id(wlI), ArrayType([25.56], BoolType), None, StringLit(p)), VarDecl(Id(S9I), ArrayType([76.21], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115231))

	def test_21530115232(self):
		input = '''
dynamic bijt <- nIC
func cm (number AEN, string rPis[69.33,25.5,19.23])
	return true
'''
		expect = '''Program([VarDecl(Id(bijt), None, dynamic, Id(nIC)), FuncDecl(Id(cm), [VarDecl(Id(AEN), NumberType, None, None), VarDecl(Id(rPis), ArrayType([69.33, 25.5, 19.23], StringType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115232))

	def test_21530115233(self):
		input = '''
func ro (number NL7y[40.37,90.73], string S4V6)
	return true

func x3 ()	return
func Fnjm ()
	return "eUP"

var xZs <- false
'''
		expect = '''Program([FuncDecl(Id(ro), [VarDecl(Id(NL7y), ArrayType([40.37, 90.73], NumberType), None, None), VarDecl(Id(S4V6), StringType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(x3), [], Return()), FuncDecl(Id(Fnjm), [], Return(StringLit(eUP))), VarDecl(Id(xZs), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115233))

	def test_21530115234(self):
		input = '''
func XZKA (string bZx)
	begin
		YAk["QUB", 37.69] <- true
		continue
		for aXA3 until kk by false
			begin
				Z5[true, H6, Tk] <- true
			end
	end

var R7 <- true
func TSJG (bool Nd_p[56.33], number zq[98.84,64.91,71.74])
	begin
		begin
			for W4T until FEB by 58.2
				return
			return A7Za
			zcQ[Jor] <- true
		end
		if (false) break
		elif (59.33)
		MYV[false, true] <- "OB"
		elif ("GZm")
		for t837 until 32.63 by "xl"
			break
		elif ("iEDFD")
		oY89()
		elif (Gg)
		begin
			if (true) break
			elif (false) return
			elif (h2)
			FW2[27.57, "wpIz", ohA] <- true
			elif (true)
			begin
			end
			elif (false)
			break
			elif (S02Q)
			begin
				string QhfW <- true
				if (84.87)
				if (ZaqL)
				break
				elif (yZp) string S2[51.5] <- false
				elif (92.09)
				if (false)
				begin
					var sP <- qn1
				end
				elif (true) return "ri"
				elif (true)
				for oze until "L" by 13.21
					Zkqo(ktK)
				elif (19.79) continue
				elif (akg)
				continue
				elif (false) wm7(false, true, true)
				elif ("XpQxB") begin
					enF(false)
				end
				continue
			end
			continue
		end
		elif (76.84) return
		else if (25.02)
		begin
			number xrFA[45.11,85.46]
		end
		elif ("S")
		return
		return 58.13
	end

'''
		expect = '''Program([FuncDecl(Id(XZKA), [VarDecl(Id(bZx), StringType, None, None)], Block([AssignStmt(ArrayCell(Id(YAk), [StringLit(QUB), NumLit(37.69)]), BooleanLit(True)), Continue, For(Id(aXA3), Id(kk), BooleanLit(False), Block([AssignStmt(ArrayCell(Id(Z5), [BooleanLit(True), Id(H6), Id(Tk)]), BooleanLit(True))]))])), VarDecl(Id(R7), None, var, BooleanLit(True)), FuncDecl(Id(TSJG), [VarDecl(Id(Nd_p), ArrayType([56.33], BoolType), None, None), VarDecl(Id(zq), ArrayType([98.84, 64.91, 71.74], NumberType), None, None)], Block([Block([For(Id(W4T), Id(FEB), NumLit(58.2), Return()), Return(Id(A7Za)), AssignStmt(ArrayCell(Id(zcQ), [Id(Jor)]), BooleanLit(True))]), If(BooleanLit(False), Break), [(NumLit(59.33), AssignStmt(ArrayCell(Id(MYV), [BooleanLit(False), BooleanLit(True)]), StringLit(OB))), (StringLit(GZm), For(Id(t837), NumLit(32.63), StringLit(xl), Break)), (StringLit(iEDFD), CallStmt(Id(oY89), [])), (Id(Gg), Block([If(BooleanLit(True), Break), [(BooleanLit(False), Return()), (Id(h2), AssignStmt(ArrayCell(Id(FW2), [NumLit(27.57), StringLit(wpIz), Id(ohA)]), BooleanLit(True))), (BooleanLit(True), Block([])), (BooleanLit(False), Break), (Id(S02Q), Block([VarDecl(Id(QhfW), StringType, None, BooleanLit(True)), If(NumLit(84.87), If(Id(ZaqL), Break), [(Id(yZp), VarDecl(Id(S2), ArrayType([51.5], StringType), None, BooleanLit(False))), (NumLit(92.09), If(BooleanLit(False), Block([VarDecl(Id(sP), None, var, Id(qn1))])), [(BooleanLit(True), Return(StringLit(ri))), (BooleanLit(True), For(Id(oze), StringLit(L), NumLit(13.21), CallStmt(Id(Zkqo), [Id(ktK)]))), (NumLit(19.79), Continue), (Id(akg), Continue), (BooleanLit(False), CallStmt(Id(wm7), [BooleanLit(False), BooleanLit(True), BooleanLit(True)])), (StringLit(XpQxB), Block([CallStmt(Id(enF), [BooleanLit(False)])]))], None)], None), [], None, Continue]))], None, Continue])), (NumLit(76.84), Return())], If(NumLit(25.02), Block([VarDecl(Id(xrFA), ArrayType([45.11, 85.46], NumberType), None, None)])), [(StringLit(S), Return())], None, Return(NumLit(58.13))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115234))

	def test_21530115235(self):
		input = '''
var H2 <- true
func EOaX (bool tdv[92.07,76.13,58.79])
	return false
number hzi_ <- "SyBif"
func zQ9 (number kyH[22.43,88.48])
	return false
'''
		expect = '''Program([VarDecl(Id(H2), None, var, BooleanLit(True)), FuncDecl(Id(EOaX), [VarDecl(Id(tdv), ArrayType([92.07, 76.13, 58.79], BoolType), None, None)], Return(BooleanLit(False))), VarDecl(Id(hzi_), NumberType, None, StringLit(SyBif)), FuncDecl(Id(zQ9), [VarDecl(Id(kyH), ArrayType([22.43, 88.48], NumberType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115235))

	def test_21530115236(self):
		input = '''
number O874 <- true
bool ym4p[42.27]
bool NSt6
'''
		expect = '''Program([VarDecl(Id(O874), NumberType, None, BooleanLit(True)), VarDecl(Id(ym4p), ArrayType([42.27], BoolType), None, None), VarDecl(Id(NSt6), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115236))

	def test_21530115237(self):
		input = '''
var Zg <- "r"
func kVHy (bool qdMq[48.47,19.24])	return

func SR (bool cR)
	begin
		bool c1q[17.85]
		for XW until false by true
			ff(62.02, true)
	end

'''
		expect = '''Program([VarDecl(Id(Zg), None, var, StringLit(r)), FuncDecl(Id(kVHy), [VarDecl(Id(qdMq), ArrayType([48.47, 19.24], BoolType), None, None)], Return()), FuncDecl(Id(SR), [VarDecl(Id(cR), BoolType, None, None)], Block([VarDecl(Id(c1q), ArrayType([17.85], BoolType), None, None), For(Id(XW), BooleanLit(False), BooleanLit(True), CallStmt(Id(ff), [NumLit(62.02), BooleanLit(True)]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115237))

	def test_21530115238(self):
		input = '''
number dT[81.86,27.7] <- "OhQ"
func CEV1 (string jAA, number hK3R[36.94,18.41,33.86])
	return true
'''
		expect = '''Program([VarDecl(Id(dT), ArrayType([81.86, 27.7], NumberType), None, StringLit(OhQ)), FuncDecl(Id(CEV1), [VarDecl(Id(jAA), StringType, None, None), VarDecl(Id(hK3R), ArrayType([36.94, 18.41, 33.86], NumberType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115238))

	def test_21530115239(self):
		input = '''
number fWPE[22.99,16.56,62.81] <- "TpJg"
func lrDz ()	return

'''
		expect = '''Program([VarDecl(Id(fWPE), ArrayType([22.99, 16.56, 62.81], NumberType), None, StringLit(TpJg)), FuncDecl(Id(lrDz), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115239))

	def test_21530115240(self):
		input = '''
dynamic fDN
func Dv (number OWXD, bool Z_, bool YUc[60.89,35.18])	return 12.8

bool e5kb <- PHx
number Kzxd[91.26,49.38]
'''
		expect = '''Program([VarDecl(Id(fDN), None, dynamic, None), FuncDecl(Id(Dv), [VarDecl(Id(OWXD), NumberType, None, None), VarDecl(Id(Z_), BoolType, None, None), VarDecl(Id(YUc), ArrayType([60.89, 35.18], BoolType), None, None)], Return(NumLit(12.8))), VarDecl(Id(e5kb), BoolType, None, Id(PHx)), VarDecl(Id(Kzxd), ArrayType([91.26, 49.38], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115240))

	def test_21530115241(self):
		input = '''
var pE <- true
'''
		expect = '''Program([VarDecl(Id(pE), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115241))

	def test_21530115242(self):
		input = '''
func yv ()	return

'''
		expect = '''Program([FuncDecl(Id(yv), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115242))

	def test_21530115243(self):
		input = '''
func mxvd (number FRZc, string wj9L, bool cV[80.15,16.17,42.14])
	begin
		dynamic LI6 <- "qkWm"
		begin
			if (false)
			begin
				dynamic B0F <- 90.88
				continue
			end
			continue
		end
	end
'''
		expect = '''Program([FuncDecl(Id(mxvd), [VarDecl(Id(FRZc), NumberType, None, None), VarDecl(Id(wj9L), StringType, None, None), VarDecl(Id(cV), ArrayType([80.15, 16.17, 42.14], BoolType), None, None)], Block([VarDecl(Id(LI6), None, dynamic, StringLit(qkWm)), Block([If(BooleanLit(False), Block([VarDecl(Id(B0F), None, dynamic, NumLit(90.88)), Continue])), [], None, Continue])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115243))

	def test_21530115244(self):
		input = '''
func R3 (number J4nb, number Q_l[22.43,22.36], string jnYs[58.26,75.45])	return RvPf
number yJ7[60.51,86.88]
'''
		expect = '''Program([FuncDecl(Id(R3), [VarDecl(Id(J4nb), NumberType, None, None), VarDecl(Id(Q_l), ArrayType([22.43, 22.36], NumberType), None, None), VarDecl(Id(jnYs), ArrayType([58.26, 75.45], StringType), None, None)], Return(Id(RvPf))), VarDecl(Id(yJ7), ArrayType([60.51, 86.88], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115244))

	def test_21530115245(self):
		input = '''
func iF (number Qr, number RSnU)	return
'''
		expect = '''Program([FuncDecl(Id(iF), [VarDecl(Id(Qr), NumberType, None, None), VarDecl(Id(RSnU), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115245))

	def test_21530115246(self):
		input = '''
string cuk[52.68,7.37,8.95] <- "Axgr"
func tAN ()
	return

bool Bsd[52.33] <- DAw
func sCo0 ()	begin
		var NgvB <- "fm"
	end

func jW (string r8hL, string QWo[89.81])
	return

'''
		expect = '''Program([VarDecl(Id(cuk), ArrayType([52.68, 7.37, 8.95], StringType), None, StringLit(Axgr)), FuncDecl(Id(tAN), [], Return()), VarDecl(Id(Bsd), ArrayType([52.33], BoolType), None, Id(DAw)), FuncDecl(Id(sCo0), [], Block([VarDecl(Id(NgvB), None, var, StringLit(fm))])), FuncDecl(Id(jW), [VarDecl(Id(r8hL), StringType, None, None), VarDecl(Id(QWo), ArrayType([89.81], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115246))

	def test_21530115247(self):
		input = '''
number IOj
'''
		expect = '''Program([VarDecl(Id(IOj), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115247))

	def test_21530115248(self):
		input = '''
func Ho ()
	return
string zS
dynamic dSV6 <- "gC"
var JXC <- "LL"
'''
		expect = '''Program([FuncDecl(Id(Ho), [], Return()), VarDecl(Id(zS), StringType, None, None), VarDecl(Id(dSV6), None, dynamic, StringLit(gC)), VarDecl(Id(JXC), None, var, StringLit(LL))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115248))

	def test_21530115249(self):
		input = '''
number P5[77.82,9.41,64.03]
'''
		expect = '''Program([VarDecl(Id(P5), ArrayType([77.82, 9.41, 64.03], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115249))

	def test_21530115250(self):
		input = '''
func xnp (string zI[8.01,50.95,81.62], bool aE[82.35,75.32,42.43])
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(xnp), [VarDecl(Id(zI), ArrayType([8.01, 50.95, 81.62], StringType), None, None), VarDecl(Id(aE), ArrayType([82.35, 75.32, 42.43], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115250))

	def test_21530115251(self):
		input = '''
number kvs[5.87]
string PG[81.02]
func PKH (number z6[99.71,96.75])
	return

dynamic Sb9
string i7jd[61.57] <- true
'''
		expect = '''Program([VarDecl(Id(kvs), ArrayType([5.87], NumberType), None, None), VarDecl(Id(PG), ArrayType([81.02], StringType), None, None), FuncDecl(Id(PKH), [VarDecl(Id(z6), ArrayType([99.71, 96.75], NumberType), None, None)], Return()), VarDecl(Id(Sb9), None, dynamic, None), VarDecl(Id(i7jd), ArrayType([61.57], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115251))

	def test_21530115252(self):
		input = '''
bool qm[67.32]
bool sAw <- true
func CZ (number sWz, string Aukd, number Jn[4.15,11.2,36.28])
	return olS
number BG0l
number tN <- RM7f
'''
		expect = '''Program([VarDecl(Id(qm), ArrayType([67.32], BoolType), None, None), VarDecl(Id(sAw), BoolType, None, BooleanLit(True)), FuncDecl(Id(CZ), [VarDecl(Id(sWz), NumberType, None, None), VarDecl(Id(Aukd), StringType, None, None), VarDecl(Id(Jn), ArrayType([4.15, 11.2, 36.28], NumberType), None, None)], Return(Id(olS))), VarDecl(Id(BG0l), NumberType, None, None), VarDecl(Id(tN), NumberType, None, Id(RM7f))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115252))

	def test_21530115253(self):
		input = '''
func Ulw ()
	begin
		if (40.4) O0oA <- 95.56
		elif (85.14)
		return "zT"
		elif (zSE)
		var PXrp <- "U"
		elif (Se1)
		return
		else begin
			begin
				if (false) if ("W") return
				elif (71.47)
				if (H5)
				begin
					UShi()
					begin
						continue
						for oIk until "hymxE" by 83.53
							var w2F <- 39.0
						QI7 <- "Byl"
					end
				end
				elif (87.99) DqT <- "MYA"
				elif (true)
				begin
					break
					break
					if (N4)
					continue
					elif (cCHT)
					if (64.4)
					zg22(true)
					elif (P1j) isc(UllW)
					elif (true) if (PBzt) for SH until false by true
						return false
					elif (true) dynamic Zcc <- ne
					elif (34.5) rNW7("HClc")
					elif (62.54) Aml(QAvx, false)
					elif (false)
					begin
						break
					end
					elif ("jLFl")
					begin
						eEDW <- vc
					end
					elif (false) break
					elif (J47W) continue
					elif (true) continue
					elif ("scJMx")
					s2B()
					elif (false)
					if ("Xf")
					begin
						if (44.76) Ykd0(76.15, td, "OB")
						elif ("CDaRR") bool ygd[94.3,69.18,27.0]
						else QICL <- false
					end
					elif ("zPdy")
					continue
					elif ("cLPj") begin
						return
						break
						if ("TU") if (T3wK) begin
							kj[qYIQ, 29.3] <- j4
						end
						elif (97.96)
						break
						elif (2.07) F4[true] <- 90.78
						elif ("D") for zX until false by true
							if (19.92) number OA[54.65]
							elif (mW6) if (LQF8)
							string V5Lb
							elif (BG)
							ng(91.64, true, true)
							elif (Dqo) break
							elif (qhbq)
							if (K7)
							number N02f
							elif (true)
							cnos <- "yv"
							elif (f_r) continue
							else if (vN) number JZhD[49.27,88.31,18.09] <- false
							elif (true) return lvW
							elif ("eb") if ("ihON") if (true)
							if ("psNM") WH3("NruRp")
							elif (true)
							for NQ until true by JZZ9
								uh6[Yp, 87.69] <- false
							else for QtOJ until 77.72 by 16.94
								begin
									return
									continue
									rX()
								end
							elif ("H") c0 <- 93.49
							elif ("e") continue
							elif (85.55) continue
							elif (oBUG) for qz1t until "XLBRT" by 45.1
								begin
									vn <- "uWf"
								end
							elif (11.32) begin
							end
							else break
							elif (Abdf)
							break
							elif ("H") aYs <- oA_
							elif (false) begin
								if ("TY")
								number jr5p[8.14,62.57]
								elif (true) nInH[false, 78.2, 12.62] <- DK
								elif ("M")
								begin
									if ("n") for EJf until 59.13 by "XGYF"
										break
									elif (VWVv) break
									elif (X9) continue
									elif (kn)
									pUb(pW1, 5.32)
									elif (43.35) WFL5(trRa)
									elif (h5ry)
									wBW9(qter)
									else break
									return
								end
								elif ("yzN") return 80.9
								else if (43.77) break
								elif ("YlB") Xgyo("aY", "WKK", Nk)
								elif (true) begin
									continue
								end
								elif ("C") LPx("Tpv")
								elif (2.49)
								break
								elif (20.1) bool twz
								else if (99.49) cY["yK", false] <- "vIwN"
								elif (99.35)
								bool i2[93.3,55.29] <- "mC"
								qL("fe", "R", "ygHP")
								eG2(WH7, NX3)
							end
							elif (Y3)
							QqM[true] <- 86.4
							else return "iJWEN"
							else begin
							end
						elif (false) for Aa until iuU by 43.43
							bool cn
						elif (98.48) if (78.41)
						return "XwRCz"
						elif (13.81)
						continue
						elif (43.99) DjC1(Vf, dbrb)
						elif (56.86)
						for hAf until "p" by "EcjT"
							begin
								continue
								for jx until "IqsHS" by 52.48
									if (false) begin
										break
										break
										break
									end
								for w6 until iZM by kLUc
									break
							end
						elif (eF_)
						continue
						else if (90.4) return true
						elif (H9w) begin
							aat <- "H"
						end
						elif ("pjNA") begin
							var x8 <- true
						end
						elif (49.53) if (J6X)
						break
						elif ("RSAVs") begin
							break
							break
							begin
							end
						end
						else bool D7Rb <- "m"
						elif (jUJ) xgh[19.55] <- 84.99
					end
					elif (fo) zF <- "yi"
					elif ("DvWX")
					if (6.09) nQ0()
					elif (true) Oq()
					elif (37.29) if (iy)
					continue
					elif (yfOl)
					continue
					elif (56.26) for fL2 until Krp by 27.1
						begin
							continue
							break
							if (56.35)
							for F6R until 1.9 by ba
								number RYNk
							elif (pEo) begin
								begin
									string wG[7.84]
									SjQL[false, "xa", true] <- aw
								end
								m1[Pozw, "rz"] <- "hcO"
								TwHS(true)
							end
							elif (roX) Sn()
							elif (83.08)
							zDmx <- 71.01
							else if (AjX)
							bool dkhs
							elif ("JJA") break
							elif ("a") I5U <- v9
							elif (true) if (83.22)
							for wPv5 until Rcz by X2h
								for Gu until 94.52 by 47.08
									for yj until 14.44 by uD
										string vy8O
							elif (pP)
							cjno <- false
							elif ("aK")
							if ("Pnn")
							continue
							elif (oo)
							nmcJ("VOS", 28.75)
							elif (false)
							continue
							else bool VVq[4.51,50.44,89.41]
							elif (84.73)
							for Xqh until "lTP" by 3.07
								yf <- true
							elif ("RGqK")
							continue
						end
					elif ("Ml") tOJh("gmFtG", 41.8, WKp)
					elif (49.51) continue
					else for RJQp until "rLOO" by "tUw"
						break
					elif (llwG) for hqr until 8.28 by KRq
						begin
						end
					elif ("Cs")
					break
					else FV <- "b"
					else for W1F until false by "z"
						return "vI"
				end
				elif ("AePA")
				if (Hgw) break
				elif (mp)
				for op until 44.2 by true
					continue
				elif (wm) ikSQ[O1W7, 28.91, false] <- true
				elif (false) BGp("NHo", "kgUfA")
				else begin
				end
				elif (83.71)
				o2 <- 69.55
			end
			ryXc(LZO3, 58.58, xM)
		end
		string IlFq
	end

string c63[67.24]
func Gg (string RSZU[6.5,50.26])
	return "jPR"

number k4tG[69.55,17.01]
'''
		expect = '''Program([FuncDecl(Id(Ulw), [], Block([If(NumLit(40.4), AssignStmt(Id(O0oA), NumLit(95.56))), [(NumLit(85.14), Return(StringLit(zT))), (Id(zSE), VarDecl(Id(PXrp), None, var, StringLit(U))), (Id(Se1), Return())], Block([Block([If(BooleanLit(False), If(StringLit(W), Return()), [(NumLit(71.47), If(Id(H5), Block([CallStmt(Id(UShi), []), Block([Continue, For(Id(oIk), StringLit(hymxE), NumLit(83.53), VarDecl(Id(w2F), None, var, NumLit(39.0))), AssignStmt(Id(QI7), StringLit(Byl))])])), [(NumLit(87.99), AssignStmt(Id(DqT), StringLit(MYA))), (BooleanLit(True), Block([Break, Break, If(Id(N4), Continue), [(Id(cCHT), If(NumLit(64.4), CallStmt(Id(zg22), [BooleanLit(True)])), [(Id(P1j), CallStmt(Id(isc), [Id(UllW)])), (BooleanLit(True), If(Id(PBzt), For(Id(SH), BooleanLit(False), BooleanLit(True), Return(BooleanLit(False)))), [(BooleanLit(True), VarDecl(Id(Zcc), None, dynamic, Id(ne))), (NumLit(34.5), CallStmt(Id(rNW7), [StringLit(HClc)])), (NumLit(62.54), CallStmt(Id(Aml), [Id(QAvx), BooleanLit(False)])), (BooleanLit(False), Block([Break])), (StringLit(jLFl), Block([AssignStmt(Id(eEDW), Id(vc))])), (BooleanLit(False), Break), (Id(J47W), Continue), (BooleanLit(True), Continue), (StringLit(scJMx), CallStmt(Id(s2B), [])), (BooleanLit(False), If(StringLit(Xf), Block([If(NumLit(44.76), CallStmt(Id(Ykd0), [NumLit(76.15), Id(td), StringLit(OB)])), [(StringLit(CDaRR), VarDecl(Id(ygd), ArrayType([94.3, 69.18, 27.0], BoolType), None, None))], AssignStmt(Id(QICL), BooleanLit(False))])), [(StringLit(zPdy), Continue), (StringLit(cLPj), Block([Return(), Break, If(StringLit(TU), If(Id(T3wK), Block([AssignStmt(ArrayCell(Id(kj), [Id(qYIQ), NumLit(29.3)]), Id(j4))])), [(NumLit(97.96), Break), (NumLit(2.07), AssignStmt(ArrayCell(Id(F4), [BooleanLit(True)]), NumLit(90.78))), (StringLit(D), For(Id(zX), BooleanLit(False), BooleanLit(True), If(NumLit(19.92), VarDecl(Id(OA), ArrayType([54.65], NumberType), None, None)), [(Id(mW6), If(Id(LQF8), VarDecl(Id(V5Lb), StringType, None, None)), [(Id(BG), CallStmt(Id(ng), [NumLit(91.64), BooleanLit(True), BooleanLit(True)])), (Id(Dqo), Break), (Id(qhbq), If(Id(K7), VarDecl(Id(N02f), NumberType, None, None)), [(BooleanLit(True), AssignStmt(Id(cnos), StringLit(yv))), (Id(f_r), Continue)], If(Id(vN), VarDecl(Id(JZhD), ArrayType([49.27, 88.31, 18.09], NumberType), None, BooleanLit(False))), [(BooleanLit(True), Return(Id(lvW))), (StringLit(eb), If(StringLit(ihON), If(BooleanLit(True), If(StringLit(psNM), CallStmt(Id(WH3), [StringLit(NruRp)])), [(BooleanLit(True), For(Id(NQ), BooleanLit(True), Id(JZZ9), AssignStmt(ArrayCell(Id(uh6), [Id(Yp), NumLit(87.69)]), BooleanLit(False))))], For(Id(QtOJ), NumLit(77.72), NumLit(16.94), Block([Return(), Continue, CallStmt(Id(rX), [])]))), [(StringLit(H), AssignStmt(Id(c0), NumLit(93.49))), (StringLit(e), Continue), (NumLit(85.55), Continue), (Id(oBUG), For(Id(qz1t), StringLit(XLBRT), NumLit(45.1), Block([AssignStmt(Id(vn), StringLit(uWf))]))), (NumLit(11.32), Block([]))], Break), [(Id(Abdf), Break), (StringLit(H), AssignStmt(Id(aYs), Id(oA_))), (BooleanLit(False), Block([If(StringLit(TY), VarDecl(Id(jr5p), ArrayType([8.14, 62.57], NumberType), None, None)), [(BooleanLit(True), AssignStmt(ArrayCell(Id(nInH), [BooleanLit(False), NumLit(78.2), NumLit(12.62)]), Id(DK))), (StringLit(M), Block([If(StringLit(n), For(Id(EJf), NumLit(59.13), StringLit(XGYF), Break)), [(Id(VWVv), Break), (Id(X9), Continue), (Id(kn), CallStmt(Id(pUb), [Id(pW1), NumLit(5.32)])), (NumLit(43.35), CallStmt(Id(WFL5), [Id(trRa)])), (Id(h5ry), CallStmt(Id(wBW9), [Id(qter)]))], Break, Return()])), (StringLit(yzN), Return(NumLit(80.9)))], If(NumLit(43.77), Break), [(StringLit(YlB), CallStmt(Id(Xgyo), [StringLit(aY), StringLit(WKK), Id(Nk)])), (BooleanLit(True), Block([Continue])), (StringLit(C), CallStmt(Id(LPx), [StringLit(Tpv)])), (NumLit(2.49), Break), (NumLit(20.1), VarDecl(Id(twz), BoolType, None, None))], If(NumLit(99.49), AssignStmt(ArrayCell(Id(cY), [StringLit(yK), BooleanLit(False)]), StringLit(vIwN))), [(NumLit(99.35), VarDecl(Id(i2), ArrayType([93.3, 55.29], BoolType), None, StringLit(mC)))], None, CallStmt(Id(qL), [StringLit(fe), StringLit(R), StringLit(ygHP)]), CallStmt(Id(eG2), [Id(WH7), Id(NX3)])])), (Id(Y3), AssignStmt(ArrayCell(Id(QqM), [BooleanLit(True)]), NumLit(86.4)))], Return(StringLit(iJWEN)))], Block([])), (BooleanLit(False), For(Id(Aa), Id(iuU), NumLit(43.43), VarDecl(Id(cn), BoolType, None, None))), (NumLit(98.48), If(NumLit(78.41), Return(StringLit(XwRCz))), [(NumLit(13.81), Continue), (NumLit(43.99), CallStmt(Id(DjC1), [Id(Vf), Id(dbrb)])), (NumLit(56.86), For(Id(hAf), StringLit(p), StringLit(EcjT), Block([Continue, For(Id(jx), StringLit(IqsHS), NumLit(52.48), If(BooleanLit(False), Block([Break, Break, Break])), [], None), For(Id(w6), Id(iZM), Id(kLUc), Break)]))), (Id(eF_), Continue)], If(NumLit(90.4), Return(BooleanLit(True))), [(Id(H9w), Block([AssignStmt(Id(aat), StringLit(H))])), (StringLit(pjNA), Block([VarDecl(Id(x8), None, var, BooleanLit(True))])), (NumLit(49.53), If(Id(J6X), Break), [(StringLit(RSAVs), Block([Break, Break, Block([])]))], VarDecl(Id(D7Rb), BoolType, None, StringLit(m))), (Id(jUJ), AssignStmt(ArrayCell(Id(xgh), [NumLit(19.55)]), NumLit(84.99)))], None)], None)], None))], None), [], None])), (Id(fo), AssignStmt(Id(zF), StringLit(yi))), (StringLit(DvWX), If(NumLit(6.09), CallStmt(Id(nQ0), [])), [(BooleanLit(True), CallStmt(Id(Oq), [])), (NumLit(37.29), If(Id(iy), Continue), [(Id(yfOl), Continue), (NumLit(56.26), For(Id(fL2), Id(Krp), NumLit(27.1), Block([Continue, Break, If(NumLit(56.35), For(Id(F6R), NumLit(1.9), Id(ba), VarDecl(Id(RYNk), NumberType, None, None))), [(Id(pEo), Block([Block([VarDecl(Id(wG), ArrayType([7.84], StringType), None, None), AssignStmt(ArrayCell(Id(SjQL), [BooleanLit(False), StringLit(xa), BooleanLit(True)]), Id(aw))]), AssignStmt(ArrayCell(Id(m1), [Id(Pozw), StringLit(rz)]), StringLit(hcO)), CallStmt(Id(TwHS), [BooleanLit(True)])])), (Id(roX), CallStmt(Id(Sn), [])), (NumLit(83.08), AssignStmt(Id(zDmx), NumLit(71.01)))], If(Id(AjX), VarDecl(Id(dkhs), BoolType, None, None)), [(StringLit(JJA), Break), (StringLit(a), AssignStmt(Id(I5U), Id(v9))), (BooleanLit(True), If(NumLit(83.22), For(Id(wPv5), Id(Rcz), Id(X2h), For(Id(Gu), NumLit(94.52), NumLit(47.08), For(Id(yj), NumLit(14.44), Id(uD), VarDecl(Id(vy8O), StringType, None, None))))), [(Id(pP), AssignStmt(Id(cjno), BooleanLit(False))), (StringLit(aK), If(StringLit(Pnn), Continue), [(Id(oo), CallStmt(Id(nmcJ), [StringLit(VOS), NumLit(28.75)])), (BooleanLit(False), Continue)], VarDecl(Id(VVq), ArrayType([4.51, 50.44, 89.41], BoolType), None, None)), (NumLit(84.73), For(Id(Xqh), StringLit(lTP), NumLit(3.07), AssignStmt(Id(yf), BooleanLit(True)))), (StringLit(RGqK), Continue)], None)], None]))), (StringLit(Ml), CallStmt(Id(tOJh), [StringLit(gmFtG), NumLit(41.8), Id(WKp)])), (NumLit(49.51), Continue)], For(Id(RJQp), StringLit(rLOO), StringLit(tUw), Break)), (Id(llwG), For(Id(hqr), NumLit(8.28), Id(KRq), Block([]))), (StringLit(Cs), Break)], AssignStmt(Id(FV), StringLit(b)))], For(Id(W1F), BooleanLit(False), StringLit(z), Return(StringLit(vI))))], None)], None)], None])), (StringLit(AePA), If(Id(Hgw), Break), [(Id(mp), For(Id(op), NumLit(44.2), BooleanLit(True), Continue)), (Id(wm), AssignStmt(ArrayCell(Id(ikSQ), [Id(O1W7), NumLit(28.91), BooleanLit(False)]), BooleanLit(True))), (BooleanLit(False), CallStmt(Id(BGp), [StringLit(NHo), StringLit(kgUfA)]))], Block([])), (NumLit(83.71), AssignStmt(Id(o2), NumLit(69.55)))], None)], None), [], None]), CallStmt(Id(ryXc), [Id(LZO3), NumLit(58.58), Id(xM)])]), VarDecl(Id(IlFq), StringType, None, None)])), VarDecl(Id(c63), ArrayType([67.24], StringType), None, None), FuncDecl(Id(Gg), [VarDecl(Id(RSZU), ArrayType([6.5, 50.26], StringType), None, None)], Return(StringLit(jPR))), VarDecl(Id(k4tG), ArrayType([69.55, 17.01], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115253))

	def test_21530115254(self):
		input = '''
func cGQq (string lV, bool I4)
	return 6.78

bool hub <- false
'''
		expect = '''Program([FuncDecl(Id(cGQq), [VarDecl(Id(lV), StringType, None, None), VarDecl(Id(I4), BoolType, None, None)], Return(NumLit(6.78))), VarDecl(Id(hub), BoolType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115254))

	def test_21530115255(self):
		input = '''
func cmHS (number rq, bool i7, bool inBK[86.58,7.06])	return
'''
		expect = '''Program([FuncDecl(Id(cmHS), [VarDecl(Id(rq), NumberType, None, None), VarDecl(Id(i7), BoolType, None, None), VarDecl(Id(inBK), ArrayType([86.58, 7.06], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115255))

	def test_21530115256(self):
		input = '''
var NHs <- 59.79
string jZo[67.67,30.44,77.99]
bool NU[16.79] <- ve83
'''
		expect = '''Program([VarDecl(Id(NHs), None, var, NumLit(59.79)), VarDecl(Id(jZo), ArrayType([67.67, 30.44, 77.99], StringType), None, None), VarDecl(Id(NU), ArrayType([16.79], BoolType), None, Id(ve83))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115256))

	def test_21530115257(self):
		input = '''
bool xhkR
func VC (bool Dbch[78.07,69.86,21.39], number dC[19.47], bool KY4V)	begin
		sg()
		bool Tj_[91.15]
	end

string sj
func i_JM (string NlI, number omy[47.64,31.14])
	return

func Yj ()
	return

'''
		expect = '''Program([VarDecl(Id(xhkR), BoolType, None, None), FuncDecl(Id(VC), [VarDecl(Id(Dbch), ArrayType([78.07, 69.86, 21.39], BoolType), None, None), VarDecl(Id(dC), ArrayType([19.47], NumberType), None, None), VarDecl(Id(KY4V), BoolType, None, None)], Block([CallStmt(Id(sg), []), VarDecl(Id(Tj_), ArrayType([91.15], BoolType), None, None)])), VarDecl(Id(sj), StringType, None, None), FuncDecl(Id(i_JM), [VarDecl(Id(NlI), StringType, None, None), VarDecl(Id(omy), ArrayType([47.64, 31.14], NumberType), None, None)], Return()), FuncDecl(Id(Yj), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115257))

	def test_21530115258(self):
		input = '''
func R6Rr (bool SFJh[19.48,45.33,74.45], bool wDX[72.46])
	return 62.56

func N3dS (bool e7d)
	begin
	end
var Bg <- 98.19
func u5t (bool ZLQA[2.89,16.35])	return
'''
		expect = '''Program([FuncDecl(Id(R6Rr), [VarDecl(Id(SFJh), ArrayType([19.48, 45.33, 74.45], BoolType), None, None), VarDecl(Id(wDX), ArrayType([72.46], BoolType), None, None)], Return(NumLit(62.56))), FuncDecl(Id(N3dS), [VarDecl(Id(e7d), BoolType, None, None)], Block([])), VarDecl(Id(Bg), None, var, NumLit(98.19)), FuncDecl(Id(u5t), [VarDecl(Id(ZLQA), ArrayType([2.89, 16.35], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115258))

	def test_21530115259(self):
		input = '''
dynamic ULY
bool UX[50.42]
number Su[40.68,60.21,41.12] <- "A"
bool Dq[58.71,33.1,36.62]
func sG_ (number Eu[12.81])	return 25.83

'''
		expect = '''Program([VarDecl(Id(ULY), None, dynamic, None), VarDecl(Id(UX), ArrayType([50.42], BoolType), None, None), VarDecl(Id(Su), ArrayType([40.68, 60.21, 41.12], NumberType), None, StringLit(A)), VarDecl(Id(Dq), ArrayType([58.71, 33.1, 36.62], BoolType), None, None), FuncDecl(Id(sG_), [VarDecl(Id(Eu), ArrayType([12.81], NumberType), None, None)], Return(NumLit(25.83)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115259))

	def test_21530115260(self):
		input = '''
func gLW ()
	return
bool Il4x[41.42,75.57,79.38] <- 18.3
number wbPF[76.39,32.81,25.89]
'''
		expect = '''Program([FuncDecl(Id(gLW), [], Return()), VarDecl(Id(Il4x), ArrayType([41.42, 75.57, 79.38], BoolType), None, NumLit(18.3)), VarDecl(Id(wbPF), ArrayType([76.39, 32.81, 25.89], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115260))

	def test_21530115261(self):
		input = '''
string Uu[29.52,82.65]
string NXv <- 19.95
func U80w (number v_xX)
	return
'''
		expect = '''Program([VarDecl(Id(Uu), ArrayType([29.52, 82.65], StringType), None, None), VarDecl(Id(NXv), StringType, None, NumLit(19.95)), FuncDecl(Id(U80w), [VarDecl(Id(v_xX), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115261))

	def test_21530115262(self):
		input = '''
func rS (bool fX[92.13,19.14,99.86], string PIy6)	return
'''
		expect = '''Program([FuncDecl(Id(rS), [VarDecl(Id(fX), ArrayType([92.13, 19.14, 99.86], BoolType), None, None), VarDecl(Id(PIy6), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115262))

	def test_21530115263(self):
		input = '''
func rc (number Wf1)	return
'''
		expect = '''Program([FuncDecl(Id(rc), [VarDecl(Id(Wf1), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115263))

	def test_21530115264(self):
		input = '''
dynamic M21X
func hjLt ()
	begin
		begin
		end
		KH("kNUj", 13.34)
		return
	end

'''
		expect = '''Program([VarDecl(Id(M21X), None, dynamic, None), FuncDecl(Id(hjLt), [], Block([Block([]), CallStmt(Id(KH), [StringLit(kNUj), NumLit(13.34)]), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115264))

	def test_21530115265(self):
		input = '''
func PPkA ()
	return
dynamic cdL <- "Bu"
func GeD (number SG)	begin
	end

string opn[42.43,60.39] <- 66.12
func evD (string jGh0)
	return
'''
		expect = '''Program([FuncDecl(Id(PPkA), [], Return()), VarDecl(Id(cdL), None, dynamic, StringLit(Bu)), FuncDecl(Id(GeD), [VarDecl(Id(SG), NumberType, None, None)], Block([])), VarDecl(Id(opn), ArrayType([42.43, 60.39], StringType), None, NumLit(66.12)), FuncDecl(Id(evD), [VarDecl(Id(jGh0), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115265))

	def test_21530115266(self):
		input = '''
func qNjh (number PV34[42.8], string muzs[48.34,11.85,72.02])
	begin
		qrzq()
		OT()
	end
dynamic MmF
func Wbqj (number MrxX[30.33], number M6[89.51], number Q2RS[7.64,80.55])
	return
bool iSMC[81.38,94.24,40.4] <- 73.82
func cf3 (number aQR)
	return "qJr"
'''
		expect = '''Program([FuncDecl(Id(qNjh), [VarDecl(Id(PV34), ArrayType([42.8], NumberType), None, None), VarDecl(Id(muzs), ArrayType([48.34, 11.85, 72.02], StringType), None, None)], Block([CallStmt(Id(qrzq), []), CallStmt(Id(OT), [])])), VarDecl(Id(MmF), None, dynamic, None), FuncDecl(Id(Wbqj), [VarDecl(Id(MrxX), ArrayType([30.33], NumberType), None, None), VarDecl(Id(M6), ArrayType([89.51], NumberType), None, None), VarDecl(Id(Q2RS), ArrayType([7.64, 80.55], NumberType), None, None)], Return()), VarDecl(Id(iSMC), ArrayType([81.38, 94.24, 40.4], BoolType), None, NumLit(73.82)), FuncDecl(Id(cf3), [VarDecl(Id(aQR), NumberType, None, None)], Return(StringLit(qJr)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115266))

	def test_21530115267(self):
		input = '''
func DD (number yhxa[91.08,26.41,5.22], number mVA, string t8i[92.79,17.56,29.54])	return false

'''
		expect = '''Program([FuncDecl(Id(DD), [VarDecl(Id(yhxa), ArrayType([91.08, 26.41, 5.22], NumberType), None, None), VarDecl(Id(mVA), NumberType, None, None), VarDecl(Id(t8i), ArrayType([92.79, 17.56, 29.54], StringType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115267))

	def test_21530115268(self):
		input = '''
number fPy2[42.21,39.68] <- 11.89
func vuC ()
	begin
	end

dynamic wjlp
bool Zf[18.55,11.9]
var Rx <- true
'''
		expect = '''Program([VarDecl(Id(fPy2), ArrayType([42.21, 39.68], NumberType), None, NumLit(11.89)), FuncDecl(Id(vuC), [], Block([])), VarDecl(Id(wjlp), None, dynamic, None), VarDecl(Id(Zf), ArrayType([18.55, 11.9], BoolType), None, None), VarDecl(Id(Rx), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115268))

	def test_21530115269(self):
		input = '''
bool oypE[8.65,20.71,52.34] <- false
'''
		expect = '''Program([VarDecl(Id(oypE), ArrayType([8.65, 20.71, 52.34], BoolType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115269))

	def test_21530115270(self):
		input = '''
dynamic fJT
number H0Z[99.0,3.14,37.1]
number P2Sl <- false
string vj[65.56] <- "Bn"
number ahu[16.77,49.83]
'''
		expect = '''Program([VarDecl(Id(fJT), None, dynamic, None), VarDecl(Id(H0Z), ArrayType([99.0, 3.14, 37.1], NumberType), None, None), VarDecl(Id(P2Sl), NumberType, None, BooleanLit(False)), VarDecl(Id(vj), ArrayType([65.56], StringType), None, StringLit(Bn)), VarDecl(Id(ahu), ArrayType([16.77, 49.83], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115270))

	def test_21530115271(self):
		input = '''
dynamic Xx
bool Eb[65.42,44.69,67.71]
string Oiz
'''
		expect = '''Program([VarDecl(Id(Xx), None, dynamic, None), VarDecl(Id(Eb), ArrayType([65.42, 44.69, 67.71], BoolType), None, None), VarDecl(Id(Oiz), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115271))

	def test_21530115272(self):
		input = '''
func ui (string pek[11.28,83.13,7.5])	begin
		KWEo <- ON4
		if ("YE") if (false)
		for HP until wXK by uMi
			continue
		elif ("Y") N2(eD)
		elif (true)
		string eZAF[59.96]
		else begin
			zan(6.2, true, E7o)
		end
		elif ("LS") return false
		elif (false)
		b9X <- xk
		elif (Sf) YXY <- true
	end

number OSdW[65.57]
bool Tzv[24.17,24.49] <- true
'''
		expect = '''Program([FuncDecl(Id(ui), [VarDecl(Id(pek), ArrayType([11.28, 83.13, 7.5], StringType), None, None)], Block([AssignStmt(Id(KWEo), Id(ON4)), If(StringLit(YE), If(BooleanLit(False), For(Id(HP), Id(wXK), Id(uMi), Continue)), [(StringLit(Y), CallStmt(Id(N2), [Id(eD)])), (BooleanLit(True), VarDecl(Id(eZAF), ArrayType([59.96], StringType), None, None))], Block([CallStmt(Id(zan), [NumLit(6.2), BooleanLit(True), Id(E7o)])])), [(StringLit(LS), Return(BooleanLit(False))), (BooleanLit(False), AssignStmt(Id(b9X), Id(xk))), (Id(Sf), AssignStmt(Id(YXY), BooleanLit(True)))], None])), VarDecl(Id(OSdW), ArrayType([65.57], NumberType), None, None), VarDecl(Id(Tzv), ArrayType([24.17, 24.49], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115272))

	def test_21530115273(self):
		input = '''
string AFq1 <- false
'''
		expect = '''Program([VarDecl(Id(AFq1), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115273))

	def test_21530115274(self):
		input = '''
number OpNw[86.64,28.63]
number spWL <- "wnR"
func Zoh (number lu3I)
	begin
		Qv("TdaGo", false, P_Hu)
		continue
	end

'''
		expect = '''Program([VarDecl(Id(OpNw), ArrayType([86.64, 28.63], NumberType), None, None), VarDecl(Id(spWL), NumberType, None, StringLit(wnR)), FuncDecl(Id(Zoh), [VarDecl(Id(lu3I), NumberType, None, None)], Block([CallStmt(Id(Qv), [StringLit(TdaGo), BooleanLit(False), Id(P_Hu)]), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115274))

	def test_21530115275(self):
		input = '''
number AZ8H <- "Rf"
bool yU_[69.76,75.35,35.55]
bool zrh5[12.34] <- "ZrvZ"
'''
		expect = '''Program([VarDecl(Id(AZ8H), NumberType, None, StringLit(Rf)), VarDecl(Id(yU_), ArrayType([69.76, 75.35, 35.55], BoolType), None, None), VarDecl(Id(zrh5), ArrayType([12.34], BoolType), None, StringLit(ZrvZ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115275))

	def test_21530115276(self):
		input = '''
string nR[75.7] <- true
'''
		expect = '''Program([VarDecl(Id(nR), ArrayType([75.7], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115276))

	def test_21530115277(self):
		input = '''
func DU (number CO)	return N2oj
dynamic W3
func Nn ()
	return 54.97
'''
		expect = '''Program([FuncDecl(Id(DU), [VarDecl(Id(CO), NumberType, None, None)], Return(Id(N2oj))), VarDecl(Id(W3), None, dynamic, None), FuncDecl(Id(Nn), [], Return(NumLit(54.97)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115277))

	def test_21530115278(self):
		input = '''
number T3[15.23,10.69,69.48]
'''
		expect = '''Program([VarDecl(Id(T3), ArrayType([15.23, 10.69, 69.48], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115278))

	def test_21530115279(self):
		input = '''
number Uvb8[71.21] <- 1.53
func ljiG ()	begin
	end

'''
		expect = '''Program([VarDecl(Id(Uvb8), ArrayType([71.21], NumberType), None, NumLit(1.53)), FuncDecl(Id(ljiG), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115279))

	def test_21530115280(self):
		input = '''
func rqi (number hc, bool WZ[12.05], number FZe)
	return
number v0
func nwx (bool Bcp[9.2])
	return

func JtSZ (number DS5)	begin
		return
	end

bool DalQ <- false
'''
		expect = '''Program([FuncDecl(Id(rqi), [VarDecl(Id(hc), NumberType, None, None), VarDecl(Id(WZ), ArrayType([12.05], BoolType), None, None), VarDecl(Id(FZe), NumberType, None, None)], Return()), VarDecl(Id(v0), NumberType, None, None), FuncDecl(Id(nwx), [VarDecl(Id(Bcp), ArrayType([9.2], BoolType), None, None)], Return()), FuncDecl(Id(JtSZ), [VarDecl(Id(DS5), NumberType, None, None)], Block([Return()])), VarDecl(Id(DalQ), BoolType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115280))

	def test_21530115281(self):
		input = '''
func CA (bool R9z, string VUOt, number tJN[84.33,17.28,41.15])
	begin
		break
		return false
		begin
			return 76.77
		end
	end
'''
		expect = '''Program([FuncDecl(Id(CA), [VarDecl(Id(R9z), BoolType, None, None), VarDecl(Id(VUOt), StringType, None, None), VarDecl(Id(tJN), ArrayType([84.33, 17.28, 41.15], NumberType), None, None)], Block([Break, Return(BooleanLit(False)), Block([Return(NumLit(76.77))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115281))

	def test_21530115282(self):
		input = '''
string z8aL <- 27.06
dynamic HD5K
func yh (bool KwZ[52.65,69.63])	begin
		hTU(false, true)
		Ti1v()
	end

'''
		expect = '''Program([VarDecl(Id(z8aL), StringType, None, NumLit(27.06)), VarDecl(Id(HD5K), None, dynamic, None), FuncDecl(Id(yh), [VarDecl(Id(KwZ), ArrayType([52.65, 69.63], BoolType), None, None)], Block([CallStmt(Id(hTU), [BooleanLit(False), BooleanLit(True)]), CallStmt(Id(Ti1v), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115282))

	def test_21530115283(self):
		input = '''
bool q6GG[46.7,96.33] <- false
func MX (number rI[52.94,81.02], number yYb[38.68,53.04])	begin
		LAOm(false, 91.96, 90.34)
		begin
			continue
		end
	end

number yaE0[8.06] <- false
number KDF <- 93.42
'''
		expect = '''Program([VarDecl(Id(q6GG), ArrayType([46.7, 96.33], BoolType), None, BooleanLit(False)), FuncDecl(Id(MX), [VarDecl(Id(rI), ArrayType([52.94, 81.02], NumberType), None, None), VarDecl(Id(yYb), ArrayType([38.68, 53.04], NumberType), None, None)], Block([CallStmt(Id(LAOm), [BooleanLit(False), NumLit(91.96), NumLit(90.34)]), Block([Continue])])), VarDecl(Id(yaE0), ArrayType([8.06], NumberType), None, BooleanLit(False)), VarDecl(Id(KDF), NumberType, None, NumLit(93.42))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115283))

	def test_21530115284(self):
		input = '''
bool jBx[26.03,93.21] <- "cvBgN"
number Gfa[3.02,49.12] <- wZ
number W5[69.92]
func RA ()
	begin
		if (35.61)
		hQc <- "mBJNW"
		elif (u4y)
		for yiu until 38.4 by "C"
			break
		elif (63.1)
		if (wh) begin
			begin
				break
			end
			for vH until U3xp by true
				break
			if (Eo) break
			elif (fY) return
			elif (false)
			break
		end
		else OT("GAqb", "LzXn")
		for UBDn until "ZAfZR" by "DTDI"
			for I_aU until 93.22 by "jAXuL"
				for kVF until true by 28.85
					return Ro
	end
'''
		expect = '''Program([VarDecl(Id(jBx), ArrayType([26.03, 93.21], BoolType), None, StringLit(cvBgN)), VarDecl(Id(Gfa), ArrayType([3.02, 49.12], NumberType), None, Id(wZ)), VarDecl(Id(W5), ArrayType([69.92], NumberType), None, None), FuncDecl(Id(RA), [], Block([If(NumLit(35.61), AssignStmt(Id(hQc), StringLit(mBJNW))), [(Id(u4y), For(Id(yiu), NumLit(38.4), StringLit(C), Break)), (NumLit(63.1), If(Id(wh), Block([Block([Break]), For(Id(vH), Id(U3xp), BooleanLit(True), Break), If(Id(Eo), Break), [(Id(fY), Return()), (BooleanLit(False), Break)], None])), [], CallStmt(Id(OT), [StringLit(GAqb), StringLit(LzXn)]))], None, For(Id(UBDn), StringLit(ZAfZR), StringLit(DTDI), For(Id(I_aU), NumLit(93.22), StringLit(jAXuL), For(Id(kVF), BooleanLit(True), NumLit(28.85), Return(Id(Ro)))))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115284))

	def test_21530115285(self):
		input = '''
func cleR (string VKjh[78.09,84.09,42.67], bool xjtI, string jRs4[64.32])	return xdx
'''
		expect = '''Program([FuncDecl(Id(cleR), [VarDecl(Id(VKjh), ArrayType([78.09, 84.09, 42.67], StringType), None, None), VarDecl(Id(xjtI), BoolType, None, None), VarDecl(Id(jRs4), ArrayType([64.32], StringType), None, None)], Return(Id(xdx)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115285))

	def test_21530115286(self):
		input = '''
bool bx
'''
		expect = '''Program([VarDecl(Id(bx), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115286))

	def test_21530115287(self):
		input = '''
string EQ[8.13]
bool pl
bool Fyrl[46.34] <- n9
func GN (bool FS[60.03,24.3,8.41], string no)
	begin
		break
		break
		begin
		end
	end
'''
		expect = '''Program([VarDecl(Id(EQ), ArrayType([8.13], StringType), None, None), VarDecl(Id(pl), BoolType, None, None), VarDecl(Id(Fyrl), ArrayType([46.34], BoolType), None, Id(n9)), FuncDecl(Id(GN), [VarDecl(Id(FS), ArrayType([60.03, 24.3, 8.41], BoolType), None, None), VarDecl(Id(no), StringType, None, None)], Block([Break, Break, Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115287))

	def test_21530115288(self):
		input = '''
func jVBH ()	begin
		if (50.54) ILH[c2, "Si"] <- 57.61
		elif ("Orlw")
		SoY5 <- 89.85
		else G3[XE, false] <- 83.91
		return false
	end
number g3_[18.2,40.74,42.5] <- "wCq"
'''
		expect = '''Program([FuncDecl(Id(jVBH), [], Block([If(NumLit(50.54), AssignStmt(ArrayCell(Id(ILH), [Id(c2), StringLit(Si)]), NumLit(57.61))), [(StringLit(Orlw), AssignStmt(Id(SoY5), NumLit(89.85)))], AssignStmt(ArrayCell(Id(G3), [Id(XE), BooleanLit(False)]), NumLit(83.91)), Return(BooleanLit(False))])), VarDecl(Id(g3_), ArrayType([18.2, 40.74, 42.5], NumberType), None, StringLit(wCq))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115288))

	def test_21530115289(self):
		input = '''
func wJ (string BL, number bnG[63.16,83.41,5.71], number JZen)	begin
		return true
		bool Ub0T <- "S"
		if ("MMUoQ") break
		else o2(37.09)
	end

string jUaa[41.87,20.84,36.85]
bool ySD[75.96,99.55]
'''
		expect = '''Program([FuncDecl(Id(wJ), [VarDecl(Id(BL), StringType, None, None), VarDecl(Id(bnG), ArrayType([63.16, 83.41, 5.71], NumberType), None, None), VarDecl(Id(JZen), NumberType, None, None)], Block([Return(BooleanLit(True)), VarDecl(Id(Ub0T), BoolType, None, StringLit(S)), If(StringLit(MMUoQ), Break), [], CallStmt(Id(o2), [NumLit(37.09)])])), VarDecl(Id(jUaa), ArrayType([41.87, 20.84, 36.85], StringType), None, None), VarDecl(Id(ySD), ArrayType([75.96, 99.55], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115289))

	def test_21530115290(self):
		input = '''
number jK[2.26] <- "DJEcw"
func gth (number TWh[60.27,74.94,64.11], number uwB[15.36,34.42], bool how)
	return gxP

'''
		expect = '''Program([VarDecl(Id(jK), ArrayType([2.26], NumberType), None, StringLit(DJEcw)), FuncDecl(Id(gth), [VarDecl(Id(TWh), ArrayType([60.27, 74.94, 64.11], NumberType), None, None), VarDecl(Id(uwB), ArrayType([15.36, 34.42], NumberType), None, None), VarDecl(Id(how), BoolType, None, None)], Return(Id(gxP)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115290))

	def test_21530115291(self):
		input = '''
func Mg (number qO, string LK4Q[17.91,64.18], string KE[3.02])
	return 88.68

func PG (number D7Ft[10.21], number Tqzg[89.11,36.63,41.51])
	return 31.27
'''
		expect = '''Program([FuncDecl(Id(Mg), [VarDecl(Id(qO), NumberType, None, None), VarDecl(Id(LK4Q), ArrayType([17.91, 64.18], StringType), None, None), VarDecl(Id(KE), ArrayType([3.02], StringType), None, None)], Return(NumLit(88.68))), FuncDecl(Id(PG), [VarDecl(Id(D7Ft), ArrayType([10.21], NumberType), None, None), VarDecl(Id(Tqzg), ArrayType([89.11, 36.63, 41.51], NumberType), None, None)], Return(NumLit(31.27)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115291))

	def test_21530115292(self):
		input = '''
func KDaw (number ywK[90.44,72.1,48.83], string cE[26.84,95.35], string Q1[17.56])	return
'''
		expect = '''Program([FuncDecl(Id(KDaw), [VarDecl(Id(ywK), ArrayType([90.44, 72.1, 48.83], NumberType), None, None), VarDecl(Id(cE), ArrayType([26.84, 95.35], StringType), None, None), VarDecl(Id(Q1), ArrayType([17.56], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115292))

	def test_21530115293(self):
		input = '''
func sm7p (string hHA, bool vROF)	return
func Cs (bool WF[13.67,45.18,46.47])	return false
'''
		expect = '''Program([FuncDecl(Id(sm7p), [VarDecl(Id(hHA), StringType, None, None), VarDecl(Id(vROF), BoolType, None, None)], Return()), FuncDecl(Id(Cs), [VarDecl(Id(WF), ArrayType([13.67, 45.18, 46.47], BoolType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115293))

	def test_21530115294(self):
		input = '''
func gN (bool AFA[4.39])
	return
bool m3[17.46] <- bsT9
'''
		expect = '''Program([FuncDecl(Id(gN), [VarDecl(Id(AFA), ArrayType([4.39], BoolType), None, None)], Return()), VarDecl(Id(m3), ArrayType([17.46], BoolType), None, Id(bsT9))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115294))

	def test_21530115295(self):
		input = '''
func Uy0 (string Da, number rn[64.32,38.8,21.02])	begin
		reg(true, 19.42, false)
		for nDH until "Uh" by 62.31
			bool F_Q
		bool sw5[31.19,76.97] <- Ht_2
	end

'''
		expect = '''Program([FuncDecl(Id(Uy0), [VarDecl(Id(Da), StringType, None, None), VarDecl(Id(rn), ArrayType([64.32, 38.8, 21.02], NumberType), None, None)], Block([CallStmt(Id(reg), [BooleanLit(True), NumLit(19.42), BooleanLit(False)]), For(Id(nDH), StringLit(Uh), NumLit(62.31), VarDecl(Id(F_Q), BoolType, None, None)), VarDecl(Id(sw5), ArrayType([31.19, 76.97], BoolType), None, Id(Ht_2))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115295))

	def test_21530115296(self):
		input = '''
string PxGR[53.57,65.54,18.1] <- ES
'''
		expect = '''Program([VarDecl(Id(PxGR), ArrayType([53.57, 65.54, 18.1], StringType), None, Id(ES))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115296))

	def test_21530115297(self):
		input = '''
string hSR_ <- kd
func X2 (bool GyUw, bool oyI, number gwi)	return true
func NCJu (number as)
	return

func zTcY (bool Hf9, number oqY8[8.81])	begin
		if (Pd)
		begin
			dBt()
		end
		else return
		return
	end

func gt (number kq8Y, string iz[60.43], string SAM)
	begin
		i4[true] <- false
		if (D0) bDg(57.43)
		elif (91.99) bool dbL[65.76,15.76,64.45]
		elif ("tZiYB")
		Cn[84.58, 16.06, true] <- wQ
		else if ("T") if (hfm) for cGH until false by "i"
			Tbf(true, oF6a, true)
		elif (0.65) VQkW(true, "CdOTA")
		elif (xLq) in_ <- 39.94
		else return 5.53
		elif (94.41)
		eg <- 51.1
		elif (25.22)
		begin
			if ("Xy") dynamic E7
			elif (CNl) return
			elif ("EEoKK")
			if (OsZ) if (OnvT) for zMBC until AA by "NsYh"
				for SuE until "sHk" by "TfUZ"
					Bm[56.18] <- jNu
			elif ("T") continue
			elif (0.33) begin
				break
				begin
					JTo[true, false] <- 60.23
					for YR until "Irbmz" by false
						begin
						end
				end
				string t4Q
			end
			elif (91.58)
			continue
			elif (esl)
			lUzl(Lp)
			elif ("hCX") begin
				ZjjC(98.7, "aq", false)
				TO(54.35, Un, 49.91)
			end
			else number FDUm[86.87] <- false
			return
			break
		end
		elif (85.49)
		smWV()
		elif ("pg")
		break
		elif ("GQag")
		zr7[Zh, 67.42] <- false
		return
	end

'''
		expect = '''Program([VarDecl(Id(hSR_), StringType, None, Id(kd)), FuncDecl(Id(X2), [VarDecl(Id(GyUw), BoolType, None, None), VarDecl(Id(oyI), BoolType, None, None), VarDecl(Id(gwi), NumberType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(NCJu), [VarDecl(Id(as), NumberType, None, None)], Return()), FuncDecl(Id(zTcY), [VarDecl(Id(Hf9), BoolType, None, None), VarDecl(Id(oqY8), ArrayType([8.81], NumberType), None, None)], Block([If(Id(Pd), Block([CallStmt(Id(dBt), [])])), [], Return(), Return()])), FuncDecl(Id(gt), [VarDecl(Id(kq8Y), NumberType, None, None), VarDecl(Id(iz), ArrayType([60.43], StringType), None, None), VarDecl(Id(SAM), StringType, None, None)], Block([AssignStmt(ArrayCell(Id(i4), [BooleanLit(True)]), BooleanLit(False)), If(Id(D0), CallStmt(Id(bDg), [NumLit(57.43)])), [(NumLit(91.99), VarDecl(Id(dbL), ArrayType([65.76, 15.76, 64.45], BoolType), None, None)), (StringLit(tZiYB), AssignStmt(ArrayCell(Id(Cn), [NumLit(84.58), NumLit(16.06), BooleanLit(True)]), Id(wQ)))], If(StringLit(T), If(Id(hfm), For(Id(cGH), BooleanLit(False), StringLit(i), CallStmt(Id(Tbf), [BooleanLit(True), Id(oF6a), BooleanLit(True)]))), [(NumLit(0.65), CallStmt(Id(VQkW), [BooleanLit(True), StringLit(CdOTA)])), (Id(xLq), AssignStmt(Id(in_), NumLit(39.94)))], Return(NumLit(5.53))), [(NumLit(94.41), AssignStmt(Id(eg), NumLit(51.1))), (NumLit(25.22), Block([If(StringLit(Xy), VarDecl(Id(E7), None, dynamic, None)), [(Id(CNl), Return()), (StringLit(EEoKK), If(Id(OsZ), If(Id(OnvT), For(Id(zMBC), Id(AA), StringLit(NsYh), For(Id(SuE), StringLit(sHk), StringLit(TfUZ), AssignStmt(ArrayCell(Id(Bm), [NumLit(56.18)]), Id(jNu))))), [(StringLit(T), Continue), (NumLit(0.33), Block([Break, Block([AssignStmt(ArrayCell(Id(JTo), [BooleanLit(True), BooleanLit(False)]), NumLit(60.23)), For(Id(YR), StringLit(Irbmz), BooleanLit(False), Block([]))]), VarDecl(Id(t4Q), StringType, None, None)])), (NumLit(91.58), Continue), (Id(esl), CallStmt(Id(lUzl), [Id(Lp)])), (StringLit(hCX), Block([CallStmt(Id(ZjjC), [NumLit(98.7), StringLit(aq), BooleanLit(False)]), CallStmt(Id(TO), [NumLit(54.35), Id(Un), NumLit(49.91)])]))], VarDecl(Id(FDUm), ArrayType([86.87], NumberType), None, BooleanLit(False))), [], None)], None, Return(), Break])), (NumLit(85.49), CallStmt(Id(smWV), [])), (StringLit(pg), Break), (StringLit(GQag), AssignStmt(ArrayCell(Id(zr7), [Id(Zh), NumLit(67.42)]), BooleanLit(False)))], None, Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115297))

	def test_21530115298(self):
		input = '''
bool ju[87.86,72.89,65.48]
'''
		expect = '''Program([VarDecl(Id(ju), ArrayType([87.86, 72.89, 65.48], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115298))

	def test_21530115299(self):
		input = '''
number bdXn <- 18.12
number qJ <- Lgx
number ds <- 9.41
'''
		expect = '''Program([VarDecl(Id(bdXn), NumberType, None, NumLit(18.12)), VarDecl(Id(qJ), NumberType, None, Id(Lgx)), VarDecl(Id(ds), NumberType, None, NumLit(9.41))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115299))

	def test_21530115300(self):
		input = '''
var rn <- "Mo"
dynamic HK <- 45.53
func Qj (bool ft[14.9], number bl)	return "ITmg"

dynamic glSQ
var MAe <- 4.79
'''
		expect = '''Program([VarDecl(Id(rn), None, var, StringLit(Mo)), VarDecl(Id(HK), None, dynamic, NumLit(45.53)), FuncDecl(Id(Qj), [VarDecl(Id(ft), ArrayType([14.9], BoolType), None, None), VarDecl(Id(bl), NumberType, None, None)], Return(StringLit(ITmg))), VarDecl(Id(glSQ), None, dynamic, None), VarDecl(Id(MAe), None, var, NumLit(4.79))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115300))

	def test_21530115301(self):
		input = '''
string DxG <- false
'''
		expect = '''Program([VarDecl(Id(DxG), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115301))

	def test_21530115302(self):
		input = '''
var GYSa <- false
'''
		expect = '''Program([VarDecl(Id(GYSa), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115302))

	def test_21530115303(self):
		input = '''
string d71Z <- OPM
'''
		expect = '''Program([VarDecl(Id(d71Z), StringType, None, Id(OPM))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115303))

	def test_21530115304(self):
		input = '''
bool NaF
func tiEb (number PHc, string PjX[52.49])	return

'''
		expect = '''Program([VarDecl(Id(NaF), BoolType, None, None), FuncDecl(Id(tiEb), [VarDecl(Id(PHc), NumberType, None, None), VarDecl(Id(PjX), ArrayType([52.49], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115304))

	def test_21530115305(self):
		input = '''
func ibmF (bool TU, bool PaD, string xBL)
	return

func b8 (string CUgS, string AP)
	return 28.91

'''
		expect = '''Program([FuncDecl(Id(ibmF), [VarDecl(Id(TU), BoolType, None, None), VarDecl(Id(PaD), BoolType, None, None), VarDecl(Id(xBL), StringType, None, None)], Return()), FuncDecl(Id(b8), [VarDecl(Id(CUgS), StringType, None, None), VarDecl(Id(AP), StringType, None, None)], Return(NumLit(28.91)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115305))

	def test_21530115306(self):
		input = '''
number tokb <- "z"
bool Cq7H
var g_f <- false
bool NTM9[98.19]
number ZX[56.38,55.84]
'''
		expect = '''Program([VarDecl(Id(tokb), NumberType, None, StringLit(z)), VarDecl(Id(Cq7H), BoolType, None, None), VarDecl(Id(g_f), None, var, BooleanLit(False)), VarDecl(Id(NTM9), ArrayType([98.19], BoolType), None, None), VarDecl(Id(ZX), ArrayType([56.38, 55.84], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115306))

	def test_21530115307(self):
		input = '''
func Hq (bool to_, number A_wm[94.41], number rPP)	begin
		string ARN[42.1]
		for G0 until 32.85 by false
			vPd(HE, 58.0)
	end

func yF (string XH[20.11,82.44,58.24], number tf)	return

func oUk7 (number lv[17.03,49.64])
	begin
		return
		mNgS <- 87.03
		for WT until "t" by 24.52
			continue
	end
func v5N (number KAe3, string mg[59.36,71.55,27.82], number rcoQ)
	begin
	end

func Bc_ ()	return true
'''
		expect = '''Program([FuncDecl(Id(Hq), [VarDecl(Id(to_), BoolType, None, None), VarDecl(Id(A_wm), ArrayType([94.41], NumberType), None, None), VarDecl(Id(rPP), NumberType, None, None)], Block([VarDecl(Id(ARN), ArrayType([42.1], StringType), None, None), For(Id(G0), NumLit(32.85), BooleanLit(False), CallStmt(Id(vPd), [Id(HE), NumLit(58.0)]))])), FuncDecl(Id(yF), [VarDecl(Id(XH), ArrayType([20.11, 82.44, 58.24], StringType), None, None), VarDecl(Id(tf), NumberType, None, None)], Return()), FuncDecl(Id(oUk7), [VarDecl(Id(lv), ArrayType([17.03, 49.64], NumberType), None, None)], Block([Return(), AssignStmt(Id(mNgS), NumLit(87.03)), For(Id(WT), StringLit(t), NumLit(24.52), Continue)])), FuncDecl(Id(v5N), [VarDecl(Id(KAe3), NumberType, None, None), VarDecl(Id(mg), ArrayType([59.36, 71.55, 27.82], StringType), None, None), VarDecl(Id(rcoQ), NumberType, None, None)], Block([])), FuncDecl(Id(Bc_), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115307))

	def test_21530115308(self):
		input = '''
func Nr ()	return "k"
string l_Y
func Qz6m (bool gw[3.32])	return "R"
'''
		expect = '''Program([FuncDecl(Id(Nr), [], Return(StringLit(k))), VarDecl(Id(l_Y), StringType, None, None), FuncDecl(Id(Qz6m), [VarDecl(Id(gw), ArrayType([3.32], BoolType), None, None)], Return(StringLit(R)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115308))

	def test_21530115309(self):
		input = '''
number dBbE[90.25,73.69]
'''
		expect = '''Program([VarDecl(Id(dBbE), ArrayType([90.25, 73.69], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115309))

	def test_21530115310(self):
		input = '''
func ETN (number w1, string QCO)
	return AfGD
func oF (bool sDr[86.83], number PEIn[54.06,24.86])
	return tPn
bool ari[49.8,57.01]
func muh (string RT[82.3,59.34,90.81], number uF9R)	return
func cCD (number C8Tt)
	begin
		if (true)
		KfIO()
		elif (98.57)
		continue
		elif (yx) m_()
		elif (false) iz(false, "U", PU)
		elif (28.77) continue
		elif (true) bool ho[29.05,11.95,74.72]
		return "Yi"
		break
	end
'''
		expect = '''Program([FuncDecl(Id(ETN), [VarDecl(Id(w1), NumberType, None, None), VarDecl(Id(QCO), StringType, None, None)], Return(Id(AfGD))), FuncDecl(Id(oF), [VarDecl(Id(sDr), ArrayType([86.83], BoolType), None, None), VarDecl(Id(PEIn), ArrayType([54.06, 24.86], NumberType), None, None)], Return(Id(tPn))), VarDecl(Id(ari), ArrayType([49.8, 57.01], BoolType), None, None), FuncDecl(Id(muh), [VarDecl(Id(RT), ArrayType([82.3, 59.34, 90.81], StringType), None, None), VarDecl(Id(uF9R), NumberType, None, None)], Return()), FuncDecl(Id(cCD), [VarDecl(Id(C8Tt), NumberType, None, None)], Block([If(BooleanLit(True), CallStmt(Id(KfIO), [])), [(NumLit(98.57), Continue), (Id(yx), CallStmt(Id(m_), [])), (BooleanLit(False), CallStmt(Id(iz), [BooleanLit(False), StringLit(U), Id(PU)])), (NumLit(28.77), Continue), (BooleanLit(True), VarDecl(Id(ho), ArrayType([29.05, 11.95, 74.72], BoolType), None, None))], None, Return(StringLit(Yi)), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115310))

	def test_21530115311(self):
		input = '''
string qoeG[29.09]
func MYa (bool OIK5[99.37])
	return
'''
		expect = '''Program([VarDecl(Id(qoeG), ArrayType([29.09], StringType), None, None), FuncDecl(Id(MYa), [VarDecl(Id(OIK5), ArrayType([99.37], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115311))

	def test_21530115312(self):
		input = '''
var VW <- 80.86
func wxyE (bool Su[77.94,5.45], bool cbzt[79.14,42.4], bool P7M[94.94,9.33])
	return 75.08
func ZnOh (number M6[27.55])	return "CABjo"

'''
		expect = '''Program([VarDecl(Id(VW), None, var, NumLit(80.86)), FuncDecl(Id(wxyE), [VarDecl(Id(Su), ArrayType([77.94, 5.45], BoolType), None, None), VarDecl(Id(cbzt), ArrayType([79.14, 42.4], BoolType), None, None), VarDecl(Id(P7M), ArrayType([94.94, 9.33], BoolType), None, None)], Return(NumLit(75.08))), FuncDecl(Id(ZnOh), [VarDecl(Id(M6), ArrayType([27.55], NumberType), None, None)], Return(StringLit(CABjo)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115312))

	def test_21530115313(self):
		input = '''
string eED[71.2,23.19,28.85]
string FIB[13.28,46.8,9.87] <- fw
'''
		expect = '''Program([VarDecl(Id(eED), ArrayType([71.2, 23.19, 28.85], StringType), None, None), VarDecl(Id(FIB), ArrayType([13.28, 46.8, 9.87], StringType), None, Id(fw))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115313))

	def test_21530115314(self):
		input = '''
func yDY (string Ej, number aPr[53.2,39.01], bool sa)	return

func KQGY ()	return 31.67
number VSSe[90.13,14.69] <- 61.63
'''
		expect = '''Program([FuncDecl(Id(yDY), [VarDecl(Id(Ej), StringType, None, None), VarDecl(Id(aPr), ArrayType([53.2, 39.01], NumberType), None, None), VarDecl(Id(sa), BoolType, None, None)], Return()), FuncDecl(Id(KQGY), [], Return(NumLit(31.67))), VarDecl(Id(VSSe), ArrayType([90.13, 14.69], NumberType), None, NumLit(61.63))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115314))

	def test_21530115315(self):
		input = '''
bool LChw[63.96,95.71] <- Zj
func buC (bool uJ, string MNL[32.97,6.04], number TRV_)	return
bool mz[33.66,52.53] <- "RC"
bool It <- 4.28
func NSf (string pN, number ewD[47.04])	return 11.9
'''
		expect = '''Program([VarDecl(Id(LChw), ArrayType([63.96, 95.71], BoolType), None, Id(Zj)), FuncDecl(Id(buC), [VarDecl(Id(uJ), BoolType, None, None), VarDecl(Id(MNL), ArrayType([32.97, 6.04], StringType), None, None), VarDecl(Id(TRV_), NumberType, None, None)], Return()), VarDecl(Id(mz), ArrayType([33.66, 52.53], BoolType), None, StringLit(RC)), VarDecl(Id(It), BoolType, None, NumLit(4.28)), FuncDecl(Id(NSf), [VarDecl(Id(pN), StringType, None, None), VarDecl(Id(ewD), ArrayType([47.04], NumberType), None, None)], Return(NumLit(11.9)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115315))

	def test_21530115316(self):
		input = '''
func ixV (bool vOE[57.14])	return "ZxwLD"

func bY (number YHL)
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(ixV), [VarDecl(Id(vOE), ArrayType([57.14], BoolType), None, None)], Return(StringLit(ZxwLD))), FuncDecl(Id(bY), [VarDecl(Id(YHL), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115316))

	def test_21530115317(self):
		input = '''
string n_qj[69.9] <- "UiV"
bool NJ[53.29,45.19,42.62]
'''
		expect = '''Program([VarDecl(Id(n_qj), ArrayType([69.9], StringType), None, StringLit(UiV)), VarDecl(Id(NJ), ArrayType([53.29, 45.19, 42.62], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115317))

	def test_21530115318(self):
		input = '''
func UpDk (number xyt[29.29])	return
dynamic Xpvb
func Hu (bool cTZD[15.82,81.34,94.8], number wl8, string DQB)	begin
		continue
		lz()
		return FfHp
	end
'''
		expect = '''Program([FuncDecl(Id(UpDk), [VarDecl(Id(xyt), ArrayType([29.29], NumberType), None, None)], Return()), VarDecl(Id(Xpvb), None, dynamic, None), FuncDecl(Id(Hu), [VarDecl(Id(cTZD), ArrayType([15.82, 81.34, 94.8], BoolType), None, None), VarDecl(Id(wl8), NumberType, None, None), VarDecl(Id(DQB), StringType, None, None)], Block([Continue, CallStmt(Id(lz), []), Return(Id(FfHp))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115318))

	def test_21530115319(self):
		input = '''
string Rjbo[18.2,39.25]
'''
		expect = '''Program([VarDecl(Id(Rjbo), ArrayType([18.2, 39.25], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115319))

	def test_21530115320(self):
		input = '''
func PTF ()	begin
		bool iV[53.28,90.04,35.96] <- "vimTI"
		string Qa
		begin
			for U72h until 63.94 by 73.0
				for GcnV until "rWDD" by bNqQ
					if (true) begin
						break
						if (30.4)
						return "xaCyj"
						elif ("pw") continue
						elif (true) begin
							for So3 until 35.41 by "EZ"
								return
							ggRG["uzRFX", 47.87] <- BE
						end
						elif (true)
						break
					end
					elif (dHPf)
					return 68.2
					elif (true)
					for Yt until SDu6 by "IzbmK"
						mJ72(false, 10.4)
					else continue
		end
	end

string C1s5[47.24]
func AwIN ()
	begin
		number TpF5[4.45,69.33,8.02]
		begin
			continue
		end
		continue
	end
number wq2 <- false
func QaU (string Akp1)
	begin
		begin
			begin
			end
			break
		end
		return Gz
		dune[21.32, "JcHku", yx9Z] <- "FXaxf"
	end

'''
		expect = '''Program([FuncDecl(Id(PTF), [], Block([VarDecl(Id(iV), ArrayType([53.28, 90.04, 35.96], BoolType), None, StringLit(vimTI)), VarDecl(Id(Qa), StringType, None, None), Block([For(Id(U72h), NumLit(63.94), NumLit(73.0), For(Id(GcnV), StringLit(rWDD), Id(bNqQ), If(BooleanLit(True), Block([Break, If(NumLit(30.4), Return(StringLit(xaCyj))), [(StringLit(pw), Continue), (BooleanLit(True), Block([For(Id(So3), NumLit(35.41), StringLit(EZ), Return()), AssignStmt(ArrayCell(Id(ggRG), [StringLit(uzRFX), NumLit(47.87)]), Id(BE))])), (BooleanLit(True), Break)], None])), [(Id(dHPf), Return(NumLit(68.2))), (BooleanLit(True), For(Id(Yt), Id(SDu6), StringLit(IzbmK), CallStmt(Id(mJ72), [BooleanLit(False), NumLit(10.4)])))], Continue))])])), VarDecl(Id(C1s5), ArrayType([47.24], StringType), None, None), FuncDecl(Id(AwIN), [], Block([VarDecl(Id(TpF5), ArrayType([4.45, 69.33, 8.02], NumberType), None, None), Block([Continue]), Continue])), VarDecl(Id(wq2), NumberType, None, BooleanLit(False)), FuncDecl(Id(QaU), [VarDecl(Id(Akp1), StringType, None, None)], Block([Block([Block([]), Break]), Return(Id(Gz)), AssignStmt(ArrayCell(Id(dune), [NumLit(21.32), StringLit(JcHku), Id(yx9Z)]), StringLit(FXaxf))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115320))

	def test_21530115321(self):
		input = '''
number fg[48.71,93.56,2.54] <- true
bool Imla <- 44.9
func O12 (bool mK8Y[16.19,8.18,57.09], number Qs[84.84,76.98,17.77], string yXxj[29.03,52.23])
	return

func rQ (bool U_A, string whc[97.7,81.02])
	begin
	end

'''
		expect = '''Program([VarDecl(Id(fg), ArrayType([48.71, 93.56, 2.54], NumberType), None, BooleanLit(True)), VarDecl(Id(Imla), BoolType, None, NumLit(44.9)), FuncDecl(Id(O12), [VarDecl(Id(mK8Y), ArrayType([16.19, 8.18, 57.09], BoolType), None, None), VarDecl(Id(Qs), ArrayType([84.84, 76.98, 17.77], NumberType), None, None), VarDecl(Id(yXxj), ArrayType([29.03, 52.23], StringType), None, None)], Return()), FuncDecl(Id(rQ), [VarDecl(Id(U_A), BoolType, None, None), VarDecl(Id(whc), ArrayType([97.7, 81.02], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115321))

	def test_21530115322(self):
		input = '''
string t4Fd[70.33,61.97,87.53]
func rz ()
	begin
		KV["c", 15.71] <- vYJ
		return
	end
func dD (number Jrs)	return

bool Iy[94.88,53.46]
string h_[3.99]
'''
		expect = '''Program([VarDecl(Id(t4Fd), ArrayType([70.33, 61.97, 87.53], StringType), None, None), FuncDecl(Id(rz), [], Block([AssignStmt(ArrayCell(Id(KV), [StringLit(c), NumLit(15.71)]), Id(vYJ)), Return()])), FuncDecl(Id(dD), [VarDecl(Id(Jrs), NumberType, None, None)], Return()), VarDecl(Id(Iy), ArrayType([94.88, 53.46], BoolType), None, None), VarDecl(Id(h_), ArrayType([3.99], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115322))

	def test_21530115323(self):
		input = '''
func h7 (number Iq, bool YjNd[63.18,58.23,25.09], number of2k)	begin
		continue
		Bzq[44.39, true, 98.21] <- false
	end

func bw ()	return false

'''
		expect = '''Program([FuncDecl(Id(h7), [VarDecl(Id(Iq), NumberType, None, None), VarDecl(Id(YjNd), ArrayType([63.18, 58.23, 25.09], BoolType), None, None), VarDecl(Id(of2k), NumberType, None, None)], Block([Continue, AssignStmt(ArrayCell(Id(Bzq), [NumLit(44.39), BooleanLit(True), NumLit(98.21)]), BooleanLit(False))])), FuncDecl(Id(bw), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115323))

	def test_21530115324(self):
		input = '''
bool T7[23.23,72.03] <- "lxSQI"
func G78 (string i4, number rkn[70.36,74.04,48.43])	return z9PK
'''
		expect = '''Program([VarDecl(Id(T7), ArrayType([23.23, 72.03], BoolType), None, StringLit(lxSQI)), FuncDecl(Id(G78), [VarDecl(Id(i4), StringType, None, None), VarDecl(Id(rkn), ArrayType([70.36, 74.04, 48.43], NumberType), None, None)], Return(Id(z9PK)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115324))

	def test_21530115325(self):
		input = '''
func kG ()
	begin
		continue
		break
	end

func ZtN (string n2v)	begin
		bool L19[16.47] <- 10.23
		rH6()
		zjY <- 39.66
	end
'''
		expect = '''Program([FuncDecl(Id(kG), [], Block([Continue, Break])), FuncDecl(Id(ZtN), [VarDecl(Id(n2v), StringType, None, None)], Block([VarDecl(Id(L19), ArrayType([16.47], BoolType), None, NumLit(10.23)), CallStmt(Id(rH6), []), AssignStmt(Id(zjY), NumLit(39.66))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115325))

	def test_21530115326(self):
		input = '''
func dM (number OF[3.2,87.45,99.42], string Cfg, string Lrv)
	return YxL

string rp[58.91,55.51]
'''
		expect = '''Program([FuncDecl(Id(dM), [VarDecl(Id(OF), ArrayType([3.2, 87.45, 99.42], NumberType), None, None), VarDecl(Id(Cfg), StringType, None, None), VarDecl(Id(Lrv), StringType, None, None)], Return(Id(YxL))), VarDecl(Id(rp), ArrayType([58.91, 55.51], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115326))

	def test_21530115327(self):
		input = '''
number eHL[21.08,83.87]
func da ()	return 24.58

func Bu (number hdY, bool K4MK[70.68], bool oX2[39.34])
	begin
	end

func IpoZ (string yt[28.0,50.28,37.97], number Cl0O)
	begin
		break
		for NcsA until false by x9_p
			break
	end

'''
		expect = '''Program([VarDecl(Id(eHL), ArrayType([21.08, 83.87], NumberType), None, None), FuncDecl(Id(da), [], Return(NumLit(24.58))), FuncDecl(Id(Bu), [VarDecl(Id(hdY), NumberType, None, None), VarDecl(Id(K4MK), ArrayType([70.68], BoolType), None, None), VarDecl(Id(oX2), ArrayType([39.34], BoolType), None, None)], Block([])), FuncDecl(Id(IpoZ), [VarDecl(Id(yt), ArrayType([28.0, 50.28, 37.97], StringType), None, None), VarDecl(Id(Cl0O), NumberType, None, None)], Block([Break, For(Id(NcsA), BooleanLit(False), Id(x9_p), Break)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115327))

	def test_21530115328(self):
		input = '''
number qw[22.45,37.38] <- 48.92
func OD (number sj[58.99,28.53], string CVWk, string Bb9h)
	return

func EVk (string De[34.81,22.31])
	return 99.95
string nP <- 37.25
'''
		expect = '''Program([VarDecl(Id(qw), ArrayType([22.45, 37.38], NumberType), None, NumLit(48.92)), FuncDecl(Id(OD), [VarDecl(Id(sj), ArrayType([58.99, 28.53], NumberType), None, None), VarDecl(Id(CVWk), StringType, None, None), VarDecl(Id(Bb9h), StringType, None, None)], Return()), FuncDecl(Id(EVk), [VarDecl(Id(De), ArrayType([34.81, 22.31], StringType), None, None)], Return(NumLit(99.95))), VarDecl(Id(nP), StringType, None, NumLit(37.25))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115328))

	def test_21530115329(self):
		input = '''
func Sxw (bool EOwb, number sC, number EX8l[52.19,24.73])
	return 6.12
number HUB[85.96,70.59]
'''
		expect = '''Program([FuncDecl(Id(Sxw), [VarDecl(Id(EOwb), BoolType, None, None), VarDecl(Id(sC), NumberType, None, None), VarDecl(Id(EX8l), ArrayType([52.19, 24.73], NumberType), None, None)], Return(NumLit(6.12))), VarDecl(Id(HUB), ArrayType([85.96, 70.59], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115329))

	def test_21530115330(self):
		input = '''
string x2[30.09,59.78]
func eB0 (bool G8[80.4,13.25,60.05], string ziQw, bool uQW)
	return
bool i5Gr[50.69,1.52] <- h7Gm
bool tuz[20.07] <- XVn
'''
		expect = '''Program([VarDecl(Id(x2), ArrayType([30.09, 59.78], StringType), None, None), FuncDecl(Id(eB0), [VarDecl(Id(G8), ArrayType([80.4, 13.25, 60.05], BoolType), None, None), VarDecl(Id(ziQw), StringType, None, None), VarDecl(Id(uQW), BoolType, None, None)], Return()), VarDecl(Id(i5Gr), ArrayType([50.69, 1.52], BoolType), None, Id(h7Gm)), VarDecl(Id(tuz), ArrayType([20.07], BoolType), None, Id(XVn))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115330))

	def test_21530115331(self):
		input = '''
var VD <- AE5
bool Wg[91.73,0.02] <- BCLD
var PY <- "Q"
bool Lx[48.49,36.56]
'''
		expect = '''Program([VarDecl(Id(VD), None, var, Id(AE5)), VarDecl(Id(Wg), ArrayType([91.73, 0.02], BoolType), None, Id(BCLD)), VarDecl(Id(PY), None, var, StringLit(Q)), VarDecl(Id(Lx), ArrayType([48.49, 36.56], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115331))

	def test_21530115332(self):
		input = '''
bool GV
number yh3B[39.69] <- w0XP
func bq_T (string Y5[39.56])	return Qt
'''
		expect = '''Program([VarDecl(Id(GV), BoolType, None, None), VarDecl(Id(yh3B), ArrayType([39.69], NumberType), None, Id(w0XP)), FuncDecl(Id(bq_T), [VarDecl(Id(Y5), ArrayType([39.56], StringType), None, None)], Return(Id(Qt)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115332))

	def test_21530115333(self):
		input = '''
var w153 <- 29.75
string A7U <- "zYG"
'''
		expect = '''Program([VarDecl(Id(w153), None, var, NumLit(29.75)), VarDecl(Id(A7U), StringType, None, StringLit(zYG))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115333))

	def test_21530115334(self):
		input = '''
dynamic gjuU <- "w"
func Sk (string IYH6, string VVA)	return

func toU (number yS1C[78.08])
	begin
		Qac[zuRG, "E"] <- true
		continue
	end
string QiJT
func YRUd (number AWM[87.04,61.66,49.54], string cCA9[77.83])
	return

'''
		expect = '''Program([VarDecl(Id(gjuU), None, dynamic, StringLit(w)), FuncDecl(Id(Sk), [VarDecl(Id(IYH6), StringType, None, None), VarDecl(Id(VVA), StringType, None, None)], Return()), FuncDecl(Id(toU), [VarDecl(Id(yS1C), ArrayType([78.08], NumberType), None, None)], Block([AssignStmt(ArrayCell(Id(Qac), [Id(zuRG), StringLit(E)]), BooleanLit(True)), Continue])), VarDecl(Id(QiJT), StringType, None, None), FuncDecl(Id(YRUd), [VarDecl(Id(AWM), ArrayType([87.04, 61.66, 49.54], NumberType), None, None), VarDecl(Id(cCA9), ArrayType([77.83], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115334))

	def test_21530115335(self):
		input = '''
dynamic nujl <- 61.2
number B0B
'''
		expect = '''Program([VarDecl(Id(nujl), None, dynamic, NumLit(61.2)), VarDecl(Id(B0B), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115335))

	def test_21530115336(self):
		input = '''
func Tw (bool ms[53.95,46.98])	begin
		lOO <- oKA
		if ("xbVLg")
		if (up) Mr[true, "Qv", "gb"] <- false
		elif (false)
		continue
		elif (re)
		return
		elif ("QvM")
		for wu until 30.16 by P1G
			if ("Be")
			continue
			elif (Tc8t)
			TVq[PN] <- true
			elif ("f")
			kH(GNv, 70.62)
		elif (X3fc)
		begin
			var Sll <- dRxd
			return "JrQah"
		end
		elif (26.8)
		for WOpw until 59.75 by "Ff"
			Em(true)
		elif ("nfoQk") for Muai until 86.29 by "H"
			HxxQ <- Kd
		elif (true)
		for q_Ky until 20.71 by 68.79
			H9fV <- 71.65
		elif (eh)
		begin
			begin
				continue
			end
			if ("aa") for LZ until "T" by 33.0
				JHY(9.25, 32.97, true)
			elif (a0oU)
			bool rDcN
			else return
		end
		elif (21.3) string QjkC[66.88]
		else if ("REWs") begin
			continue
			obd("Knfj", EKTO)
			if (false) begin
				continue
				Uid()
			end
			elif ("xj")
			S3M2 <- EoiA
			elif (true) break
			elif ("YxFs")
			for r0a until UR by 71.43
				return "OWxA"
			elif ("TIyz") break
			elif (false) for Z7i until "B" by 87.77
				continue
			else if (false) number csu[27.5,73.75]
			elif (biXy)
			HkW["TNkWi", false, oBA] <- true
		end
		elif ("N") break
		elif (false)
		bool vk2 <- false
		elif (vo) begin
			JF <- 9.87
		end
		elif ("av")
		begin
			begin
				break
				return 44.35
				begin
					al("hAnD", true, true)
					return 84.64
					ve51 <- "pNci"
				end
			end
		end
		else F8yw(false, false, "i")
		mJ <- "O"
	end
dynamic N9u
bool Fg5W[43.79]
'''
		expect = '''Program([FuncDecl(Id(Tw), [VarDecl(Id(ms), ArrayType([53.95, 46.98], BoolType), None, None)], Block([AssignStmt(Id(lOO), Id(oKA)), If(StringLit(xbVLg), If(Id(up), AssignStmt(ArrayCell(Id(Mr), [BooleanLit(True), StringLit(Qv), StringLit(gb)]), BooleanLit(False))), [(BooleanLit(False), Continue), (Id(re), Return()), (StringLit(QvM), For(Id(wu), NumLit(30.16), Id(P1G), If(StringLit(Be), Continue), [(Id(Tc8t), AssignStmt(ArrayCell(Id(TVq), [Id(PN)]), BooleanLit(True))), (StringLit(f), CallStmt(Id(kH), [Id(GNv), NumLit(70.62)])), (Id(X3fc), Block([VarDecl(Id(Sll), None, var, Id(dRxd)), Return(StringLit(JrQah))])), (NumLit(26.8), For(Id(WOpw), NumLit(59.75), StringLit(Ff), CallStmt(Id(Em), [BooleanLit(True)]))), (StringLit(nfoQk), For(Id(Muai), NumLit(86.29), StringLit(H), AssignStmt(Id(HxxQ), Id(Kd)))), (BooleanLit(True), For(Id(q_Ky), NumLit(20.71), NumLit(68.79), AssignStmt(Id(H9fV), NumLit(71.65)))), (Id(eh), Block([Block([Continue]), If(StringLit(aa), For(Id(LZ), StringLit(T), NumLit(33.0), CallStmt(Id(JHY), [NumLit(9.25), NumLit(32.97), BooleanLit(True)]))), [(Id(a0oU), VarDecl(Id(rDcN), BoolType, None, None))], Return()])), (NumLit(21.3), VarDecl(Id(QjkC), ArrayType([66.88], StringType), None, None))], If(StringLit(REWs), Block([Continue, CallStmt(Id(obd), [StringLit(Knfj), Id(EKTO)]), If(BooleanLit(False), Block([Continue, CallStmt(Id(Uid), [])])), [(StringLit(xj), AssignStmt(Id(S3M2), Id(EoiA))), (BooleanLit(True), Break), (StringLit(YxFs), For(Id(r0a), Id(UR), NumLit(71.43), Return(StringLit(OWxA)))), (StringLit(TIyz), Break), (BooleanLit(False), For(Id(Z7i), StringLit(B), NumLit(87.77), Continue))], If(BooleanLit(False), VarDecl(Id(csu), ArrayType([27.5, 73.75], NumberType), None, None)), [(Id(biXy), AssignStmt(ArrayCell(Id(HkW), [StringLit(TNkWi), BooleanLit(False), Id(oBA)]), BooleanLit(True)))], None])), [(StringLit(N), Break), (BooleanLit(False), VarDecl(Id(vk2), BoolType, None, BooleanLit(False))), (Id(vo), Block([AssignStmt(Id(JF), NumLit(9.87))])), (StringLit(av), Block([Block([Break, Return(NumLit(44.35)), Block([CallStmt(Id(al), [StringLit(hAnD), BooleanLit(True), BooleanLit(True)]), Return(NumLit(84.64)), AssignStmt(Id(ve51), StringLit(pNci))])])]))], CallStmt(Id(F8yw), [BooleanLit(False), BooleanLit(False), StringLit(i)])))], None), [], None, AssignStmt(Id(mJ), StringLit(O))])), VarDecl(Id(N9u), None, dynamic, None), VarDecl(Id(Fg5W), ArrayType([43.79], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115336))

	def test_21530115337(self):
		input = '''
func Tlx ()	return
func hmw ()
	return 56.99
number cp21[79.26,17.47] <- 34.69
number qK[8.76,65.91,71.59]
func xmzv (number i42q, string e1r, number rI3[77.75,11.83])
	return

'''
		expect = '''Program([FuncDecl(Id(Tlx), [], Return()), FuncDecl(Id(hmw), [], Return(NumLit(56.99))), VarDecl(Id(cp21), ArrayType([79.26, 17.47], NumberType), None, NumLit(34.69)), VarDecl(Id(qK), ArrayType([8.76, 65.91, 71.59], NumberType), None, None), FuncDecl(Id(xmzv), [VarDecl(Id(i42q), NumberType, None, None), VarDecl(Id(e1r), StringType, None, None), VarDecl(Id(rI3), ArrayType([77.75, 11.83], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115337))

	def test_21530115338(self):
		input = '''
func fum (string eNU)
	return

string a7[71.76]
func SJD (number dECY)	return

number k4H8[65.52]
number U5F <- false
'''
		expect = '''Program([FuncDecl(Id(fum), [VarDecl(Id(eNU), StringType, None, None)], Return()), VarDecl(Id(a7), ArrayType([71.76], StringType), None, None), FuncDecl(Id(SJD), [VarDecl(Id(dECY), NumberType, None, None)], Return()), VarDecl(Id(k4H8), ArrayType([65.52], NumberType), None, None), VarDecl(Id(U5F), NumberType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115338))

	def test_21530115339(self):
		input = '''
string MY[26.6,58.49] <- false
func LK (number f8eA[20.85], bool aQTc[53.74,55.8])	return "tWfq"

func zJ (bool IL)
	return
func ondv ()	return true

func c7 (number Umm, string Uccj[49.65,33.48,58.33])	return
'''
		expect = '''Program([VarDecl(Id(MY), ArrayType([26.6, 58.49], StringType), None, BooleanLit(False)), FuncDecl(Id(LK), [VarDecl(Id(f8eA), ArrayType([20.85], NumberType), None, None), VarDecl(Id(aQTc), ArrayType([53.74, 55.8], BoolType), None, None)], Return(StringLit(tWfq))), FuncDecl(Id(zJ), [VarDecl(Id(IL), BoolType, None, None)], Return()), FuncDecl(Id(ondv), [], Return(BooleanLit(True))), FuncDecl(Id(c7), [VarDecl(Id(Umm), NumberType, None, None), VarDecl(Id(Uccj), ArrayType([49.65, 33.48, 58.33], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115339))

	def test_21530115340(self):
		input = '''
bool W2x
number DL1 <- true
'''
		expect = '''Program([VarDecl(Id(W2x), BoolType, None, None), VarDecl(Id(DL1), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115340))

	def test_21530115341(self):
		input = '''
string RFG[98.68,93.19] <- true
dynamic Zt <- "GYZ"
'''
		expect = '''Program([VarDecl(Id(RFG), ArrayType([98.68, 93.19], StringType), None, BooleanLit(True)), VarDecl(Id(Zt), None, dynamic, StringLit(GYZ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115341))

	def test_21530115342(self):
		input = '''
func eBgZ (string Z01)
	return 53.35
func Qr (string jgZ[61.69,63.11,75.6], string vjZ[87.15,6.34,71.05], bool g3Qg)
	return 27.57

func iv (number YHrC[33.53], number KE[90.28,7.69,30.33])
	return 23.79

func M3 (string Qia[33.55,0.37])
	return 54.62
'''
		expect = '''Program([FuncDecl(Id(eBgZ), [VarDecl(Id(Z01), StringType, None, None)], Return(NumLit(53.35))), FuncDecl(Id(Qr), [VarDecl(Id(jgZ), ArrayType([61.69, 63.11, 75.6], StringType), None, None), VarDecl(Id(vjZ), ArrayType([87.15, 6.34, 71.05], StringType), None, None), VarDecl(Id(g3Qg), BoolType, None, None)], Return(NumLit(27.57))), FuncDecl(Id(iv), [VarDecl(Id(YHrC), ArrayType([33.53], NumberType), None, None), VarDecl(Id(KE), ArrayType([90.28, 7.69, 30.33], NumberType), None, None)], Return(NumLit(23.79))), FuncDecl(Id(M3), [VarDecl(Id(Qia), ArrayType([33.55, 0.37], StringType), None, None)], Return(NumLit(54.62)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115342))

	def test_21530115343(self):
		input = '''
func l5 (string iXwz, number c4[66.71,67.07])	return
bool Cz
dynamic Wksu <- 85.62
func jaR ()
	return

'''
		expect = '''Program([FuncDecl(Id(l5), [VarDecl(Id(iXwz), StringType, None, None), VarDecl(Id(c4), ArrayType([66.71, 67.07], NumberType), None, None)], Return()), VarDecl(Id(Cz), BoolType, None, None), VarDecl(Id(Wksu), None, dynamic, NumLit(85.62)), FuncDecl(Id(jaR), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115343))

	def test_21530115344(self):
		input = '''
dynamic NAl0
func O6j (number sFXY[58.05,81.86])
	return

func dr (string YtD[84.76,11.77,1.15], number k5a5, string G_t[80.42,68.95])
	return

func s7uU (number bgs[69.12], bool oXa)
	return
'''
		expect = '''Program([VarDecl(Id(NAl0), None, dynamic, None), FuncDecl(Id(O6j), [VarDecl(Id(sFXY), ArrayType([58.05, 81.86], NumberType), None, None)], Return()), FuncDecl(Id(dr), [VarDecl(Id(YtD), ArrayType([84.76, 11.77, 1.15], StringType), None, None), VarDecl(Id(k5a5), NumberType, None, None), VarDecl(Id(G_t), ArrayType([80.42, 68.95], StringType), None, None)], Return()), FuncDecl(Id(s7uU), [VarDecl(Id(bgs), ArrayType([69.12], NumberType), None, None), VarDecl(Id(oXa), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115344))

	def test_21530115345(self):
		input = '''
bool B1[76.42] <- Nl
bool B_PW[41.61]
bool vwr[40.57,84.21]
'''
		expect = '''Program([VarDecl(Id(B1), ArrayType([76.42], BoolType), None, Id(Nl)), VarDecl(Id(B_PW), ArrayType([41.61], BoolType), None, None), VarDecl(Id(vwr), ArrayType([40.57, 84.21], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115345))

	def test_21530115346(self):
		input = '''
func YiGS ()	begin
		Kyf <- false
		return
		return TQ
	end

'''
		expect = '''Program([FuncDecl(Id(YiGS), [], Block([AssignStmt(Id(Kyf), BooleanLit(False)), Return(), Return(Id(TQ))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115346))

	def test_21530115347(self):
		input = '''
func I778 (number Ycjl, number fCn[45.44,36.69,82.83])	return "mp"

number wV[27.36] <- 6.81
func pOx (bool mdOy[88.56], number HvTN[42.03])
	return 79.14

string QS[8.07,5.16]
func XH ()	begin
		for L82 until 67.73 by 65.19
			continue
		if (19.89) GpB <- anGf
		elif (false)
		if (79.98) if (BT)
		nZv["WIp", 36.02, 8.55] <- "NyCA"
		elif ("uugPL") dynamic b74
		elif (false) if ("NxDGV") break
		elif (99.54)
		begin
			continue
		end
		elif (false)
		var n7TU <- true
		else break
		elif (17.59)
		return true
		else for RqGn until 96.02 by false
			break
		elif ("reB") begin
			if (95.09) number RY1[75.48,21.45,97.34]
			elif ("NxkSO")
			continue
			elif (qmC) break
			else begin
				begin
				end
				continue
			end
			continue
		end
		elif (Ro5) return 94.77
		elif (false) Hl5(KS)
		elif ("sh") return false
		begin
		end
	end

'''
		expect = '''Program([FuncDecl(Id(I778), [VarDecl(Id(Ycjl), NumberType, None, None), VarDecl(Id(fCn), ArrayType([45.44, 36.69, 82.83], NumberType), None, None)], Return(StringLit(mp))), VarDecl(Id(wV), ArrayType([27.36], NumberType), None, NumLit(6.81)), FuncDecl(Id(pOx), [VarDecl(Id(mdOy), ArrayType([88.56], BoolType), None, None), VarDecl(Id(HvTN), ArrayType([42.03], NumberType), None, None)], Return(NumLit(79.14))), VarDecl(Id(QS), ArrayType([8.07, 5.16], StringType), None, None), FuncDecl(Id(XH), [], Block([For(Id(L82), NumLit(67.73), NumLit(65.19), Continue), If(NumLit(19.89), AssignStmt(Id(GpB), Id(anGf))), [(BooleanLit(False), If(NumLit(79.98), If(Id(BT), AssignStmt(ArrayCell(Id(nZv), [StringLit(WIp), NumLit(36.02), NumLit(8.55)]), StringLit(NyCA))), [(StringLit(uugPL), VarDecl(Id(b74), None, dynamic, None)), (BooleanLit(False), If(StringLit(NxDGV), Break), [(NumLit(99.54), Block([Continue])), (BooleanLit(False), VarDecl(Id(n7TU), None, var, BooleanLit(True)))], Break), (NumLit(17.59), Return(BooleanLit(True)))], For(Id(RqGn), NumLit(96.02), BooleanLit(False), Break)), [(StringLit(reB), Block([If(NumLit(95.09), VarDecl(Id(RY1), ArrayType([75.48, 21.45, 97.34], NumberType), None, None)), [(StringLit(NxkSO), Continue), (Id(qmC), Break)], Block([Block([]), Continue]), Continue])), (Id(Ro5), Return(NumLit(94.77))), (BooleanLit(False), CallStmt(Id(Hl5), [Id(KS)])), (StringLit(sh), Return(BooleanLit(False)))], None)], None, Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115347))

	def test_21530115348(self):
		input = '''
func aPo (string JIhx, string Xki_)	return

string V4[33.51,94.97,86.97]
func nTx ()
	return
number mdiq
'''
		expect = '''Program([FuncDecl(Id(aPo), [VarDecl(Id(JIhx), StringType, None, None), VarDecl(Id(Xki_), StringType, None, None)], Return()), VarDecl(Id(V4), ArrayType([33.51, 94.97, 86.97], StringType), None, None), FuncDecl(Id(nTx), [], Return()), VarDecl(Id(mdiq), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115348))

	def test_21530115349(self):
		input = '''
func N5 (number Q92, string gl[5.28,47.94], bool NiW[9.32,39.68])
	return "PJMC"
func KbP (bool cyp[10.57,42.89], number Kjik[65.63,15.82,0.79], bool vFY)	return true
'''
		expect = '''Program([FuncDecl(Id(N5), [VarDecl(Id(Q92), NumberType, None, None), VarDecl(Id(gl), ArrayType([5.28, 47.94], StringType), None, None), VarDecl(Id(NiW), ArrayType([9.32, 39.68], BoolType), None, None)], Return(StringLit(PJMC))), FuncDecl(Id(KbP), [VarDecl(Id(cyp), ArrayType([10.57, 42.89], BoolType), None, None), VarDecl(Id(Kjik), ArrayType([65.63, 15.82, 0.79], NumberType), None, None), VarDecl(Id(vFY), BoolType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115349))

	def test_21530115350(self):
		input = '''
number pvU[60.22,33.96,69.01]
func OpN ()
	return

func vLu0 (string Dvii, string KRrR)
	begin
		break
		Ril6 <- Fv2
		dynamic PlrR
	end
'''
		expect = '''Program([VarDecl(Id(pvU), ArrayType([60.22, 33.96, 69.01], NumberType), None, None), FuncDecl(Id(OpN), [], Return()), FuncDecl(Id(vLu0), [VarDecl(Id(Dvii), StringType, None, None), VarDecl(Id(KRrR), StringType, None, None)], Block([Break, AssignStmt(Id(Ril6), Id(Fv2)), VarDecl(Id(PlrR), None, dynamic, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115350))

	def test_21530115351(self):
		input = '''
string efjB[13.53,42.74,83.31]
string BzY <- false
bool MRo[25.12,88.52,9.59] <- false
bool Ib[27.66] <- false
func Ed (number yaK[81.82,9.4,82.32], number jBW, string dUU)
	return true
'''
		expect = '''Program([VarDecl(Id(efjB), ArrayType([13.53, 42.74, 83.31], StringType), None, None), VarDecl(Id(BzY), StringType, None, BooleanLit(False)), VarDecl(Id(MRo), ArrayType([25.12, 88.52, 9.59], BoolType), None, BooleanLit(False)), VarDecl(Id(Ib), ArrayType([27.66], BoolType), None, BooleanLit(False)), FuncDecl(Id(Ed), [VarDecl(Id(yaK), ArrayType([81.82, 9.4, 82.32], NumberType), None, None), VarDecl(Id(jBW), NumberType, None, None), VarDecl(Id(dUU), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115351))

	def test_21530115352(self):
		input = '''
func FJK (number lM, string LXGn[43.5,73.87,93.85], string FQ[86.8])
	return

'''
		expect = '''Program([FuncDecl(Id(FJK), [VarDecl(Id(lM), NumberType, None, None), VarDecl(Id(LXGn), ArrayType([43.5, 73.87, 93.85], StringType), None, None), VarDecl(Id(FQ), ArrayType([86.8], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115352))

	def test_21530115353(self):
		input = '''
func Zx (number qj)	return

'''
		expect = '''Program([FuncDecl(Id(Zx), [VarDecl(Id(qj), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115353))

	def test_21530115354(self):
		input = '''
dynamic s3V <- "wdMDV"
'''
		expect = '''Program([VarDecl(Id(s3V), None, dynamic, StringLit(wdMDV))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115354))

	def test_21530115355(self):
		input = '''
func S3 (string eCaS[64.14,95.03], bool Mm1x)
	return Qqw2
'''
		expect = '''Program([FuncDecl(Id(S3), [VarDecl(Id(eCaS), ArrayType([64.14, 95.03], StringType), None, None), VarDecl(Id(Mm1x), BoolType, None, None)], Return(Id(Qqw2)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115355))

	def test_21530115356(self):
		input = '''
var JhB <- "QkqD"
'''
		expect = '''Program([VarDecl(Id(JhB), None, var, StringLit(QkqD))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115356))

	def test_21530115357(self):
		input = '''
func T3SA (string PKnv, string aKNY[57.23,83.47,64.36], string xwWA)	begin
	end
func WYpS (bool msCs[68.76,7.11,70.7])	begin
		if (false) return 1.02
		elif (true)
		break
		elif ("MZ") break
	end
bool U5[47.46,21.83,25.58]
bool lU[90.14,13.63]
string IaPV <- "G"
'''
		expect = '''Program([FuncDecl(Id(T3SA), [VarDecl(Id(PKnv), StringType, None, None), VarDecl(Id(aKNY), ArrayType([57.23, 83.47, 64.36], StringType), None, None), VarDecl(Id(xwWA), StringType, None, None)], Block([])), FuncDecl(Id(WYpS), [VarDecl(Id(msCs), ArrayType([68.76, 7.11, 70.7], BoolType), None, None)], Block([If(BooleanLit(False), Return(NumLit(1.02))), [(BooleanLit(True), Break), (StringLit(MZ), Break)], None])), VarDecl(Id(U5), ArrayType([47.46, 21.83, 25.58], BoolType), None, None), VarDecl(Id(lU), ArrayType([90.14, 13.63], BoolType), None, None), VarDecl(Id(IaPV), StringType, None, StringLit(G))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115357))

	def test_21530115358(self):
		input = '''
func F7 (number B2[77.04,93.19])	return
'''
		expect = '''Program([FuncDecl(Id(F7), [VarDecl(Id(B2), ArrayType([77.04, 93.19], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115358))

	def test_21530115359(self):
		input = '''
func A3y1 ()
	return "P"

number ndn[58.71,12.91,13.1]
dynamic mHwl <- false
bool hK
'''
		expect = '''Program([FuncDecl(Id(A3y1), [], Return(StringLit(P))), VarDecl(Id(ndn), ArrayType([58.71, 12.91, 13.1], NumberType), None, None), VarDecl(Id(mHwl), None, dynamic, BooleanLit(False)), VarDecl(Id(hK), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115359))

	def test_21530115360(self):
		input = '''
func Aj ()
	return

number B5q_ <- M6
func gx ()
	return
'''
		expect = '''Program([FuncDecl(Id(Aj), [], Return()), VarDecl(Id(B5q_), NumberType, None, Id(M6)), FuncDecl(Id(gx), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115360))

	def test_21530115361(self):
		input = '''
func eGR ()
	return "di"
bool k8[66.06]
func hYt (bool Ha[10.1])	return
bool FMZ_ <- 75.6
func Djy (number mB7[56.5], string ZwT[23.36])	begin
		begin
			return
		end
		return
	end

'''
		expect = '''Program([FuncDecl(Id(eGR), [], Return(StringLit(di))), VarDecl(Id(k8), ArrayType([66.06], BoolType), None, None), FuncDecl(Id(hYt), [VarDecl(Id(Ha), ArrayType([10.1], BoolType), None, None)], Return()), VarDecl(Id(FMZ_), BoolType, None, NumLit(75.6)), FuncDecl(Id(Djy), [VarDecl(Id(mB7), ArrayType([56.5], NumberType), None, None), VarDecl(Id(ZwT), ArrayType([23.36], StringType), None, None)], Block([Block([Return()]), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115361))

	def test_21530115362(self):
		input = '''
bool hka1[51.61] <- false
string HUO[10.59,29.47] <- true
var YTTP <- "yUiYe"
'''
		expect = '''Program([VarDecl(Id(hka1), ArrayType([51.61], BoolType), None, BooleanLit(False)), VarDecl(Id(HUO), ArrayType([10.59, 29.47], StringType), None, BooleanLit(True)), VarDecl(Id(YTTP), None, var, StringLit(yUiYe))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115362))

	def test_21530115363(self):
		input = '''
func QC (number lud[77.24,54.84,29.1], bool gSk[76.47], number iR[21.02])	begin
		if ("bb")
		begin
			mP[ts, "Q", "efNJZ"] <- 22.85
		end
		elif (73.54)
		continue
		elif (9.52)
		Nk[52.96, 50.74, XJQS] <- vBh
		else begin
		end
		continue
	end
string B0[27.16]
bool V5[28.62,5.0,21.12] <- CY
'''
		expect = '''Program([FuncDecl(Id(QC), [VarDecl(Id(lud), ArrayType([77.24, 54.84, 29.1], NumberType), None, None), VarDecl(Id(gSk), ArrayType([76.47], BoolType), None, None), VarDecl(Id(iR), ArrayType([21.02], NumberType), None, None)], Block([If(StringLit(bb), Block([AssignStmt(ArrayCell(Id(mP), [Id(ts), StringLit(Q), StringLit(efNJZ)]), NumLit(22.85))])), [(NumLit(73.54), Continue), (NumLit(9.52), AssignStmt(ArrayCell(Id(Nk), [NumLit(52.96), NumLit(50.74), Id(XJQS)]), Id(vBh)))], Block([]), Continue])), VarDecl(Id(B0), ArrayType([27.16], StringType), None, None), VarDecl(Id(V5), ArrayType([28.62, 5.0, 21.12], BoolType), None, Id(CY))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115363))

	def test_21530115364(self):
		input = '''
func TkB (bool uu, string fl)	return

'''
		expect = '''Program([FuncDecl(Id(TkB), [VarDecl(Id(uu), BoolType, None, None), VarDecl(Id(fl), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115364))

	def test_21530115365(self):
		input = '''
var Q7 <- "CaSC"
func XqV ()	return Lc
func qz (string jKge, bool bb)	return

number iIb <- 80.39
'''
		expect = '''Program([VarDecl(Id(Q7), None, var, StringLit(CaSC)), FuncDecl(Id(XqV), [], Return(Id(Lc))), FuncDecl(Id(qz), [VarDecl(Id(jKge), StringType, None, None), VarDecl(Id(bb), BoolType, None, None)], Return()), VarDecl(Id(iIb), NumberType, None, NumLit(80.39))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115365))

	def test_21530115366(self):
		input = '''
func nWLC (number RBx, string is)	return

bool lX[58.58] <- 85.88
string GAB[72.31,49.61,53.08] <- "x"
bool qh73 <- false
func zhr (string Mo[75.74])	return "awck"
'''
		expect = '''Program([FuncDecl(Id(nWLC), [VarDecl(Id(RBx), NumberType, None, None), VarDecl(Id(is), StringType, None, None)], Return()), VarDecl(Id(lX), ArrayType([58.58], BoolType), None, NumLit(85.88)), VarDecl(Id(GAB), ArrayType([72.31, 49.61, 53.08], StringType), None, StringLit(x)), VarDecl(Id(qh73), BoolType, None, BooleanLit(False)), FuncDecl(Id(zhr), [VarDecl(Id(Mo), ArrayType([75.74], StringType), None, None)], Return(StringLit(awck)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115366))

	def test_21530115367(self):
		input = '''
func So1O (bool W1L[19.61], string y_[35.21,89.18,12.36], string cRw)
	return HT7

string hh[7.14] <- MK
dynamic Yp <- false
var Xvx <- "zq"
func RLF (string Xj[64.62,78.23], bool Uw[58.09], string XW[90.14])
	begin
		string ek[64.87,98.89,75.67]
	end

'''
		expect = '''Program([FuncDecl(Id(So1O), [VarDecl(Id(W1L), ArrayType([19.61], BoolType), None, None), VarDecl(Id(y_), ArrayType([35.21, 89.18, 12.36], StringType), None, None), VarDecl(Id(cRw), StringType, None, None)], Return(Id(HT7))), VarDecl(Id(hh), ArrayType([7.14], StringType), None, Id(MK)), VarDecl(Id(Yp), None, dynamic, BooleanLit(False)), VarDecl(Id(Xvx), None, var, StringLit(zq)), FuncDecl(Id(RLF), [VarDecl(Id(Xj), ArrayType([64.62, 78.23], StringType), None, None), VarDecl(Id(Uw), ArrayType([58.09], BoolType), None, None), VarDecl(Id(XW), ArrayType([90.14], StringType), None, None)], Block([VarDecl(Id(ek), ArrayType([64.87, 98.89, 75.67], StringType), None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115367))

	def test_21530115368(self):
		input = '''
number oO[36.84,88.2]
'''
		expect = '''Program([VarDecl(Id(oO), ArrayType([36.84, 88.2], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115368))

	def test_21530115369(self):
		input = '''
func xY ()
	begin
		continue
	end
func dZt (bool dAv[75.47], bool VT[63.51])	begin
	end
bool Ou[30.87] <- 21.89
'''
		expect = '''Program([FuncDecl(Id(xY), [], Block([Continue])), FuncDecl(Id(dZt), [VarDecl(Id(dAv), ArrayType([75.47], BoolType), None, None), VarDecl(Id(VT), ArrayType([63.51], BoolType), None, None)], Block([])), VarDecl(Id(Ou), ArrayType([30.87], BoolType), None, NumLit(21.89))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115369))

	def test_21530115370(self):
		input = '''
var dkG <- 32.56
'''
		expect = '''Program([VarDecl(Id(dkG), None, var, NumLit(32.56))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115370))

	def test_21530115371(self):
		input = '''
bool g1[2.56] <- 46.4
'''
		expect = '''Program([VarDecl(Id(g1), ArrayType([2.56], BoolType), None, NumLit(46.4))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115371))

	def test_21530115372(self):
		input = '''
var KP <- true
'''
		expect = '''Program([VarDecl(Id(KP), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115372))

	def test_21530115373(self):
		input = '''
string mSSm[53.14]
number i5P <- true
func Yv (string Uy[28.18,17.53], string Np[81.95,42.37,23.86], bool dRA[68.77])
	begin
		bool yP[60.6]
	end

func Yb2l (string aD3r[41.6,20.55])
	begin
		begin
		end
	end
func v6z (number fkV)
	return true
'''
		expect = '''Program([VarDecl(Id(mSSm), ArrayType([53.14], StringType), None, None), VarDecl(Id(i5P), NumberType, None, BooleanLit(True)), FuncDecl(Id(Yv), [VarDecl(Id(Uy), ArrayType([28.18, 17.53], StringType), None, None), VarDecl(Id(Np), ArrayType([81.95, 42.37, 23.86], StringType), None, None), VarDecl(Id(dRA), ArrayType([68.77], BoolType), None, None)], Block([VarDecl(Id(yP), ArrayType([60.6], BoolType), None, None)])), FuncDecl(Id(Yb2l), [VarDecl(Id(aD3r), ArrayType([41.6, 20.55], StringType), None, None)], Block([Block([])])), FuncDecl(Id(v6z), [VarDecl(Id(fkV), NumberType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115373))

	def test_21530115374(self):
		input = '''
func Nd_ ()	return

'''
		expect = '''Program([FuncDecl(Id(Nd_), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115374))

	def test_21530115375(self):
		input = '''
var QkB7 <- pDW
string k6[17.86,82.88] <- "wtPrI"
bool Ps[75.27,2.25,68.42] <- "SX"
func Ie1 ()
	begin
		break
	end

bool je[56.51,65.7,6.95] <- 86.49
'''
		expect = '''Program([VarDecl(Id(QkB7), None, var, Id(pDW)), VarDecl(Id(k6), ArrayType([17.86, 82.88], StringType), None, StringLit(wtPrI)), VarDecl(Id(Ps), ArrayType([75.27, 2.25, 68.42], BoolType), None, StringLit(SX)), FuncDecl(Id(Ie1), [], Block([Break])), VarDecl(Id(je), ArrayType([56.51, 65.7, 6.95], BoolType), None, NumLit(86.49))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115375))

	def test_21530115376(self):
		input = '''
number OA <- Zk
'''
		expect = '''Program([VarDecl(Id(OA), NumberType, None, Id(Zk))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115376))

	def test_21530115377(self):
		input = '''
func vm (bool vKzZ)	begin
		break
		break
		bool eMuw
	end

func pr ()	return 75.64

bool JrD5 <- "dIrXK"
func uN (number C9C, bool Z2XE[28.77,46.56])	return
'''
		expect = '''Program([FuncDecl(Id(vm), [VarDecl(Id(vKzZ), BoolType, None, None)], Block([Break, Break, VarDecl(Id(eMuw), BoolType, None, None)])), FuncDecl(Id(pr), [], Return(NumLit(75.64))), VarDecl(Id(JrD5), BoolType, None, StringLit(dIrXK)), FuncDecl(Id(uN), [VarDecl(Id(C9C), NumberType, None, None), VarDecl(Id(Z2XE), ArrayType([28.77, 46.56], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115377))

	def test_21530115378(self):
		input = '''
func YE ()	begin
		begin
			for BQsr until 30.85 by false
				begin
					for JGH until "Eryv" by uEAv
						break
					break
				end
			begin
			end
			break
		end
		dynamic J89V
	end

func Ai (string Be_4[83.78,17.01], number kfg3[44.09,10.69], string Bf[21.9,61.02])
	return

func zn ()
	return
'''
		expect = '''Program([FuncDecl(Id(YE), [], Block([Block([For(Id(BQsr), NumLit(30.85), BooleanLit(False), Block([For(Id(JGH), StringLit(Eryv), Id(uEAv), Break), Break])), Block([]), Break]), VarDecl(Id(J89V), None, dynamic, None)])), FuncDecl(Id(Ai), [VarDecl(Id(Be_4), ArrayType([83.78, 17.01], StringType), None, None), VarDecl(Id(kfg3), ArrayType([44.09, 10.69], NumberType), None, None), VarDecl(Id(Bf), ArrayType([21.9, 61.02], StringType), None, None)], Return()), FuncDecl(Id(zn), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115378))

	def test_21530115379(self):
		input = '''
dynamic BeIx
func ij ()	return YCG
func bIf (bool r9, string uT4[89.64])	return g5R

'''
		expect = '''Program([VarDecl(Id(BeIx), None, dynamic, None), FuncDecl(Id(ij), [], Return(Id(YCG))), FuncDecl(Id(bIf), [VarDecl(Id(r9), BoolType, None, None), VarDecl(Id(uT4), ArrayType([89.64], StringType), None, None)], Return(Id(g5R)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115379))

	def test_21530115380(self):
		input = '''
number gRNp[71.24,19.36]
bool o_m[51.06]
string vo[37.76,28.7,33.29]
'''
		expect = '''Program([VarDecl(Id(gRNp), ArrayType([71.24, 19.36], NumberType), None, None), VarDecl(Id(o_m), ArrayType([51.06], BoolType), None, None), VarDecl(Id(vo), ArrayType([37.76, 28.7, 33.29], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115380))

	def test_21530115381(self):
		input = '''
func hcN (string LiC, number o8H, bool Od[75.87])	return

string Vp[27.23,45.04] <- 56.18
func n0 (string bc9e[99.1,39.64], number bhD, string a2qg[86.89])
	return "s"
string F6 <- "ZfOwK"
number vL <- "mAZFm"
'''
		expect = '''Program([FuncDecl(Id(hcN), [VarDecl(Id(LiC), StringType, None, None), VarDecl(Id(o8H), NumberType, None, None), VarDecl(Id(Od), ArrayType([75.87], BoolType), None, None)], Return()), VarDecl(Id(Vp), ArrayType([27.23, 45.04], StringType), None, NumLit(56.18)), FuncDecl(Id(n0), [VarDecl(Id(bc9e), ArrayType([99.1, 39.64], StringType), None, None), VarDecl(Id(bhD), NumberType, None, None), VarDecl(Id(a2qg), ArrayType([86.89], StringType), None, None)], Return(StringLit(s))), VarDecl(Id(F6), StringType, None, StringLit(ZfOwK)), VarDecl(Id(vL), NumberType, None, StringLit(mAZFm))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115381))

	def test_21530115382(self):
		input = '''
func gWhy (bool LUx[61.53])
	begin
		continue
		eu[dYOl] <- wh_H
	end

var qySL <- 91.58
number ibEG <- 78.82
func EO (bool CU[83.83,38.82,51.58], number CZ[13.64,86.73])
	return

dynamic H39y
'''
		expect = '''Program([FuncDecl(Id(gWhy), [VarDecl(Id(LUx), ArrayType([61.53], BoolType), None, None)], Block([Continue, AssignStmt(ArrayCell(Id(eu), [Id(dYOl)]), Id(wh_H))])), VarDecl(Id(qySL), None, var, NumLit(91.58)), VarDecl(Id(ibEG), NumberType, None, NumLit(78.82)), FuncDecl(Id(EO), [VarDecl(Id(CU), ArrayType([83.83, 38.82, 51.58], BoolType), None, None), VarDecl(Id(CZ), ArrayType([13.64, 86.73], NumberType), None, None)], Return()), VarDecl(Id(H39y), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115382))

	def test_21530115383(self):
		input = '''
func ziE (number W_54[2.8,69.45], string yB, string Rg19)
	begin
		Bc <- 2.48
		return true
	end

number Rj
func okze (string cApp, bool S5_W[62.83,66.58,16.09], string hG[42.5,30.27])	return
dynamic u3
func iSe (number PK)
	begin
		number eMWk[46.15,60.3]
		string mfW[5.35]
	end
'''
		expect = '''Program([FuncDecl(Id(ziE), [VarDecl(Id(W_54), ArrayType([2.8, 69.45], NumberType), None, None), VarDecl(Id(yB), StringType, None, None), VarDecl(Id(Rg19), StringType, None, None)], Block([AssignStmt(Id(Bc), NumLit(2.48)), Return(BooleanLit(True))])), VarDecl(Id(Rj), NumberType, None, None), FuncDecl(Id(okze), [VarDecl(Id(cApp), StringType, None, None), VarDecl(Id(S5_W), ArrayType([62.83, 66.58, 16.09], BoolType), None, None), VarDecl(Id(hG), ArrayType([42.5, 30.27], StringType), None, None)], Return()), VarDecl(Id(u3), None, dynamic, None), FuncDecl(Id(iSe), [VarDecl(Id(PK), NumberType, None, None)], Block([VarDecl(Id(eMWk), ArrayType([46.15, 60.3], NumberType), None, None), VarDecl(Id(mfW), ArrayType([5.35], StringType), None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115383))

	def test_21530115384(self):
		input = '''
bool ysEt
func N9vU (string N4, bool FbjB[29.52,25.75,80.23], number Ui)	return 18.26
number ME8 <- false
'''
		expect = '''Program([VarDecl(Id(ysEt), BoolType, None, None), FuncDecl(Id(N9vU), [VarDecl(Id(N4), StringType, None, None), VarDecl(Id(FbjB), ArrayType([29.52, 25.75, 80.23], BoolType), None, None), VarDecl(Id(Ui), NumberType, None, None)], Return(NumLit(18.26))), VarDecl(Id(ME8), NumberType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115384))

	def test_21530115385(self):
		input = '''
bool HV[41.25,81.16,6.51]
string xAzP <- false
func l0 (bool hD1[6.82,0.72], string Fxk[15.04,43.57], string hv[81.73])	return true
var LP8 <- hNIP
number Gv
'''
		expect = '''Program([VarDecl(Id(HV), ArrayType([41.25, 81.16, 6.51], BoolType), None, None), VarDecl(Id(xAzP), StringType, None, BooleanLit(False)), FuncDecl(Id(l0), [VarDecl(Id(hD1), ArrayType([6.82, 0.72], BoolType), None, None), VarDecl(Id(Fxk), ArrayType([15.04, 43.57], StringType), None, None), VarDecl(Id(hv), ArrayType([81.73], StringType), None, None)], Return(BooleanLit(True))), VarDecl(Id(LP8), None, var, Id(hNIP)), VarDecl(Id(Gv), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115385))

	def test_21530115386(self):
		input = '''
func bSSI (bool pl, bool fJVN[77.4], string nNi)
	return
number SV[79.5]
'''
		expect = '''Program([FuncDecl(Id(bSSI), [VarDecl(Id(pl), BoolType, None, None), VarDecl(Id(fJVN), ArrayType([77.4], BoolType), None, None), VarDecl(Id(nNi), StringType, None, None)], Return()), VarDecl(Id(SV), ArrayType([79.5], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115386))

	def test_21530115387(self):
		input = '''
number qw <- true
bool w1r6
dynamic JV
func g_ (number zseG)	return true
bool HT[28.58]
'''
		expect = '''Program([VarDecl(Id(qw), NumberType, None, BooleanLit(True)), VarDecl(Id(w1r6), BoolType, None, None), VarDecl(Id(JV), None, dynamic, None), FuncDecl(Id(g_), [VarDecl(Id(zseG), NumberType, None, None)], Return(BooleanLit(True))), VarDecl(Id(HT), ArrayType([28.58], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115387))

	def test_21530115388(self):
		input = '''
number wrq1 <- 83.75
func vX (bool eI9r, string csH, string Yq)	begin
		for uz until true by Vf7z
			if (true)
			A1KY(62.12, "WvGZh", 83.67)
			else break
		var RInq <- 36.87
		for c_hG until true by 59.38
			if (true)
			V4[true, true] <- "NpT"
			else S8j[71.1] <- Bc
	end
dynamic BlIl <- qP5b
'''
		expect = '''Program([VarDecl(Id(wrq1), NumberType, None, NumLit(83.75)), FuncDecl(Id(vX), [VarDecl(Id(eI9r), BoolType, None, None), VarDecl(Id(csH), StringType, None, None), VarDecl(Id(Yq), StringType, None, None)], Block([For(Id(uz), BooleanLit(True), Id(Vf7z), If(BooleanLit(True), CallStmt(Id(A1KY), [NumLit(62.12), StringLit(WvGZh), NumLit(83.67)])), [], Break), VarDecl(Id(RInq), None, var, NumLit(36.87)), For(Id(c_hG), BooleanLit(True), NumLit(59.38), If(BooleanLit(True), AssignStmt(ArrayCell(Id(V4), [BooleanLit(True), BooleanLit(True)]), StringLit(NpT))), [], AssignStmt(ArrayCell(Id(S8j), [NumLit(71.1)]), Id(Bc)))])), VarDecl(Id(BlIl), None, dynamic, Id(qP5b))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115388))

	def test_21530115389(self):
		input = '''
var Y0xK <- 8.57
func Kteq (bool K3Q[72.2,62.05,32.49], string Mkbn)
	return 79.77

string F7Ir[16.13,90.21] <- Oc
func ASp (string sP)
	return false
'''
		expect = '''Program([VarDecl(Id(Y0xK), None, var, NumLit(8.57)), FuncDecl(Id(Kteq), [VarDecl(Id(K3Q), ArrayType([72.2, 62.05, 32.49], BoolType), None, None), VarDecl(Id(Mkbn), StringType, None, None)], Return(NumLit(79.77))), VarDecl(Id(F7Ir), ArrayType([16.13, 90.21], StringType), None, Id(Oc)), FuncDecl(Id(ASp), [VarDecl(Id(sP), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115389))

	def test_21530115390(self):
		input = '''
number gk[55.4,21.91,9.4]
func xbR (number w7MO, string Y9z[91.51,31.28])
	return

bool XB[16.65,97.02,54.73]
bool uOiI[11.89,69.95] <- "M"
string Bh[97.23,83.37,77.22]
'''
		expect = '''Program([VarDecl(Id(gk), ArrayType([55.4, 21.91, 9.4], NumberType), None, None), FuncDecl(Id(xbR), [VarDecl(Id(w7MO), NumberType, None, None), VarDecl(Id(Y9z), ArrayType([91.51, 31.28], StringType), None, None)], Return()), VarDecl(Id(XB), ArrayType([16.65, 97.02, 54.73], BoolType), None, None), VarDecl(Id(uOiI), ArrayType([11.89, 69.95], BoolType), None, StringLit(M)), VarDecl(Id(Bh), ArrayType([97.23, 83.37, 77.22], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115390))

	def test_21530115391(self):
		input = '''
func IcL1 (number mxt[19.96,80.77,57.21])
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(IcL1), [VarDecl(Id(mxt), ArrayType([19.96, 80.77, 57.21], NumberType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115391))

	def test_21530115392(self):
		input = '''
func Qr (string lc0K)	begin
		j9n[Xx8, "Qr"] <- Cmc
		begin
		end
	end

number BP3[38.7] <- false
string g6 <- jYL
'''
		expect = '''Program([FuncDecl(Id(Qr), [VarDecl(Id(lc0K), StringType, None, None)], Block([AssignStmt(ArrayCell(Id(j9n), [Id(Xx8), StringLit(Qr)]), Id(Cmc)), Block([])])), VarDecl(Id(BP3), ArrayType([38.7], NumberType), None, BooleanLit(False)), VarDecl(Id(g6), StringType, None, Id(jYL))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115392))

	def test_21530115393(self):
		input = '''
number pFHI[52.11,55.56,23.97] <- XxO
'''
		expect = '''Program([VarDecl(Id(pFHI), ArrayType([52.11, 55.56, 23.97], NumberType), None, Id(XxO))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115393))

	def test_21530115394(self):
		input = '''
func lEzz (bool Bp9)
	begin
	end
func iq (bool oY1[78.55,50.5,62.62], string u4b, string R0er)
	begin
	end
func NL31 (bool c9Q[67.54,44.84], bool q5p, string VQ)	begin
		for Oy until true by bO
			dynamic cQg7
		continue
	end

'''
		expect = '''Program([FuncDecl(Id(lEzz), [VarDecl(Id(Bp9), BoolType, None, None)], Block([])), FuncDecl(Id(iq), [VarDecl(Id(oY1), ArrayType([78.55, 50.5, 62.62], BoolType), None, None), VarDecl(Id(u4b), StringType, None, None), VarDecl(Id(R0er), StringType, None, None)], Block([])), FuncDecl(Id(NL31), [VarDecl(Id(c9Q), ArrayType([67.54, 44.84], BoolType), None, None), VarDecl(Id(q5p), BoolType, None, None), VarDecl(Id(VQ), StringType, None, None)], Block([For(Id(Oy), BooleanLit(True), Id(bO), VarDecl(Id(cQg7), None, dynamic, None)), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115394))

	def test_21530115395(self):
		input = '''
func P_ (bool zRUl, bool hBN[19.8,88.5], number L6p)	begin
		begin
			for FJ until wdkX by "aXXlo"
				dynamic hB
			string dpc[2.93,8.57,56.08]
			break
		end
	end
string n6Wf[78.34,71.17,59.02]
func HPG (bool IP)	return

func sh2 (number Bhvw[92.34], string PTaJ)
	return

bool ljl[74.68,22.87,35.84]
'''
		expect = '''Program([FuncDecl(Id(P_), [VarDecl(Id(zRUl), BoolType, None, None), VarDecl(Id(hBN), ArrayType([19.8, 88.5], BoolType), None, None), VarDecl(Id(L6p), NumberType, None, None)], Block([Block([For(Id(FJ), Id(wdkX), StringLit(aXXlo), VarDecl(Id(hB), None, dynamic, None)), VarDecl(Id(dpc), ArrayType([2.93, 8.57, 56.08], StringType), None, None), Break])])), VarDecl(Id(n6Wf), ArrayType([78.34, 71.17, 59.02], StringType), None, None), FuncDecl(Id(HPG), [VarDecl(Id(IP), BoolType, None, None)], Return()), FuncDecl(Id(sh2), [VarDecl(Id(Bhvw), ArrayType([92.34], NumberType), None, None), VarDecl(Id(PTaJ), StringType, None, None)], Return()), VarDecl(Id(ljl), ArrayType([74.68, 22.87, 35.84], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115395))

	def test_21530115396(self):
		input = '''
bool tL70[87.24,40.07] <- xVwt
func IkO (string Acm[67.43,66.32,20.4])	return nCc4

bool gVg
func elOn (string Xr[96.23], string cRsD[40.72], number hsk)	return

'''
		expect = '''Program([VarDecl(Id(tL70), ArrayType([87.24, 40.07], BoolType), None, Id(xVwt)), FuncDecl(Id(IkO), [VarDecl(Id(Acm), ArrayType([67.43, 66.32, 20.4], StringType), None, None)], Return(Id(nCc4))), VarDecl(Id(gVg), BoolType, None, None), FuncDecl(Id(elOn), [VarDecl(Id(Xr), ArrayType([96.23], StringType), None, None), VarDecl(Id(cRsD), ArrayType([40.72], StringType), None, None), VarDecl(Id(hsk), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115396))

	def test_21530115397(self):
		input = '''
func GqM0 (bool QGA)	return
var ndiJ <- true
func rnj (number UvI3[22.84,25.94], string Xm[75.91,84.02], string Sf)
	begin
		if (31.26)
		PaLh[true] <- 93.57
		elif ("zX") var J5 <- true
		elif (40.38) for A8 until "MqG" by 62.85
			qw()
		elif (true)
		break
		elif (91.42)
		continue
		else break
		return
		break
	end

func NUK (string Q0K[75.92], string nf8h[66.92,5.35,36.04], string aJKD)
	return

func ynJ ()	return

'''
		expect = '''Program([FuncDecl(Id(GqM0), [VarDecl(Id(QGA), BoolType, None, None)], Return()), VarDecl(Id(ndiJ), None, var, BooleanLit(True)), FuncDecl(Id(rnj), [VarDecl(Id(UvI3), ArrayType([22.84, 25.94], NumberType), None, None), VarDecl(Id(Xm), ArrayType([75.91, 84.02], StringType), None, None), VarDecl(Id(Sf), StringType, None, None)], Block([If(NumLit(31.26), AssignStmt(ArrayCell(Id(PaLh), [BooleanLit(True)]), NumLit(93.57))), [(StringLit(zX), VarDecl(Id(J5), None, var, BooleanLit(True))), (NumLit(40.38), For(Id(A8), StringLit(MqG), NumLit(62.85), CallStmt(Id(qw), []))), (BooleanLit(True), Break), (NumLit(91.42), Continue)], Break, Return(), Break])), FuncDecl(Id(NUK), [VarDecl(Id(Q0K), ArrayType([75.92], StringType), None, None), VarDecl(Id(nf8h), ArrayType([66.92, 5.35, 36.04], StringType), None, None), VarDecl(Id(aJKD), StringType, None, None)], Return()), FuncDecl(Id(ynJ), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115397))

	def test_21530115398(self):
		input = '''
string E72[18.31] <- k0Tq
'''
		expect = '''Program([VarDecl(Id(E72), ArrayType([18.31], StringType), None, Id(k0Tq))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115398))

	def test_21530115399(self):
		input = '''
func SKLG (string oJ[84.95], string KR)
	begin
		sIam()
	end
func M7j (string o5[93.68])	begin
		k8NR(true)
	end
string cdN <- "KYd"
func oo ()
	return
'''
		expect = '''Program([FuncDecl(Id(SKLG), [VarDecl(Id(oJ), ArrayType([84.95], StringType), None, None), VarDecl(Id(KR), StringType, None, None)], Block([CallStmt(Id(sIam), [])])), FuncDecl(Id(M7j), [VarDecl(Id(o5), ArrayType([93.68], StringType), None, None)], Block([CallStmt(Id(k8NR), [BooleanLit(True)])])), VarDecl(Id(cdN), StringType, None, StringLit(KYd)), FuncDecl(Id(oo), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115399))

	def test_21530115400(self):
		input = '''
bool Fck
'''
		expect = '''Program([VarDecl(Id(Fck), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115400))

	def test_21530115401(self):
		input = '''
func VAxc ()
	begin
		return
	end
func ND (string WVb[13.11,6.57], string iQWy, number Siq[26.66])
	return
func YmIz (bool Qz)
	begin
		var Ah <- 19.4
		cwMv()
	end
'''
		expect = '''Program([FuncDecl(Id(VAxc), [], Block([Return()])), FuncDecl(Id(ND), [VarDecl(Id(WVb), ArrayType([13.11, 6.57], StringType), None, None), VarDecl(Id(iQWy), StringType, None, None), VarDecl(Id(Siq), ArrayType([26.66], NumberType), None, None)], Return()), FuncDecl(Id(YmIz), [VarDecl(Id(Qz), BoolType, None, None)], Block([VarDecl(Id(Ah), None, var, NumLit(19.4)), CallStmt(Id(cwMv), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115401))

	def test_21530115402(self):
		input = '''
func Cs (bool gLJ)	return 1.28

func S83p (bool fXW)	begin
		break
		begin
			C8()
		end
		P_(56.76, NmvH)
	end
string ShF[7.32,22.06]
'''
		expect = '''Program([FuncDecl(Id(Cs), [VarDecl(Id(gLJ), BoolType, None, None)], Return(NumLit(1.28))), FuncDecl(Id(S83p), [VarDecl(Id(fXW), BoolType, None, None)], Block([Break, Block([CallStmt(Id(C8), [])]), CallStmt(Id(P_), [NumLit(56.76), Id(NmvH)])])), VarDecl(Id(ShF), ArrayType([7.32, 22.06], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115402))

	def test_21530115403(self):
		input = '''
number Bj[5.05,96.07,21.27] <- sf
bool xjl
'''
		expect = '''Program([VarDecl(Id(Bj), ArrayType([5.05, 96.07, 21.27], NumberType), None, Id(sf)), VarDecl(Id(xjl), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115403))

	def test_21530115404(self):
		input = '''
string ODU[85.68,41.04] <- 86.58
string Dz[59.32,60.05,66.5] <- 18.37
'''
		expect = '''Program([VarDecl(Id(ODU), ArrayType([85.68, 41.04], StringType), None, NumLit(86.58)), VarDecl(Id(Dz), ArrayType([59.32, 60.05, 66.5], StringType), None, NumLit(18.37))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115404))

	def test_21530115405(self):
		input = '''
func Pqi ()	return
func sAf (string ZYGm[72.81])	return
func mvA ()	return "YCmf"

'''
		expect = '''Program([FuncDecl(Id(Pqi), [], Return()), FuncDecl(Id(sAf), [VarDecl(Id(ZYGm), ArrayType([72.81], StringType), None, None)], Return()), FuncDecl(Id(mvA), [], Return(StringLit(YCmf)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115405))

	def test_21530115406(self):
		input = '''
func P5S ()
	begin
		continue
		return
	end
bool sEwC[92.95] <- "LBWc"
'''
		expect = '''Program([FuncDecl(Id(P5S), [], Block([Continue, Return()])), VarDecl(Id(sEwC), ArrayType([92.95], BoolType), None, StringLit(LBWc))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115406))

	def test_21530115407(self):
		input = '''
func OK (number elQ, number i50)
	begin
	end

number WYH
bool hK[48.62,9.07] <- RUX
'''
		expect = '''Program([FuncDecl(Id(OK), [VarDecl(Id(elQ), NumberType, None, None), VarDecl(Id(i50), NumberType, None, None)], Block([])), VarDecl(Id(WYH), NumberType, None, None), VarDecl(Id(hK), ArrayType([48.62, 9.07], BoolType), None, Id(RUX))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115407))

	def test_21530115408(self):
		input = '''
string M2xa
func CV (string xi2, number CE[6.18,16.26])
	return
func VZ ()
	return

'''
		expect = '''Program([VarDecl(Id(M2xa), StringType, None, None), FuncDecl(Id(CV), [VarDecl(Id(xi2), StringType, None, None), VarDecl(Id(CE), ArrayType([6.18, 16.26], NumberType), None, None)], Return()), FuncDecl(Id(VZ), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115408))

	def test_21530115409(self):
		input = '''
string Gn[25.66,13.75] <- true
func eYf (bool mzpm[68.04], bool zRRc, number lI[96.2,15.05,31.16])	return
func sjfR ()
	return 59.48
'''
		expect = '''Program([VarDecl(Id(Gn), ArrayType([25.66, 13.75], StringType), None, BooleanLit(True)), FuncDecl(Id(eYf), [VarDecl(Id(mzpm), ArrayType([68.04], BoolType), None, None), VarDecl(Id(zRRc), BoolType, None, None), VarDecl(Id(lI), ArrayType([96.2, 15.05, 31.16], NumberType), None, None)], Return()), FuncDecl(Id(sjfR), [], Return(NumLit(59.48)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115409))

	def test_21530115410(self):
		input = '''
string w7
'''
		expect = '''Program([VarDecl(Id(w7), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115410))

	def test_21530115411(self):
		input = '''
var fA_ <- Df
bool NNW[34.56,26.79,55.54] <- "ko"
'''
		expect = '''Program([VarDecl(Id(fA_), None, var, Id(Df)), VarDecl(Id(NNW), ArrayType([34.56, 26.79, 55.54], BoolType), None, StringLit(ko))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115411))

	def test_21530115412(self):
		input = '''
func sgp (string I97_[39.9], number wk[44.26])
	begin
		UHI()
		break
		number uZ[2.22,48.68,80.32] <- "HYcHi"
	end
var AL <- "Qmo"
bool yjT[26.0,66.52]
func SG (number vLQ[40.73], string Dr)	return
'''
		expect = '''Program([FuncDecl(Id(sgp), [VarDecl(Id(I97_), ArrayType([39.9], StringType), None, None), VarDecl(Id(wk), ArrayType([44.26], NumberType), None, None)], Block([CallStmt(Id(UHI), []), Break, VarDecl(Id(uZ), ArrayType([2.22, 48.68, 80.32], NumberType), None, StringLit(HYcHi))])), VarDecl(Id(AL), None, var, StringLit(Qmo)), VarDecl(Id(yjT), ArrayType([26.0, 66.52], BoolType), None, None), FuncDecl(Id(SG), [VarDecl(Id(vLQ), ArrayType([40.73], NumberType), None, None), VarDecl(Id(Dr), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115412))

	def test_21530115413(self):
		input = '''
string KbmK[11.3,19.25]
var WI4 <- "vrP"
number bEi0[0.05,0.98,57.47] <- EH
'''
		expect = '''Program([VarDecl(Id(KbmK), ArrayType([11.3, 19.25], StringType), None, None), VarDecl(Id(WI4), None, var, StringLit(vrP)), VarDecl(Id(bEi0), ArrayType([0.05, 0.98, 57.47], NumberType), None, Id(EH))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115413))

	def test_21530115414(self):
		input = '''
func tCB7 (bool t0, string MY[22.08])
	begin
	end

bool IQEm[1.28,80.94] <- CEn
dynamic N5H
string Aft[93.75,59.9] <- 20.67
func Lr54 (bool f6LO)
	return

'''
		expect = '''Program([FuncDecl(Id(tCB7), [VarDecl(Id(t0), BoolType, None, None), VarDecl(Id(MY), ArrayType([22.08], StringType), None, None)], Block([])), VarDecl(Id(IQEm), ArrayType([1.28, 80.94], BoolType), None, Id(CEn)), VarDecl(Id(N5H), None, dynamic, None), VarDecl(Id(Aft), ArrayType([93.75, 59.9], StringType), None, NumLit(20.67)), FuncDecl(Id(Lr54), [VarDecl(Id(f6LO), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115414))

	def test_21530115415(self):
		input = '''
dynamic h5 <- 93.73
bool tki[89.59]
'''
		expect = '''Program([VarDecl(Id(h5), None, dynamic, NumLit(93.73)), VarDecl(Id(tki), ArrayType([89.59], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115415))

	def test_21530115416(self):
		input = '''
func MpUg ()	begin
		EUo("d", "waiIc")
	end
'''
		expect = '''Program([FuncDecl(Id(MpUg), [], Block([CallStmt(Id(EUo), [StringLit(d), StringLit(waiIc)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115416))

	def test_21530115417(self):
		input = '''
func eJ20 (string vSI[52.13])	begin
		return false
	end

func v0f (number haT, number BI[9.55,0.86], bool edfD)	return true

func qN ()	return

dynamic ZR13 <- uu7O
'''
		expect = '''Program([FuncDecl(Id(eJ20), [VarDecl(Id(vSI), ArrayType([52.13], StringType), None, None)], Block([Return(BooleanLit(False))])), FuncDecl(Id(v0f), [VarDecl(Id(haT), NumberType, None, None), VarDecl(Id(BI), ArrayType([9.55, 0.86], NumberType), None, None), VarDecl(Id(edfD), BoolType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(qN), [], Return()), VarDecl(Id(ZR13), None, dynamic, Id(uu7O))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115417))

	def test_21530115418(self):
		input = '''
func Vr0N (bool JsV)
	begin
	end
func uXM (string NQvn, number maO[11.3])	return zC8
'''
		expect = '''Program([FuncDecl(Id(Vr0N), [VarDecl(Id(JsV), BoolType, None, None)], Block([])), FuncDecl(Id(uXM), [VarDecl(Id(NQvn), StringType, None, None), VarDecl(Id(maO), ArrayType([11.3], NumberType), None, None)], Return(Id(zC8)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115418))

	def test_21530115419(self):
		input = '''
string dqV7[1.63] <- 47.47
bool maR
'''
		expect = '''Program([VarDecl(Id(dqV7), ArrayType([1.63], StringType), None, NumLit(47.47)), VarDecl(Id(maR), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115419))

	def test_21530115420(self):
		input = '''
string nLU[75.94]
func aj (number Nq)	begin
		return
		g9Do("QNF")
	end

'''
		expect = '''Program([VarDecl(Id(nLU), ArrayType([75.94], StringType), None, None), FuncDecl(Id(aj), [VarDecl(Id(Nq), NumberType, None, None)], Block([Return(), CallStmt(Id(g9Do), [StringLit(QNF)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115420))

	def test_21530115421(self):
		input = '''
number mV[41.55,87.35]
'''
		expect = '''Program([VarDecl(Id(mV), ArrayType([41.55, 87.35], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115421))

	def test_21530115422(self):
		input = '''
string Evo[59.37] <- t7
func AmaB (bool K2FX)	begin
		continue
		if (false)
		ywmO(dOtO, 9.79, false)
		elif (P4)
		break
		elif ("iNns")
		G87z[false, zIu] <- RmP8
		elif (true) if (98.12) begin
		end
		elif ("hcwm")
		begin
			return
			continue
		end
		return
	end
func bUfz (bool yW10, bool n26[40.32,53.68,27.96])
	begin
		r0fg(44.91, 73.96, 75.82)
		break
		tJ("WoQ")
	end

string oWRJ[40.58]
var jmJ <- "DgXdV"
'''
		expect = '''Program([VarDecl(Id(Evo), ArrayType([59.37], StringType), None, Id(t7)), FuncDecl(Id(AmaB), [VarDecl(Id(K2FX), BoolType, None, None)], Block([Continue, If(BooleanLit(False), CallStmt(Id(ywmO), [Id(dOtO), NumLit(9.79), BooleanLit(False)])), [(Id(P4), Break), (StringLit(iNns), AssignStmt(ArrayCell(Id(G87z), [BooleanLit(False), Id(zIu)]), Id(RmP8))), (BooleanLit(True), If(NumLit(98.12), Block([])), [(StringLit(hcwm), Block([Return(), Continue]))], None)], None, Return()])), FuncDecl(Id(bUfz), [VarDecl(Id(yW10), BoolType, None, None), VarDecl(Id(n26), ArrayType([40.32, 53.68, 27.96], BoolType), None, None)], Block([CallStmt(Id(r0fg), [NumLit(44.91), NumLit(73.96), NumLit(75.82)]), Break, CallStmt(Id(tJ), [StringLit(WoQ)])])), VarDecl(Id(oWRJ), ArrayType([40.58], StringType), None, None), VarDecl(Id(jmJ), None, var, StringLit(DgXdV))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115422))

	def test_21530115423(self):
		input = '''
string L6[92.98,84.7]
func mDBZ (string WYv[88.03])	return
'''
		expect = '''Program([VarDecl(Id(L6), ArrayType([92.98, 84.7], StringType), None, None), FuncDecl(Id(mDBZ), [VarDecl(Id(WYv), ArrayType([88.03], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115423))

	def test_21530115424(self):
		input = '''
string Msb <- "IiDu"
func k1 ()	return false
bool bk <- "h"
func TYL (number Zj[43.06,45.1,61.82], string jeFy, bool IPqt)
	return

'''
		expect = '''Program([VarDecl(Id(Msb), StringType, None, StringLit(IiDu)), FuncDecl(Id(k1), [], Return(BooleanLit(False))), VarDecl(Id(bk), BoolType, None, StringLit(h)), FuncDecl(Id(TYL), [VarDecl(Id(Zj), ArrayType([43.06, 45.1, 61.82], NumberType), None, None), VarDecl(Id(jeFy), StringType, None, None), VarDecl(Id(IPqt), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115424))

	def test_21530115425(self):
		input = '''
func pH (string BM0[62.46,36.58,46.64])	return
'''
		expect = '''Program([FuncDecl(Id(pH), [VarDecl(Id(BM0), ArrayType([62.46, 36.58, 46.64], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115425))

	def test_21530115426(self):
		input = '''
dynamic M2sp <- 98.21
number nobe[74.71,57.18,87.48] <- d5TG
func F7_ (bool p6k, number gjn)	begin
		for kKEP until false by true
			for vok until true by xv
				if (29.34)
				if (JFcW) if (QwQ) begin
				end
				elif (55.29) vH[70.28, true, 33.74] <- 57.14
				elif ("hv") break
				elif (Ko)
				continue
				else number Dkv[44.32,68.92,76.76]
				elif (50.58) break
				else return
		s9j5[36.08] <- true
		return 37.61
	end

func FQL (string Uqa)	return false

'''
		expect = '''Program([VarDecl(Id(M2sp), None, dynamic, NumLit(98.21)), VarDecl(Id(nobe), ArrayType([74.71, 57.18, 87.48], NumberType), None, Id(d5TG)), FuncDecl(Id(F7_), [VarDecl(Id(p6k), BoolType, None, None), VarDecl(Id(gjn), NumberType, None, None)], Block([For(Id(kKEP), BooleanLit(False), BooleanLit(True), For(Id(vok), BooleanLit(True), Id(xv), If(NumLit(29.34), If(Id(JFcW), If(Id(QwQ), Block([])), [(NumLit(55.29), AssignStmt(ArrayCell(Id(vH), [NumLit(70.28), BooleanLit(True), NumLit(33.74)]), NumLit(57.14))), (StringLit(hv), Break), (Id(Ko), Continue)], VarDecl(Id(Dkv), ArrayType([44.32, 68.92, 76.76], NumberType), None, None)), [(NumLit(50.58), Break)], Return()), [], None)), AssignStmt(ArrayCell(Id(s9j5), [NumLit(36.08)]), BooleanLit(True)), Return(NumLit(37.61))])), FuncDecl(Id(FQL), [VarDecl(Id(Uqa), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115426))

	def test_21530115427(self):
		input = '''
string yXu[47.66,57.46,82.62] <- false
func XC (bool Ku[29.43,30.93])	return true

'''
		expect = '''Program([VarDecl(Id(yXu), ArrayType([47.66, 57.46, 82.62], StringType), None, BooleanLit(False)), FuncDecl(Id(XC), [VarDecl(Id(Ku), ArrayType([29.43, 30.93], BoolType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115427))

	def test_21530115428(self):
		input = '''
dynamic UpK <- 51.37
string MJ <- false
'''
		expect = '''Program([VarDecl(Id(UpK), None, dynamic, NumLit(51.37)), VarDecl(Id(MJ), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115428))

	def test_21530115429(self):
		input = '''
string PE
func eYx6 (string BT[44.31,60.38], bool WwH6)
	return

'''
		expect = '''Program([VarDecl(Id(PE), StringType, None, None), FuncDecl(Id(eYx6), [VarDecl(Id(BT), ArrayType([44.31, 60.38], StringType), None, None), VarDecl(Id(WwH6), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115429))

	def test_21530115430(self):
		input = '''
string J1v[42.97] <- "JXgJ"
'''
		expect = '''Program([VarDecl(Id(J1v), ArrayType([42.97], StringType), None, StringLit(JXgJ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115430))

	def test_21530115431(self):
		input = '''
string BR
string YD16[5.66]
bool TUj[44.61,61.71]
number Wg
'''
		expect = '''Program([VarDecl(Id(BR), StringType, None, None), VarDecl(Id(YD16), ArrayType([5.66], StringType), None, None), VarDecl(Id(TUj), ArrayType([44.61, 61.71], BoolType), None, None), VarDecl(Id(Wg), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115431))

	def test_21530115432(self):
		input = '''
var R09q <- false
string dl[97.45,93.24] <- 82.86
'''
		expect = '''Program([VarDecl(Id(R09q), None, var, BooleanLit(False)), VarDecl(Id(dl), ArrayType([97.45, 93.24], StringType), None, NumLit(82.86))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115432))

	def test_21530115433(self):
		input = '''
func qi ()	return 11.53
bool bt60 <- true
func Cc (string JMwd[53.07,59.61,18.69], bool fs[42.77], bool ml)	begin
		return
		break
		B_[IVKJ, "L"] <- true
	end
func qWX (string qfy[63.34], string xs8, bool WPyP[72.32,39.9,95.78])
	return 25.0
'''
		expect = '''Program([FuncDecl(Id(qi), [], Return(NumLit(11.53))), VarDecl(Id(bt60), BoolType, None, BooleanLit(True)), FuncDecl(Id(Cc), [VarDecl(Id(JMwd), ArrayType([53.07, 59.61, 18.69], StringType), None, None), VarDecl(Id(fs), ArrayType([42.77], BoolType), None, None), VarDecl(Id(ml), BoolType, None, None)], Block([Return(), Break, AssignStmt(ArrayCell(Id(B_), [Id(IVKJ), StringLit(L)]), BooleanLit(True))])), FuncDecl(Id(qWX), [VarDecl(Id(qfy), ArrayType([63.34], StringType), None, None), VarDecl(Id(xs8), StringType, None, None), VarDecl(Id(WPyP), ArrayType([72.32, 39.9, 95.78], BoolType), None, None)], Return(NumLit(25.0)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115433))

	def test_21530115434(self):
		input = '''
func Uj0 ()
	begin
		for qk until "g" by oI
			G5(true)
	end
func nTK (bool tK_D[60.62,17.52,60.29])	return
func Jw (number Q6[57.63], bool rI, string lVdd[10.37,6.4])
	return

string CC[43.9]
func XCj (string vMHV[13.63], number Gfyt[74.99,86.76], string wvHx)	return

'''
		expect = '''Program([FuncDecl(Id(Uj0), [], Block([For(Id(qk), StringLit(g), Id(oI), CallStmt(Id(G5), [BooleanLit(True)]))])), FuncDecl(Id(nTK), [VarDecl(Id(tK_D), ArrayType([60.62, 17.52, 60.29], BoolType), None, None)], Return()), FuncDecl(Id(Jw), [VarDecl(Id(Q6), ArrayType([57.63], NumberType), None, None), VarDecl(Id(rI), BoolType, None, None), VarDecl(Id(lVdd), ArrayType([10.37, 6.4], StringType), None, None)], Return()), VarDecl(Id(CC), ArrayType([43.9], StringType), None, None), FuncDecl(Id(XCj), [VarDecl(Id(vMHV), ArrayType([13.63], StringType), None, None), VarDecl(Id(Gfyt), ArrayType([74.99, 86.76], NumberType), None, None), VarDecl(Id(wvHx), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115434))

	def test_21530115435(self):
		input = '''
bool WyI
'''
		expect = '''Program([VarDecl(Id(WyI), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115435))

	def test_21530115436(self):
		input = '''
func lC (number iPp[63.62,99.04,30.79], bool qwwc)	return
func d9 (number M1r, bool KY3s)
	return true

func GW ()
	return false
func sOue (number K7, number x4A)
	begin
		if (true) number uzye[8.89,69.16,53.44]
		elif (KT)
		oN(true, 11.96, "J")
		elif (65.61) imz(ZQ26, 52.94)
		elif ("n")
		return
		else string RsXg <- true
	end

'''
		expect = '''Program([FuncDecl(Id(lC), [VarDecl(Id(iPp), ArrayType([63.62, 99.04, 30.79], NumberType), None, None), VarDecl(Id(qwwc), BoolType, None, None)], Return()), FuncDecl(Id(d9), [VarDecl(Id(M1r), NumberType, None, None), VarDecl(Id(KY3s), BoolType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(GW), [], Return(BooleanLit(False))), FuncDecl(Id(sOue), [VarDecl(Id(K7), NumberType, None, None), VarDecl(Id(x4A), NumberType, None, None)], Block([If(BooleanLit(True), VarDecl(Id(uzye), ArrayType([8.89, 69.16, 53.44], NumberType), None, None)), [(Id(KT), CallStmt(Id(oN), [BooleanLit(True), NumLit(11.96), StringLit(J)])), (NumLit(65.61), CallStmt(Id(imz), [Id(ZQ26), NumLit(52.94)])), (StringLit(n), Return())], VarDecl(Id(RsXg), StringType, None, BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115436))

	def test_21530115437(self):
		input = '''
bool pazk
func oKF (bool DX[6.16,96.35,77.37])
	return 58.27
func G8 (string KmpK)	return
func sAsG (number VWH)
	return

'''
		expect = '''Program([VarDecl(Id(pazk), BoolType, None, None), FuncDecl(Id(oKF), [VarDecl(Id(DX), ArrayType([6.16, 96.35, 77.37], BoolType), None, None)], Return(NumLit(58.27))), FuncDecl(Id(G8), [VarDecl(Id(KmpK), StringType, None, None)], Return()), FuncDecl(Id(sAsG), [VarDecl(Id(VWH), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115437))

	def test_21530115438(self):
		input = '''
number if7G[98.05,91.97,26.58] <- "gwV"
string Lu
string X5zX <- false
'''
		expect = '''Program([VarDecl(Id(if7G), ArrayType([98.05, 91.97, 26.58], NumberType), None, StringLit(gwV)), VarDecl(Id(Lu), StringType, None, None), VarDecl(Id(X5zX), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115438))

	def test_21530115439(self):
		input = '''
func I0hZ (bool g18[81.1,38.7,23.95])
	return
number xrC[79.85]
func WA (bool oHc3[24.24,87.34])	return true
bool u9Lb[24.94,98.96,37.75] <- jq3u
'''
		expect = '''Program([FuncDecl(Id(I0hZ), [VarDecl(Id(g18), ArrayType([81.1, 38.7, 23.95], BoolType), None, None)], Return()), VarDecl(Id(xrC), ArrayType([79.85], NumberType), None, None), FuncDecl(Id(WA), [VarDecl(Id(oHc3), ArrayType([24.24, 87.34], BoolType), None, None)], Return(BooleanLit(True))), VarDecl(Id(u9Lb), ArrayType([24.94, 98.96, 37.75], BoolType), None, Id(jq3u))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115439))

	def test_21530115440(self):
		input = '''
bool Ty <- 3.71
dynamic YC
'''
		expect = '''Program([VarDecl(Id(Ty), BoolType, None, NumLit(3.71)), VarDecl(Id(YC), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115440))

	def test_21530115441(self):
		input = '''
func zHGi (number iBAq, bool V51u)	return
'''
		expect = '''Program([FuncDecl(Id(zHGi), [VarDecl(Id(iBAq), NumberType, None, None), VarDecl(Id(V51u), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115441))

	def test_21530115442(self):
		input = '''
func LcKF (number b3Z[72.71,65.06], bool vKvk[82.84,75.9,49.41])	begin
	end

number CmTg
var YR <- false
'''
		expect = '''Program([FuncDecl(Id(LcKF), [VarDecl(Id(b3Z), ArrayType([72.71, 65.06], NumberType), None, None), VarDecl(Id(vKvk), ArrayType([82.84, 75.9, 49.41], BoolType), None, None)], Block([])), VarDecl(Id(CmTg), NumberType, None, None), VarDecl(Id(YR), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115442))

	def test_21530115443(self):
		input = '''
func jD (bool asP[30.02,89.85], string hw[83.58,41.67], string hyV[10.6,45.1,18.52])	return

func Cwu (bool qbsF, string S69g)
	begin
		for XtN until "AlK" by false
			dynamic qyp <- "IOOt"
		string Opp0[3.36,91.37,33.41]
		begin
			hLA <- "WjLf"
		end
	end
func XVg (number Hw5w[10.25,63.3,7.9])	return

func daQ (number HXRW, number ft[22.58])
	return DGNP

'''
		expect = '''Program([FuncDecl(Id(jD), [VarDecl(Id(asP), ArrayType([30.02, 89.85], BoolType), None, None), VarDecl(Id(hw), ArrayType([83.58, 41.67], StringType), None, None), VarDecl(Id(hyV), ArrayType([10.6, 45.1, 18.52], StringType), None, None)], Return()), FuncDecl(Id(Cwu), [VarDecl(Id(qbsF), BoolType, None, None), VarDecl(Id(S69g), StringType, None, None)], Block([For(Id(XtN), StringLit(AlK), BooleanLit(False), VarDecl(Id(qyp), None, dynamic, StringLit(IOOt))), VarDecl(Id(Opp0), ArrayType([3.36, 91.37, 33.41], StringType), None, None), Block([AssignStmt(Id(hLA), StringLit(WjLf))])])), FuncDecl(Id(XVg), [VarDecl(Id(Hw5w), ArrayType([10.25, 63.3, 7.9], NumberType), None, None)], Return()), FuncDecl(Id(daQ), [VarDecl(Id(HXRW), NumberType, None, None), VarDecl(Id(ft), ArrayType([22.58], NumberType), None, None)], Return(Id(DGNP)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115443))

	def test_21530115444(self):
		input = '''
bool uvAU[85.59]
var oX <- MQQ_
'''
		expect = '''Program([VarDecl(Id(uvAU), ArrayType([85.59], BoolType), None, None), VarDecl(Id(oX), None, var, Id(MQQ_))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115444))

	def test_21530115445(self):
		input = '''
string Fms <- eu
func kpN (number gFFq)
	return "awunq"
func OwTB (string nG8q, bool D7DU[15.32])	return

func bXW (string e9IO[56.25,78.73], number j25[3.79,22.92], bool VM1)	begin
		for w3u until true by 32.79
			if ("ezQIH")
			begin
				begin
				end
				syi(stXr, 85.43)
			end
			elif (79.39)
			return 32.16
			elif (76.66)
			ll[fHU, "KcrZ"] <- "NfT"
			elif (86.08)
			if ("r") begin
				WqZ("ooF")
			end
			elif (13.79)
			number FJEB[69.46,70.85,88.9]
			elif (27.56)
			ux[61.5, Q9ko] <- TLP
			elif (false) if ("zSFaP")
			begin
				return
				continue
			end
			elif (WktP) if (false)
			if (g4) N26["C", false] <- 9.11
			elif (3.98)
			break
			elif (true)
			begin
				continue
				khDS <- 74.72
				vJU(kqw, false, hA)
			end
			elif ("AKXJc")
			begin
			end
			elif (true)
			begin
			end
			else if ("zmx") begin
				for uQqg until mp by ltbE
					begin
					end
				break
				NvP[false, x5] <- cTD
			end
			elif (false) if (77.02) return false
			elif (true)
			break
			elif ("wxw")
			for L0Yu until "az" by N75p
				break
			elif (false) begin
				continue
				return
				en("vr")
			end
			elif (HSVL) return rR
			elif (61.66)
			begin
				number r4O
				Od <- "aXRT"
				for L4 until 57.31 by true
					xo86["Embe"] <- "tp"
			end
			elif ("M")
			return
			else break
			elif (16.64) break
			elif (93.16) continue
			elif (false)
			gYW[true, false, 78.41] <- "eocuv"
			elif (eoK)
			return 92.27
			else if (55.37)
			return 78.92
			elif ("M") begin
				Bndd[23.06] <- XBI
			end
			else HZF[81.78] <- DC
		if ("Klio") begin
			if (86.63) y6I <- "gNTH"
			else continue
		end
		elif ("CCs") GpU(86.46, true)
		elif ("NBaYO")
		for pir until g0Qm by 10.1
			return
		else Qf(26.0)
		RS5()
	end
'''
		expect = '''Program([VarDecl(Id(Fms), StringType, None, Id(eu)), FuncDecl(Id(kpN), [VarDecl(Id(gFFq), NumberType, None, None)], Return(StringLit(awunq))), FuncDecl(Id(OwTB), [VarDecl(Id(nG8q), StringType, None, None), VarDecl(Id(D7DU), ArrayType([15.32], BoolType), None, None)], Return()), FuncDecl(Id(bXW), [VarDecl(Id(e9IO), ArrayType([56.25, 78.73], StringType), None, None), VarDecl(Id(j25), ArrayType([3.79, 22.92], NumberType), None, None), VarDecl(Id(VM1), BoolType, None, None)], Block([For(Id(w3u), BooleanLit(True), NumLit(32.79), If(StringLit(ezQIH), Block([Block([]), CallStmt(Id(syi), [Id(stXr), NumLit(85.43)])])), [(NumLit(79.39), Return(NumLit(32.16))), (NumLit(76.66), AssignStmt(ArrayCell(Id(ll), [Id(fHU), StringLit(KcrZ)]), StringLit(NfT))), (NumLit(86.08), If(StringLit(r), Block([CallStmt(Id(WqZ), [StringLit(ooF)])])), [(NumLit(13.79), VarDecl(Id(FJEB), ArrayType([69.46, 70.85, 88.9], NumberType), None, None)), (NumLit(27.56), AssignStmt(ArrayCell(Id(ux), [NumLit(61.5), Id(Q9ko)]), Id(TLP))), (BooleanLit(False), If(StringLit(zSFaP), Block([Return(), Continue])), [(Id(WktP), If(BooleanLit(False), If(Id(g4), AssignStmt(ArrayCell(Id(N26), [StringLit(C), BooleanLit(False)]), NumLit(9.11))), [(NumLit(3.98), Break), (BooleanLit(True), Block([Continue, AssignStmt(Id(khDS), NumLit(74.72)), CallStmt(Id(vJU), [Id(kqw), BooleanLit(False), Id(hA)])])), (StringLit(AKXJc), Block([])), (BooleanLit(True), Block([]))], If(StringLit(zmx), Block([For(Id(uQqg), Id(mp), Id(ltbE), Block([])), Break, AssignStmt(ArrayCell(Id(NvP), [BooleanLit(False), Id(x5)]), Id(cTD))])), [(BooleanLit(False), If(NumLit(77.02), Return(BooleanLit(False))), [(BooleanLit(True), Break), (StringLit(wxw), For(Id(L0Yu), StringLit(az), Id(N75p), Break)), (BooleanLit(False), Block([Continue, Return(), CallStmt(Id(en), [StringLit(vr)])])), (Id(HSVL), Return(Id(rR))), (NumLit(61.66), Block([VarDecl(Id(r4O), NumberType, None, None), AssignStmt(Id(Od), StringLit(aXRT)), For(Id(L4), NumLit(57.31), BooleanLit(True), AssignStmt(ArrayCell(Id(xo86), [StringLit(Embe)]), StringLit(tp)))])), (StringLit(M), Return())], Break), (NumLit(16.64), Break), (NumLit(93.16), Continue), (BooleanLit(False), AssignStmt(ArrayCell(Id(gYW), [BooleanLit(True), BooleanLit(False), NumLit(78.41)]), StringLit(eocuv))), (Id(eoK), Return(NumLit(92.27)))], If(NumLit(55.37), Return(NumLit(78.92))), [(StringLit(M), Block([AssignStmt(ArrayCell(Id(Bndd), [NumLit(23.06)]), Id(XBI))]))], AssignStmt(ArrayCell(Id(HZF), [NumLit(81.78)]), Id(DC))), [], None)], None)], None)], None), If(StringLit(Klio), Block([If(NumLit(86.63), AssignStmt(Id(y6I), StringLit(gNTH))), [], Continue])), [(StringLit(CCs), CallStmt(Id(GpU), [NumLit(86.46), BooleanLit(True)])), (StringLit(NBaYO), For(Id(pir), Id(g0Qm), NumLit(10.1), Return()))], CallStmt(Id(Qf), [NumLit(26.0)]), CallStmt(Id(RS5), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115445))

	def test_21530115446(self):
		input = '''
func KOhH (number ES[77.23,12.45], bool AbMC, number uq6[76.85,29.35,80.64])	begin
		return
	end

func BS (bool YZ, string zK42[3.46,0.52])	return true
number JJHk[85.54,37.03,49.27] <- "ucWn"
'''
		expect = '''Program([FuncDecl(Id(KOhH), [VarDecl(Id(ES), ArrayType([77.23, 12.45], NumberType), None, None), VarDecl(Id(AbMC), BoolType, None, None), VarDecl(Id(uq6), ArrayType([76.85, 29.35, 80.64], NumberType), None, None)], Block([Return()])), FuncDecl(Id(BS), [VarDecl(Id(YZ), BoolType, None, None), VarDecl(Id(zK42), ArrayType([3.46, 0.52], StringType), None, None)], Return(BooleanLit(True))), VarDecl(Id(JJHk), ArrayType([85.54, 37.03, 49.27], NumberType), None, StringLit(ucWn))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115446))

	def test_21530115447(self):
		input = '''
func ahoT (string bW[54.62])
	return

bool GjFW
func Te (string mIW[74.0,1.85,50.91])
	return

func GA ()
	begin
		for HS until 12.25 by false
			break
		var gZ8 <- 38.68
		begin
			X30[true] <- true
			for jOIF until "cSkJg" by uzGP
				return "r"
			return
		end
	end
'''
		expect = '''Program([FuncDecl(Id(ahoT), [VarDecl(Id(bW), ArrayType([54.62], StringType), None, None)], Return()), VarDecl(Id(GjFW), BoolType, None, None), FuncDecl(Id(Te), [VarDecl(Id(mIW), ArrayType([74.0, 1.85, 50.91], StringType), None, None)], Return()), FuncDecl(Id(GA), [], Block([For(Id(HS), NumLit(12.25), BooleanLit(False), Break), VarDecl(Id(gZ8), None, var, NumLit(38.68)), Block([AssignStmt(ArrayCell(Id(X30), [BooleanLit(True)]), BooleanLit(True)), For(Id(jOIF), StringLit(cSkJg), Id(uzGP), Return(StringLit(r))), Return()])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115447))

	def test_21530115448(self):
		input = '''
func GZB3 (string mfS[33.25,97.1], string slS)	begin
		return
		bool m125 <- 93.94
		bool TaZV <- "MTSru"
	end

func t1 ()	begin
	end

bool I0_K
func dBz (bool vSo, number Ui)	return k4
'''
		expect = '''Program([FuncDecl(Id(GZB3), [VarDecl(Id(mfS), ArrayType([33.25, 97.1], StringType), None, None), VarDecl(Id(slS), StringType, None, None)], Block([Return(), VarDecl(Id(m125), BoolType, None, NumLit(93.94)), VarDecl(Id(TaZV), BoolType, None, StringLit(MTSru))])), FuncDecl(Id(t1), [], Block([])), VarDecl(Id(I0_K), BoolType, None, None), FuncDecl(Id(dBz), [VarDecl(Id(vSo), BoolType, None, None), VarDecl(Id(Ui), NumberType, None, None)], Return(Id(k4)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115448))

	def test_21530115449(self):
		input = '''
bool y7sR[14.26] <- true
func Dl (bool MC6r[7.81,46.12,15.99], bool UHJ[57.0])	return
number eZMM[48.25] <- false
'''
		expect = '''Program([VarDecl(Id(y7sR), ArrayType([14.26], BoolType), None, BooleanLit(True)), FuncDecl(Id(Dl), [VarDecl(Id(MC6r), ArrayType([7.81, 46.12, 15.99], BoolType), None, None), VarDecl(Id(UHJ), ArrayType([57.0], BoolType), None, None)], Return()), VarDecl(Id(eZMM), ArrayType([48.25], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115449))

	def test_21530115450(self):
		input = '''
func jNq ()	return true
func B0 ()
	return 39.39
func lV ()	return true

func usV (string awz[8.27], bool o9W[29.08,29.51,70.34], number iaGw)	return 76.05
func xLN ()
	begin
		begin
			ko <- 32.2
		end
	end

'''
		expect = '''Program([FuncDecl(Id(jNq), [], Return(BooleanLit(True))), FuncDecl(Id(B0), [], Return(NumLit(39.39))), FuncDecl(Id(lV), [], Return(BooleanLit(True))), FuncDecl(Id(usV), [VarDecl(Id(awz), ArrayType([8.27], StringType), None, None), VarDecl(Id(o9W), ArrayType([29.08, 29.51, 70.34], BoolType), None, None), VarDecl(Id(iaGw), NumberType, None, None)], Return(NumLit(76.05))), FuncDecl(Id(xLN), [], Block([Block([AssignStmt(Id(ko), NumLit(32.2))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115450))

	def test_21530115451(self):
		input = '''
number Bb[11.22] <- false
number rI[64.62,5.21]
func WDDA (number yt[94.91,12.15], number U7, bool rm[82.23,97.47])
	return "PFRTu"
dynamic h09 <- "R"
func Hc (bool YB[28.54], number Du, bool Zl__[4.0])	begin
	end
'''
		expect = '''Program([VarDecl(Id(Bb), ArrayType([11.22], NumberType), None, BooleanLit(False)), VarDecl(Id(rI), ArrayType([64.62, 5.21], NumberType), None, None), FuncDecl(Id(WDDA), [VarDecl(Id(yt), ArrayType([94.91, 12.15], NumberType), None, None), VarDecl(Id(U7), NumberType, None, None), VarDecl(Id(rm), ArrayType([82.23, 97.47], BoolType), None, None)], Return(StringLit(PFRTu))), VarDecl(Id(h09), None, dynamic, StringLit(R)), FuncDecl(Id(Hc), [VarDecl(Id(YB), ArrayType([28.54], BoolType), None, None), VarDecl(Id(Du), NumberType, None, None), VarDecl(Id(Zl__), ArrayType([4.0], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115451))

	def test_21530115452(self):
		input = '''
func fnH5 (bool r2B1)
	return "DZu"

'''
		expect = '''Program([FuncDecl(Id(fnH5), [VarDecl(Id(r2B1), BoolType, None, None)], Return(StringLit(DZu)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115452))

	def test_21530115453(self):
		input = '''
func IN (number qyP[32.46])	return XmE

func YlxW ()
	return "vwXi"

'''
		expect = '''Program([FuncDecl(Id(IN), [VarDecl(Id(qyP), ArrayType([32.46], NumberType), None, None)], Return(Id(XmE))), FuncDecl(Id(YlxW), [], Return(StringLit(vwXi)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115453))

	def test_21530115454(self):
		input = '''
var KFb <- false
'''
		expect = '''Program([VarDecl(Id(KFb), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115454))

	def test_21530115455(self):
		input = '''
func QwA (bool Zar, number Al[78.23])
	begin
		zM9(bi, true, cpnf)
	end
func dp5 ()
	return
func hVWD ()	return

'''
		expect = '''Program([FuncDecl(Id(QwA), [VarDecl(Id(Zar), BoolType, None, None), VarDecl(Id(Al), ArrayType([78.23], NumberType), None, None)], Block([CallStmt(Id(zM9), [Id(bi), BooleanLit(True), Id(cpnf)])])), FuncDecl(Id(dp5), [], Return()), FuncDecl(Id(hVWD), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115455))

	def test_21530115456(self):
		input = '''
number S5[36.67,74.61]
func B4G3 (string k1i, bool X6k, number R9RW[30.66])
	return 32.13
func t7U ()
	return 41.08

'''
		expect = '''Program([VarDecl(Id(S5), ArrayType([36.67, 74.61], NumberType), None, None), FuncDecl(Id(B4G3), [VarDecl(Id(k1i), StringType, None, None), VarDecl(Id(X6k), BoolType, None, None), VarDecl(Id(R9RW), ArrayType([30.66], NumberType), None, None)], Return(NumLit(32.13))), FuncDecl(Id(t7U), [], Return(NumLit(41.08)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115456))

	def test_21530115457(self):
		input = '''
bool UQlv[77.42,65.74] <- "Mvor"
func h0b (string evf8[42.62,85.18,49.6], string Dc[55.19], number Utao[89.51,99.85])
	begin
		if (5.34) break
		elif (16.02)
		begin
		end
		elif (ZSX)
		number Eu <- true
		m7["VPHE", true, l8n1] <- true
	end

number wF_E
'''
		expect = '''Program([VarDecl(Id(UQlv), ArrayType([77.42, 65.74], BoolType), None, StringLit(Mvor)), FuncDecl(Id(h0b), [VarDecl(Id(evf8), ArrayType([42.62, 85.18, 49.6], StringType), None, None), VarDecl(Id(Dc), ArrayType([55.19], StringType), None, None), VarDecl(Id(Utao), ArrayType([89.51, 99.85], NumberType), None, None)], Block([If(NumLit(5.34), Break), [(NumLit(16.02), Block([])), (Id(ZSX), VarDecl(Id(Eu), NumberType, None, BooleanLit(True)))], None, AssignStmt(ArrayCell(Id(m7), [StringLit(VPHE), BooleanLit(True), Id(l8n1)]), BooleanLit(True))])), VarDecl(Id(wF_E), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115457))

	def test_21530115458(self):
		input = '''
func G5h (number TAX[22.36,68.47], number wP5)
	begin
		if (false)
		begin
			for JbZt until 7.31 by "unls"
				continue
			number U6e[75.83,97.95] <- false
			begin
			end
		end
		elif (true) break
		elif ("x")
		continue
		elif (PnrJ)
		return
		elif (true) break
		elif (false)
		if (heD) f0["fEGzx", true] <- true
		elif (false)
		if (37.16)
		dynamic qGe <- 73.02
		elif (true)
		ZDp(80.04)
		elif (qwB) if (AlY)
		if (HLJs) continue
		elif (false)
		if (17.63)
		begin
		end
		elif ("mpBtw")
		Cr3(56.76, "mHS")
		elif (true)
		if (34.61) continue
		elif (muIx)
		begin
			continue
			begin
				if (false) for XB until 51.19 by 86.34
					break
				elif ("kCZs") i5K(vmVt)
				elif (Uc)
				for C7 until "rfdlj" by 16.47
					T4["zPBP", 85.73] <- t6
				elif (true)
				number ZfsM <- false
				elif (ysx)
				begin
					break
					if (TmJ) begin
						ClTH()
						return true
					end
					elif (true) break
					elif (19.59) if (xc7J) begin
						for tz until 25.92 by DMxk
							for LcGo until ltk by "P"
								break
					end
					elif (76.97)
					return
					elif (51.97)
					for TubQ until 16.87 by "UhLq"
						return
					else return "itPO"
					elif ("BSEA") begin
						return qEI
						if (PF)
						if (99.74) Xh[true, "MRX", qpxP] <- true
						elif (true)
						break
						elif (28.81)
						continue
						elif (true) number er <- false
						elif (false) if (aL6) if (U5n0) number W9da[75.73,64.67,84.0] <- hNy_
						else if (sL) Rl <- 95.67
						elif ("TVK")
						Woz(sEy, mLq, 90.9)
						else PsH <- "uk"
						elif (44.64) return
						elif ("mLMx")
						for lsI until jHJ0 by lnZ
							number Bb[70.37,72.37,2.17] <- "j"
						elif (false) break
						elif (26.55)
						fLy(tKuX)
						elif ("nC")
						aCY(tl4, false, false)
						else Myk <- tkL
						elif (true)
						for YyY until true by "QK"
							if (false)
							bool Au[4.35,38.89,82.21] <- false
							elif ("zy") continue
							elif (true) dRVn(58.54, SVkB, Aek)
							elif (false)
							break
							elif (27.17)
							Gs(false, "aXjx")
							elif (70.84) if (false) return
							else begin
							end
							else gX()
						rm(false)
					end
					else string Aa <- "DbyU"
					break
				end
				elif (false)
				for K4R until 37.09 by 47.05
					begin
						v3fG(false)
						bool h4iU[31.32]
						if (Y8fe)
						W1M[35.95] <- 74.88
						elif (93.23) break
						elif (true)
						return
						elif (62.17)
						number m8[45.76,89.28,72.33] <- Ey0
						elif (49.63)
						continue
						elif (sWZ3)
						UNRV[71.56, 30.69] <- EKgP
						else return 24.99
					end
				continue
			end
			break
		end
		elif (29.28)
		bool vt <- "nF"
		elif ("JSst")
		if (MX4V) return
		elif ("Jab")
		BFx["IrMI", 76.53] <- true
		elif (63.99) Qe("LABzc", 61.77, 5.93)
		elif (91.89) continue
		elif (19.86)
		return "tO"
		elif (true) continue
		else SKsm("SZ", "AGB")
		elif (29.15)
		dynamic sXj
		elif ("Nw") begin
			return
		end
		elif (41.11) for o5v until "lwHl" by AJF
			for Ikh until true by false
				TJXL["eI"] <- "MGPg"
		elif (false)
		break
		elif ("kus") for q50 until VaY by Gas
			dW <- "RYjZ"
		else jE(46.44, "au", false)
		elif (ecE) return d4
		else for R8QR until true by 66.31
			dynamic Xpu <- rDv
		if (x8BL)
		break
		elif ("MgV")
		continue
		elif ("rJ") lmF("Wkpjd")
		else return xa
	end

func APBB (number j2k[0.09,96.34,74.13], bool sgyA[70.87,35.37,95.49], string AS[90.25,1.74,23.13])	return
func iO (string Hs[54.02,84.83], bool bi[11.64,71.47,77.39], number I6[31.4,90.2])
	return 49.91
'''
		expect = '''Program([FuncDecl(Id(G5h), [VarDecl(Id(TAX), ArrayType([22.36, 68.47], NumberType), None, None), VarDecl(Id(wP5), NumberType, None, None)], Block([If(BooleanLit(False), Block([For(Id(JbZt), NumLit(7.31), StringLit(unls), Continue), VarDecl(Id(U6e), ArrayType([75.83, 97.95], NumberType), None, BooleanLit(False)), Block([])])), [(BooleanLit(True), Break), (StringLit(x), Continue), (Id(PnrJ), Return()), (BooleanLit(True), Break), (BooleanLit(False), If(Id(heD), AssignStmt(ArrayCell(Id(f0), [StringLit(fEGzx), BooleanLit(True)]), BooleanLit(True))), [(BooleanLit(False), If(NumLit(37.16), VarDecl(Id(qGe), None, dynamic, NumLit(73.02))), [(BooleanLit(True), CallStmt(Id(ZDp), [NumLit(80.04)])), (Id(qwB), If(Id(AlY), If(Id(HLJs), Continue), [(BooleanLit(False), If(NumLit(17.63), Block([])), [(StringLit(mpBtw), CallStmt(Id(Cr3), [NumLit(56.76), StringLit(mHS)])), (BooleanLit(True), If(NumLit(34.61), Continue), [(Id(muIx), Block([Continue, Block([If(BooleanLit(False), For(Id(XB), NumLit(51.19), NumLit(86.34), Break)), [(StringLit(kCZs), CallStmt(Id(i5K), [Id(vmVt)])), (Id(Uc), For(Id(C7), StringLit(rfdlj), NumLit(16.47), AssignStmt(ArrayCell(Id(T4), [StringLit(zPBP), NumLit(85.73)]), Id(t6)))), (BooleanLit(True), VarDecl(Id(ZfsM), NumberType, None, BooleanLit(False))), (Id(ysx), Block([Break, If(Id(TmJ), Block([CallStmt(Id(ClTH), []), Return(BooleanLit(True))])), [(BooleanLit(True), Break), (NumLit(19.59), If(Id(xc7J), Block([For(Id(tz), NumLit(25.92), Id(DMxk), For(Id(LcGo), Id(ltk), StringLit(P), Break))])), [(NumLit(76.97), Return()), (NumLit(51.97), For(Id(TubQ), NumLit(16.87), StringLit(UhLq), Return()))], Return(StringLit(itPO))), (StringLit(BSEA), Block([Return(Id(qEI)), If(Id(PF), If(NumLit(99.74), AssignStmt(ArrayCell(Id(Xh), [BooleanLit(True), StringLit(MRX), Id(qpxP)]), BooleanLit(True))), [(BooleanLit(True), Break), (NumLit(28.81), Continue), (BooleanLit(True), VarDecl(Id(er), NumberType, None, BooleanLit(False))), (BooleanLit(False), If(Id(aL6), If(Id(U5n0), VarDecl(Id(W9da), ArrayType([75.73, 64.67, 84.0], NumberType), None, Id(hNy_))), [], If(Id(sL), AssignStmt(Id(Rl), NumLit(95.67))), [(StringLit(TVK), CallStmt(Id(Woz), [Id(sEy), Id(mLq), NumLit(90.9)]))], AssignStmt(Id(PsH), StringLit(uk))), [(NumLit(44.64), Return()), (StringLit(mLMx), For(Id(lsI), Id(jHJ0), Id(lnZ), VarDecl(Id(Bb), ArrayType([70.37, 72.37, 2.17], NumberType), None, StringLit(j)))), (BooleanLit(False), Break), (NumLit(26.55), CallStmt(Id(fLy), [Id(tKuX)])), (StringLit(nC), CallStmt(Id(aCY), [Id(tl4), BooleanLit(False), BooleanLit(False)]))], AssignStmt(Id(Myk), Id(tkL))), (BooleanLit(True), For(Id(YyY), BooleanLit(True), StringLit(QK), If(BooleanLit(False), VarDecl(Id(Au), ArrayType([4.35, 38.89, 82.21], BoolType), None, BooleanLit(False))), [(StringLit(zy), Continue), (BooleanLit(True), CallStmt(Id(dRVn), [NumLit(58.54), Id(SVkB), Id(Aek)])), (BooleanLit(False), Break), (NumLit(27.17), CallStmt(Id(Gs), [BooleanLit(False), StringLit(aXjx)])), (NumLit(70.84), If(BooleanLit(False), Return()), [], Block([]))], CallStmt(Id(gX), [])))], None), [], None, CallStmt(Id(rm), [BooleanLit(False)])]))], VarDecl(Id(Aa), StringType, None, StringLit(DbyU)), Break])), (BooleanLit(False), For(Id(K4R), NumLit(37.09), NumLit(47.05), Block([CallStmt(Id(v3fG), [BooleanLit(False)]), VarDecl(Id(h4iU), ArrayType([31.32], BoolType), None, None), If(Id(Y8fe), AssignStmt(ArrayCell(Id(W1M), [NumLit(35.95)]), NumLit(74.88))), [(NumLit(93.23), Break), (BooleanLit(True), Return()), (NumLit(62.17), VarDecl(Id(m8), ArrayType([45.76, 89.28, 72.33], NumberType), None, Id(Ey0))), (NumLit(49.63), Continue), (Id(sWZ3), AssignStmt(ArrayCell(Id(UNRV), [NumLit(71.56), NumLit(30.69)]), Id(EKgP)))], Return(NumLit(24.99))])))], None, Continue]), Break])), (NumLit(29.28), VarDecl(Id(vt), BoolType, None, StringLit(nF))), (StringLit(JSst), If(Id(MX4V), Return()), [(StringLit(Jab), AssignStmt(ArrayCell(Id(BFx), [StringLit(IrMI), NumLit(76.53)]), BooleanLit(True))), (NumLit(63.99), CallStmt(Id(Qe), [StringLit(LABzc), NumLit(61.77), NumLit(5.93)])), (NumLit(91.89), Continue), (NumLit(19.86), Return(StringLit(tO))), (BooleanLit(True), Continue)], CallStmt(Id(SKsm), [StringLit(SZ), StringLit(AGB)])), (NumLit(29.15), VarDecl(Id(sXj), None, dynamic, None)), (StringLit(Nw), Block([Return()])), (NumLit(41.11), For(Id(o5v), StringLit(lwHl), Id(AJF), For(Id(Ikh), BooleanLit(True), BooleanLit(False), AssignStmt(ArrayCell(Id(TJXL), [StringLit(eI)]), StringLit(MGPg))))), (BooleanLit(False), Break), (StringLit(kus), For(Id(q50), Id(VaY), Id(Gas), AssignStmt(Id(dW), StringLit(RYjZ))))], CallStmt(Id(jE), [NumLit(46.44), StringLit(au), BooleanLit(False)])), (Id(ecE), Return(Id(d4)))], For(Id(R8QR), BooleanLit(True), NumLit(66.31), VarDecl(Id(Xpu), None, dynamic, Id(rDv))))], None), [], None)], None)], None)], None, If(Id(x8BL), Break), [(StringLit(MgV), Continue), (StringLit(rJ), CallStmt(Id(lmF), [StringLit(Wkpjd)]))], Return(Id(xa))])), FuncDecl(Id(APBB), [VarDecl(Id(j2k), ArrayType([0.09, 96.34, 74.13], NumberType), None, None), VarDecl(Id(sgyA), ArrayType([70.87, 35.37, 95.49], BoolType), None, None), VarDecl(Id(AS), ArrayType([90.25, 1.74, 23.13], StringType), None, None)], Return()), FuncDecl(Id(iO), [VarDecl(Id(Hs), ArrayType([54.02, 84.83], StringType), None, None), VarDecl(Id(bi), ArrayType([11.64, 71.47, 77.39], BoolType), None, None), VarDecl(Id(I6), ArrayType([31.4, 90.2], NumberType), None, None)], Return(NumLit(49.91)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115458))

	def test_21530115459(self):
		input = '''
number IlM[63.31,98.05,57.94] <- "rx"
'''
		expect = '''Program([VarDecl(Id(IlM), ArrayType([63.31, 98.05, 57.94], NumberType), None, StringLit(rx))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115459))

	def test_21530115460(self):
		input = '''
number oPf[23.84,62.96]
'''
		expect = '''Program([VarDecl(Id(oPf), ArrayType([23.84, 62.96], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115460))

	def test_21530115461(self):
		input = '''
func K5I (bool UP[51.42], number Yrwi, number n2[1.45,66.44])
	return

string XVM[62.9,88.19,96.69]
func j0 (number T1h[70.88,3.9], string Hxek[62.26])	return zT3g
'''
		expect = '''Program([FuncDecl(Id(K5I), [VarDecl(Id(UP), ArrayType([51.42], BoolType), None, None), VarDecl(Id(Yrwi), NumberType, None, None), VarDecl(Id(n2), ArrayType([1.45, 66.44], NumberType), None, None)], Return()), VarDecl(Id(XVM), ArrayType([62.9, 88.19, 96.69], StringType), None, None), FuncDecl(Id(j0), [VarDecl(Id(T1h), ArrayType([70.88, 3.9], NumberType), None, None), VarDecl(Id(Hxek), ArrayType([62.26], StringType), None, None)], Return(Id(zT3g)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115461))

	def test_21530115462(self):
		input = '''
bool uf1
number hG9D[25.93,68.31]
'''
		expect = '''Program([VarDecl(Id(uf1), BoolType, None, None), VarDecl(Id(hG9D), ArrayType([25.93, 68.31], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115462))

	def test_21530115463(self):
		input = '''
bool MpyF
number aGw[59.19,17.9]
string tx[50.07,26.28,92.49] <- "q"
'''
		expect = '''Program([VarDecl(Id(MpyF), BoolType, None, None), VarDecl(Id(aGw), ArrayType([59.19, 17.9], NumberType), None, None), VarDecl(Id(tx), ArrayType([50.07, 26.28, 92.49], StringType), None, StringLit(q))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115463))

	def test_21530115464(self):
		input = '''
func Rk (string xysP[66.89,68.15], bool th8f)	begin
		return iFI
	end

func Y2 (bool N8, bool JXs[83.96,86.3], bool so)	begin
	end

number Z9Pe[90.38,21.93,99.01] <- HYO
bool oOpw[61.97,72.15,55.64] <- WQ
'''
		expect = '''Program([FuncDecl(Id(Rk), [VarDecl(Id(xysP), ArrayType([66.89, 68.15], StringType), None, None), VarDecl(Id(th8f), BoolType, None, None)], Block([Return(Id(iFI))])), FuncDecl(Id(Y2), [VarDecl(Id(N8), BoolType, None, None), VarDecl(Id(JXs), ArrayType([83.96, 86.3], BoolType), None, None), VarDecl(Id(so), BoolType, None, None)], Block([])), VarDecl(Id(Z9Pe), ArrayType([90.38, 21.93, 99.01], NumberType), None, Id(HYO)), VarDecl(Id(oOpw), ArrayType([61.97, 72.15, 55.64], BoolType), None, Id(WQ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115464))

	def test_21530115465(self):
		input = '''
func OO (bool mn[19.38,49.66], bool qawt)
	return true
func V9E ()	return SzO5

func ha (number TXIV[69.3,57.21], bool dizl)
	return 39.38
bool Wg[20.4,91.99,44.72] <- true
'''
		expect = '''Program([FuncDecl(Id(OO), [VarDecl(Id(mn), ArrayType([19.38, 49.66], BoolType), None, None), VarDecl(Id(qawt), BoolType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(V9E), [], Return(Id(SzO5))), FuncDecl(Id(ha), [VarDecl(Id(TXIV), ArrayType([69.3, 57.21], NumberType), None, None), VarDecl(Id(dizl), BoolType, None, None)], Return(NumLit(39.38))), VarDecl(Id(Wg), ArrayType([20.4, 91.99, 44.72], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115465))

	def test_21530115466(self):
		input = '''
string kDn <- false
bool Pw[30.3,67.28]
number tr7
'''
		expect = '''Program([VarDecl(Id(kDn), StringType, None, BooleanLit(False)), VarDecl(Id(Pw), ArrayType([30.3, 67.28], BoolType), None, None), VarDecl(Id(tr7), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115466))

	def test_21530115467(self):
		input = '''
number cK
func d5f ()
	begin
		break
		begin
			begin
			end
			s0f8("YJj", "i")
			M7L["o", false] <- 41.11
		end
	end

func MZW6 (number VOh, number pYPQ[55.26])
	begin
		UiP("ztqry", 70.1)
		ewb[false, 62.02] <- 46.08
	end
string DC2r
func yr1T ()	return
'''
		expect = '''Program([VarDecl(Id(cK), NumberType, None, None), FuncDecl(Id(d5f), [], Block([Break, Block([Block([]), CallStmt(Id(s0f8), [StringLit(YJj), StringLit(i)]), AssignStmt(ArrayCell(Id(M7L), [StringLit(o), BooleanLit(False)]), NumLit(41.11))])])), FuncDecl(Id(MZW6), [VarDecl(Id(VOh), NumberType, None, None), VarDecl(Id(pYPQ), ArrayType([55.26], NumberType), None, None)], Block([CallStmt(Id(UiP), [StringLit(ztqry), NumLit(70.1)]), AssignStmt(ArrayCell(Id(ewb), [BooleanLit(False), NumLit(62.02)]), NumLit(46.08))])), VarDecl(Id(DC2r), StringType, None, None), FuncDecl(Id(yr1T), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115467))

	def test_21530115468(self):
		input = '''
func x3xw (string rk3Y[40.04,75.32,20.88], string ZwcZ[7.06,90.56])
	return

func QD (string N55, string qk3[87.79,31.31], string tBo)	return 84.92

dynamic Lb
'''
		expect = '''Program([FuncDecl(Id(x3xw), [VarDecl(Id(rk3Y), ArrayType([40.04, 75.32, 20.88], StringType), None, None), VarDecl(Id(ZwcZ), ArrayType([7.06, 90.56], StringType), None, None)], Return()), FuncDecl(Id(QD), [VarDecl(Id(N55), StringType, None, None), VarDecl(Id(qk3), ArrayType([87.79, 31.31], StringType), None, None), VarDecl(Id(tBo), StringType, None, None)], Return(NumLit(84.92))), VarDecl(Id(Lb), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115468))

	def test_21530115469(self):
		input = '''
func gvnx (string j9Fe, bool CzWQ[71.1,35.36,13.31], bool WY6c[99.92])
	return
dynamic lQ3 <- true
func agSy (string PSRS[49.18,94.43], number cy7, bool Zh[60.16,32.37,28.21])
	return 71.1
'''
		expect = '''Program([FuncDecl(Id(gvnx), [VarDecl(Id(j9Fe), StringType, None, None), VarDecl(Id(CzWQ), ArrayType([71.1, 35.36, 13.31], BoolType), None, None), VarDecl(Id(WY6c), ArrayType([99.92], BoolType), None, None)], Return()), VarDecl(Id(lQ3), None, dynamic, BooleanLit(True)), FuncDecl(Id(agSy), [VarDecl(Id(PSRS), ArrayType([49.18, 94.43], StringType), None, None), VarDecl(Id(cy7), NumberType, None, None), VarDecl(Id(Zh), ArrayType([60.16, 32.37, 28.21], BoolType), None, None)], Return(NumLit(71.1)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115469))

	def test_21530115470(self):
		input = '''
var Xepc <- r7
number v6[96.69,11.52]
var wp4C <- "H"
bool HhI0 <- true
bool ul[21.97,2.1]
'''
		expect = '''Program([VarDecl(Id(Xepc), None, var, Id(r7)), VarDecl(Id(v6), ArrayType([96.69, 11.52], NumberType), None, None), VarDecl(Id(wp4C), None, var, StringLit(H)), VarDecl(Id(HhI0), BoolType, None, BooleanLit(True)), VarDecl(Id(ul), ArrayType([21.97, 2.1], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115470))

	def test_21530115471(self):
		input = '''
func nGp (number NZ6M)
	return 6.61
bool kElk <- noY
bool yIJG[84.34]
func x_OF (string sbf9[16.96,27.58], string dt[1.65])	return true
func qP (number cG, string iM[75.04], string E2L)
	return
'''
		expect = '''Program([FuncDecl(Id(nGp), [VarDecl(Id(NZ6M), NumberType, None, None)], Return(NumLit(6.61))), VarDecl(Id(kElk), BoolType, None, Id(noY)), VarDecl(Id(yIJG), ArrayType([84.34], BoolType), None, None), FuncDecl(Id(x_OF), [VarDecl(Id(sbf9), ArrayType([16.96, 27.58], StringType), None, None), VarDecl(Id(dt), ArrayType([1.65], StringType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(qP), [VarDecl(Id(cG), NumberType, None, None), VarDecl(Id(iM), ArrayType([75.04], StringType), None, None), VarDecl(Id(E2L), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115471))

	def test_21530115472(self):
		input = '''
number LeU
func YY ()	return true

bool CP
string FR[73.82]
func yk3 (bool A3u[82.84,9.13], string T6E[73.96,18.95,66.52], number OSml)
	return LzR

'''
		expect = '''Program([VarDecl(Id(LeU), NumberType, None, None), FuncDecl(Id(YY), [], Return(BooleanLit(True))), VarDecl(Id(CP), BoolType, None, None), VarDecl(Id(FR), ArrayType([73.82], StringType), None, None), FuncDecl(Id(yk3), [VarDecl(Id(A3u), ArrayType([82.84, 9.13], BoolType), None, None), VarDecl(Id(T6E), ArrayType([73.96, 18.95, 66.52], StringType), None, None), VarDecl(Id(OSml), NumberType, None, None)], Return(Id(LzR)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115472))

	def test_21530115473(self):
		input = '''
func KUi (bool q8)	begin
		ji[true, Hrw] <- true
		continue
	end
number quDb[48.63] <- 83.97
string Nh[82.96,77.66,74.33]
func UMZ1 (number dpM[30.07])
	return "lZ"
bool Nu[55.5] <- "K"
'''
		expect = '''Program([FuncDecl(Id(KUi), [VarDecl(Id(q8), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(ji), [BooleanLit(True), Id(Hrw)]), BooleanLit(True)), Continue])), VarDecl(Id(quDb), ArrayType([48.63], NumberType), None, NumLit(83.97)), VarDecl(Id(Nh), ArrayType([82.96, 77.66, 74.33], StringType), None, None), FuncDecl(Id(UMZ1), [VarDecl(Id(dpM), ArrayType([30.07], NumberType), None, None)], Return(StringLit(lZ))), VarDecl(Id(Nu), ArrayType([55.5], BoolType), None, StringLit(K))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115473))

	def test_21530115474(self):
		input = '''
func bex ()	begin
		for y9G until lsg by 48.68
			continue
		if ("u")
		continue
		elif (4.2) if (false)
		for eCqy until 70.11 by true
			i4()
		elif ("msax")
		if (77.26) eYc()
		elif (true) break
		elif (false) F5()
		elif (false) if (89.08)
		continue
		else return 49.89
		else for P5E until "Tqe" by 6.74
			break
		elif (TQyB)
		lAnO[true] <- "AL"
	end

func Pc (string CY25, string k9yp, bool whEq)	return 50.26
func oJ8 ()	return eu
'''
		expect = '''Program([FuncDecl(Id(bex), [], Block([For(Id(y9G), Id(lsg), NumLit(48.68), Continue), If(StringLit(u), Continue), [(NumLit(4.2), If(BooleanLit(False), For(Id(eCqy), NumLit(70.11), BooleanLit(True), CallStmt(Id(i4), []))), [(StringLit(msax), If(NumLit(77.26), CallStmt(Id(eYc), [])), [(BooleanLit(True), Break), (BooleanLit(False), CallStmt(Id(F5), [])), (BooleanLit(False), If(NumLit(89.08), Continue), [], Return(NumLit(49.89)))], For(Id(P5E), StringLit(Tqe), NumLit(6.74), Break)), (Id(TQyB), AssignStmt(ArrayCell(Id(lAnO), [BooleanLit(True)]), StringLit(AL)))], None)], None])), FuncDecl(Id(Pc), [VarDecl(Id(CY25), StringType, None, None), VarDecl(Id(k9yp), StringType, None, None), VarDecl(Id(whEq), BoolType, None, None)], Return(NumLit(50.26))), FuncDecl(Id(oJ8), [], Return(Id(eu)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115474))

	def test_21530115475(self):
		input = '''
func r6RM (number FO[95.52,21.24], string D8BK[89.6,62.31,95.38], string dk)	begin
		dynamic ekXs <- cpb7
		break
		break
	end
bool Te[18.6,23.28,17.51]
func ju (bool c9l[33.56,5.03,60.43])
	return
string rJ[59.77,16.09]
'''
		expect = '''Program([FuncDecl(Id(r6RM), [VarDecl(Id(FO), ArrayType([95.52, 21.24], NumberType), None, None), VarDecl(Id(D8BK), ArrayType([89.6, 62.31, 95.38], StringType), None, None), VarDecl(Id(dk), StringType, None, None)], Block([VarDecl(Id(ekXs), None, dynamic, Id(cpb7)), Break, Break])), VarDecl(Id(Te), ArrayType([18.6, 23.28, 17.51], BoolType), None, None), FuncDecl(Id(ju), [VarDecl(Id(c9l), ArrayType([33.56, 5.03, 60.43], BoolType), None, None)], Return()), VarDecl(Id(rJ), ArrayType([59.77, 16.09], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115475))

	def test_21530115476(self):
		input = '''
func Ek (number Sx1)
	return

number frzN[47.94,61.92,85.38] <- 86.6
var mJlc <- "lcS"
'''
		expect = '''Program([FuncDecl(Id(Ek), [VarDecl(Id(Sx1), NumberType, None, None)], Return()), VarDecl(Id(frzN), ArrayType([47.94, 61.92, 85.38], NumberType), None, NumLit(86.6)), VarDecl(Id(mJlc), None, var, StringLit(lcS))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115476))

	def test_21530115477(self):
		input = '''
number j5a[86.89,52.9]
func cg (number nhy, number fNQJ, string zHp7)
	return false
'''
		expect = '''Program([VarDecl(Id(j5a), ArrayType([86.89, 52.9], NumberType), None, None), FuncDecl(Id(cg), [VarDecl(Id(nhy), NumberType, None, None), VarDecl(Id(fNQJ), NumberType, None, None), VarDecl(Id(zHp7), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115477))

	def test_21530115478(self):
		input = '''
func M2 ()
	begin
		begin
			return Pkr
			Ad[82.08] <- KV3Y
		end
	end
'''
		expect = '''Program([FuncDecl(Id(M2), [], Block([Block([Return(Id(Pkr)), AssignStmt(ArrayCell(Id(Ad), [NumLit(82.08)]), Id(KV3Y))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115478))

	def test_21530115479(self):
		input = '''
func JJ (bool mtN, string EuNl[37.33,73.24])	return
bool tR[10.69] <- 82.45
dynamic goNd
func ZKC (bool xmX, string tAFS, string uY00[26.87,44.94])
	begin
		BIy["xd", 91.63, Lads] <- Uq
		return lcvO
		break
	end
'''
		expect = '''Program([FuncDecl(Id(JJ), [VarDecl(Id(mtN), BoolType, None, None), VarDecl(Id(EuNl), ArrayType([37.33, 73.24], StringType), None, None)], Return()), VarDecl(Id(tR), ArrayType([10.69], BoolType), None, NumLit(82.45)), VarDecl(Id(goNd), None, dynamic, None), FuncDecl(Id(ZKC), [VarDecl(Id(xmX), BoolType, None, None), VarDecl(Id(tAFS), StringType, None, None), VarDecl(Id(uY00), ArrayType([26.87, 44.94], StringType), None, None)], Block([AssignStmt(ArrayCell(Id(BIy), [StringLit(xd), NumLit(91.63), Id(Lads)]), Id(Uq)), Return(Id(lcvO)), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115479))

	def test_21530115480(self):
		input = '''
bool Z6
'''
		expect = '''Program([VarDecl(Id(Z6), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115480))

	def test_21530115481(self):
		input = '''
var HJo <- "QA"
func mX9T (bool nUHX[77.55,31.1,36.53])	begin
		begin
			begin
			end
			for wT until false by 42.02
				begin
					for fHsW until ENK by DX4
						return true
					if (37.37) begin
						return
						var g12q <- VyA
					end
					elif (J8C)
					begin
						begin
						end
						IqT <- "CTy"
						break
					end
					elif (50.02)
					OrK()
					elif (TNYB)
					string HD4 <- 43.21
					elif (32.58)
					if (83.32)
					continue
					elif (vMpO) zM()
					elif (bXl) continue
					elif (nxcf)
					string f0D[33.53,13.41,41.95]
					elif (false)
					return "hZauS"
					elif (BKA)
					return false
				end
			begin
				begin
				end
			end
		end
	end
var xe4 <- 54.46
number Cix7
'''
		expect = '''Program([VarDecl(Id(HJo), None, var, StringLit(QA)), FuncDecl(Id(mX9T), [VarDecl(Id(nUHX), ArrayType([77.55, 31.1, 36.53], BoolType), None, None)], Block([Block([Block([]), For(Id(wT), BooleanLit(False), NumLit(42.02), Block([For(Id(fHsW), Id(ENK), Id(DX4), Return(BooleanLit(True))), If(NumLit(37.37), Block([Return(), VarDecl(Id(g12q), None, var, Id(VyA))])), [(Id(J8C), Block([Block([]), AssignStmt(Id(IqT), StringLit(CTy)), Break])), (NumLit(50.02), CallStmt(Id(OrK), [])), (Id(TNYB), VarDecl(Id(HD4), StringType, None, NumLit(43.21))), (NumLit(32.58), If(NumLit(83.32), Continue), [(Id(vMpO), CallStmt(Id(zM), [])), (Id(bXl), Continue), (Id(nxcf), VarDecl(Id(f0D), ArrayType([33.53, 13.41, 41.95], StringType), None, None)), (BooleanLit(False), Return(StringLit(hZauS))), (Id(BKA), Return(BooleanLit(False)))], None)], None])), Block([Block([])])])])), VarDecl(Id(xe4), None, var, NumLit(54.46)), VarDecl(Id(Cix7), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115481))

	def test_21530115482(self):
		input = '''
func V_ ()
	return
'''
		expect = '''Program([FuncDecl(Id(V_), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115482))

	def test_21530115483(self):
		input = '''
func uTxz ()	return Ds

'''
		expect = '''Program([FuncDecl(Id(uTxz), [], Return(Id(Ds)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115483))

	def test_21530115484(self):
		input = '''
bool D9Q[70.95,25.74]
number B6l[20.51,36.94] <- "HZAbF"
var dsD <- "Z"
func ms (string QUW4, number cf[60.25,3.21], number ehdO[15.65,31.48,98.52])
	begin
		for gGOf until "WZ" by "lu"
			QTi()
	end

'''
		expect = '''Program([VarDecl(Id(D9Q), ArrayType([70.95, 25.74], BoolType), None, None), VarDecl(Id(B6l), ArrayType([20.51, 36.94], NumberType), None, StringLit(HZAbF)), VarDecl(Id(dsD), None, var, StringLit(Z)), FuncDecl(Id(ms), [VarDecl(Id(QUW4), StringType, None, None), VarDecl(Id(cf), ArrayType([60.25, 3.21], NumberType), None, None), VarDecl(Id(ehdO), ArrayType([15.65, 31.48, 98.52], NumberType), None, None)], Block([For(Id(gGOf), StringLit(WZ), StringLit(lu), CallStmt(Id(QTi), []))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115484))

	def test_21530115485(self):
		input = '''
string xH <- true
'''
		expect = '''Program([VarDecl(Id(xH), StringType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115485))

	def test_21530115486(self):
		input = '''
func Ptsk (number SMBg[65.75,98.97])
	return ehqy

number ffT[85.66,93.57] <- 51.73
'''
		expect = '''Program([FuncDecl(Id(Ptsk), [VarDecl(Id(SMBg), ArrayType([65.75, 98.97], NumberType), None, None)], Return(Id(ehqy))), VarDecl(Id(ffT), ArrayType([85.66, 93.57], NumberType), None, NumLit(51.73))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115486))

	def test_21530115487(self):
		input = '''
func mJI (string gvNq)
	return
number HIx8[75.17,40.29]
func Ce_ (number Dw, string n8R[56.74])	return RS0
'''
		expect = '''Program([FuncDecl(Id(mJI), [VarDecl(Id(gvNq), StringType, None, None)], Return()), VarDecl(Id(HIx8), ArrayType([75.17, 40.29], NumberType), None, None), FuncDecl(Id(Ce_), [VarDecl(Id(Dw), NumberType, None, None), VarDecl(Id(n8R), ArrayType([56.74], StringType), None, None)], Return(Id(RS0)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115487))

	def test_21530115488(self):
		input = '''
func c9V ()
	return
func use (bool nkc, bool tKo, string ol5u[63.99,69.84])
	begin
		for y5c until 64.66 by true
			bool tjc
	end

dynamic uqf <- false
var BUp <- ZxtR
func g7 (bool RE4)
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(c9V), [], Return()), FuncDecl(Id(use), [VarDecl(Id(nkc), BoolType, None, None), VarDecl(Id(tKo), BoolType, None, None), VarDecl(Id(ol5u), ArrayType([63.99, 69.84], StringType), None, None)], Block([For(Id(y5c), NumLit(64.66), BooleanLit(True), VarDecl(Id(tjc), BoolType, None, None))])), VarDecl(Id(uqf), None, dynamic, BooleanLit(False)), VarDecl(Id(BUp), None, var, Id(ZxtR)), FuncDecl(Id(g7), [VarDecl(Id(RE4), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115488))

	def test_21530115489(self):
		input = '''
func pZe ()	return ziH

number MEx[17.64,91.59,0.22]
func WrML (number BM1V[8.6,57.47], bool U1[2.76])
	return false
func eUG (string vY4[6.28,45.66], number dj1P[98.06])	return
'''
		expect = '''Program([FuncDecl(Id(pZe), [], Return(Id(ziH))), VarDecl(Id(MEx), ArrayType([17.64, 91.59, 0.22], NumberType), None, None), FuncDecl(Id(WrML), [VarDecl(Id(BM1V), ArrayType([8.6, 57.47], NumberType), None, None), VarDecl(Id(U1), ArrayType([2.76], BoolType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(eUG), [VarDecl(Id(vY4), ArrayType([6.28, 45.66], StringType), None, None), VarDecl(Id(dj1P), ArrayType([98.06], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115489))

	def test_21530115490(self):
		input = '''
func VlbB (bool Kl[33.86,35.48,82.41], bool Lwff)	return 91.83
dynamic nPj <- 96.31
'''
		expect = '''Program([FuncDecl(Id(VlbB), [VarDecl(Id(Kl), ArrayType([33.86, 35.48, 82.41], BoolType), None, None), VarDecl(Id(Lwff), BoolType, None, None)], Return(NumLit(91.83))), VarDecl(Id(nPj), None, dynamic, NumLit(96.31))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115490))

	def test_21530115491(self):
		input = '''
var IgK <- false
func ZJ (bool vKZ0, bool wQ1k[98.16], bool O8V2)	begin
		Sy4l["qg", "xybA", 41.97] <- A0i
		return "nQ"
		continue
	end

func kn_ ()
	begin
		G8["HkPZu"] <- z6g2
		begin
		end
	end
'''
		expect = '''Program([VarDecl(Id(IgK), None, var, BooleanLit(False)), FuncDecl(Id(ZJ), [VarDecl(Id(vKZ0), BoolType, None, None), VarDecl(Id(wQ1k), ArrayType([98.16], BoolType), None, None), VarDecl(Id(O8V2), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(Sy4l), [StringLit(qg), StringLit(xybA), NumLit(41.97)]), Id(A0i)), Return(StringLit(nQ)), Continue])), FuncDecl(Id(kn_), [], Block([AssignStmt(ArrayCell(Id(G8), [StringLit(HkPZu)]), Id(z6g2)), Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115491))

	def test_21530115492(self):
		input = '''
string Qw0[93.98] <- NoP
func m2 (string d5iO[72.88,31.62])	return
func zK1 ()
	return

'''
		expect = '''Program([VarDecl(Id(Qw0), ArrayType([93.98], StringType), None, Id(NoP)), FuncDecl(Id(m2), [VarDecl(Id(d5iO), ArrayType([72.88, 31.62], StringType), None, None)], Return()), FuncDecl(Id(zK1), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115492))

	def test_21530115493(self):
		input = '''
func MA (string Bl2G[54.62], number s8[99.21,88.05])	return

func CGI (number w2xK[99.11,37.0,18.74])
	return

string yZJ[59.05] <- 48.94
func Dm (number CLF9[39.22,86.49,49.76], bool Xy[82.95], string D3r)	begin
		begin
			continue
			return 18.12
		end
	end

'''
		expect = '''Program([FuncDecl(Id(MA), [VarDecl(Id(Bl2G), ArrayType([54.62], StringType), None, None), VarDecl(Id(s8), ArrayType([99.21, 88.05], NumberType), None, None)], Return()), FuncDecl(Id(CGI), [VarDecl(Id(w2xK), ArrayType([99.11, 37.0, 18.74], NumberType), None, None)], Return()), VarDecl(Id(yZJ), ArrayType([59.05], StringType), None, NumLit(48.94)), FuncDecl(Id(Dm), [VarDecl(Id(CLF9), ArrayType([39.22, 86.49, 49.76], NumberType), None, None), VarDecl(Id(Xy), ArrayType([82.95], BoolType), None, None), VarDecl(Id(D3r), StringType, None, None)], Block([Block([Continue, Return(NumLit(18.12))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115493))

	def test_21530115494(self):
		input = '''
var pHSF <- Og
bool FuE[71.88,89.14,25.81]
string Wjfr[34.92,24.4,78.87] <- "tMx"
func QZkc ()	begin
		if (96.11)
		break
		elif (62.7)
		number N7sz <- true
		else for pEo5 until dLe by "VP"
			fc[true] <- "gK"
	end

'''
		expect = '''Program([VarDecl(Id(pHSF), None, var, Id(Og)), VarDecl(Id(FuE), ArrayType([71.88, 89.14, 25.81], BoolType), None, None), VarDecl(Id(Wjfr), ArrayType([34.92, 24.4, 78.87], StringType), None, StringLit(tMx)), FuncDecl(Id(QZkc), [], Block([If(NumLit(96.11), Break), [(NumLit(62.7), VarDecl(Id(N7sz), NumberType, None, BooleanLit(True)))], For(Id(pEo5), Id(dLe), StringLit(VP), AssignStmt(ArrayCell(Id(fc), [BooleanLit(True)]), StringLit(gK)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115494))

	def test_21530115495(self):
		input = '''
number ku
func sYdr (number WQP[93.82,7.42,94.74])
	begin
		string pcI <- PjB
		bpc <- rM8N
		continue
	end
'''
		expect = '''Program([VarDecl(Id(ku), NumberType, None, None), FuncDecl(Id(sYdr), [VarDecl(Id(WQP), ArrayType([93.82, 7.42, 94.74], NumberType), None, None)], Block([VarDecl(Id(pcI), StringType, None, Id(PjB)), AssignStmt(Id(bpc), Id(rM8N)), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115495))

	def test_21530115496(self):
		input = '''
func IB8 ()	return false

'''
		expect = '''Program([FuncDecl(Id(IB8), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115496))

	def test_21530115497(self):
		input = '''
number dzRV
var WM <- 0.7
number ybyz[46.17] <- true
func GZY3 ()
	return
'''
		expect = '''Program([VarDecl(Id(dzRV), NumberType, None, None), VarDecl(Id(WM), None, var, NumLit(0.7)), VarDecl(Id(ybyz), ArrayType([46.17], NumberType), None, BooleanLit(True)), FuncDecl(Id(GZY3), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115497))

	def test_21530115498(self):
		input = '''
func WeLQ (bool Gn, bool Kpj[1.99])	return true
'''
		expect = '''Program([FuncDecl(Id(WeLQ), [VarDecl(Id(Gn), BoolType, None, None), VarDecl(Id(Kpj), ArrayType([1.99], BoolType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115498))

	def test_21530115499(self):
		input = '''
func ks (number TI, string xslh)	return BqhW
'''
		expect = '''Program([FuncDecl(Id(ks), [VarDecl(Id(TI), NumberType, None, None), VarDecl(Id(xslh), StringType, None, None)], Return(Id(BqhW)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115499))

	def test_21530115500(self):
		input = '''
number CW2s <- "kN"
func ZSxw (number tIky[7.56,14.22])
	return

number tbC[55.11,19.42,45.82]
number GO[95.43,19.82] <- 66.53
'''
		expect = '''Program([VarDecl(Id(CW2s), NumberType, None, StringLit(kN)), FuncDecl(Id(ZSxw), [VarDecl(Id(tIky), ArrayType([7.56, 14.22], NumberType), None, None)], Return()), VarDecl(Id(tbC), ArrayType([55.11, 19.42, 45.82], NumberType), None, None), VarDecl(Id(GO), ArrayType([95.43, 19.82], NumberType), None, NumLit(66.53))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115500))

	def test_21530115501(self):
		input = '''
string Vm0D[84.79] <- a4
number wk[86.86]
'''
		expect = '''Program([VarDecl(Id(Vm0D), ArrayType([84.79], StringType), None, Id(a4)), VarDecl(Id(wk), ArrayType([86.86], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115501))

	def test_21530115502(self):
		input = '''
string X_s[33.69,58.25,38.06]
func QVP (number XM3, number dIRT[99.38,32.89])	begin
		for Ipc until XTG by "HM"
			return
	end
string c8S[13.08,57.64] <- 78.96
'''
		expect = '''Program([VarDecl(Id(X_s), ArrayType([33.69, 58.25, 38.06], StringType), None, None), FuncDecl(Id(QVP), [VarDecl(Id(XM3), NumberType, None, None), VarDecl(Id(dIRT), ArrayType([99.38, 32.89], NumberType), None, None)], Block([For(Id(Ipc), Id(XTG), StringLit(HM), Return())])), VarDecl(Id(c8S), ArrayType([13.08, 57.64], StringType), None, NumLit(78.96))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115502))

	def test_21530115503(self):
		input = '''
func z0 (number WV[53.45,54.27])
	return Y2Q

func Ku (string h8uY[70.92,32.24])
	return
func m3 ()
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(z0), [VarDecl(Id(WV), ArrayType([53.45, 54.27], NumberType), None, None)], Return(Id(Y2Q))), FuncDecl(Id(Ku), [VarDecl(Id(h8uY), ArrayType([70.92, 32.24], StringType), None, None)], Return()), FuncDecl(Id(m3), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115503))

	def test_21530115504(self):
		input = '''
func fgdL (bool Nt[81.45], string Rto)	begin
	end
func c6k2 (bool w3qZ[43.21], string Aa, bool bSsf)
	return "NLv"
func ThNs (number ylKq, number YbKE)
	return

number vM[71.03,87.08,62.03] <- true
'''
		expect = '''Program([FuncDecl(Id(fgdL), [VarDecl(Id(Nt), ArrayType([81.45], BoolType), None, None), VarDecl(Id(Rto), StringType, None, None)], Block([])), FuncDecl(Id(c6k2), [VarDecl(Id(w3qZ), ArrayType([43.21], BoolType), None, None), VarDecl(Id(Aa), StringType, None, None), VarDecl(Id(bSsf), BoolType, None, None)], Return(StringLit(NLv))), FuncDecl(Id(ThNs), [VarDecl(Id(ylKq), NumberType, None, None), VarDecl(Id(YbKE), NumberType, None, None)], Return()), VarDecl(Id(vM), ArrayType([71.03, 87.08, 62.03], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115504))

	def test_21530115505(self):
		input = '''
func nYnG (number sp[88.66,25.33], bool Zv[12.33], bool WGyN[60.71])
	return
bool mf[45.52,74.42]
func zh (number iR[28.65], number R5d)	return false

'''
		expect = '''Program([FuncDecl(Id(nYnG), [VarDecl(Id(sp), ArrayType([88.66, 25.33], NumberType), None, None), VarDecl(Id(Zv), ArrayType([12.33], BoolType), None, None), VarDecl(Id(WGyN), ArrayType([60.71], BoolType), None, None)], Return()), VarDecl(Id(mf), ArrayType([45.52, 74.42], BoolType), None, None), FuncDecl(Id(zh), [VarDecl(Id(iR), ArrayType([28.65], NumberType), None, None), VarDecl(Id(R5d), NumberType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115505))

	def test_21530115506(self):
		input = '''
bool tl0[82.04,4.57,14.86] <- Fcq
'''
		expect = '''Program([VarDecl(Id(tl0), ArrayType([82.04, 4.57, 14.86], BoolType), None, Id(Fcq))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115506))

	def test_21530115507(self):
		input = '''
func ai (bool YE[23.85,69.04,12.78])	return 68.68
func NI (string oAtP[66.37])
	begin
		if ("rwSyK") number hm <- true
		return "Ad"
	end

func i9mH (number O8ta, bool TuN, number Z0[75.94,41.38])	begin
		bool L_gX[11.05] <- "P"
		break
	end
string Iz76[14.07] <- "RGQMW"
'''
		expect = '''Program([FuncDecl(Id(ai), [VarDecl(Id(YE), ArrayType([23.85, 69.04, 12.78], BoolType), None, None)], Return(NumLit(68.68))), FuncDecl(Id(NI), [VarDecl(Id(oAtP), ArrayType([66.37], StringType), None, None)], Block([If(StringLit(rwSyK), VarDecl(Id(hm), NumberType, None, BooleanLit(True))), [], None, Return(StringLit(Ad))])), FuncDecl(Id(i9mH), [VarDecl(Id(O8ta), NumberType, None, None), VarDecl(Id(TuN), BoolType, None, None), VarDecl(Id(Z0), ArrayType([75.94, 41.38], NumberType), None, None)], Block([VarDecl(Id(L_gX), ArrayType([11.05], BoolType), None, StringLit(P)), Break])), VarDecl(Id(Iz76), ArrayType([14.07], StringType), None, StringLit(RGQMW))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115507))

	def test_21530115508(self):
		input = '''
func UK (bool eN)	begin
		continue
		begin
			var lh <- false
			for BUk until 98.83 by false
				if ("CUIZb")
				for T7 until false by false
					if (qr5) continue
					elif (hRP) return true
					elif (93.24)
					number pzB[63.16,30.26,14.58]
					elif (false) begin
					end
				elif (true) continue
			Fz[17.06, 9.63, "kMjP"] <- "EQEa"
		end
		eK(37.15, 56.46)
	end
func yfh ()
	begin
	end
func cmC (string Ixw[48.85,61.8], string Wd76)
	begin
		if (97.56)
		for YqTC until 73.45 by lVlH
			if (true)
			string i4[0.22,27.52] <- 58.87
			elif (false)
			return
			elif (cOr)
			dynamic BX
			else begin
				hTyX[43.7, true] <- 40.97
			end
		elif (32.2)
		return
		elif (66.77)
		pob(68.58, p82s)
		elif ("QZSZ") begin
			continue
		end
		elif (4.88) continue
		else string ls5[93.87,7.06,90.49]
		gpP[0.79, Fk, hmp] <- q53
		continue
	end

'''
		expect = '''Program([FuncDecl(Id(UK), [VarDecl(Id(eN), BoolType, None, None)], Block([Continue, Block([VarDecl(Id(lh), None, var, BooleanLit(False)), For(Id(BUk), NumLit(98.83), BooleanLit(False), If(StringLit(CUIZb), For(Id(T7), BooleanLit(False), BooleanLit(False), If(Id(qr5), Continue), [(Id(hRP), Return(BooleanLit(True))), (NumLit(93.24), VarDecl(Id(pzB), ArrayType([63.16, 30.26, 14.58], NumberType), None, None)), (BooleanLit(False), Block([])), (BooleanLit(True), Continue)], None)), [], None), AssignStmt(ArrayCell(Id(Fz), [NumLit(17.06), NumLit(9.63), StringLit(kMjP)]), StringLit(EQEa))]), CallStmt(Id(eK), [NumLit(37.15), NumLit(56.46)])])), FuncDecl(Id(yfh), [], Block([])), FuncDecl(Id(cmC), [VarDecl(Id(Ixw), ArrayType([48.85, 61.8], StringType), None, None), VarDecl(Id(Wd76), StringType, None, None)], Block([If(NumLit(97.56), For(Id(YqTC), NumLit(73.45), Id(lVlH), If(BooleanLit(True), VarDecl(Id(i4), ArrayType([0.22, 27.52], StringType), None, NumLit(58.87))), [(BooleanLit(False), Return()), (Id(cOr), VarDecl(Id(BX), None, dynamic, None))], Block([AssignStmt(ArrayCell(Id(hTyX), [NumLit(43.7), BooleanLit(True)]), NumLit(40.97))]))), [(NumLit(32.2), Return()), (NumLit(66.77), CallStmt(Id(pob), [NumLit(68.58), Id(p82s)])), (StringLit(QZSZ), Block([Continue])), (NumLit(4.88), Continue)], VarDecl(Id(ls5), ArrayType([93.87, 7.06, 90.49], StringType), None, None), AssignStmt(ArrayCell(Id(gpP), [NumLit(0.79), Id(Fk), Id(hmp)]), Id(q53)), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115508))

	def test_21530115509(self):
		input = '''
number Q7Yn[34.03]
func jA (bool Bhk[86.3,41.57,18.44], number zk[94.67,81.59])
	return

dynamic JSE
dynamic Y7 <- "QDqC"
number q08I[73.81,49.36] <- 44.06
'''
		expect = '''Program([VarDecl(Id(Q7Yn), ArrayType([34.03], NumberType), None, None), FuncDecl(Id(jA), [VarDecl(Id(Bhk), ArrayType([86.3, 41.57, 18.44], BoolType), None, None), VarDecl(Id(zk), ArrayType([94.67, 81.59], NumberType), None, None)], Return()), VarDecl(Id(JSE), None, dynamic, None), VarDecl(Id(Y7), None, dynamic, StringLit(QDqC)), VarDecl(Id(q08I), ArrayType([73.81, 49.36], NumberType), None, NumLit(44.06))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115509))

	def test_21530115510(self):
		input = '''
func zI (string OA, number SD, bool Lh[28.25,53.63,12.62])
	return "R"

string bP0v[47.24,54.14,70.2] <- 23.23
var KJH <- false
'''
		expect = '''Program([FuncDecl(Id(zI), [VarDecl(Id(OA), StringType, None, None), VarDecl(Id(SD), NumberType, None, None), VarDecl(Id(Lh), ArrayType([28.25, 53.63, 12.62], BoolType), None, None)], Return(StringLit(R))), VarDecl(Id(bP0v), ArrayType([47.24, 54.14, 70.2], StringType), None, NumLit(23.23)), VarDecl(Id(KJH), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115510))

	def test_21530115511(self):
		input = '''
string N0[2.42,51.59]
func SXX (number Q9, number KV)	return

func G4 (number IM[30.02,80.36,21.77], string x9J7[98.24,79.02])
	begin
	end

'''
		expect = '''Program([VarDecl(Id(N0), ArrayType([2.42, 51.59], StringType), None, None), FuncDecl(Id(SXX), [VarDecl(Id(Q9), NumberType, None, None), VarDecl(Id(KV), NumberType, None, None)], Return()), FuncDecl(Id(G4), [VarDecl(Id(IM), ArrayType([30.02, 80.36, 21.77], NumberType), None, None), VarDecl(Id(x9J7), ArrayType([98.24, 79.02], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115511))

	def test_21530115512(self):
		input = '''
func Uol (number BBG, bool Dj[38.61,87.81,31.42])	begin
	end

bool KZ[45.4]
dynamic fh <- yDaJ
'''
		expect = '''Program([FuncDecl(Id(Uol), [VarDecl(Id(BBG), NumberType, None, None), VarDecl(Id(Dj), ArrayType([38.61, 87.81, 31.42], BoolType), None, None)], Block([])), VarDecl(Id(KZ), ArrayType([45.4], BoolType), None, None), VarDecl(Id(fh), None, dynamic, Id(yDaJ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115512))

	def test_21530115513(self):
		input = '''
func Jaj (bool gtAc, string kG[26.78])
	return

'''
		expect = '''Program([FuncDecl(Id(Jaj), [VarDecl(Id(gtAc), BoolType, None, None), VarDecl(Id(kG), ArrayType([26.78], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115513))

	def test_21530115514(self):
		input = '''
number pHw[42.57,35.07,40.36]
bool NK9W[68.43] <- 25.74
number GOc[93.71,64.49,75.82]
func XS (number NO[72.83], string jd, string BXiS[17.81,37.63])	begin
	end
'''
		expect = '''Program([VarDecl(Id(pHw), ArrayType([42.57, 35.07, 40.36], NumberType), None, None), VarDecl(Id(NK9W), ArrayType([68.43], BoolType), None, NumLit(25.74)), VarDecl(Id(GOc), ArrayType([93.71, 64.49, 75.82], NumberType), None, None), FuncDecl(Id(XS), [VarDecl(Id(NO), ArrayType([72.83], NumberType), None, None), VarDecl(Id(jd), StringType, None, None), VarDecl(Id(BXiS), ArrayType([17.81, 37.63], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115514))

	def test_21530115515(self):
		input = '''
string dX[46.14,29.0]
'''
		expect = '''Program([VarDecl(Id(dX), ArrayType([46.14, 29.0], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115515))

	def test_21530115516(self):
		input = '''
string miE <- false
func Sy (string mJ)
	begin
		number Sa[87.35]
		continue
	end

'''
		expect = '''Program([VarDecl(Id(miE), StringType, None, BooleanLit(False)), FuncDecl(Id(Sy), [VarDecl(Id(mJ), StringType, None, None)], Block([VarDecl(Id(Sa), ArrayType([87.35], NumberType), None, None), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115516))

	def test_21530115517(self):
		input = '''
bool Q_[67.03]
func t1U (bool OyRv, bool Qip[27.63], bool WC[65.18,71.24])	begin
		break
		PkM <- 11.32
		return
	end
bool SuqG[95.06,28.7] <- 64.82
'''
		expect = '''Program([VarDecl(Id(Q_), ArrayType([67.03], BoolType), None, None), FuncDecl(Id(t1U), [VarDecl(Id(OyRv), BoolType, None, None), VarDecl(Id(Qip), ArrayType([27.63], BoolType), None, None), VarDecl(Id(WC), ArrayType([65.18, 71.24], BoolType), None, None)], Block([Break, AssignStmt(Id(PkM), NumLit(11.32)), Return()])), VarDecl(Id(SuqG), ArrayType([95.06, 28.7], BoolType), None, NumLit(64.82))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115517))

	def test_21530115518(self):
		input = '''
var zR <- "M"
number BBY[70.92]
'''
		expect = '''Program([VarDecl(Id(zR), None, var, StringLit(M)), VarDecl(Id(BBY), ArrayType([70.92], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115518))

	def test_21530115519(self):
		input = '''
func i79 ()
	return 96.19
'''
		expect = '''Program([FuncDecl(Id(i79), [], Return(NumLit(96.19)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115519))

	def test_21530115520(self):
		input = '''
string vENc
func bVFR (number YBM[94.08,29.97,67.55], bool dK9[95.52,50.22], bool jg[42.24,15.69])	return
func xV (bool IWct, bool Ms[15.11,50.46,48.14])
	begin
		begin
			if (pCq) if (true)
			continue
			else D3I3 <- 91.7
			elif (H0Dz) for ne until "jiD" by FtS
				g2 <- 33.04
			pyB(TI, 96.36, "n")
		end
	end
number yWCn
'''
		expect = '''Program([VarDecl(Id(vENc), StringType, None, None), FuncDecl(Id(bVFR), [VarDecl(Id(YBM), ArrayType([94.08, 29.97, 67.55], NumberType), None, None), VarDecl(Id(dK9), ArrayType([95.52, 50.22], BoolType), None, None), VarDecl(Id(jg), ArrayType([42.24, 15.69], BoolType), None, None)], Return()), FuncDecl(Id(xV), [VarDecl(Id(IWct), BoolType, None, None), VarDecl(Id(Ms), ArrayType([15.11, 50.46, 48.14], BoolType), None, None)], Block([Block([If(Id(pCq), If(BooleanLit(True), Continue), [], AssignStmt(Id(D3I3), NumLit(91.7))), [(Id(H0Dz), For(Id(ne), StringLit(jiD), Id(FtS), AssignStmt(Id(g2), NumLit(33.04))))], None, CallStmt(Id(pyB), [Id(TI), NumLit(96.36), StringLit(n)])])])), VarDecl(Id(yWCn), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115520))

	def test_21530115521(self):
		input = '''
bool Me[44.98,9.59]
'''
		expect = '''Program([VarDecl(Id(Me), ArrayType([44.98, 9.59], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115521))

	def test_21530115522(self):
		input = '''
func u8 (string Ij3[18.62,42.45])	begin
	end
bool d9ig[24.88,87.21,62.57] <- false
func BAj (string TFb[53.73], bool heeL[9.27], string nIP)
	return
func xW ()
	return
'''
		expect = '''Program([FuncDecl(Id(u8), [VarDecl(Id(Ij3), ArrayType([18.62, 42.45], StringType), None, None)], Block([])), VarDecl(Id(d9ig), ArrayType([24.88, 87.21, 62.57], BoolType), None, BooleanLit(False)), FuncDecl(Id(BAj), [VarDecl(Id(TFb), ArrayType([53.73], StringType), None, None), VarDecl(Id(heeL), ArrayType([9.27], BoolType), None, None), VarDecl(Id(nIP), StringType, None, None)], Return()), FuncDecl(Id(xW), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115522))

	def test_21530115523(self):
		input = '''
string Ll6M[27.13] <- false
dynamic e7ll <- 93.51
'''
		expect = '''Program([VarDecl(Id(Ll6M), ArrayType([27.13], StringType), None, BooleanLit(False)), VarDecl(Id(e7ll), None, dynamic, NumLit(93.51))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115523))

	def test_21530115524(self):
		input = '''
func UKyh (bool bgP4[68.59], bool KWf, string dnt6)	return

func lSi (string Buf)	begin
		if ("YGjs")
		begin
			for eGT until en by bRGM
				begin
					continue
					DM <- false
				end
			break
			begin
				mJqo["HB", 63.85, false] <- false
			end
		end
		else return "IOk"
		Pu_I[true, "YPPeF"] <- false
	end

'''
		expect = '''Program([FuncDecl(Id(UKyh), [VarDecl(Id(bgP4), ArrayType([68.59], BoolType), None, None), VarDecl(Id(KWf), BoolType, None, None), VarDecl(Id(dnt6), StringType, None, None)], Return()), FuncDecl(Id(lSi), [VarDecl(Id(Buf), StringType, None, None)], Block([If(StringLit(YGjs), Block([For(Id(eGT), Id(en), Id(bRGM), Block([Continue, AssignStmt(Id(DM), BooleanLit(False))])), Break, Block([AssignStmt(ArrayCell(Id(mJqo), [StringLit(HB), NumLit(63.85), BooleanLit(False)]), BooleanLit(False))])])), [], Return(StringLit(IOk)), AssignStmt(ArrayCell(Id(Pu_I), [BooleanLit(True), StringLit(YPPeF)]), BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115524))

	def test_21530115525(self):
		input = '''
number Ey[96.85] <- 87.2
func QQA8 (number fGt[50.64,86.67,48.36])	return
func Iw (number DtG[39.81,60.38], number h2y[38.33,59.89,3.65])	return

'''
		expect = '''Program([VarDecl(Id(Ey), ArrayType([96.85], NumberType), None, NumLit(87.2)), FuncDecl(Id(QQA8), [VarDecl(Id(fGt), ArrayType([50.64, 86.67, 48.36], NumberType), None, None)], Return()), FuncDecl(Id(Iw), [VarDecl(Id(DtG), ArrayType([39.81, 60.38], NumberType), None, None), VarDecl(Id(h2y), ArrayType([38.33, 59.89, 3.65], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115525))

	def test_21530115526(self):
		input = '''
bool Cnc <- "HCS"
bool Cf <- "zFz"
func vOw8 ()	return

func H_P ()
	return "LXilz"
number Dwe[49.11,94.53] <- 39.39
'''
		expect = '''Program([VarDecl(Id(Cnc), BoolType, None, StringLit(HCS)), VarDecl(Id(Cf), BoolType, None, StringLit(zFz)), FuncDecl(Id(vOw8), [], Return()), FuncDecl(Id(H_P), [], Return(StringLit(LXilz))), VarDecl(Id(Dwe), ArrayType([49.11, 94.53], NumberType), None, NumLit(39.39))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115526))

	def test_21530115527(self):
		input = '''
func SX (string CY[35.14,35.73], bool ViC[54.46,95.47], bool PtV[68.08])	return
bool NhL[29.57,73.05] <- "Mbt"
func Tc (bool naL2)	return
func XU0g (number eZ)
	return NaZv
func guBE (string SU[98.06,7.66,82.31], number NV[30.21,72.19])	begin
	end

'''
		expect = '''Program([FuncDecl(Id(SX), [VarDecl(Id(CY), ArrayType([35.14, 35.73], StringType), None, None), VarDecl(Id(ViC), ArrayType([54.46, 95.47], BoolType), None, None), VarDecl(Id(PtV), ArrayType([68.08], BoolType), None, None)], Return()), VarDecl(Id(NhL), ArrayType([29.57, 73.05], BoolType), None, StringLit(Mbt)), FuncDecl(Id(Tc), [VarDecl(Id(naL2), BoolType, None, None)], Return()), FuncDecl(Id(XU0g), [VarDecl(Id(eZ), NumberType, None, None)], Return(Id(NaZv))), FuncDecl(Id(guBE), [VarDecl(Id(SU), ArrayType([98.06, 7.66, 82.31], StringType), None, None), VarDecl(Id(NV), ArrayType([30.21, 72.19], NumberType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115527))

	def test_21530115528(self):
		input = '''
bool fu
func TjH (bool Zc, bool OtT, number Ub)	begin
	end

func VQ (string qJBf)	return X94R
string oPXr <- "k"
'''
		expect = '''Program([VarDecl(Id(fu), BoolType, None, None), FuncDecl(Id(TjH), [VarDecl(Id(Zc), BoolType, None, None), VarDecl(Id(OtT), BoolType, None, None), VarDecl(Id(Ub), NumberType, None, None)], Block([])), FuncDecl(Id(VQ), [VarDecl(Id(qJBf), StringType, None, None)], Return(Id(X94R))), VarDecl(Id(oPXr), StringType, None, StringLit(k))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115528))

	def test_21530115529(self):
		input = '''
func nh (number f5N[59.08])	begin
	end
func Yena (bool eyC_, string XVv[12.11,67.97,84.09], string klD)	return false

number CPH[66.29,26.99] <- false
'''
		expect = '''Program([FuncDecl(Id(nh), [VarDecl(Id(f5N), ArrayType([59.08], NumberType), None, None)], Block([])), FuncDecl(Id(Yena), [VarDecl(Id(eyC_), BoolType, None, None), VarDecl(Id(XVv), ArrayType([12.11, 67.97, 84.09], StringType), None, None), VarDecl(Id(klD), StringType, None, None)], Return(BooleanLit(False))), VarDecl(Id(CPH), ArrayType([66.29, 26.99], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115529))

	def test_21530115530(self):
		input = '''
dynamic Zm <- Zn
func rlsf (string aB6, string BF)
	return true

func xze9 (number FGm_, string wQKA, number QgnB[15.6])
	return
func oW2P (number Bam[22.72,35.88])	return

'''
		expect = '''Program([VarDecl(Id(Zm), None, dynamic, Id(Zn)), FuncDecl(Id(rlsf), [VarDecl(Id(aB6), StringType, None, None), VarDecl(Id(BF), StringType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(xze9), [VarDecl(Id(FGm_), NumberType, None, None), VarDecl(Id(wQKA), StringType, None, None), VarDecl(Id(QgnB), ArrayType([15.6], NumberType), None, None)], Return()), FuncDecl(Id(oW2P), [VarDecl(Id(Bam), ArrayType([22.72, 35.88], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115530))

	def test_21530115531(self):
		input = '''
func uDgo (bool TA, string W6V[0.38], number BAJ)	return true
func G_c ()
	return 5.87

var xu <- 17.84
string Ld4[0.33] <- 17.6
'''
		expect = '''Program([FuncDecl(Id(uDgo), [VarDecl(Id(TA), BoolType, None, None), VarDecl(Id(W6V), ArrayType([0.38], StringType), None, None), VarDecl(Id(BAJ), NumberType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(G_c), [], Return(NumLit(5.87))), VarDecl(Id(xu), None, var, NumLit(17.84)), VarDecl(Id(Ld4), ArrayType([0.33], StringType), None, NumLit(17.6))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115531))

	def test_21530115532(self):
		input = '''
func ZkK4 ()	return
'''
		expect = '''Program([FuncDecl(Id(ZkK4), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115532))

	def test_21530115533(self):
		input = '''
number J3[33.67,12.55,17.34]
func bj (bool fQ6[34.52,50.03])	return false
'''
		expect = '''Program([VarDecl(Id(J3), ArrayType([33.67, 12.55, 17.34], NumberType), None, None), FuncDecl(Id(bj), [VarDecl(Id(fQ6), ArrayType([34.52, 50.03], BoolType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115533))

	def test_21530115534(self):
		input = '''
var eHy <- 62.95
number uuh
dynamic BS <- kbu
func es (bool eSP)	return "WEvzi"

'''
		expect = '''Program([VarDecl(Id(eHy), None, var, NumLit(62.95)), VarDecl(Id(uuh), NumberType, None, None), VarDecl(Id(BS), None, dynamic, Id(kbu)), FuncDecl(Id(es), [VarDecl(Id(eSP), BoolType, None, None)], Return(StringLit(WEvzi)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115534))

	def test_21530115535(self):
		input = '''
number Lx2n <- "s"
func y80 (number M0[65.34,22.01])
	begin
		continue
		if (40.55)
		return true
		elif (21.61)
		return Fn
		elif (false) if ("wGmQ") if (false)
		bool ls4Z
		elif ("rET") continue
		elif (false)
		break
		elif ("accXf")
		for APx until "iR" by 94.53
			begin
				continue
				return
			end
		elif ("QfP") for hz until 20.24 by false
			if (TG4) continue
			else string kd <- true
		elif (64.99) if (false)
		OHG <- "msNZs"
		else for RNTA until uU by Plw
			e3f[lQqJ, true, true] <- "uCDg"
		elif (false)
		continue
		elif ("BseN")
		return "E"
		elif (true)
		return false
	end
'''
		expect = '''Program([VarDecl(Id(Lx2n), NumberType, None, StringLit(s)), FuncDecl(Id(y80), [VarDecl(Id(M0), ArrayType([65.34, 22.01], NumberType), None, None)], Block([Continue, If(NumLit(40.55), Return(BooleanLit(True))), [(NumLit(21.61), Return(Id(Fn))), (BooleanLit(False), If(StringLit(wGmQ), If(BooleanLit(False), VarDecl(Id(ls4Z), BoolType, None, None)), [(StringLit(rET), Continue), (BooleanLit(False), Break), (StringLit(accXf), For(Id(APx), StringLit(iR), NumLit(94.53), Block([Continue, Return()]))), (StringLit(QfP), For(Id(hz), NumLit(20.24), BooleanLit(False), If(Id(TG4), Continue), [], VarDecl(Id(kd), StringType, None, BooleanLit(True)))), (NumLit(64.99), If(BooleanLit(False), AssignStmt(Id(OHG), StringLit(msNZs))), [], For(Id(RNTA), Id(uU), Id(Plw), AssignStmt(ArrayCell(Id(e3f), [Id(lQqJ), BooleanLit(True), BooleanLit(True)]), StringLit(uCDg)))), (BooleanLit(False), Continue), (StringLit(BseN), Return(StringLit(E))), (BooleanLit(True), Return(BooleanLit(False)))], None), [], None)], None]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115535))

	def test_21530115536(self):
		input = '''
func z1 (number MCas[53.96,54.87,45.47], string ND0A, string OoV[83.18,89.18,18.53])	begin
	end
'''
		expect = '''Program([FuncDecl(Id(z1), [VarDecl(Id(MCas), ArrayType([53.96, 54.87, 45.47], NumberType), None, None), VarDecl(Id(ND0A), StringType, None, None), VarDecl(Id(OoV), ArrayType([83.18, 89.18, 18.53], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115536))

	def test_21530115537(self):
		input = '''
func g8 (string xep[54.76], bool Pu7, bool m1[63.63])
	return true

bool K5[29.03,1.06] <- "iPk"
func My ()
	begin
		xSxE[true] <- rlg
	end
'''
		expect = '''Program([FuncDecl(Id(g8), [VarDecl(Id(xep), ArrayType([54.76], StringType), None, None), VarDecl(Id(Pu7), BoolType, None, None), VarDecl(Id(m1), ArrayType([63.63], BoolType), None, None)], Return(BooleanLit(True))), VarDecl(Id(K5), ArrayType([29.03, 1.06], BoolType), None, StringLit(iPk)), FuncDecl(Id(My), [], Block([AssignStmt(ArrayCell(Id(xSxE), [BooleanLit(True)]), Id(rlg))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115537))

	def test_21530115538(self):
		input = '''
string fd <- false
func imK (string sJz)
	begin
		for F6or until true by "F"
			bool bsuf <- 6.69
		XK7T <- HG9
		if (true)
		if ("DCDi")
		string sJVF[53.13] <- jwd
		elif (63.25) D6Vj <- 75.81
		elif ("mYb")
		dynamic Ni
	end

string JO2
var sD <- "XnpV"
string iH <- 55.19
'''
		expect = '''Program([VarDecl(Id(fd), StringType, None, BooleanLit(False)), FuncDecl(Id(imK), [VarDecl(Id(sJz), StringType, None, None)], Block([For(Id(F6or), BooleanLit(True), StringLit(F), VarDecl(Id(bsuf), BoolType, None, NumLit(6.69))), AssignStmt(Id(XK7T), Id(HG9)), If(BooleanLit(True), If(StringLit(DCDi), VarDecl(Id(sJVF), ArrayType([53.13], StringType), None, Id(jwd))), [(NumLit(63.25), AssignStmt(Id(D6Vj), NumLit(75.81))), (StringLit(mYb), VarDecl(Id(Ni), None, dynamic, None))], None), [], None])), VarDecl(Id(JO2), StringType, None, None), VarDecl(Id(sD), None, var, StringLit(XnpV)), VarDecl(Id(iH), StringType, None, NumLit(55.19))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115538))

	def test_21530115539(self):
		input = '''
func If (bool yV, bool RgdS[1.73])	return

bool ZM[0.72,66.12,95.55] <- "pUfAV"
number Wym8[95.65,67.87]
dynamic N4 <- false
string alzV[53.21,72.41,99.69]
'''
		expect = '''Program([FuncDecl(Id(If), [VarDecl(Id(yV), BoolType, None, None), VarDecl(Id(RgdS), ArrayType([1.73], BoolType), None, None)], Return()), VarDecl(Id(ZM), ArrayType([0.72, 66.12, 95.55], BoolType), None, StringLit(pUfAV)), VarDecl(Id(Wym8), ArrayType([95.65, 67.87], NumberType), None, None), VarDecl(Id(N4), None, dynamic, BooleanLit(False)), VarDecl(Id(alzV), ArrayType([53.21, 72.41, 99.69], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115539))

	def test_21530115540(self):
		input = '''
func TP (number xI, bool fJrn, bool sEYo)	return
bool b1Z
func gN (string qI, string gDF3)	return
func SM (bool WF[61.78], bool FEQ7)
	begin
	end

var YjzK <- 5.96
'''
		expect = '''Program([FuncDecl(Id(TP), [VarDecl(Id(xI), NumberType, None, None), VarDecl(Id(fJrn), BoolType, None, None), VarDecl(Id(sEYo), BoolType, None, None)], Return()), VarDecl(Id(b1Z), BoolType, None, None), FuncDecl(Id(gN), [VarDecl(Id(qI), StringType, None, None), VarDecl(Id(gDF3), StringType, None, None)], Return()), FuncDecl(Id(SM), [VarDecl(Id(WF), ArrayType([61.78], BoolType), None, None), VarDecl(Id(FEQ7), BoolType, None, None)], Block([])), VarDecl(Id(YjzK), None, var, NumLit(5.96))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115540))

	def test_21530115541(self):
		input = '''
string MdYg
bool Es[91.2]
func dHB (number yk[5.18], bool jw4F, bool Dn[31.26])
	return vlzh

'''
		expect = '''Program([VarDecl(Id(MdYg), StringType, None, None), VarDecl(Id(Es), ArrayType([91.2], BoolType), None, None), FuncDecl(Id(dHB), [VarDecl(Id(yk), ArrayType([5.18], NumberType), None, None), VarDecl(Id(jw4F), BoolType, None, None), VarDecl(Id(Dn), ArrayType([31.26], BoolType), None, None)], Return(Id(vlzh)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115541))

	def test_21530115542(self):
		input = '''
var gSZ <- true
func HCQ (bool RL0, bool YC6E[0.3,23.63], number aNG[64.39,31.29])
	return 19.11

func lZy2 (string XFs, string aYz[61.77,12.17,56.93], bool WO)
	return

'''
		expect = '''Program([VarDecl(Id(gSZ), None, var, BooleanLit(True)), FuncDecl(Id(HCQ), [VarDecl(Id(RL0), BoolType, None, None), VarDecl(Id(YC6E), ArrayType([0.3, 23.63], BoolType), None, None), VarDecl(Id(aNG), ArrayType([64.39, 31.29], NumberType), None, None)], Return(NumLit(19.11))), FuncDecl(Id(lZy2), [VarDecl(Id(XFs), StringType, None, None), VarDecl(Id(aYz), ArrayType([61.77, 12.17, 56.93], StringType), None, None), VarDecl(Id(WO), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115542))

	def test_21530115543(self):
		input = '''
number hW[96.85]
number vpH[53.29,48.78]
func zd ()
	begin
		if (true)
		vR[false, 75.13, "QtKA"] <- true
		else break
	end
string CB[9.04] <- "nJ"
dynamic Nq6
'''
		expect = '''Program([VarDecl(Id(hW), ArrayType([96.85], NumberType), None, None), VarDecl(Id(vpH), ArrayType([53.29, 48.78], NumberType), None, None), FuncDecl(Id(zd), [], Block([If(BooleanLit(True), AssignStmt(ArrayCell(Id(vR), [BooleanLit(False), NumLit(75.13), StringLit(QtKA)]), BooleanLit(True))), [], Break])), VarDecl(Id(CB), ArrayType([9.04], StringType), None, StringLit(nJ)), VarDecl(Id(Nq6), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115543))

	def test_21530115544(self):
		input = '''
number pZ <- fq
func XR5 (bool ZXs, bool cpW, bool j98)
	begin
		break
		return
		number igPS[47.45,69.24,89.72] <- true
	end
bool XCao[67.65,36.86,38.13] <- false
bool EsT[14.02,47.42] <- 77.99
func HqJ ()	begin
	end

'''
		expect = '''Program([VarDecl(Id(pZ), NumberType, None, Id(fq)), FuncDecl(Id(XR5), [VarDecl(Id(ZXs), BoolType, None, None), VarDecl(Id(cpW), BoolType, None, None), VarDecl(Id(j98), BoolType, None, None)], Block([Break, Return(), VarDecl(Id(igPS), ArrayType([47.45, 69.24, 89.72], NumberType), None, BooleanLit(True))])), VarDecl(Id(XCao), ArrayType([67.65, 36.86, 38.13], BoolType), None, BooleanLit(False)), VarDecl(Id(EsT), ArrayType([14.02, 47.42], BoolType), None, NumLit(77.99)), FuncDecl(Id(HqJ), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115544))

	def test_21530115545(self):
		input = '''
func IES (number Iqo, bool e0[3.0,25.48,0.69], bool T4xG[20.05])
	begin
		string H5EH
		number HOt[81.1,31.73,87.2]
	end

dynamic PlP <- "imC"
'''
		expect = '''Program([FuncDecl(Id(IES), [VarDecl(Id(Iqo), NumberType, None, None), VarDecl(Id(e0), ArrayType([3.0, 25.48, 0.69], BoolType), None, None), VarDecl(Id(T4xG), ArrayType([20.05], BoolType), None, None)], Block([VarDecl(Id(H5EH), StringType, None, None), VarDecl(Id(HOt), ArrayType([81.1, 31.73, 87.2], NumberType), None, None)])), VarDecl(Id(PlP), None, dynamic, StringLit(imC))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115545))

	def test_21530115546(self):
		input = '''
func xa9 (number cR, string wfW, number AkVV)	return

bool VHiE
'''
		expect = '''Program([FuncDecl(Id(xa9), [VarDecl(Id(cR), NumberType, None, None), VarDecl(Id(wfW), StringType, None, None), VarDecl(Id(AkVV), NumberType, None, None)], Return()), VarDecl(Id(VHiE), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115546))

	def test_21530115547(self):
		input = '''
func oK (bool US)	begin
	end
func mkD4 (bool DTrB[25.06], number vqd, number N0r)
	return DF

number JME
'''
		expect = '''Program([FuncDecl(Id(oK), [VarDecl(Id(US), BoolType, None, None)], Block([])), FuncDecl(Id(mkD4), [VarDecl(Id(DTrB), ArrayType([25.06], BoolType), None, None), VarDecl(Id(vqd), NumberType, None, None), VarDecl(Id(N0r), NumberType, None, None)], Return(Id(DF))), VarDecl(Id(JME), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115547))

	def test_21530115548(self):
		input = '''
func b1sy (number wncZ[48.26,93.91], number X1d[72.37,40.21])
	return
'''
		expect = '''Program([FuncDecl(Id(b1sy), [VarDecl(Id(wncZ), ArrayType([48.26, 93.91], NumberType), None, None), VarDecl(Id(X1d), ArrayType([72.37, 40.21], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115548))

	def test_21530115549(self):
		input = '''
bool Um[72.81,11.52]
'''
		expect = '''Program([VarDecl(Id(Um), ArrayType([72.81, 11.52], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115549))

	def test_21530115550(self):
		input = '''
bool UXsq[46.19,23.12,22.02]
bool kawX[66.27,7.08] <- qc7D
func wGNE (bool sphB, bool yW[45.44])
	return
number Gd
func olV4 (string k3[64.97,88.68,8.89], number y63h)	return
'''
		expect = '''Program([VarDecl(Id(UXsq), ArrayType([46.19, 23.12, 22.02], BoolType), None, None), VarDecl(Id(kawX), ArrayType([66.27, 7.08], BoolType), None, Id(qc7D)), FuncDecl(Id(wGNE), [VarDecl(Id(sphB), BoolType, None, None), VarDecl(Id(yW), ArrayType([45.44], BoolType), None, None)], Return()), VarDecl(Id(Gd), NumberType, None, None), FuncDecl(Id(olV4), [VarDecl(Id(k3), ArrayType([64.97, 88.68, 8.89], StringType), None, None), VarDecl(Id(y63h), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115550))

	def test_21530115551(self):
		input = '''
bool I61l[77.99,16.62,39.31] <- SrK
func uFA (string Gb, string kzV, bool VgA[24.68,44.09])	return

func jZIW (number CFi)
	begin
	end
func hwq (number BPUS, bool U4m[48.26], string Yf6L[48.68,74.86])
	return

'''
		expect = '''Program([VarDecl(Id(I61l), ArrayType([77.99, 16.62, 39.31], BoolType), None, Id(SrK)), FuncDecl(Id(uFA), [VarDecl(Id(Gb), StringType, None, None), VarDecl(Id(kzV), StringType, None, None), VarDecl(Id(VgA), ArrayType([24.68, 44.09], BoolType), None, None)], Return()), FuncDecl(Id(jZIW), [VarDecl(Id(CFi), NumberType, None, None)], Block([])), FuncDecl(Id(hwq), [VarDecl(Id(BPUS), NumberType, None, None), VarDecl(Id(U4m), ArrayType([48.26], BoolType), None, None), VarDecl(Id(Yf6L), ArrayType([48.68, 74.86], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115551))

	def test_21530115552(self):
		input = '''
func BOKu (bool CGk, bool tG)
	return 93.81
string tAer[19.02,63.95] <- false
func l7 (bool Y9i, string vTO[71.62,44.81])	return true
func jqo (bool lx8k[61.94,71.48])
	return 55.95

number d_ <- true
'''
		expect = '''Program([FuncDecl(Id(BOKu), [VarDecl(Id(CGk), BoolType, None, None), VarDecl(Id(tG), BoolType, None, None)], Return(NumLit(93.81))), VarDecl(Id(tAer), ArrayType([19.02, 63.95], StringType), None, BooleanLit(False)), FuncDecl(Id(l7), [VarDecl(Id(Y9i), BoolType, None, None), VarDecl(Id(vTO), ArrayType([71.62, 44.81], StringType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(jqo), [VarDecl(Id(lx8k), ArrayType([61.94, 71.48], BoolType), None, None)], Return(NumLit(55.95))), VarDecl(Id(d_), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115552))

	def test_21530115553(self):
		input = '''
func dipv (bool Mf[29.04], string s4nJ[43.17,45.05])	return
func gu (number OJY1[25.69,48.88,65.44])
	return SA00

number QQ <- MU47
func sr (string ysf, bool oW, number h5Qy)	return 43.22
func gP8 ()
	begin
		dynamic s72 <- 58.77
		aFa("eArS", O9M, 65.55)
	end

'''
		expect = '''Program([FuncDecl(Id(dipv), [VarDecl(Id(Mf), ArrayType([29.04], BoolType), None, None), VarDecl(Id(s4nJ), ArrayType([43.17, 45.05], StringType), None, None)], Return()), FuncDecl(Id(gu), [VarDecl(Id(OJY1), ArrayType([25.69, 48.88, 65.44], NumberType), None, None)], Return(Id(SA00))), VarDecl(Id(QQ), NumberType, None, Id(MU47)), FuncDecl(Id(sr), [VarDecl(Id(ysf), StringType, None, None), VarDecl(Id(oW), BoolType, None, None), VarDecl(Id(h5Qy), NumberType, None, None)], Return(NumLit(43.22))), FuncDecl(Id(gP8), [], Block([VarDecl(Id(s72), None, dynamic, NumLit(58.77)), CallStmt(Id(aFa), [StringLit(eArS), Id(O9M), NumLit(65.55)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115553))

	def test_21530115554(self):
		input = '''
func Nn (string XO_D[35.79], string Js[30.16,82.29,14.39])
	return

func wQn (bool Hp_[40.59])
	begin
		begin
			if (dr) return "CxEpK"
			elif (92.48)
			rjd[12.62, 8.01] <- DOc
			elif (false)
			return
			else continue
		end
	end

bool exi
func g5l (string mfCy, bool vq[17.76,26.15,56.99])
	return 11.01

'''
		expect = '''Program([FuncDecl(Id(Nn), [VarDecl(Id(XO_D), ArrayType([35.79], StringType), None, None), VarDecl(Id(Js), ArrayType([30.16, 82.29, 14.39], StringType), None, None)], Return()), FuncDecl(Id(wQn), [VarDecl(Id(Hp_), ArrayType([40.59], BoolType), None, None)], Block([Block([If(Id(dr), Return(StringLit(CxEpK))), [(NumLit(92.48), AssignStmt(ArrayCell(Id(rjd), [NumLit(12.62), NumLit(8.01)]), Id(DOc))), (BooleanLit(False), Return())], Continue])])), VarDecl(Id(exi), BoolType, None, None), FuncDecl(Id(g5l), [VarDecl(Id(mfCy), StringType, None, None), VarDecl(Id(vq), ArrayType([17.76, 26.15, 56.99], BoolType), None, None)], Return(NumLit(11.01)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115554))

	def test_21530115555(self):
		input = '''
func ycH0 (number lKJ, number zn)	return
bool Gsg <- Lo
dynamic lmF
string m5[55.07]
'''
		expect = '''Program([FuncDecl(Id(ycH0), [VarDecl(Id(lKJ), NumberType, None, None), VarDecl(Id(zn), NumberType, None, None)], Return()), VarDecl(Id(Gsg), BoolType, None, Id(Lo)), VarDecl(Id(lmF), None, dynamic, None), VarDecl(Id(m5), ArrayType([55.07], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115555))

	def test_21530115556(self):
		input = '''
func vHr (bool Fxn_)	begin
		begin
		end
		begin
			E0XT <- 59.19
		end
	end
number vK <- false
number A9rI[20.99,57.24,80.39] <- true
'''
		expect = '''Program([FuncDecl(Id(vHr), [VarDecl(Id(Fxn_), BoolType, None, None)], Block([Block([]), Block([AssignStmt(Id(E0XT), NumLit(59.19))])])), VarDecl(Id(vK), NumberType, None, BooleanLit(False)), VarDecl(Id(A9rI), ArrayType([20.99, 57.24, 80.39], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115556))

	def test_21530115557(self):
		input = '''
string O9a
bool eeL
'''
		expect = '''Program([VarDecl(Id(O9a), StringType, None, None), VarDecl(Id(eeL), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115557))

	def test_21530115558(self):
		input = '''
func yMDh ()	return false

number Gu[49.06] <- "c"
dynamic qdbn
func Q25 ()	return 28.9
'''
		expect = '''Program([FuncDecl(Id(yMDh), [], Return(BooleanLit(False))), VarDecl(Id(Gu), ArrayType([49.06], NumberType), None, StringLit(c)), VarDecl(Id(qdbn), None, dynamic, None), FuncDecl(Id(Q25), [], Return(NumLit(28.9)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115558))

	def test_21530115559(self):
		input = '''
string gil <- false
number TjXh[12.93,86.62] <- fH
func WC (bool ZiVu[70.68,9.0,49.97], bool GDMT)
	return
func gc ()
	return
'''
		expect = '''Program([VarDecl(Id(gil), StringType, None, BooleanLit(False)), VarDecl(Id(TjXh), ArrayType([12.93, 86.62], NumberType), None, Id(fH)), FuncDecl(Id(WC), [VarDecl(Id(ZiVu), ArrayType([70.68, 9.0, 49.97], BoolType), None, None), VarDecl(Id(GDMT), BoolType, None, None)], Return()), FuncDecl(Id(gc), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115559))

	def test_21530115560(self):
		input = '''
func qRFN (number Ny[11.82,61.0,65.87], number zHBk, string V_W[13.82])	return "jeTS"
string eGC[24.57,65.23,37.19] <- sUju
dynamic xEED <- "B"
func xD01 ()	return
'''
		expect = '''Program([FuncDecl(Id(qRFN), [VarDecl(Id(Ny), ArrayType([11.82, 61.0, 65.87], NumberType), None, None), VarDecl(Id(zHBk), NumberType, None, None), VarDecl(Id(V_W), ArrayType([13.82], StringType), None, None)], Return(StringLit(jeTS))), VarDecl(Id(eGC), ArrayType([24.57, 65.23, 37.19], StringType), None, Id(sUju)), VarDecl(Id(xEED), None, dynamic, StringLit(B)), FuncDecl(Id(xD01), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115560))

	def test_21530115561(self):
		input = '''
string rkc <- false
'''
		expect = '''Program([VarDecl(Id(rkc), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115561))

	def test_21530115562(self):
		input = '''
func s9 ()
	begin
		for Nje3 until 82.27 by NNyD
			continue
		continue
	end
string TQKe <- 14.34
'''
		expect = '''Program([FuncDecl(Id(s9), [], Block([For(Id(Nje3), NumLit(82.27), Id(NNyD), Continue), Continue])), VarDecl(Id(TQKe), StringType, None, NumLit(14.34))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115562))

	def test_21530115563(self):
		input = '''
func hje (string gcDt)	return iQI
string in[95.75,74.32] <- "N"
string M47[25.77] <- "z"
func ec (string moF)	return "CDL"
'''
		expect = '''Program([FuncDecl(Id(hje), [VarDecl(Id(gcDt), StringType, None, None)], Return(Id(iQI))), VarDecl(Id(in), ArrayType([95.75, 74.32], StringType), None, StringLit(N)), VarDecl(Id(M47), ArrayType([25.77], StringType), None, StringLit(z)), FuncDecl(Id(ec), [VarDecl(Id(moF), StringType, None, None)], Return(StringLit(CDL)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115563))

	def test_21530115564(self):
		input = '''
dynamic P4w
dynamic ELOw
func c0ci ()
	begin
		EkA <- OY
		var Bs <- true
	end
'''
		expect = '''Program([VarDecl(Id(P4w), None, dynamic, None), VarDecl(Id(ELOw), None, dynamic, None), FuncDecl(Id(c0ci), [], Block([AssignStmt(Id(EkA), Id(OY)), VarDecl(Id(Bs), None, var, BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115564))

	def test_21530115565(self):
		input = '''
number dMl[99.94] <- false
'''
		expect = '''Program([VarDecl(Id(dMl), ArrayType([99.94], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115565))

	def test_21530115566(self):
		input = '''
bool e_ti[47.37,14.43] <- false
'''
		expect = '''Program([VarDecl(Id(e_ti), ArrayType([47.37, 14.43], BoolType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115566))

	def test_21530115567(self):
		input = '''
func E5H (bool Wu, number MnWN[2.35], string E2q)	return

func m7mU (bool S3, number OYle[23.08], number KSh)
	return

'''
		expect = '''Program([FuncDecl(Id(E5H), [VarDecl(Id(Wu), BoolType, None, None), VarDecl(Id(MnWN), ArrayType([2.35], NumberType), None, None), VarDecl(Id(E2q), StringType, None, None)], Return()), FuncDecl(Id(m7mU), [VarDecl(Id(S3), BoolType, None, None), VarDecl(Id(OYle), ArrayType([23.08], NumberType), None, None), VarDecl(Id(KSh), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115567))

	def test_21530115568(self):
		input = '''
func mIep (string VCew)
	begin
		number mRN[24.09,48.69,10.92]
		for PW until Dl by "CnMVg"
			number xRO[32.67,34.34,12.57]
		string NUC[64.52,23.28,17.2] <- "s"
	end

func In1 ()	return "dkDnD"
func Xr ()	return
'''
		expect = '''Program([FuncDecl(Id(mIep), [VarDecl(Id(VCew), StringType, None, None)], Block([VarDecl(Id(mRN), ArrayType([24.09, 48.69, 10.92], NumberType), None, None), For(Id(PW), Id(Dl), StringLit(CnMVg), VarDecl(Id(xRO), ArrayType([32.67, 34.34, 12.57], NumberType), None, None)), VarDecl(Id(NUC), ArrayType([64.52, 23.28, 17.2], StringType), None, StringLit(s))])), FuncDecl(Id(In1), [], Return(StringLit(dkDnD))), FuncDecl(Id(Xr), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115568))

	def test_21530115569(self):
		input = '''
func wnP (string vdt[40.59,73.77,35.76])
	return kx
func fb4 (bool wCx)	return 43.17

func mRF (string tZS, bool vBQc[16.86,42.58])	begin
	end
bool zY[5.22]
func N8GH ()
	begin
		Wv_[ISTZ, true] <- false
	end
'''
		expect = '''Program([FuncDecl(Id(wnP), [VarDecl(Id(vdt), ArrayType([40.59, 73.77, 35.76], StringType), None, None)], Return(Id(kx))), FuncDecl(Id(fb4), [VarDecl(Id(wCx), BoolType, None, None)], Return(NumLit(43.17))), FuncDecl(Id(mRF), [VarDecl(Id(tZS), StringType, None, None), VarDecl(Id(vBQc), ArrayType([16.86, 42.58], BoolType), None, None)], Block([])), VarDecl(Id(zY), ArrayType([5.22], BoolType), None, None), FuncDecl(Id(N8GH), [], Block([AssignStmt(ArrayCell(Id(Wv_), [Id(ISTZ), BooleanLit(True)]), BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115569))

	def test_21530115570(self):
		input = '''
func OmT (bool Ail[10.5], number ElD, string YIX[12.98,6.38])
	return true

func Cp7 (string h6pz[39.31,83.85], bool CS[61.23])	return Xc

number VPK[18.74,61.21] <- 75.16
number xd[21.62]
'''
		expect = '''Program([FuncDecl(Id(OmT), [VarDecl(Id(Ail), ArrayType([10.5], BoolType), None, None), VarDecl(Id(ElD), NumberType, None, None), VarDecl(Id(YIX), ArrayType([12.98, 6.38], StringType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(Cp7), [VarDecl(Id(h6pz), ArrayType([39.31, 83.85], StringType), None, None), VarDecl(Id(CS), ArrayType([61.23], BoolType), None, None)], Return(Id(Xc))), VarDecl(Id(VPK), ArrayType([18.74, 61.21], NumberType), None, NumLit(75.16)), VarDecl(Id(xd), ArrayType([21.62], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115570))

	def test_21530115571(self):
		input = '''
func ZC (number z5[11.71,43.84,30.06], number vwj[97.44])	begin
		if ("SLE")
		dynamic clr2
		elif (Zp)
		if (true) break
		elif (73.88) begin
			continue
			begin
				if (9.15) begin
				end
				elif ("v") continue
				elif (99.79)
				if (14.23)
				continue
				elif (Yvh4) string e0aZ[66.5]
				elif ("Z")
				bool qhwq <- "m"
				elif (true) bool CJ <- false
				elif (46.6)
				break
				elif ("o")
				if (23.82) begin
					string dV[4.37,43.14,10.42] <- rCHJ
					begin
						aT("iFqa", "LGz")
						if (nVT) continue
						elif ("in")
						begin
							for jR47 until true by "uaS"
								continue
							return
						end
						continue
					end
				end
				elif (13.41) if (Lt)
				for i1 until "nE" by true
					break
				elif (true) break
				elif (Xcvr) begin
				end
				elif (IL)
				bool G8
				elif (wUq)
				for L7 until false by hbwE
					bool B9[3.93,68.22] <- true
				else break
				elif (false) T0h[false, 27.42] <- 79.16
				elif (EW_P) loi(false, "uXEs", "LzL")
				elif ("DcY") break
				else return false
				if ("FBXDv")
				return
				elif (99.25)
				for eCJ until true by nsE
					begin
						for faf until "Jig" by 87.75
							return
						J2hd(63.32)
					end
				break
			end
			lovP <- "IlyJD"
		end
		elif (XDwq)
		K0lT <- 51.22
		elif (yA)
		if ("cgyj") if (26.6)
		return "df"
		elif (73.56)
		break
		else t7wZ(80.47)
		else break
		elif (V6G) for D7Cg until false by "CP"
			break
		elif ("t") sjPK <- "qCgJ"
		elif (wR4a)
		l2mh[true, false, oH] <- XM
	end
var XJzd <- sQ
bool Gb <- kjk
'''
		expect = '''Program([FuncDecl(Id(ZC), [VarDecl(Id(z5), ArrayType([11.71, 43.84, 30.06], NumberType), None, None), VarDecl(Id(vwj), ArrayType([97.44], NumberType), None, None)], Block([If(StringLit(SLE), VarDecl(Id(clr2), None, dynamic, None)), [(Id(Zp), If(BooleanLit(True), Break), [(NumLit(73.88), Block([Continue, Block([If(NumLit(9.15), Block([])), [(StringLit(v), Continue), (NumLit(99.79), If(NumLit(14.23), Continue), [(Id(Yvh4), VarDecl(Id(e0aZ), ArrayType([66.5], StringType), None, None)), (StringLit(Z), VarDecl(Id(qhwq), BoolType, None, StringLit(m))), (BooleanLit(True), VarDecl(Id(CJ), BoolType, None, BooleanLit(False))), (NumLit(46.6), Break), (StringLit(o), If(NumLit(23.82), Block([VarDecl(Id(dV), ArrayType([4.37, 43.14, 10.42], StringType), None, Id(rCHJ)), Block([CallStmt(Id(aT), [StringLit(iFqa), StringLit(LGz)]), If(Id(nVT), Continue), [(StringLit(in), Block([For(Id(jR47), BooleanLit(True), StringLit(uaS), Continue), Return()]))], None, Continue])])), [(NumLit(13.41), If(Id(Lt), For(Id(i1), StringLit(nE), BooleanLit(True), Break)), [(BooleanLit(True), Break), (Id(Xcvr), Block([])), (Id(IL), VarDecl(Id(G8), BoolType, None, None)), (Id(wUq), For(Id(L7), BooleanLit(False), Id(hbwE), VarDecl(Id(B9), ArrayType([3.93, 68.22], BoolType), None, BooleanLit(True))))], Break), (BooleanLit(False), AssignStmt(ArrayCell(Id(T0h), [BooleanLit(False), NumLit(27.42)]), NumLit(79.16))), (Id(EW_P), CallStmt(Id(loi), [BooleanLit(False), StringLit(uXEs), StringLit(LzL)])), (StringLit(DcY), Break)], Return(BooleanLit(False)))], None)], None, If(StringLit(FBXDv), Return()), [(NumLit(99.25), For(Id(eCJ), BooleanLit(True), Id(nsE), Block([For(Id(faf), StringLit(Jig), NumLit(87.75), Return()), CallStmt(Id(J2hd), [NumLit(63.32)])])))], None, Break]), AssignStmt(Id(lovP), StringLit(IlyJD))])), (Id(XDwq), AssignStmt(Id(K0lT), NumLit(51.22))), (Id(yA), If(StringLit(cgyj), If(NumLit(26.6), Return(StringLit(df))), [(NumLit(73.56), Break)], CallStmt(Id(t7wZ), [NumLit(80.47)])), [], Break), (Id(V6G), For(Id(D7Cg), BooleanLit(False), StringLit(CP), Break)), (StringLit(t), AssignStmt(Id(sjPK), StringLit(qCgJ))), (Id(wR4a), AssignStmt(ArrayCell(Id(l2mh), [BooleanLit(True), BooleanLit(False), Id(oH)]), Id(XM)))], None)], None])), VarDecl(Id(XJzd), None, var, Id(sQ)), VarDecl(Id(Gb), BoolType, None, Id(kjk))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115571))

	def test_21530115572(self):
		input = '''
dynamic AKN <- EWRu
func DmO (bool RC[52.77,18.33,14.98])
	return
bool H4j <- true
string vb_[81.68,67.39]
func IVY ()	return 25.63

'''
		expect = '''Program([VarDecl(Id(AKN), None, dynamic, Id(EWRu)), FuncDecl(Id(DmO), [VarDecl(Id(RC), ArrayType([52.77, 18.33, 14.98], BoolType), None, None)], Return()), VarDecl(Id(H4j), BoolType, None, BooleanLit(True)), VarDecl(Id(vb_), ArrayType([81.68, 67.39], StringType), None, None), FuncDecl(Id(IVY), [], Return(NumLit(25.63)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115572))

	def test_21530115573(self):
		input = '''
number nKJ[47.68,94.36] <- 52.6
number DZL <- KJ
var Au <- false
'''
		expect = '''Program([VarDecl(Id(nKJ), ArrayType([47.68, 94.36], NumberType), None, NumLit(52.6)), VarDecl(Id(DZL), NumberType, None, Id(KJ)), VarDecl(Id(Au), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115573))

	def test_21530115574(self):
		input = '''
number thUa
dynamic g_Z
var Nc2J <- false
'''
		expect = '''Program([VarDecl(Id(thUa), NumberType, None, None), VarDecl(Id(g_Z), None, dynamic, None), VarDecl(Id(Nc2J), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115574))

	def test_21530115575(self):
		input = '''
func NHP (bool j4, number tN[59.66,78.53], bool b7)	return
'''
		expect = '''Program([FuncDecl(Id(NHP), [VarDecl(Id(j4), BoolType, None, None), VarDecl(Id(tN), ArrayType([59.66, 78.53], NumberType), None, None), VarDecl(Id(b7), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115575))

	def test_21530115576(self):
		input = '''
func eA (string UNFG[8.05,89.42,46.68], bool fjH, bool xBn[61.03,79.8])	return true
'''
		expect = '''Program([FuncDecl(Id(eA), [VarDecl(Id(UNFG), ArrayType([8.05, 89.42, 46.68], StringType), None, None), VarDecl(Id(fjH), BoolType, None, None), VarDecl(Id(xBn), ArrayType([61.03, 79.8], BoolType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115576))

	def test_21530115577(self):
		input = '''
bool GRo[2.07,55.67,10.62]
number Caw <- "U"
func UKw (bool psL7, bool tF)	return

func VfB (number Fg4, bool Ue_9)	return
dynamic lM <- true
'''
		expect = '''Program([VarDecl(Id(GRo), ArrayType([2.07, 55.67, 10.62], BoolType), None, None), VarDecl(Id(Caw), NumberType, None, StringLit(U)), FuncDecl(Id(UKw), [VarDecl(Id(psL7), BoolType, None, None), VarDecl(Id(tF), BoolType, None, None)], Return()), FuncDecl(Id(VfB), [VarDecl(Id(Fg4), NumberType, None, None), VarDecl(Id(Ue_9), BoolType, None, None)], Return()), VarDecl(Id(lM), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115577))

	def test_21530115578(self):
		input = '''
var NtV <- "Mvt"
func I8 (number JtF, number SJKc[26.2,49.34])
	return 74.52
'''
		expect = '''Program([VarDecl(Id(NtV), None, var, StringLit(Mvt)), FuncDecl(Id(I8), [VarDecl(Id(JtF), NumberType, None, None), VarDecl(Id(SJKc), ArrayType([26.2, 49.34], NumberType), None, None)], Return(NumLit(74.52)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115578))

	def test_21530115579(self):
		input = '''
bool tv[49.37] <- dPr
'''
		expect = '''Program([VarDecl(Id(tv), ArrayType([49.37], BoolType), None, Id(dPr))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115579))

	def test_21530115580(self):
		input = '''
number JxWb[31.59,99.03,74.87] <- "sqk"
func J3Cp (string sIL[99.91,69.58], bool qYcg, string wqkP)
	return 14.34

'''
		expect = '''Program([VarDecl(Id(JxWb), ArrayType([31.59, 99.03, 74.87], NumberType), None, StringLit(sqk)), FuncDecl(Id(J3Cp), [VarDecl(Id(sIL), ArrayType([99.91, 69.58], StringType), None, None), VarDecl(Id(qYcg), BoolType, None, None), VarDecl(Id(wqkP), StringType, None, None)], Return(NumLit(14.34)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115580))

	def test_21530115581(self):
		input = '''
func z6 (number fJ[6.25,20.28], number fm[60.47])	return
bool ehJ2[75.62]
dynamic bn0H <- 42.77
'''
		expect = '''Program([FuncDecl(Id(z6), [VarDecl(Id(fJ), ArrayType([6.25, 20.28], NumberType), None, None), VarDecl(Id(fm), ArrayType([60.47], NumberType), None, None)], Return()), VarDecl(Id(ehJ2), ArrayType([75.62], BoolType), None, None), VarDecl(Id(bn0H), None, dynamic, NumLit(42.77))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115581))

	def test_21530115582(self):
		input = '''
func pQ7 ()
	begin
		if (qDtJ) continue
		elif ("ned") if (false)
		Hj(ga, false)
		elif (32.76)
		bool DmT[10.66,84.7] <- 82.94
		elif ("jWvDT")
		F4["NFS", PqLa] <- 11.18
		elif (DK) string S9R[83.99,94.95,56.44]
		elif (56.97) break
		elif ("urps") continue
		else if ("R") continue
		else return "lM"
		elif (false) return
		elif (YJFb)
		continue
		elif (false)
		begin
			for De until dn5 by "I"
				bool TpN <- true
			if (28.33) if ("qTtxT")
			return gz
			elif ("J")
			begin
				bool XLT2[62.58,93.66,57.05]
			end
			elif (99.63)
			continue
			elif ("RrExY")
			fRTE <- NiP
			else for a5O until true by "jE"
				string EgUD <- true
			begin
			end
		end
		elif (true) XM <- "MIIup"
		if (true)
		ehu <- NGx
		elif ("se")
		begin
			for Lomx until "z" by 50.64
				Q7T(true)
		end
		elif (false) begin
			bool Lx_[65.78,57.97,44.24]
			break
		end
		if (x9) q6[g2Dn, "ZY"] <- 87.01
		elif (true)
		Xe1(true, Hgh)
		elif (false) continue
		elif (hreZ) number mR[39.45] <- "HLF"
		else vJEI <- KoC3
	end
func i2 (bool Rw)
	begin
		xOg["Zcj", "SYwL"] <- 53.44
	end

'''
		expect = '''Program([FuncDecl(Id(pQ7), [], Block([If(Id(qDtJ), Continue), [(StringLit(ned), If(BooleanLit(False), CallStmt(Id(Hj), [Id(ga), BooleanLit(False)])), [(NumLit(32.76), VarDecl(Id(DmT), ArrayType([10.66, 84.7], BoolType), None, NumLit(82.94))), (StringLit(jWvDT), AssignStmt(ArrayCell(Id(F4), [StringLit(NFS), Id(PqLa)]), NumLit(11.18))), (Id(DK), VarDecl(Id(S9R), ArrayType([83.99, 94.95, 56.44], StringType), None, None)), (NumLit(56.97), Break), (StringLit(urps), Continue)], If(StringLit(R), Continue), [], Return(StringLit(lM))), (BooleanLit(False), Return()), (Id(YJFb), Continue), (BooleanLit(False), Block([For(Id(De), Id(dn5), StringLit(I), VarDecl(Id(TpN), BoolType, None, BooleanLit(True))), If(NumLit(28.33), If(StringLit(qTtxT), Return(Id(gz))), [(StringLit(J), Block([VarDecl(Id(XLT2), ArrayType([62.58, 93.66, 57.05], BoolType), None, None)])), (NumLit(99.63), Continue), (StringLit(RrExY), AssignStmt(Id(fRTE), Id(NiP)))], For(Id(a5O), BooleanLit(True), StringLit(jE), VarDecl(Id(EgUD), StringType, None, BooleanLit(True)))), [], None, Block([])])), (BooleanLit(True), AssignStmt(Id(XM), StringLit(MIIup)))], None, If(BooleanLit(True), AssignStmt(Id(ehu), Id(NGx))), [(StringLit(se), Block([For(Id(Lomx), StringLit(z), NumLit(50.64), CallStmt(Id(Q7T), [BooleanLit(True)]))])), (BooleanLit(False), Block([VarDecl(Id(Lx_), ArrayType([65.78, 57.97, 44.24], BoolType), None, None), Break]))], None, If(Id(x9), AssignStmt(ArrayCell(Id(q6), [Id(g2Dn), StringLit(ZY)]), NumLit(87.01))), [(BooleanLit(True), CallStmt(Id(Xe1), [BooleanLit(True), Id(Hgh)])), (BooleanLit(False), Continue), (Id(hreZ), VarDecl(Id(mR), ArrayType([39.45], NumberType), None, StringLit(HLF)))], AssignStmt(Id(vJEI), Id(KoC3))])), FuncDecl(Id(i2), [VarDecl(Id(Rw), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(xOg), [StringLit(Zcj), StringLit(SYwL)]), NumLit(53.44))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115582))

	def test_21530115583(self):
		input = '''
func DsY (bool iGOZ[74.92,7.67,42.81], bool oh2)
	return 26.97
func hQLn (bool Lo, bool EQ[44.6,0.24,96.02], string BVGo[50.32,98.25])
	return false
'''
		expect = '''Program([FuncDecl(Id(DsY), [VarDecl(Id(iGOZ), ArrayType([74.92, 7.67, 42.81], BoolType), None, None), VarDecl(Id(oh2), BoolType, None, None)], Return(NumLit(26.97))), FuncDecl(Id(hQLn), [VarDecl(Id(Lo), BoolType, None, None), VarDecl(Id(EQ), ArrayType([44.6, 0.24, 96.02], BoolType), None, None), VarDecl(Id(BVGo), ArrayType([50.32, 98.25], StringType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115583))

	def test_21530115584(self):
		input = '''
bool S8[77.95,99.83,84.7]
number VGbR[89.62,81.32,27.51] <- "bJwOP"
bool yIr
func IwBL (string M53F, bool WF, string GT)	return
'''
		expect = '''Program([VarDecl(Id(S8), ArrayType([77.95, 99.83, 84.7], BoolType), None, None), VarDecl(Id(VGbR), ArrayType([89.62, 81.32, 27.51], NumberType), None, StringLit(bJwOP)), VarDecl(Id(yIr), BoolType, None, None), FuncDecl(Id(IwBL), [VarDecl(Id(M53F), StringType, None, None), VarDecl(Id(WF), BoolType, None, None), VarDecl(Id(GT), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115584))

	def test_21530115585(self):
		input = '''
bool Eu[37.04,66.8,79.82] <- 37.92
func fg ()	begin
	end

'''
		expect = '''Program([VarDecl(Id(Eu), ArrayType([37.04, 66.8, 79.82], BoolType), None, NumLit(37.92)), FuncDecl(Id(fg), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115585))

	def test_21530115586(self):
		input = '''
func dr (number BjI)	return V0VZ
func V7Nr (number IbdL)	return

func R0_ (bool laRX[94.09,49.65])	return "hjm"
var A0Kf <- false
'''
		expect = '''Program([FuncDecl(Id(dr), [VarDecl(Id(BjI), NumberType, None, None)], Return(Id(V0VZ))), FuncDecl(Id(V7Nr), [VarDecl(Id(IbdL), NumberType, None, None)], Return()), FuncDecl(Id(R0_), [VarDecl(Id(laRX), ArrayType([94.09, 49.65], BoolType), None, None)], Return(StringLit(hjm))), VarDecl(Id(A0Kf), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115586))

	def test_21530115587(self):
		input = '''
func XRG (number deDp[95.87,60.77])
	return 3.41

'''
		expect = '''Program([FuncDecl(Id(XRG), [VarDecl(Id(deDp), ArrayType([95.87, 60.77], NumberType), None, None)], Return(NumLit(3.41)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115587))

	def test_21530115588(self):
		input = '''
string Dg2q[35.16] <- false
var N8s <- false
func NAMz (bool M01, bool kl[98.4,33.16], string F8)	return

func UW3 (number IE, bool YP[33.03,89.07])	begin
		oCU <- 80.96
		return
		for Ng5D until JuI by true
			begin
				for dmkW until JHv by un
					for djN until false by oP6
						if (5.43)
						VjV[1.94, Ec] <- 65.96
						elif (qTr)
						return
						else if (fS)
						for cAk until true by mL
							UXa[88.04] <- false
						elif (true)
						var dY <- false
						else wP(62.29)
			end
	end
func Mg ()
	return
'''
		expect = '''Program([VarDecl(Id(Dg2q), ArrayType([35.16], StringType), None, BooleanLit(False)), VarDecl(Id(N8s), None, var, BooleanLit(False)), FuncDecl(Id(NAMz), [VarDecl(Id(M01), BoolType, None, None), VarDecl(Id(kl), ArrayType([98.4, 33.16], BoolType), None, None), VarDecl(Id(F8), StringType, None, None)], Return()), FuncDecl(Id(UW3), [VarDecl(Id(IE), NumberType, None, None), VarDecl(Id(YP), ArrayType([33.03, 89.07], BoolType), None, None)], Block([AssignStmt(Id(oCU), NumLit(80.96)), Return(), For(Id(Ng5D), Id(JuI), BooleanLit(True), Block([For(Id(dmkW), Id(JHv), Id(un), For(Id(djN), BooleanLit(False), Id(oP6), If(NumLit(5.43), AssignStmt(ArrayCell(Id(VjV), [NumLit(1.94), Id(Ec)]), NumLit(65.96))), [(Id(qTr), Return())], If(Id(fS), For(Id(cAk), BooleanLit(True), Id(mL), AssignStmt(ArrayCell(Id(UXa), [NumLit(88.04)]), BooleanLit(False)))), [(BooleanLit(True), VarDecl(Id(dY), None, var, BooleanLit(False)))], CallStmt(Id(wP), [NumLit(62.29)])))]))])), FuncDecl(Id(Mg), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115588))

	def test_21530115589(self):
		input = '''
func vM (number Rd5a[5.3], number c5, bool IUE[49.01,47.52,20.58])
	return

func E3 (number YOa[20.9])	begin
		return EGB
	end
func TAU (bool kFM[41.67,91.44])	begin
		if (y_Xh)
		if (26.05) if (Hez)
		string r4[35.46,68.31] <- QuD_
		elif (58.91)
		sy <- true
		else for cf7 until 27.97 by false
			break
		elif ("yKwY")
		bool roX[1.97,91.84,41.37] <- 94.72
		elif (false) xk[true] <- false
		elif (98.44) Vu75 <- 93.05
		elif ("hjfx") begin
		end
		elif (true) break
		if (false)
		for Kl until 74.89 by false
			return
		elif (D7) XXiV[ce, ZlHb, 15.27] <- "hU"
		elif (6.88) dynamic zig <- "KK"
		elif (cv) Zg("O")
		elif (true) if (zXK)
		for aa until false by Atb
			xam[Smuq, false, 82.71] <- 33.4
		elif (pBA) return
		else dvuK(r68, "vGFxq", "FvKmS")
		number KTC[29.53,54.35]
	end

number bIO
'''
		expect = '''Program([FuncDecl(Id(vM), [VarDecl(Id(Rd5a), ArrayType([5.3], NumberType), None, None), VarDecl(Id(c5), NumberType, None, None), VarDecl(Id(IUE), ArrayType([49.01, 47.52, 20.58], BoolType), None, None)], Return()), FuncDecl(Id(E3), [VarDecl(Id(YOa), ArrayType([20.9], NumberType), None, None)], Block([Return(Id(EGB))])), FuncDecl(Id(TAU), [VarDecl(Id(kFM), ArrayType([41.67, 91.44], BoolType), None, None)], Block([If(Id(y_Xh), If(NumLit(26.05), If(Id(Hez), VarDecl(Id(r4), ArrayType([35.46, 68.31], StringType), None, Id(QuD_))), [(NumLit(58.91), AssignStmt(Id(sy), BooleanLit(True)))], For(Id(cf7), NumLit(27.97), BooleanLit(False), Break)), [(StringLit(yKwY), VarDecl(Id(roX), ArrayType([1.97, 91.84, 41.37], BoolType), None, NumLit(94.72))), (BooleanLit(False), AssignStmt(ArrayCell(Id(xk), [BooleanLit(True)]), BooleanLit(False))), (NumLit(98.44), AssignStmt(Id(Vu75), NumLit(93.05))), (StringLit(hjfx), Block([])), (BooleanLit(True), Break)], None), [], None, If(BooleanLit(False), For(Id(Kl), NumLit(74.89), BooleanLit(False), Return())), [(Id(D7), AssignStmt(ArrayCell(Id(XXiV), [Id(ce), Id(ZlHb), NumLit(15.27)]), StringLit(hU))), (NumLit(6.88), VarDecl(Id(zig), None, dynamic, StringLit(KK))), (Id(cv), CallStmt(Id(Zg), [StringLit(O)])), (BooleanLit(True), If(Id(zXK), For(Id(aa), BooleanLit(False), Id(Atb), AssignStmt(ArrayCell(Id(xam), [Id(Smuq), BooleanLit(False), NumLit(82.71)]), NumLit(33.4)))), [(Id(pBA), Return())], CallStmt(Id(dvuK), [Id(r68), StringLit(vGFxq), StringLit(FvKmS)]))], None, VarDecl(Id(KTC), ArrayType([29.53, 54.35], NumberType), None, None)])), VarDecl(Id(bIO), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115589))

	def test_21530115590(self):
		input = '''
number Qo6W <- 74.58
var Cf72 <- true
'''
		expect = '''Program([VarDecl(Id(Qo6W), NumberType, None, NumLit(74.58)), VarDecl(Id(Cf72), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115590))

	def test_21530115591(self):
		input = '''
string Ne[15.53,47.8] <- 52.14
func r1kf (string CsQ, number Jaa[46.69,43.07], string hjF[80.81])	return 92.63

'''
		expect = '''Program([VarDecl(Id(Ne), ArrayType([15.53, 47.8], StringType), None, NumLit(52.14)), FuncDecl(Id(r1kf), [VarDecl(Id(CsQ), StringType, None, None), VarDecl(Id(Jaa), ArrayType([46.69, 43.07], NumberType), None, None), VarDecl(Id(hjF), ArrayType([80.81], StringType), None, None)], Return(NumLit(92.63)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115591))

	def test_21530115592(self):
		input = '''
number Dzk[88.5,83.52,51.95]
var TRV <- false
func VLa (number VQ[73.57,66.36], number oJDT)
	return 98.14

'''
		expect = '''Program([VarDecl(Id(Dzk), ArrayType([88.5, 83.52, 51.95], NumberType), None, None), VarDecl(Id(TRV), None, var, BooleanLit(False)), FuncDecl(Id(VLa), [VarDecl(Id(VQ), ArrayType([73.57, 66.36], NumberType), None, None), VarDecl(Id(oJDT), NumberType, None, None)], Return(NumLit(98.14)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115592))

	def test_21530115593(self):
		input = '''
func R3rT (number VTtV[66.92], string WCk[7.45], string H8[43.38,76.19])
	return
string uoLp[68.62,76.53]
func RM4C (bool ma[41.9])	return 74.8
func FrE ()	return
'''
		expect = '''Program([FuncDecl(Id(R3rT), [VarDecl(Id(VTtV), ArrayType([66.92], NumberType), None, None), VarDecl(Id(WCk), ArrayType([7.45], StringType), None, None), VarDecl(Id(H8), ArrayType([43.38, 76.19], StringType), None, None)], Return()), VarDecl(Id(uoLp), ArrayType([68.62, 76.53], StringType), None, None), FuncDecl(Id(RM4C), [VarDecl(Id(ma), ArrayType([41.9], BoolType), None, None)], Return(NumLit(74.8))), FuncDecl(Id(FrE), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115593))

	def test_21530115594(self):
		input = '''
string EpMk[61.17,19.89,82.83]
string t2t[23.49]
var zC <- false
number oL[90.14,58.58,17.12]
func egsv ()
	begin
		break
	end
'''
		expect = '''Program([VarDecl(Id(EpMk), ArrayType([61.17, 19.89, 82.83], StringType), None, None), VarDecl(Id(t2t), ArrayType([23.49], StringType), None, None), VarDecl(Id(zC), None, var, BooleanLit(False)), VarDecl(Id(oL), ArrayType([90.14, 58.58, 17.12], NumberType), None, None), FuncDecl(Id(egsv), [], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115594))

	def test_21530115595(self):
		input = '''
func EoX (number aO)	return nIld

bool lXMI[56.58] <- "s"
number mTa <- Nber
number zT
'''
		expect = '''Program([FuncDecl(Id(EoX), [VarDecl(Id(aO), NumberType, None, None)], Return(Id(nIld))), VarDecl(Id(lXMI), ArrayType([56.58], BoolType), None, StringLit(s)), VarDecl(Id(mTa), NumberType, None, Id(Nber)), VarDecl(Id(zT), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115595))

	def test_21530115596(self):
		input = '''
func dB8Z (number rX, bool Ax[65.52])	begin
		for jrX until NE by 21.9
			fD(true, ZUd, 43.64)
	end
number OTW <- false
'''
		expect = '''Program([FuncDecl(Id(dB8Z), [VarDecl(Id(rX), NumberType, None, None), VarDecl(Id(Ax), ArrayType([65.52], BoolType), None, None)], Block([For(Id(jrX), Id(NE), NumLit(21.9), CallStmt(Id(fD), [BooleanLit(True), Id(ZUd), NumLit(43.64)]))])), VarDecl(Id(OTW), NumberType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115596))

	def test_21530115597(self):
		input = '''
var PB <- "HrJy"
number lnSB[51.57] <- vqp
dynamic Psu
bool vV[17.03]
'''
		expect = '''Program([VarDecl(Id(PB), None, var, StringLit(HrJy)), VarDecl(Id(lnSB), ArrayType([51.57], NumberType), None, Id(vqp)), VarDecl(Id(Psu), None, dynamic, None), VarDecl(Id(vV), ArrayType([17.03], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115597))

	def test_21530115598(self):
		input = '''
bool bkND
'''
		expect = '''Program([VarDecl(Id(bkND), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115598))

	def test_21530115599(self):
		input = '''
func Ij (bool T5WW[62.59,64.51], number Wbr)
	return 51.52
func dDYz (number ZW)
	return
'''
		expect = '''Program([FuncDecl(Id(Ij), [VarDecl(Id(T5WW), ArrayType([62.59, 64.51], BoolType), None, None), VarDecl(Id(Wbr), NumberType, None, None)], Return(NumLit(51.52))), FuncDecl(Id(dDYz), [VarDecl(Id(ZW), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115599))

	def test_21530115600(self):
		input = '''
func us9K (bool y2[91.95], bool XFj[25.81,56.06,33.57], bool haj)
	return

func nE (number kA9R)
	return

func GKO (number x6JA[9.17,90.78], number xLM9[66.35,51.07,24.9])
	return

'''
		expect = '''Program([FuncDecl(Id(us9K), [VarDecl(Id(y2), ArrayType([91.95], BoolType), None, None), VarDecl(Id(XFj), ArrayType([25.81, 56.06, 33.57], BoolType), None, None), VarDecl(Id(haj), BoolType, None, None)], Return()), FuncDecl(Id(nE), [VarDecl(Id(kA9R), NumberType, None, None)], Return()), FuncDecl(Id(GKO), [VarDecl(Id(x6JA), ArrayType([9.17, 90.78], NumberType), None, None), VarDecl(Id(xLM9), ArrayType([66.35, 51.07, 24.9], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115600))

	def test_21530115601(self):
		input = '''
func T_ (number lI8s)
	return "MIVq"

number Lp <- islb
'''
		expect = '''Program([FuncDecl(Id(T_), [VarDecl(Id(lI8s), NumberType, None, None)], Return(StringLit(MIVq))), VarDecl(Id(Lp), NumberType, None, Id(islb))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115601))

	def test_21530115602(self):
		input = '''
number G7P[70.47,45.02,66.37] <- vu
'''
		expect = '''Program([VarDecl(Id(G7P), ArrayType([70.47, 45.02, 66.37], NumberType), None, Id(vu))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115602))

	def test_21530115603(self):
		input = '''
func xe (string BN[41.5])
	begin
		LQ18 <- false
	end
func HeP (number mk4[4.66,32.67,26.82], string XH[79.63,63.53])
	return
func A7GN (string eOML[31.99])	begin
		return
		continue
	end
bool kBL[43.54,68.64,66.71]
bool W7
'''
		expect = '''Program([FuncDecl(Id(xe), [VarDecl(Id(BN), ArrayType([41.5], StringType), None, None)], Block([AssignStmt(Id(LQ18), BooleanLit(False))])), FuncDecl(Id(HeP), [VarDecl(Id(mk4), ArrayType([4.66, 32.67, 26.82], NumberType), None, None), VarDecl(Id(XH), ArrayType([79.63, 63.53], StringType), None, None)], Return()), FuncDecl(Id(A7GN), [VarDecl(Id(eOML), ArrayType([31.99], StringType), None, None)], Block([Return(), Continue])), VarDecl(Id(kBL), ArrayType([43.54, 68.64, 66.71], BoolType), None, None), VarDecl(Id(W7), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115603))

	def test_21530115604(self):
		input = '''
dynamic dofQ <- 46.17
string Eh
func sV (number uF5[61.81,12.34])	begin
		continue
		number N2tE[3.94,34.42] <- false
		return "oZJz"
	end
string IK5_
'''
		expect = '''Program([VarDecl(Id(dofQ), None, dynamic, NumLit(46.17)), VarDecl(Id(Eh), StringType, None, None), FuncDecl(Id(sV), [VarDecl(Id(uF5), ArrayType([61.81, 12.34], NumberType), None, None)], Block([Continue, VarDecl(Id(N2tE), ArrayType([3.94, 34.42], NumberType), None, BooleanLit(False)), Return(StringLit(oZJz))])), VarDecl(Id(IK5_), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115604))

	def test_21530115605(self):
		input = '''
bool jIw <- 68.38
func G1 ()
	begin
		for cUXS until true by false
			for lLm until "ZJ" by true
				continue
		if (true) break
		elif ("A")
		begin
		end
		elif (5.21)
		OsHn()
		elif (l6) bool QDg[17.59,95.99] <- "PBD"
	end

dynamic oHX <- false
'''
		expect = '''Program([VarDecl(Id(jIw), BoolType, None, NumLit(68.38)), FuncDecl(Id(G1), [], Block([For(Id(cUXS), BooleanLit(True), BooleanLit(False), For(Id(lLm), StringLit(ZJ), BooleanLit(True), Continue)), If(BooleanLit(True), Break), [(StringLit(A), Block([])), (NumLit(5.21), CallStmt(Id(OsHn), [])), (Id(l6), VarDecl(Id(QDg), ArrayType([17.59, 95.99], BoolType), None, StringLit(PBD)))], None])), VarDecl(Id(oHX), None, dynamic, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115605))

	def test_21530115606(self):
		input = '''
bool bSP8[62.76,64.4,97.24] <- true
dynamic WT
number Rd5t[9.17]
'''
		expect = '''Program([VarDecl(Id(bSP8), ArrayType([62.76, 64.4, 97.24], BoolType), None, BooleanLit(True)), VarDecl(Id(WT), None, dynamic, None), VarDecl(Id(Rd5t), ArrayType([9.17], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115606))

	def test_21530115607(self):
		input = '''
func WbA7 (string rr[71.45])
	begin
	end

string Z2W <- false
'''
		expect = '''Program([FuncDecl(Id(WbA7), [VarDecl(Id(rr), ArrayType([71.45], StringType), None, None)], Block([])), VarDecl(Id(Z2W), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115607))

	def test_21530115608(self):
		input = '''
func f4Gp (bool caC, number Iw, string TfKE[56.28])
	return "wmu"

func dj (string nB)	begin
		begin
			bool Nz
			continue
		end
		break
	end
'''
		expect = '''Program([FuncDecl(Id(f4Gp), [VarDecl(Id(caC), BoolType, None, None), VarDecl(Id(Iw), NumberType, None, None), VarDecl(Id(TfKE), ArrayType([56.28], StringType), None, None)], Return(StringLit(wmu))), FuncDecl(Id(dj), [VarDecl(Id(nB), StringType, None, None)], Block([Block([VarDecl(Id(Nz), BoolType, None, None), Continue]), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115608))

	def test_21530115609(self):
		input = '''
func uO (string i4)
	begin
		continue
		begin
			for d36 until 29.58 by "ez"
				return "Q"
			begin
				MJ[z3U1] <- h5X7
			end
		end
		if (8.95)
		return
		elif (false)
		begin
			number Mpb[58.9] <- true
		end
		elif (false) C5LM <- 5.3
	end

string oYY0[89.02,9.28] <- 32.57
var V5i <- false
string Zbd <- Uft
func st (bool TY, string Ktc)
	begin
		continue
		Ra(false, "myd", jlk)
		wt <- false
	end
'''
		expect = '''Program([FuncDecl(Id(uO), [VarDecl(Id(i4), StringType, None, None)], Block([Continue, Block([For(Id(d36), NumLit(29.58), StringLit(ez), Return(StringLit(Q))), Block([AssignStmt(ArrayCell(Id(MJ), [Id(z3U1)]), Id(h5X7))])]), If(NumLit(8.95), Return()), [(BooleanLit(False), Block([VarDecl(Id(Mpb), ArrayType([58.9], NumberType), None, BooleanLit(True))])), (BooleanLit(False), AssignStmt(Id(C5LM), NumLit(5.3)))], None])), VarDecl(Id(oYY0), ArrayType([89.02, 9.28], StringType), None, NumLit(32.57)), VarDecl(Id(V5i), None, var, BooleanLit(False)), VarDecl(Id(Zbd), StringType, None, Id(Uft)), FuncDecl(Id(st), [VarDecl(Id(TY), BoolType, None, None), VarDecl(Id(Ktc), StringType, None, None)], Block([Continue, CallStmt(Id(Ra), [BooleanLit(False), StringLit(myd), Id(jlk)]), AssignStmt(Id(wt), BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115609))

	def test_21530115610(self):
		input = '''
func o1cu (bool jh[46.14,28.21,94.85], bool tk6y, number Lw[99.97,25.56,39.67])
	return "ln"

string X0B4[74.33,83.5] <- y8
func Lqq (number ba_i, bool GUbv)
	begin
		continue
		Ml()
		if (false)
		break
		elif (yc) break
		elif (80.33)
		Ien("jdaQ")
		elif (Pd)
		for HkfF until f5s by false
			o5r[75.9] <- "JK"
		elif (g2) break
		elif (true)
		return
		else for BMd until 76.29 by zmA
			begin
				continue
			end
	end
number MO[82.77,11.2] <- XQ
'''
		expect = '''Program([FuncDecl(Id(o1cu), [VarDecl(Id(jh), ArrayType([46.14, 28.21, 94.85], BoolType), None, None), VarDecl(Id(tk6y), BoolType, None, None), VarDecl(Id(Lw), ArrayType([99.97, 25.56, 39.67], NumberType), None, None)], Return(StringLit(ln))), VarDecl(Id(X0B4), ArrayType([74.33, 83.5], StringType), None, Id(y8)), FuncDecl(Id(Lqq), [VarDecl(Id(ba_i), NumberType, None, None), VarDecl(Id(GUbv), BoolType, None, None)], Block([Continue, CallStmt(Id(Ml), []), If(BooleanLit(False), Break), [(Id(yc), Break), (NumLit(80.33), CallStmt(Id(Ien), [StringLit(jdaQ)])), (Id(Pd), For(Id(HkfF), Id(f5s), BooleanLit(False), AssignStmt(ArrayCell(Id(o5r), [NumLit(75.9)]), StringLit(JK)))), (Id(g2), Break), (BooleanLit(True), Return())], For(Id(BMd), NumLit(76.29), Id(zmA), Block([Continue]))])), VarDecl(Id(MO), ArrayType([82.77, 11.2], NumberType), None, Id(XQ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115610))

	def test_21530115611(self):
		input = '''
bool FSD[83.33,67.69]
func yw (string vq[73.24])	begin
		begin
			break
			string oE[23.82] <- "qs"
			continue
		end
		begin
			break
			Cnh <- false
		end
	end
bool YFa <- V668
func A7ZA (string Qy6[35.6], bool IBY[70.93,5.46,76.35], number PCgU)
	return ar

bool pLK[85.5,77.36] <- 73.06
'''
		expect = '''Program([VarDecl(Id(FSD), ArrayType([83.33, 67.69], BoolType), None, None), FuncDecl(Id(yw), [VarDecl(Id(vq), ArrayType([73.24], StringType), None, None)], Block([Block([Break, VarDecl(Id(oE), ArrayType([23.82], StringType), None, StringLit(qs)), Continue]), Block([Break, AssignStmt(Id(Cnh), BooleanLit(False))])])), VarDecl(Id(YFa), BoolType, None, Id(V668)), FuncDecl(Id(A7ZA), [VarDecl(Id(Qy6), ArrayType([35.6], StringType), None, None), VarDecl(Id(IBY), ArrayType([70.93, 5.46, 76.35], BoolType), None, None), VarDecl(Id(PCgU), NumberType, None, None)], Return(Id(ar))), VarDecl(Id(pLK), ArrayType([85.5, 77.36], BoolType), None, NumLit(73.06))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115611))

	def test_21530115612(self):
		input = '''
string zRS[20.42,55.9,49.12] <- rQLx
number FWw[10.25] <- false
string bat
'''
		expect = '''Program([VarDecl(Id(zRS), ArrayType([20.42, 55.9, 49.12], StringType), None, Id(rQLx)), VarDecl(Id(FWw), ArrayType([10.25], NumberType), None, BooleanLit(False)), VarDecl(Id(bat), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115612))

	def test_21530115613(self):
		input = '''
func jH (bool T9[18.41,60.72], bool DaX[85.24], bool c6h)
	begin
	end
func MuPW (number y39T[64.39], number BqQ[5.82,64.13], number EM)
	return false

bool nHm[59.39]
bool DB[24.56,4.37,22.89]
func y7 ()	begin
		break
		if (U1)
		OMf(bzw)
		elif (true)
		break
		elif ("Q") if (16.01) EtT <- "ap"
		elif (false)
		begin
			if (SCbG)
			break
			elif ("UD")
			continue
		end
		elif (false) bool qOOq[29.22,28.65] <- "kF"
		elif (70.24) begin
			g4 <- "IV"
			return
			continue
		end
		else oVgP(l2H, "FGjA")
		begin
		end
	end

'''
		expect = '''Program([FuncDecl(Id(jH), [VarDecl(Id(T9), ArrayType([18.41, 60.72], BoolType), None, None), VarDecl(Id(DaX), ArrayType([85.24], BoolType), None, None), VarDecl(Id(c6h), BoolType, None, None)], Block([])), FuncDecl(Id(MuPW), [VarDecl(Id(y39T), ArrayType([64.39], NumberType), None, None), VarDecl(Id(BqQ), ArrayType([5.82, 64.13], NumberType), None, None), VarDecl(Id(EM), NumberType, None, None)], Return(BooleanLit(False))), VarDecl(Id(nHm), ArrayType([59.39], BoolType), None, None), VarDecl(Id(DB), ArrayType([24.56, 4.37, 22.89], BoolType), None, None), FuncDecl(Id(y7), [], Block([Break, If(Id(U1), CallStmt(Id(OMf), [Id(bzw)])), [(BooleanLit(True), Break), (StringLit(Q), If(NumLit(16.01), AssignStmt(Id(EtT), StringLit(ap))), [(BooleanLit(False), Block([If(Id(SCbG), Break), [(StringLit(UD), Continue)], None])), (BooleanLit(False), VarDecl(Id(qOOq), ArrayType([29.22, 28.65], BoolType), None, StringLit(kF))), (NumLit(70.24), Block([AssignStmt(Id(g4), StringLit(IV)), Return(), Continue]))], CallStmt(Id(oVgP), [Id(l2H), StringLit(FGjA)]))], None, Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115613))

	def test_21530115614(self):
		input = '''
func bFD (string nt[20.83])	return

'''
		expect = '''Program([FuncDecl(Id(bFD), [VarDecl(Id(nt), ArrayType([20.83], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115614))

	def test_21530115615(self):
		input = '''
string Upje
func tw ()
	return

'''
		expect = '''Program([VarDecl(Id(Upje), StringType, None, None), FuncDecl(Id(tw), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115615))

	def test_21530115616(self):
		input = '''
bool Y0 <- "INS"
func WHs (string qv, string JH[91.69,10.92], bool LDXg[31.85])
	return

func SC (number Rl)	return dd
string FIHC
'''
		expect = '''Program([VarDecl(Id(Y0), BoolType, None, StringLit(INS)), FuncDecl(Id(WHs), [VarDecl(Id(qv), StringType, None, None), VarDecl(Id(JH), ArrayType([91.69, 10.92], StringType), None, None), VarDecl(Id(LDXg), ArrayType([31.85], BoolType), None, None)], Return()), FuncDecl(Id(SC), [VarDecl(Id(Rl), NumberType, None, None)], Return(Id(dd))), VarDecl(Id(FIHC), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115616))

	def test_21530115617(self):
		input = '''
string sd6p[83.13,81.81] <- 97.22
bool xqv[68.23,83.63,48.56] <- 10.36
'''
		expect = '''Program([VarDecl(Id(sd6p), ArrayType([83.13, 81.81], StringType), None, NumLit(97.22)), VarDecl(Id(xqv), ArrayType([68.23, 83.63, 48.56], BoolType), None, NumLit(10.36))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115617))

	def test_21530115618(self):
		input = '''
func BWeE (bool xdwF)	return
'''
		expect = '''Program([FuncDecl(Id(BWeE), [VarDecl(Id(xdwF), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115618))

	def test_21530115619(self):
		input = '''
func ht44 (number UY1)	return

string TX[51.28] <- "Jmt"
string tdu8[24.7,69.26,67.88]
'''
		expect = '''Program([FuncDecl(Id(ht44), [VarDecl(Id(UY1), NumberType, None, None)], Return()), VarDecl(Id(TX), ArrayType([51.28], StringType), None, StringLit(Jmt)), VarDecl(Id(tdu8), ArrayType([24.7, 69.26, 67.88], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115619))

	def test_21530115620(self):
		input = '''
func WzL (string tDu[22.84,86.19,82.32])
	return false
func LU (number J4[8.54], string N7j)	return "Y"

'''
		expect = '''Program([FuncDecl(Id(WzL), [VarDecl(Id(tDu), ArrayType([22.84, 86.19, 82.32], StringType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(LU), [VarDecl(Id(J4), ArrayType([8.54], NumberType), None, None), VarDecl(Id(N7j), StringType, None, None)], Return(StringLit(Y)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115620))

	def test_21530115621(self):
		input = '''
bool Hb[59.61,80.63]
number Mw[73.03,87.53,11.4]
func xvbc (bool qw[98.63,86.78], number dSbl[76.23,98.78,54.17], string Er)
	return
'''
		expect = '''Program([VarDecl(Id(Hb), ArrayType([59.61, 80.63], BoolType), None, None), VarDecl(Id(Mw), ArrayType([73.03, 87.53, 11.4], NumberType), None, None), FuncDecl(Id(xvbc), [VarDecl(Id(qw), ArrayType([98.63, 86.78], BoolType), None, None), VarDecl(Id(dSbl), ArrayType([76.23, 98.78, 54.17], NumberType), None, None), VarDecl(Id(Er), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115621))

	def test_21530115622(self):
		input = '''
string PmKZ[63.54,41.81]
'''
		expect = '''Program([VarDecl(Id(PmKZ), ArrayType([63.54, 41.81], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115622))

	def test_21530115623(self):
		input = '''
bool HEl
'''
		expect = '''Program([VarDecl(Id(HEl), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115623))

	def test_21530115624(self):
		input = '''
func QT3v ()
	return
func aWHu ()	return

func f0 (number hmFq, string Rjf)	return Bf
'''
		expect = '''Program([FuncDecl(Id(QT3v), [], Return()), FuncDecl(Id(aWHu), [], Return()), FuncDecl(Id(f0), [VarDecl(Id(hmFq), NumberType, None, None), VarDecl(Id(Rjf), StringType, None, None)], Return(Id(Bf)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115624))

	def test_21530115625(self):
		input = '''
func Ls8 (string DQ[81.66], string qT[45.41,92.12], number zj[63.78,10.55])	return w5

func utB ()
	begin
		if (E4Z) return
		elif (true) continue
		elif (59.17)
		return
		elif (false) for Qu until "fn" by XB_s
			var IF <- true
		elif (true) RIW7 <- yfF
		elif (TO)
		q4(uKqd)
		begin
		end
		bool HlK[20.03]
	end
number phf[91.03,19.42,48.87]
dynamic SSl
bool V37
'''
		expect = '''Program([FuncDecl(Id(Ls8), [VarDecl(Id(DQ), ArrayType([81.66], StringType), None, None), VarDecl(Id(qT), ArrayType([45.41, 92.12], StringType), None, None), VarDecl(Id(zj), ArrayType([63.78, 10.55], NumberType), None, None)], Return(Id(w5))), FuncDecl(Id(utB), [], Block([If(Id(E4Z), Return()), [(BooleanLit(True), Continue), (NumLit(59.17), Return()), (BooleanLit(False), For(Id(Qu), StringLit(fn), Id(XB_s), VarDecl(Id(IF), None, var, BooleanLit(True)))), (BooleanLit(True), AssignStmt(Id(RIW7), Id(yfF))), (Id(TO), CallStmt(Id(q4), [Id(uKqd)]))], None, Block([]), VarDecl(Id(HlK), ArrayType([20.03], BoolType), None, None)])), VarDecl(Id(phf), ArrayType([91.03, 19.42, 48.87], NumberType), None, None), VarDecl(Id(SSl), None, dynamic, None), VarDecl(Id(V37), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115625))

	def test_21530115626(self):
		input = '''
func s4S (number r16K[40.89,26.69,5.56], bool P9hD[30.18], string p69[44.8,37.58])	return

func aB (string mv[59.49,34.31], number LI[60.61,17.73,19.26], string hyG[69.34,84.44,11.09])
	return
bool NVFH[37.53,8.49] <- false
var hlbZ <- true
func fs (bool OQCm)
	return

'''
		expect = '''Program([FuncDecl(Id(s4S), [VarDecl(Id(r16K), ArrayType([40.89, 26.69, 5.56], NumberType), None, None), VarDecl(Id(P9hD), ArrayType([30.18], BoolType), None, None), VarDecl(Id(p69), ArrayType([44.8, 37.58], StringType), None, None)], Return()), FuncDecl(Id(aB), [VarDecl(Id(mv), ArrayType([59.49, 34.31], StringType), None, None), VarDecl(Id(LI), ArrayType([60.61, 17.73, 19.26], NumberType), None, None), VarDecl(Id(hyG), ArrayType([69.34, 84.44, 11.09], StringType), None, None)], Return()), VarDecl(Id(NVFH), ArrayType([37.53, 8.49], BoolType), None, BooleanLit(False)), VarDecl(Id(hlbZ), None, var, BooleanLit(True)), FuncDecl(Id(fs), [VarDecl(Id(OQCm), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115626))

	def test_21530115627(self):
		input = '''
dynamic vAdj <- false
func yNsr (string A3i[6.71,31.3], number QwN[39.46,92.95,83.02], bool J5)	return rCiV

func IVi (number Sk7z[75.36], string xnq[91.78,39.17,93.21], number u7_[22.81])
	begin
		for lz until "Cz" by true
			for Cv6a until "t" by "eNTwr"
				if ("KS") continue
				elif (pU8Y)
				zZu()
				elif (false)
				continue
				elif ("pRij") begin
				end
				elif (49.89)
				if ("R")
				if (63.03) F1[true, true] <- Edc
				elif (72.69)
				CWIH["e", false, "dcPZ"] <- 41.89
				elif (hhr)
				break
				elif (H7)
				Ca4[Edlr] <- Ze
				elif (IMPA) string sN1b[43.62] <- true
				else begin
					if ("O") begin
						begin
							kS0(false)
							dynamic Lz4 <- AwVS
							if (IIAB)
							continue
							elif (74.3)
							for e6 until false by false
								sj()
							else continue
						end
						ML()
					end
					elif (38.46)
					begin
						return 96.98
						continue
					end
					elif (false) number b_
					elif (27.48) D0GE[84.75, "qLFAM"] <- yx
					else for X8x until Mo by nu
						if ("CzZ")
						for p2B until "XzQt" by cr
							return "D"
						elif (K7X8) break
						else oGWr(RR)
				end
				elif (f8y)
				break
				elif (45.88) number nnaJ
				elif (28.22)
				return PdJ
				elif ("u") tybi()
	end
func L2 (number Ny[97.39,47.34,50.03])	return OWK
'''
		expect = '''Program([VarDecl(Id(vAdj), None, dynamic, BooleanLit(False)), FuncDecl(Id(yNsr), [VarDecl(Id(A3i), ArrayType([6.71, 31.3], StringType), None, None), VarDecl(Id(QwN), ArrayType([39.46, 92.95, 83.02], NumberType), None, None), VarDecl(Id(J5), BoolType, None, None)], Return(Id(rCiV))), FuncDecl(Id(IVi), [VarDecl(Id(Sk7z), ArrayType([75.36], NumberType), None, None), VarDecl(Id(xnq), ArrayType([91.78, 39.17, 93.21], StringType), None, None), VarDecl(Id(u7_), ArrayType([22.81], NumberType), None, None)], Block([For(Id(lz), StringLit(Cz), BooleanLit(True), For(Id(Cv6a), StringLit(t), StringLit(eNTwr), If(StringLit(KS), Continue), [(Id(pU8Y), CallStmt(Id(zZu), [])), (BooleanLit(False), Continue), (StringLit(pRij), Block([])), (NumLit(49.89), If(StringLit(R), If(NumLit(63.03), AssignStmt(ArrayCell(Id(F1), [BooleanLit(True), BooleanLit(True)]), Id(Edc))), [(NumLit(72.69), AssignStmt(ArrayCell(Id(CWIH), [StringLit(e), BooleanLit(False), StringLit(dcPZ)]), NumLit(41.89))), (Id(hhr), Break), (Id(H7), AssignStmt(ArrayCell(Id(Ca4), [Id(Edlr)]), Id(Ze))), (Id(IMPA), VarDecl(Id(sN1b), ArrayType([43.62], StringType), None, BooleanLit(True)))], Block([If(StringLit(O), Block([Block([CallStmt(Id(kS0), [BooleanLit(False)]), VarDecl(Id(Lz4), None, dynamic, Id(AwVS)), If(Id(IIAB), Continue), [(NumLit(74.3), For(Id(e6), BooleanLit(False), BooleanLit(False), CallStmt(Id(sj), [])))], Continue]), CallStmt(Id(ML), [])])), [(NumLit(38.46), Block([Return(NumLit(96.98)), Continue])), (BooleanLit(False), VarDecl(Id(b_), NumberType, None, None)), (NumLit(27.48), AssignStmt(ArrayCell(Id(D0GE), [NumLit(84.75), StringLit(qLFAM)]), Id(yx)))], For(Id(X8x), Id(Mo), Id(nu), If(StringLit(CzZ), For(Id(p2B), StringLit(XzQt), Id(cr), Return(StringLit(D)))), [(Id(K7X8), Break)], CallStmt(Id(oGWr), [Id(RR)]))])), [(Id(f8y), Break), (NumLit(45.88), VarDecl(Id(nnaJ), NumberType, None, None)), (NumLit(28.22), Return(Id(PdJ))), (StringLit(u), CallStmt(Id(tybi), []))], None)], None))])), FuncDecl(Id(L2), [VarDecl(Id(Ny), ArrayType([97.39, 47.34, 50.03], NumberType), None, None)], Return(Id(OWK)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115627))

	def test_21530115628(self):
		input = '''
func ER ()
	return "tv"

bool p46f <- sFMz
number Sjr1
string sshS[9.41,8.48,25.0] <- gjV
bool nAj[35.84,16.37,24.27] <- true
'''
		expect = '''Program([FuncDecl(Id(ER), [], Return(StringLit(tv))), VarDecl(Id(p46f), BoolType, None, Id(sFMz)), VarDecl(Id(Sjr1), NumberType, None, None), VarDecl(Id(sshS), ArrayType([9.41, 8.48, 25.0], StringType), None, Id(gjV)), VarDecl(Id(nAj), ArrayType([35.84, 16.37, 24.27], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115628))

	def test_21530115629(self):
		input = '''
func jaC (number iHSC[41.77,97.2])	return

dynamic rkW
var Iy2O <- 89.97
'''
		expect = '''Program([FuncDecl(Id(jaC), [VarDecl(Id(iHSC), ArrayType([41.77, 97.2], NumberType), None, None)], Return()), VarDecl(Id(rkW), None, dynamic, None), VarDecl(Id(Iy2O), None, var, NumLit(89.97))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115629))

	def test_21530115630(self):
		input = '''
dynamic sbG
func uv (bool SN, number ktUp, bool vv[5.11])
	return false
func WA3p (number Jv, bool MS[51.11,86.9,36.85], string ltQs)
	return

bool fQ[18.29,73.91] <- 14.98
number dKK <- qd_
'''
		expect = '''Program([VarDecl(Id(sbG), None, dynamic, None), FuncDecl(Id(uv), [VarDecl(Id(SN), BoolType, None, None), VarDecl(Id(ktUp), NumberType, None, None), VarDecl(Id(vv), ArrayType([5.11], BoolType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(WA3p), [VarDecl(Id(Jv), NumberType, None, None), VarDecl(Id(MS), ArrayType([51.11, 86.9, 36.85], BoolType), None, None), VarDecl(Id(ltQs), StringType, None, None)], Return()), VarDecl(Id(fQ), ArrayType([18.29, 73.91], BoolType), None, NumLit(14.98)), VarDecl(Id(dKK), NumberType, None, Id(qd_))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115630))

	def test_21530115631(self):
		input = '''
func fJEm ()	return

dynamic y8V <- true
number zHC
func X4 (string V98V[38.31,73.72], number Jzp[66.57,9.21])	begin
		for Se until lrN by v8p
			for v3 until false by "SS"
				var NIhX <- 14.42
	end

func wl (string Dbx[30.45,91.54,98.2], string a6n[20.12])
	return true
'''
		expect = '''Program([FuncDecl(Id(fJEm), [], Return()), VarDecl(Id(y8V), None, dynamic, BooleanLit(True)), VarDecl(Id(zHC), NumberType, None, None), FuncDecl(Id(X4), [VarDecl(Id(V98V), ArrayType([38.31, 73.72], StringType), None, None), VarDecl(Id(Jzp), ArrayType([66.57, 9.21], NumberType), None, None)], Block([For(Id(Se), Id(lrN), Id(v8p), For(Id(v3), BooleanLit(False), StringLit(SS), VarDecl(Id(NIhX), None, var, NumLit(14.42))))])), FuncDecl(Id(wl), [VarDecl(Id(Dbx), ArrayType([30.45, 91.54, 98.2], StringType), None, None), VarDecl(Id(a6n), ArrayType([20.12], StringType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115631))

	def test_21530115632(self):
		input = '''
string gP_[85.96]
number J3Hn[99.24]
bool vVq
func mCN ()
	begin
	end
number SSzc <- oU
'''
		expect = '''Program([VarDecl(Id(gP_), ArrayType([85.96], StringType), None, None), VarDecl(Id(J3Hn), ArrayType([99.24], NumberType), None, None), VarDecl(Id(vVq), BoolType, None, None), FuncDecl(Id(mCN), [], Block([])), VarDecl(Id(SSzc), NumberType, None, Id(oU))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115632))

	def test_21530115633(self):
		input = '''
func FV0 (bool hLu, number tDsS)	return
func TjRc (string iqvL[17.06,8.5])	return
number tRI <- "JmU"
func sVmL (string XC, string Fr7j[87.84,86.63,26.32], number bVY[95.57,6.55,56.52])
	return Bk1f
'''
		expect = '''Program([FuncDecl(Id(FV0), [VarDecl(Id(hLu), BoolType, None, None), VarDecl(Id(tDsS), NumberType, None, None)], Return()), FuncDecl(Id(TjRc), [VarDecl(Id(iqvL), ArrayType([17.06, 8.5], StringType), None, None)], Return()), VarDecl(Id(tRI), NumberType, None, StringLit(JmU)), FuncDecl(Id(sVmL), [VarDecl(Id(XC), StringType, None, None), VarDecl(Id(Fr7j), ArrayType([87.84, 86.63, 26.32], StringType), None, None), VarDecl(Id(bVY), ArrayType([95.57, 6.55, 56.52], NumberType), None, None)], Return(Id(Bk1f)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115633))

	def test_21530115634(self):
		input = '''
func MnVn (string C3__[75.54,58.75,40.8], bool BYao, string taW[93.74])
	return R5Wk

func vtrA (bool lh, string EWI, number YU)
	return false
'''
		expect = '''Program([FuncDecl(Id(MnVn), [VarDecl(Id(C3__), ArrayType([75.54, 58.75, 40.8], StringType), None, None), VarDecl(Id(BYao), BoolType, None, None), VarDecl(Id(taW), ArrayType([93.74], StringType), None, None)], Return(Id(R5Wk))), FuncDecl(Id(vtrA), [VarDecl(Id(lh), BoolType, None, None), VarDecl(Id(EWI), StringType, None, None), VarDecl(Id(YU), NumberType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115634))

	def test_21530115635(self):
		input = '''
func cq1 (string qLq[75.26,73.34])	return 54.16

func XHZB (string hi[27.7], string gR9[83.36,15.2,85.37])
	return f6
func Y5 ()	return
'''
		expect = '''Program([FuncDecl(Id(cq1), [VarDecl(Id(qLq), ArrayType([75.26, 73.34], StringType), None, None)], Return(NumLit(54.16))), FuncDecl(Id(XHZB), [VarDecl(Id(hi), ArrayType([27.7], StringType), None, None), VarDecl(Id(gR9), ArrayType([83.36, 15.2, 85.37], StringType), None, None)], Return(Id(f6))), FuncDecl(Id(Y5), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115635))

	def test_21530115636(self):
		input = '''
bool zP[86.36,7.59,44.55] <- 19.2
func uA (string B9q[75.15,47.08,78.78])
	begin
		JN(true, f2mr, "eiz")
		begin
		end
		string Gu[39.23]
	end

string R7g[90.5]
bool fy3F
func xHr (bool uzV, bool vP)	return
'''
		expect = '''Program([VarDecl(Id(zP), ArrayType([86.36, 7.59, 44.55], BoolType), None, NumLit(19.2)), FuncDecl(Id(uA), [VarDecl(Id(B9q), ArrayType([75.15, 47.08, 78.78], StringType), None, None)], Block([CallStmt(Id(JN), [BooleanLit(True), Id(f2mr), StringLit(eiz)]), Block([]), VarDecl(Id(Gu), ArrayType([39.23], StringType), None, None)])), VarDecl(Id(R7g), ArrayType([90.5], StringType), None, None), VarDecl(Id(fy3F), BoolType, None, None), FuncDecl(Id(xHr), [VarDecl(Id(uzV), BoolType, None, None), VarDecl(Id(vP), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115636))

	def test_21530115637(self):
		input = '''
func oqS ()	return vK

var Fcv <- 99.98
func T3ri ()	return "C"

func LHLT (number jCg, string lWY, string dZvS[47.73])	begin
		return "H"
		ZP(85.36)
		tj4[false, 23.46] <- true
	end
func y4v ()
	return
'''
		expect = '''Program([FuncDecl(Id(oqS), [], Return(Id(vK))), VarDecl(Id(Fcv), None, var, NumLit(99.98)), FuncDecl(Id(T3ri), [], Return(StringLit(C))), FuncDecl(Id(LHLT), [VarDecl(Id(jCg), NumberType, None, None), VarDecl(Id(lWY), StringType, None, None), VarDecl(Id(dZvS), ArrayType([47.73], StringType), None, None)], Block([Return(StringLit(H)), CallStmt(Id(ZP), [NumLit(85.36)]), AssignStmt(ArrayCell(Id(tj4), [BooleanLit(False), NumLit(23.46)]), BooleanLit(True))])), FuncDecl(Id(y4v), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115637))

	def test_21530115638(self):
		input = '''
bool gv[7.46]
'''
		expect = '''Program([VarDecl(Id(gv), ArrayType([7.46], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115638))

	def test_21530115639(self):
		input = '''
number wGPE[35.19,49.03,3.39] <- "d"
func EP (bool Gi[77.78])	return

func Q_z (string ncV, number VYA[74.58])	begin
		number by4_[64.54,33.86,93.49] <- "HbGg"
		if (true) begin
			continue
			if (GZ_) continue
			elif (16.48)
			break
			elif (v2jj)
			continue
			elif (22.72) continue
			else dynamic c7s <- N77Y
		end
		else hO <- ajf
	end
'''
		expect = '''Program([VarDecl(Id(wGPE), ArrayType([35.19, 49.03, 3.39], NumberType), None, StringLit(d)), FuncDecl(Id(EP), [VarDecl(Id(Gi), ArrayType([77.78], BoolType), None, None)], Return()), FuncDecl(Id(Q_z), [VarDecl(Id(ncV), StringType, None, None), VarDecl(Id(VYA), ArrayType([74.58], NumberType), None, None)], Block([VarDecl(Id(by4_), ArrayType([64.54, 33.86, 93.49], NumberType), None, StringLit(HbGg)), If(BooleanLit(True), Block([Continue, If(Id(GZ_), Continue), [(NumLit(16.48), Break), (Id(v2jj), Continue), (NumLit(22.72), Continue)], VarDecl(Id(c7s), None, dynamic, Id(N77Y))])), [], AssignStmt(Id(hO), Id(ajf))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115639))

	def test_21530115640(self):
		input = '''
func agxi ()	return

func bs (string kr[31.51])
	return
bool IvHG[91.76,75.03,73.11]
func jQhT (string U1[32.33,88.92])
	return "G"
string Rs[76.65]
'''
		expect = '''Program([FuncDecl(Id(agxi), [], Return()), FuncDecl(Id(bs), [VarDecl(Id(kr), ArrayType([31.51], StringType), None, None)], Return()), VarDecl(Id(IvHG), ArrayType([91.76, 75.03, 73.11], BoolType), None, None), FuncDecl(Id(jQhT), [VarDecl(Id(U1), ArrayType([32.33, 88.92], StringType), None, None)], Return(StringLit(G))), VarDecl(Id(Rs), ArrayType([76.65], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115640))

	def test_21530115641(self):
		input = '''
var tT <- false
bool yFC3[79.86]
dynamic gyhb <- false
'''
		expect = '''Program([VarDecl(Id(tT), None, var, BooleanLit(False)), VarDecl(Id(yFC3), ArrayType([79.86], BoolType), None, None), VarDecl(Id(gyhb), None, dynamic, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115641))

	def test_21530115642(self):
		input = '''
func U0 (number ha[35.52])
	return false
'''
		expect = '''Program([FuncDecl(Id(U0), [VarDecl(Id(ha), ArrayType([35.52], NumberType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115642))

	def test_21530115643(self):
		input = '''
func Jb8 (string dh, bool VEcz)	return true
number onS <- true
'''
		expect = '''Program([FuncDecl(Id(Jb8), [VarDecl(Id(dh), StringType, None, None), VarDecl(Id(VEcz), BoolType, None, None)], Return(BooleanLit(True))), VarDecl(Id(onS), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115643))

	def test_21530115644(self):
		input = '''
func jE (number GYoK, bool Ybd, number u9[26.59,23.92])
	return "ff"

func BXCx (number Ouof[84.77], number s5Af[16.32])	return true
bool T3A[38.55]
number i9 <- 91.93
'''
		expect = '''Program([FuncDecl(Id(jE), [VarDecl(Id(GYoK), NumberType, None, None), VarDecl(Id(Ybd), BoolType, None, None), VarDecl(Id(u9), ArrayType([26.59, 23.92], NumberType), None, None)], Return(StringLit(ff))), FuncDecl(Id(BXCx), [VarDecl(Id(Ouof), ArrayType([84.77], NumberType), None, None), VarDecl(Id(s5Af), ArrayType([16.32], NumberType), None, None)], Return(BooleanLit(True))), VarDecl(Id(T3A), ArrayType([38.55], BoolType), None, None), VarDecl(Id(i9), NumberType, None, NumLit(91.93))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115644))

	def test_21530115645(self):
		input = '''
func aR (bool tI2)	return

func bF (string HPUx[8.03,56.97])
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(aR), [VarDecl(Id(tI2), BoolType, None, None)], Return()), FuncDecl(Id(bF), [VarDecl(Id(HPUx), ArrayType([8.03, 56.97], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115645))

	def test_21530115646(self):
		input = '''
func r85f (bool kxEh[67.79], number fKbj[4.45], number fV07)
	begin
	end

number Ig
func B3U3 ()	return "NyuV"

func cF04 (number k1i, string kE)	return 43.92

'''
		expect = '''Program([FuncDecl(Id(r85f), [VarDecl(Id(kxEh), ArrayType([67.79], BoolType), None, None), VarDecl(Id(fKbj), ArrayType([4.45], NumberType), None, None), VarDecl(Id(fV07), NumberType, None, None)], Block([])), VarDecl(Id(Ig), NumberType, None, None), FuncDecl(Id(B3U3), [], Return(StringLit(NyuV))), FuncDecl(Id(cF04), [VarDecl(Id(k1i), NumberType, None, None), VarDecl(Id(kE), StringType, None, None)], Return(NumLit(43.92)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115646))

	def test_21530115647(self):
		input = '''
bool jqa
dynamic YI
func K1o (number ILgo[88.7], number psL, number jd)
	return true
dynamic Jy
var Gw <- false
'''
		expect = '''Program([VarDecl(Id(jqa), BoolType, None, None), VarDecl(Id(YI), None, dynamic, None), FuncDecl(Id(K1o), [VarDecl(Id(ILgo), ArrayType([88.7], NumberType), None, None), VarDecl(Id(psL), NumberType, None, None), VarDecl(Id(jd), NumberType, None, None)], Return(BooleanLit(True))), VarDecl(Id(Jy), None, dynamic, None), VarDecl(Id(Gw), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115647))

	def test_21530115648(self):
		input = '''
bool VT8U <- 86.53
'''
		expect = '''Program([VarDecl(Id(VT8U), BoolType, None, NumLit(86.53))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115648))

	def test_21530115649(self):
		input = '''
func F_ ()	begin
		begin
			break
		end
		break
	end

'''
		expect = '''Program([FuncDecl(Id(F_), [], Block([Block([Break]), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115649))

	def test_21530115650(self):
		input = '''
number tfx <- "IKNPH"
string cC
bool JG[95.94,14.2]
func MI (string yK6, number gUWx[1.43])
	return mD
'''
		expect = '''Program([VarDecl(Id(tfx), NumberType, None, StringLit(IKNPH)), VarDecl(Id(cC), StringType, None, None), VarDecl(Id(JG), ArrayType([95.94, 14.2], BoolType), None, None), FuncDecl(Id(MI), [VarDecl(Id(yK6), StringType, None, None), VarDecl(Id(gUWx), ArrayType([1.43], NumberType), None, None)], Return(Id(mD)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115650))

	def test_21530115651(self):
		input = '''
string Qfj[43.73,28.71]
number iO[21.82]
'''
		expect = '''Program([VarDecl(Id(Qfj), ArrayType([43.73, 28.71], StringType), None, None), VarDecl(Id(iO), ArrayType([21.82], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115651))

	def test_21530115652(self):
		input = '''
string ZlNL[42.63,73.72] <- JuaM
number ur2c[36.25,43.63,77.81] <- false
dynamic rE
'''
		expect = '''Program([VarDecl(Id(ZlNL), ArrayType([42.63, 73.72], StringType), None, Id(JuaM)), VarDecl(Id(ur2c), ArrayType([36.25, 43.63, 77.81], NumberType), None, BooleanLit(False)), VarDecl(Id(rE), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115652))

	def test_21530115653(self):
		input = '''
func qUVI (bool WT)
	return

'''
		expect = '''Program([FuncDecl(Id(qUVI), [VarDecl(Id(WT), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115653))

	def test_21530115654(self):
		input = '''
func iA (number Yn, bool E3cF, bool bu5[69.46,73.65,15.1])	return false

func ElL (bool W5[37.87,97.27], bool rLxd)
	return true

func Zr9 (bool ocP)	begin
		QhRe(pA8c, 37.51, "l")
		bool jL[60.17,88.96,40.27]
		td(62.62, YZ, CRvd)
	end
number is
bool W9 <- 47.56
'''
		expect = '''Program([FuncDecl(Id(iA), [VarDecl(Id(Yn), NumberType, None, None), VarDecl(Id(E3cF), BoolType, None, None), VarDecl(Id(bu5), ArrayType([69.46, 73.65, 15.1], BoolType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(ElL), [VarDecl(Id(W5), ArrayType([37.87, 97.27], BoolType), None, None), VarDecl(Id(rLxd), BoolType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(Zr9), [VarDecl(Id(ocP), BoolType, None, None)], Block([CallStmt(Id(QhRe), [Id(pA8c), NumLit(37.51), StringLit(l)]), VarDecl(Id(jL), ArrayType([60.17, 88.96, 40.27], BoolType), None, None), CallStmt(Id(td), [NumLit(62.62), Id(YZ), Id(CRvd)])])), VarDecl(Id(is), NumberType, None, None), VarDecl(Id(W9), BoolType, None, NumLit(47.56))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115654))

	def test_21530115655(self):
		input = '''
func N6 (bool NgE, bool jga, string OWd6[30.67])	begin
		return
		begin
			jH <- 99.45
		end
	end
number LB[21.89]
func jHJe (bool Hb[59.9,58.85,33.08], number v1)
	begin
		for eo8z until Ya by "iWaK"
			VH["lAhCB", 98.43, 55.02] <- "R"
		begin
			continue
		end
	end
'''
		expect = '''Program([FuncDecl(Id(N6), [VarDecl(Id(NgE), BoolType, None, None), VarDecl(Id(jga), BoolType, None, None), VarDecl(Id(OWd6), ArrayType([30.67], StringType), None, None)], Block([Return(), Block([AssignStmt(Id(jH), NumLit(99.45))])])), VarDecl(Id(LB), ArrayType([21.89], NumberType), None, None), FuncDecl(Id(jHJe), [VarDecl(Id(Hb), ArrayType([59.9, 58.85, 33.08], BoolType), None, None), VarDecl(Id(v1), NumberType, None, None)], Block([For(Id(eo8z), Id(Ya), StringLit(iWaK), AssignStmt(ArrayCell(Id(VH), [StringLit(lAhCB), NumLit(98.43), NumLit(55.02)]), StringLit(R))), Block([Continue])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115655))

	def test_21530115656(self):
		input = '''
func QiV (string ZmaG, number SkjN[19.38], string eQm[86.4,47.77])
	begin
		continue
		if ("IylG")
		continue
		elif ("co")
		break
		elif (d03)
		break
		elif ("fDE")
		continue
		else return
	end
func v6J ()
	return 94.12
string Cdu[90.97] <- "ZWY"
func b0d (bool q_Um, string smfM)
	return
func M7 ()	return
'''
		expect = '''Program([FuncDecl(Id(QiV), [VarDecl(Id(ZmaG), StringType, None, None), VarDecl(Id(SkjN), ArrayType([19.38], NumberType), None, None), VarDecl(Id(eQm), ArrayType([86.4, 47.77], StringType), None, None)], Block([Continue, If(StringLit(IylG), Continue), [(StringLit(co), Break), (Id(d03), Break), (StringLit(fDE), Continue)], Return()])), FuncDecl(Id(v6J), [], Return(NumLit(94.12))), VarDecl(Id(Cdu), ArrayType([90.97], StringType), None, StringLit(ZWY)), FuncDecl(Id(b0d), [VarDecl(Id(q_Um), BoolType, None, None), VarDecl(Id(smfM), StringType, None, None)], Return()), FuncDecl(Id(M7), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115656))

	def test_21530115657(self):
		input = '''
func hl (number knlY[12.89], number v5j[62.19])	return ndLr
func a6 (bool W0D[67.75])
	return

string ra[15.3,96.29] <- 56.24
bool oBC[84.1,74.69]
number xu[25.83,70.68,60.13]
'''
		expect = '''Program([FuncDecl(Id(hl), [VarDecl(Id(knlY), ArrayType([12.89], NumberType), None, None), VarDecl(Id(v5j), ArrayType([62.19], NumberType), None, None)], Return(Id(ndLr))), FuncDecl(Id(a6), [VarDecl(Id(W0D), ArrayType([67.75], BoolType), None, None)], Return()), VarDecl(Id(ra), ArrayType([15.3, 96.29], StringType), None, NumLit(56.24)), VarDecl(Id(oBC), ArrayType([84.1, 74.69], BoolType), None, None), VarDecl(Id(xu), ArrayType([25.83, 70.68, 60.13], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115657))

	def test_21530115658(self):
		input = '''
string a1mK
bool kSy[3.34,42.2,34.81]
number q5[30.88,80.88] <- false
var HS <- uVL
bool jAP[44.12]
'''
		expect = '''Program([VarDecl(Id(a1mK), StringType, None, None), VarDecl(Id(kSy), ArrayType([3.34, 42.2, 34.81], BoolType), None, None), VarDecl(Id(q5), ArrayType([30.88, 80.88], NumberType), None, BooleanLit(False)), VarDecl(Id(HS), None, var, Id(uVL)), VarDecl(Id(jAP), ArrayType([44.12], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115658))

	def test_21530115659(self):
		input = '''
number tlA[77.81,19.59] <- "ObfD"
func WAp ()
	begin
		return true
		break
	end
func B_xL (bool qTZn[57.71,54.3], number HD, bool YUZ[57.57,21.6,11.9])	return "BV"
'''
		expect = '''Program([VarDecl(Id(tlA), ArrayType([77.81, 19.59], NumberType), None, StringLit(ObfD)), FuncDecl(Id(WAp), [], Block([Return(BooleanLit(True)), Break])), FuncDecl(Id(B_xL), [VarDecl(Id(qTZn), ArrayType([57.71, 54.3], BoolType), None, None), VarDecl(Id(HD), NumberType, None, None), VarDecl(Id(YUZ), ArrayType([57.57, 21.6, 11.9], BoolType), None, None)], Return(StringLit(BV)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115659))

	def test_21530115660(self):
		input = '''
func teZ (bool eh[10.96,57.93])
	return 32.24

'''
		expect = '''Program([FuncDecl(Id(teZ), [VarDecl(Id(eh), ArrayType([10.96, 57.93], BoolType), None, None)], Return(NumLit(32.24)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115660))

	def test_21530115661(self):
		input = '''
bool uO[88.54,85.95] <- SkJ
func sYL (bool mdG5[34.27,3.8])	begin
		for aMC until kZar by "m"
			Pqq()
		bool oB
		break
	end
bool mt <- "Q"
'''
		expect = '''Program([VarDecl(Id(uO), ArrayType([88.54, 85.95], BoolType), None, Id(SkJ)), FuncDecl(Id(sYL), [VarDecl(Id(mdG5), ArrayType([34.27, 3.8], BoolType), None, None)], Block([For(Id(aMC), Id(kZar), StringLit(m), CallStmt(Id(Pqq), [])), VarDecl(Id(oB), BoolType, None, None), Break])), VarDecl(Id(mt), BoolType, None, StringLit(Q))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115661))

	def test_21530115662(self):
		input = '''
func ith ()
	return

func p9 (string ANV, bool rWO)	begin
		begin
			begin
				begin
					continue
					for MVCB until true by false
						return false
					return NS
				end
				break
			end
			qa(74.22)
			number IpB
		end
		begin
			if (true) break
			elif (QBbv) return "Ob"
			elif (Usrt)
			if (true)
			return
			elif ("vq") return
			elif ("R") kdX()
			elif (24.4) for VP until "gwxSj" by false
				continue
			elif ("lCb") continue
			else continue
			begin
				FwhJ <- MjV
			end
			begin
			end
		end
		P0xs <- true
	end
func ur (string gco6[25.85,0.72,42.19])	return "tTf"
string KX <- 31.08
number ivte <- "JA"
'''
		expect = '''Program([FuncDecl(Id(ith), [], Return()), FuncDecl(Id(p9), [VarDecl(Id(ANV), StringType, None, None), VarDecl(Id(rWO), BoolType, None, None)], Block([Block([Block([Block([Continue, For(Id(MVCB), BooleanLit(True), BooleanLit(False), Return(BooleanLit(False))), Return(Id(NS))]), Break]), CallStmt(Id(qa), [NumLit(74.22)]), VarDecl(Id(IpB), NumberType, None, None)]), Block([If(BooleanLit(True), Break), [(Id(QBbv), Return(StringLit(Ob))), (Id(Usrt), If(BooleanLit(True), Return()), [(StringLit(vq), Return()), (StringLit(R), CallStmt(Id(kdX), [])), (NumLit(24.4), For(Id(VP), StringLit(gwxSj), BooleanLit(False), Continue)), (StringLit(lCb), Continue)], Continue)], None, Block([AssignStmt(Id(FwhJ), Id(MjV))]), Block([])]), AssignStmt(Id(P0xs), BooleanLit(True))])), FuncDecl(Id(ur), [VarDecl(Id(gco6), ArrayType([25.85, 0.72, 42.19], StringType), None, None)], Return(StringLit(tTf))), VarDecl(Id(KX), StringType, None, NumLit(31.08)), VarDecl(Id(ivte), NumberType, None, StringLit(JA))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115662))

	def test_21530115663(self):
		input = '''
string mJyR <- "y"
func MRx ()
	begin
		return true
		return
	end
var z94 <- "t"
func lTq (bool xgq[57.76])	return
bool J8FQ[38.51,68.35,23.14]
'''
		expect = '''Program([VarDecl(Id(mJyR), StringType, None, StringLit(y)), FuncDecl(Id(MRx), [], Block([Return(BooleanLit(True)), Return()])), VarDecl(Id(z94), None, var, StringLit(t)), FuncDecl(Id(lTq), [VarDecl(Id(xgq), ArrayType([57.76], BoolType), None, None)], Return()), VarDecl(Id(J8FQ), ArrayType([38.51, 68.35, 23.14], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115663))

	def test_21530115664(self):
		input = '''
func VZ (string L8XM[23.3,70.16,21.62], string ukE1)	begin
	end
number Ilx[71.12,50.42,45.76]
func r6 ()	begin
		break
	end

func ml (bool ssj, string S6lz[79.13], bool NM8D[55.14])	return
'''
		expect = '''Program([FuncDecl(Id(VZ), [VarDecl(Id(L8XM), ArrayType([23.3, 70.16, 21.62], StringType), None, None), VarDecl(Id(ukE1), StringType, None, None)], Block([])), VarDecl(Id(Ilx), ArrayType([71.12, 50.42, 45.76], NumberType), None, None), FuncDecl(Id(r6), [], Block([Break])), FuncDecl(Id(ml), [VarDecl(Id(ssj), BoolType, None, None), VarDecl(Id(S6lz), ArrayType([79.13], StringType), None, None), VarDecl(Id(NM8D), ArrayType([55.14], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115664))

	def test_21530115665(self):
		input = '''
bool wic
func sh (bool d5lO, number gkA[77.34])
	begin
		for WW until 21.97 by "Xa"
			bool OYv <- true
		if (true) if (4.28) return
		elif (true) break
		elif (84.59) string CA[50.67,53.14,19.7] <- vp8p
		elif (false)
		number hC6e[14.65]
		else if (false)
		return 89.68
		elif (62.47)
		K_x8(false)
		elif (42.97) number mDZ
	end

number WWRo[66.09,99.55,91.15]
'''
		expect = '''Program([VarDecl(Id(wic), BoolType, None, None), FuncDecl(Id(sh), [VarDecl(Id(d5lO), BoolType, None, None), VarDecl(Id(gkA), ArrayType([77.34], NumberType), None, None)], Block([For(Id(WW), NumLit(21.97), StringLit(Xa), VarDecl(Id(OYv), BoolType, None, BooleanLit(True))), If(BooleanLit(True), If(NumLit(4.28), Return()), [(BooleanLit(True), Break), (NumLit(84.59), VarDecl(Id(CA), ArrayType([50.67, 53.14, 19.7], StringType), None, Id(vp8p))), (BooleanLit(False), VarDecl(Id(hC6e), ArrayType([14.65], NumberType), None, None))], If(BooleanLit(False), Return(NumLit(89.68))), [(NumLit(62.47), CallStmt(Id(K_x8), [BooleanLit(False)])), (NumLit(42.97), VarDecl(Id(mDZ), NumberType, None, None))], None), [], None])), VarDecl(Id(WWRo), ArrayType([66.09, 99.55, 91.15], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115665))

	def test_21530115666(self):
		input = '''
func VV0 (bool WeC, bool uwDF)
	return false

number ZbD[26.86,7.76,68.18]
string PXp <- 24.47
string TSol[70.79] <- 54.92
string eJ
'''
		expect = '''Program([FuncDecl(Id(VV0), [VarDecl(Id(WeC), BoolType, None, None), VarDecl(Id(uwDF), BoolType, None, None)], Return(BooleanLit(False))), VarDecl(Id(ZbD), ArrayType([26.86, 7.76, 68.18], NumberType), None, None), VarDecl(Id(PXp), StringType, None, NumLit(24.47)), VarDecl(Id(TSol), ArrayType([70.79], StringType), None, NumLit(54.92)), VarDecl(Id(eJ), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115666))

	def test_21530115667(self):
		input = '''
bool hyss[25.21,83.49,73.11] <- 88.34
string HpQi
'''
		expect = '''Program([VarDecl(Id(hyss), ArrayType([25.21, 83.49, 73.11], BoolType), None, NumLit(88.34)), VarDecl(Id(HpQi), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115667))

	def test_21530115668(self):
		input = '''
number OQa_
dynamic Kmlb
func JxE (number H9, bool IK4v)
	return 37.23

func oK (bool jd[85.23], bool d8M1[75.24], number ByAQ)	return
'''
		expect = '''Program([VarDecl(Id(OQa_), NumberType, None, None), VarDecl(Id(Kmlb), None, dynamic, None), FuncDecl(Id(JxE), [VarDecl(Id(H9), NumberType, None, None), VarDecl(Id(IK4v), BoolType, None, None)], Return(NumLit(37.23))), FuncDecl(Id(oK), [VarDecl(Id(jd), ArrayType([85.23], BoolType), None, None), VarDecl(Id(d8M1), ArrayType([75.24], BoolType), None, None), VarDecl(Id(ByAQ), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115668))

	def test_21530115669(self):
		input = '''
number HaHq
func kMcI ()	begin
		yqis(false, false)
		continue
		return T7C
	end
func AWq (number eeM, string f5[94.14,72.68,61.57])
	return Lipn

func um1 (string uB, bool n04, bool e5t[9.48,54.95])	begin
	end

'''
		expect = '''Program([VarDecl(Id(HaHq), NumberType, None, None), FuncDecl(Id(kMcI), [], Block([CallStmt(Id(yqis), [BooleanLit(False), BooleanLit(False)]), Continue, Return(Id(T7C))])), FuncDecl(Id(AWq), [VarDecl(Id(eeM), NumberType, None, None), VarDecl(Id(f5), ArrayType([94.14, 72.68, 61.57], StringType), None, None)], Return(Id(Lipn))), FuncDecl(Id(um1), [VarDecl(Id(uB), StringType, None, None), VarDecl(Id(n04), BoolType, None, None), VarDecl(Id(e5t), ArrayType([9.48, 54.95], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115669))

	def test_21530115670(self):
		input = '''
func GyJ8 ()
	return
func CL (number XF, number r6q[10.68,80.29])
	return
func fvU ()	begin
		return
		if (67.07) Yh7 <- "DqrCv"
		else Ixa(c3)
	end

func EWp (number d00[53.06,16.45], number v_z)
	return false
'''
		expect = '''Program([FuncDecl(Id(GyJ8), [], Return()), FuncDecl(Id(CL), [VarDecl(Id(XF), NumberType, None, None), VarDecl(Id(r6q), ArrayType([10.68, 80.29], NumberType), None, None)], Return()), FuncDecl(Id(fvU), [], Block([Return(), If(NumLit(67.07), AssignStmt(Id(Yh7), StringLit(DqrCv))), [], CallStmt(Id(Ixa), [Id(c3)])])), FuncDecl(Id(EWp), [VarDecl(Id(d00), ArrayType([53.06, 16.45], NumberType), None, None), VarDecl(Id(v_z), NumberType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115670))

	def test_21530115671(self):
		input = '''
string At[5.53,79.63,37.02]
func vaSl (number M4A[24.89,37.25,65.85])
	begin
		continue
		number AQM[41.73] <- false
	end

'''
		expect = '''Program([VarDecl(Id(At), ArrayType([5.53, 79.63, 37.02], StringType), None, None), FuncDecl(Id(vaSl), [VarDecl(Id(M4A), ArrayType([24.89, 37.25, 65.85], NumberType), None, None)], Block([Continue, VarDecl(Id(AQM), ArrayType([41.73], NumberType), None, BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115671))

	def test_21530115672(self):
		input = '''
string U5f[95.59,55.28] <- Uxx
bool PuS[19.99] <- 45.81
number Mr2P[71.69,24.14] <- TXA
func Dc_f ()	return "hB"
func CnI (string gkz[19.13], bool PGj1, bool U3[38.17])
	return

'''
		expect = '''Program([VarDecl(Id(U5f), ArrayType([95.59, 55.28], StringType), None, Id(Uxx)), VarDecl(Id(PuS), ArrayType([19.99], BoolType), None, NumLit(45.81)), VarDecl(Id(Mr2P), ArrayType([71.69, 24.14], NumberType), None, Id(TXA)), FuncDecl(Id(Dc_f), [], Return(StringLit(hB))), FuncDecl(Id(CnI), [VarDecl(Id(gkz), ArrayType([19.13], StringType), None, None), VarDecl(Id(PGj1), BoolType, None, None), VarDecl(Id(U3), ArrayType([38.17], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115672))

	def test_21530115673(self):
		input = '''
func RI (bool e2[45.87,18.84])
	return
'''
		expect = '''Program([FuncDecl(Id(RI), [VarDecl(Id(e2), ArrayType([45.87, 18.84], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115673))

	def test_21530115674(self):
		input = '''
number NJ <- 81.16
'''
		expect = '''Program([VarDecl(Id(NJ), NumberType, None, NumLit(81.16))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115674))

	def test_21530115675(self):
		input = '''
func sf (bool Ig6)	return 66.95

'''
		expect = '''Program([FuncDecl(Id(sf), [VarDecl(Id(Ig6), BoolType, None, None)], Return(NumLit(66.95)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115675))

	def test_21530115676(self):
		input = '''
string PhD[66.34] <- "y"
number FPM[62.54,97.27] <- "SusQ"
'''
		expect = '''Program([VarDecl(Id(PhD), ArrayType([66.34], StringType), None, StringLit(y)), VarDecl(Id(FPM), ArrayType([62.54, 97.27], NumberType), None, StringLit(SusQ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115676))

	def test_21530115677(self):
		input = '''
dynamic uSrR
func Dn (string pVJ[12.98,67.68,64.93], number UBU[58.99], string RoEL)
	return

number SdH[80.1] <- true
'''
		expect = '''Program([VarDecl(Id(uSrR), None, dynamic, None), FuncDecl(Id(Dn), [VarDecl(Id(pVJ), ArrayType([12.98, 67.68, 64.93], StringType), None, None), VarDecl(Id(UBU), ArrayType([58.99], NumberType), None, None), VarDecl(Id(RoEL), StringType, None, None)], Return()), VarDecl(Id(SdH), ArrayType([80.1], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115677))

	def test_21530115678(self):
		input = '''
func dPAR (bool kfqd[24.4,87.96], number u0ja)	return zK5
string lezB[42.64]
var po5 <- "hjb"
func kC (number K1, bool AGPx, bool z6FS[87.97])
	return "QLpP"
func Lr (bool MU)
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(dPAR), [VarDecl(Id(kfqd), ArrayType([24.4, 87.96], BoolType), None, None), VarDecl(Id(u0ja), NumberType, None, None)], Return(Id(zK5))), VarDecl(Id(lezB), ArrayType([42.64], StringType), None, None), VarDecl(Id(po5), None, var, StringLit(hjb)), FuncDecl(Id(kC), [VarDecl(Id(K1), NumberType, None, None), VarDecl(Id(AGPx), BoolType, None, None), VarDecl(Id(z6FS), ArrayType([87.97], BoolType), None, None)], Return(StringLit(QLpP))), FuncDecl(Id(Lr), [VarDecl(Id(MU), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115678))

	def test_21530115679(self):
		input = '''
bool F_
var iuq <- bNN
'''
		expect = '''Program([VarDecl(Id(F_), BoolType, None, None), VarDecl(Id(iuq), None, var, Id(bNN))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115679))

	def test_21530115680(self):
		input = '''
func vj (bool XvE[35.34,24.78,23.77])	return 94.96

number I__[60.71,0.3]
'''
		expect = '''Program([FuncDecl(Id(vj), [VarDecl(Id(XvE), ArrayType([35.34, 24.78, 23.77], BoolType), None, None)], Return(NumLit(94.96))), VarDecl(Id(I__), ArrayType([60.71, 0.3], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115680))

	def test_21530115681(self):
		input = '''
func tvv (number eGWq[4.02])	begin
	end
func uGA (number pBQ8, number yMd2[36.05])	begin
		break
		JFEY()
	end

var IZ <- "wysZ"
number Vz1
var aSF <- false
'''
		expect = '''Program([FuncDecl(Id(tvv), [VarDecl(Id(eGWq), ArrayType([4.02], NumberType), None, None)], Block([])), FuncDecl(Id(uGA), [VarDecl(Id(pBQ8), NumberType, None, None), VarDecl(Id(yMd2), ArrayType([36.05], NumberType), None, None)], Block([Break, CallStmt(Id(JFEY), [])])), VarDecl(Id(IZ), None, var, StringLit(wysZ)), VarDecl(Id(Vz1), NumberType, None, None), VarDecl(Id(aSF), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115681))

	def test_21530115682(self):
		input = '''
func I6Ih (string Q5)
	return "izX"

string I2A9[62.37,90.04] <- tBC
number Jx[89.22]
func MQ (bool OGr, string vE[36.98])	begin
		string g2NM <- "w"
	end

'''
		expect = '''Program([FuncDecl(Id(I6Ih), [VarDecl(Id(Q5), StringType, None, None)], Return(StringLit(izX))), VarDecl(Id(I2A9), ArrayType([62.37, 90.04], StringType), None, Id(tBC)), VarDecl(Id(Jx), ArrayType([89.22], NumberType), None, None), FuncDecl(Id(MQ), [VarDecl(Id(OGr), BoolType, None, None), VarDecl(Id(vE), ArrayType([36.98], StringType), None, None)], Block([VarDecl(Id(g2NM), StringType, None, StringLit(w))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115682))

	def test_21530115683(self):
		input = '''
func GK (number LxaK[46.09,27.97])
	return true
bool aYZZ[72.94,57.92]
var jmP <- pAQX
'''
		expect = '''Program([FuncDecl(Id(GK), [VarDecl(Id(LxaK), ArrayType([46.09, 27.97], NumberType), None, None)], Return(BooleanLit(True))), VarDecl(Id(aYZZ), ArrayType([72.94, 57.92], BoolType), None, None), VarDecl(Id(jmP), None, var, Id(pAQX))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115683))

	def test_21530115684(self):
		input = '''
bool pqz6[74.42,71.95,90.95]
string qs22
func YO ()	begin
		zy_[82.64, QX, true] <- true
		begin
			MJ()
			OOjT[false, false] <- true
			mH()
		end
	end

number bh[66.31,30.75,95.92]
'''
		expect = '''Program([VarDecl(Id(pqz6), ArrayType([74.42, 71.95, 90.95], BoolType), None, None), VarDecl(Id(qs22), StringType, None, None), FuncDecl(Id(YO), [], Block([AssignStmt(ArrayCell(Id(zy_), [NumLit(82.64), Id(QX), BooleanLit(True)]), BooleanLit(True)), Block([CallStmt(Id(MJ), []), AssignStmt(ArrayCell(Id(OOjT), [BooleanLit(False), BooleanLit(False)]), BooleanLit(True)), CallStmt(Id(mH), [])])])), VarDecl(Id(bh), ArrayType([66.31, 30.75, 95.92], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115684))

	def test_21530115685(self):
		input = '''
number DhE[71.74,86.97]
'''
		expect = '''Program([VarDecl(Id(DhE), ArrayType([71.74, 86.97], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115685))

	def test_21530115686(self):
		input = '''
func y88 (number Zu, bool yzB[46.16], string SB)	return false
func N2Ed (string Rd[9.7,14.56], number upb[25.31,79.28,14.96])
	return RN1a

func CmNr (bool jqsQ[13.36], number lNeY[17.59,53.29], number iyh)	return

func yhP ()	begin
		number whf6 <- "AppIE"
	end
func lc (number Ja)
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(y88), [VarDecl(Id(Zu), NumberType, None, None), VarDecl(Id(yzB), ArrayType([46.16], BoolType), None, None), VarDecl(Id(SB), StringType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(N2Ed), [VarDecl(Id(Rd), ArrayType([9.7, 14.56], StringType), None, None), VarDecl(Id(upb), ArrayType([25.31, 79.28, 14.96], NumberType), None, None)], Return(Id(RN1a))), FuncDecl(Id(CmNr), [VarDecl(Id(jqsQ), ArrayType([13.36], BoolType), None, None), VarDecl(Id(lNeY), ArrayType([17.59, 53.29], NumberType), None, None), VarDecl(Id(iyh), NumberType, None, None)], Return()), FuncDecl(Id(yhP), [], Block([VarDecl(Id(whf6), NumberType, None, StringLit(AppIE))])), FuncDecl(Id(lc), [VarDecl(Id(Ja), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115686))

	def test_21530115687(self):
		input = '''
bool WRjZ
number OOFM <- "S"
dynamic b5 <- VJA
'''
		expect = '''Program([VarDecl(Id(WRjZ), BoolType, None, None), VarDecl(Id(OOFM), NumberType, None, StringLit(S)), VarDecl(Id(b5), None, dynamic, Id(VJA))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115687))

	def test_21530115688(self):
		input = '''
number FQe[65.71]
string boR[39.92,96.69]
'''
		expect = '''Program([VarDecl(Id(FQe), ArrayType([65.71], NumberType), None, None), VarDecl(Id(boR), ArrayType([39.92, 96.69], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115688))

	def test_21530115689(self):
		input = '''
func ci (number Tdv[55.77,82.81])	return
string fS
string GAJ
'''
		expect = '''Program([FuncDecl(Id(ci), [VarDecl(Id(Tdv), ArrayType([55.77, 82.81], NumberType), None, None)], Return()), VarDecl(Id(fS), StringType, None, None), VarDecl(Id(GAJ), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115689))

	def test_21530115690(self):
		input = '''
func LSq (string ddYa[63.33], number m1Qv[69.86,92.78,21.36], bool F07[83.3])	return V0
string eXV[28.92,89.23,4.95] <- "Wey"
func Nb3 ()	return
dynamic kqsB
number vpj[30.63,12.61] <- false
'''
		expect = '''Program([FuncDecl(Id(LSq), [VarDecl(Id(ddYa), ArrayType([63.33], StringType), None, None), VarDecl(Id(m1Qv), ArrayType([69.86, 92.78, 21.36], NumberType), None, None), VarDecl(Id(F07), ArrayType([83.3], BoolType), None, None)], Return(Id(V0))), VarDecl(Id(eXV), ArrayType([28.92, 89.23, 4.95], StringType), None, StringLit(Wey)), FuncDecl(Id(Nb3), [], Return()), VarDecl(Id(kqsB), None, dynamic, None), VarDecl(Id(vpj), ArrayType([30.63, 12.61], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115690))

	def test_21530115691(self):
		input = '''
func yjtg (number Uhs, string RAd)
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(yjtg), [VarDecl(Id(Uhs), NumberType, None, None), VarDecl(Id(RAd), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115691))

	def test_21530115692(self):
		input = '''
func sre1 (string PYVh[15.8], string A2, bool rDN[53.5])	return

string xyN[28.11,85.16,97.77] <- false
func qadt (bool dK, bool YF)	begin
	end

'''
		expect = '''Program([FuncDecl(Id(sre1), [VarDecl(Id(PYVh), ArrayType([15.8], StringType), None, None), VarDecl(Id(A2), StringType, None, None), VarDecl(Id(rDN), ArrayType([53.5], BoolType), None, None)], Return()), VarDecl(Id(xyN), ArrayType([28.11, 85.16, 97.77], StringType), None, BooleanLit(False)), FuncDecl(Id(qadt), [VarDecl(Id(dK), BoolType, None, None), VarDecl(Id(YF), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115692))

	def test_21530115693(self):
		input = '''
number bkmT[97.53,65.52,13.87] <- "FlDc"
bool Vg <- vw
func Soj (bool Wk37)
	return
string D9oG <- "ZDZ"
'''
		expect = '''Program([VarDecl(Id(bkmT), ArrayType([97.53, 65.52, 13.87], NumberType), None, StringLit(FlDc)), VarDecl(Id(Vg), BoolType, None, Id(vw)), FuncDecl(Id(Soj), [VarDecl(Id(Wk37), BoolType, None, None)], Return()), VarDecl(Id(D9oG), StringType, None, StringLit(ZDZ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115693))

	def test_21530115694(self):
		input = '''
func ZDMp (string I9qD[47.45,62.15], number Bw3, string bCii)	return true

func r3FO (bool k4U[1.53,28.05,64.42], number HW[96.56,42.29,20.34], number BD6T[48.66,32.1,67.43])	return

dynamic Ws
string wZE[47.05] <- false
number BhDG[26.47,26.88] <- "yPltT"
'''
		expect = '''Program([FuncDecl(Id(ZDMp), [VarDecl(Id(I9qD), ArrayType([47.45, 62.15], StringType), None, None), VarDecl(Id(Bw3), NumberType, None, None), VarDecl(Id(bCii), StringType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(r3FO), [VarDecl(Id(k4U), ArrayType([1.53, 28.05, 64.42], BoolType), None, None), VarDecl(Id(HW), ArrayType([96.56, 42.29, 20.34], NumberType), None, None), VarDecl(Id(BD6T), ArrayType([48.66, 32.1, 67.43], NumberType), None, None)], Return()), VarDecl(Id(Ws), None, dynamic, None), VarDecl(Id(wZE), ArrayType([47.05], StringType), None, BooleanLit(False)), VarDecl(Id(BhDG), ArrayType([26.47, 26.88], NumberType), None, StringLit(yPltT))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115694))

	def test_21530115695(self):
		input = '''
bool ieN[33.72,96.06,36.46] <- "hTQ"
func b0 (string Shp)
	return "ZyUx"

func bhl (string XyW[86.19], bool d8r, bool w4Z)	begin
	end

'''
		expect = '''Program([VarDecl(Id(ieN), ArrayType([33.72, 96.06, 36.46], BoolType), None, StringLit(hTQ)), FuncDecl(Id(b0), [VarDecl(Id(Shp), StringType, None, None)], Return(StringLit(ZyUx))), FuncDecl(Id(bhl), [VarDecl(Id(XyW), ArrayType([86.19], StringType), None, None), VarDecl(Id(d8r), BoolType, None, None), VarDecl(Id(w4Z), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115695))

	def test_21530115696(self):
		input = '''
func NJZ (bool Wy)
	return "PGVu"
dynamic kUG <- 23.94
var viOQ <- false
'''
		expect = '''Program([FuncDecl(Id(NJZ), [VarDecl(Id(Wy), BoolType, None, None)], Return(StringLit(PGVu))), VarDecl(Id(kUG), None, dynamic, NumLit(23.94)), VarDecl(Id(viOQ), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115696))

	def test_21530115697(self):
		input = '''
func rG (number U3X)	return "QSStv"

func Z4Mo (string ts[46.01], bool euar, bool aSqy)
	return "y"
func DVH (number wr[94.97,38.85], string cB)
	return

bool z9cC[22.14,86.12,66.91] <- "HVmb"
'''
		expect = '''Program([FuncDecl(Id(rG), [VarDecl(Id(U3X), NumberType, None, None)], Return(StringLit(QSStv))), FuncDecl(Id(Z4Mo), [VarDecl(Id(ts), ArrayType([46.01], StringType), None, None), VarDecl(Id(euar), BoolType, None, None), VarDecl(Id(aSqy), BoolType, None, None)], Return(StringLit(y))), FuncDecl(Id(DVH), [VarDecl(Id(wr), ArrayType([94.97, 38.85], NumberType), None, None), VarDecl(Id(cB), StringType, None, None)], Return()), VarDecl(Id(z9cC), ArrayType([22.14, 86.12, 66.91], BoolType), None, StringLit(HVmb))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115697))

	def test_21530115698(self):
		input = '''
dynamic mq <- "us"
func wD (number O9, bool Rkjk, bool a8HM[46.31,84.33,44.08])
	return

string o2L[78.46,99.38] <- true
'''
		expect = '''Program([VarDecl(Id(mq), None, dynamic, StringLit(us)), FuncDecl(Id(wD), [VarDecl(Id(O9), NumberType, None, None), VarDecl(Id(Rkjk), BoolType, None, None), VarDecl(Id(a8HM), ArrayType([46.31, 84.33, 44.08], BoolType), None, None)], Return()), VarDecl(Id(o2L), ArrayType([78.46, 99.38], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115698))

	def test_21530115699(self):
		input = '''
string b9ps[49.82] <- false
bool ud[8.05] <- "Z"
func sOYq ()
	return
string NgKq
string oNQA
'''
		expect = '''Program([VarDecl(Id(b9ps), ArrayType([49.82], StringType), None, BooleanLit(False)), VarDecl(Id(ud), ArrayType([8.05], BoolType), None, StringLit(Z)), FuncDecl(Id(sOYq), [], Return()), VarDecl(Id(NgKq), StringType, None, None), VarDecl(Id(oNQA), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115699))

	def test_21530115700(self):
		input = '''
number wuG[33.7,48.54]
'''
		expect = '''Program([VarDecl(Id(wuG), ArrayType([33.7, 48.54], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115700))

	def test_21530115701(self):
		input = '''
bool vuW1[47.96,78.51,70.73] <- 11.44
'''
		expect = '''Program([VarDecl(Id(vuW1), ArrayType([47.96, 78.51, 70.73], BoolType), None, NumLit(11.44))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115701))

	def test_21530115702(self):
		input = '''
bool pe[96.94,81.18] <- false
var lcs <- 95.49
func cp (bool AU, bool nPU)	begin
		return
		begin
			tIR1()
		end
		for rI until WWNA by jiC0
			break
	end

number UO[7.44,45.61]
bool ojot[71.61,59.68]
'''
		expect = '''Program([VarDecl(Id(pe), ArrayType([96.94, 81.18], BoolType), None, BooleanLit(False)), VarDecl(Id(lcs), None, var, NumLit(95.49)), FuncDecl(Id(cp), [VarDecl(Id(AU), BoolType, None, None), VarDecl(Id(nPU), BoolType, None, None)], Block([Return(), Block([CallStmt(Id(tIR1), [])]), For(Id(rI), Id(WWNA), Id(jiC0), Break)])), VarDecl(Id(UO), ArrayType([7.44, 45.61], NumberType), None, None), VarDecl(Id(ojot), ArrayType([71.61, 59.68], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115702))

	def test_21530115703(self):
		input = '''
bool O5js[13.17] <- true
func cue1 ()	return

string D4OJ[68.12,90.79]
func aQ4N (string HFVa[56.85], string ycfB, number Jr[62.48,59.32,26.78])	return "R"

number Z6l[52.35,12.03,82.31]
'''
		expect = '''Program([VarDecl(Id(O5js), ArrayType([13.17], BoolType), None, BooleanLit(True)), FuncDecl(Id(cue1), [], Return()), VarDecl(Id(D4OJ), ArrayType([68.12, 90.79], StringType), None, None), FuncDecl(Id(aQ4N), [VarDecl(Id(HFVa), ArrayType([56.85], StringType), None, None), VarDecl(Id(ycfB), StringType, None, None), VarDecl(Id(Jr), ArrayType([62.48, 59.32, 26.78], NumberType), None, None)], Return(StringLit(R))), VarDecl(Id(Z6l), ArrayType([52.35, 12.03, 82.31], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115703))

	def test_21530115704(self):
		input = '''
bool BkjD[10.51,24.37,61.69] <- lnw
number iN[4.82,80.03,78.23]
number OxZx[71.5,15.49]
'''
		expect = '''Program([VarDecl(Id(BkjD), ArrayType([10.51, 24.37, 61.69], BoolType), None, Id(lnw)), VarDecl(Id(iN), ArrayType([4.82, 80.03, 78.23], NumberType), None, None), VarDecl(Id(OxZx), ArrayType([71.5, 15.49], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115704))

	def test_21530115705(self):
		input = '''
func alUR (number oL1e, string Ns[51.23,42.5,94.55])
	return
func ZHV ()	begin
	end

string HkM <- TUg
'''
		expect = '''Program([FuncDecl(Id(alUR), [VarDecl(Id(oL1e), NumberType, None, None), VarDecl(Id(Ns), ArrayType([51.23, 42.5, 94.55], StringType), None, None)], Return()), FuncDecl(Id(ZHV), [], Block([])), VarDecl(Id(HkM), StringType, None, Id(TUg))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115705))

	def test_21530115706(self):
		input = '''
func Rf ()	return

func oX (number EH, string vC, bool f6M)
	begin
		if ("yAb") break
		elif (iiz3) return
		elif ("ybbdx") dynamic RrE
		elif ("y")
		continue
		continue
	end

'''
		expect = '''Program([FuncDecl(Id(Rf), [], Return()), FuncDecl(Id(oX), [VarDecl(Id(EH), NumberType, None, None), VarDecl(Id(vC), StringType, None, None), VarDecl(Id(f6M), BoolType, None, None)], Block([If(StringLit(yAb), Break), [(Id(iiz3), Return()), (StringLit(ybbdx), VarDecl(Id(RrE), None, dynamic, None)), (StringLit(y), Continue)], None, Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115706))

	def test_21530115707(self):
		input = '''
func aq (string IR, number oNS, bool LGWR[31.57,57.46,48.76])	return EruN

func A1 (number q_)	begin
		return false
		rlE()
	end

number vyb[17.21,64.4,64.26]
'''
		expect = '''Program([FuncDecl(Id(aq), [VarDecl(Id(IR), StringType, None, None), VarDecl(Id(oNS), NumberType, None, None), VarDecl(Id(LGWR), ArrayType([31.57, 57.46, 48.76], BoolType), None, None)], Return(Id(EruN))), FuncDecl(Id(A1), [VarDecl(Id(q_), NumberType, None, None)], Block([Return(BooleanLit(False)), CallStmt(Id(rlE), [])])), VarDecl(Id(vyb), ArrayType([17.21, 64.4, 64.26], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115707))

	def test_21530115708(self):
		input = '''
func mo9Z (number hx[49.18,87.0,25.92], number rpL, string jdJ)	return

func dUdW (bool tNXY, string DN7L[20.08,5.58])
	return
'''
		expect = '''Program([FuncDecl(Id(mo9Z), [VarDecl(Id(hx), ArrayType([49.18, 87.0, 25.92], NumberType), None, None), VarDecl(Id(rpL), NumberType, None, None), VarDecl(Id(jdJ), StringType, None, None)], Return()), FuncDecl(Id(dUdW), [VarDecl(Id(tNXY), BoolType, None, None), VarDecl(Id(DN7L), ArrayType([20.08, 5.58], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115708))

	def test_21530115709(self):
		input = '''
func k5TA (string Bf[95.59], number fO9H)
	return rXD

'''
		expect = '''Program([FuncDecl(Id(k5TA), [VarDecl(Id(Bf), ArrayType([95.59], StringType), None, None), VarDecl(Id(fO9H), NumberType, None, None)], Return(Id(rXD)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115709))

	def test_21530115710(self):
		input = '''
number dES[47.53,30.87] <- 95.57
bool lF <- 16.44
'''
		expect = '''Program([VarDecl(Id(dES), ArrayType([47.53, 30.87], NumberType), None, NumLit(95.57)), VarDecl(Id(lF), BoolType, None, NumLit(16.44))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115710))

	def test_21530115711(self):
		input = '''
func LfdC (bool lo, bool P2ZH)	return

number pbtP
func hf3 (number u1E[73.03], bool zTT[16.65])
	return

bool Ey
'''
		expect = '''Program([FuncDecl(Id(LfdC), [VarDecl(Id(lo), BoolType, None, None), VarDecl(Id(P2ZH), BoolType, None, None)], Return()), VarDecl(Id(pbtP), NumberType, None, None), FuncDecl(Id(hf3), [VarDecl(Id(u1E), ArrayType([73.03], NumberType), None, None), VarDecl(Id(zTT), ArrayType([16.65], BoolType), None, None)], Return()), VarDecl(Id(Ey), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115711))

	def test_21530115712(self):
		input = '''
func Sf7f ()
	return
'''
		expect = '''Program([FuncDecl(Id(Sf7f), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115712))

	def test_21530115713(self):
		input = '''
func k0Xu (number WB[42.71,84.0,22.95], bool B0[5.51,6.34,79.89])
	return

var vxHC <- "OGuv"
'''
		expect = '''Program([FuncDecl(Id(k0Xu), [VarDecl(Id(WB), ArrayType([42.71, 84.0, 22.95], NumberType), None, None), VarDecl(Id(B0), ArrayType([5.51, 6.34, 79.89], BoolType), None, None)], Return()), VarDecl(Id(vxHC), None, var, StringLit(OGuv))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115713))

	def test_21530115714(self):
		input = '''
func cB20 (string Z2p[49.78,9.17,94.31])	begin
	end
string ZIZ[43.52,91.57,38.78] <- false
func Nu (string NrZ, number oJVu, bool pq[24.52])
	return
'''
		expect = '''Program([FuncDecl(Id(cB20), [VarDecl(Id(Z2p), ArrayType([49.78, 9.17, 94.31], StringType), None, None)], Block([])), VarDecl(Id(ZIZ), ArrayType([43.52, 91.57, 38.78], StringType), None, BooleanLit(False)), FuncDecl(Id(Nu), [VarDecl(Id(NrZ), StringType, None, None), VarDecl(Id(oJVu), NumberType, None, None), VarDecl(Id(pq), ArrayType([24.52], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115714))

	def test_21530115715(self):
		input = '''
bool H0[77.67]
bool uBc[59.68,13.71] <- Dq
'''
		expect = '''Program([VarDecl(Id(H0), ArrayType([77.67], BoolType), None, None), VarDecl(Id(uBc), ArrayType([59.68, 13.71], BoolType), None, Id(Dq))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115715))

	def test_21530115716(self):
		input = '''
string N7l[75.62,92.14]
'''
		expect = '''Program([VarDecl(Id(N7l), ArrayType([75.62, 92.14], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115716))

	def test_21530115717(self):
		input = '''
func tVf ()	return false
string XA1w[83.37,97.94] <- false
func hHI (string hV, number aA)	return false

number UKn[79.21,53.51] <- false
bool jq <- "Zwp"
'''
		expect = '''Program([FuncDecl(Id(tVf), [], Return(BooleanLit(False))), VarDecl(Id(XA1w), ArrayType([83.37, 97.94], StringType), None, BooleanLit(False)), FuncDecl(Id(hHI), [VarDecl(Id(hV), StringType, None, None), VarDecl(Id(aA), NumberType, None, None)], Return(BooleanLit(False))), VarDecl(Id(UKn), ArrayType([79.21, 53.51], NumberType), None, BooleanLit(False)), VarDecl(Id(jq), BoolType, None, StringLit(Zwp))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115717))

	def test_21530115718(self):
		input = '''
bool fq[70.59,77.71,33.97] <- Yy
dynamic qef
func og2 (string L8[47.57,36.03,84.67], bool HwY[21.75])
	return
bool Ycd
number Hk2G[60.92,77.33] <- 63.57
'''
		expect = '''Program([VarDecl(Id(fq), ArrayType([70.59, 77.71, 33.97], BoolType), None, Id(Yy)), VarDecl(Id(qef), None, dynamic, None), FuncDecl(Id(og2), [VarDecl(Id(L8), ArrayType([47.57, 36.03, 84.67], StringType), None, None), VarDecl(Id(HwY), ArrayType([21.75], BoolType), None, None)], Return()), VarDecl(Id(Ycd), BoolType, None, None), VarDecl(Id(Hk2G), ArrayType([60.92, 77.33], NumberType), None, NumLit(63.57))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115718))

	def test_21530115719(self):
		input = '''
func QsAO (string qgV7, string d3AT)	return

number ecL[75.41]
number uH
'''
		expect = '''Program([FuncDecl(Id(QsAO), [VarDecl(Id(qgV7), StringType, None, None), VarDecl(Id(d3AT), StringType, None, None)], Return()), VarDecl(Id(ecL), ArrayType([75.41], NumberType), None, None), VarDecl(Id(uH), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115719))

	def test_21530115720(self):
		input = '''
func Qrd ()
	return ekC4
number uA <- Xkv
dynamic tXC
'''
		expect = '''Program([FuncDecl(Id(Qrd), [], Return(Id(ekC4))), VarDecl(Id(uA), NumberType, None, Id(Xkv)), VarDecl(Id(tXC), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115720))

	def test_21530115721(self):
		input = '''
var OHQ <- 84.99
func n7u (string oXH)
	begin
	end
func rL (number kZi, bool ni8B, bool pu[72.62,48.5,29.59])
	return

'''
		expect = '''Program([VarDecl(Id(OHQ), None, var, NumLit(84.99)), FuncDecl(Id(n7u), [VarDecl(Id(oXH), StringType, None, None)], Block([])), FuncDecl(Id(rL), [VarDecl(Id(kZi), NumberType, None, None), VarDecl(Id(ni8B), BoolType, None, None), VarDecl(Id(pu), ArrayType([72.62, 48.5, 29.59], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115721))

	def test_21530115722(self):
		input = '''
var quPv <- 21.5
func xXJ (string Fifc[97.36,56.46,25.44], string oP[22.47], number D5i[59.29,90.21])
	begin
		begin
			continue
			q6(97.81, "ylD", 44.72)
			B4 <- MP_
		end
		return
	end

func pq ()
	return fzQ6

dynamic KinR
func X5 (bool Vy1Q[80.67,12.35,25.74], bool Or, number Vix)	return E3

'''
		expect = '''Program([VarDecl(Id(quPv), None, var, NumLit(21.5)), FuncDecl(Id(xXJ), [VarDecl(Id(Fifc), ArrayType([97.36, 56.46, 25.44], StringType), None, None), VarDecl(Id(oP), ArrayType([22.47], StringType), None, None), VarDecl(Id(D5i), ArrayType([59.29, 90.21], NumberType), None, None)], Block([Block([Continue, CallStmt(Id(q6), [NumLit(97.81), StringLit(ylD), NumLit(44.72)]), AssignStmt(Id(B4), Id(MP_))]), Return()])), FuncDecl(Id(pq), [], Return(Id(fzQ6))), VarDecl(Id(KinR), None, dynamic, None), FuncDecl(Id(X5), [VarDecl(Id(Vy1Q), ArrayType([80.67, 12.35, 25.74], BoolType), None, None), VarDecl(Id(Or), BoolType, None, None), VarDecl(Id(Vix), NumberType, None, None)], Return(Id(E3)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115722))

	def test_21530115723(self):
		input = '''
string ymwN <- 29.32
func Thb_ (bool znsX[18.36,68.07], number qXj[83.38,75.51,31.27], bool BjFg[77.78])	return

dynamic NS
func zUfX (number WB, string Izr[14.2,74.33,68.99])	return
'''
		expect = '''Program([VarDecl(Id(ymwN), StringType, None, NumLit(29.32)), FuncDecl(Id(Thb_), [VarDecl(Id(znsX), ArrayType([18.36, 68.07], BoolType), None, None), VarDecl(Id(qXj), ArrayType([83.38, 75.51, 31.27], NumberType), None, None), VarDecl(Id(BjFg), ArrayType([77.78], BoolType), None, None)], Return()), VarDecl(Id(NS), None, dynamic, None), FuncDecl(Id(zUfX), [VarDecl(Id(WB), NumberType, None, None), VarDecl(Id(Izr), ArrayType([14.2, 74.33, 68.99], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115723))

	def test_21530115724(self):
		input = '''
bool OS[82.43] <- false
number nM
'''
		expect = '''Program([VarDecl(Id(OS), ArrayType([82.43], BoolType), None, BooleanLit(False)), VarDecl(Id(nM), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115724))

	def test_21530115725(self):
		input = '''
bool Mg[46.1,65.16] <- 67.09
'''
		expect = '''Program([VarDecl(Id(Mg), ArrayType([46.1, 65.16], BoolType), None, NumLit(67.09))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115725))

	def test_21530115726(self):
		input = '''
dynamic H20 <- tIm8
bool PNf[54.57,90.45]
bool XTo
'''
		expect = '''Program([VarDecl(Id(H20), None, dynamic, Id(tIm8)), VarDecl(Id(PNf), ArrayType([54.57, 90.45], BoolType), None, None), VarDecl(Id(XTo), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115726))

	def test_21530115727(self):
		input = '''
func w5WD (number GI1c[54.89,91.47], string HL[32.47,23.84])
	begin
		tap(false, NNF, 78.48)
	end

'''
		expect = '''Program([FuncDecl(Id(w5WD), [VarDecl(Id(GI1c), ArrayType([54.89, 91.47], NumberType), None, None), VarDecl(Id(HL), ArrayType([32.47, 23.84], StringType), None, None)], Block([CallStmt(Id(tap), [BooleanLit(False), Id(NNF), NumLit(78.48)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115727))

	def test_21530115728(self):
		input = '''
number OU[63.45] <- 46.64
'''
		expect = '''Program([VarDecl(Id(OU), ArrayType([63.45], NumberType), None, NumLit(46.64))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115728))

	def test_21530115729(self):
		input = '''
bool ZJJg[54.93]
string VqH8[44.67]
bool QKO
'''
		expect = '''Program([VarDecl(Id(ZJJg), ArrayType([54.93], BoolType), None, None), VarDecl(Id(VqH8), ArrayType([44.67], StringType), None, None), VarDecl(Id(QKO), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115729))

	def test_21530115730(self):
		input = '''
bool PB9
number H1[58.78,37.09] <- "v"
func Qx (bool bV6[90.32,6.15,32.67], string ogJu[28.71,62.48])	return
number jo
bool j5bf[0.81]
'''
		expect = '''Program([VarDecl(Id(PB9), BoolType, None, None), VarDecl(Id(H1), ArrayType([58.78, 37.09], NumberType), None, StringLit(v)), FuncDecl(Id(Qx), [VarDecl(Id(bV6), ArrayType([90.32, 6.15, 32.67], BoolType), None, None), VarDecl(Id(ogJu), ArrayType([28.71, 62.48], StringType), None, None)], Return()), VarDecl(Id(jo), NumberType, None, None), VarDecl(Id(j5bf), ArrayType([0.81], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115730))

	def test_21530115731(self):
		input = '''
number WxnJ[36.68,3.61,45.52] <- true
var yxUU <- true
number vr5a[47.56,85.39] <- true
string YF[59.9,91.7,66.34] <- Uc
'''
		expect = '''Program([VarDecl(Id(WxnJ), ArrayType([36.68, 3.61, 45.52], NumberType), None, BooleanLit(True)), VarDecl(Id(yxUU), None, var, BooleanLit(True)), VarDecl(Id(vr5a), ArrayType([47.56, 85.39], NumberType), None, BooleanLit(True)), VarDecl(Id(YF), ArrayType([59.9, 91.7, 66.34], StringType), None, Id(Uc))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115731))

	def test_21530115732(self):
		input = '''
number eWh[5.77]
func hb ()	return 77.44
bool ZPMa <- "MYC"
func oBL (string qYt[97.2], bool Sxy, string avL)
	begin
	end
string jf[71.39] <- "LgFFk"
'''
		expect = '''Program([VarDecl(Id(eWh), ArrayType([5.77], NumberType), None, None), FuncDecl(Id(hb), [], Return(NumLit(77.44))), VarDecl(Id(ZPMa), BoolType, None, StringLit(MYC)), FuncDecl(Id(oBL), [VarDecl(Id(qYt), ArrayType([97.2], StringType), None, None), VarDecl(Id(Sxy), BoolType, None, None), VarDecl(Id(avL), StringType, None, None)], Block([])), VarDecl(Id(jf), ArrayType([71.39], StringType), None, StringLit(LgFFk))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115732))

	def test_21530115733(self):
		input = '''
func Ds (number jXH)
	return 57.77

func v70w (number d6L0, bool tk[21.95,18.7,40.05])	return false
'''
		expect = '''Program([FuncDecl(Id(Ds), [VarDecl(Id(jXH), NumberType, None, None)], Return(NumLit(57.77))), FuncDecl(Id(v70w), [VarDecl(Id(d6L0), NumberType, None, None), VarDecl(Id(tk), ArrayType([21.95, 18.7, 40.05], BoolType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115733))

	def test_21530115734(self):
		input = '''
number es
'''
		expect = '''Program([VarDecl(Id(es), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115734))

	def test_21530115735(self):
		input = '''
var HO <- false
'''
		expect = '''Program([VarDecl(Id(HO), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115735))

	def test_21530115736(self):
		input = '''
func jI (bool R6[20.71], string df, bool t2p)
	begin
	end

string A9m
'''
		expect = '''Program([FuncDecl(Id(jI), [VarDecl(Id(R6), ArrayType([20.71], BoolType), None, None), VarDecl(Id(df), StringType, None, None), VarDecl(Id(t2p), BoolType, None, None)], Block([])), VarDecl(Id(A9m), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115736))

	def test_21530115737(self):
		input = '''
string inM[46.36] <- "dL"
func wQ0q (number zj[27.58], string Vm, string Gwc[12.93,47.0,1.75])	return

number cn[7.71,71.69,37.92]
func bW_ (bool aFEM, string nF)
	begin
		HeM2 <- true
		for Ibb until jI3 by "KS"
			break
		bool kc[15.18,32.12]
	end

string LEIW <- 81.74
'''
		expect = '''Program([VarDecl(Id(inM), ArrayType([46.36], StringType), None, StringLit(dL)), FuncDecl(Id(wQ0q), [VarDecl(Id(zj), ArrayType([27.58], NumberType), None, None), VarDecl(Id(Vm), StringType, None, None), VarDecl(Id(Gwc), ArrayType([12.93, 47.0, 1.75], StringType), None, None)], Return()), VarDecl(Id(cn), ArrayType([7.71, 71.69, 37.92], NumberType), None, None), FuncDecl(Id(bW_), [VarDecl(Id(aFEM), BoolType, None, None), VarDecl(Id(nF), StringType, None, None)], Block([AssignStmt(Id(HeM2), BooleanLit(True)), For(Id(Ibb), Id(jI3), StringLit(KS), Break), VarDecl(Id(kc), ArrayType([15.18, 32.12], BoolType), None, None)])), VarDecl(Id(LEIW), StringType, None, NumLit(81.74))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115737))

	def test_21530115738(self):
		input = '''
string CA2J[19.3,29.83,50.55]
func d6j ()	return 93.92

string lK1S[14.88] <- "M"
'''
		expect = '''Program([VarDecl(Id(CA2J), ArrayType([19.3, 29.83, 50.55], StringType), None, None), FuncDecl(Id(d6j), [], Return(NumLit(93.92))), VarDecl(Id(lK1S), ArrayType([14.88], StringType), None, StringLit(M))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115738))

	def test_21530115739(self):
		input = '''
func vih (bool ag[67.6,26.39,17.16], bool gIBc)
	return VP
'''
		expect = '''Program([FuncDecl(Id(vih), [VarDecl(Id(ag), ArrayType([67.6, 26.39, 17.16], BoolType), None, None), VarDecl(Id(gIBc), BoolType, None, None)], Return(Id(VP)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115739))

	def test_21530115740(self):
		input = '''
string GW[74.82,18.99,62.2] <- oG
'''
		expect = '''Program([VarDecl(Id(GW), ArrayType([74.82, 18.99, 62.2], StringType), None, Id(oG))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115740))

	def test_21530115741(self):
		input = '''
string jqg[5.45] <- false
func x5 (bool aamP)
	begin
		hyyY["mfUSf"] <- false
		if (false)
		break
		elif (37.43)
		for Pr until "nx" by 68.66
			begin
				for stg until zV by mai
					for F20d until "ZnHdD" by false
						for TKVj until ow by N6
							break
			end
		elif (false)
		G2["cwTdL"] <- "TJbvh"
		elif (dCb) mBNb[false, "WuVU", "tJKA"] <- qvg
		elif (16.6) if (59.09)
		break
		elif (h2Dn)
		return 47.64
		elif (Xnh0) continue
		else break
		elif (I8O_) break
		return 29.43
	end

'''
		expect = '''Program([VarDecl(Id(jqg), ArrayType([5.45], StringType), None, BooleanLit(False)), FuncDecl(Id(x5), [VarDecl(Id(aamP), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(hyyY), [StringLit(mfUSf)]), BooleanLit(False)), If(BooleanLit(False), Break), [(NumLit(37.43), For(Id(Pr), StringLit(nx), NumLit(68.66), Block([For(Id(stg), Id(zV), Id(mai), For(Id(F20d), StringLit(ZnHdD), BooleanLit(False), For(Id(TKVj), Id(ow), Id(N6), Break)))]))), (BooleanLit(False), AssignStmt(ArrayCell(Id(G2), [StringLit(cwTdL)]), StringLit(TJbvh))), (Id(dCb), AssignStmt(ArrayCell(Id(mBNb), [BooleanLit(False), StringLit(WuVU), StringLit(tJKA)]), Id(qvg))), (NumLit(16.6), If(NumLit(59.09), Break), [(Id(h2Dn), Return(NumLit(47.64))), (Id(Xnh0), Continue)], Break), (Id(I8O_), Break)], None, Return(NumLit(29.43))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115741))

	def test_21530115742(self):
		input = '''
string QZ[88.27,84.54,67.44]
func QC (string NRK, number V6, string wh[0.56])
	begin
		if (false)
		continue
		begin
			begin
				for tp7t until "O" by uo8m
					if (pDW7)
					continue
				r6kH(28.34)
			end
			if (false)
			Aa[ZN40, "btIvW", Fy] <- 69.41
			elif (X0sV)
			for jgoj until "mQ" by "C"
				GM()
			elif (23.64) break
			return 41.75
		end
		VC("Y", true)
	end

func rTW0 (bool H_[54.32,37.8,88.07], bool qS, bool LZz[67.48,57.97])
	return I2M
'''
		expect = '''Program([VarDecl(Id(QZ), ArrayType([88.27, 84.54, 67.44], StringType), None, None), FuncDecl(Id(QC), [VarDecl(Id(NRK), StringType, None, None), VarDecl(Id(V6), NumberType, None, None), VarDecl(Id(wh), ArrayType([0.56], StringType), None, None)], Block([If(BooleanLit(False), Continue), [], None, Block([Block([For(Id(tp7t), StringLit(O), Id(uo8m), If(Id(pDW7), Continue), [], None), CallStmt(Id(r6kH), [NumLit(28.34)])]), If(BooleanLit(False), AssignStmt(ArrayCell(Id(Aa), [Id(ZN40), StringLit(btIvW), Id(Fy)]), NumLit(69.41))), [(Id(X0sV), For(Id(jgoj), StringLit(mQ), StringLit(C), CallStmt(Id(GM), []))), (NumLit(23.64), Break)], None, Return(NumLit(41.75))]), CallStmt(Id(VC), [StringLit(Y), BooleanLit(True)])])), FuncDecl(Id(rTW0), [VarDecl(Id(H_), ArrayType([54.32, 37.8, 88.07], BoolType), None, None), VarDecl(Id(qS), BoolType, None, None), VarDecl(Id(LZz), ArrayType([67.48, 57.97], BoolType), None, None)], Return(Id(I2M)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115742))

	def test_21530115743(self):
		input = '''
var Rt <- false
func OxJ8 (number kpe, bool ht[9.24,86.5], bool Ck[75.38,56.67])	return D40
func t3K (string Bv0)
	return 90.33
'''
		expect = '''Program([VarDecl(Id(Rt), None, var, BooleanLit(False)), FuncDecl(Id(OxJ8), [VarDecl(Id(kpe), NumberType, None, None), VarDecl(Id(ht), ArrayType([9.24, 86.5], BoolType), None, None), VarDecl(Id(Ck), ArrayType([75.38, 56.67], BoolType), None, None)], Return(Id(D40))), FuncDecl(Id(t3K), [VarDecl(Id(Bv0), StringType, None, None)], Return(NumLit(90.33)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115743))

	def test_21530115744(self):
		input = '''
func vef (string x22D, number Ptk[76.15,35.29])	return
bool ZVD[85.56,87.08]
'''
		expect = '''Program([FuncDecl(Id(vef), [VarDecl(Id(x22D), StringType, None, None), VarDecl(Id(Ptk), ArrayType([76.15, 35.29], NumberType), None, None)], Return()), VarDecl(Id(ZVD), ArrayType([85.56, 87.08], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115744))

	def test_21530115745(self):
		input = '''
bool TJqt[11.15,14.27,69.95] <- true
func iG (bool Zj[25.34,67.71,21.51], bool qx[56.57], number v8[77.01])
	return

'''
		expect = '''Program([VarDecl(Id(TJqt), ArrayType([11.15, 14.27, 69.95], BoolType), None, BooleanLit(True)), FuncDecl(Id(iG), [VarDecl(Id(Zj), ArrayType([25.34, 67.71, 21.51], BoolType), None, None), VarDecl(Id(qx), ArrayType([56.57], BoolType), None, None), VarDecl(Id(v8), ArrayType([77.01], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115745))

	def test_21530115746(self):
		input = '''
func EX5 (number a0Q, string XK9[31.97,54.2,96.84])	begin
		return
		begin
			var Cg <- 81.74
		end
		continue
	end

dynamic SXm
'''
		expect = '''Program([FuncDecl(Id(EX5), [VarDecl(Id(a0Q), NumberType, None, None), VarDecl(Id(XK9), ArrayType([31.97, 54.2, 96.84], StringType), None, None)], Block([Return(), Block([VarDecl(Id(Cg), None, var, NumLit(81.74))]), Continue])), VarDecl(Id(SXm), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115746))

	def test_21530115747(self):
		input = '''
func wzdJ (bool Yf[52.86,76.22], number Mi, number WQ[71.57])
	return
var bb2 <- 0.39
func DI (bool Up)
	return 39.15
func Dn (number LXD[15.29])	return z7L

func v4A (string Hd, string Hry)	begin
	end

'''
		expect = '''Program([FuncDecl(Id(wzdJ), [VarDecl(Id(Yf), ArrayType([52.86, 76.22], BoolType), None, None), VarDecl(Id(Mi), NumberType, None, None), VarDecl(Id(WQ), ArrayType([71.57], NumberType), None, None)], Return()), VarDecl(Id(bb2), None, var, NumLit(0.39)), FuncDecl(Id(DI), [VarDecl(Id(Up), BoolType, None, None)], Return(NumLit(39.15))), FuncDecl(Id(Dn), [VarDecl(Id(LXD), ArrayType([15.29], NumberType), None, None)], Return(Id(z7L))), FuncDecl(Id(v4A), [VarDecl(Id(Hd), StringType, None, None), VarDecl(Id(Hry), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115747))

	def test_21530115748(self):
		input = '''
func aA (bool a2[3.33])
	begin
		begin
			continue
		end
	end

func p6 ()	return

func nZB (string dYeD[60.95,56.69,88.43], number vX[69.38,76.95])
	return

'''
		expect = '''Program([FuncDecl(Id(aA), [VarDecl(Id(a2), ArrayType([3.33], BoolType), None, None)], Block([Block([Continue])])), FuncDecl(Id(p6), [], Return()), FuncDecl(Id(nZB), [VarDecl(Id(dYeD), ArrayType([60.95, 56.69, 88.43], StringType), None, None), VarDecl(Id(vX), ArrayType([69.38, 76.95], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115748))

	def test_21530115749(self):
		input = '''
number yHMu
func GG (string fdms[46.47,84.7,54.08], bool ip_Y)
	return 56.11

string BPq[15.51] <- true
bool Vuse <- "AvM"
'''
		expect = '''Program([VarDecl(Id(yHMu), NumberType, None, None), FuncDecl(Id(GG), [VarDecl(Id(fdms), ArrayType([46.47, 84.7, 54.08], StringType), None, None), VarDecl(Id(ip_Y), BoolType, None, None)], Return(NumLit(56.11))), VarDecl(Id(BPq), ArrayType([15.51], StringType), None, BooleanLit(True)), VarDecl(Id(Vuse), BoolType, None, StringLit(AvM))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115749))

	def test_21530115750(self):
		input = '''
bool xPmA
string cA[75.4,17.59,54.1] <- Lmsx
'''
		expect = '''Program([VarDecl(Id(xPmA), BoolType, None, None), VarDecl(Id(cA), ArrayType([75.4, 17.59, 54.1], StringType), None, Id(Lmsx))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115750))

	def test_21530115751(self):
		input = '''
func e_ ()
	begin
		return
		return
	end

func VFhf ()	return tI
func mTA (string shzI)	begin
		if (22.24)
		begin
			seFn["sCMbT", "fN"] <- false
			SY["bpEz", "HOh", Uy] <- 99.13
		end
		elif (true) number Hge[17.64,87.68] <- 88.43
		else break
	end
func tG6 (bool n3j)
	begin
		begin
			continue
			FUd[false, false] <- img
		end
		U9()
	end

func yBpY (number ds[42.92], string S5O)	return iv5
'''
		expect = '''Program([FuncDecl(Id(e_), [], Block([Return(), Return()])), FuncDecl(Id(VFhf), [], Return(Id(tI))), FuncDecl(Id(mTA), [VarDecl(Id(shzI), StringType, None, None)], Block([If(NumLit(22.24), Block([AssignStmt(ArrayCell(Id(seFn), [StringLit(sCMbT), StringLit(fN)]), BooleanLit(False)), AssignStmt(ArrayCell(Id(SY), [StringLit(bpEz), StringLit(HOh), Id(Uy)]), NumLit(99.13))])), [(BooleanLit(True), VarDecl(Id(Hge), ArrayType([17.64, 87.68], NumberType), None, NumLit(88.43)))], Break])), FuncDecl(Id(tG6), [VarDecl(Id(n3j), BoolType, None, None)], Block([Block([Continue, AssignStmt(ArrayCell(Id(FUd), [BooleanLit(False), BooleanLit(False)]), Id(img))]), CallStmt(Id(U9), [])])), FuncDecl(Id(yBpY), [VarDecl(Id(ds), ArrayType([42.92], NumberType), None, None), VarDecl(Id(S5O), StringType, None, None)], Return(Id(iv5)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115751))

	def test_21530115752(self):
		input = '''
func tQ ()	begin
		continue
		begin
			continue
			continue
		end
		Kyyr <- 79.41
	end
func frvY (number xLFW[95.5], bool YfA[38.71,56.71], bool TEk3[53.58,33.02])
	return false

'''
		expect = '''Program([FuncDecl(Id(tQ), [], Block([Continue, Block([Continue, Continue]), AssignStmt(Id(Kyyr), NumLit(79.41))])), FuncDecl(Id(frvY), [VarDecl(Id(xLFW), ArrayType([95.5], NumberType), None, None), VarDecl(Id(YfA), ArrayType([38.71, 56.71], BoolType), None, None), VarDecl(Id(TEk3), ArrayType([53.58, 33.02], BoolType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115752))

	def test_21530115753(self):
		input = '''
var YH8 <- "hOX"
func ZWHQ (string WW8[53.85,35.87])	begin
	end

bool zd[34.18,19.64,43.86]
string T6E[16.47,48.22] <- true
'''
		expect = '''Program([VarDecl(Id(YH8), None, var, StringLit(hOX)), FuncDecl(Id(ZWHQ), [VarDecl(Id(WW8), ArrayType([53.85, 35.87], StringType), None, None)], Block([])), VarDecl(Id(zd), ArrayType([34.18, 19.64, 43.86], BoolType), None, None), VarDecl(Id(T6E), ArrayType([16.47, 48.22], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115753))

	def test_21530115754(self):
		input = '''
func Cwp (string DEv)	begin
		break
	end
'''
		expect = '''Program([FuncDecl(Id(Cwp), [VarDecl(Id(DEv), StringType, None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115754))

	def test_21530115755(self):
		input = '''
string W9b <- WT
number cNC[83.34,68.87,59.38] <- vAD
func FvhD (bool KrP, string b1tU[80.81])
	begin
		Wp4 <- 30.97
	end
number nWlu[47.19,32.64] <- ZQ
string lDe[86.28,97.73,69.85]
'''
		expect = '''Program([VarDecl(Id(W9b), StringType, None, Id(WT)), VarDecl(Id(cNC), ArrayType([83.34, 68.87, 59.38], NumberType), None, Id(vAD)), FuncDecl(Id(FvhD), [VarDecl(Id(KrP), BoolType, None, None), VarDecl(Id(b1tU), ArrayType([80.81], StringType), None, None)], Block([AssignStmt(Id(Wp4), NumLit(30.97))])), VarDecl(Id(nWlu), ArrayType([47.19, 32.64], NumberType), None, Id(ZQ)), VarDecl(Id(lDe), ArrayType([86.28, 97.73, 69.85], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115755))

	def test_21530115756(self):
		input = '''
number YG[83.06,95.93,96.82] <- "YBe"
func a4Fz (bool QIs[46.82,72.85,74.99])
	return SMK
func yx (number uo[81.2,18.73,44.98], string qSOH)
	return NpWC

'''
		expect = '''Program([VarDecl(Id(YG), ArrayType([83.06, 95.93, 96.82], NumberType), None, StringLit(YBe)), FuncDecl(Id(a4Fz), [VarDecl(Id(QIs), ArrayType([46.82, 72.85, 74.99], BoolType), None, None)], Return(Id(SMK))), FuncDecl(Id(yx), [VarDecl(Id(uo), ArrayType([81.2, 18.73, 44.98], NumberType), None, None), VarDecl(Id(qSOH), StringType, None, None)], Return(Id(NpWC)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115756))

	def test_21530115757(self):
		input = '''
func nya (bool VL[65.28])	begin
	end

func PXx (string nxL, bool Lcbf, string h_0A[5.79])	begin
		pj1("dxuG", 24.03)
	end

func Wq (number TRyx[70.0,80.44,48.42])
	return

func Wa3V (string b7[67.66], bool xLH[12.97,94.33])
	return

string LPkQ[45.3,41.7,26.28] <- false
'''
		expect = '''Program([FuncDecl(Id(nya), [VarDecl(Id(VL), ArrayType([65.28], BoolType), None, None)], Block([])), FuncDecl(Id(PXx), [VarDecl(Id(nxL), StringType, None, None), VarDecl(Id(Lcbf), BoolType, None, None), VarDecl(Id(h_0A), ArrayType([5.79], StringType), None, None)], Block([CallStmt(Id(pj1), [StringLit(dxuG), NumLit(24.03)])])), FuncDecl(Id(Wq), [VarDecl(Id(TRyx), ArrayType([70.0, 80.44, 48.42], NumberType), None, None)], Return()), FuncDecl(Id(Wa3V), [VarDecl(Id(b7), ArrayType([67.66], StringType), None, None), VarDecl(Id(xLH), ArrayType([12.97, 94.33], BoolType), None, None)], Return()), VarDecl(Id(LPkQ), ArrayType([45.3, 41.7, 26.28], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115757))

	def test_21530115758(self):
		input = '''
number zr <- 48.94
func IQJp (string OR0[30.88,29.59], number VE79)
	begin
		z1 <- true
		break
		string Mg_[99.94,5.89,71.73] <- false
	end

'''
		expect = '''Program([VarDecl(Id(zr), NumberType, None, NumLit(48.94)), FuncDecl(Id(IQJp), [VarDecl(Id(OR0), ArrayType([30.88, 29.59], StringType), None, None), VarDecl(Id(VE79), NumberType, None, None)], Block([AssignStmt(Id(z1), BooleanLit(True)), Break, VarDecl(Id(Mg_), ArrayType([99.94, 5.89, 71.73], StringType), None, BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115758))

	def test_21530115759(self):
		input = '''
bool Ux
'''
		expect = '''Program([VarDecl(Id(Ux), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115759))

	def test_21530115760(self):
		input = '''
string sVn[62.46,81.71,86.98] <- XOnV
var Z0D <- "Ulp"
'''
		expect = '''Program([VarDecl(Id(sVn), ArrayType([62.46, 81.71, 86.98], StringType), None, Id(XOnV)), VarDecl(Id(Z0D), None, var, StringLit(Ulp))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115760))

	def test_21530115761(self):
		input = '''
bool XG <- "a"
'''
		expect = '''Program([VarDecl(Id(XG), BoolType, None, StringLit(a))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115761))

	def test_21530115762(self):
		input = '''
number Fyb[72.81,93.14] <- true
func oI6 (string U7q[14.02,69.06,97.29], bool e_, string lj)	begin
		return "Tip"
		return
		for xD until false by "dY"
			ccHE("lA")
	end

number dy[62.44] <- 17.24
func U831 (string Cn[72.27], number lhKH[7.08])	begin
		return
	end
func fB (bool BKes[89.26,0.41], bool hz, bool RP)	begin
	end

'''
		expect = '''Program([VarDecl(Id(Fyb), ArrayType([72.81, 93.14], NumberType), None, BooleanLit(True)), FuncDecl(Id(oI6), [VarDecl(Id(U7q), ArrayType([14.02, 69.06, 97.29], StringType), None, None), VarDecl(Id(e_), BoolType, None, None), VarDecl(Id(lj), StringType, None, None)], Block([Return(StringLit(Tip)), Return(), For(Id(xD), BooleanLit(False), StringLit(dY), CallStmt(Id(ccHE), [StringLit(lA)]))])), VarDecl(Id(dy), ArrayType([62.44], NumberType), None, NumLit(17.24)), FuncDecl(Id(U831), [VarDecl(Id(Cn), ArrayType([72.27], StringType), None, None), VarDecl(Id(lhKH), ArrayType([7.08], NumberType), None, None)], Block([Return()])), FuncDecl(Id(fB), [VarDecl(Id(BKes), ArrayType([89.26, 0.41], BoolType), None, None), VarDecl(Id(hz), BoolType, None, None), VarDecl(Id(RP), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115762))

	def test_21530115763(self):
		input = '''
func xL9 (number MbD3, bool Fh)
	return
'''
		expect = '''Program([FuncDecl(Id(xL9), [VarDecl(Id(MbD3), NumberType, None, None), VarDecl(Id(Fh), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115763))

	def test_21530115764(self):
		input = '''
func RH (string iM[61.15,75.11])
	begin
	end

func S4ii (string L8[6.94,95.1], number KA, bool KMEY[27.7,87.88])	return aV
string s0gl[51.7,53.42]
func UG (bool m_pH, string DJ[92.35,88.68,83.42], bool hehd[21.91,32.14])
	return true

'''
		expect = '''Program([FuncDecl(Id(RH), [VarDecl(Id(iM), ArrayType([61.15, 75.11], StringType), None, None)], Block([])), FuncDecl(Id(S4ii), [VarDecl(Id(L8), ArrayType([6.94, 95.1], StringType), None, None), VarDecl(Id(KA), NumberType, None, None), VarDecl(Id(KMEY), ArrayType([27.7, 87.88], BoolType), None, None)], Return(Id(aV))), VarDecl(Id(s0gl), ArrayType([51.7, 53.42], StringType), None, None), FuncDecl(Id(UG), [VarDecl(Id(m_pH), BoolType, None, None), VarDecl(Id(DJ), ArrayType([92.35, 88.68, 83.42], StringType), None, None), VarDecl(Id(hehd), ArrayType([21.91, 32.14], BoolType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115764))

	def test_21530115765(self):
		input = '''
func Bg ()
	begin
		for a4AW until "T" by LGO
			break
	end

func bRHt ()
	return 49.65

string OQ[37.12,94.71] <- true
string mhPq[15.83]
'''
		expect = '''Program([FuncDecl(Id(Bg), [], Block([For(Id(a4AW), StringLit(T), Id(LGO), Break)])), FuncDecl(Id(bRHt), [], Return(NumLit(49.65))), VarDecl(Id(OQ), ArrayType([37.12, 94.71], StringType), None, BooleanLit(True)), VarDecl(Id(mhPq), ArrayType([15.83], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115765))

	def test_21530115766(self):
		input = '''
bool THk <- po2
string VnaQ <- 85.85
func rkZ ()	begin
		Hxui[false] <- false
	end
number L9VS
'''
		expect = '''Program([VarDecl(Id(THk), BoolType, None, Id(po2)), VarDecl(Id(VnaQ), StringType, None, NumLit(85.85)), FuncDecl(Id(rkZ), [], Block([AssignStmt(ArrayCell(Id(Hxui), [BooleanLit(False)]), BooleanLit(False))])), VarDecl(Id(L9VS), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115766))

	def test_21530115767(self):
		input = '''
string Yqz
func jqH (number Y9jg[75.57,8.2], string zZ[37.46,66.24,38.94], bool QEeO)	begin
		if (false)
		continue
		elif (0.81)
		break
		else return l3E
		if (true) begin
		end
		elif ("XBv") continue
		elif (QV) sMKO[CnR, FbX4, 60.87] <- "a"
		elif (97.9)
		if ("Cbib")
		return "VzPR"
		elif (Q9E) break
		else begin
			continue
			VX(QuA4)
			return
		end
		break
	end
number FG <- 23.32
string Ry[75.62,79.54,71.1]
'''
		expect = '''Program([VarDecl(Id(Yqz), StringType, None, None), FuncDecl(Id(jqH), [VarDecl(Id(Y9jg), ArrayType([75.57, 8.2], NumberType), None, None), VarDecl(Id(zZ), ArrayType([37.46, 66.24, 38.94], StringType), None, None), VarDecl(Id(QEeO), BoolType, None, None)], Block([If(BooleanLit(False), Continue), [(NumLit(0.81), Break)], Return(Id(l3E)), If(BooleanLit(True), Block([])), [(StringLit(XBv), Continue), (Id(QV), AssignStmt(ArrayCell(Id(sMKO), [Id(CnR), Id(FbX4), NumLit(60.87)]), StringLit(a))), (NumLit(97.9), If(StringLit(Cbib), Return(StringLit(VzPR))), [(Id(Q9E), Break)], Block([Continue, CallStmt(Id(VX), [Id(QuA4)]), Return()]))], None, Break])), VarDecl(Id(FG), NumberType, None, NumLit(23.32)), VarDecl(Id(Ry), ArrayType([75.62, 79.54, 71.1], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115767))

	def test_21530115768(self):
		input = '''
func TA (string HVb, bool Ysrs, bool xbOq)	return
func lmw ()
	begin
		BW <- true
		if (8.5) xBKA <- 38.8
		elif (true) for AFn until "QCZl" by YHm
			begin
				mC[true, 14.53, 32.32] <- false
				for CFD until F7 by false
					break
				number SLy0 <- NJ
			end
		elif ("Hnp") return true
		elif (true) uDDu()
		elif (57.34) return
		elif (false)
		return K7
		else Gn9[yy, Ny] <- YEX
	end

number aIk[27.92,32.41,84.35]
func uulj (string oyH[79.39,68.56], bool NEpP, number eA[14.59,23.58,41.27])
	return
func h71 (string GAv[18.12])
	return vDeX

'''
		expect = '''Program([FuncDecl(Id(TA), [VarDecl(Id(HVb), StringType, None, None), VarDecl(Id(Ysrs), BoolType, None, None), VarDecl(Id(xbOq), BoolType, None, None)], Return()), FuncDecl(Id(lmw), [], Block([AssignStmt(Id(BW), BooleanLit(True)), If(NumLit(8.5), AssignStmt(Id(xBKA), NumLit(38.8))), [(BooleanLit(True), For(Id(AFn), StringLit(QCZl), Id(YHm), Block([AssignStmt(ArrayCell(Id(mC), [BooleanLit(True), NumLit(14.53), NumLit(32.32)]), BooleanLit(False)), For(Id(CFD), Id(F7), BooleanLit(False), Break), VarDecl(Id(SLy0), NumberType, None, Id(NJ))]))), (StringLit(Hnp), Return(BooleanLit(True))), (BooleanLit(True), CallStmt(Id(uDDu), [])), (NumLit(57.34), Return()), (BooleanLit(False), Return(Id(K7)))], AssignStmt(ArrayCell(Id(Gn9), [Id(yy), Id(Ny)]), Id(YEX))])), VarDecl(Id(aIk), ArrayType([27.92, 32.41, 84.35], NumberType), None, None), FuncDecl(Id(uulj), [VarDecl(Id(oyH), ArrayType([79.39, 68.56], StringType), None, None), VarDecl(Id(NEpP), BoolType, None, None), VarDecl(Id(eA), ArrayType([14.59, 23.58, 41.27], NumberType), None, None)], Return()), FuncDecl(Id(h71), [VarDecl(Id(GAv), ArrayType([18.12], StringType), None, None)], Return(Id(vDeX)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115768))

	def test_21530115769(self):
		input = '''
string R7kd
func jez (string vYtF[1.93])
	return 0.91

string JZ[9.25] <- qA
'''
		expect = '''Program([VarDecl(Id(R7kd), StringType, None, None), FuncDecl(Id(jez), [VarDecl(Id(vYtF), ArrayType([1.93], StringType), None, None)], Return(NumLit(0.91))), VarDecl(Id(JZ), ArrayType([9.25], StringType), None, Id(qA))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115769))

	def test_21530115770(self):
		input = '''
func vz (string vc[56.63], string He[0.27,39.11,24.54])	begin
	end
var xN <- sI
func hRT (bool UV[41.24,30.38], bool i4XZ[75.12,96.99,7.3], number Ax3S[26.88,27.37,4.42])
	begin
		dynamic FIUa
		for e7V until 65.56 by "D"
			for x_ until 28.12 by 7.25
				begin
					return
					if (true) for JJj until "Zo" by x_4
						continue
					elif (false)
					break
					elif ("Qg") for Kt until true by BVN
						if ("B") break
						elif ("DdeCz")
						return
						elif (true)
						continue
						elif (Mi7)
						if (false) begin
							bool IlfO
							for a1oK until 77.29 by dCWf
								begin
								end
							bool TW0[82.45]
						end
						elif (23.89)
						number bik[32.49,35.43] <- 90.83
						elif (77.55) if (false) if (mj)
						break
						else Fh("Q", "NSqt", nDX0)
						elif (false) break
						elif ("TkU") lG_ <- 4.09
						elif ("xfR")
						GRg(smZ)
						elif ("mqMZf") for VEY6 until L1J by "CVC"
							if (84.79)
							begin
							end
							else for H3ea until 24.74 by 12.52
								begin
								end
						elif ("uQ")
						for EH until 95.13 by BK
							begin
							end
					elif (WzOY) begin
					end
					elif (true) JXI[WmJ] <- false
					elif ("qYB") break
					else continue
					break
				end
	end

'''
		expect = '''Program([FuncDecl(Id(vz), [VarDecl(Id(vc), ArrayType([56.63], StringType), None, None), VarDecl(Id(He), ArrayType([0.27, 39.11, 24.54], StringType), None, None)], Block([])), VarDecl(Id(xN), None, var, Id(sI)), FuncDecl(Id(hRT), [VarDecl(Id(UV), ArrayType([41.24, 30.38], BoolType), None, None), VarDecl(Id(i4XZ), ArrayType([75.12, 96.99, 7.3], BoolType), None, None), VarDecl(Id(Ax3S), ArrayType([26.88, 27.37, 4.42], NumberType), None, None)], Block([VarDecl(Id(FIUa), None, dynamic, None), For(Id(e7V), NumLit(65.56), StringLit(D), For(Id(x_), NumLit(28.12), NumLit(7.25), Block([Return(), If(BooleanLit(True), For(Id(JJj), StringLit(Zo), Id(x_4), Continue)), [(BooleanLit(False), Break), (StringLit(Qg), For(Id(Kt), BooleanLit(True), Id(BVN), If(StringLit(B), Break), [(StringLit(DdeCz), Return()), (BooleanLit(True), Continue), (Id(Mi7), If(BooleanLit(False), Block([VarDecl(Id(IlfO), BoolType, None, None), For(Id(a1oK), NumLit(77.29), Id(dCWf), Block([])), VarDecl(Id(TW0), ArrayType([82.45], BoolType), None, None)])), [(NumLit(23.89), VarDecl(Id(bik), ArrayType([32.49, 35.43], NumberType), None, NumLit(90.83))), (NumLit(77.55), If(BooleanLit(False), If(Id(mj), Break), [], CallStmt(Id(Fh), [StringLit(Q), StringLit(NSqt), Id(nDX0)])), [(BooleanLit(False), Break), (StringLit(TkU), AssignStmt(Id(lG_), NumLit(4.09))), (StringLit(xfR), CallStmt(Id(GRg), [Id(smZ)])), (StringLit(mqMZf), For(Id(VEY6), Id(L1J), StringLit(CVC), If(NumLit(84.79), Block([])), [], For(Id(H3ea), NumLit(24.74), NumLit(12.52), Block([])))), (StringLit(uQ), For(Id(EH), NumLit(95.13), Id(BK), Block([]))), (Id(WzOY), Block([])), (BooleanLit(True), AssignStmt(ArrayCell(Id(JXI), [Id(WmJ)]), BooleanLit(False))), (StringLit(qYB), Break)], Continue)], None)], None))], None, Break])))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115770))

	def test_21530115771(self):
		input = '''
bool GRs[31.47,66.47,18.74]
number lY <- 97.19
var fLLT <- 71.68
'''
		expect = '''Program([VarDecl(Id(GRs), ArrayType([31.47, 66.47, 18.74], BoolType), None, None), VarDecl(Id(lY), NumberType, None, NumLit(97.19)), VarDecl(Id(fLLT), None, var, NumLit(71.68))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115771))

	def test_21530115772(self):
		input = '''
number WsL[91.47,93.16,51.01] <- lef
'''
		expect = '''Program([VarDecl(Id(WsL), ArrayType([91.47, 93.16, 51.01], NumberType), None, Id(lef))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115772))

	def test_21530115773(self):
		input = '''
func EpmL (number bsA[21.38])
	return
func rVn (bool ila[17.58,22.95], string ErSq, string Ky)
	begin
		return
	end
number UZgW <- true
var XsCE <- xnGv
func a7Ut (string Cw1f, bool G5q[31.5,44.23,23.65], number WR[37.51])	return true

'''
		expect = '''Program([FuncDecl(Id(EpmL), [VarDecl(Id(bsA), ArrayType([21.38], NumberType), None, None)], Return()), FuncDecl(Id(rVn), [VarDecl(Id(ila), ArrayType([17.58, 22.95], BoolType), None, None), VarDecl(Id(ErSq), StringType, None, None), VarDecl(Id(Ky), StringType, None, None)], Block([Return()])), VarDecl(Id(UZgW), NumberType, None, BooleanLit(True)), VarDecl(Id(XsCE), None, var, Id(xnGv)), FuncDecl(Id(a7Ut), [VarDecl(Id(Cw1f), StringType, None, None), VarDecl(Id(G5q), ArrayType([31.5, 44.23, 23.65], BoolType), None, None), VarDecl(Id(WR), ArrayType([37.51], NumberType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115773))

	def test_21530115774(self):
		input = '''
var RE <- true
bool lpBa[54.54,87.89,6.46] <- jr3
string erFn[77.39,86.13]
func Ls (string a0rW[44.51], number Ak)
	return
func vh (number Qy_[65.33,41.7], number qI0[69.77,45.6], string sRHD[17.07])
	begin
		if (true)
		if ("TrhED")
		break
		elif (41.46) break
		elif (GU)
		for hO_e until "IJL" by "gs"
			q9D <- 53.63
		elif (25.56)
		a49()
		elif (79.64)
		number gC
		elif (29.76) begin
		end
		else number fTN
		else for BBy until true by 63.26
			number fLq[4.22] <- "k"
	end

'''
		expect = '''Program([VarDecl(Id(RE), None, var, BooleanLit(True)), VarDecl(Id(lpBa), ArrayType([54.54, 87.89, 6.46], BoolType), None, Id(jr3)), VarDecl(Id(erFn), ArrayType([77.39, 86.13], StringType), None, None), FuncDecl(Id(Ls), [VarDecl(Id(a0rW), ArrayType([44.51], StringType), None, None), VarDecl(Id(Ak), NumberType, None, None)], Return()), FuncDecl(Id(vh), [VarDecl(Id(Qy_), ArrayType([65.33, 41.7], NumberType), None, None), VarDecl(Id(qI0), ArrayType([69.77, 45.6], NumberType), None, None), VarDecl(Id(sRHD), ArrayType([17.07], StringType), None, None)], Block([If(BooleanLit(True), If(StringLit(TrhED), Break), [(NumLit(41.46), Break), (Id(GU), For(Id(hO_e), StringLit(IJL), StringLit(gs), AssignStmt(Id(q9D), NumLit(53.63)))), (NumLit(25.56), CallStmt(Id(a49), [])), (NumLit(79.64), VarDecl(Id(gC), NumberType, None, None)), (NumLit(29.76), Block([]))], VarDecl(Id(fTN), NumberType, None, None)), [], For(Id(BBy), BooleanLit(True), NumLit(63.26), VarDecl(Id(fLq), ArrayType([4.22], NumberType), None, StringLit(k)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115774))

	def test_21530115775(self):
		input = '''
func T0 (bool RQ, number AVh[54.61], string omt[91.36,41.07])	return
func Ad4x (bool mGn2, number g13l[88.94,90.77,31.23])	begin
		if (72.93)
		for H0B until 18.55 by false
			continue
		elif (91.08) if (bLf2) dynamic kt5j
		Zwh()
	end
bool cOoD[4.81,30.1] <- "Y"
func TMg ()
	return
'''
		expect = '''Program([FuncDecl(Id(T0), [VarDecl(Id(RQ), BoolType, None, None), VarDecl(Id(AVh), ArrayType([54.61], NumberType), None, None), VarDecl(Id(omt), ArrayType([91.36, 41.07], StringType), None, None)], Return()), FuncDecl(Id(Ad4x), [VarDecl(Id(mGn2), BoolType, None, None), VarDecl(Id(g13l), ArrayType([88.94, 90.77, 31.23], NumberType), None, None)], Block([If(NumLit(72.93), For(Id(H0B), NumLit(18.55), BooleanLit(False), Continue)), [(NumLit(91.08), If(Id(bLf2), VarDecl(Id(kt5j), None, dynamic, None)), [], None)], None, CallStmt(Id(Zwh), [])])), VarDecl(Id(cOoD), ArrayType([4.81, 30.1], BoolType), None, StringLit(Y)), FuncDecl(Id(TMg), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115775))

	def test_21530115776(self):
		input = '''
func fPXc ()
	begin
	end

func SDZ (bool Ryku[40.31])	return Gm

'''
		expect = '''Program([FuncDecl(Id(fPXc), [], Block([])), FuncDecl(Id(SDZ), [VarDecl(Id(Ryku), ArrayType([40.31], BoolType), None, None)], Return(Id(Gm)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115776))

	def test_21530115777(self):
		input = '''
string ZykR[7.47] <- 77.33
'''
		expect = '''Program([VarDecl(Id(ZykR), ArrayType([7.47], StringType), None, NumLit(77.33))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115777))

	def test_21530115778(self):
		input = '''
number IPj8[58.28] <- true
func xPii (bool UV4R)	return false

func Y9 (string eK[77.33])
	return "jMNna"

'''
		expect = '''Program([VarDecl(Id(IPj8), ArrayType([58.28], NumberType), None, BooleanLit(True)), FuncDecl(Id(xPii), [VarDecl(Id(UV4R), BoolType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(Y9), [VarDecl(Id(eK), ArrayType([77.33], StringType), None, None)], Return(StringLit(jMNna)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115778))

	def test_21530115779(self):
		input = '''
string MEVm <- "OE"
func n5 (string dmZ9, number fw7, string iyYA)	return

'''
		expect = '''Program([VarDecl(Id(MEVm), StringType, None, StringLit(OE)), FuncDecl(Id(n5), [VarDecl(Id(dmZ9), StringType, None, None), VarDecl(Id(fw7), NumberType, None, None), VarDecl(Id(iyYA), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115779))

	def test_21530115780(self):
		input = '''
func Mm5 ()	return "FWM"

bool ce[95.35,71.5,50.52]
bool uM8 <- NQ
bool f5n[12.45] <- oa7I
func krZ (bool Nvw, bool zjY[95.45,95.21])	begin
		continue
		return true
		continue
	end

'''
		expect = '''Program([FuncDecl(Id(Mm5), [], Return(StringLit(FWM))), VarDecl(Id(ce), ArrayType([95.35, 71.5, 50.52], BoolType), None, None), VarDecl(Id(uM8), BoolType, None, Id(NQ)), VarDecl(Id(f5n), ArrayType([12.45], BoolType), None, Id(oa7I)), FuncDecl(Id(krZ), [VarDecl(Id(Nvw), BoolType, None, None), VarDecl(Id(zjY), ArrayType([95.45, 95.21], BoolType), None, None)], Block([Continue, Return(BooleanLit(True)), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115780))

	def test_21530115781(self):
		input = '''
var owj6 <- 91.65
string Y7 <- "ObAw"
func weCD (string V74, bool wk, string hdQ)
	return

'''
		expect = '''Program([VarDecl(Id(owj6), None, var, NumLit(91.65)), VarDecl(Id(Y7), StringType, None, StringLit(ObAw)), FuncDecl(Id(weCD), [VarDecl(Id(V74), StringType, None, None), VarDecl(Id(wk), BoolType, None, None), VarDecl(Id(hdQ), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115781))

	def test_21530115782(self):
		input = '''
string DE[26.96,12.95,17.31] <- false
func ee (bool WOu[82.03], number L4)
	return

number Qa[5.78,59.25,9.56]
'''
		expect = '''Program([VarDecl(Id(DE), ArrayType([26.96, 12.95, 17.31], StringType), None, BooleanLit(False)), FuncDecl(Id(ee), [VarDecl(Id(WOu), ArrayType([82.03], BoolType), None, None), VarDecl(Id(L4), NumberType, None, None)], Return()), VarDecl(Id(Qa), ArrayType([5.78, 59.25, 9.56], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115782))

	def test_21530115783(self):
		input = '''
bool dlC1[97.41,62.88,14.52]
'''
		expect = '''Program([VarDecl(Id(dlC1), ArrayType([97.41, 62.88, 14.52], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115783))

	def test_21530115784(self):
		input = '''
func H7N8 (string DBUw, string MR[35.49,82.97,82.9], number IC)	return
'''
		expect = '''Program([FuncDecl(Id(H7N8), [VarDecl(Id(DBUw), StringType, None, None), VarDecl(Id(MR), ArrayType([35.49, 82.97, 82.9], StringType), None, None), VarDecl(Id(IC), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115784))

	def test_21530115785(self):
		input = '''
dynamic ZtL <- "hLZ"
func B9jH ()
	return

number z3l[53.55]
'''
		expect = '''Program([VarDecl(Id(ZtL), None, dynamic, StringLit(hLZ)), FuncDecl(Id(B9jH), [], Return()), VarDecl(Id(z3l), ArrayType([53.55], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115785))

	def test_21530115786(self):
		input = '''
func CI3U (bool WzN[69.58,15.96], number Go, bool o2Mb[26.89])
	return
number c4y3[21.28]
func DQBX (string yjN, number XLAp)
	return false

var b4B <- y2
'''
		expect = '''Program([FuncDecl(Id(CI3U), [VarDecl(Id(WzN), ArrayType([69.58, 15.96], BoolType), None, None), VarDecl(Id(Go), NumberType, None, None), VarDecl(Id(o2Mb), ArrayType([26.89], BoolType), None, None)], Return()), VarDecl(Id(c4y3), ArrayType([21.28], NumberType), None, None), FuncDecl(Id(DQBX), [VarDecl(Id(yjN), StringType, None, None), VarDecl(Id(XLAp), NumberType, None, None)], Return(BooleanLit(False))), VarDecl(Id(b4B), None, var, Id(y2))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115786))

	def test_21530115787(self):
		input = '''
var lN <- "tj"
number Nvb <- 5.72
func etF (string e1H[12.48,68.73,33.02])	return 94.78

var suEA <- wSU4
'''
		expect = '''Program([VarDecl(Id(lN), None, var, StringLit(tj)), VarDecl(Id(Nvb), NumberType, None, NumLit(5.72)), FuncDecl(Id(etF), [VarDecl(Id(e1H), ArrayType([12.48, 68.73, 33.02], StringType), None, None)], Return(NumLit(94.78))), VarDecl(Id(suEA), None, var, Id(wSU4))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115787))

	def test_21530115788(self):
		input = '''
func sK0q (bool SU, bool YiQ)	begin
		return
		return
		if (true) continue
		elif (false)
		if (69.5)
		for TBuF until miww by 38.39
			continue
		elif (Zux)
		begin
			if (true) bool fmb <- false
			elif (false)
			AY(false, "IZs")
			else break
			continue
		end
		elif (23.98)
		var R8Ak <- N0vk
		elif (63.61)
		ZQI <- 65.48
		elif (true)
		for Nf until true by "pmqo"
			JvZ(72.41, true)
		else begin
			continue
		end
		elif (75.34)
		number XY[72.34]
		elif (KUfr) continue
		elif (z1) return true
	end

bool EKYu
func efr (number k8Z5[3.27], number V5[9.5,51.3,41.31])	return

func QgjS (number j1)	return
func Ou (bool qgZ)	begin
	end

'''
		expect = '''Program([FuncDecl(Id(sK0q), [VarDecl(Id(SU), BoolType, None, None), VarDecl(Id(YiQ), BoolType, None, None)], Block([Return(), Return(), If(BooleanLit(True), Continue), [(BooleanLit(False), If(NumLit(69.5), For(Id(TBuF), Id(miww), NumLit(38.39), Continue)), [(Id(Zux), Block([If(BooleanLit(True), VarDecl(Id(fmb), BoolType, None, BooleanLit(False))), [(BooleanLit(False), CallStmt(Id(AY), [BooleanLit(False), StringLit(IZs)]))], Break, Continue])), (NumLit(23.98), VarDecl(Id(R8Ak), None, var, Id(N0vk))), (NumLit(63.61), AssignStmt(Id(ZQI), NumLit(65.48))), (BooleanLit(True), For(Id(Nf), BooleanLit(True), StringLit(pmqo), CallStmt(Id(JvZ), [NumLit(72.41), BooleanLit(True)])))], Block([Continue])), (NumLit(75.34), VarDecl(Id(XY), ArrayType([72.34], NumberType), None, None)), (Id(KUfr), Continue), (Id(z1), Return(BooleanLit(True)))], None])), VarDecl(Id(EKYu), BoolType, None, None), FuncDecl(Id(efr), [VarDecl(Id(k8Z5), ArrayType([3.27], NumberType), None, None), VarDecl(Id(V5), ArrayType([9.5, 51.3, 41.31], NumberType), None, None)], Return()), FuncDecl(Id(QgjS), [VarDecl(Id(j1), NumberType, None, None)], Return()), FuncDecl(Id(Ou), [VarDecl(Id(qgZ), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115788))

	def test_21530115789(self):
		input = '''
func SO ()	return "YmZlM"
string yU3[4.31,64.03,74.34]
func F3yT ()	return false

'''
		expect = '''Program([FuncDecl(Id(SO), [], Return(StringLit(YmZlM))), VarDecl(Id(yU3), ArrayType([4.31, 64.03, 74.34], StringType), None, None), FuncDecl(Id(F3yT), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115789))

	def test_21530115790(self):
		input = '''
number Yv[88.49,0.03,14.19] <- 44.89
'''
		expect = '''Program([VarDecl(Id(Yv), ArrayType([88.49, 0.03, 14.19], NumberType), None, NumLit(44.89))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115790))

	def test_21530115791(self):
		input = '''
func hg (string KcVR[31.0,88.0,65.59])
	return

func oR4Z ()
	return 6.32

func Y09V (number fB)	return

'''
		expect = '''Program([FuncDecl(Id(hg), [VarDecl(Id(KcVR), ArrayType([31.0, 88.0, 65.59], StringType), None, None)], Return()), FuncDecl(Id(oR4Z), [], Return(NumLit(6.32))), FuncDecl(Id(Y09V), [VarDecl(Id(fB), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115791))

	def test_21530115792(self):
		input = '''
func fVJ5 ()	return

bool Zj <- true
bool eP00[47.13]
func Dp3 (number s64, bool qWsU[77.55,10.21])
	return 32.59
'''
		expect = '''Program([FuncDecl(Id(fVJ5), [], Return()), VarDecl(Id(Zj), BoolType, None, BooleanLit(True)), VarDecl(Id(eP00), ArrayType([47.13], BoolType), None, None), FuncDecl(Id(Dp3), [VarDecl(Id(s64), NumberType, None, None), VarDecl(Id(qWsU), ArrayType([77.55, 10.21], BoolType), None, None)], Return(NumLit(32.59)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115792))

	def test_21530115793(self):
		input = '''
bool AHbj[67.4,90.81,11.12] <- "aDXl"
'''
		expect = '''Program([VarDecl(Id(AHbj), ArrayType([67.4, 90.81, 11.12], BoolType), None, StringLit(aDXl))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115793))

	def test_21530115794(self):
		input = '''
func Wt (string Dfc, string vaeu)
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(Wt), [VarDecl(Id(Dfc), StringType, None, None), VarDecl(Id(vaeu), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115794))

	def test_21530115795(self):
		input = '''
string G8[30.99]
func ek ()	return
bool fU <- "SIW"
func NZrx (number RIzU[52.43,14.68], number m_w8[6.66])	return false

'''
		expect = '''Program([VarDecl(Id(G8), ArrayType([30.99], StringType), None, None), FuncDecl(Id(ek), [], Return()), VarDecl(Id(fU), BoolType, None, StringLit(SIW)), FuncDecl(Id(NZrx), [VarDecl(Id(RIzU), ArrayType([52.43, 14.68], NumberType), None, None), VarDecl(Id(m_w8), ArrayType([6.66], NumberType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115795))

	def test_21530115796(self):
		input = '''
dynamic r4Wy <- fdUx
'''
		expect = '''Program([VarDecl(Id(r4Wy), None, dynamic, Id(fdUx))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115796))

	def test_21530115797(self):
		input = '''
func qy (string mF, string wD)
	return true
func aze (bool Y4b4[68.66,28.36,25.19], bool fh2m)	return
func dUVQ (number HUt[49.7,63.33,82.4])	return

number CGM[49.38,72.64,90.99] <- 72.45
func MKk (bool Z7z, bool OT[91.6,5.79])	begin
		continue
		continue
	end

'''
		expect = '''Program([FuncDecl(Id(qy), [VarDecl(Id(mF), StringType, None, None), VarDecl(Id(wD), StringType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(aze), [VarDecl(Id(Y4b4), ArrayType([68.66, 28.36, 25.19], BoolType), None, None), VarDecl(Id(fh2m), BoolType, None, None)], Return()), FuncDecl(Id(dUVQ), [VarDecl(Id(HUt), ArrayType([49.7, 63.33, 82.4], NumberType), None, None)], Return()), VarDecl(Id(CGM), ArrayType([49.38, 72.64, 90.99], NumberType), None, NumLit(72.45)), FuncDecl(Id(MKk), [VarDecl(Id(Z7z), BoolType, None, None), VarDecl(Id(OT), ArrayType([91.6, 5.79], BoolType), None, None)], Block([Continue, Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115797))

	def test_21530115798(self):
		input = '''
func aa (number S0g, string FPBv, bool ia0[7.73,99.98,9.91])
	return

func BS (string u_D[27.75,73.26])
	begin
		return
		if ("hfU")
		if (46.79) if (16.02) var RMvj <- 28.54
		elif (diuV) begin
			break
			fH(true, hFF, xY3)
		end
		elif (true)
		nW6[51.73, bt] <- "ZUky"
		else break
		elif (57.9)
		bool NbSA[95.58,78.9] <- false
		elif ("FLoi")
		rE[t2Yu] <- 27.13
		elif (55.51)
		jbR3 <- 39.44
		elif (21.72)
		Lfs(35.78, true)
		elif (12.95)
		string YF <- 34.06
	end
func Yb ()
	return
func vPFV (bool Y6Z, number XrXq[41.87,63.0])	return fR97

func X7 (bool cJro)	return "CaHXc"

'''
		expect = '''Program([FuncDecl(Id(aa), [VarDecl(Id(S0g), NumberType, None, None), VarDecl(Id(FPBv), StringType, None, None), VarDecl(Id(ia0), ArrayType([7.73, 99.98, 9.91], BoolType), None, None)], Return()), FuncDecl(Id(BS), [VarDecl(Id(u_D), ArrayType([27.75, 73.26], StringType), None, None)], Block([Return(), If(StringLit(hfU), If(NumLit(46.79), If(NumLit(16.02), VarDecl(Id(RMvj), None, var, NumLit(28.54))), [(Id(diuV), Block([Break, CallStmt(Id(fH), [BooleanLit(True), Id(hFF), Id(xY3)])])), (BooleanLit(True), AssignStmt(ArrayCell(Id(nW6), [NumLit(51.73), Id(bt)]), StringLit(ZUky)))], Break), [(NumLit(57.9), VarDecl(Id(NbSA), ArrayType([95.58, 78.9], BoolType), None, BooleanLit(False))), (StringLit(FLoi), AssignStmt(ArrayCell(Id(rE), [Id(t2Yu)]), NumLit(27.13))), (NumLit(55.51), AssignStmt(Id(jbR3), NumLit(39.44))), (NumLit(21.72), CallStmt(Id(Lfs), [NumLit(35.78), BooleanLit(True)])), (NumLit(12.95), VarDecl(Id(YF), StringType, None, NumLit(34.06)))], None), [], None])), FuncDecl(Id(Yb), [], Return()), FuncDecl(Id(vPFV), [VarDecl(Id(Y6Z), BoolType, None, None), VarDecl(Id(XrXq), ArrayType([41.87, 63.0], NumberType), None, None)], Return(Id(fR97))), FuncDecl(Id(X7), [VarDecl(Id(cJro), BoolType, None, None)], Return(StringLit(CaHXc)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115798))

	def test_21530115799(self):
		input = '''
string u2 <- xViY
func B4 ()
	return
var Zq <- vT8Y
number AmCl[92.6,43.57]
'''
		expect = '''Program([VarDecl(Id(u2), StringType, None, Id(xViY)), FuncDecl(Id(B4), [], Return()), VarDecl(Id(Zq), None, var, Id(vT8Y)), VarDecl(Id(AmCl), ArrayType([92.6, 43.57], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115799))

	def test_21530115800(self):
		input = '''
func r9A (string rNi[98.55])
	return false

number jg
dynamic o4U
func WJk (number rL, number mm[78.23,75.04], number wa5G)
	return "rpK"
'''
		expect = '''Program([FuncDecl(Id(r9A), [VarDecl(Id(rNi), ArrayType([98.55], StringType), None, None)], Return(BooleanLit(False))), VarDecl(Id(jg), NumberType, None, None), VarDecl(Id(o4U), None, dynamic, None), FuncDecl(Id(WJk), [VarDecl(Id(rL), NumberType, None, None), VarDecl(Id(mm), ArrayType([78.23, 75.04], NumberType), None, None), VarDecl(Id(wa5G), NumberType, None, None)], Return(StringLit(rpK)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115800))

	def test_21530115801(self):
		input = '''
func zfl ()
	return true

var rS <- "vpdm"
func cbJ (string u8sj[83.0,79.99], string KV, string Hi4)
	return
func qUsR ()
	begin
		LU(99.68)
		return Es5Y
		string bJ[54.94] <- "zg"
	end
'''
		expect = '''Program([FuncDecl(Id(zfl), [], Return(BooleanLit(True))), VarDecl(Id(rS), None, var, StringLit(vpdm)), FuncDecl(Id(cbJ), [VarDecl(Id(u8sj), ArrayType([83.0, 79.99], StringType), None, None), VarDecl(Id(KV), StringType, None, None), VarDecl(Id(Hi4), StringType, None, None)], Return()), FuncDecl(Id(qUsR), [], Block([CallStmt(Id(LU), [NumLit(99.68)]), Return(Id(Es5Y)), VarDecl(Id(bJ), ArrayType([54.94], StringType), None, StringLit(zg))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115801))

	def test_21530115802(self):
		input = '''
string sPs[87.21]
'''
		expect = '''Program([VarDecl(Id(sPs), ArrayType([87.21], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115802))

	def test_21530115803(self):
		input = '''
func K8 (number qgDA, string Al[96.28,8.77,72.79], bool WZH)	begin
		return
	end

func W_ (number uaFw[0.72,10.96])
	begin
		if (JR)
		SlEO <- mg58
		kodN("N")
		string GMN[38.31,37.7] <- hMA
	end

func b7p (bool KMR[49.39,77.64,81.53], number Cax[86.72], bool gIK[43.72])
	return false
string No6h <- 20.73
'''
		expect = '''Program([FuncDecl(Id(K8), [VarDecl(Id(qgDA), NumberType, None, None), VarDecl(Id(Al), ArrayType([96.28, 8.77, 72.79], StringType), None, None), VarDecl(Id(WZH), BoolType, None, None)], Block([Return()])), FuncDecl(Id(W_), [VarDecl(Id(uaFw), ArrayType([0.72, 10.96], NumberType), None, None)], Block([If(Id(JR), AssignStmt(Id(SlEO), Id(mg58))), [], None, CallStmt(Id(kodN), [StringLit(N)]), VarDecl(Id(GMN), ArrayType([38.31, 37.7], StringType), None, Id(hMA))])), FuncDecl(Id(b7p), [VarDecl(Id(KMR), ArrayType([49.39, 77.64, 81.53], BoolType), None, None), VarDecl(Id(Cax), ArrayType([86.72], NumberType), None, None), VarDecl(Id(gIK), ArrayType([43.72], BoolType), None, None)], Return(BooleanLit(False))), VarDecl(Id(No6h), StringType, None, NumLit(20.73))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115803))

	def test_21530115804(self):
		input = '''
func hfS (string nZV7[4.03,83.69], bool cXR7[16.98])	begin
		break
		begin
			continue
			bool Hsv_
			cz("WWPSo", "Z")
		end
		ZP8t(43.89, 59.03, EB)
	end
func yQ7 ()
	return "TRox"

var Ns <- yyi0
bool en[28.02] <- "aIy"
'''
		expect = '''Program([FuncDecl(Id(hfS), [VarDecl(Id(nZV7), ArrayType([4.03, 83.69], StringType), None, None), VarDecl(Id(cXR7), ArrayType([16.98], BoolType), None, None)], Block([Break, Block([Continue, VarDecl(Id(Hsv_), BoolType, None, None), CallStmt(Id(cz), [StringLit(WWPSo), StringLit(Z)])]), CallStmt(Id(ZP8t), [NumLit(43.89), NumLit(59.03), Id(EB)])])), FuncDecl(Id(yQ7), [], Return(StringLit(TRox))), VarDecl(Id(Ns), None, var, Id(yyi0)), VarDecl(Id(en), ArrayType([28.02], BoolType), None, StringLit(aIy))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115804))

	def test_21530115805(self):
		input = '''
string Ps
'''
		expect = '''Program([VarDecl(Id(Ps), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115805))

	def test_21530115806(self):
		input = '''
func Vks7 (number ANRt[22.41,76.73])
	return 71.24

number ZW <- false
func nH (bool Yg[86.23,91.1], number MH[53.68,89.51,92.5])
	return Rxqr
func m1U8 (string o8N, bool zj[68.63,8.61,23.07], number fj[88.49,1.6])
	begin
		var H8wF <- 75.88
		break
	end
'''
		expect = '''Program([FuncDecl(Id(Vks7), [VarDecl(Id(ANRt), ArrayType([22.41, 76.73], NumberType), None, None)], Return(NumLit(71.24))), VarDecl(Id(ZW), NumberType, None, BooleanLit(False)), FuncDecl(Id(nH), [VarDecl(Id(Yg), ArrayType([86.23, 91.1], BoolType), None, None), VarDecl(Id(MH), ArrayType([53.68, 89.51, 92.5], NumberType), None, None)], Return(Id(Rxqr))), FuncDecl(Id(m1U8), [VarDecl(Id(o8N), StringType, None, None), VarDecl(Id(zj), ArrayType([68.63, 8.61, 23.07], BoolType), None, None), VarDecl(Id(fj), ArrayType([88.49, 1.6], NumberType), None, None)], Block([VarDecl(Id(H8wF), None, var, NumLit(75.88)), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115806))

	def test_21530115807(self):
		input = '''
func Mf (bool sR0a[76.52])
	return "fH"
'''
		expect = '''Program([FuncDecl(Id(Mf), [VarDecl(Id(sR0a), ArrayType([76.52], BoolType), None, None)], Return(StringLit(fH)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115807))

	def test_21530115808(self):
		input = '''
dynamic Cgn
func tGOJ ()
	return Jbg

func JKFe (bool czy)	return false
func tX14 (string Ab[1.03,93.69])
	begin
		continue
		fW3["qhW", false, "vu"] <- "CeqUW"
		nLtF <- 71.0
	end

func rPwT (bool Bl)
	return "gWaAA"

'''
		expect = '''Program([VarDecl(Id(Cgn), None, dynamic, None), FuncDecl(Id(tGOJ), [], Return(Id(Jbg))), FuncDecl(Id(JKFe), [VarDecl(Id(czy), BoolType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(tX14), [VarDecl(Id(Ab), ArrayType([1.03, 93.69], StringType), None, None)], Block([Continue, AssignStmt(ArrayCell(Id(fW3), [StringLit(qhW), BooleanLit(False), StringLit(vu)]), StringLit(CeqUW)), AssignStmt(Id(nLtF), NumLit(71.0))])), FuncDecl(Id(rPwT), [VarDecl(Id(Bl), BoolType, None, None)], Return(StringLit(gWaAA)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115808))

	def test_21530115809(self):
		input = '''
func qZ (string NG[8.3,72.82])
	begin
	end
func guo5 ()	return "Q"

func BH (number yRk)
	return
func Par (number pWU, bool kGL)	return

'''
		expect = '''Program([FuncDecl(Id(qZ), [VarDecl(Id(NG), ArrayType([8.3, 72.82], StringType), None, None)], Block([])), FuncDecl(Id(guo5), [], Return(StringLit(Q))), FuncDecl(Id(BH), [VarDecl(Id(yRk), NumberType, None, None)], Return()), FuncDecl(Id(Par), [VarDecl(Id(pWU), NumberType, None, None), VarDecl(Id(kGL), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115809))

	def test_21530115810(self):
		input = '''
bool kkhc[57.75]
var qhn <- "qKiIn"
'''
		expect = '''Program([VarDecl(Id(kkhc), ArrayType([57.75], BoolType), None, None), VarDecl(Id(qhn), None, var, StringLit(qKiIn))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115810))

	def test_21530115811(self):
		input = '''
func X8hG ()
	return 26.99

'''
		expect = '''Program([FuncDecl(Id(X8hG), [], Return(NumLit(26.99)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115811))

	def test_21530115812(self):
		input = '''
func wA (bool hslV, bool vz[69.47,11.51,33.15], string UW)
	return
func iJ0 (string rZ5f[7.7,18.45,39.04])	begin
		begin
			return 6.04
		end
	end

string qc[8.21] <- "U"
'''
		expect = '''Program([FuncDecl(Id(wA), [VarDecl(Id(hslV), BoolType, None, None), VarDecl(Id(vz), ArrayType([69.47, 11.51, 33.15], BoolType), None, None), VarDecl(Id(UW), StringType, None, None)], Return()), FuncDecl(Id(iJ0), [VarDecl(Id(rZ5f), ArrayType([7.7, 18.45, 39.04], StringType), None, None)], Block([Block([Return(NumLit(6.04))])])), VarDecl(Id(qc), ArrayType([8.21], StringType), None, StringLit(U))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115812))

	def test_21530115813(self):
		input = '''
func o6 (string d9Rx, string vxa)	begin
		VQVJ <- "pxy"
		continue
	end
func fdE ()	return
var D3hZ <- uliT
bool prp[88.6,6.17,52.23]
'''
		expect = '''Program([FuncDecl(Id(o6), [VarDecl(Id(d9Rx), StringType, None, None), VarDecl(Id(vxa), StringType, None, None)], Block([AssignStmt(Id(VQVJ), StringLit(pxy)), Continue])), FuncDecl(Id(fdE), [], Return()), VarDecl(Id(D3hZ), None, var, Id(uliT)), VarDecl(Id(prp), ArrayType([88.6, 6.17, 52.23], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115813))

	def test_21530115814(self):
		input = '''
bool Kz[0.27,13.66] <- "kUS"
number mRkQ[70.33,73.68] <- VC
bool MdzC[44.37] <- 25.84
'''
		expect = '''Program([VarDecl(Id(Kz), ArrayType([0.27, 13.66], BoolType), None, StringLit(kUS)), VarDecl(Id(mRkQ), ArrayType([70.33, 73.68], NumberType), None, Id(VC)), VarDecl(Id(MdzC), ArrayType([44.37], BoolType), None, NumLit(25.84))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115814))

	def test_21530115815(self):
		input = '''
number HVik[34.71]
'''
		expect = '''Program([VarDecl(Id(HVik), ArrayType([34.71], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115815))

	def test_21530115816(self):
		input = '''
string Jlw[79.23,18.61] <- "Yi"
string zN[91.06,6.97] <- false
var kT <- true
'''
		expect = '''Program([VarDecl(Id(Jlw), ArrayType([79.23, 18.61], StringType), None, StringLit(Yi)), VarDecl(Id(zN), ArrayType([91.06, 6.97], StringType), None, BooleanLit(False)), VarDecl(Id(kT), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115816))

	def test_21530115817(self):
		input = '''
number kB[30.64] <- 96.4
func O2 (number uA, number qvM, number dFhr[17.51])	return

func v8f ()	begin
		rb(Qy, 53.12)
	end
func su ()
	begin
		break
		bool F1te <- false
	end

'''
		expect = '''Program([VarDecl(Id(kB), ArrayType([30.64], NumberType), None, NumLit(96.4)), FuncDecl(Id(O2), [VarDecl(Id(uA), NumberType, None, None), VarDecl(Id(qvM), NumberType, None, None), VarDecl(Id(dFhr), ArrayType([17.51], NumberType), None, None)], Return()), FuncDecl(Id(v8f), [], Block([CallStmt(Id(rb), [Id(Qy), NumLit(53.12)])])), FuncDecl(Id(su), [], Block([Break, VarDecl(Id(F1te), BoolType, None, BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115817))

	def test_21530115818(self):
		input = '''
func RVb ()	return
func zaZ ()
	return 67.56
'''
		expect = '''Program([FuncDecl(Id(RVb), [], Return()), FuncDecl(Id(zaZ), [], Return(NumLit(67.56)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115818))

	def test_21530115819(self):
		input = '''
func BR ()	return iAt
func l3lY (number KY1[80.65,36.11,93.84], number V54[69.36,23.22])	return
func W3S6 ()	return

'''
		expect = '''Program([FuncDecl(Id(BR), [], Return(Id(iAt))), FuncDecl(Id(l3lY), [VarDecl(Id(KY1), ArrayType([80.65, 36.11, 93.84], NumberType), None, None), VarDecl(Id(V54), ArrayType([69.36, 23.22], NumberType), None, None)], Return()), FuncDecl(Id(W3S6), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115819))

	def test_21530115820(self):
		input = '''
bool Up8s
'''
		expect = '''Program([VarDecl(Id(Up8s), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115820))

	def test_21530115821(self):
		input = '''
number iI54 <- false
string Qn4[56.4,46.65,47.56] <- 13.36
number Jc_
func B05 ()	return

'''
		expect = '''Program([VarDecl(Id(iI54), NumberType, None, BooleanLit(False)), VarDecl(Id(Qn4), ArrayType([56.4, 46.65, 47.56], StringType), None, NumLit(13.36)), VarDecl(Id(Jc_), NumberType, None, None), FuncDecl(Id(B05), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115821))

	def test_21530115822(self):
		input = '''
func Ss ()	return "qxd"
var n0B <- eBx4
func D7ib (bool ad0H[18.23], string mOIS[69.89,60.75,59.85], number OkMd[81.97,63.22,42.76])	return
func vn (number dHH)
	return AL

func AHyU ()
	return srT
'''
		expect = '''Program([FuncDecl(Id(Ss), [], Return(StringLit(qxd))), VarDecl(Id(n0B), None, var, Id(eBx4)), FuncDecl(Id(D7ib), [VarDecl(Id(ad0H), ArrayType([18.23], BoolType), None, None), VarDecl(Id(mOIS), ArrayType([69.89, 60.75, 59.85], StringType), None, None), VarDecl(Id(OkMd), ArrayType([81.97, 63.22, 42.76], NumberType), None, None)], Return()), FuncDecl(Id(vn), [VarDecl(Id(dHH), NumberType, None, None)], Return(Id(AL))), FuncDecl(Id(AHyU), [], Return(Id(srT)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115822))

	def test_21530115823(self):
		input = '''
number H88r[8.04,63.72]
bool igI6[78.67]
bool fk <- false
'''
		expect = '''Program([VarDecl(Id(H88r), ArrayType([8.04, 63.72], NumberType), None, None), VarDecl(Id(igI6), ArrayType([78.67], BoolType), None, None), VarDecl(Id(fk), BoolType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115823))

	def test_21530115824(self):
		input = '''
func Upz (string KAo)
	return
bool Mh[46.41,50.51]
'''
		expect = '''Program([FuncDecl(Id(Upz), [VarDecl(Id(KAo), StringType, None, None)], Return()), VarDecl(Id(Mh), ArrayType([46.41, 50.51], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115824))

	def test_21530115825(self):
		input = '''
func ZVnS (bool fQ, number jXH[70.2], string THgq)	return
number GeS_[54.96,52.25,9.66]
'''
		expect = '''Program([FuncDecl(Id(ZVnS), [VarDecl(Id(fQ), BoolType, None, None), VarDecl(Id(jXH), ArrayType([70.2], NumberType), None, None), VarDecl(Id(THgq), StringType, None, None)], Return()), VarDecl(Id(GeS_), ArrayType([54.96, 52.25, 9.66], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115825))

	def test_21530115826(self):
		input = '''
func RG ()	begin
		pb_s(false, true)
		continue
		return true
	end
bool NSq[47.83,50.39,60.93] <- true
bool juN[44.57]
func sMjT (string Na, bool lw[60.18,41.03], number uCUI[53.21])
	begin
		eaDu["LzS"] <- 80.59
	end
string Sv[77.11,67.36,99.36] <- "YUy"
'''
		expect = '''Program([FuncDecl(Id(RG), [], Block([CallStmt(Id(pb_s), [BooleanLit(False), BooleanLit(True)]), Continue, Return(BooleanLit(True))])), VarDecl(Id(NSq), ArrayType([47.83, 50.39, 60.93], BoolType), None, BooleanLit(True)), VarDecl(Id(juN), ArrayType([44.57], BoolType), None, None), FuncDecl(Id(sMjT), [VarDecl(Id(Na), StringType, None, None), VarDecl(Id(lw), ArrayType([60.18, 41.03], BoolType), None, None), VarDecl(Id(uCUI), ArrayType([53.21], NumberType), None, None)], Block([AssignStmt(ArrayCell(Id(eaDu), [StringLit(LzS)]), NumLit(80.59))])), VarDecl(Id(Sv), ArrayType([77.11, 67.36, 99.36], StringType), None, StringLit(YUy))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115826))

	def test_21530115827(self):
		input = '''
number T9sP[3.38,55.92,62.42]
'''
		expect = '''Program([VarDecl(Id(T9sP), ArrayType([3.38, 55.92, 62.42], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115827))

	def test_21530115828(self):
		input = '''
string firM[41.7,10.78,43.53]
func AgDC ()
	begin
		return
		continue
	end

bool mj2 <- "eMgXY"
bool WAZ[15.49]
'''
		expect = '''Program([VarDecl(Id(firM), ArrayType([41.7, 10.78, 43.53], StringType), None, None), FuncDecl(Id(AgDC), [], Block([Return(), Continue])), VarDecl(Id(mj2), BoolType, None, StringLit(eMgXY)), VarDecl(Id(WAZ), ArrayType([15.49], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115828))

	def test_21530115829(self):
		input = '''
var N0 <- "AE"
func stEl (bool NUI, bool CM, number rD9b)	begin
		return
		Hpk2("f", xh)
	end
func dQMF (number XviQ[31.47,41.64])
	return "fD"

func s4P (string dSd, string SNA, number Qdx)
	return 94.69

bool jH
'''
		expect = '''Program([VarDecl(Id(N0), None, var, StringLit(AE)), FuncDecl(Id(stEl), [VarDecl(Id(NUI), BoolType, None, None), VarDecl(Id(CM), BoolType, None, None), VarDecl(Id(rD9b), NumberType, None, None)], Block([Return(), CallStmt(Id(Hpk2), [StringLit(f), Id(xh)])])), FuncDecl(Id(dQMF), [VarDecl(Id(XviQ), ArrayType([31.47, 41.64], NumberType), None, None)], Return(StringLit(fD))), FuncDecl(Id(s4P), [VarDecl(Id(dSd), StringType, None, None), VarDecl(Id(SNA), StringType, None, None), VarDecl(Id(Qdx), NumberType, None, None)], Return(NumLit(94.69))), VarDecl(Id(jH), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115829))

	def test_21530115830(self):
		input = '''
func zhzH (number dQ)
	begin
	end
number ClYW[1.25]
'''
		expect = '''Program([FuncDecl(Id(zhzH), [VarDecl(Id(dQ), NumberType, None, None)], Block([])), VarDecl(Id(ClYW), ArrayType([1.25], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115830))

	def test_21530115831(self):
		input = '''
func At9 ()
	return 53.67
string CzgB[38.91,10.5]
'''
		expect = '''Program([FuncDecl(Id(At9), [], Return(NumLit(53.67))), VarDecl(Id(CzgB), ArrayType([38.91, 10.5], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115831))

	def test_21530115832(self):
		input = '''
string Rf
func Yq ()
	return 53.84

'''
		expect = '''Program([VarDecl(Id(Rf), StringType, None, None), FuncDecl(Id(Yq), [], Return(NumLit(53.84)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115832))

	def test_21530115833(self):
		input = '''
bool waZ7
dynamic GOaa
func muWT ()
	begin
		begin
		end
		return
		for pP until true by enU0
			dynamic xx
	end
func lG_E ()	return

'''
		expect = '''Program([VarDecl(Id(waZ7), BoolType, None, None), VarDecl(Id(GOaa), None, dynamic, None), FuncDecl(Id(muWT), [], Block([Block([]), Return(), For(Id(pP), BooleanLit(True), Id(enU0), VarDecl(Id(xx), None, dynamic, None))])), FuncDecl(Id(lG_E), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115833))

	def test_21530115834(self):
		input = '''
func Ztq ()
	return "sn"

'''
		expect = '''Program([FuncDecl(Id(Ztq), [], Return(StringLit(sn)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115834))

	def test_21530115835(self):
		input = '''
func Q3_ (number D5LA, bool Ac2_[92.07,75.66])
	return "pc"

var J2Pn <- "E"
'''
		expect = '''Program([FuncDecl(Id(Q3_), [VarDecl(Id(D5LA), NumberType, None, None), VarDecl(Id(Ac2_), ArrayType([92.07, 75.66], BoolType), None, None)], Return(StringLit(pc))), VarDecl(Id(J2Pn), None, var, StringLit(E))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115835))

	def test_21530115836(self):
		input = '''
func bRm1 (number dAC, number W1RA)
	begin
	end

func X9 (number Xox[68.98,53.53], string BJ1u[60.5], string N6e)	begin
		return true
	end
'''
		expect = '''Program([FuncDecl(Id(bRm1), [VarDecl(Id(dAC), NumberType, None, None), VarDecl(Id(W1RA), NumberType, None, None)], Block([])), FuncDecl(Id(X9), [VarDecl(Id(Xox), ArrayType([68.98, 53.53], NumberType), None, None), VarDecl(Id(BJ1u), ArrayType([60.5], StringType), None, None), VarDecl(Id(N6e), StringType, None, None)], Block([Return(BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115836))

	def test_21530115837(self):
		input = '''
func HYdM ()
	begin
		Y5py <- "QVBg"
		return "eGbP"
	end

'''
		expect = '''Program([FuncDecl(Id(HYdM), [], Block([AssignStmt(Id(Y5py), StringLit(QVBg)), Return(StringLit(eGbP))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115837))

	def test_21530115838(self):
		input = '''
func gZ (number jS[90.44,23.48,90.51], string HC[13.83,16.72], bool PAk[56.63,80.15])
	return

func EDL ()
	return Qmm
bool HsnZ
'''
		expect = '''Program([FuncDecl(Id(gZ), [VarDecl(Id(jS), ArrayType([90.44, 23.48, 90.51], NumberType), None, None), VarDecl(Id(HC), ArrayType([13.83, 16.72], StringType), None, None), VarDecl(Id(PAk), ArrayType([56.63, 80.15], BoolType), None, None)], Return()), FuncDecl(Id(EDL), [], Return(Id(Qmm))), VarDecl(Id(HsnZ), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115838))

	def test_21530115839(self):
		input = '''
dynamic ea <- "WMO"
number Cg[13.76,94.71]
'''
		expect = '''Program([VarDecl(Id(ea), None, dynamic, StringLit(WMO)), VarDecl(Id(Cg), ArrayType([13.76, 94.71], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115839))

	def test_21530115840(self):
		input = '''
string ga
'''
		expect = '''Program([VarDecl(Id(ga), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115840))

	def test_21530115841(self):
		input = '''
func Qd (number CDwq, string mUS[29.9,21.11], number Zy)	return YGpj

number zn <- false
var SJZO <- true
dynamic q0jz
func GqG (bool wL7[31.77,11.25,69.42])	begin
		continue
		number fSF_[61.62,53.86] <- "ZK"
		sNo()
	end

'''
		expect = '''Program([FuncDecl(Id(Qd), [VarDecl(Id(CDwq), NumberType, None, None), VarDecl(Id(mUS), ArrayType([29.9, 21.11], StringType), None, None), VarDecl(Id(Zy), NumberType, None, None)], Return(Id(YGpj))), VarDecl(Id(zn), NumberType, None, BooleanLit(False)), VarDecl(Id(SJZO), None, var, BooleanLit(True)), VarDecl(Id(q0jz), None, dynamic, None), FuncDecl(Id(GqG), [VarDecl(Id(wL7), ArrayType([31.77, 11.25, 69.42], BoolType), None, None)], Block([Continue, VarDecl(Id(fSF_), ArrayType([61.62, 53.86], NumberType), None, StringLit(ZK)), CallStmt(Id(sNo), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115841))

	def test_21530115842(self):
		input = '''
func j62 ()
	begin
		continue
	end
number FvS[68.03,8.62] <- true
func OIb (string uU7)
	return false
number e6F <- oCIm
'''
		expect = '''Program([FuncDecl(Id(j62), [], Block([Continue])), VarDecl(Id(FvS), ArrayType([68.03, 8.62], NumberType), None, BooleanLit(True)), FuncDecl(Id(OIb), [VarDecl(Id(uU7), StringType, None, None)], Return(BooleanLit(False))), VarDecl(Id(e6F), NumberType, None, Id(oCIm))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115842))

	def test_21530115843(self):
		input = '''
func abX ()
	begin
		begin
		end
	end

var Jd9Y <- bD
func g8sB ()
	return
'''
		expect = '''Program([FuncDecl(Id(abX), [], Block([Block([])])), VarDecl(Id(Jd9Y), None, var, Id(bD)), FuncDecl(Id(g8sB), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115843))

	def test_21530115844(self):
		input = '''
string FQr[48.31,19.34,54.49]
func iZ ()
	return
dynamic kI <- "R"
string GV0 <- wHSv
'''
		expect = '''Program([VarDecl(Id(FQr), ArrayType([48.31, 19.34, 54.49], StringType), None, None), FuncDecl(Id(iZ), [], Return()), VarDecl(Id(kI), None, dynamic, StringLit(R)), VarDecl(Id(GV0), StringType, None, Id(wHSv))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115844))

	def test_21530115845(self):
		input = '''
func VpZ (number QCP[61.43], string El)
	return
number BrgU <- false
'''
		expect = '''Program([FuncDecl(Id(VpZ), [VarDecl(Id(QCP), ArrayType([61.43], NumberType), None, None), VarDecl(Id(El), StringType, None, None)], Return()), VarDecl(Id(BrgU), NumberType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115845))

	def test_21530115846(self):
		input = '''
func ls0W (number PB[57.96,2.28], bool ss[3.07,27.18], string v7O[77.44,94.68,48.54])	begin
	end

func v07 (bool mEG[83.75,6.64], number fp[37.57], bool Usn)
	return 83.62

bool ZBHP[20.96,1.12,26.2]
'''
		expect = '''Program([FuncDecl(Id(ls0W), [VarDecl(Id(PB), ArrayType([57.96, 2.28], NumberType), None, None), VarDecl(Id(ss), ArrayType([3.07, 27.18], BoolType), None, None), VarDecl(Id(v7O), ArrayType([77.44, 94.68, 48.54], StringType), None, None)], Block([])), FuncDecl(Id(v07), [VarDecl(Id(mEG), ArrayType([83.75, 6.64], BoolType), None, None), VarDecl(Id(fp), ArrayType([37.57], NumberType), None, None), VarDecl(Id(Usn), BoolType, None, None)], Return(NumLit(83.62))), VarDecl(Id(ZBHP), ArrayType([20.96, 1.12, 26.2], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115846))

	def test_21530115847(self):
		input = '''
func JxO (string aP)	begin
	end
number hcuO
'''
		expect = '''Program([FuncDecl(Id(JxO), [VarDecl(Id(aP), StringType, None, None)], Block([])), VarDecl(Id(hcuO), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115847))

	def test_21530115848(self):
		input = '''
string A2[66.96,83.52,32.1] <- true
'''
		expect = '''Program([VarDecl(Id(A2), ArrayType([66.96, 83.52, 32.1], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115848))

	def test_21530115849(self):
		input = '''
func VB (number tuY[65.96,87.07])
	begin
	end
func kA (string zu[11.51,99.13,43.57])	return
'''
		expect = '''Program([FuncDecl(Id(VB), [VarDecl(Id(tuY), ArrayType([65.96, 87.07], NumberType), None, None)], Block([])), FuncDecl(Id(kA), [VarDecl(Id(zu), ArrayType([11.51, 99.13, 43.57], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115849))

	def test_21530115850(self):
		input = '''
dynamic LPa2 <- false
func bpd (string JJ[39.25], number G10, bool Ydr[30.05])	return 13.39
'''
		expect = '''Program([VarDecl(Id(LPa2), None, dynamic, BooleanLit(False)), FuncDecl(Id(bpd), [VarDecl(Id(JJ), ArrayType([39.25], StringType), None, None), VarDecl(Id(G10), NumberType, None, None), VarDecl(Id(Ydr), ArrayType([30.05], BoolType), None, None)], Return(NumLit(13.39)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115850))

	def test_21530115851(self):
		input = '''
number Tg[57.15] <- true
number JWdP
'''
		expect = '''Program([VarDecl(Id(Tg), ArrayType([57.15], NumberType), None, BooleanLit(True)), VarDecl(Id(JWdP), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115851))

	def test_21530115852(self):
		input = '''
func enL (number EfS)	return
func lp (number XBLn[40.18])
	begin
		if (true) continue
	end
func axA ()
	begin
		return false
	end

'''
		expect = '''Program([FuncDecl(Id(enL), [VarDecl(Id(EfS), NumberType, None, None)], Return()), FuncDecl(Id(lp), [VarDecl(Id(XBLn), ArrayType([40.18], NumberType), None, None)], Block([If(BooleanLit(True), Continue), [], None])), FuncDecl(Id(axA), [], Block([Return(BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115852))

	def test_21530115853(self):
		input = '''
func svNw (bool mKgy, number UPC)	begin
		number oO[20.79]
		break
	end

func JC9 (string M4[90.84], bool iBP)
	return

bool qxt
'''
		expect = '''Program([FuncDecl(Id(svNw), [VarDecl(Id(mKgy), BoolType, None, None), VarDecl(Id(UPC), NumberType, None, None)], Block([VarDecl(Id(oO), ArrayType([20.79], NumberType), None, None), Break])), FuncDecl(Id(JC9), [VarDecl(Id(M4), ArrayType([90.84], StringType), None, None), VarDecl(Id(iBP), BoolType, None, None)], Return()), VarDecl(Id(qxt), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115853))

	def test_21530115854(self):
		input = '''
number AiYW
'''
		expect = '''Program([VarDecl(Id(AiYW), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115854))

	def test_21530115855(self):
		input = '''
func Htj (bool qiZN[65.19,89.85,53.58], bool V_Sx[40.99,29.1])	begin
		return true
		return false
		sXiL[62.43, 89.63] <- 12.7
	end

string Hp
'''
		expect = '''Program([FuncDecl(Id(Htj), [VarDecl(Id(qiZN), ArrayType([65.19, 89.85, 53.58], BoolType), None, None), VarDecl(Id(V_Sx), ArrayType([40.99, 29.1], BoolType), None, None)], Block([Return(BooleanLit(True)), Return(BooleanLit(False)), AssignStmt(ArrayCell(Id(sXiL), [NumLit(62.43), NumLit(89.63)]), NumLit(12.7))])), VarDecl(Id(Hp), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115855))

	def test_21530115856(self):
		input = '''
bool Ar[8.61] <- 38.24
func vKi (bool VIS[50.25,10.02,7.13])	begin
		if (HCke) begin
			if ("Xl") break
			elif ("PH") number PD[94.66,22.49]
			elif (T_k) ku(EOqt, true)
			elif (22.96) break
			elif (true)
			for UG until "B" by true
				q6(false)
			for nO until Fq9 by uMp
				t0XR <- 2.5
		end
		elif (96.55) bool Oy
		elif (false) JC("UURS", 57.5, "xdC")
		elif (lFS) continue
	end
func GiVB (string I_t, string wZ[14.66,36.15])	begin
	end
'''
		expect = '''Program([VarDecl(Id(Ar), ArrayType([8.61], BoolType), None, NumLit(38.24)), FuncDecl(Id(vKi), [VarDecl(Id(VIS), ArrayType([50.25, 10.02, 7.13], BoolType), None, None)], Block([If(Id(HCke), Block([If(StringLit(Xl), Break), [(StringLit(PH), VarDecl(Id(PD), ArrayType([94.66, 22.49], NumberType), None, None)), (Id(T_k), CallStmt(Id(ku), [Id(EOqt), BooleanLit(True)])), (NumLit(22.96), Break), (BooleanLit(True), For(Id(UG), StringLit(B), BooleanLit(True), CallStmt(Id(q6), [BooleanLit(False)])))], None, For(Id(nO), Id(Fq9), Id(uMp), AssignStmt(Id(t0XR), NumLit(2.5)))])), [(NumLit(96.55), VarDecl(Id(Oy), BoolType, None, None)), (BooleanLit(False), CallStmt(Id(JC), [StringLit(UURS), NumLit(57.5), StringLit(xdC)])), (Id(lFS), Continue)], None])), FuncDecl(Id(GiVB), [VarDecl(Id(I_t), StringType, None, None), VarDecl(Id(wZ), ArrayType([14.66, 36.15], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115856))

	def test_21530115857(self):
		input = '''
bool C7bQ[86.31] <- Kd
func bHR_ (string yTl[64.7], number eWLd)	return TFIC

bool w3[83.24,24.16]
number cRe4[8.68,25.12,13.36]
func DRx (number tEmL[75.28,29.8], bool Fg)	begin
		continue
		if (pc)
		dynamic uHH
		elif (bMJu)
		begin
			v9[qi] <- 6.28
			return
			ego(6.18, 18.83, "zy")
		end
		elif (11.36)
		return
		elif ("tycO") return
		elif ("DFnih")
		if (true)
		s9a <- NY
		elif (false) continue
		elif (VmMG) return pr9
		elif ("KkbLm")
		continue
		elif ("ur") km <- 61.52
		else for r6p8 until "C" by true
			number AS[10.03,37.27,48.45] <- "UVvxs"
		elif (false) string Xald[5.16,18.18]
	end

'''
		expect = '''Program([VarDecl(Id(C7bQ), ArrayType([86.31], BoolType), None, Id(Kd)), FuncDecl(Id(bHR_), [VarDecl(Id(yTl), ArrayType([64.7], StringType), None, None), VarDecl(Id(eWLd), NumberType, None, None)], Return(Id(TFIC))), VarDecl(Id(w3), ArrayType([83.24, 24.16], BoolType), None, None), VarDecl(Id(cRe4), ArrayType([8.68, 25.12, 13.36], NumberType), None, None), FuncDecl(Id(DRx), [VarDecl(Id(tEmL), ArrayType([75.28, 29.8], NumberType), None, None), VarDecl(Id(Fg), BoolType, None, None)], Block([Continue, If(Id(pc), VarDecl(Id(uHH), None, dynamic, None)), [(Id(bMJu), Block([AssignStmt(ArrayCell(Id(v9), [Id(qi)]), NumLit(6.28)), Return(), CallStmt(Id(ego), [NumLit(6.18), NumLit(18.83), StringLit(zy)])])), (NumLit(11.36), Return()), (StringLit(tycO), Return()), (StringLit(DFnih), If(BooleanLit(True), AssignStmt(Id(s9a), Id(NY))), [(BooleanLit(False), Continue), (Id(VmMG), Return(Id(pr9))), (StringLit(KkbLm), Continue), (StringLit(ur), AssignStmt(Id(km), NumLit(61.52)))], For(Id(r6p8), StringLit(C), BooleanLit(True), VarDecl(Id(AS), ArrayType([10.03, 37.27, 48.45], NumberType), None, StringLit(UVvxs)))), (BooleanLit(False), VarDecl(Id(Xald), ArrayType([5.16, 18.18], StringType), None, None))], None]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115857))

	def test_21530115858(self):
		input = '''
func ty (bool Q_Q[55.02,19.31], string hS, bool y1A)
	return
'''
		expect = '''Program([FuncDecl(Id(ty), [VarDecl(Id(Q_Q), ArrayType([55.02, 19.31], BoolType), None, None), VarDecl(Id(hS), StringType, None, None), VarDecl(Id(y1A), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115858))

	def test_21530115859(self):
		input = '''
number O_[66.16] <- AfTZ
bool HsYz[45.95] <- "S"
func La (bool gdKm[25.94,11.07])
	begin
		if (6.29)
		return
		elif ("RHmU") string QiV[56.5] <- "DNZhJ"
		elif ("hwDsL")
		if (true) continue
		elif (UAqg) if (ag) for NQ until 48.32 by is
			continue
		elif (false) break
		elif (74.38)
		if ("Nwu")
		if (Sm)
		QiI[VasO] <- true
		elif (true)
		fx(true, false, hR)
		elif (false)
		break
		elif (88.08)
		if (71.8)
		number DJh[4.07,98.98] <- true
		elif ("ACf")
		L6(26.65, "IxZI", true)
		else return 44.52
		elif ("phGr")
		W10[32.39] <- mJJ
		elif ("OwS") break
		elif (74.02) OjPS[false, o2Su, "ySZ"] <- 18.08
		else VFY(Zxq_, false, 17.57)
		elif (nj6)
		if (false) begin
			if ("VmN")
			if ("XQra") for kX until false by false
				for xnf4 until false by "OK"
					return VK
			elif (NUDa) for S1 until true by NgAh
				continue
			elif (false)
			if (false) usAY(XH, true)
			elif (Df) break
			elif (vi) for ph until Fmy5 by "vBG"
				begin
					begin
						for WH8_ until false by pG
							lDv[false, true] <- 40.62
						qI["lSOd", false, "CZOEk"] <- ynyr
						return eRLu
					end
					begin
						continue
						break
						break
					end
				end
			elif (false)
			TnoS <- 18.75
			elif (98.11) if (SP) break
			elif ("D")
			continue
			elif (70.17)
			begin
				if (true) return
				else number K0
			end
			elif (C4RA)
			string Aw[32.64,73.31] <- gqpi
			elif (NC)
			ETqH[0.01, false] <- GSe
			else break
			elif (Dk7) begin
			end
			else for OkF7 until true by true
				if (13.76) T1x()
				elif ("ZXoJJ") break
				elif (wSB) pIO(vYXB, AV, 89.75)
				elif (96.16)
				for ya until false by true
					number RETH
				elif ("IV")
				QHm()
				elif (Gb) WMb_()
				else ePI["nZ", "THD"] <- "tzJ"
			elif (true)
			break
			elif (true) return
			elif (80.67)
			number Qm <- GZQ
			else begin
				return
				for Mz until false by false
					continue
				rBTw["l"] <- S6Q0
			end
			return
		end
		elif (false) begin
			begin
			end
		end
		elif ("KvmYm")
		return
		elif (true)
		begin
			Xah["cBNwh"] <- true
			return 89.61
		end
		elif (EZ)
		continue
		else continue
		elif ("NANbj") string i_Ju <- 30.25
		elif (88.65)
		break
		elif (true) break
		elif (V8)
		ERaP <- "Hs"
		elif ("KKZpW")
		vRO(true, 8.21, 38.63)
		elif ("zEKg") begin
			if ("t") if (52.96)
			return true
			elif (26.81)
			fpO(zGU, "chBD", GU)
			elif (false) for mrIy until 60.93 by true
				if ("juw")
				FhZ("tbQbw")
				elif ("Fk") CXR(BX, sxn, "ouvN")
				elif (false) for cFL until 12.9 by 22.56
					continue
				elif (vVE6)
				av("Dl", 86.22, "Kbq")
			elif (false)
			bool IWN9[85.22] <- At
			elif (xN) if (u9)
			string sL
			elif ("b")
			begin
				string cQ[51.82] <- "png"
				var uZi <- false
			end
			elif (kF)
			continue
			elif ("cl")
			break
			elif (false)
			break
			elif (true) begin
				return
				for cdDP until false by TVD
					begin
						dynamic Qd5 <- 6.09
					end
				bool yT[85.85,45.84,84.51]
			end
			else if (true) for Fu until false by "JN"
				continue
			else continue
			elif (true)
			bool G37[81.28,65.8,31.15]
			elif (Uc_Y)
			if (true)
			break
			elif ("JbUI") Tyi <- 20.66
			elif (true)
			continue
		end
		elif (false)
		h0()
		elif (19.46) if (95.24) Wa[34.64, true] <- 89.7
		elif (jd1)
		for Rz5 until "Edr" by 22.6
			return oh
		elif (false)
		begin
			continue
			begin
				v7()
			end
			continue
		end
		else continue
		else return
		break
	end
func Rik (bool kt[45.62])	begin
		for e02u until 52.59 by 34.85
			break
	end
'''
		expect = '''Program([VarDecl(Id(O_), ArrayType([66.16], NumberType), None, Id(AfTZ)), VarDecl(Id(HsYz), ArrayType([45.95], BoolType), None, StringLit(S)), FuncDecl(Id(La), [VarDecl(Id(gdKm), ArrayType([25.94, 11.07], BoolType), None, None)], Block([If(NumLit(6.29), Return()), [(StringLit(RHmU), VarDecl(Id(QiV), ArrayType([56.5], StringType), None, StringLit(DNZhJ))), (StringLit(hwDsL), If(BooleanLit(True), Continue), [(Id(UAqg), If(Id(ag), For(Id(NQ), NumLit(48.32), Id(is), Continue)), [(BooleanLit(False), Break), (NumLit(74.38), If(StringLit(Nwu), If(Id(Sm), AssignStmt(ArrayCell(Id(QiI), [Id(VasO)]), BooleanLit(True))), [(BooleanLit(True), CallStmt(Id(fx), [BooleanLit(True), BooleanLit(False), Id(hR)])), (BooleanLit(False), Break), (NumLit(88.08), If(NumLit(71.8), VarDecl(Id(DJh), ArrayType([4.07, 98.98], NumberType), None, BooleanLit(True))), [(StringLit(ACf), CallStmt(Id(L6), [NumLit(26.65), StringLit(IxZI), BooleanLit(True)]))], Return(NumLit(44.52))), (StringLit(phGr), AssignStmt(ArrayCell(Id(W10), [NumLit(32.39)]), Id(mJJ))), (StringLit(OwS), Break), (NumLit(74.02), AssignStmt(ArrayCell(Id(OjPS), [BooleanLit(False), Id(o2Su), StringLit(ySZ)]), NumLit(18.08)))], CallStmt(Id(VFY), [Id(Zxq_), BooleanLit(False), NumLit(17.57)])), [(Id(nj6), If(BooleanLit(False), Block([If(StringLit(VmN), If(StringLit(XQra), For(Id(kX), BooleanLit(False), BooleanLit(False), For(Id(xnf4), BooleanLit(False), StringLit(OK), Return(Id(VK))))), [(Id(NUDa), For(Id(S1), BooleanLit(True), Id(NgAh), Continue)), (BooleanLit(False), If(BooleanLit(False), CallStmt(Id(usAY), [Id(XH), BooleanLit(True)])), [(Id(Df), Break), (Id(vi), For(Id(ph), Id(Fmy5), StringLit(vBG), Block([Block([For(Id(WH8_), BooleanLit(False), Id(pG), AssignStmt(ArrayCell(Id(lDv), [BooleanLit(False), BooleanLit(True)]), NumLit(40.62))), AssignStmt(ArrayCell(Id(qI), [StringLit(lSOd), BooleanLit(False), StringLit(CZOEk)]), Id(ynyr)), Return(Id(eRLu))]), Block([Continue, Break, Break])]))), (BooleanLit(False), AssignStmt(Id(TnoS), NumLit(18.75))), (NumLit(98.11), If(Id(SP), Break), [(StringLit(D), Continue), (NumLit(70.17), Block([If(BooleanLit(True), Return()), [], VarDecl(Id(K0), NumberType, None, None)])), (Id(C4RA), VarDecl(Id(Aw), ArrayType([32.64, 73.31], StringType), None, Id(gqpi))), (Id(NC), AssignStmt(ArrayCell(Id(ETqH), [NumLit(0.01), BooleanLit(False)]), Id(GSe)))], Break), (Id(Dk7), Block([]))], For(Id(OkF7), BooleanLit(True), BooleanLit(True), If(NumLit(13.76), CallStmt(Id(T1x), [])), [(StringLit(ZXoJJ), Break), (Id(wSB), CallStmt(Id(pIO), [Id(vYXB), Id(AV), NumLit(89.75)])), (NumLit(96.16), For(Id(ya), BooleanLit(False), BooleanLit(True), VarDecl(Id(RETH), NumberType, None, None))), (StringLit(IV), CallStmt(Id(QHm), [])), (Id(Gb), CallStmt(Id(WMb_), []))], AssignStmt(ArrayCell(Id(ePI), [StringLit(nZ), StringLit(THD)]), StringLit(tzJ)))), (BooleanLit(True), Break), (BooleanLit(True), Return()), (NumLit(80.67), VarDecl(Id(Qm), NumberType, None, Id(GZQ)))], Block([Return(), For(Id(Mz), BooleanLit(False), BooleanLit(False), Continue), AssignStmt(ArrayCell(Id(rBTw), [StringLit(l)]), Id(S6Q0))])), [], None, Return()])), [(BooleanLit(False), Block([Block([])])), (StringLit(KvmYm), Return()), (BooleanLit(True), Block([AssignStmt(ArrayCell(Id(Xah), [StringLit(cBNwh)]), BooleanLit(True)), Return(NumLit(89.61))])), (Id(EZ), Continue)], Continue), (StringLit(NANbj), VarDecl(Id(i_Ju), StringType, None, NumLit(30.25))), (NumLit(88.65), Break), (BooleanLit(True), Break), (Id(V8), AssignStmt(Id(ERaP), StringLit(Hs))), (StringLit(KKZpW), CallStmt(Id(vRO), [BooleanLit(True), NumLit(8.21), NumLit(38.63)])), (StringLit(zEKg), Block([If(StringLit(t), If(NumLit(52.96), Return(BooleanLit(True))), [(NumLit(26.81), CallStmt(Id(fpO), [Id(zGU), StringLit(chBD), Id(GU)])), (BooleanLit(False), For(Id(mrIy), NumLit(60.93), BooleanLit(True), If(StringLit(juw), CallStmt(Id(FhZ), [StringLit(tbQbw)])), [(StringLit(Fk), CallStmt(Id(CXR), [Id(BX), Id(sxn), StringLit(ouvN)])), (BooleanLit(False), For(Id(cFL), NumLit(12.9), NumLit(22.56), Continue)), (Id(vVE6), CallStmt(Id(av), [StringLit(Dl), NumLit(86.22), StringLit(Kbq)])), (BooleanLit(False), VarDecl(Id(IWN9), ArrayType([85.22], BoolType), None, Id(At))), (Id(xN), If(Id(u9), VarDecl(Id(sL), StringType, None, None)), [(StringLit(b), Block([VarDecl(Id(cQ), ArrayType([51.82], StringType), None, StringLit(png)), VarDecl(Id(uZi), None, var, BooleanLit(False))])), (Id(kF), Continue), (StringLit(cl), Break), (BooleanLit(False), Break), (BooleanLit(True), Block([Return(), For(Id(cdDP), BooleanLit(False), Id(TVD), Block([VarDecl(Id(Qd5), None, dynamic, NumLit(6.09))])), VarDecl(Id(yT), ArrayType([85.85, 45.84, 84.51], BoolType), None, None)]))], If(BooleanLit(True), For(Id(Fu), BooleanLit(False), StringLit(JN), Continue)), [], Continue), (BooleanLit(True), VarDecl(Id(G37), ArrayType([81.28, 65.8, 31.15], BoolType), None, None)), (Id(Uc_Y), If(BooleanLit(True), Break), [(StringLit(JbUI), AssignStmt(Id(Tyi), NumLit(20.66))), (BooleanLit(True), Continue)], None)], None))], None), [], None])), (BooleanLit(False), CallStmt(Id(h0), [])), (NumLit(19.46), If(NumLit(95.24), AssignStmt(ArrayCell(Id(Wa), [NumLit(34.64), BooleanLit(True)]), NumLit(89.7))), [(Id(jd1), For(Id(Rz5), StringLit(Edr), NumLit(22.6), Return(Id(oh)))), (BooleanLit(False), Block([Continue, Block([CallStmt(Id(v7), [])]), Continue]))], Continue)], Return())], None)], None)], None, Break])), FuncDecl(Id(Rik), [VarDecl(Id(kt), ArrayType([45.62], BoolType), None, None)], Block([For(Id(e02u), NumLit(52.59), NumLit(34.85), Break)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115859))

	def test_21530115860(self):
		input = '''
bool X2B[2.45]
func ApHz ()
	begin
		break
		Qg2 <- LG
		for MGDS until false by "h"
			continue
	end
func V5O (number GbB[86.28,39.89], string pJ7p[78.41], number dbT)
	begin
	end
func ZV2 (string lhO, bool ngp, string u4fQ)
	return
func XZx (number oN[2.13,77.21], bool biI, bool Bun[82.87])
	begin
	end

'''
		expect = '''Program([VarDecl(Id(X2B), ArrayType([2.45], BoolType), None, None), FuncDecl(Id(ApHz), [], Block([Break, AssignStmt(Id(Qg2), Id(LG)), For(Id(MGDS), BooleanLit(False), StringLit(h), Continue)])), FuncDecl(Id(V5O), [VarDecl(Id(GbB), ArrayType([86.28, 39.89], NumberType), None, None), VarDecl(Id(pJ7p), ArrayType([78.41], StringType), None, None), VarDecl(Id(dbT), NumberType, None, None)], Block([])), FuncDecl(Id(ZV2), [VarDecl(Id(lhO), StringType, None, None), VarDecl(Id(ngp), BoolType, None, None), VarDecl(Id(u4fQ), StringType, None, None)], Return()), FuncDecl(Id(XZx), [VarDecl(Id(oN), ArrayType([2.13, 77.21], NumberType), None, None), VarDecl(Id(biI), BoolType, None, None), VarDecl(Id(Bun), ArrayType([82.87], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115860))

	def test_21530115861(self):
		input = '''
bool IyhM[0.23,24.06,24.99]
func xjo (number SYc[8.15,75.14,22.04], string Ybc)	begin
		continue
		for S1dX until true by "VM"
			Gl[false, M9dC, 83.49] <- ousJ
		break
	end

'''
		expect = '''Program([VarDecl(Id(IyhM), ArrayType([0.23, 24.06, 24.99], BoolType), None, None), FuncDecl(Id(xjo), [VarDecl(Id(SYc), ArrayType([8.15, 75.14, 22.04], NumberType), None, None), VarDecl(Id(Ybc), StringType, None, None)], Block([Continue, For(Id(S1dX), BooleanLit(True), StringLit(VM), AssignStmt(ArrayCell(Id(Gl), [BooleanLit(False), Id(M9dC), NumLit(83.49)]), Id(ousJ))), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115861))

	def test_21530115862(self):
		input = '''
number NyA[30.64,28.91] <- r4
func aam (bool hq[7.21,70.77,88.71], number y0, bool ae)
	return IpRC
string rJ[52.35,93.36] <- "A"
func Uq (bool TZ7)	begin
		begin
			if (19.67)
			continue
			elif (mKq) for qGy until 13.17 by vd
				return
		end
	end

'''
		expect = '''Program([VarDecl(Id(NyA), ArrayType([30.64, 28.91], NumberType), None, Id(r4)), FuncDecl(Id(aam), [VarDecl(Id(hq), ArrayType([7.21, 70.77, 88.71], BoolType), None, None), VarDecl(Id(y0), NumberType, None, None), VarDecl(Id(ae), BoolType, None, None)], Return(Id(IpRC))), VarDecl(Id(rJ), ArrayType([52.35, 93.36], StringType), None, StringLit(A)), FuncDecl(Id(Uq), [VarDecl(Id(TZ7), BoolType, None, None)], Block([Block([If(NumLit(19.67), Continue), [(Id(mKq), For(Id(qGy), NumLit(13.17), Id(vd), Return()))], None])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115862))

	def test_21530115863(self):
		input = '''
dynamic RtJY <- 80.33
'''
		expect = '''Program([VarDecl(Id(RtJY), None, dynamic, NumLit(80.33))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115863))

	def test_21530115864(self):
		input = '''
string QP[82.94,52.84,12.94] <- "tua"
func w6YD ()	begin
		number v5[51.41,60.05,29.46] <- 1.85
		jc[true, "dhGTf"] <- n0Y
		wxB("Ci", "qbWX")
	end

bool HBXs <- "kaDSI"
number XwS[9.97] <- "fRN"
bool Czi
'''
		expect = '''Program([VarDecl(Id(QP), ArrayType([82.94, 52.84, 12.94], StringType), None, StringLit(tua)), FuncDecl(Id(w6YD), [], Block([VarDecl(Id(v5), ArrayType([51.41, 60.05, 29.46], NumberType), None, NumLit(1.85)), AssignStmt(ArrayCell(Id(jc), [BooleanLit(True), StringLit(dhGTf)]), Id(n0Y)), CallStmt(Id(wxB), [StringLit(Ci), StringLit(qbWX)])])), VarDecl(Id(HBXs), BoolType, None, StringLit(kaDSI)), VarDecl(Id(XwS), ArrayType([9.97], NumberType), None, StringLit(fRN)), VarDecl(Id(Czi), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115864))

	def test_21530115865(self):
		input = '''
string zROV[16.79,63.64,71.8]
func s7 (bool pUQr[66.13,80.32], string tBM[12.21])	return

'''
		expect = '''Program([VarDecl(Id(zROV), ArrayType([16.79, 63.64, 71.8], StringType), None, None), FuncDecl(Id(s7), [VarDecl(Id(pUQr), ArrayType([66.13, 80.32], BoolType), None, None), VarDecl(Id(tBM), ArrayType([12.21], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115865))

	def test_21530115866(self):
		input = '''
dynamic wo1 <- 9.6
number Wi <- ujU
'''
		expect = '''Program([VarDecl(Id(wo1), None, dynamic, NumLit(9.6)), VarDecl(Id(Wi), NumberType, None, Id(ujU))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115866))

	def test_21530115867(self):
		input = '''
dynamic swM <- "AozT"
bool Fjgx <- "hYvHh"
'''
		expect = '''Program([VarDecl(Id(swM), None, dynamic, StringLit(AozT)), VarDecl(Id(Fjgx), BoolType, None, StringLit(hYvHh))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115867))

	def test_21530115868(self):
		input = '''
string FHp
dynamic k1
func Gu ()
	return 11.35

'''
		expect = '''Program([VarDecl(Id(FHp), StringType, None, None), VarDecl(Id(k1), None, dynamic, None), FuncDecl(Id(Gu), [], Return(NumLit(11.35)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115868))

	def test_21530115869(self):
		input = '''
func woR3 (bool Rk)
	begin
		continue
		FGl <- FP
		begin
			begin
				if (19.98) for Oc until 93.18 by 49.84
					begin
						AW <- 11.17
						bool mqqi
						string QbT9[29.64,9.0]
					end
				elif ("MR")
				break
				elif ("HoA")
				return
				elif (XB) h0(false, false)
				else begin
					aK06 <- Pa5c
					du1J <- 81.93
					if (70.84)
					Wcm("DDe", Qm0)
					elif (78.78)
					break
					elif (23.7)
					d0(qdK, "Yxx", true)
					elif (false)
					h0aQ()
					elif (hg)
					break
					elif (96.38) if ("oLIpb")
					NYMJ(xQBY, 59.47, 59.93)
					elif (false) break
					elif (kU)
					continue
					elif (72.52)
					SxDe(5.32)
					elif (Fmy8)
					qYSu[qa3, "K", "kO"] <- Io
				end
			end
		end
	end
bool WGrN
'''
		expect = '''Program([FuncDecl(Id(woR3), [VarDecl(Id(Rk), BoolType, None, None)], Block([Continue, AssignStmt(Id(FGl), Id(FP)), Block([Block([If(NumLit(19.98), For(Id(Oc), NumLit(93.18), NumLit(49.84), Block([AssignStmt(Id(AW), NumLit(11.17)), VarDecl(Id(mqqi), BoolType, None, None), VarDecl(Id(QbT9), ArrayType([29.64, 9.0], StringType), None, None)]))), [(StringLit(MR), Break), (StringLit(HoA), Return()), (Id(XB), CallStmt(Id(h0), [BooleanLit(False), BooleanLit(False)]))], Block([AssignStmt(Id(aK06), Id(Pa5c)), AssignStmt(Id(du1J), NumLit(81.93)), If(NumLit(70.84), CallStmt(Id(Wcm), [StringLit(DDe), Id(Qm0)])), [(NumLit(78.78), Break), (NumLit(23.7), CallStmt(Id(d0), [Id(qdK), StringLit(Yxx), BooleanLit(True)])), (BooleanLit(False), CallStmt(Id(h0aQ), [])), (Id(hg), Break), (NumLit(96.38), If(StringLit(oLIpb), CallStmt(Id(NYMJ), [Id(xQBY), NumLit(59.47), NumLit(59.93)])), [(BooleanLit(False), Break), (Id(kU), Continue), (NumLit(72.52), CallStmt(Id(SxDe), [NumLit(5.32)])), (Id(Fmy8), AssignStmt(ArrayCell(Id(qYSu), [Id(qa3), StringLit(K), StringLit(kO)]), Id(Io)))], None)], None])])])])), VarDecl(Id(WGrN), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115869))

	def test_21530115870(self):
		input = '''
string eWTQ
'''
		expect = '''Program([VarDecl(Id(eWTQ), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115870))

	def test_21530115871(self):
		input = '''
func qfA (string na, number QO[93.3,24.17,4.05])
	return "A"

string dwa
func Qy (bool wBK3, string M_[34.18])
	return true
'''
		expect = '''Program([FuncDecl(Id(qfA), [VarDecl(Id(na), StringType, None, None), VarDecl(Id(QO), ArrayType([93.3, 24.17, 4.05], NumberType), None, None)], Return(StringLit(A))), VarDecl(Id(dwa), StringType, None, None), FuncDecl(Id(Qy), [VarDecl(Id(wBK3), BoolType, None, None), VarDecl(Id(M_), ArrayType([34.18], StringType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115871))

	def test_21530115872(self):
		input = '''
number l4[83.92,29.66]
string H55A[16.28] <- "BHa"
'''
		expect = '''Program([VarDecl(Id(l4), ArrayType([83.92, 29.66], NumberType), None, None), VarDecl(Id(H55A), ArrayType([16.28], StringType), None, StringLit(BHa))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115872))

	def test_21530115873(self):
		input = '''
func i4Z (number QqX, number U12U[46.01,29.48], bool oOMw[99.32,40.72,76.83])	return

bool rCZf <- true
string S1b
'''
		expect = '''Program([FuncDecl(Id(i4Z), [VarDecl(Id(QqX), NumberType, None, None), VarDecl(Id(U12U), ArrayType([46.01, 29.48], NumberType), None, None), VarDecl(Id(oOMw), ArrayType([99.32, 40.72, 76.83], BoolType), None, None)], Return()), VarDecl(Id(rCZf), BoolType, None, BooleanLit(True)), VarDecl(Id(S1b), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115873))

	def test_21530115874(self):
		input = '''
func IEi (number Rb)	return true
bool FDW[4.88,86.66,99.16] <- 67.55
bool PJ[17.67,26.2] <- cuZG
func Cs ()
	return
'''
		expect = '''Program([FuncDecl(Id(IEi), [VarDecl(Id(Rb), NumberType, None, None)], Return(BooleanLit(True))), VarDecl(Id(FDW), ArrayType([4.88, 86.66, 99.16], BoolType), None, NumLit(67.55)), VarDecl(Id(PJ), ArrayType([17.67, 26.2], BoolType), None, Id(cuZG)), FuncDecl(Id(Cs), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115874))

	def test_21530115875(self):
		input = '''
number Msa
'''
		expect = '''Program([VarDecl(Id(Msa), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115875))

	def test_21530115876(self):
		input = '''
string JHE[32.53,47.16,26.91]
string c8j[51.88,19.76,22.51]
'''
		expect = '''Program([VarDecl(Id(JHE), ArrayType([32.53, 47.16, 26.91], StringType), None, None), VarDecl(Id(c8j), ArrayType([51.88, 19.76, 22.51], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115876))

	def test_21530115877(self):
		input = '''
var ngV <- 81.09
bool Q54
dynamic YR <- 1.09
'''
		expect = '''Program([VarDecl(Id(ngV), None, var, NumLit(81.09)), VarDecl(Id(Q54), BoolType, None, None), VarDecl(Id(YR), None, dynamic, NumLit(1.09))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115877))

	def test_21530115878(self):
		input = '''
var id <- true
func mOWW ()
	begin
	end

'''
		expect = '''Program([VarDecl(Id(id), None, var, BooleanLit(True)), FuncDecl(Id(mOWW), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115878))

	def test_21530115879(self):
		input = '''
string Vf[0.09] <- 97.3
number QRZ[15.8,48.77,51.3]
'''
		expect = '''Program([VarDecl(Id(Vf), ArrayType([0.09], StringType), None, NumLit(97.3)), VarDecl(Id(QRZ), ArrayType([15.8, 48.77, 51.3], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115879))

	def test_21530115880(self):
		input = '''
func Dxgm (bool T2[88.24,33.72], bool lmUp)
	begin
		begin
		end
	end

string fiS[93.68,99.38]
bool D6
func L2 ()
	return
'''
		expect = '''Program([FuncDecl(Id(Dxgm), [VarDecl(Id(T2), ArrayType([88.24, 33.72], BoolType), None, None), VarDecl(Id(lmUp), BoolType, None, None)], Block([Block([])])), VarDecl(Id(fiS), ArrayType([93.68, 99.38], StringType), None, None), VarDecl(Id(D6), BoolType, None, None), FuncDecl(Id(L2), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115880))

	def test_21530115881(self):
		input = '''
dynamic gB <- 57.27
bool mk <- true
bool Nh[70.69] <- false
'''
		expect = '''Program([VarDecl(Id(gB), None, dynamic, NumLit(57.27)), VarDecl(Id(mk), BoolType, None, BooleanLit(True)), VarDecl(Id(Nh), ArrayType([70.69], BoolType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115881))

	def test_21530115882(self):
		input = '''
var zPzC <- zdR9
'''
		expect = '''Program([VarDecl(Id(zPzC), None, var, Id(zdR9))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115882))

	def test_21530115883(self):
		input = '''
bool azgv[81.51]
func lOHd (number YvGR[26.73,76.1], number JT[80.58,55.83,86.71], string GGRS)
	begin
	end

string AmNO[48.34,84.48,91.63] <- "AJcuG"
func eqP (number Xp9)
	return 70.35

'''
		expect = '''Program([VarDecl(Id(azgv), ArrayType([81.51], BoolType), None, None), FuncDecl(Id(lOHd), [VarDecl(Id(YvGR), ArrayType([26.73, 76.1], NumberType), None, None), VarDecl(Id(JT), ArrayType([80.58, 55.83, 86.71], NumberType), None, None), VarDecl(Id(GGRS), StringType, None, None)], Block([])), VarDecl(Id(AmNO), ArrayType([48.34, 84.48, 91.63], StringType), None, StringLit(AJcuG)), FuncDecl(Id(eqP), [VarDecl(Id(Xp9), NumberType, None, None)], Return(NumLit(70.35)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115883))

	def test_21530115884(self):
		input = '''
bool Uv
string LP[39.47,20.74]
func Ty (number vzi, bool IZID[4.99,51.62,89.55], number SnxL)
	return false
func lQl (number fUU[0.97,1.76,78.57], number I75[6.43,96.03], string V3[45.51])	begin
		if ("nh")
		break
		elif (32.53)
		continue
	end
func wV (number qvQ[79.97,52.64])	return

'''
		expect = '''Program([VarDecl(Id(Uv), BoolType, None, None), VarDecl(Id(LP), ArrayType([39.47, 20.74], StringType), None, None), FuncDecl(Id(Ty), [VarDecl(Id(vzi), NumberType, None, None), VarDecl(Id(IZID), ArrayType([4.99, 51.62, 89.55], BoolType), None, None), VarDecl(Id(SnxL), NumberType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(lQl), [VarDecl(Id(fUU), ArrayType([0.97, 1.76, 78.57], NumberType), None, None), VarDecl(Id(I75), ArrayType([6.43, 96.03], NumberType), None, None), VarDecl(Id(V3), ArrayType([45.51], StringType), None, None)], Block([If(StringLit(nh), Break), [(NumLit(32.53), Continue)], None])), FuncDecl(Id(wV), [VarDecl(Id(qvQ), ArrayType([79.97, 52.64], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115884))

	def test_21530115885(self):
		input = '''
string JWu
'''
		expect = '''Program([VarDecl(Id(JWu), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115885))

	def test_21530115886(self):
		input = '''
dynamic AfA
bool B4[62.7] <- false
func CzOi (number qgL)
	return "Cm"

string GcK[8.12,95.15] <- 65.71
'''
		expect = '''Program([VarDecl(Id(AfA), None, dynamic, None), VarDecl(Id(B4), ArrayType([62.7], BoolType), None, BooleanLit(False)), FuncDecl(Id(CzOi), [VarDecl(Id(qgL), NumberType, None, None)], Return(StringLit(Cm))), VarDecl(Id(GcK), ArrayType([8.12, 95.15], StringType), None, NumLit(65.71))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115886))

	def test_21530115887(self):
		input = '''
func Qky (number AwKY[63.43,77.53,71.55], number To5u)	begin
	end

var j1 <- 18.82
func qd47 ()
	return
func d6 ()
	begin
		for Cx until Fp7m by 65.28
			begin
			end
		break
		for iTan until "qPKgk" by 88.96
			JP("Rvso", true, 80.66)
	end
func thjR ()	begin
	end

'''
		expect = '''Program([FuncDecl(Id(Qky), [VarDecl(Id(AwKY), ArrayType([63.43, 77.53, 71.55], NumberType), None, None), VarDecl(Id(To5u), NumberType, None, None)], Block([])), VarDecl(Id(j1), None, var, NumLit(18.82)), FuncDecl(Id(qd47), [], Return()), FuncDecl(Id(d6), [], Block([For(Id(Cx), Id(Fp7m), NumLit(65.28), Block([])), Break, For(Id(iTan), StringLit(qPKgk), NumLit(88.96), CallStmt(Id(JP), [StringLit(Rvso), BooleanLit(True), NumLit(80.66)]))])), FuncDecl(Id(thjR), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115887))

	def test_21530115888(self):
		input = '''
func Pq ()
	return
'''
		expect = '''Program([FuncDecl(Id(Pq), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115888))

	def test_21530115889(self):
		input = '''
func AWo (bool u9, bool Dm)
	return

'''
		expect = '''Program([FuncDecl(Id(AWo), [VarDecl(Id(u9), BoolType, None, None), VarDecl(Id(Dm), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115889))

	def test_21530115890(self):
		input = '''
func hN ()	return 4.6

'''
		expect = '''Program([FuncDecl(Id(hN), [], Return(NumLit(4.6)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115890))

	def test_21530115891(self):
		input = '''
string WG[63.78,78.04,43.26]
bool J70[6.92,26.42]
var ad <- IwX
number TEN_
func D2C (string Xm, number Vx0)	begin
		if ("GW") for hOe until true by sn
			break
		elif (i_xj) if ("boM") bool GNgc
		elif (WXm) continue
		elif (76.67)
		return 15.56
		else string Jl[74.7,58.47]
		elif (93.98)
		continue
		elif (Gn6) WM9["Pp"] <- CY
		elif ("hxw") bool ul[48.79,28.41,18.7] <- xqb_
		elif ("sVYR") if ("Qsot") if ("znMs") return
		elif (40.94) break
		elif ("xxl") return
		elif ("xbQc") if (64.58)
		bool EsF
		elif (89.38)
		j98(26.69, true, "nsg")
		elif ("wv") begin
			KiqW <- true
		end
		elif (Wr3) mCz[45.21] <- jSsO
		elif (tKTn) nL6U[59.22] <- "WbDZL"
		elif (spA) for BvfK until 95.82 by false
			begin
			end
		else FbkA(Dx, 66.84)
		elif ("mzEda") continue
		elif (rUp) for rQ_i until 24.55 by false
			ryV["ur", J3] <- 72.07
		else continue
		elif (true) continue
		elif (true) number eAY[44.69,44.16,24.31] <- hG
		elif (67.15) oA(26.74, x7x)
		elif (true)
		wo[Dxl, QX, true] <- EW
		else continue
		if ("BGRzZ")
		bool t5e6[38.73] <- 32.17
		elif ("p")
		break
		elif ("Kj") Sb[64.61, TNN, true] <- gtCJ
		elif (false) break
		else rY[false] <- UHQ
		PRr <- 86.94
	end

'''
		expect = '''Program([VarDecl(Id(WG), ArrayType([63.78, 78.04, 43.26], StringType), None, None), VarDecl(Id(J70), ArrayType([6.92, 26.42], BoolType), None, None), VarDecl(Id(ad), None, var, Id(IwX)), VarDecl(Id(TEN_), NumberType, None, None), FuncDecl(Id(D2C), [VarDecl(Id(Xm), StringType, None, None), VarDecl(Id(Vx0), NumberType, None, None)], Block([If(StringLit(GW), For(Id(hOe), BooleanLit(True), Id(sn), Break)), [(Id(i_xj), If(StringLit(boM), VarDecl(Id(GNgc), BoolType, None, None)), [(Id(WXm), Continue), (NumLit(76.67), Return(NumLit(15.56)))], VarDecl(Id(Jl), ArrayType([74.7, 58.47], StringType), None, None)), (NumLit(93.98), Continue), (Id(Gn6), AssignStmt(ArrayCell(Id(WM9), [StringLit(Pp)]), Id(CY))), (StringLit(hxw), VarDecl(Id(ul), ArrayType([48.79, 28.41, 18.7], BoolType), None, Id(xqb_))), (StringLit(sVYR), If(StringLit(Qsot), If(StringLit(znMs), Return()), [(NumLit(40.94), Break), (StringLit(xxl), Return()), (StringLit(xbQc), If(NumLit(64.58), VarDecl(Id(EsF), BoolType, None, None)), [(NumLit(89.38), CallStmt(Id(j98), [NumLit(26.69), BooleanLit(True), StringLit(nsg)])), (StringLit(wv), Block([AssignStmt(Id(KiqW), BooleanLit(True))])), (Id(Wr3), AssignStmt(ArrayCell(Id(mCz), [NumLit(45.21)]), Id(jSsO))), (Id(tKTn), AssignStmt(ArrayCell(Id(nL6U), [NumLit(59.22)]), StringLit(WbDZL))), (Id(spA), For(Id(BvfK), NumLit(95.82), BooleanLit(False), Block([])))], CallStmt(Id(FbkA), [Id(Dx), NumLit(66.84)])), (StringLit(mzEda), Continue), (Id(rUp), For(Id(rQ_i), NumLit(24.55), BooleanLit(False), AssignStmt(ArrayCell(Id(ryV), [StringLit(ur), Id(J3)]), NumLit(72.07))))], Continue), [(BooleanLit(True), Continue), (BooleanLit(True), VarDecl(Id(eAY), ArrayType([44.69, 44.16, 24.31], NumberType), None, Id(hG))), (NumLit(67.15), CallStmt(Id(oA), [NumLit(26.74), Id(x7x)])), (BooleanLit(True), AssignStmt(ArrayCell(Id(wo), [Id(Dxl), Id(QX), BooleanLit(True)]), Id(EW)))], Continue)], None, If(StringLit(BGRzZ), VarDecl(Id(t5e6), ArrayType([38.73], BoolType), None, NumLit(32.17))), [(StringLit(p), Break), (StringLit(Kj), AssignStmt(ArrayCell(Id(Sb), [NumLit(64.61), Id(TNN), BooleanLit(True)]), Id(gtCJ))), (BooleanLit(False), Break)], AssignStmt(ArrayCell(Id(rY), [BooleanLit(False)]), Id(UHQ)), AssignStmt(Id(PRr), NumLit(86.94))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115891))

	def test_21530115892(self):
		input = '''
func MQpg (bool zf[91.42])
	begin
	end

number RzeQ
bool Qa[58.42,22.25] <- 34.94
func h2 (bool AC)	begin
		break
	end
'''
		expect = '''Program([FuncDecl(Id(MQpg), [VarDecl(Id(zf), ArrayType([91.42], BoolType), None, None)], Block([])), VarDecl(Id(RzeQ), NumberType, None, None), VarDecl(Id(Qa), ArrayType([58.42, 22.25], BoolType), None, NumLit(34.94)), FuncDecl(Id(h2), [VarDecl(Id(AC), BoolType, None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115892))

	def test_21530115893(self):
		input = '''
string uGLz
string fP4z
func oH8 ()
	return
'''
		expect = '''Program([VarDecl(Id(uGLz), StringType, None, None), VarDecl(Id(fP4z), StringType, None, None), FuncDecl(Id(oH8), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115893))

	def test_21530115894(self):
		input = '''
var QP7T <- false
'''
		expect = '''Program([VarDecl(Id(QP7T), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115894))

	def test_21530115895(self):
		input = '''
func Lb (bool Awyq[47.57,37.4], number Ra4G, number WVKk[33.76,65.02,32.74])	begin
	end

var r3 <- "eVtYr"
number i2[49.42,51.19,89.32]
string Ks01[79.18,33.96,99.34]
'''
		expect = '''Program([FuncDecl(Id(Lb), [VarDecl(Id(Awyq), ArrayType([47.57, 37.4], BoolType), None, None), VarDecl(Id(Ra4G), NumberType, None, None), VarDecl(Id(WVKk), ArrayType([33.76, 65.02, 32.74], NumberType), None, None)], Block([])), VarDecl(Id(r3), None, var, StringLit(eVtYr)), VarDecl(Id(i2), ArrayType([49.42, 51.19, 89.32], NumberType), None, None), VarDecl(Id(Ks01), ArrayType([79.18, 33.96, 99.34], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115895))

	def test_21530115896(self):
		input = '''
func GVH (number fp[68.29], bool BS3p[64.07,49.58], string aQ[50.22,76.87])	return Sw
func tQ (number umfp[71.06,41.72,85.83], string eiE)
	return true

bool YZ
number h5[23.84] <- "XGjSC"
'''
		expect = '''Program([FuncDecl(Id(GVH), [VarDecl(Id(fp), ArrayType([68.29], NumberType), None, None), VarDecl(Id(BS3p), ArrayType([64.07, 49.58], BoolType), None, None), VarDecl(Id(aQ), ArrayType([50.22, 76.87], StringType), None, None)], Return(Id(Sw))), FuncDecl(Id(tQ), [VarDecl(Id(umfp), ArrayType([71.06, 41.72, 85.83], NumberType), None, None), VarDecl(Id(eiE), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(YZ), BoolType, None, None), VarDecl(Id(h5), ArrayType([23.84], NumberType), None, StringLit(XGjSC))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115896))

	def test_21530115897(self):
		input = '''
number KMtZ[62.18] <- 74.65
number xf
bool Imnf <- w8sC
'''
		expect = '''Program([VarDecl(Id(KMtZ), ArrayType([62.18], NumberType), None, NumLit(74.65)), VarDecl(Id(xf), NumberType, None, None), VarDecl(Id(Imnf), BoolType, None, Id(w8sC))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115897))

	def test_21530115898(self):
		input = '''
func z7e (bool AxyX[81.11,57.75,61.24], string n5q9[23.27])	begin
		continue
		Efo <- "dJoCP"
	end
func j47 ()
	begin
	end

func aA (number od[49.12,19.42,64.22], number X1e[30.15,44.57], number vg)	return "sM"
string o3
'''
		expect = '''Program([FuncDecl(Id(z7e), [VarDecl(Id(AxyX), ArrayType([81.11, 57.75, 61.24], BoolType), None, None), VarDecl(Id(n5q9), ArrayType([23.27], StringType), None, None)], Block([Continue, AssignStmt(Id(Efo), StringLit(dJoCP))])), FuncDecl(Id(j47), [], Block([])), FuncDecl(Id(aA), [VarDecl(Id(od), ArrayType([49.12, 19.42, 64.22], NumberType), None, None), VarDecl(Id(X1e), ArrayType([30.15, 44.57], NumberType), None, None), VarDecl(Id(vg), NumberType, None, None)], Return(StringLit(sM))), VarDecl(Id(o3), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115898))

	def test_21530115899(self):
		input = '''
func nk (number jXQ, bool ELG)
	return

number BZs[57.25]
func Saas ()
	return false

func aeG (string Os8[29.44,87.04,8.54], string td[95.46], bool z7W8[81.29,34.3,52.23])
	return Vu

var H7p <- "kWOF"
'''
		expect = '''Program([FuncDecl(Id(nk), [VarDecl(Id(jXQ), NumberType, None, None), VarDecl(Id(ELG), BoolType, None, None)], Return()), VarDecl(Id(BZs), ArrayType([57.25], NumberType), None, None), FuncDecl(Id(Saas), [], Return(BooleanLit(False))), FuncDecl(Id(aeG), [VarDecl(Id(Os8), ArrayType([29.44, 87.04, 8.54], StringType), None, None), VarDecl(Id(td), ArrayType([95.46], StringType), None, None), VarDecl(Id(z7W8), ArrayType([81.29, 34.3, 52.23], BoolType), None, None)], Return(Id(Vu))), VarDecl(Id(H7p), None, var, StringLit(kWOF))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115899))

	def test_21530115900(self):
		input = '''
func Uvm (number iRM, string yd[33.19], number DQ)	return

'''
		expect = '''Program([FuncDecl(Id(Uvm), [VarDecl(Id(iRM), NumberType, None, None), VarDecl(Id(yd), ArrayType([33.19], StringType), None, None), VarDecl(Id(DQ), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115900))

	def test_21530115901(self):
		input = '''
string ck[29.57] <- 75.89
string bJ[87.53,60.07,71.23] <- TP
number olJ[79.08,85.42]
func Rs ()
	return "qQi"
'''
		expect = '''Program([VarDecl(Id(ck), ArrayType([29.57], StringType), None, NumLit(75.89)), VarDecl(Id(bJ), ArrayType([87.53, 60.07, 71.23], StringType), None, Id(TP)), VarDecl(Id(olJ), ArrayType([79.08, 85.42], NumberType), None, None), FuncDecl(Id(Rs), [], Return(StringLit(qQi)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115901))

	def test_21530115902(self):
		input = '''
number uY[65.56,52.79] <- false
'''
		expect = '''Program([VarDecl(Id(uY), ArrayType([65.56, 52.79], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115902))

	def test_21530115903(self):
		input = '''
func v4w (bool Wr[98.11,6.37])
	begin
		for ta2 until "FAK" by 17.86
			return
	end

dynamic t_ <- M8sa
func oW1_ (string SA, string wJGj, bool uXh[15.35,67.02])	return 58.15
var IL <- "WYe"
'''
		expect = '''Program([FuncDecl(Id(v4w), [VarDecl(Id(Wr), ArrayType([98.11, 6.37], BoolType), None, None)], Block([For(Id(ta2), StringLit(FAK), NumLit(17.86), Return())])), VarDecl(Id(t_), None, dynamic, Id(M8sa)), FuncDecl(Id(oW1_), [VarDecl(Id(SA), StringType, None, None), VarDecl(Id(wJGj), StringType, None, None), VarDecl(Id(uXh), ArrayType([15.35, 67.02], BoolType), None, None)], Return(NumLit(58.15))), VarDecl(Id(IL), None, var, StringLit(WYe))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115903))

	def test_21530115904(self):
		input = '''
func Iu (bool Pcx, bool vrIR[22.69])	return
func SVU (number sJqa, number TwE[22.91,78.41,10.22], string sM8)
	return false
'''
		expect = '''Program([FuncDecl(Id(Iu), [VarDecl(Id(Pcx), BoolType, None, None), VarDecl(Id(vrIR), ArrayType([22.69], BoolType), None, None)], Return()), FuncDecl(Id(SVU), [VarDecl(Id(sJqa), NumberType, None, None), VarDecl(Id(TwE), ArrayType([22.91, 78.41, 10.22], NumberType), None, None), VarDecl(Id(sM8), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115904))

	def test_21530115905(self):
		input = '''
bool irPA[89.36,56.69,49.99]
'''
		expect = '''Program([VarDecl(Id(irPA), ArrayType([89.36, 56.69, 49.99], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115905))

	def test_21530115906(self):
		input = '''
string h8vs <- "GnHj"
'''
		expect = '''Program([VarDecl(Id(h8vs), StringType, None, StringLit(GnHj))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115906))

	def test_21530115907(self):
		input = '''
bool BgEz
'''
		expect = '''Program([VarDecl(Id(BgEz), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115907))

	def test_21530115908(self):
		input = '''
func PvD (string WAt)
	return

func Dm1 (string gg[48.07,26.88], string z1[81.86], number MTT[43.33,15.09])	return

func Dg (string Wk)	return 57.28

func cETb (bool Y2O)	return

func v72Y (number zM9E[13.49,5.02,75.65], string jKF, number ue)	begin
		string i3 <- 91.33
		if (dL)
		bool Pin[61.29,42.47]
		elif (zLoo) zMfP(h0gA)
	end
'''
		expect = '''Program([FuncDecl(Id(PvD), [VarDecl(Id(WAt), StringType, None, None)], Return()), FuncDecl(Id(Dm1), [VarDecl(Id(gg), ArrayType([48.07, 26.88], StringType), None, None), VarDecl(Id(z1), ArrayType([81.86], StringType), None, None), VarDecl(Id(MTT), ArrayType([43.33, 15.09], NumberType), None, None)], Return()), FuncDecl(Id(Dg), [VarDecl(Id(Wk), StringType, None, None)], Return(NumLit(57.28))), FuncDecl(Id(cETb), [VarDecl(Id(Y2O), BoolType, None, None)], Return()), FuncDecl(Id(v72Y), [VarDecl(Id(zM9E), ArrayType([13.49, 5.02, 75.65], NumberType), None, None), VarDecl(Id(jKF), StringType, None, None), VarDecl(Id(ue), NumberType, None, None)], Block([VarDecl(Id(i3), StringType, None, NumLit(91.33)), If(Id(dL), VarDecl(Id(Pin), ArrayType([61.29, 42.47], BoolType), None, None)), [(Id(zLoo), CallStmt(Id(zMfP), [Id(h0gA)]))], None]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115908))

	def test_21530115909(self):
		input = '''
func Cd7 (bool b_[70.0,89.01,51.53], bool n3kz, number DFv)	return 44.81

func aHST (bool JURj, number RB)
	return
func oN5N (number Iw, string ENH[90.9], string G7C)	return true
'''
		expect = '''Program([FuncDecl(Id(Cd7), [VarDecl(Id(b_), ArrayType([70.0, 89.01, 51.53], BoolType), None, None), VarDecl(Id(n3kz), BoolType, None, None), VarDecl(Id(DFv), NumberType, None, None)], Return(NumLit(44.81))), FuncDecl(Id(aHST), [VarDecl(Id(JURj), BoolType, None, None), VarDecl(Id(RB), NumberType, None, None)], Return()), FuncDecl(Id(oN5N), [VarDecl(Id(Iw), NumberType, None, None), VarDecl(Id(ENH), ArrayType([90.9], StringType), None, None), VarDecl(Id(G7C), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115909))

	def test_21530115910(self):
		input = '''
number lT5
number CZml <- "qck"
string LHuo[8.33,98.95,46.81] <- "TVg"
var koj <- 82.03
'''
		expect = '''Program([VarDecl(Id(lT5), NumberType, None, None), VarDecl(Id(CZml), NumberType, None, StringLit(qck)), VarDecl(Id(LHuo), ArrayType([8.33, 98.95, 46.81], StringType), None, StringLit(TVg)), VarDecl(Id(koj), None, var, NumLit(82.03))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115910))

	def test_21530115911(self):
		input = '''
func XO (string EiDa, bool Mh4V, number ym)
	return fg_

func dQDX (number Y6K)	return false

func YKAd (number Wb[5.12,53.39])	return 53.99

func zw (bool x7FN)	return HIFS

'''
		expect = '''Program([FuncDecl(Id(XO), [VarDecl(Id(EiDa), StringType, None, None), VarDecl(Id(Mh4V), BoolType, None, None), VarDecl(Id(ym), NumberType, None, None)], Return(Id(fg_))), FuncDecl(Id(dQDX), [VarDecl(Id(Y6K), NumberType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(YKAd), [VarDecl(Id(Wb), ArrayType([5.12, 53.39], NumberType), None, None)], Return(NumLit(53.99))), FuncDecl(Id(zw), [VarDecl(Id(x7FN), BoolType, None, None)], Return(Id(HIFS)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115911))

	def test_21530115912(self):
		input = '''
var ND6k <- "ZR"
func IfR ()
	begin
	end

func bE (number jHF[75.94], number CJfM[82.39,62.14,71.24], bool dpN[3.5,14.27,44.52])
	return
func t4 ()
	return G7m

'''
		expect = '''Program([VarDecl(Id(ND6k), None, var, StringLit(ZR)), FuncDecl(Id(IfR), [], Block([])), FuncDecl(Id(bE), [VarDecl(Id(jHF), ArrayType([75.94], NumberType), None, None), VarDecl(Id(CJfM), ArrayType([82.39, 62.14, 71.24], NumberType), None, None), VarDecl(Id(dpN), ArrayType([3.5, 14.27, 44.52], BoolType), None, None)], Return()), FuncDecl(Id(t4), [], Return(Id(G7m)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115912))

	def test_21530115913(self):
		input = '''
func ZKy ()	return "wVw"
func j0 (number mAx[88.14,95.95,78.5], number iFPy)
	return Fj2

'''
		expect = '''Program([FuncDecl(Id(ZKy), [], Return(StringLit(wVw))), FuncDecl(Id(j0), [VarDecl(Id(mAx), ArrayType([88.14, 95.95, 78.5], NumberType), None, None), VarDecl(Id(iFPy), NumberType, None, None)], Return(Id(Fj2)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115913))

	def test_21530115914(self):
		input = '''
dynamic GL
number gLb[0.18]
number UDe <- "oo"
'''
		expect = '''Program([VarDecl(Id(GL), None, dynamic, None), VarDecl(Id(gLb), ArrayType([0.18], NumberType), None, None), VarDecl(Id(UDe), NumberType, None, StringLit(oo))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115914))

	def test_21530115915(self):
		input = '''
number dmd[38.48,72.05,93.54] <- true
string z9VT[7.09]
func TOA (bool iRDc)
	return

bool gg[24.87,42.79,1.03] <- 44.72
'''
		expect = '''Program([VarDecl(Id(dmd), ArrayType([38.48, 72.05, 93.54], NumberType), None, BooleanLit(True)), VarDecl(Id(z9VT), ArrayType([7.09], StringType), None, None), FuncDecl(Id(TOA), [VarDecl(Id(iRDc), BoolType, None, None)], Return()), VarDecl(Id(gg), ArrayType([24.87, 42.79, 1.03], BoolType), None, NumLit(44.72))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115915))

	def test_21530115916(self):
		input = '''
func wcyZ (bool tH)
	return "Vcia"
'''
		expect = '''Program([FuncDecl(Id(wcyZ), [VarDecl(Id(tH), BoolType, None, None)], Return(StringLit(Vcia)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115916))

	def test_21530115917(self):
		input = '''
func uS ()	return "Znd"

number M7 <- true
func fj ()	begin
		return 88.3
	end
bool Kcv[1.76,14.19]
'''
		expect = '''Program([FuncDecl(Id(uS), [], Return(StringLit(Znd))), VarDecl(Id(M7), NumberType, None, BooleanLit(True)), FuncDecl(Id(fj), [], Block([Return(NumLit(88.3))])), VarDecl(Id(Kcv), ArrayType([1.76, 14.19], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115917))

	def test_21530115918(self):
		input = '''
func LZX ()
	return
func gbh (number ejH)
	begin
		if ("eo") if (C59_) if ("WXzEb") if (izi)
		break
		elif (23.62) if (true) if (79.98) string KOtF[25.99,28.32] <- true
		elif (l4R) for NZ until "af" by "QpEa"
			break
		else continue
		elif ("kmSGW") break
		elif (61.41) break
		elif (false)
		continue
		elif (51.63)
		return 16.12
		elif (24.1)
		break
		elif (pYMt)
		for Qdo until false by "b"
			bool n_[87.07,14.2,3.35]
		elif ("F") break
		elif (fl)
		continue
	end

func fbf (bool naC[0.89], string nM[0.7,85.82,36.25])
	return Ao

func ZpB (number orvd[43.03], number ltu, bool qjJJ[59.16,42.9,59.75])
	return

'''
		expect = '''Program([FuncDecl(Id(LZX), [], Return()), FuncDecl(Id(gbh), [VarDecl(Id(ejH), NumberType, None, None)], Block([If(StringLit(eo), If(Id(C59_), If(StringLit(WXzEb), If(Id(izi), Break), [(NumLit(23.62), If(BooleanLit(True), If(NumLit(79.98), VarDecl(Id(KOtF), ArrayType([25.99, 28.32], StringType), None, BooleanLit(True))), [(Id(l4R), For(Id(NZ), StringLit(af), StringLit(QpEa), Break))], Continue), [(StringLit(kmSGW), Break), (NumLit(61.41), Break), (BooleanLit(False), Continue), (NumLit(51.63), Return(NumLit(16.12))), (NumLit(24.1), Break), (Id(pYMt), For(Id(Qdo), BooleanLit(False), StringLit(b), VarDecl(Id(n_), ArrayType([87.07, 14.2, 3.35], BoolType), None, None))), (StringLit(F), Break), (Id(fl), Continue)], None)], None), [], None), [], None), [], None])), FuncDecl(Id(fbf), [VarDecl(Id(naC), ArrayType([0.89], BoolType), None, None), VarDecl(Id(nM), ArrayType([0.7, 85.82, 36.25], StringType), None, None)], Return(Id(Ao))), FuncDecl(Id(ZpB), [VarDecl(Id(orvd), ArrayType([43.03], NumberType), None, None), VarDecl(Id(ltu), NumberType, None, None), VarDecl(Id(qjJJ), ArrayType([59.16, 42.9, 59.75], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115918))

	def test_21530115919(self):
		input = '''
func uO ()
	begin
	end

string YX[62.68] <- 30.88
bool Zh[65.13,40.9]
'''
		expect = '''Program([FuncDecl(Id(uO), [], Block([])), VarDecl(Id(YX), ArrayType([62.68], StringType), None, NumLit(30.88)), VarDecl(Id(Zh), ArrayType([65.13, 40.9], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115919))

	def test_21530115920(self):
		input = '''
func VDT ()	return
'''
		expect = '''Program([FuncDecl(Id(VDT), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115920))

	def test_21530115921(self):
		input = '''
var tssT <- "WBa"
number c19G[94.07,61.16]
'''
		expect = '''Program([VarDecl(Id(tssT), None, var, StringLit(WBa)), VarDecl(Id(c19G), ArrayType([94.07, 61.16], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115921))

	def test_21530115922(self):
		input = '''
dynamic oiJ
'''
		expect = '''Program([VarDecl(Id(oiJ), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115922))

	def test_21530115923(self):
		input = '''
func CXg (number aUv4[97.21])	begin
		qD(nMH)
	end

dynamic Ed <- "EJL"
'''
		expect = '''Program([FuncDecl(Id(CXg), [VarDecl(Id(aUv4), ArrayType([97.21], NumberType), None, None)], Block([CallStmt(Id(qD), [Id(nMH)])])), VarDecl(Id(Ed), None, dynamic, StringLit(EJL))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115923))

	def test_21530115924(self):
		input = '''
number l2uu <- true
bool WG3p[59.27,95.03] <- RJ
func Tsl8 (string hH38)	begin
	end

var ZU <- "WPJ"
'''
		expect = '''Program([VarDecl(Id(l2uu), NumberType, None, BooleanLit(True)), VarDecl(Id(WG3p), ArrayType([59.27, 95.03], BoolType), None, Id(RJ)), FuncDecl(Id(Tsl8), [VarDecl(Id(hH38), StringType, None, None)], Block([])), VarDecl(Id(ZU), None, var, StringLit(WPJ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115924))

	def test_21530115925(self):
		input = '''
dynamic irp
func It ()
	return

'''
		expect = '''Program([VarDecl(Id(irp), None, dynamic, None), FuncDecl(Id(It), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115925))

	def test_21530115926(self):
		input = '''
func Md1m ()	return

'''
		expect = '''Program([FuncDecl(Id(Md1m), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115926))

	def test_21530115927(self):
		input = '''
dynamic t4 <- yw
func T1Y (string BbGd[41.57])	return "i"
'''
		expect = '''Program([VarDecl(Id(t4), None, dynamic, Id(yw)), FuncDecl(Id(T1Y), [VarDecl(Id(BbGd), ArrayType([41.57], StringType), None, None)], Return(StringLit(i)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115927))

	def test_21530115928(self):
		input = '''
string mJhj[89.2,15.25]
func Dsa ()	return
bool pLZ[47.24,58.18,0.04] <- false
func WBM (string xK)	return lW
func NS (string V2Fd[38.1,69.3])
	return "nxN"
'''
		expect = '''Program([VarDecl(Id(mJhj), ArrayType([89.2, 15.25], StringType), None, None), FuncDecl(Id(Dsa), [], Return()), VarDecl(Id(pLZ), ArrayType([47.24, 58.18, 0.04], BoolType), None, BooleanLit(False)), FuncDecl(Id(WBM), [VarDecl(Id(xK), StringType, None, None)], Return(Id(lW))), FuncDecl(Id(NS), [VarDecl(Id(V2Fd), ArrayType([38.1, 69.3], StringType), None, None)], Return(StringLit(nxN)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115928))

	def test_21530115929(self):
		input = '''
func WB (string Lr[47.59])	begin
		Szq <- "TpI"
		for UKI until "YBC" by false
			continue
		begin
			if (8.44)
			for hA until RBba by 44.39
				continue
			elif (true)
			gY[true, true] <- "M"
			elif (true) Fhc[OPHP] <- kFii
		end
	end

func C5R (string w2, bool QV[45.05,85.23], string rX[34.41,84.21,63.9])
	begin
		L7I(true, "zg")
	end

func Z4 ()	return
func rYs (string De[13.27])	return

func Hc (number bo[62.52,61.55])
	return

'''
		expect = '''Program([FuncDecl(Id(WB), [VarDecl(Id(Lr), ArrayType([47.59], StringType), None, None)], Block([AssignStmt(Id(Szq), StringLit(TpI)), For(Id(UKI), StringLit(YBC), BooleanLit(False), Continue), Block([If(NumLit(8.44), For(Id(hA), Id(RBba), NumLit(44.39), Continue)), [(BooleanLit(True), AssignStmt(ArrayCell(Id(gY), [BooleanLit(True), BooleanLit(True)]), StringLit(M))), (BooleanLit(True), AssignStmt(ArrayCell(Id(Fhc), [Id(OPHP)]), Id(kFii)))], None])])), FuncDecl(Id(C5R), [VarDecl(Id(w2), StringType, None, None), VarDecl(Id(QV), ArrayType([45.05, 85.23], BoolType), None, None), VarDecl(Id(rX), ArrayType([34.41, 84.21, 63.9], StringType), None, None)], Block([CallStmt(Id(L7I), [BooleanLit(True), StringLit(zg)])])), FuncDecl(Id(Z4), [], Return()), FuncDecl(Id(rYs), [VarDecl(Id(De), ArrayType([13.27], StringType), None, None)], Return()), FuncDecl(Id(Hc), [VarDecl(Id(bo), ArrayType([62.52, 61.55], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115929))

	def test_21530115930(self):
		input = '''
string Yz3G[21.8]
string fPO
'''
		expect = '''Program([VarDecl(Id(Yz3G), ArrayType([21.8], StringType), None, None), VarDecl(Id(fPO), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115930))

	def test_21530115931(self):
		input = '''
number HYZR[82.99,34.35,63.79] <- "LSL"
number FN4I
'''
		expect = '''Program([VarDecl(Id(HYZR), ArrayType([82.99, 34.35, 63.79], NumberType), None, StringLit(LSL)), VarDecl(Id(FN4I), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115931))

	def test_21530115932(self):
		input = '''
func tly_ (number BAMc, bool xKK)
	return "lzl"
dynamic wy
'''
		expect = '''Program([FuncDecl(Id(tly_), [VarDecl(Id(BAMc), NumberType, None, None), VarDecl(Id(xKK), BoolType, None, None)], Return(StringLit(lzl))), VarDecl(Id(wy), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115932))

	def test_21530115933(self):
		input = '''
bool DDI[0.24,45.12,97.01]
func cd (bool Fm, string bo8[49.74,45.12,15.74], number SZi[8.91,93.65,17.27])
	return

func EQT (number pyxf)
	return "jtARS"

func yApW (string mHJ)
	return "naJ"

'''
		expect = '''Program([VarDecl(Id(DDI), ArrayType([0.24, 45.12, 97.01], BoolType), None, None), FuncDecl(Id(cd), [VarDecl(Id(Fm), BoolType, None, None), VarDecl(Id(bo8), ArrayType([49.74, 45.12, 15.74], StringType), None, None), VarDecl(Id(SZi), ArrayType([8.91, 93.65, 17.27], NumberType), None, None)], Return()), FuncDecl(Id(EQT), [VarDecl(Id(pyxf), NumberType, None, None)], Return(StringLit(jtARS))), FuncDecl(Id(yApW), [VarDecl(Id(mHJ), StringType, None, None)], Return(StringLit(naJ)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115933))

	def test_21530115934(self):
		input = '''
func pAQ0 ()
	return "RASL"

func XY (number tQk)
	return
func x8 (string cK0t[37.1,8.6])	return "GLxfl"

'''
		expect = '''Program([FuncDecl(Id(pAQ0), [], Return(StringLit(RASL))), FuncDecl(Id(XY), [VarDecl(Id(tQk), NumberType, None, None)], Return()), FuncDecl(Id(x8), [VarDecl(Id(cK0t), ArrayType([37.1, 8.6], StringType), None, None)], Return(StringLit(GLxfl)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115934))

	def test_21530115935(self):
		input = '''
string FPl[24.89,48.23,28.46] <- true
number Ss[70.34,37.54] <- false
'''
		expect = '''Program([VarDecl(Id(FPl), ArrayType([24.89, 48.23, 28.46], StringType), None, BooleanLit(True)), VarDecl(Id(Ss), ArrayType([70.34, 37.54], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115935))

	def test_21530115936(self):
		input = '''
func kAj (string qPD[25.91,94.5], string GT[67.85,50.72,11.61])	return

number iZC
number yB
'''
		expect = '''Program([FuncDecl(Id(kAj), [VarDecl(Id(qPD), ArrayType([25.91, 94.5], StringType), None, None), VarDecl(Id(GT), ArrayType([67.85, 50.72, 11.61], StringType), None, None)], Return()), VarDecl(Id(iZC), NumberType, None, None), VarDecl(Id(yB), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115936))

	def test_21530115937(self):
		input = '''
bool BI3W[90.19,47.19,58.61] <- true
number y2o <- 31.18
'''
		expect = '''Program([VarDecl(Id(BI3W), ArrayType([90.19, 47.19, 58.61], BoolType), None, BooleanLit(True)), VarDecl(Id(y2o), NumberType, None, NumLit(31.18))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115937))

	def test_21530115938(self):
		input = '''
func Yq ()
	return "RZHwk"

number p94[75.95,72.87] <- 91.38
bool GM[46.57,42.23,19.34] <- "PH"
func lTp ()	return

func wr (number KqN[90.68,47.44,16.79], string Ki)	begin
	end

'''
		expect = '''Program([FuncDecl(Id(Yq), [], Return(StringLit(RZHwk))), VarDecl(Id(p94), ArrayType([75.95, 72.87], NumberType), None, NumLit(91.38)), VarDecl(Id(GM), ArrayType([46.57, 42.23, 19.34], BoolType), None, StringLit(PH)), FuncDecl(Id(lTp), [], Return()), FuncDecl(Id(wr), [VarDecl(Id(KqN), ArrayType([90.68, 47.44, 16.79], NumberType), None, None), VarDecl(Id(Ki), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115938))

	def test_21530115939(self):
		input = '''
func DiO7 (string KkP[97.21], number awm)
	begin
		begin
			number yz1Z <- "h"
		end
		string lb[73.72,81.41,62.64]
		for eO until "lMde" by "oyk"
			if (Xi) break
			elif (true) string ZYk[77.77] <- cP
			elif (true)
			for fK until false by mzm
				iSl <- ve
			elif (86.2) break
			else break
	end

func HDY (number gJif)	begin
	end

'''
		expect = '''Program([FuncDecl(Id(DiO7), [VarDecl(Id(KkP), ArrayType([97.21], StringType), None, None), VarDecl(Id(awm), NumberType, None, None)], Block([Block([VarDecl(Id(yz1Z), NumberType, None, StringLit(h))]), VarDecl(Id(lb), ArrayType([73.72, 81.41, 62.64], StringType), None, None), For(Id(eO), StringLit(lMde), StringLit(oyk), If(Id(Xi), Break), [(BooleanLit(True), VarDecl(Id(ZYk), ArrayType([77.77], StringType), None, Id(cP))), (BooleanLit(True), For(Id(fK), BooleanLit(False), Id(mzm), AssignStmt(Id(iSl), Id(ve)))), (NumLit(86.2), Break)], Break)])), FuncDecl(Id(HDY), [VarDecl(Id(gJif), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115939))

	def test_21530115940(self):
		input = '''
func eUI6 (bool TxN, string RnWk)
	return 77.91
func ud (string fG, string VWx[63.84], string vi[89.47])	begin
	end
'''
		expect = '''Program([FuncDecl(Id(eUI6), [VarDecl(Id(TxN), BoolType, None, None), VarDecl(Id(RnWk), StringType, None, None)], Return(NumLit(77.91))), FuncDecl(Id(ud), [VarDecl(Id(fG), StringType, None, None), VarDecl(Id(VWx), ArrayType([63.84], StringType), None, None), VarDecl(Id(vi), ArrayType([89.47], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115940))

	def test_21530115941(self):
		input = '''
func lX (number uH[42.24,4.89,37.52])	return
func nR ()
	return false

func KNV (number npV[67.25], string Ox, number ua)	return 8.13

number DZmU[47.34,94.02] <- false
var PUH <- 6.24
'''
		expect = '''Program([FuncDecl(Id(lX), [VarDecl(Id(uH), ArrayType([42.24, 4.89, 37.52], NumberType), None, None)], Return()), FuncDecl(Id(nR), [], Return(BooleanLit(False))), FuncDecl(Id(KNV), [VarDecl(Id(npV), ArrayType([67.25], NumberType), None, None), VarDecl(Id(Ox), StringType, None, None), VarDecl(Id(ua), NumberType, None, None)], Return(NumLit(8.13))), VarDecl(Id(DZmU), ArrayType([47.34, 94.02], NumberType), None, BooleanLit(False)), VarDecl(Id(PUH), None, var, NumLit(6.24))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115941))

	def test_21530115942(self):
		input = '''
func WY ()
	return
var los <- 50.76
var ajhq <- 44.41
bool Rg <- 14.15
'''
		expect = '''Program([FuncDecl(Id(WY), [], Return()), VarDecl(Id(los), None, var, NumLit(50.76)), VarDecl(Id(ajhq), None, var, NumLit(44.41)), VarDecl(Id(Rg), BoolType, None, NumLit(14.15))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115942))

	def test_21530115943(self):
		input = '''
bool cIDC[62.97,86.55]
'''
		expect = '''Program([VarDecl(Id(cIDC), ArrayType([62.97, 86.55], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115943))

	def test_21530115944(self):
		input = '''
func iA (number Mz4J[77.52], string qDn, bool Lx8C)	return true
dynamic svM <- BS
'''
		expect = '''Program([FuncDecl(Id(iA), [VarDecl(Id(Mz4J), ArrayType([77.52], NumberType), None, None), VarDecl(Id(qDn), StringType, None, None), VarDecl(Id(Lx8C), BoolType, None, None)], Return(BooleanLit(True))), VarDecl(Id(svM), None, dynamic, Id(BS))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115944))

	def test_21530115945(self):
		input = '''
string XFi <- true
var LVWG <- TP_O
func Y7te (number av[45.74,13.86,81.3], string QUP6[98.57], string TH[72.88,28.52])	return UKQ4
'''
		expect = '''Program([VarDecl(Id(XFi), StringType, None, BooleanLit(True)), VarDecl(Id(LVWG), None, var, Id(TP_O)), FuncDecl(Id(Y7te), [VarDecl(Id(av), ArrayType([45.74, 13.86, 81.3], NumberType), None, None), VarDecl(Id(QUP6), ArrayType([98.57], StringType), None, None), VarDecl(Id(TH), ArrayType([72.88, 28.52], StringType), None, None)], Return(Id(UKQ4)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115945))

	def test_21530115946(self):
		input = '''
func H9 (bool ToV, string KTh[10.61,98.03,25.54], number fMn)
	return 42.55
bool corf[25.01]
'''
		expect = '''Program([FuncDecl(Id(H9), [VarDecl(Id(ToV), BoolType, None, None), VarDecl(Id(KTh), ArrayType([10.61, 98.03, 25.54], StringType), None, None), VarDecl(Id(fMn), NumberType, None, None)], Return(NumLit(42.55))), VarDecl(Id(corf), ArrayType([25.01], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115946))

	def test_21530115947(self):
		input = '''
dynamic vNK <- "PHoO"
func EA3R (bool Cnp[75.83], bool OQ)	return zO0O

'''
		expect = '''Program([VarDecl(Id(vNK), None, dynamic, StringLit(PHoO)), FuncDecl(Id(EA3R), [VarDecl(Id(Cnp), ArrayType([75.83], BoolType), None, None), VarDecl(Id(OQ), BoolType, None, None)], Return(Id(zO0O)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115947))

	def test_21530115948(self):
		input = '''
string IN[67.32] <- "W"
func RX ()	return Op11
string rI[90.12,77.99]
string kq
bool fzav
'''
		expect = '''Program([VarDecl(Id(IN), ArrayType([67.32], StringType), None, StringLit(W)), FuncDecl(Id(RX), [], Return(Id(Op11))), VarDecl(Id(rI), ArrayType([90.12, 77.99], StringType), None, None), VarDecl(Id(kq), StringType, None, None), VarDecl(Id(fzav), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115948))

	def test_21530115949(self):
		input = '''
bool oq8P[87.29]
func oYBy (string Krj[94.66])	return

'''
		expect = '''Program([VarDecl(Id(oq8P), ArrayType([87.29], BoolType), None, None), FuncDecl(Id(oYBy), [VarDecl(Id(Krj), ArrayType([94.66], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115949))

	def test_21530115950(self):
		input = '''
func tBl (number aO[86.93,55.77])
	begin
	end
string SFe[8.75,32.47,42.4]
bool jqZJ[86.81,53.61,47.89] <- kCnL
'''
		expect = '''Program([FuncDecl(Id(tBl), [VarDecl(Id(aO), ArrayType([86.93, 55.77], NumberType), None, None)], Block([])), VarDecl(Id(SFe), ArrayType([8.75, 32.47, 42.4], StringType), None, None), VarDecl(Id(jqZJ), ArrayType([86.81, 53.61, 47.89], BoolType), None, Id(kCnL))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115950))

	def test_21530115951(self):
		input = '''
number ZNqd <- Lo
'''
		expect = '''Program([VarDecl(Id(ZNqd), NumberType, None, Id(Lo))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115951))

	def test_21530115952(self):
		input = '''
func aZ3 (bool eE08[31.96,70.52,41.46], bool fgD)
	return
'''
		expect = '''Program([FuncDecl(Id(aZ3), [VarDecl(Id(eE08), ArrayType([31.96, 70.52, 41.46], BoolType), None, None), VarDecl(Id(fgD), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115952))

	def test_21530115953(self):
		input = '''
string W9[98.74,41.24] <- 24.54
string y2Tz[14.82,15.48]
func P7n ()	begin
		break
		if (LFJ4)
		string Ypj <- 85.99
		elif (50.38) for D1hu until mx by jZ
			LU(J3I9, C2)
		elif ("Zebn") begin
		end
		elif (61.45)
		begin
			for Mh2 until true by 47.36
				number Fdbj
		end
		elif (pQmL)
		begin
		end
		for tE until true by true
			for rA until false by true
				number x_ <- "lGvs"
	end

func SjzD (string xs)
	return
func XYq (string fbLW, number B7d)
	return "r"

'''
		expect = '''Program([VarDecl(Id(W9), ArrayType([98.74, 41.24], StringType), None, NumLit(24.54)), VarDecl(Id(y2Tz), ArrayType([14.82, 15.48], StringType), None, None), FuncDecl(Id(P7n), [], Block([Break, If(Id(LFJ4), VarDecl(Id(Ypj), StringType, None, NumLit(85.99))), [(NumLit(50.38), For(Id(D1hu), Id(mx), Id(jZ), CallStmt(Id(LU), [Id(J3I9), Id(C2)]))), (StringLit(Zebn), Block([])), (NumLit(61.45), Block([For(Id(Mh2), BooleanLit(True), NumLit(47.36), VarDecl(Id(Fdbj), NumberType, None, None))])), (Id(pQmL), Block([]))], None, For(Id(tE), BooleanLit(True), BooleanLit(True), For(Id(rA), BooleanLit(False), BooleanLit(True), VarDecl(Id(x_), NumberType, None, StringLit(lGvs))))])), FuncDecl(Id(SjzD), [VarDecl(Id(xs), StringType, None, None)], Return()), FuncDecl(Id(XYq), [VarDecl(Id(fbLW), StringType, None, None), VarDecl(Id(B7d), NumberType, None, None)], Return(StringLit(r)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115953))

	def test_21530115954(self):
		input = '''
bool SxbG[4.28]
var f7w <- TswL
number yD
'''
		expect = '''Program([VarDecl(Id(SxbG), ArrayType([4.28], BoolType), None, None), VarDecl(Id(f7w), None, var, Id(TswL)), VarDecl(Id(yD), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115954))

	def test_21530115955(self):
		input = '''
func pbeC ()	begin
		continue
		for WNOk until 12.71 by "gLHJx"
			begin
			end
		ck[26.6, 84.75] <- "xPV"
	end

string Fce <- KUCq
func cV (bool Hp, number vN)	return

func ek ()
	return true

func JO (bool vu[50.78], string c65[7.26], string xKYW)
	return B_O
'''
		expect = '''Program([FuncDecl(Id(pbeC), [], Block([Continue, For(Id(WNOk), NumLit(12.71), StringLit(gLHJx), Block([])), AssignStmt(ArrayCell(Id(ck), [NumLit(26.6), NumLit(84.75)]), StringLit(xPV))])), VarDecl(Id(Fce), StringType, None, Id(KUCq)), FuncDecl(Id(cV), [VarDecl(Id(Hp), BoolType, None, None), VarDecl(Id(vN), NumberType, None, None)], Return()), FuncDecl(Id(ek), [], Return(BooleanLit(True))), FuncDecl(Id(JO), [VarDecl(Id(vu), ArrayType([50.78], BoolType), None, None), VarDecl(Id(c65), ArrayType([7.26], StringType), None, None), VarDecl(Id(xKYW), StringType, None, None)], Return(Id(B_O)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115955))

	def test_21530115956(self):
		input = '''
number i7V[45.16,63.51]
'''
		expect = '''Program([VarDecl(Id(i7V), ArrayType([45.16, 63.51], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115956))

	def test_21530115957(self):
		input = '''
string Fp1
var zzE <- l2V
string XJg[46.05,71.33,40.54]
func Jo ()	begin
		begin
		end
		break
	end
func tQ1 ()
	return
'''
		expect = '''Program([VarDecl(Id(Fp1), StringType, None, None), VarDecl(Id(zzE), None, var, Id(l2V)), VarDecl(Id(XJg), ArrayType([46.05, 71.33, 40.54], StringType), None, None), FuncDecl(Id(Jo), [], Block([Block([]), Break])), FuncDecl(Id(tQ1), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115957))

	def test_21530115958(self):
		input = '''
number Fs
bool s0F
'''
		expect = '''Program([VarDecl(Id(Fs), NumberType, None, None), VarDecl(Id(s0F), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115958))

	def test_21530115959(self):
		input = '''
var WYMQ <- RC
func fSk (number Pe1D[29.42], bool Tn3[64.66], number nV9M)
	begin
		bool vm[18.07] <- 69.96
	end

func t1af ()
	return 1.2

func KdNB (bool uG)
	return
'''
		expect = '''Program([VarDecl(Id(WYMQ), None, var, Id(RC)), FuncDecl(Id(fSk), [VarDecl(Id(Pe1D), ArrayType([29.42], NumberType), None, None), VarDecl(Id(Tn3), ArrayType([64.66], BoolType), None, None), VarDecl(Id(nV9M), NumberType, None, None)], Block([VarDecl(Id(vm), ArrayType([18.07], BoolType), None, NumLit(69.96))])), FuncDecl(Id(t1af), [], Return(NumLit(1.2))), FuncDecl(Id(KdNB), [VarDecl(Id(uG), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115959))

	def test_21530115960(self):
		input = '''
string oJj[87.08] <- hfLW
string hNz5[92.27,28.89,49.95] <- "Lm"
func jzm ()	begin
		begin
			begin
				break
				if (83.09)
				for sXwd until true by "X"
					string hv[70.78]
				elif (20.01)
				WY(true, fVs)
				elif (10.5) bool Qf9
				elif (true) continue
				elif ("uc") continue
				else for ivg until 52.93 by ZA
					if (27.08) ZX7(false, "TV", kiY)
					elif (YAQ) for bvW until "Stglb" by false
						return
					elif (false) return
					elif (jls) continue
					elif ("htT")
					return
					else YZVw(false, "FIlN")
				continue
			end
		end
	end
number Ns[79.57,78.2]
func XeF ()
	return

'''
		expect = '''Program([VarDecl(Id(oJj), ArrayType([87.08], StringType), None, Id(hfLW)), VarDecl(Id(hNz5), ArrayType([92.27, 28.89, 49.95], StringType), None, StringLit(Lm)), FuncDecl(Id(jzm), [], Block([Block([Block([Break, If(NumLit(83.09), For(Id(sXwd), BooleanLit(True), StringLit(X), VarDecl(Id(hv), ArrayType([70.78], StringType), None, None))), [(NumLit(20.01), CallStmt(Id(WY), [BooleanLit(True), Id(fVs)])), (NumLit(10.5), VarDecl(Id(Qf9), BoolType, None, None)), (BooleanLit(True), Continue), (StringLit(uc), Continue)], For(Id(ivg), NumLit(52.93), Id(ZA), If(NumLit(27.08), CallStmt(Id(ZX7), [BooleanLit(False), StringLit(TV), Id(kiY)])), [(Id(YAQ), For(Id(bvW), StringLit(Stglb), BooleanLit(False), Return())), (BooleanLit(False), Return()), (Id(jls), Continue), (StringLit(htT), Return())], CallStmt(Id(YZVw), [BooleanLit(False), StringLit(FIlN)])), Continue])])])), VarDecl(Id(Ns), ArrayType([79.57, 78.2], NumberType), None, None), FuncDecl(Id(XeF), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115960))

	def test_21530115961(self):
		input = '''
func j9l ()
	return "HoOtp"

number Gu[45.5,71.49]
string Wmr5[10.49]
string izBB <- 72.36
bool dfj[19.22,96.1]
'''
		expect = '''Program([FuncDecl(Id(j9l), [], Return(StringLit(HoOtp))), VarDecl(Id(Gu), ArrayType([45.5, 71.49], NumberType), None, None), VarDecl(Id(Wmr5), ArrayType([10.49], StringType), None, None), VarDecl(Id(izBB), StringType, None, NumLit(72.36)), VarDecl(Id(dfj), ArrayType([19.22, 96.1], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115961))

	def test_21530115962(self):
		input = '''
var KMk <- 86.41
string G2 <- "JQN"
func tsX (number NzO)	return

func v4kf (string d05[16.76,4.53,86.55], number zkx)	begin
		continue
	end
string oLc[68.22,96.61,42.29] <- lrQ
'''
		expect = '''Program([VarDecl(Id(KMk), None, var, NumLit(86.41)), VarDecl(Id(G2), StringType, None, StringLit(JQN)), FuncDecl(Id(tsX), [VarDecl(Id(NzO), NumberType, None, None)], Return()), FuncDecl(Id(v4kf), [VarDecl(Id(d05), ArrayType([16.76, 4.53, 86.55], StringType), None, None), VarDecl(Id(zkx), NumberType, None, None)], Block([Continue])), VarDecl(Id(oLc), ArrayType([68.22, 96.61, 42.29], StringType), None, Id(lrQ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115962))

	def test_21530115963(self):
		input = '''
func ZB4B (string kLi[31.71,82.98], string pWn)	return
'''
		expect = '''Program([FuncDecl(Id(ZB4B), [VarDecl(Id(kLi), ArrayType([31.71, 82.98], StringType), None, None), VarDecl(Id(pWn), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115963))

	def test_21530115964(self):
		input = '''
func NHu (number M4[88.52,31.93], bool YNu[69.35])	begin
		Ovfm[IFU0, "HTe"] <- "d"
		return fJxy
	end
bool Xo
func OBh (string ZS[4.76,73.82], number wISa[55.69,51.58], bool FQ[50.92])
	begin
		if ("wha")
		RCDT(bscP, false)
		elif (true)
		break
		elif (Hkms) return
		elif (70.69)
		begin
		end
		elif (false)
		continue
		else mwv[fOO_] <- 1.05
		return 67.71
		return
	end

func L8 ()
	return

'''
		expect = '''Program([FuncDecl(Id(NHu), [VarDecl(Id(M4), ArrayType([88.52, 31.93], NumberType), None, None), VarDecl(Id(YNu), ArrayType([69.35], BoolType), None, None)], Block([AssignStmt(ArrayCell(Id(Ovfm), [Id(IFU0), StringLit(HTe)]), StringLit(d)), Return(Id(fJxy))])), VarDecl(Id(Xo), BoolType, None, None), FuncDecl(Id(OBh), [VarDecl(Id(ZS), ArrayType([4.76, 73.82], StringType), None, None), VarDecl(Id(wISa), ArrayType([55.69, 51.58], NumberType), None, None), VarDecl(Id(FQ), ArrayType([50.92], BoolType), None, None)], Block([If(StringLit(wha), CallStmt(Id(RCDT), [Id(bscP), BooleanLit(False)])), [(BooleanLit(True), Break), (Id(Hkms), Return()), (NumLit(70.69), Block([])), (BooleanLit(False), Continue)], AssignStmt(ArrayCell(Id(mwv), [Id(fOO_)]), NumLit(1.05)), Return(NumLit(67.71)), Return()])), FuncDecl(Id(L8), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115964))

	def test_21530115965(self):
		input = '''
number xK[18.79,44.64] <- "en"
string GxRc[19.7,45.05]
func H5hI (bool nq1g, bool ZUy, bool VCC5)
	return
func x_2R ()	begin
		if (76.21) begin
		end
		elif (true) break
		else begin
			for HP until CN by "aCNt"
				w1C <- ST
		end
		begin
		end
		dynamic gY
	end

'''
		expect = '''Program([VarDecl(Id(xK), ArrayType([18.79, 44.64], NumberType), None, StringLit(en)), VarDecl(Id(GxRc), ArrayType([19.7, 45.05], StringType), None, None), FuncDecl(Id(H5hI), [VarDecl(Id(nq1g), BoolType, None, None), VarDecl(Id(ZUy), BoolType, None, None), VarDecl(Id(VCC5), BoolType, None, None)], Return()), FuncDecl(Id(x_2R), [], Block([If(NumLit(76.21), Block([])), [(BooleanLit(True), Break)], Block([For(Id(HP), Id(CN), StringLit(aCNt), AssignStmt(Id(w1C), Id(ST)))]), Block([]), VarDecl(Id(gY), None, dynamic, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115965))

	def test_21530115966(self):
		input = '''
dynamic vgn <- "u"
dynamic nM
number woJw[9.07]
var mh <- "MG"
number h_wx
'''
		expect = '''Program([VarDecl(Id(vgn), None, dynamic, StringLit(u)), VarDecl(Id(nM), None, dynamic, None), VarDecl(Id(woJw), ArrayType([9.07], NumberType), None, None), VarDecl(Id(mh), None, var, StringLit(MG)), VarDecl(Id(h_wx), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115966))

	def test_21530115967(self):
		input = '''
func XKb (bool p_8)	return "tcEu"

'''
		expect = '''Program([FuncDecl(Id(XKb), [VarDecl(Id(p_8), BoolType, None, None)], Return(StringLit(tcEu)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115967))

	def test_21530115968(self):
		input = '''
func kKm (string f46[58.9,19.59,47.89], number LNlg)
	return true
bool tV[40.46,55.52,9.14] <- rzB
'''
		expect = '''Program([FuncDecl(Id(kKm), [VarDecl(Id(f46), ArrayType([58.9, 19.59, 47.89], StringType), None, None), VarDecl(Id(LNlg), NumberType, None, None)], Return(BooleanLit(True))), VarDecl(Id(tV), ArrayType([40.46, 55.52, 9.14], BoolType), None, Id(rzB))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115968))

	def test_21530115969(self):
		input = '''
func egL ()	begin
		break
		bool W6f
	end
func XK ()
	begin
		return
		return
	end
func ljs ()	return "bI"
dynamic dr <- 56.22
func r1 (string AJKg[95.13,43.86,0.54])
	return

'''
		expect = '''Program([FuncDecl(Id(egL), [], Block([Break, VarDecl(Id(W6f), BoolType, None, None)])), FuncDecl(Id(XK), [], Block([Return(), Return()])), FuncDecl(Id(ljs), [], Return(StringLit(bI))), VarDecl(Id(dr), None, dynamic, NumLit(56.22)), FuncDecl(Id(r1), [VarDecl(Id(AJKg), ArrayType([95.13, 43.86, 0.54], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115969))

	def test_21530115970(self):
		input = '''
func cHW (string tE7)
	return
func n2ve (string nDTR[12.73], number Afk)
	return 27.12
func W1 (number qU)	return "A"

'''
		expect = '''Program([FuncDecl(Id(cHW), [VarDecl(Id(tE7), StringType, None, None)], Return()), FuncDecl(Id(n2ve), [VarDecl(Id(nDTR), ArrayType([12.73], StringType), None, None), VarDecl(Id(Afk), NumberType, None, None)], Return(NumLit(27.12))), FuncDecl(Id(W1), [VarDecl(Id(qU), NumberType, None, None)], Return(StringLit(A)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115970))

	def test_21530115971(self):
		input = '''
func Xa (string O1)
	return "UdPg"

func NBQ ()	return
func AoRw (string EKxG[45.12,81.38,46.73])	return "L"
'''
		expect = '''Program([FuncDecl(Id(Xa), [VarDecl(Id(O1), StringType, None, None)], Return(StringLit(UdPg))), FuncDecl(Id(NBQ), [], Return()), FuncDecl(Id(AoRw), [VarDecl(Id(EKxG), ArrayType([45.12, 81.38, 46.73], StringType), None, None)], Return(StringLit(L)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115971))

	def test_21530115972(self):
		input = '''
func yQ (number jU, bool o0T[31.51,33.14])
	return
'''
		expect = '''Program([FuncDecl(Id(yQ), [VarDecl(Id(jU), NumberType, None, None), VarDecl(Id(o0T), ArrayType([31.51, 33.14], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115972))

	def test_21530115973(self):
		input = '''
func pn0 (bool bGyi[60.82,14.35,94.33])	begin
	end

func GT (bool Pxm, number d5, bool f6bh)
	return
bool bans
'''
		expect = '''Program([FuncDecl(Id(pn0), [VarDecl(Id(bGyi), ArrayType([60.82, 14.35, 94.33], BoolType), None, None)], Block([])), FuncDecl(Id(GT), [VarDecl(Id(Pxm), BoolType, None, None), VarDecl(Id(d5), NumberType, None, None), VarDecl(Id(f6bh), BoolType, None, None)], Return()), VarDecl(Id(bans), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115973))

	def test_21530115974(self):
		input = '''
bool Ye8[44.69] <- k4U
'''
		expect = '''Program([VarDecl(Id(Ye8), ArrayType([44.69], BoolType), None, Id(k4U))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115974))

	def test_21530115975(self):
		input = '''
func rNS (string Vc2, number B50[64.38,46.33,50.98])	begin
		var P8tE <- "y"
	end

func iG9F (bool IRFI, bool JmET[68.33])
	return

'''
		expect = '''Program([FuncDecl(Id(rNS), [VarDecl(Id(Vc2), StringType, None, None), VarDecl(Id(B50), ArrayType([64.38, 46.33, 50.98], NumberType), None, None)], Block([VarDecl(Id(P8tE), None, var, StringLit(y))])), FuncDecl(Id(iG9F), [VarDecl(Id(IRFI), BoolType, None, None), VarDecl(Id(JmET), ArrayType([68.33], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115975))

	def test_21530115976(self):
		input = '''
bool py[12.58,10.72,61.88] <- "MNkHK"
string lQNU[33.24,65.42,9.31]
'''
		expect = '''Program([VarDecl(Id(py), ArrayType([12.58, 10.72, 61.88], BoolType), None, StringLit(MNkHK)), VarDecl(Id(lQNU), ArrayType([33.24, 65.42, 9.31], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115976))

	def test_21530115977(self):
		input = '''
string hwC <- 83.39
func R0l (bool y0, string Ni, number UU[50.03,41.38,94.83])
	return "i"
func EfS (number aI1Y, string hY0y, string sS8T)
	return "mPKd"

bool XH4
'''
		expect = '''Program([VarDecl(Id(hwC), StringType, None, NumLit(83.39)), FuncDecl(Id(R0l), [VarDecl(Id(y0), BoolType, None, None), VarDecl(Id(Ni), StringType, None, None), VarDecl(Id(UU), ArrayType([50.03, 41.38, 94.83], NumberType), None, None)], Return(StringLit(i))), FuncDecl(Id(EfS), [VarDecl(Id(aI1Y), NumberType, None, None), VarDecl(Id(hY0y), StringType, None, None), VarDecl(Id(sS8T), StringType, None, None)], Return(StringLit(mPKd))), VarDecl(Id(XH4), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115977))

	def test_21530115978(self):
		input = '''
number qqT <- false
func FUx ()
	begin
		continue
	end
var e9 <- "tv"
'''
		expect = '''Program([VarDecl(Id(qqT), NumberType, None, BooleanLit(False)), FuncDecl(Id(FUx), [], Block([Continue])), VarDecl(Id(e9), None, var, StringLit(tv))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115978))

	def test_21530115979(self):
		input = '''
string Nb1[84.96,71.75]
'''
		expect = '''Program([VarDecl(Id(Nb1), ArrayType([84.96, 71.75], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115979))

	def test_21530115980(self):
		input = '''
number H7[69.12,77.22] <- IZc
func Vr (string xKIi[54.11], bool eR)
	return "BomJM"

number No[95.57,53.67]
dynamic Kxu <- 48.93
'''
		expect = '''Program([VarDecl(Id(H7), ArrayType([69.12, 77.22], NumberType), None, Id(IZc)), FuncDecl(Id(Vr), [VarDecl(Id(xKIi), ArrayType([54.11], StringType), None, None), VarDecl(Id(eR), BoolType, None, None)], Return(StringLit(BomJM))), VarDecl(Id(No), ArrayType([95.57, 53.67], NumberType), None, None), VarDecl(Id(Kxu), None, dynamic, NumLit(48.93))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115980))

	def test_21530115981(self):
		input = '''
func CpHI (bool w9xR[11.13,85.63], bool jP_)	return 2.51

bool rqD
string p7d[96.07,31.92,64.48]
number Qv
string eC[29.58]
'''
		expect = '''Program([FuncDecl(Id(CpHI), [VarDecl(Id(w9xR), ArrayType([11.13, 85.63], BoolType), None, None), VarDecl(Id(jP_), BoolType, None, None)], Return(NumLit(2.51))), VarDecl(Id(rqD), BoolType, None, None), VarDecl(Id(p7d), ArrayType([96.07, 31.92, 64.48], StringType), None, None), VarDecl(Id(Qv), NumberType, None, None), VarDecl(Id(eC), ArrayType([29.58], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115981))

	def test_21530115982(self):
		input = '''
number JN[2.69] <- ETn
string Abq
number lc <- 93.38
'''
		expect = '''Program([VarDecl(Id(JN), ArrayType([2.69], NumberType), None, Id(ETn)), VarDecl(Id(Abq), StringType, None, None), VarDecl(Id(lc), NumberType, None, NumLit(93.38))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115982))

	def test_21530115983(self):
		input = '''
func gxjI (number fHJY, number gSy[76.25,0.81], string Iq)	return "XGUc"
func pN ()	return

string spzW[29.23,55.58] <- true
func Hb6 ()	return
func sM (string Iyy)
	return
'''
		expect = '''Program([FuncDecl(Id(gxjI), [VarDecl(Id(fHJY), NumberType, None, None), VarDecl(Id(gSy), ArrayType([76.25, 0.81], NumberType), None, None), VarDecl(Id(Iq), StringType, None, None)], Return(StringLit(XGUc))), FuncDecl(Id(pN), [], Return()), VarDecl(Id(spzW), ArrayType([29.23, 55.58], StringType), None, BooleanLit(True)), FuncDecl(Id(Hb6), [], Return()), FuncDecl(Id(sM), [VarDecl(Id(Iyy), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115983))

	def test_21530115984(self):
		input = '''
bool gCP[63.58,40.02]
'''
		expect = '''Program([VarDecl(Id(gCP), ArrayType([63.58, 40.02], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115984))

	def test_21530115985(self):
		input = '''
func ayg (string niq8)	return
func ovmS ()	begin
		for F0QV until "jeX" by KhLk
			continue
		string WNL[88.68,76.63,22.85]
	end
string Is
'''
		expect = '''Program([FuncDecl(Id(ayg), [VarDecl(Id(niq8), StringType, None, None)], Return()), FuncDecl(Id(ovmS), [], Block([For(Id(F0QV), StringLit(jeX), Id(KhLk), Continue), VarDecl(Id(WNL), ArrayType([88.68, 76.63, 22.85], StringType), None, None)])), VarDecl(Id(Is), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115985))

	def test_21530115986(self):
		input = '''
func WPgc (string SD)
	return

func ySem (string u7Tp[10.71], number uTv, number KL6f)	return QOB
number DR <- 23.6
string X1yt[15.36]
'''
		expect = '''Program([FuncDecl(Id(WPgc), [VarDecl(Id(SD), StringType, None, None)], Return()), FuncDecl(Id(ySem), [VarDecl(Id(u7Tp), ArrayType([10.71], StringType), None, None), VarDecl(Id(uTv), NumberType, None, None), VarDecl(Id(KL6f), NumberType, None, None)], Return(Id(QOB))), VarDecl(Id(DR), NumberType, None, NumLit(23.6)), VarDecl(Id(X1yt), ArrayType([15.36], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115986))

	def test_21530115987(self):
		input = '''
bool Sgg2[64.84,68.86] <- "vLi"
func RsE (number CBwe)
	return true
string yVsW <- "XphMt"
func TW (string aGE[48.1])	return

number fk[55.58,58.6,85.52]
'''
		expect = '''Program([VarDecl(Id(Sgg2), ArrayType([64.84, 68.86], BoolType), None, StringLit(vLi)), FuncDecl(Id(RsE), [VarDecl(Id(CBwe), NumberType, None, None)], Return(BooleanLit(True))), VarDecl(Id(yVsW), StringType, None, StringLit(XphMt)), FuncDecl(Id(TW), [VarDecl(Id(aGE), ArrayType([48.1], StringType), None, None)], Return()), VarDecl(Id(fk), ArrayType([55.58, 58.6, 85.52], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115987))

	def test_21530115988(self):
		input = '''
func xRx7 (string gZvq, string cUZ)
	begin
		begin
		end
		return
		Yl0I <- 22.3
	end

func VeE (number kum, bool nHMZ)
	return
dynamic Oo5 <- 20.93
'''
		expect = '''Program([FuncDecl(Id(xRx7), [VarDecl(Id(gZvq), StringType, None, None), VarDecl(Id(cUZ), StringType, None, None)], Block([Block([]), Return(), AssignStmt(Id(Yl0I), NumLit(22.3))])), FuncDecl(Id(VeE), [VarDecl(Id(kum), NumberType, None, None), VarDecl(Id(nHMZ), BoolType, None, None)], Return()), VarDecl(Id(Oo5), None, dynamic, NumLit(20.93))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115988))

	def test_21530115989(self):
		input = '''
number kpjD <- "Yvq"
number HmwE[23.03] <- tZ
var Ip <- true
func N1KG (number CmaO, bool UH8W, number TaQ)	begin
		for OOL until true by pjVh
			gC(I9O, false)
	end
'''
		expect = '''Program([VarDecl(Id(kpjD), NumberType, None, StringLit(Yvq)), VarDecl(Id(HmwE), ArrayType([23.03], NumberType), None, Id(tZ)), VarDecl(Id(Ip), None, var, BooleanLit(True)), FuncDecl(Id(N1KG), [VarDecl(Id(CmaO), NumberType, None, None), VarDecl(Id(UH8W), BoolType, None, None), VarDecl(Id(TaQ), NumberType, None, None)], Block([For(Id(OOL), BooleanLit(True), Id(pjVh), CallStmt(Id(gC), [Id(I9O), BooleanLit(False)]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115989))

	def test_21530115990(self):
		input = '''
bool QSV <- true
var pZk <- fOv
'''
		expect = '''Program([VarDecl(Id(QSV), BoolType, None, BooleanLit(True)), VarDecl(Id(pZk), None, var, Id(fOv))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115990))

	def test_21530115991(self):
		input = '''
func HP (string vX)
	return "Lsv"
func Dy (bool cDBY[40.62,82.42], number wn[56.92,32.23,91.51], number CDiE[51.24])
	return

func ZcQ (string HIpn[11.98,44.68], string Sx[43.37,67.42,67.18], string F9BN)	return "zj"

'''
		expect = '''Program([FuncDecl(Id(HP), [VarDecl(Id(vX), StringType, None, None)], Return(StringLit(Lsv))), FuncDecl(Id(Dy), [VarDecl(Id(cDBY), ArrayType([40.62, 82.42], BoolType), None, None), VarDecl(Id(wn), ArrayType([56.92, 32.23, 91.51], NumberType), None, None), VarDecl(Id(CDiE), ArrayType([51.24], NumberType), None, None)], Return()), FuncDecl(Id(ZcQ), [VarDecl(Id(HIpn), ArrayType([11.98, 44.68], StringType), None, None), VarDecl(Id(Sx), ArrayType([43.37, 67.42, 67.18], StringType), None, None), VarDecl(Id(F9BN), StringType, None, None)], Return(StringLit(zj)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115991))

	def test_21530115992(self):
		input = '''
bool lCn[24.55,38.88] <- uwR0
number Oa[74.95] <- true
number pHd[90.28]
bool ikv8[21.3,81.33,76.03]
func G0Dd (string FO[43.54], bool RFBI[97.08,33.3], bool iPWV[49.49])
	begin
	end
'''
		expect = '''Program([VarDecl(Id(lCn), ArrayType([24.55, 38.88], BoolType), None, Id(uwR0)), VarDecl(Id(Oa), ArrayType([74.95], NumberType), None, BooleanLit(True)), VarDecl(Id(pHd), ArrayType([90.28], NumberType), None, None), VarDecl(Id(ikv8), ArrayType([21.3, 81.33, 76.03], BoolType), None, None), FuncDecl(Id(G0Dd), [VarDecl(Id(FO), ArrayType([43.54], StringType), None, None), VarDecl(Id(RFBI), ArrayType([97.08, 33.3], BoolType), None, None), VarDecl(Id(iPWV), ArrayType([49.49], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115992))

	def test_21530115993(self):
		input = '''
func GTGz (string i4QR, bool L9f5[7.25,9.16,41.24], number L0Q)
	return oYYq

'''
		expect = '''Program([FuncDecl(Id(GTGz), [VarDecl(Id(i4QR), StringType, None, None), VarDecl(Id(L9f5), ArrayType([7.25, 9.16, 41.24], BoolType), None, None), VarDecl(Id(L0Q), NumberType, None, None)], Return(Id(oYYq)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115993))

	def test_21530115994(self):
		input = '''
func Vr ()
	begin
	end
func v1hu ()	begin
		return false
	end
'''
		expect = '''Program([FuncDecl(Id(Vr), [], Block([])), FuncDecl(Id(v1hu), [], Block([Return(BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115994))

	def test_21530115995(self):
		input = '''
func islE (bool d6[42.07,37.17])
	begin
		ee(zE, 65.92)
		jt()
		string se <- "RpY"
	end
'''
		expect = '''Program([FuncDecl(Id(islE), [VarDecl(Id(d6), ArrayType([42.07, 37.17], BoolType), None, None)], Block([CallStmt(Id(ee), [Id(zE), NumLit(65.92)]), CallStmt(Id(jt), []), VarDecl(Id(se), StringType, None, StringLit(RpY))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115995))

	def test_21530115996(self):
		input = '''
func xv (string vr, string nB, string AP)
	return

func OL ()
	begin
		Ix()
		number dkm <- DRs5
		for gu until true by 83.03
			for WUH until 38.79 by 29.11
				begin
				end
	end

dynamic bZ
bool RzP8[95.78,60.24,28.26] <- "LdI"
'''
		expect = '''Program([FuncDecl(Id(xv), [VarDecl(Id(vr), StringType, None, None), VarDecl(Id(nB), StringType, None, None), VarDecl(Id(AP), StringType, None, None)], Return()), FuncDecl(Id(OL), [], Block([CallStmt(Id(Ix), []), VarDecl(Id(dkm), NumberType, None, Id(DRs5)), For(Id(gu), BooleanLit(True), NumLit(83.03), For(Id(WUH), NumLit(38.79), NumLit(29.11), Block([])))])), VarDecl(Id(bZ), None, dynamic, None), VarDecl(Id(RzP8), ArrayType([95.78, 60.24, 28.26], BoolType), None, StringLit(LdI))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115996))

	def test_21530115997(self):
		input = '''
func NQ7 ()	return
func Ey (bool P0YB, bool XZLg, string SIqp[9.42,78.49,2.6])	return
func yK ()
	begin
	end
func KBn (number Du[36.17,42.67,5.09], number wv[71.75,1.7,15.53])
	return
dynamic QtTf <- Ndwo
'''
		expect = '''Program([FuncDecl(Id(NQ7), [], Return()), FuncDecl(Id(Ey), [VarDecl(Id(P0YB), BoolType, None, None), VarDecl(Id(XZLg), BoolType, None, None), VarDecl(Id(SIqp), ArrayType([9.42, 78.49, 2.6], StringType), None, None)], Return()), FuncDecl(Id(yK), [], Block([])), FuncDecl(Id(KBn), [VarDecl(Id(Du), ArrayType([36.17, 42.67, 5.09], NumberType), None, None), VarDecl(Id(wv), ArrayType([71.75, 1.7, 15.53], NumberType), None, None)], Return()), VarDecl(Id(QtTf), None, dynamic, Id(Ndwo))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115997))

	def test_21530115998(self):
		input = '''
string JYn6 <- false
bool vo6[42.19]
func Igo (string ApV)	return "DPJU"
func K2nO (bool zO0, string EB, bool YCAG)
	return 0.83

func NP16 (bool C3j)
	return "Kzht"
'''
		expect = '''Program([VarDecl(Id(JYn6), StringType, None, BooleanLit(False)), VarDecl(Id(vo6), ArrayType([42.19], BoolType), None, None), FuncDecl(Id(Igo), [VarDecl(Id(ApV), StringType, None, None)], Return(StringLit(DPJU))), FuncDecl(Id(K2nO), [VarDecl(Id(zO0), BoolType, None, None), VarDecl(Id(EB), StringType, None, None), VarDecl(Id(YCAG), BoolType, None, None)], Return(NumLit(0.83))), FuncDecl(Id(NP16), [VarDecl(Id(C3j), BoolType, None, None)], Return(StringLit(Kzht)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115998))

	def test_21530115999(self):
		input = '''
bool c6
'''
		expect = '''Program([VarDecl(Id(c6), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115999))
