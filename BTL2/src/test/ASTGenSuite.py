import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
	def test_2153011500(self):
		input = '''
func huk ()	return
bool Wl <- 90.69
func sGw (number qFYw[79.3], bool Y4y, bool q9)	return ["R", YrKt]
'''
		expect = '''Program([FuncDecl(Id(huk), [], Return()), VarDecl(Id(Wl), BoolType, None, NumLit(90.69)), FuncDecl(Id(sGw), [VarDecl(Id(qFYw), ArrayType([79.3], NumberType), None, None), VarDecl(Id(Y4y), BoolType, None, None), VarDecl(Id(q9), BoolType, None, None)], Return(ArrayLit(StringLit(R), Id(YrKt))))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011500))

	def test_2153011501(self):
		input = '''
number Xx[57.92,21.12,27.68]
string eh
dynamic dmwQ <- false or false
bool Eq[75.22,90.34,59.56] <- VIy
'''
		expect = '''Program([VarDecl(Id(Xx), ArrayType([57.92, 21.12, 27.68], NumberType), None, None), VarDecl(Id(eh), StringType, None, None), VarDecl(Id(dmwQ), None, dynamic, BinaryOp(or, BooleanLit(False), BooleanLit(False))), VarDecl(Id(Eq), ArrayType([75.22, 90.34, 59.56], BoolType), None, Id(VIy))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011501))

	def test_2153011502(self):
		input = '''
func yJC (number ii)	return

var wO <- true
number yYQ[64.38,17.02]
func hIU (number ct5[29.87], bool b0Ne, number R4S)
	return
number QS[41.23,97.06,80.42]
'''
		expect = '''Program([FuncDecl(Id(yJC), [VarDecl(Id(ii), NumberType, None, None)], Return()), VarDecl(Id(wO), None, var, BooleanLit(True)), VarDecl(Id(yYQ), ArrayType([64.38, 17.02], NumberType), None, None), FuncDecl(Id(hIU), [VarDecl(Id(ct5), ArrayType([29.87], NumberType), None, None), VarDecl(Id(b0Ne), BoolType, None, None), VarDecl(Id(R4S), NumberType, None, None)], Return()), VarDecl(Id(QS), ArrayType([41.23, 97.06, 80.42], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011502))

	def test_2153011503(self):
		input = '''
number cQg
func MyP (string BZYm)	return

'''
		expect = '''Program([VarDecl(Id(cQg), NumberType, None, None), FuncDecl(Id(MyP), [VarDecl(Id(BZYm), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011503))

	def test_2153011504(self):
		input = '''
var Zp6 <- sQ
func sW (bool Aa1)	begin
	end

func Wpam (number yZVL[58.18,40.12], string TgAD[62.7])	return false

'''
		expect = '''Program([VarDecl(Id(Zp6), None, var, Id(sQ)), FuncDecl(Id(sW), [VarDecl(Id(Aa1), BoolType, None, None)], Block([])), FuncDecl(Id(Wpam), [VarDecl(Id(yZVL), ArrayType([58.18, 40.12], NumberType), None, None), VarDecl(Id(TgAD), ArrayType([62.7], StringType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011504))

	def test_2153011505(self):
		input = '''
func it4X (number GOi, string aZ[43.53,70.44], bool qvXa[43.3,63.76,68.18])	return true
number UOP[28.83]
bool XCX5 <- RG
func dIv (number bM7N[99.08,12.65,9.35], number EiN)	return 34.81

'''
		expect = '''Program([FuncDecl(Id(it4X), [VarDecl(Id(GOi), NumberType, None, None), VarDecl(Id(aZ), ArrayType([43.53, 70.44], StringType), None, None), VarDecl(Id(qvXa), ArrayType([43.3, 63.76, 68.18], BoolType), None, None)], Return(BooleanLit(True))), VarDecl(Id(UOP), ArrayType([28.83], NumberType), None, None), VarDecl(Id(XCX5), BoolType, None, Id(RG)), FuncDecl(Id(dIv), [VarDecl(Id(bM7N), ArrayType([99.08, 12.65, 9.35], NumberType), None, None), VarDecl(Id(EiN), NumberType, None, None)], Return(NumLit(34.81)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011505))

	def test_2153011506(self):
		input = '''
func CjqZ (number Sd)	begin
	end

var Fj <- "IUdxm"
dynamic xGXm
var vlfo <- "FAg"
'''
		expect = '''Program([FuncDecl(Id(CjqZ), [VarDecl(Id(Sd), NumberType, None, None)], Block([])), VarDecl(Id(Fj), None, var, StringLit(IUdxm)), VarDecl(Id(xGXm), None, dynamic, None), VarDecl(Id(vlfo), None, var, StringLit(FAg))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011506))

	def test_2153011507(self):
		input = '''
func Bpdm ()
	return 24.78
bool PSfK[29.88,14.72,68.17]
'''
		expect = '''Program([FuncDecl(Id(Bpdm), [], Return(NumLit(24.78))), VarDecl(Id(PSfK), ArrayType([29.88, 14.72, 68.17], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011507))

	def test_2153011508(self):
		input = '''
func cs (string BB[12.0,95.15], number qb[58.46], number AlSO)	begin
		VEQv(false, false)
		for WMn until false by 2.77
			begin
				YHL0()
				begin
					begin
						if (21.23) break
						elif ("XbN")
						if (true)
						continue
						elif (wF) MNzH(3.12, 51.84)
						elif (KEZ)
						continue
						elif ("iY") dL6i(plB, "u")
						else continue
						elif ("seW")
						MF <- ZrV
						else string rWK[73.32,13.63,62.01]
					end
					bool CPz
					number eZKf[48.91,58.92,19.77] <- true
				end
				break
			end
		if (63.57)
		if (J0)
		begin
			if (AC) bA("Xxu", ZbU, true)
		end
		elif (28.46) cLby <- false
		elif (true) Pz <- "Zyz"
		else begin
			UkLk <- 52.48
		end
		elif (true)
		WPK("iuTL", "Ey")
		elif (21.59) continue
		elif ("T")
		begin
		end
		elif (50.86)
		number Bobf[93.8] <- "xbw"
		else begin
		end
	end
func nHB (bool g6, string Q7HN, number tySR[82.37,74.03,15.16])
	begin
		for jcdx until J0 by aRVH
			SYuU(AQyz, HQN5)
		return bC0
		break
	end
string inf[89.5,70.71] <- true
string bV1E
func Wk (string eH, bool Dv[58.63,13.7,2.03], bool ZN[89.53,99.73,67.42])	return 55.73

'''
		expect = '''Program([FuncDecl(Id(cs), [VarDecl(Id(BB), ArrayType([12.0, 95.15], StringType), None, None), VarDecl(Id(qb), ArrayType([58.46], NumberType), None, None), VarDecl(Id(AlSO), NumberType, None, None)], Block([CallStmt(Id(VEQv), [BooleanLit(False), BooleanLit(False)]), For(Id(WMn), BooleanLit(False), NumLit(2.77), Block([CallStmt(Id(YHL0), []), Block([Block([If((NumLit(21.23), Break), [(StringLit(XbN), If((BooleanLit(True), Continue), [(Id(wF), CallStmt(Id(MNzH), [NumLit(3.12), NumLit(51.84)])), (Id(KEZ), Continue), (StringLit(iY), CallStmt(Id(dL6i), [Id(plB), StringLit(u)]))], Continue)), (StringLit(seW), AssignStmt(Id(MF), Id(ZrV)))], VarDecl(Id(rWK), ArrayType([73.32, 13.63, 62.01], StringType), None, None))]), VarDecl(Id(CPz), BoolType, None, None), VarDecl(Id(eZKf), ArrayType([48.91, 58.92, 19.77], NumberType), None, BooleanLit(True))]), Break])), If((NumLit(63.57), If((Id(J0), Block([If((Id(AC), CallStmt(Id(bA), [StringLit(Xxu), Id(ZbU), BooleanLit(True)])), [], None)])), [(NumLit(28.46), AssignStmt(Id(cLby), BooleanLit(False))), (BooleanLit(True), AssignStmt(Id(Pz), StringLit(Zyz)))], Block([AssignStmt(Id(UkLk), NumLit(52.48))]))), [(BooleanLit(True), CallStmt(Id(WPK), [StringLit(iuTL), StringLit(Ey)])), (NumLit(21.59), Continue), (StringLit(T), Block([])), (NumLit(50.86), VarDecl(Id(Bobf), ArrayType([93.8], NumberType), None, StringLit(xbw)))], Block([]))])), FuncDecl(Id(nHB), [VarDecl(Id(g6), BoolType, None, None), VarDecl(Id(Q7HN), StringType, None, None), VarDecl(Id(tySR), ArrayType([82.37, 74.03, 15.16], NumberType), None, None)], Block([For(Id(jcdx), Id(J0), Id(aRVH), CallStmt(Id(SYuU), [Id(AQyz), Id(HQN5)])), Return(Id(bC0)), Break])), VarDecl(Id(inf), ArrayType([89.5, 70.71], StringType), None, BooleanLit(True)), VarDecl(Id(bV1E), StringType, None, None), FuncDecl(Id(Wk), [VarDecl(Id(eH), StringType, None, None), VarDecl(Id(Dv), ArrayType([58.63, 13.7, 2.03], BoolType), None, None), VarDecl(Id(ZN), ArrayType([89.53, 99.73, 67.42], BoolType), None, None)], Return(NumLit(55.73)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011508))

	def test_2153011509(self):
		input = '''
string saCE
bool Jhef[83.6]
func GH (bool Io[81.67,19.39], number ZZ, bool i8_U)
	begin
		continue
		for UVaX until false by false
			number Zm <- false
		jnkv(false, Cw2e, Zt)
	end

'''
		expect = '''Program([VarDecl(Id(saCE), StringType, None, None), VarDecl(Id(Jhef), ArrayType([83.6], BoolType), None, None), FuncDecl(Id(GH), [VarDecl(Id(Io), ArrayType([81.67, 19.39], BoolType), None, None), VarDecl(Id(ZZ), NumberType, None, None), VarDecl(Id(i8_U), BoolType, None, None)], Block([Continue, For(Id(UVaX), BooleanLit(False), BooleanLit(False), VarDecl(Id(Zm), NumberType, None, BooleanLit(False))), CallStmt(Id(jnkv), [BooleanLit(False), Id(Cw2e), Id(Zt)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011509))

	def test_2153011510(self):
		input = '''
bool Ea1h
number qA2d[61.27]
'''
		expect = '''Program([VarDecl(Id(Ea1h), BoolType, None, None), VarDecl(Id(qA2d), ArrayType([61.27], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011510))

	def test_2153011511(self):
		input = '''
dynamic mfOc
func IUD (number EuO[11.07], number Vb, bool Bt)	begin
		return
		number eTF8[21.95,53.1]
	end
number j7[45.43,27.46,5.35] <- true
bool YW3q[80.51,28.77,41.64] <- false
'''
		expect = '''Program([VarDecl(Id(mfOc), None, dynamic, None), FuncDecl(Id(IUD), [VarDecl(Id(EuO), ArrayType([11.07], NumberType), None, None), VarDecl(Id(Vb), NumberType, None, None), VarDecl(Id(Bt), BoolType, None, None)], Block([Return(), VarDecl(Id(eTF8), ArrayType([21.95, 53.1], NumberType), None, None)])), VarDecl(Id(j7), ArrayType([45.43, 27.46, 5.35], NumberType), None, BooleanLit(True)), VarDecl(Id(YW3q), ArrayType([80.51, 28.77, 41.64], BoolType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011511))

	def test_2153011512(self):
		input = '''
number Rg[57.05]
var Da <- "JsC"
'''
		expect = '''Program([VarDecl(Id(Rg), ArrayType([57.05], NumberType), None, None), VarDecl(Id(Da), None, var, StringLit(JsC))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011512))

	def test_2153011513(self):
		input = '''
bool Dp
func Au8i ()	begin
		string NX[3.86]
		break
	end
func EU9 (number pmCi, string Szgn)
	return false
'''
		expect = '''Program([VarDecl(Id(Dp), BoolType, None, None), FuncDecl(Id(Au8i), [], Block([VarDecl(Id(NX), ArrayType([3.86], StringType), None, None), Break])), FuncDecl(Id(EU9), [VarDecl(Id(pmCi), NumberType, None, None), VarDecl(Id(Szgn), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011513))

	def test_2153011514(self):
		input = '''
func eOCq (number geO[93.69,48.54,93.57], number KIKY)	begin
	end

func eSAB (bool mzDJ[30.25], bool ne[42.44,18.18])
	return

'''
		expect = '''Program([FuncDecl(Id(eOCq), [VarDecl(Id(geO), ArrayType([93.69, 48.54, 93.57], NumberType), None, None), VarDecl(Id(KIKY), NumberType, None, None)], Block([])), FuncDecl(Id(eSAB), [VarDecl(Id(mzDJ), ArrayType([30.25], BoolType), None, None), VarDecl(Id(ne), ArrayType([42.44, 18.18], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011514))

	def test_2153011515(self):
		input = '''
func AK (bool H5[99.32], number bbM[67.47,92.12], string hO7X[89.9,79.22])
	return

bool aD <- false
'''
		expect = '''Program([FuncDecl(Id(AK), [VarDecl(Id(H5), ArrayType([99.32], BoolType), None, None), VarDecl(Id(bbM), ArrayType([67.47, 92.12], NumberType), None, None), VarDecl(Id(hO7X), ArrayType([89.9, 79.22], StringType), None, None)], Return()), VarDecl(Id(aD), BoolType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011515))

	def test_2153011516(self):
		input = '''
func ehpr (bool CG[81.78,30.18,48.74])
	begin
		IV09["p", "yeicK", 55.84] <- "auNM"
		continue
		return
	end
'''
		expect = '''Program([FuncDecl(Id(ehpr), [VarDecl(Id(CG), ArrayType([81.78, 30.18, 48.74], BoolType), None, None)], Block([AssignStmt(ArrayCell(Id(IV09), [StringLit(p), StringLit(yeicK), NumLit(55.84)]), StringLit(auNM)), Continue, Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011516))

	def test_2153011517(self):
		input = '''
string REjH[52.78]
func K4h (string QzdN[66.57,76.32])
	begin
	end
number y5[82.81,55.63]
'''
		expect = '''Program([VarDecl(Id(REjH), ArrayType([52.78], StringType), None, None), FuncDecl(Id(K4h), [VarDecl(Id(QzdN), ArrayType([66.57, 76.32], StringType), None, None)], Block([])), VarDecl(Id(y5), ArrayType([82.81, 55.63], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011517))

	def test_2153011518(self):
		input = '''
number T6
func AItW ()
	return "F"

bool DK <- bc
string Hxcy[28.29] <- w1in
func qLa (bool oJD[27.77], bool sDU, bool mUA4)
	begin
	end

'''
		expect = '''Program([VarDecl(Id(T6), NumberType, None, None), FuncDecl(Id(AItW), [], Return(StringLit(F))), VarDecl(Id(DK), BoolType, None, Id(bc)), VarDecl(Id(Hxcy), ArrayType([28.29], StringType), None, Id(w1in)), FuncDecl(Id(qLa), [VarDecl(Id(oJD), ArrayType([27.77], BoolType), None, None), VarDecl(Id(sDU), BoolType, None, None), VarDecl(Id(mUA4), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011518))

	def test_2153011519(self):
		input = '''
func ZB (number Wr, bool Xqmi, number T5[31.51,16.01,1.31])
	return qWA
func CxP (number CwB[24.63], number uK[21.92,55.53], number inpu)
	return false

number XR3 <- false
number HZ <- q4bU
func grk (string tmq_[60.91,22.7], string WksT[31.39,78.42,22.61], string uj1t[19.62,57.82,36.09])	return

'''
		expect = '''Program([FuncDecl(Id(ZB), [VarDecl(Id(Wr), NumberType, None, None), VarDecl(Id(Xqmi), BoolType, None, None), VarDecl(Id(T5), ArrayType([31.51, 16.01, 1.31], NumberType), None, None)], Return(Id(qWA))), FuncDecl(Id(CxP), [VarDecl(Id(CwB), ArrayType([24.63], NumberType), None, None), VarDecl(Id(uK), ArrayType([21.92, 55.53], NumberType), None, None), VarDecl(Id(inpu), NumberType, None, None)], Return(BooleanLit(False))), VarDecl(Id(XR3), NumberType, None, BooleanLit(False)), VarDecl(Id(HZ), NumberType, None, Id(q4bU)), FuncDecl(Id(grk), [VarDecl(Id(tmq_), ArrayType([60.91, 22.7], StringType), None, None), VarDecl(Id(WksT), ArrayType([31.39, 78.42, 22.61], StringType), None, None), VarDecl(Id(uj1t), ArrayType([19.62, 57.82, 36.09], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011519))

	def test_2153011520(self):
		input = '''
func kG ()
	return "liyWr"

'''
		expect = '''Program([FuncDecl(Id(kG), [], Return(StringLit(liyWr)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011520))

	def test_2153011521(self):
		input = '''
string zF[69.6]
'''
		expect = '''Program([VarDecl(Id(zF), ArrayType([69.6], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011521))

	def test_2153011522(self):
		input = '''
string MpV0
var xUc <- ywh5
func Yo (string ELhH)
	begin
		QDpz[vsvb, false] <- false
	end

'''
		expect = '''Program([VarDecl(Id(MpV0), StringType, None, None), VarDecl(Id(xUc), None, var, Id(ywh5)), FuncDecl(Id(Yo), [VarDecl(Id(ELhH), StringType, None, None)], Block([AssignStmt(ArrayCell(Id(QDpz), [Id(vsvb), BooleanLit(False)]), BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011522))

	def test_2153011523(self):
		input = '''
func ULar ()
	return true
number roOe[88.09,35.07]
func jXjv (bool LTKE[86.3], string tdCW, bool KEoH)
	return

'''
		expect = '''Program([FuncDecl(Id(ULar), [], Return(BooleanLit(True))), VarDecl(Id(roOe), ArrayType([88.09, 35.07], NumberType), None, None), FuncDecl(Id(jXjv), [VarDecl(Id(LTKE), ArrayType([86.3], BoolType), None, None), VarDecl(Id(tdCW), StringType, None, None), VarDecl(Id(KEoH), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011523))

	def test_2153011524(self):
		input = '''
string L7I[75.49,67.97,81.39]
func rm (bool Vf3, string MJ1O[55.14])
	begin
		string QW[89.89]
		p1[87.15] <- true
	end
'''
		expect = '''Program([VarDecl(Id(L7I), ArrayType([75.49, 67.97, 81.39], StringType), None, None), FuncDecl(Id(rm), [VarDecl(Id(Vf3), BoolType, None, None), VarDecl(Id(MJ1O), ArrayType([55.14], StringType), None, None)], Block([VarDecl(Id(QW), ArrayType([89.89], StringType), None, None), AssignStmt(ArrayCell(Id(p1), [NumLit(87.15)]), BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011524))

	def test_2153011525(self):
		input = '''
bool Dp[76.96] <- "dTM"
'''
		expect = '''Program([VarDecl(Id(Dp), ArrayType([76.96], BoolType), None, StringLit(dTM))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011525))

	def test_2153011526(self):
		input = '''
func pX_m (string KJ, number uIp[46.84,8.72])	return true

func xmFW (string f4o, string pj, bool cTfo[40.17,93.09,15.05])
	return "ZqTt"
func aO (bool Fgc[41.84,97.72], number WnSS, string uW[9.18,4.59,6.96])
	begin
		break
		return "ruUT"
	end
'''
		expect = '''Program([FuncDecl(Id(pX_m), [VarDecl(Id(KJ), StringType, None, None), VarDecl(Id(uIp), ArrayType([46.84, 8.72], NumberType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(xmFW), [VarDecl(Id(f4o), StringType, None, None), VarDecl(Id(pj), StringType, None, None), VarDecl(Id(cTfo), ArrayType([40.17, 93.09, 15.05], BoolType), None, None)], Return(StringLit(ZqTt))), FuncDecl(Id(aO), [VarDecl(Id(Fgc), ArrayType([41.84, 97.72], BoolType), None, None), VarDecl(Id(WnSS), NumberType, None, None), VarDecl(Id(uW), ArrayType([9.18, 4.59, 6.96], StringType), None, None)], Block([Break, Return(StringLit(ruUT))]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011526))

	def test_2153011527(self):
		input = '''
func amf (number Zrqu, bool VA[44.29], string oFM3[21.5,74.95])	begin
		begin
		end
		for K1n until false by 19.6
			return
	end
bool fv[3.98,81.99,96.33] <- false
'''
		expect = '''Program([FuncDecl(Id(amf), [VarDecl(Id(Zrqu), NumberType, None, None), VarDecl(Id(VA), ArrayType([44.29], BoolType), None, None), VarDecl(Id(oFM3), ArrayType([21.5, 74.95], StringType), None, None)], Block([Block([]), For(Id(K1n), BooleanLit(False), NumLit(19.6), Return())])), VarDecl(Id(fv), ArrayType([3.98, 81.99, 96.33], BoolType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011527))

	def test_2153011528(self):
		input = '''
var UUo7 <- 46.07
string hAf_[92.91]
func uhi ()
	return
number toga[47.94] <- true
'''
		expect = '''Program([VarDecl(Id(UUo7), None, var, NumLit(46.07)), VarDecl(Id(hAf_), ArrayType([92.91], StringType), None, None), FuncDecl(Id(uhi), [], Return()), VarDecl(Id(toga), ArrayType([47.94], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011528))

	def test_2153011529(self):
		input = '''
func Sq9 (number MKe[80.31], bool QuyY)
	return "jDp"

bool q_T7[19.62,16.32,6.24]
number wJ[10.54,23.6] <- "lTvFB"
bool OJD[28.76,30.66,64.06] <- y7yV
'''
		expect = '''Program([FuncDecl(Id(Sq9), [VarDecl(Id(MKe), ArrayType([80.31], NumberType), None, None), VarDecl(Id(QuyY), BoolType, None, None)], Return(StringLit(jDp))), VarDecl(Id(q_T7), ArrayType([19.62, 16.32, 6.24], BoolType), None, None), VarDecl(Id(wJ), ArrayType([10.54, 23.6], NumberType), None, StringLit(lTvFB)), VarDecl(Id(OJD), ArrayType([28.76, 30.66, 64.06], BoolType), None, Id(y7yV))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011529))

	def test_2153011530(self):
		input = '''
func eBjn (bool XYI[24.9])	return jwW

string Ql <- false
bool gj6g <- 78.88
'''
		expect = '''Program([FuncDecl(Id(eBjn), [VarDecl(Id(XYI), ArrayType([24.9], BoolType), None, None)], Return(Id(jwW))), VarDecl(Id(Ql), StringType, None, BooleanLit(False)), VarDecl(Id(gj6g), BoolType, None, NumLit(78.88))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011530))

	def test_2153011531(self):
		input = '''
bool caY4[5.98,55.19] <- SpE7
func AYy9 ()
	begin
		break
		for GBja until false by "Xa"
			soI("vgTuR", "w")
		eLT[false, "fppED", false] <- false
	end

'''
		expect = '''Program([VarDecl(Id(caY4), ArrayType([5.98, 55.19], BoolType), None, Id(SpE7)), FuncDecl(Id(AYy9), [], Block([Break, For(Id(GBja), BooleanLit(False), StringLit(Xa), CallStmt(Id(soI), [StringLit(vgTuR), StringLit(w)])), AssignStmt(ArrayCell(Id(eLT), [BooleanLit(False), StringLit(fppED), BooleanLit(False)]), BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011531))

	def test_2153011532(self):
		input = '''
string tQ[55.35,11.82,45.41] <- false
string mOg[12.36] <- PMA
func vREB (string FtOD[73.89,58.89,65.75])	return "pIDG"

dynamic pd <- zEK
func pc ()
	return 29.77

'''
		expect = '''Program([VarDecl(Id(tQ), ArrayType([55.35, 11.82, 45.41], StringType), None, BooleanLit(False)), VarDecl(Id(mOg), ArrayType([12.36], StringType), None, Id(PMA)), FuncDecl(Id(vREB), [VarDecl(Id(FtOD), ArrayType([73.89, 58.89, 65.75], StringType), None, None)], Return(StringLit(pIDG))), VarDecl(Id(pd), None, dynamic, Id(zEK)), FuncDecl(Id(pc), [], Return(NumLit(29.77)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011532))

	def test_2153011533(self):
		input = '''
bool QP
'''
		expect = '''Program([VarDecl(Id(QP), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011533))

	def test_2153011534(self):
		input = '''
func hntM (number vZ, string y0u)	return
func JOan ()	begin
		continue
	end
func mFCh (bool nh4[52.04,99.67], string Tc)	return
number W9[96.58,22.88,8.95]
func N1cU (bool GU, string ZTq, number G51g)	return "UDRN"

'''
		expect = '''Program([FuncDecl(Id(hntM), [VarDecl(Id(vZ), NumberType, None, None), VarDecl(Id(y0u), StringType, None, None)], Return()), FuncDecl(Id(JOan), [], Block([Continue])), FuncDecl(Id(mFCh), [VarDecl(Id(nh4), ArrayType([52.04, 99.67], BoolType), None, None), VarDecl(Id(Tc), StringType, None, None)], Return()), VarDecl(Id(W9), ArrayType([96.58, 22.88, 8.95], NumberType), None, None), FuncDecl(Id(N1cU), [VarDecl(Id(GU), BoolType, None, None), VarDecl(Id(ZTq), StringType, None, None), VarDecl(Id(G51g), NumberType, None, None)], Return(StringLit(UDRN)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011534))

	def test_2153011535(self):
		input = '''
number SLPb
number i0[36.81,81.77] <- true
func Pkc (number Zm, number scH[84.99])
	begin
		gzs[false, Rq5, 66.5] <- "gwmQz"
		for xB5 until 76.05 by "dGBF"
			Z6[false, 67.24] <- 55.41
		string Ur
	end

'''
		expect = '''Program([VarDecl(Id(SLPb), NumberType, None, None), VarDecl(Id(i0), ArrayType([36.81, 81.77], NumberType), None, BooleanLit(True)), FuncDecl(Id(Pkc), [VarDecl(Id(Zm), NumberType, None, None), VarDecl(Id(scH), ArrayType([84.99], NumberType), None, None)], Block([AssignStmt(ArrayCell(Id(gzs), [BooleanLit(False), Id(Rq5), NumLit(66.5)]), StringLit(gwmQz)), For(Id(xB5), NumLit(76.05), StringLit(dGBF), AssignStmt(ArrayCell(Id(Z6), [BooleanLit(False), NumLit(67.24)]), NumLit(55.41))), VarDecl(Id(Ur), StringType, None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011535))

	def test_2153011536(self):
		input = '''
bool zbX0
string pk
string iF <- false
'''
		expect = '''Program([VarDecl(Id(zbX0), BoolType, None, None), VarDecl(Id(pk), StringType, None, None), VarDecl(Id(iF), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011536))

	def test_2153011537(self):
		input = '''
func E1 (bool qsYX, number CGi, number tY9o)	begin
	end

var ar <- 59.29
var lAx <- Qcz
'''
		expect = '''Program([FuncDecl(Id(E1), [VarDecl(Id(qsYX), BoolType, None, None), VarDecl(Id(CGi), NumberType, None, None), VarDecl(Id(tY9o), NumberType, None, None)], Block([])), VarDecl(Id(ar), None, var, NumLit(59.29)), VarDecl(Id(lAx), None, var, Id(Qcz))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011537))

	def test_2153011538(self):
		input = '''
func H3 (number KPo)
	begin
		if ("A") LZem(52.41, PYf, true)
		elif (25.34)
		continue
		else break
		begin
		end
		return "Ax"
	end
dynamic YMp
func i3 (bool no, number lG[46.74,96.18], bool l18v)	return "P"
'''
		expect = '''Program([FuncDecl(Id(H3), [VarDecl(Id(KPo), NumberType, None, None)], Block([If((StringLit(A), CallStmt(Id(LZem), [NumLit(52.41), Id(PYf), BooleanLit(True)])), [(NumLit(25.34), Continue)], Break), Block([]), Return(StringLit(Ax))])), VarDecl(Id(YMp), None, dynamic, None), FuncDecl(Id(i3), [VarDecl(Id(no), BoolType, None, None), VarDecl(Id(lG), ArrayType([46.74, 96.18], NumberType), None, None), VarDecl(Id(l18v), BoolType, None, None)], Return(StringLit(P)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011538))

	def test_2153011539(self):
		input = '''
bool qZ9[24.36,54.69]
var wFfp <- k23
bool sM[8.5,10.28,0.84]
func cp (string zy2)
	return 95.45
'''
		expect = '''Program([VarDecl(Id(qZ9), ArrayType([24.36, 54.69], BoolType), None, None), VarDecl(Id(wFfp), None, var, Id(k23)), VarDecl(Id(sM), ArrayType([8.5, 10.28, 0.84], BoolType), None, None), FuncDecl(Id(cp), [VarDecl(Id(zy2), StringType, None, None)], Return(NumLit(95.45)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011539))

	def test_2153011540(self):
		input = '''
bool Iww[73.62]
'''
		expect = '''Program([VarDecl(Id(Iww), ArrayType([73.62], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011540))

	def test_2153011541(self):
		input = '''
func nw (bool qri[77.51,99.33,0.04], string Rr1x[45.05,80.75,39.89])
	begin
		if (false) if ("hAU")
		for kx until 38.53 by NPf
			for TL6 until MT70 by "rO"
				for cf until bW6s by 40.81
					B2[false, 31.77, "vW"] <- QPo
		elif (qi)
		for pEy until 82.55 by t7N
			begin
				if (92.17) for xr7 until "sThDc" by Adt
					if (false)
					continue
					elif ("nflis") begin
						ok()
					end
					elif (CJw) begin
					end
					elif (2.33)
					continue
					elif (nn1) bool Oh[39.52,61.63]
				elif (true) break
				return 26.59
			end
		elif (92.42) if (Lpn0) break
		elif (true) var cxC <- "Nk"
		elif (Q9)
		if (true) return
		elif ("mJa") break
		elif (true) return
		elif (rl) var Gp5a <- 36.03
		elif ("o") for gA until 77.31 by false
			continue
		elif (true)
		ws("lqvs", 23.02, "iRDl")
		elif (false)
		if ("i") if (vfA)
		return Zx
		elif (63.63)
		for JL until 61.73 by false
			if (true) if (true) for NBf until 24.23 by RY6
				woVp(false, SjV, true)
			elif (false)
			if (true) continue
			elif ("pdZ")
			cxb(HPUw)
			elif (true) string Qq <- "NGWxF"
			elif ("c") k_D("cB")
			elif ("s") continue
			elif ("E") begin
			end
			else y6NY("tbHN", SA)
		elif (DfF4)
		return
		else break
		else bool V18
		elif (false)
		string JD4 <- "CuNma"
		elif (HCs)
		if ("I")
		string aFQ[18.16,7.17,81.83]
		elif (false) for Rk5R until 59.0 by "OqfbL"
			string iJxL[76.01]
		elif (37.55) begin
			continue
			tW(J9K, false, false)
		end
		elif (true)
		RRNw("SNOiq")
		elif (qtS) if (ED) for Hv until "EFb" by 72.86
			HraW()
		elif (Rj_d) break
		elif ("GE")
		break
		elif (true) if (48.86)
		return Eqid
		G5Ep[false, "Tgupu", "bqS"] <- 85.21
	end
func jVxQ (string Kc[82.18])
	return

func j1t (number Kzo, number sh, number rc5)	begin
		Xj("mayI")
		bool q94i[48.2,72.44]
		for eFz until bT by true
			break
	end
'''
		expect = '''Program([FuncDecl(Id(nw), [VarDecl(Id(qri), ArrayType([77.51, 99.33, 0.04], BoolType), None, None), VarDecl(Id(Rr1x), ArrayType([45.05, 80.75, 39.89], StringType), None, None)], Block([If((BooleanLit(False), If((StringLit(hAU), For(Id(kx), NumLit(38.53), Id(NPf), For(Id(TL6), Id(MT70), StringLit(rO), For(Id(cf), Id(bW6s), NumLit(40.81), AssignStmt(ArrayCell(Id(B2), [BooleanLit(False), NumLit(31.77), StringLit(vW)]), Id(QPo)))))), [(Id(qi), For(Id(pEy), NumLit(82.55), Id(t7N), Block([If((NumLit(92.17), For(Id(xr7), StringLit(sThDc), Id(Adt), If((BooleanLit(False), Continue), [(StringLit(nflis), Block([CallStmt(Id(ok), [])])), (Id(CJw), Block([])), (NumLit(2.33), Continue), (Id(nn1), VarDecl(Id(Oh), ArrayType([39.52, 61.63], BoolType), None, None)), (BooleanLit(True), Break)], None))), [], None), Return(NumLit(26.59))]))), (NumLit(92.42), If((Id(Lpn0), Break), [(BooleanLit(True), VarDecl(Id(cxC), None, var, StringLit(Nk))), (Id(Q9), If((BooleanLit(True), Return()), [(StringLit(mJa), Break), (BooleanLit(True), Return()), (Id(rl), VarDecl(Id(Gp5a), None, var, NumLit(36.03))), (StringLit(o), For(Id(gA), NumLit(77.31), BooleanLit(False), Continue)), (BooleanLit(True), CallStmt(Id(ws), [StringLit(lqvs), NumLit(23.02), StringLit(iRDl)])), (BooleanLit(False), If((StringLit(i), If((Id(vfA), Return(Id(Zx))), [(NumLit(63.63), For(Id(JL), NumLit(61.73), BooleanLit(False), If((BooleanLit(True), If((BooleanLit(True), For(Id(NBf), NumLit(24.23), Id(RY6), CallStmt(Id(woVp), [BooleanLit(False), Id(SjV), BooleanLit(True)]))), [(BooleanLit(False), If((BooleanLit(True), Continue), [(StringLit(pdZ), CallStmt(Id(cxb), [Id(HPUw)])), (BooleanLit(True), VarDecl(Id(Qq), StringType, None, StringLit(NGWxF))), (StringLit(c), CallStmt(Id(k_D), [StringLit(cB)])), (StringLit(s), Continue), (StringLit(E), Block([]))], CallStmt(Id(y6NY), [StringLit(tbHN), Id(SA)]))), (Id(DfF4), Return())], Break)), [], VarDecl(Id(V18), BoolType, None, None)))), (BooleanLit(False), VarDecl(Id(JD4), StringType, None, StringLit(CuNma))), (Id(HCs), If((StringLit(I), VarDecl(Id(aFQ), ArrayType([18.16, 7.17, 81.83], StringType), None, None)), [(BooleanLit(False), For(Id(Rk5R), NumLit(59.0), StringLit(OqfbL), VarDecl(Id(iJxL), ArrayType([76.01], StringType), None, None))), (NumLit(37.55), Block([Continue, CallStmt(Id(tW), [Id(J9K), BooleanLit(False), BooleanLit(False)])])), (BooleanLit(True), CallStmt(Id(RRNw), [StringLit(SNOiq)])), (Id(qtS), If((Id(ED), For(Id(Hv), StringLit(EFb), NumLit(72.86), CallStmt(Id(HraW), []))), [(Id(Rj_d), Break), (StringLit(GE), Break), (BooleanLit(True), If((NumLit(48.86), Return(Id(Eqid))), [], None))], None))], None))], None)), [], None))], None))], None))], None)), [], None), AssignStmt(ArrayCell(Id(G5Ep), [BooleanLit(False), StringLit(Tgupu), StringLit(bqS)]), NumLit(85.21))])), FuncDecl(Id(jVxQ), [VarDecl(Id(Kc), ArrayType([82.18], StringType), None, None)], Return()), FuncDecl(Id(j1t), [VarDecl(Id(Kzo), NumberType, None, None), VarDecl(Id(sh), NumberType, None, None), VarDecl(Id(rc5), NumberType, None, None)], Block([CallStmt(Id(Xj), [StringLit(mayI)]), VarDecl(Id(q94i), ArrayType([48.2, 72.44], BoolType), None, None), For(Id(eFz), Id(bT), BooleanLit(True), Break)]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011541))

	def test_2153011542(self):
		input = '''
func KFAO (string nm, number h_S)	return "kG"
string F8ye[43.24]
func VC (number jH, bool cH[3.19,18.01,64.4], bool qj[7.04])
	return true

number lK2I
'''
		expect = '''Program([FuncDecl(Id(KFAO), [VarDecl(Id(nm), StringType, None, None), VarDecl(Id(h_S), NumberType, None, None)], Return(StringLit(kG))), VarDecl(Id(F8ye), ArrayType([43.24], StringType), None, None), FuncDecl(Id(VC), [VarDecl(Id(jH), NumberType, None, None), VarDecl(Id(cH), ArrayType([3.19, 18.01, 64.4], BoolType), None, None), VarDecl(Id(qj), ArrayType([7.04], BoolType), None, None)], Return(BooleanLit(True))), VarDecl(Id(lK2I), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011542))

	def test_2153011543(self):
		input = '''
bool dua[58.44,36.3,62.95] <- "CEtw"
number D5uE[15.52,55.98,64.09]
'''
		expect = '''Program([VarDecl(Id(dua), ArrayType([58.44, 36.3, 62.95], BoolType), None, StringLit(CEtw)), VarDecl(Id(D5uE), ArrayType([15.52, 55.98, 64.09], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011543))

	def test_2153011544(self):
		input = '''
func Yb (bool fA)
	begin
		begin
			continue
			continue
		end
		var vxH8 <- false
	end
func Iy ()
	begin
		bool rw[89.71,92.41] <- r7x5
		continue
		number fHg
	end
func P0 (string a4F[79.06], number is[66.01], string fHN)	return

bool Ypdx[78.34] <- f7
'''
		expect = '''Program([FuncDecl(Id(Yb), [VarDecl(Id(fA), BoolType, None, None)], Block([Block([Continue, Continue]), VarDecl(Id(vxH8), None, var, BooleanLit(False))])), FuncDecl(Id(Iy), [], Block([VarDecl(Id(rw), ArrayType([89.71, 92.41], BoolType), None, Id(r7x5)), Continue, VarDecl(Id(fHg), NumberType, None, None)])), FuncDecl(Id(P0), [VarDecl(Id(a4F), ArrayType([79.06], StringType), None, None), VarDecl(Id(is), ArrayType([66.01], NumberType), None, None), VarDecl(Id(fHN), StringType, None, None)], Return()), VarDecl(Id(Ypdx), ArrayType([78.34], BoolType), None, Id(f7))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011544))

	def test_2153011545(self):
		input = '''
string FN
'''
		expect = '''Program([VarDecl(Id(FN), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011545))

	def test_2153011546(self):
		input = '''
func fw (bool jd[82.58], string TOdU, string Nfkz)	return

'''
		expect = '''Program([FuncDecl(Id(fw), [VarDecl(Id(jd), ArrayType([82.58], BoolType), None, None), VarDecl(Id(TOdU), StringType, None, None), VarDecl(Id(Nfkz), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011546))

	def test_2153011547(self):
		input = '''
func wm (bool lo, string qKO[25.02])
	return

func Hvbx (number oFh3[76.41,46.5], number D8t, number cH0[99.2,20.72,12.25])	return "D"
number Dm[22.43] <- UYxd
'''
		expect = '''Program([FuncDecl(Id(wm), [VarDecl(Id(lo), BoolType, None, None), VarDecl(Id(qKO), ArrayType([25.02], StringType), None, None)], Return()), FuncDecl(Id(Hvbx), [VarDecl(Id(oFh3), ArrayType([76.41, 46.5], NumberType), None, None), VarDecl(Id(D8t), NumberType, None, None), VarDecl(Id(cH0), ArrayType([99.2, 20.72, 12.25], NumberType), None, None)], Return(StringLit(D))), VarDecl(Id(Dm), ArrayType([22.43], NumberType), None, Id(UYxd))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011547))

	def test_2153011548(self):
		input = '''
func Azt ()	begin
	end

string LXr[16.17,66.16]
bool cmh
'''
		expect = '''Program([FuncDecl(Id(Azt), [], Block([])), VarDecl(Id(LXr), ArrayType([16.17, 66.16], StringType), None, None), VarDecl(Id(cmh), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011548))

	def test_2153011549(self):
		input = '''
var tA <- 64.0
func dE_l (bool n6X[44.38])
	begin
		break
		break
		break
	end
func o9A ()	return
func oNHV ()	return i5U

'''
		expect = '''Program([VarDecl(Id(tA), None, var, NumLit(64.0)), FuncDecl(Id(dE_l), [VarDecl(Id(n6X), ArrayType([44.38], BoolType), None, None)], Block([Break, Break, Break])), FuncDecl(Id(o9A), [], Return()), FuncDecl(Id(oNHV), [], Return(Id(i5U)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011549))

	def test_2153011550(self):
		input = '''
number eKs
func zKc (string a8fB[39.73])	return "vbPA"
func jtt ()	return true

bool db[31.58] <- "o"
func Y28w (bool Nqt[67.97,42.0,83.52])
	begin
		LjL <- "ooj"
		for umko until zaZ by true
			break
		return "g"
	end

'''
		expect = '''Program([VarDecl(Id(eKs), NumberType, None, None), FuncDecl(Id(zKc), [VarDecl(Id(a8fB), ArrayType([39.73], StringType), None, None)], Return(StringLit(vbPA))), FuncDecl(Id(jtt), [], Return(BooleanLit(True))), VarDecl(Id(db), ArrayType([31.58], BoolType), None, StringLit(o)), FuncDecl(Id(Y28w), [VarDecl(Id(Nqt), ArrayType([67.97, 42.0, 83.52], BoolType), None, None)], Block([AssignStmt(Id(LjL), StringLit(ooj)), For(Id(umko), Id(zaZ), BooleanLit(True), Break), Return(StringLit(g))]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011550))

	def test_2153011551(self):
		input = '''
func fi4C (string zw, bool CB2[25.71,99.26,90.61])
	return

func fq_n (string uW, string uyX[14.66], string M_Z)
	begin
	end
dynamic DN
'''
		expect = '''Program([FuncDecl(Id(fi4C), [VarDecl(Id(zw), StringType, None, None), VarDecl(Id(CB2), ArrayType([25.71, 99.26, 90.61], BoolType), None, None)], Return()), FuncDecl(Id(fq_n), [VarDecl(Id(uW), StringType, None, None), VarDecl(Id(uyX), ArrayType([14.66], StringType), None, None), VarDecl(Id(M_Z), StringType, None, None)], Block([])), VarDecl(Id(DN), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011551))

	def test_2153011552(self):
		input = '''
func pMJc (number YFRM, number T5C[17.83,93.76])	return false

var P0 <- false
'''
		expect = '''Program([FuncDecl(Id(pMJc), [VarDecl(Id(YFRM), NumberType, None, None), VarDecl(Id(T5C), ArrayType([17.83, 93.76], NumberType), None, None)], Return(BooleanLit(False))), VarDecl(Id(P0), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011552))

	def test_2153011553(self):
		input = '''
bool W_n
string YNSE[44.52]
'''
		expect = '''Program([VarDecl(Id(W_n), BoolType, None, None), VarDecl(Id(YNSE), ArrayType([44.52], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011553))

	def test_2153011554(self):
		input = '''
var D0rO <- true
dynamic uaBQ
'''
		expect = '''Program([VarDecl(Id(D0rO), None, var, BooleanLit(True)), VarDecl(Id(uaBQ), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011554))

	def test_2153011555(self):
		input = '''
bool Ouyl
func Twuo (bool pz[16.25], string Ysgp[68.36], string bWbZ[46.48,62.81])
	begin
		Jr()
		begin
			bool c46u <- "xgc"
			begin
				begin
					if (true)
					number Ry[37.73,96.07,6.06] <- "j"
					elif (42.0)
					break
					elif (37.06)
					if ("Ono")
					return "hZ"
					elif (false) string yyXB[61.93,83.36] <- true
					else if (true)
					break
					elif (false)
					continue
					elif (false)
					begin
					end
					elif (kG) string B96[48.14] <- 8.26
					elif (x2)
					for siY until ySp by pq
						tgzT[true] <- false
					elif (Yv)
					in("fYL", "Ky")
					elif (false) if ("dg")
					for Ylu until "cfB" by true
						continue
					elif (R752)
					break
					elif (KTh) if (45.72) if ("ED") uT()
					elif (87.9) if ("tEDn") begin
						Er5a <- false
						if (true) break
						elif (false)
						pi <- xkR
						elif (40.78)
						gXM_[29.75, "drSiz", 41.68] <- "zW"
						elif (78.52)
						begin
							break
						end
						elif (false)
						return
						break
					end
					elif (false)
					l9X <- 55.9
					else for SBF until L6Jq by 51.24
						number QV
					else begin
					end
					elif ("TIYA")
					number MF
					elif (WX)
					for YZ until "FGyPm" by 26.73
						begin
							if ("bP")
							dynamic g_8m
							fUjz(yIvB)
							if (true) G_(true, "gpjRm")
							elif (true) break
							elif (false)
							if (93.09)
							continue
							elif (reO) for pbXy until 83.13 by true
								break
							elif (false)
							return
							elif (true)
							return 67.04
							else continue
							elif (pq) ODJM <- "W"
							elif (26.97) R0_I(true)
							elif (true) continue
						end
					elif (67.65) xU[false] <- true
					elif (false) if (83.04)
					continue
					elif (17.0) continue
					elif (true)
					break
					elif (false) return DY
					elif (false) v8(49.93)
					elif (52.24) Xj("AUOJ", 18.67, 67.53)
					elif (LJm) if (true) for JB3 until "FRH" by cUA
						if (false) string Bh[3.0,22.32,89.18] <- true
						elif (MEd)
						break
						elif (92.16)
						return ZC
						elif (yM)
						continue
						else continue
					else Es <- false
					else Jo8[true, 35.7, 59.0] <- true
					elif (false) return
				end
				if (true)
				bool Fg7[53.34,20.46,4.06]
				continue
			end
			break
		end
		break
	end
'''
		expect = '''Program([VarDecl(Id(Ouyl), BoolType, None, None), FuncDecl(Id(Twuo), [VarDecl(Id(pz), ArrayType([16.25], BoolType), None, None), VarDecl(Id(Ysgp), ArrayType([68.36], StringType), None, None), VarDecl(Id(bWbZ), ArrayType([46.48, 62.81], StringType), None, None)], Block([CallStmt(Id(Jr), []), Block([VarDecl(Id(c46u), BoolType, None, StringLit(xgc)), Block([Block([If((BooleanLit(True), VarDecl(Id(Ry), ArrayType([37.73, 96.07, 6.06], NumberType), None, StringLit(j))), [(NumLit(42.0), Break), (NumLit(37.06), If((StringLit(Ono), Return(StringLit(hZ))), [(BooleanLit(False), VarDecl(Id(yyXB), ArrayType([61.93, 83.36], StringType), None, BooleanLit(True)))], If((BooleanLit(True), Break), [(BooleanLit(False), Continue), (BooleanLit(False), Block([])), (Id(kG), VarDecl(Id(B96), ArrayType([48.14], StringType), None, NumLit(8.26))), (Id(x2), For(Id(siY), Id(ySp), Id(pq), AssignStmt(ArrayCell(Id(tgzT), [BooleanLit(True)]), BooleanLit(False)))), (Id(Yv), CallStmt(Id(in), [StringLit(fYL), StringLit(Ky)])), (BooleanLit(False), If((StringLit(dg), For(Id(Ylu), StringLit(cfB), BooleanLit(True), Continue)), [(Id(R752), Break), (Id(KTh), If((NumLit(45.72), If((StringLit(ED), CallStmt(Id(uT), [])), [(NumLit(87.9), If((StringLit(tEDn), Block([AssignStmt(Id(Er5a), BooleanLit(False)), If((BooleanLit(True), Break), [(BooleanLit(False), AssignStmt(Id(pi), Id(xkR))), (NumLit(40.78), AssignStmt(ArrayCell(Id(gXM_), [NumLit(29.75), StringLit(drSiz), NumLit(41.68)]), StringLit(zW))), (NumLit(78.52), Block([Break])), (BooleanLit(False), Return())], None), Break])), [(BooleanLit(False), AssignStmt(Id(l9X), NumLit(55.9)))], For(Id(SBF), Id(L6Jq), NumLit(51.24), VarDecl(Id(QV), NumberType, None, None))))], Block([]))), [(StringLit(TIYA), VarDecl(Id(MF), NumberType, None, None)), (Id(WX), For(Id(YZ), StringLit(FGyPm), NumLit(26.73), Block([If((StringLit(bP), VarDecl(Id(g_8m), None, dynamic, None)), [], None), CallStmt(Id(fUjz), [Id(yIvB)]), If((BooleanLit(True), CallStmt(Id(G_), [BooleanLit(True), StringLit(gpjRm)])), [(BooleanLit(True), Break), (BooleanLit(False), If((NumLit(93.09), Continue), [(Id(reO), For(Id(pbXy), NumLit(83.13), BooleanLit(True), Break)), (BooleanLit(False), Return()), (BooleanLit(True), Return(NumLit(67.04)))], Continue)), (Id(pq), AssignStmt(Id(ODJM), StringLit(W))), (NumLit(26.97), CallStmt(Id(R0_I), [BooleanLit(True)])), (BooleanLit(True), Continue)], None)]))), (NumLit(67.65), AssignStmt(ArrayCell(Id(xU), [BooleanLit(False)]), BooleanLit(True))), (BooleanLit(False), If((NumLit(83.04), Continue), [(NumLit(17.0), Continue), (BooleanLit(True), Break), (BooleanLit(False), Return(Id(DY))), (BooleanLit(False), CallStmt(Id(v8), [NumLit(49.93)])), (NumLit(52.24), CallStmt(Id(Xj), [StringLit(AUOJ), NumLit(18.67), NumLit(67.53)])), (Id(LJm), If((BooleanLit(True), For(Id(JB3), StringLit(FRH), Id(cUA), If((BooleanLit(False), VarDecl(Id(Bh), ArrayType([3.0, 22.32, 89.18], StringType), None, BooleanLit(True))), [(Id(MEd), Break), (NumLit(92.16), Return(Id(ZC))), (Id(yM), Continue)], Continue))), [], AssignStmt(Id(Es), BooleanLit(False))))], AssignStmt(ArrayCell(Id(Jo8), [BooleanLit(True), NumLit(35.7), NumLit(59.0)]), BooleanLit(True)))), (BooleanLit(False), Return())], None))], None))], None)))], None)]), If((BooleanLit(True), VarDecl(Id(Fg7), ArrayType([53.34, 20.46, 4.06], BoolType), None, None)), [], None), Continue]), Break]), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011555))

	def test_2153011556(self):
		input = '''
number eb1a[92.93,24.44,87.54]
bool Hx
bool PTU <- 18.38
bool GaLS[42.1,37.35,13.09] <- "tilf"
'''
		expect = '''Program([VarDecl(Id(eb1a), ArrayType([92.93, 24.44, 87.54], NumberType), None, None), VarDecl(Id(Hx), BoolType, None, None), VarDecl(Id(PTU), BoolType, None, NumLit(18.38)), VarDecl(Id(GaLS), ArrayType([42.1, 37.35, 13.09], BoolType), None, StringLit(tilf))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011556))

	def test_2153011557(self):
		input = '''
var XK2L <- true
'''
		expect = '''Program([VarDecl(Id(XK2L), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011557))

	def test_2153011558(self):
		input = '''
number Qnrk[92.9,61.76,53.19]
bool rLo
string q719[36.07,98.92,40.69]
func RqP5 ()	begin
		string HjU <- 46.89
		continue
	end
dynamic Dn
'''
		expect = '''Program([VarDecl(Id(Qnrk), ArrayType([92.9, 61.76, 53.19], NumberType), None, None), VarDecl(Id(rLo), BoolType, None, None), VarDecl(Id(q719), ArrayType([36.07, 98.92, 40.69], StringType), None, None), FuncDecl(Id(RqP5), [], Block([VarDecl(Id(HjU), StringType, None, NumLit(46.89)), Continue])), VarDecl(Id(Dn), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011558))

	def test_2153011559(self):
		input = '''
func kXf7 ()	begin
	end

'''
		expect = '''Program([FuncDecl(Id(kXf7), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011559))

	def test_2153011560(self):
		input = '''
dynamic lk5 <- 28.46
func Ut7O (bool VtW[27.61], bool Bg)	return xntN

bool xoqc[40.71,72.67]
string Onj
func tuq (bool tT)
	return
'''
		expect = '''Program([VarDecl(Id(lk5), None, dynamic, NumLit(28.46)), FuncDecl(Id(Ut7O), [VarDecl(Id(VtW), ArrayType([27.61], BoolType), None, None), VarDecl(Id(Bg), BoolType, None, None)], Return(Id(xntN))), VarDecl(Id(xoqc), ArrayType([40.71, 72.67], BoolType), None, None), VarDecl(Id(Onj), StringType, None, None), FuncDecl(Id(tuq), [VarDecl(Id(tT), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011560))

	def test_2153011561(self):
		input = '''
bool ZB8[95.71,8.91]
'''
		expect = '''Program([VarDecl(Id(ZB8), ArrayType([95.71, 8.91], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011561))

	def test_2153011562(self):
		input = '''
func HKi6 (bool qG, bool w7[80.3], bool YW0[7.2])
	return
number dr2
string gK5[90.65,16.02,55.52] <- MrZu
'''
		expect = '''Program([FuncDecl(Id(HKi6), [VarDecl(Id(qG), BoolType, None, None), VarDecl(Id(w7), ArrayType([80.3], BoolType), None, None), VarDecl(Id(YW0), ArrayType([7.2], BoolType), None, None)], Return()), VarDecl(Id(dr2), NumberType, None, None), VarDecl(Id(gK5), ArrayType([90.65, 16.02, 55.52], StringType), None, Id(MrZu))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011562))

	def test_2153011563(self):
		input = '''
string Z1Hs <- Ui_
func eBwp (string CkzW[84.34,28.28], bool NH, string emC)	return

'''
		expect = '''Program([VarDecl(Id(Z1Hs), StringType, None, Id(Ui_)), FuncDecl(Id(eBwp), [VarDecl(Id(CkzW), ArrayType([84.34, 28.28], StringType), None, None), VarDecl(Id(NH), BoolType, None, None), VarDecl(Id(emC), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011563))

	def test_2153011564(self):
		input = '''
string hEm3 <- B5T5
bool PoG <- 28.67
func Evu (string STN[83.55,27.21], string SVQ)
	return
'''
		expect = '''Program([VarDecl(Id(hEm3), StringType, None, Id(B5T5)), VarDecl(Id(PoG), BoolType, None, NumLit(28.67)), FuncDecl(Id(Evu), [VarDecl(Id(STN), ArrayType([83.55, 27.21], StringType), None, None), VarDecl(Id(SVQ), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011564))

	def test_2153011565(self):
		input = '''
string PRy[42.52,57.3]
'''
		expect = '''Program([VarDecl(Id(PRy), ArrayType([42.52, 57.3], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011565))

	def test_2153011566(self):
		input = '''
string h2[27.16,1.32,36.31]
dynamic No <- "G"
func AI ()
	return
func rs (string vUN)	return true

'''
		expect = '''Program([VarDecl(Id(h2), ArrayType([27.16, 1.32, 36.31], StringType), None, None), VarDecl(Id(No), None, dynamic, StringLit(G)), FuncDecl(Id(AI), [], Return()), FuncDecl(Id(rs), [VarDecl(Id(vUN), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011566))

	def test_2153011567(self):
		input = '''
func mZ (number Qs, string JdJF, string iFP[29.02,95.74,67.53])	return

string ja[43.39]
string fre <- JP6U
'''
		expect = '''Program([FuncDecl(Id(mZ), [VarDecl(Id(Qs), NumberType, None, None), VarDecl(Id(JdJF), StringType, None, None), VarDecl(Id(iFP), ArrayType([29.02, 95.74, 67.53], StringType), None, None)], Return()), VarDecl(Id(ja), ArrayType([43.39], StringType), None, None), VarDecl(Id(fre), StringType, None, Id(JP6U))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011567))

	def test_2153011568(self):
		input = '''
func t8gz (string gT, string SJ)	return DRf
number dtr <- 48.03
'''
		expect = '''Program([FuncDecl(Id(t8gz), [VarDecl(Id(gT), StringType, None, None), VarDecl(Id(SJ), StringType, None, None)], Return(Id(DRf))), VarDecl(Id(dtr), NumberType, None, NumLit(48.03))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011568))

	def test_2153011569(self):
		input = '''
number kn <- 89.47
dynamic rs <- "FvY"
func JpFa ()
	return "V"
func Hovz (number tu[95.23,70.49,79.4])	return
'''
		expect = '''Program([VarDecl(Id(kn), NumberType, None, NumLit(89.47)), VarDecl(Id(rs), None, dynamic, StringLit(FvY)), FuncDecl(Id(JpFa), [], Return(StringLit(V))), FuncDecl(Id(Hovz), [VarDecl(Id(tu), ArrayType([95.23, 70.49, 79.4], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011569))

	def test_2153011570(self):
		input = '''
func a_xg ()	return GGXO

func dm (number zW, string RxB2[96.83,21.3])	return "I"

func cezl (number sLr, bool AcDh)
	begin
		break
		rxP <- 99.6
	end
func WD1 (string RU)
	return 76.73

'''
		expect = '''Program([FuncDecl(Id(a_xg), [], Return(Id(GGXO))), FuncDecl(Id(dm), [VarDecl(Id(zW), NumberType, None, None), VarDecl(Id(RxB2), ArrayType([96.83, 21.3], StringType), None, None)], Return(StringLit(I))), FuncDecl(Id(cezl), [VarDecl(Id(sLr), NumberType, None, None), VarDecl(Id(AcDh), BoolType, None, None)], Block([Break, AssignStmt(Id(rxP), NumLit(99.6))])), FuncDecl(Id(WD1), [VarDecl(Id(RU), StringType, None, None)], Return(NumLit(76.73)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011570))

	def test_2153011571(self):
		input = '''
func s5MX (bool syEB[69.45], bool U2oL[75.4,37.77])	return 34.08

number kGD
number wq[37.83] <- "JHz"
'''
		expect = '''Program([FuncDecl(Id(s5MX), [VarDecl(Id(syEB), ArrayType([69.45], BoolType), None, None), VarDecl(Id(U2oL), ArrayType([75.4, 37.77], BoolType), None, None)], Return(NumLit(34.08))), VarDecl(Id(kGD), NumberType, None, None), VarDecl(Id(wq), ArrayType([37.83], NumberType), None, StringLit(JHz))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011571))

	def test_2153011572(self):
		input = '''
number jz
func sx3 (number jP)
	return
number CnZ[97.98,36.32]
func YE2 (bool v8vn, string UZYq[91.16,76.0], bool yU93[3.15,89.38])	return true

'''
		expect = '''Program([VarDecl(Id(jz), NumberType, None, None), FuncDecl(Id(sx3), [VarDecl(Id(jP), NumberType, None, None)], Return()), VarDecl(Id(CnZ), ArrayType([97.98, 36.32], NumberType), None, None), FuncDecl(Id(YE2), [VarDecl(Id(v8vn), BoolType, None, None), VarDecl(Id(UZYq), ArrayType([91.16, 76.0], StringType), None, None), VarDecl(Id(yU93), ArrayType([3.15, 89.38], BoolType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011572))

	def test_2153011573(self):
		input = '''
func qe7s (bool JW, bool zdM[92.62,81.33,67.54], string EQt6[23.03])
	return 46.42
string rzP[28.89] <- true
'''
		expect = '''Program([FuncDecl(Id(qe7s), [VarDecl(Id(JW), BoolType, None, None), VarDecl(Id(zdM), ArrayType([92.62, 81.33, 67.54], BoolType), None, None), VarDecl(Id(EQt6), ArrayType([23.03], StringType), None, None)], Return(NumLit(46.42))), VarDecl(Id(rzP), ArrayType([28.89], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011573))

	def test_2153011574(self):
		input = '''
func gpC ()
	begin
		return
		break
	end

bool UPm[14.61,0.11] <- urhZ
'''
		expect = '''Program([FuncDecl(Id(gpC), [], Block([Return(), Break])), VarDecl(Id(UPm), ArrayType([14.61, 0.11], BoolType), None, Id(urhZ))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011574))

	def test_2153011575(self):
		input = '''
dynamic k2 <- LY
string Gt7X[0.68] <- 39.55
func J_y4 (string da[4.84,81.48], number naE5, bool zPtP[25.11,97.96])
	return

string H4cx[93.71,87.85]
func x7Yo ()
	begin
	end
'''
		expect = '''Program([VarDecl(Id(k2), None, dynamic, Id(LY)), VarDecl(Id(Gt7X), ArrayType([0.68], StringType), None, NumLit(39.55)), FuncDecl(Id(J_y4), [VarDecl(Id(da), ArrayType([4.84, 81.48], StringType), None, None), VarDecl(Id(naE5), NumberType, None, None), VarDecl(Id(zPtP), ArrayType([25.11, 97.96], BoolType), None, None)], Return()), VarDecl(Id(H4cx), ArrayType([93.71, 87.85], StringType), None, None), FuncDecl(Id(x7Yo), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011575))

	def test_2153011576(self):
		input = '''
number mFx <- hAI
func e6Is (number GvN[61.4,35.46,90.19], string V0U[89.53], string Pd8H)	return
'''
		expect = '''Program([VarDecl(Id(mFx), NumberType, None, Id(hAI)), FuncDecl(Id(e6Is), [VarDecl(Id(GvN), ArrayType([61.4, 35.46, 90.19], NumberType), None, None), VarDecl(Id(V0U), ArrayType([89.53], StringType), None, None), VarDecl(Id(Pd8H), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011576))

	def test_2153011577(self):
		input = '''
func jn (number z8, string h8wq)
	return
var HWGj <- "OqWe"
number X16[93.39,81.76,85.86] <- 19.05
func x7 (bool D0an[69.78,9.07])	begin
		wa[R_, "v"] <- Z9B
	end

'''
		expect = '''Program([FuncDecl(Id(jn), [VarDecl(Id(z8), NumberType, None, None), VarDecl(Id(h8wq), StringType, None, None)], Return()), VarDecl(Id(HWGj), None, var, StringLit(OqWe)), VarDecl(Id(X16), ArrayType([93.39, 81.76, 85.86], NumberType), None, NumLit(19.05)), FuncDecl(Id(x7), [VarDecl(Id(D0an), ArrayType([69.78, 9.07], BoolType), None, None)], Block([AssignStmt(ArrayCell(Id(wa), [Id(R_), StringLit(v)]), Id(Z9B))]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011577))

	def test_2153011578(self):
		input = '''
string tsE
'''
		expect = '''Program([VarDecl(Id(tsE), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011578))

	def test_2153011579(self):
		input = '''
func qNak (number dyD6[60.94,68.3])	return

'''
		expect = '''Program([FuncDecl(Id(qNak), [VarDecl(Id(dyD6), ArrayType([60.94, 68.3], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011579))

	def test_2153011580(self):
		input = '''
number Lrq[13.9]
string dQ3I[44.45]
number dps[33.8]
bool AzM[4.45,54.18] <- 85.61
number l1[64.31,8.08,88.66] <- true
'''
		expect = '''Program([VarDecl(Id(Lrq), ArrayType([13.9], NumberType), None, None), VarDecl(Id(dQ3I), ArrayType([44.45], StringType), None, None), VarDecl(Id(dps), ArrayType([33.8], NumberType), None, None), VarDecl(Id(AzM), ArrayType([4.45, 54.18], BoolType), None, NumLit(85.61)), VarDecl(Id(l1), ArrayType([64.31, 8.08, 88.66], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011580))

	def test_2153011581(self):
		input = '''
string xX
string v4V6[51.23,73.23] <- TF
'''
		expect = '''Program([VarDecl(Id(xX), StringType, None, None), VarDecl(Id(v4V6), ArrayType([51.23, 73.23], StringType), None, Id(TF))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011581))

	def test_2153011582(self):
		input = '''
number ft71[68.01,42.58] <- DSn
string XVLM[13.45,52.55,54.49]
func Vb ()
	begin
		begin
			continue
		end
	end

func USz ()	return
func DaP (string sy)
	return "zQlax"

'''
		expect = '''Program([VarDecl(Id(ft71), ArrayType([68.01, 42.58], NumberType), None, Id(DSn)), VarDecl(Id(XVLM), ArrayType([13.45, 52.55, 54.49], StringType), None, None), FuncDecl(Id(Vb), [], Block([Block([Continue])])), FuncDecl(Id(USz), [], Return()), FuncDecl(Id(DaP), [VarDecl(Id(sy), StringType, None, None)], Return(StringLit(zQlax)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011582))

	def test_2153011583(self):
		input = '''
number qAzy
'''
		expect = '''Program([VarDecl(Id(qAzy), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011583))

	def test_2153011584(self):
		input = '''
string Bo[41.16,6.87]
func UuZ (string iqB7)	begin
	end

func nu (number Y9[36.59,83.51,19.81], string keNb, number me[78.47])	begin
		continue
	end

string eo6[64.58,75.11]
'''
		expect = '''Program([VarDecl(Id(Bo), ArrayType([41.16, 6.87], StringType), None, None), FuncDecl(Id(UuZ), [VarDecl(Id(iqB7), StringType, None, None)], Block([])), FuncDecl(Id(nu), [VarDecl(Id(Y9), ArrayType([36.59, 83.51, 19.81], NumberType), None, None), VarDecl(Id(keNb), StringType, None, None), VarDecl(Id(me), ArrayType([78.47], NumberType), None, None)], Block([Continue])), VarDecl(Id(eo6), ArrayType([64.58, 75.11], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011584))

	def test_2153011585(self):
		input = '''
func Y71 (bool h5, number zPNc[4.44,8.15])	begin
		begin
			if ("YPuDn") continue
			if (10.73)
			string G4Rs[5.66,87.21]
			if (true)
			dN(xTD)
			elif ("P") Qgu(vi)
			elif ("swas")
			var e2 <- false
		end
		break
		begin
		end
	end

number jML <- 17.86
'''
		expect = '''Program([FuncDecl(Id(Y71), [VarDecl(Id(h5), BoolType, None, None), VarDecl(Id(zPNc), ArrayType([4.44, 8.15], NumberType), None, None)], Block([Block([If((StringLit(YPuDn), Continue), [], None), If((NumLit(10.73), VarDecl(Id(G4Rs), ArrayType([5.66, 87.21], StringType), None, None)), [], None), If((BooleanLit(True), CallStmt(Id(dN), [Id(xTD)])), [(StringLit(P), CallStmt(Id(Qgu), [Id(vi)])), (StringLit(swas), VarDecl(Id(e2), None, var, BooleanLit(False)))], None)]), Break, Block([])])), VarDecl(Id(jML), NumberType, None, NumLit(17.86))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011585))

	def test_2153011586(self):
		input = '''
string hc <- "y"
func I15G ()
	begin
		continue
		if (true) UylB <- "LBz"
		elif (false)
		GDqL <- v451
		elif (27.71) PCtc <- GUMZ
		elif (70.78)
		dynamic b1 <- 80.97
		elif (87.74) begin
		end
		begin
			ur(38.22, "ObRUE", yf)
			IrG(false)
		end
	end

string rb[49.22]
func lSDg (number b1G, bool bIeN, number lM[32.3,20.81,12.25])
	begin
		break
	end

func JDC3 (string jJU[9.17,7.03], number xRh, string Cz)	begin
		begin
		end
		break
		return
	end
'''
		expect = '''Program([VarDecl(Id(hc), StringType, None, StringLit(y)), FuncDecl(Id(I15G), [], Block([Continue, If((BooleanLit(True), AssignStmt(Id(UylB), StringLit(LBz))), [(BooleanLit(False), AssignStmt(Id(GDqL), Id(v451))), (NumLit(27.71), AssignStmt(Id(PCtc), Id(GUMZ))), (NumLit(70.78), VarDecl(Id(b1), None, dynamic, NumLit(80.97))), (NumLit(87.74), Block([]))], None), Block([CallStmt(Id(ur), [NumLit(38.22), StringLit(ObRUE), Id(yf)]), CallStmt(Id(IrG), [BooleanLit(False)])])])), VarDecl(Id(rb), ArrayType([49.22], StringType), None, None), FuncDecl(Id(lSDg), [VarDecl(Id(b1G), NumberType, None, None), VarDecl(Id(bIeN), BoolType, None, None), VarDecl(Id(lM), ArrayType([32.3, 20.81, 12.25], NumberType), None, None)], Block([Break])), FuncDecl(Id(JDC3), [VarDecl(Id(jJU), ArrayType([9.17, 7.03], StringType), None, None), VarDecl(Id(xRh), NumberType, None, None), VarDecl(Id(Cz), StringType, None, None)], Block([Block([]), Break, Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011586))

	def test_2153011587(self):
		input = '''
func Vu1U (string qW[21.66,28.32,65.97])
	return kLA
bool qD <- r7iT
bool Awd <- 84.92
bool pfBL[40.48,29.64] <- "s"
var aO <- x9
'''
		expect = '''Program([FuncDecl(Id(Vu1U), [VarDecl(Id(qW), ArrayType([21.66, 28.32, 65.97], StringType), None, None)], Return(Id(kLA))), VarDecl(Id(qD), BoolType, None, Id(r7iT)), VarDecl(Id(Awd), BoolType, None, NumLit(84.92)), VarDecl(Id(pfBL), ArrayType([40.48, 29.64], BoolType), None, StringLit(s)), VarDecl(Id(aO), None, var, Id(x9))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011587))

	def test_2153011588(self):
		input = '''
string Oc[1.89,9.04,28.54]
func E1Yv ()
	begin
		begin
			c5I(false, Jkiv, false)
			if (aFE)
			for Nf until wDia by true
				iE(false, "p", 80.23)
			elif ("Pisu") string fr
			sl <- 97.09
		end
		KIsr(false, true, "cS")
	end

func Yq (string Wcpz, string zk, bool zsu)	return
'''
		expect = '''Program([VarDecl(Id(Oc), ArrayType([1.89, 9.04, 28.54], StringType), None, None), FuncDecl(Id(E1Yv), [], Block([Block([CallStmt(Id(c5I), [BooleanLit(False), Id(Jkiv), BooleanLit(False)]), If((Id(aFE), For(Id(Nf), Id(wDia), BooleanLit(True), CallStmt(Id(iE), [BooleanLit(False), StringLit(p), NumLit(80.23)]))), [(StringLit(Pisu), VarDecl(Id(fr), StringType, None, None))], None), AssignStmt(Id(sl), NumLit(97.09))]), CallStmt(Id(KIsr), [BooleanLit(False), BooleanLit(True), StringLit(cS)])])), FuncDecl(Id(Yq), [VarDecl(Id(Wcpz), StringType, None, None), VarDecl(Id(zk), StringType, None, None), VarDecl(Id(zsu), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011588))

	def test_2153011589(self):
		input = '''
func cibO (bool pZn7)	begin
	end

'''
		expect = '''Program([FuncDecl(Id(cibO), [VarDecl(Id(pZn7), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011589))

	def test_2153011590(self):
		input = '''
func rzSR (bool Q8P1, string bG[75.45], number ptA7)	begin
		break
		break
	end

func sF (number uVE9, string rqXt)	begin
		break
	end

bool Vd <- "aHx"
number TUo
func Bs ()
	return 5.55
'''
		expect = '''Program([FuncDecl(Id(rzSR), [VarDecl(Id(Q8P1), BoolType, None, None), VarDecl(Id(bG), ArrayType([75.45], StringType), None, None), VarDecl(Id(ptA7), NumberType, None, None)], Block([Break, Break])), FuncDecl(Id(sF), [VarDecl(Id(uVE9), NumberType, None, None), VarDecl(Id(rqXt), StringType, None, None)], Block([Break])), VarDecl(Id(Vd), BoolType, None, StringLit(aHx)), VarDecl(Id(TUo), NumberType, None, None), FuncDecl(Id(Bs), [], Return(NumLit(5.55)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011590))

	def test_2153011591(self):
		input = '''
string uV[46.55] <- melc
'''
		expect = '''Program([VarDecl(Id(uV), ArrayType([46.55], StringType), None, Id(melc))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011591))

	def test_2153011592(self):
		input = '''
func N2 ()
	begin
		if (true)
		return false
		elif (88.47) continue
		else return
		begin
			string w8L9[79.37] <- "Q"
			if (qd)
			break
			elif ("qOMF")
			for e6t7 until 43.76 by 22.72
				if (Y7p)
				pM9()
				elif (gC4q) string CB5[4.25,9.51] <- 14.88
				elif (E4) begin
					if ("RM") continue
					elif (true) break
					elif (false) break
					else begin
						ZZZ <- "wNuz"
						QIde <- A1at
						if (false)
						for iin until true by false
							continue
						elif ("hdm") number cA[92.69] <- 51.31
						elif (TSr6) break
						elif (a_) fSc <- 70.16
						elif ("Uyl")
						continue
						elif ("OACAh")
						if (87.13) continue
						elif (zoS)
						hE <- B8Z0
						elif (58.03)
						continue
					end
				end
				elif (98.85) zJ <- Db
				elif (R8V)
				break
				elif ("HMxRL") begin
					Fq(true)
					number Pv[96.78,12.55,22.73]
					continue
				end
				else begin
					for O_sT until false by 96.65
						for xc until "ZtW" by 0.21
							string ysQB[84.56,4.23,58.52] <- Et1V
				end
			elif ("ZWgX") return
			elif (39.71) Hiqa <- true
		end
	end

'''
		expect = '''Program([FuncDecl(Id(N2), [], Block([If((BooleanLit(True), Return(BooleanLit(False))), [(NumLit(88.47), Continue)], Return()), Block([VarDecl(Id(w8L9), ArrayType([79.37], StringType), None, StringLit(Q)), If((Id(qd), Break), [(StringLit(qOMF), For(Id(e6t7), NumLit(43.76), NumLit(22.72), If((Id(Y7p), CallStmt(Id(pM9), [])), [(Id(gC4q), VarDecl(Id(CB5), ArrayType([4.25, 9.51], StringType), None, NumLit(14.88))), (Id(E4), Block([If((StringLit(RM), Continue), [(BooleanLit(True), Break), (BooleanLit(False), Break)], Block([AssignStmt(Id(ZZZ), StringLit(wNuz)), AssignStmt(Id(QIde), Id(A1at)), If((BooleanLit(False), For(Id(iin), BooleanLit(True), BooleanLit(False), Continue)), [(StringLit(hdm), VarDecl(Id(cA), ArrayType([92.69], NumberType), None, NumLit(51.31))), (Id(TSr6), Break), (Id(a_), AssignStmt(Id(fSc), NumLit(70.16))), (StringLit(Uyl), Continue), (StringLit(OACAh), If((NumLit(87.13), Continue), [(Id(zoS), AssignStmt(Id(hE), Id(B8Z0))), (NumLit(58.03), Continue)], None))], None)]))])), (NumLit(98.85), AssignStmt(Id(zJ), Id(Db))), (Id(R8V), Break), (StringLit(HMxRL), Block([CallStmt(Id(Fq), [BooleanLit(True)]), VarDecl(Id(Pv), ArrayType([96.78, 12.55, 22.73], NumberType), None, None), Continue]))], Block([For(Id(O_sT), BooleanLit(False), NumLit(96.65), For(Id(xc), StringLit(ZtW), NumLit(0.21), VarDecl(Id(ysQB), ArrayType([84.56, 4.23, 58.52], StringType), None, Id(Et1V))))])))), (StringLit(ZWgX), Return()), (NumLit(39.71), AssignStmt(Id(Hiqa), BooleanLit(True)))], None)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011592))

	def test_2153011593(self):
		input = '''
string owk
number GoVK[86.26,41.24,20.03] <- true
'''
		expect = '''Program([VarDecl(Id(owk), StringType, None, None), VarDecl(Id(GoVK), ArrayType([86.26, 41.24, 20.03], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011593))

	def test_2153011594(self):
		input = '''
func oJjs (bool WNwn[20.13])
	return

func B96 (string EVf)
	return

func L6Mu (bool Rv, bool Xv[91.3,79.17], string LE2[90.27,1.51,40.5])	begin
		if (KCR)
		EHCf()
		elif (cVwI)
		continue
		break
	end
'''
		expect = '''Program([FuncDecl(Id(oJjs), [VarDecl(Id(WNwn), ArrayType([20.13], BoolType), None, None)], Return()), FuncDecl(Id(B96), [VarDecl(Id(EVf), StringType, None, None)], Return()), FuncDecl(Id(L6Mu), [VarDecl(Id(Rv), BoolType, None, None), VarDecl(Id(Xv), ArrayType([91.3, 79.17], BoolType), None, None), VarDecl(Id(LE2), ArrayType([90.27, 1.51, 40.5], StringType), None, None)], Block([If((Id(KCR), CallStmt(Id(EHCf), [])), [(Id(cVwI), Continue)], None), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011594))

	def test_2153011595(self):
		input = '''
func Hz3O ()	return false

number Ma
func zwKD ()	return
'''
		expect = '''Program([FuncDecl(Id(Hz3O), [], Return(BooleanLit(False))), VarDecl(Id(Ma), NumberType, None, None), FuncDecl(Id(zwKD), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011595))

	def test_2153011596(self):
		input = '''
func dH (string Y4[11.13,56.12,71.89], string CUSR[16.13,13.34])	begin
		break
		if (true) begin
		end
		continue
	end
'''
		expect = '''Program([FuncDecl(Id(dH), [VarDecl(Id(Y4), ArrayType([11.13, 56.12, 71.89], StringType), None, None), VarDecl(Id(CUSR), ArrayType([16.13, 13.34], StringType), None, None)], Block([Break, If((BooleanLit(True), Block([])), [], None), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011596))

	def test_2153011597(self):
		input = '''
func C3I (bool Dw, string UY[32.14,49.08,33.34])
	return

func Xid (number PGgE, string G4iE, number z_nd)	return

func bTpk (string aB)	begin
		return
	end

'''
		expect = '''Program([FuncDecl(Id(C3I), [VarDecl(Id(Dw), BoolType, None, None), VarDecl(Id(UY), ArrayType([32.14, 49.08, 33.34], StringType), None, None)], Return()), FuncDecl(Id(Xid), [VarDecl(Id(PGgE), NumberType, None, None), VarDecl(Id(G4iE), StringType, None, None), VarDecl(Id(z_nd), NumberType, None, None)], Return()), FuncDecl(Id(bTpk), [VarDecl(Id(aB), StringType, None, None)], Block([Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011597))

	def test_2153011598(self):
		input = '''
bool GNj[40.51]
func Ud (string Kbh[87.85], bool oY, number f5[89.98,87.86,62.21])	return 27.28

func BOHy (bool Gz[96.96,16.1,82.02])
	begin
	end

'''
		expect = '''Program([VarDecl(Id(GNj), ArrayType([40.51], BoolType), None, None), FuncDecl(Id(Ud), [VarDecl(Id(Kbh), ArrayType([87.85], StringType), None, None), VarDecl(Id(oY), BoolType, None, None), VarDecl(Id(f5), ArrayType([89.98, 87.86, 62.21], NumberType), None, None)], Return(NumLit(27.28))), FuncDecl(Id(BOHy), [VarDecl(Id(Gz), ArrayType([96.96, 16.1, 82.02], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011598))

	def test_2153011599(self):
		input = '''
dynamic Lh
func uta ()	begin
	end
func hou ()
	begin
		string tj[39.16] <- "JGPo"
		nC <- 10.73
		continue
	end

'''
		expect = '''Program([VarDecl(Id(Lh), None, dynamic, None), FuncDecl(Id(uta), [], Block([])), FuncDecl(Id(hou), [], Block([VarDecl(Id(tj), ArrayType([39.16], StringType), None, StringLit(JGPo)), AssignStmt(Id(nC), NumLit(10.73)), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011599))
