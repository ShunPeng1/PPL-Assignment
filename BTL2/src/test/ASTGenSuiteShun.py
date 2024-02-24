import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
	def test_2153011500(self):
		input = '''
func A7Sk (string YmcE[72.58])	return

var OK <- false + false
var Qw24 <- (KR("ynMU", j6P)[false])
'''
		expect = '''Program([FuncDecl(Id(A7Sk), [VarDecl(Id(YmcE), ArrayType([72.58], StringType), None, None)], Return()), VarDecl(Id(OK), None, var, BinaryOp(+, BooleanLit(False), BooleanLit(False))), VarDecl(Id(Qw24), None, var, ArrayCell(CallExpr(Id(KR), [StringLit(ynMU), Id(j6P)]), [BooleanLit(False)]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011500))

	def test_2153011501(self):
		input = '''
string XQ[62.37]
func Xrx (string BxsB[96.77])	return mrk

'''
		expect = '''Program([VarDecl(Id(XQ), ArrayType([62.37], StringType), None, None), FuncDecl(Id(Xrx), [VarDecl(Id(BxsB), ArrayType([96.77], StringType), None, None)], Return(Id(mrk)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011501))

	def test_2153011502(self):
		input = '''
bool GGD[88.21,19.61] <- true
func If8k ()	return 58.84
string Yru[41.23] <- true
var Z8p <- hz
func bOm (number Gtu[10.92,14.77,71.02], number T9b[55.58,64.63,95.09])	begin
	end
'''
		expect = '''Program([VarDecl(Id(GGD), ArrayType([88.21, 19.61], BoolType), None, BooleanLit(True)), FuncDecl(Id(If8k), [], Return(NumLit(58.84))), VarDecl(Id(Yru), ArrayType([41.23], StringType), None, BooleanLit(True)), VarDecl(Id(Z8p), None, var, Id(hz)), FuncDecl(Id(bOm), [VarDecl(Id(Gtu), ArrayType([10.92, 14.77, 71.02], NumberType), None, None), VarDecl(Id(T9b), ArrayType([55.58, 64.63, 95.09], NumberType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011502))

	def test_2153011503(self):
		input = '''
func og (number C1lG[90.57])	return "p"

func Hc8 (string EpP)	return true
string k_rR[89.54]
string twWg <- GM
'''
		expect = '''Program([FuncDecl(Id(og), [VarDecl(Id(C1lG), ArrayType([90.57], NumberType), None, None)], Return(StringLit(p))), FuncDecl(Id(Hc8), [VarDecl(Id(EpP), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(k_rR), ArrayType([89.54], StringType), None, None), VarDecl(Id(twWg), StringType, None, Id(GM))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011503))

	def test_2153011504(self):
		input = '''
number OKVP[35.41]
func CW (number uT[95.63,66.01], number k4Bh[27.68,73.03], number UTd[69.96,73.21])	begin
		continue
		if (false)
		Y4e[false, false] <- "vC"
		elif (false) QPr["YU", "ldBEZ", false] <- 32.13
		elif ("raR")
		for CI_Z until "VmOb" by j5ru
			cT()
		elif (jg)
		break
		elif (YUw9) begin
			return RUa2
			var D3a <- true
		end
		else var e2T <- "O"
	end
func J5 ()	return 21.31

func QZ7 (bool AM2[65.67], string qobf[52.43,40.81])	return "pzed"

'''
		expect = '''Program([VarDecl(Id(OKVP), ArrayType([35.41], NumberType), None, None), FuncDecl(Id(CW), [VarDecl(Id(uT), ArrayType([95.63, 66.01], NumberType), None, None), VarDecl(Id(k4Bh), ArrayType([27.68, 73.03], NumberType), None, None), VarDecl(Id(UTd), ArrayType([69.96, 73.21], NumberType), None, None)], Block([Continue, If(BooleanLit(False), AssignStmt(ArrayCell(Id(Y4e), [BooleanLit(False), BooleanLit(False)]), StringLit(vC))), [(BooleanLit(False), AssignStmt(ArrayCell(Id(QPr), [StringLit(YU), StringLit(ldBEZ), BooleanLit(False)]), NumLit(32.13))), (StringLit(raR), For(Id(CI_Z), StringLit(VmOb), Id(j5ru), CallStmt(Id(cT), []))), (Id(jg), Break), (Id(YUw9), Block([Return(Id(RUa2)), VarDecl(Id(D3a), None, var, BooleanLit(True))]))], VarDecl(Id(e2T), None, var, StringLit(O))])), FuncDecl(Id(J5), [], Return(NumLit(21.31))), FuncDecl(Id(QZ7), [VarDecl(Id(AM2), ArrayType([65.67], BoolType), None, None), VarDecl(Id(qobf), ArrayType([52.43, 40.81], StringType), None, None)], Return(StringLit(pzed)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011504))

	def test_2153011505(self):
		input = '''
func Q3 (bool Nr5, number qqqC[75.59,30.75], bool xT)	return
bool DzK[79.25,44.92] <- "McUh"
func zs (number FN8)
	return
func dRHo (number IqwC, number dy)
	return

'''
		expect = '''Program([FuncDecl(Id(Q3), [VarDecl(Id(Nr5), BoolType, None, None), VarDecl(Id(qqqC), ArrayType([75.59, 30.75], NumberType), None, None), VarDecl(Id(xT), BoolType, None, None)], Return()), VarDecl(Id(DzK), ArrayType([79.25, 44.92], BoolType), None, StringLit(McUh)), FuncDecl(Id(zs), [VarDecl(Id(FN8), NumberType, None, None)], Return()), FuncDecl(Id(dRHo), [VarDecl(Id(IqwC), NumberType, None, None), VarDecl(Id(dy), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011505))

	def test_2153011506(self):
		input = '''
string SL06[5.71,35.87] <- IY
number DHL
'''
		expect = '''Program([VarDecl(Id(SL06), ArrayType([5.71, 35.87], StringType), None, Id(IY)), VarDecl(Id(DHL), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011506))

	def test_2153011507(self):
		input = '''
func WiwF (string u6mM)
	return
'''
		expect = '''Program([FuncDecl(Id(WiwF), [VarDecl(Id(u6mM), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011507))

	def test_2153011508(self):
		input = '''
func NT (string gSkc)	return
string vpQP
string nW
var cG <- ey
number GdK
'''
		expect = '''Program([FuncDecl(Id(NT), [VarDecl(Id(gSkc), StringType, None, None)], Return()), VarDecl(Id(vpQP), StringType, None, None), VarDecl(Id(nW), StringType, None, None), VarDecl(Id(cG), None, var, Id(ey)), VarDecl(Id(GdK), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011508))

	def test_2153011509(self):
		input = '''
func QI8x (string mXJ[98.44,98.15], number zYo)	return

func uZ (bool Ag, string xwiN)	return 5.73
bool AcK <- 16.28
string cnNL[86.84,13.44,87.79]
var oKIm <- 96.36
'''
		expect = '''Program([FuncDecl(Id(QI8x), [VarDecl(Id(mXJ), ArrayType([98.44, 98.15], StringType), None, None), VarDecl(Id(zYo), NumberType, None, None)], Return()), FuncDecl(Id(uZ), [VarDecl(Id(Ag), BoolType, None, None), VarDecl(Id(xwiN), StringType, None, None)], Return(NumLit(5.73))), VarDecl(Id(AcK), BoolType, None, NumLit(16.28)), VarDecl(Id(cnNL), ArrayType([86.84, 13.44, 87.79], StringType), None, None), VarDecl(Id(oKIm), None, var, NumLit(96.36))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011509))

	def test_2153011510(self):
		input = '''
var LiH <- 78.95
func iP (bool MKq)
	return true

func Flq ()	return "vaw"
number bYvi <- 17.16
number RnE[32.56] <- "dRLPK"
'''
		expect = '''Program([VarDecl(Id(LiH), None, var, NumLit(78.95)), FuncDecl(Id(iP), [VarDecl(Id(MKq), BoolType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(Flq), [], Return(StringLit(vaw))), VarDecl(Id(bYvi), NumberType, None, NumLit(17.16)), VarDecl(Id(RnE), ArrayType([32.56], NumberType), None, StringLit(dRLPK))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011510))

	def test_2153011511(self):
		input = '''
string Ef1G[32.55] <- true
'''
		expect = '''Program([VarDecl(Id(Ef1G), ArrayType([32.55], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011511))

	def test_2153011512(self):
		input = '''
func iTO (string wr5V[71.93,60.48,43.93], string WQ[70.06,98.68], string LB)
	return

func n3 (number T3Z, bool tfm[73.52,84.43,11.32], string CUC[42.19])
	return

bool big[14.38,52.97]
'''
		expect = '''Program([FuncDecl(Id(iTO), [VarDecl(Id(wr5V), ArrayType([71.93, 60.48, 43.93], StringType), None, None), VarDecl(Id(WQ), ArrayType([70.06, 98.68], StringType), None, None), VarDecl(Id(LB), StringType, None, None)], Return()), FuncDecl(Id(n3), [VarDecl(Id(T3Z), NumberType, None, None), VarDecl(Id(tfm), ArrayType([73.52, 84.43, 11.32], BoolType), None, None), VarDecl(Id(CUC), ArrayType([42.19], StringType), None, None)], Return()), VarDecl(Id(big), ArrayType([14.38, 52.97], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011512))

	def test_2153011513(self):
		input = '''
string GXp <- "sVbKR"
func LWv (number yP7)
	begin
		number XFB
	end
string wmX <- "B"
number L_[13.51,97.42,76.11]
dynamic CU
'''
		expect = '''Program([VarDecl(Id(GXp), StringType, None, StringLit(sVbKR)), FuncDecl(Id(LWv), [VarDecl(Id(yP7), NumberType, None, None)], Block([VarDecl(Id(XFB), NumberType, None, None)])), VarDecl(Id(wmX), StringType, None, StringLit(B)), VarDecl(Id(L_), ArrayType([13.51, 97.42, 76.11], NumberType), None, None), VarDecl(Id(CU), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011513))

	def test_2153011514(self):
		input = '''
func gAm5 (bool We1, number buM9[0.36,60.37,98.43], number mwcM[77.88,96.54])
	return
var Sb <- 15.48
number Afx1[45.42] <- 17.39
'''
		expect = '''Program([FuncDecl(Id(gAm5), [VarDecl(Id(We1), BoolType, None, None), VarDecl(Id(buM9), ArrayType([0.36, 60.37, 98.43], NumberType), None, None), VarDecl(Id(mwcM), ArrayType([77.88, 96.54], NumberType), None, None)], Return()), VarDecl(Id(Sb), None, var, NumLit(15.48)), VarDecl(Id(Afx1), ArrayType([45.42], NumberType), None, NumLit(17.39))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011514))

	def test_2153011515(self):
		input = '''
func QnM8 (number THv9, string epaY)	return

func FncU (string fA3[20.72,39.6,33.55], string kuWo[99.76,86.27], string ho9[25.1,71.57])
	return false
func w2ek (bool Oi[3.95])
	return

func qp (string lD[29.87])
	return "beed"

bool V6[81.89,14.79] <- true
'''
		expect = '''Program([FuncDecl(Id(QnM8), [VarDecl(Id(THv9), NumberType, None, None), VarDecl(Id(epaY), StringType, None, None)], Return()), FuncDecl(Id(FncU), [VarDecl(Id(fA3), ArrayType([20.72, 39.6, 33.55], StringType), None, None), VarDecl(Id(kuWo), ArrayType([99.76, 86.27], StringType), None, None), VarDecl(Id(ho9), ArrayType([25.1, 71.57], StringType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(w2ek), [VarDecl(Id(Oi), ArrayType([3.95], BoolType), None, None)], Return()), FuncDecl(Id(qp), [VarDecl(Id(lD), ArrayType([29.87], StringType), None, None)], Return(StringLit(beed))), VarDecl(Id(V6), ArrayType([81.89, 14.79], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011515))

	def test_2153011516(self):
		input = '''
func JGxj (number K_, number WrmT[83.36], number a65)	begin
		if (true)
		if (MZa) for rf until "bxXti" by PIIB
			if ("tw") return 23.13
			elif (true) if (gSS5)
			if (24.66)
			begin
				if (false)
				string ul[77.47] <- "GEy"
				elif (false) continue
				elif ("JD")
				if (TkME) return
				else for QDTg until zZ by true
					break
				elif ("EYv")
				break
				elif (BLx)
				begin
					c3()
					if (73.85)
					break
					begin
						return
					end
				end
				elif (false) if ("nvJDr") begin
					fNd <- hYgw
				end
				else number Xp[45.42] <- 57.35
				continue
				continue
			end
			elif (false)
			return "mHUYp"
			elif (HB)
			bool Oty[87.49,84.25,61.37] <- iC
			elif (aTae)
			continue
			elif (true) begin
			end
			elif (cvFY)
			for QIpL until true by nA
				begin
					dynamic sq <- D4I
				end
			elif (true) for bR until H_kT by 29.35
				return
			elif (false)
			for oLxo until "S" by true
				return
			elif (TpA) aidj()
			elif (true)
			break
			else if (15.54)
			return
			elif (false) qt0S <- 0.13
			elif (Hx) continue
			else continue
			elif (29.43)
			if (false)
			K2Wz("ZFCGb", true, false)
			elif (true)
			x0(true, v5EA, 15.71)
			elif (true)
			number s7[35.67,19.56,19.92]
			else continue
			elif (VM) for Rc until gd7 by "V"
				ZCjN <- mcis
		elif (true) continue
		elif ("gUz") for oI_1 until "a" by true
			begin
			end
		elif (MxP) if ("apuT")
		KyPl <- r4dT
		elif (true)
		return false
		elif (23.11)
		begin
			gb["KIFla", vK, 23.82] <- true
			for B_g until "y" by "Mr"
				mC0I <- 20.19
			SJ(83.56)
		end
		elif (false)
		if ("OE") break
		else begin
			break
		end
		elif (94.11)
		return false
		elif ("ZtR") number wF <- 60.54
		return "tqG"
		begin
			begin
				return "GMyvm"
				begin
				end
			end
			jsXp[jJVF] <- false
		end
	end
'''
		expect = '''Program([FuncDecl(Id(JGxj), [VarDecl(Id(K_), NumberType, None, None), VarDecl(Id(WrmT), ArrayType([83.36], NumberType), None, None), VarDecl(Id(a65), NumberType, None, None)], Block([If(BooleanLit(True), If(Id(MZa), For(Id(rf), StringLit(bxXti), Id(PIIB), If(StringLit(tw), Return(NumLit(23.13))), [(BooleanLit(True), If(Id(gSS5), If(NumLit(24.66), Block([If(BooleanLit(False), VarDecl(Id(ul), ArrayType([77.47], StringType), None, StringLit(GEy))), [(BooleanLit(False), Continue), (StringLit(JD), If(Id(TkME), Return()), [], For(Id(QDTg), Id(zZ), BooleanLit(True), Break)), (StringLit(EYv), Break), (Id(BLx), Block([CallStmt(Id(c3), []), If(NumLit(73.85), Break), [], None, Block([Return()])])), (BooleanLit(False), If(StringLit(nvJDr), Block([AssignStmt(Id(fNd), Id(hYgw))])), [], VarDecl(Id(Xp), ArrayType([45.42], NumberType), None, NumLit(57.35)))], None, Continue, Continue])), [(BooleanLit(False), Return(StringLit(mHUYp))), (Id(HB), VarDecl(Id(Oty), ArrayType([87.49, 84.25, 61.37], BoolType), None, Id(iC))), (Id(aTae), Continue), (BooleanLit(True), Block([])), (Id(cvFY), For(Id(QIpL), BooleanLit(True), Id(nA), Block([VarDecl(Id(sq), None, dynamic, Id(D4I))]))), (BooleanLit(True), For(Id(bR), Id(H_kT), NumLit(29.35), Return())), (BooleanLit(False), For(Id(oLxo), StringLit(S), BooleanLit(True), Return())), (Id(TpA), CallStmt(Id(aidj), [])), (BooleanLit(True), Break)], If(NumLit(15.54), Return()), [(BooleanLit(False), AssignStmt(Id(qt0S), NumLit(0.13))), (Id(Hx), Continue)], Continue), [(NumLit(29.43), If(BooleanLit(False), CallStmt(Id(K2Wz), [StringLit(ZFCGb), BooleanLit(True), BooleanLit(False)])), [(BooleanLit(True), CallStmt(Id(x0), [BooleanLit(True), Id(v5EA), NumLit(15.71)])), (BooleanLit(True), VarDecl(Id(s7), ArrayType([35.67, 19.56, 19.92], NumberType), None, None))], Continue), (Id(VM), For(Id(Rc), Id(gd7), StringLit(V), AssignStmt(Id(ZCjN), Id(mcis)))), (BooleanLit(True), Continue), (StringLit(gUz), For(Id(oI_1), StringLit(a), BooleanLit(True), Block([]))), (Id(MxP), If(StringLit(apuT), AssignStmt(Id(KyPl), Id(r4dT))), [(BooleanLit(True), Return(BooleanLit(False))), (NumLit(23.11), Block([AssignStmt(ArrayCell(Id(gb), [StringLit(KIFla), Id(vK), NumLit(23.82)]), BooleanLit(True)), For(Id(B_g), StringLit(y), StringLit(Mr), AssignStmt(Id(mC0I), NumLit(20.19))), CallStmt(Id(SJ), [NumLit(83.56)])])), (BooleanLit(False), If(StringLit(OE), Break), [], Block([Break])), (NumLit(94.11), Return(BooleanLit(False))), (StringLit(ZtR), VarDecl(Id(wF), NumberType, None, NumLit(60.54)))], None)], None)], None)), [], None), [], None, Return(StringLit(tqG)), Block([Block([Return(StringLit(GMyvm)), Block([])]), AssignStmt(ArrayCell(Id(jsXp), [Id(jJVF)]), BooleanLit(False))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011516))

	def test_2153011517(self):
		input = '''
bool bBP1[3.64,95.56,14.45] <- false
func qVy (number JOf, number i4w[91.35,8.11,65.52], string Td9f)	return

'''
		expect = '''Program([VarDecl(Id(bBP1), ArrayType([3.64, 95.56, 14.45], BoolType), None, BooleanLit(False)), FuncDecl(Id(qVy), [VarDecl(Id(JOf), NumberType, None, None), VarDecl(Id(i4w), ArrayType([91.35, 8.11, 65.52], NumberType), None, None), VarDecl(Id(Td9f), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011517))

	def test_2153011518(self):
		input = '''
func DU0 ()
	begin
		break
		uRB <- "cpwn"
		Dj(99.69, Zv)
	end

bool Z3t[45.14,37.11,4.43] <- true
dynamic Hcu
bool z9X[90.66] <- false
number mF[1.87,72.41,89.74] <- 72.5
'''
		expect = '''Program([FuncDecl(Id(DU0), [], Block([Break, AssignStmt(Id(uRB), StringLit(cpwn)), CallStmt(Id(Dj), [NumLit(99.69), Id(Zv)])])), VarDecl(Id(Z3t), ArrayType([45.14, 37.11, 4.43], BoolType), None, BooleanLit(True)), VarDecl(Id(Hcu), None, dynamic, None), VarDecl(Id(z9X), ArrayType([90.66], BoolType), None, BooleanLit(False)), VarDecl(Id(mF), ArrayType([1.87, 72.41, 89.74], NumberType), None, NumLit(72.5))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011518))

	def test_2153011519(self):
		input = '''
dynamic p7 <- "N"
'''
		expect = '''Program([VarDecl(Id(p7), None, dynamic, StringLit(N))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011519))

	def test_2153011520(self):
		input = '''
bool dzh <- true
'''
		expect = '''Program([VarDecl(Id(dzh), BoolType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011520))

	def test_2153011521(self):
		input = '''
dynamic WwaC
string S2 <- 11.99
string BY7r <- 16.33
number W1k[43.36,69.08]
var sX <- h3ze
'''
		expect = '''Program([VarDecl(Id(WwaC), None, dynamic, None), VarDecl(Id(S2), StringType, None, NumLit(11.99)), VarDecl(Id(BY7r), StringType, None, NumLit(16.33)), VarDecl(Id(W1k), ArrayType([43.36, 69.08], NumberType), None, None), VarDecl(Id(sX), None, var, Id(h3ze))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011521))

	def test_2153011522(self):
		input = '''
func pq (bool a80, bool WU)
	return

'''
		expect = '''Program([FuncDecl(Id(pq), [VarDecl(Id(a80), BoolType, None, None), VarDecl(Id(WU), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011522))

	def test_2153011523(self):
		input = '''
string pL_w[77.44,34.88]
bool k6f[1.34] <- true
bool jJ
'''
		expect = '''Program([VarDecl(Id(pL_w), ArrayType([77.44, 34.88], StringType), None, None), VarDecl(Id(k6f), ArrayType([1.34], BoolType), None, BooleanLit(True)), VarDecl(Id(jJ), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011523))

	def test_2153011524(self):
		input = '''
func jl5j ()
	return 55.69
func eRZ (bool y6)
	return

func NP ()	begin
		bool af[72.49,74.89,6.19] <- "rMXr"
	end
'''
		expect = '''Program([FuncDecl(Id(jl5j), [], Return(NumLit(55.69))), FuncDecl(Id(eRZ), [VarDecl(Id(y6), BoolType, None, None)], Return()), FuncDecl(Id(NP), [], Block([VarDecl(Id(af), ArrayType([72.49, 74.89, 6.19], BoolType), None, StringLit(rMXr))]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011524))

	def test_2153011525(self):
		input = '''
bool cH[46.29,83.25,43.24]
func ToB (bool ZxWc[30.92,29.68,56.04], bool xAZP)	begin
		number u5xK[46.1] <- zqw
		break
	end

var Eu0 <- false
func a8vA ()	begin
		break
		xf[true, "KwtZ", 30.7] <- VDas
	end
number o5
'''
		expect = '''Program([VarDecl(Id(cH), ArrayType([46.29, 83.25, 43.24], BoolType), None, None), FuncDecl(Id(ToB), [VarDecl(Id(ZxWc), ArrayType([30.92, 29.68, 56.04], BoolType), None, None), VarDecl(Id(xAZP), BoolType, None, None)], Block([VarDecl(Id(u5xK), ArrayType([46.1], NumberType), None, Id(zqw)), Break])), VarDecl(Id(Eu0), None, var, BooleanLit(False)), FuncDecl(Id(a8vA), [], Block([Break, AssignStmt(ArrayCell(Id(xf), [BooleanLit(True), StringLit(KwtZ), NumLit(30.7)]), Id(VDas))])), VarDecl(Id(o5), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011525))

	def test_2153011526(self):
		input = '''
func rm (string IpCd[58.44,2.96], number on[1.58,36.72,74.3], string G5sN[3.71])	return "SGEWw"
func sUdo (number w7fF, bool dIBG[68.27,0.18,19.77], bool Sq)
	begin
		for S4 until tT by 63.81
			for OEk until 20.26 by false
				break
	end
'''
		expect = '''Program([FuncDecl(Id(rm), [VarDecl(Id(IpCd), ArrayType([58.44, 2.96], StringType), None, None), VarDecl(Id(on), ArrayType([1.58, 36.72, 74.3], NumberType), None, None), VarDecl(Id(G5sN), ArrayType([3.71], StringType), None, None)], Return(StringLit(SGEWw))), FuncDecl(Id(sUdo), [VarDecl(Id(w7fF), NumberType, None, None), VarDecl(Id(dIBG), ArrayType([68.27, 0.18, 19.77], BoolType), None, None), VarDecl(Id(Sq), BoolType, None, None)], Block([For(Id(S4), Id(tT), NumLit(63.81), For(Id(OEk), NumLit(20.26), BooleanLit(False), Break))]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011526))

	def test_2153011527(self):
		input = '''
number cVDq
number x842[94.43]
func IL (number ds[43.46,92.89,57.3])
	return

'''
		expect = '''Program([VarDecl(Id(cVDq), NumberType, None, None), VarDecl(Id(x842), ArrayType([94.43], NumberType), None, None), FuncDecl(Id(IL), [VarDecl(Id(ds), ArrayType([43.46, 92.89, 57.3], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011527))

	def test_2153011528(self):
		input = '''
func rV (bool v27, number vp[74.48,16.37])
	begin
	end
func qgjw (bool vjqH, number T4Z2[27.13])
	begin
		break
		continue
		for UE until false by true
			if (d0ZN)
			cRd <- 49.61
			elif (fh)
			if (51.85) for yu1g until true by H3
				return
			elif (false) begin
			end
			elif (false)
			if (63.64) if ("JEwZ") R87y <- true
			elif ("W")
			for QOR0 until "uo" by "G"
				begin
					string XH
					W_(lt, 45.11, 81.04)
				end
			elif (fNJ) continue
			elif (ICmz)
			return
			elif (fA)
			pEj(XF3O, 48.37)
			elif (34.49)
			return
			elif (false) bool p14d[26.2,61.25,41.12] <- false
			elif (true)
			if ("dzGW") return true
			elif (10.61) continue
			elif (59.85)
			string VUGf[93.09,68.35] <- 74.84
			elif ("pIpNS")
			break
			elif (0.56)
			if ("UOVQm") continue
			elif (yj) return
			elif ("MML") if (18.25)
			qUGU(B_)
			elif ("O") begin
				return true
				begin
					QfW("QBX")
				end
			end
			elif (true)
			if (true) break
			elif (90.23)
			break
			elif (74.54) return
			elif ("H")
			je6U(xfC, false, false)
			elif ("NllnN")
			for XRhC until 2.33 by "c"
				continue
			elif (50.32) break
			elif (46.52)
			number Eyy1[60.53,79.81,90.26] <- 87.62
			else return s1D
			elif (0.58)
			continue
			elif (33.96)
			continue
			elif (86.51)
			for jy until JiW by false
				for wt9 until true by NL
					break
			elif (true)
			if (i8e1) if (51.54) return NQ
			elif (true)
			continue
			elif (CV) return false
			elif (FEur) continue
			elif (true)
			if (true)
			if ("qeaTp") break
			elif (wo4W) return
			elif (Un) if (false)
			for S9 until false by 98.46
				continue
			else return 31.96
			elif (TyRp)
			break
			elif (cA)
			begin
				continue
			end
	end

number b0 <- e1QT
'''
		expect = '''Program([FuncDecl(Id(rV), [VarDecl(Id(v27), BoolType, None, None), VarDecl(Id(vp), ArrayType([74.48, 16.37], NumberType), None, None)], Block([])), FuncDecl(Id(qgjw), [VarDecl(Id(vjqH), BoolType, None, None), VarDecl(Id(T4Z2), ArrayType([27.13], NumberType), None, None)], Block([Break, Continue, For(Id(UE), BooleanLit(False), BooleanLit(True), If(Id(d0ZN), AssignStmt(Id(cRd), NumLit(49.61))), [(Id(fh), If(NumLit(51.85), For(Id(yu1g), BooleanLit(True), Id(H3), Return())), [(BooleanLit(False), Block([])), (BooleanLit(False), If(NumLit(63.64), If(StringLit(JEwZ), AssignStmt(Id(R87y), BooleanLit(True))), [(StringLit(W), For(Id(QOR0), StringLit(uo), StringLit(G), Block([VarDecl(Id(XH), StringType, None, None), CallStmt(Id(W_), [Id(lt), NumLit(45.11), NumLit(81.04)])]))), (Id(fNJ), Continue), (Id(ICmz), Return()), (Id(fA), CallStmt(Id(pEj), [Id(XF3O), NumLit(48.37)])), (NumLit(34.49), Return()), (BooleanLit(False), VarDecl(Id(p14d), ArrayType([26.2, 61.25, 41.12], BoolType), None, BooleanLit(False))), (BooleanLit(True), If(StringLit(dzGW), Return(BooleanLit(True))), [(NumLit(10.61), Continue), (NumLit(59.85), VarDecl(Id(VUGf), ArrayType([93.09, 68.35], StringType), None, NumLit(74.84))), (StringLit(pIpNS), Break), (NumLit(0.56), If(StringLit(UOVQm), Continue), [(Id(yj), Return()), (StringLit(MML), If(NumLit(18.25), CallStmt(Id(qUGU), [Id(B_)])), [(StringLit(O), Block([Return(BooleanLit(True)), Block([CallStmt(Id(QfW), [StringLit(QBX)])])])), (BooleanLit(True), If(BooleanLit(True), Break), [(NumLit(90.23), Break), (NumLit(74.54), Return()), (StringLit(H), CallStmt(Id(je6U), [Id(xfC), BooleanLit(False), BooleanLit(False)])), (StringLit(NllnN), For(Id(XRhC), NumLit(2.33), StringLit(c), Continue)), (NumLit(50.32), Break), (NumLit(46.52), VarDecl(Id(Eyy1), ArrayType([60.53, 79.81, 90.26], NumberType), None, NumLit(87.62)))], Return(Id(s1D))), (NumLit(0.58), Continue), (NumLit(33.96), Continue), (NumLit(86.51), For(Id(jy), Id(JiW), BooleanLit(False), For(Id(wt9), BooleanLit(True), Id(NL), Break))), (BooleanLit(True), If(Id(i8e1), If(NumLit(51.54), Return(Id(NQ))), [(BooleanLit(True), Continue), (Id(CV), Return(BooleanLit(False))), (Id(FEur), Continue), (BooleanLit(True), If(BooleanLit(True), If(StringLit(qeaTp), Break), [(Id(wo4W), Return()), (Id(Un), If(BooleanLit(False), For(Id(S9), BooleanLit(False), NumLit(98.46), Continue)), [], Return(NumLit(31.96))), (Id(TyRp), Break), (Id(cA), Block([Continue]))], None), [], None)], None), [], None)], None)], None)], None)], None), [], None)], None)], None)])), VarDecl(Id(b0), NumberType, None, Id(e1QT))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011528))

	def test_2153011529(self):
		input = '''
func cN (string Hco, number zem, number tj8T[99.02,31.79])	return "U"
func kqBI (bool URu, number ZY4)
	return

string pnL[26.39,33.7,64.86]
func nnCa (number T7B[30.11,27.25], bool M8, bool U9y[27.47])	begin
	end

'''
		expect = '''Program([FuncDecl(Id(cN), [VarDecl(Id(Hco), StringType, None, None), VarDecl(Id(zem), NumberType, None, None), VarDecl(Id(tj8T), ArrayType([99.02, 31.79], NumberType), None, None)], Return(StringLit(U))), FuncDecl(Id(kqBI), [VarDecl(Id(URu), BoolType, None, None), VarDecl(Id(ZY4), NumberType, None, None)], Return()), VarDecl(Id(pnL), ArrayType([26.39, 33.7, 64.86], StringType), None, None), FuncDecl(Id(nnCa), [VarDecl(Id(T7B), ArrayType([30.11, 27.25], NumberType), None, None), VarDecl(Id(M8), BoolType, None, None), VarDecl(Id(U9y), ArrayType([27.47], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011529))

	def test_2153011530(self):
		input = '''
number hCM[79.72]
func wLkA (number mp)
	begin
		continue
		return
		QS(dh)
	end

func lM (number wMgl[73.55,95.1,11.97], bool QV[16.4,30.45,88.54], bool fUT[91.09,22.84,94.53])
	return
func gDxR ()
	return true
'''
		expect = '''Program([VarDecl(Id(hCM), ArrayType([79.72], NumberType), None, None), FuncDecl(Id(wLkA), [VarDecl(Id(mp), NumberType, None, None)], Block([Continue, Return(), CallStmt(Id(QS), [Id(dh)])])), FuncDecl(Id(lM), [VarDecl(Id(wMgl), ArrayType([73.55, 95.1, 11.97], NumberType), None, None), VarDecl(Id(QV), ArrayType([16.4, 30.45, 88.54], BoolType), None, None), VarDecl(Id(fUT), ArrayType([91.09, 22.84, 94.53], BoolType), None, None)], Return()), FuncDecl(Id(gDxR), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011530))

	def test_2153011531(self):
		input = '''
number oydE[67.68,23.6]
var bP <- uW
func nY (number YcZ, bool HH[28.85])	return true

'''
		expect = '''Program([VarDecl(Id(oydE), ArrayType([67.68, 23.6], NumberType), None, None), VarDecl(Id(bP), None, var, Id(uW)), FuncDecl(Id(nY), [VarDecl(Id(YcZ), NumberType, None, None), VarDecl(Id(HH), ArrayType([28.85], BoolType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011531))

	def test_2153011532(self):
		input = '''
dynamic GN
'''
		expect = '''Program([VarDecl(Id(GN), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011532))

	def test_2153011533(self):
		input = '''
func IKGp ()	begin
		break
	end

bool CPj1 <- vMkB
'''
		expect = '''Program([FuncDecl(Id(IKGp), [], Block([Break])), VarDecl(Id(CPj1), BoolType, None, Id(vMkB))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011533))

	def test_2153011534(self):
		input = '''
func ouQ (string a6[66.94], number OD)
	begin
		continue
		break
		Ha9u <- 64.3
	end
number Hd9 <- ro
number pt[76.02]
func yRvT (string fq[40.21,92.91,78.42], number gl, bool Knis)	return

'''
		expect = '''Program([FuncDecl(Id(ouQ), [VarDecl(Id(a6), ArrayType([66.94], StringType), None, None), VarDecl(Id(OD), NumberType, None, None)], Block([Continue, Break, AssignStmt(Id(Ha9u), NumLit(64.3))])), VarDecl(Id(Hd9), NumberType, None, Id(ro)), VarDecl(Id(pt), ArrayType([76.02], NumberType), None, None), FuncDecl(Id(yRvT), [VarDecl(Id(fq), ArrayType([40.21, 92.91, 78.42], StringType), None, None), VarDecl(Id(gl), NumberType, None, None), VarDecl(Id(Knis), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011534))

	def test_2153011535(self):
		input = '''
func Tgv (bool vd)
	begin
		for w_ until 63.61 by "sAk"
			a3o()
	end

'''
		expect = '''Program([FuncDecl(Id(Tgv), [VarDecl(Id(vd), BoolType, None, None)], Block([For(Id(w_), NumLit(63.61), StringLit(sAk), CallStmt(Id(a3o), []))]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011535))

	def test_2153011536(self):
		input = '''
dynamic jNw5 <- false
func Nynw (bool VQLH, number dOx_[58.0,83.77,36.37])
	begin
		break
		begin
			continue
			IsA()
			number C7 <- false
		end
		return
	end
string Y_R7[9.41] <- mTtJ
number ku
number Lm70 <- bzaw
'''
		expect = '''Program([VarDecl(Id(jNw5), None, dynamic, BooleanLit(False)), FuncDecl(Id(Nynw), [VarDecl(Id(VQLH), BoolType, None, None), VarDecl(Id(dOx_), ArrayType([58.0, 83.77, 36.37], NumberType), None, None)], Block([Break, Block([Continue, CallStmt(Id(IsA), []), VarDecl(Id(C7), NumberType, None, BooleanLit(False))]), Return()])), VarDecl(Id(Y_R7), ArrayType([9.41], StringType), None, Id(mTtJ)), VarDecl(Id(ku), NumberType, None, None), VarDecl(Id(Lm70), NumberType, None, Id(bzaw))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011536))

	def test_2153011537(self):
		input = '''
bool pJ[38.71] <- true
bool ID[56.15,50.54]
'''
		expect = '''Program([VarDecl(Id(pJ), ArrayType([38.71], BoolType), None, BooleanLit(True)), VarDecl(Id(ID), ArrayType([56.15, 50.54], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011537))

	def test_2153011538(self):
		input = '''
string xEZ[52.19,39.66,77.37]
'''
		expect = '''Program([VarDecl(Id(xEZ), ArrayType([52.19, 39.66, 77.37], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011538))

	def test_2153011539(self):
		input = '''
func vihd (number Gq0j[30.25,29.33,36.07], string Y0n, number M223[75.83,26.31,85.32])
	return
func TPY (number i6, string yDI_, bool nvea[36.94])	begin
		for YyAV until tN by "IumQ"
			return
		gs <- true
	end
bool IJs0[17.74] <- Gb4q
'''
		expect = '''Program([FuncDecl(Id(vihd), [VarDecl(Id(Gq0j), ArrayType([30.25, 29.33, 36.07], NumberType), None, None), VarDecl(Id(Y0n), StringType, None, None), VarDecl(Id(M223), ArrayType([75.83, 26.31, 85.32], NumberType), None, None)], Return()), FuncDecl(Id(TPY), [VarDecl(Id(i6), NumberType, None, None), VarDecl(Id(yDI_), StringType, None, None), VarDecl(Id(nvea), ArrayType([36.94], BoolType), None, None)], Block([For(Id(YyAV), Id(tN), StringLit(IumQ), Return()), AssignStmt(Id(gs), BooleanLit(True))])), VarDecl(Id(IJs0), ArrayType([17.74], BoolType), None, Id(Gb4q))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011539))

	def test_2153011540(self):
		input = '''
var e9 <- ysY
func GTM (number ejn[21.08,50.23,32.99], string JU5[3.7,79.1])
	return

number TI <- true
var Ofs <- "ucUWi"
'''
		expect = '''Program([VarDecl(Id(e9), None, var, Id(ysY)), FuncDecl(Id(GTM), [VarDecl(Id(ejn), ArrayType([21.08, 50.23, 32.99], NumberType), None, None), VarDecl(Id(JU5), ArrayType([3.7, 79.1], StringType), None, None)], Return()), VarDecl(Id(TI), NumberType, None, BooleanLit(True)), VarDecl(Id(Ofs), None, var, StringLit(ucUWi))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011540))

	def test_2153011541(self):
		input = '''
func CF ()
	begin
		if (91.83) continue
		elif (FY3A)
		bool pku[7.25,17.21,33.31] <- false
	end

'''
		expect = '''Program([FuncDecl(Id(CF), [], Block([If(NumLit(91.83), Continue), [(Id(FY3A), VarDecl(Id(pku), ArrayType([7.25, 17.21, 33.31], BoolType), None, BooleanLit(False)))], None]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011541))

	def test_2153011542(self):
		input = '''
bool bPrT <- q7
bool qw[23.21,61.3,56.0] <- Xh1
string bT <- false
string YES[82.52,82.85] <- false
'''
		expect = '''Program([VarDecl(Id(bPrT), BoolType, None, Id(q7)), VarDecl(Id(qw), ArrayType([23.21, 61.3, 56.0], BoolType), None, Id(Xh1)), VarDecl(Id(bT), StringType, None, BooleanLit(False)), VarDecl(Id(YES), ArrayType([82.52, 82.85], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011542))

	def test_2153011543(self):
		input = '''
var eRyC <- 94.01
bool NSz
func F4 ()	return 81.25

func uOSP (number jMa[32.18,45.65], number EHG, number v6dk[90.09,21.42])	begin
	end
dynamic ed23 <- 96.92
'''
		expect = '''Program([VarDecl(Id(eRyC), None, var, NumLit(94.01)), VarDecl(Id(NSz), BoolType, None, None), FuncDecl(Id(F4), [], Return(NumLit(81.25))), FuncDecl(Id(uOSP), [VarDecl(Id(jMa), ArrayType([32.18, 45.65], NumberType), None, None), VarDecl(Id(EHG), NumberType, None, None), VarDecl(Id(v6dk), ArrayType([90.09, 21.42], NumberType), None, None)], Block([])), VarDecl(Id(ed23), None, dynamic, NumLit(96.92))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011543))

	def test_2153011544(self):
		input = '''
func aX (number KD[2.73,0.19], number b3ZS)	begin
		begin
			Fkl <- EXjr
			He(false, "pxGv")
			ED <- 91.22
		end
		ZyZ[75.77, nF1] <- yVaz
		return
	end
'''
		expect = '''Program([FuncDecl(Id(aX), [VarDecl(Id(KD), ArrayType([2.73, 0.19], NumberType), None, None), VarDecl(Id(b3ZS), NumberType, None, None)], Block([Block([AssignStmt(Id(Fkl), Id(EXjr)), CallStmt(Id(He), [BooleanLit(False), StringLit(pxGv)]), AssignStmt(Id(ED), NumLit(91.22))]), AssignStmt(ArrayCell(Id(ZyZ), [NumLit(75.77), Id(nF1)]), Id(yVaz)), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011544))

	def test_2153011545(self):
		input = '''
string rO <- "tXD"
string m2[66.74] <- false
bool CGtj <- vc
'''
		expect = '''Program([VarDecl(Id(rO), StringType, None, StringLit(tXD)), VarDecl(Id(m2), ArrayType([66.74], StringType), None, BooleanLit(False)), VarDecl(Id(CGtj), BoolType, None, Id(vc))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011545))

	def test_2153011546(self):
		input = '''
string x35 <- 11.63
'''
		expect = '''Program([VarDecl(Id(x35), StringType, None, NumLit(11.63))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011546))

	def test_2153011547(self):
		input = '''
func oBk (string RR, bool wG7m[54.38,29.88])
	return

string sE6[4.99,42.56]
string wTHJ[66.0]
dynamic pW <- u_Q
func X8t ()
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(oBk), [VarDecl(Id(RR), StringType, None, None), VarDecl(Id(wG7m), ArrayType([54.38, 29.88], BoolType), None, None)], Return()), VarDecl(Id(sE6), ArrayType([4.99, 42.56], StringType), None, None), VarDecl(Id(wTHJ), ArrayType([66.0], StringType), None, None), VarDecl(Id(pW), None, dynamic, Id(u_Q)), FuncDecl(Id(X8t), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011547))

	def test_2153011548(self):
		input = '''
func Cq (string pCN[22.38], bool oGD, bool B3sh[47.69,90.82,17.48])
	return false

bool sdn[65.2]
'''
		expect = '''Program([FuncDecl(Id(Cq), [VarDecl(Id(pCN), ArrayType([22.38], StringType), None, None), VarDecl(Id(oGD), BoolType, None, None), VarDecl(Id(B3sh), ArrayType([47.69, 90.82, 17.48], BoolType), None, None)], Return(BooleanLit(False))), VarDecl(Id(sdn), ArrayType([65.2], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011548))

	def test_2153011549(self):
		input = '''
bool jSJ[2.1] <- 98.69
'''
		expect = '''Program([VarDecl(Id(jSJ), ArrayType([2.1], BoolType), None, NumLit(98.69))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011549))

	def test_2153011550(self):
		input = '''
bool uUOR[35.81,75.34,35.68] <- e7K
func bxnt (number wP[99.19])
	begin
		return true
		if (false)
		if (NgN4) begin
			SqC()
			continue
		end
		elif ("jwKC")
		return 47.92
		elif (true)
		break
		elif (true)
		Ul7[oR, 56.97, 98.74] <- 92.94
		elif (wduN) if ("TxWD")
		continue
		elif (true) for eMI until vHm by "YiA"
			begin
				UE <- true
			end
		return "S"
	end

func fKfa (bool man)
	return false

func cxwW (string BI0[14.88], string lv[97.33,85.84], bool yrNn[59.89])
	begin
		if ("b") begin
			eB8B()
			for J_6J until "WllY" by "nHsVk"
				return
		end
		elif (iXn)
		for SK until "trVI" by false
			I4()
		elif ("I")
		TLZ4("Vd", 78.43, false)
		elif (0.31)
		break
		else begin
		end
		for Pk until 5.78 by KO
			if (true) continue
			elif (vQI0)
			Xjs0 <- "GXXZ"
			elif ("ozSG")
			return
	end

func kWDE (bool dC0e[24.39,11.44])	return

'''
		expect = '''Program([VarDecl(Id(uUOR), ArrayType([35.81, 75.34, 35.68], BoolType), None, Id(e7K)), FuncDecl(Id(bxnt), [VarDecl(Id(wP), ArrayType([99.19], NumberType), None, None)], Block([Return(BooleanLit(True)), If(BooleanLit(False), If(Id(NgN4), Block([CallStmt(Id(SqC), []), Continue])), [(StringLit(jwKC), Return(NumLit(47.92))), (BooleanLit(True), Break), (BooleanLit(True), AssignStmt(ArrayCell(Id(Ul7), [Id(oR), NumLit(56.97), NumLit(98.74)]), NumLit(92.94))), (Id(wduN), If(StringLit(TxWD), Continue), [(BooleanLit(True), For(Id(eMI), Id(vHm), StringLit(YiA), Block([AssignStmt(Id(UE), BooleanLit(True))])))], None)], None), [], None, Return(StringLit(S))])), FuncDecl(Id(fKfa), [VarDecl(Id(man), BoolType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(cxwW), [VarDecl(Id(BI0), ArrayType([14.88], StringType), None, None), VarDecl(Id(lv), ArrayType([97.33, 85.84], StringType), None, None), VarDecl(Id(yrNn), ArrayType([59.89], BoolType), None, None)], Block([If(StringLit(b), Block([CallStmt(Id(eB8B), []), For(Id(J_6J), StringLit(WllY), StringLit(nHsVk), Return())])), [(Id(iXn), For(Id(SK), StringLit(trVI), BooleanLit(False), CallStmt(Id(I4), []))), (StringLit(I), CallStmt(Id(TLZ4), [StringLit(Vd), NumLit(78.43), BooleanLit(False)])), (NumLit(0.31), Break)], Block([]), For(Id(Pk), NumLit(5.78), Id(KO), If(BooleanLit(True), Continue), [(Id(vQI0), AssignStmt(Id(Xjs0), StringLit(GXXZ))), (StringLit(ozSG), Return())], None)])), FuncDecl(Id(kWDE), [VarDecl(Id(dC0e), ArrayType([24.39, 11.44], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011550))

	def test_2153011551(self):
		input = '''
func csn (bool i9)	return "Gnl"

string Ru[93.75]
'''
		expect = '''Program([FuncDecl(Id(csn), [VarDecl(Id(i9), BoolType, None, None)], Return(StringLit(Gnl))), VarDecl(Id(Ru), ArrayType([93.75], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011551))

	def test_2153011552(self):
		input = '''
func wh ()
	begin
		begin
		end
		for wK until false by "Lizv"
			wc["G"] <- 8.04
	end

string Tnq <- "io"
func HO (number Ve)	return Po2k

bool ZzU9[1.49,29.88,54.77]
dynamic UtUh
'''
		expect = '''Program([FuncDecl(Id(wh), [], Block([Block([]), For(Id(wK), BooleanLit(False), StringLit(Lizv), AssignStmt(ArrayCell(Id(wc), [StringLit(G)]), NumLit(8.04)))])), VarDecl(Id(Tnq), StringType, None, StringLit(io)), FuncDecl(Id(HO), [VarDecl(Id(Ve), NumberType, None, None)], Return(Id(Po2k))), VarDecl(Id(ZzU9), ArrayType([1.49, 29.88, 54.77], BoolType), None, None), VarDecl(Id(UtUh), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011552))

	def test_2153011553(self):
		input = '''
string u3[52.26,48.82,90.19]
'''
		expect = '''Program([VarDecl(Id(u3), ArrayType([52.26, 48.82, 90.19], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011553))

	def test_2153011554(self):
		input = '''
func mM9w (bool Td, number joK[16.65,47.01], bool ut)
	begin
		EsCP <- 12.09
		bool gELW[36.29,59.15,47.69] <- y329
		return "Al"
	end
func PB (string FP4, number xY)	return
number nN
func abx (string LJ, string fI, bool Cp2)	begin
		break
		string CH[43.99,41.3] <- M9B
		number q8IU[96.47,10.28,77.52]
	end
bool gIbB[83.77] <- true
'''
		expect = '''Program([FuncDecl(Id(mM9w), [VarDecl(Id(Td), BoolType, None, None), VarDecl(Id(joK), ArrayType([16.65, 47.01], NumberType), None, None), VarDecl(Id(ut), BoolType, None, None)], Block([AssignStmt(Id(EsCP), NumLit(12.09)), VarDecl(Id(gELW), ArrayType([36.29, 59.15, 47.69], BoolType), None, Id(y329)), Return(StringLit(Al))])), FuncDecl(Id(PB), [VarDecl(Id(FP4), StringType, None, None), VarDecl(Id(xY), NumberType, None, None)], Return()), VarDecl(Id(nN), NumberType, None, None), FuncDecl(Id(abx), [VarDecl(Id(LJ), StringType, None, None), VarDecl(Id(fI), StringType, None, None), VarDecl(Id(Cp2), BoolType, None, None)], Block([Break, VarDecl(Id(CH), ArrayType([43.99, 41.3], StringType), None, Id(M9B)), VarDecl(Id(q8IU), ArrayType([96.47, 10.28, 77.52], NumberType), None, None)])), VarDecl(Id(gIbB), ArrayType([83.77], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011554))

	def test_2153011555(self):
		input = '''
string faa
func f7 (string K6sL, bool nHBU[58.9,0.53])	return 9.74

func n1mY (number CHs[54.82], bool A4L4)
	begin
		KhAw(ZG_, dH)
	end
'''
		expect = '''Program([VarDecl(Id(faa), StringType, None, None), FuncDecl(Id(f7), [VarDecl(Id(K6sL), StringType, None, None), VarDecl(Id(nHBU), ArrayType([58.9, 0.53], BoolType), None, None)], Return(NumLit(9.74))), FuncDecl(Id(n1mY), [VarDecl(Id(CHs), ArrayType([54.82], NumberType), None, None), VarDecl(Id(A4L4), BoolType, None, None)], Block([CallStmt(Id(KhAw), [Id(ZG_), Id(dH)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011555))

	def test_2153011556(self):
		input = '''
func efl1 (bool PQ, string fP, bool L8X3[5.71])	return

bool b6[74.98]
number ze <- true
func VnR (number Vd, number UbX[96.17,38.15,83.12], number EQ3)
	return

'''
		expect = '''Program([FuncDecl(Id(efl1), [VarDecl(Id(PQ), BoolType, None, None), VarDecl(Id(fP), StringType, None, None), VarDecl(Id(L8X3), ArrayType([5.71], BoolType), None, None)], Return()), VarDecl(Id(b6), ArrayType([74.98], BoolType), None, None), VarDecl(Id(ze), NumberType, None, BooleanLit(True)), FuncDecl(Id(VnR), [VarDecl(Id(Vd), NumberType, None, None), VarDecl(Id(UbX), ArrayType([96.17, 38.15, 83.12], NumberType), None, None), VarDecl(Id(EQ3), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011556))

	def test_2153011557(self):
		input = '''
func sd (number uVV[8.63,71.83,90.03])	begin
	end

'''
		expect = '''Program([FuncDecl(Id(sd), [VarDecl(Id(uVV), ArrayType([8.63, 71.83, 90.03], NumberType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011557))

	def test_2153011558(self):
		input = '''
number M605 <- DJ
func xq_ (number RsO[55.99,88.9], number ddPF[80.06])
	return
bool xas[37.07,52.38,36.11] <- F8XC
'''
		expect = '''Program([VarDecl(Id(M605), NumberType, None, Id(DJ)), FuncDecl(Id(xq_), [VarDecl(Id(RsO), ArrayType([55.99, 88.9], NumberType), None, None), VarDecl(Id(ddPF), ArrayType([80.06], NumberType), None, None)], Return()), VarDecl(Id(xas), ArrayType([37.07, 52.38, 36.11], BoolType), None, Id(F8XC))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011558))

	def test_2153011559(self):
		input = '''
func BM (number vc[31.36], number ry[99.08], string GzDz[13.76,6.24,95.57])
	return

func oNGA ()	begin
		for g9f until 97.75 by 15.12
			if (false)
			break
			elif ("PF")
			if (15.74) continue
			elif (vwo)
			begin
				bool fc[86.82,1.7,48.96] <- c3P7
			end
			elif ("ZE") return
			elif (27.36) return
			else Obn2()
			else continue
	end
number q9TH <- bN
'''
		expect = '''Program([FuncDecl(Id(BM), [VarDecl(Id(vc), ArrayType([31.36], NumberType), None, None), VarDecl(Id(ry), ArrayType([99.08], NumberType), None, None), VarDecl(Id(GzDz), ArrayType([13.76, 6.24, 95.57], StringType), None, None)], Return()), FuncDecl(Id(oNGA), [], Block([For(Id(g9f), NumLit(97.75), NumLit(15.12), If(BooleanLit(False), Break), [(StringLit(PF), If(NumLit(15.74), Continue), [(Id(vwo), Block([VarDecl(Id(fc), ArrayType([86.82, 1.7, 48.96], BoolType), None, Id(c3P7))])), (StringLit(ZE), Return()), (NumLit(27.36), Return())], CallStmt(Id(Obn2), []))], Continue)])), VarDecl(Id(q9TH), NumberType, None, Id(bN))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011559))

	def test_2153011560(self):
		input = '''
func VgA (number DoW9)	return
string wcQ <- 19.06
func tlhx (number awt[11.86,54.0,49.58])
	return

'''
		expect = '''Program([FuncDecl(Id(VgA), [VarDecl(Id(DoW9), NumberType, None, None)], Return()), VarDecl(Id(wcQ), StringType, None, NumLit(19.06)), FuncDecl(Id(tlhx), [VarDecl(Id(awt), ArrayType([11.86, 54.0, 49.58], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011560))

	def test_2153011561(self):
		input = '''
func Pdl ()
	return

string Pv[5.17,96.74,37.68]
string Pktu[75.1] <- zt
'''
		expect = '''Program([FuncDecl(Id(Pdl), [], Return()), VarDecl(Id(Pv), ArrayType([5.17, 96.74, 37.68], StringType), None, None), VarDecl(Id(Pktu), ArrayType([75.1], StringType), None, Id(zt))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011561))

	def test_2153011562(self):
		input = '''
bool kk
func Z4Q (number Y1RL, string JxeU)	return
func w77I (number qrN)
	begin
	end

'''
		expect = '''Program([VarDecl(Id(kk), BoolType, None, None), FuncDecl(Id(Z4Q), [VarDecl(Id(Y1RL), NumberType, None, None), VarDecl(Id(JxeU), StringType, None, None)], Return()), FuncDecl(Id(w77I), [VarDecl(Id(qrN), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011562))

	def test_2153011563(self):
		input = '''
bool YT <- 23.14
dynamic Qxbu
var oPN <- 73.74
'''
		expect = '''Program([VarDecl(Id(YT), BoolType, None, NumLit(23.14)), VarDecl(Id(Qxbu), None, dynamic, None), VarDecl(Id(oPN), None, var, NumLit(73.74))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011563))

	def test_2153011564(self):
		input = '''
func y5c (string msvt[97.66], bool Wcs)
	return Mf
func UUp9 (string oEc[16.0], number sTl1[81.9,35.82], bool Ou)
	begin
		OWT5["qVt"] <- 8.22
		continue
	end

string U3X[26.82,67.46,80.43]
bool Ij
'''
		expect = '''Program([FuncDecl(Id(y5c), [VarDecl(Id(msvt), ArrayType([97.66], StringType), None, None), VarDecl(Id(Wcs), BoolType, None, None)], Return(Id(Mf))), FuncDecl(Id(UUp9), [VarDecl(Id(oEc), ArrayType([16.0], StringType), None, None), VarDecl(Id(sTl1), ArrayType([81.9, 35.82], NumberType), None, None), VarDecl(Id(Ou), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(OWT5), [StringLit(qVt)]), NumLit(8.22)), Continue])), VarDecl(Id(U3X), ArrayType([26.82, 67.46, 80.43], StringType), None, None), VarDecl(Id(Ij), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011564))

	def test_2153011565(self):
		input = '''
func WJt (bool aw[27.99,49.09], string PsY[56.98], string CkGE)	return "i"
func oUK ()	return

string Ple[77.06,36.08,58.61] <- "PLL"
func Kf (string v0, string ym[71.13])	begin
		for aEbg until false by false
			G6i["UbuX"] <- 80.17
	end

'''
		expect = '''Program([FuncDecl(Id(WJt), [VarDecl(Id(aw), ArrayType([27.99, 49.09], BoolType), None, None), VarDecl(Id(PsY), ArrayType([56.98], StringType), None, None), VarDecl(Id(CkGE), StringType, None, None)], Return(StringLit(i))), FuncDecl(Id(oUK), [], Return()), VarDecl(Id(Ple), ArrayType([77.06, 36.08, 58.61], StringType), None, StringLit(PLL)), FuncDecl(Id(Kf), [VarDecl(Id(v0), StringType, None, None), VarDecl(Id(ym), ArrayType([71.13], StringType), None, None)], Block([For(Id(aEbg), BooleanLit(False), BooleanLit(False), AssignStmt(ArrayCell(Id(G6i), [StringLit(UbuX)]), NumLit(80.17)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011565))

	def test_2153011566(self):
		input = '''
string zdV[32.87,53.91] <- "umCSi"
'''
		expect = '''Program([VarDecl(Id(zdV), ArrayType([32.87, 53.91], StringType), None, StringLit(umCSi))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011566))

	def test_2153011567(self):
		input = '''
func nP (number Vvln[67.53,78.19,57.8], string JG4A[10.72], bool Qn[25.03,96.35])
	return "u"
func fc (bool R7Ln[5.12], string iV, number Yru)	return ihF

'''
		expect = '''Program([FuncDecl(Id(nP), [VarDecl(Id(Vvln), ArrayType([67.53, 78.19, 57.8], NumberType), None, None), VarDecl(Id(JG4A), ArrayType([10.72], StringType), None, None), VarDecl(Id(Qn), ArrayType([25.03, 96.35], BoolType), None, None)], Return(StringLit(u))), FuncDecl(Id(fc), [VarDecl(Id(R7Ln), ArrayType([5.12], BoolType), None, None), VarDecl(Id(iV), StringType, None, None), VarDecl(Id(Yru), NumberType, None, None)], Return(Id(ihF)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011567))

	def test_2153011568(self):
		input = '''
func fRV (string cmx)
	return

var GVx <- true
bool n3W[13.2,63.06,65.73]
'''
		expect = '''Program([FuncDecl(Id(fRV), [VarDecl(Id(cmx), StringType, None, None)], Return()), VarDecl(Id(GVx), None, var, BooleanLit(True)), VarDecl(Id(n3W), ArrayType([13.2, 63.06, 65.73], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011568))

	def test_2153011569(self):
		input = '''
func O11k (string Gpb)
	begin
		for vs until H1Y by 15.84
			break
		string wgnz[34.65] <- "ar"
		dnSa(false, 63.0, "IyTSw")
	end
func bpK (bool kjXe[14.87], bool jjs[31.07,69.41,51.56], bool pijm[81.8,26.97,74.52])	return false
func vLM (string tGZ)	return

func aI (string Ht1k[11.77,9.41], number Acs[12.55])	return

'''
		expect = '''Program([FuncDecl(Id(O11k), [VarDecl(Id(Gpb), StringType, None, None)], Block([For(Id(vs), Id(H1Y), NumLit(15.84), Break), VarDecl(Id(wgnz), ArrayType([34.65], StringType), None, StringLit(ar)), CallStmt(Id(dnSa), [BooleanLit(False), NumLit(63.0), StringLit(IyTSw)])])), FuncDecl(Id(bpK), [VarDecl(Id(kjXe), ArrayType([14.87], BoolType), None, None), VarDecl(Id(jjs), ArrayType([31.07, 69.41, 51.56], BoolType), None, None), VarDecl(Id(pijm), ArrayType([81.8, 26.97, 74.52], BoolType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(vLM), [VarDecl(Id(tGZ), StringType, None, None)], Return()), FuncDecl(Id(aI), [VarDecl(Id(Ht1k), ArrayType([11.77, 9.41], StringType), None, None), VarDecl(Id(Acs), ArrayType([12.55], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011569))

	def test_2153011570(self):
		input = '''
dynamic CD49 <- "n"
'''
		expect = '''Program([VarDecl(Id(CD49), None, dynamic, StringLit(n))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011570))

	def test_2153011571(self):
		input = '''
var rX5j <- true
'''
		expect = '''Program([VarDecl(Id(rX5j), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011571))

	def test_2153011572(self):
		input = '''
func s25x (bool B85L[63.13,47.92], string k4j[47.87,74.63,71.47], bool dU)	begin
	end
dynamic h2x <- oI
bool Un[29.26]
func gvSt (number dw[97.64,15.48,32.49], number Wk[43.6,72.5,74.3])	begin
		for wsD until "iO" by WE
			DL <- LpUj
		continue
	end

func scgP (bool Ts4[31.66,10.15])	begin
	end

'''
		expect = '''Program([FuncDecl(Id(s25x), [VarDecl(Id(B85L), ArrayType([63.13, 47.92], BoolType), None, None), VarDecl(Id(k4j), ArrayType([47.87, 74.63, 71.47], StringType), None, None), VarDecl(Id(dU), BoolType, None, None)], Block([])), VarDecl(Id(h2x), None, dynamic, Id(oI)), VarDecl(Id(Un), ArrayType([29.26], BoolType), None, None), FuncDecl(Id(gvSt), [VarDecl(Id(dw), ArrayType([97.64, 15.48, 32.49], NumberType), None, None), VarDecl(Id(Wk), ArrayType([43.6, 72.5, 74.3], NumberType), None, None)], Block([For(Id(wsD), StringLit(iO), Id(WE), AssignStmt(Id(DL), Id(LpUj))), Continue])), FuncDecl(Id(scgP), [VarDecl(Id(Ts4), ArrayType([31.66, 10.15], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011572))

	def test_2153011573(self):
		input = '''
dynamic zn <- true
number TX[65.33] <- "izNJ"
string bA[47.03,5.33]
string hz3 <- "G"
'''
		expect = '''Program([VarDecl(Id(zn), None, dynamic, BooleanLit(True)), VarDecl(Id(TX), ArrayType([65.33], NumberType), None, StringLit(izNJ)), VarDecl(Id(bA), ArrayType([47.03, 5.33], StringType), None, None), VarDecl(Id(hz3), StringType, None, StringLit(G))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011573))

	def test_2153011574(self):
		input = '''
string o5o[5.66,57.38,79.43] <- false
func nUNm (bool GBS)	begin
		var zS0T <- "k"
		break
	end
func nY (bool nEO, number xnhO)	return true
var TEN <- vL8
var JnQ3 <- 90.12
'''
		expect = '''Program([VarDecl(Id(o5o), ArrayType([5.66, 57.38, 79.43], StringType), None, BooleanLit(False)), FuncDecl(Id(nUNm), [VarDecl(Id(GBS), BoolType, None, None)], Block([VarDecl(Id(zS0T), None, var, StringLit(k)), Break])), FuncDecl(Id(nY), [VarDecl(Id(nEO), BoolType, None, None), VarDecl(Id(xnhO), NumberType, None, None)], Return(BooleanLit(True))), VarDecl(Id(TEN), None, var, Id(vL8)), VarDecl(Id(JnQ3), None, var, NumLit(90.12))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011574))

	def test_2153011575(self):
		input = '''
bool KG[68.19,67.41]
func JG (string kUQ[49.43])
	return NAO
func jL (bool X2P8, string eN)
	return
number MiT <- true
func vSzs (string po[58.72,47.41,1.34], string xm[88.01,77.07], number wiwk[84.63,63.03,20.84])
	return
'''
		expect = '''Program([VarDecl(Id(KG), ArrayType([68.19, 67.41], BoolType), None, None), FuncDecl(Id(JG), [VarDecl(Id(kUQ), ArrayType([49.43], StringType), None, None)], Return(Id(NAO))), FuncDecl(Id(jL), [VarDecl(Id(X2P8), BoolType, None, None), VarDecl(Id(eN), StringType, None, None)], Return()), VarDecl(Id(MiT), NumberType, None, BooleanLit(True)), FuncDecl(Id(vSzs), [VarDecl(Id(po), ArrayType([58.72, 47.41, 1.34], StringType), None, None), VarDecl(Id(xm), ArrayType([88.01, 77.07], StringType), None, None), VarDecl(Id(wiwk), ArrayType([84.63, 63.03, 20.84], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011575))

	def test_2153011576(self):
		input = '''
string X8eK[65.77]
func Vk (bool OPT, string KWOh[57.87,76.39])
	begin
		begin
			break
			continue
		end
		if (true)
		if (ri)
		qGG(mX, true)
		elif (true)
		Av <- kdN
		elif (DoFl)
		begin
			break
			number xrs[96.03,77.43,63.41] <- 0.15
			break
		end
		elif ("lTyA")
		continue
		elif (79.13) for b6I until qQq by "llI"
			number CL9[67.58,8.59]
		elif (S3) break
		elif (false) break
		elif (SfOQ) number UU_
		elif (2.73) number BA[66.17,35.46,61.0]
		elif ("tut")
		WbP[73.15] <- "Qe"
		elif (true) number smI[2.2,38.98,97.96] <- 66.06
		else continue
	end

func a2 ()	return
'''
		expect = '''Program([VarDecl(Id(X8eK), ArrayType([65.77], StringType), None, None), FuncDecl(Id(Vk), [VarDecl(Id(OPT), BoolType, None, None), VarDecl(Id(KWOh), ArrayType([57.87, 76.39], StringType), None, None)], Block([Block([Break, Continue]), If(BooleanLit(True), If(Id(ri), CallStmt(Id(qGG), [Id(mX), BooleanLit(True)])), [(BooleanLit(True), AssignStmt(Id(Av), Id(kdN))), (Id(DoFl), Block([Break, VarDecl(Id(xrs), ArrayType([96.03, 77.43, 63.41], NumberType), None, NumLit(0.15)), Break])), (StringLit(lTyA), Continue), (NumLit(79.13), For(Id(b6I), Id(qQq), StringLit(llI), VarDecl(Id(CL9), ArrayType([67.58, 8.59], NumberType), None, None))), (Id(S3), Break), (BooleanLit(False), Break), (Id(SfOQ), VarDecl(Id(UU_), NumberType, None, None)), (NumLit(2.73), VarDecl(Id(BA), ArrayType([66.17, 35.46, 61.0], NumberType), None, None)), (StringLit(tut), AssignStmt(ArrayCell(Id(WbP), [NumLit(73.15)]), StringLit(Qe))), (BooleanLit(True), VarDecl(Id(smI), ArrayType([2.2, 38.98, 97.96], NumberType), None, NumLit(66.06)))], Continue), [], None])), FuncDecl(Id(a2), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011576))

	def test_2153011577(self):
		input = '''
func ujDe (number S1K_[47.03,33.74,41.61], bool EqM[14.97,56.41])	return false
number q_3[99.06,52.52,88.47]
dynamic gx
func Uq (number cCb6)	return
'''
		expect = '''Program([FuncDecl(Id(ujDe), [VarDecl(Id(S1K_), ArrayType([47.03, 33.74, 41.61], NumberType), None, None), VarDecl(Id(EqM), ArrayType([14.97, 56.41], BoolType), None, None)], Return(BooleanLit(False))), VarDecl(Id(q_3), ArrayType([99.06, 52.52, 88.47], NumberType), None, None), VarDecl(Id(gx), None, dynamic, None), FuncDecl(Id(Uq), [VarDecl(Id(cCb6), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011577))

	def test_2153011578(self):
		input = '''
number bVH
'''
		expect = '''Program([VarDecl(Id(bVH), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011578))

	def test_2153011579(self):
		input = '''
dynamic S_
func nK ()
	return 20.35
bool kI3 <- "xerS"
number nVl[87.4]
'''
		expect = '''Program([VarDecl(Id(S_), None, dynamic, None), FuncDecl(Id(nK), [], Return(NumLit(20.35))), VarDecl(Id(kI3), BoolType, None, StringLit(xerS)), VarDecl(Id(nVl), ArrayType([87.4], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011579))

	def test_2153011580(self):
		input = '''
func cs (string vg)	begin
		begin
			fd("CKE")
			break
		end
	end
var Dd0r <- "erGmK"
number gq <- true
'''
		expect = '''Program([FuncDecl(Id(cs), [VarDecl(Id(vg), StringType, None, None)], Block([Block([CallStmt(Id(fd), [StringLit(CKE)]), Break])])), VarDecl(Id(Dd0r), None, var, StringLit(erGmK)), VarDecl(Id(gq), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011580))

	def test_2153011581(self):
		input = '''
func NE8 (number Hfk[36.95])
	begin
	end
func dBO (string HrX, number Th5z)	return
string aOW6[94.78,44.09,80.67]
dynamic Jar
string dx[62.76] <- 92.94
'''
		expect = '''Program([FuncDecl(Id(NE8), [VarDecl(Id(Hfk), ArrayType([36.95], NumberType), None, None)], Block([])), FuncDecl(Id(dBO), [VarDecl(Id(HrX), StringType, None, None), VarDecl(Id(Th5z), NumberType, None, None)], Return()), VarDecl(Id(aOW6), ArrayType([94.78, 44.09, 80.67], StringType), None, None), VarDecl(Id(Jar), None, dynamic, None), VarDecl(Id(dx), ArrayType([62.76], StringType), None, NumLit(92.94))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011581))

	def test_2153011582(self):
		input = '''
func XO ()	return

'''
		expect = '''Program([FuncDecl(Id(XO), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011582))

	def test_2153011583(self):
		input = '''
string rR1[47.7,17.87]
func Hc (number GmGX[54.35,59.74], bool aB)
	begin
	end
func SV2z (bool w7[57.12,59.75], number t50[49.53,98.37], string Xi25[94.84,99.77,11.57])	begin
		Xfg <- false
		continue
		H28T()
	end
var f4 <- 6.79
string jhhl
'''
		expect = '''Program([VarDecl(Id(rR1), ArrayType([47.7, 17.87], StringType), None, None), FuncDecl(Id(Hc), [VarDecl(Id(GmGX), ArrayType([54.35, 59.74], NumberType), None, None), VarDecl(Id(aB), BoolType, None, None)], Block([])), FuncDecl(Id(SV2z), [VarDecl(Id(w7), ArrayType([57.12, 59.75], BoolType), None, None), VarDecl(Id(t50), ArrayType([49.53, 98.37], NumberType), None, None), VarDecl(Id(Xi25), ArrayType([94.84, 99.77, 11.57], StringType), None, None)], Block([AssignStmt(Id(Xfg), BooleanLit(False)), Continue, CallStmt(Id(H28T), [])])), VarDecl(Id(f4), None, var, NumLit(6.79)), VarDecl(Id(jhhl), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011583))

	def test_2153011584(self):
		input = '''
string gNSw
number h6[27.96,93.22]
func F9I (string VPo)	return gqI5

bool gQc[14.48,70.85]
number YKlV[67.1,24.87] <- dg
'''
		expect = '''Program([VarDecl(Id(gNSw), StringType, None, None), VarDecl(Id(h6), ArrayType([27.96, 93.22], NumberType), None, None), FuncDecl(Id(F9I), [VarDecl(Id(VPo), StringType, None, None)], Return(Id(gqI5))), VarDecl(Id(gQc), ArrayType([14.48, 70.85], BoolType), None, None), VarDecl(Id(YKlV), ArrayType([67.1, 24.87], NumberType), None, Id(dg))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011584))

	def test_2153011585(self):
		input = '''
func EV (bool pJXr, string Pm6, bool lY[9.72,91.86])	return

string u9J[11.14] <- false
'''
		expect = '''Program([FuncDecl(Id(EV), [VarDecl(Id(pJXr), BoolType, None, None), VarDecl(Id(Pm6), StringType, None, None), VarDecl(Id(lY), ArrayType([9.72, 91.86], BoolType), None, None)], Return()), VarDecl(Id(u9J), ArrayType([11.14], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011585))

	def test_2153011586(self):
		input = '''
func My (string Fe)	return 55.07

dynamic at1k
'''
		expect = '''Program([FuncDecl(Id(My), [VarDecl(Id(Fe), StringType, None, None)], Return(NumLit(55.07))), VarDecl(Id(at1k), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011586))

	def test_2153011587(self):
		input = '''
func Xm (bool fYT2, string oT, number JiD[86.01,64.9])
	return false
func ybWy ()
	return
func TF (number MR, bool M_g, string p9b[48.05,83.74,69.61])
	begin
	end
bool t9[72.37]
'''
		expect = '''Program([FuncDecl(Id(Xm), [VarDecl(Id(fYT2), BoolType, None, None), VarDecl(Id(oT), StringType, None, None), VarDecl(Id(JiD), ArrayType([86.01, 64.9], NumberType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(ybWy), [], Return()), FuncDecl(Id(TF), [VarDecl(Id(MR), NumberType, None, None), VarDecl(Id(M_g), BoolType, None, None), VarDecl(Id(p9b), ArrayType([48.05, 83.74, 69.61], StringType), None, None)], Block([])), VarDecl(Id(t9), ArrayType([72.37], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011587))

	def test_2153011588(self):
		input = '''
func B87A (bool oe[48.3,41.26,10.16], bool GS[58.18,29.63,67.5], string YUc[22.14,69.76,32.01])	return false

'''
		expect = '''Program([FuncDecl(Id(B87A), [VarDecl(Id(oe), ArrayType([48.3, 41.26, 10.16], BoolType), None, None), VarDecl(Id(GS), ArrayType([58.18, 29.63, 67.5], BoolType), None, None), VarDecl(Id(YUc), ArrayType([22.14, 69.76, 32.01], StringType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011588))

	def test_2153011589(self):
		input = '''
var po <- true
'''
		expect = '''Program([VarDecl(Id(po), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011589))

	def test_2153011590(self):
		input = '''
func bt (bool LUx1)	begin
		break
	end
bool e4t[85.2,18.94,68.31]
func zosE (string GCJ[30.15,98.56], string IX, string Gd)
	return false

'''
		expect = '''Program([FuncDecl(Id(bt), [VarDecl(Id(LUx1), BoolType, None, None)], Block([Break])), VarDecl(Id(e4t), ArrayType([85.2, 18.94, 68.31], BoolType), None, None), FuncDecl(Id(zosE), [VarDecl(Id(GCJ), ArrayType([30.15, 98.56], StringType), None, None), VarDecl(Id(IX), StringType, None, None), VarDecl(Id(Gd), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011590))

	def test_2153011591(self):
		input = '''
func at (bool MAC)
	return "DpOZL"
func GyS (bool f7z[5.44,44.05])
	begin
		for lu1 until h0 by Tk
			for ngPu until T37k by false
				begin
					return 0.56
				end
		if ("OOP") if (true)
		QdMb["sRUGw", "HLC", jw] <- false
		elif (false)
		var PC <- "Vmb"
		elif ("rWS")
		return 34.07
		elif ("amAS")
		F1TK <- ce7
		else return
		string XZYU[97.34,88.88]
	end
func U8 (number h1yx)	return "Ydl"

func bnS ()	begin
		return false
		number fCRI
	end
string ua[28.58,96.48]
'''
		expect = '''Program([FuncDecl(Id(at), [VarDecl(Id(MAC), BoolType, None, None)], Return(StringLit(DpOZL))), FuncDecl(Id(GyS), [VarDecl(Id(f7z), ArrayType([5.44, 44.05], BoolType), None, None)], Block([For(Id(lu1), Id(h0), Id(Tk), For(Id(ngPu), Id(T37k), BooleanLit(False), Block([Return(NumLit(0.56))]))), If(StringLit(OOP), If(BooleanLit(True), AssignStmt(ArrayCell(Id(QdMb), [StringLit(sRUGw), StringLit(HLC), Id(jw)]), BooleanLit(False))), [(BooleanLit(False), VarDecl(Id(PC), None, var, StringLit(Vmb))), (StringLit(rWS), Return(NumLit(34.07))), (StringLit(amAS), AssignStmt(Id(F1TK), Id(ce7)))], Return()), [], None, VarDecl(Id(XZYU), ArrayType([97.34, 88.88], StringType), None, None)])), FuncDecl(Id(U8), [VarDecl(Id(h1yx), NumberType, None, None)], Return(StringLit(Ydl))), FuncDecl(Id(bnS), [], Block([Return(BooleanLit(False)), VarDecl(Id(fCRI), NumberType, None, None)])), VarDecl(Id(ua), ArrayType([28.58, 96.48], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011591))

	def test_2153011592(self):
		input = '''
number geoZ
'''
		expect = '''Program([VarDecl(Id(geoZ), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011592))

	def test_2153011593(self):
		input = '''
bool sR <- 86.44
var u_I <- 66.29
'''
		expect = '''Program([VarDecl(Id(sR), BoolType, None, NumLit(86.44)), VarDecl(Id(u_I), None, var, NumLit(66.29))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011593))

	def test_2153011594(self):
		input = '''
func cou8 (number uN[18.29,57.16], bool SUMa)
	return

func J4nq (bool NV, string TasA[77.78], number sn[26.87,94.65])	return 99.77

'''
		expect = '''Program([FuncDecl(Id(cou8), [VarDecl(Id(uN), ArrayType([18.29, 57.16], NumberType), None, None), VarDecl(Id(SUMa), BoolType, None, None)], Return()), FuncDecl(Id(J4nq), [VarDecl(Id(NV), BoolType, None, None), VarDecl(Id(TasA), ArrayType([77.78], StringType), None, None), VarDecl(Id(sn), ArrayType([26.87, 94.65], NumberType), None, None)], Return(NumLit(99.77)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011594))

	def test_2153011595(self):
		input = '''
func v8Z0 ()	begin
		for Mtsg until true by 98.63
			if ("CGeDM")
			if (SV1u) continue
			elif ("s") if (xD0X)
			var DW <- false
			elif (96.23) break
			elif (true)
			continue
			else return
			elif (67.24) var Nxw8 <- 71.93
			elif ("UQp") RDv[BU3, false] <- 74.18
			elif (true) for hpVB until true by 96.12
				break
			else return
			elif (74.14) g8 <- hwk
		MoZv[s72, Kf, FNei] <- true
	end
func glA ()	return

func EQ (number n8[49.35,53.77], number jT6c)
	return

func ot ()
	return sPd
'''
		expect = '''Program([FuncDecl(Id(v8Z0), [], Block([For(Id(Mtsg), BooleanLit(True), NumLit(98.63), If(StringLit(CGeDM), If(Id(SV1u), Continue), [(StringLit(s), If(Id(xD0X), VarDecl(Id(DW), None, var, BooleanLit(False))), [(NumLit(96.23), Break), (BooleanLit(True), Continue)], Return()), (NumLit(67.24), VarDecl(Id(Nxw8), None, var, NumLit(71.93))), (StringLit(UQp), AssignStmt(ArrayCell(Id(RDv), [Id(BU3), BooleanLit(False)]), NumLit(74.18))), (BooleanLit(True), For(Id(hpVB), BooleanLit(True), NumLit(96.12), Break))], Return()), [(NumLit(74.14), AssignStmt(Id(g8), Id(hwk)))], None), AssignStmt(ArrayCell(Id(MoZv), [Id(s72), Id(Kf), Id(FNei)]), BooleanLit(True))])), FuncDecl(Id(glA), [], Return()), FuncDecl(Id(EQ), [VarDecl(Id(n8), ArrayType([49.35, 53.77], NumberType), None, None), VarDecl(Id(jT6c), NumberType, None, None)], Return()), FuncDecl(Id(ot), [], Return(Id(sPd)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011595))

	def test_2153011596(self):
		input = '''
string BM
bool VzG[33.74,62.98,5.54]
number PUr
'''
		expect = '''Program([VarDecl(Id(BM), StringType, None, None), VarDecl(Id(VzG), ArrayType([33.74, 62.98, 5.54], BoolType), None, None), VarDecl(Id(PUr), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011596))

	def test_2153011597(self):
		input = '''
string xnM[63.7] <- 66.89
func FWH (string YV6[89.25,63.93], bool g7IK[33.64,56.06])
	return true
var qUJ <- true
bool I3_[37.11,6.22] <- 2.57
dynamic nX <- 86.66
'''
		expect = '''Program([VarDecl(Id(xnM), ArrayType([63.7], StringType), None, NumLit(66.89)), FuncDecl(Id(FWH), [VarDecl(Id(YV6), ArrayType([89.25, 63.93], StringType), None, None), VarDecl(Id(g7IK), ArrayType([33.64, 56.06], BoolType), None, None)], Return(BooleanLit(True))), VarDecl(Id(qUJ), None, var, BooleanLit(True)), VarDecl(Id(I3_), ArrayType([37.11, 6.22], BoolType), None, NumLit(2.57)), VarDecl(Id(nX), None, dynamic, NumLit(86.66))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011597))

	def test_2153011598(self):
		input = '''
var zC <- false
func gU (number RE[44.76,22.64], string MeH, number y_)
	return
number SI[41.02] <- 81.04
number CTBy[3.92] <- iq
func PDn (number Qq3, number ne)	return
'''
		expect = '''Program([VarDecl(Id(zC), None, var, BooleanLit(False)), FuncDecl(Id(gU), [VarDecl(Id(RE), ArrayType([44.76, 22.64], NumberType), None, None), VarDecl(Id(MeH), StringType, None, None), VarDecl(Id(y_), NumberType, None, None)], Return()), VarDecl(Id(SI), ArrayType([41.02], NumberType), None, NumLit(81.04)), VarDecl(Id(CTBy), ArrayType([3.92], NumberType), None, Id(iq)), FuncDecl(Id(PDn), [VarDecl(Id(Qq3), NumberType, None, None), VarDecl(Id(ne), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011598))

	def test_2153011599(self):
		input = '''
func EP (bool zC2, number OdQo[74.69,77.18])
	return

dynamic YcXl <- 90.67
func R2o (number jiMn[48.84,69.62])	return 34.44

'''
		expect = '''Program([FuncDecl(Id(EP), [VarDecl(Id(zC2), BoolType, None, None), VarDecl(Id(OdQo), ArrayType([74.69, 77.18], NumberType), None, None)], Return()), VarDecl(Id(YcXl), None, dynamic, NumLit(90.67)), FuncDecl(Id(R2o), [VarDecl(Id(jiMn), ArrayType([48.84, 69.62], NumberType), None, None)], Return(NumLit(34.44)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011599))
