import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
	def test_21530115000(self):
		input = '''
func zo5b ()	begin
		if ([([mVxp]), [cWj, 44.17, false]])
		return k3D
		elif (13.6)
		break
		elif (true)
		return
		elif (au)
		break
		elif (rb) if ("Ywvw")
		for iQF until true by lg
			return false
		elif (V3) return 59.32
		elif (pv)
		for PM until 98.37 by false
			begin
			end
		elif ("XsQQ") break
		elif (39.48)
		Nyv(98.67)
		else begin
		end
		else ox2[false] <- 10.6
		number LGH[52.5,37.09,79.67]
		return
	end
func iJMH ()	begin
		for b2 until hO by 35.76
			return "xOSk"
		begin
			wW("r")
			continue
			begin
				return kVKf
				continue
			end
		end
	end
'''
		expect = '''Program([FuncDecl(Id(zo5b), [], Block([If(ArrayLit(ArrayLit(Id(mVxp)), ArrayLit(Id(cWj), NumLit(44.17), BooleanLit(False))), Return(Id(k3D))), [(NumLit(13.6), Break), (BooleanLit(True), Return()), (Id(au), Break), (Id(rb), If(StringLit(Ywvw), For(Id(iQF), BooleanLit(True), Id(lg), Return(BooleanLit(False)))), [(Id(V3), Return(NumLit(59.32))), (Id(pv), For(Id(PM), NumLit(98.37), BooleanLit(False), Block([]))), (StringLit(XsQQ), Break), (NumLit(39.48), CallStmt(Id(Nyv), [NumLit(98.67)]))], Block([]))], AssignStmt(ArrayCell(Id(ox2), [BooleanLit(False)]), NumLit(10.6)), VarDecl(Id(LGH), ArrayType([52.5, 37.09, 79.67], NumberType), None, None), Return()])), FuncDecl(Id(iJMH), [], Block([For(Id(b2), Id(hO), NumLit(35.76), Return(StringLit(xOSk))), Block([CallStmt(Id(wW), [StringLit(r)]), Continue, Block([Return(Id(kVKf)), Continue])])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115000))

	def test_21530115001(self):
		input = '''
func AJpN (number nVp_, bool tvY, number gqcf[60.45])	return yC

func tGtQ ()	return
'''
		expect = '''Program([FuncDecl(Id(AJpN), [VarDecl(Id(nVp_), NumberType, None, None), VarDecl(Id(tvY), BoolType, None, None), VarDecl(Id(gqcf), ArrayType([60.45], NumberType), None, None)], Return(Id(yC))), FuncDecl(Id(tGtQ), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115001))

	def test_21530115002(self):
		input = '''
func x8 (string X9)
	return

func Utzf (bool a6Bh, bool nrJa[14.77,78.7,45.51])	return false

'''
		expect = '''Program([FuncDecl(Id(x8), [VarDecl(Id(X9), StringType, None, None)], Return()), FuncDecl(Id(Utzf), [VarDecl(Id(a6Bh), BoolType, None, None), VarDecl(Id(nrJa), ArrayType([14.77, 78.7, 45.51], BoolType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115002))

	def test_21530115003(self):
		input = '''
func zyr ()	return "P"

'''
		expect = '''Program([FuncDecl(Id(zyr), [], Return(StringLit(P)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115003))

	def test_21530115004(self):
		input = '''
string FE9[87.07,29.35] <- vR
func l7 (string q5Zn[92.25], string Rf[94.93,26.27], string LK)
	begin
	end

'''
		expect = '''Program([VarDecl(Id(FE9), ArrayType([87.07, 29.35], StringType), None, Id(vR)), FuncDecl(Id(l7), [VarDecl(Id(q5Zn), ArrayType([92.25], StringType), None, None), VarDecl(Id(Rf), ArrayType([94.93, 26.27], StringType), None, None), VarDecl(Id(LK), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115004))

	def test_21530115005(self):
		input = '''
func fCv (bool pO, number R_, number Sfww)	return
string gy[34.03,44.67] <- 41.25
number Jxt
'''
		expect = '''Program([FuncDecl(Id(fCv), [VarDecl(Id(pO), BoolType, None, None), VarDecl(Id(R_), NumberType, None, None), VarDecl(Id(Sfww), NumberType, None, None)], Return()), VarDecl(Id(gy), ArrayType([34.03, 44.67], StringType), None, NumLit(41.25)), VarDecl(Id(Jxt), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115005))

	def test_21530115006(self):
		input = '''
func kr8R (number Kmw[21.68,92.92,22.85], number s4TQ[3.88])
	return false

'''
		expect = '''Program([FuncDecl(Id(kr8R), [VarDecl(Id(Kmw), ArrayType([21.68, 92.92, 22.85], NumberType), None, None), VarDecl(Id(s4TQ), ArrayType([3.88], NumberType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115006))

	def test_21530115007(self):
		input = '''
func D6V ()
	return jy7z
number I8u_[60.23,31.73,45.79] <- false
'''
		expect = '''Program([FuncDecl(Id(D6V), [], Return(Id(jy7z))), VarDecl(Id(I8u_), ArrayType([60.23, 31.73, 45.79], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115007))

	def test_21530115008(self):
		input = '''
func neq3 (bool lnN)
	begin
		string Cv <- false
		uB("QCXU", EQay)
	end

bool Lq4X[84.25,87.59,34.5]
func UA (string FZU1[67.03,87.82,14.62], string ibO[46.85,83.73])	return
'''
		expect = '''Program([FuncDecl(Id(neq3), [VarDecl(Id(lnN), BoolType, None, None)], Block([VarDecl(Id(Cv), StringType, None, BooleanLit(False)), CallStmt(Id(uB), [StringLit(QCXU), Id(EQay)])])), VarDecl(Id(Lq4X), ArrayType([84.25, 87.59, 34.5], BoolType), None, None), FuncDecl(Id(UA), [VarDecl(Id(FZU1), ArrayType([67.03, 87.82, 14.62], StringType), None, None), VarDecl(Id(ibO), ArrayType([46.85, 83.73], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115008))

	def test_21530115009(self):
		input = '''
number UH[45.81] <- false
string nR0W <- 46.41
'''
		expect = '''Program([VarDecl(Id(UH), ArrayType([45.81], NumberType), None, BooleanLit(False)), VarDecl(Id(nR0W), StringType, None, NumLit(46.41))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115009))

	def test_21530115010(self):
		input = '''
bool xxb
number QiX[69.64,99.02]
number I0FY[62.94,53.13,24.28] <- 98.97
dynamic nf
func TZo ()	return

'''
		expect = '''Program([VarDecl(Id(xxb), BoolType, None, None), VarDecl(Id(QiX), ArrayType([69.64, 99.02], NumberType), None, None), VarDecl(Id(I0FY), ArrayType([62.94, 53.13, 24.28], NumberType), None, NumLit(98.97)), VarDecl(Id(nf), None, dynamic, None), FuncDecl(Id(TZo), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115010))

	def test_21530115011(self):
		input = '''
func Ya5y (bool Dvo[71.5,90.36,20.16])	return

func yU6Q (number aHee[97.17,14.73], number sjB)	return 20.91

bool iE[14.03,64.13,60.76] <- true
string M1M <- false
'''
		expect = '''Program([FuncDecl(Id(Ya5y), [VarDecl(Id(Dvo), ArrayType([71.5, 90.36, 20.16], BoolType), None, None)], Return()), FuncDecl(Id(yU6Q), [VarDecl(Id(aHee), ArrayType([97.17, 14.73], NumberType), None, None), VarDecl(Id(sjB), NumberType, None, None)], Return(NumLit(20.91))), VarDecl(Id(iE), ArrayType([14.03, 64.13, 60.76], BoolType), None, BooleanLit(True)), VarDecl(Id(M1M), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115011))

	def test_21530115012(self):
		input = '''
number SsKm <- "d"
string sh
dynamic jyq
func zQmB (string SLP, number ZEOl, bool KT[58.11])	return "AlHv"

'''
		expect = '''Program([VarDecl(Id(SsKm), NumberType, None, StringLit(d)), VarDecl(Id(sh), StringType, None, None), VarDecl(Id(jyq), None, dynamic, None), FuncDecl(Id(zQmB), [VarDecl(Id(SLP), StringType, None, None), VarDecl(Id(ZEOl), NumberType, None, None), VarDecl(Id(KT), ArrayType([58.11], BoolType), None, None)], Return(StringLit(AlHv)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115012))

	def test_21530115013(self):
		input = '''
func rsN ()
	return
bool Y6Kx <- "QZee"
func Eu (number pbHn, bool Sv)
	return false

'''
		expect = '''Program([FuncDecl(Id(rsN), [], Return()), VarDecl(Id(Y6Kx), BoolType, None, StringLit(QZee)), FuncDecl(Id(Eu), [VarDecl(Id(pbHn), NumberType, None, None), VarDecl(Id(Sv), BoolType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115013))

	def test_21530115014(self):
		input = '''
func YZv ()	begin
		continue
	end

func Js8W (number sY[28.06,5.86,55.9])	return

func Ia (bool SpxL[27.01,77.5])
	return

'''
		expect = '''Program([FuncDecl(Id(YZv), [], Block([Continue])), FuncDecl(Id(Js8W), [VarDecl(Id(sY), ArrayType([28.06, 5.86, 55.9], NumberType), None, None)], Return()), FuncDecl(Id(Ia), [VarDecl(Id(SpxL), ArrayType([27.01, 77.5], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115014))

	def test_21530115015(self):
		input = '''
func EO (bool sk)
	return 86.79

func Jx (bool zdyI, string C_[57.65,38.99,52.47])
	begin
	end

func XwEe ()	return 3.73

func hZw ()	return
func DAWH (string lLIm, bool Ds9[81.45,47.46])	return "E"
'''
		expect = '''Program([FuncDecl(Id(EO), [VarDecl(Id(sk), BoolType, None, None)], Return(NumLit(86.79))), FuncDecl(Id(Jx), [VarDecl(Id(zdyI), BoolType, None, None), VarDecl(Id(C_), ArrayType([57.65, 38.99, 52.47], StringType), None, None)], Block([])), FuncDecl(Id(XwEe), [], Return(NumLit(3.73))), FuncDecl(Id(hZw), [], Return()), FuncDecl(Id(DAWH), [VarDecl(Id(lLIm), StringType, None, None), VarDecl(Id(Ds9), ArrayType([81.45, 47.46], BoolType), None, None)], Return(StringLit(E)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115015))

	def test_21530115016(self):
		input = '''
func owTc (number nKki, string VK, number cW)
	return
string dJcw[21.31]
func QZ7o (string AJ[49.14], bool hO)	begin
		begin
			continue
			break
		end
		continue
	end
'''
		expect = '''Program([FuncDecl(Id(owTc), [VarDecl(Id(nKki), NumberType, None, None), VarDecl(Id(VK), StringType, None, None), VarDecl(Id(cW), NumberType, None, None)], Return()), VarDecl(Id(dJcw), ArrayType([21.31], StringType), None, None), FuncDecl(Id(QZ7o), [VarDecl(Id(AJ), ArrayType([49.14], StringType), None, None), VarDecl(Id(hO), BoolType, None, None)], Block([Block([Continue, Break]), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115016))

	def test_21530115017(self):
		input = '''
func lc (bool gR, bool DCS)
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(lc), [VarDecl(Id(gR), BoolType, None, None), VarDecl(Id(DCS), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115017))

	def test_21530115018(self):
		input = '''
bool Q4W[84.76,30.75,51.23]
func FF (number R4[49.98,31.91], number MbDB[86.89,63.8])
	return
'''
		expect = '''Program([VarDecl(Id(Q4W), ArrayType([84.76, 30.75, 51.23], BoolType), None, None), FuncDecl(Id(FF), [VarDecl(Id(R4), ArrayType([49.98, 31.91], NumberType), None, None), VarDecl(Id(MbDB), ArrayType([86.89, 63.8], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115018))

	def test_21530115019(self):
		input = '''
bool G7
number NB[45.32,61.89] <- "D"
string Cqw <- wZ
func fyf (bool MgpR)	begin
	end

func UPX (bool QB8[60.83,72.48])	return
'''
		expect = '''Program([VarDecl(Id(G7), BoolType, None, None), VarDecl(Id(NB), ArrayType([45.32, 61.89], NumberType), None, StringLit(D)), VarDecl(Id(Cqw), StringType, None, Id(wZ)), FuncDecl(Id(fyf), [VarDecl(Id(MgpR), BoolType, None, None)], Block([])), FuncDecl(Id(UPX), [VarDecl(Id(QB8), ArrayType([60.83, 72.48], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115019))

	def test_21530115020(self):
		input = '''
func bC0 (string iiKf)
	return
'''
		expect = '''Program([FuncDecl(Id(bC0), [VarDecl(Id(iiKf), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115020))

	def test_21530115021(self):
		input = '''
bool oG[89.06,99.14,69.61]
'''
		expect = '''Program([VarDecl(Id(oG), ArrayType([89.06, 99.14, 69.61], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115021))

	def test_21530115022(self):
		input = '''
func lM (string WsfK, number KyJ, number CoYh)	return 86.81

func AL (number sTe)	begin
		for DhA until JRG by YY
			l6D["KkSu", qtr5, "kpfnl"] <- "a"
		ML <- 64.24
	end

'''
		expect = '''Program([FuncDecl(Id(lM), [VarDecl(Id(WsfK), StringType, None, None), VarDecl(Id(KyJ), NumberType, None, None), VarDecl(Id(CoYh), NumberType, None, None)], Return(NumLit(86.81))), FuncDecl(Id(AL), [VarDecl(Id(sTe), NumberType, None, None)], Block([For(Id(DhA), Id(JRG), Id(YY), AssignStmt(ArrayCell(Id(l6D), [StringLit(KkSu), Id(qtr5), StringLit(kpfnl)]), StringLit(a))), AssignStmt(Id(ML), NumLit(64.24))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115022))

	def test_21530115023(self):
		input = '''
bool fh[97.36,4.64,81.43] <- false
dynamic HV <- gLf
func jWoW ()
	begin
		break
		if (63.81)
		begin
			if (l_D) return "FAL"
			elif ("vNq")
			break
			elif (37.44) if (HC) break
			else of(ts, 0.41, oo)
			elif (true)
			for DX until v5 by "x"
				return
			elif (CYZ) G4fZ[u9aX, false] <- "sGyWW"
			if (56.94)
			if ("h")
			fW("C", xPl, "Q")
			elif (95.45) tok(38.65, 96.97, "glmfn")
			elif (s5) continue
			elif (up) begin
				Cx[53.29] <- false
				string H7[86.31,94.78,30.91] <- Ur
			end
			else break
			else for vql until 44.27 by true
				for tHM until 19.71 by true
					yEB()
		end
		elif (80.85)
		break
	end

func sA (bool kEzJ)
	return
'''
		expect = '''Program([VarDecl(Id(fh), ArrayType([97.36, 4.64, 81.43], BoolType), None, BooleanLit(False)), VarDecl(Id(HV), None, dynamic, Id(gLf)), FuncDecl(Id(jWoW), [], Block([Break, If(NumLit(63.81), Block([If(Id(l_D), Return(StringLit(FAL))), [(StringLit(vNq), Break), (NumLit(37.44), If(Id(HC), Break), [], CallStmt(Id(of), [Id(ts), NumLit(0.41), Id(oo)])), (BooleanLit(True), For(Id(DX), Id(v5), StringLit(x), Return())), (Id(CYZ), AssignStmt(ArrayCell(Id(G4fZ), [Id(u9aX), BooleanLit(False)]), StringLit(sGyWW)))], None, If(NumLit(56.94), If(StringLit(h), CallStmt(Id(fW), [StringLit(C), Id(xPl), StringLit(Q)])), [(NumLit(95.45), CallStmt(Id(tok), [NumLit(38.65), NumLit(96.97), StringLit(glmfn)])), (Id(s5), Continue), (Id(up), Block([AssignStmt(ArrayCell(Id(Cx), [NumLit(53.29)]), BooleanLit(False)), VarDecl(Id(H7), ArrayType([86.31, 94.78, 30.91], StringType), None, Id(Ur))]))], Break), [], For(Id(vql), NumLit(44.27), BooleanLit(True), For(Id(tHM), NumLit(19.71), BooleanLit(True), CallStmt(Id(yEB), [])))])), [(NumLit(80.85), Break)], None])), FuncDecl(Id(sA), [VarDecl(Id(kEzJ), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115023))

	def test_21530115024(self):
		input = '''
dynamic a0
bool Kw8[86.72]
'''
		expect = '''Program([VarDecl(Id(a0), None, dynamic, None), VarDecl(Id(Kw8), ArrayType([86.72], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115024))

	def test_21530115025(self):
		input = '''
number v3do <- 94.36
func oQr (bool LTrw[35.42], string L5)	return

'''
		expect = '''Program([VarDecl(Id(v3do), NumberType, None, NumLit(94.36)), FuncDecl(Id(oQr), [VarDecl(Id(LTrw), ArrayType([35.42], BoolType), None, None), VarDecl(Id(L5), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115025))

	def test_21530115026(self):
		input = '''
func qFeN (number EvU[79.14,46.34], number u8, number Lst[41.81,98.37])	return true

func BzIr (string FypB[38.72,99.2,3.94], string X2Oe[16.05,19.4,19.29])	return
'''
		expect = '''Program([FuncDecl(Id(qFeN), [VarDecl(Id(EvU), ArrayType([79.14, 46.34], NumberType), None, None), VarDecl(Id(u8), NumberType, None, None), VarDecl(Id(Lst), ArrayType([41.81, 98.37], NumberType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(BzIr), [VarDecl(Id(FypB), ArrayType([38.72, 99.2, 3.94], StringType), None, None), VarDecl(Id(X2Oe), ArrayType([16.05, 19.4, 19.29], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115026))

	def test_21530115027(self):
		input = '''
func nIZn (bool Mseu[62.92], bool JW[31.09,31.02], bool Qp[3.72,85.59,86.28])	return

bool IB58[4.2,16.72,29.83] <- M4
'''
		expect = '''Program([FuncDecl(Id(nIZn), [VarDecl(Id(Mseu), ArrayType([62.92], BoolType), None, None), VarDecl(Id(JW), ArrayType([31.09, 31.02], BoolType), None, None), VarDecl(Id(Qp), ArrayType([3.72, 85.59, 86.28], BoolType), None, None)], Return()), VarDecl(Id(IB58), ArrayType([4.2, 16.72, 29.83], BoolType), None, Id(M4))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115027))

	def test_21530115028(self):
		input = '''
func n5 (bool bpqZ[2.65,69.34,80.23], string OE[6.02], bool cb7[92.83,32.86,53.51])
	begin
	end

dynamic BNHB
'''
		expect = '''Program([FuncDecl(Id(n5), [VarDecl(Id(bpqZ), ArrayType([2.65, 69.34, 80.23], BoolType), None, None), VarDecl(Id(OE), ArrayType([6.02], StringType), None, None), VarDecl(Id(cb7), ArrayType([92.83, 32.86, 53.51], BoolType), None, None)], Block([])), VarDecl(Id(BNHB), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115028))

	def test_21530115029(self):
		input = '''
var yJ <- true
func hDd (bool bx5[38.62])	begin
		begin
			break
			for XLGA until false by 8.11
				begin
					DNAc("NU", 65.4, lmSw)
					continue
					if (true)
					begin
						break
						for KIe until "DbM" by YAI
							break
					end
					elif (65.28)
					return FK
					elif (25.41)
					s9s(true, "KZU")
					elif (MFSP)
					break
					elif (1.57)
					return
					elif ("XB")
					for iW until hfmz by "LaWkS"
						return
					else return
				end
		end
	end
func oXD (bool WOA[60.53,87.39], string zcL[30.85,98.95], bool t7q[12.85,59.18,65.97])	begin
		bool wy5
		continue
		break
	end
bool Pw
'''
		expect = '''Program([VarDecl(Id(yJ), None, var, BooleanLit(True)), FuncDecl(Id(hDd), [VarDecl(Id(bx5), ArrayType([38.62], BoolType), None, None)], Block([Block([Break, For(Id(XLGA), BooleanLit(False), NumLit(8.11), Block([CallStmt(Id(DNAc), [StringLit(NU), NumLit(65.4), Id(lmSw)]), Continue, If(BooleanLit(True), Block([Break, For(Id(KIe), StringLit(DbM), Id(YAI), Break)])), [(NumLit(65.28), Return(Id(FK))), (NumLit(25.41), CallStmt(Id(s9s), [BooleanLit(True), StringLit(KZU)])), (Id(MFSP), Break), (NumLit(1.57), Return()), (StringLit(XB), For(Id(iW), Id(hfmz), StringLit(LaWkS), Return()))], Return()]))])])), FuncDecl(Id(oXD), [VarDecl(Id(WOA), ArrayType([60.53, 87.39], BoolType), None, None), VarDecl(Id(zcL), ArrayType([30.85, 98.95], StringType), None, None), VarDecl(Id(t7q), ArrayType([12.85, 59.18, 65.97], BoolType), None, None)], Block([VarDecl(Id(wy5), BoolType, None, None), Continue, Break])), VarDecl(Id(Pw), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115029))

	def test_21530115030(self):
		input = '''
string I6[30.6,83.49] <- RB8F
'''
		expect = '''Program([VarDecl(Id(I6), ArrayType([30.6, 83.49], StringType), None, Id(RB8F))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115030))

	def test_21530115031(self):
		input = '''
number Kd3[80.76,67.94]
'''
		expect = '''Program([VarDecl(Id(Kd3), ArrayType([80.76, 67.94], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115031))

	def test_21530115032(self):
		input = '''
string QSbW <- 31.18
func Os (number Am[65.85], string t2[79.7])	return
func koED (bool hHI, number kDI, number ROiN)	return
'''
		expect = '''Program([VarDecl(Id(QSbW), StringType, None, NumLit(31.18)), FuncDecl(Id(Os), [VarDecl(Id(Am), ArrayType([65.85], NumberType), None, None), VarDecl(Id(t2), ArrayType([79.7], StringType), None, None)], Return()), FuncDecl(Id(koED), [VarDecl(Id(hHI), BoolType, None, None), VarDecl(Id(kDI), NumberType, None, None), VarDecl(Id(ROiN), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115032))

	def test_21530115033(self):
		input = '''
func yJfa (bool lylt, bool VE, string vn7J)	return
string CDh
dynamic zvg
var aB <- false
bool NWcP[1.53,57.34] <- "VWwZd"
'''
		expect = '''Program([FuncDecl(Id(yJfa), [VarDecl(Id(lylt), BoolType, None, None), VarDecl(Id(VE), BoolType, None, None), VarDecl(Id(vn7J), StringType, None, None)], Return()), VarDecl(Id(CDh), StringType, None, None), VarDecl(Id(zvg), None, dynamic, None), VarDecl(Id(aB), None, var, BooleanLit(False)), VarDecl(Id(NWcP), ArrayType([1.53, 57.34], BoolType), None, StringLit(VWwZd))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115033))

	def test_21530115034(self):
		input = '''
number duU[96.42,77.02] <- 2.02
bool sd
'''
		expect = '''Program([VarDecl(Id(duU), ArrayType([96.42, 77.02], NumberType), None, NumLit(2.02)), VarDecl(Id(sd), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115034))

	def test_21530115035(self):
		input = '''
var Wb <- "tBFB"
'''
		expect = '''Program([VarDecl(Id(Wb), None, var, StringLit(tBFB))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115035))

	def test_21530115036(self):
		input = '''
var wWF <- "Est"
func HhAp (number Q5[58.21], number Oft[78.88,80.79,75.96], string AEl)	begin
		if (opW5)
		for weh until fu4 by false
			continue
		elif ("C") var QGK <- "ZOY"
		string qsX[62.71] <- true
		continue
	end
'''
		expect = '''Program([VarDecl(Id(wWF), None, var, StringLit(Est)), FuncDecl(Id(HhAp), [VarDecl(Id(Q5), ArrayType([58.21], NumberType), None, None), VarDecl(Id(Oft), ArrayType([78.88, 80.79, 75.96], NumberType), None, None), VarDecl(Id(AEl), StringType, None, None)], Block([If(Id(opW5), For(Id(weh), Id(fu4), BooleanLit(False), Continue)), [(StringLit(C), VarDecl(Id(QGK), None, var, StringLit(ZOY)))], None, VarDecl(Id(qsX), ArrayType([62.71], StringType), None, BooleanLit(True)), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115036))

	def test_21530115037(self):
		input = '''
func fs ()	begin
		string Axw[2.09,33.15] <- 71.12
	end
func nWRd (number M1, string adh9[71.06], string by8z)
	return

func ou (number DQ2K[17.25,80.81,45.04], string TVp[57.63,34.75])	return true
'''
		expect = '''Program([FuncDecl(Id(fs), [], Block([VarDecl(Id(Axw), ArrayType([2.09, 33.15], StringType), None, NumLit(71.12))])), FuncDecl(Id(nWRd), [VarDecl(Id(M1), NumberType, None, None), VarDecl(Id(adh9), ArrayType([71.06], StringType), None, None), VarDecl(Id(by8z), StringType, None, None)], Return()), FuncDecl(Id(ou), [VarDecl(Id(DQ2K), ArrayType([17.25, 80.81, 45.04], NumberType), None, None), VarDecl(Id(TVp), ArrayType([57.63, 34.75], StringType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115037))

	def test_21530115038(self):
		input = '''
func BFFX ()
	begin
	end

number uFwV[28.01]
func hES ()	return
func mrnj (bool vqW, string Ta[65.91,96.2])	return 79.48
string TNZ[53.36] <- ca
'''
		expect = '''Program([FuncDecl(Id(BFFX), [], Block([])), VarDecl(Id(uFwV), ArrayType([28.01], NumberType), None, None), FuncDecl(Id(hES), [], Return()), FuncDecl(Id(mrnj), [VarDecl(Id(vqW), BoolType, None, None), VarDecl(Id(Ta), ArrayType([65.91, 96.2], StringType), None, None)], Return(NumLit(79.48))), VarDecl(Id(TNZ), ArrayType([53.36], StringType), None, Id(ca))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115038))

	def test_21530115039(self):
		input = '''
var NgDx <- 16.38
func M_L (string Vofa[95.04])	return 65.78

'''
		expect = '''Program([VarDecl(Id(NgDx), None, var, NumLit(16.38)), FuncDecl(Id(M_L), [VarDecl(Id(Vofa), ArrayType([95.04], StringType), None, None)], Return(NumLit(65.78)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115039))

	def test_21530115040(self):
		input = '''
var BBSq <- false
string sX[59.38,82.77,84.82]
number vnLo[55.78,51.76,11.37] <- 63.92
string QM[14.55,98.73]
'''
		expect = '''Program([VarDecl(Id(BBSq), None, var, BooleanLit(False)), VarDecl(Id(sX), ArrayType([59.38, 82.77, 84.82], StringType), None, None), VarDecl(Id(vnLo), ArrayType([55.78, 51.76, 11.37], NumberType), None, NumLit(63.92)), VarDecl(Id(QM), ArrayType([14.55, 98.73], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115040))

	def test_21530115041(self):
		input = '''
func Hj (string SYQd[75.21,59.95,99.34], bool nU[97.31,28.5,94.43])	return "x"

string A5CG[30.08] <- true
'''
		expect = '''Program([FuncDecl(Id(Hj), [VarDecl(Id(SYQd), ArrayType([75.21, 59.95, 99.34], StringType), None, None), VarDecl(Id(nU), ArrayType([97.31, 28.5, 94.43], BoolType), None, None)], Return(StringLit(x))), VarDecl(Id(A5CG), ArrayType([30.08], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115041))

	def test_21530115042(self):
		input = '''
dynamic y7 <- "Z"
dynamic yo5q <- 47.12
'''
		expect = '''Program([VarDecl(Id(y7), None, dynamic, StringLit(Z)), VarDecl(Id(yo5q), None, dynamic, NumLit(47.12))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115042))

	def test_21530115043(self):
		input = '''
func Bp3u ()	return

func p0r ()	return 41.34

func R64K (string BpkJ[3.64,27.94,40.25], string JWWa[79.42,39.69,66.47], string s2C[37.82,7.88,18.33])
	return
dynamic Hr <- tX
func g2 (number hnf, string aTB)	return u6g

'''
		expect = '''Program([FuncDecl(Id(Bp3u), [], Return()), FuncDecl(Id(p0r), [], Return(NumLit(41.34))), FuncDecl(Id(R64K), [VarDecl(Id(BpkJ), ArrayType([3.64, 27.94, 40.25], StringType), None, None), VarDecl(Id(JWWa), ArrayType([79.42, 39.69, 66.47], StringType), None, None), VarDecl(Id(s2C), ArrayType([37.82, 7.88, 18.33], StringType), None, None)], Return()), VarDecl(Id(Hr), None, dynamic, Id(tX)), FuncDecl(Id(g2), [VarDecl(Id(hnf), NumberType, None, None), VarDecl(Id(aTB), StringType, None, None)], Return(Id(u6g)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115043))

	def test_21530115044(self):
		input = '''
var S2w <- 25.58
func Dpo (string k4Ls, string Uj[36.52,58.03,83.1])	begin
		return
	end
func dNc ()	begin
		HkoK()
		break
		continue
	end

func qJH (string sn, number cfng[47.56])	return

func Fz ()	return "cPIms"

'''
		expect = '''Program([VarDecl(Id(S2w), None, var, NumLit(25.58)), FuncDecl(Id(Dpo), [VarDecl(Id(k4Ls), StringType, None, None), VarDecl(Id(Uj), ArrayType([36.52, 58.03, 83.1], StringType), None, None)], Block([Return()])), FuncDecl(Id(dNc), [], Block([CallStmt(Id(HkoK), []), Break, Continue])), FuncDecl(Id(qJH), [VarDecl(Id(sn), StringType, None, None), VarDecl(Id(cfng), ArrayType([47.56], NumberType), None, None)], Return()), FuncDecl(Id(Fz), [], Return(StringLit(cPIms)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115044))

	def test_21530115045(self):
		input = '''
func PE (number so[53.22,64.58])	return true

func jb (bool yp[69.89,75.5], number fp[90.61], string iYH[34.48])	return

func Ugt (number Gn)
	return "hrh"
'''
		expect = '''Program([FuncDecl(Id(PE), [VarDecl(Id(so), ArrayType([53.22, 64.58], NumberType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(jb), [VarDecl(Id(yp), ArrayType([69.89, 75.5], BoolType), None, None), VarDecl(Id(fp), ArrayType([90.61], NumberType), None, None), VarDecl(Id(iYH), ArrayType([34.48], StringType), None, None)], Return()), FuncDecl(Id(Ugt), [VarDecl(Id(Gn), NumberType, None, None)], Return(StringLit(hrh)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115045))

	def test_21530115046(self):
		input = '''
func e8y2 (number Rx8P[83.42], number sj9E[73.91,38.51])	begin
	end
bool tIWX <- "HLQV"
'''
		expect = '''Program([FuncDecl(Id(e8y2), [VarDecl(Id(Rx8P), ArrayType([83.42], NumberType), None, None), VarDecl(Id(sj9E), ArrayType([73.91, 38.51], NumberType), None, None)], Block([])), VarDecl(Id(tIWX), BoolType, None, StringLit(HLQV))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115046))

	def test_21530115047(self):
		input = '''
func bZ2 (number RV[40.99], bool IVii)	return
func k_ (bool xV5U, number xGrF[48.82], string JLrb)	return
number AuY
func YvT (number NxM, number Jp[27.4,81.66,62.59])
	return "bsOV"

'''
		expect = '''Program([FuncDecl(Id(bZ2), [VarDecl(Id(RV), ArrayType([40.99], NumberType), None, None), VarDecl(Id(IVii), BoolType, None, None)], Return()), FuncDecl(Id(k_), [VarDecl(Id(xV5U), BoolType, None, None), VarDecl(Id(xGrF), ArrayType([48.82], NumberType), None, None), VarDecl(Id(JLrb), StringType, None, None)], Return()), VarDecl(Id(AuY), NumberType, None, None), FuncDecl(Id(YvT), [VarDecl(Id(NxM), NumberType, None, None), VarDecl(Id(Jp), ArrayType([27.4, 81.66, 62.59], NumberType), None, None)], Return(StringLit(bsOV)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115047))

	def test_21530115048(self):
		input = '''
func ot ()
	return 29.0
string I7[14.81,44.66,3.92] <- true
'''
		expect = '''Program([FuncDecl(Id(ot), [], Return(NumLit(29.0))), VarDecl(Id(I7), ArrayType([14.81, 44.66, 3.92], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115048))

	def test_21530115049(self):
		input = '''
func ORx (bool mh, bool ywB[32.47,7.44,94.92])	return UIZQ

func GE (string sVC, number CX[26.82])	return

'''
		expect = '''Program([FuncDecl(Id(ORx), [VarDecl(Id(mh), BoolType, None, None), VarDecl(Id(ywB), ArrayType([32.47, 7.44, 94.92], BoolType), None, None)], Return(Id(UIZQ))), FuncDecl(Id(GE), [VarDecl(Id(sVC), StringType, None, None), VarDecl(Id(CX), ArrayType([26.82], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115049))

	def test_21530115050(self):
		input = '''
func tY (bool cI[72.1], bool cTU[47.46], string RFJ[39.46,17.11])	begin
		return false
	end

func EoqO (string YHG)
	return 41.98
func Av3O (number mD[38.66,98.69,74.95], string wIF)
	return 35.12

'''
		expect = '''Program([FuncDecl(Id(tY), [VarDecl(Id(cI), ArrayType([72.1], BoolType), None, None), VarDecl(Id(cTU), ArrayType([47.46], BoolType), None, None), VarDecl(Id(RFJ), ArrayType([39.46, 17.11], StringType), None, None)], Block([Return(BooleanLit(False))])), FuncDecl(Id(EoqO), [VarDecl(Id(YHG), StringType, None, None)], Return(NumLit(41.98))), FuncDecl(Id(Av3O), [VarDecl(Id(mD), ArrayType([38.66, 98.69, 74.95], NumberType), None, None), VarDecl(Id(wIF), StringType, None, None)], Return(NumLit(35.12)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115050))

	def test_21530115051(self):
		input = '''
var sZq <- Pm
'''
		expect = '''Program([VarDecl(Id(sZq), None, var, Id(Pm))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115051))

	def test_21530115052(self):
		input = '''
number IgO[66.69] <- "vFA"
func x8 (string RMU[32.24,82.19], string Sy)
	begin
		begin
			bool pCh
			continue
		end
	end
'''
		expect = '''Program([VarDecl(Id(IgO), ArrayType([66.69], NumberType), None, StringLit(vFA)), FuncDecl(Id(x8), [VarDecl(Id(RMU), ArrayType([32.24, 82.19], StringType), None, None), VarDecl(Id(Sy), StringType, None, None)], Block([Block([VarDecl(Id(pCh), BoolType, None, None), Continue])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115052))

	def test_21530115053(self):
		input = '''
func Xi9D (bool Itv[82.48], number Bgi[42.31])
	return

var F4Ap <- false
func x1u (string xB, bool FHdn, string RY[36.17,80.41,34.34])	return

'''
		expect = '''Program([FuncDecl(Id(Xi9D), [VarDecl(Id(Itv), ArrayType([82.48], BoolType), None, None), VarDecl(Id(Bgi), ArrayType([42.31], NumberType), None, None)], Return()), VarDecl(Id(F4Ap), None, var, BooleanLit(False)), FuncDecl(Id(x1u), [VarDecl(Id(xB), StringType, None, None), VarDecl(Id(FHdn), BoolType, None, None), VarDecl(Id(RY), ArrayType([36.17, 80.41, 34.34], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115053))

	def test_21530115054(self):
		input = '''
bool NP0 <- "sBvz"
number drw7[45.63,94.99,50.12]
'''
		expect = '''Program([VarDecl(Id(NP0), BoolType, None, StringLit(sBvz)), VarDecl(Id(drw7), ArrayType([45.63, 94.99, 50.12], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115054))

	def test_21530115055(self):
		input = '''
func mEGx ()	return 61.54

'''
		expect = '''Program([FuncDecl(Id(mEGx), [], Return(NumLit(61.54)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115055))

	def test_21530115056(self):
		input = '''
string xuhG <- true
string gQ[92.64,11.5,16.26] <- 5.66
func Dt (bool csu4, string yalc[28.86], number Xzg)
	return

'''
		expect = '''Program([VarDecl(Id(xuhG), StringType, None, BooleanLit(True)), VarDecl(Id(gQ), ArrayType([92.64, 11.5, 16.26], StringType), None, NumLit(5.66)), FuncDecl(Id(Dt), [VarDecl(Id(csu4), BoolType, None, None), VarDecl(Id(yalc), ArrayType([28.86], StringType), None, None), VarDecl(Id(Xzg), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115056))

	def test_21530115057(self):
		input = '''
func VuV1 (number Ko3n)
	return
func Ud (string HK[14.38,60.14,40.62], number huA5, bool iyj[20.51])
	return 44.58
func xmzZ ()
	return

func l6 (string esrj)	return 27.23

'''
		expect = '''Program([FuncDecl(Id(VuV1), [VarDecl(Id(Ko3n), NumberType, None, None)], Return()), FuncDecl(Id(Ud), [VarDecl(Id(HK), ArrayType([14.38, 60.14, 40.62], StringType), None, None), VarDecl(Id(huA5), NumberType, None, None), VarDecl(Id(iyj), ArrayType([20.51], BoolType), None, None)], Return(NumLit(44.58))), FuncDecl(Id(xmzZ), [], Return()), FuncDecl(Id(l6), [VarDecl(Id(esrj), StringType, None, None)], Return(NumLit(27.23)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115057))

	def test_21530115058(self):
		input = '''
number fkFw <- 98.32
'''
		expect = '''Program([VarDecl(Id(fkFw), NumberType, None, NumLit(98.32))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115058))

	def test_21530115059(self):
		input = '''
func M1G6 (string xP, bool BR[37.85,56.29], number mH1m)
	return "vCRg"

func NC (string sK, string q1t)
	begin
		begin
			number Ap[5.57,87.88] <- "r"
			break
			continue
		end
	end

func tY ()	begin
		string jIf[91.97,49.34,27.13]
		return
		mo8p()
	end
string PvLW
'''
		expect = '''Program([FuncDecl(Id(M1G6), [VarDecl(Id(xP), StringType, None, None), VarDecl(Id(BR), ArrayType([37.85, 56.29], BoolType), None, None), VarDecl(Id(mH1m), NumberType, None, None)], Return(StringLit(vCRg))), FuncDecl(Id(NC), [VarDecl(Id(sK), StringType, None, None), VarDecl(Id(q1t), StringType, None, None)], Block([Block([VarDecl(Id(Ap), ArrayType([5.57, 87.88], NumberType), None, StringLit(r)), Break, Continue])])), FuncDecl(Id(tY), [], Block([VarDecl(Id(jIf), ArrayType([91.97, 49.34, 27.13], StringType), None, None), Return(), CallStmt(Id(mo8p), [])])), VarDecl(Id(PvLW), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115059))

	def test_21530115060(self):
		input = '''
bool RS[54.6,11.37] <- "YmRD"
bool qk[46.83,49.91,7.41]
'''
		expect = '''Program([VarDecl(Id(RS), ArrayType([54.6, 11.37], BoolType), None, StringLit(YmRD)), VarDecl(Id(qk), ArrayType([46.83, 49.91, 7.41], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115060))

	def test_21530115061(self):
		input = '''
func Lwlj (string ZjsU[80.59,8.53,99.56], number vP3w)	return true
func dA (number C_k, number CB[21.76,6.92,76.48], number rjD)	return
func b4fZ (string Wt[94.27,8.28], string nAox[72.53], number GBxH[86.51,96.87,11.96])
	return "kgifx"

func pGN (number ksp[7.78,92.42], number oe[40.82])
	return

func rx8 (number gAae[67.04,6.04,5.1], string q49, string FDN)
	return

'''
		expect = '''Program([FuncDecl(Id(Lwlj), [VarDecl(Id(ZjsU), ArrayType([80.59, 8.53, 99.56], StringType), None, None), VarDecl(Id(vP3w), NumberType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(dA), [VarDecl(Id(C_k), NumberType, None, None), VarDecl(Id(CB), ArrayType([21.76, 6.92, 76.48], NumberType), None, None), VarDecl(Id(rjD), NumberType, None, None)], Return()), FuncDecl(Id(b4fZ), [VarDecl(Id(Wt), ArrayType([94.27, 8.28], StringType), None, None), VarDecl(Id(nAox), ArrayType([72.53], StringType), None, None), VarDecl(Id(GBxH), ArrayType([86.51, 96.87, 11.96], NumberType), None, None)], Return(StringLit(kgifx))), FuncDecl(Id(pGN), [VarDecl(Id(ksp), ArrayType([7.78, 92.42], NumberType), None, None), VarDecl(Id(oe), ArrayType([40.82], NumberType), None, None)], Return()), FuncDecl(Id(rx8), [VarDecl(Id(gAae), ArrayType([67.04, 6.04, 5.1], NumberType), None, None), VarDecl(Id(q49), StringType, None, None), VarDecl(Id(FDN), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115061))

	def test_21530115062(self):
		input = '''
bool PN5j[22.33,73.87]
'''
		expect = '''Program([VarDecl(Id(PN5j), ArrayType([22.33, 73.87], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115062))

	def test_21530115063(self):
		input = '''
bool ed[69.39,4.8] <- "BYhfw"
func LpVS (bool xN, string uRL[59.31])	begin
	end
func ts4 (bool r34G[81.87,49.08,16.06], string PR, number ejoj[68.56])	return

'''
		expect = '''Program([VarDecl(Id(ed), ArrayType([69.39, 4.8], BoolType), None, StringLit(BYhfw)), FuncDecl(Id(LpVS), [VarDecl(Id(xN), BoolType, None, None), VarDecl(Id(uRL), ArrayType([59.31], StringType), None, None)], Block([])), FuncDecl(Id(ts4), [VarDecl(Id(r34G), ArrayType([81.87, 49.08, 16.06], BoolType), None, None), VarDecl(Id(PR), StringType, None, None), VarDecl(Id(ejoj), ArrayType([68.56], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115063))

	def test_21530115064(self):
		input = '''
func nPCW (number XA, string Cj7)
	begin
	end
func Vj (number I0km)	return
'''
		expect = '''Program([FuncDecl(Id(nPCW), [VarDecl(Id(XA), NumberType, None, None), VarDecl(Id(Cj7), StringType, None, None)], Block([])), FuncDecl(Id(Vj), [VarDecl(Id(I0km), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115064))

	def test_21530115065(self):
		input = '''
func IRf ()	return rHWk

func a6gi ()	return "bfy"
func QIi (bool GgG[81.68,20.44], bool SOj4, number Qcd[47.77,60.01,62.52])
	return "M"
number OMie
'''
		expect = '''Program([FuncDecl(Id(IRf), [], Return(Id(rHWk))), FuncDecl(Id(a6gi), [], Return(StringLit(bfy))), FuncDecl(Id(QIi), [VarDecl(Id(GgG), ArrayType([81.68, 20.44], BoolType), None, None), VarDecl(Id(SOj4), BoolType, None, None), VarDecl(Id(Qcd), ArrayType([47.77, 60.01, 62.52], NumberType), None, None)], Return(StringLit(M))), VarDecl(Id(OMie), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115065))

	def test_21530115066(self):
		input = '''
func Aq (string la7Q)
	begin
		string b6z[92.57,13.34]
		if ("E")
		for wF until 78.03 by false
			continue
		elif (true) for Z9 until false by "dP"
			bool pnE
		elif (84.98) if (gQ) for UuR0 until 91.99 by eX
			if (63.98)
			begin
			end
			elif (53.65)
			GSJo()
			elif (zn)
			continue
			else begin
			end
		elif (88.13) return 89.16
		elif (false) if (false) Zjhs(false, 12.7, true)
		elif (SoL) if (cL)
		Eh3U <- true
		elif (75.85) for lu until qc0Q by true
			begin
				rBJI("zGNBM", 38.63, false)
			end
		elif (true)
		number E1I[30.06,63.59,43.86] <- 36.65
		elif (false) dynamic QjGr <- "P"
		elif (QBu)
		string Mn[11.4,61.0,86.41]
		else var ryG <- 35.85
		kh[76.43, true] <- 69.74
	end

func ZnM (string RbFA[83.65,30.52])	begin
		CzP()
		TH6b <- "DwSAi"
		kJ(false)
	end

'''
		expect = '''Program([FuncDecl(Id(Aq), [VarDecl(Id(la7Q), StringType, None, None)], Block([VarDecl(Id(b6z), ArrayType([92.57, 13.34], StringType), None, None), If(StringLit(E), For(Id(wF), NumLit(78.03), BooleanLit(False), Continue)), [(BooleanLit(True), For(Id(Z9), BooleanLit(False), StringLit(dP), VarDecl(Id(pnE), BoolType, None, None))), (NumLit(84.98), If(Id(gQ), For(Id(UuR0), NumLit(91.99), Id(eX), If(NumLit(63.98), Block([])), [(NumLit(53.65), CallStmt(Id(GSJo), [])), (Id(zn), Continue)], Block([]))), [(NumLit(88.13), Return(NumLit(89.16))), (BooleanLit(False), If(BooleanLit(False), CallStmt(Id(Zjhs), [BooleanLit(False), NumLit(12.7), BooleanLit(True)])), [(Id(SoL), If(Id(cL), AssignStmt(Id(Eh3U), BooleanLit(True))), [(NumLit(75.85), For(Id(lu), Id(qc0Q), BooleanLit(True), Block([CallStmt(Id(rBJI), [StringLit(zGNBM), NumLit(38.63), BooleanLit(False)])])))], None), (BooleanLit(True), VarDecl(Id(E1I), ArrayType([30.06, 63.59, 43.86], NumberType), None, NumLit(36.65)))], None), (BooleanLit(False), VarDecl(Id(QjGr), None, dynamic, StringLit(P)))], None), (Id(QBu), VarDecl(Id(Mn), ArrayType([11.4, 61.0, 86.41], StringType), None, None))], VarDecl(Id(ryG), None, var, NumLit(35.85)), AssignStmt(ArrayCell(Id(kh), [NumLit(76.43), BooleanLit(True)]), NumLit(69.74))])), FuncDecl(Id(ZnM), [VarDecl(Id(RbFA), ArrayType([83.65, 30.52], StringType), None, None)], Block([CallStmt(Id(CzP), []), AssignStmt(Id(TH6b), StringLit(DwSAi)), CallStmt(Id(kJ), [BooleanLit(False)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115066))

	def test_21530115067(self):
		input = '''
bool kbFq[62.51,24.9]
string JqoX[56.08,77.27,22.35]
'''
		expect = '''Program([VarDecl(Id(kbFq), ArrayType([62.51, 24.9], BoolType), None, None), VarDecl(Id(JqoX), ArrayType([56.08, 77.27, 22.35], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115067))

	def test_21530115068(self):
		input = '''
func Te (string FW2, bool Oo1[84.17,35.04,47.37], number uBf[1.47,17.59])	return
string a8[65.03,70.73,83.96] <- fu
'''
		expect = '''Program([FuncDecl(Id(Te), [VarDecl(Id(FW2), StringType, None, None), VarDecl(Id(Oo1), ArrayType([84.17, 35.04, 47.37], BoolType), None, None), VarDecl(Id(uBf), ArrayType([1.47, 17.59], NumberType), None, None)], Return()), VarDecl(Id(a8), ArrayType([65.03, 70.73, 83.96], StringType), None, Id(fu))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115068))

	def test_21530115069(self):
		input = '''
func feAM ()
	return
'''
		expect = '''Program([FuncDecl(Id(feAM), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115069))

	def test_21530115070(self):
		input = '''
dynamic sFx
'''
		expect = '''Program([VarDecl(Id(sFx), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115070))

	def test_21530115071(self):
		input = '''
func GdV (bool Z_9[89.98], bool UNl1, string DH)
	return

func Ol9w ()	return
dynamic qD
func dFhF (bool FRaX[56.93,57.18])	begin
		continue
		return
		continue
	end

string Yo[49.92,92.52] <- false
'''
		expect = '''Program([FuncDecl(Id(GdV), [VarDecl(Id(Z_9), ArrayType([89.98], BoolType), None, None), VarDecl(Id(UNl1), BoolType, None, None), VarDecl(Id(DH), StringType, None, None)], Return()), FuncDecl(Id(Ol9w), [], Return()), VarDecl(Id(qD), None, dynamic, None), FuncDecl(Id(dFhF), [VarDecl(Id(FRaX), ArrayType([56.93, 57.18], BoolType), None, None)], Block([Continue, Return(), Continue])), VarDecl(Id(Yo), ArrayType([49.92, 92.52], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115071))

	def test_21530115072(self):
		input = '''
dynamic TUV
'''
		expect = '''Program([VarDecl(Id(TUV), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115072))

	def test_21530115073(self):
		input = '''
var q0 <- "QtT"
func oi (bool WogM[76.48,64.18,58.15], bool o5LN[90.01,24.35], bool L1U)
	return

func BRHw (number YP[71.33], number iJ6)
	begin
		break
		begin
		end
		aumO(vxh_, false)
	end

'''
		expect = '''Program([VarDecl(Id(q0), None, var, StringLit(QtT)), FuncDecl(Id(oi), [VarDecl(Id(WogM), ArrayType([76.48, 64.18, 58.15], BoolType), None, None), VarDecl(Id(o5LN), ArrayType([90.01, 24.35], BoolType), None, None), VarDecl(Id(L1U), BoolType, None, None)], Return()), FuncDecl(Id(BRHw), [VarDecl(Id(YP), ArrayType([71.33], NumberType), None, None), VarDecl(Id(iJ6), NumberType, None, None)], Block([Break, Block([]), CallStmt(Id(aumO), [Id(vxh_), BooleanLit(False)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115073))

	def test_21530115074(self):
		input = '''
string l6
func Q9YB (number heF[31.08,61.62])
	return 73.08
var nt0 <- 23.84
'''
		expect = '''Program([VarDecl(Id(l6), StringType, None, None), FuncDecl(Id(Q9YB), [VarDecl(Id(heF), ArrayType([31.08, 61.62], NumberType), None, None)], Return(NumLit(73.08))), VarDecl(Id(nt0), None, var, NumLit(23.84))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115074))

	def test_21530115075(self):
		input = '''
string Htm <- true
number XN
func iO7Q (string Ozy[41.63], number d3M1[89.74,65.18,76.15], number SH[19.83,39.19])
	begin
		var JTRe <- "HN"
		break
	end

'''
		expect = '''Program([VarDecl(Id(Htm), StringType, None, BooleanLit(True)), VarDecl(Id(XN), NumberType, None, None), FuncDecl(Id(iO7Q), [VarDecl(Id(Ozy), ArrayType([41.63], StringType), None, None), VarDecl(Id(d3M1), ArrayType([89.74, 65.18, 76.15], NumberType), None, None), VarDecl(Id(SH), ArrayType([19.83, 39.19], NumberType), None, None)], Block([VarDecl(Id(JTRe), None, var, StringLit(HN)), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115075))

	def test_21530115076(self):
		input = '''
func zGlT (string J9[61.04], bool Zx4[81.45,45.28,26.97], string zf3[88.46,20.42])
	begin
		EZlo <- "g"
		SI(false, 17.73, Kx)
		break
	end

var Ee <- true
func kD ()
	return wbM
string zkJ <- 34.48
var w_x <- d9
'''
		expect = '''Program([FuncDecl(Id(zGlT), [VarDecl(Id(J9), ArrayType([61.04], StringType), None, None), VarDecl(Id(Zx4), ArrayType([81.45, 45.28, 26.97], BoolType), None, None), VarDecl(Id(zf3), ArrayType([88.46, 20.42], StringType), None, None)], Block([AssignStmt(Id(EZlo), StringLit(g)), CallStmt(Id(SI), [BooleanLit(False), NumLit(17.73), Id(Kx)]), Break])), VarDecl(Id(Ee), None, var, BooleanLit(True)), FuncDecl(Id(kD), [], Return(Id(wbM))), VarDecl(Id(zkJ), StringType, None, NumLit(34.48)), VarDecl(Id(w_x), None, var, Id(d9))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115076))

	def test_21530115077(self):
		input = '''
bool Kp[79.35,28.66]
number iY1 <- 36.69
'''
		expect = '''Program([VarDecl(Id(Kp), ArrayType([79.35, 28.66], BoolType), None, None), VarDecl(Id(iY1), NumberType, None, NumLit(36.69))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115077))

	def test_21530115078(self):
		input = '''
func C98O (string cKLN, bool kFme, bool Dvo[91.74,8.57])
	begin
		qe()
		return false
	end

func Fw0 (number Juz[72.72,25.77])
	return qRaW
func b9k9 (number Nv[16.18,51.03,38.48])	return
'''
		expect = '''Program([FuncDecl(Id(C98O), [VarDecl(Id(cKLN), StringType, None, None), VarDecl(Id(kFme), BoolType, None, None), VarDecl(Id(Dvo), ArrayType([91.74, 8.57], BoolType), None, None)], Block([CallStmt(Id(qe), []), Return(BooleanLit(False))])), FuncDecl(Id(Fw0), [VarDecl(Id(Juz), ArrayType([72.72, 25.77], NumberType), None, None)], Return(Id(qRaW))), FuncDecl(Id(b9k9), [VarDecl(Id(Nv), ArrayType([16.18, 51.03, 38.48], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115078))

	def test_21530115079(self):
		input = '''
func ykF (bool nD, string bBc[88.95])	begin
		return false
	end

func fJTI (bool TKiG, number D35J[57.85,6.6], bool I2)
	begin
		break
	end

dynamic M5e <- "jSau"
func Ebw (string cmA)	begin
		break
	end

'''
		expect = '''Program([FuncDecl(Id(ykF), [VarDecl(Id(nD), BoolType, None, None), VarDecl(Id(bBc), ArrayType([88.95], StringType), None, None)], Block([Return(BooleanLit(False))])), FuncDecl(Id(fJTI), [VarDecl(Id(TKiG), BoolType, None, None), VarDecl(Id(D35J), ArrayType([57.85, 6.6], NumberType), None, None), VarDecl(Id(I2), BoolType, None, None)], Block([Break])), VarDecl(Id(M5e), None, dynamic, StringLit(jSau)), FuncDecl(Id(Ebw), [VarDecl(Id(cmA), StringType, None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115079))

	def test_21530115080(self):
		input = '''
func o0s ()
	begin
		begin
			rE <- "i"
			begin
				lCKT <- rg
			end
			return HVkW
		end
		return "LJlZ"
	end

number Hf
func PIt ()
	return "RfsG"
bool t2
'''
		expect = '''Program([FuncDecl(Id(o0s), [], Block([Block([AssignStmt(Id(rE), StringLit(i)), Block([AssignStmt(Id(lCKT), Id(rg))]), Return(Id(HVkW))]), Return(StringLit(LJlZ))])), VarDecl(Id(Hf), NumberType, None, None), FuncDecl(Id(PIt), [], Return(StringLit(RfsG))), VarDecl(Id(t2), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115080))

	def test_21530115081(self):
		input = '''
number An9[51.23,3.7,39.78]
string XPA[0.42,90.21] <- "ngh"
string dp_[55.36,76.42,2.78]
number U1P[57.5,71.87,46.65] <- false
number bz6D[94.35,63.82] <- "frPr"
'''
		expect = '''Program([VarDecl(Id(An9), ArrayType([51.23, 3.7, 39.78], NumberType), None, None), VarDecl(Id(XPA), ArrayType([0.42, 90.21], StringType), None, StringLit(ngh)), VarDecl(Id(dp_), ArrayType([55.36, 76.42, 2.78], StringType), None, None), VarDecl(Id(U1P), ArrayType([57.5, 71.87, 46.65], NumberType), None, BooleanLit(False)), VarDecl(Id(bz6D), ArrayType([94.35, 63.82], NumberType), None, StringLit(frPr))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115081))

	def test_21530115082(self):
		input = '''
var t7G <- true
'''
		expect = '''Program([VarDecl(Id(t7G), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115082))

	def test_21530115083(self):
		input = '''
func sS (string sHI[44.87], string sb[32.51,69.08])
	begin
		break
		bool huH[91.53,16.51]
	end

func tE4 (bool i0)
	return

func STgT (string rj[8.37,99.6,9.72])	return true

'''
		expect = '''Program([FuncDecl(Id(sS), [VarDecl(Id(sHI), ArrayType([44.87], StringType), None, None), VarDecl(Id(sb), ArrayType([32.51, 69.08], StringType), None, None)], Block([Break, VarDecl(Id(huH), ArrayType([91.53, 16.51], BoolType), None, None)])), FuncDecl(Id(tE4), [VarDecl(Id(i0), BoolType, None, None)], Return()), FuncDecl(Id(STgT), [VarDecl(Id(rj), ArrayType([8.37, 99.6, 9.72], StringType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115083))

	def test_21530115084(self):
		input = '''
func lYIl (string P4[96.66,85.35], bool rI, number ynVi)	return
bool cpck[8.48] <- "MvxWa"
func Am ()	begin
		for lFG until true by "xA"
			begin
				for rad until Hp by 92.46
					number pIMO[76.29,73.14,15.79]
			end
		begin
		end
		continue
	end
'''
		expect = '''Program([FuncDecl(Id(lYIl), [VarDecl(Id(P4), ArrayType([96.66, 85.35], StringType), None, None), VarDecl(Id(rI), BoolType, None, None), VarDecl(Id(ynVi), NumberType, None, None)], Return()), VarDecl(Id(cpck), ArrayType([8.48], BoolType), None, StringLit(MvxWa)), FuncDecl(Id(Am), [], Block([For(Id(lFG), BooleanLit(True), StringLit(xA), Block([For(Id(rad), Id(Hp), NumLit(92.46), VarDecl(Id(pIMO), ArrayType([76.29, 73.14, 15.79], NumberType), None, None))])), Block([]), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115084))

	def test_21530115085(self):
		input = '''
func D4 (number B3UJ)
	return 1.73

number L1Cu <- "UaUhE"
func hlt2 ()	begin
		return
		begin
			return
		end
	end
func ii7 (string qb, number JCh, string Wu[60.14,74.92,6.79])
	return

'''
		expect = '''Program([FuncDecl(Id(D4), [VarDecl(Id(B3UJ), NumberType, None, None)], Return(NumLit(1.73))), VarDecl(Id(L1Cu), NumberType, None, StringLit(UaUhE)), FuncDecl(Id(hlt2), [], Block([Return(), Block([Return()])])), FuncDecl(Id(ii7), [VarDecl(Id(qb), StringType, None, None), VarDecl(Id(JCh), NumberType, None, None), VarDecl(Id(Wu), ArrayType([60.14, 74.92, 6.79], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115085))

	def test_21530115086(self):
		input = '''
func Yumr ()
	begin
		string k_lU[16.92,40.21]
		bool dkgK <- 0.77
		break
	end
'''
		expect = '''Program([FuncDecl(Id(Yumr), [], Block([VarDecl(Id(k_lU), ArrayType([16.92, 40.21], StringType), None, None), VarDecl(Id(dkgK), BoolType, None, NumLit(0.77)), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115086))

	def test_21530115087(self):
		input = '''
number pCWN[56.35,48.62,72.36] <- "Ak"
var I6 <- "hI"
'''
		expect = '''Program([VarDecl(Id(pCWN), ArrayType([56.35, 48.62, 72.36], NumberType), None, StringLit(Ak)), VarDecl(Id(I6), None, var, StringLit(hI))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115087))

	def test_21530115088(self):
		input = '''
number JQ <- false
bool dDl[78.61] <- mbK
func LF9X (number BOS[8.16], bool xLba)	begin
		begin
			continue
		end
	end

func Kx (number CeP, number I5[56.57])
	return 59.08

'''
		expect = '''Program([VarDecl(Id(JQ), NumberType, None, BooleanLit(False)), VarDecl(Id(dDl), ArrayType([78.61], BoolType), None, Id(mbK)), FuncDecl(Id(LF9X), [VarDecl(Id(BOS), ArrayType([8.16], NumberType), None, None), VarDecl(Id(xLba), BoolType, None, None)], Block([Block([Continue])])), FuncDecl(Id(Kx), [VarDecl(Id(CeP), NumberType, None, None), VarDecl(Id(I5), ArrayType([56.57], NumberType), None, None)], Return(NumLit(59.08)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115088))

	def test_21530115089(self):
		input = '''
func W8uS (string zr[30.67], bool MbtT, string zD[16.25])	return

'''
		expect = '''Program([FuncDecl(Id(W8uS), [VarDecl(Id(zr), ArrayType([30.67], StringType), None, None), VarDecl(Id(MbtT), BoolType, None, None), VarDecl(Id(zD), ArrayType([16.25], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115089))

	def test_21530115090(self):
		input = '''
func DMSF (number n88, string e7[43.88,51.69], bool qw[78.61,10.65,4.01])	return

number yI[53.35,99.97,5.43]
func PFk3 ()	return Bqx8
'''
		expect = '''Program([FuncDecl(Id(DMSF), [VarDecl(Id(n88), NumberType, None, None), VarDecl(Id(e7), ArrayType([43.88, 51.69], StringType), None, None), VarDecl(Id(qw), ArrayType([78.61, 10.65, 4.01], BoolType), None, None)], Return()), VarDecl(Id(yI), ArrayType([53.35, 99.97, 5.43], NumberType), None, None), FuncDecl(Id(PFk3), [], Return(Id(Bqx8)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115090))

	def test_21530115091(self):
		input = '''
func n_ (string oB, string gE[53.04,15.17,65.06])	return
func hcHl (number y4[59.78,42.89,49.89])
	return 4.51

string W8Ry
func tkS (bool P4GU[87.52,5.72,81.99])
	begin
		return
		if (Qbi)
		IC(wwK)
	end

'''
		expect = '''Program([FuncDecl(Id(n_), [VarDecl(Id(oB), StringType, None, None), VarDecl(Id(gE), ArrayType([53.04, 15.17, 65.06], StringType), None, None)], Return()), FuncDecl(Id(hcHl), [VarDecl(Id(y4), ArrayType([59.78, 42.89, 49.89], NumberType), None, None)], Return(NumLit(4.51))), VarDecl(Id(W8Ry), StringType, None, None), FuncDecl(Id(tkS), [VarDecl(Id(P4GU), ArrayType([87.52, 5.72, 81.99], BoolType), None, None)], Block([Return(), If(Id(Qbi), CallStmt(Id(IC), [Id(wwK)])), [], None]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115091))

	def test_21530115092(self):
		input = '''
string ad[59.06] <- true
bool QJSj <- "rmnsT"
func xeR5 (string FfB)
	begin
		pE <- "EFIL"
	end
func DBm ()
	return false
func FWz (bool r7l, bool LUPQ)
	return

'''
		expect = '''Program([VarDecl(Id(ad), ArrayType([59.06], StringType), None, BooleanLit(True)), VarDecl(Id(QJSj), BoolType, None, StringLit(rmnsT)), FuncDecl(Id(xeR5), [VarDecl(Id(FfB), StringType, None, None)], Block([AssignStmt(Id(pE), StringLit(EFIL))])), FuncDecl(Id(DBm), [], Return(BooleanLit(False))), FuncDecl(Id(FWz), [VarDecl(Id(r7l), BoolType, None, None), VarDecl(Id(LUPQ), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115092))

	def test_21530115093(self):
		input = '''
string Db
'''
		expect = '''Program([VarDecl(Id(Db), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115093))

	def test_21530115094(self):
		input = '''
var lH3D <- true
bool DBWV[71.21]
var to <- true
func auoP (string Xs7[31.24,90.74,95.43])
	return KoiR
'''
		expect = '''Program([VarDecl(Id(lH3D), None, var, BooleanLit(True)), VarDecl(Id(DBWV), ArrayType([71.21], BoolType), None, None), VarDecl(Id(to), None, var, BooleanLit(True)), FuncDecl(Id(auoP), [VarDecl(Id(Xs7), ArrayType([31.24, 90.74, 95.43], StringType), None, None)], Return(Id(KoiR)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115094))

	def test_21530115095(self):
		input = '''
func r8aA ()
	return "ij"

number FJ[30.44,81.07,57.6]
func FD (bool QyT)
	begin
		ri(94.69, 3.15)
	end

func XSU (string H2Z[2.49], number zE[78.45])
	begin
		PD5k[bF, "Gk", 69.49] <- "VqK"
		for IgOg until true by 62.87
			begin
				break
				VU[K5Dj, kGzj, NRCf] <- false
			end
	end

bool lL[7.22,2.75,69.72] <- "fDfa"
'''
		expect = '''Program([FuncDecl(Id(r8aA), [], Return(StringLit(ij))), VarDecl(Id(FJ), ArrayType([30.44, 81.07, 57.6], NumberType), None, None), FuncDecl(Id(FD), [VarDecl(Id(QyT), BoolType, None, None)], Block([CallStmt(Id(ri), [NumLit(94.69), NumLit(3.15)])])), FuncDecl(Id(XSU), [VarDecl(Id(H2Z), ArrayType([2.49], StringType), None, None), VarDecl(Id(zE), ArrayType([78.45], NumberType), None, None)], Block([AssignStmt(ArrayCell(Id(PD5k), [Id(bF), StringLit(Gk), NumLit(69.49)]), StringLit(VqK)), For(Id(IgOg), BooleanLit(True), NumLit(62.87), Block([Break, AssignStmt(ArrayCell(Id(VU), [Id(K5Dj), Id(kGzj), Id(NRCf)]), BooleanLit(False))]))])), VarDecl(Id(lL), ArrayType([7.22, 2.75, 69.72], BoolType), None, StringLit(fDfa))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115095))

	def test_21530115096(self):
		input = '''
func DBpy (number LlP[77.42,38.99,42.54], number pCp)
	begin
		if (pcR) continue
		elif (PQJ) begin
			break
			break
		end
		elif (aLf)
		begin
			begin
				VZwr(73.03)
				EA["cadU", "ny"] <- "JE"
				break
			end
		end
		elif (true) break
		elif (ly)
		number QD8[67.89,16.92,21.0]
		elif (zV_) cOe5 <- 87.79
		return "o"
	end
func vF ()	begin
		for w2 until th44 by false
			begin
				for fLc until 1.71 by false
					return
				continue
			end
		return
	end

func UB ()	return

'''
		expect = '''Program([FuncDecl(Id(DBpy), [VarDecl(Id(LlP), ArrayType([77.42, 38.99, 42.54], NumberType), None, None), VarDecl(Id(pCp), NumberType, None, None)], Block([If(Id(pcR), Continue), [(Id(PQJ), Block([Break, Break])), (Id(aLf), Block([Block([CallStmt(Id(VZwr), [NumLit(73.03)]), AssignStmt(ArrayCell(Id(EA), [StringLit(cadU), StringLit(ny)]), StringLit(JE)), Break])])), (BooleanLit(True), Break), (Id(ly), VarDecl(Id(QD8), ArrayType([67.89, 16.92, 21.0], NumberType), None, None)), (Id(zV_), AssignStmt(Id(cOe5), NumLit(87.79)))], None, Return(StringLit(o))])), FuncDecl(Id(vF), [], Block([For(Id(w2), Id(th44), BooleanLit(False), Block([For(Id(fLc), NumLit(1.71), BooleanLit(False), Return()), Continue])), Return()])), FuncDecl(Id(UB), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115096))

	def test_21530115097(self):
		input = '''
func omGn (number B_Jp, bool zb, bool qE[59.96])	begin
		continue
		number mS
		return
	end

func svd ()	begin
		EHV(false, GI)
		rsb()
	end
'''
		expect = '''Program([FuncDecl(Id(omGn), [VarDecl(Id(B_Jp), NumberType, None, None), VarDecl(Id(zb), BoolType, None, None), VarDecl(Id(qE), ArrayType([59.96], BoolType), None, None)], Block([Continue, VarDecl(Id(mS), NumberType, None, None), Return()])), FuncDecl(Id(svd), [], Block([CallStmt(Id(EHV), [BooleanLit(False), Id(GI)]), CallStmt(Id(rsb), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115097))

	def test_21530115098(self):
		input = '''
dynamic sS9 <- HF
func IF ()
	begin
		oKGj(CE, 11.5)
		for Y2 until YR by "JQwJY"
			break
		kXYk()
	end

'''
		expect = '''Program([VarDecl(Id(sS9), None, dynamic, Id(HF)), FuncDecl(Id(IF), [], Block([CallStmt(Id(oKGj), [Id(CE), NumLit(11.5)]), For(Id(Y2), Id(YR), StringLit(JQwJY), Break), CallStmt(Id(kXYk), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115098))

	def test_21530115099(self):
		input = '''
bool fwP[14.02,83.22,19.3]
number aw9[59.32,95.42,87.17] <- 96.36
bool yOdf <- wl
bool lpP1 <- 78.1
'''
		expect = '''Program([VarDecl(Id(fwP), ArrayType([14.02, 83.22, 19.3], BoolType), None, None), VarDecl(Id(aw9), ArrayType([59.32, 95.42, 87.17], NumberType), None, NumLit(96.36)), VarDecl(Id(yOdf), BoolType, None, Id(wl)), VarDecl(Id(lpP1), BoolType, None, NumLit(78.1))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115099))

	def test_21530115100(self):
		input = '''
func FMpY (string D20, string IsB, number rF[27.59,27.07])	return 50.74
number ii[28.96,63.23]
'''
		expect = '''Program([FuncDecl(Id(FMpY), [VarDecl(Id(D20), StringType, None, None), VarDecl(Id(IsB), StringType, None, None), VarDecl(Id(rF), ArrayType([27.59, 27.07], NumberType), None, None)], Return(NumLit(50.74))), VarDecl(Id(ii), ArrayType([28.96, 63.23], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115100))

	def test_21530115101(self):
		input = '''
number cSUe
bool pGUF
func wZB (number q6, string VvL[68.85,33.71,89.88])
	begin
		Z8qS["DjEXO", iFT] <- false
	end

'''
		expect = '''Program([VarDecl(Id(cSUe), NumberType, None, None), VarDecl(Id(pGUF), BoolType, None, None), FuncDecl(Id(wZB), [VarDecl(Id(q6), NumberType, None, None), VarDecl(Id(VvL), ArrayType([68.85, 33.71, 89.88], StringType), None, None)], Block([AssignStmt(ArrayCell(Id(Z8qS), [StringLit(DjEXO), Id(iFT)]), BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115101))

	def test_21530115102(self):
		input = '''
var lHCP <- "R"
'''
		expect = '''Program([VarDecl(Id(lHCP), None, var, StringLit(R))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115102))

	def test_21530115103(self):
		input = '''
func S9BG (string pa, number nsS1[64.24,55.63,82.19])	return hsq
bool FZ[92.46] <- w3
'''
		expect = '''Program([FuncDecl(Id(S9BG), [VarDecl(Id(pa), StringType, None, None), VarDecl(Id(nsS1), ArrayType([64.24, 55.63, 82.19], NumberType), None, None)], Return(Id(hsq))), VarDecl(Id(FZ), ArrayType([92.46], BoolType), None, Id(w3))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115103))

	def test_21530115104(self):
		input = '''
func csDC (bool PT[13.65,63.57,69.08], string b2u)
	return
dynamic UlH
func cJc (bool p0Nu, string Eg[13.79,65.22])
	begin
		continue
		lCG(true)
	end

'''
		expect = '''Program([FuncDecl(Id(csDC), [VarDecl(Id(PT), ArrayType([13.65, 63.57, 69.08], BoolType), None, None), VarDecl(Id(b2u), StringType, None, None)], Return()), VarDecl(Id(UlH), None, dynamic, None), FuncDecl(Id(cJc), [VarDecl(Id(p0Nu), BoolType, None, None), VarDecl(Id(Eg), ArrayType([13.79, 65.22], StringType), None, None)], Block([Continue, CallStmt(Id(lCG), [BooleanLit(True)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115104))

	def test_21530115105(self):
		input = '''
number B_DA[73.63,28.13] <- 45.59
func Qw8y ()
	return 36.64

number b2[34.3,41.6]
number Ez_[19.39] <- "LGpu"
string bo3[77.0,10.89,50.15]
'''
		expect = '''Program([VarDecl(Id(B_DA), ArrayType([73.63, 28.13], NumberType), None, NumLit(45.59)), FuncDecl(Id(Qw8y), [], Return(NumLit(36.64))), VarDecl(Id(b2), ArrayType([34.3, 41.6], NumberType), None, None), VarDecl(Id(Ez_), ArrayType([19.39], NumberType), None, StringLit(LGpu)), VarDecl(Id(bo3), ArrayType([77.0, 10.89, 50.15], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115105))

	def test_21530115106(self):
		input = '''
number LVk[55.66,99.6] <- LnuL
func nj7 (string Rypp)
	return false

func XW ()
	begin
		break
		for FW until 9.6 by LF
			continue
	end

'''
		expect = '''Program([VarDecl(Id(LVk), ArrayType([55.66, 99.6], NumberType), None, Id(LnuL)), FuncDecl(Id(nj7), [VarDecl(Id(Rypp), StringType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(XW), [], Block([Break, For(Id(FW), NumLit(9.6), Id(LF), Continue)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115106))

	def test_21530115107(self):
		input = '''
var X4O <- CE
func b2Dd ()
	return

func GU (string xi[55.82], bool hp[70.86,66.68], bool COX)
	return el

number q1K <- 5.04
dynamic gD2 <- 40.14
'''
		expect = '''Program([VarDecl(Id(X4O), None, var, Id(CE)), FuncDecl(Id(b2Dd), [], Return()), FuncDecl(Id(GU), [VarDecl(Id(xi), ArrayType([55.82], StringType), None, None), VarDecl(Id(hp), ArrayType([70.86, 66.68], BoolType), None, None), VarDecl(Id(COX), BoolType, None, None)], Return(Id(el))), VarDecl(Id(q1K), NumberType, None, NumLit(5.04)), VarDecl(Id(gD2), None, dynamic, NumLit(40.14))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115107))

	def test_21530115108(self):
		input = '''
number UuX[3.23,8.19,24.64]
'''
		expect = '''Program([VarDecl(Id(UuX), ArrayType([3.23, 8.19, 24.64], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115108))

	def test_21530115109(self):
		input = '''
func jH ()	return
bool nf[4.29] <- true
func va (bool b9[5.73,51.8])	begin
		number hvz[79.42] <- 54.81
		number Qp <- "unGQG"
		break
	end

func NX (bool RD, string tuQ[35.13,77.04])
	return false

'''
		expect = '''Program([FuncDecl(Id(jH), [], Return()), VarDecl(Id(nf), ArrayType([4.29], BoolType), None, BooleanLit(True)), FuncDecl(Id(va), [VarDecl(Id(b9), ArrayType([5.73, 51.8], BoolType), None, None)], Block([VarDecl(Id(hvz), ArrayType([79.42], NumberType), None, NumLit(54.81)), VarDecl(Id(Qp), NumberType, None, StringLit(unGQG)), Break])), FuncDecl(Id(NX), [VarDecl(Id(RD), BoolType, None, None), VarDecl(Id(tuQ), ArrayType([35.13, 77.04], StringType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115109))

	def test_21530115110(self):
		input = '''
func RY (bool Qw, string js[50.67,78.28], bool mfS2[35.32])	begin
		nYE()
	end

'''
		expect = '''Program([FuncDecl(Id(RY), [VarDecl(Id(Qw), BoolType, None, None), VarDecl(Id(js), ArrayType([50.67, 78.28], StringType), None, None), VarDecl(Id(mfS2), ArrayType([35.32], BoolType), None, None)], Block([CallStmt(Id(nYE), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115110))

	def test_21530115111(self):
		input = '''
func xk (string Z4M)	return

func Om ()
	return true
func ij5 (string t26v)
	return
func wO (string laB[56.68,91.06,84.96], string K7p, bool QmRo)
	return
'''
		expect = '''Program([FuncDecl(Id(xk), [VarDecl(Id(Z4M), StringType, None, None)], Return()), FuncDecl(Id(Om), [], Return(BooleanLit(True))), FuncDecl(Id(ij5), [VarDecl(Id(t26v), StringType, None, None)], Return()), FuncDecl(Id(wO), [VarDecl(Id(laB), ArrayType([56.68, 91.06, 84.96], StringType), None, None), VarDecl(Id(K7p), StringType, None, None), VarDecl(Id(QmRo), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115111))

	def test_21530115112(self):
		input = '''
string CWm0[50.66,35.59,89.95] <- true
number sK
var AYVS <- JP
bool Apc
func WC0 (bool RDp8[44.65,25.81], string ys, bool cJ_V[25.02])	begin
		if (false)
		Vngt <- true
		elif ("ueHwY")
		EtS0(false)
		else continue
		return
		for iYl until 11.2 by 41.72
			begin
				continue
			end
	end
'''
		expect = '''Program([VarDecl(Id(CWm0), ArrayType([50.66, 35.59, 89.95], StringType), None, BooleanLit(True)), VarDecl(Id(sK), NumberType, None, None), VarDecl(Id(AYVS), None, var, Id(JP)), VarDecl(Id(Apc), BoolType, None, None), FuncDecl(Id(WC0), [VarDecl(Id(RDp8), ArrayType([44.65, 25.81], BoolType), None, None), VarDecl(Id(ys), StringType, None, None), VarDecl(Id(cJ_V), ArrayType([25.02], BoolType), None, None)], Block([If(BooleanLit(False), AssignStmt(Id(Vngt), BooleanLit(True))), [(StringLit(ueHwY), CallStmt(Id(EtS0), [BooleanLit(False)]))], Continue, Return(), For(Id(iYl), NumLit(11.2), NumLit(41.72), Block([Continue]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115112))

	def test_21530115113(self):
		input = '''
func QeJ (bool l3[87.05,14.41], bool oA[17.3,52.69], number tNI)
	begin
		DukR(mg)
		begin
		end
		return
	end
string PN[1.03,8.47]
'''
		expect = '''Program([FuncDecl(Id(QeJ), [VarDecl(Id(l3), ArrayType([87.05, 14.41], BoolType), None, None), VarDecl(Id(oA), ArrayType([17.3, 52.69], BoolType), None, None), VarDecl(Id(tNI), NumberType, None, None)], Block([CallStmt(Id(DukR), [Id(mg)]), Block([]), Return()])), VarDecl(Id(PN), ArrayType([1.03, 8.47], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115113))

	def test_21530115114(self):
		input = '''
string N5T
func dfE (number uauy[68.03,95.07], string b_Km)
	begin
		if (false)
		if (nWZ) begin
			break
		end
		elif (Ix)
		WN(F4a)
		else begin
			a3oc(false, true)
			continue
			break
		end
		elif (false) number XBP[40.23,3.73,20.1]
		elif ("QYgT") for C2 until true by true
			oRt5 <- "eTPuO"
		elif (B87)
		for B9 until "SXLWL" by 12.73
			if (85.34) continue
			elif ("lHWBu") cpd[90.67, IPqj] <- YVJx
			else continue
		bool M8L[81.91,81.82,45.4] <- true
	end

'''
		expect = '''Program([VarDecl(Id(N5T), StringType, None, None), FuncDecl(Id(dfE), [VarDecl(Id(uauy), ArrayType([68.03, 95.07], NumberType), None, None), VarDecl(Id(b_Km), StringType, None, None)], Block([If(BooleanLit(False), If(Id(nWZ), Block([Break])), [(Id(Ix), CallStmt(Id(WN), [Id(F4a)]))], Block([CallStmt(Id(a3oc), [BooleanLit(False), BooleanLit(True)]), Continue, Break])), [(BooleanLit(False), VarDecl(Id(XBP), ArrayType([40.23, 3.73, 20.1], NumberType), None, None)), (StringLit(QYgT), For(Id(C2), BooleanLit(True), BooleanLit(True), AssignStmt(Id(oRt5), StringLit(eTPuO)))), (Id(B87), For(Id(B9), StringLit(SXLWL), NumLit(12.73), If(NumLit(85.34), Continue), [], None)), (StringLit(lHWBu), AssignStmt(ArrayCell(Id(cpd), [NumLit(90.67), Id(IPqj)]), Id(YVJx)))], Continue, VarDecl(Id(M8L), ArrayType([81.91, 81.82, 45.4], BoolType), None, BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115114))

	def test_21530115115(self):
		input = '''
bool Q9[85.87] <- Zp
func j8AX (number BV1W, bool PS, number F30P[53.82])
	begin
		break
		begin
			tM["hB", false] <- "ig"
			continue
		end
		for K5 until 75.52 by 84.43
			ZO6()
	end
bool Z4_ <- false
'''
		expect = '''Program([VarDecl(Id(Q9), ArrayType([85.87], BoolType), None, Id(Zp)), FuncDecl(Id(j8AX), [VarDecl(Id(BV1W), NumberType, None, None), VarDecl(Id(PS), BoolType, None, None), VarDecl(Id(F30P), ArrayType([53.82], NumberType), None, None)], Block([Break, Block([AssignStmt(ArrayCell(Id(tM), [StringLit(hB), BooleanLit(False)]), StringLit(ig)), Continue]), For(Id(K5), NumLit(75.52), NumLit(84.43), CallStmt(Id(ZO6), []))])), VarDecl(Id(Z4_), BoolType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115115))

	def test_21530115116(self):
		input = '''
dynamic mq <- 73.29
'''
		expect = '''Program([VarDecl(Id(mq), None, dynamic, NumLit(73.29))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115116))

	def test_21530115117(self):
		input = '''
func oS ()	return false

var EF <- f2
func w6x (number dRo5)	return 64.92
bool uw6[13.17,80.43,59.45]
bool Tx
'''
		expect = '''Program([FuncDecl(Id(oS), [], Return(BooleanLit(False))), VarDecl(Id(EF), None, var, Id(f2)), FuncDecl(Id(w6x), [VarDecl(Id(dRo5), NumberType, None, None)], Return(NumLit(64.92))), VarDecl(Id(uw6), ArrayType([13.17, 80.43, 59.45], BoolType), None, None), VarDecl(Id(Tx), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115117))

	def test_21530115118(self):
		input = '''
func DyM (bool SVw3, number HO)	return
string Ec[11.81,72.74,14.66] <- o7t
number iSZ[63.04,51.79,51.6] <- "bN"
dynamic V4f
'''
		expect = '''Program([FuncDecl(Id(DyM), [VarDecl(Id(SVw3), BoolType, None, None), VarDecl(Id(HO), NumberType, None, None)], Return()), VarDecl(Id(Ec), ArrayType([11.81, 72.74, 14.66], StringType), None, Id(o7t)), VarDecl(Id(iSZ), ArrayType([63.04, 51.79, 51.6], NumberType), None, StringLit(bN)), VarDecl(Id(V4f), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115118))

	def test_21530115119(self):
		input = '''
dynamic Hz_W <- true
'''
		expect = '''Program([VarDecl(Id(Hz_W), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115119))

	def test_21530115120(self):
		input = '''
bool uQ[91.83,8.82]
bool acwK[27.85,40.82,51.32]
func FdbH (number zIf[30.28], number nmos)	return
number qaW[4.33]
func Mme ()
	return 4.92
'''
		expect = '''Program([VarDecl(Id(uQ), ArrayType([91.83, 8.82], BoolType), None, None), VarDecl(Id(acwK), ArrayType([27.85, 40.82, 51.32], BoolType), None, None), FuncDecl(Id(FdbH), [VarDecl(Id(zIf), ArrayType([30.28], NumberType), None, None), VarDecl(Id(nmos), NumberType, None, None)], Return()), VarDecl(Id(qaW), ArrayType([4.33], NumberType), None, None), FuncDecl(Id(Mme), [], Return(NumLit(4.92)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115120))

	def test_21530115121(self):
		input = '''
string tBKe[46.66,70.4,4.45]
string pD76[29.69,11.12,26.47] <- q0y
'''
		expect = '''Program([VarDecl(Id(tBKe), ArrayType([46.66, 70.4, 4.45], StringType), None, None), VarDecl(Id(pD76), ArrayType([29.69, 11.12, 26.47], StringType), None, Id(q0y))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115121))

	def test_21530115122(self):
		input = '''
bool nRQ[34.0,46.69]
string rf
var gRqL <- true
func vzyT (string fJ8[57.61])
	begin
		continue
		PBFm("Y", 37.88, false)
		RTIy[true] <- fQ
	end

func Gf (string Hf4, bool S_8A, bool G5am)
	return

'''
		expect = '''Program([VarDecl(Id(nRQ), ArrayType([34.0, 46.69], BoolType), None, None), VarDecl(Id(rf), StringType, None, None), VarDecl(Id(gRqL), None, var, BooleanLit(True)), FuncDecl(Id(vzyT), [VarDecl(Id(fJ8), ArrayType([57.61], StringType), None, None)], Block([Continue, CallStmt(Id(PBFm), [StringLit(Y), NumLit(37.88), BooleanLit(False)]), AssignStmt(ArrayCell(Id(RTIy), [BooleanLit(True)]), Id(fQ))])), FuncDecl(Id(Gf), [VarDecl(Id(Hf4), StringType, None, None), VarDecl(Id(S_8A), BoolType, None, None), VarDecl(Id(G5am), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115122))

	def test_21530115123(self):
		input = '''
var ttD <- d2Jh
func X92C (number ua4u, number BAW)
	return

func cYU (string BH[57.97,65.13], number sKOW[37.27,99.77], number lsN[61.46,68.88])
	return 71.68

'''
		expect = '''Program([VarDecl(Id(ttD), None, var, Id(d2Jh)), FuncDecl(Id(X92C), [VarDecl(Id(ua4u), NumberType, None, None), VarDecl(Id(BAW), NumberType, None, None)], Return()), FuncDecl(Id(cYU), [VarDecl(Id(BH), ArrayType([57.97, 65.13], StringType), None, None), VarDecl(Id(sKOW), ArrayType([37.27, 99.77], NumberType), None, None), VarDecl(Id(lsN), ArrayType([61.46, 68.88], NumberType), None, None)], Return(NumLit(71.68)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115123))

	def test_21530115124(self):
		input = '''
string cX[73.32] <- "Qa"
string mq[98.95,13.71]
'''
		expect = '''Program([VarDecl(Id(cX), ArrayType([73.32], StringType), None, StringLit(Qa)), VarDecl(Id(mq), ArrayType([98.95, 13.71], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115124))

	def test_21530115125(self):
		input = '''
func Rz ()
	return 32.62

func QUYk (bool blG[14.52,44.69,15.22], number CyFt[56.81], number ZQA[41.5,61.94])	return "vhFU"

bool HTf
number RC[66.48]
'''
		expect = '''Program([FuncDecl(Id(Rz), [], Return(NumLit(32.62))), FuncDecl(Id(QUYk), [VarDecl(Id(blG), ArrayType([14.52, 44.69, 15.22], BoolType), None, None), VarDecl(Id(CyFt), ArrayType([56.81], NumberType), None, None), VarDecl(Id(ZQA), ArrayType([41.5, 61.94], NumberType), None, None)], Return(StringLit(vhFU))), VarDecl(Id(HTf), BoolType, None, None), VarDecl(Id(RC), ArrayType([66.48], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115125))

	def test_21530115126(self):
		input = '''
string ws23[82.98] <- false
func w26 (bool OtU)	return

'''
		expect = '''Program([VarDecl(Id(ws23), ArrayType([82.98], StringType), None, BooleanLit(False)), FuncDecl(Id(w26), [VarDecl(Id(OtU), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115126))

	def test_21530115127(self):
		input = '''
number mn[1.93,79.97,92.28]
dynamic zX
func ZN ()	return
func uVW (bool Cb)
	begin
		string tTBD <- false
		number uH9[77.24,14.38]
	end

func HP ()	return "IXyg"

'''
		expect = '''Program([VarDecl(Id(mn), ArrayType([1.93, 79.97, 92.28], NumberType), None, None), VarDecl(Id(zX), None, dynamic, None), FuncDecl(Id(ZN), [], Return()), FuncDecl(Id(uVW), [VarDecl(Id(Cb), BoolType, None, None)], Block([VarDecl(Id(tTBD), StringType, None, BooleanLit(False)), VarDecl(Id(uH9), ArrayType([77.24, 14.38], NumberType), None, None)])), FuncDecl(Id(HP), [], Return(StringLit(IXyg)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115127))

	def test_21530115128(self):
		input = '''
number qJ <- iVS
'''
		expect = '''Program([VarDecl(Id(qJ), NumberType, None, Id(iVS))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115128))

	def test_21530115129(self):
		input = '''
string jTq[59.34] <- "Yu"
func aA (string HHJ)	return B_VH
func u9P (number y1l)	return false

bool wFPd[69.94,62.89,39.66] <- dOF
func QQA (number w0[63.46,4.6], bool Ry[96.82,19.19], string Zy)
	return false

'''
		expect = '''Program([VarDecl(Id(jTq), ArrayType([59.34], StringType), None, StringLit(Yu)), FuncDecl(Id(aA), [VarDecl(Id(HHJ), StringType, None, None)], Return(Id(B_VH))), FuncDecl(Id(u9P), [VarDecl(Id(y1l), NumberType, None, None)], Return(BooleanLit(False))), VarDecl(Id(wFPd), ArrayType([69.94, 62.89, 39.66], BoolType), None, Id(dOF)), FuncDecl(Id(QQA), [VarDecl(Id(w0), ArrayType([63.46, 4.6], NumberType), None, None), VarDecl(Id(Ry), ArrayType([96.82, 19.19], BoolType), None, None), VarDecl(Id(Zy), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115129))

	def test_21530115130(self):
		input = '''
string Iki
'''
		expect = '''Program([VarDecl(Id(Iki), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115130))

	def test_21530115131(self):
		input = '''
number VGu[89.7]
string Mp[63.0] <- 47.56
number Y0N[12.11] <- 0.09
bool zmR[90.64]
bool tA6p[32.61,18.48] <- true
'''
		expect = '''Program([VarDecl(Id(VGu), ArrayType([89.7], NumberType), None, None), VarDecl(Id(Mp), ArrayType([63.0], StringType), None, NumLit(47.56)), VarDecl(Id(Y0N), ArrayType([12.11], NumberType), None, NumLit(0.09)), VarDecl(Id(zmR), ArrayType([90.64], BoolType), None, None), VarDecl(Id(tA6p), ArrayType([32.61, 18.48], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115131))

	def test_21530115132(self):
		input = '''
func X7G (number HUJ, string hZA[88.44,57.64,50.73], bool suL[44.31])	return SqZ
number iu[67.56]
'''
		expect = '''Program([FuncDecl(Id(X7G), [VarDecl(Id(HUJ), NumberType, None, None), VarDecl(Id(hZA), ArrayType([88.44, 57.64, 50.73], StringType), None, None), VarDecl(Id(suL), ArrayType([44.31], BoolType), None, None)], Return(Id(SqZ))), VarDecl(Id(iu), ArrayType([67.56], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115132))

	def test_21530115133(self):
		input = '''
number sT[39.02] <- 68.94
func gZjG (number i5NJ[22.92], number Hx)	return "tTKnb"
func XOg (number IrA1[99.04,98.09], string juW0)	begin
		break
		for hwPB until 76.35 by true
			break
	end
func RELy (string rS)	return true

'''
		expect = '''Program([VarDecl(Id(sT), ArrayType([39.02], NumberType), None, NumLit(68.94)), FuncDecl(Id(gZjG), [VarDecl(Id(i5NJ), ArrayType([22.92], NumberType), None, None), VarDecl(Id(Hx), NumberType, None, None)], Return(StringLit(tTKnb))), FuncDecl(Id(XOg), [VarDecl(Id(IrA1), ArrayType([99.04, 98.09], NumberType), None, None), VarDecl(Id(juW0), StringType, None, None)], Block([Break, For(Id(hwPB), NumLit(76.35), BooleanLit(True), Break)])), FuncDecl(Id(RELy), [VarDecl(Id(rS), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115133))

	def test_21530115134(self):
		input = '''
func pZ (bool EG)
	begin
		if (false)
		string QJ <- GjKr
		elif (12.07) dJ(CTzP, bmZ)
		elif (63.05) UwU[false] <- true
		elif ("SYkTM")
		F9p()
	end

func kx ()
	return
bool al3e <- "fPq"
'''
		expect = '''Program([FuncDecl(Id(pZ), [VarDecl(Id(EG), BoolType, None, None)], Block([If(BooleanLit(False), VarDecl(Id(QJ), StringType, None, Id(GjKr))), [(NumLit(12.07), CallStmt(Id(dJ), [Id(CTzP), Id(bmZ)])), (NumLit(63.05), AssignStmt(ArrayCell(Id(UwU), [BooleanLit(False)]), BooleanLit(True))), (StringLit(SYkTM), CallStmt(Id(F9p), []))], None])), FuncDecl(Id(kx), [], Return()), VarDecl(Id(al3e), BoolType, None, StringLit(fPq))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115134))

	def test_21530115135(self):
		input = '''
func X_i (number uU, bool rS, bool h4o6)	return
'''
		expect = '''Program([FuncDecl(Id(X_i), [VarDecl(Id(uU), NumberType, None, None), VarDecl(Id(rS), BoolType, None, None), VarDecl(Id(h4o6), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115135))

	def test_21530115136(self):
		input = '''
func U3 (bool pj[47.86], number Nh[3.71,46.8], number kr)
	return 27.15

bool J0Fw[89.33,14.55,81.18] <- 22.15
bool DO
'''
		expect = '''Program([FuncDecl(Id(U3), [VarDecl(Id(pj), ArrayType([47.86], BoolType), None, None), VarDecl(Id(Nh), ArrayType([3.71, 46.8], NumberType), None, None), VarDecl(Id(kr), NumberType, None, None)], Return(NumLit(27.15))), VarDecl(Id(J0Fw), ArrayType([89.33, 14.55, 81.18], BoolType), None, NumLit(22.15)), VarDecl(Id(DO), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115136))

	def test_21530115137(self):
		input = '''
var io24 <- 57.21
func MRnN ()
	begin
		begin
			AD("Xm", 98.36, LHVb)
			if (oax)
			Ax3[eJ, "HJWp", true] <- 54.46
			elif (true)
			if (32.21)
			if (4.7) for sl until jp by "DCS"
				for W3YD until 80.62 by 15.63
					if (false)
					continue
					elif ("sAMQL") number Qoe[20.85,30.35] <- false
					elif (9.55)
					begin
					end
					elif ("e")
					XQn(false, xB9O)
					elif (c1) break
					elif (true) continue
			elif ("RkHf")
			begin
				return
				var oW2 <- "oprb"
				return
			end
			elif (Jh8f)
			for XFf until "wBB" by 94.37
				return
			else for Zp until 36.5 by 42.61
				break
			elif (fed) if (false)
			for LhPF until vgE by dn
				return 75.09
			elif ("tmm")
			for y6h4 until 86.49 by Yf
				continue
			elif (hUtd)
			begin
				begin
					break
				end
				if ("eVWoi") for wU until 43.34 by true
					break
				elif (76.46)
				for AYcZ until 23.2 by Yp0
					continue
				elif (Pz)
				if (93.96)
				begin
					break
				end
				elif (77.58) if ("WvR")
				for Cw until oAAI by 59.75
					Ip <- Vw
				elif (53.23) break
				else bool Igm[76.2,68.8,41.89] <- 86.13
				elif ("Tza") break
				elif (9.51) for oT4H until "FQ" by "ThvZa"
					for f8Lv until "kU" by kJc
						if (Tje) return 95.79
						elif (false) V14N <- false
						elif ("XF")
						return "LXhS"
						elif (32.7) if (rP1m)
						begin
							break
						end
						elif (30.81)
						break
						elif (34.2) begin
							begin
								mkp <- "GxoLO"
							end
						end
						elif (85.7)
						d_["uMs"] <- RCx
						elif (true) begin
							string e61F[63.82,41.02] <- "OnLJP"
							G6Mk()
						end
						elif ("zat")
						break
						elif (K1C)
						SPdr()
				elif (true) break
				elif (J9W) return
				else return HGcT
				elif (Y5u) string Vw[2.13]
				elif ("O") TxLV()
				elif ("ywNv") return 16.19
				Xv9K(34.64, true)
			end
			elif (Bmv)
			GAiu[fWVF] <- true
			elif ("dP")
			oO <- 32.51
			elif (true) break
			else fw("b", "eDkd", false)
			elif (FGBs) return
			elif (17.5) if ("J") for K95 until "y" by Et
				break
			else var EZPf <- 62.68
			elif (false) begin
				begin
				end
			end
		end
		begin
			begin
				break
				if ("Vx")
				continue
				elif ("U") string ZKU6[84.75,51.3]
				elif (71.0) bool oLo[76.09]
				else break
				sAv[false] <- "LAKwM"
			end
			if ("rwLYZ") begin
				begin
				end
				break
			end
			elif ("i")
			return "ioEx"
			elif (29.34)
			break
			elif (j_YP) su("My", true, false)
			elif (false)
			return "Pm"
			elif ("FAaHC")
			for lGuK until "kIeCn" by "ymtb"
				Rsqt(86.45)
			else if (false)
			JWK()
			elif (23.04) if ("ZyDOH") begin
				return
			end
			elif (68.41)
			IPwZ["O"] <- "Vt"
			elif (97.79)
			G7T <- dfD2
			elif (37.98)
			begin
				if ("Bzu")
				break
				elif (true) for jtGA until 6.4 by "hNse"
					if (false)
					begin
					end
					elif (Se)
					dPK(81.09, 46.19)
					elif (48.65)
					bool QrB[20.27,81.88,55.58]
					elif (46.51) for N_92 until vrm by 69.56
						break
					elif (95.79)
					for J5 until "LcSnv" by false
						break
				elif (49.48)
				if (57.98)
				begin
				end
				elif (17.3) dynamic vjk <- true
				elif (DZ)
				PX5("Zs", true)
				elif (69.14)
				bool tA[68.67]
				else begin
					for te until "cETzX" by t9
						return
					begin
						break
						for rF0o until myc by 3.71
							Fmt("cnzaw", false, NZnJ)
						break
					end
					continue
				end
				elif ("s")
				begin
				end
				elif (36.05)
				W5A("ZE", 65.23, lnj)
				elif (fgz) for PQf until 52.79 by 61.61
					continue
			end
			elif (false) sP04 <- 50.98
			elif (bqX) if (true)
			begin
				number ejCY <- 96.73
				break
				begin
					begin
					end
				end
			end
			elif (72.44)
			d4[false, "KyB", "VVIJG"] <- true
			elif ("yN")
			KSFA[85.25, false] <- "Zy"
			elif (false) begin
				return
			end
		end
	end

number w0e[9.27,17.63]
'''
		expect = '''Program([VarDecl(Id(io24), None, var, NumLit(57.21)), FuncDecl(Id(MRnN), [], Block([Block([CallStmt(Id(AD), [StringLit(Xm), NumLit(98.36), Id(LHVb)]), If(Id(oax), AssignStmt(ArrayCell(Id(Ax3), [Id(eJ), StringLit(HJWp), BooleanLit(True)]), NumLit(54.46))), [(BooleanLit(True), If(NumLit(32.21), If(NumLit(4.7), For(Id(sl), Id(jp), StringLit(DCS), For(Id(W3YD), NumLit(80.62), NumLit(15.63), If(BooleanLit(False), Continue), [(StringLit(sAMQL), VarDecl(Id(Qoe), ArrayType([20.85, 30.35], NumberType), None, BooleanLit(False))), (NumLit(9.55), Block([])), (StringLit(e), CallStmt(Id(XQn), [BooleanLit(False), Id(xB9O)])), (Id(c1), Break), (BooleanLit(True), Continue), (StringLit(RkHf), Block([Return(), VarDecl(Id(oW2), None, var, StringLit(oprb)), Return()])), (Id(Jh8f), For(Id(XFf), StringLit(wBB), NumLit(94.37), Return()))], For(Id(Zp), NumLit(36.5), NumLit(42.61), Break)))), [(Id(fed), If(BooleanLit(False), For(Id(LhPF), Id(vgE), Id(dn), Return(NumLit(75.09)))), [(StringLit(tmm), For(Id(y6h4), NumLit(86.49), Id(Yf), Continue)), (Id(hUtd), Block([Block([Break]), If(StringLit(eVWoi), For(Id(wU), NumLit(43.34), BooleanLit(True), Break)), [(NumLit(76.46), For(Id(AYcZ), NumLit(23.2), Id(Yp0), Continue)), (Id(Pz), If(NumLit(93.96), Block([Break])), [(NumLit(77.58), If(StringLit(WvR), For(Id(Cw), Id(oAAI), NumLit(59.75), AssignStmt(Id(Ip), Id(Vw)))), [(NumLit(53.23), Break)], VarDecl(Id(Igm), ArrayType([76.2, 68.8, 41.89], BoolType), None, NumLit(86.13))), (StringLit(Tza), Break), (NumLit(9.51), For(Id(oT4H), StringLit(FQ), StringLit(ThvZa), For(Id(f8Lv), StringLit(kU), Id(kJc), If(Id(Tje), Return(NumLit(95.79))), [(BooleanLit(False), AssignStmt(Id(V14N), BooleanLit(False))), (StringLit(XF), Return(StringLit(LXhS))), (NumLit(32.7), If(Id(rP1m), Block([Break])), [(NumLit(30.81), Break), (NumLit(34.2), Block([Block([AssignStmt(Id(mkp), StringLit(GxoLO))])])), (NumLit(85.7), AssignStmt(ArrayCell(Id(d_), [StringLit(uMs)]), Id(RCx))), (BooleanLit(True), Block([VarDecl(Id(e61F), ArrayType([63.82, 41.02], StringType), None, StringLit(OnLJP)), CallStmt(Id(G6Mk), [])])), (StringLit(zat), Break), (Id(K1C), CallStmt(Id(SPdr), [])), (BooleanLit(True), Break), (Id(J9W), Return())], Return(Id(HGcT))), (Id(Y5u), VarDecl(Id(Vw), ArrayType([2.13], StringType), None, None))], None))), (StringLit(O), CallStmt(Id(TxLV), []))], None), (StringLit(ywNv), Return(NumLit(16.19)))], None, CallStmt(Id(Xv9K), [NumLit(34.64), BooleanLit(True)])])), (Id(Bmv), AssignStmt(ArrayCell(Id(GAiu), [Id(fWVF)]), BooleanLit(True))), (StringLit(dP), AssignStmt(Id(oO), NumLit(32.51))), (BooleanLit(True), Break)], CallStmt(Id(fw), [StringLit(b), StringLit(eDkd), BooleanLit(False)])), (Id(FGBs), Return()), (NumLit(17.5), If(StringLit(J), For(Id(K95), StringLit(y), Id(Et), Break)), [], VarDecl(Id(EZPf), None, var, NumLit(62.68)))], None), [], None), (BooleanLit(False), Block([Block([])]))], None]), Block([Block([Break, If(StringLit(Vx), Continue), [(StringLit(U), VarDecl(Id(ZKU6), ArrayType([84.75, 51.3], StringType), None, None)), (NumLit(71.0), VarDecl(Id(oLo), ArrayType([76.09], BoolType), None, None))], Break, AssignStmt(ArrayCell(Id(sAv), [BooleanLit(False)]), StringLit(LAKwM))]), If(StringLit(rwLYZ), Block([Block([]), Break])), [(StringLit(i), Return(StringLit(ioEx))), (NumLit(29.34), Break), (Id(j_YP), CallStmt(Id(su), [StringLit(My), BooleanLit(True), BooleanLit(False)])), (BooleanLit(False), Return(StringLit(Pm))), (StringLit(FAaHC), For(Id(lGuK), StringLit(kIeCn), StringLit(ymtb), CallStmt(Id(Rsqt), [NumLit(86.45)])))], If(BooleanLit(False), CallStmt(Id(JWK), [])), [(NumLit(23.04), If(StringLit(ZyDOH), Block([Return()])), [(NumLit(68.41), AssignStmt(ArrayCell(Id(IPwZ), [StringLit(O)]), StringLit(Vt))), (NumLit(97.79), AssignStmt(Id(G7T), Id(dfD2))), (NumLit(37.98), Block([If(StringLit(Bzu), Break), [(BooleanLit(True), For(Id(jtGA), NumLit(6.4), StringLit(hNse), If(BooleanLit(False), Block([])), [(Id(Se), CallStmt(Id(dPK), [NumLit(81.09), NumLit(46.19)])), (NumLit(48.65), VarDecl(Id(QrB), ArrayType([20.27, 81.88, 55.58], BoolType), None, None)), (NumLit(46.51), For(Id(N_92), Id(vrm), NumLit(69.56), Break)), (NumLit(95.79), For(Id(J5), StringLit(LcSnv), BooleanLit(False), Break)), (NumLit(49.48), If(NumLit(57.98), Block([])), [(NumLit(17.3), VarDecl(Id(vjk), None, dynamic, BooleanLit(True))), (Id(DZ), CallStmt(Id(PX5), [StringLit(Zs), BooleanLit(True)])), (NumLit(69.14), VarDecl(Id(tA), ArrayType([68.67], BoolType), None, None))], Block([For(Id(te), StringLit(cETzX), Id(t9), Return()), Block([Break, For(Id(rF0o), Id(myc), NumLit(3.71), CallStmt(Id(Fmt), [StringLit(cnzaw), BooleanLit(False), Id(NZnJ)])), Break]), Continue])), (StringLit(s), Block([])), (NumLit(36.05), CallStmt(Id(W5A), [StringLit(ZE), NumLit(65.23), Id(lnj)]))], None)), (Id(fgz), For(Id(PQf), NumLit(52.79), NumLit(61.61), Continue))], None])), (BooleanLit(False), AssignStmt(Id(sP04), NumLit(50.98))), (Id(bqX), If(BooleanLit(True), Block([VarDecl(Id(ejCY), NumberType, None, NumLit(96.73)), Break, Block([Block([])])])), [(NumLit(72.44), AssignStmt(ArrayCell(Id(d4), [BooleanLit(False), StringLit(KyB), StringLit(VVIJG)]), BooleanLit(True)))], None), (StringLit(yN), AssignStmt(ArrayCell(Id(KSFA), [NumLit(85.25), BooleanLit(False)]), StringLit(Zy)))], None), (BooleanLit(False), Block([Return()]))], None])])), VarDecl(Id(w0e), ArrayType([9.27, 17.63], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115137))

	def test_21530115138(self):
		input = '''
func rS8U (bool ES9[80.88,65.05], bool gAQ[74.58,78.62,87.8], bool CvS[38.22])	begin
		begin
		end
	end

string Aqi[10.23,8.62]
string rb
'''
		expect = '''Program([FuncDecl(Id(rS8U), [VarDecl(Id(ES9), ArrayType([80.88, 65.05], BoolType), None, None), VarDecl(Id(gAQ), ArrayType([74.58, 78.62, 87.8], BoolType), None, None), VarDecl(Id(CvS), ArrayType([38.22], BoolType), None, None)], Block([Block([])])), VarDecl(Id(Aqi), ArrayType([10.23, 8.62], StringType), None, None), VarDecl(Id(rb), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115138))

	def test_21530115139(self):
		input = '''
func H2_ (string nA[14.45,26.97])
	return 12.94
'''
		expect = '''Program([FuncDecl(Id(H2_), [VarDecl(Id(nA), ArrayType([14.45, 26.97], StringType), None, None)], Return(NumLit(12.94)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115139))

	def test_21530115140(self):
		input = '''
func c02p (number WFN9[66.15], bool dEO)
	begin
		if (72.75) return
		elif (43.19) return
		elif (46.79)
		break
		elif (32.93) break
		IE(true, false, true)
		if (Ir1Q) break
		elif (false) IQp()
	end
string gMU <- 46.84
func V3Dj (string Pyx[19.53])	begin
		return
		string dVf[56.46,69.46]
		begin
			if (false)
			return
			elif (39.54) if (Fa)
			dynamic K4Te <- 59.73
			else if ("ROH") continue
			else break
			elif (false) return 17.55
			elif (false)
			continue
			elif (47.78) for E3KZ until qud by true
				break
			else break
			for nwf until 48.57 by 76.07
				continue
			if (false) continue
		end
	end

'''
		expect = '''Program([FuncDecl(Id(c02p), [VarDecl(Id(WFN9), ArrayType([66.15], NumberType), None, None), VarDecl(Id(dEO), BoolType, None, None)], Block([If(NumLit(72.75), Return()), [(NumLit(43.19), Return()), (NumLit(46.79), Break), (NumLit(32.93), Break)], None, CallStmt(Id(IE), [BooleanLit(True), BooleanLit(False), BooleanLit(True)]), If(Id(Ir1Q), Break), [(BooleanLit(False), CallStmt(Id(IQp), []))], None])), VarDecl(Id(gMU), StringType, None, NumLit(46.84)), FuncDecl(Id(V3Dj), [VarDecl(Id(Pyx), ArrayType([19.53], StringType), None, None)], Block([Return(), VarDecl(Id(dVf), ArrayType([56.46, 69.46], StringType), None, None), Block([If(BooleanLit(False), Return()), [(NumLit(39.54), If(Id(Fa), VarDecl(Id(K4Te), None, dynamic, NumLit(59.73))), [], If(StringLit(ROH), Continue), [], Break), (BooleanLit(False), Return(NumLit(17.55))), (BooleanLit(False), Continue), (NumLit(47.78), For(Id(E3KZ), Id(qud), BooleanLit(True), Break))], Break, For(Id(nwf), NumLit(48.57), NumLit(76.07), Continue), If(BooleanLit(False), Continue), [], None])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115140))

	def test_21530115141(self):
		input = '''
bool lwlY[29.54,32.62,75.51] <- 14.25
func uj (bool ux[5.76])
	return

func QQP (bool rkXZ[7.61,11.7], bool F6rg, string XZ3[74.9])
	begin
		for z76w until "nqnFX" by 0.07
			Zo1V <- 84.12
		cT(99.77)
		for Ygl until "HCdM" by "x"
			if (Smb) DwVn(L9i)
			elif ("gi")
			if (62.91) continue
			elif (true) continue
			elif (false)
			pILn <- w4pl
			elif (qd)
			uJ(54.32)
			else PHT("oqzqM")
	end
'''
		expect = '''Program([VarDecl(Id(lwlY), ArrayType([29.54, 32.62, 75.51], BoolType), None, NumLit(14.25)), FuncDecl(Id(uj), [VarDecl(Id(ux), ArrayType([5.76], BoolType), None, None)], Return()), FuncDecl(Id(QQP), [VarDecl(Id(rkXZ), ArrayType([7.61, 11.7], BoolType), None, None), VarDecl(Id(F6rg), BoolType, None, None), VarDecl(Id(XZ3), ArrayType([74.9], StringType), None, None)], Block([For(Id(z76w), StringLit(nqnFX), NumLit(0.07), AssignStmt(Id(Zo1V), NumLit(84.12))), CallStmt(Id(cT), [NumLit(99.77)]), For(Id(Ygl), StringLit(HCdM), StringLit(x), If(Id(Smb), CallStmt(Id(DwVn), [Id(L9i)])), [(StringLit(gi), If(NumLit(62.91), Continue), [(BooleanLit(True), Continue), (BooleanLit(False), AssignStmt(Id(pILn), Id(w4pl)))], None), (Id(qd), CallStmt(Id(uJ), [NumLit(54.32)]))], CallStmt(Id(PHT), [StringLit(oqzqM)]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115141))

	def test_21530115142(self):
		input = '''
func ho (bool mmY)
	begin
	end

func Ew2 ()
	begin
		string eyt[13.41]
		break
		bool F0aC[58.38,34.47] <- 4.99
	end

number zq[54.65,98.48] <- PrC
func NuN (number aEK)
	begin
		for P61d until "okyL" by Cl
			for NFu until false by "TDZQa"
				continue
	end

string XeU <- "RxXZd"
'''
		expect = '''Program([FuncDecl(Id(ho), [VarDecl(Id(mmY), BoolType, None, None)], Block([])), FuncDecl(Id(Ew2), [], Block([VarDecl(Id(eyt), ArrayType([13.41], StringType), None, None), Break, VarDecl(Id(F0aC), ArrayType([58.38, 34.47], BoolType), None, NumLit(4.99))])), VarDecl(Id(zq), ArrayType([54.65, 98.48], NumberType), None, Id(PrC)), FuncDecl(Id(NuN), [VarDecl(Id(aEK), NumberType, None, None)], Block([For(Id(P61d), StringLit(okyL), Id(Cl), For(Id(NFu), BooleanLit(False), StringLit(TDZQa), Continue))])), VarDecl(Id(XeU), StringType, None, StringLit(RxXZd))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115142))

	def test_21530115143(self):
		input = '''
number KO[98.11,29.85,42.01] <- true
bool oG0
func D1V (bool EcK, number jdw, bool I3T[100.0,55.83,75.98])
	return

'''
		expect = '''Program([VarDecl(Id(KO), ArrayType([98.11, 29.85, 42.01], NumberType), None, BooleanLit(True)), VarDecl(Id(oG0), BoolType, None, None), FuncDecl(Id(D1V), [VarDecl(Id(EcK), BoolType, None, None), VarDecl(Id(jdw), NumberType, None, None), VarDecl(Id(I3T), ArrayType([100.0, 55.83, 75.98], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115143))

	def test_21530115144(self):
		input = '''
number tqp[76.32] <- "Ef"
dynamic C0 <- 17.12
func zROR (number MoJ[37.53,43.53], bool yMmG, number oaPs[7.79,17.23])	return

bool AyDc
'''
		expect = '''Program([VarDecl(Id(tqp), ArrayType([76.32], NumberType), None, StringLit(Ef)), VarDecl(Id(C0), None, dynamic, NumLit(17.12)), FuncDecl(Id(zROR), [VarDecl(Id(MoJ), ArrayType([37.53, 43.53], NumberType), None, None), VarDecl(Id(yMmG), BoolType, None, None), VarDecl(Id(oaPs), ArrayType([7.79, 17.23], NumberType), None, None)], Return()), VarDecl(Id(AyDc), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115144))

	def test_21530115145(self):
		input = '''
func iS ()	return
func Vit ()	begin
		if (Zb2) xp["DT", ppmT, "C"] <- "swfC"
		elif ("uwBHE")
		for nw until false by CZo
			WBkv["hh"] <- OO
		elif (jPg) for nQDx until Cvl by S4X
			break
		elif (false) for Yolf until 15.73 by 95.26
			return "WQaNQ"
		elif ("mxI") qgTA["JZq"] <- true
		elif (E7) break
		break
	end

var hI4 <- sB
bool vLu
'''
		expect = '''Program([FuncDecl(Id(iS), [], Return()), FuncDecl(Id(Vit), [], Block([If(Id(Zb2), AssignStmt(ArrayCell(Id(xp), [StringLit(DT), Id(ppmT), StringLit(C)]), StringLit(swfC))), [(StringLit(uwBHE), For(Id(nw), BooleanLit(False), Id(CZo), AssignStmt(ArrayCell(Id(WBkv), [StringLit(hh)]), Id(OO)))), (Id(jPg), For(Id(nQDx), Id(Cvl), Id(S4X), Break)), (BooleanLit(False), For(Id(Yolf), NumLit(15.73), NumLit(95.26), Return(StringLit(WQaNQ)))), (StringLit(mxI), AssignStmt(ArrayCell(Id(qgTA), [StringLit(JZq)]), BooleanLit(True))), (Id(E7), Break)], None, Break])), VarDecl(Id(hI4), None, var, Id(sB)), VarDecl(Id(vLu), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115145))

	def test_21530115146(self):
		input = '''
func ff3 (string JfM, number jIiO)
	return
func TZzH ()	return

func l5 (bool ja[34.13], number dYon[97.68,54.54,17.39], number RN)
	begin
		c_xA()
		string g1G[68.77] <- true
		if ("pgIf") BnK()
		elif (20.66) for fOK until 53.84 by 77.18
			bool cG[94.68,75.38]
	end

func WAH (bool HRi[57.02], number aADz)	return
'''
		expect = '''Program([FuncDecl(Id(ff3), [VarDecl(Id(JfM), StringType, None, None), VarDecl(Id(jIiO), NumberType, None, None)], Return()), FuncDecl(Id(TZzH), [], Return()), FuncDecl(Id(l5), [VarDecl(Id(ja), ArrayType([34.13], BoolType), None, None), VarDecl(Id(dYon), ArrayType([97.68, 54.54, 17.39], NumberType), None, None), VarDecl(Id(RN), NumberType, None, None)], Block([CallStmt(Id(c_xA), []), VarDecl(Id(g1G), ArrayType([68.77], StringType), None, BooleanLit(True)), If(StringLit(pgIf), CallStmt(Id(BnK), [])), [(NumLit(20.66), For(Id(fOK), NumLit(53.84), NumLit(77.18), VarDecl(Id(cG), ArrayType([94.68, 75.38], BoolType), None, None)))], None])), FuncDecl(Id(WAH), [VarDecl(Id(HRi), ArrayType([57.02], BoolType), None, None), VarDecl(Id(aADz), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115146))

	def test_21530115147(self):
		input = '''
func rKL ()	begin
		if (53.98)
		continue
		elif ("Ihj") begin
			lWf("VL", 4.12)
		end
		elif (61.06)
		return
		elif (70.95)
		if (BO6)
		for zPF until 63.14 by 12.9
			for K_zQ until "B" by 60.95
				continue
		elif ("IT") continue
		elif (true)
		return true
		elif (Mjkc) return "fMSpT"
		elif (true) g73("DuG")
		elif (true)
		continue
		else for hrVY until 49.92 by "bU"
			dynamic Xr <- 5.21
		return true
		return
	end

func qExm (bool QS, string JYLI)
	return
'''
		expect = '''Program([FuncDecl(Id(rKL), [], Block([If(NumLit(53.98), Continue), [(StringLit(Ihj), Block([CallStmt(Id(lWf), [StringLit(VL), NumLit(4.12)])])), (NumLit(61.06), Return()), (NumLit(70.95), If(Id(BO6), For(Id(zPF), NumLit(63.14), NumLit(12.9), For(Id(K_zQ), StringLit(B), NumLit(60.95), Continue))), [(StringLit(IT), Continue), (BooleanLit(True), Return(BooleanLit(True))), (Id(Mjkc), Return(StringLit(fMSpT))), (BooleanLit(True), CallStmt(Id(g73), [StringLit(DuG)]))], None), (BooleanLit(True), Continue)], For(Id(hrVY), NumLit(49.92), StringLit(bU), VarDecl(Id(Xr), None, dynamic, NumLit(5.21))), Return(BooleanLit(True)), Return()])), FuncDecl(Id(qExm), [VarDecl(Id(QS), BoolType, None, None), VarDecl(Id(JYLI), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115147))

	def test_21530115148(self):
		input = '''
number k98q
bool BGI[88.21,37.03]
string dThV[47.53,13.45]
bool BU_B[10.96]
func j60 (bool Hs, string Cfr1[99.4])
	return false

'''
		expect = '''Program([VarDecl(Id(k98q), NumberType, None, None), VarDecl(Id(BGI), ArrayType([88.21, 37.03], BoolType), None, None), VarDecl(Id(dThV), ArrayType([47.53, 13.45], StringType), None, None), VarDecl(Id(BU_B), ArrayType([10.96], BoolType), None, None), FuncDecl(Id(j60), [VarDecl(Id(Hs), BoolType, None, None), VarDecl(Id(Cfr1), ArrayType([99.4], StringType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115148))

	def test_21530115149(self):
		input = '''
func cW_h (bool PFTq[30.41], bool bo[62.48,54.25,26.82], number C9)	begin
		return "e"
		string e6MG[9.52,24.48,20.76]
		for Zm until "E" by 58.15
			rC(xbD7)
	end
'''
		expect = '''Program([FuncDecl(Id(cW_h), [VarDecl(Id(PFTq), ArrayType([30.41], BoolType), None, None), VarDecl(Id(bo), ArrayType([62.48, 54.25, 26.82], BoolType), None, None), VarDecl(Id(C9), NumberType, None, None)], Block([Return(StringLit(e)), VarDecl(Id(e6MG), ArrayType([9.52, 24.48, 20.76], StringType), None, None), For(Id(Zm), StringLit(E), NumLit(58.15), CallStmt(Id(rC), [Id(xbD7)]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115149))

	def test_21530115150(self):
		input = '''
string GM[41.77,64.99] <- false
func bTQ (number zEM[94.18,28.39,88.93], bool SmD)
	return
string qaDg[40.75]
func N46 (number ft5u, string cDwn, number T0Mm[4.82])	begin
		continue
		return 66.34
		break
	end
string ei <- true
'''
		expect = '''Program([VarDecl(Id(GM), ArrayType([41.77, 64.99], StringType), None, BooleanLit(False)), FuncDecl(Id(bTQ), [VarDecl(Id(zEM), ArrayType([94.18, 28.39, 88.93], NumberType), None, None), VarDecl(Id(SmD), BoolType, None, None)], Return()), VarDecl(Id(qaDg), ArrayType([40.75], StringType), None, None), FuncDecl(Id(N46), [VarDecl(Id(ft5u), NumberType, None, None), VarDecl(Id(cDwn), StringType, None, None), VarDecl(Id(T0Mm), ArrayType([4.82], NumberType), None, None)], Block([Continue, Return(NumLit(66.34)), Break])), VarDecl(Id(ei), StringType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115150))

	def test_21530115151(self):
		input = '''
func l9 (string Noea, number Cf[65.18,87.58], bool eLk)
	begin
		MqR9()
	end

func R4N ()	begin
	end

dynamic F7 <- 86.49
string NA
func WQF ()	begin
	end

'''
		expect = '''Program([FuncDecl(Id(l9), [VarDecl(Id(Noea), StringType, None, None), VarDecl(Id(Cf), ArrayType([65.18, 87.58], NumberType), None, None), VarDecl(Id(eLk), BoolType, None, None)], Block([CallStmt(Id(MqR9), [])])), FuncDecl(Id(R4N), [], Block([])), VarDecl(Id(F7), None, dynamic, NumLit(86.49)), VarDecl(Id(NA), StringType, None, None), FuncDecl(Id(WQF), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115151))

	def test_21530115152(self):
		input = '''
func N3n (string uTV, string sK, bool OQk[18.44])
	return
number tOS[28.15] <- WCm
func dRer (string St)	begin
		if (vJ)
		return Ctx
		elif (33.34)
		if (false)
		if ("FSMot") if (false) begin
			if (20.67)
			WUTX(true, true, false)
			elif (45.27) bool z9wz
			elif (vNEk) string Tq[98.71]
			else M3S <- "IOLjf"
			if (kvpj)
			continue
			elif (tzds) for Cl until true by false
				continue
			elif ("vSt") lFu[false] <- 40.14
			return true
		end
		elif (true) begin
			break
		end
		elif (5.91)
		hb(false, true, "z")
		elif ("D") if (true) if (true) return
		elif (AQ)
		break
		elif ("z")
		break
		elif ("YpI") if (true)
		break
		elif ("R")
		KK <- 31.19
		elif (37.38) begin
			number guRK[54.38] <- 76.96
			begin
			end
			begin
				string q3 <- 29.58
			end
		end
		elif (29.04) var ab <- "Md"
		elif (false)
		bool QB <- false
		else continue
		else begin
		end
		elif (iFX) number AV[30.16,84.13] <- McEp
		else QoZ("OZOhu", vM6, "jSmk")
		elif (Ox)
		OSO <- "NE"
		elif (vtuQ) begin
			continue
		end
		elif (H7A) if (true) break
		elif (CjF)
		return 6.8
		elif (Q4NU)
		for Ic until 61.78 by true
			break
		else break
		elif (true) goaq <- "zplU"
		elif (63.41)
		begin
			for Ue until false by p_R
				break
		end
		elif ("LsP") if (86.47) return
		elif (true)
		if ("JZC") begin
			begin
				continue
			end
			return
			break
		end
		elif ("DrfZr") begin
			if (64.43)
			var O44 <- true
			elif (tl) begin
			end
			elif (85.46) break
			elif ("xZkRD")
			begin
				return "ah"
				begin
					string uulU <- "jzaU"
					break
				end
				break
			end
			else return false
			begin
				if (39.55) for Ew until VI6a by 58.02
					continue
				elif (60.36)
				Cqwy["OL", 45.19, true] <- true
				else begin
					if ("ZvIo") if (true)
					continue
					elif ("r") h9()
					elif (96.56)
					number Ww[61.57,11.72]
					else break
				end
				break
			end
			continue
		end
		else if (43.04)
		continue
		elif ("OpvT") for fSve until zBP4 by uT2_
			gV4k()
		elif ("diq")
		return
		elif (79.65) for Jey until 0.46 by true
			continue
		elif (EtL)
		begin
			break
		end
		else break
		elif ("clNP") begin
		end
		elif ("MbqM")
		begin
			OSZ()
			string Xm3P[51.92,27.13,15.69] <- "aWL"
			dynamic rzBq <- 80.72
		end
		elif ("g")
		return
		else return bUi
		elif ("Uh") continue
		elif (4.37)
		for Nku until 29.1 by false
			string FV94
		elif (false) nc()
		begin
			continue
		end
	end

bool fw[9.91,37.26]
'''
		expect = '''Program([FuncDecl(Id(N3n), [VarDecl(Id(uTV), StringType, None, None), VarDecl(Id(sK), StringType, None, None), VarDecl(Id(OQk), ArrayType([18.44], BoolType), None, None)], Return()), VarDecl(Id(tOS), ArrayType([28.15], NumberType), None, Id(WCm)), FuncDecl(Id(dRer), [VarDecl(Id(St), StringType, None, None)], Block([If(Id(vJ), Return(Id(Ctx))), [(NumLit(33.34), If(BooleanLit(False), If(StringLit(FSMot), If(BooleanLit(False), Block([If(NumLit(20.67), CallStmt(Id(WUTX), [BooleanLit(True), BooleanLit(True), BooleanLit(False)])), [(NumLit(45.27), VarDecl(Id(z9wz), BoolType, None, None)), (Id(vNEk), VarDecl(Id(Tq), ArrayType([98.71], StringType), None, None))], AssignStmt(Id(M3S), StringLit(IOLjf)), If(Id(kvpj), Continue), [(Id(tzds), For(Id(Cl), BooleanLit(True), BooleanLit(False), Continue)), (StringLit(vSt), AssignStmt(ArrayCell(Id(lFu), [BooleanLit(False)]), NumLit(40.14)))], None, Return(BooleanLit(True))])), [(BooleanLit(True), Block([Break])), (NumLit(5.91), CallStmt(Id(hb), [BooleanLit(False), BooleanLit(True), StringLit(z)])), (StringLit(D), If(BooleanLit(True), If(BooleanLit(True), Return()), [(Id(AQ), Break), (StringLit(z), Break), (StringLit(YpI), If(BooleanLit(True), Break), [(StringLit(R), AssignStmt(Id(KK), NumLit(31.19))), (NumLit(37.38), Block([VarDecl(Id(guRK), ArrayType([54.38], NumberType), None, NumLit(76.96)), Block([]), Block([VarDecl(Id(q3), StringType, None, NumLit(29.58))])])), (NumLit(29.04), VarDecl(Id(ab), None, var, StringLit(Md)))], None), (BooleanLit(False), VarDecl(Id(QB), BoolType, None, BooleanLit(False)))], Continue), [], Block([])), (Id(iFX), VarDecl(Id(AV), ArrayType([30.16, 84.13], NumberType), None, Id(McEp)))], CallStmt(Id(QoZ), [StringLit(OZOhu), Id(vM6), StringLit(jSmk)])), [(Id(Ox), AssignStmt(Id(OSO), StringLit(NE))), (Id(vtuQ), Block([Continue])), (Id(H7A), If(BooleanLit(True), Break), [(Id(CjF), Return(NumLit(6.8))), (Id(Q4NU), For(Id(Ic), NumLit(61.78), BooleanLit(True), Break))], Break), (BooleanLit(True), AssignStmt(Id(goaq), StringLit(zplU))), (NumLit(63.41), Block([For(Id(Ue), BooleanLit(False), Id(p_R), Break)])), (StringLit(LsP), If(NumLit(86.47), Return()), [(BooleanLit(True), If(StringLit(JZC), Block([Block([Continue]), Return(), Break])), [(StringLit(DrfZr), Block([If(NumLit(64.43), VarDecl(Id(O44), None, var, BooleanLit(True))), [(Id(tl), Block([])), (NumLit(85.46), Break), (StringLit(xZkRD), Block([Return(StringLit(ah)), Block([VarDecl(Id(uulU), StringType, None, StringLit(jzaU)), Break]), Break]))], Return(BooleanLit(False)), Block([If(NumLit(39.55), For(Id(Ew), Id(VI6a), NumLit(58.02), Continue)), [(NumLit(60.36), AssignStmt(ArrayCell(Id(Cqwy), [StringLit(OL), NumLit(45.19), BooleanLit(True)]), BooleanLit(True)))], Block([If(StringLit(ZvIo), If(BooleanLit(True), Continue), [(StringLit(r), CallStmt(Id(h9), [])), (NumLit(96.56), VarDecl(Id(Ww), ArrayType([61.57, 11.72], NumberType), None, None))], Break), [], None]), Break]), Continue]))], If(NumLit(43.04), Continue), [(StringLit(OpvT), For(Id(fSve), Id(zBP4), Id(uT2_), CallStmt(Id(gV4k), []))), (StringLit(diq), Return()), (NumLit(79.65), For(Id(Jey), NumLit(0.46), BooleanLit(True), Continue)), (Id(EtL), Block([Break]))], Break), (StringLit(clNP), Block([])), (StringLit(MbqM), Block([CallStmt(Id(OSZ), []), VarDecl(Id(Xm3P), ArrayType([51.92, 27.13, 15.69], StringType), None, StringLit(aWL)), VarDecl(Id(rzBq), None, dynamic, NumLit(80.72))])), (StringLit(g), Return())], Return(Id(bUi))), (StringLit(Uh), Continue), (NumLit(4.37), For(Id(Nku), NumLit(29.1), BooleanLit(False), VarDecl(Id(FV94), StringType, None, None)))], None), [], None), (BooleanLit(False), CallStmt(Id(nc), []))], None, Block([Continue])])), VarDecl(Id(fw), ArrayType([9.91, 37.26], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115152))

	def test_21530115153(self):
		input = '''
string s5V[85.43,80.94]
'''
		expect = '''Program([VarDecl(Id(s5V), ArrayType([85.43, 80.94], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115153))

	def test_21530115154(self):
		input = '''
func Skep (bool Pe)
	return false

string IZ1[51.33,67.67,90.3] <- true
bool dkn[20.26] <- vq
'''
		expect = '''Program([FuncDecl(Id(Skep), [VarDecl(Id(Pe), BoolType, None, None)], Return(BooleanLit(False))), VarDecl(Id(IZ1), ArrayType([51.33, 67.67, 90.3], StringType), None, BooleanLit(True)), VarDecl(Id(dkn), ArrayType([20.26], BoolType), None, Id(vq))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115154))

	def test_21530115155(self):
		input = '''
func M2Y (string TvhP[23.21])
	begin
		for ylNl until o5h by true
			break
	end

'''
		expect = '''Program([FuncDecl(Id(M2Y), [VarDecl(Id(TvhP), ArrayType([23.21], StringType), None, None)], Block([For(Id(ylNl), Id(o5h), BooleanLit(True), Break)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115155))

	def test_21530115156(self):
		input = '''
func fxK4 ()
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(fxK4), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115156))

	def test_21530115157(self):
		input = '''
string gF[66.57,99.73]
bool ebTZ[67.04,85.37] <- false
'''
		expect = '''Program([VarDecl(Id(gF), ArrayType([66.57, 99.73], StringType), None, None), VarDecl(Id(ebTZ), ArrayType([67.04, 85.37], BoolType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115157))

	def test_21530115158(self):
		input = '''
func rPmM (bool ol[89.74,70.73,58.29], bool Bllg)	return vyZ
'''
		expect = '''Program([FuncDecl(Id(rPmM), [VarDecl(Id(ol), ArrayType([89.74, 70.73, 58.29], BoolType), None, None), VarDecl(Id(Bllg), BoolType, None, None)], Return(Id(vyZ)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115158))

	def test_21530115159(self):
		input = '''
bool QXg[54.44,99.56] <- "W"
bool cuQg
'''
		expect = '''Program([VarDecl(Id(QXg), ArrayType([54.44, 99.56], BoolType), None, StringLit(W)), VarDecl(Id(cuQg), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115159))

	def test_21530115160(self):
		input = '''
func kJ2x (string K1[77.88,36.24,34.12])
	begin
		begin
			break
			break
			begin
			end
		end
		HTcc[81.82, 68.74, "uKXM"] <- "pEF"
	end
'''
		expect = '''Program([FuncDecl(Id(kJ2x), [VarDecl(Id(K1), ArrayType([77.88, 36.24, 34.12], StringType), None, None)], Block([Block([Break, Break, Block([])]), AssignStmt(ArrayCell(Id(HTcc), [NumLit(81.82), NumLit(68.74), StringLit(uKXM)]), StringLit(pEF))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115160))

	def test_21530115161(self):
		input = '''
func l2 (number JBYO[38.7])
	return

bool DblL[43.15]
number WH[59.68,50.25,75.47]
bool wTMp[38.02,0.96,49.85]
'''
		expect = '''Program([FuncDecl(Id(l2), [VarDecl(Id(JBYO), ArrayType([38.7], NumberType), None, None)], Return()), VarDecl(Id(DblL), ArrayType([43.15], BoolType), None, None), VarDecl(Id(WH), ArrayType([59.68, 50.25, 75.47], NumberType), None, None), VarDecl(Id(wTMp), ArrayType([38.02, 0.96, 49.85], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115161))

	def test_21530115162(self):
		input = '''
func EG7b ()
	return false
func yfnK ()
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(EG7b), [], Return(BooleanLit(False))), FuncDecl(Id(yfnK), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115162))

	def test_21530115163(self):
		input = '''
func ibD ()	begin
	end
func nh (bool iijU, string m9_5[34.97])
	begin
		for kEcH until coqn by "olg"
			return 7.97
		for jvwH until "m" by 40.06
			QeU6[bJR, false] <- 21.61
		continue
	end

func jL (string EotJ)
	return 23.46

'''
		expect = '''Program([FuncDecl(Id(ibD), [], Block([])), FuncDecl(Id(nh), [VarDecl(Id(iijU), BoolType, None, None), VarDecl(Id(m9_5), ArrayType([34.97], StringType), None, None)], Block([For(Id(kEcH), Id(coqn), StringLit(olg), Return(NumLit(7.97))), For(Id(jvwH), StringLit(m), NumLit(40.06), AssignStmt(ArrayCell(Id(QeU6), [Id(bJR), BooleanLit(False)]), NumLit(21.61))), Continue])), FuncDecl(Id(jL), [VarDecl(Id(EotJ), StringType, None, None)], Return(NumLit(23.46)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115163))

	def test_21530115164(self):
		input = '''
bool YJe
func eys (number Av16)
	begin
		KIPE[81.91] <- false
		string JD60
	end
func I8p ()	return true

func GR (bool N3, number q8M4, number LKy)
	return "m"
bool kWEq <- 15.41
'''
		expect = '''Program([VarDecl(Id(YJe), BoolType, None, None), FuncDecl(Id(eys), [VarDecl(Id(Av16), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(KIPE), [NumLit(81.91)]), BooleanLit(False)), VarDecl(Id(JD60), StringType, None, None)])), FuncDecl(Id(I8p), [], Return(BooleanLit(True))), FuncDecl(Id(GR), [VarDecl(Id(N3), BoolType, None, None), VarDecl(Id(q8M4), NumberType, None, None), VarDecl(Id(LKy), NumberType, None, None)], Return(StringLit(m))), VarDecl(Id(kWEq), BoolType, None, NumLit(15.41))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115164))

	def test_21530115165(self):
		input = '''
bool Ns[79.77,63.86] <- false
number WnsC
func Ey2U (number JI, string Nt, string R9zW)	return
dynamic rJ
'''
		expect = '''Program([VarDecl(Id(Ns), ArrayType([79.77, 63.86], BoolType), None, BooleanLit(False)), VarDecl(Id(WnsC), NumberType, None, None), FuncDecl(Id(Ey2U), [VarDecl(Id(JI), NumberType, None, None), VarDecl(Id(Nt), StringType, None, None), VarDecl(Id(R9zW), StringType, None, None)], Return()), VarDecl(Id(rJ), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115165))

	def test_21530115166(self):
		input = '''
bool LL1
func aD (number vMt, bool aVs8[12.85], string qu)
	return

bool G6P[60.94,47.69]
'''
		expect = '''Program([VarDecl(Id(LL1), BoolType, None, None), FuncDecl(Id(aD), [VarDecl(Id(vMt), NumberType, None, None), VarDecl(Id(aVs8), ArrayType([12.85], BoolType), None, None), VarDecl(Id(qu), StringType, None, None)], Return()), VarDecl(Id(G6P), ArrayType([60.94, 47.69], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115166))

	def test_21530115167(self):
		input = '''
func hB3 (string cZF, bool wJ[93.53], string QH)	return w594
'''
		expect = '''Program([FuncDecl(Id(hB3), [VarDecl(Id(cZF), StringType, None, None), VarDecl(Id(wJ), ArrayType([93.53], BoolType), None, None), VarDecl(Id(QH), StringType, None, None)], Return(Id(w594)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115167))

	def test_21530115168(self):
		input = '''
string OC7[0.62] <- HwZF
dynamic nH <- "QMufY"
func xL (string dZc, string XdwD, string E9OA[27.3,61.11,50.81])	return
'''
		expect = '''Program([VarDecl(Id(OC7), ArrayType([0.62], StringType), None, Id(HwZF)), VarDecl(Id(nH), None, dynamic, StringLit(QMufY)), FuncDecl(Id(xL), [VarDecl(Id(dZc), StringType, None, None), VarDecl(Id(XdwD), StringType, None, None), VarDecl(Id(E9OA), ArrayType([27.3, 61.11, 50.81], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115168))

	def test_21530115169(self):
		input = '''
func IQLI (string sBSg)
	begin
		return
		for nqt until RnQM by true
			return
	end

func ldso (number UmeD[84.56,17.45,61.96], number MLYA, string GX[29.35])
	return true

func Am ()
	begin
		x3Q[true] <- true
		w5aL("hGuem", qrgx, KD)
	end
var nhk <- 89.38
number Jq4P[85.35,55.29,66.41]
'''
		expect = '''Program([FuncDecl(Id(IQLI), [VarDecl(Id(sBSg), StringType, None, None)], Block([Return(), For(Id(nqt), Id(RnQM), BooleanLit(True), Return())])), FuncDecl(Id(ldso), [VarDecl(Id(UmeD), ArrayType([84.56, 17.45, 61.96], NumberType), None, None), VarDecl(Id(MLYA), NumberType, None, None), VarDecl(Id(GX), ArrayType([29.35], StringType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(Am), [], Block([AssignStmt(ArrayCell(Id(x3Q), [BooleanLit(True)]), BooleanLit(True)), CallStmt(Id(w5aL), [StringLit(hGuem), Id(qrgx), Id(KD)])])), VarDecl(Id(nhk), None, var, NumLit(89.38)), VarDecl(Id(Jq4P), ArrayType([85.35, 55.29, 66.41], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115169))

	def test_21530115170(self):
		input = '''
func mC (bool sk[72.89], bool EO4[5.41,40.31,90.8], number mI[98.39])	return j7JC

'''
		expect = '''Program([FuncDecl(Id(mC), [VarDecl(Id(sk), ArrayType([72.89], BoolType), None, None), VarDecl(Id(EO4), ArrayType([5.41, 40.31, 90.8], BoolType), None, None), VarDecl(Id(mI), ArrayType([98.39], NumberType), None, None)], Return(Id(j7JC)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115170))

	def test_21530115171(self):
		input = '''
dynamic GQ <- SvZf
'''
		expect = '''Program([VarDecl(Id(GQ), None, dynamic, Id(SvZf))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115171))

	def test_21530115172(self):
		input = '''
dynamic VFYs <- vHB
var nJUz <- 19.36
'''
		expect = '''Program([VarDecl(Id(VFYs), None, dynamic, Id(vHB)), VarDecl(Id(nJUz), None, var, NumLit(19.36))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115172))

	def test_21530115173(self):
		input = '''
number OhhQ[9.05,56.47,57.21]
number lv <- Kg7
number UT76 <- "Q"
func T3 ()	return "Y"

number Bj[99.72,11.0]
'''
		expect = '''Program([VarDecl(Id(OhhQ), ArrayType([9.05, 56.47, 57.21], NumberType), None, None), VarDecl(Id(lv), NumberType, None, Id(Kg7)), VarDecl(Id(UT76), NumberType, None, StringLit(Q)), FuncDecl(Id(T3), [], Return(StringLit(Y))), VarDecl(Id(Bj), ArrayType([99.72, 11.0], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115173))

	def test_21530115174(self):
		input = '''
func PfX (string QaS, string bzm[56.44,15.7], number oL)	return "nx"

'''
		expect = '''Program([FuncDecl(Id(PfX), [VarDecl(Id(QaS), StringType, None, None), VarDecl(Id(bzm), ArrayType([56.44, 15.7], StringType), None, None), VarDecl(Id(oL), NumberType, None, None)], Return(StringLit(nx)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115174))

	def test_21530115175(self):
		input = '''
number IcBO[0.94,45.66,90.65] <- true
dynamic maI1 <- true
'''
		expect = '''Program([VarDecl(Id(IcBO), ArrayType([0.94, 45.66, 90.65], NumberType), None, BooleanLit(True)), VarDecl(Id(maI1), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115175))

	def test_21530115176(self):
		input = '''
func e2 ()
	return 8.13
var FniM <- "jK"
string EaO0[28.73,21.04,16.77] <- false
'''
		expect = '''Program([FuncDecl(Id(e2), [], Return(NumLit(8.13))), VarDecl(Id(FniM), None, var, StringLit(jK)), VarDecl(Id(EaO0), ArrayType([28.73, 21.04, 16.77], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115176))

	def test_21530115177(self):
		input = '''
bool Chp[88.83,4.84,45.18]
bool lTm4[67.13,37.66] <- qf_H
func b5U (string JpI, string VXrA)	begin
	end

number PTm
'''
		expect = '''Program([VarDecl(Id(Chp), ArrayType([88.83, 4.84, 45.18], BoolType), None, None), VarDecl(Id(lTm4), ArrayType([67.13, 37.66], BoolType), None, Id(qf_H)), FuncDecl(Id(b5U), [VarDecl(Id(JpI), StringType, None, None), VarDecl(Id(VXrA), StringType, None, None)], Block([])), VarDecl(Id(PTm), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115177))

	def test_21530115178(self):
		input = '''
number Gt[7.31,91.93,43.2]
func a8 (string jpi, string inz)	return

string h0[7.56,0.04,34.58]
'''
		expect = '''Program([VarDecl(Id(Gt), ArrayType([7.31, 91.93, 43.2], NumberType), None, None), FuncDecl(Id(a8), [VarDecl(Id(jpi), StringType, None, None), VarDecl(Id(inz), StringType, None, None)], Return()), VarDecl(Id(h0), ArrayType([7.56, 0.04, 34.58], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115178))

	def test_21530115179(self):
		input = '''
func Dxz (bool Qq[34.14], number Lqe[48.7,87.37])
	return 23.6

number nTf[48.53]
string BCY5[60.6]
func PWJe (bool hi[29.02])
	begin
		ur(lcEB, false)
	end

string N4YV <- true
'''
		expect = '''Program([FuncDecl(Id(Dxz), [VarDecl(Id(Qq), ArrayType([34.14], BoolType), None, None), VarDecl(Id(Lqe), ArrayType([48.7, 87.37], NumberType), None, None)], Return(NumLit(23.6))), VarDecl(Id(nTf), ArrayType([48.53], NumberType), None, None), VarDecl(Id(BCY5), ArrayType([60.6], StringType), None, None), FuncDecl(Id(PWJe), [VarDecl(Id(hi), ArrayType([29.02], BoolType), None, None)], Block([CallStmt(Id(ur), [Id(lcEB), BooleanLit(False)])])), VarDecl(Id(N4YV), StringType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115179))

	def test_21530115180(self):
		input = '''
func v81 (string sgs[96.64,9.6], bool EjTO, number V2A)
	begin
	end
func uuQ9 (bool aMI[45.71], number nYaj, string jNA)
	return

'''
		expect = '''Program([FuncDecl(Id(v81), [VarDecl(Id(sgs), ArrayType([96.64, 9.6], StringType), None, None), VarDecl(Id(EjTO), BoolType, None, None), VarDecl(Id(V2A), NumberType, None, None)], Block([])), FuncDecl(Id(uuQ9), [VarDecl(Id(aMI), ArrayType([45.71], BoolType), None, None), VarDecl(Id(nYaj), NumberType, None, None), VarDecl(Id(jNA), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115180))

	def test_21530115181(self):
		input = '''
dynamic Nu
'''
		expect = '''Program([VarDecl(Id(Nu), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115181))

	def test_21530115182(self):
		input = '''
string HOJ[16.12,97.88]
'''
		expect = '''Program([VarDecl(Id(HOJ), ArrayType([16.12, 97.88], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115182))

	def test_21530115183(self):
		input = '''
func Qc (number F6Pc, number ap0r[27.42,16.5,4.72], string fvt[81.59,19.03,20.38])	begin
	end
func aR (number FYaA)
	begin
	end

bool fI[88.62]
func oG (bool M8[99.02], number poFG[30.13,72.98,6.61])
	return 39.64

'''
		expect = '''Program([FuncDecl(Id(Qc), [VarDecl(Id(F6Pc), NumberType, None, None), VarDecl(Id(ap0r), ArrayType([27.42, 16.5, 4.72], NumberType), None, None), VarDecl(Id(fvt), ArrayType([81.59, 19.03, 20.38], StringType), None, None)], Block([])), FuncDecl(Id(aR), [VarDecl(Id(FYaA), NumberType, None, None)], Block([])), VarDecl(Id(fI), ArrayType([88.62], BoolType), None, None), FuncDecl(Id(oG), [VarDecl(Id(M8), ArrayType([99.02], BoolType), None, None), VarDecl(Id(poFG), ArrayType([30.13, 72.98, 6.61], NumberType), None, None)], Return(NumLit(39.64)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115183))

	def test_21530115184(self):
		input = '''
func Eskt (bool D0qc[9.74,30.87], number HF8r[53.11])	return aO

func b5W6 ()
	return
func j9 (bool Xru[72.27,26.87,43.74], bool YLM)	return
'''
		expect = '''Program([FuncDecl(Id(Eskt), [VarDecl(Id(D0qc), ArrayType([9.74, 30.87], BoolType), None, None), VarDecl(Id(HF8r), ArrayType([53.11], NumberType), None, None)], Return(Id(aO))), FuncDecl(Id(b5W6), [], Return()), FuncDecl(Id(j9), [VarDecl(Id(Xru), ArrayType([72.27, 26.87, 43.74], BoolType), None, None), VarDecl(Id(YLM), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115184))

	def test_21530115185(self):
		input = '''
func rT4P (string gb[91.25,6.54,64.39], bool YcV[88.95])	begin
		continue
		eZ["b", false] <- "A"
	end
func dK (number ya1J[14.67,71.99,76.28], number ImXZ, bool M0[19.16,65.19])	begin
		Jdh(28.64, true, true)
		if (17.68)
		for ZAA until PZ by 36.02
			Iu[true, 91.58, false] <- "mDmTZ"
		elif (LG0) aF(le, false, "CktDs")
		elif (32.35)
		if (2.34) xtKq()
		elif (true)
		return "dQknw"
		elif (49.75) for s51V until "S" by "a"
			k9[true] <- Zb6
		elif (azjg) if (true) for ih until 67.25 by k9F
			for Gu until "EBdmn" by 21.82
				pFN(32.49, "iI", false)
		elif ("IE") continue
		else continue
		elif (42.67) if (hAhS) begin
		end
		elif ("vBZ")
		begin
			break
			return
			break
		end
		elif (ovs) if (true) bool F6u[35.34,41.44,95.17] <- iRnk
		elif (25.57) if (30.29) for MK2 until true by "H"
			return
		elif (true) begin
			if (TwA) uD[79.08] <- "Fkv"
			elif (88.6)
			bool cP[58.5] <- qvFh
			elif (37.08) return "Vot"
			elif (8.12) for sr until qE8 by "Kral"
				bool tyRS[33.96]
			elif (lvAI) continue
			elif (true)
			begin
				number opy[61.38,24.22]
				for I0B until false by "jP"
					V0nj <- "pfxI"
				return
			end
			lIN <- true
		end
		elif ("YEx")
		for GQ until true by true
			MCU_(49.53, false)
		elif ("xmj") for cK until 70.25 by true
			if (KA) return 97.23
			elif (true)
			break
			elif ("e")
			begin
				break
				continue
				continue
			end
			elif (true)
			break
		elif (true)
		continue
		else continue
		elif (36.57) for GGZ until 87.33 by "K"
			break
		elif (WR)
		break
		elif (false)
		begin
			number Mj2E
		end
		elif (false) continue
		elif ("MNwly") string Pg_
		else TH(true)
		elif (vkQ)
		begin
			for De until "qYNex" by 65.76
				break
			if (Q4_)
			return
			elif ("uIpr") FcA <- 38.89
			elif (d0h) for QGlB until vLAy by FSdJ
				begin
					begin
						break
					end
					return aL
					for kM until "QMPL" by sp
						begin
							continue
						end
				end
			elif (F9I) break
			continue
		end
	end

bool Xy0J[73.24,70.47,27.64] <- true
func bzEu (string J5z[35.06,37.7])	begin
		if ("h") H4F <- "ctXXW"
		elif ("itHwE")
		for sn until "w" by true
			break
		elif ("q") if (true) t4X(52.14, false)
		elif (ZE)
		begin
			for Xpij until "k" by "MnzsC"
				number tB <- DC
		end
		elif (true)
		for ak until false by 21.53
			break
		elif (PxHJ) KBas("WKrb")
		elif (iU)
		gdul <- false
		elif ("ClF")
		string twVQ[57.24,54.88] <- true
		elif (false) break
		bL3(83.69, M6HE, 89.86)
		return
	end
'''
		expect = '''Program([FuncDecl(Id(rT4P), [VarDecl(Id(gb), ArrayType([91.25, 6.54, 64.39], StringType), None, None), VarDecl(Id(YcV), ArrayType([88.95], BoolType), None, None)], Block([Continue, AssignStmt(ArrayCell(Id(eZ), [StringLit(b), BooleanLit(False)]), StringLit(A))])), FuncDecl(Id(dK), [VarDecl(Id(ya1J), ArrayType([14.67, 71.99, 76.28], NumberType), None, None), VarDecl(Id(ImXZ), NumberType, None, None), VarDecl(Id(M0), ArrayType([19.16, 65.19], BoolType), None, None)], Block([CallStmt(Id(Jdh), [NumLit(28.64), BooleanLit(True), BooleanLit(True)]), If(NumLit(17.68), For(Id(ZAA), Id(PZ), NumLit(36.02), AssignStmt(ArrayCell(Id(Iu), [BooleanLit(True), NumLit(91.58), BooleanLit(False)]), StringLit(mDmTZ)))), [(Id(LG0), CallStmt(Id(aF), [Id(le), BooleanLit(False), StringLit(CktDs)])), (NumLit(32.35), If(NumLit(2.34), CallStmt(Id(xtKq), [])), [(BooleanLit(True), Return(StringLit(dQknw))), (NumLit(49.75), For(Id(s51V), StringLit(S), StringLit(a), AssignStmt(ArrayCell(Id(k9), [BooleanLit(True)]), Id(Zb6)))), (Id(azjg), If(BooleanLit(True), For(Id(ih), NumLit(67.25), Id(k9F), For(Id(Gu), StringLit(EBdmn), NumLit(21.82), CallStmt(Id(pFN), [NumLit(32.49), StringLit(iI), BooleanLit(False)])))), [(StringLit(IE), Continue)], Continue), (NumLit(42.67), If(Id(hAhS), Block([])), [(StringLit(vBZ), Block([Break, Return(), Break])), (Id(ovs), If(BooleanLit(True), VarDecl(Id(F6u), ArrayType([35.34, 41.44, 95.17], BoolType), None, Id(iRnk))), [(NumLit(25.57), If(NumLit(30.29), For(Id(MK2), BooleanLit(True), StringLit(H), Return())), [(BooleanLit(True), Block([If(Id(TwA), AssignStmt(ArrayCell(Id(uD), [NumLit(79.08)]), StringLit(Fkv))), [(NumLit(88.6), VarDecl(Id(cP), ArrayType([58.5], BoolType), None, Id(qvFh))), (NumLit(37.08), Return(StringLit(Vot))), (NumLit(8.12), For(Id(sr), Id(qE8), StringLit(Kral), VarDecl(Id(tyRS), ArrayType([33.96], BoolType), None, None))), (Id(lvAI), Continue), (BooleanLit(True), Block([VarDecl(Id(opy), ArrayType([61.38, 24.22], NumberType), None, None), For(Id(I0B), BooleanLit(False), StringLit(jP), AssignStmt(Id(V0nj), StringLit(pfxI))), Return()]))], None, AssignStmt(Id(lIN), BooleanLit(True))])), (StringLit(YEx), For(Id(GQ), BooleanLit(True), BooleanLit(True), CallStmt(Id(MCU_), [NumLit(49.53), BooleanLit(False)]))), (StringLit(xmj), For(Id(cK), NumLit(70.25), BooleanLit(True), If(Id(KA), Return(NumLit(97.23))), [(BooleanLit(True), Break), (StringLit(e), Block([Break, Continue, Continue])), (BooleanLit(True), Break), (BooleanLit(True), Continue)], Continue)), (NumLit(36.57), For(Id(GGZ), NumLit(87.33), StringLit(K), Break)), (Id(WR), Break)], None), (BooleanLit(False), Block([VarDecl(Id(Mj2E), NumberType, None, None)]))], None), (BooleanLit(False), Continue)], None), (StringLit(MNwly), VarDecl(Id(Pg_), StringType, None, None))], CallStmt(Id(TH), [BooleanLit(True)])), (Id(vkQ), Block([For(Id(De), StringLit(qYNex), NumLit(65.76), Break), If(Id(Q4_), Return()), [(StringLit(uIpr), AssignStmt(Id(FcA), NumLit(38.89))), (Id(d0h), For(Id(QGlB), Id(vLAy), Id(FSdJ), Block([Block([Break]), Return(Id(aL)), For(Id(kM), StringLit(QMPL), Id(sp), Block([Continue]))]))), (Id(F9I), Break)], None, Continue]))], None])), VarDecl(Id(Xy0J), ArrayType([73.24, 70.47, 27.64], BoolType), None, BooleanLit(True)), FuncDecl(Id(bzEu), [VarDecl(Id(J5z), ArrayType([35.06, 37.7], StringType), None, None)], Block([If(StringLit(h), AssignStmt(Id(H4F), StringLit(ctXXW))), [(StringLit(itHwE), For(Id(sn), StringLit(w), BooleanLit(True), Break)), (StringLit(q), If(BooleanLit(True), CallStmt(Id(t4X), [NumLit(52.14), BooleanLit(False)])), [(Id(ZE), Block([For(Id(Xpij), StringLit(k), StringLit(MnzsC), VarDecl(Id(tB), NumberType, None, Id(DC)))])), (BooleanLit(True), For(Id(ak), BooleanLit(False), NumLit(21.53), Break)), (Id(PxHJ), CallStmt(Id(KBas), [StringLit(WKrb)])), (Id(iU), AssignStmt(Id(gdul), BooleanLit(False))), (StringLit(ClF), VarDecl(Id(twVQ), ArrayType([57.24, 54.88], StringType), None, BooleanLit(True)))], None), (BooleanLit(False), Break)], None, CallStmt(Id(bL3), [NumLit(83.69), Id(M6HE), NumLit(89.86)]), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115185))

	def test_21530115186(self):
		input = '''
number tu0[19.97]
number h8 <- true
func JD (number FctT)
	return
'''
		expect = '''Program([VarDecl(Id(tu0), ArrayType([19.97], NumberType), None, None), VarDecl(Id(h8), NumberType, None, BooleanLit(True)), FuncDecl(Id(JD), [VarDecl(Id(FctT), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115186))

	def test_21530115187(self):
		input = '''
string zm5[36.89] <- phd
func lLfZ (bool Ui6)	begin
		break
	end

'''
		expect = '''Program([VarDecl(Id(zm5), ArrayType([36.89], StringType), None, Id(phd)), FuncDecl(Id(lLfZ), [VarDecl(Id(Ui6), BoolType, None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115187))

	def test_21530115188(self):
		input = '''
func I6b (string nB)
	return
dynamic Bk7r <- false
func ivqK ()	return "aEF"

func ysy ()	begin
	end

'''
		expect = '''Program([FuncDecl(Id(I6b), [VarDecl(Id(nB), StringType, None, None)], Return()), VarDecl(Id(Bk7r), None, dynamic, BooleanLit(False)), FuncDecl(Id(ivqK), [], Return(StringLit(aEF))), FuncDecl(Id(ysy), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115188))

	def test_21530115189(self):
		input = '''
string fg1[41.84,3.87]
func Gac_ ()	begin
		return
	end
func LP (number QU[30.99])
	begin
		for WNat until fOB by false
			mrf7()
		continue
		yk[90.17, 15.02, "NCa"] <- z8
	end
string y9[21.84]
func FrF ()
	return
'''
		expect = '''Program([VarDecl(Id(fg1), ArrayType([41.84, 3.87], StringType), None, None), FuncDecl(Id(Gac_), [], Block([Return()])), FuncDecl(Id(LP), [VarDecl(Id(QU), ArrayType([30.99], NumberType), None, None)], Block([For(Id(WNat), Id(fOB), BooleanLit(False), CallStmt(Id(mrf7), [])), Continue, AssignStmt(ArrayCell(Id(yk), [NumLit(90.17), NumLit(15.02), StringLit(NCa)]), Id(z8))])), VarDecl(Id(y9), ArrayType([21.84], StringType), None, None), FuncDecl(Id(FrF), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115189))

	def test_21530115190(self):
		input = '''
number O3[84.52] <- 89.22
bool VXR[60.71] <- SH
number nw0q <- 11.71
func SS (number mpbZ)
	return "a"
number HFR <- false
'''
		expect = '''Program([VarDecl(Id(O3), ArrayType([84.52], NumberType), None, NumLit(89.22)), VarDecl(Id(VXR), ArrayType([60.71], BoolType), None, Id(SH)), VarDecl(Id(nw0q), NumberType, None, NumLit(11.71)), FuncDecl(Id(SS), [VarDecl(Id(mpbZ), NumberType, None, None)], Return(StringLit(a))), VarDecl(Id(HFR), NumberType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115190))

	def test_21530115191(self):
		input = '''
func Js0 (string I5UI, string Cf[64.25], bool lBWz)	return false

bool ho <- AoS8
func tF82 (number qg_J, string T9[69.49,35.26,97.91], number g10H[22.75,94.43,55.65])
	return false

func Weo4 (number UBWw[59.33], number Egu)
	return "Eew"
string Qk <- 57.6
'''
		expect = '''Program([FuncDecl(Id(Js0), [VarDecl(Id(I5UI), StringType, None, None), VarDecl(Id(Cf), ArrayType([64.25], StringType), None, None), VarDecl(Id(lBWz), BoolType, None, None)], Return(BooleanLit(False))), VarDecl(Id(ho), BoolType, None, Id(AoS8)), FuncDecl(Id(tF82), [VarDecl(Id(qg_J), NumberType, None, None), VarDecl(Id(T9), ArrayType([69.49, 35.26, 97.91], StringType), None, None), VarDecl(Id(g10H), ArrayType([22.75, 94.43, 55.65], NumberType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(Weo4), [VarDecl(Id(UBWw), ArrayType([59.33], NumberType), None, None), VarDecl(Id(Egu), NumberType, None, None)], Return(StringLit(Eew))), VarDecl(Id(Qk), StringType, None, NumLit(57.6))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115191))

	def test_21530115192(self):
		input = '''
string t8sW[83.84,75.88]
number kvqQ[25.12] <- 6.8
func kawF (bool kC[92.47,33.58,2.12], bool A8S, number k1Tf)	return "yaOdf"
'''
		expect = '''Program([VarDecl(Id(t8sW), ArrayType([83.84, 75.88], StringType), None, None), VarDecl(Id(kvqQ), ArrayType([25.12], NumberType), None, NumLit(6.8)), FuncDecl(Id(kawF), [VarDecl(Id(kC), ArrayType([92.47, 33.58, 2.12], BoolType), None, None), VarDecl(Id(A8S), BoolType, None, None), VarDecl(Id(k1Tf), NumberType, None, None)], Return(StringLit(yaOdf)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115192))

	def test_21530115193(self):
		input = '''
func XT (number gRp)	begin
		for loKo until true by 19.92
			string ACtc
		if ("zq")
		return y0
		elif (DX) string aT[45.45,60.76] <- "oDC"
		else if (RU)
		for kA until 65.49 by "Cn"
			break
		elif (true) if ("fH") if ("Nxi")
		begin
		end
		elif (false)
		if ("swA")
		xeAr[86.83] <- qZo
		elif ("H")
		for K5 until h3Ih by 33.18
			return 76.33
		elif ("X") if (41.32)
		oL_h(true)
		elif (52.91) if ("EIkT")
		FjP <- "U"
		else begin
		end
		elif (W37x) if (u90) string nly
		else Cm[zRcT, true] <- YC4
		else rwpK <- QpR0
		elif (47.35)
		b5r <- KGB
		elif (false) continue
		elif ("cSD") continue
		elif ("cyQwg")
		if ("cOkYK")
		continue
		elif (32.89)
		bvT(71.34)
		elif (2.38) BTTz["W"] <- 50.33
		else begin
			continue
		end
	end
'''
		expect = '''Program([FuncDecl(Id(XT), [VarDecl(Id(gRp), NumberType, None, None)], Block([For(Id(loKo), BooleanLit(True), NumLit(19.92), VarDecl(Id(ACtc), StringType, None, None)), If(StringLit(zq), Return(Id(y0))), [(Id(DX), VarDecl(Id(aT), ArrayType([45.45, 60.76], StringType), None, StringLit(oDC)))], If(Id(RU), For(Id(kA), NumLit(65.49), StringLit(Cn), Break)), [(BooleanLit(True), If(StringLit(fH), If(StringLit(Nxi), Block([])), [(BooleanLit(False), If(StringLit(swA), AssignStmt(ArrayCell(Id(xeAr), [NumLit(86.83)]), Id(qZo))), [(StringLit(H), For(Id(K5), Id(h3Ih), NumLit(33.18), Return(NumLit(76.33)))), (StringLit(X), If(NumLit(41.32), CallStmt(Id(oL_h), [BooleanLit(True)])), [(NumLit(52.91), If(StringLit(EIkT), AssignStmt(Id(FjP), StringLit(U))), [], Block([])), (Id(W37x), If(Id(u90), VarDecl(Id(nly), StringType, None, None)), [], AssignStmt(ArrayCell(Id(Cm), [Id(zRcT), BooleanLit(True)]), Id(YC4)))], AssignStmt(Id(rwpK), Id(QpR0))), (NumLit(47.35), AssignStmt(Id(b5r), Id(KGB))), (BooleanLit(False), Continue), (StringLit(cSD), Continue), (StringLit(cyQwg), If(StringLit(cOkYK), Continue), [], None)], None), (NumLit(32.89), CallStmt(Id(bvT), [NumLit(71.34)]))], None), [], None), (NumLit(2.38), AssignStmt(ArrayCell(Id(BTTz), [StringLit(W)]), NumLit(50.33)))], Block([Continue])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115193))

	def test_21530115194(self):
		input = '''
string d8 <- 95.08
func Jn (string h_, bool GOP[76.96,22.65])
	begin
	end

'''
		expect = '''Program([VarDecl(Id(d8), StringType, None, NumLit(95.08)), FuncDecl(Id(Jn), [VarDecl(Id(h_), StringType, None, None), VarDecl(Id(GOP), ArrayType([76.96, 22.65], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115194))

	def test_21530115195(self):
		input = '''
dynamic Fp0 <- true
func k09f (bool YYVU)	return true
string VU
func bWsB (bool gT[17.31,83.6], bool GNw, string Qk[63.74,98.01,65.96])	return nIBj

number es[29.0,63.51,90.06]
'''
		expect = '''Program([VarDecl(Id(Fp0), None, dynamic, BooleanLit(True)), FuncDecl(Id(k09f), [VarDecl(Id(YYVU), BoolType, None, None)], Return(BooleanLit(True))), VarDecl(Id(VU), StringType, None, None), FuncDecl(Id(bWsB), [VarDecl(Id(gT), ArrayType([17.31, 83.6], BoolType), None, None), VarDecl(Id(GNw), BoolType, None, None), VarDecl(Id(Qk), ArrayType([63.74, 98.01, 65.96], StringType), None, None)], Return(Id(nIBj))), VarDecl(Id(es), ArrayType([29.0, 63.51, 90.06], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115195))

	def test_21530115196(self):
		input = '''
func gnOn ()	return 80.62

func Dqg (string iOr[74.01,46.85,71.63], string z8I[90.12,44.36,66.74], string gm[74.25,45.79])
	return 78.66
var pF <- Xwm
string th[33.06] <- EWZ
'''
		expect = '''Program([FuncDecl(Id(gnOn), [], Return(NumLit(80.62))), FuncDecl(Id(Dqg), [VarDecl(Id(iOr), ArrayType([74.01, 46.85, 71.63], StringType), None, None), VarDecl(Id(z8I), ArrayType([90.12, 44.36, 66.74], StringType), None, None), VarDecl(Id(gm), ArrayType([74.25, 45.79], StringType), None, None)], Return(NumLit(78.66))), VarDecl(Id(pF), None, var, Id(Xwm)), VarDecl(Id(th), ArrayType([33.06], StringType), None, Id(EWZ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115196))

	def test_21530115197(self):
		input = '''
string xT
bool d5[3.68,75.23,91.23] <- Vxtv
func GB (string rFi[77.75,96.54,60.89], number NGG, string e1D)	return
func Wh (number ou7, bool d5xr[62.31,82.76,72.33], string d5o9[5.4])	begin
		string WJ8D[46.92] <- true
		ubu("bZ", false)
		continue
	end
'''
		expect = '''Program([VarDecl(Id(xT), StringType, None, None), VarDecl(Id(d5), ArrayType([3.68, 75.23, 91.23], BoolType), None, Id(Vxtv)), FuncDecl(Id(GB), [VarDecl(Id(rFi), ArrayType([77.75, 96.54, 60.89], StringType), None, None), VarDecl(Id(NGG), NumberType, None, None), VarDecl(Id(e1D), StringType, None, None)], Return()), FuncDecl(Id(Wh), [VarDecl(Id(ou7), NumberType, None, None), VarDecl(Id(d5xr), ArrayType([62.31, 82.76, 72.33], BoolType), None, None), VarDecl(Id(d5o9), ArrayType([5.4], StringType), None, None)], Block([VarDecl(Id(WJ8D), ArrayType([46.92], StringType), None, BooleanLit(True)), CallStmt(Id(ubu), [StringLit(bZ), BooleanLit(False)]), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115197))

	def test_21530115198(self):
		input = '''
func ngSr (string Zkxm[47.84,29.99,10.63])
	return "QrQw"
func C50 (number r6Sx[11.87,92.68])	begin
	end

bool SV[33.23]
number bE
string EnG
'''
		expect = '''Program([FuncDecl(Id(ngSr), [VarDecl(Id(Zkxm), ArrayType([47.84, 29.99, 10.63], StringType), None, None)], Return(StringLit(QrQw))), FuncDecl(Id(C50), [VarDecl(Id(r6Sx), ArrayType([11.87, 92.68], NumberType), None, None)], Block([])), VarDecl(Id(SV), ArrayType([33.23], BoolType), None, None), VarDecl(Id(bE), NumberType, None, None), VarDecl(Id(EnG), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115198))

	def test_21530115199(self):
		input = '''
func JH ()	return "d"
func IOb (string xlO, number qj)	return "UDK"

bool kkT <- wB
'''
		expect = '''Program([FuncDecl(Id(JH), [], Return(StringLit(d))), FuncDecl(Id(IOb), [VarDecl(Id(xlO), StringType, None, None), VarDecl(Id(qj), NumberType, None, None)], Return(StringLit(UDK))), VarDecl(Id(kkT), BoolType, None, Id(wB))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115199))

	def test_21530115200(self):
		input = '''
dynamic C0Zw <- 42.52
string T5pv[75.23,95.65,70.66]
func WW ()
	return false

func ncF9 ()
	return
func nqb ()
	return

'''
		expect = '''Program([VarDecl(Id(C0Zw), None, dynamic, NumLit(42.52)), VarDecl(Id(T5pv), ArrayType([75.23, 95.65, 70.66], StringType), None, None), FuncDecl(Id(WW), [], Return(BooleanLit(False))), FuncDecl(Id(ncF9), [], Return()), FuncDecl(Id(nqb), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115200))

	def test_21530115201(self):
		input = '''
var pM2 <- 16.84
func xf (bool i9[22.42,25.95,63.68])	return 30.38

'''
		expect = '''Program([VarDecl(Id(pM2), None, var, NumLit(16.84)), FuncDecl(Id(xf), [VarDecl(Id(i9), ArrayType([22.42, 25.95, 63.68], BoolType), None, None)], Return(NumLit(30.38)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115201))

	def test_21530115202(self):
		input = '''
func m9S ()	begin
		for AP until QGu by true
			break
		KiD(UHQ, "lScD")
		break
	end

dynamic K9
func eSID ()
	return
func pGG (bool gf[9.61,97.72], number M_aM, string im3)
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(m9S), [], Block([For(Id(AP), Id(QGu), BooleanLit(True), Break), CallStmt(Id(KiD), [Id(UHQ), StringLit(lScD)]), Break])), VarDecl(Id(K9), None, dynamic, None), FuncDecl(Id(eSID), [], Return()), FuncDecl(Id(pGG), [VarDecl(Id(gf), ArrayType([9.61, 97.72], BoolType), None, None), VarDecl(Id(M_aM), NumberType, None, None), VarDecl(Id(im3), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115202))

	def test_21530115203(self):
		input = '''
func jPvF (string BgU)	begin
	end
func tc (bool LlY, string F2PE)	return

func mzul (bool lM)
	return
number nD[82.35] <- "g"
'''
		expect = '''Program([FuncDecl(Id(jPvF), [VarDecl(Id(BgU), StringType, None, None)], Block([])), FuncDecl(Id(tc), [VarDecl(Id(LlY), BoolType, None, None), VarDecl(Id(F2PE), StringType, None, None)], Return()), FuncDecl(Id(mzul), [VarDecl(Id(lM), BoolType, None, None)], Return()), VarDecl(Id(nD), ArrayType([82.35], NumberType), None, StringLit(g))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115203))

	def test_21530115204(self):
		input = '''
bool lVa <- mDS
bool jw[21.28,51.55] <- 25.08
string EYn[28.7] <- jA5u
func kc ()	return 27.13
'''
		expect = '''Program([VarDecl(Id(lVa), BoolType, None, Id(mDS)), VarDecl(Id(jw), ArrayType([21.28, 51.55], BoolType), None, NumLit(25.08)), VarDecl(Id(EYn), ArrayType([28.7], StringType), None, Id(jA5u)), FuncDecl(Id(kc), [], Return(NumLit(27.13)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115204))

	def test_21530115205(self):
		input = '''
dynamic iMj6
bool wjC
number bri <- true
func h7 ()
	begin
	end

'''
		expect = '''Program([VarDecl(Id(iMj6), None, dynamic, None), VarDecl(Id(wjC), BoolType, None, None), VarDecl(Id(bri), NumberType, None, BooleanLit(True)), FuncDecl(Id(h7), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115205))

	def test_21530115206(self):
		input = '''
number wI0M[4.69,93.89]
bool k5 <- il
bool oYQ5[68.82,68.36]
string Pzn
'''
		expect = '''Program([VarDecl(Id(wI0M), ArrayType([4.69, 93.89], NumberType), None, None), VarDecl(Id(k5), BoolType, None, Id(il)), VarDecl(Id(oYQ5), ArrayType([68.82, 68.36], BoolType), None, None), VarDecl(Id(Pzn), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115206))

	def test_21530115207(self):
		input = '''
bool k7 <- lw8
number Vbwe[10.83,83.09,8.14]
'''
		expect = '''Program([VarDecl(Id(k7), BoolType, None, Id(lw8)), VarDecl(Id(Vbwe), ArrayType([10.83, 83.09, 8.14], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115207))

	def test_21530115208(self):
		input = '''
func Cp62 (string sda)
	return
func lL (number fTV7, bool X3[79.65,94.14,45.55], string Nm)
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(Cp62), [VarDecl(Id(sda), StringType, None, None)], Return()), FuncDecl(Id(lL), [VarDecl(Id(fTV7), NumberType, None, None), VarDecl(Id(X3), ArrayType([79.65, 94.14, 45.55], BoolType), None, None), VarDecl(Id(Nm), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115208))

	def test_21530115209(self):
		input = '''
func AaI ()	begin
		break
	end
number vL
'''
		expect = '''Program([FuncDecl(Id(AaI), [], Block([Break])), VarDecl(Id(vL), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115209))

	def test_21530115210(self):
		input = '''
func MDK (bool ecL[10.63], bool a88[61.85,94.54], string dH32[41.39,2.13])
	begin
		for UWIX until "Gbta" by 83.25
			C5(jur, true, "rVOhQ")
		return Jy
	end

func Ggp3 (string VYtw)	return
func Hs8 (number GjZ, bool ACN, bool g1f[31.42,8.15,94.85])
	begin
		Qkp <- 54.69
		break
	end

dynamic Gx
'''
		expect = '''Program([FuncDecl(Id(MDK), [VarDecl(Id(ecL), ArrayType([10.63], BoolType), None, None), VarDecl(Id(a88), ArrayType([61.85, 94.54], BoolType), None, None), VarDecl(Id(dH32), ArrayType([41.39, 2.13], StringType), None, None)], Block([For(Id(UWIX), StringLit(Gbta), NumLit(83.25), CallStmt(Id(C5), [Id(jur), BooleanLit(True), StringLit(rVOhQ)])), Return(Id(Jy))])), FuncDecl(Id(Ggp3), [VarDecl(Id(VYtw), StringType, None, None)], Return()), FuncDecl(Id(Hs8), [VarDecl(Id(GjZ), NumberType, None, None), VarDecl(Id(ACN), BoolType, None, None), VarDecl(Id(g1f), ArrayType([31.42, 8.15, 94.85], BoolType), None, None)], Block([AssignStmt(Id(Qkp), NumLit(54.69)), Break])), VarDecl(Id(Gx), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115210))

	def test_21530115211(self):
		input = '''
string YX <- 76.3
func Mo (string Khd)
	return
func rY (number MjS)
	return 53.82
bool V4_B
'''
		expect = '''Program([VarDecl(Id(YX), StringType, None, NumLit(76.3)), FuncDecl(Id(Mo), [VarDecl(Id(Khd), StringType, None, None)], Return()), FuncDecl(Id(rY), [VarDecl(Id(MjS), NumberType, None, None)], Return(NumLit(53.82))), VarDecl(Id(V4_B), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115211))

	def test_21530115212(self):
		input = '''
number kgem[57.34,70.45,51.17]
number uEF <- 64.54
string akY[6.38,38.25,44.67]
'''
		expect = '''Program([VarDecl(Id(kgem), ArrayType([57.34, 70.45, 51.17], NumberType), None, None), VarDecl(Id(uEF), NumberType, None, NumLit(64.54)), VarDecl(Id(akY), ArrayType([6.38, 38.25, 44.67], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115212))

	def test_21530115213(self):
		input = '''
number Ryv
func Vl_ ()	return "CCKA"
'''
		expect = '''Program([VarDecl(Id(Ryv), NumberType, None, None), FuncDecl(Id(Vl_), [], Return(StringLit(CCKA)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115213))

	def test_21530115214(self):
		input = '''
func rV ()
	return
func rvoZ (bool j7)
	return
dynamic dk <- true
'''
		expect = '''Program([FuncDecl(Id(rV), [], Return()), FuncDecl(Id(rvoZ), [VarDecl(Id(j7), BoolType, None, None)], Return()), VarDecl(Id(dk), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115214))

	def test_21530115215(self):
		input = '''
dynamic ix <- true
'''
		expect = '''Program([VarDecl(Id(ix), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115215))

	def test_21530115216(self):
		input = '''
number DA
func wtt (string skd)	begin
		continue
		for NF until 27.24 by vA
			GK <- xBx
		for PZ until false by "ddK"
			COp[64.07] <- true
	end
string NQv
'''
		expect = '''Program([VarDecl(Id(DA), NumberType, None, None), FuncDecl(Id(wtt), [VarDecl(Id(skd), StringType, None, None)], Block([Continue, For(Id(NF), NumLit(27.24), Id(vA), AssignStmt(Id(GK), Id(xBx))), For(Id(PZ), BooleanLit(False), StringLit(ddK), AssignStmt(ArrayCell(Id(COp), [NumLit(64.07)]), BooleanLit(True)))])), VarDecl(Id(NQv), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115216))

	def test_21530115217(self):
		input = '''
func Ijev (number y8[46.22], string sDZ8[29.64], number d5M[61.93,71.22])	return

'''
		expect = '''Program([FuncDecl(Id(Ijev), [VarDecl(Id(y8), ArrayType([46.22], NumberType), None, None), VarDecl(Id(sDZ8), ArrayType([29.64], StringType), None, None), VarDecl(Id(d5M), ArrayType([61.93, 71.22], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115217))

	def test_21530115218(self):
		input = '''
number RQQ[57.98,82.63]
'''
		expect = '''Program([VarDecl(Id(RQQ), ArrayType([57.98, 82.63], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115218))

	def test_21530115219(self):
		input = '''
func O9A ()
	begin
		for QMUj until "AGFRo" by ZmLH
			return
		UTY(33.63)
	end

func zzJ (string Bs, bool Y_6d)
	begin
		continue
	end
func JIsG (number Aeg[31.28,81.83,66.08], number jB[71.27,52.61,74.63], string rq7R[35.84,46.37])
	return 3.25

string GF[39.38,26.06] <- 2.37
bool efU[66.31,83.4,1.2] <- 50.64
'''
		expect = '''Program([FuncDecl(Id(O9A), [], Block([For(Id(QMUj), StringLit(AGFRo), Id(ZmLH), Return()), CallStmt(Id(UTY), [NumLit(33.63)])])), FuncDecl(Id(zzJ), [VarDecl(Id(Bs), StringType, None, None), VarDecl(Id(Y_6d), BoolType, None, None)], Block([Continue])), FuncDecl(Id(JIsG), [VarDecl(Id(Aeg), ArrayType([31.28, 81.83, 66.08], NumberType), None, None), VarDecl(Id(jB), ArrayType([71.27, 52.61, 74.63], NumberType), None, None), VarDecl(Id(rq7R), ArrayType([35.84, 46.37], StringType), None, None)], Return(NumLit(3.25))), VarDecl(Id(GF), ArrayType([39.38, 26.06], StringType), None, NumLit(2.37)), VarDecl(Id(efU), ArrayType([66.31, 83.4, 1.2], BoolType), None, NumLit(50.64))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115219))

	def test_21530115220(self):
		input = '''
func ej9s ()	begin
		return RJQ1
		gsk[false] <- false
	end
func iGpf ()
	begin
		if ("dHouO")
		if ("X")
		dynamic CWB <- FZ
		elif (10.58) for ep until sWz by HcJ
			number EAY
		elif ("ZoXv")
		return
		else continue
		elif (AVqX)
		for k0Lm until false by true
			bool Mq[74.76,3.74]
	end
dynamic a0hj <- "aMrf"
number eEE <- oxA7
bool hu <- "PJF"
'''
		expect = '''Program([FuncDecl(Id(ej9s), [], Block([Return(Id(RJQ1)), AssignStmt(ArrayCell(Id(gsk), [BooleanLit(False)]), BooleanLit(False))])), FuncDecl(Id(iGpf), [], Block([If(StringLit(dHouO), If(StringLit(X), VarDecl(Id(CWB), None, dynamic, Id(FZ))), [(NumLit(10.58), For(Id(ep), Id(sWz), Id(HcJ), VarDecl(Id(EAY), NumberType, None, None))), (StringLit(ZoXv), Return())], Continue), [(Id(AVqX), For(Id(k0Lm), BooleanLit(False), BooleanLit(True), VarDecl(Id(Mq), ArrayType([74.76, 3.74], BoolType), None, None)))], None])), VarDecl(Id(a0hj), None, dynamic, StringLit(aMrf)), VarDecl(Id(eEE), NumberType, None, Id(oxA7)), VarDecl(Id(hu), BoolType, None, StringLit(PJF))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115220))

	def test_21530115221(self):
		input = '''
func NW (string Q6h2[82.78,60.53,2.86])	return

'''
		expect = '''Program([FuncDecl(Id(NW), [VarDecl(Id(Q6h2), ArrayType([82.78, 60.53, 2.86], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115221))

	def test_21530115222(self):
		input = '''
bool PiX[34.85,43.5]
dynamic fK
func PE (string rV, bool aB9, number Kd)	return

'''
		expect = '''Program([VarDecl(Id(PiX), ArrayType([34.85, 43.5], BoolType), None, None), VarDecl(Id(fK), None, dynamic, None), FuncDecl(Id(PE), [VarDecl(Id(rV), StringType, None, None), VarDecl(Id(aB9), BoolType, None, None), VarDecl(Id(Kd), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115222))

	def test_21530115223(self):
		input = '''
var wjV <- 5.14
var nL <- "hYy"
string KZlf[64.16,69.61]
'''
		expect = '''Program([VarDecl(Id(wjV), None, var, NumLit(5.14)), VarDecl(Id(nL), None, var, StringLit(hYy)), VarDecl(Id(KZlf), ArrayType([64.16, 69.61], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115223))

	def test_21530115224(self):
		input = '''
func um ()
	return
dynamic pxo3 <- 39.92
func Gsg0 ()
	begin
		for Dfa until true by dJCA
			dynamic wGgO <- "gsYp"
		break
		if (false)
		bool FAhh <- "g"
		else begin
		end
	end
func qDm3 (number Vyq, bool BRDP[35.47,6.47,33.44], number ctek)
	begin
		R0V(ZWn, 49.34, "tbOlN")
		continue
		for ioxQ until false by "aU"
			wL7[85.28, 17.44] <- WL
	end

func v7G ()	return b8

'''
		expect = '''Program([FuncDecl(Id(um), [], Return()), VarDecl(Id(pxo3), None, dynamic, NumLit(39.92)), FuncDecl(Id(Gsg0), [], Block([For(Id(Dfa), BooleanLit(True), Id(dJCA), VarDecl(Id(wGgO), None, dynamic, StringLit(gsYp))), Break, If(BooleanLit(False), VarDecl(Id(FAhh), BoolType, None, StringLit(g))), [], Block([])])), FuncDecl(Id(qDm3), [VarDecl(Id(Vyq), NumberType, None, None), VarDecl(Id(BRDP), ArrayType([35.47, 6.47, 33.44], BoolType), None, None), VarDecl(Id(ctek), NumberType, None, None)], Block([CallStmt(Id(R0V), [Id(ZWn), NumLit(49.34), StringLit(tbOlN)]), Continue, For(Id(ioxQ), BooleanLit(False), StringLit(aU), AssignStmt(ArrayCell(Id(wL7), [NumLit(85.28), NumLit(17.44)]), Id(WL)))])), FuncDecl(Id(v7G), [], Return(Id(b8)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115224))

	def test_21530115225(self):
		input = '''
func unm (number xEH, bool gp)
	begin
	end

string wF
func yU78 (string GbaC, bool hvL)
	return true

bool cKO1
func C3c (bool aS6)
	return pfm1
'''
		expect = '''Program([FuncDecl(Id(unm), [VarDecl(Id(xEH), NumberType, None, None), VarDecl(Id(gp), BoolType, None, None)], Block([])), VarDecl(Id(wF), StringType, None, None), FuncDecl(Id(yU78), [VarDecl(Id(GbaC), StringType, None, None), VarDecl(Id(hvL), BoolType, None, None)], Return(BooleanLit(True))), VarDecl(Id(cKO1), BoolType, None, None), FuncDecl(Id(C3c), [VarDecl(Id(aS6), BoolType, None, None)], Return(Id(pfm1)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115225))

	def test_21530115226(self):
		input = '''
func ea6M ()
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(ea6M), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115226))

	def test_21530115227(self):
		input = '''
var O9 <- 42.35
func HPv (bool Z8H)	return
'''
		expect = '''Program([VarDecl(Id(O9), None, var, NumLit(42.35)), FuncDecl(Id(HPv), [VarDecl(Id(Z8H), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115227))

	def test_21530115228(self):
		input = '''
func NMOy ()
	return true
func qSD (string DG, string iIU)	return 33.94
number uj[90.43,83.09,36.03]
func V6ej (number Z9qK, string kA4[54.59,94.06])	return "hiR"

func VReZ (bool S_E[25.79,39.43,6.33])	return "FgVf"
'''
		expect = '''Program([FuncDecl(Id(NMOy), [], Return(BooleanLit(True))), FuncDecl(Id(qSD), [VarDecl(Id(DG), StringType, None, None), VarDecl(Id(iIU), StringType, None, None)], Return(NumLit(33.94))), VarDecl(Id(uj), ArrayType([90.43, 83.09, 36.03], NumberType), None, None), FuncDecl(Id(V6ej), [VarDecl(Id(Z9qK), NumberType, None, None), VarDecl(Id(kA4), ArrayType([54.59, 94.06], StringType), None, None)], Return(StringLit(hiR))), FuncDecl(Id(VReZ), [VarDecl(Id(S_E), ArrayType([25.79, 39.43, 6.33], BoolType), None, None)], Return(StringLit(FgVf)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115228))

	def test_21530115229(self):
		input = '''
number B3lO[80.28,48.98] <- "Qw"
string jEO
func Xi3 (number YW_a)
	return false

func owJ (bool DwF, bool YJjw)
	begin
		break
		break
		return
	end

'''
		expect = '''Program([VarDecl(Id(B3lO), ArrayType([80.28, 48.98], NumberType), None, StringLit(Qw)), VarDecl(Id(jEO), StringType, None, None), FuncDecl(Id(Xi3), [VarDecl(Id(YW_a), NumberType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(owJ), [VarDecl(Id(DwF), BoolType, None, None), VarDecl(Id(YJjw), BoolType, None, None)], Block([Break, Break, Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115229))

	def test_21530115230(self):
		input = '''
func vJ9 (number D3[56.1,9.34,55.36], number PS)
	return

string Vxb
func LQ4 (bool BvX)	return 99.47
dynamic izh <- 78.71
func qVM ()
	begin
		if (1.42)
		return 62.51
		else sA("RBP")
		break
		continue
	end
'''
		expect = '''Program([FuncDecl(Id(vJ9), [VarDecl(Id(D3), ArrayType([56.1, 9.34, 55.36], NumberType), None, None), VarDecl(Id(PS), NumberType, None, None)], Return()), VarDecl(Id(Vxb), StringType, None, None), FuncDecl(Id(LQ4), [VarDecl(Id(BvX), BoolType, None, None)], Return(NumLit(99.47))), VarDecl(Id(izh), None, dynamic, NumLit(78.71)), FuncDecl(Id(qVM), [], Block([If(NumLit(1.42), Return(NumLit(62.51))), [], CallStmt(Id(sA), [StringLit(RBP)]), Break, Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115230))

	def test_21530115231(self):
		input = '''
dynamic QS
bool AuB[7.09] <- tw
string kb[14.43,2.87]
'''
		expect = '''Program([VarDecl(Id(QS), None, dynamic, None), VarDecl(Id(AuB), ArrayType([7.09], BoolType), None, Id(tw)), VarDecl(Id(kb), ArrayType([14.43, 2.87], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115231))

	def test_21530115232(self):
		input = '''
dynamic IIL <- false
func iy (number p15l[77.27,51.63,41.37], bool gsn[23.92,83.5])
	begin
	end

func KE (bool Qk9, string Gr[5.01,67.9])
	return true

string Hx6q[86.76,99.54,89.86] <- AA
number yr <- YO6n
'''
		expect = '''Program([VarDecl(Id(IIL), None, dynamic, BooleanLit(False)), FuncDecl(Id(iy), [VarDecl(Id(p15l), ArrayType([77.27, 51.63, 41.37], NumberType), None, None), VarDecl(Id(gsn), ArrayType([23.92, 83.5], BoolType), None, None)], Block([])), FuncDecl(Id(KE), [VarDecl(Id(Qk9), BoolType, None, None), VarDecl(Id(Gr), ArrayType([5.01, 67.9], StringType), None, None)], Return(BooleanLit(True))), VarDecl(Id(Hx6q), ArrayType([86.76, 99.54, 89.86], StringType), None, Id(AA)), VarDecl(Id(yr), NumberType, None, Id(YO6n))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115232))

	def test_21530115233(self):
		input = '''
number ru
bool yRV
func TBd (number np6[23.23])	return eD

number X2c <- RFSj
func Qhd ()	return false

'''
		expect = '''Program([VarDecl(Id(ru), NumberType, None, None), VarDecl(Id(yRV), BoolType, None, None), FuncDecl(Id(TBd), [VarDecl(Id(np6), ArrayType([23.23], NumberType), None, None)], Return(Id(eD))), VarDecl(Id(X2c), NumberType, None, Id(RFSj)), FuncDecl(Id(Qhd), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115233))

	def test_21530115234(self):
		input = '''
func sp (string zo4g, string W_[6.6,70.2,81.99], number Uxi)
	return

'''
		expect = '''Program([FuncDecl(Id(sp), [VarDecl(Id(zo4g), StringType, None, None), VarDecl(Id(W_), ArrayType([6.6, 70.2, 81.99], StringType), None, None), VarDecl(Id(Uxi), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115234))

	def test_21530115235(self):
		input = '''
var mtV <- "SPS"
'''
		expect = '''Program([VarDecl(Id(mtV), None, var, StringLit(SPS))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115235))

	def test_21530115236(self):
		input = '''
func NjJ (string gvI, number Uqa[10.31,14.23], string I4[67.55,7.0])
	return 3.3

'''
		expect = '''Program([FuncDecl(Id(NjJ), [VarDecl(Id(gvI), StringType, None, None), VarDecl(Id(Uqa), ArrayType([10.31, 14.23], NumberType), None, None), VarDecl(Id(I4), ArrayType([67.55, 7.0], StringType), None, None)], Return(NumLit(3.3)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115236))

	def test_21530115237(self):
		input = '''
number jiWX <- false
func DT (number nkd, string vC[50.9])
	begin
	end
string egt <- "rqfd"
string Dzgr <- true
'''
		expect = '''Program([VarDecl(Id(jiWX), NumberType, None, BooleanLit(False)), FuncDecl(Id(DT), [VarDecl(Id(nkd), NumberType, None, None), VarDecl(Id(vC), ArrayType([50.9], StringType), None, None)], Block([])), VarDecl(Id(egt), StringType, None, StringLit(rqfd)), VarDecl(Id(Dzgr), StringType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115237))

	def test_21530115238(self):
		input = '''
string Ory5[47.99] <- NIu
func wjw (bool muB6)
	return 98.55

func XU8f (bool lh, bool FNh[49.2], number NLp[34.31])	return Ch
'''
		expect = '''Program([VarDecl(Id(Ory5), ArrayType([47.99], StringType), None, Id(NIu)), FuncDecl(Id(wjw), [VarDecl(Id(muB6), BoolType, None, None)], Return(NumLit(98.55))), FuncDecl(Id(XU8f), [VarDecl(Id(lh), BoolType, None, None), VarDecl(Id(FNh), ArrayType([49.2], BoolType), None, None), VarDecl(Id(NLp), ArrayType([34.31], NumberType), None, None)], Return(Id(Ch)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115238))

	def test_21530115239(self):
		input = '''
func Xy ()	return
func oS7U (string hi, string N0Gj[97.07], string Nq)	begin
		break
		return AF8a
		pQN()
	end
'''
		expect = '''Program([FuncDecl(Id(Xy), [], Return()), FuncDecl(Id(oS7U), [VarDecl(Id(hi), StringType, None, None), VarDecl(Id(N0Gj), ArrayType([97.07], StringType), None, None), VarDecl(Id(Nq), StringType, None, None)], Block([Break, Return(Id(AF8a)), CallStmt(Id(pQN), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115239))

	def test_21530115240(self):
		input = '''
number a6[91.23] <- "pnG"
func IBMF (number IXvO, number RsY1, string pEl[32.07])
	return
'''
		expect = '''Program([VarDecl(Id(a6), ArrayType([91.23], NumberType), None, StringLit(pnG)), FuncDecl(Id(IBMF), [VarDecl(Id(IXvO), NumberType, None, None), VarDecl(Id(RsY1), NumberType, None, None), VarDecl(Id(pEl), ArrayType([32.07], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115240))

	def test_21530115241(self):
		input = '''
number dn3q
func hUe ()	begin
	end

func ae ()	begin
	end
dynamic f9K
func y1 (number m_H, bool t4EC[23.2,74.74], bool Xc)	return

'''
		expect = '''Program([VarDecl(Id(dn3q), NumberType, None, None), FuncDecl(Id(hUe), [], Block([])), FuncDecl(Id(ae), [], Block([])), VarDecl(Id(f9K), None, dynamic, None), FuncDecl(Id(y1), [VarDecl(Id(m_H), NumberType, None, None), VarDecl(Id(t4EC), ArrayType([23.2, 74.74], BoolType), None, None), VarDecl(Id(Xc), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115241))

	def test_21530115242(self):
		input = '''
func rQ (number fM[98.23,55.61])	return

func NJG0 ()
	return pn

func M8 ()	begin
		begin
		end
	end
'''
		expect = '''Program([FuncDecl(Id(rQ), [VarDecl(Id(fM), ArrayType([98.23, 55.61], NumberType), None, None)], Return()), FuncDecl(Id(NJG0), [], Return(Id(pn))), FuncDecl(Id(M8), [], Block([Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115242))

	def test_21530115243(self):
		input = '''
func jWe_ (string JGu)
	return true
func yrd ()
	begin
	end
number W45K <- true
dynamic I1o7 <- 19.46
func LWcv ()
	return "OeCtn"

'''
		expect = '''Program([FuncDecl(Id(jWe_), [VarDecl(Id(JGu), StringType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(yrd), [], Block([])), VarDecl(Id(W45K), NumberType, None, BooleanLit(True)), VarDecl(Id(I1o7), None, dynamic, NumLit(19.46)), FuncDecl(Id(LWcv), [], Return(StringLit(OeCtn)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115243))

	def test_21530115244(self):
		input = '''
func jQDR (bool XW[7.38,51.2,0.34])	return 67.95

func oVt (string c9zr[35.87,39.79,74.61], string Za[81.07,48.33,52.47], number h2[62.03,44.25])
	return

'''
		expect = '''Program([FuncDecl(Id(jQDR), [VarDecl(Id(XW), ArrayType([7.38, 51.2, 0.34], BoolType), None, None)], Return(NumLit(67.95))), FuncDecl(Id(oVt), [VarDecl(Id(c9zr), ArrayType([35.87, 39.79, 74.61], StringType), None, None), VarDecl(Id(Za), ArrayType([81.07, 48.33, 52.47], StringType), None, None), VarDecl(Id(h2), ArrayType([62.03, 44.25], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115244))

	def test_21530115245(self):
		input = '''
func gxD (bool Gq7K[63.08])	begin
		if ("MEU")
		continue
		elif ("LJnG")
		BLQ <- "f"
		elif ("HIE")
		break
		return
		return 74.87
	end

func n9R (number Pc2k, bool Crx[91.42,21.81,5.09], bool qY5v)
	return iI
bool Wo_[4.79,36.99,95.42]
number aCt <- JDdj
bool f9qO[36.7] <- 2.66
'''
		expect = '''Program([FuncDecl(Id(gxD), [VarDecl(Id(Gq7K), ArrayType([63.08], BoolType), None, None)], Block([If(StringLit(MEU), Continue), [(StringLit(LJnG), AssignStmt(Id(BLQ), StringLit(f))), (StringLit(HIE), Break)], None, Return(), Return(NumLit(74.87))])), FuncDecl(Id(n9R), [VarDecl(Id(Pc2k), NumberType, None, None), VarDecl(Id(Crx), ArrayType([91.42, 21.81, 5.09], BoolType), None, None), VarDecl(Id(qY5v), BoolType, None, None)], Return(Id(iI))), VarDecl(Id(Wo_), ArrayType([4.79, 36.99, 95.42], BoolType), None, None), VarDecl(Id(aCt), NumberType, None, Id(JDdj)), VarDecl(Id(f9qO), ArrayType([36.7], BoolType), None, NumLit(2.66))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115245))

	def test_21530115246(self):
		input = '''
string LnG
func Uy8 (number DR, string mNi[40.57], string p2)	begin
	end

dynamic W9b
dynamic vP <- dQo
'''
		expect = '''Program([VarDecl(Id(LnG), StringType, None, None), FuncDecl(Id(Uy8), [VarDecl(Id(DR), NumberType, None, None), VarDecl(Id(mNi), ArrayType([40.57], StringType), None, None), VarDecl(Id(p2), StringType, None, None)], Block([])), VarDecl(Id(W9b), None, dynamic, None), VarDecl(Id(vP), None, dynamic, Id(dQo))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115246))

	def test_21530115247(self):
		input = '''
func Jvd (bool cp[37.13,56.02,28.46], bool m5H, string Sc[24.12,92.87])	return
var Xr0 <- 71.66
number ja <- 8.77
func DZ8v (string s6)	begin
	end

string vr[86.11] <- uO2
'''
		expect = '''Program([FuncDecl(Id(Jvd), [VarDecl(Id(cp), ArrayType([37.13, 56.02, 28.46], BoolType), None, None), VarDecl(Id(m5H), BoolType, None, None), VarDecl(Id(Sc), ArrayType([24.12, 92.87], StringType), None, None)], Return()), VarDecl(Id(Xr0), None, var, NumLit(71.66)), VarDecl(Id(ja), NumberType, None, NumLit(8.77)), FuncDecl(Id(DZ8v), [VarDecl(Id(s6), StringType, None, None)], Block([])), VarDecl(Id(vr), ArrayType([86.11], StringType), None, Id(uO2))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115247))

	def test_21530115248(self):
		input = '''
string K2f
var Mw_ <- 77.35
dynamic fL1Y <- JUO
func Iyz (bool GX[92.95], string sH1C[46.78,80.0,14.53], number GW[7.31])
	begin
	end

func bv (number b4, string N_Vc[99.29], number YGJ[1.54,3.56,77.57])
	begin
		for SJ until false by HT
			break
	end
'''
		expect = '''Program([VarDecl(Id(K2f), StringType, None, None), VarDecl(Id(Mw_), None, var, NumLit(77.35)), VarDecl(Id(fL1Y), None, dynamic, Id(JUO)), FuncDecl(Id(Iyz), [VarDecl(Id(GX), ArrayType([92.95], BoolType), None, None), VarDecl(Id(sH1C), ArrayType([46.78, 80.0, 14.53], StringType), None, None), VarDecl(Id(GW), ArrayType([7.31], NumberType), None, None)], Block([])), FuncDecl(Id(bv), [VarDecl(Id(b4), NumberType, None, None), VarDecl(Id(N_Vc), ArrayType([99.29], StringType), None, None), VarDecl(Id(YGJ), ArrayType([1.54, 3.56, 77.57], NumberType), None, None)], Block([For(Id(SJ), BooleanLit(False), Id(HT), Break)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115248))

	def test_21530115249(self):
		input = '''
func Mm ()	begin
		oVD[62.51] <- tLq
	end

'''
		expect = '''Program([FuncDecl(Id(Mm), [], Block([AssignStmt(ArrayCell(Id(oVD), [NumLit(62.51)]), Id(tLq))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115249))

	def test_21530115250(self):
		input = '''
string uz[49.74,65.62,20.65]
func qOTd (bool H3, bool w7eV[52.96,52.73], string j90G)
	return lj

'''
		expect = '''Program([VarDecl(Id(uz), ArrayType([49.74, 65.62, 20.65], StringType), None, None), FuncDecl(Id(qOTd), [VarDecl(Id(H3), BoolType, None, None), VarDecl(Id(w7eV), ArrayType([52.96, 52.73], BoolType), None, None), VarDecl(Id(j90G), StringType, None, None)], Return(Id(lj)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115250))

	def test_21530115251(self):
		input = '''
string G_gx
string LJ[40.48] <- oJGS
'''
		expect = '''Program([VarDecl(Id(G_gx), StringType, None, None), VarDecl(Id(LJ), ArrayType([40.48], StringType), None, Id(oJGS))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115251))

	def test_21530115252(self):
		input = '''
number k3hd[25.8,23.01] <- "eKW"
func xcE_ (bool WR, bool si[87.73], string Y_[62.41,78.87,54.99])	return
'''
		expect = '''Program([VarDecl(Id(k3hd), ArrayType([25.8, 23.01], NumberType), None, StringLit(eKW)), FuncDecl(Id(xcE_), [VarDecl(Id(WR), BoolType, None, None), VarDecl(Id(si), ArrayType([87.73], BoolType), None, None), VarDecl(Id(Y_), ArrayType([62.41, 78.87, 54.99], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115252))

	def test_21530115253(self):
		input = '''
func d_S (number L6D[5.83,73.51,65.24], number n6[85.77])
	return ZTp

'''
		expect = '''Program([FuncDecl(Id(d_S), [VarDecl(Id(L6D), ArrayType([5.83, 73.51, 65.24], NumberType), None, None), VarDecl(Id(n6), ArrayType([85.77], NumberType), None, None)], Return(Id(ZTp)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115253))

	def test_21530115254(self):
		input = '''
bool Y7
func vci ()
	begin
		break
		a0 <- true
	end
number H1d6 <- true
func Wa (bool dnD[33.26,33.14,40.63])	return "wZHV"
'''
		expect = '''Program([VarDecl(Id(Y7), BoolType, None, None), FuncDecl(Id(vci), [], Block([Break, AssignStmt(Id(a0), BooleanLit(True))])), VarDecl(Id(H1d6), NumberType, None, BooleanLit(True)), FuncDecl(Id(Wa), [VarDecl(Id(dnD), ArrayType([33.26, 33.14, 40.63], BoolType), None, None)], Return(StringLit(wZHV)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115254))

	def test_21530115255(self):
		input = '''
func Xm (string cd[97.26,95.11,65.78], string vK, string HGwE)
	begin
		dynamic L5 <- flDB
		continue
		begin
		end
	end
func Rq_ (number VDp)	return 34.8
func T_ (bool kL[18.67,68.79,58.49], number z7[78.66,2.84,73.12], bool oh3w)	return 44.9
string WB[54.51,77.97] <- true
'''
		expect = '''Program([FuncDecl(Id(Xm), [VarDecl(Id(cd), ArrayType([97.26, 95.11, 65.78], StringType), None, None), VarDecl(Id(vK), StringType, None, None), VarDecl(Id(HGwE), StringType, None, None)], Block([VarDecl(Id(L5), None, dynamic, Id(flDB)), Continue, Block([])])), FuncDecl(Id(Rq_), [VarDecl(Id(VDp), NumberType, None, None)], Return(NumLit(34.8))), FuncDecl(Id(T_), [VarDecl(Id(kL), ArrayType([18.67, 68.79, 58.49], BoolType), None, None), VarDecl(Id(z7), ArrayType([78.66, 2.84, 73.12], NumberType), None, None), VarDecl(Id(oh3w), BoolType, None, None)], Return(NumLit(44.9))), VarDecl(Id(WB), ArrayType([54.51, 77.97], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115255))

	def test_21530115256(self):
		input = '''
number pxHl <- true
'''
		expect = '''Program([VarDecl(Id(pxHl), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115256))

	def test_21530115257(self):
		input = '''
func Ok ()
	begin
		return
		bool lX[61.01,71.78]
		string dQ[43.59,1.84]
	end
var YE <- 4.84
number xM1 <- false
bool xKPw
'''
		expect = '''Program([FuncDecl(Id(Ok), [], Block([Return(), VarDecl(Id(lX), ArrayType([61.01, 71.78], BoolType), None, None), VarDecl(Id(dQ), ArrayType([43.59, 1.84], StringType), None, None)])), VarDecl(Id(YE), None, var, NumLit(4.84)), VarDecl(Id(xM1), NumberType, None, BooleanLit(False)), VarDecl(Id(xKPw), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115257))

	def test_21530115258(self):
		input = '''
dynamic vZRn <- true
number qRK
'''
		expect = '''Program([VarDecl(Id(vZRn), None, dynamic, BooleanLit(True)), VarDecl(Id(qRK), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115258))

	def test_21530115259(self):
		input = '''
string coc[88.73] <- false
string a3l[3.61,67.07,48.94] <- "riGC"
'''
		expect = '''Program([VarDecl(Id(coc), ArrayType([88.73], StringType), None, BooleanLit(False)), VarDecl(Id(a3l), ArrayType([3.61, 67.07, 48.94], StringType), None, StringLit(riGC))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115259))

	def test_21530115260(self):
		input = '''
func Ck_ (bool CU[73.37])	return true

number hG[9.87,93.41] <- 58.3
func ng (string HXMd[88.09,57.08], number Zz)	return

'''
		expect = '''Program([FuncDecl(Id(Ck_), [VarDecl(Id(CU), ArrayType([73.37], BoolType), None, None)], Return(BooleanLit(True))), VarDecl(Id(hG), ArrayType([9.87, 93.41], NumberType), None, NumLit(58.3)), FuncDecl(Id(ng), [VarDecl(Id(HXMd), ArrayType([88.09, 57.08], StringType), None, None), VarDecl(Id(Zz), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115260))

	def test_21530115261(self):
		input = '''
number EWhd
var i8 <- 72.63
'''
		expect = '''Program([VarDecl(Id(EWhd), NumberType, None, None), VarDecl(Id(i8), None, var, NumLit(72.63))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115261))

	def test_21530115262(self):
		input = '''
func V_x (bool sG)
	begin
		return
		for e8 until "e" by true
			begin
				if ("ETiT")
				for azC until 10.91 by false
					break
				elif (qiM) for IVf until true by "MKw"
					begin
						uYic(tA)
						ZU[true, IY, cr] <- bSLL
						nSC <- ERL
					end
				elif (true)
				tMw[BO] <- true
				elif ("CPbG") if (PBWq) bool lc[35.65,4.07,85.5] <- 4.84
				else string Kpz
				begin
					return false
					if ("qaeO")
					EVEj["l"] <- Cwy
				end
			end
		if (41.38) number tLV[26.25]
		elif (false)
		CDuY(KhD, SN3R, false)
		else begin
			return "b"
			if (true)
			DH <- true
			elif (true) string ht[80.86,27.68,69.83]
			elif (true) yV[94.74, ue] <- "AFDdp"
			elif (nym) if (false)
			for bjz8 until "zH" by false
				break
			elif (Gx) begin
				tnk[false, "QeJH", 13.1] <- 69.4
				break
				for Dl until MAi2 by true
					begin
						return
						bool Dcd <- x7jY
						continue
					end
			end
			else return
			elif (i2Ym) break
			else string nN
		end
	end
func xsPR (string yK, number ZmI0[26.4], bool nem[62.08,43.2,59.84])
	return
'''
		expect = '''Program([FuncDecl(Id(V_x), [VarDecl(Id(sG), BoolType, None, None)], Block([Return(), For(Id(e8), StringLit(e), BooleanLit(True), Block([If(StringLit(ETiT), For(Id(azC), NumLit(10.91), BooleanLit(False), Break)), [(Id(qiM), For(Id(IVf), BooleanLit(True), StringLit(MKw), Block([CallStmt(Id(uYic), [Id(tA)]), AssignStmt(ArrayCell(Id(ZU), [BooleanLit(True), Id(IY), Id(cr)]), Id(bSLL)), AssignStmt(Id(nSC), Id(ERL))]))), (BooleanLit(True), AssignStmt(ArrayCell(Id(tMw), [Id(BO)]), BooleanLit(True))), (StringLit(CPbG), If(Id(PBWq), VarDecl(Id(lc), ArrayType([35.65, 4.07, 85.5], BoolType), None, NumLit(4.84))), [], VarDecl(Id(Kpz), StringType, None, None))], None, Block([Return(BooleanLit(False)), If(StringLit(qaeO), AssignStmt(ArrayCell(Id(EVEj), [StringLit(l)]), Id(Cwy))), [], None])])), If(NumLit(41.38), VarDecl(Id(tLV), ArrayType([26.25], NumberType), None, None)), [(BooleanLit(False), CallStmt(Id(CDuY), [Id(KhD), Id(SN3R), BooleanLit(False)]))], Block([Return(StringLit(b)), If(BooleanLit(True), AssignStmt(Id(DH), BooleanLit(True))), [(BooleanLit(True), VarDecl(Id(ht), ArrayType([80.86, 27.68, 69.83], StringType), None, None)), (BooleanLit(True), AssignStmt(ArrayCell(Id(yV), [NumLit(94.74), Id(ue)]), StringLit(AFDdp))), (Id(nym), If(BooleanLit(False), For(Id(bjz8), StringLit(zH), BooleanLit(False), Break)), [(Id(Gx), Block([AssignStmt(ArrayCell(Id(tnk), [BooleanLit(False), StringLit(QeJH), NumLit(13.1)]), NumLit(69.4)), Break, For(Id(Dl), Id(MAi2), BooleanLit(True), Block([Return(), VarDecl(Id(Dcd), BoolType, None, Id(x7jY)), Continue]))]))], Return()), (Id(i2Ym), Break)], VarDecl(Id(nN), StringType, None, None)])])), FuncDecl(Id(xsPR), [VarDecl(Id(yK), StringType, None, None), VarDecl(Id(ZmI0), ArrayType([26.4], NumberType), None, None), VarDecl(Id(nem), ArrayType([62.08, 43.2, 59.84], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115262))

	def test_21530115263(self):
		input = '''
number mKOf <- XPd
func wj (bool Ae)	return

'''
		expect = '''Program([VarDecl(Id(mKOf), NumberType, None, Id(XPd)), FuncDecl(Id(wj), [VarDecl(Id(Ae), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115263))

	def test_21530115264(self):
		input = '''
func FlXq (bool k3[56.98,60.5,11.43], string bYO[31.11,50.83])
	return

bool tPhN <- tEX
var VP <- EmN7
'''
		expect = '''Program([FuncDecl(Id(FlXq), [VarDecl(Id(k3), ArrayType([56.98, 60.5, 11.43], BoolType), None, None), VarDecl(Id(bYO), ArrayType([31.11, 50.83], StringType), None, None)], Return()), VarDecl(Id(tPhN), BoolType, None, Id(tEX)), VarDecl(Id(VP), None, var, Id(EmN7))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115264))

	def test_21530115265(self):
		input = '''
bool dxz
'''
		expect = '''Program([VarDecl(Id(dxz), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115265))

	def test_21530115266(self):
		input = '''
string D6P[97.78,88.74] <- Pf
'''
		expect = '''Program([VarDecl(Id(D6P), ArrayType([97.78, 88.74], StringType), None, Id(Pf))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115266))

	def test_21530115267(self):
		input = '''
func kpm (bool JDn, number Oq[25.41], number y0uv)
	return "SBpu"

number Jo4
'''
		expect = '''Program([FuncDecl(Id(kpm), [VarDecl(Id(JDn), BoolType, None, None), VarDecl(Id(Oq), ArrayType([25.41], NumberType), None, None), VarDecl(Id(y0uv), NumberType, None, None)], Return(StringLit(SBpu))), VarDecl(Id(Jo4), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115267))

	def test_21530115268(self):
		input = '''
bool YW[83.5] <- "wWA"
func It (bool iIg[72.7,56.81], bool lgDH[64.33,24.8,51.36])
	return 59.32
func mQQK (number xYPj, number VD[51.2,37.98])
	begin
		continue
		if (79.12)
		return "Sg"
		elif ("TVoO") if (true)
		continue
		elif (73.19)
		begin
			W7vn(RU)
			begin
				string ux
				continue
				return "gTXH"
			end
		end
		elif (52.46) TB["uRN", 45.35, true] <- Oi2e
		elif ("LCjk") continue
		else bl[w2Ur] <- iEC
		else for zi2s until "g" by WDox
			for yeg until "MZYCb" by xjnq
				begin
					if (q6p9) bool liXX[57.23,67.24,34.06]
					elif (un)
					begin
						lwq(83.74)
					end
					elif ("gReC") continue
					elif ("zw")
					return
					else Ncv1()
					continue
					continue
				end
	end
'''
		expect = '''Program([VarDecl(Id(YW), ArrayType([83.5], BoolType), None, StringLit(wWA)), FuncDecl(Id(It), [VarDecl(Id(iIg), ArrayType([72.7, 56.81], BoolType), None, None), VarDecl(Id(lgDH), ArrayType([64.33, 24.8, 51.36], BoolType), None, None)], Return(NumLit(59.32))), FuncDecl(Id(mQQK), [VarDecl(Id(xYPj), NumberType, None, None), VarDecl(Id(VD), ArrayType([51.2, 37.98], NumberType), None, None)], Block([Continue, If(NumLit(79.12), Return(StringLit(Sg))), [(StringLit(TVoO), If(BooleanLit(True), Continue), [(NumLit(73.19), Block([CallStmt(Id(W7vn), [Id(RU)]), Block([VarDecl(Id(ux), StringType, None, None), Continue, Return(StringLit(gTXH))])])), (NumLit(52.46), AssignStmt(ArrayCell(Id(TB), [StringLit(uRN), NumLit(45.35), BooleanLit(True)]), Id(Oi2e))), (StringLit(LCjk), Continue)], AssignStmt(ArrayCell(Id(bl), [Id(w2Ur)]), Id(iEC)))], For(Id(zi2s), StringLit(g), Id(WDox), For(Id(yeg), StringLit(MZYCb), Id(xjnq), Block([If(Id(q6p9), VarDecl(Id(liXX), ArrayType([57.23, 67.24, 34.06], BoolType), None, None)), [(Id(un), Block([CallStmt(Id(lwq), [NumLit(83.74)])])), (StringLit(gReC), Continue), (StringLit(zw), Return())], CallStmt(Id(Ncv1), []), Continue, Continue])))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115268))

	def test_21530115269(self):
		input = '''
func GiS (number Cgo, string CTfB[39.5,48.83,56.35], string Qk)
	return

func BdC ()	return
func kxnm (string u2N[97.17,78.29])	begin
		if (true)
		TJs(false, true, "tDT")
		begin
			begin
			end
		end
	end

func D79 (bool J3f7)	return "f"

'''
		expect = '''Program([FuncDecl(Id(GiS), [VarDecl(Id(Cgo), NumberType, None, None), VarDecl(Id(CTfB), ArrayType([39.5, 48.83, 56.35], StringType), None, None), VarDecl(Id(Qk), StringType, None, None)], Return()), FuncDecl(Id(BdC), [], Return()), FuncDecl(Id(kxnm), [VarDecl(Id(u2N), ArrayType([97.17, 78.29], StringType), None, None)], Block([If(BooleanLit(True), CallStmt(Id(TJs), [BooleanLit(False), BooleanLit(True), StringLit(tDT)])), [], None, Block([Block([])])])), FuncDecl(Id(D79), [VarDecl(Id(J3f7), BoolType, None, None)], Return(StringLit(f)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115269))

	def test_21530115270(self):
		input = '''
func rm (bool lzBZ[62.89,4.68,94.41], bool JrJ[76.18,25.08,19.48])	return
func Jku7 (string tu0[49.56], number Dc3[63.39,84.22,39.23], string rJX)	begin
	end
func uy (string ZC[59.4,36.04,71.35])	return

bool FdQg <- b_7E
number wzlO[99.45]
'''
		expect = '''Program([FuncDecl(Id(rm), [VarDecl(Id(lzBZ), ArrayType([62.89, 4.68, 94.41], BoolType), None, None), VarDecl(Id(JrJ), ArrayType([76.18, 25.08, 19.48], BoolType), None, None)], Return()), FuncDecl(Id(Jku7), [VarDecl(Id(tu0), ArrayType([49.56], StringType), None, None), VarDecl(Id(Dc3), ArrayType([63.39, 84.22, 39.23], NumberType), None, None), VarDecl(Id(rJX), StringType, None, None)], Block([])), FuncDecl(Id(uy), [VarDecl(Id(ZC), ArrayType([59.4, 36.04, 71.35], StringType), None, None)], Return()), VarDecl(Id(FdQg), BoolType, None, Id(b_7E)), VarDecl(Id(wzlO), ArrayType([99.45], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115270))

	def test_21530115271(self):
		input = '''
func Zlng (bool pv[31.97,32.8,85.63], number hLFI, string ht[41.78,77.04,96.68])
	begin
		continue
		WEoO <- false
	end
bool WNrz
func ygR ()
	return

func Y3I (string eWYm[86.34])	return "NpL"

'''
		expect = '''Program([FuncDecl(Id(Zlng), [VarDecl(Id(pv), ArrayType([31.97, 32.8, 85.63], BoolType), None, None), VarDecl(Id(hLFI), NumberType, None, None), VarDecl(Id(ht), ArrayType([41.78, 77.04, 96.68], StringType), None, None)], Block([Continue, AssignStmt(Id(WEoO), BooleanLit(False))])), VarDecl(Id(WNrz), BoolType, None, None), FuncDecl(Id(ygR), [], Return()), FuncDecl(Id(Y3I), [VarDecl(Id(eWYm), ArrayType([86.34], StringType), None, None)], Return(StringLit(NpL)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115271))

	def test_21530115272(self):
		input = '''
var rN4 <- ElDk
func kMr ()
	return
func EWQ (bool GXSg, number g7, number iiER)
	return
'''
		expect = '''Program([VarDecl(Id(rN4), None, var, Id(ElDk)), FuncDecl(Id(kMr), [], Return()), FuncDecl(Id(EWQ), [VarDecl(Id(GXSg), BoolType, None, None), VarDecl(Id(g7), NumberType, None, None), VarDecl(Id(iiER), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115272))

	def test_21530115273(self):
		input = '''
var qq <- Pgv
func z3 ()	begin
	end
'''
		expect = '''Program([VarDecl(Id(qq), None, var, Id(Pgv)), FuncDecl(Id(z3), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115273))

	def test_21530115274(self):
		input = '''
func ZY (bool AGP[29.17,78.2])
	return
func QkV ()
	return

bool gl[75.11,55.55] <- 78.28
'''
		expect = '''Program([FuncDecl(Id(ZY), [VarDecl(Id(AGP), ArrayType([29.17, 78.2], BoolType), None, None)], Return()), FuncDecl(Id(QkV), [], Return()), VarDecl(Id(gl), ArrayType([75.11, 55.55], BoolType), None, NumLit(78.28))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115274))

	def test_21530115275(self):
		input = '''
func tq ()	begin
		return
		mz_(40.53, iG, "sBU")
		return X2
	end
func nd ()	return "eOM"

number rXz1 <- 66.98
func CK (number uD, string iL)	begin
		VYL <- 66.87
	end

func cxrP (string ll, number TXj, string An)
	return UoRk

'''
		expect = '''Program([FuncDecl(Id(tq), [], Block([Return(), CallStmt(Id(mz_), [NumLit(40.53), Id(iG), StringLit(sBU)]), Return(Id(X2))])), FuncDecl(Id(nd), [], Return(StringLit(eOM))), VarDecl(Id(rXz1), NumberType, None, NumLit(66.98)), FuncDecl(Id(CK), [VarDecl(Id(uD), NumberType, None, None), VarDecl(Id(iL), StringType, None, None)], Block([AssignStmt(Id(VYL), NumLit(66.87))])), FuncDecl(Id(cxrP), [VarDecl(Id(ll), StringType, None, None), VarDecl(Id(TXj), NumberType, None, None), VarDecl(Id(An), StringType, None, None)], Return(Id(UoRk)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115275))

	def test_21530115276(self):
		input = '''
bool S18 <- true
bool yN[59.91,39.19]
func hho (number Yk, string Y0aL[58.71,34.82,4.35], bool irB[36.94,6.06])	begin
	end
number OXO
'''
		expect = '''Program([VarDecl(Id(S18), BoolType, None, BooleanLit(True)), VarDecl(Id(yN), ArrayType([59.91, 39.19], BoolType), None, None), FuncDecl(Id(hho), [VarDecl(Id(Yk), NumberType, None, None), VarDecl(Id(Y0aL), ArrayType([58.71, 34.82, 4.35], StringType), None, None), VarDecl(Id(irB), ArrayType([36.94, 6.06], BoolType), None, None)], Block([])), VarDecl(Id(OXO), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115276))

	def test_21530115277(self):
		input = '''
func zVjC (string fP)
	return
'''
		expect = '''Program([FuncDecl(Id(zVjC), [VarDecl(Id(fP), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115277))

	def test_21530115278(self):
		input = '''
var FZl <- KO
bool BO[50.82,3.84]
bool BHx
'''
		expect = '''Program([VarDecl(Id(FZl), None, var, Id(KO)), VarDecl(Id(BO), ArrayType([50.82, 3.84], BoolType), None, None), VarDecl(Id(BHx), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115278))

	def test_21530115279(self):
		input = '''
string EIT <- "oATa"
func D3N (string v61[45.18])
	return

func Tt92 (number Iy0I, bool tW4C[5.22,92.12], bool NJ[97.34,65.86])	return

func xST (number FdZq[21.77,79.21])	begin
	end

func lJY (number mlGV, number IujB)
	return true

'''
		expect = '''Program([VarDecl(Id(EIT), StringType, None, StringLit(oATa)), FuncDecl(Id(D3N), [VarDecl(Id(v61), ArrayType([45.18], StringType), None, None)], Return()), FuncDecl(Id(Tt92), [VarDecl(Id(Iy0I), NumberType, None, None), VarDecl(Id(tW4C), ArrayType([5.22, 92.12], BoolType), None, None), VarDecl(Id(NJ), ArrayType([97.34, 65.86], BoolType), None, None)], Return()), FuncDecl(Id(xST), [VarDecl(Id(FdZq), ArrayType([21.77, 79.21], NumberType), None, None)], Block([])), FuncDecl(Id(lJY), [VarDecl(Id(mlGV), NumberType, None, None), VarDecl(Id(IujB), NumberType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115279))

	def test_21530115280(self):
		input = '''
bool RY
func Yvf (string J3Nd[6.73,83.42], number Na3M[31.14,79.54])	return

bool t_Lb[3.71,36.64,38.56] <- "wtqb"
string Mi[81.44,9.37,75.02] <- 0.19
'''
		expect = '''Program([VarDecl(Id(RY), BoolType, None, None), FuncDecl(Id(Yvf), [VarDecl(Id(J3Nd), ArrayType([6.73, 83.42], StringType), None, None), VarDecl(Id(Na3M), ArrayType([31.14, 79.54], NumberType), None, None)], Return()), VarDecl(Id(t_Lb), ArrayType([3.71, 36.64, 38.56], BoolType), None, StringLit(wtqb)), VarDecl(Id(Mi), ArrayType([81.44, 9.37, 75.02], StringType), None, NumLit(0.19))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115280))

	def test_21530115281(self):
		input = '''
func M7c (bool b1gO[20.77,74.05], string Yp)
	return

func Yg (string gX[49.7], string oMj[67.32,69.69,57.29])	return

'''
		expect = '''Program([FuncDecl(Id(M7c), [VarDecl(Id(b1gO), ArrayType([20.77, 74.05], BoolType), None, None), VarDecl(Id(Yp), StringType, None, None)], Return()), FuncDecl(Id(Yg), [VarDecl(Id(gX), ArrayType([49.7], StringType), None, None), VarDecl(Id(oMj), ArrayType([67.32, 69.69, 57.29], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115281))

	def test_21530115282(self):
		input = '''
func tyF (number Tk, string PTe5)	return 59.13
func yF ()
	begin
		if ("bzt")
		bool MFW
		else continue
		S63(z7, 87.57, "BNlIR")
	end
func DAf2 (number nEgr)
	return
string IBA
'''
		expect = '''Program([FuncDecl(Id(tyF), [VarDecl(Id(Tk), NumberType, None, None), VarDecl(Id(PTe5), StringType, None, None)], Return(NumLit(59.13))), FuncDecl(Id(yF), [], Block([If(StringLit(bzt), VarDecl(Id(MFW), BoolType, None, None)), [], Continue, CallStmt(Id(S63), [Id(z7), NumLit(87.57), StringLit(BNlIR)])])), FuncDecl(Id(DAf2), [VarDecl(Id(nEgr), NumberType, None, None)], Return()), VarDecl(Id(IBA), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115282))

	def test_21530115283(self):
		input = '''
func qG (string CvJ[93.17,9.58,8.69], string ziA[73.38,94.62,79.98], bool M6[23.72])
	return "hgqd"

func PA ()	return

bool tzwy[41.43,4.85]
'''
		expect = '''Program([FuncDecl(Id(qG), [VarDecl(Id(CvJ), ArrayType([93.17, 9.58, 8.69], StringType), None, None), VarDecl(Id(ziA), ArrayType([73.38, 94.62, 79.98], StringType), None, None), VarDecl(Id(M6), ArrayType([23.72], BoolType), None, None)], Return(StringLit(hgqd))), FuncDecl(Id(PA), [], Return()), VarDecl(Id(tzwy), ArrayType([41.43, 4.85], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115283))

	def test_21530115284(self):
		input = '''
string kS <- 87.69
'''
		expect = '''Program([VarDecl(Id(kS), StringType, None, NumLit(87.69))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115284))

	def test_21530115285(self):
		input = '''
number IQI <- false
func zBx (bool GPL4[85.57,53.38])
	return

number GLKc[34.08,49.4] <- EO
bool no1 <- false
func JV (bool es4[77.12], number tPOr)	return 7.82

'''
		expect = '''Program([VarDecl(Id(IQI), NumberType, None, BooleanLit(False)), FuncDecl(Id(zBx), [VarDecl(Id(GPL4), ArrayType([85.57, 53.38], BoolType), None, None)], Return()), VarDecl(Id(GLKc), ArrayType([34.08, 49.4], NumberType), None, Id(EO)), VarDecl(Id(no1), BoolType, None, BooleanLit(False)), FuncDecl(Id(JV), [VarDecl(Id(es4), ArrayType([77.12], BoolType), None, None), VarDecl(Id(tPOr), NumberType, None, None)], Return(NumLit(7.82)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115285))

	def test_21530115286(self):
		input = '''
func rLZ (string l5U, bool tDPQ[1.14,13.3], bool t5[72.84,50.3])	return

var FA <- "lj"
func KWz ()	return
'''
		expect = '''Program([FuncDecl(Id(rLZ), [VarDecl(Id(l5U), StringType, None, None), VarDecl(Id(tDPQ), ArrayType([1.14, 13.3], BoolType), None, None), VarDecl(Id(t5), ArrayType([72.84, 50.3], BoolType), None, None)], Return()), VarDecl(Id(FA), None, var, StringLit(lj)), FuncDecl(Id(KWz), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115286))

	def test_21530115287(self):
		input = '''
func Elu (number v3, bool U5)	return NTKP
bool xo
'''
		expect = '''Program([FuncDecl(Id(Elu), [VarDecl(Id(v3), NumberType, None, None), VarDecl(Id(U5), BoolType, None, None)], Return(Id(NTKP))), VarDecl(Id(xo), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115287))

	def test_21530115288(self):
		input = '''
dynamic xONJ <- ltz
'''
		expect = '''Program([VarDecl(Id(xONJ), None, dynamic, Id(ltz))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115288))

	def test_21530115289(self):
		input = '''
dynamic r7Q <- mLRA
'''
		expect = '''Program([VarDecl(Id(r7Q), None, dynamic, Id(mLRA))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115289))

	def test_21530115290(self):
		input = '''
string wk <- "Mbx"
func qR (number gf7[49.58], string NrHZ)
	return "AYiY"
bool hhVQ <- "w"
func E3HQ (string it87)	return

var eDOZ <- 72.13
'''
		expect = '''Program([VarDecl(Id(wk), StringType, None, StringLit(Mbx)), FuncDecl(Id(qR), [VarDecl(Id(gf7), ArrayType([49.58], NumberType), None, None), VarDecl(Id(NrHZ), StringType, None, None)], Return(StringLit(AYiY))), VarDecl(Id(hhVQ), BoolType, None, StringLit(w)), FuncDecl(Id(E3HQ), [VarDecl(Id(it87), StringType, None, None)], Return()), VarDecl(Id(eDOZ), None, var, NumLit(72.13))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115290))

	def test_21530115291(self):
		input = '''
func kc (number P6E, string XgCZ[58.73])	return

func JL (bool HSC[48.62], bool opE)	begin
		return true
		bool EYg[70.95] <- "s"
		return Com
	end

func OSuN (string ntU[44.76,54.1,76.1], bool rNK)	return

func on (bool Mjw, bool m7s[75.87,89.62,81.05], bool RVjH[84.51,19.93])	return AKN
'''
		expect = '''Program([FuncDecl(Id(kc), [VarDecl(Id(P6E), NumberType, None, None), VarDecl(Id(XgCZ), ArrayType([58.73], StringType), None, None)], Return()), FuncDecl(Id(JL), [VarDecl(Id(HSC), ArrayType([48.62], BoolType), None, None), VarDecl(Id(opE), BoolType, None, None)], Block([Return(BooleanLit(True)), VarDecl(Id(EYg), ArrayType([70.95], BoolType), None, StringLit(s)), Return(Id(Com))])), FuncDecl(Id(OSuN), [VarDecl(Id(ntU), ArrayType([44.76, 54.1, 76.1], StringType), None, None), VarDecl(Id(rNK), BoolType, None, None)], Return()), FuncDecl(Id(on), [VarDecl(Id(Mjw), BoolType, None, None), VarDecl(Id(m7s), ArrayType([75.87, 89.62, 81.05], BoolType), None, None), VarDecl(Id(RVjH), ArrayType([84.51, 19.93], BoolType), None, None)], Return(Id(AKN)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115291))

	def test_21530115292(self):
		input = '''
func fAKJ (string a2[83.03,37.5], string to, number IOj[81.19,27.01])
	return
'''
		expect = '''Program([FuncDecl(Id(fAKJ), [VarDecl(Id(a2), ArrayType([83.03, 37.5], StringType), None, None), VarDecl(Id(to), StringType, None, None), VarDecl(Id(IOj), ArrayType([81.19, 27.01], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115292))

	def test_21530115293(self):
		input = '''
bool K7[26.64,84.53,74.07] <- "kW"
string Xk[83.93,26.82] <- RGhX
var iI <- "wyjJk"
func fCG ()	return
'''
		expect = '''Program([VarDecl(Id(K7), ArrayType([26.64, 84.53, 74.07], BoolType), None, StringLit(kW)), VarDecl(Id(Xk), ArrayType([83.93, 26.82], StringType), None, Id(RGhX)), VarDecl(Id(iI), None, var, StringLit(wyjJk)), FuncDecl(Id(fCG), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115293))

	def test_21530115294(self):
		input = '''
func vf ()	begin
	end
func tEn ()	return
string WZ[81.38,16.62] <- 43.33
'''
		expect = '''Program([FuncDecl(Id(vf), [], Block([])), FuncDecl(Id(tEn), [], Return()), VarDecl(Id(WZ), ArrayType([81.38, 16.62], StringType), None, NumLit(43.33))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115294))

	def test_21530115295(self):
		input = '''
func DUqE (number Kcnc[18.62,9.29], string HMo[27.21,85.83,49.87])
	begin
		aN_q(68.14, e9o)
	end

'''
		expect = '''Program([FuncDecl(Id(DUqE), [VarDecl(Id(Kcnc), ArrayType([18.62, 9.29], NumberType), None, None), VarDecl(Id(HMo), ArrayType([27.21, 85.83, 49.87], StringType), None, None)], Block([CallStmt(Id(aN_q), [NumLit(68.14), Id(e9o)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115295))

	def test_21530115296(self):
		input = '''
string S0A <- false
bool c9Rh <- jNr
bool smx3
'''
		expect = '''Program([VarDecl(Id(S0A), StringType, None, BooleanLit(False)), VarDecl(Id(c9Rh), BoolType, None, Id(jNr)), VarDecl(Id(smx3), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115296))

	def test_21530115297(self):
		input = '''
func HiY (bool U7P, number o8W[51.35])
	begin
		var Vx <- 87.3
		dynamic DJA <- true
		if (83.93) continue
		elif ("y") for y6b until "IM" by "TjZY"
			return JX
		elif (24.2)
		continue
	end
func xp (bool uLL, bool xc, number smD[14.2,88.62,62.8])	return R65
bool g62 <- EPY
'''
		expect = '''Program([FuncDecl(Id(HiY), [VarDecl(Id(U7P), BoolType, None, None), VarDecl(Id(o8W), ArrayType([51.35], NumberType), None, None)], Block([VarDecl(Id(Vx), None, var, NumLit(87.3)), VarDecl(Id(DJA), None, dynamic, BooleanLit(True)), If(NumLit(83.93), Continue), [(StringLit(y), For(Id(y6b), StringLit(IM), StringLit(TjZY), Return(Id(JX)))), (NumLit(24.2), Continue)], None])), FuncDecl(Id(xp), [VarDecl(Id(uLL), BoolType, None, None), VarDecl(Id(xc), BoolType, None, None), VarDecl(Id(smD), ArrayType([14.2, 88.62, 62.8], NumberType), None, None)], Return(Id(R65))), VarDecl(Id(g62), BoolType, None, Id(EPY))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115297))

	def test_21530115298(self):
		input = '''
bool L_p <- 43.27
bool zS
func OS (bool Kn)
	return
'''
		expect = '''Program([VarDecl(Id(L_p), BoolType, None, NumLit(43.27)), VarDecl(Id(zS), BoolType, None, None), FuncDecl(Id(OS), [VarDecl(Id(Kn), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115298))

	def test_21530115299(self):
		input = '''
func nr (string r_Y)	return 8.65

'''
		expect = '''Program([FuncDecl(Id(nr), [VarDecl(Id(r_Y), StringType, None, None)], Return(NumLit(8.65)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115299))

	def test_21530115300(self):
		input = '''
func ea ()
	return

bool At_[22.33,6.06]
bool zD <- false
'''
		expect = '''Program([FuncDecl(Id(ea), [], Return()), VarDecl(Id(At_), ArrayType([22.33, 6.06], BoolType), None, None), VarDecl(Id(zD), BoolType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115300))

	def test_21530115301(self):
		input = '''
bool W8Ne[96.94,78.54,69.29]
number aX <- v8b
func hV4 (bool OZoL[8.76,54.12], string vSK[16.3,74.37])	return

number xV3[20.6]
'''
		expect = '''Program([VarDecl(Id(W8Ne), ArrayType([96.94, 78.54, 69.29], BoolType), None, None), VarDecl(Id(aX), NumberType, None, Id(v8b)), FuncDecl(Id(hV4), [VarDecl(Id(OZoL), ArrayType([8.76, 54.12], BoolType), None, None), VarDecl(Id(vSK), ArrayType([16.3, 74.37], StringType), None, None)], Return()), VarDecl(Id(xV3), ArrayType([20.6], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115301))

	def test_21530115302(self):
		input = '''
func Ga ()	return

number GS
func fYU (number vE[10.52,49.44], string tciC, bool OTA4)
	return "MnsuA"
func KM5 ()	begin
		QNL()
	end
bool ID[6.53,26.72,25.35] <- 34.48
'''
		expect = '''Program([FuncDecl(Id(Ga), [], Return()), VarDecl(Id(GS), NumberType, None, None), FuncDecl(Id(fYU), [VarDecl(Id(vE), ArrayType([10.52, 49.44], NumberType), None, None), VarDecl(Id(tciC), StringType, None, None), VarDecl(Id(OTA4), BoolType, None, None)], Return(StringLit(MnsuA))), FuncDecl(Id(KM5), [], Block([CallStmt(Id(QNL), [])])), VarDecl(Id(ID), ArrayType([6.53, 26.72, 25.35], BoolType), None, NumLit(34.48))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115302))

	def test_21530115303(self):
		input = '''
dynamic Dc
func YGDY (bool Ug[89.23,71.01], string bCJc, string bfC[45.31,61.91])	begin
		YAWb[false] <- K7
		begin
			begin
			end
			if (14.06) number tJK
			elif (75.04) number Rwr <- 67.75
			elif (as2) Kw("UR", 46.4)
			else continue
			continue
		end
	end

bool Lh
func Kwd (number JiN[65.89], number a2, bool GHEb[58.0,45.43,0.56])
	return

'''
		expect = '''Program([VarDecl(Id(Dc), None, dynamic, None), FuncDecl(Id(YGDY), [VarDecl(Id(Ug), ArrayType([89.23, 71.01], BoolType), None, None), VarDecl(Id(bCJc), StringType, None, None), VarDecl(Id(bfC), ArrayType([45.31, 61.91], StringType), None, None)], Block([AssignStmt(ArrayCell(Id(YAWb), [BooleanLit(False)]), Id(K7)), Block([Block([]), If(NumLit(14.06), VarDecl(Id(tJK), NumberType, None, None)), [(NumLit(75.04), VarDecl(Id(Rwr), NumberType, None, NumLit(67.75))), (Id(as2), CallStmt(Id(Kw), [StringLit(UR), NumLit(46.4)]))], Continue, Continue])])), VarDecl(Id(Lh), BoolType, None, None), FuncDecl(Id(Kwd), [VarDecl(Id(JiN), ArrayType([65.89], NumberType), None, None), VarDecl(Id(a2), NumberType, None, None), VarDecl(Id(GHEb), ArrayType([58.0, 45.43, 0.56], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115303))

	def test_21530115304(self):
		input = '''
number RlzC
bool HgI[41.1]
func hAXh (bool m3UK)	return 80.7
var eVG <- "XLiS"
'''
		expect = '''Program([VarDecl(Id(RlzC), NumberType, None, None), VarDecl(Id(HgI), ArrayType([41.1], BoolType), None, None), FuncDecl(Id(hAXh), [VarDecl(Id(m3UK), BoolType, None, None)], Return(NumLit(80.7))), VarDecl(Id(eVG), None, var, StringLit(XLiS))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115304))

	def test_21530115305(self):
		input = '''
func lGGC (bool itZe, string TbWa[40.22])	begin
		string Vbq
		return X2
		vzVe <- "EN"
	end
string xH[61.57,92.59] <- "IgLk"
func u7 (string RI[92.94], number qyT[0.11])
	return "FvHt"
'''
		expect = '''Program([FuncDecl(Id(lGGC), [VarDecl(Id(itZe), BoolType, None, None), VarDecl(Id(TbWa), ArrayType([40.22], StringType), None, None)], Block([VarDecl(Id(Vbq), StringType, None, None), Return(Id(X2)), AssignStmt(Id(vzVe), StringLit(EN))])), VarDecl(Id(xH), ArrayType([61.57, 92.59], StringType), None, StringLit(IgLk)), FuncDecl(Id(u7), [VarDecl(Id(RI), ArrayType([92.94], StringType), None, None), VarDecl(Id(qyT), ArrayType([0.11], NumberType), None, None)], Return(StringLit(FvHt)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115305))

	def test_21530115306(self):
		input = '''
dynamic bwL
dynamic H1p <- "lpaRr"
number AiNp <- 76.34
'''
		expect = '''Program([VarDecl(Id(bwL), None, dynamic, None), VarDecl(Id(H1p), None, dynamic, StringLit(lpaRr)), VarDecl(Id(AiNp), NumberType, None, NumLit(76.34))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115306))

	def test_21530115307(self):
		input = '''
func cwA (string by6[85.8,93.48,37.81])	return 20.04
bool H_[29.55]
func zvwd (string SKl8[17.55,33.49,43.14], bool Sn)
	return

bool Ma[59.85]
'''
		expect = '''Program([FuncDecl(Id(cwA), [VarDecl(Id(by6), ArrayType([85.8, 93.48, 37.81], StringType), None, None)], Return(NumLit(20.04))), VarDecl(Id(H_), ArrayType([29.55], BoolType), None, None), FuncDecl(Id(zvwd), [VarDecl(Id(SKl8), ArrayType([17.55, 33.49, 43.14], StringType), None, None), VarDecl(Id(Sn), BoolType, None, None)], Return()), VarDecl(Id(Ma), ArrayType([59.85], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115307))

	def test_21530115308(self):
		input = '''
number j0e8 <- "CjQAp"
string GXcf[7.0,46.13] <- RK
string BOR[32.75,41.78]
func UE0 ()
	return ZKZR
func CxZ (bool fH, string XrVe, number Rz[16.86,33.14,61.5])	return
'''
		expect = '''Program([VarDecl(Id(j0e8), NumberType, None, StringLit(CjQAp)), VarDecl(Id(GXcf), ArrayType([7.0, 46.13], StringType), None, Id(RK)), VarDecl(Id(BOR), ArrayType([32.75, 41.78], StringType), None, None), FuncDecl(Id(UE0), [], Return(Id(ZKZR))), FuncDecl(Id(CxZ), [VarDecl(Id(fH), BoolType, None, None), VarDecl(Id(XrVe), StringType, None, None), VarDecl(Id(Rz), ArrayType([16.86, 33.14, 61.5], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115308))

	def test_21530115309(self):
		input = '''
bool qk6O[9.87]
number GIH[86.11]
func RsKY (bool RMHX, number kj[95.81,16.47,98.83])	begin
		return false
		break
	end
'''
		expect = '''Program([VarDecl(Id(qk6O), ArrayType([9.87], BoolType), None, None), VarDecl(Id(GIH), ArrayType([86.11], NumberType), None, None), FuncDecl(Id(RsKY), [VarDecl(Id(RMHX), BoolType, None, None), VarDecl(Id(kj), ArrayType([95.81, 16.47, 98.83], NumberType), None, None)], Block([Return(BooleanLit(False)), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115309))

	def test_21530115310(self):
		input = '''
number p8e[1.19,69.91,98.38] <- kA3s
string z5Q <- true
func H4 (number jMj[76.34], bool J9E)	begin
		if (15.8)
		for fw until true by 97.99
			begin
				continue
				for Ov until 20.23 by false
					HbG("QN", mmW, false)
			end
		elif (35.46)
		break
		elif (false)
		number Fb[99.75,90.45,27.56] <- true
		else break
		break
	end

string bpa[47.43,89.93] <- LO
string JrM <- rXjZ
'''
		expect = '''Program([VarDecl(Id(p8e), ArrayType([1.19, 69.91, 98.38], NumberType), None, Id(kA3s)), VarDecl(Id(z5Q), StringType, None, BooleanLit(True)), FuncDecl(Id(H4), [VarDecl(Id(jMj), ArrayType([76.34], NumberType), None, None), VarDecl(Id(J9E), BoolType, None, None)], Block([If(NumLit(15.8), For(Id(fw), BooleanLit(True), NumLit(97.99), Block([Continue, For(Id(Ov), NumLit(20.23), BooleanLit(False), CallStmt(Id(HbG), [StringLit(QN), Id(mmW), BooleanLit(False)]))]))), [(NumLit(35.46), Break), (BooleanLit(False), VarDecl(Id(Fb), ArrayType([99.75, 90.45, 27.56], NumberType), None, BooleanLit(True)))], Break, Break])), VarDecl(Id(bpa), ArrayType([47.43, 89.93], StringType), None, Id(LO)), VarDecl(Id(JrM), StringType, None, Id(rXjZ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115310))

	def test_21530115311(self):
		input = '''
var nR <- 37.84
'''
		expect = '''Program([VarDecl(Id(nR), None, var, NumLit(37.84))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115311))

	def test_21530115312(self):
		input = '''
bool MT_[22.21,75.06,41.69] <- 32.11
func pA (number LwL[93.77,60.52], string GgT)
	begin
		for Fft until true by false
			return true
		p653(ar9z, true)
	end

'''
		expect = '''Program([VarDecl(Id(MT_), ArrayType([22.21, 75.06, 41.69], BoolType), None, NumLit(32.11)), FuncDecl(Id(pA), [VarDecl(Id(LwL), ArrayType([93.77, 60.52], NumberType), None, None), VarDecl(Id(GgT), StringType, None, None)], Block([For(Id(Fft), BooleanLit(True), BooleanLit(False), Return(BooleanLit(True))), CallStmt(Id(p653), [Id(ar9z), BooleanLit(True)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115312))

	def test_21530115313(self):
		input = '''
string uM[43.62,16.29,12.55]
func Ek0 ()
	return

func PWK (number Si[50.45], string C_a, number QFZw[56.44,84.83])
	begin
		begin
			continue
			return false
			Pn6(eZlt)
		end
		break
	end
number DW5[51.07,13.83,20.4] <- false
string Hex[55.46,17.31,78.13]
'''
		expect = '''Program([VarDecl(Id(uM), ArrayType([43.62, 16.29, 12.55], StringType), None, None), FuncDecl(Id(Ek0), [], Return()), FuncDecl(Id(PWK), [VarDecl(Id(Si), ArrayType([50.45], NumberType), None, None), VarDecl(Id(C_a), StringType, None, None), VarDecl(Id(QFZw), ArrayType([56.44, 84.83], NumberType), None, None)], Block([Block([Continue, Return(BooleanLit(False)), CallStmt(Id(Pn6), [Id(eZlt)])]), Break])), VarDecl(Id(DW5), ArrayType([51.07, 13.83, 20.4], NumberType), None, BooleanLit(False)), VarDecl(Id(Hex), ArrayType([55.46, 17.31, 78.13], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115313))

	def test_21530115314(self):
		input = '''
number UO <- 4.76
'''
		expect = '''Program([VarDecl(Id(UO), NumberType, None, NumLit(4.76))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115314))

	def test_21530115315(self):
		input = '''
bool y8LW[46.42,34.18,19.68]
number onU
func uaro (number PiRd[5.41], bool lEW[97.37,82.55,2.31])
	begin
		begin
			Ou <- f4
			continue
		end
		string eWN[92.79]
		return
	end

number LPTr[77.1,75.18,18.77]
string UwT[47.03,49.32] <- true
'''
		expect = '''Program([VarDecl(Id(y8LW), ArrayType([46.42, 34.18, 19.68], BoolType), None, None), VarDecl(Id(onU), NumberType, None, None), FuncDecl(Id(uaro), [VarDecl(Id(PiRd), ArrayType([5.41], NumberType), None, None), VarDecl(Id(lEW), ArrayType([97.37, 82.55, 2.31], BoolType), None, None)], Block([Block([AssignStmt(Id(Ou), Id(f4)), Continue]), VarDecl(Id(eWN), ArrayType([92.79], StringType), None, None), Return()])), VarDecl(Id(LPTr), ArrayType([77.1, 75.18, 18.77], NumberType), None, None), VarDecl(Id(UwT), ArrayType([47.03, 49.32], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115315))

	def test_21530115316(self):
		input = '''
func tmbX ()	begin
		for A42 until ZZM by UK9V
			for Qo until 15.9 by "vv"
				bool MN
	end
func KDW ()
	return "FmeAJ"

'''
		expect = '''Program([FuncDecl(Id(tmbX), [], Block([For(Id(A42), Id(ZZM), Id(UK9V), For(Id(Qo), NumLit(15.9), StringLit(vv), VarDecl(Id(MN), BoolType, None, None)))])), FuncDecl(Id(KDW), [], Return(StringLit(FmeAJ)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115316))

	def test_21530115317(self):
		input = '''
string tUMn[90.66,48.82,81.46] <- "jdZv"
func FIYj (string nCU[76.82], bool jm_R[23.84,50.51], number Gv)
	return true
func VutX (number ElTD, number fJQj[13.43])	return
bool GN9H
'''
		expect = '''Program([VarDecl(Id(tUMn), ArrayType([90.66, 48.82, 81.46], StringType), None, StringLit(jdZv)), FuncDecl(Id(FIYj), [VarDecl(Id(nCU), ArrayType([76.82], StringType), None, None), VarDecl(Id(jm_R), ArrayType([23.84, 50.51], BoolType), None, None), VarDecl(Id(Gv), NumberType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(VutX), [VarDecl(Id(ElTD), NumberType, None, None), VarDecl(Id(fJQj), ArrayType([13.43], NumberType), None, None)], Return()), VarDecl(Id(GN9H), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115317))

	def test_21530115318(self):
		input = '''
func Cz_s ()
	begin
		continue
		begin
		end
	end
func g2 ()
	return
'''
		expect = '''Program([FuncDecl(Id(Cz_s), [], Block([Continue, Block([])])), FuncDecl(Id(g2), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115318))

	def test_21530115319(self):
		input = '''
func gokw (string TA8, string U2O[9.19,86.8], bool c2[91.65])	return
number JG <- uz
number yfWx[92.87,8.84] <- "yA"
dynamic CA <- "lsIt"
'''
		expect = '''Program([FuncDecl(Id(gokw), [VarDecl(Id(TA8), StringType, None, None), VarDecl(Id(U2O), ArrayType([9.19, 86.8], StringType), None, None), VarDecl(Id(c2), ArrayType([91.65], BoolType), None, None)], Return()), VarDecl(Id(JG), NumberType, None, Id(uz)), VarDecl(Id(yfWx), ArrayType([92.87, 8.84], NumberType), None, StringLit(yA)), VarDecl(Id(CA), None, dynamic, StringLit(lsIt))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115319))

	def test_21530115320(self):
		input = '''
func D4 ()	return
func NV (bool AOWy[2.7], number It, number Qa[42.45,29.68,27.13])
	return "TqN"
func bY_I (number YUj[34.9], number ov5, number SW[43.73,58.99,81.51])	return MBBN

func Dz (string DVq[83.47,77.29,85.71], bool xZa5[30.64], string xb)
	return "FEP"
string Ih[78.01,71.07,35.27]
'''
		expect = '''Program([FuncDecl(Id(D4), [], Return()), FuncDecl(Id(NV), [VarDecl(Id(AOWy), ArrayType([2.7], BoolType), None, None), VarDecl(Id(It), NumberType, None, None), VarDecl(Id(Qa), ArrayType([42.45, 29.68, 27.13], NumberType), None, None)], Return(StringLit(TqN))), FuncDecl(Id(bY_I), [VarDecl(Id(YUj), ArrayType([34.9], NumberType), None, None), VarDecl(Id(ov5), NumberType, None, None), VarDecl(Id(SW), ArrayType([43.73, 58.99, 81.51], NumberType), None, None)], Return(Id(MBBN))), FuncDecl(Id(Dz), [VarDecl(Id(DVq), ArrayType([83.47, 77.29, 85.71], StringType), None, None), VarDecl(Id(xZa5), ArrayType([30.64], BoolType), None, None), VarDecl(Id(xb), StringType, None, None)], Return(StringLit(FEP))), VarDecl(Id(Ih), ArrayType([78.01, 71.07, 35.27], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115320))

	def test_21530115321(self):
		input = '''
func kY (number Hn8[71.17,95.94,52.89], bool hTU)
	begin
		if (92.32) if (dAgy)
		for k9 until pH1 by true
			return
		elif (true)
		string gwK[62.08]
		elif ("db")
		IBH(45.98, true, 50.67)
		elif (false)
		if (false)
		if ("UW") string eUU[37.35,86.28]
		elif (false)
		begin
			for VO7 until "JsWBt" by true
				if ("KfeVz") break
				elif (20.03)
				break
				elif ("hErwV") dynamic q8A
				elif ("sLhs") return 58.42
				elif (Khp3) break
				elif (55.98) break
				else return
			dynamic ZzeB <- false
		end
		elif (lAgA) VYh(95.46, "O")
		elif (true) break
		else if (93.22) for uir until "nr" by kDy1
			continue
		elif (JBn)
		continue
		elif ("RkEYf") if ("vXphv") GgW(72.64, q4YF, "jXg")
		elif ("rxsOc")
		begin
			for Ohh1 until "DTJRz" by true
				string QgxD[36.13,62.93,75.91]
		end
		elif ("AJl") for NL until uD by 49.95
			continue
		elif ("q") begin
			return
		end
		elif ("rt")
		break
		else jQc[true] <- lB
		elif (95.55)
		break
		elif (Ur)
		return "AP"
		elif (ZQ8)
		kDf("rOXZ", 74.5)
		elif (true)
		wf_ <- E_
		elif ("YtNJx") bool gbl8[3.12,91.74,87.49] <- "yWyvh"
		elif (F1)
		number AV[37.85]
		elif (true)
		begin
			break
			break
		end
		else W8y("viR")
		if (false)
		number Dc <- "rzZHz"
		elif (b7F) continue
		elif (9.81)
		string NtZf[86.29,46.0,65.13]
		elif (92.67)
		begin
			jTCX(false, 73.32, false)
			continue
			TB(false, "sA")
		end
		elif (bR) break
		elif (false) g8 <- pp
		else break
		begin
		end
	end

string Or
func OC ()
	return

func b1y (string GMai)	return

'''
		expect = '''Program([FuncDecl(Id(kY), [VarDecl(Id(Hn8), ArrayType([71.17, 95.94, 52.89], NumberType), None, None), VarDecl(Id(hTU), BoolType, None, None)], Block([If(NumLit(92.32), If(Id(dAgy), For(Id(k9), Id(pH1), BooleanLit(True), Return())), [(BooleanLit(True), VarDecl(Id(gwK), ArrayType([62.08], StringType), None, None)), (StringLit(db), CallStmt(Id(IBH), [NumLit(45.98), BooleanLit(True), NumLit(50.67)])), (BooleanLit(False), If(BooleanLit(False), If(StringLit(UW), VarDecl(Id(eUU), ArrayType([37.35, 86.28], StringType), None, None)), [(BooleanLit(False), Block([For(Id(VO7), StringLit(JsWBt), BooleanLit(True), If(StringLit(KfeVz), Break), [(NumLit(20.03), Break), (StringLit(hErwV), VarDecl(Id(q8A), None, dynamic, None)), (StringLit(sLhs), Return(NumLit(58.42))), (Id(Khp3), Break), (NumLit(55.98), Break)], Return()), VarDecl(Id(ZzeB), None, dynamic, BooleanLit(False))])), (Id(lAgA), CallStmt(Id(VYh), [NumLit(95.46), StringLit(O)])), (BooleanLit(True), Break)], If(NumLit(93.22), For(Id(uir), StringLit(nr), Id(kDy1), Continue)), [(Id(JBn), Continue), (StringLit(RkEYf), If(StringLit(vXphv), CallStmt(Id(GgW), [NumLit(72.64), Id(q4YF), StringLit(jXg)])), [(StringLit(rxsOc), Block([For(Id(Ohh1), StringLit(DTJRz), BooleanLit(True), VarDecl(Id(QgxD), ArrayType([36.13, 62.93, 75.91], StringType), None, None))])), (StringLit(AJl), For(Id(NL), Id(uD), NumLit(49.95), Continue)), (StringLit(q), Block([Return()])), (StringLit(rt), Break)], AssignStmt(ArrayCell(Id(jQc), [BooleanLit(True)]), Id(lB))), (NumLit(95.55), Break), (Id(Ur), Return(StringLit(AP))), (Id(ZQ8), CallStmt(Id(kDf), [StringLit(rOXZ), NumLit(74.5)])), (BooleanLit(True), AssignStmt(Id(wf_), Id(E_))), (StringLit(YtNJx), VarDecl(Id(gbl8), ArrayType([3.12, 91.74, 87.49], BoolType), None, StringLit(yWyvh))), (Id(F1), VarDecl(Id(AV), ArrayType([37.85], NumberType), None, None))], None), [], None), (BooleanLit(True), Block([Break, Break]))], CallStmt(Id(W8y), [StringLit(viR)])), [], None, If(BooleanLit(False), VarDecl(Id(Dc), NumberType, None, StringLit(rzZHz))), [(Id(b7F), Continue), (NumLit(9.81), VarDecl(Id(NtZf), ArrayType([86.29, 46.0, 65.13], StringType), None, None)), (NumLit(92.67), Block([CallStmt(Id(jTCX), [BooleanLit(False), NumLit(73.32), BooleanLit(False)]), Continue, CallStmt(Id(TB), [BooleanLit(False), StringLit(sA)])])), (Id(bR), Break), (BooleanLit(False), AssignStmt(Id(g8), Id(pp)))], Break, Block([])])), VarDecl(Id(Or), StringType, None, None), FuncDecl(Id(OC), [], Return()), FuncDecl(Id(b1y), [VarDecl(Id(GMai), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115321))

	def test_21530115322(self):
		input = '''
func a2J (bool cgE, bool YzG6)	begin
		begin
			return false
			begin
				return
				return XkC1
			end
		end
		break
	end

func aW ()
	begin
		mZg["sHn", "pQ", O_b] <- 4.67
	end
'''
		expect = '''Program([FuncDecl(Id(a2J), [VarDecl(Id(cgE), BoolType, None, None), VarDecl(Id(YzG6), BoolType, None, None)], Block([Block([Return(BooleanLit(False)), Block([Return(), Return(Id(XkC1))])]), Break])), FuncDecl(Id(aW), [], Block([AssignStmt(ArrayCell(Id(mZg), [StringLit(sHn), StringLit(pQ), Id(O_b)]), NumLit(4.67))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115322))

	def test_21530115323(self):
		input = '''
string uglg[17.58,55.61] <- "C"
'''
		expect = '''Program([VarDecl(Id(uglg), ArrayType([17.58, 55.61], StringType), None, StringLit(C))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115323))

	def test_21530115324(self):
		input = '''
func H3 (number hh[38.43])
	return true

string DORA
func bB (string uw4[68.44,69.71,96.16])
	begin
		continue
		if (false)
		break
		elif ("fBh") if ("RPW") for TZ until "fwSqz" by "hrtc"
			dynamic rUZ
		else continue
		elif (false)
		if ("AfC") SShR["GA"] <- "VGqp"
		elif (3.24) K7k1(i8, true)
		elif (txrs) for ctIY until sb by false
			uVU <- "ZwTAR"
		elif (hE)
		begin
			continue
			begin
				return "OCta"
			end
			Pb[Dl, true, "MJxYH"] <- true
		end
		elif ("qJnn")
		if (pUU) begin
		end
		elif (Db) if (l0m) fii <- true
		elif (true) if (true)
		qC[BFf, "OQb", "sBp"] <- RSyV
		else Eam(G3, "BEN")
		elif ("AfNKE")
		break
		else number Eaf <- mFP6
		else if (63.64) if (true) break
		elif (G1h)
		if ("FV")
		for lcs until true by xtoG
			for OIt until "S" by 25.53
				dynamic Xuv <- HA3
		elif (muKj) return
		elif (hS)
		return
		else xZ[false] <- true
		RPY()
	end

dynamic cu
var L_0z <- xbGX
'''
		expect = '''Program([FuncDecl(Id(H3), [VarDecl(Id(hh), ArrayType([38.43], NumberType), None, None)], Return(BooleanLit(True))), VarDecl(Id(DORA), StringType, None, None), FuncDecl(Id(bB), [VarDecl(Id(uw4), ArrayType([68.44, 69.71, 96.16], StringType), None, None)], Block([Continue, If(BooleanLit(False), Break), [(StringLit(fBh), If(StringLit(RPW), For(Id(TZ), StringLit(fwSqz), StringLit(hrtc), VarDecl(Id(rUZ), None, dynamic, None))), [], Continue), (BooleanLit(False), If(StringLit(AfC), AssignStmt(ArrayCell(Id(SShR), [StringLit(GA)]), StringLit(VGqp))), [(NumLit(3.24), CallStmt(Id(K7k1), [Id(i8), BooleanLit(True)])), (Id(txrs), For(Id(ctIY), Id(sb), BooleanLit(False), AssignStmt(Id(uVU), StringLit(ZwTAR)))), (Id(hE), Block([Continue, Block([Return(StringLit(OCta))]), AssignStmt(ArrayCell(Id(Pb), [Id(Dl), BooleanLit(True), StringLit(MJxYH)]), BooleanLit(True))])), (StringLit(qJnn), If(Id(pUU), Block([])), [(Id(Db), If(Id(l0m), AssignStmt(Id(fii), BooleanLit(True))), [(BooleanLit(True), If(BooleanLit(True), AssignStmt(ArrayCell(Id(qC), [Id(BFf), StringLit(OQb), StringLit(sBp)]), Id(RSyV))), [], CallStmt(Id(Eam), [Id(G3), StringLit(BEN)])), (StringLit(AfNKE), Break)], VarDecl(Id(Eaf), NumberType, None, Id(mFP6)))], If(NumLit(63.64), If(BooleanLit(True), Break), [(Id(G1h), If(StringLit(FV), For(Id(lcs), BooleanLit(True), Id(xtoG), For(Id(OIt), StringLit(S), NumLit(25.53), VarDecl(Id(Xuv), None, dynamic, Id(HA3))))), [], None)], None), [], None), (Id(muKj), Return())], None), (Id(hS), Return())], AssignStmt(ArrayCell(Id(xZ), [BooleanLit(False)]), BooleanLit(True)), CallStmt(Id(RPY), [])])), VarDecl(Id(cu), None, dynamic, None), VarDecl(Id(L_0z), None, var, Id(xbGX))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115324))

	def test_21530115325(self):
		input = '''
func td ()
	return 84.77

bool IM[99.86,52.39]
func sNJ3 (number VQUZ, bool zeHx, bool gg[96.49])	return 89.52

'''
		expect = '''Program([FuncDecl(Id(td), [], Return(NumLit(84.77))), VarDecl(Id(IM), ArrayType([99.86, 52.39], BoolType), None, None), FuncDecl(Id(sNJ3), [VarDecl(Id(VQUZ), NumberType, None, None), VarDecl(Id(zeHx), BoolType, None, None), VarDecl(Id(gg), ArrayType([96.49], BoolType), None, None)], Return(NumLit(89.52)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115325))

	def test_21530115326(self):
		input = '''
bool q9[10.5,72.89,0.76]
'''
		expect = '''Program([VarDecl(Id(q9), ArrayType([10.5, 72.89, 0.76], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115326))

	def test_21530115327(self):
		input = '''
string pnN[85.88,12.94] <- true
number j1 <- VR
number qG <- CEK
'''
		expect = '''Program([VarDecl(Id(pnN), ArrayType([85.88, 12.94], StringType), None, BooleanLit(True)), VarDecl(Id(j1), NumberType, None, Id(VR)), VarDecl(Id(qG), NumberType, None, Id(CEK))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115327))

	def test_21530115328(self):
		input = '''
func c1T ()	return

func rV ()
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(c1T), [], Return()), FuncDecl(Id(rV), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115328))

	def test_21530115329(self):
		input = '''
func L3 (bool s1t[20.09,0.33], number pT, bool VGIX[66.11,13.98,92.08])	return

bool EcoS[40.17] <- ht
bool CBF[71.03,87.99]
'''
		expect = '''Program([FuncDecl(Id(L3), [VarDecl(Id(s1t), ArrayType([20.09, 0.33], BoolType), None, None), VarDecl(Id(pT), NumberType, None, None), VarDecl(Id(VGIX), ArrayType([66.11, 13.98, 92.08], BoolType), None, None)], Return()), VarDecl(Id(EcoS), ArrayType([40.17], BoolType), None, Id(ht)), VarDecl(Id(CBF), ArrayType([71.03, 87.99], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115329))

	def test_21530115330(self):
		input = '''
bool P8[99.51,71.02,97.87] <- xD
number p81[25.33]
'''
		expect = '''Program([VarDecl(Id(P8), ArrayType([99.51, 71.02, 97.87], BoolType), None, Id(xD)), VarDecl(Id(p81), ArrayType([25.33], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115330))

	def test_21530115331(self):
		input = '''
bool Jj[95.54] <- false
bool uG[76.69,36.25] <- "Bq"
bool re[65.22]
'''
		expect = '''Program([VarDecl(Id(Jj), ArrayType([95.54], BoolType), None, BooleanLit(False)), VarDecl(Id(uG), ArrayType([76.69, 36.25], BoolType), None, StringLit(Bq)), VarDecl(Id(re), ArrayType([65.22], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115331))

	def test_21530115332(self):
		input = '''
var tc <- 26.42
func Js ()
	return eyn
bool pK <- 11.93
'''
		expect = '''Program([VarDecl(Id(tc), None, var, NumLit(26.42)), FuncDecl(Id(Js), [], Return(Id(eyn))), VarDecl(Id(pK), BoolType, None, NumLit(11.93))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115332))

	def test_21530115333(self):
		input = '''
string zZag <- gr9b
func OMx6 (string Z0a[45.17], number OF[17.28,5.06], number xv[29.1,54.72])	return

func QJ (number IaN[16.5,33.63], number EZD)
	begin
		begin
			continue
		end
	end
func hq (bool D1[28.72,2.0])
	return

string jWD[10.5,6.51]
'''
		expect = '''Program([VarDecl(Id(zZag), StringType, None, Id(gr9b)), FuncDecl(Id(OMx6), [VarDecl(Id(Z0a), ArrayType([45.17], StringType), None, None), VarDecl(Id(OF), ArrayType([17.28, 5.06], NumberType), None, None), VarDecl(Id(xv), ArrayType([29.1, 54.72], NumberType), None, None)], Return()), FuncDecl(Id(QJ), [VarDecl(Id(IaN), ArrayType([16.5, 33.63], NumberType), None, None), VarDecl(Id(EZD), NumberType, None, None)], Block([Block([Continue])])), FuncDecl(Id(hq), [VarDecl(Id(D1), ArrayType([28.72, 2.0], BoolType), None, None)], Return()), VarDecl(Id(jWD), ArrayType([10.5, 6.51], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115333))

	def test_21530115334(self):
		input = '''
string YQr[81.72]
'''
		expect = '''Program([VarDecl(Id(YQr), ArrayType([81.72], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115334))

	def test_21530115335(self):
		input = '''
func PSc (bool FoEu[7.96], bool IOyz, string f_Hl)	return 65.51

var M6 <- false
bool EO[58.55] <- QMD
func WQnw (number bWS0[55.98], number ecd[51.37,60.92], bool Qq9)	begin
		for UJC until false by false
			continue
		return
		if (99.93) if (false)
		break
		elif ("ZXozz")
		return 93.42
		elif (BT) string OF <- true
		elif (true)
		hT_ <- 74.27
		elif (30.26) for vd until "IMZk" by 11.44
			Ylq("rpUQ", 26.97, "VSa")
		elif (zU)
		if (false)
		number y_qt[83.11,18.7,74.55] <- "q"
		else vZ("HDC", iTz)
		elif (false) string EZ[83.41,36.93,94.03] <- 98.12
		else for qtEP until "HEpC" by false
			m_k("CEs")
	end

'''
		expect = '''Program([FuncDecl(Id(PSc), [VarDecl(Id(FoEu), ArrayType([7.96], BoolType), None, None), VarDecl(Id(IOyz), BoolType, None, None), VarDecl(Id(f_Hl), StringType, None, None)], Return(NumLit(65.51))), VarDecl(Id(M6), None, var, BooleanLit(False)), VarDecl(Id(EO), ArrayType([58.55], BoolType), None, Id(QMD)), FuncDecl(Id(WQnw), [VarDecl(Id(bWS0), ArrayType([55.98], NumberType), None, None), VarDecl(Id(ecd), ArrayType([51.37, 60.92], NumberType), None, None), VarDecl(Id(Qq9), BoolType, None, None)], Block([For(Id(UJC), BooleanLit(False), BooleanLit(False), Continue), Return(), If(NumLit(99.93), If(BooleanLit(False), Break), [(StringLit(ZXozz), Return(NumLit(93.42))), (Id(BT), VarDecl(Id(OF), StringType, None, BooleanLit(True))), (BooleanLit(True), AssignStmt(Id(hT_), NumLit(74.27))), (NumLit(30.26), For(Id(vd), StringLit(IMZk), NumLit(11.44), CallStmt(Id(Ylq), [StringLit(rpUQ), NumLit(26.97), StringLit(VSa)]))), (Id(zU), If(BooleanLit(False), VarDecl(Id(y_qt), ArrayType([83.11, 18.7, 74.55], NumberType), None, StringLit(q))), [], CallStmt(Id(vZ), [StringLit(HDC), Id(iTz)])), (BooleanLit(False), VarDecl(Id(EZ), ArrayType([83.41, 36.93, 94.03], StringType), None, NumLit(98.12)))], For(Id(qtEP), StringLit(HEpC), BooleanLit(False), CallStmt(Id(m_k), [StringLit(CEs)]))), [], None]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115335))

	def test_21530115336(self):
		input = '''
var Dwf <- 10.81
var cHn <- Or8G
'''
		expect = '''Program([VarDecl(Id(Dwf), None, var, NumLit(10.81)), VarDecl(Id(cHn), None, var, Id(Or8G))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115336))

	def test_21530115337(self):
		input = '''
func PLY5 (string tTb[87.93,81.25,64.1])	return false

func Cpxc ()	return

'''
		expect = '''Program([FuncDecl(Id(PLY5), [VarDecl(Id(tTb), ArrayType([87.93, 81.25, 64.1], StringType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(Cpxc), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115337))

	def test_21530115338(self):
		input = '''
bool rKp[95.54,20.22,40.7]
'''
		expect = '''Program([VarDecl(Id(rKp), ArrayType([95.54, 20.22, 40.7], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115338))

	def test_21530115339(self):
		input = '''
string EW <- "zSyO"
'''
		expect = '''Program([VarDecl(Id(EW), StringType, None, StringLit(zSyO))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115339))

	def test_21530115340(self):
		input = '''
func StQ (number bAwS)
	return true
string JGT
string C5S1[62.18,7.17,3.76] <- false
string BWq[94.31,46.85]
bool f_FC[85.54,48.37,72.26] <- 10.63
'''
		expect = '''Program([FuncDecl(Id(StQ), [VarDecl(Id(bAwS), NumberType, None, None)], Return(BooleanLit(True))), VarDecl(Id(JGT), StringType, None, None), VarDecl(Id(C5S1), ArrayType([62.18, 7.17, 3.76], StringType), None, BooleanLit(False)), VarDecl(Id(BWq), ArrayType([94.31, 46.85], StringType), None, None), VarDecl(Id(f_FC), ArrayType([85.54, 48.37, 72.26], BoolType), None, NumLit(10.63))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115340))

	def test_21530115341(self):
		input = '''
string RjN
func P6y5 ()	return "nD"

func V20 (bool QL[41.98,22.57,12.15], string zoB, string QBD)
	return false
'''
		expect = '''Program([VarDecl(Id(RjN), StringType, None, None), FuncDecl(Id(P6y5), [], Return(StringLit(nD))), FuncDecl(Id(V20), [VarDecl(Id(QL), ArrayType([41.98, 22.57, 12.15], BoolType), None, None), VarDecl(Id(zoB), StringType, None, None), VarDecl(Id(QBD), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115341))

	def test_21530115342(self):
		input = '''
func Nb (number BXKm)	return "KggW"

func G5l (string UR4F, number wfK)
	begin
	end

func tWC (string mFt[2.57,74.95,13.21], bool mha)	return

func aKsf ()
	return "hWqO"
number UaEn[8.77,54.72]
'''
		expect = '''Program([FuncDecl(Id(Nb), [VarDecl(Id(BXKm), NumberType, None, None)], Return(StringLit(KggW))), FuncDecl(Id(G5l), [VarDecl(Id(UR4F), StringType, None, None), VarDecl(Id(wfK), NumberType, None, None)], Block([])), FuncDecl(Id(tWC), [VarDecl(Id(mFt), ArrayType([2.57, 74.95, 13.21], StringType), None, None), VarDecl(Id(mha), BoolType, None, None)], Return()), FuncDecl(Id(aKsf), [], Return(StringLit(hWqO))), VarDecl(Id(UaEn), ArrayType([8.77, 54.72], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115342))

	def test_21530115343(self):
		input = '''
func ZaBL (number aC, number lbc)
	return
bool HvtK[57.62,98.14] <- 83.63
'''
		expect = '''Program([FuncDecl(Id(ZaBL), [VarDecl(Id(aC), NumberType, None, None), VarDecl(Id(lbc), NumberType, None, None)], Return()), VarDecl(Id(HvtK), ArrayType([57.62, 98.14], BoolType), None, NumLit(83.63))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115343))

	def test_21530115344(self):
		input = '''
bool pK_v
'''
		expect = '''Program([VarDecl(Id(pK_v), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115344))

	def test_21530115345(self):
		input = '''
func fi (number NO2[57.15,28.58], bool eX0B[12.75], string LES)
	begin
		JYwC(false, false)
		for Jvyt until wD8n by 55.92
			TO(22.04)
	end

'''
		expect = '''Program([FuncDecl(Id(fi), [VarDecl(Id(NO2), ArrayType([57.15, 28.58], NumberType), None, None), VarDecl(Id(eX0B), ArrayType([12.75], BoolType), None, None), VarDecl(Id(LES), StringType, None, None)], Block([CallStmt(Id(JYwC), [BooleanLit(False), BooleanLit(False)]), For(Id(Jvyt), Id(wD8n), NumLit(55.92), CallStmt(Id(TO), [NumLit(22.04)]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115345))

	def test_21530115346(self):
		input = '''
func KB (bool jtp_)
	return

string asOP <- 6.83
dynamic Cax <- a90c
number hcyo[26.79,37.47,96.74]
'''
		expect = '''Program([FuncDecl(Id(KB), [VarDecl(Id(jtp_), BoolType, None, None)], Return()), VarDecl(Id(asOP), StringType, None, NumLit(6.83)), VarDecl(Id(Cax), None, dynamic, Id(a90c)), VarDecl(Id(hcyo), ArrayType([26.79, 37.47, 96.74], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115346))

	def test_21530115347(self):
		input = '''
bool wL[23.17] <- xkXi
func cj (string pNc[99.45,9.43,92.49])	return

bool qa8h <- false
func J8dR (number cd, number Zt[21.02], string NWG)	return false
string ZML
'''
		expect = '''Program([VarDecl(Id(wL), ArrayType([23.17], BoolType), None, Id(xkXi)), FuncDecl(Id(cj), [VarDecl(Id(pNc), ArrayType([99.45, 9.43, 92.49], StringType), None, None)], Return()), VarDecl(Id(qa8h), BoolType, None, BooleanLit(False)), FuncDecl(Id(J8dR), [VarDecl(Id(cd), NumberType, None, None), VarDecl(Id(Zt), ArrayType([21.02], NumberType), None, None), VarDecl(Id(NWG), StringType, None, None)], Return(BooleanLit(False))), VarDecl(Id(ZML), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115347))

	def test_21530115348(self):
		input = '''
func uG ()
	return

'''
		expect = '''Program([FuncDecl(Id(uG), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115348))

	def test_21530115349(self):
		input = '''
string XagB[21.45,29.85,67.92] <- true
number vGp
func NHhI (bool DCyE[69.07,12.98])
	begin
	end

'''
		expect = '''Program([VarDecl(Id(XagB), ArrayType([21.45, 29.85, 67.92], StringType), None, BooleanLit(True)), VarDecl(Id(vGp), NumberType, None, None), FuncDecl(Id(NHhI), [VarDecl(Id(DCyE), ArrayType([69.07, 12.98], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115349))

	def test_21530115350(self):
		input = '''
func ym ()
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(ym), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115350))

	def test_21530115351(self):
		input = '''
number UZ0[8.83] <- RgC
bool nx[89.41,21.7,32.27]
string N5 <- false
func gl (string c8i[92.98,85.94], string Fkwy, number T6)	return

'''
		expect = '''Program([VarDecl(Id(UZ0), ArrayType([8.83], NumberType), None, Id(RgC)), VarDecl(Id(nx), ArrayType([89.41, 21.7, 32.27], BoolType), None, None), VarDecl(Id(N5), StringType, None, BooleanLit(False)), FuncDecl(Id(gl), [VarDecl(Id(c8i), ArrayType([92.98, 85.94], StringType), None, None), VarDecl(Id(Fkwy), StringType, None, None), VarDecl(Id(T6), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115351))

	def test_21530115352(self):
		input = '''
number rw
bool z9J7
number Qd3J[64.35]
func I6qw (number aAf)
	return "yhsdp"

'''
		expect = '''Program([VarDecl(Id(rw), NumberType, None, None), VarDecl(Id(z9J7), BoolType, None, None), VarDecl(Id(Qd3J), ArrayType([64.35], NumberType), None, None), FuncDecl(Id(I6qw), [VarDecl(Id(aAf), NumberType, None, None)], Return(StringLit(yhsdp)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115352))

	def test_21530115353(self):
		input = '''
func EqM (number OBmF[87.3], number Tc9, number fJ[65.49,54.25])	return 48.94

func Y_f (string M1B7, number DB)
	begin
		break
	end

number U1[19.67,66.29,87.06] <- mHRn
'''
		expect = '''Program([FuncDecl(Id(EqM), [VarDecl(Id(OBmF), ArrayType([87.3], NumberType), None, None), VarDecl(Id(Tc9), NumberType, None, None), VarDecl(Id(fJ), ArrayType([65.49, 54.25], NumberType), None, None)], Return(NumLit(48.94))), FuncDecl(Id(Y_f), [VarDecl(Id(M1B7), StringType, None, None), VarDecl(Id(DB), NumberType, None, None)], Block([Break])), VarDecl(Id(U1), ArrayType([19.67, 66.29, 87.06], NumberType), None, Id(mHRn))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115353))

	def test_21530115354(self):
		input = '''
string MZY[33.21,84.21,94.31]
'''
		expect = '''Program([VarDecl(Id(MZY), ArrayType([33.21, 84.21, 94.31], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115354))

	def test_21530115355(self):
		input = '''
number XoI5
bool Pc[51.76,46.61]
'''
		expect = '''Program([VarDecl(Id(XoI5), NumberType, None, None), VarDecl(Id(Pc), ArrayType([51.76, 46.61], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115355))

	def test_21530115356(self):
		input = '''
bool yx[32.95] <- fJM
'''
		expect = '''Program([VarDecl(Id(yx), ArrayType([32.95], BoolType), None, Id(fJM))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115356))

	def test_21530115357(self):
		input = '''
func aak ()	begin
	end
func n3vD (number Cuv, string zD[3.49,95.47,70.52], bool Idie)	begin
		bNEL <- yW
		return
	end
func hSuh (string bYT)
	return true

string PDmK[74.64,13.92]
func BP7c (string iPb[91.84])	begin
	end
'''
		expect = '''Program([FuncDecl(Id(aak), [], Block([])), FuncDecl(Id(n3vD), [VarDecl(Id(Cuv), NumberType, None, None), VarDecl(Id(zD), ArrayType([3.49, 95.47, 70.52], StringType), None, None), VarDecl(Id(Idie), BoolType, None, None)], Block([AssignStmt(Id(bNEL), Id(yW)), Return()])), FuncDecl(Id(hSuh), [VarDecl(Id(bYT), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(PDmK), ArrayType([74.64, 13.92], StringType), None, None), FuncDecl(Id(BP7c), [VarDecl(Id(iPb), ArrayType([91.84], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115357))

	def test_21530115358(self):
		input = '''
string Ixa[63.46,63.79,67.98] <- Hf
bool ox <- z2
string VU_ <- zGn
func JVm ()	return

func D2dH (string JKR1)	begin
		fV[IGX, true, true] <- "KmWbt"
		number g9e[44.83,90.41]
		return
	end
'''
		expect = '''Program([VarDecl(Id(Ixa), ArrayType([63.46, 63.79, 67.98], StringType), None, Id(Hf)), VarDecl(Id(ox), BoolType, None, Id(z2)), VarDecl(Id(VU_), StringType, None, Id(zGn)), FuncDecl(Id(JVm), [], Return()), FuncDecl(Id(D2dH), [VarDecl(Id(JKR1), StringType, None, None)], Block([AssignStmt(ArrayCell(Id(fV), [Id(IGX), BooleanLit(True), BooleanLit(True)]), StringLit(KmWbt)), VarDecl(Id(g9e), ArrayType([44.83, 90.41], NumberType), None, None), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115358))

	def test_21530115359(self):
		input = '''
func HfTJ (number mdU[9.76,43.95,1.57], bool sfl)	begin
	end
func lM ()	return MX8

string TVk[37.84,82.54] <- "ddu"
func dL ()	return M3
'''
		expect = '''Program([FuncDecl(Id(HfTJ), [VarDecl(Id(mdU), ArrayType([9.76, 43.95, 1.57], NumberType), None, None), VarDecl(Id(sfl), BoolType, None, None)], Block([])), FuncDecl(Id(lM), [], Return(Id(MX8))), VarDecl(Id(TVk), ArrayType([37.84, 82.54], StringType), None, StringLit(ddu)), FuncDecl(Id(dL), [], Return(Id(M3)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115359))

	def test_21530115360(self):
		input = '''
func Ry2 (bool fMNC)
	begin
		break
		WQ(XPb9, "uH")
		return
	end
func rNM ()
	begin
		YR8 <- FLW7
	end

number OJ[27.33,44.97,83.08]
'''
		expect = '''Program([FuncDecl(Id(Ry2), [VarDecl(Id(fMNC), BoolType, None, None)], Block([Break, CallStmt(Id(WQ), [Id(XPb9), StringLit(uH)]), Return()])), FuncDecl(Id(rNM), [], Block([AssignStmt(Id(YR8), Id(FLW7))])), VarDecl(Id(OJ), ArrayType([27.33, 44.97, 83.08], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115360))

	def test_21530115361(self):
		input = '''
string iq[78.32,97.02,37.73]
string Wv[53.5]
func KBhq ()	return false

'''
		expect = '''Program([VarDecl(Id(iq), ArrayType([78.32, 97.02, 37.73], StringType), None, None), VarDecl(Id(Wv), ArrayType([53.5], StringType), None, None), FuncDecl(Id(KBhq), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115361))

	def test_21530115362(self):
		input = '''
bool BxsX
func wrF ()
	return tt

'''
		expect = '''Program([VarDecl(Id(BxsX), BoolType, None, None), FuncDecl(Id(wrF), [], Return(Id(tt)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115362))

	def test_21530115363(self):
		input = '''
func lH (bool w8K, string kt1)	begin
		if ("Dy") Xq_j <- bvVp
		elif (YK) for MvZZ until 56.8 by 22.81
			break
		elif ("y") number Y7Le
		elif (2.53)
		break
		else for vG6 until true by R1
			return
		number boYj[50.6] <- true
		string uBQ <- cw5
	end

'''
		expect = '''Program([FuncDecl(Id(lH), [VarDecl(Id(w8K), BoolType, None, None), VarDecl(Id(kt1), StringType, None, None)], Block([If(StringLit(Dy), AssignStmt(Id(Xq_j), Id(bvVp))), [(Id(YK), For(Id(MvZZ), NumLit(56.8), NumLit(22.81), Break)), (StringLit(y), VarDecl(Id(Y7Le), NumberType, None, None)), (NumLit(2.53), Break)], For(Id(vG6), BooleanLit(True), Id(R1), Return()), VarDecl(Id(boYj), ArrayType([50.6], NumberType), None, BooleanLit(True)), VarDecl(Id(uBQ), StringType, None, Id(cw5))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115363))

	def test_21530115364(self):
		input = '''
func bG0o (string npPZ[1.97])
	return

'''
		expect = '''Program([FuncDecl(Id(bG0o), [VarDecl(Id(npPZ), ArrayType([1.97], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115364))

	def test_21530115365(self):
		input = '''
bool fqg[24.7,79.52]
'''
		expect = '''Program([VarDecl(Id(fqg), ArrayType([24.7, 79.52], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115365))

	def test_21530115366(self):
		input = '''
func yyh (bool QAr, number G5O[52.55,35.82,96.04], string cPWX[9.13,51.38])	return

number wn[76.47]
dynamic Wc
'''
		expect = '''Program([FuncDecl(Id(yyh), [VarDecl(Id(QAr), BoolType, None, None), VarDecl(Id(G5O), ArrayType([52.55, 35.82, 96.04], NumberType), None, None), VarDecl(Id(cPWX), ArrayType([9.13, 51.38], StringType), None, None)], Return()), VarDecl(Id(wn), ArrayType([76.47], NumberType), None, None), VarDecl(Id(Wc), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115366))

	def test_21530115367(self):
		input = '''
string thCF <- "Tcv"
'''
		expect = '''Program([VarDecl(Id(thCF), StringType, None, StringLit(Tcv))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115367))

	def test_21530115368(self):
		input = '''
func YnRx (bool y0Sh, bool tFj)
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(YnRx), [VarDecl(Id(y0Sh), BoolType, None, None), VarDecl(Id(tFj), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115368))

	def test_21530115369(self):
		input = '''
func aud2 (string lA[65.59], bool n24f[5.79,50.73,99.84])
	begin
	end
string Vdc <- sL
func U1_ (bool SKn[58.05,30.32], number zY0s, string Eiz[51.52])	return false
number Ovg
func bQw ()	return

'''
		expect = '''Program([FuncDecl(Id(aud2), [VarDecl(Id(lA), ArrayType([65.59], StringType), None, None), VarDecl(Id(n24f), ArrayType([5.79, 50.73, 99.84], BoolType), None, None)], Block([])), VarDecl(Id(Vdc), StringType, None, Id(sL)), FuncDecl(Id(U1_), [VarDecl(Id(SKn), ArrayType([58.05, 30.32], BoolType), None, None), VarDecl(Id(zY0s), NumberType, None, None), VarDecl(Id(Eiz), ArrayType([51.52], StringType), None, None)], Return(BooleanLit(False))), VarDecl(Id(Ovg), NumberType, None, None), FuncDecl(Id(bQw), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115369))

	def test_21530115370(self):
		input = '''
string wOWJ[72.77,3.29]
func RM (bool bSp, number yy5, bool wjTc)
	begin
		bool T2O[1.83,84.68]
		zt3[43.49, false] <- "l"
		P0(true)
	end
var iSm <- 94.88
'''
		expect = '''Program([VarDecl(Id(wOWJ), ArrayType([72.77, 3.29], StringType), None, None), FuncDecl(Id(RM), [VarDecl(Id(bSp), BoolType, None, None), VarDecl(Id(yy5), NumberType, None, None), VarDecl(Id(wjTc), BoolType, None, None)], Block([VarDecl(Id(T2O), ArrayType([1.83, 84.68], BoolType), None, None), AssignStmt(ArrayCell(Id(zt3), [NumLit(43.49), BooleanLit(False)]), StringLit(l)), CallStmt(Id(P0), [BooleanLit(True)])])), VarDecl(Id(iSm), None, var, NumLit(94.88))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115370))

	def test_21530115371(self):
		input = '''
number hoUC <- true
'''
		expect = '''Program([VarDecl(Id(hoUC), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115371))

	def test_21530115372(self):
		input = '''
func ULeJ (bool T5X, bool Dd)	return uqL

'''
		expect = '''Program([FuncDecl(Id(ULeJ), [VarDecl(Id(T5X), BoolType, None, None), VarDecl(Id(Dd), BoolType, None, None)], Return(Id(uqL)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115372))

	def test_21530115373(self):
		input = '''
string ln
'''
		expect = '''Program([VarDecl(Id(ln), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115373))

	def test_21530115374(self):
		input = '''
func rdgQ (string lY, bool DxY[34.29])	return

dynamic gdD7
func Ir ()	return "qcPeb"
func bSh ()
	return
func zD ()
	return 27.18
'''
		expect = '''Program([FuncDecl(Id(rdgQ), [VarDecl(Id(lY), StringType, None, None), VarDecl(Id(DxY), ArrayType([34.29], BoolType), None, None)], Return()), VarDecl(Id(gdD7), None, dynamic, None), FuncDecl(Id(Ir), [], Return(StringLit(qcPeb))), FuncDecl(Id(bSh), [], Return()), FuncDecl(Id(zD), [], Return(NumLit(27.18)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115374))

	def test_21530115375(self):
		input = '''
string y8 <- "nwBt"
func N1ZW (number q7H[15.26,14.82,99.06])
	begin
		string KbxB <- g8M0
		if (90.53)
		continue
		elif (65.02)
		continue
	end
dynamic jmm <- 54.27
func E2IW (number Qr, number k2Y[63.5])
	return "hIb"

'''
		expect = '''Program([VarDecl(Id(y8), StringType, None, StringLit(nwBt)), FuncDecl(Id(N1ZW), [VarDecl(Id(q7H), ArrayType([15.26, 14.82, 99.06], NumberType), None, None)], Block([VarDecl(Id(KbxB), StringType, None, Id(g8M0)), If(NumLit(90.53), Continue), [(NumLit(65.02), Continue)], None])), VarDecl(Id(jmm), None, dynamic, NumLit(54.27)), FuncDecl(Id(E2IW), [VarDecl(Id(Qr), NumberType, None, None), VarDecl(Id(k2Y), ArrayType([63.5], NumberType), None, None)], Return(StringLit(hIb)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115375))

	def test_21530115376(self):
		input = '''
string v2h <- soz
'''
		expect = '''Program([VarDecl(Id(v2h), StringType, None, Id(soz))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115376))

	def test_21530115377(self):
		input = '''
func ByF (number HZJC)	begin
		continue
		begin
			vec <- false
			Li(sCW, true, false)
		end
		if (kdG)
		return
		elif (pDZg) qjen(false)
		elif (djV6)
		for rs until Wcp by 10.81
			yzL(ChbS)
		elif ("cy") dynamic yT <- 81.5
		elif (VQ) ft <- "Iefz"
		else begin
			if (81.62) string v1RL[19.21,71.25,27.26] <- UH
			else break
			bool sttZ
		end
	end
string h_[83.78,32.72,85.99]
func mBG ()	begin
	end

number pB_[7.79,37.17] <- YECV
'''
		expect = '''Program([FuncDecl(Id(ByF), [VarDecl(Id(HZJC), NumberType, None, None)], Block([Continue, Block([AssignStmt(Id(vec), BooleanLit(False)), CallStmt(Id(Li), [Id(sCW), BooleanLit(True), BooleanLit(False)])]), If(Id(kdG), Return()), [(Id(pDZg), CallStmt(Id(qjen), [BooleanLit(False)])), (Id(djV6), For(Id(rs), Id(Wcp), NumLit(10.81), CallStmt(Id(yzL), [Id(ChbS)]))), (StringLit(cy), VarDecl(Id(yT), None, dynamic, NumLit(81.5))), (Id(VQ), AssignStmt(Id(ft), StringLit(Iefz)))], Block([If(NumLit(81.62), VarDecl(Id(v1RL), ArrayType([19.21, 71.25, 27.26], StringType), None, Id(UH))), [], Break, VarDecl(Id(sttZ), BoolType, None, None)])])), VarDecl(Id(h_), ArrayType([83.78, 32.72, 85.99], StringType), None, None), FuncDecl(Id(mBG), [], Block([])), VarDecl(Id(pB_), ArrayType([7.79, 37.17], NumberType), None, Id(YECV))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115377))

	def test_21530115378(self):
		input = '''
bool Ox <- 0.93
func k9 ()
	begin
		if (x4) break
		elif (USqb)
		Y7ft <- false
		elif ("BDsJI")
		number Jr
		return "IEZ"
	end

bool MDH
'''
		expect = '''Program([VarDecl(Id(Ox), BoolType, None, NumLit(0.93)), FuncDecl(Id(k9), [], Block([If(Id(x4), Break), [(Id(USqb), AssignStmt(Id(Y7ft), BooleanLit(False))), (StringLit(BDsJI), VarDecl(Id(Jr), NumberType, None, None))], None, Return(StringLit(IEZ))])), VarDecl(Id(MDH), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115378))

	def test_21530115379(self):
		input = '''
func Su (number hxqU[86.77,47.91,23.84])	return 42.73
func zDU (bool RVY, string ZotW)
	return true

bool JPA4[8.98,37.99] <- 30.5
'''
		expect = '''Program([FuncDecl(Id(Su), [VarDecl(Id(hxqU), ArrayType([86.77, 47.91, 23.84], NumberType), None, None)], Return(NumLit(42.73))), FuncDecl(Id(zDU), [VarDecl(Id(RVY), BoolType, None, None), VarDecl(Id(ZotW), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(JPA4), ArrayType([8.98, 37.99], BoolType), None, NumLit(30.5))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115379))

	def test_21530115380(self):
		input = '''
func jmqI (number aN1M, number CDM[11.61,35.74,68.66])	begin
		continue
	end

func uUS (number Qwg, number jX[85.28,88.99,9.63])
	return
'''
		expect = '''Program([FuncDecl(Id(jmqI), [VarDecl(Id(aN1M), NumberType, None, None), VarDecl(Id(CDM), ArrayType([11.61, 35.74, 68.66], NumberType), None, None)], Block([Continue])), FuncDecl(Id(uUS), [VarDecl(Id(Qwg), NumberType, None, None), VarDecl(Id(jX), ArrayType([85.28, 88.99, 9.63], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115380))

	def test_21530115381(self):
		input = '''
bool BuW[62.94] <- "JnrTG"
bool pB[5.46]
func oPU (bool kXM0[63.6,0.79,13.89])	begin
		jV96[KnKf, true, "A"] <- QZO
		mWPj <- "lP"
		begin
			gSRc[jZm, 88.92, 71.82] <- false
		end
	end

func E2 ()	return false
string hf
'''
		expect = '''Program([VarDecl(Id(BuW), ArrayType([62.94], BoolType), None, StringLit(JnrTG)), VarDecl(Id(pB), ArrayType([5.46], BoolType), None, None), FuncDecl(Id(oPU), [VarDecl(Id(kXM0), ArrayType([63.6, 0.79, 13.89], BoolType), None, None)], Block([AssignStmt(ArrayCell(Id(jV96), [Id(KnKf), BooleanLit(True), StringLit(A)]), Id(QZO)), AssignStmt(Id(mWPj), StringLit(lP)), Block([AssignStmt(ArrayCell(Id(gSRc), [Id(jZm), NumLit(88.92), NumLit(71.82)]), BooleanLit(False))])])), FuncDecl(Id(E2), [], Return(BooleanLit(False))), VarDecl(Id(hf), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115381))

	def test_21530115382(self):
		input = '''
dynamic ng <- "QDNmq"
var f1 <- false
func de (number u2, number pdC[62.14], bool Fh0Y)	return
'''
		expect = '''Program([VarDecl(Id(ng), None, dynamic, StringLit(QDNmq)), VarDecl(Id(f1), None, var, BooleanLit(False)), FuncDecl(Id(de), [VarDecl(Id(u2), NumberType, None, None), VarDecl(Id(pdC), ArrayType([62.14], NumberType), None, None), VarDecl(Id(Fh0Y), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115382))

	def test_21530115383(self):
		input = '''
number Wur_[95.41] <- "FLp"
'''
		expect = '''Program([VarDecl(Id(Wur_), ArrayType([95.41], NumberType), None, StringLit(FLp))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115383))

	def test_21530115384(self):
		input = '''
func Qd (bool B2, bool YEU[40.34])	return
bool wqL[47.27,52.13,72.75]
'''
		expect = '''Program([FuncDecl(Id(Qd), [VarDecl(Id(B2), BoolType, None, None), VarDecl(Id(YEU), ArrayType([40.34], BoolType), None, None)], Return()), VarDecl(Id(wqL), ArrayType([47.27, 52.13, 72.75], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115384))

	def test_21530115385(self):
		input = '''
bool CTN[56.37] <- 25.68
'''
		expect = '''Program([VarDecl(Id(CTN), ArrayType([56.37], BoolType), None, NumLit(25.68))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115385))

	def test_21530115386(self):
		input = '''
func XY (string SXyw, number j7, bool ZNUL[64.78,69.59,37.11])
	return false
func Py (bool jcbx[50.8], number OWV[18.57,8.58])
	return "aiLh"
func I2qO (string vnA[30.68,81.63,73.39])
	begin
		ltPi["uef"] <- "uOVY"
		continue
		string dS
	end

'''
		expect = '''Program([FuncDecl(Id(XY), [VarDecl(Id(SXyw), StringType, None, None), VarDecl(Id(j7), NumberType, None, None), VarDecl(Id(ZNUL), ArrayType([64.78, 69.59, 37.11], BoolType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(Py), [VarDecl(Id(jcbx), ArrayType([50.8], BoolType), None, None), VarDecl(Id(OWV), ArrayType([18.57, 8.58], NumberType), None, None)], Return(StringLit(aiLh))), FuncDecl(Id(I2qO), [VarDecl(Id(vnA), ArrayType([30.68, 81.63, 73.39], StringType), None, None)], Block([AssignStmt(ArrayCell(Id(ltPi), [StringLit(uef)]), StringLit(uOVY)), Continue, VarDecl(Id(dS), StringType, None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115386))

	def test_21530115387(self):
		input = '''
func kH_e ()
	return
func cb (bool N_AH[21.85,40.37], bool Uw[41.18,48.55])	begin
		if ("chCp") break
		else for otyP until true by true
			return 57.05
		return dx6B
		IAOv <- dGqu
	end
'''
		expect = '''Program([FuncDecl(Id(kH_e), [], Return()), FuncDecl(Id(cb), [VarDecl(Id(N_AH), ArrayType([21.85, 40.37], BoolType), None, None), VarDecl(Id(Uw), ArrayType([41.18, 48.55], BoolType), None, None)], Block([If(StringLit(chCp), Break), [], For(Id(otyP), BooleanLit(True), BooleanLit(True), Return(NumLit(57.05))), Return(Id(dx6B)), AssignStmt(Id(IAOv), Id(dGqu))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115387))

	def test_21530115388(self):
		input = '''
func Yf (string HbWX[64.7,79.68,89.66])
	return
string h96 <- 93.77
func Ljiq (bool t8x[18.5,5.47])
	return

'''
		expect = '''Program([FuncDecl(Id(Yf), [VarDecl(Id(HbWX), ArrayType([64.7, 79.68, 89.66], StringType), None, None)], Return()), VarDecl(Id(h96), StringType, None, NumLit(93.77)), FuncDecl(Id(Ljiq), [VarDecl(Id(t8x), ArrayType([18.5, 5.47], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115388))

	def test_21530115389(self):
		input = '''
bool VkWn[9.47] <- w2E
number eU[39.79]
func qN ()	begin
		SR <- true
		break
		if ("rmBl")
		continue
		elif (PTMZ) m_C[r_] <- true
		elif ("mHjss")
		break
		elif (vS)
		begin
		end
		else U_G <- "g"
	end
'''
		expect = '''Program([VarDecl(Id(VkWn), ArrayType([9.47], BoolType), None, Id(w2E)), VarDecl(Id(eU), ArrayType([39.79], NumberType), None, None), FuncDecl(Id(qN), [], Block([AssignStmt(Id(SR), BooleanLit(True)), Break, If(StringLit(rmBl), Continue), [(Id(PTMZ), AssignStmt(ArrayCell(Id(m_C), [Id(r_)]), BooleanLit(True))), (StringLit(mHjss), Break), (Id(vS), Block([]))], AssignStmt(Id(U_G), StringLit(g))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115389))

	def test_21530115390(self):
		input = '''
string ThB8
bool TQz[96.86,14.09,68.2] <- "KER"
bool nr[80.0] <- "zmIQ"
func Qxy (string jf, number OdxU, string R7s)	begin
		DV <- true
		jy <- 38.72
	end

'''
		expect = '''Program([VarDecl(Id(ThB8), StringType, None, None), VarDecl(Id(TQz), ArrayType([96.86, 14.09, 68.2], BoolType), None, StringLit(KER)), VarDecl(Id(nr), ArrayType([80.0], BoolType), None, StringLit(zmIQ)), FuncDecl(Id(Qxy), [VarDecl(Id(jf), StringType, None, None), VarDecl(Id(OdxU), NumberType, None, None), VarDecl(Id(R7s), StringType, None, None)], Block([AssignStmt(Id(DV), BooleanLit(True)), AssignStmt(Id(jy), NumLit(38.72))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115390))

	def test_21530115391(self):
		input = '''
func fXdF ()	return Gfdg
func DE (string GWe, bool nYy[13.64,8.79,79.41], string hNqV[43.79,6.18,71.47])
	return MizF
func OH9 (number Hm[53.9,45.23], string eFtT, bool zFN4[30.4])
	return true
func vOZ ()	return
func wb ()
	begin
		for mK86 until 84.23 by true
			return 52.2
		bool aky[34.9]
	end
'''
		expect = '''Program([FuncDecl(Id(fXdF), [], Return(Id(Gfdg))), FuncDecl(Id(DE), [VarDecl(Id(GWe), StringType, None, None), VarDecl(Id(nYy), ArrayType([13.64, 8.79, 79.41], BoolType), None, None), VarDecl(Id(hNqV), ArrayType([43.79, 6.18, 71.47], StringType), None, None)], Return(Id(MizF))), FuncDecl(Id(OH9), [VarDecl(Id(Hm), ArrayType([53.9, 45.23], NumberType), None, None), VarDecl(Id(eFtT), StringType, None, None), VarDecl(Id(zFN4), ArrayType([30.4], BoolType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(vOZ), [], Return()), FuncDecl(Id(wb), [], Block([For(Id(mK86), NumLit(84.23), BooleanLit(True), Return(NumLit(52.2))), VarDecl(Id(aky), ArrayType([34.9], BoolType), None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115391))

	def test_21530115392(self):
		input = '''
bool Bn7[74.25,40.54,19.05]
bool fuXx <- 52.8
'''
		expect = '''Program([VarDecl(Id(Bn7), ArrayType([74.25, 40.54, 19.05], BoolType), None, None), VarDecl(Id(fuXx), BoolType, None, NumLit(52.8))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115392))

	def test_21530115393(self):
		input = '''
func kE2A (bool h7, bool Zex[93.65,69.05])
	return "eLPT"

'''
		expect = '''Program([FuncDecl(Id(kE2A), [VarDecl(Id(h7), BoolType, None, None), VarDecl(Id(Zex), ArrayType([93.65, 69.05], BoolType), None, None)], Return(StringLit(eLPT)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115393))

	def test_21530115394(self):
		input = '''
func tU (string kPE, string t11, number PR)
	return
'''
		expect = '''Program([FuncDecl(Id(tU), [VarDecl(Id(kPE), StringType, None, None), VarDecl(Id(t11), StringType, None, None), VarDecl(Id(PR), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115394))

	def test_21530115395(self):
		input = '''
bool EBS[42.18] <- HIDe
func MPJ ()
	begin
		begin
			break
			PWE[0.4, false] <- true
		end
	end
func AH (string dV5E[30.93], number QuGG)	return

number d4z
'''
		expect = '''Program([VarDecl(Id(EBS), ArrayType([42.18], BoolType), None, Id(HIDe)), FuncDecl(Id(MPJ), [], Block([Block([Break, AssignStmt(ArrayCell(Id(PWE), [NumLit(0.4), BooleanLit(False)]), BooleanLit(True))])])), FuncDecl(Id(AH), [VarDecl(Id(dV5E), ArrayType([30.93], StringType), None, None), VarDecl(Id(QuGG), NumberType, None, None)], Return()), VarDecl(Id(d4z), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115395))

	def test_21530115396(self):
		input = '''
bool GWUZ <- Z5R
'''
		expect = '''Program([VarDecl(Id(GWUZ), BoolType, None, Id(Z5R))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115396))

	def test_21530115397(self):
		input = '''
bool Dh8s[64.42,91.8] <- 11.78
string mno
func VlgK ()	return true
number zw[55.43] <- egqQ
'''
		expect = '''Program([VarDecl(Id(Dh8s), ArrayType([64.42, 91.8], BoolType), None, NumLit(11.78)), VarDecl(Id(mno), StringType, None, None), FuncDecl(Id(VlgK), [], Return(BooleanLit(True))), VarDecl(Id(zw), ArrayType([55.43], NumberType), None, Id(egqQ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115397))

	def test_21530115398(self):
		input = '''
number Fc[41.67,19.3,38.93]
string ojI5
'''
		expect = '''Program([VarDecl(Id(Fc), ArrayType([41.67, 19.3, 38.93], NumberType), None, None), VarDecl(Id(ojI5), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115398))

	def test_21530115399(self):
		input = '''
bool Zm[78.77]
'''
		expect = '''Program([VarDecl(Id(Zm), ArrayType([78.77], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115399))

	def test_21530115400(self):
		input = '''
dynamic AYy
var X6 <- 32.8
'''
		expect = '''Program([VarDecl(Id(AYy), None, dynamic, None), VarDecl(Id(X6), None, var, NumLit(32.8))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115400))

	def test_21530115401(self):
		input = '''
number eQ[66.8,13.37,70.04]
func YM (bool H3co[31.74])	return
func o2 (string rT8[47.77,85.2,39.09], string VE, string pB)	return

bool RI[83.96,45.22,49.18]
func XnP ()	return "KW"

'''
		expect = '''Program([VarDecl(Id(eQ), ArrayType([66.8, 13.37, 70.04], NumberType), None, None), FuncDecl(Id(YM), [VarDecl(Id(H3co), ArrayType([31.74], BoolType), None, None)], Return()), FuncDecl(Id(o2), [VarDecl(Id(rT8), ArrayType([47.77, 85.2, 39.09], StringType), None, None), VarDecl(Id(VE), StringType, None, None), VarDecl(Id(pB), StringType, None, None)], Return()), VarDecl(Id(RI), ArrayType([83.96, 45.22, 49.18], BoolType), None, None), FuncDecl(Id(XnP), [], Return(StringLit(KW)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115401))

	def test_21530115402(self):
		input = '''
func MRd (bool fsO, number tZa6)
	return
string uZbr <- "jxcP"
var QHxY <- 80.84
string Ujj[75.09,67.86] <- true
'''
		expect = '''Program([FuncDecl(Id(MRd), [VarDecl(Id(fsO), BoolType, None, None), VarDecl(Id(tZa6), NumberType, None, None)], Return()), VarDecl(Id(uZbr), StringType, None, StringLit(jxcP)), VarDecl(Id(QHxY), None, var, NumLit(80.84)), VarDecl(Id(Ujj), ArrayType([75.09, 67.86], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115402))

	def test_21530115403(self):
		input = '''
bool Vy[32.51,55.11,21.55] <- 59.32
func f6WY (number y7x1[84.91], number vm7[27.98,40.31])
	return 89.43

string Ei7[1.96]
func Yy ()	begin
		R3(false, CU7S)
		continue
	end
'''
		expect = '''Program([VarDecl(Id(Vy), ArrayType([32.51, 55.11, 21.55], BoolType), None, NumLit(59.32)), FuncDecl(Id(f6WY), [VarDecl(Id(y7x1), ArrayType([84.91], NumberType), None, None), VarDecl(Id(vm7), ArrayType([27.98, 40.31], NumberType), None, None)], Return(NumLit(89.43))), VarDecl(Id(Ei7), ArrayType([1.96], StringType), None, None), FuncDecl(Id(Yy), [], Block([CallStmt(Id(R3), [BooleanLit(False), Id(CU7S)]), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115403))

	def test_21530115404(self):
		input = '''
func xg (number HBG[0.57,12.48])
	begin
		bool TsLj <- 13.97
		for qtlJ until "HrE" by "Yq"
			Y5(true, false, true)
		begin
			CfV("Kdk", 67.79)
			return O9i
		end
	end
'''
		expect = '''Program([FuncDecl(Id(xg), [VarDecl(Id(HBG), ArrayType([0.57, 12.48], NumberType), None, None)], Block([VarDecl(Id(TsLj), BoolType, None, NumLit(13.97)), For(Id(qtlJ), StringLit(HrE), StringLit(Yq), CallStmt(Id(Y5), [BooleanLit(True), BooleanLit(False), BooleanLit(True)])), Block([CallStmt(Id(CfV), [StringLit(Kdk), NumLit(67.79)]), Return(Id(O9i))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115404))

	def test_21530115405(self):
		input = '''
func YnVm ()	return true

'''
		expect = '''Program([FuncDecl(Id(YnVm), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115405))

	def test_21530115406(self):
		input = '''
func SWOC ()	begin
		xMY6 <- true
	end

func wtcH ()	begin
		r3h <- "Zrsl"
		number d5Qa
		for ft until O5a by 83.07
			bool pUZe <- 73.24
	end

func vIK ()	return
'''
		expect = '''Program([FuncDecl(Id(SWOC), [], Block([AssignStmt(Id(xMY6), BooleanLit(True))])), FuncDecl(Id(wtcH), [], Block([AssignStmt(Id(r3h), StringLit(Zrsl)), VarDecl(Id(d5Qa), NumberType, None, None), For(Id(ft), Id(O5a), NumLit(83.07), VarDecl(Id(pUZe), BoolType, None, NumLit(73.24)))])), FuncDecl(Id(vIK), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115406))

	def test_21530115407(self):
		input = '''
bool NLP[7.33,8.76,86.09] <- 88.16
string ct[56.63] <- lr
func y5 (number RZEo, string LAJT)	return
number yw8H
string aHLv[9.76] <- 24.7
'''
		expect = '''Program([VarDecl(Id(NLP), ArrayType([7.33, 8.76, 86.09], BoolType), None, NumLit(88.16)), VarDecl(Id(ct), ArrayType([56.63], StringType), None, Id(lr)), FuncDecl(Id(y5), [VarDecl(Id(RZEo), NumberType, None, None), VarDecl(Id(LAJT), StringType, None, None)], Return()), VarDecl(Id(yw8H), NumberType, None, None), VarDecl(Id(aHLv), ArrayType([9.76], StringType), None, NumLit(24.7))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115407))

	def test_21530115408(self):
		input = '''
func Um ()
	return false
number FS
func MCO ()	begin
		VJ3[55.7] <- true
		bool Gn[41.86,47.37] <- false
	end

func sgD (bool WkH[82.93,54.74,79.1], string xk)	return true
number Pp0Y
'''
		expect = '''Program([FuncDecl(Id(Um), [], Return(BooleanLit(False))), VarDecl(Id(FS), NumberType, None, None), FuncDecl(Id(MCO), [], Block([AssignStmt(ArrayCell(Id(VJ3), [NumLit(55.7)]), BooleanLit(True)), VarDecl(Id(Gn), ArrayType([41.86, 47.37], BoolType), None, BooleanLit(False))])), FuncDecl(Id(sgD), [VarDecl(Id(WkH), ArrayType([82.93, 54.74, 79.1], BoolType), None, None), VarDecl(Id(xk), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(Pp0Y), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115408))

	def test_21530115409(self):
		input = '''
number GQ0[43.84,54.87,13.95]
func NEMa (bool mN[75.85,32.6,98.17], number cMhn, bool ql[56.24,88.45,26.33])	return "elhC"

number b5ng[28.74,39.53] <- 92.05
'''
		expect = '''Program([VarDecl(Id(GQ0), ArrayType([43.84, 54.87, 13.95], NumberType), None, None), FuncDecl(Id(NEMa), [VarDecl(Id(mN), ArrayType([75.85, 32.6, 98.17], BoolType), None, None), VarDecl(Id(cMhn), NumberType, None, None), VarDecl(Id(ql), ArrayType([56.24, 88.45, 26.33], BoolType), None, None)], Return(StringLit(elhC))), VarDecl(Id(b5ng), ArrayType([28.74, 39.53], NumberType), None, NumLit(92.05))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115409))

	def test_21530115410(self):
		input = '''
number LYJ7
func tA (string Plp, number V6H)	return
var Wg <- mznd
bool FQp
func StNE ()	return GH
'''
		expect = '''Program([VarDecl(Id(LYJ7), NumberType, None, None), FuncDecl(Id(tA), [VarDecl(Id(Plp), StringType, None, None), VarDecl(Id(V6H), NumberType, None, None)], Return()), VarDecl(Id(Wg), None, var, Id(mznd)), VarDecl(Id(FQp), BoolType, None, None), FuncDecl(Id(StNE), [], Return(Id(GH)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115410))

	def test_21530115411(self):
		input = '''
func TEA (string qok, bool bi, bool nl[34.16])
	return r7vK
number NM1[48.85]
func Um (bool ghv[9.68,47.14,20.97])
	return

func B5aY (number bB[46.02])
	return old

'''
		expect = '''Program([FuncDecl(Id(TEA), [VarDecl(Id(qok), StringType, None, None), VarDecl(Id(bi), BoolType, None, None), VarDecl(Id(nl), ArrayType([34.16], BoolType), None, None)], Return(Id(r7vK))), VarDecl(Id(NM1), ArrayType([48.85], NumberType), None, None), FuncDecl(Id(Um), [VarDecl(Id(ghv), ArrayType([9.68, 47.14, 20.97], BoolType), None, None)], Return()), FuncDecl(Id(B5aY), [VarDecl(Id(bB), ArrayType([46.02], NumberType), None, None)], Return(Id(old)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115411))

	def test_21530115412(self):
		input = '''
func ZgvF (string efJ6)	return true

number OLl[6.54,53.19]
string tbz[12.68,76.12,1.08] <- false
func Upa (number AWSt, string w_[29.29,19.81,76.96])	begin
		break
		continue
	end

number V6g[12.71,86.85]
'''
		expect = '''Program([FuncDecl(Id(ZgvF), [VarDecl(Id(efJ6), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(OLl), ArrayType([6.54, 53.19], NumberType), None, None), VarDecl(Id(tbz), ArrayType([12.68, 76.12, 1.08], StringType), None, BooleanLit(False)), FuncDecl(Id(Upa), [VarDecl(Id(AWSt), NumberType, None, None), VarDecl(Id(w_), ArrayType([29.29, 19.81, 76.96], StringType), None, None)], Block([Break, Continue])), VarDecl(Id(V6g), ArrayType([12.71, 86.85], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115412))

	def test_21530115413(self):
		input = '''
func IM (string WJlb[37.89,11.42], string tRfv, number cUG[78.85,6.26,29.47])	begin
		return Qf_
		bRtP[svl, tkV] <- true
		plVA <- 72.69
	end
'''
		expect = '''Program([FuncDecl(Id(IM), [VarDecl(Id(WJlb), ArrayType([37.89, 11.42], StringType), None, None), VarDecl(Id(tRfv), StringType, None, None), VarDecl(Id(cUG), ArrayType([78.85, 6.26, 29.47], NumberType), None, None)], Block([Return(Id(Qf_)), AssignStmt(ArrayCell(Id(bRtP), [Id(svl), Id(tkV)]), BooleanLit(True)), AssignStmt(Id(plVA), NumLit(72.69))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115413))

	def test_21530115414(self):
		input = '''
bool poI[99.65]
func dm5V (string ugJ)
	begin
		for pz until CO by false
			return 53.25
	end

func Zg0w ()	begin
		break
		for Kko4 until oSe by "sq"
			break
		begin
			break
		end
	end
func WmFT (number JoT, number CV, string PPg)
	return 80.36
func Cz (string nC, bool Rq, bool OFg)	return 69.0
'''
		expect = '''Program([VarDecl(Id(poI), ArrayType([99.65], BoolType), None, None), FuncDecl(Id(dm5V), [VarDecl(Id(ugJ), StringType, None, None)], Block([For(Id(pz), Id(CO), BooleanLit(False), Return(NumLit(53.25)))])), FuncDecl(Id(Zg0w), [], Block([Break, For(Id(Kko4), Id(oSe), StringLit(sq), Break), Block([Break])])), FuncDecl(Id(WmFT), [VarDecl(Id(JoT), NumberType, None, None), VarDecl(Id(CV), NumberType, None, None), VarDecl(Id(PPg), StringType, None, None)], Return(NumLit(80.36))), FuncDecl(Id(Cz), [VarDecl(Id(nC), StringType, None, None), VarDecl(Id(Rq), BoolType, None, None), VarDecl(Id(OFg), BoolType, None, None)], Return(NumLit(69.0)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115414))

	def test_21530115415(self):
		input = '''
func rNw (number vh)
	return "bq"

func rrT (number R49, bool jxd[45.95,70.33])	return uJ

func dvE ()	begin
		begin
		end
		D_ <- MC
		begin
			break
		end
	end

'''
		expect = '''Program([FuncDecl(Id(rNw), [VarDecl(Id(vh), NumberType, None, None)], Return(StringLit(bq))), FuncDecl(Id(rrT), [VarDecl(Id(R49), NumberType, None, None), VarDecl(Id(jxd), ArrayType([45.95, 70.33], BoolType), None, None)], Return(Id(uJ))), FuncDecl(Id(dvE), [], Block([Block([]), AssignStmt(Id(D_), Id(MC)), Block([Break])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115415))

	def test_21530115416(self):
		input = '''
func OM2 ()	return ApU

func DYT ()
	begin
		break
		continue
	end
'''
		expect = '''Program([FuncDecl(Id(OM2), [], Return(Id(ApU))), FuncDecl(Id(DYT), [], Block([Break, Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115416))

	def test_21530115417(self):
		input = '''
func W3Bl (number wt0K)	begin
		if (false)
		break
		else bool EIn[59.9] <- false
	end

number Xk3L[92.68,32.96]
'''
		expect = '''Program([FuncDecl(Id(W3Bl), [VarDecl(Id(wt0K), NumberType, None, None)], Block([If(BooleanLit(False), Break), [], VarDecl(Id(EIn), ArrayType([59.9], BoolType), None, BooleanLit(False))])), VarDecl(Id(Xk3L), ArrayType([92.68, 32.96], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115417))

	def test_21530115418(self):
		input = '''
func PT (string C_n8)
	return false
func ym (string SxW, number xab[66.22,10.01])
	return

'''
		expect = '''Program([FuncDecl(Id(PT), [VarDecl(Id(C_n8), StringType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(ym), [VarDecl(Id(SxW), StringType, None, None), VarDecl(Id(xab), ArrayType([66.22, 10.01], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115418))

	def test_21530115419(self):
		input = '''
var jeqO <- "DAZh"
string m3H[76.31] <- TwJ
'''
		expect = '''Program([VarDecl(Id(jeqO), None, var, StringLit(DAZh)), VarDecl(Id(m3H), ArrayType([76.31], StringType), None, Id(TwJ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115419))

	def test_21530115420(self):
		input = '''
func Vf2 (number FJ9[92.08], number J8[62.86,69.05])	return

func wRe (number Waw, string ZPz[80.06], bool LK)	return
var DDw <- 82.0
bool RHk9 <- 9.55
func Ayj (string So5[20.75,66.66], string Q7H)
	return false

'''
		expect = '''Program([FuncDecl(Id(Vf2), [VarDecl(Id(FJ9), ArrayType([92.08], NumberType), None, None), VarDecl(Id(J8), ArrayType([62.86, 69.05], NumberType), None, None)], Return()), FuncDecl(Id(wRe), [VarDecl(Id(Waw), NumberType, None, None), VarDecl(Id(ZPz), ArrayType([80.06], StringType), None, None), VarDecl(Id(LK), BoolType, None, None)], Return()), VarDecl(Id(DDw), None, var, NumLit(82.0)), VarDecl(Id(RHk9), BoolType, None, NumLit(9.55)), FuncDecl(Id(Ayj), [VarDecl(Id(So5), ArrayType([20.75, 66.66], StringType), None, None), VarDecl(Id(Q7H), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115420))

	def test_21530115421(self):
		input = '''
bool EN
string axlq[75.64,8.27] <- orcU
dynamic Mj <- "TOFo"
func dx (string Mc[40.61,57.66], string Y6)	begin
		continue
		begin
			break
			begin
			end
		end
	end
func tY ()	return
'''
		expect = '''Program([VarDecl(Id(EN), BoolType, None, None), VarDecl(Id(axlq), ArrayType([75.64, 8.27], StringType), None, Id(orcU)), VarDecl(Id(Mj), None, dynamic, StringLit(TOFo)), FuncDecl(Id(dx), [VarDecl(Id(Mc), ArrayType([40.61, 57.66], StringType), None, None), VarDecl(Id(Y6), StringType, None, None)], Block([Continue, Block([Break, Block([])])])), FuncDecl(Id(tY), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115421))

	def test_21530115422(self):
		input = '''
bool RZ <- false
'''
		expect = '''Program([VarDecl(Id(RZ), BoolType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115422))

	def test_21530115423(self):
		input = '''
string VF <- true
'''
		expect = '''Program([VarDecl(Id(VF), StringType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115423))

	def test_21530115424(self):
		input = '''
func xT6j ()
	return
number z0[15.11,2.37,65.12]
'''
		expect = '''Program([FuncDecl(Id(xT6j), [], Return()), VarDecl(Id(z0), ArrayType([15.11, 2.37, 65.12], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115424))

	def test_21530115425(self):
		input = '''
string kyW[22.94,5.06,91.43] <- 39.18
number dgEV[84.76] <- uo
'''
		expect = '''Program([VarDecl(Id(kyW), ArrayType([22.94, 5.06, 91.43], StringType), None, NumLit(39.18)), VarDecl(Id(dgEV), ArrayType([84.76], NumberType), None, Id(uo))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115425))

	def test_21530115426(self):
		input = '''
number ju[40.67,53.55,5.33] <- "V"
'''
		expect = '''Program([VarDecl(Id(ju), ArrayType([40.67, 53.55, 5.33], NumberType), None, StringLit(V))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115426))

	def test_21530115427(self):
		input = '''
func GY8r (number Syk)
	return "HNdhM"

string hWt <- "dKStz"
func uI6N (bool zyu)	return

'''
		expect = '''Program([FuncDecl(Id(GY8r), [VarDecl(Id(Syk), NumberType, None, None)], Return(StringLit(HNdhM))), VarDecl(Id(hWt), StringType, None, StringLit(dKStz)), FuncDecl(Id(uI6N), [VarDecl(Id(zyu), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115427))

	def test_21530115428(self):
		input = '''
string opV[24.3,13.46,17.61] <- "b"
string Ai3 <- 42.72
func OL8 (string Yb[91.8,67.16], number ruW, bool OK[79.1,96.12])
	return 93.86
'''
		expect = '''Program([VarDecl(Id(opV), ArrayType([24.3, 13.46, 17.61], StringType), None, StringLit(b)), VarDecl(Id(Ai3), StringType, None, NumLit(42.72)), FuncDecl(Id(OL8), [VarDecl(Id(Yb), ArrayType([91.8, 67.16], StringType), None, None), VarDecl(Id(ruW), NumberType, None, None), VarDecl(Id(OK), ArrayType([79.1, 96.12], BoolType), None, None)], Return(NumLit(93.86)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115428))

	def test_21530115429(self):
		input = '''
func koL (string GnJ[79.13,78.52])	begin
		continue
	end
func kpP (string P9[17.48,54.83], number Jfd, number ccRR)	return 6.23

string SEt[89.23,16.83,74.45]
'''
		expect = '''Program([FuncDecl(Id(koL), [VarDecl(Id(GnJ), ArrayType([79.13, 78.52], StringType), None, None)], Block([Continue])), FuncDecl(Id(kpP), [VarDecl(Id(P9), ArrayType([17.48, 54.83], StringType), None, None), VarDecl(Id(Jfd), NumberType, None, None), VarDecl(Id(ccRR), NumberType, None, None)], Return(NumLit(6.23))), VarDecl(Id(SEt), ArrayType([89.23, 16.83, 74.45], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115429))

	def test_21530115430(self):
		input = '''
func oZ4a (number XYa)
	begin
	end
func J2k (number VT[62.42], string x4, number gy)	return

func pOo (number r0, bool s6)
	begin
		for LZ until iys by 67.4
			if ("KGdBH") for EXk until "Nxv" by false
				for z8K until "OCHg" by false
					begin
						Nxhi <- at
						dcRK <- "tNp"
					end
			elif (false)
			if (DL8) if (false) if (DB) if ("VRTU")
			for BQ until "zi" by QSn
				continue
			elif (70.05) break
			elif (true) string Hps[60.76,43.23] <- false
			elif (70.08) continue
			elif ("JlUc")
			break
			else break
			elif (yR) begin
			end
			elif (sb)
			string pdl5
			elif ("Vqg") return
			elif (71.62) break
			elif (true) continue
			else Br1S(40.24, E4, "YiVRI")
			elif (63.19) FbB <- 57.35
			elif (27.52)
			return true
			elif ("xtnk") number Ut[29.44,72.92] <- true
			else uVF <- true
	end

'''
		expect = '''Program([FuncDecl(Id(oZ4a), [VarDecl(Id(XYa), NumberType, None, None)], Block([])), FuncDecl(Id(J2k), [VarDecl(Id(VT), ArrayType([62.42], NumberType), None, None), VarDecl(Id(x4), StringType, None, None), VarDecl(Id(gy), NumberType, None, None)], Return()), FuncDecl(Id(pOo), [VarDecl(Id(r0), NumberType, None, None), VarDecl(Id(s6), BoolType, None, None)], Block([For(Id(LZ), Id(iys), NumLit(67.4), If(StringLit(KGdBH), For(Id(EXk), StringLit(Nxv), BooleanLit(False), For(Id(z8K), StringLit(OCHg), BooleanLit(False), Block([AssignStmt(Id(Nxhi), Id(at)), AssignStmt(Id(dcRK), StringLit(tNp))])))), [(BooleanLit(False), If(Id(DL8), If(BooleanLit(False), If(Id(DB), If(StringLit(VRTU), For(Id(BQ), StringLit(zi), Id(QSn), Continue)), [(NumLit(70.05), Break), (BooleanLit(True), VarDecl(Id(Hps), ArrayType([60.76, 43.23], StringType), None, BooleanLit(False))), (NumLit(70.08), Continue), (StringLit(JlUc), Break)], Break), [(Id(yR), Block([])), (Id(sb), VarDecl(Id(pdl5), StringType, None, None)), (StringLit(Vqg), Return()), (NumLit(71.62), Break), (BooleanLit(True), Continue)], CallStmt(Id(Br1S), [NumLit(40.24), Id(E4), StringLit(YiVRI)])), [(NumLit(63.19), AssignStmt(Id(FbB), NumLit(57.35))), (NumLit(27.52), Return(BooleanLit(True)))], None), [], None), (StringLit(xtnk), VarDecl(Id(Ut), ArrayType([29.44, 72.92], NumberType), None, BooleanLit(True)))], AssignStmt(Id(uVF), BooleanLit(True)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115430))

	def test_21530115431(self):
		input = '''
var OO7Z <- true
'''
		expect = '''Program([VarDecl(Id(OO7Z), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115431))

	def test_21530115432(self):
		input = '''
func zy8 (number cUt, string CWoq[48.91], string N3[83.03,55.39,21.09])
	begin
		return "AP"
		if ("etB") q4Ud(DjR, 52.57, 74.76)
		elif ("wsyX")
		break
		elif ("ymHPf") if (40.96) T0(c98)
		elif (51.01)
		if (false) if (13.7) Jd["nHfX", "q"] <- Hf
		elif ("mnBh") dynamic DUA <- "ISNq"
		else break
		elif (true) return 17.98
		elif (false) ElS(94.73)
		else break
		elif (82.02)
		return 16.9
		elif (false)
		if (e_T)
		continue
		elif (XP6) wl(YhL3, "zjE", false)
		elif (96.85) break
		elif (false)
		for RTD_ until 91.61 by 16.71
			dynamic Mhs
		elif (false)
		begin
			return 42.1
		end
		elif (true) continue
		else number Wa[32.69,52.98]
		else break
	end
'''
		expect = '''Program([FuncDecl(Id(zy8), [VarDecl(Id(cUt), NumberType, None, None), VarDecl(Id(CWoq), ArrayType([48.91], StringType), None, None), VarDecl(Id(N3), ArrayType([83.03, 55.39, 21.09], StringType), None, None)], Block([Return(StringLit(AP)), If(StringLit(etB), CallStmt(Id(q4Ud), [Id(DjR), NumLit(52.57), NumLit(74.76)])), [(StringLit(wsyX), Break), (StringLit(ymHPf), If(NumLit(40.96), CallStmt(Id(T0), [Id(c98)])), [(NumLit(51.01), If(BooleanLit(False), If(NumLit(13.7), AssignStmt(ArrayCell(Id(Jd), [StringLit(nHfX), StringLit(q)]), Id(Hf))), [(StringLit(mnBh), VarDecl(Id(DUA), None, dynamic, StringLit(ISNq)))], Break), [(BooleanLit(True), Return(NumLit(17.98))), (BooleanLit(False), CallStmt(Id(ElS), [NumLit(94.73)]))], Break), (NumLit(82.02), Return(NumLit(16.9)))], None), (BooleanLit(False), If(Id(e_T), Continue), [(Id(XP6), CallStmt(Id(wl), [Id(YhL3), StringLit(zjE), BooleanLit(False)])), (NumLit(96.85), Break), (BooleanLit(False), For(Id(RTD_), NumLit(91.61), NumLit(16.71), VarDecl(Id(Mhs), None, dynamic, None))), (BooleanLit(False), Block([Return(NumLit(42.1))])), (BooleanLit(True), Continue)], VarDecl(Id(Wa), ArrayType([32.69, 52.98], NumberType), None, None))], Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115432))

	def test_21530115433(self):
		input = '''
number Pn <- 84.34
func hVQ (bool ng, string gM, string Pi)	begin
		qw <- "dV"
	end

func EFT (string D4MB, string P6S[95.44,74.67,80.0], bool XqkF[55.97,68.04,76.86])
	return
func fqr (number lCR_, number vXw)	begin
		return lIB
	end
func IqyP (bool sx4d[74.8])
	return 67.27
'''
		expect = '''Program([VarDecl(Id(Pn), NumberType, None, NumLit(84.34)), FuncDecl(Id(hVQ), [VarDecl(Id(ng), BoolType, None, None), VarDecl(Id(gM), StringType, None, None), VarDecl(Id(Pi), StringType, None, None)], Block([AssignStmt(Id(qw), StringLit(dV))])), FuncDecl(Id(EFT), [VarDecl(Id(D4MB), StringType, None, None), VarDecl(Id(P6S), ArrayType([95.44, 74.67, 80.0], StringType), None, None), VarDecl(Id(XqkF), ArrayType([55.97, 68.04, 76.86], BoolType), None, None)], Return()), FuncDecl(Id(fqr), [VarDecl(Id(lCR_), NumberType, None, None), VarDecl(Id(vXw), NumberType, None, None)], Block([Return(Id(lIB))])), FuncDecl(Id(IqyP), [VarDecl(Id(sx4d), ArrayType([74.8], BoolType), None, None)], Return(NumLit(67.27)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115433))

	def test_21530115434(self):
		input = '''
func s_ (number PIL, string Mbr[89.24], bool Zwa[38.56,96.28,88.08])	begin
	end
func Yi3 (number JHh, number lfcB, bool Hx3)	return
'''
		expect = '''Program([FuncDecl(Id(s_), [VarDecl(Id(PIL), NumberType, None, None), VarDecl(Id(Mbr), ArrayType([89.24], StringType), None, None), VarDecl(Id(Zwa), ArrayType([38.56, 96.28, 88.08], BoolType), None, None)], Block([])), FuncDecl(Id(Yi3), [VarDecl(Id(JHh), NumberType, None, None), VarDecl(Id(lfcB), NumberType, None, None), VarDecl(Id(Hx3), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115434))

	def test_21530115435(self):
		input = '''
dynamic Lm <- "yJ"
'''
		expect = '''Program([VarDecl(Id(Lm), None, dynamic, StringLit(yJ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115435))

	def test_21530115436(self):
		input = '''
func bsiD (string x5)
	return 66.1
func SNn ()
	return
'''
		expect = '''Program([FuncDecl(Id(bsiD), [VarDecl(Id(x5), StringType, None, None)], Return(NumLit(66.1))), FuncDecl(Id(SNn), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115436))

	def test_21530115437(self):
		input = '''
func ZFE ()	begin
		dynamic MIp <- false
	end
'''
		expect = '''Program([FuncDecl(Id(ZFE), [], Block([VarDecl(Id(MIp), None, dynamic, BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115437))

	def test_21530115438(self):
		input = '''
bool Cm[61.57]
'''
		expect = '''Program([VarDecl(Id(Cm), ArrayType([61.57], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115438))

	def test_21530115439(self):
		input = '''
bool vcOg
'''
		expect = '''Program([VarDecl(Id(vcOg), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115439))

	def test_21530115440(self):
		input = '''
bool SO[27.29,78.36,43.9]
func GB (bool j08[94.62], bool Mf36[44.81], string Aelk)	return 69.25
func IXIb (bool Sf[34.49], bool ZCMk[58.03])	return

'''
		expect = '''Program([VarDecl(Id(SO), ArrayType([27.29, 78.36, 43.9], BoolType), None, None), FuncDecl(Id(GB), [VarDecl(Id(j08), ArrayType([94.62], BoolType), None, None), VarDecl(Id(Mf36), ArrayType([44.81], BoolType), None, None), VarDecl(Id(Aelk), StringType, None, None)], Return(NumLit(69.25))), FuncDecl(Id(IXIb), [VarDecl(Id(Sf), ArrayType([34.49], BoolType), None, None), VarDecl(Id(ZCMk), ArrayType([58.03], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115440))

	def test_21530115441(self):
		input = '''
func Q2LB ()
	begin
	end

func wcgD (number Fgg[26.61,36.44], bool gZw[61.42,10.47,69.19])	begin
		return
		return ILY3
	end
string WL7[4.86,23.52,15.57]
number iI[85.91,2.77]
func aJ (number iK[80.01,5.5,50.12], bool iLX)
	return
'''
		expect = '''Program([FuncDecl(Id(Q2LB), [], Block([])), FuncDecl(Id(wcgD), [VarDecl(Id(Fgg), ArrayType([26.61, 36.44], NumberType), None, None), VarDecl(Id(gZw), ArrayType([61.42, 10.47, 69.19], BoolType), None, None)], Block([Return(), Return(Id(ILY3))])), VarDecl(Id(WL7), ArrayType([4.86, 23.52, 15.57], StringType), None, None), VarDecl(Id(iI), ArrayType([85.91, 2.77], NumberType), None, None), FuncDecl(Id(aJ), [VarDecl(Id(iK), ArrayType([80.01, 5.5, 50.12], NumberType), None, None), VarDecl(Id(iLX), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115441))

	def test_21530115442(self):
		input = '''
func Qd5 (number oh[6.69])	begin
	end

'''
		expect = '''Program([FuncDecl(Id(Qd5), [VarDecl(Id(oh), ArrayType([6.69], NumberType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115442))

	def test_21530115443(self):
		input = '''
number R4Bp <- false
bool Ov2e <- 15.92
string dr0
'''
		expect = '''Program([VarDecl(Id(R4Bp), NumberType, None, BooleanLit(False)), VarDecl(Id(Ov2e), BoolType, None, NumLit(15.92)), VarDecl(Id(dr0), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115443))

	def test_21530115444(self):
		input = '''
bool Uj[28.9,19.72,62.29]
func UT (number Di[61.14,34.13], string HbB[44.99,26.43,72.66], string UNdB)	return lq
func Li ()	return
'''
		expect = '''Program([VarDecl(Id(Uj), ArrayType([28.9, 19.72, 62.29], BoolType), None, None), FuncDecl(Id(UT), [VarDecl(Id(Di), ArrayType([61.14, 34.13], NumberType), None, None), VarDecl(Id(HbB), ArrayType([44.99, 26.43, 72.66], StringType), None, None), VarDecl(Id(UNdB), StringType, None, None)], Return(Id(lq))), FuncDecl(Id(Li), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115444))

	def test_21530115445(self):
		input = '''
func Ajw (number vSSK[30.49,39.48], number vDw[24.26], bool mq02[61.79,61.7,52.0])	begin
	end
func x5 (string mHw)	return
func Eq0a (string NlU[57.06,60.57,43.14], bool iJfn, string r0k)
	return "KPk"

number ylad[24.17] <- "NIgME"
'''
		expect = '''Program([FuncDecl(Id(Ajw), [VarDecl(Id(vSSK), ArrayType([30.49, 39.48], NumberType), None, None), VarDecl(Id(vDw), ArrayType([24.26], NumberType), None, None), VarDecl(Id(mq02), ArrayType([61.79, 61.7, 52.0], BoolType), None, None)], Block([])), FuncDecl(Id(x5), [VarDecl(Id(mHw), StringType, None, None)], Return()), FuncDecl(Id(Eq0a), [VarDecl(Id(NlU), ArrayType([57.06, 60.57, 43.14], StringType), None, None), VarDecl(Id(iJfn), BoolType, None, None), VarDecl(Id(r0k), StringType, None, None)], Return(StringLit(KPk))), VarDecl(Id(ylad), ArrayType([24.17], NumberType), None, StringLit(NIgME))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115445))

	def test_21530115446(self):
		input = '''
func jRD (number yDF)	begin
	end
string QsnF[22.45,32.99,22.39] <- uIeK
'''
		expect = '''Program([FuncDecl(Id(jRD), [VarDecl(Id(yDF), NumberType, None, None)], Block([])), VarDecl(Id(QsnF), ArrayType([22.45, 32.99, 22.39], StringType), None, Id(uIeK))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115446))

	def test_21530115447(self):
		input = '''
bool dAh <- azJ
'''
		expect = '''Program([VarDecl(Id(dAh), BoolType, None, Id(azJ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115447))

	def test_21530115448(self):
		input = '''
func ES (bool x7[7.96,95.74], string VFv[36.11], number Uz[95.46,46.84,36.14])	return
'''
		expect = '''Program([FuncDecl(Id(ES), [VarDecl(Id(x7), ArrayType([7.96, 95.74], BoolType), None, None), VarDecl(Id(VFv), ArrayType([36.11], StringType), None, None), VarDecl(Id(Uz), ArrayType([95.46, 46.84, 36.14], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115448))

	def test_21530115449(self):
		input = '''
var fdmd <- 43.32
func qO5 (bool OaM2)	return true

number FW[4.76,91.85,9.46] <- 34.38
func Nlma (bool gIQ6[34.99,49.65], number ER)
	begin
	end
string iB[9.89,28.92,14.77] <- 98.44
'''
		expect = '''Program([VarDecl(Id(fdmd), None, var, NumLit(43.32)), FuncDecl(Id(qO5), [VarDecl(Id(OaM2), BoolType, None, None)], Return(BooleanLit(True))), VarDecl(Id(FW), ArrayType([4.76, 91.85, 9.46], NumberType), None, NumLit(34.38)), FuncDecl(Id(Nlma), [VarDecl(Id(gIQ6), ArrayType([34.99, 49.65], BoolType), None, None), VarDecl(Id(ER), NumberType, None, None)], Block([])), VarDecl(Id(iB), ArrayType([9.89, 28.92, 14.77], StringType), None, NumLit(98.44))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115449))

	def test_21530115450(self):
		input = '''
func Sy ()
	return
number TfS <- true
'''
		expect = '''Program([FuncDecl(Id(Sy), [], Return()), VarDecl(Id(TfS), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115450))

	def test_21530115451(self):
		input = '''
string hV8M
'''
		expect = '''Program([VarDecl(Id(hV8M), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115451))

	def test_21530115452(self):
		input = '''
func l1 (bool Tx6[57.54,47.46], bool II, string Rd7N[62.97])	begin
		if (true) wE(true)
		elif (4.46) return
		elif (false) break
		bool nlro[25.8]
		begin
			continue
		end
	end
func Tx ()
	return
string eXTh
'''
		expect = '''Program([FuncDecl(Id(l1), [VarDecl(Id(Tx6), ArrayType([57.54, 47.46], BoolType), None, None), VarDecl(Id(II), BoolType, None, None), VarDecl(Id(Rd7N), ArrayType([62.97], StringType), None, None)], Block([If(BooleanLit(True), CallStmt(Id(wE), [BooleanLit(True)])), [(NumLit(4.46), Return()), (BooleanLit(False), Break)], None, VarDecl(Id(nlro), ArrayType([25.8], BoolType), None, None), Block([Continue])])), FuncDecl(Id(Tx), [], Return()), VarDecl(Id(eXTh), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115452))

	def test_21530115453(self):
		input = '''
number Gi
number hQJP[1.65,27.4,9.35]
'''
		expect = '''Program([VarDecl(Id(Gi), NumberType, None, None), VarDecl(Id(hQJP), ArrayType([1.65, 27.4, 9.35], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115453))

	def test_21530115454(self):
		input = '''
number Kq2[22.14] <- 15.39
'''
		expect = '''Program([VarDecl(Id(Kq2), ArrayType([22.14], NumberType), None, NumLit(15.39))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115454))

	def test_21530115455(self):
		input = '''
string lP[1.44]
func wJXg (string jA4[33.27,15.96], bool NZcQ)
	begin
		continue
	end
func L11G (number i3p)
	return

func ULku (bool P_Yd[96.72,32.06], string RUkz[87.48,8.62,19.45])	return

func s0y (number gS[48.82,74.05], number fVSV)	return
'''
		expect = '''Program([VarDecl(Id(lP), ArrayType([1.44], StringType), None, None), FuncDecl(Id(wJXg), [VarDecl(Id(jA4), ArrayType([33.27, 15.96], StringType), None, None), VarDecl(Id(NZcQ), BoolType, None, None)], Block([Continue])), FuncDecl(Id(L11G), [VarDecl(Id(i3p), NumberType, None, None)], Return()), FuncDecl(Id(ULku), [VarDecl(Id(P_Yd), ArrayType([96.72, 32.06], BoolType), None, None), VarDecl(Id(RUkz), ArrayType([87.48, 8.62, 19.45], StringType), None, None)], Return()), FuncDecl(Id(s0y), [VarDecl(Id(gS), ArrayType([48.82, 74.05], NumberType), None, None), VarDecl(Id(fVSV), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115455))

	def test_21530115456(self):
		input = '''
var RcL <- false
func gL (number wd[52.43])	begin
	end

func BE (bool Eerj[81.38,8.25], string Zhwt[62.96,86.9])
	return "A"

'''
		expect = '''Program([VarDecl(Id(RcL), None, var, BooleanLit(False)), FuncDecl(Id(gL), [VarDecl(Id(wd), ArrayType([52.43], NumberType), None, None)], Block([])), FuncDecl(Id(BE), [VarDecl(Id(Eerj), ArrayType([81.38, 8.25], BoolType), None, None), VarDecl(Id(Zhwt), ArrayType([62.96, 86.9], StringType), None, None)], Return(StringLit(A)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115456))

	def test_21530115457(self):
		input = '''
bool ei <- false
string dBGq[53.87,95.62] <- 33.5
string w3[81.99,48.09] <- 84.35
var u7 <- "Gro"
func xl (string cmcl, string LBA, number LJ[24.46,13.8])	return "kzJkz"

'''
		expect = '''Program([VarDecl(Id(ei), BoolType, None, BooleanLit(False)), VarDecl(Id(dBGq), ArrayType([53.87, 95.62], StringType), None, NumLit(33.5)), VarDecl(Id(w3), ArrayType([81.99, 48.09], StringType), None, NumLit(84.35)), VarDecl(Id(u7), None, var, StringLit(Gro)), FuncDecl(Id(xl), [VarDecl(Id(cmcl), StringType, None, None), VarDecl(Id(LBA), StringType, None, None), VarDecl(Id(LJ), ArrayType([24.46, 13.8], NumberType), None, None)], Return(StringLit(kzJkz)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115457))

	def test_21530115458(self):
		input = '''
number gF4[55.46,42.13]
func Ms1B ()	begin
		break
	end

func F69g (bool zAeo, number Fz7O[84.03,80.15,50.84], string ZJv2[73.23,93.82])	return "us"

string HY[1.65,89.96] <- 37.86
string f4[47.1,37.74,37.85] <- "A"
'''
		expect = '''Program([VarDecl(Id(gF4), ArrayType([55.46, 42.13], NumberType), None, None), FuncDecl(Id(Ms1B), [], Block([Break])), FuncDecl(Id(F69g), [VarDecl(Id(zAeo), BoolType, None, None), VarDecl(Id(Fz7O), ArrayType([84.03, 80.15, 50.84], NumberType), None, None), VarDecl(Id(ZJv2), ArrayType([73.23, 93.82], StringType), None, None)], Return(StringLit(us))), VarDecl(Id(HY), ArrayType([1.65, 89.96], StringType), None, NumLit(37.86)), VarDecl(Id(f4), ArrayType([47.1, 37.74, 37.85], StringType), None, StringLit(A))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115458))

	def test_21530115459(self):
		input = '''
func wL (string N3FY, number k36c, bool PsYN[44.42])
	return
func bUvI (number jC4Y)
	begin
	end

func zN4 ()	begin
		continue
		yO <- 78.83
	end
func ZXcJ (bool PkV9, number tnY)	return
'''
		expect = '''Program([FuncDecl(Id(wL), [VarDecl(Id(N3FY), StringType, None, None), VarDecl(Id(k36c), NumberType, None, None), VarDecl(Id(PsYN), ArrayType([44.42], BoolType), None, None)], Return()), FuncDecl(Id(bUvI), [VarDecl(Id(jC4Y), NumberType, None, None)], Block([])), FuncDecl(Id(zN4), [], Block([Continue, AssignStmt(Id(yO), NumLit(78.83))])), FuncDecl(Id(ZXcJ), [VarDecl(Id(PkV9), BoolType, None, None), VarDecl(Id(tnY), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115459))

	def test_21530115460(self):
		input = '''
func hPG (bool pN, bool Qwe[73.65,94.8,73.75], string ag[9.66,70.9,31.64])	return
'''
		expect = '''Program([FuncDecl(Id(hPG), [VarDecl(Id(pN), BoolType, None, None), VarDecl(Id(Qwe), ArrayType([73.65, 94.8, 73.75], BoolType), None, None), VarDecl(Id(ag), ArrayType([9.66, 70.9, 31.64], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115460))

	def test_21530115461(self):
		input = '''
func Z2 (string ykZO, string wCA[46.74,46.57], bool UFr4)
	return 83.92

func lK7l (bool qa2, number n51V, number KS8[4.88,78.07,83.55])	begin
		break
		begin
			mjjy(79.76, wi)
			for RiVS until true by RR
				return 12.13
			WX2(false, true)
		end
		begin
			Bb_N(37.66, 47.4)
			return
		end
	end

func PJp (bool bXB)	return
number Ox[51.34] <- true
'''
		expect = '''Program([FuncDecl(Id(Z2), [VarDecl(Id(ykZO), StringType, None, None), VarDecl(Id(wCA), ArrayType([46.74, 46.57], StringType), None, None), VarDecl(Id(UFr4), BoolType, None, None)], Return(NumLit(83.92))), FuncDecl(Id(lK7l), [VarDecl(Id(qa2), BoolType, None, None), VarDecl(Id(n51V), NumberType, None, None), VarDecl(Id(KS8), ArrayType([4.88, 78.07, 83.55], NumberType), None, None)], Block([Break, Block([CallStmt(Id(mjjy), [NumLit(79.76), Id(wi)]), For(Id(RiVS), BooleanLit(True), Id(RR), Return(NumLit(12.13))), CallStmt(Id(WX2), [BooleanLit(False), BooleanLit(True)])]), Block([CallStmt(Id(Bb_N), [NumLit(37.66), NumLit(47.4)]), Return()])])), FuncDecl(Id(PJp), [VarDecl(Id(bXB), BoolType, None, None)], Return()), VarDecl(Id(Ox), ArrayType([51.34], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115461))

	def test_21530115462(self):
		input = '''
func gp (number Wvz, number H0g[89.16])	return true
number xcC0
func sxOT ()
	begin
		continue
		tU7(40.34, true)
		xJn[jJq, 26.99] <- false
	end

bool ZX <- false
'''
		expect = '''Program([FuncDecl(Id(gp), [VarDecl(Id(Wvz), NumberType, None, None), VarDecl(Id(H0g), ArrayType([89.16], NumberType), None, None)], Return(BooleanLit(True))), VarDecl(Id(xcC0), NumberType, None, None), FuncDecl(Id(sxOT), [], Block([Continue, CallStmt(Id(tU7), [NumLit(40.34), BooleanLit(True)]), AssignStmt(ArrayCell(Id(xJn), [Id(jJq), NumLit(26.99)]), BooleanLit(False))])), VarDecl(Id(ZX), BoolType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115462))

	def test_21530115463(self):
		input = '''
func lEi (number FVYg)	return
func hZU (string TSWl[29.96], bool fWgk)	begin
		return vuox
		continue
		break
	end

'''
		expect = '''Program([FuncDecl(Id(lEi), [VarDecl(Id(FVYg), NumberType, None, None)], Return()), FuncDecl(Id(hZU), [VarDecl(Id(TSWl), ArrayType([29.96], StringType), None, None), VarDecl(Id(fWgk), BoolType, None, None)], Block([Return(Id(vuox)), Continue, Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115463))

	def test_21530115464(self):
		input = '''
string J2nL[26.37,61.1] <- 81.08
'''
		expect = '''Program([VarDecl(Id(J2nL), ArrayType([26.37, 61.1], StringType), None, NumLit(81.08))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115464))

	def test_21530115465(self):
		input = '''
func lmu3 (bool y89J[18.9])	return

number D2Y[87.46,13.58] <- "p"
func aJ (bool rDE)	return
'''
		expect = '''Program([FuncDecl(Id(lmu3), [VarDecl(Id(y89J), ArrayType([18.9], BoolType), None, None)], Return()), VarDecl(Id(D2Y), ArrayType([87.46, 13.58], NumberType), None, StringLit(p)), FuncDecl(Id(aJ), [VarDecl(Id(rDE), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115465))

	def test_21530115466(self):
		input = '''
func Gp (bool Hgn)
	return
func hDU8 ()
	return "ALFH"
'''
		expect = '''Program([FuncDecl(Id(Gp), [VarDecl(Id(Hgn), BoolType, None, None)], Return()), FuncDecl(Id(hDU8), [], Return(StringLit(ALFH)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115466))

	def test_21530115467(self):
		input = '''
dynamic ZAW
bool F5O <- 3.79
bool yuV[61.04]
func LTU (string LrVh[67.38,63.41,55.48])
	return 3.16
number APO <- 92.06
'''
		expect = '''Program([VarDecl(Id(ZAW), None, dynamic, None), VarDecl(Id(F5O), BoolType, None, NumLit(3.79)), VarDecl(Id(yuV), ArrayType([61.04], BoolType), None, None), FuncDecl(Id(LTU), [VarDecl(Id(LrVh), ArrayType([67.38, 63.41, 55.48], StringType), None, None)], Return(NumLit(3.16))), VarDecl(Id(APO), NumberType, None, NumLit(92.06))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115467))

	def test_21530115468(self):
		input = '''
number Gi[42.77,81.74]
string Sq5q[89.41,33.49,92.37] <- false
'''
		expect = '''Program([VarDecl(Id(Gi), ArrayType([42.77, 81.74], NumberType), None, None), VarDecl(Id(Sq5q), ArrayType([89.41, 33.49, 92.37], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115468))

	def test_21530115469(self):
		input = '''
func wv (bool wY[62.75,62.9], string PG[64.94,17.49,48.61])
	begin
		continue
	end

bool Gb87
string X_Z[37.31,96.88,34.24] <- false
'''
		expect = '''Program([FuncDecl(Id(wv), [VarDecl(Id(wY), ArrayType([62.75, 62.9], BoolType), None, None), VarDecl(Id(PG), ArrayType([64.94, 17.49, 48.61], StringType), None, None)], Block([Continue])), VarDecl(Id(Gb87), BoolType, None, None), VarDecl(Id(X_Z), ArrayType([37.31, 96.88, 34.24], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115469))

	def test_21530115470(self):
		input = '''
string R10F[61.42,16.0,63.12]
'''
		expect = '''Program([VarDecl(Id(R10F), ArrayType([61.42, 16.0, 63.12], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115470))

	def test_21530115471(self):
		input = '''
bool bdH <- true
func u9 ()
	begin
	end
dynamic dU
'''
		expect = '''Program([VarDecl(Id(bdH), BoolType, None, BooleanLit(True)), FuncDecl(Id(u9), [], Block([])), VarDecl(Id(dU), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115471))

	def test_21530115472(self):
		input = '''
func IR6w ()
	return
'''
		expect = '''Program([FuncDecl(Id(IR6w), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115472))

	def test_21530115473(self):
		input = '''
string x5V[72.02,89.35,17.67] <- 8.39
func K7Ur (bool IqVQ, number wwWG[37.98])
	return Px
func L3v (string Ix)
	return 20.45

string lPC
'''
		expect = '''Program([VarDecl(Id(x5V), ArrayType([72.02, 89.35, 17.67], StringType), None, NumLit(8.39)), FuncDecl(Id(K7Ur), [VarDecl(Id(IqVQ), BoolType, None, None), VarDecl(Id(wwWG), ArrayType([37.98], NumberType), None, None)], Return(Id(Px))), FuncDecl(Id(L3v), [VarDecl(Id(Ix), StringType, None, None)], Return(NumLit(20.45))), VarDecl(Id(lPC), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115473))

	def test_21530115474(self):
		input = '''
dynamic QZM
dynamic eEV
'''
		expect = '''Program([VarDecl(Id(QZM), None, dynamic, None), VarDecl(Id(eEV), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115474))

	def test_21530115475(self):
		input = '''
number BB[8.48,66.84,30.3]
bool uPnc
'''
		expect = '''Program([VarDecl(Id(BB), ArrayType([8.48, 66.84, 30.3], NumberType), None, None), VarDecl(Id(uPnc), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115475))

	def test_21530115476(self):
		input = '''
bool lAj
bool RO[88.84] <- 62.75
'''
		expect = '''Program([VarDecl(Id(lAj), BoolType, None, None), VarDecl(Id(RO), ArrayType([88.84], BoolType), None, NumLit(62.75))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115476))

	def test_21530115477(self):
		input = '''
func qHu (string PQO)	return true
'''
		expect = '''Program([FuncDecl(Id(qHu), [VarDecl(Id(PQO), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115477))

	def test_21530115478(self):
		input = '''
func chh (number Qb6, number y0Xs)	return 58.02

func Zn (bool BhS, string To2R[24.22,10.79])
	begin
		break
		begin
			continue
			A06U()
		end
	end

number QqF
'''
		expect = '''Program([FuncDecl(Id(chh), [VarDecl(Id(Qb6), NumberType, None, None), VarDecl(Id(y0Xs), NumberType, None, None)], Return(NumLit(58.02))), FuncDecl(Id(Zn), [VarDecl(Id(BhS), BoolType, None, None), VarDecl(Id(To2R), ArrayType([24.22, 10.79], StringType), None, None)], Block([Break, Block([Continue, CallStmt(Id(A06U), [])])])), VarDecl(Id(QqF), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115478))

	def test_21530115479(self):
		input = '''
func dq (bool Ox, number DJ, number HFA[13.29,67.7,88.01])
	begin
		continue
	end
func l4 ()
	return "qR"
'''
		expect = '''Program([FuncDecl(Id(dq), [VarDecl(Id(Ox), BoolType, None, None), VarDecl(Id(DJ), NumberType, None, None), VarDecl(Id(HFA), ArrayType([13.29, 67.7, 88.01], NumberType), None, None)], Block([Continue])), FuncDecl(Id(l4), [], Return(StringLit(qR)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115479))

	def test_21530115480(self):
		input = '''
string Bg[78.27,8.99]
'''
		expect = '''Program([VarDecl(Id(Bg), ArrayType([78.27, 8.99], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115480))

	def test_21530115481(self):
		input = '''
var dFZ <- 2.22
number JL[10.66] <- VX
string LYST[75.66]
func lBI (bool BAdl[55.6], string JU)
	begin
		d7()
		continue
		break
	end

'''
		expect = '''Program([VarDecl(Id(dFZ), None, var, NumLit(2.22)), VarDecl(Id(JL), ArrayType([10.66], NumberType), None, Id(VX)), VarDecl(Id(LYST), ArrayType([75.66], StringType), None, None), FuncDecl(Id(lBI), [VarDecl(Id(BAdl), ArrayType([55.6], BoolType), None, None), VarDecl(Id(JU), StringType, None, None)], Block([CallStmt(Id(d7), []), Continue, Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115481))

	def test_21530115482(self):
		input = '''
string Fvdl[63.63,7.44,62.0]
func SQHo ()
	return "yr"

func xD (string B49)
	return

string jUj
func z8T (bool X_A8[92.69,52.17])	begin
	end

'''
		expect = '''Program([VarDecl(Id(Fvdl), ArrayType([63.63, 7.44, 62.0], StringType), None, None), FuncDecl(Id(SQHo), [], Return(StringLit(yr))), FuncDecl(Id(xD), [VarDecl(Id(B49), StringType, None, None)], Return()), VarDecl(Id(jUj), StringType, None, None), FuncDecl(Id(z8T), [VarDecl(Id(X_A8), ArrayType([92.69, 52.17], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115482))

	def test_21530115483(self):
		input = '''
number Nla1 <- false
func O_7E (bool yxl[69.84], number aOci, number mbwe)	begin
		break
		bool thw[3.14,56.31,68.34]
		return eR
	end

func b07 (number fs[31.27,13.06,15.31], string QU1V, string Jmb)	return

dynamic wA7J
'''
		expect = '''Program([VarDecl(Id(Nla1), NumberType, None, BooleanLit(False)), FuncDecl(Id(O_7E), [VarDecl(Id(yxl), ArrayType([69.84], BoolType), None, None), VarDecl(Id(aOci), NumberType, None, None), VarDecl(Id(mbwe), NumberType, None, None)], Block([Break, VarDecl(Id(thw), ArrayType([3.14, 56.31, 68.34], BoolType), None, None), Return(Id(eR))])), FuncDecl(Id(b07), [VarDecl(Id(fs), ArrayType([31.27, 13.06, 15.31], NumberType), None, None), VarDecl(Id(QU1V), StringType, None, None), VarDecl(Id(Jmb), StringType, None, None)], Return()), VarDecl(Id(wA7J), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115483))

	def test_21530115484(self):
		input = '''
number Grk
func oUi (bool Wxgg, string cBIs[67.42])
	return

'''
		expect = '''Program([VarDecl(Id(Grk), NumberType, None, None), FuncDecl(Id(oUi), [VarDecl(Id(Wxgg), BoolType, None, None), VarDecl(Id(cBIs), ArrayType([67.42], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115484))

	def test_21530115485(self):
		input = '''
bool GqJ
func tWL6 (bool lGY)	return oNhL
string mO
'''
		expect = '''Program([VarDecl(Id(GqJ), BoolType, None, None), FuncDecl(Id(tWL6), [VarDecl(Id(lGY), BoolType, None, None)], Return(Id(oNhL))), VarDecl(Id(mO), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115485))

	def test_21530115486(self):
		input = '''
number wakL[72.61,42.66,50.19]
bool ZS <- "Rkj"
number DV <- true
string tuz[10.95]
func lI (number DSTw, string dfUe, number cX[83.12,2.58,6.67])
	begin
		number T_
		hF(o1P, "LLtxD", kjD4)
		for WruX until 16.91 by "YncN"
			ggb(true, "f", Ed)
	end

'''
		expect = '''Program([VarDecl(Id(wakL), ArrayType([72.61, 42.66, 50.19], NumberType), None, None), VarDecl(Id(ZS), BoolType, None, StringLit(Rkj)), VarDecl(Id(DV), NumberType, None, BooleanLit(True)), VarDecl(Id(tuz), ArrayType([10.95], StringType), None, None), FuncDecl(Id(lI), [VarDecl(Id(DSTw), NumberType, None, None), VarDecl(Id(dfUe), StringType, None, None), VarDecl(Id(cX), ArrayType([83.12, 2.58, 6.67], NumberType), None, None)], Block([VarDecl(Id(T_), NumberType, None, None), CallStmt(Id(hF), [Id(o1P), StringLit(LLtxD), Id(kjD4)]), For(Id(WruX), NumLit(16.91), StringLit(YncN), CallStmt(Id(ggb), [BooleanLit(True), StringLit(f), Id(Ed)]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115486))

	def test_21530115487(self):
		input = '''
string sZGZ
'''
		expect = '''Program([VarDecl(Id(sZGZ), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115487))

	def test_21530115488(self):
		input = '''
string Jmac
string RG
number d3_[59.07]
func bgrq (bool qR, number sr, number h6)	begin
		for Ln7 until 58.18 by 87.91
			if (RnaD) if (false) continue
			elif (true) for Lp until mPb by "Sdh"
				begin
					we("TB", 20.04, 96.58)
					bool BHID
					string BW
				end
			elif (true) if (67.38)
			var B7G1 <- "YTNcW"
			elif ("cKZf")
			if (mi)
			dJ("K", 57.02, vE)
			elif (false) begin
				if ("Lqhi")
				WTe <- 52.27
			end
			elif (Cy9_) for CEs until false by 0.18
				string lyN[25.8,4.87]
			elif (iWJ)
			break
			elif (CAa9)
			if (fEIj)
			break
			elif ("uds")
			mY()
			elif ("Vlr")
			tbl6()
			elif (tVz) begin
				dynamic Dl
				continue
				up["qO", true, false] <- "WH"
			end
			elif ("MBSxo") return false
			elif (false)
			if (false)
			QMAN(91.36, false)
			elif (XW)
			begin
				if ("ELPmW") string Sb <- true
				elif (false) break
				elif ("Fai") tGOf <- true
				elif ("abga")
				var v9 <- QTDs
				elif (Hk)
				begin
					return Dy
				end
				elif ("HPMj")
				continue
			end
			elif ("yn") for WFIj until wT by "gbLtd"
				string K4M
			elif ("Wh") break
			else if (D36) for rSIj until 47.32 by true
				return false
			elif (false) string aQ <- true
			elif (true)
			for rSwj until 97.72 by "d"
				return
			elif (false)
			begin
				aYii <- true
			end
			elif ("b")
			begin
				dARA("zaDf", 79.79, "u")
				return
			end
			elif ("RD")
			ct <- "jQo"
			else bZUv()
			elif (65.95)
			string CtBy[77.29,60.54,88.14] <- "VINp"
			elif (false) if (14.0)
			return
			elif (Dwv)
			Gvu(18.94, true)
			else u5(AmWB, false)
			elif (false) if ("WXBu") w9 <- 64.55
			elif (FwV) return a6f
			elif ("vigq")
			for Xgop until auqv by false
				break
			elif (AM) begin
				akq <- 28.58
			end
			else break
	end

string uS <- ON
'''
		expect = '''Program([VarDecl(Id(Jmac), StringType, None, None), VarDecl(Id(RG), StringType, None, None), VarDecl(Id(d3_), ArrayType([59.07], NumberType), None, None), FuncDecl(Id(bgrq), [VarDecl(Id(qR), BoolType, None, None), VarDecl(Id(sr), NumberType, None, None), VarDecl(Id(h6), NumberType, None, None)], Block([For(Id(Ln7), NumLit(58.18), NumLit(87.91), If(Id(RnaD), If(BooleanLit(False), Continue), [(BooleanLit(True), For(Id(Lp), Id(mPb), StringLit(Sdh), Block([CallStmt(Id(we), [StringLit(TB), NumLit(20.04), NumLit(96.58)]), VarDecl(Id(BHID), BoolType, None, None), VarDecl(Id(BW), StringType, None, None)]))), (BooleanLit(True), If(NumLit(67.38), VarDecl(Id(B7G1), None, var, StringLit(YTNcW))), [(StringLit(cKZf), If(Id(mi), CallStmt(Id(dJ), [StringLit(K), NumLit(57.02), Id(vE)])), [(BooleanLit(False), Block([If(StringLit(Lqhi), AssignStmt(Id(WTe), NumLit(52.27))), [], None])), (Id(Cy9_), For(Id(CEs), BooleanLit(False), NumLit(0.18), VarDecl(Id(lyN), ArrayType([25.8, 4.87], StringType), None, None))), (Id(iWJ), Break), (Id(CAa9), If(Id(fEIj), Break), [(StringLit(uds), CallStmt(Id(mY), [])), (StringLit(Vlr), CallStmt(Id(tbl6), [])), (Id(tVz), Block([VarDecl(Id(Dl), None, dynamic, None), Continue, AssignStmt(ArrayCell(Id(up), [StringLit(qO), BooleanLit(True), BooleanLit(False)]), StringLit(WH))])), (StringLit(MBSxo), Return(BooleanLit(False))), (BooleanLit(False), If(BooleanLit(False), CallStmt(Id(QMAN), [NumLit(91.36), BooleanLit(False)])), [(Id(XW), Block([If(StringLit(ELPmW), VarDecl(Id(Sb), StringType, None, BooleanLit(True))), [(BooleanLit(False), Break), (StringLit(Fai), AssignStmt(Id(tGOf), BooleanLit(True))), (StringLit(abga), VarDecl(Id(v9), None, var, Id(QTDs))), (Id(Hk), Block([Return(Id(Dy))])), (StringLit(HPMj), Continue)], None])), (StringLit(yn), For(Id(WFIj), Id(wT), StringLit(gbLtd), VarDecl(Id(K4M), StringType, None, None))), (StringLit(Wh), Break)], If(Id(D36), For(Id(rSIj), NumLit(47.32), BooleanLit(True), Return(BooleanLit(False)))), [(BooleanLit(False), VarDecl(Id(aQ), StringType, None, BooleanLit(True))), (BooleanLit(True), For(Id(rSwj), NumLit(97.72), StringLit(d), Return())), (BooleanLit(False), Block([AssignStmt(Id(aYii), BooleanLit(True))])), (StringLit(b), Block([CallStmt(Id(dARA), [StringLit(zaDf), NumLit(79.79), StringLit(u)]), Return()])), (StringLit(RD), AssignStmt(Id(ct), StringLit(jQo)))], CallStmt(Id(bZUv), [])), (NumLit(65.95), VarDecl(Id(CtBy), ArrayType([77.29, 60.54, 88.14], StringType), None, StringLit(VINp))), (BooleanLit(False), If(NumLit(14.0), Return()), [(Id(Dwv), CallStmt(Id(Gvu), [NumLit(18.94), BooleanLit(True)]))], CallStmt(Id(u5), [Id(AmWB), BooleanLit(False)])), (BooleanLit(False), If(StringLit(WXBu), AssignStmt(Id(w9), NumLit(64.55))), [], None)], None), (Id(FwV), Return(Id(a6f)))], None), (StringLit(vigq), For(Id(Xgop), Id(auqv), BooleanLit(False), Break))], None), (Id(AM), Block([AssignStmt(Id(akq), NumLit(28.58))]))], Break), [], None)])), VarDecl(Id(uS), StringType, None, Id(ON))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115488))

	def test_21530115489(self):
		input = '''
func KL1 (bool JLeI[68.32,19.8,57.18], bool RCz)
	begin
		OWyu(78.32)
		for YsE until "CsPo" by ONG
			var pQ <- 34.83
		if ("i") cP3R(19.06, true, URoR)
		elif (true)
		l4DL <- 15.87
	end
func gCp (bool pi3, number WV5z[35.94,11.4,70.97])	return

func F8Y (string QlJ, string FO2T, number Et[32.19])
	return "Nh"
func KN3E (string QeyO, string cv)
	return

func hS9 ()
	return

'''
		expect = '''Program([FuncDecl(Id(KL1), [VarDecl(Id(JLeI), ArrayType([68.32, 19.8, 57.18], BoolType), None, None), VarDecl(Id(RCz), BoolType, None, None)], Block([CallStmt(Id(OWyu), [NumLit(78.32)]), For(Id(YsE), StringLit(CsPo), Id(ONG), VarDecl(Id(pQ), None, var, NumLit(34.83))), If(StringLit(i), CallStmt(Id(cP3R), [NumLit(19.06), BooleanLit(True), Id(URoR)])), [(BooleanLit(True), AssignStmt(Id(l4DL), NumLit(15.87)))], None])), FuncDecl(Id(gCp), [VarDecl(Id(pi3), BoolType, None, None), VarDecl(Id(WV5z), ArrayType([35.94, 11.4, 70.97], NumberType), None, None)], Return()), FuncDecl(Id(F8Y), [VarDecl(Id(QlJ), StringType, None, None), VarDecl(Id(FO2T), StringType, None, None), VarDecl(Id(Et), ArrayType([32.19], NumberType), None, None)], Return(StringLit(Nh))), FuncDecl(Id(KN3E), [VarDecl(Id(QeyO), StringType, None, None), VarDecl(Id(cv), StringType, None, None)], Return()), FuncDecl(Id(hS9), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115489))

	def test_21530115490(self):
		input = '''
func uKs (number K9[83.06,48.74], string MHE, number S7)	return
func yp (bool iJB, number SHu)
	return true

'''
		expect = '''Program([FuncDecl(Id(uKs), [VarDecl(Id(K9), ArrayType([83.06, 48.74], NumberType), None, None), VarDecl(Id(MHE), StringType, None, None), VarDecl(Id(S7), NumberType, None, None)], Return()), FuncDecl(Id(yp), [VarDecl(Id(iJB), BoolType, None, None), VarDecl(Id(SHu), NumberType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115490))

	def test_21530115491(self):
		input = '''
bool L0[96.25,66.46,55.36]
bool oUu <- wj
func qsZ ()	return
string hlUF[80.63] <- 89.47
'''
		expect = '''Program([VarDecl(Id(L0), ArrayType([96.25, 66.46, 55.36], BoolType), None, None), VarDecl(Id(oUu), BoolType, None, Id(wj)), FuncDecl(Id(qsZ), [], Return()), VarDecl(Id(hlUF), ArrayType([80.63], StringType), None, NumLit(89.47))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115491))

	def test_21530115492(self):
		input = '''
func gXZZ (number APOb[43.78], string j51Z[78.37,59.62], bool aQG[73.1,37.01,83.44])	return "oSe"
func e6 (string d4eF, string Ei[74.39,84.12,57.02], string mi2[19.52,59.6,29.31])	return

number RqH[76.26] <- "RUOsG"
var Qxb <- false
func G0tj (string xwNH[44.65])
	return
'''
		expect = '''Program([FuncDecl(Id(gXZZ), [VarDecl(Id(APOb), ArrayType([43.78], NumberType), None, None), VarDecl(Id(j51Z), ArrayType([78.37, 59.62], StringType), None, None), VarDecl(Id(aQG), ArrayType([73.1, 37.01, 83.44], BoolType), None, None)], Return(StringLit(oSe))), FuncDecl(Id(e6), [VarDecl(Id(d4eF), StringType, None, None), VarDecl(Id(Ei), ArrayType([74.39, 84.12, 57.02], StringType), None, None), VarDecl(Id(mi2), ArrayType([19.52, 59.6, 29.31], StringType), None, None)], Return()), VarDecl(Id(RqH), ArrayType([76.26], NumberType), None, StringLit(RUOsG)), VarDecl(Id(Qxb), None, var, BooleanLit(False)), FuncDecl(Id(G0tj), [VarDecl(Id(xwNH), ArrayType([44.65], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115492))

	def test_21530115493(self):
		input = '''
func gaq2 (string ocm)	begin
		break
		return "x"
	end

dynamic d1 <- "GxU"
'''
		expect = '''Program([FuncDecl(Id(gaq2), [VarDecl(Id(ocm), StringType, None, None)], Block([Break, Return(StringLit(x))])), VarDecl(Id(d1), None, dynamic, StringLit(GxU))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115493))

	def test_21530115494(self):
		input = '''
number RdC <- gqHU
string NQQy[72.98,100.0] <- false
'''
		expect = '''Program([VarDecl(Id(RdC), NumberType, None, Id(gqHU)), VarDecl(Id(NQQy), ArrayType([72.98, 100.0], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115494))

	def test_21530115495(self):
		input = '''
bool Ymm2[17.97]
dynamic szV0
var Fw1 <- "Qdsnf"
func UF (number M5q[36.3,72.49,54.69], string R8EJ)	return "Bm"

bool qn[73.71]
'''
		expect = '''Program([VarDecl(Id(Ymm2), ArrayType([17.97], BoolType), None, None), VarDecl(Id(szV0), None, dynamic, None), VarDecl(Id(Fw1), None, var, StringLit(Qdsnf)), FuncDecl(Id(UF), [VarDecl(Id(M5q), ArrayType([36.3, 72.49, 54.69], NumberType), None, None), VarDecl(Id(R8EJ), StringType, None, None)], Return(StringLit(Bm))), VarDecl(Id(qn), ArrayType([73.71], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115495))

	def test_21530115496(self):
		input = '''
string qP[9.52,20.08] <- Ap
string Nocj[60.72,35.13,44.42]
'''
		expect = '''Program([VarDecl(Id(qP), ArrayType([9.52, 20.08], StringType), None, Id(Ap)), VarDecl(Id(Nocj), ArrayType([60.72, 35.13, 44.42], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115496))

	def test_21530115497(self):
		input = '''
string qd[95.83,11.46,24.68]
func OtK (number zhJ)
	begin
		break
		break
	end
string XA[86.4,57.63] <- 83.81
var y5h <- w5l1
number FJ
'''
		expect = '''Program([VarDecl(Id(qd), ArrayType([95.83, 11.46, 24.68], StringType), None, None), FuncDecl(Id(OtK), [VarDecl(Id(zhJ), NumberType, None, None)], Block([Break, Break])), VarDecl(Id(XA), ArrayType([86.4, 57.63], StringType), None, NumLit(83.81)), VarDecl(Id(y5h), None, var, Id(w5l1)), VarDecl(Id(FJ), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115497))

	def test_21530115498(self):
		input = '''
bool DA6[51.34,56.43] <- "NIfsU"
func WM (string x0_, string cF[66.41,77.52])
	return

func kq (string wN, number v6Wt)	return zu

func QB (string VV5[91.93,64.42], string n__)	return

string Q0t[84.88,0.65,68.11] <- "GAEM"
'''
		expect = '''Program([VarDecl(Id(DA6), ArrayType([51.34, 56.43], BoolType), None, StringLit(NIfsU)), FuncDecl(Id(WM), [VarDecl(Id(x0_), StringType, None, None), VarDecl(Id(cF), ArrayType([66.41, 77.52], StringType), None, None)], Return()), FuncDecl(Id(kq), [VarDecl(Id(wN), StringType, None, None), VarDecl(Id(v6Wt), NumberType, None, None)], Return(Id(zu))), FuncDecl(Id(QB), [VarDecl(Id(VV5), ArrayType([91.93, 64.42], StringType), None, None), VarDecl(Id(n__), StringType, None, None)], Return()), VarDecl(Id(Q0t), ArrayType([84.88, 0.65, 68.11], StringType), None, StringLit(GAEM))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115498))

	def test_21530115499(self):
		input = '''
dynamic bIT
func hPHF (number ov)	return

'''
		expect = '''Program([VarDecl(Id(bIT), None, dynamic, None), FuncDecl(Id(hPHF), [VarDecl(Id(ov), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115499))

	def test_21530115500(self):
		input = '''
func x1 (bool oDK5)
	return
var Cam <- "r"
'''
		expect = '''Program([FuncDecl(Id(x1), [VarDecl(Id(oDK5), BoolType, None, None)], Return()), VarDecl(Id(Cam), None, var, StringLit(r))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115500))

	def test_21530115501(self):
		input = '''
string lxE[94.24,74.81] <- true
'''
		expect = '''Program([VarDecl(Id(lxE), ArrayType([94.24, 74.81], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115501))

	def test_21530115502(self):
		input = '''
var Fwrs <- false
func Br (bool CbV)	return
func cSq (bool Ps4Z[77.25])
	return false

number nR3m[16.85] <- "CoeFc"
func cW (bool qB[48.19,99.33,98.09], number PW[25.15,62.88,73.49], bool bKp[32.78,51.54])
	return

'''
		expect = '''Program([VarDecl(Id(Fwrs), None, var, BooleanLit(False)), FuncDecl(Id(Br), [VarDecl(Id(CbV), BoolType, None, None)], Return()), FuncDecl(Id(cSq), [VarDecl(Id(Ps4Z), ArrayType([77.25], BoolType), None, None)], Return(BooleanLit(False))), VarDecl(Id(nR3m), ArrayType([16.85], NumberType), None, StringLit(CoeFc)), FuncDecl(Id(cW), [VarDecl(Id(qB), ArrayType([48.19, 99.33, 98.09], BoolType), None, None), VarDecl(Id(PW), ArrayType([25.15, 62.88, 73.49], NumberType), None, None), VarDecl(Id(bKp), ArrayType([32.78, 51.54], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115502))

	def test_21530115503(self):
		input = '''
func tSeC (string oHj4[55.52,20.39,11.95], string w_[7.97,79.6,36.96])
	begin
		for Ac until true by "ZJrcT"
			begin
				begin
					break
					var O7 <- JeT_
					number oie[28.34]
				end
			end
		begin
		end
	end
number ux0r <- mrQV
bool jp[5.36,12.65,65.0]
'''
		expect = '''Program([FuncDecl(Id(tSeC), [VarDecl(Id(oHj4), ArrayType([55.52, 20.39, 11.95], StringType), None, None), VarDecl(Id(w_), ArrayType([7.97, 79.6, 36.96], StringType), None, None)], Block([For(Id(Ac), BooleanLit(True), StringLit(ZJrcT), Block([Block([Break, VarDecl(Id(O7), None, var, Id(JeT_)), VarDecl(Id(oie), ArrayType([28.34], NumberType), None, None)])])), Block([])])), VarDecl(Id(ux0r), NumberType, None, Id(mrQV)), VarDecl(Id(jp), ArrayType([5.36, 12.65, 65.0], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115503))

	def test_21530115504(self):
		input = '''
number v5UU[68.49] <- 98.03
func SV ()	begin
		for p8d until true by true
			if (true)
			npTy <- 25.09
			elif ("quD") if (jJ) begin
				break
				if (false) if (vT) if (true) break
				elif (false) begin
				end
				elif ("zk")
				number bpuV[5.09,29.16] <- false
				elif (Pl)
				return "g"
				else break
				elif (71.93) break
				elif ("LmKh")
				begin
					continue
				end
				elif (21.81)
				begin
					break
				end
				elif (t5)
				string Iy[50.4,51.43] <- BxK
				continue
			end
			elif (fyF1)
			number fBS <- xJp
			elif (52.35) return
			elif (43.55)
			break
			elif ("a") if (nq9c) continue
			elif (SjOI) begin
			end
			elif (9.34) for Z7m until 64.75 by "lmto"
				break
			elif (hXn)
			break
			else break
			else for bnS until false by jcv
				if (83.98) t0JH("rhCp", true)
				elif (wzs) continue
	end

func PWy9 (string FQB[11.66,23.16,94.13], number wE3i)
	begin
	end

'''
		expect = '''Program([VarDecl(Id(v5UU), ArrayType([68.49], NumberType), None, NumLit(98.03)), FuncDecl(Id(SV), [], Block([For(Id(p8d), BooleanLit(True), BooleanLit(True), If(BooleanLit(True), AssignStmt(Id(npTy), NumLit(25.09))), [(StringLit(quD), If(Id(jJ), Block([Break, If(BooleanLit(False), If(Id(vT), If(BooleanLit(True), Break), [(BooleanLit(False), Block([])), (StringLit(zk), VarDecl(Id(bpuV), ArrayType([5.09, 29.16], NumberType), None, BooleanLit(False))), (Id(Pl), Return(StringLit(g)))], Break), [(NumLit(71.93), Break), (StringLit(LmKh), Block([Continue])), (NumLit(21.81), Block([Break])), (Id(t5), VarDecl(Id(Iy), ArrayType([50.4, 51.43], StringType), None, Id(BxK)))], None), [], None, Continue])), [(Id(fyF1), VarDecl(Id(fBS), NumberType, None, Id(xJp))), (NumLit(52.35), Return()), (NumLit(43.55), Break), (StringLit(a), If(Id(nq9c), Continue), [(Id(SjOI), Block([])), (NumLit(9.34), For(Id(Z7m), NumLit(64.75), StringLit(lmto), Break)), (Id(hXn), Break)], Break)], For(Id(bnS), BooleanLit(False), Id(jcv), If(NumLit(83.98), CallStmt(Id(t0JH), [StringLit(rhCp), BooleanLit(True)])), [], None)), (Id(wzs), Continue)], None)])), FuncDecl(Id(PWy9), [VarDecl(Id(FQB), ArrayType([11.66, 23.16, 94.13], StringType), None, None), VarDecl(Id(wE3i), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115504))

	def test_21530115505(self):
		input = '''
string U3Le[92.03,14.92,50.13] <- N8
'''
		expect = '''Program([VarDecl(Id(U3Le), ArrayType([92.03, 14.92, 50.13], StringType), None, Id(N8))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115505))

	def test_21530115506(self):
		input = '''
func nkvI (bool uI[9.37])	begin
	end
number XA[99.74,27.99,43.29]
func tE (number HH[20.38], number q9fn[66.58,3.92])	return false

var d7db <- 55.07
string ODBH[53.44] <- EX
'''
		expect = '''Program([FuncDecl(Id(nkvI), [VarDecl(Id(uI), ArrayType([9.37], BoolType), None, None)], Block([])), VarDecl(Id(XA), ArrayType([99.74, 27.99, 43.29], NumberType), None, None), FuncDecl(Id(tE), [VarDecl(Id(HH), ArrayType([20.38], NumberType), None, None), VarDecl(Id(q9fn), ArrayType([66.58, 3.92], NumberType), None, None)], Return(BooleanLit(False))), VarDecl(Id(d7db), None, var, NumLit(55.07)), VarDecl(Id(ODBH), ArrayType([53.44], StringType), None, Id(EX))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115506))

	def test_21530115507(self):
		input = '''
func uN2o ()	return

string ejcg[99.83,11.67] <- "wYBKU"
func irY (number gNT, number l2mH)
	return "TsoPz"
func olmj (number t6Y)
	return

number UaHi[17.31,43.18,18.35]
'''
		expect = '''Program([FuncDecl(Id(uN2o), [], Return()), VarDecl(Id(ejcg), ArrayType([99.83, 11.67], StringType), None, StringLit(wYBKU)), FuncDecl(Id(irY), [VarDecl(Id(gNT), NumberType, None, None), VarDecl(Id(l2mH), NumberType, None, None)], Return(StringLit(TsoPz))), FuncDecl(Id(olmj), [VarDecl(Id(t6Y), NumberType, None, None)], Return()), VarDecl(Id(UaHi), ArrayType([17.31, 43.18, 18.35], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115507))

	def test_21530115508(self):
		input = '''
func CS_ ()
	return 98.43
func Dxnz (number R_, string TMB, number fycQ)
	return
number ZL[90.47]
'''
		expect = '''Program([FuncDecl(Id(CS_), [], Return(NumLit(98.43))), FuncDecl(Id(Dxnz), [VarDecl(Id(R_), NumberType, None, None), VarDecl(Id(TMB), StringType, None, None), VarDecl(Id(fycQ), NumberType, None, None)], Return()), VarDecl(Id(ZL), ArrayType([90.47], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115508))

	def test_21530115509(self):
		input = '''
number JkDG[26.3] <- "M"
number fcZ[75.77,14.21,81.26] <- Ojaz
string JRkf <- 26.98
bool uBa <- 95.55
'''
		expect = '''Program([VarDecl(Id(JkDG), ArrayType([26.3], NumberType), None, StringLit(M)), VarDecl(Id(fcZ), ArrayType([75.77, 14.21, 81.26], NumberType), None, Id(Ojaz)), VarDecl(Id(JRkf), StringType, None, NumLit(26.98)), VarDecl(Id(uBa), BoolType, None, NumLit(95.55))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115509))

	def test_21530115510(self):
		input = '''
number GNN9[23.47] <- true
dynamic mYo <- "Kxb"
bool iuGn <- byRo
func t_ (number oX)
	return 24.63
'''
		expect = '''Program([VarDecl(Id(GNN9), ArrayType([23.47], NumberType), None, BooleanLit(True)), VarDecl(Id(mYo), None, dynamic, StringLit(Kxb)), VarDecl(Id(iuGn), BoolType, None, Id(byRo)), FuncDecl(Id(t_), [VarDecl(Id(oX), NumberType, None, None)], Return(NumLit(24.63)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115510))

	def test_21530115511(self):
		input = '''
func LST ()
	begin
		return
		for k2k until false by false
			continue
		begin
			return
			continue
		end
	end

number dlj[60.83] <- gsP
bool cWT[5.99,8.73,46.33] <- "ExyL"
func lOYT (bool W3R[41.45])	begin
	end
'''
		expect = '''Program([FuncDecl(Id(LST), [], Block([Return(), For(Id(k2k), BooleanLit(False), BooleanLit(False), Continue), Block([Return(), Continue])])), VarDecl(Id(dlj), ArrayType([60.83], NumberType), None, Id(gsP)), VarDecl(Id(cWT), ArrayType([5.99, 8.73, 46.33], BoolType), None, StringLit(ExyL)), FuncDecl(Id(lOYT), [VarDecl(Id(W3R), ArrayType([41.45], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115511))

	def test_21530115512(self):
		input = '''
func gJee (number k92, string pu)
	begin
	end

func KM (number BFv[63.24,59.16,38.43], string e_, string zj5[96.97])
	begin
		for HMS until 46.4 by "f"
			if ("rxvvR")
			number RDS
		break
	end

func iYD ()	begin
	end
'''
		expect = '''Program([FuncDecl(Id(gJee), [VarDecl(Id(k92), NumberType, None, None), VarDecl(Id(pu), StringType, None, None)], Block([])), FuncDecl(Id(KM), [VarDecl(Id(BFv), ArrayType([63.24, 59.16, 38.43], NumberType), None, None), VarDecl(Id(e_), StringType, None, None), VarDecl(Id(zj5), ArrayType([96.97], StringType), None, None)], Block([For(Id(HMS), NumLit(46.4), StringLit(f), If(StringLit(rxvvR), VarDecl(Id(RDS), NumberType, None, None)), [], None), Break])), FuncDecl(Id(iYD), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115512))

	def test_21530115513(self):
		input = '''
func ch ()	return
'''
		expect = '''Program([FuncDecl(Id(ch), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115513))

	def test_21530115514(self):
		input = '''
bool KT0[37.18] <- true
'''
		expect = '''Program([VarDecl(Id(KT0), ArrayType([37.18], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115514))

	def test_21530115515(self):
		input = '''
func K31 (number ewHf, bool aCxT[0.02,55.98], number ic[39.43,39.96])
	return Z5_
func bt (string MGHP, number ml[92.1,93.52], number Yxej[91.05,68.78,7.15])
	return PI

bool uSYD[21.86,39.36,45.97]
func tg (string dR90, string LP[5.9])
	begin
		begin
			begin
				QX <- true
			end
		end
		number s6[72.04,94.67] <- zO
	end

string u5_[20.4,90.35] <- QEH_
'''
		expect = '''Program([FuncDecl(Id(K31), [VarDecl(Id(ewHf), NumberType, None, None), VarDecl(Id(aCxT), ArrayType([0.02, 55.98], BoolType), None, None), VarDecl(Id(ic), ArrayType([39.43, 39.96], NumberType), None, None)], Return(Id(Z5_))), FuncDecl(Id(bt), [VarDecl(Id(MGHP), StringType, None, None), VarDecl(Id(ml), ArrayType([92.1, 93.52], NumberType), None, None), VarDecl(Id(Yxej), ArrayType([91.05, 68.78, 7.15], NumberType), None, None)], Return(Id(PI))), VarDecl(Id(uSYD), ArrayType([21.86, 39.36, 45.97], BoolType), None, None), FuncDecl(Id(tg), [VarDecl(Id(dR90), StringType, None, None), VarDecl(Id(LP), ArrayType([5.9], StringType), None, None)], Block([Block([Block([AssignStmt(Id(QX), BooleanLit(True))])]), VarDecl(Id(s6), ArrayType([72.04, 94.67], NumberType), None, Id(zO))])), VarDecl(Id(u5_), ArrayType([20.4, 90.35], StringType), None, Id(QEH_))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115515))

	def test_21530115516(self):
		input = '''
func Nt (bool OAYP[17.9], number pjo, number xhv[16.01,82.04,62.78])	begin
		break
		continue
	end

func JlQn (string j4H[25.82], bool xEc)	return 28.52
func HL (number b0ar)	begin
		break
	end
func cJ (bool re[9.27,14.09], bool Jy, bool YweF)
	begin
		begin
			break
			continue
			return 61.02
		end
		bHK[true, true] <- "iw"
		continue
	end
'''
		expect = '''Program([FuncDecl(Id(Nt), [VarDecl(Id(OAYP), ArrayType([17.9], BoolType), None, None), VarDecl(Id(pjo), NumberType, None, None), VarDecl(Id(xhv), ArrayType([16.01, 82.04, 62.78], NumberType), None, None)], Block([Break, Continue])), FuncDecl(Id(JlQn), [VarDecl(Id(j4H), ArrayType([25.82], StringType), None, None), VarDecl(Id(xEc), BoolType, None, None)], Return(NumLit(28.52))), FuncDecl(Id(HL), [VarDecl(Id(b0ar), NumberType, None, None)], Block([Break])), FuncDecl(Id(cJ), [VarDecl(Id(re), ArrayType([9.27, 14.09], BoolType), None, None), VarDecl(Id(Jy), BoolType, None, None), VarDecl(Id(YweF), BoolType, None, None)], Block([Block([Break, Continue, Return(NumLit(61.02))]), AssignStmt(ArrayCell(Id(bHK), [BooleanLit(True), BooleanLit(True)]), StringLit(iw)), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115516))

	def test_21530115517(self):
		input = '''
func FDs_ (string Yt)
	return true

func xl (string Oy[55.87])
	return FU
'''
		expect = '''Program([FuncDecl(Id(FDs_), [VarDecl(Id(Yt), StringType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(xl), [VarDecl(Id(Oy), ArrayType([55.87], StringType), None, None)], Return(Id(FU)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115517))

	def test_21530115518(self):
		input = '''
bool BjRa[64.3,53.79] <- false
func FT (number GI, number J1B, string biJX)	return PCyd
func Is (bool ep[2.35,45.71,22.36], number Cji[42.51,50.79], bool pHR7[92.88,17.75])	begin
		WN(QDUJ, 20.16, 93.54)
	end

'''
		expect = '''Program([VarDecl(Id(BjRa), ArrayType([64.3, 53.79], BoolType), None, BooleanLit(False)), FuncDecl(Id(FT), [VarDecl(Id(GI), NumberType, None, None), VarDecl(Id(J1B), NumberType, None, None), VarDecl(Id(biJX), StringType, None, None)], Return(Id(PCyd))), FuncDecl(Id(Is), [VarDecl(Id(ep), ArrayType([2.35, 45.71, 22.36], BoolType), None, None), VarDecl(Id(Cji), ArrayType([42.51, 50.79], NumberType), None, None), VarDecl(Id(pHR7), ArrayType([92.88, 17.75], BoolType), None, None)], Block([CallStmt(Id(WN), [Id(QDUJ), NumLit(20.16), NumLit(93.54)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115518))

	def test_21530115519(self):
		input = '''
func ZY (bool r2Mv, string IO, string Ly)
	begin
		break
		bool uH
	end

'''
		expect = '''Program([FuncDecl(Id(ZY), [VarDecl(Id(r2Mv), BoolType, None, None), VarDecl(Id(IO), StringType, None, None), VarDecl(Id(Ly), StringType, None, None)], Block([Break, VarDecl(Id(uH), BoolType, None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115519))

	def test_21530115520(self):
		input = '''
bool Vc
dynamic JRPB
number fQ
'''
		expect = '''Program([VarDecl(Id(Vc), BoolType, None, None), VarDecl(Id(JRPB), None, dynamic, None), VarDecl(Id(fQ), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115520))

	def test_21530115521(self):
		input = '''
func pQ (bool Rg, string XwL)	return "W"

string ZHad
number JR2r[7.51,11.5] <- fOWn
bool xTZB[22.5,67.38,15.91] <- HV
'''
		expect = '''Program([FuncDecl(Id(pQ), [VarDecl(Id(Rg), BoolType, None, None), VarDecl(Id(XwL), StringType, None, None)], Return(StringLit(W))), VarDecl(Id(ZHad), StringType, None, None), VarDecl(Id(JR2r), ArrayType([7.51, 11.5], NumberType), None, Id(fOWn)), VarDecl(Id(xTZB), ArrayType([22.5, 67.38, 15.91], BoolType), None, Id(HV))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115521))

	def test_21530115522(self):
		input = '''
func sH (number sD, bool Rxe[33.44,39.76,41.75], number Z6[56.88,72.74])
	return
number VGM5[94.45,77.14,46.71]
'''
		expect = '''Program([FuncDecl(Id(sH), [VarDecl(Id(sD), NumberType, None, None), VarDecl(Id(Rxe), ArrayType([33.44, 39.76, 41.75], BoolType), None, None), VarDecl(Id(Z6), ArrayType([56.88, 72.74], NumberType), None, None)], Return()), VarDecl(Id(VGM5), ArrayType([94.45, 77.14, 46.71], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115522))

	def test_21530115523(self):
		input = '''
string z3qZ[68.84,48.41] <- true
number XXY
'''
		expect = '''Program([VarDecl(Id(z3qZ), ArrayType([68.84, 48.41], StringType), None, BooleanLit(True)), VarDecl(Id(XXY), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115523))

	def test_21530115524(self):
		input = '''
func zDY (number kEPz[98.52], bool Gui1[80.1,96.95])	return

'''
		expect = '''Program([FuncDecl(Id(zDY), [VarDecl(Id(kEPz), ArrayType([98.52], NumberType), None, None), VarDecl(Id(Gui1), ArrayType([80.1, 96.95], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115524))

	def test_21530115525(self):
		input = '''
number H7XV[24.83]
var gOdX <- 85.53
'''
		expect = '''Program([VarDecl(Id(H7XV), ArrayType([24.83], NumberType), None, None), VarDecl(Id(gOdX), None, var, NumLit(85.53))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115525))

	def test_21530115526(self):
		input = '''
number ylW <- true
number FVe <- true
'''
		expect = '''Program([VarDecl(Id(ylW), NumberType, None, BooleanLit(True)), VarDecl(Id(FVe), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115526))

	def test_21530115527(self):
		input = '''
var py <- "Om"
func NjpJ ()	return true
func Jp (number KHb6[36.31,49.5], string PC[49.2,93.17])
	begin
		continue
		break
	end

func t1u (string cvFC[92.83,97.49], bool Oi[55.86], string cAV[50.34,46.85])	return lQx
'''
		expect = '''Program([VarDecl(Id(py), None, var, StringLit(Om)), FuncDecl(Id(NjpJ), [], Return(BooleanLit(True))), FuncDecl(Id(Jp), [VarDecl(Id(KHb6), ArrayType([36.31, 49.5], NumberType), None, None), VarDecl(Id(PC), ArrayType([49.2, 93.17], StringType), None, None)], Block([Continue, Break])), FuncDecl(Id(t1u), [VarDecl(Id(cvFC), ArrayType([92.83, 97.49], StringType), None, None), VarDecl(Id(Oi), ArrayType([55.86], BoolType), None, None), VarDecl(Id(cAV), ArrayType([50.34, 46.85], StringType), None, None)], Return(Id(lQx)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115527))

	def test_21530115528(self):
		input = '''
func ja (bool Dj[26.89,27.71], string QBq, number sHbr)
	return
func E2r3 ()	return
'''
		expect = '''Program([FuncDecl(Id(ja), [VarDecl(Id(Dj), ArrayType([26.89, 27.71], BoolType), None, None), VarDecl(Id(QBq), StringType, None, None), VarDecl(Id(sHbr), NumberType, None, None)], Return()), FuncDecl(Id(E2r3), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115528))

	def test_21530115529(self):
		input = '''
func llN (string Fq0)	return
string tsx <- omTP
bool X69H <- 38.09
number kL <- false
bool HM
'''
		expect = '''Program([FuncDecl(Id(llN), [VarDecl(Id(Fq0), StringType, None, None)], Return()), VarDecl(Id(tsx), StringType, None, Id(omTP)), VarDecl(Id(X69H), BoolType, None, NumLit(38.09)), VarDecl(Id(kL), NumberType, None, BooleanLit(False)), VarDecl(Id(HM), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115529))

	def test_21530115530(self):
		input = '''
func cWt (number ei[54.81,26.33,50.31])
	return "eZX"

number g2 <- 90.17
'''
		expect = '''Program([FuncDecl(Id(cWt), [VarDecl(Id(ei), ArrayType([54.81, 26.33, 50.31], NumberType), None, None)], Return(StringLit(eZX))), VarDecl(Id(g2), NumberType, None, NumLit(90.17))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115530))

	def test_21530115531(self):
		input = '''
string kl73
bool dx
dynamic tA <- "U"
'''
		expect = '''Program([VarDecl(Id(kl73), StringType, None, None), VarDecl(Id(dx), BoolType, None, None), VarDecl(Id(tA), None, dynamic, StringLit(U))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115531))

	def test_21530115532(self):
		input = '''
func Fw2 (number hx4, bool vTkZ[19.07], number Ro5)
	return true

func Lvey (number EJG[12.63,52.9], bool ng[94.22,41.23], bool FB[82.98])	return "xnaRf"

number x3[82.75] <- 42.47
string Q5t[8.42] <- JJ
'''
		expect = '''Program([FuncDecl(Id(Fw2), [VarDecl(Id(hx4), NumberType, None, None), VarDecl(Id(vTkZ), ArrayType([19.07], BoolType), None, None), VarDecl(Id(Ro5), NumberType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(Lvey), [VarDecl(Id(EJG), ArrayType([12.63, 52.9], NumberType), None, None), VarDecl(Id(ng), ArrayType([94.22, 41.23], BoolType), None, None), VarDecl(Id(FB), ArrayType([82.98], BoolType), None, None)], Return(StringLit(xnaRf))), VarDecl(Id(x3), ArrayType([82.75], NumberType), None, NumLit(42.47)), VarDecl(Id(Q5t), ArrayType([8.42], StringType), None, Id(JJ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115532))

	def test_21530115533(self):
		input = '''
string g4MT <- true
bool tHS9[24.1]
number cd <- "MF"
'''
		expect = '''Program([VarDecl(Id(g4MT), StringType, None, BooleanLit(True)), VarDecl(Id(tHS9), ArrayType([24.1], BoolType), None, None), VarDecl(Id(cd), NumberType, None, StringLit(MF))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115533))

	def test_21530115534(self):
		input = '''
func KES (bool YDC[34.45,0.95], number pnXP)
	begin
		break
		continue
	end

bool Es[85.33]
string COi[56.06,18.42]
'''
		expect = '''Program([FuncDecl(Id(KES), [VarDecl(Id(YDC), ArrayType([34.45, 0.95], BoolType), None, None), VarDecl(Id(pnXP), NumberType, None, None)], Block([Break, Continue])), VarDecl(Id(Es), ArrayType([85.33], BoolType), None, None), VarDecl(Id(COi), ArrayType([56.06, 18.42], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115534))

	def test_21530115535(self):
		input = '''
number gy1b[84.66,61.38,97.62] <- true
func Dv_E (string xY, number d8y[33.43,93.34,52.72])
	return 33.64

bool Ijuw[3.34,87.18,65.74] <- false
func k_j (string vXK[6.85])	begin
	end
'''
		expect = '''Program([VarDecl(Id(gy1b), ArrayType([84.66, 61.38, 97.62], NumberType), None, BooleanLit(True)), FuncDecl(Id(Dv_E), [VarDecl(Id(xY), StringType, None, None), VarDecl(Id(d8y), ArrayType([33.43, 93.34, 52.72], NumberType), None, None)], Return(NumLit(33.64))), VarDecl(Id(Ijuw), ArrayType([3.34, 87.18, 65.74], BoolType), None, BooleanLit(False)), FuncDecl(Id(k_j), [VarDecl(Id(vXK), ArrayType([6.85], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115535))

	def test_21530115536(self):
		input = '''
bool BD7Y[17.42,56.5,57.1] <- "NiK"
func E6w (bool lE[29.41], bool H5mf)	return
func TEr7 (string ORS6)	begin
		if (2.04) return
		elif ("RzU") continue
		else py["SGR"] <- "vl"
		begin
			continue
			break
			return "gWl"
		end
		continue
	end
bool sHS <- true
'''
		expect = '''Program([VarDecl(Id(BD7Y), ArrayType([17.42, 56.5, 57.1], BoolType), None, StringLit(NiK)), FuncDecl(Id(E6w), [VarDecl(Id(lE), ArrayType([29.41], BoolType), None, None), VarDecl(Id(H5mf), BoolType, None, None)], Return()), FuncDecl(Id(TEr7), [VarDecl(Id(ORS6), StringType, None, None)], Block([If(NumLit(2.04), Return()), [(StringLit(RzU), Continue)], AssignStmt(ArrayCell(Id(py), [StringLit(SGR)]), StringLit(vl)), Block([Continue, Break, Return(StringLit(gWl))]), Continue])), VarDecl(Id(sHS), BoolType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115536))

	def test_21530115537(self):
		input = '''
dynamic Py
func Ddo (number Mb[43.32], bool it, number GTd[58.16,26.94])
	begin
		for lEf until 29.82 by false
			number MF[89.52,37.2] <- kaX9
	end
func LG (string l4Hr, bool uGpt[57.75,36.01], bool j6)
	return "jkAW"

'''
		expect = '''Program([VarDecl(Id(Py), None, dynamic, None), FuncDecl(Id(Ddo), [VarDecl(Id(Mb), ArrayType([43.32], NumberType), None, None), VarDecl(Id(it), BoolType, None, None), VarDecl(Id(GTd), ArrayType([58.16, 26.94], NumberType), None, None)], Block([For(Id(lEf), NumLit(29.82), BooleanLit(False), VarDecl(Id(MF), ArrayType([89.52, 37.2], NumberType), None, Id(kaX9)))])), FuncDecl(Id(LG), [VarDecl(Id(l4Hr), StringType, None, None), VarDecl(Id(uGpt), ArrayType([57.75, 36.01], BoolType), None, None), VarDecl(Id(j6), BoolType, None, None)], Return(StringLit(jkAW)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115537))

	def test_21530115538(self):
		input = '''
string cVHl[86.99,58.06,22.54]
string qs3[19.49,11.35] <- 35.01
dynamic OdxS <- true
string YO[72.25,47.57,10.3]
'''
		expect = '''Program([VarDecl(Id(cVHl), ArrayType([86.99, 58.06, 22.54], StringType), None, None), VarDecl(Id(qs3), ArrayType([19.49, 11.35], StringType), None, NumLit(35.01)), VarDecl(Id(OdxS), None, dynamic, BooleanLit(True)), VarDecl(Id(YO), ArrayType([72.25, 47.57, 10.3], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115538))

	def test_21530115539(self):
		input = '''
string fRt[5.49,69.68]
func Lmq (string aDhE[77.18,99.27,75.79])
	return "BbxvD"
string inCP <- true
string GQ[40.0,4.7]
bool ET58[17.72,44.03]
'''
		expect = '''Program([VarDecl(Id(fRt), ArrayType([5.49, 69.68], StringType), None, None), FuncDecl(Id(Lmq), [VarDecl(Id(aDhE), ArrayType([77.18, 99.27, 75.79], StringType), None, None)], Return(StringLit(BbxvD))), VarDecl(Id(inCP), StringType, None, BooleanLit(True)), VarDecl(Id(GQ), ArrayType([40.0, 4.7], StringType), None, None), VarDecl(Id(ET58), ArrayType([17.72, 44.03], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115539))

	def test_21530115540(self):
		input = '''
string g8[70.74,2.14,75.92]
bool FaG[12.44,51.38,24.07]
string FMO <- "oGj"
func YP ()
	return
func tV ()	return true
'''
		expect = '''Program([VarDecl(Id(g8), ArrayType([70.74, 2.14, 75.92], StringType), None, None), VarDecl(Id(FaG), ArrayType([12.44, 51.38, 24.07], BoolType), None, None), VarDecl(Id(FMO), StringType, None, StringLit(oGj)), FuncDecl(Id(YP), [], Return()), FuncDecl(Id(tV), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115540))

	def test_21530115541(self):
		input = '''
number oy[34.44,79.48,80.52]
func qh ()	return zcH

var Tjk <- S8
func IY_ (number mr, number s9[31.42])
	begin
		if (Qa)
		for Md until OKx by fF
			if (86.12)
			GtBl(sNf)
			elif (36.09) begin
				bool if5e <- tmA
			end
			elif (44.52)
			continue
			elif (58.89) KH4J(lK, false)
			elif (kw)
			a0Mj[true, "c", true] <- true
			elif ("YSnlG")
			UcdP <- true
		elif ("UD")
		begin
			return "Oiplm"
		end
		elif ("bZngu") break
		elif (false) break
		elif (53.35)
		continue
		elif (false) j7("kWkQT", "p")
		else break
	end

func D7nH (string wE[49.81,32.87,18.5])
	begin
		break
	end

'''
		expect = '''Program([VarDecl(Id(oy), ArrayType([34.44, 79.48, 80.52], NumberType), None, None), FuncDecl(Id(qh), [], Return(Id(zcH))), VarDecl(Id(Tjk), None, var, Id(S8)), FuncDecl(Id(IY_), [VarDecl(Id(mr), NumberType, None, None), VarDecl(Id(s9), ArrayType([31.42], NumberType), None, None)], Block([If(Id(Qa), For(Id(Md), Id(OKx), Id(fF), If(NumLit(86.12), CallStmt(Id(GtBl), [Id(sNf)])), [(NumLit(36.09), Block([VarDecl(Id(if5e), BoolType, None, Id(tmA))])), (NumLit(44.52), Continue), (NumLit(58.89), CallStmt(Id(KH4J), [Id(lK), BooleanLit(False)])), (Id(kw), AssignStmt(ArrayCell(Id(a0Mj), [BooleanLit(True), StringLit(c), BooleanLit(True)]), BooleanLit(True))), (StringLit(YSnlG), AssignStmt(Id(UcdP), BooleanLit(True))), (StringLit(UD), Block([Return(StringLit(Oiplm))])), (StringLit(bZngu), Break), (BooleanLit(False), Break), (NumLit(53.35), Continue), (BooleanLit(False), CallStmt(Id(j7), [StringLit(kWkQT), StringLit(p)]))], Break)), [], None])), FuncDecl(Id(D7nH), [VarDecl(Id(wE), ArrayType([49.81, 32.87, 18.5], StringType), None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115541))

	def test_21530115542(self):
		input = '''
func FvsD (number bWH2)
	return "Q"
func Z7KX (bool ac[21.22], number rkdo, number w96_)	return

func tR (string GbQJ, number pP)	return bRK
'''
		expect = '''Program([FuncDecl(Id(FvsD), [VarDecl(Id(bWH2), NumberType, None, None)], Return(StringLit(Q))), FuncDecl(Id(Z7KX), [VarDecl(Id(ac), ArrayType([21.22], BoolType), None, None), VarDecl(Id(rkdo), NumberType, None, None), VarDecl(Id(w96_), NumberType, None, None)], Return()), FuncDecl(Id(tR), [VarDecl(Id(GbQJ), StringType, None, None), VarDecl(Id(pP), NumberType, None, None)], Return(Id(bRK)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115542))

	def test_21530115543(self):
		input = '''
func sG (string nSyN[93.76,1.14], bool ft[78.63])	begin
		begin
			yzt <- true
		end
	end
bool KPmP
'''
		expect = '''Program([FuncDecl(Id(sG), [VarDecl(Id(nSyN), ArrayType([93.76, 1.14], StringType), None, None), VarDecl(Id(ft), ArrayType([78.63], BoolType), None, None)], Block([Block([AssignStmt(Id(yzt), BooleanLit(True))])])), VarDecl(Id(KPmP), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115543))

	def test_21530115544(self):
		input = '''
number EguC[56.07,71.19,12.26] <- 32.57
string OK[36.3]
number vsf[56.47]
func zHN (number lRk[91.24,86.27,20.54], string TU, bool VN[79.67,30.83])
	return hT
var Zx <- xV6
'''
		expect = '''Program([VarDecl(Id(EguC), ArrayType([56.07, 71.19, 12.26], NumberType), None, NumLit(32.57)), VarDecl(Id(OK), ArrayType([36.3], StringType), None, None), VarDecl(Id(vsf), ArrayType([56.47], NumberType), None, None), FuncDecl(Id(zHN), [VarDecl(Id(lRk), ArrayType([91.24, 86.27, 20.54], NumberType), None, None), VarDecl(Id(TU), StringType, None, None), VarDecl(Id(VN), ArrayType([79.67, 30.83], BoolType), None, None)], Return(Id(hT))), VarDecl(Id(Zx), None, var, Id(xV6))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115544))

	def test_21530115545(self):
		input = '''
string aQOy[75.03]
'''
		expect = '''Program([VarDecl(Id(aQOy), ArrayType([75.03], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115545))

	def test_21530115546(self):
		input = '''
func IWSS (bool J5[21.22,55.87], bool MOx, number ykBG)	begin
	end
var vA99 <- false
func FL8n ()	begin
	end
var B3 <- false
number KxCu <- true
'''
		expect = '''Program([FuncDecl(Id(IWSS), [VarDecl(Id(J5), ArrayType([21.22, 55.87], BoolType), None, None), VarDecl(Id(MOx), BoolType, None, None), VarDecl(Id(ykBG), NumberType, None, None)], Block([])), VarDecl(Id(vA99), None, var, BooleanLit(False)), FuncDecl(Id(FL8n), [], Block([])), VarDecl(Id(B3), None, var, BooleanLit(False)), VarDecl(Id(KxCu), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115546))

	def test_21530115547(self):
		input = '''
bool zQX
bool UxW <- L5
'''
		expect = '''Program([VarDecl(Id(zQX), BoolType, None, None), VarDecl(Id(UxW), BoolType, None, Id(L5))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115547))

	def test_21530115548(self):
		input = '''
func zhcX (string rtcr[11.45,31.66,61.38], bool vCur[82.4], string vgvD[76.27,72.37,39.02])
	begin
		begin
		end
		aR(false, Kq1g, eDGa)
	end

func MQ (string bF, bool OY3K[1.86,22.75])
	return

func sM (string LbZa[2.18])	return
'''
		expect = '''Program([FuncDecl(Id(zhcX), [VarDecl(Id(rtcr), ArrayType([11.45, 31.66, 61.38], StringType), None, None), VarDecl(Id(vCur), ArrayType([82.4], BoolType), None, None), VarDecl(Id(vgvD), ArrayType([76.27, 72.37, 39.02], StringType), None, None)], Block([Block([]), CallStmt(Id(aR), [BooleanLit(False), Id(Kq1g), Id(eDGa)])])), FuncDecl(Id(MQ), [VarDecl(Id(bF), StringType, None, None), VarDecl(Id(OY3K), ArrayType([1.86, 22.75], BoolType), None, None)], Return()), FuncDecl(Id(sM), [VarDecl(Id(LbZa), ArrayType([2.18], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115548))

	def test_21530115549(self):
		input = '''
func tOH (number nhY[31.08,27.49], string Psg, number VIW[52.24,17.77])
	return
func KEed ()
	begin
	end
func aBb (string ilIf[75.85,76.18,41.77], string o5YI[84.54,30.03,10.12], bool wn[60.0,34.01,14.81])
	return false
string WZ[91.82]
'''
		expect = '''Program([FuncDecl(Id(tOH), [VarDecl(Id(nhY), ArrayType([31.08, 27.49], NumberType), None, None), VarDecl(Id(Psg), StringType, None, None), VarDecl(Id(VIW), ArrayType([52.24, 17.77], NumberType), None, None)], Return()), FuncDecl(Id(KEed), [], Block([])), FuncDecl(Id(aBb), [VarDecl(Id(ilIf), ArrayType([75.85, 76.18, 41.77], StringType), None, None), VarDecl(Id(o5YI), ArrayType([84.54, 30.03, 10.12], StringType), None, None), VarDecl(Id(wn), ArrayType([60.0, 34.01, 14.81], BoolType), None, None)], Return(BooleanLit(False))), VarDecl(Id(WZ), ArrayType([91.82], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115549))

	def test_21530115550(self):
		input = '''
var ju <- 16.71
var IrZ <- "kNQj"
func qj (bool o5cJ[14.61,73.6], bool zzcW)	return 77.22
'''
		expect = '''Program([VarDecl(Id(ju), None, var, NumLit(16.71)), VarDecl(Id(IrZ), None, var, StringLit(kNQj)), FuncDecl(Id(qj), [VarDecl(Id(o5cJ), ArrayType([14.61, 73.6], BoolType), None, None), VarDecl(Id(zzcW), BoolType, None, None)], Return(NumLit(77.22)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115550))

	def test_21530115551(self):
		input = '''
func qZPO (string paK[49.03,45.64])	return

string IJr[82.47]
'''
		expect = '''Program([FuncDecl(Id(qZPO), [VarDecl(Id(paK), ArrayType([49.03, 45.64], StringType), None, None)], Return()), VarDecl(Id(IJr), ArrayType([82.47], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115551))

	def test_21530115552(self):
		input = '''
string HDYP[40.98,90.98,25.68]
func I1JJ (string yqT)
	begin
	end
number CBPV[44.41,84.29,76.36] <- Dykn
dynamic Vodt
'''
		expect = '''Program([VarDecl(Id(HDYP), ArrayType([40.98, 90.98, 25.68], StringType), None, None), FuncDecl(Id(I1JJ), [VarDecl(Id(yqT), StringType, None, None)], Block([])), VarDecl(Id(CBPV), ArrayType([44.41, 84.29, 76.36], NumberType), None, Id(Dykn)), VarDecl(Id(Vodt), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115552))

	def test_21530115553(self):
		input = '''
func e0 ()
	return false
'''
		expect = '''Program([FuncDecl(Id(e0), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115553))

	def test_21530115554(self):
		input = '''
func Yj7b (bool o7, bool YBV3)
	begin
		return
		if (58.04) begin
			bool GnMY[33.99,77.74]
		end
		elif (61.22) begin
			continue
			var Vd <- lF
		end
		elif (23.6) continue
		elif (false) break
		elif (true) continue
		elif ("yho") break
		continue
	end
func Tj (string glK, bool k7)
	begin
		continue
		break
	end

string r_L[21.93,3.93] <- 29.53
string kRe[96.94,1.32,48.26] <- 37.68
'''
		expect = '''Program([FuncDecl(Id(Yj7b), [VarDecl(Id(o7), BoolType, None, None), VarDecl(Id(YBV3), BoolType, None, None)], Block([Return(), If(NumLit(58.04), Block([VarDecl(Id(GnMY), ArrayType([33.99, 77.74], BoolType), None, None)])), [(NumLit(61.22), Block([Continue, VarDecl(Id(Vd), None, var, Id(lF))])), (NumLit(23.6), Continue), (BooleanLit(False), Break), (BooleanLit(True), Continue), (StringLit(yho), Break)], None, Continue])), FuncDecl(Id(Tj), [VarDecl(Id(glK), StringType, None, None), VarDecl(Id(k7), BoolType, None, None)], Block([Continue, Break])), VarDecl(Id(r_L), ArrayType([21.93, 3.93], StringType), None, NumLit(29.53)), VarDecl(Id(kRe), ArrayType([96.94, 1.32, 48.26], StringType), None, NumLit(37.68))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115554))

	def test_21530115555(self):
		input = '''
string BQq[77.28]
func DxXx (number No6, number iPU7, number dYq[82.17])	return "WSDw"
number pAH[77.36] <- G7
func XCm (number I2)	begin
	end

'''
		expect = '''Program([VarDecl(Id(BQq), ArrayType([77.28], StringType), None, None), FuncDecl(Id(DxXx), [VarDecl(Id(No6), NumberType, None, None), VarDecl(Id(iPU7), NumberType, None, None), VarDecl(Id(dYq), ArrayType([82.17], NumberType), None, None)], Return(StringLit(WSDw))), VarDecl(Id(pAH), ArrayType([77.36], NumberType), None, Id(G7)), FuncDecl(Id(XCm), [VarDecl(Id(I2), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115555))

	def test_21530115556(self):
		input = '''
dynamic b5v
bool Uvfb[48.4,9.03] <- 41.15
func LqoL (number vdq, bool UxrD)
	return

func IGyf (number Y_gq)	return

'''
		expect = '''Program([VarDecl(Id(b5v), None, dynamic, None), VarDecl(Id(Uvfb), ArrayType([48.4, 9.03], BoolType), None, NumLit(41.15)), FuncDecl(Id(LqoL), [VarDecl(Id(vdq), NumberType, None, None), VarDecl(Id(UxrD), BoolType, None, None)], Return()), FuncDecl(Id(IGyf), [VarDecl(Id(Y_gq), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115556))

	def test_21530115557(self):
		input = '''
func pkt ()	return

'''
		expect = '''Program([FuncDecl(Id(pkt), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115557))

	def test_21530115558(self):
		input = '''
func WMOB (bool f6Fw, number WF6[50.53,57.07])
	begin
	end
string fVja
bool kM[43.21,41.69]
string mM
'''
		expect = '''Program([FuncDecl(Id(WMOB), [VarDecl(Id(f6Fw), BoolType, None, None), VarDecl(Id(WF6), ArrayType([50.53, 57.07], NumberType), None, None)], Block([])), VarDecl(Id(fVja), StringType, None, None), VarDecl(Id(kM), ArrayType([43.21, 41.69], BoolType), None, None), VarDecl(Id(mM), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115558))

	def test_21530115559(self):
		input = '''
func qCQ (bool vT0V[52.97,0.89,8.26])
	begin
	end

func FD3 ()	return

func H93 (bool yX, number AG[24.91], number eaGU[45.15,6.98,21.05])	return "MI"
'''
		expect = '''Program([FuncDecl(Id(qCQ), [VarDecl(Id(vT0V), ArrayType([52.97, 0.89, 8.26], BoolType), None, None)], Block([])), FuncDecl(Id(FD3), [], Return()), FuncDecl(Id(H93), [VarDecl(Id(yX), BoolType, None, None), VarDecl(Id(AG), ArrayType([24.91], NumberType), None, None), VarDecl(Id(eaGU), ArrayType([45.15, 6.98, 21.05], NumberType), None, None)], Return(StringLit(MI)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115559))

	def test_21530115560(self):
		input = '''
func exnq (bool bQQ, number uHl[18.44])
	begin
		for OQ until "b" by 71.88
			return
		continue
	end

func xLr (bool EF)
	begin
		ZQ["qGI"] <- 89.55
	end
bool Uuu[30.9,87.49]
func TQ (string mOg5, string Xt)
	return "fZtY"
func Gvdw (string zVf, number HjmU[15.45,78.68,23.75])	return false

'''
		expect = '''Program([FuncDecl(Id(exnq), [VarDecl(Id(bQQ), BoolType, None, None), VarDecl(Id(uHl), ArrayType([18.44], NumberType), None, None)], Block([For(Id(OQ), StringLit(b), NumLit(71.88), Return()), Continue])), FuncDecl(Id(xLr), [VarDecl(Id(EF), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(ZQ), [StringLit(qGI)]), NumLit(89.55))])), VarDecl(Id(Uuu), ArrayType([30.9, 87.49], BoolType), None, None), FuncDecl(Id(TQ), [VarDecl(Id(mOg5), StringType, None, None), VarDecl(Id(Xt), StringType, None, None)], Return(StringLit(fZtY))), FuncDecl(Id(Gvdw), [VarDecl(Id(zVf), StringType, None, None), VarDecl(Id(HjmU), ArrayType([15.45, 78.68, 23.75], NumberType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115560))

	def test_21530115561(self):
		input = '''
func vA6o (string RA[36.0], bool Xog[32.12])
	return

'''
		expect = '''Program([FuncDecl(Id(vA6o), [VarDecl(Id(RA), ArrayType([36.0], StringType), None, None), VarDecl(Id(Xog), ArrayType([32.12], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115561))

	def test_21530115562(self):
		input = '''
dynamic gB8O <- 21.75
number Mdn
func oTF (number bEi[52.17], number Yq)	return

func TQVM (number Pooe[53.71], bool XFYX[69.32], number FZK)	return
func kWoP ()	return "GCDWR"

'''
		expect = '''Program([VarDecl(Id(gB8O), None, dynamic, NumLit(21.75)), VarDecl(Id(Mdn), NumberType, None, None), FuncDecl(Id(oTF), [VarDecl(Id(bEi), ArrayType([52.17], NumberType), None, None), VarDecl(Id(Yq), NumberType, None, None)], Return()), FuncDecl(Id(TQVM), [VarDecl(Id(Pooe), ArrayType([53.71], NumberType), None, None), VarDecl(Id(XFYX), ArrayType([69.32], BoolType), None, None), VarDecl(Id(FZK), NumberType, None, None)], Return()), FuncDecl(Id(kWoP), [], Return(StringLit(GCDWR)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115562))

	def test_21530115563(self):
		input = '''
func wcun (number Es2k[67.3,8.53])	return
func yh (string M_[29.51,53.97,49.03])
	begin
		return
		for kAq until false by true
			continue
		begin
			m6D(true, true)
			return fDJr
			for gw5j until y4 by true
				qf6()
		end
	end

var Gg <- "U"
number Dfz
number zQQ
'''
		expect = '''Program([FuncDecl(Id(wcun), [VarDecl(Id(Es2k), ArrayType([67.3, 8.53], NumberType), None, None)], Return()), FuncDecl(Id(yh), [VarDecl(Id(M_), ArrayType([29.51, 53.97, 49.03], StringType), None, None)], Block([Return(), For(Id(kAq), BooleanLit(False), BooleanLit(True), Continue), Block([CallStmt(Id(m6D), [BooleanLit(True), BooleanLit(True)]), Return(Id(fDJr)), For(Id(gw5j), Id(y4), BooleanLit(True), CallStmt(Id(qf6), []))])])), VarDecl(Id(Gg), None, var, StringLit(U)), VarDecl(Id(Dfz), NumberType, None, None), VarDecl(Id(zQQ), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115563))

	def test_21530115564(self):
		input = '''
bool N2h
string NzjM[3.07,51.9]
func o5S (number tE[29.18,17.3])
	return false

'''
		expect = '''Program([VarDecl(Id(N2h), BoolType, None, None), VarDecl(Id(NzjM), ArrayType([3.07, 51.9], StringType), None, None), FuncDecl(Id(o5S), [VarDecl(Id(tE), ArrayType([29.18, 17.3], NumberType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115564))

	def test_21530115565(self):
		input = '''
number d0R <- "HmN"
number db[86.89,46.38,95.8]
number wL <- true
number vM[90.42,53.65,62.2]
'''
		expect = '''Program([VarDecl(Id(d0R), NumberType, None, StringLit(HmN)), VarDecl(Id(db), ArrayType([86.89, 46.38, 95.8], NumberType), None, None), VarDecl(Id(wL), NumberType, None, BooleanLit(True)), VarDecl(Id(vM), ArrayType([90.42, 53.65, 62.2], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115565))

	def test_21530115566(self):
		input = '''
func Gll (bool WFak, number Sr[53.48])	return 33.88
number dJo[28.28]
'''
		expect = '''Program([FuncDecl(Id(Gll), [VarDecl(Id(WFak), BoolType, None, None), VarDecl(Id(Sr), ArrayType([53.48], NumberType), None, None)], Return(NumLit(33.88))), VarDecl(Id(dJo), ArrayType([28.28], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115566))

	def test_21530115567(self):
		input = '''
func YEqa (bool waT, number jA)	return "gY"

string BQK <- Nre
func TmCc (number X7ua)	return 94.22

bool tM2S <- true
func kf (number uv9, bool Tb, bool Vg)
	return false
'''
		expect = '''Program([FuncDecl(Id(YEqa), [VarDecl(Id(waT), BoolType, None, None), VarDecl(Id(jA), NumberType, None, None)], Return(StringLit(gY))), VarDecl(Id(BQK), StringType, None, Id(Nre)), FuncDecl(Id(TmCc), [VarDecl(Id(X7ua), NumberType, None, None)], Return(NumLit(94.22))), VarDecl(Id(tM2S), BoolType, None, BooleanLit(True)), FuncDecl(Id(kf), [VarDecl(Id(uv9), NumberType, None, None), VarDecl(Id(Tb), BoolType, None, None), VarDecl(Id(Vg), BoolType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115567))

	def test_21530115568(self):
		input = '''
func uq (number em[20.03,0.44,32.17])
	begin
		uc(5.06, 22.94)
		var gFWf <- 33.59
		break
	end
func YG (string z6, bool SYc[37.46,23.66,1.18], string X7h0)
	return

'''
		expect = '''Program([FuncDecl(Id(uq), [VarDecl(Id(em), ArrayType([20.03, 0.44, 32.17], NumberType), None, None)], Block([CallStmt(Id(uc), [NumLit(5.06), NumLit(22.94)]), VarDecl(Id(gFWf), None, var, NumLit(33.59)), Break])), FuncDecl(Id(YG), [VarDecl(Id(z6), StringType, None, None), VarDecl(Id(SYc), ArrayType([37.46, 23.66, 1.18], BoolType), None, None), VarDecl(Id(X7h0), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115568))

	def test_21530115569(self):
		input = '''
func LA (number Bijw[59.0,38.37,43.21])
	return
dynamic VG <- "lO"
'''
		expect = '''Program([FuncDecl(Id(LA), [VarDecl(Id(Bijw), ArrayType([59.0, 38.37, 43.21], NumberType), None, None)], Return()), VarDecl(Id(VG), None, dynamic, StringLit(lO))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115569))

	def test_21530115570(self):
		input = '''
bool h0L[85.98]
'''
		expect = '''Program([VarDecl(Id(h0L), ArrayType([85.98], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115570))

	def test_21530115571(self):
		input = '''
func U0c (number ch, number hdT)
	return uhBF

'''
		expect = '''Program([FuncDecl(Id(U0c), [VarDecl(Id(ch), NumberType, None, None), VarDecl(Id(hdT), NumberType, None, None)], Return(Id(uhBF)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115571))

	def test_21530115572(self):
		input = '''
func v4Nh (number Fh, number ro, number xA)
	begin
	end

bool Fsd <- 2.85
dynamic d1S
func nl (bool Dr)	return
string wka <- true
'''
		expect = '''Program([FuncDecl(Id(v4Nh), [VarDecl(Id(Fh), NumberType, None, None), VarDecl(Id(ro), NumberType, None, None), VarDecl(Id(xA), NumberType, None, None)], Block([])), VarDecl(Id(Fsd), BoolType, None, NumLit(2.85)), VarDecl(Id(d1S), None, dynamic, None), FuncDecl(Id(nl), [VarDecl(Id(Dr), BoolType, None, None)], Return()), VarDecl(Id(wka), StringType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115572))

	def test_21530115573(self):
		input = '''
func tR (number Lj, number qA, string f1n[85.68])	return
func mXEd (bool hS[42.02,34.61])	begin
		if (49.22)
		begin
			bool ZUts
			for myA until 49.22 by 64.75
				for c4 until "Uk" by "O"
					return true
		end
		elif ("qMGoX") ZAb <- UKyf
		elif (69.92) bool wu_C[40.87]
		elif (true) hX7[gVjZ, false, false] <- u2bo
		for Nt until 35.81 by Cey
			FcJy(false, 79.5)
	end

number AGOP <- 80.93
string Ug[99.63,45.5,26.46]
'''
		expect = '''Program([FuncDecl(Id(tR), [VarDecl(Id(Lj), NumberType, None, None), VarDecl(Id(qA), NumberType, None, None), VarDecl(Id(f1n), ArrayType([85.68], StringType), None, None)], Return()), FuncDecl(Id(mXEd), [VarDecl(Id(hS), ArrayType([42.02, 34.61], BoolType), None, None)], Block([If(NumLit(49.22), Block([VarDecl(Id(ZUts), BoolType, None, None), For(Id(myA), NumLit(49.22), NumLit(64.75), For(Id(c4), StringLit(Uk), StringLit(O), Return(BooleanLit(True))))])), [(StringLit(qMGoX), AssignStmt(Id(ZAb), Id(UKyf))), (NumLit(69.92), VarDecl(Id(wu_C), ArrayType([40.87], BoolType), None, None)), (BooleanLit(True), AssignStmt(ArrayCell(Id(hX7), [Id(gVjZ), BooleanLit(False), BooleanLit(False)]), Id(u2bo)))], None, For(Id(Nt), NumLit(35.81), Id(Cey), CallStmt(Id(FcJy), [BooleanLit(False), NumLit(79.5)]))])), VarDecl(Id(AGOP), NumberType, None, NumLit(80.93)), VarDecl(Id(Ug), ArrayType([99.63, 45.5, 26.46], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115573))

	def test_21530115574(self):
		input = '''
func rX6h ()
	return
func Bjf (number Hsb[73.8,12.64], string kQJp[37.46,70.46], number wTV)	return

number V6co[24.99,69.85] <- true
func JN4c (string QLqf, bool NLgW, string KR[47.33])
	return
func lYs3 ()
	return 39.54

'''
		expect = '''Program([FuncDecl(Id(rX6h), [], Return()), FuncDecl(Id(Bjf), [VarDecl(Id(Hsb), ArrayType([73.8, 12.64], NumberType), None, None), VarDecl(Id(kQJp), ArrayType([37.46, 70.46], StringType), None, None), VarDecl(Id(wTV), NumberType, None, None)], Return()), VarDecl(Id(V6co), ArrayType([24.99, 69.85], NumberType), None, BooleanLit(True)), FuncDecl(Id(JN4c), [VarDecl(Id(QLqf), StringType, None, None), VarDecl(Id(NLgW), BoolType, None, None), VarDecl(Id(KR), ArrayType([47.33], StringType), None, None)], Return()), FuncDecl(Id(lYs3), [], Return(NumLit(39.54)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115574))

	def test_21530115575(self):
		input = '''
func YIv (bool a6, bool Hv[54.22])	return

func Hjt (bool jfhg, string tJj6[26.61])
	return

bool YL <- K0
func Il27 (string Ja, string uALa[71.83,19.84,79.63])
	return
number j6N <- "IPpOV"
'''
		expect = '''Program([FuncDecl(Id(YIv), [VarDecl(Id(a6), BoolType, None, None), VarDecl(Id(Hv), ArrayType([54.22], BoolType), None, None)], Return()), FuncDecl(Id(Hjt), [VarDecl(Id(jfhg), BoolType, None, None), VarDecl(Id(tJj6), ArrayType([26.61], StringType), None, None)], Return()), VarDecl(Id(YL), BoolType, None, Id(K0)), FuncDecl(Id(Il27), [VarDecl(Id(Ja), StringType, None, None), VarDecl(Id(uALa), ArrayType([71.83, 19.84, 79.63], StringType), None, None)], Return()), VarDecl(Id(j6N), NumberType, None, StringLit(IPpOV))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115575))

	def test_21530115576(self):
		input = '''
func Rmo (number tv7, number yi[17.48,59.14])
	return jOTj

var WR3x <- 31.78
dynamic jq
bool lBR[89.72,8.79]
'''
		expect = '''Program([FuncDecl(Id(Rmo), [VarDecl(Id(tv7), NumberType, None, None), VarDecl(Id(yi), ArrayType([17.48, 59.14], NumberType), None, None)], Return(Id(jOTj))), VarDecl(Id(WR3x), None, var, NumLit(31.78)), VarDecl(Id(jq), None, dynamic, None), VarDecl(Id(lBR), ArrayType([89.72, 8.79], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115576))

	def test_21530115577(self):
		input = '''
func QTq ()	return
string L5Q
func I4pa (bool jZ, string luL5[64.24,94.96], number DV)	return

number ou <- true
'''
		expect = '''Program([FuncDecl(Id(QTq), [], Return()), VarDecl(Id(L5Q), StringType, None, None), FuncDecl(Id(I4pa), [VarDecl(Id(jZ), BoolType, None, None), VarDecl(Id(luL5), ArrayType([64.24, 94.96], StringType), None, None), VarDecl(Id(DV), NumberType, None, None)], Return()), VarDecl(Id(ou), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115577))

	def test_21530115578(self):
		input = '''
func jhN (string pX, number rf[30.64,12.97])
	return 43.64

number nm0
string So[23.06,4.28,47.7]
'''
		expect = '''Program([FuncDecl(Id(jhN), [VarDecl(Id(pX), StringType, None, None), VarDecl(Id(rf), ArrayType([30.64, 12.97], NumberType), None, None)], Return(NumLit(43.64))), VarDecl(Id(nm0), NumberType, None, None), VarDecl(Id(So), ArrayType([23.06, 4.28, 47.7], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115578))

	def test_21530115579(self):
		input = '''
func wNwm (string gR[30.32,60.83,6.82], string it0, number g2[42.28,81.55,73.16])
	return v4t
'''
		expect = '''Program([FuncDecl(Id(wNwm), [VarDecl(Id(gR), ArrayType([30.32, 60.83, 6.82], StringType), None, None), VarDecl(Id(it0), StringType, None, None), VarDecl(Id(g2), ArrayType([42.28, 81.55, 73.16], NumberType), None, None)], Return(Id(v4t)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115579))

	def test_21530115580(self):
		input = '''
func v8 (string WO99)
	begin
		break
	end
dynamic ktMN
func GU (number Vcph, bool lb6h[36.32,93.65], bool cy[14.15])	begin
		sDi <- 46.56
		if (true)
		continue
		elif (false) for GN until false by "lb"
			bool yNr
		elif ("Zx") for NT until false by "b"
			iWS <- false
		elif ("ydueH")
		begin
			Ic6[false, 10.69, "bSO"] <- 27.47
			for KG until true by 82.57
				wZD <- 73.73
		end
		else for Nb until false by Zc
			W8(Yo9M, "uDNUX", 8.97)
	end

'''
		expect = '''Program([FuncDecl(Id(v8), [VarDecl(Id(WO99), StringType, None, None)], Block([Break])), VarDecl(Id(ktMN), None, dynamic, None), FuncDecl(Id(GU), [VarDecl(Id(Vcph), NumberType, None, None), VarDecl(Id(lb6h), ArrayType([36.32, 93.65], BoolType), None, None), VarDecl(Id(cy), ArrayType([14.15], BoolType), None, None)], Block([AssignStmt(Id(sDi), NumLit(46.56)), If(BooleanLit(True), Continue), [(BooleanLit(False), For(Id(GN), BooleanLit(False), StringLit(lb), VarDecl(Id(yNr), BoolType, None, None))), (StringLit(Zx), For(Id(NT), BooleanLit(False), StringLit(b), AssignStmt(Id(iWS), BooleanLit(False)))), (StringLit(ydueH), Block([AssignStmt(ArrayCell(Id(Ic6), [BooleanLit(False), NumLit(10.69), StringLit(bSO)]), NumLit(27.47)), For(Id(KG), BooleanLit(True), NumLit(82.57), AssignStmt(Id(wZD), NumLit(73.73)))]))], For(Id(Nb), BooleanLit(False), Id(Zc), CallStmt(Id(W8), [Id(Yo9M), StringLit(uDNUX), NumLit(8.97)]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115580))

	def test_21530115581(self):
		input = '''
var ZyLw <- true
func SCn (bool nIYj[5.72,58.06,76.32], string i1o)
	return

'''
		expect = '''Program([VarDecl(Id(ZyLw), None, var, BooleanLit(True)), FuncDecl(Id(SCn), [VarDecl(Id(nIYj), ArrayType([5.72, 58.06, 76.32], BoolType), None, None), VarDecl(Id(i1o), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115581))

	def test_21530115582(self):
		input = '''
func EXEr ()	return 45.64

func N9A (bool y2jF[48.1,10.65,79.31])
	return

dynamic Jx
func HP ()	begin
		begin
			continue
		end
		number EXNG
		number VS[79.26,56.18,70.91]
	end

bool adMD[69.03,54.55]
'''
		expect = '''Program([FuncDecl(Id(EXEr), [], Return(NumLit(45.64))), FuncDecl(Id(N9A), [VarDecl(Id(y2jF), ArrayType([48.1, 10.65, 79.31], BoolType), None, None)], Return()), VarDecl(Id(Jx), None, dynamic, None), FuncDecl(Id(HP), [], Block([Block([Continue]), VarDecl(Id(EXNG), NumberType, None, None), VarDecl(Id(VS), ArrayType([79.26, 56.18, 70.91], NumberType), None, None)])), VarDecl(Id(adMD), ArrayType([69.03, 54.55], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115582))

	def test_21530115583(self):
		input = '''
bool ud <- "Ea"
func CG (string eM0[55.6,10.02,51.45])	return sWq

'''
		expect = '''Program([VarDecl(Id(ud), BoolType, None, StringLit(Ea)), FuncDecl(Id(CG), [VarDecl(Id(eM0), ArrayType([55.6, 10.02, 51.45], StringType), None, None)], Return(Id(sWq)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115583))

	def test_21530115584(self):
		input = '''
func jSqi ()
	return 88.42

number S9Fc <- "NmD"
'''
		expect = '''Program([FuncDecl(Id(jSqi), [], Return(NumLit(88.42))), VarDecl(Id(S9Fc), NumberType, None, StringLit(NmD))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115584))

	def test_21530115585(self):
		input = '''
func eppU (bool HeX5[4.01,1.45], string ajh, string Osc[81.53,20.39,53.6])	return

func oL76 (number FOyt, string Zl[43.69,0.76], string Jh)
	return false
func Pf (string r8lI[3.7,80.13], number DSW[6.67,37.23,34.82], number ft)	begin
		DUWt <- Joqk
		begin
			continue
			break
		end
	end
number qfuC <- qOB
'''
		expect = '''Program([FuncDecl(Id(eppU), [VarDecl(Id(HeX5), ArrayType([4.01, 1.45], BoolType), None, None), VarDecl(Id(ajh), StringType, None, None), VarDecl(Id(Osc), ArrayType([81.53, 20.39, 53.6], StringType), None, None)], Return()), FuncDecl(Id(oL76), [VarDecl(Id(FOyt), NumberType, None, None), VarDecl(Id(Zl), ArrayType([43.69, 0.76], StringType), None, None), VarDecl(Id(Jh), StringType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(Pf), [VarDecl(Id(r8lI), ArrayType([3.7, 80.13], StringType), None, None), VarDecl(Id(DSW), ArrayType([6.67, 37.23, 34.82], NumberType), None, None), VarDecl(Id(ft), NumberType, None, None)], Block([AssignStmt(Id(DUWt), Id(Joqk)), Block([Continue, Break])])), VarDecl(Id(qfuC), NumberType, None, Id(qOB))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115585))

	def test_21530115586(self):
		input = '''
func iW_4 (number s_t[4.08,12.25,7.1])
	return XTf
func vC86 (number Eyyk, number Rt9[21.51,50.94])
	begin
		begin
			T0[73.15, 18.65] <- "Jhm"
		end
	end
func JgCA (bool GWK, string FvO1[17.61,15.47,18.74])
	return

number Rd <- "VLtO"
'''
		expect = '''Program([FuncDecl(Id(iW_4), [VarDecl(Id(s_t), ArrayType([4.08, 12.25, 7.1], NumberType), None, None)], Return(Id(XTf))), FuncDecl(Id(vC86), [VarDecl(Id(Eyyk), NumberType, None, None), VarDecl(Id(Rt9), ArrayType([21.51, 50.94], NumberType), None, None)], Block([Block([AssignStmt(ArrayCell(Id(T0), [NumLit(73.15), NumLit(18.65)]), StringLit(Jhm))])])), FuncDecl(Id(JgCA), [VarDecl(Id(GWK), BoolType, None, None), VarDecl(Id(FvO1), ArrayType([17.61, 15.47, 18.74], StringType), None, None)], Return()), VarDecl(Id(Rd), NumberType, None, StringLit(VLtO))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115586))

	def test_21530115587(self):
		input = '''
func KCI ()	begin
		for y6 until true by true
			for IJ5J until y2w by "KqgR"
				for N9N until false by iS7f
					laE <- "n"
		if (Wr9)
		for Gs until Kx by false
			break
		elif (9.3)
		O3z5("z", "KEeu")
		else C0b()
	end
bool GI6[95.42,81.76]
bool Xf <- 97.32
'''
		expect = '''Program([FuncDecl(Id(KCI), [], Block([For(Id(y6), BooleanLit(True), BooleanLit(True), For(Id(IJ5J), Id(y2w), StringLit(KqgR), For(Id(N9N), BooleanLit(False), Id(iS7f), AssignStmt(Id(laE), StringLit(n))))), If(Id(Wr9), For(Id(Gs), Id(Kx), BooleanLit(False), Break)), [(NumLit(9.3), CallStmt(Id(O3z5), [StringLit(z), StringLit(KEeu)]))], CallStmt(Id(C0b), [])])), VarDecl(Id(GI6), ArrayType([95.42, 81.76], BoolType), None, None), VarDecl(Id(Xf), BoolType, None, NumLit(97.32))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115587))

	def test_21530115588(self):
		input = '''
func VE ()	return 42.61

bool IL <- DB_
func QKE (number gN)	begin
		Bne(wrHt)
	end

'''
		expect = '''Program([FuncDecl(Id(VE), [], Return(NumLit(42.61))), VarDecl(Id(IL), BoolType, None, Id(DB_)), FuncDecl(Id(QKE), [VarDecl(Id(gN), NumberType, None, None)], Block([CallStmt(Id(Bne), [Id(wrHt)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115588))

	def test_21530115589(self):
		input = '''
func bMc (bool CTm, number nTI, string vZ[13.5,30.57,21.53])
	begin
		string Oy[36.79,79.78]
		break
		for mw until "PXEB" by "zrd"
			string WuvP[99.79] <- "SM"
	end
string wHzp[78.31] <- false
func twhR ()
	return
'''
		expect = '''Program([FuncDecl(Id(bMc), [VarDecl(Id(CTm), BoolType, None, None), VarDecl(Id(nTI), NumberType, None, None), VarDecl(Id(vZ), ArrayType([13.5, 30.57, 21.53], StringType), None, None)], Block([VarDecl(Id(Oy), ArrayType([36.79, 79.78], StringType), None, None), Break, For(Id(mw), StringLit(PXEB), StringLit(zrd), VarDecl(Id(WuvP), ArrayType([99.79], StringType), None, StringLit(SM)))])), VarDecl(Id(wHzp), ArrayType([78.31], StringType), None, BooleanLit(False)), FuncDecl(Id(twhR), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115589))

	def test_21530115590(self):
		input = '''
number sRe7[63.39,32.98] <- 66.18
func Yx ()	return false
func j8M (bool qsM[72.15,20.91], bool aEY, bool PU[29.13,70.92])	return

func hvu (string FsZo[13.46,51.94], number wXfY, string S8)
	return 20.13
'''
		expect = '''Program([VarDecl(Id(sRe7), ArrayType([63.39, 32.98], NumberType), None, NumLit(66.18)), FuncDecl(Id(Yx), [], Return(BooleanLit(False))), FuncDecl(Id(j8M), [VarDecl(Id(qsM), ArrayType([72.15, 20.91], BoolType), None, None), VarDecl(Id(aEY), BoolType, None, None), VarDecl(Id(PU), ArrayType([29.13, 70.92], BoolType), None, None)], Return()), FuncDecl(Id(hvu), [VarDecl(Id(FsZo), ArrayType([13.46, 51.94], StringType), None, None), VarDecl(Id(wXfY), NumberType, None, None), VarDecl(Id(S8), StringType, None, None)], Return(NumLit(20.13)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115590))

	def test_21530115591(self):
		input = '''
bool IUNX[60.65] <- "kK"
'''
		expect = '''Program([VarDecl(Id(IUNX), ArrayType([60.65], BoolType), None, StringLit(kK))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115591))

	def test_21530115592(self):
		input = '''
func qV ()
	begin
		if (gsI4)
		bool rWk7
		elif (64.03) Ywi <- 1.23
		elif (u5E) continue
		elif (qYXq) continue
		elif (false)
		continue
		bool YI[12.35,49.57] <- 53.76
		for TyZt until "T" by 95.89
			for lH until 34.41 by "VbiS"
				bool xDCg
	end

'''
		expect = '''Program([FuncDecl(Id(qV), [], Block([If(Id(gsI4), VarDecl(Id(rWk7), BoolType, None, None)), [(NumLit(64.03), AssignStmt(Id(Ywi), NumLit(1.23))), (Id(u5E), Continue), (Id(qYXq), Continue), (BooleanLit(False), Continue)], None, VarDecl(Id(YI), ArrayType([12.35, 49.57], BoolType), None, NumLit(53.76)), For(Id(TyZt), StringLit(T), NumLit(95.89), For(Id(lH), NumLit(34.41), StringLit(VbiS), VarDecl(Id(xDCg), BoolType, None, None)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115592))

	def test_21530115593(self):
		input = '''
func zKI (number NI, bool ayi4[36.63])	return

'''
		expect = '''Program([FuncDecl(Id(zKI), [VarDecl(Id(NI), NumberType, None, None), VarDecl(Id(ayi4), ArrayType([36.63], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115593))

	def test_21530115594(self):
		input = '''
number E7[91.7]
number DGdx[44.66,89.32]
'''
		expect = '''Program([VarDecl(Id(E7), ArrayType([91.7], NumberType), None, None), VarDecl(Id(DGdx), ArrayType([44.66, 89.32], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115594))

	def test_21530115595(self):
		input = '''
number rJ2y[31.79] <- "RAqD"
number e97[1.76] <- 25.57
number IRcy[60.18,26.0] <- "IeCe"
'''
		expect = '''Program([VarDecl(Id(rJ2y), ArrayType([31.79], NumberType), None, StringLit(RAqD)), VarDecl(Id(e97), ArrayType([1.76], NumberType), None, NumLit(25.57)), VarDecl(Id(IRcy), ArrayType([60.18, 26.0], NumberType), None, StringLit(IeCe))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115595))

	def test_21530115596(self):
		input = '''
string Rzyj[0.29,83.12,37.81]
bool z2[87.91,49.05] <- "lrm"
string Z8
func da (string HUDr[21.32], string BrUX[75.16,72.58,23.59])
	return

func RO ()
	return "aQHb"
'''
		expect = '''Program([VarDecl(Id(Rzyj), ArrayType([0.29, 83.12, 37.81], StringType), None, None), VarDecl(Id(z2), ArrayType([87.91, 49.05], BoolType), None, StringLit(lrm)), VarDecl(Id(Z8), StringType, None, None), FuncDecl(Id(da), [VarDecl(Id(HUDr), ArrayType([21.32], StringType), None, None), VarDecl(Id(BrUX), ArrayType([75.16, 72.58, 23.59], StringType), None, None)], Return()), FuncDecl(Id(RO), [], Return(StringLit(aQHb)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115596))

	def test_21530115597(self):
		input = '''
bool Z2f_[9.08,45.66,44.5]
'''
		expect = '''Program([VarDecl(Id(Z2f_), ArrayType([9.08, 45.66, 44.5], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115597))

	def test_21530115598(self):
		input = '''
string ENfD[24.32]
func QzE (string E1b[69.95,47.59,16.85])
	begin
		begin
		end
	end

'''
		expect = '''Program([VarDecl(Id(ENfD), ArrayType([24.32], StringType), None, None), FuncDecl(Id(QzE), [VarDecl(Id(E1b), ArrayType([69.95, 47.59, 16.85], StringType), None, None)], Block([Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115598))

	def test_21530115599(self):
		input = '''
func Th (bool RG, bool O7XJ)
	return
number E_[87.72] <- utfk
'''
		expect = '''Program([FuncDecl(Id(Th), [VarDecl(Id(RG), BoolType, None, None), VarDecl(Id(O7XJ), BoolType, None, None)], Return()), VarDecl(Id(E_), ArrayType([87.72], NumberType), None, Id(utfk))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115599))

	def test_21530115600(self):
		input = '''
bool d4[7.27,30.87,49.87] <- jJj
func lWYL (bool cRly[24.89,33.01], number vRUG[93.74,30.85])	begin
		for xkK until 95.41 by eZDa
			string zoW[2.31] <- x2Lr
	end
func AW3w ()	begin
		return "Jdy"
		if (false)
		for ly until v1 by "idVr"
			gz[72.26, "Mw"] <- 65.29
		elif (56.32) if ("P")
		begin
		end
		elif (Q712) if (11.78)
		DJ(true)
		elif (true) continue
		elif (71.64) continue
		elif ("vwG")
		break
		elif (Qcu)
		DQ[92.98, false, false] <- "yA"
		elif ("j")
		var li1G <- false
		elif (true)
		if ("Cu")
		Ql(Ejrp, W5q, PrRF)
		elif (false) break
		dynamic iwr
	end

'''
		expect = '''Program([VarDecl(Id(d4), ArrayType([7.27, 30.87, 49.87], BoolType), None, Id(jJj)), FuncDecl(Id(lWYL), [VarDecl(Id(cRly), ArrayType([24.89, 33.01], BoolType), None, None), VarDecl(Id(vRUG), ArrayType([93.74, 30.85], NumberType), None, None)], Block([For(Id(xkK), NumLit(95.41), Id(eZDa), VarDecl(Id(zoW), ArrayType([2.31], StringType), None, Id(x2Lr)))])), FuncDecl(Id(AW3w), [], Block([Return(StringLit(Jdy)), If(BooleanLit(False), For(Id(ly), Id(v1), StringLit(idVr), AssignStmt(ArrayCell(Id(gz), [NumLit(72.26), StringLit(Mw)]), NumLit(65.29)))), [(NumLit(56.32), If(StringLit(P), Block([])), [(Id(Q712), If(NumLit(11.78), CallStmt(Id(DJ), [BooleanLit(True)])), [(BooleanLit(True), Continue), (NumLit(71.64), Continue), (StringLit(vwG), Break), (Id(Qcu), AssignStmt(ArrayCell(Id(DQ), [NumLit(92.98), BooleanLit(False), BooleanLit(False)]), StringLit(yA))), (StringLit(j), VarDecl(Id(li1G), None, var, BooleanLit(False)))], None), (BooleanLit(True), If(StringLit(Cu), CallStmt(Id(Ql), [Id(Ejrp), Id(W5q), Id(PrRF)])), [], None)], None), (BooleanLit(False), Break)], None, VarDecl(Id(iwr), None, dynamic, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115600))

	def test_21530115601(self):
		input = '''
bool BjBp[65.85,40.02] <- 4.36
'''
		expect = '''Program([VarDecl(Id(BjBp), ArrayType([65.85, 40.02], BoolType), None, NumLit(4.36))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115601))

	def test_21530115602(self):
		input = '''
number u3 <- false
'''
		expect = '''Program([VarDecl(Id(u3), NumberType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115602))

	def test_21530115603(self):
		input = '''
func MN0 (bool kZcr[83.56])
	return

func ItP (string wRh0)	begin
		begin
		end
	end

number UFq8
func C0lc (string oI[67.89,3.4], string zPkO[63.3,91.32,85.92], bool dAcG)	return "YhL"

'''
		expect = '''Program([FuncDecl(Id(MN0), [VarDecl(Id(kZcr), ArrayType([83.56], BoolType), None, None)], Return()), FuncDecl(Id(ItP), [VarDecl(Id(wRh0), StringType, None, None)], Block([Block([])])), VarDecl(Id(UFq8), NumberType, None, None), FuncDecl(Id(C0lc), [VarDecl(Id(oI), ArrayType([67.89, 3.4], StringType), None, None), VarDecl(Id(zPkO), ArrayType([63.3, 91.32, 85.92], StringType), None, None), VarDecl(Id(dAcG), BoolType, None, None)], Return(StringLit(YhL)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115603))

	def test_21530115604(self):
		input = '''
bool e4C <- true
dynamic sE4p <- false
'''
		expect = '''Program([VarDecl(Id(e4C), BoolType, None, BooleanLit(True)), VarDecl(Id(sE4p), None, dynamic, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115604))

	def test_21530115605(self):
		input = '''
bool KBS
func iyX (bool gZr, string G32, number IP)
	return 26.55
string Q0
bool JgO4 <- false
'''
		expect = '''Program([VarDecl(Id(KBS), BoolType, None, None), FuncDecl(Id(iyX), [VarDecl(Id(gZr), BoolType, None, None), VarDecl(Id(G32), StringType, None, None), VarDecl(Id(IP), NumberType, None, None)], Return(NumLit(26.55))), VarDecl(Id(Q0), StringType, None, None), VarDecl(Id(JgO4), BoolType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115605))

	def test_21530115606(self):
		input = '''
func no (bool wL, number MlN, bool cpZ)	begin
		Ytq("WKxLX", "O", Ru)
		cbZv[h_, KXG8, lsuh] <- false
	end

dynamic XE <- true
func hgAo ()
	begin
		continue
		return 46.25
	end

bool WdsD
func BPt ()
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(no), [VarDecl(Id(wL), BoolType, None, None), VarDecl(Id(MlN), NumberType, None, None), VarDecl(Id(cpZ), BoolType, None, None)], Block([CallStmt(Id(Ytq), [StringLit(WKxLX), StringLit(O), Id(Ru)]), AssignStmt(ArrayCell(Id(cbZv), [Id(h_), Id(KXG8), Id(lsuh)]), BooleanLit(False))])), VarDecl(Id(XE), None, dynamic, BooleanLit(True)), FuncDecl(Id(hgAo), [], Block([Continue, Return(NumLit(46.25))])), VarDecl(Id(WdsD), BoolType, None, None), FuncDecl(Id(BPt), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115606))

	def test_21530115607(self):
		input = '''
string gL[88.87,13.9]
func dR (bool j3w, bool Gaf[5.17,71.87], string u5J[89.07,90.73])	begin
		begin
		end
	end
dynamic rYEI
func jW3 (number sh[43.97,34.9,70.61], bool mn[20.62,66.88,91.38], bool off)
	return
'''
		expect = '''Program([VarDecl(Id(gL), ArrayType([88.87, 13.9], StringType), None, None), FuncDecl(Id(dR), [VarDecl(Id(j3w), BoolType, None, None), VarDecl(Id(Gaf), ArrayType([5.17, 71.87], BoolType), None, None), VarDecl(Id(u5J), ArrayType([89.07, 90.73], StringType), None, None)], Block([Block([])])), VarDecl(Id(rYEI), None, dynamic, None), FuncDecl(Id(jW3), [VarDecl(Id(sh), ArrayType([43.97, 34.9, 70.61], NumberType), None, None), VarDecl(Id(mn), ArrayType([20.62, 66.88, 91.38], BoolType), None, None), VarDecl(Id(off), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115607))

	def test_21530115608(self):
		input = '''
func qA ()
	return "DXhc"
string JPrW[33.03,23.05] <- Lsd
func D8 (bool xPft, bool tmq, bool nZZH)	return
number na
bool Kdz[66.33,61.13] <- true
'''
		expect = '''Program([FuncDecl(Id(qA), [], Return(StringLit(DXhc))), VarDecl(Id(JPrW), ArrayType([33.03, 23.05], StringType), None, Id(Lsd)), FuncDecl(Id(D8), [VarDecl(Id(xPft), BoolType, None, None), VarDecl(Id(tmq), BoolType, None, None), VarDecl(Id(nZZH), BoolType, None, None)], Return()), VarDecl(Id(na), NumberType, None, None), VarDecl(Id(Kdz), ArrayType([66.33, 61.13], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115608))

	def test_21530115609(self):
		input = '''
func ou (number NPt2[17.13,24.31], string gsm, number v8)	return

func on ()	begin
		dBI <- LvT
		XyYU <- 91.16
		Hejs()
	end

'''
		expect = '''Program([FuncDecl(Id(ou), [VarDecl(Id(NPt2), ArrayType([17.13, 24.31], NumberType), None, None), VarDecl(Id(gsm), StringType, None, None), VarDecl(Id(v8), NumberType, None, None)], Return()), FuncDecl(Id(on), [], Block([AssignStmt(Id(dBI), Id(LvT)), AssignStmt(Id(XyYU), NumLit(91.16)), CallStmt(Id(Hejs), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115609))

	def test_21530115610(self):
		input = '''
var wbLG <- true
func aW (number bJ[97.77,11.82,3.28], number fVj6, number YFf[34.79])
	return 5.42

bool DrZ <- 37.13
number Iub[7.29,13.32,50.58] <- eN
bool qGK[33.94,25.38]
'''
		expect = '''Program([VarDecl(Id(wbLG), None, var, BooleanLit(True)), FuncDecl(Id(aW), [VarDecl(Id(bJ), ArrayType([97.77, 11.82, 3.28], NumberType), None, None), VarDecl(Id(fVj6), NumberType, None, None), VarDecl(Id(YFf), ArrayType([34.79], NumberType), None, None)], Return(NumLit(5.42))), VarDecl(Id(DrZ), BoolType, None, NumLit(37.13)), VarDecl(Id(Iub), ArrayType([7.29, 13.32, 50.58], NumberType), None, Id(eN)), VarDecl(Id(qGK), ArrayType([33.94, 25.38], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115610))

	def test_21530115611(self):
		input = '''
func khl4 (string h9XZ, string Jwt[47.13,69.58])	return
string wR0[8.62,57.55,49.23] <- "RensT"
func Xee1 ()	begin
		break
	end
func xq0 ()
	begin
		Raif("Ts", "gId", true)
		return "LgWS"
	end

func nW9 (bool W9z[97.2,19.07,37.03], number Q0)	return
'''
		expect = '''Program([FuncDecl(Id(khl4), [VarDecl(Id(h9XZ), StringType, None, None), VarDecl(Id(Jwt), ArrayType([47.13, 69.58], StringType), None, None)], Return()), VarDecl(Id(wR0), ArrayType([8.62, 57.55, 49.23], StringType), None, StringLit(RensT)), FuncDecl(Id(Xee1), [], Block([Break])), FuncDecl(Id(xq0), [], Block([CallStmt(Id(Raif), [StringLit(Ts), StringLit(gId), BooleanLit(True)]), Return(StringLit(LgWS))])), FuncDecl(Id(nW9), [VarDecl(Id(W9z), ArrayType([97.2, 19.07, 37.03], BoolType), None, None), VarDecl(Id(Q0), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115611))

	def test_21530115612(self):
		input = '''
func AFAK (number jQa)
	begin
		Vv[o8, true] <- true
		continue
		n8(BtU)
	end

func gf (number JY[86.47,64.39])	return

'''
		expect = '''Program([FuncDecl(Id(AFAK), [VarDecl(Id(jQa), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(Vv), [Id(o8), BooleanLit(True)]), BooleanLit(True)), Continue, CallStmt(Id(n8), [Id(BtU)])])), FuncDecl(Id(gf), [VarDecl(Id(JY), ArrayType([86.47, 64.39], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115612))

	def test_21530115613(self):
		input = '''
bool Uct[70.01]
'''
		expect = '''Program([VarDecl(Id(Uct), ArrayType([70.01], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115613))

	def test_21530115614(self):
		input = '''
func XNR (string y3y, string pxk_, string wS3)	return 76.21
func JHbR (string gNB2[95.33,91.57], string dHj[77.43])	begin
		return
		break
		break
	end
func OdJo (number ongL[71.96,78.34], string lR, number kAm[56.89])	return FU
'''
		expect = '''Program([FuncDecl(Id(XNR), [VarDecl(Id(y3y), StringType, None, None), VarDecl(Id(pxk_), StringType, None, None), VarDecl(Id(wS3), StringType, None, None)], Return(NumLit(76.21))), FuncDecl(Id(JHbR), [VarDecl(Id(gNB2), ArrayType([95.33, 91.57], StringType), None, None), VarDecl(Id(dHj), ArrayType([77.43], StringType), None, None)], Block([Return(), Break, Break])), FuncDecl(Id(OdJo), [VarDecl(Id(ongL), ArrayType([71.96, 78.34], NumberType), None, None), VarDecl(Id(lR), StringType, None, None), VarDecl(Id(kAm), ArrayType([56.89], NumberType), None, None)], Return(Id(FU)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115614))

	def test_21530115615(self):
		input = '''
number HL[29.85,11.96]
bool hvLs[95.69,79.87,59.24]
func LiK ()	begin
		begin
			Zk(beKd)
			OqK0 <- 29.13
			break
		end
		if (18.8) for O2P until lYQ by "XxYO"
			AYa[false] <- 38.92
		elif ("GYER")
		break
		elif (84.71) break
		elif (true)
		for iqz until dMOX by true
			break
		elif (61.04)
		Yv[8.21, gH8] <- true
		elif ("FCRg")
		return
		else continue
		continue
	end
'''
		expect = '''Program([VarDecl(Id(HL), ArrayType([29.85, 11.96], NumberType), None, None), VarDecl(Id(hvLs), ArrayType([95.69, 79.87, 59.24], BoolType), None, None), FuncDecl(Id(LiK), [], Block([Block([CallStmt(Id(Zk), [Id(beKd)]), AssignStmt(Id(OqK0), NumLit(29.13)), Break]), If(NumLit(18.8), For(Id(O2P), Id(lYQ), StringLit(XxYO), AssignStmt(ArrayCell(Id(AYa), [BooleanLit(False)]), NumLit(38.92)))), [(StringLit(GYER), Break), (NumLit(84.71), Break), (BooleanLit(True), For(Id(iqz), Id(dMOX), BooleanLit(True), Break)), (NumLit(61.04), AssignStmt(ArrayCell(Id(Yv), [NumLit(8.21), Id(gH8)]), BooleanLit(True))), (StringLit(FCRg), Return())], Continue, Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115615))

	def test_21530115616(self):
		input = '''
dynamic JEQ2
bool Bs <- false
func Cujk (bool x_3L, string zpD[8.98])	return "z"

'''
		expect = '''Program([VarDecl(Id(JEQ2), None, dynamic, None), VarDecl(Id(Bs), BoolType, None, BooleanLit(False)), FuncDecl(Id(Cujk), [VarDecl(Id(x_3L), BoolType, None, None), VarDecl(Id(zpD), ArrayType([8.98], StringType), None, None)], Return(StringLit(z)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115616))

	def test_21530115617(self):
		input = '''
dynamic AY
string DZ
'''
		expect = '''Program([VarDecl(Id(AY), None, dynamic, None), VarDecl(Id(DZ), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115617))

	def test_21530115618(self):
		input = '''
func V_Hn (string C_[81.49], string mmtF[22.82,19.55], bool H7)	begin
		dXF(xDVf, kRfx, U1W)
		string b4[21.79,88.58,90.04]
	end
func Sqp (bool e8cv[0.9,72.34,10.53], string N8A, bool gbr3[26.65,97.39,58.85])	return
number Cb <- "xZ"
number Lt[47.25,55.31]
func YY (bool VX[6.42,99.11,64.85], string E_l)
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(V_Hn), [VarDecl(Id(C_), ArrayType([81.49], StringType), None, None), VarDecl(Id(mmtF), ArrayType([22.82, 19.55], StringType), None, None), VarDecl(Id(H7), BoolType, None, None)], Block([CallStmt(Id(dXF), [Id(xDVf), Id(kRfx), Id(U1W)]), VarDecl(Id(b4), ArrayType([21.79, 88.58, 90.04], StringType), None, None)])), FuncDecl(Id(Sqp), [VarDecl(Id(e8cv), ArrayType([0.9, 72.34, 10.53], BoolType), None, None), VarDecl(Id(N8A), StringType, None, None), VarDecl(Id(gbr3), ArrayType([26.65, 97.39, 58.85], BoolType), None, None)], Return()), VarDecl(Id(Cb), NumberType, None, StringLit(xZ)), VarDecl(Id(Lt), ArrayType([47.25, 55.31], NumberType), None, None), FuncDecl(Id(YY), [VarDecl(Id(VX), ArrayType([6.42, 99.11, 64.85], BoolType), None, None), VarDecl(Id(E_l), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115618))

	def test_21530115619(self):
		input = '''
func M9SI (bool mK[74.91], bool em)
	return "OtFca"

func SxCq (number Yz[69.93])	begin
		qip <- false
		return fn
	end

func nMgQ (bool Oy[60.89,10.55,87.98])	begin
	end
'''
		expect = '''Program([FuncDecl(Id(M9SI), [VarDecl(Id(mK), ArrayType([74.91], BoolType), None, None), VarDecl(Id(em), BoolType, None, None)], Return(StringLit(OtFca))), FuncDecl(Id(SxCq), [VarDecl(Id(Yz), ArrayType([69.93], NumberType), None, None)], Block([AssignStmt(Id(qip), BooleanLit(False)), Return(Id(fn))])), FuncDecl(Id(nMgQ), [VarDecl(Id(Oy), ArrayType([60.89, 10.55, 87.98], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115619))

	def test_21530115620(self):
		input = '''
string lu[22.77,72.74] <- X8x6
'''
		expect = '''Program([VarDecl(Id(lu), ArrayType([22.77, 72.74], StringType), None, Id(X8x6))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115620))

	def test_21530115621(self):
		input = '''
func yAH (bool VB[65.15,20.25])	begin
		Bd <- false
	end

'''
		expect = '''Program([FuncDecl(Id(yAH), [VarDecl(Id(VB), ArrayType([65.15, 20.25], BoolType), None, None)], Block([AssignStmt(Id(Bd), BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115621))

	def test_21530115622(self):
		input = '''
func k4JM (string HEh8, string UQ)	return
bool djUK <- "Q"
number jxsP[24.01]
number L8
'''
		expect = '''Program([FuncDecl(Id(k4JM), [VarDecl(Id(HEh8), StringType, None, None), VarDecl(Id(UQ), StringType, None, None)], Return()), VarDecl(Id(djUK), BoolType, None, StringLit(Q)), VarDecl(Id(jxsP), ArrayType([24.01], NumberType), None, None), VarDecl(Id(L8), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115622))

	def test_21530115623(self):
		input = '''
func ops (number yJVc[66.78,80.72])
	begin
	end

func orkJ (bool KCQy)	return
string qf[63.37,33.65]
number T5[7.96,82.25]
func kS (number AQ, bool kT[60.69])	begin
	end
'''
		expect = '''Program([FuncDecl(Id(ops), [VarDecl(Id(yJVc), ArrayType([66.78, 80.72], NumberType), None, None)], Block([])), FuncDecl(Id(orkJ), [VarDecl(Id(KCQy), BoolType, None, None)], Return()), VarDecl(Id(qf), ArrayType([63.37, 33.65], StringType), None, None), VarDecl(Id(T5), ArrayType([7.96, 82.25], NumberType), None, None), FuncDecl(Id(kS), [VarDecl(Id(AQ), NumberType, None, None), VarDecl(Id(kT), ArrayType([60.69], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115623))

	def test_21530115624(self):
		input = '''
func pv (string AtZ, bool pU[60.69])
	begin
		continue
	end

func RO (bool WGb, string FN[81.22,20.06])
	begin
	end

func Fbp (number Bsd)
	return

func dnCC (bool mXpE, bool G2[73.97])
	return yNfI
number Mlk9
'''
		expect = '''Program([FuncDecl(Id(pv), [VarDecl(Id(AtZ), StringType, None, None), VarDecl(Id(pU), ArrayType([60.69], BoolType), None, None)], Block([Continue])), FuncDecl(Id(RO), [VarDecl(Id(WGb), BoolType, None, None), VarDecl(Id(FN), ArrayType([81.22, 20.06], StringType), None, None)], Block([])), FuncDecl(Id(Fbp), [VarDecl(Id(Bsd), NumberType, None, None)], Return()), FuncDecl(Id(dnCC), [VarDecl(Id(mXpE), BoolType, None, None), VarDecl(Id(G2), ArrayType([73.97], BoolType), None, None)], Return(Id(yNfI))), VarDecl(Id(Mlk9), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115624))

	def test_21530115625(self):
		input = '''
string Xm
func afdT (bool zwER, number XkR6, number Tt[9.16,91.41,78.07])
	begin
		l1(false)
		continue
		for Mt5 until Dg3j by false
			break
	end
func Y1u (bool TBe, number qE[30.19], bool Cg[6.28,89.39,91.21])	return

'''
		expect = '''Program([VarDecl(Id(Xm), StringType, None, None), FuncDecl(Id(afdT), [VarDecl(Id(zwER), BoolType, None, None), VarDecl(Id(XkR6), NumberType, None, None), VarDecl(Id(Tt), ArrayType([9.16, 91.41, 78.07], NumberType), None, None)], Block([CallStmt(Id(l1), [BooleanLit(False)]), Continue, For(Id(Mt5), Id(Dg3j), BooleanLit(False), Break)])), FuncDecl(Id(Y1u), [VarDecl(Id(TBe), BoolType, None, None), VarDecl(Id(qE), ArrayType([30.19], NumberType), None, None), VarDecl(Id(Cg), ArrayType([6.28, 89.39, 91.21], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115625))

	def test_21530115626(self):
		input = '''
func QT (bool vLO[40.69], number QZkg[90.11,35.5], number Cf)
	begin
		if ("kHGJB")
		continue
		Png(67.32, "YF", false)
	end

string weZC[30.99]
bool Nra[44.76,46.84]
number Gnp
'''
		expect = '''Program([FuncDecl(Id(QT), [VarDecl(Id(vLO), ArrayType([40.69], BoolType), None, None), VarDecl(Id(QZkg), ArrayType([90.11, 35.5], NumberType), None, None), VarDecl(Id(Cf), NumberType, None, None)], Block([If(StringLit(kHGJB), Continue), [], None, CallStmt(Id(Png), [NumLit(67.32), StringLit(YF), BooleanLit(False)])])), VarDecl(Id(weZC), ArrayType([30.99], StringType), None, None), VarDecl(Id(Nra), ArrayType([44.76, 46.84], BoolType), None, None), VarDecl(Id(Gnp), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115626))

	def test_21530115627(self):
		input = '''
func wDs (string sc[9.13,89.81,48.74], number tlug)
	return
number PAr[95.04] <- "IDAiw"
func Dd ()	begin
		fWNR <- true
		u8x <- azg
		QR <- SXW
	end
var gp <- aR
func UM (bool Frf)	begin
		BNz_ <- false
		continue
		bool sp[17.61,56.57]
	end
'''
		expect = '''Program([FuncDecl(Id(wDs), [VarDecl(Id(sc), ArrayType([9.13, 89.81, 48.74], StringType), None, None), VarDecl(Id(tlug), NumberType, None, None)], Return()), VarDecl(Id(PAr), ArrayType([95.04], NumberType), None, StringLit(IDAiw)), FuncDecl(Id(Dd), [], Block([AssignStmt(Id(fWNR), BooleanLit(True)), AssignStmt(Id(u8x), Id(azg)), AssignStmt(Id(QR), Id(SXW))])), VarDecl(Id(gp), None, var, Id(aR)), FuncDecl(Id(UM), [VarDecl(Id(Frf), BoolType, None, None)], Block([AssignStmt(Id(BNz_), BooleanLit(False)), Continue, VarDecl(Id(sp), ArrayType([17.61, 56.57], BoolType), None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115627))

	def test_21530115628(self):
		input = '''
func ylDV (string rJ, string oCt)	return "xVOn"
func qv6s (string qOx, bool fPJx, bool q3sZ)	return 13.28
func VdJc (number eB14, bool R4vz[31.94,29.2,89.11])	return
func Iv (bool Dti2[31.12], string IT, number Eo1[71.82])
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(ylDV), [VarDecl(Id(rJ), StringType, None, None), VarDecl(Id(oCt), StringType, None, None)], Return(StringLit(xVOn))), FuncDecl(Id(qv6s), [VarDecl(Id(qOx), StringType, None, None), VarDecl(Id(fPJx), BoolType, None, None), VarDecl(Id(q3sZ), BoolType, None, None)], Return(NumLit(13.28))), FuncDecl(Id(VdJc), [VarDecl(Id(eB14), NumberType, None, None), VarDecl(Id(R4vz), ArrayType([31.94, 29.2, 89.11], BoolType), None, None)], Return()), FuncDecl(Id(Iv), [VarDecl(Id(Dti2), ArrayType([31.12], BoolType), None, None), VarDecl(Id(IT), StringType, None, None), VarDecl(Id(Eo1), ArrayType([71.82], NumberType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115628))

	def test_21530115629(self):
		input = '''
dynamic PF_
'''
		expect = '''Program([VarDecl(Id(PF_), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115629))

	def test_21530115630(self):
		input = '''
func zkd6 (string DFg[27.7,54.76])
	begin
		bool P9fF <- false
		if (z6Jq)
		number i21F[43.35,35.5] <- XO7Y
		elif (rz) begin
			bCg <- "a"
		end
		elif (4.4)
		return
		elif (false)
		PdYV(10.4, 5.12)
		break
	end

'''
		expect = '''Program([FuncDecl(Id(zkd6), [VarDecl(Id(DFg), ArrayType([27.7, 54.76], StringType), None, None)], Block([VarDecl(Id(P9fF), BoolType, None, BooleanLit(False)), If(Id(z6Jq), VarDecl(Id(i21F), ArrayType([43.35, 35.5], NumberType), None, Id(XO7Y))), [(Id(rz), Block([AssignStmt(Id(bCg), StringLit(a))])), (NumLit(4.4), Return()), (BooleanLit(False), CallStmt(Id(PdYV), [NumLit(10.4), NumLit(5.12)]))], None, Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115630))

	def test_21530115631(self):
		input = '''
number Zl[17.04,71.97,87.52]
func XN (string Sno, number QN6)	begin
		for E1 until "dV" by true
			for rX until "ja" by true
				begin
					for jD until "PYJNJ" by Nj
						Mwu("gRIS", "vl")
					for omfC until "R" by false
						begin
							bool cTp[63.51,63.3] <- iO
							for L6QE until "Muuf" by false
								begin
									return 21.96
								end
							return
						end
					for UR until "VJdyw" by 5.8
						if ("F") begin
							r4n <- "WWBJF"
							return true
							w3()
						end
						elif ("Kg")
						begin
							if (TXp) bool os
						end
				end
	end
var Wp40 <- "d"
'''
		expect = '''Program([VarDecl(Id(Zl), ArrayType([17.04, 71.97, 87.52], NumberType), None, None), FuncDecl(Id(XN), [VarDecl(Id(Sno), StringType, None, None), VarDecl(Id(QN6), NumberType, None, None)], Block([For(Id(E1), StringLit(dV), BooleanLit(True), For(Id(rX), StringLit(ja), BooleanLit(True), Block([For(Id(jD), StringLit(PYJNJ), Id(Nj), CallStmt(Id(Mwu), [StringLit(gRIS), StringLit(vl)])), For(Id(omfC), StringLit(R), BooleanLit(False), Block([VarDecl(Id(cTp), ArrayType([63.51, 63.3], BoolType), None, Id(iO)), For(Id(L6QE), StringLit(Muuf), BooleanLit(False), Block([Return(NumLit(21.96))])), Return()])), For(Id(UR), StringLit(VJdyw), NumLit(5.8), If(StringLit(F), Block([AssignStmt(Id(r4n), StringLit(WWBJF)), Return(BooleanLit(True)), CallStmt(Id(w3), [])])), [(StringLit(Kg), Block([If(Id(TXp), VarDecl(Id(os), BoolType, None, None)), [], None]))], None)])))])), VarDecl(Id(Wp40), None, var, StringLit(d))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115631))

	def test_21530115632(self):
		input = '''
func mvk (string lfF[86.24,46.31,20.91])
	return

func g_D ()
	return 8.47
'''
		expect = '''Program([FuncDecl(Id(mvk), [VarDecl(Id(lfF), ArrayType([86.24, 46.31, 20.91], StringType), None, None)], Return()), FuncDecl(Id(g_D), [], Return(NumLit(8.47)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115632))

	def test_21530115633(self):
		input = '''
number CxJ[13.78,43.68,16.93] <- true
number Wv[38.53]
number DeG <- false
bool kDgS[22.48,47.75,10.29] <- "fI"
'''
		expect = '''Program([VarDecl(Id(CxJ), ArrayType([13.78, 43.68, 16.93], NumberType), None, BooleanLit(True)), VarDecl(Id(Wv), ArrayType([38.53], NumberType), None, None), VarDecl(Id(DeG), NumberType, None, BooleanLit(False)), VarDecl(Id(kDgS), ArrayType([22.48, 47.75, 10.29], BoolType), None, StringLit(fI))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115633))

	def test_21530115634(self):
		input = '''
number BlPj
func OQH (number XC_[32.52,56.83], bool KW[95.55,97.51,76.35], number jUcm)	return "R"

'''
		expect = '''Program([VarDecl(Id(BlPj), NumberType, None, None), FuncDecl(Id(OQH), [VarDecl(Id(XC_), ArrayType([32.52, 56.83], NumberType), None, None), VarDecl(Id(KW), ArrayType([95.55, 97.51, 76.35], BoolType), None, None), VarDecl(Id(jUcm), NumberType, None, None)], Return(StringLit(R)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115634))

	def test_21530115635(self):
		input = '''
func NJU4 (bool Jf[3.94], string mo)
	return
string GPKC <- 62.54
func XbL (number RD3N, number VQxU[25.7], number n1[85.45,25.84,77.66])	begin
		uX("O")
	end
'''
		expect = '''Program([FuncDecl(Id(NJU4), [VarDecl(Id(Jf), ArrayType([3.94], BoolType), None, None), VarDecl(Id(mo), StringType, None, None)], Return()), VarDecl(Id(GPKC), StringType, None, NumLit(62.54)), FuncDecl(Id(XbL), [VarDecl(Id(RD3N), NumberType, None, None), VarDecl(Id(VQxU), ArrayType([25.7], NumberType), None, None), VarDecl(Id(n1), ArrayType([85.45, 25.84, 77.66], NumberType), None, None)], Block([CallStmt(Id(uX), [StringLit(O)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115635))

	def test_21530115636(self):
		input = '''
number NhF8[2.76,58.47,73.88] <- false
'''
		expect = '''Program([VarDecl(Id(NhF8), ArrayType([2.76, 58.47, 73.88], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115636))

	def test_21530115637(self):
		input = '''
string NI[49.29]
'''
		expect = '''Program([VarDecl(Id(NI), ArrayType([49.29], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115637))

	def test_21530115638(self):
		input = '''
func wsv (number hggg, number BJ[39.16])
	return 42.0

'''
		expect = '''Program([FuncDecl(Id(wsv), [VarDecl(Id(hggg), NumberType, None, None), VarDecl(Id(BJ), ArrayType([39.16], NumberType), None, None)], Return(NumLit(42.0)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115638))

	def test_21530115639(self):
		input = '''
func yLe (bool HS, string t8, number JLng)
	return
func t0c (string NE5[35.49], number FVjH[18.93], bool uG)
	return "nFO"

'''
		expect = '''Program([FuncDecl(Id(yLe), [VarDecl(Id(HS), BoolType, None, None), VarDecl(Id(t8), StringType, None, None), VarDecl(Id(JLng), NumberType, None, None)], Return()), FuncDecl(Id(t0c), [VarDecl(Id(NE5), ArrayType([35.49], StringType), None, None), VarDecl(Id(FVjH), ArrayType([18.93], NumberType), None, None), VarDecl(Id(uG), BoolType, None, None)], Return(StringLit(nFO)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115639))

	def test_21530115640(self):
		input = '''
func iA (string i4_[51.92,8.53,92.18], bool QT[19.17], number nP[58.01,80.14])
	return

'''
		expect = '''Program([FuncDecl(Id(iA), [VarDecl(Id(i4_), ArrayType([51.92, 8.53, 92.18], StringType), None, None), VarDecl(Id(QT), ArrayType([19.17], BoolType), None, None), VarDecl(Id(nP), ArrayType([58.01, 80.14], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115640))

	def test_21530115641(self):
		input = '''
string yifs[52.35,89.47,80.59] <- 35.89
bool JIRy <- true
string oJf[98.01,48.54,3.22]
var toI <- "qKPw"
number uh
'''
		expect = '''Program([VarDecl(Id(yifs), ArrayType([52.35, 89.47, 80.59], StringType), None, NumLit(35.89)), VarDecl(Id(JIRy), BoolType, None, BooleanLit(True)), VarDecl(Id(oJf), ArrayType([98.01, 48.54, 3.22], StringType), None, None), VarDecl(Id(toI), None, var, StringLit(qKPw)), VarDecl(Id(uh), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115641))

	def test_21530115642(self):
		input = '''
bool QM[7.61,95.09,65.18] <- "Wb"
dynamic zHRA
func tF (bool dwn)
	return

'''
		expect = '''Program([VarDecl(Id(QM), ArrayType([7.61, 95.09, 65.18], BoolType), None, StringLit(Wb)), VarDecl(Id(zHRA), None, dynamic, None), FuncDecl(Id(tF), [VarDecl(Id(dwn), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115642))

	def test_21530115643(self):
		input = '''
string G7
bool EG
number u5y[56.15,9.8,91.71]
func Iu8 (bool jgA2, number POL[44.87], string VBnl[48.99])	return
bool lnS[67.96,44.09,35.95] <- 4.08
'''
		expect = '''Program([VarDecl(Id(G7), StringType, None, None), VarDecl(Id(EG), BoolType, None, None), VarDecl(Id(u5y), ArrayType([56.15, 9.8, 91.71], NumberType), None, None), FuncDecl(Id(Iu8), [VarDecl(Id(jgA2), BoolType, None, None), VarDecl(Id(POL), ArrayType([44.87], NumberType), None, None), VarDecl(Id(VBnl), ArrayType([48.99], StringType), None, None)], Return()), VarDecl(Id(lnS), ArrayType([67.96, 44.09, 35.95], BoolType), None, NumLit(4.08))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115643))

	def test_21530115644(self):
		input = '''
func co (string jb8[2.95,59.3], number mP)
	return

'''
		expect = '''Program([FuncDecl(Id(co), [VarDecl(Id(jb8), ArrayType([2.95, 59.3], StringType), None, None), VarDecl(Id(mP), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115644))

	def test_21530115645(self):
		input = '''
string Wo
'''
		expect = '''Program([VarDecl(Id(Wo), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115645))

	def test_21530115646(self):
		input = '''
func Ld ()	return msqh
number m5U
bool MZ <- 26.75
func pd (string kF, string bYKW)
	return ghC

func XX (number ap)	return 19.25
'''
		expect = '''Program([FuncDecl(Id(Ld), [], Return(Id(msqh))), VarDecl(Id(m5U), NumberType, None, None), VarDecl(Id(MZ), BoolType, None, NumLit(26.75)), FuncDecl(Id(pd), [VarDecl(Id(kF), StringType, None, None), VarDecl(Id(bYKW), StringType, None, None)], Return(Id(ghC))), FuncDecl(Id(XX), [VarDecl(Id(ap), NumberType, None, None)], Return(NumLit(19.25)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115646))

	def test_21530115647(self):
		input = '''
string kNL[84.19,43.19,91.76]
dynamic ihE9
var IoMh <- true
'''
		expect = '''Program([VarDecl(Id(kNL), ArrayType([84.19, 43.19, 91.76], StringType), None, None), VarDecl(Id(ihE9), None, dynamic, None), VarDecl(Id(IoMh), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115647))

	def test_21530115648(self):
		input = '''
number sFh <- HH
bool VYM <- zb
func rL6t (string LV, number Sz)
	return true

dynamic ZuA <- 84.64
'''
		expect = '''Program([VarDecl(Id(sFh), NumberType, None, Id(HH)), VarDecl(Id(VYM), BoolType, None, Id(zb)), FuncDecl(Id(rL6t), [VarDecl(Id(LV), StringType, None, None), VarDecl(Id(Sz), NumberType, None, None)], Return(BooleanLit(True))), VarDecl(Id(ZuA), None, dynamic, NumLit(84.64))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115648))

	def test_21530115649(self):
		input = '''
bool Khp9
'''
		expect = '''Program([VarDecl(Id(Khp9), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115649))

	def test_21530115650(self):
		input = '''
func cK (number aS6m, string xL)
	begin
		break
		for wJ until 6.76 by 95.02
			return
		continue
	end
var FA <- nX
bool xj
'''
		expect = '''Program([FuncDecl(Id(cK), [VarDecl(Id(aS6m), NumberType, None, None), VarDecl(Id(xL), StringType, None, None)], Block([Break, For(Id(wJ), NumLit(6.76), NumLit(95.02), Return()), Continue])), VarDecl(Id(FA), None, var, Id(nX)), VarDecl(Id(xj), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115650))

	def test_21530115651(self):
		input = '''
func ik (string ugT)	return "c"

'''
		expect = '''Program([FuncDecl(Id(ik), [VarDecl(Id(ugT), StringType, None, None)], Return(StringLit(c)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115651))

	def test_21530115652(self):
		input = '''
number Fy <- K6ob
func SoP (string IJS, string JcV[60.77,57.98,2.24])
	return false

string Tt <- "wWR"
func ny (bool Okh)	return o_FX
func Boxo (bool Kg96[6.55])
	begin
		begin
			break
		end
		owf(XD5P)
		if (rbj) CL[qF] <- cIU
		elif (false)
		string WL <- "ObTE"
		elif (36.81) WcE("Eble")
		elif (DFB) begin
			continue
			gy <- CCkm
		end
		elif (85.15) return
		else EJgG("NY", fGaz)
	end
'''
		expect = '''Program([VarDecl(Id(Fy), NumberType, None, Id(K6ob)), FuncDecl(Id(SoP), [VarDecl(Id(IJS), StringType, None, None), VarDecl(Id(JcV), ArrayType([60.77, 57.98, 2.24], StringType), None, None)], Return(BooleanLit(False))), VarDecl(Id(Tt), StringType, None, StringLit(wWR)), FuncDecl(Id(ny), [VarDecl(Id(Okh), BoolType, None, None)], Return(Id(o_FX))), FuncDecl(Id(Boxo), [VarDecl(Id(Kg96), ArrayType([6.55], BoolType), None, None)], Block([Block([Break]), CallStmt(Id(owf), [Id(XD5P)]), If(Id(rbj), AssignStmt(ArrayCell(Id(CL), [Id(qF)]), Id(cIU))), [(BooleanLit(False), VarDecl(Id(WL), StringType, None, StringLit(ObTE))), (NumLit(36.81), CallStmt(Id(WcE), [StringLit(Eble)])), (Id(DFB), Block([Continue, AssignStmt(Id(gy), Id(CCkm))])), (NumLit(85.15), Return())], CallStmt(Id(EJgG), [StringLit(NY), Id(fGaz)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115652))

	def test_21530115653(self):
		input = '''
string DHkd
func z1Xn (number MGU, string oT[90.24])
	begin
		continue
		return
	end
string xcM1[75.26,61.77,87.16] <- true
'''
		expect = '''Program([VarDecl(Id(DHkd), StringType, None, None), FuncDecl(Id(z1Xn), [VarDecl(Id(MGU), NumberType, None, None), VarDecl(Id(oT), ArrayType([90.24], StringType), None, None)], Block([Continue, Return()])), VarDecl(Id(xcM1), ArrayType([75.26, 61.77, 87.16], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115653))

	def test_21530115654(self):
		input = '''
bool vdL[57.85]
func FtmZ (number sXV[54.96,21.81], string nR[83.51,39.15])	return

'''
		expect = '''Program([VarDecl(Id(vdL), ArrayType([57.85], BoolType), None, None), FuncDecl(Id(FtmZ), [VarDecl(Id(sXV), ArrayType([54.96, 21.81], NumberType), None, None), VarDecl(Id(nR), ArrayType([83.51, 39.15], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115654))

	def test_21530115655(self):
		input = '''
func ETzz (string MD, string MiUs[45.37], number e3K)	return 51.56
func ZUU (bool jm[8.81,47.52], bool OOy)	return true
'''
		expect = '''Program([FuncDecl(Id(ETzz), [VarDecl(Id(MD), StringType, None, None), VarDecl(Id(MiUs), ArrayType([45.37], StringType), None, None), VarDecl(Id(e3K), NumberType, None, None)], Return(NumLit(51.56))), FuncDecl(Id(ZUU), [VarDecl(Id(jm), ArrayType([8.81, 47.52], BoolType), None, None), VarDecl(Id(OOy), BoolType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115655))

	def test_21530115656(self):
		input = '''
func eTd3 (number y9QV[57.97], string VQam[23.02,78.77,79.49], number gZ0P[85.91,96.19,83.5])
	return

bool mK[81.01] <- 79.86
func lPZ ()
	begin
		begin
			xj("LC")
		end
	end
string ll[54.57,12.06,21.43] <- T2
func ABT (bool x1[7.93,65.79], bool g3_[73.63,33.88], number bFb)
	begin
		Oq(false)
		break
		break
	end

'''
		expect = '''Program([FuncDecl(Id(eTd3), [VarDecl(Id(y9QV), ArrayType([57.97], NumberType), None, None), VarDecl(Id(VQam), ArrayType([23.02, 78.77, 79.49], StringType), None, None), VarDecl(Id(gZ0P), ArrayType([85.91, 96.19, 83.5], NumberType), None, None)], Return()), VarDecl(Id(mK), ArrayType([81.01], BoolType), None, NumLit(79.86)), FuncDecl(Id(lPZ), [], Block([Block([CallStmt(Id(xj), [StringLit(LC)])])])), VarDecl(Id(ll), ArrayType([54.57, 12.06, 21.43], StringType), None, Id(T2)), FuncDecl(Id(ABT), [VarDecl(Id(x1), ArrayType([7.93, 65.79], BoolType), None, None), VarDecl(Id(g3_), ArrayType([73.63, 33.88], BoolType), None, None), VarDecl(Id(bFb), NumberType, None, None)], Block([CallStmt(Id(Oq), [BooleanLit(False)]), Break, Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115656))

	def test_21530115657(self):
		input = '''
bool P68O
number G_[91.41,61.01]
func pm (number Ms, number bGu2[62.6,19.57])	return

'''
		expect = '''Program([VarDecl(Id(P68O), BoolType, None, None), VarDecl(Id(G_), ArrayType([91.41, 61.01], NumberType), None, None), FuncDecl(Id(pm), [VarDecl(Id(Ms), NumberType, None, None), VarDecl(Id(bGu2), ArrayType([62.6, 19.57], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115657))

	def test_21530115658(self):
		input = '''
var Rh <- true
string bE4[48.31]
func R2 (bool irwV[42.61,76.94])
	begin
		if (mCa) bool lk_[55.11,50.2,0.53]
		elif (false) break
		elif (false)
		if (79.39)
		break
		elif (cauQ)
		break
		elif (2.86)
		for EsW until "ADWq" by true
			for MMK5 until 10.77 by M9B
				bool D9ar[79.95,9.73,52.53] <- 0.13
		elif (false)
		GU5()
		elif ("e")
		return
		elif (false) if (61.97) oPA[58.29, true, true] <- 30.09
		else break
		elif ("ZH") begin
		end
		elif (17.38)
		P5y["fv", "veWf"] <- R2mm
		bool zH8
	end

func t55 ()
	begin
	end
'''
		expect = '''Program([VarDecl(Id(Rh), None, var, BooleanLit(True)), VarDecl(Id(bE4), ArrayType([48.31], StringType), None, None), FuncDecl(Id(R2), [VarDecl(Id(irwV), ArrayType([42.61, 76.94], BoolType), None, None)], Block([If(Id(mCa), VarDecl(Id(lk_), ArrayType([55.11, 50.2, 0.53], BoolType), None, None)), [(BooleanLit(False), Break), (BooleanLit(False), If(NumLit(79.39), Break), [(Id(cauQ), Break), (NumLit(2.86), For(Id(EsW), StringLit(ADWq), BooleanLit(True), For(Id(MMK5), NumLit(10.77), Id(M9B), VarDecl(Id(D9ar), ArrayType([79.95, 9.73, 52.53], BoolType), None, NumLit(0.13))))), (BooleanLit(False), CallStmt(Id(GU5), [])), (StringLit(e), Return()), (BooleanLit(False), If(NumLit(61.97), AssignStmt(ArrayCell(Id(oPA), [NumLit(58.29), BooleanLit(True), BooleanLit(True)]), NumLit(30.09))), [], Break), (StringLit(ZH), Block([]))], None), (NumLit(17.38), AssignStmt(ArrayCell(Id(P5y), [StringLit(fv), StringLit(veWf)]), Id(R2mm)))], None, VarDecl(Id(zH8), BoolType, None, None)])), FuncDecl(Id(t55), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115658))

	def test_21530115659(self):
		input = '''
func ew (number Ix[28.47,3.89], bool KX)
	begin
		continue
	end
'''
		expect = '''Program([FuncDecl(Id(ew), [VarDecl(Id(Ix), ArrayType([28.47, 3.89], NumberType), None, None), VarDecl(Id(KX), BoolType, None, None)], Block([Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115659))

	def test_21530115660(self):
		input = '''
string ctY2[43.3,34.13]
func lZz (string On7h[31.14,91.65])
	return "v"

'''
		expect = '''Program([VarDecl(Id(ctY2), ArrayType([43.3, 34.13], StringType), None, None), FuncDecl(Id(lZz), [VarDecl(Id(On7h), ArrayType([31.14, 91.65], StringType), None, None)], Return(StringLit(v)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115660))

	def test_21530115661(self):
		input = '''
bool tDl[35.61]
'''
		expect = '''Program([VarDecl(Id(tDl), ArrayType([35.61], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115661))

	def test_21530115662(self):
		input = '''
func fUTe (number n5RV[39.54], number PT[9.27], number La)	begin
		T_I <- 58.27
	end
bool loi <- false
func kw ()	return

'''
		expect = '''Program([FuncDecl(Id(fUTe), [VarDecl(Id(n5RV), ArrayType([39.54], NumberType), None, None), VarDecl(Id(PT), ArrayType([9.27], NumberType), None, None), VarDecl(Id(La), NumberType, None, None)], Block([AssignStmt(Id(T_I), NumLit(58.27))])), VarDecl(Id(loi), BoolType, None, BooleanLit(False)), FuncDecl(Id(kw), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115662))

	def test_21530115663(self):
		input = '''
string eth[29.79,14.5,34.06] <- LRh
'''
		expect = '''Program([VarDecl(Id(eth), ArrayType([29.79, 14.5, 34.06], StringType), None, Id(LRh))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115663))

	def test_21530115664(self):
		input = '''
bool HDQ
func SsG (string are6[26.3,39.44,12.1], bool go[43.31,48.86,43.73])
	return

bool TL[2.74,98.64,69.15] <- "GL"
'''
		expect = '''Program([VarDecl(Id(HDQ), BoolType, None, None), FuncDecl(Id(SsG), [VarDecl(Id(are6), ArrayType([26.3, 39.44, 12.1], StringType), None, None), VarDecl(Id(go), ArrayType([43.31, 48.86, 43.73], BoolType), None, None)], Return()), VarDecl(Id(TL), ArrayType([2.74, 98.64, 69.15], BoolType), None, StringLit(GL))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115664))

	def test_21530115665(self):
		input = '''
bool RYYV[97.0,56.99] <- AM6
'''
		expect = '''Program([VarDecl(Id(RYYV), ArrayType([97.0, 56.99], BoolType), None, Id(AM6))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115665))

	def test_21530115666(self):
		input = '''
number KZA
dynamic E3YS
func AP ()	return 0.96

string pQp
func yi ()
	begin
		return
		break
	end
'''
		expect = '''Program([VarDecl(Id(KZA), NumberType, None, None), VarDecl(Id(E3YS), None, dynamic, None), FuncDecl(Id(AP), [], Return(NumLit(0.96))), VarDecl(Id(pQp), StringType, None, None), FuncDecl(Id(yi), [], Block([Return(), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115666))

	def test_21530115667(self):
		input = '''
bool d6I[23.6,43.96,57.9]
number Vl
string dkr[17.31,58.47,54.76]
'''
		expect = '''Program([VarDecl(Id(d6I), ArrayType([23.6, 43.96, 57.9], BoolType), None, None), VarDecl(Id(Vl), NumberType, None, None), VarDecl(Id(dkr), ArrayType([17.31, 58.47, 54.76], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115667))

	def test_21530115668(self):
		input = '''
func LTV (number d2z[54.01], bool Q_PJ[58.4], bool Ej)
	begin
	end

bool BJ7W <- true
func A80i (number wfg, number Im[84.23])
	return

func Iv (bool DJv[2.52,60.93,79.77], number MX[88.84,24.99], string YzUH[70.91,57.57])	begin
	end

bool qBsP[80.05,99.71,84.03] <- true
'''
		expect = '''Program([FuncDecl(Id(LTV), [VarDecl(Id(d2z), ArrayType([54.01], NumberType), None, None), VarDecl(Id(Q_PJ), ArrayType([58.4], BoolType), None, None), VarDecl(Id(Ej), BoolType, None, None)], Block([])), VarDecl(Id(BJ7W), BoolType, None, BooleanLit(True)), FuncDecl(Id(A80i), [VarDecl(Id(wfg), NumberType, None, None), VarDecl(Id(Im), ArrayType([84.23], NumberType), None, None)], Return()), FuncDecl(Id(Iv), [VarDecl(Id(DJv), ArrayType([2.52, 60.93, 79.77], BoolType), None, None), VarDecl(Id(MX), ArrayType([88.84, 24.99], NumberType), None, None), VarDecl(Id(YzUH), ArrayType([70.91, 57.57], StringType), None, None)], Block([])), VarDecl(Id(qBsP), ArrayType([80.05, 99.71, 84.03], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115668))

	def test_21530115669(self):
		input = '''
string ITo_[69.83]
'''
		expect = '''Program([VarDecl(Id(ITo_), ArrayType([69.83], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115669))

	def test_21530115670(self):
		input = '''
number MLN
string Gc[95.02,88.14]
string sDq
func aJ (bool LFS[59.38,20.31], number waS[60.43], string PQj[73.75,48.39])
	begin
		number Jn <- Zx
	end

'''
		expect = '''Program([VarDecl(Id(MLN), NumberType, None, None), VarDecl(Id(Gc), ArrayType([95.02, 88.14], StringType), None, None), VarDecl(Id(sDq), StringType, None, None), FuncDecl(Id(aJ), [VarDecl(Id(LFS), ArrayType([59.38, 20.31], BoolType), None, None), VarDecl(Id(waS), ArrayType([60.43], NumberType), None, None), VarDecl(Id(PQj), ArrayType([73.75, 48.39], StringType), None, None)], Block([VarDecl(Id(Jn), NumberType, None, Id(Zx))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115670))

	def test_21530115671(self):
		input = '''
bool TQ[36.93,99.89,10.47]
dynamic l4Y
func VfUS (string qKg[47.24,95.91,66.91], string TMU[75.57])	return
'''
		expect = '''Program([VarDecl(Id(TQ), ArrayType([36.93, 99.89, 10.47], BoolType), None, None), VarDecl(Id(l4Y), None, dynamic, None), FuncDecl(Id(VfUS), [VarDecl(Id(qKg), ArrayType([47.24, 95.91, 66.91], StringType), None, None), VarDecl(Id(TMU), ArrayType([75.57], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115671))

	def test_21530115672(self):
		input = '''
bool QB
string zYKh <- "JT"
bool xZ[49.27,22.04]
'''
		expect = '''Program([VarDecl(Id(QB), BoolType, None, None), VarDecl(Id(zYKh), StringType, None, StringLit(JT)), VarDecl(Id(xZ), ArrayType([49.27, 22.04], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115672))

	def test_21530115673(self):
		input = '''
bool rN <- false
dynamic XA8j
func PN (number m4N, number Hhv[68.84,35.68], bool pz[41.2,28.64])
	begin
	end
string QVfe[33.38,84.48,92.17] <- 64.11
'''
		expect = '''Program([VarDecl(Id(rN), BoolType, None, BooleanLit(False)), VarDecl(Id(XA8j), None, dynamic, None), FuncDecl(Id(PN), [VarDecl(Id(m4N), NumberType, None, None), VarDecl(Id(Hhv), ArrayType([68.84, 35.68], NumberType), None, None), VarDecl(Id(pz), ArrayType([41.2, 28.64], BoolType), None, None)], Block([])), VarDecl(Id(QVfe), ArrayType([33.38, 84.48, 92.17], StringType), None, NumLit(64.11))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115673))

	def test_21530115674(self):
		input = '''
func Gm (string JI[60.65,56.55,17.75], string q8c)
	return
number b8h[26.52] <- true
func aip (string M8K2, string hC[90.78])	begin
		return Ec
		return
	end
'''
		expect = '''Program([FuncDecl(Id(Gm), [VarDecl(Id(JI), ArrayType([60.65, 56.55, 17.75], StringType), None, None), VarDecl(Id(q8c), StringType, None, None)], Return()), VarDecl(Id(b8h), ArrayType([26.52], NumberType), None, BooleanLit(True)), FuncDecl(Id(aip), [VarDecl(Id(M8K2), StringType, None, None), VarDecl(Id(hC), ArrayType([90.78], StringType), None, None)], Block([Return(Id(Ec)), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115674))

	def test_21530115675(self):
		input = '''
number ix0f[46.31,43.85]
dynamic LnI <- 62.35
func uhW (number Fm8[78.23,89.16], string REl, number Z_[65.65,1.07])
	begin
		continue
		NUML("YVU", 85.59)
	end
'''
		expect = '''Program([VarDecl(Id(ix0f), ArrayType([46.31, 43.85], NumberType), None, None), VarDecl(Id(LnI), None, dynamic, NumLit(62.35)), FuncDecl(Id(uhW), [VarDecl(Id(Fm8), ArrayType([78.23, 89.16], NumberType), None, None), VarDecl(Id(REl), StringType, None, None), VarDecl(Id(Z_), ArrayType([65.65, 1.07], NumberType), None, None)], Block([Continue, CallStmt(Id(NUML), [StringLit(YVU), NumLit(85.59)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115675))

	def test_21530115676(self):
		input = '''
func IWp ()	return "nt"
bool Ots <- "jKZU"
'''
		expect = '''Program([FuncDecl(Id(IWp), [], Return(StringLit(nt))), VarDecl(Id(Ots), BoolType, None, StringLit(jKZU))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115676))

	def test_21530115677(self):
		input = '''
func lv (bool EM, number z4q)	begin
		return
		Ur <- YY
		return "rSVcn"
	end

dynamic fD4
func XSoG ()	begin
		if (pcHg) begin
			for OcTq until II by true
				bool bAPe[22.76,54.35]
			string bic <- true
		end
		elif (false)
		continue
		bool i56[99.31]
		PM[84.37, true] <- true
	end
'''
		expect = '''Program([FuncDecl(Id(lv), [VarDecl(Id(EM), BoolType, None, None), VarDecl(Id(z4q), NumberType, None, None)], Block([Return(), AssignStmt(Id(Ur), Id(YY)), Return(StringLit(rSVcn))])), VarDecl(Id(fD4), None, dynamic, None), FuncDecl(Id(XSoG), [], Block([If(Id(pcHg), Block([For(Id(OcTq), Id(II), BooleanLit(True), VarDecl(Id(bAPe), ArrayType([22.76, 54.35], BoolType), None, None)), VarDecl(Id(bic), StringType, None, BooleanLit(True))])), [(BooleanLit(False), Continue)], None, VarDecl(Id(i56), ArrayType([99.31], BoolType), None, None), AssignStmt(ArrayCell(Id(PM), [NumLit(84.37), BooleanLit(True)]), BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115677))

	def test_21530115678(self):
		input = '''
func Dq (number BdT, string UuUK, string JXji)	return

var l7R <- "HUU"
func wp7c (number gAz4[15.28,71.55,53.83], number eeP[91.67,5.34], number yFmc[95.92])	return
func aK (string Ydp[52.27], number tbjV, string NBH[17.8])	return

'''
		expect = '''Program([FuncDecl(Id(Dq), [VarDecl(Id(BdT), NumberType, None, None), VarDecl(Id(UuUK), StringType, None, None), VarDecl(Id(JXji), StringType, None, None)], Return()), VarDecl(Id(l7R), None, var, StringLit(HUU)), FuncDecl(Id(wp7c), [VarDecl(Id(gAz4), ArrayType([15.28, 71.55, 53.83], NumberType), None, None), VarDecl(Id(eeP), ArrayType([91.67, 5.34], NumberType), None, None), VarDecl(Id(yFmc), ArrayType([95.92], NumberType), None, None)], Return()), FuncDecl(Id(aK), [VarDecl(Id(Ydp), ArrayType([52.27], StringType), None, None), VarDecl(Id(tbjV), NumberType, None, None), VarDecl(Id(NBH), ArrayType([17.8], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115678))

	def test_21530115679(self):
		input = '''
number nozS[72.59]
func TYn7 ()	return
number iA[64.66]
bool s6B[69.97,71.41]
string kc[46.56] <- OWkd
'''
		expect = '''Program([VarDecl(Id(nozS), ArrayType([72.59], NumberType), None, None), FuncDecl(Id(TYn7), [], Return()), VarDecl(Id(iA), ArrayType([64.66], NumberType), None, None), VarDecl(Id(s6B), ArrayType([69.97, 71.41], BoolType), None, None), VarDecl(Id(kc), ArrayType([46.56], StringType), None, Id(OWkd))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115679))

	def test_21530115680(self):
		input = '''
bool adAy <- 51.79
func HP ()
	return
number Xd <- "ID"
func D87 (bool MU, bool vj5Z[70.9,60.5])
	begin
		continue
	end

number Ofuh[23.97,64.66,47.73] <- hv5w
'''
		expect = '''Program([VarDecl(Id(adAy), BoolType, None, NumLit(51.79)), FuncDecl(Id(HP), [], Return()), VarDecl(Id(Xd), NumberType, None, StringLit(ID)), FuncDecl(Id(D87), [VarDecl(Id(MU), BoolType, None, None), VarDecl(Id(vj5Z), ArrayType([70.9, 60.5], BoolType), None, None)], Block([Continue])), VarDecl(Id(Ofuh), ArrayType([23.97, 64.66, 47.73], NumberType), None, Id(hv5w))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115680))

	def test_21530115681(self):
		input = '''
func dT (string B2ot[78.65,69.13,19.73])
	return
bool hqf <- "xnC"
func kmD (bool YLX[80.66,89.33])	return IVEl

'''
		expect = '''Program([FuncDecl(Id(dT), [VarDecl(Id(B2ot), ArrayType([78.65, 69.13, 19.73], StringType), None, None)], Return()), VarDecl(Id(hqf), BoolType, None, StringLit(xnC)), FuncDecl(Id(kmD), [VarDecl(Id(YLX), ArrayType([80.66, 89.33], BoolType), None, None)], Return(Id(IVEl)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115681))

	def test_21530115682(self):
		input = '''
func sMI (string MurW[28.56,54.72], number vKN[71.49,11.53,90.06], string sB)
	begin
	end
dynamic e9 <- 14.82
func fNN1 (bool GTP[64.63], number RRKA[93.97])
	return "EvjoV"
'''
		expect = '''Program([FuncDecl(Id(sMI), [VarDecl(Id(MurW), ArrayType([28.56, 54.72], StringType), None, None), VarDecl(Id(vKN), ArrayType([71.49, 11.53, 90.06], NumberType), None, None), VarDecl(Id(sB), StringType, None, None)], Block([])), VarDecl(Id(e9), None, dynamic, NumLit(14.82)), FuncDecl(Id(fNN1), [VarDecl(Id(GTP), ArrayType([64.63], BoolType), None, None), VarDecl(Id(RRKA), ArrayType([93.97], NumberType), None, None)], Return(StringLit(EvjoV)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115682))

	def test_21530115683(self):
		input = '''
bool F9S
bool lRp
'''
		expect = '''Program([VarDecl(Id(F9S), BoolType, None, None), VarDecl(Id(lRp), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115683))

	def test_21530115684(self):
		input = '''
func dj (number H7j1, string obgZ)	return "R"
func bre ()
	return wJE

bool qr[93.95,67.02] <- "RJFO"
'''
		expect = '''Program([FuncDecl(Id(dj), [VarDecl(Id(H7j1), NumberType, None, None), VarDecl(Id(obgZ), StringType, None, None)], Return(StringLit(R))), FuncDecl(Id(bre), [], Return(Id(wJE))), VarDecl(Id(qr), ArrayType([93.95, 67.02], BoolType), None, StringLit(RJFO))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115684))

	def test_21530115685(self):
		input = '''
func qmG (bool V6tH)	return
bool oqUI <- 78.38
string vD[37.39,6.7,0.58] <- 80.93
func Z85U (number JQpl, bool J7[56.5,16.58,82.6])	return false

'''
		expect = '''Program([FuncDecl(Id(qmG), [VarDecl(Id(V6tH), BoolType, None, None)], Return()), VarDecl(Id(oqUI), BoolType, None, NumLit(78.38)), VarDecl(Id(vD), ArrayType([37.39, 6.7, 0.58], StringType), None, NumLit(80.93)), FuncDecl(Id(Z85U), [VarDecl(Id(JQpl), NumberType, None, None), VarDecl(Id(J7), ArrayType([56.5, 16.58, 82.6], BoolType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115685))

	def test_21530115686(self):
		input = '''
dynamic Tut5 <- "Tu"
string fX <- 47.58
number pU[0.58]
func Ca4 ()
	return ZP9
func bNU (number ReU6[61.66])
	return

'''
		expect = '''Program([VarDecl(Id(Tut5), None, dynamic, StringLit(Tu)), VarDecl(Id(fX), StringType, None, NumLit(47.58)), VarDecl(Id(pU), ArrayType([0.58], NumberType), None, None), FuncDecl(Id(Ca4), [], Return(Id(ZP9))), FuncDecl(Id(bNU), [VarDecl(Id(ReU6), ArrayType([61.66], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115686))

	def test_21530115687(self):
		input = '''
string wlMP <- false
func Q8 ()
	return "FRE"
func lDU (number Gtg, number u2vX[65.89,24.53], bool xKui)
	begin
		i3Z(false, 55.48, "rCc")
		for Er until TD by true
			bool CHi[98.09,11.59]
		begin
			var nto <- 24.86
		end
	end

func mcdC (bool tct[4.39], bool H9F6[73.33,62.76,33.02])	begin
		continue
		QT1Z[27.49, 84.94, lk] <- "Mcx"
		for l1 until "YivqF" by "QQs"
			tvh <- BO
	end
func rriM (number lft, bool xUg, string BRj[71.76,60.51])	return "FmSG"
'''
		expect = '''Program([VarDecl(Id(wlMP), StringType, None, BooleanLit(False)), FuncDecl(Id(Q8), [], Return(StringLit(FRE))), FuncDecl(Id(lDU), [VarDecl(Id(Gtg), NumberType, None, None), VarDecl(Id(u2vX), ArrayType([65.89, 24.53], NumberType), None, None), VarDecl(Id(xKui), BoolType, None, None)], Block([CallStmt(Id(i3Z), [BooleanLit(False), NumLit(55.48), StringLit(rCc)]), For(Id(Er), Id(TD), BooleanLit(True), VarDecl(Id(CHi), ArrayType([98.09, 11.59], BoolType), None, None)), Block([VarDecl(Id(nto), None, var, NumLit(24.86))])])), FuncDecl(Id(mcdC), [VarDecl(Id(tct), ArrayType([4.39], BoolType), None, None), VarDecl(Id(H9F6), ArrayType([73.33, 62.76, 33.02], BoolType), None, None)], Block([Continue, AssignStmt(ArrayCell(Id(QT1Z), [NumLit(27.49), NumLit(84.94), Id(lk)]), StringLit(Mcx)), For(Id(l1), StringLit(YivqF), StringLit(QQs), AssignStmt(Id(tvh), Id(BO)))])), FuncDecl(Id(rriM), [VarDecl(Id(lft), NumberType, None, None), VarDecl(Id(xUg), BoolType, None, None), VarDecl(Id(BRj), ArrayType([71.76, 60.51], StringType), None, None)], Return(StringLit(FmSG)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115687))

	def test_21530115688(self):
		input = '''
number Kk[81.82,23.12,64.61] <- "Ca"
func WZD (bool ln[88.37], string s3cP, string iJtk[44.02])	begin
	end
func pw ()	begin
		begin
		end
	end

func MPt (string Bdp[92.68])
	begin
		if (false)
		return
		elif (Kpo) break
		y9_2[24.45] <- IQ
		if (73.3) break
		elif (1.13) return
		elif (true)
		W4Tk[false, oD, 47.02] <- mOQo
		else begin
			if ("wU")
			number XkB[24.94,98.96,89.79]
			elif ("A") dr()
			else break
		end
	end

number bD <- "l"
'''
		expect = '''Program([VarDecl(Id(Kk), ArrayType([81.82, 23.12, 64.61], NumberType), None, StringLit(Ca)), FuncDecl(Id(WZD), [VarDecl(Id(ln), ArrayType([88.37], BoolType), None, None), VarDecl(Id(s3cP), StringType, None, None), VarDecl(Id(iJtk), ArrayType([44.02], StringType), None, None)], Block([])), FuncDecl(Id(pw), [], Block([Block([])])), FuncDecl(Id(MPt), [VarDecl(Id(Bdp), ArrayType([92.68], StringType), None, None)], Block([If(BooleanLit(False), Return()), [(Id(Kpo), Break)], None, AssignStmt(ArrayCell(Id(y9_2), [NumLit(24.45)]), Id(IQ)), If(NumLit(73.3), Break), [(NumLit(1.13), Return()), (BooleanLit(True), AssignStmt(ArrayCell(Id(W4Tk), [BooleanLit(False), Id(oD), NumLit(47.02)]), Id(mOQo)))], Block([If(StringLit(wU), VarDecl(Id(XkB), ArrayType([24.94, 98.96, 89.79], NumberType), None, None)), [(StringLit(A), CallStmt(Id(dr), []))], Break])])), VarDecl(Id(bD), NumberType, None, StringLit(l))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115688))

	def test_21530115689(self):
		input = '''
func Ed3 ()	begin
		begin
			number zSLw[97.64] <- true
			if (true)
			break
			elif (Cau3) ckwK <- "IGUDX"
			else Az[true] <- "ZehqQ"
		end
		TY(75.5)
	end

func EGD (string lM[6.49])	return
'''
		expect = '''Program([FuncDecl(Id(Ed3), [], Block([Block([VarDecl(Id(zSLw), ArrayType([97.64], NumberType), None, BooleanLit(True)), If(BooleanLit(True), Break), [(Id(Cau3), AssignStmt(Id(ckwK), StringLit(IGUDX)))], AssignStmt(ArrayCell(Id(Az), [BooleanLit(True)]), StringLit(ZehqQ))]), CallStmt(Id(TY), [NumLit(75.5)])])), FuncDecl(Id(EGD), [VarDecl(Id(lM), ArrayType([6.49], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115689))

	def test_21530115690(self):
		input = '''
bool ufJN
var Vz <- 16.67
string soG
dynamic B0gm <- Ahp
number gWt <- 22.69
'''
		expect = '''Program([VarDecl(Id(ufJN), BoolType, None, None), VarDecl(Id(Vz), None, var, NumLit(16.67)), VarDecl(Id(soG), StringType, None, None), VarDecl(Id(B0gm), None, dynamic, Id(Ahp)), VarDecl(Id(gWt), NumberType, None, NumLit(22.69))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115690))

	def test_21530115691(self):
		input = '''
string jOW[88.62]
string POj4 <- 91.46
string Zdf[15.41]
number YP0[58.31] <- cFMb
dynamic kPGa
'''
		expect = '''Program([VarDecl(Id(jOW), ArrayType([88.62], StringType), None, None), VarDecl(Id(POj4), StringType, None, NumLit(91.46)), VarDecl(Id(Zdf), ArrayType([15.41], StringType), None, None), VarDecl(Id(YP0), ArrayType([58.31], NumberType), None, Id(cFMb)), VarDecl(Id(kPGa), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115691))

	def test_21530115692(self):
		input = '''
string r3Y[56.59] <- false
'''
		expect = '''Program([VarDecl(Id(r3Y), ArrayType([56.59], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115692))

	def test_21530115693(self):
		input = '''
number Qba
'''
		expect = '''Program([VarDecl(Id(Qba), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115693))

	def test_21530115694(self):
		input = '''
var nwo <- "ouuH"
'''
		expect = '''Program([VarDecl(Id(nwo), None, var, StringLit(ouuH))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115694))

	def test_21530115695(self):
		input = '''
bool Hw
func RA ()	begin
		begin
			break
			if (55.24)
			for UHib until true by "kyt"
				continue
			else return "ubTx"
			continue
		end
		number CXNy[45.91,89.31,74.38]
	end
func Os ()	return false

'''
		expect = '''Program([VarDecl(Id(Hw), BoolType, None, None), FuncDecl(Id(RA), [], Block([Block([Break, If(NumLit(55.24), For(Id(UHib), BooleanLit(True), StringLit(kyt), Continue)), [], Return(StringLit(ubTx)), Continue]), VarDecl(Id(CXNy), ArrayType([45.91, 89.31, 74.38], NumberType), None, None)])), FuncDecl(Id(Os), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115695))

	def test_21530115696(self):
		input = '''
func vm (bool u7wu[51.02,60.17,28.5])
	begin
	end
bool BUXL[45.79,82.6] <- "xizo"
func HQ (string TFMM[57.01,23.37], number poj[41.6,68.92,99.59])
	return 65.29
func Zk (bool Tje8[56.64,8.1,90.27], number V9)
	return 66.66

string Fl[85.44]
'''
		expect = '''Program([FuncDecl(Id(vm), [VarDecl(Id(u7wu), ArrayType([51.02, 60.17, 28.5], BoolType), None, None)], Block([])), VarDecl(Id(BUXL), ArrayType([45.79, 82.6], BoolType), None, StringLit(xizo)), FuncDecl(Id(HQ), [VarDecl(Id(TFMM), ArrayType([57.01, 23.37], StringType), None, None), VarDecl(Id(poj), ArrayType([41.6, 68.92, 99.59], NumberType), None, None)], Return(NumLit(65.29))), FuncDecl(Id(Zk), [VarDecl(Id(Tje8), ArrayType([56.64, 8.1, 90.27], BoolType), None, None), VarDecl(Id(V9), NumberType, None, None)], Return(NumLit(66.66))), VarDecl(Id(Fl), ArrayType([85.44], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115696))

	def test_21530115697(self):
		input = '''
number AIn[74.08] <- false
string jC <- 37.34
bool rl_W[84.8,93.42]
'''
		expect = '''Program([VarDecl(Id(AIn), ArrayType([74.08], NumberType), None, BooleanLit(False)), VarDecl(Id(jC), StringType, None, NumLit(37.34)), VarDecl(Id(rl_W), ArrayType([84.8, 93.42], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115697))

	def test_21530115698(self):
		input = '''
func ix ()	return "fKBua"
func wnq (string zs0[65.49], bool WJ, string ug[31.19])	return 22.92

'''
		expect = '''Program([FuncDecl(Id(ix), [], Return(StringLit(fKBua))), FuncDecl(Id(wnq), [VarDecl(Id(zs0), ArrayType([65.49], StringType), None, None), VarDecl(Id(WJ), BoolType, None, None), VarDecl(Id(ug), ArrayType([31.19], StringType), None, None)], Return(NumLit(22.92)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115698))

	def test_21530115699(self):
		input = '''
func Ri (bool ul, number eV_, string Up5p)
	begin
		if (false) Q1[Bp4U, 54.33] <- "eXi"
		elif ("sdOh")
		begin
			break
			bool yPB[62.12,23.38,81.78]
			string gM <- "Q"
		end
		elif (N3J)
		EF5["tjcq"] <- "rOArv"
		elif (true)
		AQ31(81.67, 81.05)
		for Yi until true by false
			for Ufe until 90.62 by "jZmap"
				break
		continue
	end

number uk[86.47]
string Li7[14.33] <- 67.84
'''
		expect = '''Program([FuncDecl(Id(Ri), [VarDecl(Id(ul), BoolType, None, None), VarDecl(Id(eV_), NumberType, None, None), VarDecl(Id(Up5p), StringType, None, None)], Block([If(BooleanLit(False), AssignStmt(ArrayCell(Id(Q1), [Id(Bp4U), NumLit(54.33)]), StringLit(eXi))), [(StringLit(sdOh), Block([Break, VarDecl(Id(yPB), ArrayType([62.12, 23.38, 81.78], BoolType), None, None), VarDecl(Id(gM), StringType, None, StringLit(Q))])), (Id(N3J), AssignStmt(ArrayCell(Id(EF5), [StringLit(tjcq)]), StringLit(rOArv))), (BooleanLit(True), CallStmt(Id(AQ31), [NumLit(81.67), NumLit(81.05)]))], None, For(Id(Yi), BooleanLit(True), BooleanLit(False), For(Id(Ufe), NumLit(90.62), StringLit(jZmap), Break)), Continue])), VarDecl(Id(uk), ArrayType([86.47], NumberType), None, None), VarDecl(Id(Li7), ArrayType([14.33], StringType), None, NumLit(67.84))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115699))

	def test_21530115700(self):
		input = '''
string Pxtj[68.37,50.59] <- 0.03
string cU <- Z2
'''
		expect = '''Program([VarDecl(Id(Pxtj), ArrayType([68.37, 50.59], StringType), None, NumLit(0.03)), VarDecl(Id(cU), StringType, None, Id(Z2))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115700))

	def test_21530115701(self):
		input = '''
func av (string HFY[4.83,20.69,98.01], bool oami)	return
func PUH (number VGt1[75.15,98.43,6.97])	return
'''
		expect = '''Program([FuncDecl(Id(av), [VarDecl(Id(HFY), ArrayType([4.83, 20.69, 98.01], StringType), None, None), VarDecl(Id(oami), BoolType, None, None)], Return()), FuncDecl(Id(PUH), [VarDecl(Id(VGt1), ArrayType([75.15, 98.43, 6.97], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115701))

	def test_21530115702(self):
		input = '''
func mqA2 ()	begin
		break
	end

dynamic MZEP
func oB2S (number nx[83.87,99.23])
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(mqA2), [], Block([Break])), VarDecl(Id(MZEP), None, dynamic, None), FuncDecl(Id(oB2S), [VarDecl(Id(nx), ArrayType([83.87, 99.23], NumberType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115702))

	def test_21530115703(self):
		input = '''
number aVBo <- "qMa"
number PSO[76.43,32.71,16.14]
number UL
string Mq9P[37.16,84.41]
'''
		expect = '''Program([VarDecl(Id(aVBo), NumberType, None, StringLit(qMa)), VarDecl(Id(PSO), ArrayType([76.43, 32.71, 16.14], NumberType), None, None), VarDecl(Id(UL), NumberType, None, None), VarDecl(Id(Mq9P), ArrayType([37.16, 84.41], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115703))

	def test_21530115704(self):
		input = '''
func WtK ()	return

string UVk <- true
func WHO ()	begin
	end

'''
		expect = '''Program([FuncDecl(Id(WtK), [], Return()), VarDecl(Id(UVk), StringType, None, BooleanLit(True)), FuncDecl(Id(WHO), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115704))

	def test_21530115705(self):
		input = '''
func MohZ (bool qqf[10.06])	return
bool kCt[41.72,36.72]
bool Npn <- yT
number eJW <- pA
'''
		expect = '''Program([FuncDecl(Id(MohZ), [VarDecl(Id(qqf), ArrayType([10.06], BoolType), None, None)], Return()), VarDecl(Id(kCt), ArrayType([41.72, 36.72], BoolType), None, None), VarDecl(Id(Npn), BoolType, None, Id(yT)), VarDecl(Id(eJW), NumberType, None, Id(pA))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115705))

	def test_21530115706(self):
		input = '''
number qLUP[51.67,24.41,70.49] <- "BAV"
'''
		expect = '''Program([VarDecl(Id(qLUP), ArrayType([51.67, 24.41, 70.49], NumberType), None, StringLit(BAV))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115706))

	def test_21530115707(self):
		input = '''
func XS (bool zDfq)	return "B"

string MR
'''
		expect = '''Program([FuncDecl(Id(XS), [VarDecl(Id(zDfq), BoolType, None, None)], Return(StringLit(B))), VarDecl(Id(MR), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115707))

	def test_21530115708(self):
		input = '''
dynamic o15
func YaH0 (string wzo[31.48,83.15,1.82])
	begin
		dynamic vx95 <- true
		string NEn
	end

func Sv (number cO[48.82,73.6], string jR)	begin
		ZIka(54.16)
	end

func aAn (number NwM[70.62,21.87,78.87], bool HW[65.46,7.74], bool XDnU[64.61,7.73])
	return

func gJ9J (string Ck6[88.17], number Sv6)	return "BcoS"

'''
		expect = '''Program([VarDecl(Id(o15), None, dynamic, None), FuncDecl(Id(YaH0), [VarDecl(Id(wzo), ArrayType([31.48, 83.15, 1.82], StringType), None, None)], Block([VarDecl(Id(vx95), None, dynamic, BooleanLit(True)), VarDecl(Id(NEn), StringType, None, None)])), FuncDecl(Id(Sv), [VarDecl(Id(cO), ArrayType([48.82, 73.6], NumberType), None, None), VarDecl(Id(jR), StringType, None, None)], Block([CallStmt(Id(ZIka), [NumLit(54.16)])])), FuncDecl(Id(aAn), [VarDecl(Id(NwM), ArrayType([70.62, 21.87, 78.87], NumberType), None, None), VarDecl(Id(HW), ArrayType([65.46, 7.74], BoolType), None, None), VarDecl(Id(XDnU), ArrayType([64.61, 7.73], BoolType), None, None)], Return()), FuncDecl(Id(gJ9J), [VarDecl(Id(Ck6), ArrayType([88.17], StringType), None, None), VarDecl(Id(Sv6), NumberType, None, None)], Return(StringLit(BcoS)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115708))

	def test_21530115709(self):
		input = '''
func Tb0 (string TI4[89.2,39.5,81.17])
	return f7oe

func VFI (number sH8N[23.7,19.83])
	return "pdtbn"

string uN[76.86,67.64,53.99] <- 18.77
bool P2
'''
		expect = '''Program([FuncDecl(Id(Tb0), [VarDecl(Id(TI4), ArrayType([89.2, 39.5, 81.17], StringType), None, None)], Return(Id(f7oe))), FuncDecl(Id(VFI), [VarDecl(Id(sH8N), ArrayType([23.7, 19.83], NumberType), None, None)], Return(StringLit(pdtbn))), VarDecl(Id(uN), ArrayType([76.86, 67.64, 53.99], StringType), None, NumLit(18.77)), VarDecl(Id(P2), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115709))

	def test_21530115710(self):
		input = '''
func H580 (string QOxb[6.25,43.08], bool h9M[25.83])
	return
func SF (string OY[41.98,94.13,15.7], string YXuv[64.8,25.1,74.31])
	begin
		continue
		if (19.72)
		return
		else begin
			s0("vqq", x0, "Mg")
			if (false) OwRK[true, false, gWx0] <- v3
			elif (12.38)
			for p97u until "MYzWc" by false
				if (true)
				S5qC <- 26.93
				elif (true)
				return
				elif (7.01) bool iy[40.07,17.4,29.5] <- true
				elif (62.19) E2 <- true
				elif (Dub7)
				number XL3m[29.86,95.48,65.87] <- "XQAn"
				else qVR[false, true] <- Qe
			return
		end
	end
number QmhK[57.36,53.41]
func qdel ()	return
'''
		expect = '''Program([FuncDecl(Id(H580), [VarDecl(Id(QOxb), ArrayType([6.25, 43.08], StringType), None, None), VarDecl(Id(h9M), ArrayType([25.83], BoolType), None, None)], Return()), FuncDecl(Id(SF), [VarDecl(Id(OY), ArrayType([41.98, 94.13, 15.7], StringType), None, None), VarDecl(Id(YXuv), ArrayType([64.8, 25.1, 74.31], StringType), None, None)], Block([Continue, If(NumLit(19.72), Return()), [], Block([CallStmt(Id(s0), [StringLit(vqq), Id(x0), StringLit(Mg)]), If(BooleanLit(False), AssignStmt(ArrayCell(Id(OwRK), [BooleanLit(True), BooleanLit(False), Id(gWx0)]), Id(v3))), [(NumLit(12.38), For(Id(p97u), StringLit(MYzWc), BooleanLit(False), If(BooleanLit(True), AssignStmt(Id(S5qC), NumLit(26.93))), [(BooleanLit(True), Return()), (NumLit(7.01), VarDecl(Id(iy), ArrayType([40.07, 17.4, 29.5], BoolType), None, BooleanLit(True))), (NumLit(62.19), AssignStmt(Id(E2), BooleanLit(True)))], None)), (Id(Dub7), VarDecl(Id(XL3m), ArrayType([29.86, 95.48, 65.87], NumberType), None, StringLit(XQAn)))], AssignStmt(ArrayCell(Id(qVR), [BooleanLit(False), BooleanLit(True)]), Id(Qe)), Return()])])), VarDecl(Id(QmhK), ArrayType([57.36, 53.41], NumberType), None, None), FuncDecl(Id(qdel), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115710))

	def test_21530115711(self):
		input = '''
string kd9E[96.6,29.17,74.41] <- lDIW
func k5UZ (number lI[72.99], number yNB, number lCD[54.88])
	return
'''
		expect = '''Program([VarDecl(Id(kd9E), ArrayType([96.6, 29.17, 74.41], StringType), None, Id(lDIW)), FuncDecl(Id(k5UZ), [VarDecl(Id(lI), ArrayType([72.99], NumberType), None, None), VarDecl(Id(yNB), NumberType, None, None), VarDecl(Id(lCD), ArrayType([54.88], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115711))

	def test_21530115712(self):
		input = '''
bool uqOr <- BGj
func pI (string up[88.12,43.87,26.58], bool pD[64.83,58.32,30.73])	begin
		for WrH until 63.76 by "oJP"
			if (true) for dt until JI83 by 78.0
				Uq[lA] <- true
			elif (RAt)
			break
			else dynamic Bjpm
		continue
		break
	end

func Ypw (string D5)
	return 97.62

'''
		expect = '''Program([VarDecl(Id(uqOr), BoolType, None, Id(BGj)), FuncDecl(Id(pI), [VarDecl(Id(up), ArrayType([88.12, 43.87, 26.58], StringType), None, None), VarDecl(Id(pD), ArrayType([64.83, 58.32, 30.73], BoolType), None, None)], Block([For(Id(WrH), NumLit(63.76), StringLit(oJP), If(BooleanLit(True), For(Id(dt), Id(JI83), NumLit(78.0), AssignStmt(ArrayCell(Id(Uq), [Id(lA)]), BooleanLit(True)))), [(Id(RAt), Break)], VarDecl(Id(Bjpm), None, dynamic, None)), Continue, Break])), FuncDecl(Id(Ypw), [VarDecl(Id(D5), StringType, None, None)], Return(NumLit(97.62)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115712))

	def test_21530115713(self):
		input = '''
number Qnj[34.96,78.58] <- 76.94
number sg <- false
func NLhE (string Kw[90.34,71.72,78.9], bool BHg3, string CN[43.81,12.68,54.17])	return

number MxxH[78.03,4.9,10.58]
func wv (bool Pn)
	begin
		break
	end

'''
		expect = '''Program([VarDecl(Id(Qnj), ArrayType([34.96, 78.58], NumberType), None, NumLit(76.94)), VarDecl(Id(sg), NumberType, None, BooleanLit(False)), FuncDecl(Id(NLhE), [VarDecl(Id(Kw), ArrayType([90.34, 71.72, 78.9], StringType), None, None), VarDecl(Id(BHg3), BoolType, None, None), VarDecl(Id(CN), ArrayType([43.81, 12.68, 54.17], StringType), None, None)], Return()), VarDecl(Id(MxxH), ArrayType([78.03, 4.9, 10.58], NumberType), None, None), FuncDecl(Id(wv), [VarDecl(Id(Pn), BoolType, None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115713))

	def test_21530115714(self):
		input = '''
func gr (bool lF)
	return
func m_ (number Cv1)
	return kRk

func IT ()	begin
		break
	end

func k9aQ (bool Ek, string Di58[86.49,13.05,88.08])	begin
		zc8B["HRHX"] <- 95.61
	end
dynamic JwDa <- false
'''
		expect = '''Program([FuncDecl(Id(gr), [VarDecl(Id(lF), BoolType, None, None)], Return()), FuncDecl(Id(m_), [VarDecl(Id(Cv1), NumberType, None, None)], Return(Id(kRk))), FuncDecl(Id(IT), [], Block([Break])), FuncDecl(Id(k9aQ), [VarDecl(Id(Ek), BoolType, None, None), VarDecl(Id(Di58), ArrayType([86.49, 13.05, 88.08], StringType), None, None)], Block([AssignStmt(ArrayCell(Id(zc8B), [StringLit(HRHX)]), NumLit(95.61))])), VarDecl(Id(JwDa), None, dynamic, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115714))

	def test_21530115715(self):
		input = '''
number ERQ[45.25,41.49] <- r8Am
bool M_[93.41] <- VU
func Fs (number cKI, number iS1m)	return
func yP (string xE9)
	return "JzfL"
'''
		expect = '''Program([VarDecl(Id(ERQ), ArrayType([45.25, 41.49], NumberType), None, Id(r8Am)), VarDecl(Id(M_), ArrayType([93.41], BoolType), None, Id(VU)), FuncDecl(Id(Fs), [VarDecl(Id(cKI), NumberType, None, None), VarDecl(Id(iS1m), NumberType, None, None)], Return()), FuncDecl(Id(yP), [VarDecl(Id(xE9), StringType, None, None)], Return(StringLit(JzfL)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115715))

	def test_21530115716(self):
		input = '''
bool EPx
number Q7N <- blP0
string LhP[77.13] <- "kUWyY"
func e6t ()
	begin
		for xgz until true by Jz_8
			break
		if (adc) break
		else number eT[44.77,56.89,48.67]
	end

'''
		expect = '''Program([VarDecl(Id(EPx), BoolType, None, None), VarDecl(Id(Q7N), NumberType, None, Id(blP0)), VarDecl(Id(LhP), ArrayType([77.13], StringType), None, StringLit(kUWyY)), FuncDecl(Id(e6t), [], Block([For(Id(xgz), BooleanLit(True), Id(Jz_8), Break), If(Id(adc), Break), [], VarDecl(Id(eT), ArrayType([44.77, 56.89, 48.67], NumberType), None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115716))

	def test_21530115717(self):
		input = '''
string SEj <- 25.88
func fv (string Ic[96.69], number fS, number SiQ[45.34,94.33])
	begin
		PIlt(n3d1, true, false)
		return false
	end
func akE (number HKK[20.39,28.14])
	begin
	end
'''
		expect = '''Program([VarDecl(Id(SEj), StringType, None, NumLit(25.88)), FuncDecl(Id(fv), [VarDecl(Id(Ic), ArrayType([96.69], StringType), None, None), VarDecl(Id(fS), NumberType, None, None), VarDecl(Id(SiQ), ArrayType([45.34, 94.33], NumberType), None, None)], Block([CallStmt(Id(PIlt), [Id(n3d1), BooleanLit(True), BooleanLit(False)]), Return(BooleanLit(False))])), FuncDecl(Id(akE), [VarDecl(Id(HKK), ArrayType([20.39, 28.14], NumberType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115717))

	def test_21530115718(self):
		input = '''
string Gh
func TNV ()	begin
	end
string Nle[94.99,19.85]
'''
		expect = '''Program([VarDecl(Id(Gh), StringType, None, None), FuncDecl(Id(TNV), [], Block([])), VarDecl(Id(Nle), ArrayType([94.99, 19.85], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115718))

	def test_21530115719(self):
		input = '''
func mxN (string Jr, number Ec, bool kPD)
	return
'''
		expect = '''Program([FuncDecl(Id(mxN), [VarDecl(Id(Jr), StringType, None, None), VarDecl(Id(Ec), NumberType, None, None), VarDecl(Id(kPD), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115719))

	def test_21530115720(self):
		input = '''
string kTt[74.97]
'''
		expect = '''Program([VarDecl(Id(kTt), ArrayType([74.97], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115720))

	def test_21530115721(self):
		input = '''
func WRB ()
	return

func S3 (bool Jxd[96.59], string YDz9[27.41,86.35])	return
func jq (string FQL)	return
func m0xD (bool Hijj[60.34,65.55])
	return false
'''
		expect = '''Program([FuncDecl(Id(WRB), [], Return()), FuncDecl(Id(S3), [VarDecl(Id(Jxd), ArrayType([96.59], BoolType), None, None), VarDecl(Id(YDz9), ArrayType([27.41, 86.35], StringType), None, None)], Return()), FuncDecl(Id(jq), [VarDecl(Id(FQL), StringType, None, None)], Return()), FuncDecl(Id(m0xD), [VarDecl(Id(Hijj), ArrayType([60.34, 65.55], BoolType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115721))

	def test_21530115722(self):
		input = '''
func aT (number U13, bool IbHq[9.26,79.61], bool n4Q)
	return

'''
		expect = '''Program([FuncDecl(Id(aT), [VarDecl(Id(U13), NumberType, None, None), VarDecl(Id(IbHq), ArrayType([9.26, 79.61], BoolType), None, None), VarDecl(Id(n4Q), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115722))

	def test_21530115723(self):
		input = '''
func PvP (bool Dv[63.34])	return
number Wcu
'''
		expect = '''Program([FuncDecl(Id(PvP), [VarDecl(Id(Dv), ArrayType([63.34], BoolType), None, None)], Return()), VarDecl(Id(Wcu), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115723))

	def test_21530115724(self):
		input = '''
func U_ (number hE, bool UqK[90.66,63.4], string z_[87.21,29.18])
	return "mi"

func akGk ()
	return
'''
		expect = '''Program([FuncDecl(Id(U_), [VarDecl(Id(hE), NumberType, None, None), VarDecl(Id(UqK), ArrayType([90.66, 63.4], BoolType), None, None), VarDecl(Id(z_), ArrayType([87.21, 29.18], StringType), None, None)], Return(StringLit(mi))), FuncDecl(Id(akGk), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115724))

	def test_21530115725(self):
		input = '''
dynamic u2U <- true
'''
		expect = '''Program([VarDecl(Id(u2U), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115725))

	def test_21530115726(self):
		input = '''
func ZPzS ()
	begin
		for tOY until "o" by 89.56
			if (98.57) begin
				g_4()
				sD(9.28, false)
				AG("xbD", "AhsqS", true)
			end
			elif ("X")
			lV(61.4)
			elif (cb) number R8[64.07,54.6] <- "fo"
			elif (false) begin
				begin
				end
			end
			elif (h6) break
			elif (false)
			continue
			else continue
		begin
		end
		for ZK1 until true by true
			if (vCR)
			fiy2[33.76, AG] <- false
			elif (74.58)
			return
			elif ("f")
			for Xvn0 until "srX" by tp
				f1U8()
			elif ("kWLD")
			LMd <- "mKJ"
			elif (60.88) begin
			end
	end
'''
		expect = '''Program([FuncDecl(Id(ZPzS), [], Block([For(Id(tOY), StringLit(o), NumLit(89.56), If(NumLit(98.57), Block([CallStmt(Id(g_4), []), CallStmt(Id(sD), [NumLit(9.28), BooleanLit(False)]), CallStmt(Id(AG), [StringLit(xbD), StringLit(AhsqS), BooleanLit(True)])])), [(StringLit(X), CallStmt(Id(lV), [NumLit(61.4)])), (Id(cb), VarDecl(Id(R8), ArrayType([64.07, 54.6], NumberType), None, StringLit(fo))), (BooleanLit(False), Block([Block([])])), (Id(h6), Break), (BooleanLit(False), Continue)], Continue), Block([]), For(Id(ZK1), BooleanLit(True), BooleanLit(True), If(Id(vCR), AssignStmt(ArrayCell(Id(fiy2), [NumLit(33.76), Id(AG)]), BooleanLit(False))), [(NumLit(74.58), Return()), (StringLit(f), For(Id(Xvn0), StringLit(srX), Id(tp), CallStmt(Id(f1U8), []))), (StringLit(kWLD), AssignStmt(Id(LMd), StringLit(mKJ))), (NumLit(60.88), Block([]))], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115726))

	def test_21530115727(self):
		input = '''
func uJ (number osgX, string iGN, string B6)	return
var P0pG <- "HCRAt"
func I4a (bool Gh, string dg, number RN)
	begin
		return true
	end

func lB_Q (bool fy, number UDf[2.05], number Zi)
	return false
func Czb9 (bool Mgt, string dum)
	begin
		break
	end

'''
		expect = '''Program([FuncDecl(Id(uJ), [VarDecl(Id(osgX), NumberType, None, None), VarDecl(Id(iGN), StringType, None, None), VarDecl(Id(B6), StringType, None, None)], Return()), VarDecl(Id(P0pG), None, var, StringLit(HCRAt)), FuncDecl(Id(I4a), [VarDecl(Id(Gh), BoolType, None, None), VarDecl(Id(dg), StringType, None, None), VarDecl(Id(RN), NumberType, None, None)], Block([Return(BooleanLit(True))])), FuncDecl(Id(lB_Q), [VarDecl(Id(fy), BoolType, None, None), VarDecl(Id(UDf), ArrayType([2.05], NumberType), None, None), VarDecl(Id(Zi), NumberType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(Czb9), [VarDecl(Id(Mgt), BoolType, None, None), VarDecl(Id(dum), StringType, None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115727))

	def test_21530115728(self):
		input = '''
func sCH (bool ayG4[36.23])	begin
		for UO until 24.51 by XW0
			for bB until "rSM" by "pFFbD"
				FH[19.74, ylf3, "l"] <- "YaitS"
		continue
	end

func LeUA (string Wnxt, string Ac)	return
func LNb (bool hf[50.76,22.33], bool Wz)	begin
		if (Pe3o)
		continue
		V62I <- "itvRH"
	end

string F0t0[23.43,60.6] <- R0
func Zh (string tjd[2.59,55.17])
	return

'''
		expect = '''Program([FuncDecl(Id(sCH), [VarDecl(Id(ayG4), ArrayType([36.23], BoolType), None, None)], Block([For(Id(UO), NumLit(24.51), Id(XW0), For(Id(bB), StringLit(rSM), StringLit(pFFbD), AssignStmt(ArrayCell(Id(FH), [NumLit(19.74), Id(ylf3), StringLit(l)]), StringLit(YaitS)))), Continue])), FuncDecl(Id(LeUA), [VarDecl(Id(Wnxt), StringType, None, None), VarDecl(Id(Ac), StringType, None, None)], Return()), FuncDecl(Id(LNb), [VarDecl(Id(hf), ArrayType([50.76, 22.33], BoolType), None, None), VarDecl(Id(Wz), BoolType, None, None)], Block([If(Id(Pe3o), Continue), [], None, AssignStmt(Id(V62I), StringLit(itvRH))])), VarDecl(Id(F0t0), ArrayType([23.43, 60.6], StringType), None, Id(R0)), FuncDecl(Id(Zh), [VarDecl(Id(tjd), ArrayType([2.59, 55.17], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115728))

	def test_21530115729(self):
		input = '''
string E2C[65.97] <- Xi0a
'''
		expect = '''Program([VarDecl(Id(E2C), ArrayType([65.97], StringType), None, Id(Xi0a))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115729))

	def test_21530115730(self):
		input = '''
bool qGfo[79.01] <- false
func x3zg (bool Plv2, bool Tiqs)	begin
	end

var sUNa <- 66.24
func yUWD (number VG, bool IyIv, string Eidz)	return 69.67

'''
		expect = '''Program([VarDecl(Id(qGfo), ArrayType([79.01], BoolType), None, BooleanLit(False)), FuncDecl(Id(x3zg), [VarDecl(Id(Plv2), BoolType, None, None), VarDecl(Id(Tiqs), BoolType, None, None)], Block([])), VarDecl(Id(sUNa), None, var, NumLit(66.24)), FuncDecl(Id(yUWD), [VarDecl(Id(VG), NumberType, None, None), VarDecl(Id(IyIv), BoolType, None, None), VarDecl(Id(Eidz), StringType, None, None)], Return(NumLit(69.67)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115730))

	def test_21530115731(self):
		input = '''
func BABr (bool SX4V)
	return

'''
		expect = '''Program([FuncDecl(Id(BABr), [VarDecl(Id(SX4V), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115731))

	def test_21530115732(self):
		input = '''
number gcc[61.62,22.46]
bool cs[34.21,62.23]
number dX <- "Nk"
dynamic HV
string QhlU <- false
'''
		expect = '''Program([VarDecl(Id(gcc), ArrayType([61.62, 22.46], NumberType), None, None), VarDecl(Id(cs), ArrayType([34.21, 62.23], BoolType), None, None), VarDecl(Id(dX), NumberType, None, StringLit(Nk)), VarDecl(Id(HV), None, dynamic, None), VarDecl(Id(QhlU), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115732))

	def test_21530115733(self):
		input = '''
func AmY (string fbr[29.98,87.3], string JpJ2, bool O9[62.98])
	begin
		return lfF
		zn <- UEU9
	end
func Uj (bool Io[88.03,97.2,38.67])	return

func BvB0 (string oBPX)
	begin
		for UoAY until "cN" by "XGvUL"
			MhyO(17.27, 92.59, "VcxN")
	end
string YJ_[70.65] <- 90.98
number ky4[5.05]
'''
		expect = '''Program([FuncDecl(Id(AmY), [VarDecl(Id(fbr), ArrayType([29.98, 87.3], StringType), None, None), VarDecl(Id(JpJ2), StringType, None, None), VarDecl(Id(O9), ArrayType([62.98], BoolType), None, None)], Block([Return(Id(lfF)), AssignStmt(Id(zn), Id(UEU9))])), FuncDecl(Id(Uj), [VarDecl(Id(Io), ArrayType([88.03, 97.2, 38.67], BoolType), None, None)], Return()), FuncDecl(Id(BvB0), [VarDecl(Id(oBPX), StringType, None, None)], Block([For(Id(UoAY), StringLit(cN), StringLit(XGvUL), CallStmt(Id(MhyO), [NumLit(17.27), NumLit(92.59), StringLit(VcxN)]))])), VarDecl(Id(YJ_), ArrayType([70.65], StringType), None, NumLit(90.98)), VarDecl(Id(ky4), ArrayType([5.05], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115733))

	def test_21530115734(self):
		input = '''
string o2Nh
bool fl <- "oaKzv"
func ez (bool B53)
	return "kWseE"
func aVxG (bool r7_7[65.6], bool aa2Y[1.38,13.91,84.48], string oLY[96.73])	return yy

func SOdk (string IEN[89.06], bool LLs[73.76,73.55,69.41])
	return

'''
		expect = '''Program([VarDecl(Id(o2Nh), StringType, None, None), VarDecl(Id(fl), BoolType, None, StringLit(oaKzv)), FuncDecl(Id(ez), [VarDecl(Id(B53), BoolType, None, None)], Return(StringLit(kWseE))), FuncDecl(Id(aVxG), [VarDecl(Id(r7_7), ArrayType([65.6], BoolType), None, None), VarDecl(Id(aa2Y), ArrayType([1.38, 13.91, 84.48], BoolType), None, None), VarDecl(Id(oLY), ArrayType([96.73], StringType), None, None)], Return(Id(yy))), FuncDecl(Id(SOdk), [VarDecl(Id(IEN), ArrayType([89.06], StringType), None, None), VarDecl(Id(LLs), ArrayType([73.76, 73.55, 69.41], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115734))

	def test_21530115735(self):
		input = '''
func Erws (bool f_, bool I3[20.0,12.76])
	return Wps

func kV (bool yN, number tu[3.59])	return yKQ
'''
		expect = '''Program([FuncDecl(Id(Erws), [VarDecl(Id(f_), BoolType, None, None), VarDecl(Id(I3), ArrayType([20.0, 12.76], BoolType), None, None)], Return(Id(Wps))), FuncDecl(Id(kV), [VarDecl(Id(yN), BoolType, None, None), VarDecl(Id(tu), ArrayType([3.59], NumberType), None, None)], Return(Id(yKQ)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115735))

	def test_21530115736(self):
		input = '''
func mo3 (number n4[68.34])	begin
		continue
	end
number u9 <- 85.88
func G3I (string kZ7, string CA9, bool mtG)	begin
		if (true)
		return 8.42
		elif (true) begin
		end
		elif ("jIs") if (QEL) break
		elif (true)
		return false
		elif (Awb)
		for feG4 until false by 2.79
			continue
		elif (FQM) FM_(17.04)
		elif ("dhv")
		begin
			ageb()
		end
		elif (false)
		emS4[false, 6.92] <- N47
		else break
		for KoR until PUu by true
			sE[43.08, "nar", vDmy] <- 81.21
		for wY until true by "wA"
			duB(false, 66.19, CMLc)
	end
number hDRT[76.71]
'''
		expect = '''Program([FuncDecl(Id(mo3), [VarDecl(Id(n4), ArrayType([68.34], NumberType), None, None)], Block([Continue])), VarDecl(Id(u9), NumberType, None, NumLit(85.88)), FuncDecl(Id(G3I), [VarDecl(Id(kZ7), StringType, None, None), VarDecl(Id(CA9), StringType, None, None), VarDecl(Id(mtG), BoolType, None, None)], Block([If(BooleanLit(True), Return(NumLit(8.42))), [(BooleanLit(True), Block([])), (StringLit(jIs), If(Id(QEL), Break), [(BooleanLit(True), Return(BooleanLit(False))), (Id(Awb), For(Id(feG4), BooleanLit(False), NumLit(2.79), Continue)), (Id(FQM), CallStmt(Id(FM_), [NumLit(17.04)])), (StringLit(dhv), Block([CallStmt(Id(ageb), [])]))], None), (BooleanLit(False), AssignStmt(ArrayCell(Id(emS4), [BooleanLit(False), NumLit(6.92)]), Id(N47)))], Break, For(Id(KoR), Id(PUu), BooleanLit(True), AssignStmt(ArrayCell(Id(sE), [NumLit(43.08), StringLit(nar), Id(vDmy)]), NumLit(81.21))), For(Id(wY), BooleanLit(True), StringLit(wA), CallStmt(Id(duB), [BooleanLit(False), NumLit(66.19), Id(CMLc)]))])), VarDecl(Id(hDRT), ArrayType([76.71], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115736))

	def test_21530115737(self):
		input = '''
bool a14[57.66,87.2]
func VKK (number rwu[21.12,80.78], bool DQ[54.01,56.02])	return

string K4[20.81] <- 0.58
number Yq
func GvQr ()	return 98.39
'''
		expect = '''Program([VarDecl(Id(a14), ArrayType([57.66, 87.2], BoolType), None, None), FuncDecl(Id(VKK), [VarDecl(Id(rwu), ArrayType([21.12, 80.78], NumberType), None, None), VarDecl(Id(DQ), ArrayType([54.01, 56.02], BoolType), None, None)], Return()), VarDecl(Id(K4), ArrayType([20.81], StringType), None, NumLit(0.58)), VarDecl(Id(Yq), NumberType, None, None), FuncDecl(Id(GvQr), [], Return(NumLit(98.39)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115737))

	def test_21530115738(self):
		input = '''
string pwU[31.71,6.87,92.59] <- false
func scEX ()	return 42.84

func caY (string mA_, string wi[76.2,24.85], bool d1)
	return
string upf[69.09,62.64]
'''
		expect = '''Program([VarDecl(Id(pwU), ArrayType([31.71, 6.87, 92.59], StringType), None, BooleanLit(False)), FuncDecl(Id(scEX), [], Return(NumLit(42.84))), FuncDecl(Id(caY), [VarDecl(Id(mA_), StringType, None, None), VarDecl(Id(wi), ArrayType([76.2, 24.85], StringType), None, None), VarDecl(Id(d1), BoolType, None, None)], Return()), VarDecl(Id(upf), ArrayType([69.09, 62.64], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115738))

	def test_21530115739(self):
		input = '''
func gz ()	return

'''
		expect = '''Program([FuncDecl(Id(gz), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115739))

	def test_21530115740(self):
		input = '''
string mn7Q
bool YHE[14.4,69.74] <- VIUX
func Gh (number iyU4[51.94,52.68])
	return 78.49

func ny (bool Mwk[99.76])
	return

func CoHM ()	return
'''
		expect = '''Program([VarDecl(Id(mn7Q), StringType, None, None), VarDecl(Id(YHE), ArrayType([14.4, 69.74], BoolType), None, Id(VIUX)), FuncDecl(Id(Gh), [VarDecl(Id(iyU4), ArrayType([51.94, 52.68], NumberType), None, None)], Return(NumLit(78.49))), FuncDecl(Id(ny), [VarDecl(Id(Mwk), ArrayType([99.76], BoolType), None, None)], Return()), FuncDecl(Id(CoHM), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115740))

	def test_21530115741(self):
		input = '''
bool cI <- "h"
func c8 (bool dl[58.8], number ZZS)
	begin
		if (57.91) return
		elif (25.71) return false
		elif (false) if (wux) for DY until false by Pu
			MVgv[false, true] <- vWK
		elif (33.35)
		return "SI"
		elif ("UDoe")
		continue
		elif ("VP")
		continue
		elif ("jAEpE")
		if (H5) for uH until false by "Emm"
			string Bot[0.13] <- 54.19
		elif (true)
		break
		elif ("PEEP") if ("olEf") break
		elif (oF) for bZph until 71.87 by "E"
			Cxgh <- "wA"
		elif (84.88)
		if (oW) return
		elif ("I")
		TQ(jwCP, false, true)
		elif (false)
		return sJg
		elif ("Qg") return
		elif (XdOB)
		dynamic DS
		elif (qHFm)
		xZ <- "nL"
		elif (34.81)
		continue
		else begin
		end
	end

bool GAc[38.83,46.28,11.44] <- 51.64
func EL (bool PdJo, string OzRc)	begin
		number XI_r <- Wf
		begin
			break
			ekXr(true, 28.66, false)
			return vT1
		end
		break
	end

func SpCg (bool OOB[2.86,89.42,38.5], bool le8L)
	return false
'''
		expect = '''Program([VarDecl(Id(cI), BoolType, None, StringLit(h)), FuncDecl(Id(c8), [VarDecl(Id(dl), ArrayType([58.8], BoolType), None, None), VarDecl(Id(ZZS), NumberType, None, None)], Block([If(NumLit(57.91), Return()), [(NumLit(25.71), Return(BooleanLit(False))), (BooleanLit(False), If(Id(wux), For(Id(DY), BooleanLit(False), Id(Pu), AssignStmt(ArrayCell(Id(MVgv), [BooleanLit(False), BooleanLit(True)]), Id(vWK)))), [(NumLit(33.35), Return(StringLit(SI))), (StringLit(UDoe), Continue), (StringLit(VP), Continue), (StringLit(jAEpE), If(Id(H5), For(Id(uH), BooleanLit(False), StringLit(Emm), VarDecl(Id(Bot), ArrayType([0.13], StringType), None, NumLit(54.19)))), [(BooleanLit(True), Break), (StringLit(PEEP), If(StringLit(olEf), Break), [(Id(oF), For(Id(bZph), NumLit(71.87), StringLit(E), AssignStmt(Id(Cxgh), StringLit(wA)))), (NumLit(84.88), If(Id(oW), Return()), [(StringLit(I), CallStmt(Id(TQ), [Id(jwCP), BooleanLit(False), BooleanLit(True)])), (BooleanLit(False), Return(Id(sJg)))], None), (StringLit(Qg), Return())], None), (Id(XdOB), VarDecl(Id(DS), None, dynamic, None))], None), (Id(qHFm), AssignStmt(Id(xZ), StringLit(nL)))], None), (NumLit(34.81), Continue)], Block([])])), VarDecl(Id(GAc), ArrayType([38.83, 46.28, 11.44], BoolType), None, NumLit(51.64)), FuncDecl(Id(EL), [VarDecl(Id(PdJo), BoolType, None, None), VarDecl(Id(OzRc), StringType, None, None)], Block([VarDecl(Id(XI_r), NumberType, None, Id(Wf)), Block([Break, CallStmt(Id(ekXr), [BooleanLit(True), NumLit(28.66), BooleanLit(False)]), Return(Id(vT1))]), Break])), FuncDecl(Id(SpCg), [VarDecl(Id(OOB), ArrayType([2.86, 89.42, 38.5], BoolType), None, None), VarDecl(Id(le8L), BoolType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115741))

	def test_21530115742(self):
		input = '''
func cnT ()	return P4rg
dynamic teO
func V3 (bool S6[45.94,80.23,82.04])
	return 38.24

'''
		expect = '''Program([FuncDecl(Id(cnT), [], Return(Id(P4rg))), VarDecl(Id(teO), None, dynamic, None), FuncDecl(Id(V3), [VarDecl(Id(S6), ArrayType([45.94, 80.23, 82.04], BoolType), None, None)], Return(NumLit(38.24)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115742))

	def test_21530115743(self):
		input = '''
func flp (number kq[64.88,94.98,83.66], number z9[25.64,67.35,27.54], bool dAk_)
	return 80.39

func sa6 ()	begin
		var Z1 <- true
		Lr(Ia)
		var cz <- UMdA
	end
bool gfsf[75.03]
'''
		expect = '''Program([FuncDecl(Id(flp), [VarDecl(Id(kq), ArrayType([64.88, 94.98, 83.66], NumberType), None, None), VarDecl(Id(z9), ArrayType([25.64, 67.35, 27.54], NumberType), None, None), VarDecl(Id(dAk_), BoolType, None, None)], Return(NumLit(80.39))), FuncDecl(Id(sa6), [], Block([VarDecl(Id(Z1), None, var, BooleanLit(True)), CallStmt(Id(Lr), [Id(Ia)]), VarDecl(Id(cz), None, var, Id(UMdA))])), VarDecl(Id(gfsf), ArrayType([75.03], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115743))

	def test_21530115744(self):
		input = '''
number X8fA[85.48,57.7,52.35]
bool g_[73.63] <- "iePG"
string ZkRN[70.31,31.18] <- Fnqf
number AOv <- "XCG"
func Y0x ()	return
'''
		expect = '''Program([VarDecl(Id(X8fA), ArrayType([85.48, 57.7, 52.35], NumberType), None, None), VarDecl(Id(g_), ArrayType([73.63], BoolType), None, StringLit(iePG)), VarDecl(Id(ZkRN), ArrayType([70.31, 31.18], StringType), None, Id(Fnqf)), VarDecl(Id(AOv), NumberType, None, StringLit(XCG)), FuncDecl(Id(Y0x), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115744))

	def test_21530115745(self):
		input = '''
number v6F[32.72]
number t239[51.62,65.74]
number im[44.25] <- 12.29
func RG7z ()	begin
		continue
		for v59 until "Z" by 16.9
			continue
	end

bool Yx
'''
		expect = '''Program([VarDecl(Id(v6F), ArrayType([32.72], NumberType), None, None), VarDecl(Id(t239), ArrayType([51.62, 65.74], NumberType), None, None), VarDecl(Id(im), ArrayType([44.25], NumberType), None, NumLit(12.29)), FuncDecl(Id(RG7z), [], Block([Continue, For(Id(v59), StringLit(Z), NumLit(16.9), Continue)])), VarDecl(Id(Yx), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115745))

	def test_21530115746(self):
		input = '''
string ow[27.13,90.83,65.57]
func D2H (bool Xz, string Ie6)	return true

func FYf ()	return "sCOit"

string rjgi[99.6] <- Yu
'''
		expect = '''Program([VarDecl(Id(ow), ArrayType([27.13, 90.83, 65.57], StringType), None, None), FuncDecl(Id(D2H), [VarDecl(Id(Xz), BoolType, None, None), VarDecl(Id(Ie6), StringType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(FYf), [], Return(StringLit(sCOit))), VarDecl(Id(rjgi), ArrayType([99.6], StringType), None, Id(Yu))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115746))

	def test_21530115747(self):
		input = '''
var dzX4 <- DWW
func AJPi (number KR6r, string Q9, bool wlg[43.58,99.02,21.43])
	return false
func Q3 ()
	return

func Q0 (string AO, number yn)	return
'''
		expect = '''Program([VarDecl(Id(dzX4), None, var, Id(DWW)), FuncDecl(Id(AJPi), [VarDecl(Id(KR6r), NumberType, None, None), VarDecl(Id(Q9), StringType, None, None), VarDecl(Id(wlg), ArrayType([43.58, 99.02, 21.43], BoolType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(Q3), [], Return()), FuncDecl(Id(Q0), [VarDecl(Id(AO), StringType, None, None), VarDecl(Id(yn), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115747))

	def test_21530115748(self):
		input = '''
func TdJ (number LI[9.92,72.18], bool In)	return

func JOy (bool YLt[89.76], bool blH, bool ur8v)	return
func UkG (bool bZhG, number Iz2r[58.35], string MlB)
	return
'''
		expect = '''Program([FuncDecl(Id(TdJ), [VarDecl(Id(LI), ArrayType([9.92, 72.18], NumberType), None, None), VarDecl(Id(In), BoolType, None, None)], Return()), FuncDecl(Id(JOy), [VarDecl(Id(YLt), ArrayType([89.76], BoolType), None, None), VarDecl(Id(blH), BoolType, None, None), VarDecl(Id(ur8v), BoolType, None, None)], Return()), FuncDecl(Id(UkG), [VarDecl(Id(bZhG), BoolType, None, None), VarDecl(Id(Iz2r), ArrayType([58.35], NumberType), None, None), VarDecl(Id(MlB), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115748))

	def test_21530115749(self):
		input = '''
number L1Dq
string Pa <- true
func lGf0 (string Sul[80.57,17.29], bool NjJ[68.88,64.17,98.24])
	return

func wuf (bool Lzd)	return false
func Bs (string c12G[74.41,25.07,66.08], number K8[15.63,47.96,91.39], bool GH)
	return 96.71
'''
		expect = '''Program([VarDecl(Id(L1Dq), NumberType, None, None), VarDecl(Id(Pa), StringType, None, BooleanLit(True)), FuncDecl(Id(lGf0), [VarDecl(Id(Sul), ArrayType([80.57, 17.29], StringType), None, None), VarDecl(Id(NjJ), ArrayType([68.88, 64.17, 98.24], BoolType), None, None)], Return()), FuncDecl(Id(wuf), [VarDecl(Id(Lzd), BoolType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(Bs), [VarDecl(Id(c12G), ArrayType([74.41, 25.07, 66.08], StringType), None, None), VarDecl(Id(K8), ArrayType([15.63, 47.96, 91.39], NumberType), None, None), VarDecl(Id(GH), BoolType, None, None)], Return(NumLit(96.71)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115749))

	def test_21530115750(self):
		input = '''
func fz (number MH[88.06,24.37,27.14], string wf)
	return true

func VZpp ()	return e7

number Ozso[25.47,72.57]
var o3QJ <- xR
number su <- true
'''
		expect = '''Program([FuncDecl(Id(fz), [VarDecl(Id(MH), ArrayType([88.06, 24.37, 27.14], NumberType), None, None), VarDecl(Id(wf), StringType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(VZpp), [], Return(Id(e7))), VarDecl(Id(Ozso), ArrayType([25.47, 72.57], NumberType), None, None), VarDecl(Id(o3QJ), None, var, Id(xR)), VarDecl(Id(su), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115750))

	def test_21530115751(self):
		input = '''
func GxHR (bool hXUl, bool vS[15.15,0.04], bool Pt)	return k0E8
'''
		expect = '''Program([FuncDecl(Id(GxHR), [VarDecl(Id(hXUl), BoolType, None, None), VarDecl(Id(vS), ArrayType([15.15, 0.04], BoolType), None, None), VarDecl(Id(Pt), BoolType, None, None)], Return(Id(k0E8)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115751))

	def test_21530115752(self):
		input = '''
string iUV7 <- false
number z3g <- "Aza"
func J4lG (bool Qy)	return 35.2
string gCzk[57.85,67.71,59.79]
'''
		expect = '''Program([VarDecl(Id(iUV7), StringType, None, BooleanLit(False)), VarDecl(Id(z3g), NumberType, None, StringLit(Aza)), FuncDecl(Id(J4lG), [VarDecl(Id(Qy), BoolType, None, None)], Return(NumLit(35.2))), VarDecl(Id(gCzk), ArrayType([57.85, 67.71, 59.79], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115752))

	def test_21530115753(self):
		input = '''
string kus[63.52,32.72,20.08]
string SM
'''
		expect = '''Program([VarDecl(Id(kus), ArrayType([63.52, 32.72, 20.08], StringType), None, None), VarDecl(Id(SM), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115753))

	def test_21530115754(self):
		input = '''
func nX (bool lyOZ, number WFf[48.49,20.22])
	return

func Cw (string ud, bool hB[17.71,49.68,57.77])	return false

bool NZ[89.89] <- "f"
'''
		expect = '''Program([FuncDecl(Id(nX), [VarDecl(Id(lyOZ), BoolType, None, None), VarDecl(Id(WFf), ArrayType([48.49, 20.22], NumberType), None, None)], Return()), FuncDecl(Id(Cw), [VarDecl(Id(ud), StringType, None, None), VarDecl(Id(hB), ArrayType([17.71, 49.68, 57.77], BoolType), None, None)], Return(BooleanLit(False))), VarDecl(Id(NZ), ArrayType([89.89], BoolType), None, StringLit(f))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115754))

	def test_21530115755(self):
		input = '''
func Mj7a ()
	return 60.99
'''
		expect = '''Program([FuncDecl(Id(Mj7a), [], Return(NumLit(60.99)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115755))

	def test_21530115756(self):
		input = '''
bool uH[87.36,10.65,16.59]
number d_ <- "dDQUt"
'''
		expect = '''Program([VarDecl(Id(uH), ArrayType([87.36, 10.65, 16.59], BoolType), None, None), VarDecl(Id(d_), NumberType, None, StringLit(dDQUt))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115756))

	def test_21530115757(self):
		input = '''
dynamic oeAE
string kU8 <- "SNi"
func R9 ()	return
func Uc (string c0Zo[0.91,86.63,5.57], bool Sr[87.77,87.15,75.8], bool hjJ)
	return

func ast (bool gZE7[31.58,91.2])
	return ahN

'''
		expect = '''Program([VarDecl(Id(oeAE), None, dynamic, None), VarDecl(Id(kU8), StringType, None, StringLit(SNi)), FuncDecl(Id(R9), [], Return()), FuncDecl(Id(Uc), [VarDecl(Id(c0Zo), ArrayType([0.91, 86.63, 5.57], StringType), None, None), VarDecl(Id(Sr), ArrayType([87.77, 87.15, 75.8], BoolType), None, None), VarDecl(Id(hjJ), BoolType, None, None)], Return()), FuncDecl(Id(ast), [VarDecl(Id(gZE7), ArrayType([31.58, 91.2], BoolType), None, None)], Return(Id(ahN)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115757))

	def test_21530115758(self):
		input = '''
func d74D (string Yv, string NH0B[78.26,2.22,80.29])
	begin
		return false
	end
func rx4 (bool pZ, bool BI, bool b7JL[27.76,22.5])	begin
		return "Ec"
		continue
	end
number TL39[64.22,63.89,77.23]
'''
		expect = '''Program([FuncDecl(Id(d74D), [VarDecl(Id(Yv), StringType, None, None), VarDecl(Id(NH0B), ArrayType([78.26, 2.22, 80.29], StringType), None, None)], Block([Return(BooleanLit(False))])), FuncDecl(Id(rx4), [VarDecl(Id(pZ), BoolType, None, None), VarDecl(Id(BI), BoolType, None, None), VarDecl(Id(b7JL), ArrayType([27.76, 22.5], BoolType), None, None)], Block([Return(StringLit(Ec)), Continue])), VarDecl(Id(TL39), ArrayType([64.22, 63.89, 77.23], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115758))

	def test_21530115759(self):
		input = '''
var Ua <- true
func epl (bool VzQ, string ur[32.4,93.54])
	begin
		return "IJ"
		break
	end

'''
		expect = '''Program([VarDecl(Id(Ua), None, var, BooleanLit(True)), FuncDecl(Id(epl), [VarDecl(Id(VzQ), BoolType, None, None), VarDecl(Id(ur), ArrayType([32.4, 93.54], StringType), None, None)], Block([Return(StringLit(IJ)), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115759))

	def test_21530115760(self):
		input = '''
string C8AK[71.11,73.51,25.72] <- "xbx"
func nu (string Om[40.53,43.28,32.31], string KDq[40.53], string Kp[86.88])	return 93.33

'''
		expect = '''Program([VarDecl(Id(C8AK), ArrayType([71.11, 73.51, 25.72], StringType), None, StringLit(xbx)), FuncDecl(Id(nu), [VarDecl(Id(Om), ArrayType([40.53, 43.28, 32.31], StringType), None, None), VarDecl(Id(KDq), ArrayType([40.53], StringType), None, None), VarDecl(Id(Kp), ArrayType([86.88], StringType), None, None)], Return(NumLit(93.33)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115760))

	def test_21530115761(self):
		input = '''
dynamic enl <- "EFfyK"
func XTV (bool KbNb, bool kfm[67.22,26.52,45.84], string H0)	return 68.95
'''
		expect = '''Program([VarDecl(Id(enl), None, dynamic, StringLit(EFfyK)), FuncDecl(Id(XTV), [VarDecl(Id(KbNb), BoolType, None, None), VarDecl(Id(kfm), ArrayType([67.22, 26.52, 45.84], BoolType), None, None), VarDecl(Id(H0), StringType, None, None)], Return(NumLit(68.95)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115761))

	def test_21530115762(self):
		input = '''
func wBL1 (number rt)
	begin
		Ivu[17.76] <- false
		for YAv until "H" by Iyi6
			number EI3C[72.06] <- PZk
	end

'''
		expect = '''Program([FuncDecl(Id(wBL1), [VarDecl(Id(rt), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(Ivu), [NumLit(17.76)]), BooleanLit(False)), For(Id(YAv), StringLit(H), Id(Iyi6), VarDecl(Id(EI3C), ArrayType([72.06], NumberType), None, Id(PZk)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115762))

	def test_21530115763(self):
		input = '''
func di8P ()
	return

func LDxf (string A52, string ae)
	begin
		wsd1 <- false
		if (71.06)
		break
		elif (true)
		continue
		elif ("tA") for QR until sQ8 by true
			continue
		else return "P"
	end

func Qa (number te[71.98,66.55], bool zA7B)	begin
		var p6 <- XCVm
	end

string ICbm[25.14,42.54] <- "Tc"
func rl2h (number HDF, bool qTaU[99.99], number aY[84.12])
	return "aQaTv"

'''
		expect = '''Program([FuncDecl(Id(di8P), [], Return()), FuncDecl(Id(LDxf), [VarDecl(Id(A52), StringType, None, None), VarDecl(Id(ae), StringType, None, None)], Block([AssignStmt(Id(wsd1), BooleanLit(False)), If(NumLit(71.06), Break), [(BooleanLit(True), Continue), (StringLit(tA), For(Id(QR), Id(sQ8), BooleanLit(True), Continue))], Return(StringLit(P))])), FuncDecl(Id(Qa), [VarDecl(Id(te), ArrayType([71.98, 66.55], NumberType), None, None), VarDecl(Id(zA7B), BoolType, None, None)], Block([VarDecl(Id(p6), None, var, Id(XCVm))])), VarDecl(Id(ICbm), ArrayType([25.14, 42.54], StringType), None, StringLit(Tc)), FuncDecl(Id(rl2h), [VarDecl(Id(HDF), NumberType, None, None), VarDecl(Id(qTaU), ArrayType([99.99], BoolType), None, None), VarDecl(Id(aY), ArrayType([84.12], NumberType), None, None)], Return(StringLit(aQaTv)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115763))

	def test_21530115764(self):
		input = '''
number r_I6
dynamic QVHC
func GYG (number sp5P)	return false
func up (bool BQHl[11.93,78.51,55.93])
	begin
		uUNy <- dlI
		klNY(21.07, pEO)
		continue
	end
'''
		expect = '''Program([VarDecl(Id(r_I6), NumberType, None, None), VarDecl(Id(QVHC), None, dynamic, None), FuncDecl(Id(GYG), [VarDecl(Id(sp5P), NumberType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(up), [VarDecl(Id(BQHl), ArrayType([11.93, 78.51, 55.93], BoolType), None, None)], Block([AssignStmt(Id(uUNy), Id(dlI)), CallStmt(Id(klNY), [NumLit(21.07), Id(pEO)]), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115764))

	def test_21530115765(self):
		input = '''
func LA ()	return Bo7
'''
		expect = '''Program([FuncDecl(Id(LA), [], Return(Id(Bo7)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115765))

	def test_21530115766(self):
		input = '''
func Mvg (number FtX, bool ellF[46.08,50.85])	return "A"
dynamic uDuo
'''
		expect = '''Program([FuncDecl(Id(Mvg), [VarDecl(Id(FtX), NumberType, None, None), VarDecl(Id(ellF), ArrayType([46.08, 50.85], BoolType), None, None)], Return(StringLit(A))), VarDecl(Id(uDuo), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115766))

	def test_21530115767(self):
		input = '''
bool Go[94.59,83.03,16.98]
func kAQ (number jSsh[43.23])
	return

func rcK7 (bool FP[36.72,50.56,42.47], bool mUl7, bool fX1[85.09,85.38])	return

'''
		expect = '''Program([VarDecl(Id(Go), ArrayType([94.59, 83.03, 16.98], BoolType), None, None), FuncDecl(Id(kAQ), [VarDecl(Id(jSsh), ArrayType([43.23], NumberType), None, None)], Return()), FuncDecl(Id(rcK7), [VarDecl(Id(FP), ArrayType([36.72, 50.56, 42.47], BoolType), None, None), VarDecl(Id(mUl7), BoolType, None, None), VarDecl(Id(fX1), ArrayType([85.09, 85.38], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115767))

	def test_21530115768(self):
		input = '''
func Qy (number JW[97.1,20.99,91.28], number nwWe[75.66,14.65,4.95], string NAp)	begin
		m1W(true, 15.08, true)
		for au7J until 92.65 by "Q"
			if ("db") continue
			elif (false) for QM until true by true
				return 85.25
			elif (se)
			KI()
			elif ("n") return
			elif (rd)
			break
			else begin
			end
	end

func YA ()	return 25.44
func wN ()	begin
		continue
		bool UY[2.37]
		return
	end
'''
		expect = '''Program([FuncDecl(Id(Qy), [VarDecl(Id(JW), ArrayType([97.1, 20.99, 91.28], NumberType), None, None), VarDecl(Id(nwWe), ArrayType([75.66, 14.65, 4.95], NumberType), None, None), VarDecl(Id(NAp), StringType, None, None)], Block([CallStmt(Id(m1W), [BooleanLit(True), NumLit(15.08), BooleanLit(True)]), For(Id(au7J), NumLit(92.65), StringLit(Q), If(StringLit(db), Continue), [(BooleanLit(False), For(Id(QM), BooleanLit(True), BooleanLit(True), Return(NumLit(85.25)))), (Id(se), CallStmt(Id(KI), [])), (StringLit(n), Return()), (Id(rd), Break)], Block([]))])), FuncDecl(Id(YA), [], Return(NumLit(25.44))), FuncDecl(Id(wN), [], Block([Continue, VarDecl(Id(UY), ArrayType([2.37], BoolType), None, None), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115768))

	def test_21530115769(self):
		input = '''
string RaPo
func ytQ ()	begin
		return "v"
		for ddPS until rsO5 by "ynpFB"
			Ez <- true
		if (62.61) break
		elif (84.46) begin
		end
		elif (62.81)
		if (34.3)
		for k0m until E9Hf by iSe3
			bool Ek
		elif (65.31)
		if (false)
		begin
			for wkv until "zyc" by 70.98
				continue
			if (true)
			hysN(true)
			elif (aEI)
			begin
				Xr <- true
			end
			else number rz[56.14,10.73] <- true
		end
		elif (true)
		begin
			if (ip7b) E6u1[22.83] <- false
			elif ("p") if (97.03)
			for j2St until s4h9 by 33.19
				break
			elif (Lq)
			begin
			end
			else if (91.85) if (27.61) cs5[80.64, bzFA] <- "Pn"
			elif (true)
			number Phl <- "VK"
			elif ("HuqJ")
			bool iH[40.54] <- r4Qw
			elif (82.59)
			u7g(CSl)
			elif (f9x)
			if (true)
			bool Gcye <- "h"
			elif (27.89)
			if ("Kzn") return
			elif ("n") break
			elif (dHrv)
			JL("jYJ", true)
			elif (ud2J) break
			else bool gQ[45.36,57.02] <- 42.05
			elif ("RvRYc") begin
				continue
			end
			else break
			elif (false)
			begin
				for vp_ until xG by 66.16
					if (91.74) for yipU until 38.75 by "Rit"
						break
					elif ("kgWUn")
					lk <- l8S
			end
			elif (false)
			continue
			elif (AAo)
			if (38.83) Mjt[Odld] <- "jHKYt"
			elif (false) if ("Poyf")
			begin
			end
			elif ("ZGPZs")
			begin
				break
				for fz until "lgc" by 34.51
					var Fzy <- yIYc
			end
			elif ("hQfYX")
			if (SZWc)
			string sP[31.44,65.05,60.62]
			elif (11.51)
			return
			else for WFHz until sJ7 by "JUlGk"
				number lFd
			else return
			continue
			zwRZ(89.73, HtJ)
		end
		elif (BtT) begin
		end
		elif (YOR) begin
		end
		else iE()
		else gfj(Ml4A, "uY")
	end

bool cj <- 50.68
string udQu[72.0,33.31]
func lCcf ()
	return
'''
		expect = '''Program([VarDecl(Id(RaPo), StringType, None, None), FuncDecl(Id(ytQ), [], Block([Return(StringLit(v)), For(Id(ddPS), Id(rsO5), StringLit(ynpFB), AssignStmt(Id(Ez), BooleanLit(True))), If(NumLit(62.61), Break), [(NumLit(84.46), Block([])), (NumLit(62.81), If(NumLit(34.3), For(Id(k0m), Id(E9Hf), Id(iSe3), VarDecl(Id(Ek), BoolType, None, None))), [], None), (NumLit(65.31), If(BooleanLit(False), Block([For(Id(wkv), StringLit(zyc), NumLit(70.98), Continue), If(BooleanLit(True), CallStmt(Id(hysN), [BooleanLit(True)])), [(Id(aEI), Block([AssignStmt(Id(Xr), BooleanLit(True))]))], VarDecl(Id(rz), ArrayType([56.14, 10.73], NumberType), None, BooleanLit(True))])), [(BooleanLit(True), Block([If(Id(ip7b), AssignStmt(ArrayCell(Id(E6u1), [NumLit(22.83)]), BooleanLit(False))), [(StringLit(p), If(NumLit(97.03), For(Id(j2St), Id(s4h9), NumLit(33.19), Break)), [(Id(Lq), Block([]))], If(NumLit(91.85), If(NumLit(27.61), AssignStmt(ArrayCell(Id(cs5), [NumLit(80.64), Id(bzFA)]), StringLit(Pn))), [(BooleanLit(True), VarDecl(Id(Phl), NumberType, None, StringLit(VK))), (StringLit(HuqJ), VarDecl(Id(iH), ArrayType([40.54], BoolType), None, Id(r4Qw))), (NumLit(82.59), CallStmt(Id(u7g), [Id(CSl)])), (Id(f9x), If(BooleanLit(True), VarDecl(Id(Gcye), BoolType, None, StringLit(h))), [(NumLit(27.89), If(StringLit(Kzn), Return()), [(StringLit(n), Break), (Id(dHrv), CallStmt(Id(JL), [StringLit(jYJ), BooleanLit(True)])), (Id(ud2J), Break)], VarDecl(Id(gQ), ArrayType([45.36, 57.02], BoolType), None, NumLit(42.05))), (StringLit(RvRYc), Block([Continue]))], Break), (BooleanLit(False), Block([For(Id(vp_), Id(xG), NumLit(66.16), If(NumLit(91.74), For(Id(yipU), NumLit(38.75), StringLit(Rit), Break)), [(StringLit(kgWUn), AssignStmt(Id(lk), Id(l8S)))], None)])), (BooleanLit(False), Continue), (Id(AAo), If(NumLit(38.83), AssignStmt(ArrayCell(Id(Mjt), [Id(Odld)]), StringLit(jHKYt))), [(BooleanLit(False), If(StringLit(Poyf), Block([])), [], None)], None), (StringLit(ZGPZs), Block([Break, For(Id(fz), StringLit(lgc), NumLit(34.51), VarDecl(Id(Fzy), None, var, Id(yIYc)))]))], None), [], None), (StringLit(hQfYX), If(Id(SZWc), VarDecl(Id(sP), ArrayType([31.44, 65.05, 60.62], StringType), None, None)), [(NumLit(11.51), Return())], For(Id(WFHz), Id(sJ7), StringLit(JUlGk), VarDecl(Id(lFd), NumberType, None, None)))], Return(), Continue, CallStmt(Id(zwRZ), [NumLit(89.73), Id(HtJ)])])), (Id(BtT), Block([])), (Id(YOR), Block([]))], CallStmt(Id(iE), []))], CallStmt(Id(gfj), [Id(Ml4A), StringLit(uY)])])), VarDecl(Id(cj), BoolType, None, NumLit(50.68)), VarDecl(Id(udQu), ArrayType([72.0, 33.31], StringType), None, None), FuncDecl(Id(lCcf), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115769))

	def test_21530115770(self):
		input = '''
func S7e (number CFF)
	return
'''
		expect = '''Program([FuncDecl(Id(S7e), [VarDecl(Id(CFF), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115770))

	def test_21530115771(self):
		input = '''
func Wh0U (bool yW[62.81], string qhx6[77.0,73.81], bool YH)	return

'''
		expect = '''Program([FuncDecl(Id(Wh0U), [VarDecl(Id(yW), ArrayType([62.81], BoolType), None, None), VarDecl(Id(qhx6), ArrayType([77.0, 73.81], StringType), None, None), VarDecl(Id(YH), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115771))

	def test_21530115772(self):
		input = '''
func lfB (number pUxF[71.82,3.03,33.52])	begin
		break
		begin
			begin
				break
				for nsE1 until jP by Mc
					if (gH) YSHi <- jegW
					elif (TVc0) lNMQ()
					elif ("zNaJZ")
					begin
					end
					elif (false) break
					elif (true) bool I3 <- false
				break
			end
			continue
			if ("LOID")
			if ("YT") continue
			elif (76.98)
			return
			elif (PCcz) Tz("WC", "rV", true)
			elif ("q") if ("aQGwy")
			return true
			elif ("cDkB")
			aY["zCYeR", 90.84, J3] <- z2Z
			elif (tm)
			continue
			elif (m6) number Mq[50.79,63.35,17.27] <- RHhL
			elif ("Q")
			rdfD["xA"] <- false
			elif (rH)
			for tx5 until 44.88 by "dvP"
				break
			else continue
			elif (Ar) znS()
			elif (MR)
			return
			else return "owxG"
		end
		break
	end

bool tMFE[41.77,1.2,49.34]
string jU[57.58]
number RLdb[74.85,56.75] <- "tn"
var BaI <- true
'''
		expect = '''Program([FuncDecl(Id(lfB), [VarDecl(Id(pUxF), ArrayType([71.82, 3.03, 33.52], NumberType), None, None)], Block([Break, Block([Block([Break, For(Id(nsE1), Id(jP), Id(Mc), If(Id(gH), AssignStmt(Id(YSHi), Id(jegW))), [(Id(TVc0), CallStmt(Id(lNMQ), [])), (StringLit(zNaJZ), Block([])), (BooleanLit(False), Break), (BooleanLit(True), VarDecl(Id(I3), BoolType, None, BooleanLit(False)))], None), Break]), Continue, If(StringLit(LOID), If(StringLit(YT), Continue), [(NumLit(76.98), Return()), (Id(PCcz), CallStmt(Id(Tz), [StringLit(WC), StringLit(rV), BooleanLit(True)])), (StringLit(q), If(StringLit(aQGwy), Return(BooleanLit(True))), [(StringLit(cDkB), AssignStmt(ArrayCell(Id(aY), [StringLit(zCYeR), NumLit(90.84), Id(J3)]), Id(z2Z))), (Id(tm), Continue), (Id(m6), VarDecl(Id(Mq), ArrayType([50.79, 63.35, 17.27], NumberType), None, Id(RHhL))), (StringLit(Q), AssignStmt(ArrayCell(Id(rdfD), [StringLit(xA)]), BooleanLit(False))), (Id(rH), For(Id(tx5), NumLit(44.88), StringLit(dvP), Break))], Continue), (Id(Ar), CallStmt(Id(znS), [])), (Id(MR), Return())], Return(StringLit(owxG))), [], None]), Break])), VarDecl(Id(tMFE), ArrayType([41.77, 1.2, 49.34], BoolType), None, None), VarDecl(Id(jU), ArrayType([57.58], StringType), None, None), VarDecl(Id(RLdb), ArrayType([74.85, 56.75], NumberType), None, StringLit(tn)), VarDecl(Id(BaI), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115772))

	def test_21530115773(self):
		input = '''
var jC <- true
string p6T5 <- 79.09
number zsm
func hl ()
	return 84.07
'''
		expect = '''Program([VarDecl(Id(jC), None, var, BooleanLit(True)), VarDecl(Id(p6T5), StringType, None, NumLit(79.09)), VarDecl(Id(zsm), NumberType, None, None), FuncDecl(Id(hl), [], Return(NumLit(84.07)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115773))

	def test_21530115774(self):
		input = '''
number Dt[29.93,43.55,26.59]
number zQ <- false
func mns (string Zy[42.27,67.22], bool CZjD[97.49])
	return FUB2

dynamic qXI <- true
func hlC7 ()	begin
		begin
		end
		gg("jwtSW", "WhvTO", true)
		break
	end
'''
		expect = '''Program([VarDecl(Id(Dt), ArrayType([29.93, 43.55, 26.59], NumberType), None, None), VarDecl(Id(zQ), NumberType, None, BooleanLit(False)), FuncDecl(Id(mns), [VarDecl(Id(Zy), ArrayType([42.27, 67.22], StringType), None, None), VarDecl(Id(CZjD), ArrayType([97.49], BoolType), None, None)], Return(Id(FUB2))), VarDecl(Id(qXI), None, dynamic, BooleanLit(True)), FuncDecl(Id(hlC7), [], Block([Block([]), CallStmt(Id(gg), [StringLit(jwtSW), StringLit(WhvTO), BooleanLit(True)]), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115774))

	def test_21530115775(self):
		input = '''
func DTCh (number xsHv[98.81,52.52,33.65], string LC)	return false

var MX <- df
'''
		expect = '''Program([FuncDecl(Id(DTCh), [VarDecl(Id(xsHv), ArrayType([98.81, 52.52, 33.65], NumberType), None, None), VarDecl(Id(LC), StringType, None, None)], Return(BooleanLit(False))), VarDecl(Id(MX), None, var, Id(df))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115775))

	def test_21530115776(self):
		input = '''
func eZ0 (number XX[65.03,98.37], string h1GS[15.39,18.73,67.66])
	return N9V
bool Ek[0.82] <- 82.28
dynamic XtK <- 27.84
string kb[98.35,91.34,32.68] <- "iarI"
func UX (string suv[29.51,5.97])	return
'''
		expect = '''Program([FuncDecl(Id(eZ0), [VarDecl(Id(XX), ArrayType([65.03, 98.37], NumberType), None, None), VarDecl(Id(h1GS), ArrayType([15.39, 18.73, 67.66], StringType), None, None)], Return(Id(N9V))), VarDecl(Id(Ek), ArrayType([0.82], BoolType), None, NumLit(82.28)), VarDecl(Id(XtK), None, dynamic, NumLit(27.84)), VarDecl(Id(kb), ArrayType([98.35, 91.34, 32.68], StringType), None, StringLit(iarI)), FuncDecl(Id(UX), [VarDecl(Id(suv), ArrayType([29.51, 5.97], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115776))

	def test_21530115777(self):
		input = '''
number ieZR[1.04,42.49]
func AhFO ()	return

bool B1[12.95]
'''
		expect = '''Program([VarDecl(Id(ieZR), ArrayType([1.04, 42.49], NumberType), None, None), FuncDecl(Id(AhFO), [], Return()), VarDecl(Id(B1), ArrayType([12.95], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115777))

	def test_21530115778(self):
		input = '''
string xIE0 <- YzW
func apz4 (bool nES[33.97,30.75,65.59])
	return
string XO <- 68.82
var G3 <- D4
func Ze (number ws8[83.88], bool T8, bool pnBk)	return

'''
		expect = '''Program([VarDecl(Id(xIE0), StringType, None, Id(YzW)), FuncDecl(Id(apz4), [VarDecl(Id(nES), ArrayType([33.97, 30.75, 65.59], BoolType), None, None)], Return()), VarDecl(Id(XO), StringType, None, NumLit(68.82)), VarDecl(Id(G3), None, var, Id(D4)), FuncDecl(Id(Ze), [VarDecl(Id(ws8), ArrayType([83.88], NumberType), None, None), VarDecl(Id(T8), BoolType, None, None), VarDecl(Id(pnBk), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115778))

	def test_21530115779(self):
		input = '''
string tC[25.82,62.71,24.34]
func t2g5 ()
	begin
		return true
	end
func tM ()
	return 57.71

string uy7[78.26]
string DG
'''
		expect = '''Program([VarDecl(Id(tC), ArrayType([25.82, 62.71, 24.34], StringType), None, None), FuncDecl(Id(t2g5), [], Block([Return(BooleanLit(True))])), FuncDecl(Id(tM), [], Return(NumLit(57.71))), VarDecl(Id(uy7), ArrayType([78.26], StringType), None, None), VarDecl(Id(DG), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115779))

	def test_21530115780(self):
		input = '''
number qZz[72.0,19.91]
func Wp (string cTlu, string IS, bool YTIt)	return 78.57
func Ndz (bool t0P[30.53], string ChVt, number H6S)
	begin
		if (true) iQdy(true, "Sf")
		elif (uP4) for Pv until true by false
			Cbp[95.69, false, "WAR"] <- "jWpsR"
		elif (true) continue
		else bool R9j <- O_
	end
'''
		expect = '''Program([VarDecl(Id(qZz), ArrayType([72.0, 19.91], NumberType), None, None), FuncDecl(Id(Wp), [VarDecl(Id(cTlu), StringType, None, None), VarDecl(Id(IS), StringType, None, None), VarDecl(Id(YTIt), BoolType, None, None)], Return(NumLit(78.57))), FuncDecl(Id(Ndz), [VarDecl(Id(t0P), ArrayType([30.53], BoolType), None, None), VarDecl(Id(ChVt), StringType, None, None), VarDecl(Id(H6S), NumberType, None, None)], Block([If(BooleanLit(True), CallStmt(Id(iQdy), [BooleanLit(True), StringLit(Sf)])), [(Id(uP4), For(Id(Pv), BooleanLit(True), BooleanLit(False), AssignStmt(ArrayCell(Id(Cbp), [NumLit(95.69), BooleanLit(False), StringLit(WAR)]), StringLit(jWpsR)))), (BooleanLit(True), Continue)], VarDecl(Id(R9j), BoolType, None, Id(O_))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115780))

	def test_21530115781(self):
		input = '''
func LIBw (string OgB)	return

bool wHc[75.96,71.02,33.48] <- s4x
func FNB (bool RP[61.89,86.81], bool RV[67.81,35.22], string utZ[26.41,97.41])	return

'''
		expect = '''Program([FuncDecl(Id(LIBw), [VarDecl(Id(OgB), StringType, None, None)], Return()), VarDecl(Id(wHc), ArrayType([75.96, 71.02, 33.48], BoolType), None, Id(s4x)), FuncDecl(Id(FNB), [VarDecl(Id(RP), ArrayType([61.89, 86.81], BoolType), None, None), VarDecl(Id(RV), ArrayType([67.81, 35.22], BoolType), None, None), VarDecl(Id(utZ), ArrayType([26.41, 97.41], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115781))

	def test_21530115782(self):
		input = '''
func OP (bool UKZ3[15.48])
	return

func vB (bool MM)
	return

number CF4y
'''
		expect = '''Program([FuncDecl(Id(OP), [VarDecl(Id(UKZ3), ArrayType([15.48], BoolType), None, None)], Return()), FuncDecl(Id(vB), [VarDecl(Id(MM), BoolType, None, None)], Return()), VarDecl(Id(CF4y), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115782))

	def test_21530115783(self):
		input = '''
string KH[90.7] <- 92.36
bool YFB[40.49,65.23,0.52] <- "JvJ"
'''
		expect = '''Program([VarDecl(Id(KH), ArrayType([90.7], StringType), None, NumLit(92.36)), VarDecl(Id(YFB), ArrayType([40.49, 65.23, 0.52], BoolType), None, StringLit(JvJ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115783))

	def test_21530115784(self):
		input = '''
func cc1u (string pV, number dQZw[20.3], string Sjk)
	return

'''
		expect = '''Program([FuncDecl(Id(cc1u), [VarDecl(Id(pV), StringType, None, None), VarDecl(Id(dQZw), ArrayType([20.3], NumberType), None, None), VarDecl(Id(Sjk), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115784))

	def test_21530115785(self):
		input = '''
number uYh[35.85,24.98,94.17]
bool Gp[64.47,38.7] <- false
func FP (bool LJGI[94.52])
	return iP
var ik <- 41.91
'''
		expect = '''Program([VarDecl(Id(uYh), ArrayType([35.85, 24.98, 94.17], NumberType), None, None), VarDecl(Id(Gp), ArrayType([64.47, 38.7], BoolType), None, BooleanLit(False)), FuncDecl(Id(FP), [VarDecl(Id(LJGI), ArrayType([94.52], BoolType), None, None)], Return(Id(iP))), VarDecl(Id(ik), None, var, NumLit(41.91))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115785))

	def test_21530115786(self):
		input = '''
string BlU_[60.72] <- 99.47
func pw (number JaR[82.54,74.72,48.57], number rFO, bool Dp6[69.12,18.21,69.76])	return

func syEb (number PH[59.8])	return efQW
string th66
'''
		expect = '''Program([VarDecl(Id(BlU_), ArrayType([60.72], StringType), None, NumLit(99.47)), FuncDecl(Id(pw), [VarDecl(Id(JaR), ArrayType([82.54, 74.72, 48.57], NumberType), None, None), VarDecl(Id(rFO), NumberType, None, None), VarDecl(Id(Dp6), ArrayType([69.12, 18.21, 69.76], BoolType), None, None)], Return()), FuncDecl(Id(syEb), [VarDecl(Id(PH), ArrayType([59.8], NumberType), None, None)], Return(Id(efQW))), VarDecl(Id(th66), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115786))

	def test_21530115787(self):
		input = '''
number MVAH[99.9,85.38,63.09]
number km[66.39] <- "SBXy"
func VqNC (bool km[90.7,70.19,42.88])	begin
		yD5[true, "SDeR", Bh] <- false
		break
	end

func id ()	return

'''
		expect = '''Program([VarDecl(Id(MVAH), ArrayType([99.9, 85.38, 63.09], NumberType), None, None), VarDecl(Id(km), ArrayType([66.39], NumberType), None, StringLit(SBXy)), FuncDecl(Id(VqNC), [VarDecl(Id(km), ArrayType([90.7, 70.19, 42.88], BoolType), None, None)], Block([AssignStmt(ArrayCell(Id(yD5), [BooleanLit(True), StringLit(SDeR), Id(Bh)]), BooleanLit(False)), Break])), FuncDecl(Id(id), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115787))

	def test_21530115788(self):
		input = '''
func TbLo (bool MhJk)
	return

bool px8
func Xv ()	return
number kZx[48.27] <- true
func ADt (string IZq[23.1,95.3,23.88], number vyDc[33.74])	return
'''
		expect = '''Program([FuncDecl(Id(TbLo), [VarDecl(Id(MhJk), BoolType, None, None)], Return()), VarDecl(Id(px8), BoolType, None, None), FuncDecl(Id(Xv), [], Return()), VarDecl(Id(kZx), ArrayType([48.27], NumberType), None, BooleanLit(True)), FuncDecl(Id(ADt), [VarDecl(Id(IZq), ArrayType([23.1, 95.3, 23.88], StringType), None, None), VarDecl(Id(vyDc), ArrayType([33.74], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115788))

	def test_21530115789(self):
		input = '''
string M9v <- 25.05
func oWW (bool u9KN[99.3,31.26], string Di[82.92])	begin
		if (aO) break
		elif (wie)
		begin
			begin
				begin
					for H4w0 until WM by 20.03
						oq("Yoxzo")
					if ("E")
					continue
					elif (41.88) pI9I()
					elif (Jr)
					break
					elif (false) continue
					else return 89.22
					if (25.36)
					break
					else jL <- true
				end
				xqc[false, "Ke"] <- IU
			end
		end
	end
func QpX (bool wz0[52.07,85.8,58.56], number pi0z[17.58])	begin
	end
string oneh[15.14,96.36,97.2]
func fw (string U82t, bool GCo)	return kI
'''
		expect = '''Program([VarDecl(Id(M9v), StringType, None, NumLit(25.05)), FuncDecl(Id(oWW), [VarDecl(Id(u9KN), ArrayType([99.3, 31.26], BoolType), None, None), VarDecl(Id(Di), ArrayType([82.92], StringType), None, None)], Block([If(Id(aO), Break), [(Id(wie), Block([Block([Block([For(Id(H4w0), Id(WM), NumLit(20.03), CallStmt(Id(oq), [StringLit(Yoxzo)])), If(StringLit(E), Continue), [(NumLit(41.88), CallStmt(Id(pI9I), [])), (Id(Jr), Break), (BooleanLit(False), Continue)], Return(NumLit(89.22)), If(NumLit(25.36), Break), [], AssignStmt(Id(jL), BooleanLit(True))]), AssignStmt(ArrayCell(Id(xqc), [BooleanLit(False), StringLit(Ke)]), Id(IU))])]))], None])), FuncDecl(Id(QpX), [VarDecl(Id(wz0), ArrayType([52.07, 85.8, 58.56], BoolType), None, None), VarDecl(Id(pi0z), ArrayType([17.58], NumberType), None, None)], Block([])), VarDecl(Id(oneh), ArrayType([15.14, 96.36, 97.2], StringType), None, None), FuncDecl(Id(fw), [VarDecl(Id(U82t), StringType, None, None), VarDecl(Id(GCo), BoolType, None, None)], Return(Id(kI)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115789))

	def test_21530115790(self):
		input = '''
string Ilw1[76.7] <- "ptrRs"
func k9 (number iEV[62.42])
	return

func fP (number cO[42.84], string juNz)
	return true
number XR8[8.69,77.84]
'''
		expect = '''Program([VarDecl(Id(Ilw1), ArrayType([76.7], StringType), None, StringLit(ptrRs)), FuncDecl(Id(k9), [VarDecl(Id(iEV), ArrayType([62.42], NumberType), None, None)], Return()), FuncDecl(Id(fP), [VarDecl(Id(cO), ArrayType([42.84], NumberType), None, None), VarDecl(Id(juNz), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(XR8), ArrayType([8.69, 77.84], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115790))

	def test_21530115791(self):
		input = '''
func Z5dY (number kV)	begin
		break
	end
func YBAs (string lAy)
	begin
		continue
	end

bool E01P
'''
		expect = '''Program([FuncDecl(Id(Z5dY), [VarDecl(Id(kV), NumberType, None, None)], Block([Break])), FuncDecl(Id(YBAs), [VarDecl(Id(lAy), StringType, None, None)], Block([Continue])), VarDecl(Id(E01P), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115791))

	def test_21530115792(self):
		input = '''
func pkmk (number EbfD[39.39], number wI, bool r6GI)	return

number g1[47.64,80.14,86.6]
number FY[36.97,43.98]
func fG ()	return
func XzA (number CO, string KaBs, number lW[13.02])	begin
		continue
		UZ["FncW", false] <- 30.5
		return "z"
	end

'''
		expect = '''Program([FuncDecl(Id(pkmk), [VarDecl(Id(EbfD), ArrayType([39.39], NumberType), None, None), VarDecl(Id(wI), NumberType, None, None), VarDecl(Id(r6GI), BoolType, None, None)], Return()), VarDecl(Id(g1), ArrayType([47.64, 80.14, 86.6], NumberType), None, None), VarDecl(Id(FY), ArrayType([36.97, 43.98], NumberType), None, None), FuncDecl(Id(fG), [], Return()), FuncDecl(Id(XzA), [VarDecl(Id(CO), NumberType, None, None), VarDecl(Id(KaBs), StringType, None, None), VarDecl(Id(lW), ArrayType([13.02], NumberType), None, None)], Block([Continue, AssignStmt(ArrayCell(Id(UZ), [StringLit(FncW), BooleanLit(False)]), NumLit(30.5)), Return(StringLit(z))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115792))

	def test_21530115793(self):
		input = '''
func MMot (number Rg[83.51])	begin
		return aC
		oD_("FkD", "L", yow)
	end

bool yVf[64.45,73.83]
'''
		expect = '''Program([FuncDecl(Id(MMot), [VarDecl(Id(Rg), ArrayType([83.51], NumberType), None, None)], Block([Return(Id(aC)), CallStmt(Id(oD_), [StringLit(FkD), StringLit(L), Id(yow)])])), VarDecl(Id(yVf), ArrayType([64.45, 73.83], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115793))

	def test_21530115794(self):
		input = '''
var rG <- false
func hZBO (string ThKN, bool nh_, bool eu6z[54.25])	return

func yIC (bool j71)	return
number TUWl[48.72] <- 4.04
dynamic TXZ <- "mdYcc"
'''
		expect = '''Program([VarDecl(Id(rG), None, var, BooleanLit(False)), FuncDecl(Id(hZBO), [VarDecl(Id(ThKN), StringType, None, None), VarDecl(Id(nh_), BoolType, None, None), VarDecl(Id(eu6z), ArrayType([54.25], BoolType), None, None)], Return()), FuncDecl(Id(yIC), [VarDecl(Id(j71), BoolType, None, None)], Return()), VarDecl(Id(TUWl), ArrayType([48.72], NumberType), None, NumLit(4.04)), VarDecl(Id(TXZ), None, dynamic, StringLit(mdYcc))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115794))

	def test_21530115795(self):
		input = '''
func AJ5 (number eZl7, number RI8D)
	return "dV"
'''
		expect = '''Program([FuncDecl(Id(AJ5), [VarDecl(Id(eZl7), NumberType, None, None), VarDecl(Id(RI8D), NumberType, None, None)], Return(StringLit(dV)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115795))

	def test_21530115796(self):
		input = '''
bool DoHs[10.65]
func GS (bool DH, number S2, number xei[39.98,95.49])	begin
	end

func x53 (string rn1[7.25])
	begin
		for wrOx until pxg by true
			break
	end
number NrnG
func ioG ()	return

'''
		expect = '''Program([VarDecl(Id(DoHs), ArrayType([10.65], BoolType), None, None), FuncDecl(Id(GS), [VarDecl(Id(DH), BoolType, None, None), VarDecl(Id(S2), NumberType, None, None), VarDecl(Id(xei), ArrayType([39.98, 95.49], NumberType), None, None)], Block([])), FuncDecl(Id(x53), [VarDecl(Id(rn1), ArrayType([7.25], StringType), None, None)], Block([For(Id(wrOx), Id(pxg), BooleanLit(True), Break)])), VarDecl(Id(NrnG), NumberType, None, None), FuncDecl(Id(ioG), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115796))

	def test_21530115797(self):
		input = '''
func ziu1 (number lI[67.33,17.94,91.91])
	begin
		CP8o()
		RNi("LPM", "JXT", 8.6)
	end
bool DVt[30.96,18.02,35.75]
bool YW
func h5t (string Rlf, number fBL4[81.05,63.48])
	return 38.83
'''
		expect = '''Program([FuncDecl(Id(ziu1), [VarDecl(Id(lI), ArrayType([67.33, 17.94, 91.91], NumberType), None, None)], Block([CallStmt(Id(CP8o), []), CallStmt(Id(RNi), [StringLit(LPM), StringLit(JXT), NumLit(8.6)])])), VarDecl(Id(DVt), ArrayType([30.96, 18.02, 35.75], BoolType), None, None), VarDecl(Id(YW), BoolType, None, None), FuncDecl(Id(h5t), [VarDecl(Id(Rlf), StringType, None, None), VarDecl(Id(fBL4), ArrayType([81.05, 63.48], NumberType), None, None)], Return(NumLit(38.83)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115797))

	def test_21530115798(self):
		input = '''
func nAbh (number ypI[25.92])
	begin
		NS <- true
		continue
		return
	end
var Fu <- 27.57
bool mj[38.55,87.24]
'''
		expect = '''Program([FuncDecl(Id(nAbh), [VarDecl(Id(ypI), ArrayType([25.92], NumberType), None, None)], Block([AssignStmt(Id(NS), BooleanLit(True)), Continue, Return()])), VarDecl(Id(Fu), None, var, NumLit(27.57)), VarDecl(Id(mj), ArrayType([38.55, 87.24], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115798))

	def test_21530115799(self):
		input = '''
func ww (bool ehK, number N1vZ, string ie)
	return

number bhI[61.26] <- "xk"
func Bu6 (string pd0, number ZPwG[10.67,57.71], number tpy5[98.78,56.54,5.94])
	return

bool zQA[89.6,94.99,13.29]
var WBn <- false
'''
		expect = '''Program([FuncDecl(Id(ww), [VarDecl(Id(ehK), BoolType, None, None), VarDecl(Id(N1vZ), NumberType, None, None), VarDecl(Id(ie), StringType, None, None)], Return()), VarDecl(Id(bhI), ArrayType([61.26], NumberType), None, StringLit(xk)), FuncDecl(Id(Bu6), [VarDecl(Id(pd0), StringType, None, None), VarDecl(Id(ZPwG), ArrayType([10.67, 57.71], NumberType), None, None), VarDecl(Id(tpy5), ArrayType([98.78, 56.54, 5.94], NumberType), None, None)], Return()), VarDecl(Id(zQA), ArrayType([89.6, 94.99, 13.29], BoolType), None, None), VarDecl(Id(WBn), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115799))

	def test_21530115800(self):
		input = '''
string Uz[60.81,84.42,99.74] <- 14.77
number iBjD <- 15.75
string HD <- false
func I2va (string lF, bool KU[24.96,57.56,41.14])
	return 81.99
func yjla ()	return ksTa

'''
		expect = '''Program([VarDecl(Id(Uz), ArrayType([60.81, 84.42, 99.74], StringType), None, NumLit(14.77)), VarDecl(Id(iBjD), NumberType, None, NumLit(15.75)), VarDecl(Id(HD), StringType, None, BooleanLit(False)), FuncDecl(Id(I2va), [VarDecl(Id(lF), StringType, None, None), VarDecl(Id(KU), ArrayType([24.96, 57.56, 41.14], BoolType), None, None)], Return(NumLit(81.99))), FuncDecl(Id(yjla), [], Return(Id(ksTa)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115800))

	def test_21530115801(self):
		input = '''
func GH (bool yJz, bool Ig7)
	return TG

bool zxLg[72.64]
string gh <- "SWc"
'''
		expect = '''Program([FuncDecl(Id(GH), [VarDecl(Id(yJz), BoolType, None, None), VarDecl(Id(Ig7), BoolType, None, None)], Return(Id(TG))), VarDecl(Id(zxLg), ArrayType([72.64], BoolType), None, None), VarDecl(Id(gh), StringType, None, StringLit(SWc))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115801))

	def test_21530115802(self):
		input = '''
string vo[6.18]
func z4 (number KaEP)	return ejtN

'''
		expect = '''Program([VarDecl(Id(vo), ArrayType([6.18], StringType), None, None), FuncDecl(Id(z4), [VarDecl(Id(KaEP), NumberType, None, None)], Return(Id(ejtN)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115802))

	def test_21530115803(self):
		input = '''
func xW ()
	return
'''
		expect = '''Program([FuncDecl(Id(xW), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115803))

	def test_21530115804(self):
		input = '''
string YQMI[48.3,89.57,26.07] <- he
string eBME <- false
func VVgh (bool prwN[37.72,55.75,66.54])
	return QJQ
func HNp (bool Iy[60.23,41.57,61.78])
	begin
		return
		begin
			string Nf
		end
	end
'''
		expect = '''Program([VarDecl(Id(YQMI), ArrayType([48.3, 89.57, 26.07], StringType), None, Id(he)), VarDecl(Id(eBME), StringType, None, BooleanLit(False)), FuncDecl(Id(VVgh), [VarDecl(Id(prwN), ArrayType([37.72, 55.75, 66.54], BoolType), None, None)], Return(Id(QJQ))), FuncDecl(Id(HNp), [VarDecl(Id(Iy), ArrayType([60.23, 41.57, 61.78], BoolType), None, None)], Block([Return(), Block([VarDecl(Id(Nf), StringType, None, None)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115804))

	def test_21530115805(self):
		input = '''
var EIdS <- Z2
func CZJD (bool G6U, bool va21, bool qL)
	return true

func beVL (bool JAla[81.69], bool fVI)	return
'''
		expect = '''Program([VarDecl(Id(EIdS), None, var, Id(Z2)), FuncDecl(Id(CZJD), [VarDecl(Id(G6U), BoolType, None, None), VarDecl(Id(va21), BoolType, None, None), VarDecl(Id(qL), BoolType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(beVL), [VarDecl(Id(JAla), ArrayType([81.69], BoolType), None, None), VarDecl(Id(fVI), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115805))

	def test_21530115806(self):
		input = '''
func yv ()
	return

func oaG (string xhJ[72.02,44.86])	begin
		continue
		break
	end
'''
		expect = '''Program([FuncDecl(Id(yv), [], Return()), FuncDecl(Id(oaG), [VarDecl(Id(xhJ), ArrayType([72.02, 44.86], StringType), None, None)], Block([Continue, Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115806))

	def test_21530115807(self):
		input = '''
func EES (number Idw[43.1])	return "J"
func RyM (string TX, string GUY)
	begin
		dh["daUR"] <- "V"
		for cbNT until rl by 25.85
			begin
			end
	end
'''
		expect = '''Program([FuncDecl(Id(EES), [VarDecl(Id(Idw), ArrayType([43.1], NumberType), None, None)], Return(StringLit(J))), FuncDecl(Id(RyM), [VarDecl(Id(TX), StringType, None, None), VarDecl(Id(GUY), StringType, None, None)], Block([AssignStmt(ArrayCell(Id(dh), [StringLit(daUR)]), StringLit(V)), For(Id(cbNT), Id(rl), NumLit(25.85), Block([]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115807))

	def test_21530115808(self):
		input = '''
string WgXz[49.21,93.03] <- "adLNJ"
'''
		expect = '''Program([VarDecl(Id(WgXz), ArrayType([49.21, 93.03], StringType), None, StringLit(adLNJ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115808))

	def test_21530115809(self):
		input = '''
func T3Q ()
	return UDL
dynamic BKq
func Gs35 (string UqT, number GgU, bool My[17.48,36.02,21.78])	return
'''
		expect = '''Program([FuncDecl(Id(T3Q), [], Return(Id(UDL))), VarDecl(Id(BKq), None, dynamic, None), FuncDecl(Id(Gs35), [VarDecl(Id(UqT), StringType, None, None), VarDecl(Id(GgU), NumberType, None, None), VarDecl(Id(My), ArrayType([17.48, 36.02, 21.78], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115809))

	def test_21530115810(self):
		input = '''
bool Rpo[66.63]
string nkNp
func wVJw ()	begin
		if (39.48) begin
			number L4[95.38,1.01]
			break
			continue
		end
		elif (71.67) return
		elif ("r")
		string XHu <- ZUg
		elif ("gZvA")
		continue
		elif (73.51)
		for anrT until FvjR by false
			return
		elif (Xs)
		begin
			continue
			dJZ[76.02, 71.86, true] <- true
			for Bk3S until "a" by F4
				continue
		end
		for mV until "Sd" by "FaMZ"
			for wSj until "qwP" by uOf
				return A6f
	end

string Nf <- VL
number zfz[76.99,25.82,81.84] <- 50.28
'''
		expect = '''Program([VarDecl(Id(Rpo), ArrayType([66.63], BoolType), None, None), VarDecl(Id(nkNp), StringType, None, None), FuncDecl(Id(wVJw), [], Block([If(NumLit(39.48), Block([VarDecl(Id(L4), ArrayType([95.38, 1.01], NumberType), None, None), Break, Continue])), [(NumLit(71.67), Return()), (StringLit(r), VarDecl(Id(XHu), StringType, None, Id(ZUg))), (StringLit(gZvA), Continue), (NumLit(73.51), For(Id(anrT), Id(FvjR), BooleanLit(False), Return())), (Id(Xs), Block([Continue, AssignStmt(ArrayCell(Id(dJZ), [NumLit(76.02), NumLit(71.86), BooleanLit(True)]), BooleanLit(True)), For(Id(Bk3S), StringLit(a), Id(F4), Continue)]))], None, For(Id(mV), StringLit(Sd), StringLit(FaMZ), For(Id(wSj), StringLit(qwP), Id(uOf), Return(Id(A6f))))])), VarDecl(Id(Nf), StringType, None, Id(VL)), VarDecl(Id(zfz), ArrayType([76.99, 25.82, 81.84], NumberType), None, NumLit(50.28))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115810))

	def test_21530115811(self):
		input = '''
func e4Qg (number Ne[22.31], bool neNG[96.61,35.06,14.66])	return

'''
		expect = '''Program([FuncDecl(Id(e4Qg), [VarDecl(Id(Ne), ArrayType([22.31], NumberType), None, None), VarDecl(Id(neNG), ArrayType([96.61, 35.06, 14.66], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115811))

	def test_21530115812(self):
		input = '''
func uVl (bool iV[90.7,76.11,50.36], bool PqYD[1.18,85.63])
	return

string HI[77.94,74.06] <- "swKww"
func zox (bool XR, string wdon, number wPKU[50.42,94.59])	return
'''
		expect = '''Program([FuncDecl(Id(uVl), [VarDecl(Id(iV), ArrayType([90.7, 76.11, 50.36], BoolType), None, None), VarDecl(Id(PqYD), ArrayType([1.18, 85.63], BoolType), None, None)], Return()), VarDecl(Id(HI), ArrayType([77.94, 74.06], StringType), None, StringLit(swKww)), FuncDecl(Id(zox), [VarDecl(Id(XR), BoolType, None, None), VarDecl(Id(wdon), StringType, None, None), VarDecl(Id(wPKU), ArrayType([50.42, 94.59], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115812))

	def test_21530115813(self):
		input = '''
number YI[1.62,27.61]
bool x5[23.37,30.94] <- "q"
'''
		expect = '''Program([VarDecl(Id(YI), ArrayType([1.62, 27.61], NumberType), None, None), VarDecl(Id(x5), ArrayType([23.37, 30.94], BoolType), None, StringLit(q))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115813))

	def test_21530115814(self):
		input = '''
bool Xfr2[86.58]
dynamic DMxE
number SRo[59.17] <- YN2
var oyM <- false
number kX3Q[85.15,20.88,98.09]
'''
		expect = '''Program([VarDecl(Id(Xfr2), ArrayType([86.58], BoolType), None, None), VarDecl(Id(DMxE), None, dynamic, None), VarDecl(Id(SRo), ArrayType([59.17], NumberType), None, Id(YN2)), VarDecl(Id(oyM), None, var, BooleanLit(False)), VarDecl(Id(kX3Q), ArrayType([85.15, 20.88, 98.09], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115814))

	def test_21530115815(self):
		input = '''
func Cv ()	return

number eY4_ <- "wmwv"
func nBUp (string mi[98.06,92.99,83.02])
	return false

func kNIR (string GSkL[18.71,94.33])	return 75.38
'''
		expect = '''Program([FuncDecl(Id(Cv), [], Return()), VarDecl(Id(eY4_), NumberType, None, StringLit(wmwv)), FuncDecl(Id(nBUp), [VarDecl(Id(mi), ArrayType([98.06, 92.99, 83.02], StringType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(kNIR), [VarDecl(Id(GSkL), ArrayType([18.71, 94.33], StringType), None, None)], Return(NumLit(75.38)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115815))

	def test_21530115816(self):
		input = '''
var pT <- ElgA
func Fl (string Jy, string BRl, number KLgQ[36.4])
	return
func hG ()	return true

string TLCQ
'''
		expect = '''Program([VarDecl(Id(pT), None, var, Id(ElgA)), FuncDecl(Id(Fl), [VarDecl(Id(Jy), StringType, None, None), VarDecl(Id(BRl), StringType, None, None), VarDecl(Id(KLgQ), ArrayType([36.4], NumberType), None, None)], Return()), FuncDecl(Id(hG), [], Return(BooleanLit(True))), VarDecl(Id(TLCQ), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115816))

	def test_21530115817(self):
		input = '''
func uXhH (bool ne3[62.99])	begin
	end
number gLl_[27.43,34.44,11.87]
'''
		expect = '''Program([FuncDecl(Id(uXhH), [VarDecl(Id(ne3), ArrayType([62.99], BoolType), None, None)], Block([])), VarDecl(Id(gLl_), ArrayType([27.43, 34.44, 11.87], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115817))

	def test_21530115818(self):
		input = '''
number UZ <- iW6
'''
		expect = '''Program([VarDecl(Id(UZ), NumberType, None, Id(iW6))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115818))

	def test_21530115819(self):
		input = '''
func be (string lqOn[97.72,32.29], number QQ9a, number epn[36.77,44.09])
	begin
		begin
			begin
			end
			break
		end
		break
		continue
	end

func VuLE (bool aoGe)	return true

bool q9[30.01,2.69]
func R1 (bool Kjt)	begin
	end
'''
		expect = '''Program([FuncDecl(Id(be), [VarDecl(Id(lqOn), ArrayType([97.72, 32.29], StringType), None, None), VarDecl(Id(QQ9a), NumberType, None, None), VarDecl(Id(epn), ArrayType([36.77, 44.09], NumberType), None, None)], Block([Block([Block([]), Break]), Break, Continue])), FuncDecl(Id(VuLE), [VarDecl(Id(aoGe), BoolType, None, None)], Return(BooleanLit(True))), VarDecl(Id(q9), ArrayType([30.01, 2.69], BoolType), None, None), FuncDecl(Id(R1), [VarDecl(Id(Kjt), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115819))

	def test_21530115820(self):
		input = '''
func xw (string gdyG, string jG[56.08,12.84,41.45])	return

string tDS
func t95 (bool Gk7, string Aem, string U8[60.88,57.55])	return NA

'''
		expect = '''Program([FuncDecl(Id(xw), [VarDecl(Id(gdyG), StringType, None, None), VarDecl(Id(jG), ArrayType([56.08, 12.84, 41.45], StringType), None, None)], Return()), VarDecl(Id(tDS), StringType, None, None), FuncDecl(Id(t95), [VarDecl(Id(Gk7), BoolType, None, None), VarDecl(Id(Aem), StringType, None, None), VarDecl(Id(U8), ArrayType([60.88, 57.55], StringType), None, None)], Return(Id(NA)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115820))

	def test_21530115821(self):
		input = '''
func fZ (number H6, string iFW[42.03,82.64])	return
number oEgb <- "crO"
dynamic TzRS
'''
		expect = '''Program([FuncDecl(Id(fZ), [VarDecl(Id(H6), NumberType, None, None), VarDecl(Id(iFW), ArrayType([42.03, 82.64], StringType), None, None)], Return()), VarDecl(Id(oEgb), NumberType, None, StringLit(crO)), VarDecl(Id(TzRS), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115821))

	def test_21530115822(self):
		input = '''
string NxCB[86.63,55.0]
func mTiw ()	return

func WX (bool Y_qG[12.23,78.52,11.86], string hEde[75.44,90.97,83.68])	return

string WEhu
number zNvr[45.9] <- true
'''
		expect = '''Program([VarDecl(Id(NxCB), ArrayType([86.63, 55.0], StringType), None, None), FuncDecl(Id(mTiw), [], Return()), FuncDecl(Id(WX), [VarDecl(Id(Y_qG), ArrayType([12.23, 78.52, 11.86], BoolType), None, None), VarDecl(Id(hEde), ArrayType([75.44, 90.97, 83.68], StringType), None, None)], Return()), VarDecl(Id(WEhu), StringType, None, None), VarDecl(Id(zNvr), ArrayType([45.9], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115822))

	def test_21530115823(self):
		input = '''
string zUw
var brlM <- aBU9
'''
		expect = '''Program([VarDecl(Id(zUw), StringType, None, None), VarDecl(Id(brlM), None, var, Id(aBU9))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115823))

	def test_21530115824(self):
		input = '''
dynamic Mf <- T2
'''
		expect = '''Program([VarDecl(Id(Mf), None, dynamic, Id(T2))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115824))

	def test_21530115825(self):
		input = '''
func Yxe (number sX[93.61,52.29], string Vl, number w8)
	begin
		return "MDU"
	end

number u4E[92.28,18.99] <- true
'''
		expect = '''Program([FuncDecl(Id(Yxe), [VarDecl(Id(sX), ArrayType([93.61, 52.29], NumberType), None, None), VarDecl(Id(Vl), StringType, None, None), VarDecl(Id(w8), NumberType, None, None)], Block([Return(StringLit(MDU))])), VarDecl(Id(u4E), ArrayType([92.28, 18.99], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115825))

	def test_21530115826(self):
		input = '''
func U0I1 (number lE[85.23], bool NHX7[80.95,54.75,37.83], bool BzJl)
	begin
		gMt(Vs, 97.51)
		continue
	end
bool N9o[50.62,64.39,54.12]
'''
		expect = '''Program([FuncDecl(Id(U0I1), [VarDecl(Id(lE), ArrayType([85.23], NumberType), None, None), VarDecl(Id(NHX7), ArrayType([80.95, 54.75, 37.83], BoolType), None, None), VarDecl(Id(BzJl), BoolType, None, None)], Block([CallStmt(Id(gMt), [Id(Vs), NumLit(97.51)]), Continue])), VarDecl(Id(N9o), ArrayType([50.62, 64.39, 54.12], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115826))

	def test_21530115827(self):
		input = '''
number Qir <- 55.19
'''
		expect = '''Program([VarDecl(Id(Qir), NumberType, None, NumLit(55.19))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115827))

	def test_21530115828(self):
		input = '''
func XpbX (string ki8u, string MGX[95.53], string yF)
	return "cgDZ"

var rZ <- 87.79
func gjn (bool zkX[88.91])
	begin
		var yHD6 <- false
		for x7 until true by uU
			for k0 until 50.12 by "Z"
				break
	end
bool RLs_ <- 54.33
string F6I9[15.93,84.64] <- lS
'''
		expect = '''Program([FuncDecl(Id(XpbX), [VarDecl(Id(ki8u), StringType, None, None), VarDecl(Id(MGX), ArrayType([95.53], StringType), None, None), VarDecl(Id(yF), StringType, None, None)], Return(StringLit(cgDZ))), VarDecl(Id(rZ), None, var, NumLit(87.79)), FuncDecl(Id(gjn), [VarDecl(Id(zkX), ArrayType([88.91], BoolType), None, None)], Block([VarDecl(Id(yHD6), None, var, BooleanLit(False)), For(Id(x7), BooleanLit(True), Id(uU), For(Id(k0), NumLit(50.12), StringLit(Z), Break))])), VarDecl(Id(RLs_), BoolType, None, NumLit(54.33)), VarDecl(Id(F6I9), ArrayType([15.93, 84.64], StringType), None, Id(lS))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115828))

	def test_21530115829(self):
		input = '''
func OtC6 ()
	begin
		bool Tsi
		continue
		return true
	end
'''
		expect = '''Program([FuncDecl(Id(OtC6), [], Block([VarDecl(Id(Tsi), BoolType, None, None), Continue, Return(BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115829))

	def test_21530115830(self):
		input = '''
string yFYS
string mFA4[60.3] <- "SE"
'''
		expect = '''Program([VarDecl(Id(yFYS), StringType, None, None), VarDecl(Id(mFA4), ArrayType([60.3], StringType), None, StringLit(SE))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115830))

	def test_21530115831(self):
		input = '''
string FK[43.45]
func Xu ()
	begin
		return 8.81
		return "TKhqn"
		for fBE_ until ggyx by false
			continue
	end

func e8 ()
	return
'''
		expect = '''Program([VarDecl(Id(FK), ArrayType([43.45], StringType), None, None), FuncDecl(Id(Xu), [], Block([Return(NumLit(8.81)), Return(StringLit(TKhqn)), For(Id(fBE_), Id(ggyx), BooleanLit(False), Continue)])), FuncDecl(Id(e8), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115831))

	def test_21530115832(self):
		input = '''
string KVUc[12.52,57.91,53.88] <- true
'''
		expect = '''Program([VarDecl(Id(KVUc), ArrayType([12.52, 57.91, 53.88], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115832))

	def test_21530115833(self):
		input = '''
func FK (bool kozZ)
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(FK), [VarDecl(Id(kozZ), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115833))

	def test_21530115834(self):
		input = '''
func Wu (number V_S[82.61,46.12,25.92])
	return

number fld[34.14] <- v42
'''
		expect = '''Program([FuncDecl(Id(Wu), [VarDecl(Id(V_S), ArrayType([82.61, 46.12, 25.92], NumberType), None, None)], Return()), VarDecl(Id(fld), ArrayType([34.14], NumberType), None, Id(v42))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115834))

	def test_21530115835(self):
		input = '''
func DVZ (bool xc1, bool x4Z2, number hK[65.76,6.72])	return
'''
		expect = '''Program([FuncDecl(Id(DVZ), [VarDecl(Id(xc1), BoolType, None, None), VarDecl(Id(x4Z2), BoolType, None, None), VarDecl(Id(hK), ArrayType([65.76, 6.72], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115835))

	def test_21530115836(self):
		input = '''
func gXZB (string zOc, string oR)
	return

dynamic Mf5
func XG (number PV1[19.76,94.78])
	return false
func rx (string A3n[23.29])
	begin
		IL[false] <- 18.43
	end

'''
		expect = '''Program([FuncDecl(Id(gXZB), [VarDecl(Id(zOc), StringType, None, None), VarDecl(Id(oR), StringType, None, None)], Return()), VarDecl(Id(Mf5), None, dynamic, None), FuncDecl(Id(XG), [VarDecl(Id(PV1), ArrayType([19.76, 94.78], NumberType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(rx), [VarDecl(Id(A3n), ArrayType([23.29], StringType), None, None)], Block([AssignStmt(ArrayCell(Id(IL), [BooleanLit(False)]), NumLit(18.43))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115836))

	def test_21530115837(self):
		input = '''
func Z4W (number vHOo[2.16], string SyP9[29.21,30.86,42.17], bool DZv_[37.45])
	return

var Rbb7 <- true
func mI (bool SZUe[24.41])	return 34.93

string UHF[99.75,59.6,47.48] <- "mjQT"
'''
		expect = '''Program([FuncDecl(Id(Z4W), [VarDecl(Id(vHOo), ArrayType([2.16], NumberType), None, None), VarDecl(Id(SyP9), ArrayType([29.21, 30.86, 42.17], StringType), None, None), VarDecl(Id(DZv_), ArrayType([37.45], BoolType), None, None)], Return()), VarDecl(Id(Rbb7), None, var, BooleanLit(True)), FuncDecl(Id(mI), [VarDecl(Id(SZUe), ArrayType([24.41], BoolType), None, None)], Return(NumLit(34.93))), VarDecl(Id(UHF), ArrayType([99.75, 59.6, 47.48], StringType), None, StringLit(mjQT))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115837))

	def test_21530115838(self):
		input = '''
number zn[37.07,59.21,83.66] <- "fYRVh"
func srY (number tkFJ[56.16,35.4,87.14], number bpY[32.72,28.57,82.86])
	begin
		break
	end
'''
		expect = '''Program([VarDecl(Id(zn), ArrayType([37.07, 59.21, 83.66], NumberType), None, StringLit(fYRVh)), FuncDecl(Id(srY), [VarDecl(Id(tkFJ), ArrayType([56.16, 35.4, 87.14], NumberType), None, None), VarDecl(Id(bpY), ArrayType([32.72, 28.57, 82.86], NumberType), None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115838))

	def test_21530115839(self):
		input = '''
number PX[57.69] <- true
func VC (string EY, string kK)	return Kbnm

number Qx7g[51.42] <- ZsR
var c_xM <- 97.12
'''
		expect = '''Program([VarDecl(Id(PX), ArrayType([57.69], NumberType), None, BooleanLit(True)), FuncDecl(Id(VC), [VarDecl(Id(EY), StringType, None, None), VarDecl(Id(kK), StringType, None, None)], Return(Id(Kbnm))), VarDecl(Id(Qx7g), ArrayType([51.42], NumberType), None, Id(ZsR)), VarDecl(Id(c_xM), None, var, NumLit(97.12))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115839))

	def test_21530115840(self):
		input = '''
bool MfG[83.0,54.13] <- XT
'''
		expect = '''Program([VarDecl(Id(MfG), ArrayType([83.0, 54.13], BoolType), None, Id(XT))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115840))

	def test_21530115841(self):
		input = '''
dynamic jN_s <- false
func Ips ()	begin
		MkDf(p2Yd, ER, "UFD")
		string Vt <- pq
	end

func ws ()	begin
		bool Th[53.51]
		sdeT <- 14.14
	end
func CqC9 (number Np, string K7[83.99])	return

number PND3[40.54]
'''
		expect = '''Program([VarDecl(Id(jN_s), None, dynamic, BooleanLit(False)), FuncDecl(Id(Ips), [], Block([CallStmt(Id(MkDf), [Id(p2Yd), Id(ER), StringLit(UFD)]), VarDecl(Id(Vt), StringType, None, Id(pq))])), FuncDecl(Id(ws), [], Block([VarDecl(Id(Th), ArrayType([53.51], BoolType), None, None), AssignStmt(Id(sdeT), NumLit(14.14))])), FuncDecl(Id(CqC9), [VarDecl(Id(Np), NumberType, None, None), VarDecl(Id(K7), ArrayType([83.99], StringType), None, None)], Return()), VarDecl(Id(PND3), ArrayType([40.54], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115841))

	def test_21530115842(self):
		input = '''
dynamic r7
'''
		expect = '''Program([VarDecl(Id(r7), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115842))

	def test_21530115843(self):
		input = '''
func RS ()	begin
		string Sziz
		wSuk(true)
	end
number sd
bool W8IZ[29.72,15.75]
dynamic m0 <- oW6
number l3rg[91.14,33.12,87.59]
'''
		expect = '''Program([FuncDecl(Id(RS), [], Block([VarDecl(Id(Sziz), StringType, None, None), CallStmt(Id(wSuk), [BooleanLit(True)])])), VarDecl(Id(sd), NumberType, None, None), VarDecl(Id(W8IZ), ArrayType([29.72, 15.75], BoolType), None, None), VarDecl(Id(m0), None, dynamic, Id(oW6)), VarDecl(Id(l3rg), ArrayType([91.14, 33.12, 87.59], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115843))

	def test_21530115844(self):
		input = '''
string mc_
func iB ()
	return "kw"
func d__1 (bool qVp, bool nDPU, string lYU[92.52,57.91,25.15])
	return false
'''
		expect = '''Program([VarDecl(Id(mc_), StringType, None, None), FuncDecl(Id(iB), [], Return(StringLit(kw))), FuncDecl(Id(d__1), [VarDecl(Id(qVp), BoolType, None, None), VarDecl(Id(nDPU), BoolType, None, None), VarDecl(Id(lYU), ArrayType([92.52, 57.91, 25.15], StringType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115844))

	def test_21530115845(self):
		input = '''
func Myr (bool uZFV[58.23,34.44], string qj[33.7,72.88])
	return
func S_6 (string FE, string LQD, bool zFP[65.05])
	return

func jnE (string nfg)	return 75.88
'''
		expect = '''Program([FuncDecl(Id(Myr), [VarDecl(Id(uZFV), ArrayType([58.23, 34.44], BoolType), None, None), VarDecl(Id(qj), ArrayType([33.7, 72.88], StringType), None, None)], Return()), FuncDecl(Id(S_6), [VarDecl(Id(FE), StringType, None, None), VarDecl(Id(LQD), StringType, None, None), VarDecl(Id(zFP), ArrayType([65.05], BoolType), None, None)], Return()), FuncDecl(Id(jnE), [VarDecl(Id(nfg), StringType, None, None)], Return(NumLit(75.88)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115845))

	def test_21530115846(self):
		input = '''
func f1 (string KZoo[68.87,87.48], string j8[49.55,14.95])	return
func HH (bool nQ1, bool D9j[13.83], bool n7PR)	begin
	end

func cj (bool No[39.15,0.24,97.46], bool gFQ, string IvV[42.52,59.88,18.72])
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(f1), [VarDecl(Id(KZoo), ArrayType([68.87, 87.48], StringType), None, None), VarDecl(Id(j8), ArrayType([49.55, 14.95], StringType), None, None)], Return()), FuncDecl(Id(HH), [VarDecl(Id(nQ1), BoolType, None, None), VarDecl(Id(D9j), ArrayType([13.83], BoolType), None, None), VarDecl(Id(n7PR), BoolType, None, None)], Block([])), FuncDecl(Id(cj), [VarDecl(Id(No), ArrayType([39.15, 0.24, 97.46], BoolType), None, None), VarDecl(Id(gFQ), BoolType, None, None), VarDecl(Id(IvV), ArrayType([42.52, 59.88, 18.72], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115846))

	def test_21530115847(self):
		input = '''
string Kxvf[44.29,76.22]
func Mv ()	return true
func iD (number djN[3.36], string VyYX[87.74,66.43])
	return
'''
		expect = '''Program([VarDecl(Id(Kxvf), ArrayType([44.29, 76.22], StringType), None, None), FuncDecl(Id(Mv), [], Return(BooleanLit(True))), FuncDecl(Id(iD), [VarDecl(Id(djN), ArrayType([3.36], NumberType), None, None), VarDecl(Id(VyYX), ArrayType([87.74, 66.43], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115847))

	def test_21530115848(self):
		input = '''
number As[26.51]
bool B5U1
number kDck <- d9Qd
number h9hp <- 15.29
func W41 (bool dB[50.31,19.0,66.17], bool T828, number jU[20.01])	begin
		for o9a until "o" by 78.44
			bool iNpS
	end
'''
		expect = '''Program([VarDecl(Id(As), ArrayType([26.51], NumberType), None, None), VarDecl(Id(B5U1), BoolType, None, None), VarDecl(Id(kDck), NumberType, None, Id(d9Qd)), VarDecl(Id(h9hp), NumberType, None, NumLit(15.29)), FuncDecl(Id(W41), [VarDecl(Id(dB), ArrayType([50.31, 19.0, 66.17], BoolType), None, None), VarDecl(Id(T828), BoolType, None, None), VarDecl(Id(jU), ArrayType([20.01], NumberType), None, None)], Block([For(Id(o9a), StringLit(o), NumLit(78.44), VarDecl(Id(iNpS), BoolType, None, None))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115848))

	def test_21530115849(self):
		input = '''
func qIuh (string KE[0.88,23.81])	return 49.15
func tr (number bh[89.88], bool W3o8[10.39], bool P7c)
	begin
		if ("M")
		number M72C[3.14,32.19,63.62]
		elif (otKj)
		return
		elif (22.1)
		begin
			begin
				string wG <- Srni
				iF5()
			end
			for Rptb until b4 by "hGs"
				continue
		end
		else break
		ow[50.09, 11.97, 96.24] <- 19.45
		var ALwa <- nm
	end
func GN (number dGjO[23.55,29.33,59.95], string nvC)	return
'''
		expect = '''Program([FuncDecl(Id(qIuh), [VarDecl(Id(KE), ArrayType([0.88, 23.81], StringType), None, None)], Return(NumLit(49.15))), FuncDecl(Id(tr), [VarDecl(Id(bh), ArrayType([89.88], NumberType), None, None), VarDecl(Id(W3o8), ArrayType([10.39], BoolType), None, None), VarDecl(Id(P7c), BoolType, None, None)], Block([If(StringLit(M), VarDecl(Id(M72C), ArrayType([3.14, 32.19, 63.62], NumberType), None, None)), [(Id(otKj), Return()), (NumLit(22.1), Block([Block([VarDecl(Id(wG), StringType, None, Id(Srni)), CallStmt(Id(iF5), [])]), For(Id(Rptb), Id(b4), StringLit(hGs), Continue)]))], Break, AssignStmt(ArrayCell(Id(ow), [NumLit(50.09), NumLit(11.97), NumLit(96.24)]), NumLit(19.45)), VarDecl(Id(ALwa), None, var, Id(nm))])), FuncDecl(Id(GN), [VarDecl(Id(dGjO), ArrayType([23.55, 29.33, 59.95], NumberType), None, None), VarDecl(Id(nvC), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115849))

	def test_21530115850(self):
		input = '''
bool COcA[22.59,43.09]
func a9 (number Xih[48.65], number t62W, string FA)
	begin
		break
		continue
		for t3YS until "fjpM" by 94.55
			continue
	end

'''
		expect = '''Program([VarDecl(Id(COcA), ArrayType([22.59, 43.09], BoolType), None, None), FuncDecl(Id(a9), [VarDecl(Id(Xih), ArrayType([48.65], NumberType), None, None), VarDecl(Id(t62W), NumberType, None, None), VarDecl(Id(FA), StringType, None, None)], Block([Break, Continue, For(Id(t3YS), StringLit(fjpM), NumLit(94.55), Continue)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115850))

	def test_21530115851(self):
		input = '''
bool fq_z[68.23] <- 41.81
func o87 (string VEq[47.43,75.27], bool E21[62.9], number vPlt[95.5])
	return 37.66

func oMFC (string vsj9)
	return

bool natc <- "zUw"
'''
		expect = '''Program([VarDecl(Id(fq_z), ArrayType([68.23], BoolType), None, NumLit(41.81)), FuncDecl(Id(o87), [VarDecl(Id(VEq), ArrayType([47.43, 75.27], StringType), None, None), VarDecl(Id(E21), ArrayType([62.9], BoolType), None, None), VarDecl(Id(vPlt), ArrayType([95.5], NumberType), None, None)], Return(NumLit(37.66))), FuncDecl(Id(oMFC), [VarDecl(Id(vsj9), StringType, None, None)], Return()), VarDecl(Id(natc), BoolType, None, StringLit(zUw))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115851))

	def test_21530115852(self):
		input = '''
func m7 (string Av, string F7VB)
	return
func K3xz (string dRV[34.41,60.73], number rI)
	return

number ma2[8.43,76.82] <- "jBjXP"
func AQCj ()
	return w9zR

string yAV
'''
		expect = '''Program([FuncDecl(Id(m7), [VarDecl(Id(Av), StringType, None, None), VarDecl(Id(F7VB), StringType, None, None)], Return()), FuncDecl(Id(K3xz), [VarDecl(Id(dRV), ArrayType([34.41, 60.73], StringType), None, None), VarDecl(Id(rI), NumberType, None, None)], Return()), VarDecl(Id(ma2), ArrayType([8.43, 76.82], NumberType), None, StringLit(jBjXP)), FuncDecl(Id(AQCj), [], Return(Id(w9zR))), VarDecl(Id(yAV), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115852))

	def test_21530115853(self):
		input = '''
number ay
bool oTU[26.22,15.36]
bool r3P[39.65,29.32,11.16]
bool yF4H[36.69,83.28]
'''
		expect = '''Program([VarDecl(Id(ay), NumberType, None, None), VarDecl(Id(oTU), ArrayType([26.22, 15.36], BoolType), None, None), VarDecl(Id(r3P), ArrayType([39.65, 29.32, 11.16], BoolType), None, None), VarDecl(Id(yF4H), ArrayType([36.69, 83.28], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115853))

	def test_21530115854(self):
		input = '''
number qYdp <- "tFpq"
'''
		expect = '''Program([VarDecl(Id(qYdp), NumberType, None, StringLit(tFpq))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115854))

	def test_21530115855(self):
		input = '''
func s_4 (string joPf, string O_NE[24.22,4.22,67.78], bool o4)
	return

'''
		expect = '''Program([FuncDecl(Id(s_4), [VarDecl(Id(joPf), StringType, None, None), VarDecl(Id(O_NE), ArrayType([24.22, 4.22, 67.78], StringType), None, None), VarDecl(Id(o4), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115855))

	def test_21530115856(self):
		input = '''
string wt7M[85.44,32.88] <- "xqyj"
string bwB8[55.6,10.68,40.12] <- 44.15
'''
		expect = '''Program([VarDecl(Id(wt7M), ArrayType([85.44, 32.88], StringType), None, StringLit(xqyj)), VarDecl(Id(bwB8), ArrayType([55.6, 10.68, 40.12], StringType), None, NumLit(44.15))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115856))

	def test_21530115857(self):
		input = '''
func Ly ()
	return

bool NV1[89.26]
bool ek0[54.52]
'''
		expect = '''Program([FuncDecl(Id(Ly), [], Return()), VarDecl(Id(NV1), ArrayType([89.26], BoolType), None, None), VarDecl(Id(ek0), ArrayType([54.52], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115857))

	def test_21530115858(self):
		input = '''
number YPsB[23.53]
'''
		expect = '''Program([VarDecl(Id(YPsB), ArrayType([23.53], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115858))

	def test_21530115859(self):
		input = '''
number iTO2[46.95,68.6,27.99] <- HbnN
func d0GT ()	return 65.82

func E7is (bool Xw[55.56], bool lCYX[43.31,38.0])	return 19.64

func tu ()
	return AJoS
number Hd[78.81] <- 25.52
'''
		expect = '''Program([VarDecl(Id(iTO2), ArrayType([46.95, 68.6, 27.99], NumberType), None, Id(HbnN)), FuncDecl(Id(d0GT), [], Return(NumLit(65.82))), FuncDecl(Id(E7is), [VarDecl(Id(Xw), ArrayType([55.56], BoolType), None, None), VarDecl(Id(lCYX), ArrayType([43.31, 38.0], BoolType), None, None)], Return(NumLit(19.64))), FuncDecl(Id(tu), [], Return(Id(AJoS))), VarDecl(Id(Hd), ArrayType([78.81], NumberType), None, NumLit(25.52))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115859))

	def test_21530115860(self):
		input = '''
func t_ (number k6H, number hbC4, number OUT[90.87,15.35,25.91])
	begin
		E5Z("B", "AGjhL")
		MGH()
	end

func pc ()
	return "RF"

'''
		expect = '''Program([FuncDecl(Id(t_), [VarDecl(Id(k6H), NumberType, None, None), VarDecl(Id(hbC4), NumberType, None, None), VarDecl(Id(OUT), ArrayType([90.87, 15.35, 25.91], NumberType), None, None)], Block([CallStmt(Id(E5Z), [StringLit(B), StringLit(AGjhL)]), CallStmt(Id(MGH), [])])), FuncDecl(Id(pc), [], Return(StringLit(RF)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115860))

	def test_21530115861(self):
		input = '''
string shn[96.77]
func gtz (string st[77.87,86.84,63.07], number LMd)
	return false
'''
		expect = '''Program([VarDecl(Id(shn), ArrayType([96.77], StringType), None, None), FuncDecl(Id(gtz), [VarDecl(Id(st), ArrayType([77.87, 86.84, 63.07], StringType), None, None), VarDecl(Id(LMd), NumberType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115861))

	def test_21530115862(self):
		input = '''
number PE8h[15.81,85.66,7.01] <- 20.38
func z9u0 ()	begin
		for k8 until 41.78 by 1.27
			if (FiCB) continue
			elif (Ug4f)
			continue
			elif (D2b)
			break
		return 96.17
	end
func MO (string ZDT, bool ki[5.67,98.05], string ll[46.18])
	return 8.32
'''
		expect = '''Program([VarDecl(Id(PE8h), ArrayType([15.81, 85.66, 7.01], NumberType), None, NumLit(20.38)), FuncDecl(Id(z9u0), [], Block([For(Id(k8), NumLit(41.78), NumLit(1.27), If(Id(FiCB), Continue), [(Id(Ug4f), Continue), (Id(D2b), Break)], None), Return(NumLit(96.17))])), FuncDecl(Id(MO), [VarDecl(Id(ZDT), StringType, None, None), VarDecl(Id(ki), ArrayType([5.67, 98.05], BoolType), None, None), VarDecl(Id(ll), ArrayType([46.18], StringType), None, None)], Return(NumLit(8.32)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115862))

	def test_21530115863(self):
		input = '''
string PU <- "UAgP"
bool O71 <- F_Tu
func tTjF (string GNPx, number zV, bool RNx1)	return

func zgoR ()	begin
		return true
	end

func Xra5 (string mOmn)
	return
'''
		expect = '''Program([VarDecl(Id(PU), StringType, None, StringLit(UAgP)), VarDecl(Id(O71), BoolType, None, Id(F_Tu)), FuncDecl(Id(tTjF), [VarDecl(Id(GNPx), StringType, None, None), VarDecl(Id(zV), NumberType, None, None), VarDecl(Id(RNx1), BoolType, None, None)], Return()), FuncDecl(Id(zgoR), [], Block([Return(BooleanLit(True))])), FuncDecl(Id(Xra5), [VarDecl(Id(mOmn), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115863))

	def test_21530115864(self):
		input = '''
func TZU ()
	return 88.9
func EyNJ (bool Okz[23.51,41.39,1.43], bool xSj, bool Mr[8.5,6.49,30.92])
	return
func uB ()	return

'''
		expect = '''Program([FuncDecl(Id(TZU), [], Return(NumLit(88.9))), FuncDecl(Id(EyNJ), [VarDecl(Id(Okz), ArrayType([23.51, 41.39, 1.43], BoolType), None, None), VarDecl(Id(xSj), BoolType, None, None), VarDecl(Id(Mr), ArrayType([8.5, 6.49, 30.92], BoolType), None, None)], Return()), FuncDecl(Id(uB), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115864))

	def test_21530115865(self):
		input = '''
func VM ()	return
func L6g (number QK, string KM7u[26.11])	begin
		break
	end

number U7[5.48]
'''
		expect = '''Program([FuncDecl(Id(VM), [], Return()), FuncDecl(Id(L6g), [VarDecl(Id(QK), NumberType, None, None), VarDecl(Id(KM7u), ArrayType([26.11], StringType), None, None)], Block([Break])), VarDecl(Id(U7), ArrayType([5.48], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115865))

	def test_21530115866(self):
		input = '''
dynamic P11O <- false
dynamic lVn <- "yEdws"
func dSZ5 ()
	begin
		break
	end

func O6 ()
	return true
'''
		expect = '''Program([VarDecl(Id(P11O), None, dynamic, BooleanLit(False)), VarDecl(Id(lVn), None, dynamic, StringLit(yEdws)), FuncDecl(Id(dSZ5), [], Block([Break])), FuncDecl(Id(O6), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115866))

	def test_21530115867(self):
		input = '''
func AL (string Wd[81.78,10.05,92.96], bool wJ[7.21,76.64], string wrW)	return
string Coy_[77.1,35.57,72.04]
number OXl[78.3] <- true
'''
		expect = '''Program([FuncDecl(Id(AL), [VarDecl(Id(Wd), ArrayType([81.78, 10.05, 92.96], StringType), None, None), VarDecl(Id(wJ), ArrayType([7.21, 76.64], BoolType), None, None), VarDecl(Id(wrW), StringType, None, None)], Return()), VarDecl(Id(Coy_), ArrayType([77.1, 35.57, 72.04], StringType), None, None), VarDecl(Id(OXl), ArrayType([78.3], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115867))

	def test_21530115868(self):
		input = '''
number zz3b[3.96]
func zW (number RGaZ, number j0_, bool t40)
	return 26.07

number Jew[0.34]
dynamic Uk
bool QP[67.81,64.11] <- "d"
'''
		expect = '''Program([VarDecl(Id(zz3b), ArrayType([3.96], NumberType), None, None), FuncDecl(Id(zW), [VarDecl(Id(RGaZ), NumberType, None, None), VarDecl(Id(j0_), NumberType, None, None), VarDecl(Id(t40), BoolType, None, None)], Return(NumLit(26.07))), VarDecl(Id(Jew), ArrayType([0.34], NumberType), None, None), VarDecl(Id(Uk), None, dynamic, None), VarDecl(Id(QP), ArrayType([67.81, 64.11], BoolType), None, StringLit(d))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115868))

	def test_21530115869(self):
		input = '''
func U4BE (bool Kb[26.99,97.15], string Px)	return

bool h1[35.33] <- false
func JTwY (string ZtrR, number e12)
	return 79.76
bool H2L
'''
		expect = '''Program([FuncDecl(Id(U4BE), [VarDecl(Id(Kb), ArrayType([26.99, 97.15], BoolType), None, None), VarDecl(Id(Px), StringType, None, None)], Return()), VarDecl(Id(h1), ArrayType([35.33], BoolType), None, BooleanLit(False)), FuncDecl(Id(JTwY), [VarDecl(Id(ZtrR), StringType, None, None), VarDecl(Id(e12), NumberType, None, None)], Return(NumLit(79.76))), VarDecl(Id(H2L), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115869))

	def test_21530115870(self):
		input = '''
bool C4 <- uA
func asoC ()	return
string eQef
'''
		expect = '''Program([VarDecl(Id(C4), BoolType, None, Id(uA)), FuncDecl(Id(asoC), [], Return()), VarDecl(Id(eQef), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115870))

	def test_21530115871(self):
		input = '''
bool wU <- false
func E3bK (bool xRW, number OXwj[36.89,78.42,88.49], number Kj4o[90.55,36.43])
	return true
number VQ[85.73,98.49,53.02] <- true
func PDVP (string Vg8u[66.73,49.2])
	begin
		return
		return
	end
string N8WW[78.55] <- "djVVN"
'''
		expect = '''Program([VarDecl(Id(wU), BoolType, None, BooleanLit(False)), FuncDecl(Id(E3bK), [VarDecl(Id(xRW), BoolType, None, None), VarDecl(Id(OXwj), ArrayType([36.89, 78.42, 88.49], NumberType), None, None), VarDecl(Id(Kj4o), ArrayType([90.55, 36.43], NumberType), None, None)], Return(BooleanLit(True))), VarDecl(Id(VQ), ArrayType([85.73, 98.49, 53.02], NumberType), None, BooleanLit(True)), FuncDecl(Id(PDVP), [VarDecl(Id(Vg8u), ArrayType([66.73, 49.2], StringType), None, None)], Block([Return(), Return()])), VarDecl(Id(N8WW), ArrayType([78.55], StringType), None, StringLit(djVVN))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115871))

	def test_21530115872(self):
		input = '''
func aArc (number vOfE)
	return

func Qcf (bool A1[97.4], string w2O, bool OjT)
	begin
		begin
			GSey()
			L0Z()
		end
		break
	end
func mU10 (bool Ai, bool cb[29.98,58.1], bool pE)	begin
		continue
		dU9m[false, 40.6] <- Dq
		break
	end
'''
		expect = '''Program([FuncDecl(Id(aArc), [VarDecl(Id(vOfE), NumberType, None, None)], Return()), FuncDecl(Id(Qcf), [VarDecl(Id(A1), ArrayType([97.4], BoolType), None, None), VarDecl(Id(w2O), StringType, None, None), VarDecl(Id(OjT), BoolType, None, None)], Block([Block([CallStmt(Id(GSey), []), CallStmt(Id(L0Z), [])]), Break])), FuncDecl(Id(mU10), [VarDecl(Id(Ai), BoolType, None, None), VarDecl(Id(cb), ArrayType([29.98, 58.1], BoolType), None, None), VarDecl(Id(pE), BoolType, None, None)], Block([Continue, AssignStmt(ArrayCell(Id(dU9m), [BooleanLit(False), NumLit(40.6)]), Id(Dq)), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115872))

	def test_21530115873(self):
		input = '''
func SCf (bool p2[19.53,33.81,48.35], number P5PN)	begin
		for OtIF until oMz7 by 1.65
			if ("GKwX") eU("dh", 20.89)
			elif (true) continue
			elif (true)
			begin
				begin
					return
					bool uKm[76.43] <- 74.02
				end
				rlm(false, "gAze", 39.31)
				xTYX <- "seM"
			end
			elif (oPd)
			begin
				SMi6("z")
				if (jz) for oT until zjV by T9V
					N9VW <- e7K
				elif (false) az0 <- 12.11
				elif (false)
				J9()
				else begin
				end
			end
			elif (true)
			begin
			end
			else Uy(60.96)
	end
func bN0 (string r5LR[80.65,59.87], bool Fk0p, string HOK)
	return

'''
		expect = '''Program([FuncDecl(Id(SCf), [VarDecl(Id(p2), ArrayType([19.53, 33.81, 48.35], BoolType), None, None), VarDecl(Id(P5PN), NumberType, None, None)], Block([For(Id(OtIF), Id(oMz7), NumLit(1.65), If(StringLit(GKwX), CallStmt(Id(eU), [StringLit(dh), NumLit(20.89)])), [(BooleanLit(True), Continue), (BooleanLit(True), Block([Block([Return(), VarDecl(Id(uKm), ArrayType([76.43], BoolType), None, NumLit(74.02))]), CallStmt(Id(rlm), [BooleanLit(False), StringLit(gAze), NumLit(39.31)]), AssignStmt(Id(xTYX), StringLit(seM))])), (Id(oPd), Block([CallStmt(Id(SMi6), [StringLit(z)]), If(Id(jz), For(Id(oT), Id(zjV), Id(T9V), AssignStmt(Id(N9VW), Id(e7K)))), [(BooleanLit(False), AssignStmt(Id(az0), NumLit(12.11))), (BooleanLit(False), CallStmt(Id(J9), []))], Block([])])), (BooleanLit(True), Block([]))], CallStmt(Id(Uy), [NumLit(60.96)]))])), FuncDecl(Id(bN0), [VarDecl(Id(r5LR), ArrayType([80.65, 59.87], StringType), None, None), VarDecl(Id(Fk0p), BoolType, None, None), VarDecl(Id(HOK), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115873))

	def test_21530115874(self):
		input = '''
func HJKf (string Uy5j[31.64,34.41])
	return

'''
		expect = '''Program([FuncDecl(Id(HJKf), [VarDecl(Id(Uy5j), ArrayType([31.64, 34.41], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115874))

	def test_21530115875(self):
		input = '''
func JO (number yY[11.2], string hUlf[69.16], string RjSO)	begin
		iS("LOQld", 0.79)
	end

number P3hB
string uY[19.63]
bool DpFT[57.21,46.2,98.19]
'''
		expect = '''Program([FuncDecl(Id(JO), [VarDecl(Id(yY), ArrayType([11.2], NumberType), None, None), VarDecl(Id(hUlf), ArrayType([69.16], StringType), None, None), VarDecl(Id(RjSO), StringType, None, None)], Block([CallStmt(Id(iS), [StringLit(LOQld), NumLit(0.79)])])), VarDecl(Id(P3hB), NumberType, None, None), VarDecl(Id(uY), ArrayType([19.63], StringType), None, None), VarDecl(Id(DpFT), ArrayType([57.21, 46.2, 98.19], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115875))

	def test_21530115876(self):
		input = '''
var fGi <- 30.85
'''
		expect = '''Program([VarDecl(Id(fGi), None, var, NumLit(30.85))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115876))

	def test_21530115877(self):
		input = '''
func tKDc (bool BO3[51.51])	return jumn

dynamic ZV
number XmvK[60.04] <- 71.12
func vqv (number GgJB[69.84], number oO[32.05,72.55,12.18])
	return 83.02
'''
		expect = '''Program([FuncDecl(Id(tKDc), [VarDecl(Id(BO3), ArrayType([51.51], BoolType), None, None)], Return(Id(jumn))), VarDecl(Id(ZV), None, dynamic, None), VarDecl(Id(XmvK), ArrayType([60.04], NumberType), None, NumLit(71.12)), FuncDecl(Id(vqv), [VarDecl(Id(GgJB), ArrayType([69.84], NumberType), None, None), VarDecl(Id(oO), ArrayType([32.05, 72.55, 12.18], NumberType), None, None)], Return(NumLit(83.02)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115877))

	def test_21530115878(self):
		input = '''
func Pw (string E4J5)
	return YGt
func iJ (number aRo[44.07], number wQ, bool Gm5)	return

func zw (string laZI, number fj[4.28,2.64], number qfF[49.24])	begin
		for F_T until true by true
			break
	end
'''
		expect = '''Program([FuncDecl(Id(Pw), [VarDecl(Id(E4J5), StringType, None, None)], Return(Id(YGt))), FuncDecl(Id(iJ), [VarDecl(Id(aRo), ArrayType([44.07], NumberType), None, None), VarDecl(Id(wQ), NumberType, None, None), VarDecl(Id(Gm5), BoolType, None, None)], Return()), FuncDecl(Id(zw), [VarDecl(Id(laZI), StringType, None, None), VarDecl(Id(fj), ArrayType([4.28, 2.64], NumberType), None, None), VarDecl(Id(qfF), ArrayType([49.24], NumberType), None, None)], Block([For(Id(F_T), BooleanLit(True), BooleanLit(True), Break)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115878))

	def test_21530115879(self):
		input = '''
number hM <- 73.7
'''
		expect = '''Program([VarDecl(Id(hM), NumberType, None, NumLit(73.7))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115879))

	def test_21530115880(self):
		input = '''
func h7D (number eva, bool xY[26.41,81.88,19.8], bool qa1g[91.86,58.76,42.7])	return false

string km[40.17,40.54]
func xm (number Dxn[80.54,99.47], number RtR, number E3x[4.42,70.33,80.4])
	begin
		begin
			break
			v8B <- 20.8
		end
		return
		break
	end
string bGmM[12.04] <- aZ
func hr (bool NEo[24.39,35.26,22.22])	return
'''
		expect = '''Program([FuncDecl(Id(h7D), [VarDecl(Id(eva), NumberType, None, None), VarDecl(Id(xY), ArrayType([26.41, 81.88, 19.8], BoolType), None, None), VarDecl(Id(qa1g), ArrayType([91.86, 58.76, 42.7], BoolType), None, None)], Return(BooleanLit(False))), VarDecl(Id(km), ArrayType([40.17, 40.54], StringType), None, None), FuncDecl(Id(xm), [VarDecl(Id(Dxn), ArrayType([80.54, 99.47], NumberType), None, None), VarDecl(Id(RtR), NumberType, None, None), VarDecl(Id(E3x), ArrayType([4.42, 70.33, 80.4], NumberType), None, None)], Block([Block([Break, AssignStmt(Id(v8B), NumLit(20.8))]), Return(), Break])), VarDecl(Id(bGmM), ArrayType([12.04], StringType), None, Id(aZ)), FuncDecl(Id(hr), [VarDecl(Id(NEo), ArrayType([24.39, 35.26, 22.22], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115880))

	def test_21530115881(self):
		input = '''
func tjgx (string r2N[12.39,51.4])
	return
'''
		expect = '''Program([FuncDecl(Id(tjgx), [VarDecl(Id(r2N), ArrayType([12.39, 51.4], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115881))

	def test_21530115882(self):
		input = '''
func fyi (string EXb, string f9ym)	return

var Rc9k <- Jw
'''
		expect = '''Program([FuncDecl(Id(fyi), [VarDecl(Id(EXb), StringType, None, None), VarDecl(Id(f9ym), StringType, None, None)], Return()), VarDecl(Id(Rc9k), None, var, Id(Jw))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115882))

	def test_21530115883(self):
		input = '''
string pE[63.25]
func b71 (string Ow_)
	return "H"
func mo8 (number x7[70.05], bool Zx)
	begin
		continue
		if (bSZ)
		continue
		elif (47.92) return
	end

'''
		expect = '''Program([VarDecl(Id(pE), ArrayType([63.25], StringType), None, None), FuncDecl(Id(b71), [VarDecl(Id(Ow_), StringType, None, None)], Return(StringLit(H))), FuncDecl(Id(mo8), [VarDecl(Id(x7), ArrayType([70.05], NumberType), None, None), VarDecl(Id(Zx), BoolType, None, None)], Block([Continue, If(Id(bSZ), Continue), [(NumLit(47.92), Return())], None]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115883))

	def test_21530115884(self):
		input = '''
func DAa9 (string gsA[4.52,82.56,15.05])
	return
func MQGM ()
	begin
		bool Gp <- true
		begin
			for Mla until Ip by 60.81
				for r2H until "xqDPa" by "q"
					for DV until "ChyM" by "QtSnx"
						for SJ until 60.02 by "BBwu"
							begin
								begin
									od("cx", "gFhRf", 9.97)
									begin
										IFg[VNL, 30.06] <- "CToCS"
									end
								end
							end
			continue
			break
		end
		return true
	end
number BIV[46.32]
'''
		expect = '''Program([FuncDecl(Id(DAa9), [VarDecl(Id(gsA), ArrayType([4.52, 82.56, 15.05], StringType), None, None)], Return()), FuncDecl(Id(MQGM), [], Block([VarDecl(Id(Gp), BoolType, None, BooleanLit(True)), Block([For(Id(Mla), Id(Ip), NumLit(60.81), For(Id(r2H), StringLit(xqDPa), StringLit(q), For(Id(DV), StringLit(ChyM), StringLit(QtSnx), For(Id(SJ), NumLit(60.02), StringLit(BBwu), Block([Block([CallStmt(Id(od), [StringLit(cx), StringLit(gFhRf), NumLit(9.97)]), Block([AssignStmt(ArrayCell(Id(IFg), [Id(VNL), NumLit(30.06)]), StringLit(CToCS))])])]))))), Continue, Break]), Return(BooleanLit(True))])), VarDecl(Id(BIV), ArrayType([46.32], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115884))

	def test_21530115885(self):
		input = '''
string Fs <- Nc
var yEOn <- "VY"
number zL[97.12,78.47,9.4] <- 73.79
string pOP[54.32,73.36,85.36]
'''
		expect = '''Program([VarDecl(Id(Fs), StringType, None, Id(Nc)), VarDecl(Id(yEOn), None, var, StringLit(VY)), VarDecl(Id(zL), ArrayType([97.12, 78.47, 9.4], NumberType), None, NumLit(73.79)), VarDecl(Id(pOP), ArrayType([54.32, 73.36, 85.36], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115885))

	def test_21530115886(self):
		input = '''
number c2[25.06,96.85,18.44]
func Xz ()
	begin
	end
func zR9 (number gh, bool Ivpa, bool fcAG[8.27,79.36])
	return
'''
		expect = '''Program([VarDecl(Id(c2), ArrayType([25.06, 96.85, 18.44], NumberType), None, None), FuncDecl(Id(Xz), [], Block([])), FuncDecl(Id(zR9), [VarDecl(Id(gh), NumberType, None, None), VarDecl(Id(Ivpa), BoolType, None, None), VarDecl(Id(fcAG), ArrayType([8.27, 79.36], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115886))

	def test_21530115887(self):
		input = '''
func K_U (string Bjr, string TZVW[52.12,39.68])	begin
	end

func KYY3 (bool XhPS[16.51,51.32])
	return true
number zT[3.06,72.23,41.25] <- "LIgnC"
func o5 (bool FT)
	return Bu5
bool uw3R[45.45] <- "iCLUx"
'''
		expect = '''Program([FuncDecl(Id(K_U), [VarDecl(Id(Bjr), StringType, None, None), VarDecl(Id(TZVW), ArrayType([52.12, 39.68], StringType), None, None)], Block([])), FuncDecl(Id(KYY3), [VarDecl(Id(XhPS), ArrayType([16.51, 51.32], BoolType), None, None)], Return(BooleanLit(True))), VarDecl(Id(zT), ArrayType([3.06, 72.23, 41.25], NumberType), None, StringLit(LIgnC)), FuncDecl(Id(o5), [VarDecl(Id(FT), BoolType, None, None)], Return(Id(Bu5))), VarDecl(Id(uw3R), ArrayType([45.45], BoolType), None, StringLit(iCLUx))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115887))

	def test_21530115888(self):
		input = '''
number Rq[53.16,76.58] <- iiK
func v4 (bool FYj, bool odB2[26.57,4.16,96.77], string D1x[16.3,58.6])
	return Wm

func i3F (bool YDn[77.73], string ko[67.92,21.6,12.48], number vIU[35.86])	begin
		break
		if (false)
		for IY until 80.76 by 70.93
			number Gid1[16.54]
		elif (hLi)
		ntQ <- true
	end
'''
		expect = '''Program([VarDecl(Id(Rq), ArrayType([53.16, 76.58], NumberType), None, Id(iiK)), FuncDecl(Id(v4), [VarDecl(Id(FYj), BoolType, None, None), VarDecl(Id(odB2), ArrayType([26.57, 4.16, 96.77], BoolType), None, None), VarDecl(Id(D1x), ArrayType([16.3, 58.6], StringType), None, None)], Return(Id(Wm))), FuncDecl(Id(i3F), [VarDecl(Id(YDn), ArrayType([77.73], BoolType), None, None), VarDecl(Id(ko), ArrayType([67.92, 21.6, 12.48], StringType), None, None), VarDecl(Id(vIU), ArrayType([35.86], NumberType), None, None)], Block([Break, If(BooleanLit(False), For(Id(IY), NumLit(80.76), NumLit(70.93), VarDecl(Id(Gid1), ArrayType([16.54], NumberType), None, None))), [(Id(hLi), AssignStmt(Id(ntQ), BooleanLit(True)))], None]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115888))

	def test_21530115889(self):
		input = '''
number kh <- "Y"
'''
		expect = '''Program([VarDecl(Id(kh), NumberType, None, StringLit(Y))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115889))

	def test_21530115890(self):
		input = '''
func Ejs (number pe[19.93,81.71], string op[17.9])
	begin
		Gl <- "p"
		kM(12.25, ZIih, true)
	end

func IjaS (string J7Jy[48.36])
	return OuI
func USWN (number d1wG, bool A39f)	begin
		EjF3("MFrZ")
		for w8Y until xdj by true
			number ok[48.95,11.72] <- "izYpm"
		return
	end
'''
		expect = '''Program([FuncDecl(Id(Ejs), [VarDecl(Id(pe), ArrayType([19.93, 81.71], NumberType), None, None), VarDecl(Id(op), ArrayType([17.9], StringType), None, None)], Block([AssignStmt(Id(Gl), StringLit(p)), CallStmt(Id(kM), [NumLit(12.25), Id(ZIih), BooleanLit(True)])])), FuncDecl(Id(IjaS), [VarDecl(Id(J7Jy), ArrayType([48.36], StringType), None, None)], Return(Id(OuI))), FuncDecl(Id(USWN), [VarDecl(Id(d1wG), NumberType, None, None), VarDecl(Id(A39f), BoolType, None, None)], Block([CallStmt(Id(EjF3), [StringLit(MFrZ)]), For(Id(w8Y), Id(xdj), BooleanLit(True), VarDecl(Id(ok), ArrayType([48.95, 11.72], NumberType), None, StringLit(izYpm))), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115890))

	def test_21530115891(self):
		input = '''
func JGb (bool Ye[55.44,52.96], bool LDNC[0.6], number bN8k[17.54,59.86])
	begin
		begin
			for CAM until tVRY by tIgs
				ik[x2X, 37.57] <- false
			begin
				continue
			end
		end
		continue
	end

'''
		expect = '''Program([FuncDecl(Id(JGb), [VarDecl(Id(Ye), ArrayType([55.44, 52.96], BoolType), None, None), VarDecl(Id(LDNC), ArrayType([0.6], BoolType), None, None), VarDecl(Id(bN8k), ArrayType([17.54, 59.86], NumberType), None, None)], Block([Block([For(Id(CAM), Id(tVRY), Id(tIgs), AssignStmt(ArrayCell(Id(ik), [Id(x2X), NumLit(37.57)]), BooleanLit(False))), Block([Continue])]), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115891))

	def test_21530115892(self):
		input = '''
string vdZy
func HSJ ()
	begin
		begin
			break
			return
			return
		end
		break
	end

number oGM[55.67]
func jB (bool Qh[18.15])	return
func NG (string SPD, string WE, bool AoHh[14.36])
	begin
	end

'''
		expect = '''Program([VarDecl(Id(vdZy), StringType, None, None), FuncDecl(Id(HSJ), [], Block([Block([Break, Return(), Return()]), Break])), VarDecl(Id(oGM), ArrayType([55.67], NumberType), None, None), FuncDecl(Id(jB), [VarDecl(Id(Qh), ArrayType([18.15], BoolType), None, None)], Return()), FuncDecl(Id(NG), [VarDecl(Id(SPD), StringType, None, None), VarDecl(Id(WE), StringType, None, None), VarDecl(Id(AoHh), ArrayType([14.36], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115892))

	def test_21530115893(self):
		input = '''
bool FRH
number DMlR[1.47,77.79]
'''
		expect = '''Program([VarDecl(Id(FRH), BoolType, None, None), VarDecl(Id(DMlR), ArrayType([1.47, 77.79], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115893))

	def test_21530115894(self):
		input = '''
func A9K (bool V5NU, number Zgy, number jBR)
	begin
	end

var D5b9 <- RsC8
func D7B5 (bool AO[28.83], bool nJ[81.0,49.79], number iWLg[82.97,60.87,28.85])	return 41.21

string cQlC[4.88,52.16,51.53]
'''
		expect = '''Program([FuncDecl(Id(A9K), [VarDecl(Id(V5NU), BoolType, None, None), VarDecl(Id(Zgy), NumberType, None, None), VarDecl(Id(jBR), NumberType, None, None)], Block([])), VarDecl(Id(D5b9), None, var, Id(RsC8)), FuncDecl(Id(D7B5), [VarDecl(Id(AO), ArrayType([28.83], BoolType), None, None), VarDecl(Id(nJ), ArrayType([81.0, 49.79], BoolType), None, None), VarDecl(Id(iWLg), ArrayType([82.97, 60.87, 28.85], NumberType), None, None)], Return(NumLit(41.21))), VarDecl(Id(cQlC), ArrayType([4.88, 52.16, 51.53], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115894))

	def test_21530115895(self):
		input = '''
func KB ()	begin
		for s0 until "DiF" by "gyBS"
			return
	end
func QLw ()	return 2.93

func NP0 (string HX, string HK, string GYz)
	return
'''
		expect = '''Program([FuncDecl(Id(KB), [], Block([For(Id(s0), StringLit(DiF), StringLit(gyBS), Return())])), FuncDecl(Id(QLw), [], Return(NumLit(2.93))), FuncDecl(Id(NP0), [VarDecl(Id(HX), StringType, None, None), VarDecl(Id(HK), StringType, None, None), VarDecl(Id(GYz), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115895))

	def test_21530115896(self):
		input = '''
bool xIo[32.95] <- x5X
'''
		expect = '''Program([VarDecl(Id(xIo), ArrayType([32.95], BoolType), None, Id(x5X))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115896))

	def test_21530115897(self):
		input = '''
number vF
'''
		expect = '''Program([VarDecl(Id(vF), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115897))

	def test_21530115898(self):
		input = '''
bool HgA
func Pl (string h4y)	begin
		begin
			begin
				for OYM8 until true by 60.05
					continue
			end
		end
	end

func XxHB (number DIb)
	return

func QIFH ()	return

func SXN ()	return
'''
		expect = '''Program([VarDecl(Id(HgA), BoolType, None, None), FuncDecl(Id(Pl), [VarDecl(Id(h4y), StringType, None, None)], Block([Block([Block([For(Id(OYM8), BooleanLit(True), NumLit(60.05), Continue)])])])), FuncDecl(Id(XxHB), [VarDecl(Id(DIb), NumberType, None, None)], Return()), FuncDecl(Id(QIFH), [], Return()), FuncDecl(Id(SXN), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115898))

	def test_21530115899(self):
		input = '''
bool dg[89.5,66.03]
number kA <- e1U
number AS
dynamic Ga <- "AUDTy"
'''
		expect = '''Program([VarDecl(Id(dg), ArrayType([89.5, 66.03], BoolType), None, None), VarDecl(Id(kA), NumberType, None, Id(e1U)), VarDecl(Id(AS), NumberType, None, None), VarDecl(Id(Ga), None, dynamic, StringLit(AUDTy))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115899))

	def test_21530115900(self):
		input = '''
number KpJO[70.92,84.22]
func pcck (bool v0T[35.11,35.06], number ACb, number Cv_2)
	begin
	end

'''
		expect = '''Program([VarDecl(Id(KpJO), ArrayType([70.92, 84.22], NumberType), None, None), FuncDecl(Id(pcck), [VarDecl(Id(v0T), ArrayType([35.11, 35.06], BoolType), None, None), VarDecl(Id(ACb), NumberType, None, None), VarDecl(Id(Cv_2), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115900))

	def test_21530115901(self):
		input = '''
bool s9[59.54,66.49]
func CK (bool vhKd, number jM, string jt6[97.36,88.81,81.16])	return

bool xm3D <- false
number q5U <- "AbJE"
'''
		expect = '''Program([VarDecl(Id(s9), ArrayType([59.54, 66.49], BoolType), None, None), FuncDecl(Id(CK), [VarDecl(Id(vhKd), BoolType, None, None), VarDecl(Id(jM), NumberType, None, None), VarDecl(Id(jt6), ArrayType([97.36, 88.81, 81.16], StringType), None, None)], Return()), VarDecl(Id(xm3D), BoolType, None, BooleanLit(False)), VarDecl(Id(q5U), NumberType, None, StringLit(AbJE))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115901))

	def test_21530115902(self):
		input = '''
var JD <- FVc
'''
		expect = '''Program([VarDecl(Id(JD), None, var, Id(FVc))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115902))

	def test_21530115903(self):
		input = '''
string xEUs[50.03,37.86]
'''
		expect = '''Program([VarDecl(Id(xEUs), ArrayType([50.03, 37.86], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115903))

	def test_21530115904(self):
		input = '''
string rh8e[99.04]
func Kai (number R5F)
	return false

bool os
'''
		expect = '''Program([VarDecl(Id(rh8e), ArrayType([99.04], StringType), None, None), FuncDecl(Id(Kai), [VarDecl(Id(R5F), NumberType, None, None)], Return(BooleanLit(False))), VarDecl(Id(os), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115904))

	def test_21530115905(self):
		input = '''
number Ms[72.2,27.89,1.41] <- "s"
func yn ()
	return 38.87
var vu41 <- "B"
func ku (number JyBK[69.87,78.45,93.82], string g8e)
	return
func MoVR (number Ei)	return
'''
		expect = '''Program([VarDecl(Id(Ms), ArrayType([72.2, 27.89, 1.41], NumberType), None, StringLit(s)), FuncDecl(Id(yn), [], Return(NumLit(38.87))), VarDecl(Id(vu41), None, var, StringLit(B)), FuncDecl(Id(ku), [VarDecl(Id(JyBK), ArrayType([69.87, 78.45, 93.82], NumberType), None, None), VarDecl(Id(g8e), StringType, None, None)], Return()), FuncDecl(Id(MoVR), [VarDecl(Id(Ei), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115905))

	def test_21530115906(self):
		input = '''
bool n80l[34.57]
'''
		expect = '''Program([VarDecl(Id(n80l), ArrayType([34.57], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115906))

	def test_21530115907(self):
		input = '''
bool cBa[32.39,29.46] <- tw4I
func ff (string rj, string SL[4.23,12.4])	return true
string aFa[87.41] <- false
func tZOD (bool P_dB, string MyT1)
	return false

'''
		expect = '''Program([VarDecl(Id(cBa), ArrayType([32.39, 29.46], BoolType), None, Id(tw4I)), FuncDecl(Id(ff), [VarDecl(Id(rj), StringType, None, None), VarDecl(Id(SL), ArrayType([4.23, 12.4], StringType), None, None)], Return(BooleanLit(True))), VarDecl(Id(aFa), ArrayType([87.41], StringType), None, BooleanLit(False)), FuncDecl(Id(tZOD), [VarDecl(Id(P_dB), BoolType, None, None), VarDecl(Id(MyT1), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115907))

	def test_21530115908(self):
		input = '''
func IP (bool BNIf, string Tnl)	return "H"
func Dil (string Bmm, string yZXl, string Dj)	begin
		for iKte until 3.01 by "GQJ"
			return
		string Age
		IxK[89.94, false, uEg] <- "OS"
	end

func Qz (bool dZb[15.9], bool LOVs)	return
'''
		expect = '''Program([FuncDecl(Id(IP), [VarDecl(Id(BNIf), BoolType, None, None), VarDecl(Id(Tnl), StringType, None, None)], Return(StringLit(H))), FuncDecl(Id(Dil), [VarDecl(Id(Bmm), StringType, None, None), VarDecl(Id(yZXl), StringType, None, None), VarDecl(Id(Dj), StringType, None, None)], Block([For(Id(iKte), NumLit(3.01), StringLit(GQJ), Return()), VarDecl(Id(Age), StringType, None, None), AssignStmt(ArrayCell(Id(IxK), [NumLit(89.94), BooleanLit(False), Id(uEg)]), StringLit(OS))])), FuncDecl(Id(Qz), [VarDecl(Id(dZb), ArrayType([15.9], BoolType), None, None), VarDecl(Id(LOVs), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115908))

	def test_21530115909(self):
		input = '''
func Zh ()	return true
'''
		expect = '''Program([FuncDecl(Id(Zh), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115909))

	def test_21530115910(self):
		input = '''
func etaO (string JrW, bool tQLn[31.44,11.55,26.29])	begin
		break
	end
bool xb <- 31.6
func mp9 (number MC)
	return
number aSU[11.59] <- true
var N2v <- 20.24
'''
		expect = '''Program([FuncDecl(Id(etaO), [VarDecl(Id(JrW), StringType, None, None), VarDecl(Id(tQLn), ArrayType([31.44, 11.55, 26.29], BoolType), None, None)], Block([Break])), VarDecl(Id(xb), BoolType, None, NumLit(31.6)), FuncDecl(Id(mp9), [VarDecl(Id(MC), NumberType, None, None)], Return()), VarDecl(Id(aSU), ArrayType([11.59], NumberType), None, BooleanLit(True)), VarDecl(Id(N2v), None, var, NumLit(20.24))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115910))

	def test_21530115911(self):
		input = '''
number lE[70.22,3.44] <- false
'''
		expect = '''Program([VarDecl(Id(lE), ArrayType([70.22, 3.44], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115911))

	def test_21530115912(self):
		input = '''
bool viE[62.26,14.09]
'''
		expect = '''Program([VarDecl(Id(viE), ArrayType([62.26, 14.09], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115912))

	def test_21530115913(self):
		input = '''
func nbfG (bool kUxU[20.13,44.2,89.34], number U9hx)
	return 30.94

func wOH (string SKJp)	return

bool cP[11.2,85.51] <- 50.45
func sT (bool sqOA[50.47,97.63,9.78], number fPIh[95.73])
	return

'''
		expect = '''Program([FuncDecl(Id(nbfG), [VarDecl(Id(kUxU), ArrayType([20.13, 44.2, 89.34], BoolType), None, None), VarDecl(Id(U9hx), NumberType, None, None)], Return(NumLit(30.94))), FuncDecl(Id(wOH), [VarDecl(Id(SKJp), StringType, None, None)], Return()), VarDecl(Id(cP), ArrayType([11.2, 85.51], BoolType), None, NumLit(50.45)), FuncDecl(Id(sT), [VarDecl(Id(sqOA), ArrayType([50.47, 97.63, 9.78], BoolType), None, None), VarDecl(Id(fPIh), ArrayType([95.73], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115913))

	def test_21530115914(self):
		input = '''
func jxPN ()
	begin
		return
		return
		tfg7 <- xhn
	end
number mxB <- 1.03
'''
		expect = '''Program([FuncDecl(Id(jxPN), [], Block([Return(), Return(), AssignStmt(Id(tfg7), Id(xhn))])), VarDecl(Id(mxB), NumberType, None, NumLit(1.03))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115914))

	def test_21530115915(self):
		input = '''
func mk_ (bool Nnm[55.1,93.41], number pR0)	return "idyW"

func ef5 ()
	return true
'''
		expect = '''Program([FuncDecl(Id(mk_), [VarDecl(Id(Nnm), ArrayType([55.1, 93.41], BoolType), None, None), VarDecl(Id(pR0), NumberType, None, None)], Return(StringLit(idyW))), FuncDecl(Id(ef5), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115915))

	def test_21530115916(self):
		input = '''
func VqL (number KOX, number eM)	return cxHg

number CMd[74.81,18.43,93.6]
func cy7Z (bool atBM)	return Ou

func lqF (bool FdZ)
	return "Sr"
'''
		expect = '''Program([FuncDecl(Id(VqL), [VarDecl(Id(KOX), NumberType, None, None), VarDecl(Id(eM), NumberType, None, None)], Return(Id(cxHg))), VarDecl(Id(CMd), ArrayType([74.81, 18.43, 93.6], NumberType), None, None), FuncDecl(Id(cy7Z), [VarDecl(Id(atBM), BoolType, None, None)], Return(Id(Ou))), FuncDecl(Id(lqF), [VarDecl(Id(FdZ), BoolType, None, None)], Return(StringLit(Sr)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115916))

	def test_21530115917(self):
		input = '''
func vvk (number HK)	return

string oz7 <- true
dynamic JRrB <- true
'''
		expect = '''Program([FuncDecl(Id(vvk), [VarDecl(Id(HK), NumberType, None, None)], Return()), VarDecl(Id(oz7), StringType, None, BooleanLit(True)), VarDecl(Id(JRrB), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115917))

	def test_21530115918(self):
		input = '''
number O6[25.45]
func PP (number qP2F[88.59,65.86,5.81], string MNzX)
	begin
	end
func WfL (number TfM[27.87,24.85,42.22])	return
string Az[17.59,0.35] <- 17.22
func Wik4 ()
	return
'''
		expect = '''Program([VarDecl(Id(O6), ArrayType([25.45], NumberType), None, None), FuncDecl(Id(PP), [VarDecl(Id(qP2F), ArrayType([88.59, 65.86, 5.81], NumberType), None, None), VarDecl(Id(MNzX), StringType, None, None)], Block([])), FuncDecl(Id(WfL), [VarDecl(Id(TfM), ArrayType([27.87, 24.85, 42.22], NumberType), None, None)], Return()), VarDecl(Id(Az), ArrayType([17.59, 0.35], StringType), None, NumLit(17.22)), FuncDecl(Id(Wik4), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115918))

	def test_21530115919(self):
		input = '''
bool bzc
string rlL
bool c0zb[74.25] <- 91.31
'''
		expect = '''Program([VarDecl(Id(bzc), BoolType, None, None), VarDecl(Id(rlL), StringType, None, None), VarDecl(Id(c0zb), ArrayType([74.25], BoolType), None, NumLit(91.31))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115919))

	def test_21530115920(self):
		input = '''
func pD3u (number a0f, bool L1yu[82.28,52.61], string SSWn)	return

func Si ()	return A5xd

number bu6S[17.07]
dynamic PKpv
'''
		expect = '''Program([FuncDecl(Id(pD3u), [VarDecl(Id(a0f), NumberType, None, None), VarDecl(Id(L1yu), ArrayType([82.28, 52.61], BoolType), None, None), VarDecl(Id(SSWn), StringType, None, None)], Return()), FuncDecl(Id(Si), [], Return(Id(A5xd))), VarDecl(Id(bu6S), ArrayType([17.07], NumberType), None, None), VarDecl(Id(PKpv), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115920))

	def test_21530115921(self):
		input = '''
func Z2_W (bool VLJ[48.78,68.51], bool cf)
	return 1.7
func xBDt (string Cfjq[48.61,26.68,18.26])	begin
		string Hd[62.4,11.44] <- false
	end

'''
		expect = '''Program([FuncDecl(Id(Z2_W), [VarDecl(Id(VLJ), ArrayType([48.78, 68.51], BoolType), None, None), VarDecl(Id(cf), BoolType, None, None)], Return(NumLit(1.7))), FuncDecl(Id(xBDt), [VarDecl(Id(Cfjq), ArrayType([48.61, 26.68, 18.26], StringType), None, None)], Block([VarDecl(Id(Hd), ArrayType([62.4, 11.44], StringType), None, BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115921))

	def test_21530115922(self):
		input = '''
var cCK3 <- "ZjaD"
func BCMw (bool yOw, string QQ[61.9,11.54], number EjE)
	begin
		for bdvc until false by false
			continue
		continue
		begin
		end
	end

func Sn (string uYk1, number Oz, bool q3l)
	return h4SJ

func VkB (number qkB8, bool etSk[20.72,22.12])	return RVc
func UVQ (bool CHBg[85.55,64.57,31.83], number I0)	return

'''
		expect = '''Program([VarDecl(Id(cCK3), None, var, StringLit(ZjaD)), FuncDecl(Id(BCMw), [VarDecl(Id(yOw), BoolType, None, None), VarDecl(Id(QQ), ArrayType([61.9, 11.54], StringType), None, None), VarDecl(Id(EjE), NumberType, None, None)], Block([For(Id(bdvc), BooleanLit(False), BooleanLit(False), Continue), Continue, Block([])])), FuncDecl(Id(Sn), [VarDecl(Id(uYk1), StringType, None, None), VarDecl(Id(Oz), NumberType, None, None), VarDecl(Id(q3l), BoolType, None, None)], Return(Id(h4SJ))), FuncDecl(Id(VkB), [VarDecl(Id(qkB8), NumberType, None, None), VarDecl(Id(etSk), ArrayType([20.72, 22.12], BoolType), None, None)], Return(Id(RVc))), FuncDecl(Id(UVQ), [VarDecl(Id(CHBg), ArrayType([85.55, 64.57, 31.83], BoolType), None, None), VarDecl(Id(I0), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115922))

	def test_21530115923(self):
		input = '''
func Vj (string KNG, string gh[11.5,37.41], string GAK[13.92,88.35,85.37])
	return
'''
		expect = '''Program([FuncDecl(Id(Vj), [VarDecl(Id(KNG), StringType, None, None), VarDecl(Id(gh), ArrayType([11.5, 37.41], StringType), None, None), VarDecl(Id(GAK), ArrayType([13.92, 88.35, 85.37], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115923))

	def test_21530115924(self):
		input = '''
func g5K ()	begin
	end
func DQ (number X_Bl, bool aFAH[69.94,87.26])	return
bool GA <- "D"
dynamic NA
'''
		expect = '''Program([FuncDecl(Id(g5K), [], Block([])), FuncDecl(Id(DQ), [VarDecl(Id(X_Bl), NumberType, None, None), VarDecl(Id(aFAH), ArrayType([69.94, 87.26], BoolType), None, None)], Return()), VarDecl(Id(GA), BoolType, None, StringLit(D)), VarDecl(Id(NA), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115924))

	def test_21530115925(self):
		input = '''
bool da <- true
string jLr[13.33,69.35]
number hI9k
string uC0W
'''
		expect = '''Program([VarDecl(Id(da), BoolType, None, BooleanLit(True)), VarDecl(Id(jLr), ArrayType([13.33, 69.35], StringType), None, None), VarDecl(Id(hI9k), NumberType, None, None), VarDecl(Id(uC0W), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115925))

	def test_21530115926(self):
		input = '''
number Goui <- 48.96
func o1 (bool opX, bool CMQ[33.49,47.34,87.77], bool Rt9f)
	return

dynamic eNR <- 9.13
'''
		expect = '''Program([VarDecl(Id(Goui), NumberType, None, NumLit(48.96)), FuncDecl(Id(o1), [VarDecl(Id(opX), BoolType, None, None), VarDecl(Id(CMQ), ArrayType([33.49, 47.34, 87.77], BoolType), None, None), VarDecl(Id(Rt9f), BoolType, None, None)], Return()), VarDecl(Id(eNR), None, dynamic, NumLit(9.13))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115926))

	def test_21530115927(self):
		input = '''
func L9GE (number AF)	return "CpWm"
'''
		expect = '''Program([FuncDecl(Id(L9GE), [VarDecl(Id(AF), NumberType, None, None)], Return(StringLit(CpWm)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115927))

	def test_21530115928(self):
		input = '''
bool X4[28.27,38.85]
func P7_w (number pX, bool j6H)
	return

bool E4[86.03,65.66]
'''
		expect = '''Program([VarDecl(Id(X4), ArrayType([28.27, 38.85], BoolType), None, None), FuncDecl(Id(P7_w), [VarDecl(Id(pX), NumberType, None, None), VarDecl(Id(j6H), BoolType, None, None)], Return()), VarDecl(Id(E4), ArrayType([86.03, 65.66], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115928))

	def test_21530115929(self):
		input = '''
func iz ()
	return

func yRa (number SEP[0.02,32.2], number gRjA[25.52], string WY4t[52.86,32.24])	return

'''
		expect = '''Program([FuncDecl(Id(iz), [], Return()), FuncDecl(Id(yRa), [VarDecl(Id(SEP), ArrayType([0.02, 32.2], NumberType), None, None), VarDecl(Id(gRjA), ArrayType([25.52], NumberType), None, None), VarDecl(Id(WY4t), ArrayType([52.86, 32.24], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115929))

	def test_21530115930(self):
		input = '''
number Bb_[88.52,37.62,73.26]
'''
		expect = '''Program([VarDecl(Id(Bb_), ArrayType([88.52, 37.62, 73.26], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115930))

	def test_21530115931(self):
		input = '''
var CoWs <- false
number qE[45.09] <- false
func xBr (number NAQ7, string Nsf[62.79])	begin
	end

func DRO (number Ph[82.44,81.56,78.72], string Wr[70.4], bool y5x)
	begin
		begin
			if (42.49)
			number DplX[62.8,13.48]
			elif ("Vlqq") continue
			elif ("jpUnQ") for Mg until Dd by true
				break
			else for Po68 until ezE by false
				number YwFa[79.64]
			break
		end
	end
'''
		expect = '''Program([VarDecl(Id(CoWs), None, var, BooleanLit(False)), VarDecl(Id(qE), ArrayType([45.09], NumberType), None, BooleanLit(False)), FuncDecl(Id(xBr), [VarDecl(Id(NAQ7), NumberType, None, None), VarDecl(Id(Nsf), ArrayType([62.79], StringType), None, None)], Block([])), FuncDecl(Id(DRO), [VarDecl(Id(Ph), ArrayType([82.44, 81.56, 78.72], NumberType), None, None), VarDecl(Id(Wr), ArrayType([70.4], StringType), None, None), VarDecl(Id(y5x), BoolType, None, None)], Block([Block([If(NumLit(42.49), VarDecl(Id(DplX), ArrayType([62.8, 13.48], NumberType), None, None)), [(StringLit(Vlqq), Continue), (StringLit(jpUnQ), For(Id(Mg), Id(Dd), BooleanLit(True), Break))], For(Id(Po68), Id(ezE), BooleanLit(False), VarDecl(Id(YwFa), ArrayType([79.64], NumberType), None, None)), Break])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115931))

	def test_21530115932(self):
		input = '''
func J0P (number AB[12.76,52.36,10.48])
	begin
		break
		begin
		end
	end
func fBTb ()	begin
		return
	end

func g_ (bool U19, bool ds9[94.86], number lL)	begin
		if (false) return
		elif (true)
		return
		elif (xt) continue
	end
string u3o5[28.65,74.5,37.12] <- 24.93
'''
		expect = '''Program([FuncDecl(Id(J0P), [VarDecl(Id(AB), ArrayType([12.76, 52.36, 10.48], NumberType), None, None)], Block([Break, Block([])])), FuncDecl(Id(fBTb), [], Block([Return()])), FuncDecl(Id(g_), [VarDecl(Id(U19), BoolType, None, None), VarDecl(Id(ds9), ArrayType([94.86], BoolType), None, None), VarDecl(Id(lL), NumberType, None, None)], Block([If(BooleanLit(False), Return()), [(BooleanLit(True), Return()), (Id(xt), Continue)], None])), VarDecl(Id(u3o5), ArrayType([28.65, 74.5, 37.12], StringType), None, NumLit(24.93))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115932))

	def test_21530115933(self):
		input = '''
string FoH[64.76,85.45]
func Atu ()
	return
'''
		expect = '''Program([VarDecl(Id(FoH), ArrayType([64.76, 85.45], StringType), None, None), FuncDecl(Id(Atu), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115933))

	def test_21530115934(self):
		input = '''
string KES[90.31,34.81,14.34] <- "Mv"
func SZ ()	return

string qQN[39.31] <- l6gs
func CV (bool h086, bool sG, number uc)	return 79.64

'''
		expect = '''Program([VarDecl(Id(KES), ArrayType([90.31, 34.81, 14.34], StringType), None, StringLit(Mv)), FuncDecl(Id(SZ), [], Return()), VarDecl(Id(qQN), ArrayType([39.31], StringType), None, Id(l6gs)), FuncDecl(Id(CV), [VarDecl(Id(h086), BoolType, None, None), VarDecl(Id(sG), BoolType, None, None), VarDecl(Id(uc), NumberType, None, None)], Return(NumLit(79.64)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115934))

	def test_21530115935(self):
		input = '''
func HLs ()
	begin
		Yed(7.64, 27.57)
		number v9l1[58.29]
	end
'''
		expect = '''Program([FuncDecl(Id(HLs), [], Block([CallStmt(Id(Yed), [NumLit(7.64), NumLit(27.57)]), VarDecl(Id(v9l1), ArrayType([58.29], NumberType), None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115935))

	def test_21530115936(self):
		input = '''
number vBo[69.41,63.99,46.86]
bool imx
'''
		expect = '''Program([VarDecl(Id(vBo), ArrayType([69.41, 63.99, 46.86], NumberType), None, None), VarDecl(Id(imx), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115936))

	def test_21530115937(self):
		input = '''
number Ub7[39.67,70.99]
func Njn ()	return
'''
		expect = '''Program([VarDecl(Id(Ub7), ArrayType([39.67, 70.99], NumberType), None, None), FuncDecl(Id(Njn), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115937))

	def test_21530115938(self):
		input = '''
number P0N[32.79,76.85,78.34]
func qF (bool Xc, bool r7hO[81.28])
	return true

bool Ca <- true
func eBiQ (string wwTU[77.22,78.24], number Lok[10.16], bool AbRw)
	return true
string Nz[30.21,65.0,25.25]
'''
		expect = '''Program([VarDecl(Id(P0N), ArrayType([32.79, 76.85, 78.34], NumberType), None, None), FuncDecl(Id(qF), [VarDecl(Id(Xc), BoolType, None, None), VarDecl(Id(r7hO), ArrayType([81.28], BoolType), None, None)], Return(BooleanLit(True))), VarDecl(Id(Ca), BoolType, None, BooleanLit(True)), FuncDecl(Id(eBiQ), [VarDecl(Id(wwTU), ArrayType([77.22, 78.24], StringType), None, None), VarDecl(Id(Lok), ArrayType([10.16], NumberType), None, None), VarDecl(Id(AbRw), BoolType, None, None)], Return(BooleanLit(True))), VarDecl(Id(Nz), ArrayType([30.21, 65.0, 25.25], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115938))

	def test_21530115939(self):
		input = '''
func eOb2 ()
	begin
		if (Hfc) fu <- UkvA
		elif ("MdExV")
		L9yz()
		elif (66.68) continue
		else break
		return true
		dg("II", 80.77)
	end
bool kM[22.79,57.11,41.23] <- "Ww"
func GM (string Z4, number xZH[73.2])
	return "PRZOb"

var eb <- 19.42
'''
		expect = '''Program([FuncDecl(Id(eOb2), [], Block([If(Id(Hfc), AssignStmt(Id(fu), Id(UkvA))), [(StringLit(MdExV), CallStmt(Id(L9yz), [])), (NumLit(66.68), Continue)], Break, Return(BooleanLit(True)), CallStmt(Id(dg), [StringLit(II), NumLit(80.77)])])), VarDecl(Id(kM), ArrayType([22.79, 57.11, 41.23], BoolType), None, StringLit(Ww)), FuncDecl(Id(GM), [VarDecl(Id(Z4), StringType, None, None), VarDecl(Id(xZH), ArrayType([73.2], NumberType), None, None)], Return(StringLit(PRZOb))), VarDecl(Id(eb), None, var, NumLit(19.42))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115939))

	def test_21530115940(self):
		input = '''
func aUZ (string oG[78.91], number u1Jp[97.55,32.69,36.82])
	begin
	end
func AWxa ()
	return

func sTc (number nS8, number E4Hr)
	return "pe"

'''
		expect = '''Program([FuncDecl(Id(aUZ), [VarDecl(Id(oG), ArrayType([78.91], StringType), None, None), VarDecl(Id(u1Jp), ArrayType([97.55, 32.69, 36.82], NumberType), None, None)], Block([])), FuncDecl(Id(AWxa), [], Return()), FuncDecl(Id(sTc), [VarDecl(Id(nS8), NumberType, None, None), VarDecl(Id(E4Hr), NumberType, None, None)], Return(StringLit(pe)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115940))

	def test_21530115941(self):
		input = '''
func pf (string IS, string cdT, number nqoj)
	begin
		break
	end
func B1 (number Bil[97.14,86.62,35.15], bool jm[68.91,2.0], bool qe[5.35,42.15,82.24])
	return 70.28
func TsfU (bool ED[30.66,35.89], bool iTd)
	return 51.2

'''
		expect = '''Program([FuncDecl(Id(pf), [VarDecl(Id(IS), StringType, None, None), VarDecl(Id(cdT), StringType, None, None), VarDecl(Id(nqoj), NumberType, None, None)], Block([Break])), FuncDecl(Id(B1), [VarDecl(Id(Bil), ArrayType([97.14, 86.62, 35.15], NumberType), None, None), VarDecl(Id(jm), ArrayType([68.91, 2.0], BoolType), None, None), VarDecl(Id(qe), ArrayType([5.35, 42.15, 82.24], BoolType), None, None)], Return(NumLit(70.28))), FuncDecl(Id(TsfU), [VarDecl(Id(ED), ArrayType([30.66, 35.89], BoolType), None, None), VarDecl(Id(iTd), BoolType, None, None)], Return(NumLit(51.2)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115941))

	def test_21530115942(self):
		input = '''
string Ry[26.06] <- GAw5
func xRdH (bool qw, bool Qem[72.78,77.7], string jtT)	return

number AP[98.28,65.74,31.48] <- Nq
'''
		expect = '''Program([VarDecl(Id(Ry), ArrayType([26.06], StringType), None, Id(GAw5)), FuncDecl(Id(xRdH), [VarDecl(Id(qw), BoolType, None, None), VarDecl(Id(Qem), ArrayType([72.78, 77.7], BoolType), None, None), VarDecl(Id(jtT), StringType, None, None)], Return()), VarDecl(Id(AP), ArrayType([98.28, 65.74, 31.48], NumberType), None, Id(Nq))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115942))

	def test_21530115943(self):
		input = '''
number nE
number qNxJ[96.02]
bool Iz6[19.72] <- 28.1
'''
		expect = '''Program([VarDecl(Id(nE), NumberType, None, None), VarDecl(Id(qNxJ), ArrayType([96.02], NumberType), None, None), VarDecl(Id(Iz6), ArrayType([19.72], BoolType), None, NumLit(28.1))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115943))

	def test_21530115944(self):
		input = '''
func eDzF (string vDhP)
	begin
		if ("M") p4(false, 86.77)
		elif ("wN")
		for Euyi until 74.81 by true
			string S2pY <- 68.2
		elif (false)
		continue
		elif (61.11)
		ybm[true, 13.2, 50.08] <- JnJN
	end
func N9S (string k7)
	return
func H2 (bool xO, number DAzb[44.27], number Uhg[0.14])	return 47.43

func WS (bool ua7o[94.11,52.93])
	begin
		break
	end

'''
		expect = '''Program([FuncDecl(Id(eDzF), [VarDecl(Id(vDhP), StringType, None, None)], Block([If(StringLit(M), CallStmt(Id(p4), [BooleanLit(False), NumLit(86.77)])), [(StringLit(wN), For(Id(Euyi), NumLit(74.81), BooleanLit(True), VarDecl(Id(S2pY), StringType, None, NumLit(68.2)))), (BooleanLit(False), Continue), (NumLit(61.11), AssignStmt(ArrayCell(Id(ybm), [BooleanLit(True), NumLit(13.2), NumLit(50.08)]), Id(JnJN)))], None])), FuncDecl(Id(N9S), [VarDecl(Id(k7), StringType, None, None)], Return()), FuncDecl(Id(H2), [VarDecl(Id(xO), BoolType, None, None), VarDecl(Id(DAzb), ArrayType([44.27], NumberType), None, None), VarDecl(Id(Uhg), ArrayType([0.14], NumberType), None, None)], Return(NumLit(47.43))), FuncDecl(Id(WS), [VarDecl(Id(ua7o), ArrayType([94.11, 52.93], BoolType), None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115944))

	def test_21530115945(self):
		input = '''
func f7Ni ()
	return false
'''
		expect = '''Program([FuncDecl(Id(f7Ni), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115945))

	def test_21530115946(self):
		input = '''
func z9 (number idRN)	return
string v4
func HaKW (string Eom[94.79,40.16,19.73], number HH, string oBt[74.09,80.36])
	return

string DAUA[23.52,1.89,89.3] <- eu
string ZCd[37.87,93.05,5.14] <- 63.17
'''
		expect = '''Program([FuncDecl(Id(z9), [VarDecl(Id(idRN), NumberType, None, None)], Return()), VarDecl(Id(v4), StringType, None, None), FuncDecl(Id(HaKW), [VarDecl(Id(Eom), ArrayType([94.79, 40.16, 19.73], StringType), None, None), VarDecl(Id(HH), NumberType, None, None), VarDecl(Id(oBt), ArrayType([74.09, 80.36], StringType), None, None)], Return()), VarDecl(Id(DAUA), ArrayType([23.52, 1.89, 89.3], StringType), None, Id(eu)), VarDecl(Id(ZCd), ArrayType([37.87, 93.05, 5.14], StringType), None, NumLit(63.17))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115946))

	def test_21530115947(self):
		input = '''
func cVy (number QWc4, string BDK[74.11,22.56,14.23], string yP)
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(cVy), [VarDecl(Id(QWc4), NumberType, None, None), VarDecl(Id(BDK), ArrayType([74.11, 22.56, 14.23], StringType), None, None), VarDecl(Id(yP), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115947))

	def test_21530115948(self):
		input = '''
number znB[27.0] <- 53.64
func UxF (number ZyR[60.59])
	return false
bool CH0n[45.68,90.46,12.95]
'''
		expect = '''Program([VarDecl(Id(znB), ArrayType([27.0], NumberType), None, NumLit(53.64)), FuncDecl(Id(UxF), [VarDecl(Id(ZyR), ArrayType([60.59], NumberType), None, None)], Return(BooleanLit(False))), VarDecl(Id(CH0n), ArrayType([45.68, 90.46, 12.95], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115948))

	def test_21530115949(self):
		input = '''
func xoc ()
	begin
	end

func leIN ()	begin
	end
func kt (string W21[98.24])
	begin
		RjD()
		bool yR7[92.65,45.96,60.51] <- mL
		J9zI("VYGQ")
	end
'''
		expect = '''Program([FuncDecl(Id(xoc), [], Block([])), FuncDecl(Id(leIN), [], Block([])), FuncDecl(Id(kt), [VarDecl(Id(W21), ArrayType([98.24], StringType), None, None)], Block([CallStmt(Id(RjD), []), VarDecl(Id(yR7), ArrayType([92.65, 45.96, 60.51], BoolType), None, Id(mL)), CallStmt(Id(J9zI), [StringLit(VYGQ)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115949))

	def test_21530115950(self):
		input = '''
func kz9Z (bool QiC, string FRq)	begin
	end

var jj <- JI
'''
		expect = '''Program([FuncDecl(Id(kz9Z), [VarDecl(Id(QiC), BoolType, None, None), VarDecl(Id(FRq), StringType, None, None)], Block([])), VarDecl(Id(jj), None, var, Id(JI))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115950))

	def test_21530115951(self):
		input = '''
func oW (string XVQ[92.87], string GW)
	return

func mN2l (bool efQ[61.5])
	begin
		break
	end
bool TnFE
'''
		expect = '''Program([FuncDecl(Id(oW), [VarDecl(Id(XVQ), ArrayType([92.87], StringType), None, None), VarDecl(Id(GW), StringType, None, None)], Return()), FuncDecl(Id(mN2l), [VarDecl(Id(efQ), ArrayType([61.5], BoolType), None, None)], Block([Break])), VarDecl(Id(TnFE), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115951))

	def test_21530115952(self):
		input = '''
number OW9
func Cql (string pUII[94.81,98.08,77.22])
	return nYfH
func MC (number Eo[56.91,88.85], bool ooMG)
	begin
	end
'''
		expect = '''Program([VarDecl(Id(OW9), NumberType, None, None), FuncDecl(Id(Cql), [VarDecl(Id(pUII), ArrayType([94.81, 98.08, 77.22], StringType), None, None)], Return(Id(nYfH))), FuncDecl(Id(MC), [VarDecl(Id(Eo), ArrayType([56.91, 88.85], NumberType), None, None), VarDecl(Id(ooMG), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115952))

	def test_21530115953(self):
		input = '''
func PPx (bool WZT, number KoNE, number Gn2Z[56.06])	begin
		break
		continue
		break
	end
'''
		expect = '''Program([FuncDecl(Id(PPx), [VarDecl(Id(WZT), BoolType, None, None), VarDecl(Id(KoNE), NumberType, None, None), VarDecl(Id(Gn2Z), ArrayType([56.06], NumberType), None, None)], Block([Break, Continue, Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115953))

	def test_21530115954(self):
		input = '''
string uJ_ <- xF6
func iVP (bool Vx, number yasC[87.7,13.09], bool JIV_)	return 50.27
bool oV <- "G"
bool yb[95.34,98.85] <- true
'''
		expect = '''Program([VarDecl(Id(uJ_), StringType, None, Id(xF6)), FuncDecl(Id(iVP), [VarDecl(Id(Vx), BoolType, None, None), VarDecl(Id(yasC), ArrayType([87.7, 13.09], NumberType), None, None), VarDecl(Id(JIV_), BoolType, None, None)], Return(NumLit(50.27))), VarDecl(Id(oV), BoolType, None, StringLit(G)), VarDecl(Id(yb), ArrayType([95.34, 98.85], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115954))

	def test_21530115955(self):
		input = '''
bool W4E[16.02]
func v3bH (string zxKw, string SIyN[59.99,88.6], number GgWa[37.14,83.5,42.43])
	return

func iE ()	return
func z2N ()	return
func b2 (bool eP[45.12,25.51,91.35], number IdEV[54.15,38.29,97.06])
	return

'''
		expect = '''Program([VarDecl(Id(W4E), ArrayType([16.02], BoolType), None, None), FuncDecl(Id(v3bH), [VarDecl(Id(zxKw), StringType, None, None), VarDecl(Id(SIyN), ArrayType([59.99, 88.6], StringType), None, None), VarDecl(Id(GgWa), ArrayType([37.14, 83.5, 42.43], NumberType), None, None)], Return()), FuncDecl(Id(iE), [], Return()), FuncDecl(Id(z2N), [], Return()), FuncDecl(Id(b2), [VarDecl(Id(eP), ArrayType([45.12, 25.51, 91.35], BoolType), None, None), VarDecl(Id(IdEV), ArrayType([54.15, 38.29, 97.06], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115955))

	def test_21530115956(self):
		input = '''
func HeM (bool jFS[62.85,49.32,79.54], number OsK[42.43])
	return Wh
'''
		expect = '''Program([FuncDecl(Id(HeM), [VarDecl(Id(jFS), ArrayType([62.85, 49.32, 79.54], BoolType), None, None), VarDecl(Id(OsK), ArrayType([42.43], NumberType), None, None)], Return(Id(Wh)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115956))

	def test_21530115957(self):
		input = '''
var Be <- false
'''
		expect = '''Program([VarDecl(Id(Be), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115957))

	def test_21530115958(self):
		input = '''
var xqr <- false
number rm[21.67,65.16]
'''
		expect = '''Program([VarDecl(Id(xqr), None, var, BooleanLit(False)), VarDecl(Id(rm), ArrayType([21.67, 65.16], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115958))

	def test_21530115959(self):
		input = '''
bool MbTp
string tXI7 <- ii
'''
		expect = '''Program([VarDecl(Id(MbTp), BoolType, None, None), VarDecl(Id(tXI7), StringType, None, Id(ii))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115959))

	def test_21530115960(self):
		input = '''
string Sr <- true
func SBn (string cZC[44.54,12.1], number dPo[90.82], number emZL[8.64,81.32,0.37])	return
func oe (bool ZGA[49.99])	return
number FfXf[34.01,35.37,30.98]
string aeK[4.65,84.89]
'''
		expect = '''Program([VarDecl(Id(Sr), StringType, None, BooleanLit(True)), FuncDecl(Id(SBn), [VarDecl(Id(cZC), ArrayType([44.54, 12.1], StringType), None, None), VarDecl(Id(dPo), ArrayType([90.82], NumberType), None, None), VarDecl(Id(emZL), ArrayType([8.64, 81.32, 0.37], NumberType), None, None)], Return()), FuncDecl(Id(oe), [VarDecl(Id(ZGA), ArrayType([49.99], BoolType), None, None)], Return()), VarDecl(Id(FfXf), ArrayType([34.01, 35.37, 30.98], NumberType), None, None), VarDecl(Id(aeK), ArrayType([4.65, 84.89], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115960))

	def test_21530115961(self):
		input = '''
bool vC[54.62,25.84]
func kMVv (string WrZZ, number r2)
	begin
		begin
			lX <- is9s
			if (60.44)
			continue
			elif (16.85)
			number Lxa[8.36,62.6,66.62]
			else bool kWCu
			continue
		end
	end
func SD ()
	begin
	end

func VI (bool w5bE)	return

'''
		expect = '''Program([VarDecl(Id(vC), ArrayType([54.62, 25.84], BoolType), None, None), FuncDecl(Id(kMVv), [VarDecl(Id(WrZZ), StringType, None, None), VarDecl(Id(r2), NumberType, None, None)], Block([Block([AssignStmt(Id(lX), Id(is9s)), If(NumLit(60.44), Continue), [(NumLit(16.85), VarDecl(Id(Lxa), ArrayType([8.36, 62.6, 66.62], NumberType), None, None))], VarDecl(Id(kWCu), BoolType, None, None), Continue])])), FuncDecl(Id(SD), [], Block([])), FuncDecl(Id(VI), [VarDecl(Id(w5bE), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115961))

	def test_21530115962(self):
		input = '''
func bc (bool q1, number PYY[49.56], bool CNWU[36.2,1.25,33.32])
	return "moWn"

bool pdg[22.86,21.84,33.06]
func d8M (bool Dl, bool IwT, bool ic)	return 88.16

func jdT (number IwgJ, string Kk[41.06,47.58,23.76], string u9j[6.02])	begin
	end

bool KNQ
'''
		expect = '''Program([FuncDecl(Id(bc), [VarDecl(Id(q1), BoolType, None, None), VarDecl(Id(PYY), ArrayType([49.56], NumberType), None, None), VarDecl(Id(CNWU), ArrayType([36.2, 1.25, 33.32], BoolType), None, None)], Return(StringLit(moWn))), VarDecl(Id(pdg), ArrayType([22.86, 21.84, 33.06], BoolType), None, None), FuncDecl(Id(d8M), [VarDecl(Id(Dl), BoolType, None, None), VarDecl(Id(IwT), BoolType, None, None), VarDecl(Id(ic), BoolType, None, None)], Return(NumLit(88.16))), FuncDecl(Id(jdT), [VarDecl(Id(IwgJ), NumberType, None, None), VarDecl(Id(Kk), ArrayType([41.06, 47.58, 23.76], StringType), None, None), VarDecl(Id(u9j), ArrayType([6.02], StringType), None, None)], Block([])), VarDecl(Id(KNQ), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115962))

	def test_21530115963(self):
		input = '''
string UM[88.65,31.87] <- "GTNDB"
'''
		expect = '''Program([VarDecl(Id(UM), ArrayType([88.65, 31.87], StringType), None, StringLit(GTNDB))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115963))

	def test_21530115964(self):
		input = '''
var G5ko <- "jrYB"
func ZG30 (string VBuc[54.47])
	return "u"

'''
		expect = '''Program([VarDecl(Id(G5ko), None, var, StringLit(jrYB)), FuncDecl(Id(ZG30), [VarDecl(Id(VBuc), ArrayType([54.47], StringType), None, None)], Return(StringLit(u)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115964))

	def test_21530115965(self):
		input = '''
func mN (number eDWz[7.16,69.07,0.87])
	begin
		begin
			if (98.17)
			FoE()
			elif (fxgg) continue
			elif (55.33)
			number mJ[68.69,48.84]
			elif (25.86) return "Mcuee"
			else string tK59[43.03,45.21,84.16]
			bool Kg[70.35,14.19,18.47]
			bool VS[58.33]
		end
		continue
	end

func Hv1L (string ERSL[30.17,71.29,69.14])	return NmF

func z81 (bool xSQ, string AH, bool q3)
	return 97.91
'''
		expect = '''Program([FuncDecl(Id(mN), [VarDecl(Id(eDWz), ArrayType([7.16, 69.07, 0.87], NumberType), None, None)], Block([Block([If(NumLit(98.17), CallStmt(Id(FoE), [])), [(Id(fxgg), Continue), (NumLit(55.33), VarDecl(Id(mJ), ArrayType([68.69, 48.84], NumberType), None, None)), (NumLit(25.86), Return(StringLit(Mcuee)))], VarDecl(Id(tK59), ArrayType([43.03, 45.21, 84.16], StringType), None, None), VarDecl(Id(Kg), ArrayType([70.35, 14.19, 18.47], BoolType), None, None), VarDecl(Id(VS), ArrayType([58.33], BoolType), None, None)]), Continue])), FuncDecl(Id(Hv1L), [VarDecl(Id(ERSL), ArrayType([30.17, 71.29, 69.14], StringType), None, None)], Return(Id(NmF))), FuncDecl(Id(z81), [VarDecl(Id(xSQ), BoolType, None, None), VarDecl(Id(AH), StringType, None, None), VarDecl(Id(q3), BoolType, None, None)], Return(NumLit(97.91)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115965))

	def test_21530115966(self):
		input = '''
func uBM (number Itmw, number bjq, number bT)
	return true
func LHz (string UoUK[50.3,68.4])	return
func wR86 ()	begin
		if (58.37)
		continue
		elif (wpS)
		begin
			bool BK[13.14] <- "ff"
			UE(ft)
			break
		end
		elif (Yn)
		ES(ODX2, "fbize")
		else break
		R93v[ZAs, true, ouR] <- false
		number NK
	end
bool ly
'''
		expect = '''Program([FuncDecl(Id(uBM), [VarDecl(Id(Itmw), NumberType, None, None), VarDecl(Id(bjq), NumberType, None, None), VarDecl(Id(bT), NumberType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(LHz), [VarDecl(Id(UoUK), ArrayType([50.3, 68.4], StringType), None, None)], Return()), FuncDecl(Id(wR86), [], Block([If(NumLit(58.37), Continue), [(Id(wpS), Block([VarDecl(Id(BK), ArrayType([13.14], BoolType), None, StringLit(ff)), CallStmt(Id(UE), [Id(ft)]), Break])), (Id(Yn), CallStmt(Id(ES), [Id(ODX2), StringLit(fbize)]))], Break, AssignStmt(ArrayCell(Id(R93v), [Id(ZAs), BooleanLit(True), Id(ouR)]), BooleanLit(False)), VarDecl(Id(NK), NumberType, None, None)])), VarDecl(Id(ly), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115966))

	def test_21530115967(self):
		input = '''
func TxO ()
	return 5.39
string r_[37.7]
bool nyD4[78.76,99.55]
func Gz (number ZR4, string qrng, string ITq)
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(TxO), [], Return(NumLit(5.39))), VarDecl(Id(r_), ArrayType([37.7], StringType), None, None), VarDecl(Id(nyD4), ArrayType([78.76, 99.55], BoolType), None, None), FuncDecl(Id(Gz), [VarDecl(Id(ZR4), NumberType, None, None), VarDecl(Id(qrng), StringType, None, None), VarDecl(Id(ITq), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115967))

	def test_21530115968(self):
		input = '''
bool gkcb[50.84] <- false
'''
		expect = '''Program([VarDecl(Id(gkcb), ArrayType([50.84], BoolType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115968))

	def test_21530115969(self):
		input = '''
func yVde (string ag3C)	return

'''
		expect = '''Program([FuncDecl(Id(yVde), [VarDecl(Id(ag3C), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115969))

	def test_21530115970(self):
		input = '''
func g_Q ()
	return 63.64
bool gpIs[57.76,33.71,93.0] <- 63.25
string F5 <- true
number jadL <- 76.57
'''
		expect = '''Program([FuncDecl(Id(g_Q), [], Return(NumLit(63.64))), VarDecl(Id(gpIs), ArrayType([57.76, 33.71, 93.0], BoolType), None, NumLit(63.25)), VarDecl(Id(F5), StringType, None, BooleanLit(True)), VarDecl(Id(jadL), NumberType, None, NumLit(76.57))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115970))

	def test_21530115971(self):
		input = '''
number wVda
string rh1 <- 97.37
func puMV (bool iy2j[66.42])	begin
		if (ntW) if (81.48) for SP until XI5 by ZyM
			return 38.18
		elif ("uGK")
		continue
		elif (true)
		continue
		elif (YDt)
		begin
			return
			begin
			end
		end
		for YTPS until false by "vsTD"
			if (97.58)
			if (zxw) for aNo9 until false by "wsl"
				number Y2zR <- obDg
			elif (Sf) if (36.95) HJ(14.9, true, 44.71)
			elif (37.28) for hZFa until EOgw by jes
				kuV2(false, "N", j0)
			else for J5h until 49.38 by true
				break
			elif ("gnR")
			Erv[true, scjq] <- KDLA
	end
string lOjJ <- "jsci"
'''
		expect = '''Program([VarDecl(Id(wVda), NumberType, None, None), VarDecl(Id(rh1), StringType, None, NumLit(97.37)), FuncDecl(Id(puMV), [VarDecl(Id(iy2j), ArrayType([66.42], BoolType), None, None)], Block([If(Id(ntW), If(NumLit(81.48), For(Id(SP), Id(XI5), Id(ZyM), Return(NumLit(38.18)))), [(StringLit(uGK), Continue), (BooleanLit(True), Continue), (Id(YDt), Block([Return(), Block([])]))], None), [], None, For(Id(YTPS), BooleanLit(False), StringLit(vsTD), If(NumLit(97.58), If(Id(zxw), For(Id(aNo9), BooleanLit(False), StringLit(wsl), VarDecl(Id(Y2zR), NumberType, None, Id(obDg)))), [(Id(Sf), If(NumLit(36.95), CallStmt(Id(HJ), [NumLit(14.9), BooleanLit(True), NumLit(44.71)])), [(NumLit(37.28), For(Id(hZFa), Id(EOgw), Id(jes), CallStmt(Id(kuV2), [BooleanLit(False), StringLit(N), Id(j0)])))], For(Id(J5h), NumLit(49.38), BooleanLit(True), Break)), (StringLit(gnR), AssignStmt(ArrayCell(Id(Erv), [BooleanLit(True), Id(scjq)]), Id(KDLA)))], None), [], None)])), VarDecl(Id(lOjJ), StringType, None, StringLit(jsci))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115971))

	def test_21530115972(self):
		input = '''
func SQSS (number uO, string xJ, string u4[64.62,53.19])	return "w"

bool jJL[75.03,28.99,92.95]
dynamic bRAt <- PK
func Qbs0 ()
	return "GMw"

func dZS (bool Rlj)	begin
	end
'''
		expect = '''Program([FuncDecl(Id(SQSS), [VarDecl(Id(uO), NumberType, None, None), VarDecl(Id(xJ), StringType, None, None), VarDecl(Id(u4), ArrayType([64.62, 53.19], StringType), None, None)], Return(StringLit(w))), VarDecl(Id(jJL), ArrayType([75.03, 28.99, 92.95], BoolType), None, None), VarDecl(Id(bRAt), None, dynamic, Id(PK)), FuncDecl(Id(Qbs0), [], Return(StringLit(GMw))), FuncDecl(Id(dZS), [VarDecl(Id(Rlj), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115972))

	def test_21530115973(self):
		input = '''
number Szw0
func c1 (bool V_, bool i5C[15.65], bool DHlh)	return

func Xn (string l9i[53.74,33.2], bool Bi5, bool HVy[43.62])
	return VM
'''
		expect = '''Program([VarDecl(Id(Szw0), NumberType, None, None), FuncDecl(Id(c1), [VarDecl(Id(V_), BoolType, None, None), VarDecl(Id(i5C), ArrayType([15.65], BoolType), None, None), VarDecl(Id(DHlh), BoolType, None, None)], Return()), FuncDecl(Id(Xn), [VarDecl(Id(l9i), ArrayType([53.74, 33.2], StringType), None, None), VarDecl(Id(Bi5), BoolType, None, None), VarDecl(Id(HVy), ArrayType([43.62], BoolType), None, None)], Return(Id(VM)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115973))

	def test_21530115974(self):
		input = '''
number KV[18.27,33.81,47.74] <- false
func Sl76 (number nswJ, string l0OB, number JI)
	return
func mlR (bool AwV7, number aKNw)	return

number MI[33.02] <- false
'''
		expect = '''Program([VarDecl(Id(KV), ArrayType([18.27, 33.81, 47.74], NumberType), None, BooleanLit(False)), FuncDecl(Id(Sl76), [VarDecl(Id(nswJ), NumberType, None, None), VarDecl(Id(l0OB), StringType, None, None), VarDecl(Id(JI), NumberType, None, None)], Return()), FuncDecl(Id(mlR), [VarDecl(Id(AwV7), BoolType, None, None), VarDecl(Id(aKNw), NumberType, None, None)], Return()), VarDecl(Id(MI), ArrayType([33.02], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115974))

	def test_21530115975(self):
		input = '''
func erNZ (bool P94)	return

'''
		expect = '''Program([FuncDecl(Id(erNZ), [VarDecl(Id(P94), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115975))

	def test_21530115976(self):
		input = '''
number LV[10.26,71.22] <- 86.7
func hA3t (bool Qy, string Z6lb)
	return

func XNTe (number pV1[82.41,75.84])	return JkXQ
'''
		expect = '''Program([VarDecl(Id(LV), ArrayType([10.26, 71.22], NumberType), None, NumLit(86.7)), FuncDecl(Id(hA3t), [VarDecl(Id(Qy), BoolType, None, None), VarDecl(Id(Z6lb), StringType, None, None)], Return()), FuncDecl(Id(XNTe), [VarDecl(Id(pV1), ArrayType([82.41, 75.84], NumberType), None, None)], Return(Id(JkXQ)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115976))

	def test_21530115977(self):
		input = '''
number CEGj[65.66,58.84,6.58]
number RuEg
func LBw ()
	return "IQl"
'''
		expect = '''Program([VarDecl(Id(CEGj), ArrayType([65.66, 58.84, 6.58], NumberType), None, None), VarDecl(Id(RuEg), NumberType, None, None), FuncDecl(Id(LBw), [], Return(StringLit(IQl)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115977))

	def test_21530115978(self):
		input = '''
string KJo1
bool C7Uw <- ThH
func pak ()	begin
		if (hw) continue
		elif (53.44) return
		elif (false)
		sO()
		elif (23.99) continue
		if (TL)
		begin
			break
			for j59q until false by 9.18
				for FeC until QHQ by true
					return "hig"
			oO <- 15.87
		end
		elif ("Zv") break
		elif (UJ) for J0f until false by 82.82
			return false
		elif (70.25)
		continue
		elif (14.66)
		Mgf()
	end
func Gp (bool DoAw, bool EieS[63.83,78.04])
	return

bool x4Ft <- true
'''
		expect = '''Program([VarDecl(Id(KJo1), StringType, None, None), VarDecl(Id(C7Uw), BoolType, None, Id(ThH)), FuncDecl(Id(pak), [], Block([If(Id(hw), Continue), [(NumLit(53.44), Return()), (BooleanLit(False), CallStmt(Id(sO), [])), (NumLit(23.99), Continue)], None, If(Id(TL), Block([Break, For(Id(j59q), BooleanLit(False), NumLit(9.18), For(Id(FeC), Id(QHQ), BooleanLit(True), Return(StringLit(hig)))), AssignStmt(Id(oO), NumLit(15.87))])), [(StringLit(Zv), Break), (Id(UJ), For(Id(J0f), BooleanLit(False), NumLit(82.82), Return(BooleanLit(False)))), (NumLit(70.25), Continue), (NumLit(14.66), CallStmt(Id(Mgf), []))], None])), FuncDecl(Id(Gp), [VarDecl(Id(DoAw), BoolType, None, None), VarDecl(Id(EieS), ArrayType([63.83, 78.04], BoolType), None, None)], Return()), VarDecl(Id(x4Ft), BoolType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115978))

	def test_21530115979(self):
		input = '''
func Py (string kY, string DK, bool cyVT[23.87,33.86,57.55])
	return 58.07
func kX (bool ZO[33.71,51.41,47.43])
	return "rvyl"
bool G8[33.1] <- "K"
'''
		expect = '''Program([FuncDecl(Id(Py), [VarDecl(Id(kY), StringType, None, None), VarDecl(Id(DK), StringType, None, None), VarDecl(Id(cyVT), ArrayType([23.87, 33.86, 57.55], BoolType), None, None)], Return(NumLit(58.07))), FuncDecl(Id(kX), [VarDecl(Id(ZO), ArrayType([33.71, 51.41, 47.43], BoolType), None, None)], Return(StringLit(rvyl))), VarDecl(Id(G8), ArrayType([33.1], BoolType), None, StringLit(K))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115979))

	def test_21530115980(self):
		input = '''
func IkRN (number pVH)	return

string L4[42.42,45.62]
dynamic WI7D
string Bq <- true
'''
		expect = '''Program([FuncDecl(Id(IkRN), [VarDecl(Id(pVH), NumberType, None, None)], Return()), VarDecl(Id(L4), ArrayType([42.42, 45.62], StringType), None, None), VarDecl(Id(WI7D), None, dynamic, None), VarDecl(Id(Bq), StringType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115980))

	def test_21530115981(self):
		input = '''
var sZ6 <- true
'''
		expect = '''Program([VarDecl(Id(sZ6), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115981))

	def test_21530115982(self):
		input = '''
bool OiON[13.22,46.26,26.38] <- true
string UT[55.02,52.08,81.53] <- 50.1
'''
		expect = '''Program([VarDecl(Id(OiON), ArrayType([13.22, 46.26, 26.38], BoolType), None, BooleanLit(True)), VarDecl(Id(UT), ArrayType([55.02, 52.08, 81.53], StringType), None, NumLit(50.1))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115982))

	def test_21530115983(self):
		input = '''
number Dm8[40.16,24.24] <- "uRD"
func gYjy (bool Y4[93.16,71.23,69.11])
	begin
		if (73.76)
		begin
			Pl82["u", false] <- "Xm"
		end
		elif (true) if (true)
		break
		elif (15.64) bool nhT9[90.18]
		elif (false)
		continue
		elif (10.57)
		return n_U
		elif (true)
		begin
			for W2z until 79.44 by 0.84
				for XU until yX by "uBxb"
					return
			j_G(false, true)
			return ds
		end
		else if (MS)
		return
		elif (aWxU)
		for Ias until 38.74 by 52.6
			if (AuRp) return 34.64
			elif (17.9) f9 <- eJV0
			elif (48.34)
			if ("KZfXX")
			string Wm
			elif ("m") PN <- "ar"
			elif (AW)
			number nP6
			elif (fS) bW <- G9kp
			elif ("Is")
			begin
			end
			else return
			else break
		elif (34.65) break
		else continue
		elif ("Urhwe")
		for XWA4 until 24.13 by Ojla
			if (Gp) u0p <- true
			elif (vIEP) lY6N("jNtQl", 76.73)
			elif ("st")
			for Yh until "B" by "Gr"
				begin
					break
					Aj("t", GFK, Tok)
				end
			elif (Nes) if (false) break
			elif ("OcCW") break
			elif (22.03)
			begin
				continue
				for gq until true by 53.72
					begin
						Ipj[gb, true] <- false
						return
					end
			end
			else if (false)
			for z7 until true by 49.68
				Et("I")
			elif (9.4)
			smw1(false, "XfUcW", lty)
			elif (nv9) Ceh(70.66, y50p, T0)
			elif (YOU) break
			elif (true) begin
				return
			end
		elif (6.4)
		qmp(47.75, true)
		m7Xo(G8, false)
		begin
			break
			KRh <- RRE
			f92(Lx2r, R2)
		end
	end

'''
		expect = '''Program([VarDecl(Id(Dm8), ArrayType([40.16, 24.24], NumberType), None, StringLit(uRD)), FuncDecl(Id(gYjy), [VarDecl(Id(Y4), ArrayType([93.16, 71.23, 69.11], BoolType), None, None)], Block([If(NumLit(73.76), Block([AssignStmt(ArrayCell(Id(Pl82), [StringLit(u), BooleanLit(False)]), StringLit(Xm))])), [(BooleanLit(True), If(BooleanLit(True), Break), [(NumLit(15.64), VarDecl(Id(nhT9), ArrayType([90.18], BoolType), None, None)), (BooleanLit(False), Continue), (NumLit(10.57), Return(Id(n_U))), (BooleanLit(True), Block([For(Id(W2z), NumLit(79.44), NumLit(0.84), For(Id(XU), Id(yX), StringLit(uBxb), Return())), CallStmt(Id(j_G), [BooleanLit(False), BooleanLit(True)]), Return(Id(ds))]))], If(Id(MS), Return()), [(Id(aWxU), For(Id(Ias), NumLit(38.74), NumLit(52.6), If(Id(AuRp), Return(NumLit(34.64))), [(NumLit(17.9), AssignStmt(Id(f9), Id(eJV0))), (NumLit(48.34), If(StringLit(KZfXX), VarDecl(Id(Wm), StringType, None, None)), [(StringLit(m), AssignStmt(Id(PN), StringLit(ar))), (Id(AW), VarDecl(Id(nP6), NumberType, None, None)), (Id(fS), AssignStmt(Id(bW), Id(G9kp))), (StringLit(Is), Block([]))], Return())], Break)), (NumLit(34.65), Break)], Continue), (StringLit(Urhwe), For(Id(XWA4), NumLit(24.13), Id(Ojla), If(Id(Gp), AssignStmt(Id(u0p), BooleanLit(True))), [(Id(vIEP), CallStmt(Id(lY6N), [StringLit(jNtQl), NumLit(76.73)])), (StringLit(st), For(Id(Yh), StringLit(B), StringLit(Gr), Block([Break, CallStmt(Id(Aj), [StringLit(t), Id(GFK), Id(Tok)])]))), (Id(Nes), If(BooleanLit(False), Break), [(StringLit(OcCW), Break), (NumLit(22.03), Block([Continue, For(Id(gq), BooleanLit(True), NumLit(53.72), Block([AssignStmt(ArrayCell(Id(Ipj), [Id(gb), BooleanLit(True)]), BooleanLit(False)), Return()]))]))], If(BooleanLit(False), For(Id(z7), BooleanLit(True), NumLit(49.68), CallStmt(Id(Et), [StringLit(I)]))), [(NumLit(9.4), CallStmt(Id(smw1), [BooleanLit(False), StringLit(XfUcW), Id(lty)])), (Id(nv9), CallStmt(Id(Ceh), [NumLit(70.66), Id(y50p), Id(T0)])), (Id(YOU), Break)], None), (BooleanLit(True), Block([Return()]))], None)), (NumLit(6.4), CallStmt(Id(qmp), [NumLit(47.75), BooleanLit(True)]))], None, CallStmt(Id(m7Xo), [Id(G8), BooleanLit(False)]), Block([Break, AssignStmt(Id(KRh), Id(RRE)), CallStmt(Id(f92), [Id(Lx2r), Id(R2)])])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115983))

	def test_21530115984(self):
		input = '''
bool Lr[62.2,25.8]
func g9q ()
	return
dynamic FbRJ <- false
func gW ()	return

func RyXh (number nT, number tiOO, string v7fv[6.67,49.43,5.5])
	begin
		begin
			break
			continue
		end
	end

'''
		expect = '''Program([VarDecl(Id(Lr), ArrayType([62.2, 25.8], BoolType), None, None), FuncDecl(Id(g9q), [], Return()), VarDecl(Id(FbRJ), None, dynamic, BooleanLit(False)), FuncDecl(Id(gW), [], Return()), FuncDecl(Id(RyXh), [VarDecl(Id(nT), NumberType, None, None), VarDecl(Id(tiOO), NumberType, None, None), VarDecl(Id(v7fv), ArrayType([6.67, 49.43, 5.5], StringType), None, None)], Block([Block([Break, Continue])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115984))

	def test_21530115985(self):
		input = '''
string p0_X[2.52,29.53,28.3]
func Rs (number plRj, number rO)
	return
'''
		expect = '''Program([VarDecl(Id(p0_X), ArrayType([2.52, 29.53, 28.3], StringType), None, None), FuncDecl(Id(Rs), [VarDecl(Id(plRj), NumberType, None, None), VarDecl(Id(rO), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115985))

	def test_21530115986(self):
		input = '''
func cref ()	return
func TE (string Ht[73.44,68.74], bool gM_[53.2,84.55])
	return k5F
'''
		expect = '''Program([FuncDecl(Id(cref), [], Return()), FuncDecl(Id(TE), [VarDecl(Id(Ht), ArrayType([73.44, 68.74], StringType), None, None), VarDecl(Id(gM_), ArrayType([53.2, 84.55], BoolType), None, None)], Return(Id(k5F)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115986))

	def test_21530115987(self):
		input = '''
bool D6
number i53[63.12,81.16]
var Ns <- 34.2
'''
		expect = '''Program([VarDecl(Id(D6), BoolType, None, None), VarDecl(Id(i53), ArrayType([63.12, 81.16], NumberType), None, None), VarDecl(Id(Ns), None, var, NumLit(34.2))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115987))

	def test_21530115988(self):
		input = '''
func DS (string FjFq[61.18,16.73,55.99], string Xcq)	return
func Jd ()	return "QX"
func zMAL ()	begin
		oI3 <- false
		break
	end

'''
		expect = '''Program([FuncDecl(Id(DS), [VarDecl(Id(FjFq), ArrayType([61.18, 16.73, 55.99], StringType), None, None), VarDecl(Id(Xcq), StringType, None, None)], Return()), FuncDecl(Id(Jd), [], Return(StringLit(QX))), FuncDecl(Id(zMAL), [], Block([AssignStmt(Id(oI3), BooleanLit(False)), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115988))

	def test_21530115989(self):
		input = '''
number gW[81.0,45.11,63.97] <- false
dynamic qJ <- 96.42
'''
		expect = '''Program([VarDecl(Id(gW), ArrayType([81.0, 45.11, 63.97], NumberType), None, BooleanLit(False)), VarDecl(Id(qJ), None, dynamic, NumLit(96.42))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115989))

	def test_21530115990(self):
		input = '''
string C1f[75.02,76.61,80.9]
'''
		expect = '''Program([VarDecl(Id(C1f), ArrayType([75.02, 76.61, 80.9], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115990))

	def test_21530115991(self):
		input = '''
func Ge4 ()
	begin
		break
		break
	end

func hmf (number GHIW)	begin
		begin
			break
			return
			vy[84.38] <- 4.6
		end
		break
	end
func knO ()
	return
'''
		expect = '''Program([FuncDecl(Id(Ge4), [], Block([Break, Break])), FuncDecl(Id(hmf), [VarDecl(Id(GHIW), NumberType, None, None)], Block([Block([Break, Return(), AssignStmt(ArrayCell(Id(vy), [NumLit(84.38)]), NumLit(4.6))]), Break])), FuncDecl(Id(knO), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115991))

	def test_21530115992(self):
		input = '''
dynamic ySaM
func cX4 (bool yS, string TUq7, bool zC7Y[38.85,98.58])
	return

'''
		expect = '''Program([VarDecl(Id(ySaM), None, dynamic, None), FuncDecl(Id(cX4), [VarDecl(Id(yS), BoolType, None, None), VarDecl(Id(TUq7), StringType, None, None), VarDecl(Id(zC7Y), ArrayType([38.85, 98.58], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115992))

	def test_21530115993(self):
		input = '''
number CF
func Z5Xu (bool uI, string qc5[28.81], bool Vg)
	return true

number mw[78.07,20.04] <- "dMD"
'''
		expect = '''Program([VarDecl(Id(CF), NumberType, None, None), FuncDecl(Id(Z5Xu), [VarDecl(Id(uI), BoolType, None, None), VarDecl(Id(qc5), ArrayType([28.81], StringType), None, None), VarDecl(Id(Vg), BoolType, None, None)], Return(BooleanLit(True))), VarDecl(Id(mw), ArrayType([78.07, 20.04], NumberType), None, StringLit(dMD))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115993))

	def test_21530115994(self):
		input = '''
var AZ3n <- "M"
bool KgT[53.77,29.3]
bool LHKZ
func oh63 ()	return

func mM (number AB, number Cyr)	return HQ
'''
		expect = '''Program([VarDecl(Id(AZ3n), None, var, StringLit(M)), VarDecl(Id(KgT), ArrayType([53.77, 29.3], BoolType), None, None), VarDecl(Id(LHKZ), BoolType, None, None), FuncDecl(Id(oh63), [], Return()), FuncDecl(Id(mM), [VarDecl(Id(AB), NumberType, None, None), VarDecl(Id(Cyr), NumberType, None, None)], Return(Id(HQ)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115994))

	def test_21530115995(self):
		input = '''
func OE (bool ouu7, string ePem[9.15], string MGdJ[53.28,1.23])
	return

func oUF (number eV[73.57,37.62,28.03], number G9W)	return
func fOX (string aX42[26.76,93.14], number F2qI[41.26,73.6], number WO)	return

func ej (bool hEg[5.47], number sKl)
	begin
		YZ()
		break
	end
func vxq ()	return
'''
		expect = '''Program([FuncDecl(Id(OE), [VarDecl(Id(ouu7), BoolType, None, None), VarDecl(Id(ePem), ArrayType([9.15], StringType), None, None), VarDecl(Id(MGdJ), ArrayType([53.28, 1.23], StringType), None, None)], Return()), FuncDecl(Id(oUF), [VarDecl(Id(eV), ArrayType([73.57, 37.62, 28.03], NumberType), None, None), VarDecl(Id(G9W), NumberType, None, None)], Return()), FuncDecl(Id(fOX), [VarDecl(Id(aX42), ArrayType([26.76, 93.14], StringType), None, None), VarDecl(Id(F2qI), ArrayType([41.26, 73.6], NumberType), None, None), VarDecl(Id(WO), NumberType, None, None)], Return()), FuncDecl(Id(ej), [VarDecl(Id(hEg), ArrayType([5.47], BoolType), None, None), VarDecl(Id(sKl), NumberType, None, None)], Block([CallStmt(Id(YZ), []), Break])), FuncDecl(Id(vxq), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115995))

	def test_21530115996(self):
		input = '''
string taf[87.2,17.8]
'''
		expect = '''Program([VarDecl(Id(taf), ArrayType([87.2, 17.8], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115996))

	def test_21530115997(self):
		input = '''
func HOj (number vKB, string nf)	begin
	end
func S_1 (number fz, number wd[32.57,96.98])
	return hZl
func QY (number W5Tx[1.99,67.03,69.78])
	begin
		break
		begin
			number sGaC[89.23]
			return
			ijkT[J2v, 66.42, "ioRja"] <- bKl
		end
	end
func r5 (bool d3A)
	return 29.34

number DNpw
'''
		expect = '''Program([FuncDecl(Id(HOj), [VarDecl(Id(vKB), NumberType, None, None), VarDecl(Id(nf), StringType, None, None)], Block([])), FuncDecl(Id(S_1), [VarDecl(Id(fz), NumberType, None, None), VarDecl(Id(wd), ArrayType([32.57, 96.98], NumberType), None, None)], Return(Id(hZl))), FuncDecl(Id(QY), [VarDecl(Id(W5Tx), ArrayType([1.99, 67.03, 69.78], NumberType), None, None)], Block([Break, Block([VarDecl(Id(sGaC), ArrayType([89.23], NumberType), None, None), Return(), AssignStmt(ArrayCell(Id(ijkT), [Id(J2v), NumLit(66.42), StringLit(ioRja)]), Id(bKl))])])), FuncDecl(Id(r5), [VarDecl(Id(d3A), BoolType, None, None)], Return(NumLit(29.34))), VarDecl(Id(DNpw), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115997))

	def test_21530115998(self):
		input = '''
string f6
number TUd8[66.92,38.45,34.14]
bool fpo[86.45,71.94]
func Xb7 (string d2, bool B2_h)	return
func GW (number ao[23.53,84.6,17.12], bool We, string Scm[50.57])	begin
	end

'''
		expect = '''Program([VarDecl(Id(f6), StringType, None, None), VarDecl(Id(TUd8), ArrayType([66.92, 38.45, 34.14], NumberType), None, None), VarDecl(Id(fpo), ArrayType([86.45, 71.94], BoolType), None, None), FuncDecl(Id(Xb7), [VarDecl(Id(d2), StringType, None, None), VarDecl(Id(B2_h), BoolType, None, None)], Return()), FuncDecl(Id(GW), [VarDecl(Id(ao), ArrayType([23.53, 84.6, 17.12], NumberType), None, None), VarDecl(Id(We), BoolType, None, None), VarDecl(Id(Scm), ArrayType([50.57], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115998))

	def test_21530115999(self):
		input = '''
func ttoB (bool OiY, bool V2p[41.38,40.88])	return true
func Isy (bool D1z[33.2,50.48,34.23])
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(ttoB), [VarDecl(Id(OiY), BoolType, None, None), VarDecl(Id(V2p), ArrayType([41.38, 40.88], BoolType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(Isy), [VarDecl(Id(D1z), ArrayType([33.2, 50.48, 34.23], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115999))
