import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
	def test_2153011500(self):
		input = '''
func D6Nm ()
	return [tRN[gy(false, 51.06, 35.16) >= "IABb", true, "YR"]]

'''
		expect = '''Program([FuncDecl(Id(D6Nm), [], Return(ArrayLit(ArrayCell(Id(tRN), [BinaryOp(>=, CallExpr(Id(gy), [BooleanLit(False), NumLit(51.06), NumLit(35.16)]), StringLit(IABb)), BooleanLit(True), StringLit(YR)]))))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011500))

	def test_2153011501(self):
		input = '''
func Cr (number QW, bool rL, number uC)	return j4Z

number SIk[87.57,43.1,98.85] <- 23.0
bool f7[94.42,94.24,25.75]
string aL <- 41.25
string PDwa[54.17,88.15,26.7] <- false
'''
		expect = '''Program([FuncDecl(Id(Cr), [VarDecl(Id(QW), NumberType, None, None), VarDecl(Id(rL), BoolType, None, None), VarDecl(Id(uC), NumberType, None, None)], Return(Id(j4Z))), VarDecl(Id(SIk), ArrayType([87.57, 43.1, 98.85], NumberType), None, NumLit(23.0)), VarDecl(Id(f7), ArrayType([94.42, 94.24, 25.75], BoolType), None, None), VarDecl(Id(aL), StringType, None, NumLit(41.25)), VarDecl(Id(PDwa), ArrayType([54.17, 88.15, 26.7], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011501))

	def test_2153011502(self):
		input = '''
string pqZf <- "KQ"
string D3h9
'''
		expect = '''Program([VarDecl(Id(pqZf), StringType, None, StringLit(KQ)), VarDecl(Id(D3h9), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011502))

	def test_2153011503(self):
		input = '''
func K_ (string FiBC, number KNC)	return
number NI[49.31] <- 24.86
func D3LE (bool i4[38.78], number xH7, bool k2O)
	return

'''
		expect = '''Program([FuncDecl(Id(K_), [VarDecl(Id(FiBC), StringType, None, None), VarDecl(Id(KNC), NumberType, None, None)], Return()), VarDecl(Id(NI), ArrayType([49.31], NumberType), None, NumLit(24.86)), FuncDecl(Id(D3LE), [VarDecl(Id(i4), ArrayType([38.78], BoolType), None, None), VarDecl(Id(xH7), NumberType, None, None), VarDecl(Id(k2O), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011503))

	def test_2153011504(self):
		input = '''
func r3i (string BwGq[47.6,94.03], number tK[82.35,89.73,10.03], bool oR)
	begin
		break
		for F9D until "Nd" by true
			continue
	end

'''
		expect = '''Program([FuncDecl(Id(r3i), [VarDecl(Id(BwGq), ArrayType([47.6, 94.03], StringType), None, None), VarDecl(Id(tK), ArrayType([82.35, 89.73, 10.03], NumberType), None, None), VarDecl(Id(oR), BoolType, None, None)], Block([Break, For(Id(F9D), StringLit(Nd), BooleanLit(True), Continue)]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011504))

	def test_2153011505(self):
		input = '''
string VE[27.29]
func F6 (number DSD[85.16,23.62], number MY27, number cD)	begin
		v6(59.28)
		return
	end

var YUL <- 69.09
func Ykt (bool mM4k[52.77,56.48])
	return "Hbt"
'''
		expect = '''Program([VarDecl(Id(VE), ArrayType([27.29], StringType), None, None), FuncDecl(Id(F6), [VarDecl(Id(DSD), ArrayType([85.16, 23.62], NumberType), None, None), VarDecl(Id(MY27), NumberType, None, None), VarDecl(Id(cD), NumberType, None, None)], Block([CallStmt(Id(v6), [NumLit(59.28)]), Return()])), VarDecl(Id(YUL), None, var, NumLit(69.09)), FuncDecl(Id(Ykt), [VarDecl(Id(mM4k), ArrayType([52.77, 56.48], BoolType), None, None)], Return(StringLit(Hbt)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011505))

	def test_2153011506(self):
		input = '''
bool b6R[34.12]
func OwZ (string ckm[95.37,62.04,33.3], bool P8)
	return

func vsg (bool Ob8L[97.42,41.29,48.86], string oM[78.68])
	begin
		MGS(true, false, false)
		bool fnF[73.19]
		if (62.32) var kd <- "ilZb"
		elif (XT)
		if (10.59)
		Tr(true, 12.14)
		elif (vw65)
		GKmb <- 57.45
		elif ("Ft")
		Oyv()
	end

var ee4 <- true
string uJvv <- true
'''
		expect = '''Program([VarDecl(Id(b6R), ArrayType([34.12], BoolType), None, None), FuncDecl(Id(OwZ), [VarDecl(Id(ckm), ArrayType([95.37, 62.04, 33.3], StringType), None, None), VarDecl(Id(P8), BoolType, None, None)], Return()), FuncDecl(Id(vsg), [VarDecl(Id(Ob8L), ArrayType([97.42, 41.29, 48.86], BoolType), None, None), VarDecl(Id(oM), ArrayType([78.68], StringType), None, None)], Block([CallStmt(Id(MGS), [BooleanLit(True), BooleanLit(False), BooleanLit(False)]), VarDecl(Id(fnF), ArrayType([73.19], BoolType), None, None), If(NumLit(62.32), VarDecl(Id(kd), None, var, StringLit(ilZb))), [(Id(XT), If(NumLit(10.59), CallStmt(Id(Tr), [BooleanLit(True), NumLit(12.14)])), [(Id(vw65), AssignStmt(Id(GKmb), NumLit(57.45)))], None), (StringLit(Ft), CallStmt(Id(Oyv), []))], None])), VarDecl(Id(ee4), None, var, BooleanLit(True)), VarDecl(Id(uJvv), StringType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011506))

	def test_2153011507(self):
		input = '''
string pX7L
func cLO_ ()
	begin
		break
		begin
			dB <- "UWcH"
		end
		for Xv3S until "xHP" by F_0
			if (qTp)
			bool ODJ_[31.33,71.69,62.89] <- 11.85
	end
var ykd <- SEq
'''
		expect = '''Program([VarDecl(Id(pX7L), StringType, None, None), FuncDecl(Id(cLO_), [], Block([Break, Block([AssignStmt(Id(dB), StringLit(UWcH))]), For(Id(Xv3S), StringLit(xHP), Id(F_0), If(Id(qTp), VarDecl(Id(ODJ_), ArrayType([31.33, 71.69, 62.89], BoolType), None, NumLit(11.85))), [], None)])), VarDecl(Id(ykd), None, var, Id(SEq))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011507))

	def test_2153011508(self):
		input = '''
func S6V (bool BJq, bool Ouyq[52.31,36.4,45.64])
	return "sNd"
func tj (bool PO[58.86,13.93], bool Vdl, string CoKg[56.88,25.93,63.35])
	begin
		bool EkmM[45.42,98.66] <- true
		string Ne
		begin
			CIj <- "ayS"
			for BN3 until 49.92 by 30.11
				oX("wH", false)
			break
		end
	end

func DY (bool Guq[16.53,83.97], string LE[30.81])
	return

func IsSj ()	begin
		for sdqf until "uQ" by rWK
			begin
				if (BEj)
				return "sLRLW"
				elif (aTKJ) hCq_ <- J1I
				elif (34.93)
				begin
					return 87.02
				end
				elif (true)
				if (true) bool G2 <- 15.67
				elif ("R") continue
				elif (true) UKF(41.78, true)
				elif ("wxkHD")
				return
				elif (false) for Bj9j until "ZLyqm" by false
					break
				elif (false) continue
				else xQ8I[false, NU0] <- YHm
				return
			end
	end
func wU (number i5)	return
'''
		expect = '''Program([FuncDecl(Id(S6V), [VarDecl(Id(BJq), BoolType, None, None), VarDecl(Id(Ouyq), ArrayType([52.31, 36.4, 45.64], BoolType), None, None)], Return(StringLit(sNd))), FuncDecl(Id(tj), [VarDecl(Id(PO), ArrayType([58.86, 13.93], BoolType), None, None), VarDecl(Id(Vdl), BoolType, None, None), VarDecl(Id(CoKg), ArrayType([56.88, 25.93, 63.35], StringType), None, None)], Block([VarDecl(Id(EkmM), ArrayType([45.42, 98.66], BoolType), None, BooleanLit(True)), VarDecl(Id(Ne), StringType, None, None), Block([AssignStmt(Id(CIj), StringLit(ayS)), For(Id(BN3), NumLit(49.92), NumLit(30.11), CallStmt(Id(oX), [StringLit(wH), BooleanLit(False)])), Break])])), FuncDecl(Id(DY), [VarDecl(Id(Guq), ArrayType([16.53, 83.97], BoolType), None, None), VarDecl(Id(LE), ArrayType([30.81], StringType), None, None)], Return()), FuncDecl(Id(IsSj), [], Block([For(Id(sdqf), StringLit(uQ), Id(rWK), Block([If(Id(BEj), Return(StringLit(sLRLW))), [(Id(aTKJ), AssignStmt(Id(hCq_), Id(J1I))), (NumLit(34.93), Block([Return(NumLit(87.02))])), (BooleanLit(True), If(BooleanLit(True), VarDecl(Id(G2), BoolType, None, NumLit(15.67))), [(StringLit(R), Continue), (BooleanLit(True), CallStmt(Id(UKF), [NumLit(41.78), BooleanLit(True)])), (StringLit(wxkHD), Return()), (BooleanLit(False), For(Id(Bj9j), StringLit(ZLyqm), BooleanLit(False), Break))], None), (BooleanLit(False), Continue)], AssignStmt(ArrayCell(Id(xQ8I), [BooleanLit(False), Id(NU0)]), Id(YHm)), Return()]))])), FuncDecl(Id(wU), [VarDecl(Id(i5), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011508))

	def test_2153011509(self):
		input = '''
func ul ()	return false

dynamic Az
func X6 (bool zGX[87.09], number BW1[1.74,7.73,54.24], string BB[36.62])
	begin
		begin
			break
			for jY5 until "zuJ" by "dGkU"
				begin
					begin
					end
					if ("zbAYs") Wg(true)
					elif ("F") if ("ksK")
					for M1q until "HLsG" by Tm
						if ("g") bool XdIC[10.5,78.02,10.14] <- true
						elif (11.52) continue
						elif (32.17) number AIt <- "sue"
					else begin
					end
					elif (Oo) bool iK[56.78]
					elif (G6ZY) for xakV until F6Pf by "Bs"
						if ("yx")
						string fqia[4.12]
						elif ("I") meE <- 10.61
						elif (78.73) return Cl
						elif (v31)
						begin
							begin
							end
							Aj("rM", false, 59.6)
						end
						elif (true)
						for ro until ggFk by true
							return wrEJ
						elif (70.6)
						for Eg until "twbT" by OGW
							if (77.19) begin
								break
								for NZv until false by true
									return 58.33
								begin
									if (false)
									for U2 until oi by true
										begin
											if (72.09) HO6a()
											elif (51.39) bool FOo <- qPD
											elif (true) break
											elif (84.8) begin
												continue
												JgQ5()
											end
											elif (N0gS) f52i(qMo)
											elif (AP)
											begin
												if ("yzs") for JWD until 4.71 by Gb
													return true
												elif ("dl")
												continue
												elif (21.85) break
												elif ("fW")
												var zdJ <- true
												return false
											end
											continue
										end
									elif (Bh)
									break
									elif ("pu") begin
										for w9rv until true by "kdeI"
											if (true)
											begin
												bool iUVP[61.15,29.09,39.02]
											end
											elif (30.79) string sr3j <- 3.66
											elif ("u")
											break
											elif (Dmq)
											for Ii until false by "kQk"
												begin
													o_ <- false
													X8Qs["Wd", "mMFC"] <- "B"
													vx <- true
												end
											elif (false)
											string KE[95.03,79.76]
											else return
										NF[ck1y, true] <- "Jfx"
									end
									else return BusO
								end
							end
							elif (true) for IZh1 until "eQ" by TOvJ
								break
							elif (60.73) break
							elif (false)
							begin
								continue
							end
					Bj <- NM
				end
		end
		TAFi[34.48, QlR5] <- aq
	end

func nr (string TK, number JR[96.69], string mb[3.07])	return
'''
		expect = '''Program([FuncDecl(Id(ul), [], Return(BooleanLit(False))), VarDecl(Id(Az), None, dynamic, None), FuncDecl(Id(X6), [VarDecl(Id(zGX), ArrayType([87.09], BoolType), None, None), VarDecl(Id(BW1), ArrayType([1.74, 7.73, 54.24], NumberType), None, None), VarDecl(Id(BB), ArrayType([36.62], StringType), None, None)], Block([Block([Break, For(Id(jY5), StringLit(zuJ), StringLit(dGkU), Block([Block([]), If(StringLit(zbAYs), CallStmt(Id(Wg), [BooleanLit(True)])), [(StringLit(F), If(StringLit(ksK), For(Id(M1q), StringLit(HLsG), Id(Tm), If(StringLit(g), VarDecl(Id(XdIC), ArrayType([10.5, 78.02, 10.14], BoolType), None, BooleanLit(True))), [(NumLit(11.52), Continue), (NumLit(32.17), VarDecl(Id(AIt), NumberType, None, StringLit(sue)))], Block([]))), [(Id(Oo), VarDecl(Id(iK), ArrayType([56.78], BoolType), None, None)), (Id(G6ZY), For(Id(xakV), Id(F6Pf), StringLit(Bs), If(StringLit(yx), VarDecl(Id(fqia), ArrayType([4.12], StringType), None, None)), [(StringLit(I), AssignStmt(Id(meE), NumLit(10.61))), (NumLit(78.73), Return(Id(Cl))), (Id(v31), Block([Block([]), CallStmt(Id(Aj), [StringLit(rM), BooleanLit(False), NumLit(59.6)])])), (BooleanLit(True), For(Id(ro), Id(ggFk), BooleanLit(True), Return(Id(wrEJ)))), (NumLit(70.6), For(Id(Eg), StringLit(twbT), Id(OGW), If(NumLit(77.19), Block([Break, For(Id(NZv), BooleanLit(False), BooleanLit(True), Return(NumLit(58.33))), Block([If(BooleanLit(False), For(Id(U2), Id(oi), BooleanLit(True), Block([If(NumLit(72.09), CallStmt(Id(HO6a), [])), [(NumLit(51.39), VarDecl(Id(FOo), BoolType, None, Id(qPD))), (BooleanLit(True), Break), (NumLit(84.8), Block([Continue, CallStmt(Id(JgQ5), [])])), (Id(N0gS), CallStmt(Id(f52i), [Id(qMo)])), (Id(AP), Block([If(StringLit(yzs), For(Id(JWD), NumLit(4.71), Id(Gb), Return(BooleanLit(True)))), [(StringLit(dl), Continue), (NumLit(21.85), Break), (StringLit(fW), VarDecl(Id(zdJ), None, var, BooleanLit(True)))], None, Return(BooleanLit(False))]))], None, Continue]))), [(Id(Bh), Break), (StringLit(pu), Block([For(Id(w9rv), BooleanLit(True), StringLit(kdeI), If(BooleanLit(True), Block([VarDecl(Id(iUVP), ArrayType([61.15, 29.09, 39.02], BoolType), None, None)])), [(NumLit(30.79), VarDecl(Id(sr3j), StringType, None, NumLit(3.66))), (StringLit(u), Break), (Id(Dmq), For(Id(Ii), BooleanLit(False), StringLit(kQk), Block([AssignStmt(Id(o_), BooleanLit(False)), AssignStmt(ArrayCell(Id(X8Qs), [StringLit(Wd), StringLit(mMFC)]), StringLit(B)), AssignStmt(Id(vx), BooleanLit(True))]))), (BooleanLit(False), VarDecl(Id(KE), ArrayType([95.03, 79.76], StringType), None, None))], Return()), AssignStmt(ArrayCell(Id(NF), [Id(ck1y), BooleanLit(True)]), StringLit(Jfx))]))], Return(Id(BusO))])])), [], None)), (BooleanLit(True), For(Id(IZh1), StringLit(eQ), Id(TOvJ), Break))], None)), (NumLit(60.73), Break)], None), (BooleanLit(False), Block([Continue]))], None, AssignStmt(Id(Bj), Id(NM))]))]), AssignStmt(ArrayCell(Id(TAFi), [NumLit(34.48), Id(QlR5)]), Id(aq))])), FuncDecl(Id(nr), [VarDecl(Id(TK), StringType, None, None), VarDecl(Id(JR), ArrayType([96.69], NumberType), None, None), VarDecl(Id(mb), ArrayType([3.07], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011509))

	def test_2153011510(self):
		input = '''
string uSM6 <- true
'''
		expect = '''Program([VarDecl(Id(uSM6), StringType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011510))

	def test_2153011511(self):
		input = '''
number yQq[72.39]
bool wM1 <- sY7
func wmWW (bool x1J6, number DCm)
	return false
bool CdNk <- "YV"
func IxWm (string n0, string vr6b)
	begin
	end

'''
		expect = '''Program([VarDecl(Id(yQq), ArrayType([72.39], NumberType), None, None), VarDecl(Id(wM1), BoolType, None, Id(sY7)), FuncDecl(Id(wmWW), [VarDecl(Id(x1J6), BoolType, None, None), VarDecl(Id(DCm), NumberType, None, None)], Return(BooleanLit(False))), VarDecl(Id(CdNk), BoolType, None, StringLit(YV)), FuncDecl(Id(IxWm), [VarDecl(Id(n0), StringType, None, None), VarDecl(Id(vr6b), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011511))

	def test_2153011512(self):
		input = '''
dynamic YvVD
dynamic m6
'''
		expect = '''Program([VarDecl(Id(YvVD), None, dynamic, None), VarDecl(Id(m6), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011512))

	def test_2153011513(self):
		input = '''
func aM ()	return
'''
		expect = '''Program([FuncDecl(Id(aM), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011513))

	def test_2153011514(self):
		input = '''
func Sy (string efc[86.04,24.25], bool KdJ[63.7], string DQE[82.46,84.17])	return
'''
		expect = '''Program([FuncDecl(Id(Sy), [VarDecl(Id(efc), ArrayType([86.04, 24.25], StringType), None, None), VarDecl(Id(KdJ), ArrayType([63.7], BoolType), None, None), VarDecl(Id(DQE), ArrayType([82.46, 84.17], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011514))

	def test_2153011515(self):
		input = '''
func wspO ()	return "hNJS"

'''
		expect = '''Program([FuncDecl(Id(wspO), [], Return(StringLit(hNJS)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011515))

	def test_2153011516(self):
		input = '''
bool yF[33.92] <- "j"
'''
		expect = '''Program([VarDecl(Id(yF), ArrayType([33.92], BoolType), None, StringLit(j))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011516))

	def test_2153011517(self):
		input = '''
func KDn (bool D_c, string LhWr[60.54,61.02], string R3xL)
	return

var vKQY <- "f"
'''
		expect = '''Program([FuncDecl(Id(KDn), [VarDecl(Id(D_c), BoolType, None, None), VarDecl(Id(LhWr), ArrayType([60.54, 61.02], StringType), None, None), VarDecl(Id(R3xL), StringType, None, None)], Return()), VarDecl(Id(vKQY), None, var, StringLit(f))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011517))

	def test_2153011518(self):
		input = '''
bool CMPy <- false
number yJ[25.61,7.61]
func XqjV ()
	return VE
number D__ <- true
number a2E
'''
		expect = '''Program([VarDecl(Id(CMPy), BoolType, None, BooleanLit(False)), VarDecl(Id(yJ), ArrayType([25.61, 7.61], NumberType), None, None), FuncDecl(Id(XqjV), [], Return(Id(VE))), VarDecl(Id(D__), NumberType, None, BooleanLit(True)), VarDecl(Id(a2E), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011518))

	def test_2153011519(self):
		input = '''
bool Ap[95.89]
number WP[71.06]
func Akm (number RZ)
	return true

'''
		expect = '''Program([VarDecl(Id(Ap), ArrayType([95.89], BoolType), None, None), VarDecl(Id(WP), ArrayType([71.06], NumberType), None, None), FuncDecl(Id(Akm), [VarDecl(Id(RZ), NumberType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011519))

	def test_2153011520(self):
		input = '''
var CMbV <- "MqiJ"
bool WCi <- 74.91
number yvx[5.98,62.64]
string Jt
'''
		expect = '''Program([VarDecl(Id(CMbV), None, var, StringLit(MqiJ)), VarDecl(Id(WCi), BoolType, None, NumLit(74.91)), VarDecl(Id(yvx), ArrayType([5.98, 62.64], NumberType), None, None), VarDecl(Id(Jt), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011520))

	def test_2153011521(self):
		input = '''
bool VS[17.56,26.79] <- "KGmA"
func R2b (bool OhL, string u9t[62.82,80.62])
	return 70.75
bool ifcp[72.23] <- false
dynamic bB <- HII7
string fc <- 36.5
'''
		expect = '''Program([VarDecl(Id(VS), ArrayType([17.56, 26.79], BoolType), None, StringLit(KGmA)), FuncDecl(Id(R2b), [VarDecl(Id(OhL), BoolType, None, None), VarDecl(Id(u9t), ArrayType([62.82, 80.62], StringType), None, None)], Return(NumLit(70.75))), VarDecl(Id(ifcp), ArrayType([72.23], BoolType), None, BooleanLit(False)), VarDecl(Id(bB), None, dynamic, Id(HII7)), VarDecl(Id(fc), StringType, None, NumLit(36.5))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011521))

	def test_2153011522(self):
		input = '''
bool P1[97.81]
func SJf (number lH, string qTDg, string Fkm[78.31,35.65,11.86])
	begin
		O4p("ZY", Q1F_)
		if (Uc)
		begin
		end
		elif (ddPN)
		begin
			for Lr2 until cpA3 by true
				TVd(78.5)
			break
		end
	end
func XC3u (number wDxU, bool tpd, string dWF[85.14])
	return

'''
		expect = '''Program([VarDecl(Id(P1), ArrayType([97.81], BoolType), None, None), FuncDecl(Id(SJf), [VarDecl(Id(lH), NumberType, None, None), VarDecl(Id(qTDg), StringType, None, None), VarDecl(Id(Fkm), ArrayType([78.31, 35.65, 11.86], StringType), None, None)], Block([CallStmt(Id(O4p), [StringLit(ZY), Id(Q1F_)]), If(Id(Uc), Block([])), [(Id(ddPN), Block([For(Id(Lr2), Id(cpA3), BooleanLit(True), CallStmt(Id(TVd), [NumLit(78.5)])), Break]))], None])), FuncDecl(Id(XC3u), [VarDecl(Id(wDxU), NumberType, None, None), VarDecl(Id(tpd), BoolType, None, None), VarDecl(Id(dWF), ArrayType([85.14], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011522))

	def test_2153011523(self):
		input = '''
func nMoQ (bool jE, string opV[82.1], number jg[19.77])
	begin
		begin
		end
		begin
			break
			number wb
			Agb <- 5.0
		end
	end
func iQI (number nx[84.25], number igi[84.42], number mNn)
	return true

var wXK <- VV
string Ju0O <- "hukpP"
'''
		expect = '''Program([FuncDecl(Id(nMoQ), [VarDecl(Id(jE), BoolType, None, None), VarDecl(Id(opV), ArrayType([82.1], StringType), None, None), VarDecl(Id(jg), ArrayType([19.77], NumberType), None, None)], Block([Block([]), Block([Break, VarDecl(Id(wb), NumberType, None, None), AssignStmt(Id(Agb), NumLit(5.0))])])), FuncDecl(Id(iQI), [VarDecl(Id(nx), ArrayType([84.25], NumberType), None, None), VarDecl(Id(igi), ArrayType([84.42], NumberType), None, None), VarDecl(Id(mNn), NumberType, None, None)], Return(BooleanLit(True))), VarDecl(Id(wXK), None, var, Id(VV)), VarDecl(Id(Ju0O), StringType, None, StringLit(hukpP))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011523))

	def test_2153011524(self):
		input = '''
func vZU (bool tm, bool Pyjk, bool NK[32.23,5.68])
	return
dynamic vYu <- qo
number Q7y_[60.98,73.77,23.37]
'''
		expect = '''Program([FuncDecl(Id(vZU), [VarDecl(Id(tm), BoolType, None, None), VarDecl(Id(Pyjk), BoolType, None, None), VarDecl(Id(NK), ArrayType([32.23, 5.68], BoolType), None, None)], Return()), VarDecl(Id(vYu), None, dynamic, Id(qo)), VarDecl(Id(Q7y_), ArrayType([60.98, 73.77, 23.37], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011524))

	def test_2153011525(self):
		input = '''
string YdJn[92.17,22.06,60.27]
'''
		expect = '''Program([VarDecl(Id(YdJn), ArrayType([92.17, 22.06, 60.27], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011525))

	def test_2153011526(self):
		input = '''
func K9 (bool W1O[51.44,27.67], bool KB)	begin
		break
	end
func z5X (number X9, number dWw[97.82,63.4])	return
func x_1 ()	begin
		CAgF("QwKY")
		return false
	end
'''
		expect = '''Program([FuncDecl(Id(K9), [VarDecl(Id(W1O), ArrayType([51.44, 27.67], BoolType), None, None), VarDecl(Id(KB), BoolType, None, None)], Block([Break])), FuncDecl(Id(z5X), [VarDecl(Id(X9), NumberType, None, None), VarDecl(Id(dWw), ArrayType([97.82, 63.4], NumberType), None, None)], Return()), FuncDecl(Id(x_1), [], Block([CallStmt(Id(CAgF), [StringLit(QwKY)]), Return(BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011526))

	def test_2153011527(self):
		input = '''
func YA (string M_y2, bool v3c[77.6])	return
string Do <- 79.93
func URAr (number y6I[56.91,69.48,25.63], number IR)
	begin
		begin
			return
		end
	end

string T7H[74.35,38.59,42.73]
dynamic ZMAw <- "smeBD"
'''
		expect = '''Program([FuncDecl(Id(YA), [VarDecl(Id(M_y2), StringType, None, None), VarDecl(Id(v3c), ArrayType([77.6], BoolType), None, None)], Return()), VarDecl(Id(Do), StringType, None, NumLit(79.93)), FuncDecl(Id(URAr), [VarDecl(Id(y6I), ArrayType([56.91, 69.48, 25.63], NumberType), None, None), VarDecl(Id(IR), NumberType, None, None)], Block([Block([Return()])])), VarDecl(Id(T7H), ArrayType([74.35, 38.59, 42.73], StringType), None, None), VarDecl(Id(ZMAw), None, dynamic, StringLit(smeBD))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011527))

	def test_2153011528(self):
		input = '''
func m4 (number rlbg[88.32,37.67])	return false

dynamic V_mj <- "ym"
func ZlXm ()
	return

string m7
func AW (number fyPm[73.96])
	return true

'''
		expect = '''Program([FuncDecl(Id(m4), [VarDecl(Id(rlbg), ArrayType([88.32, 37.67], NumberType), None, None)], Return(BooleanLit(False))), VarDecl(Id(V_mj), None, dynamic, StringLit(ym)), FuncDecl(Id(ZlXm), [], Return()), VarDecl(Id(m7), StringType, None, None), FuncDecl(Id(AW), [VarDecl(Id(fyPm), ArrayType([73.96], NumberType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011528))

	def test_2153011529(self):
		input = '''
func VKz ()
	begin
		zk_["xsrqH", "GSaq", ae2] <- CXE
		break
		return
	end

dynamic UgJ <- "oRi"
func oo5 (number guu[70.2,69.91])
	return "fT"
dynamic EG <- 32.75
func ekT (string BqO[44.74], number ec, string E7[62.77,59.19])
	begin
		sq <- 4.67
		return "XuNdx"
	end
'''
		expect = '''Program([FuncDecl(Id(VKz), [], Block([AssignStmt(ArrayCell(Id(zk_), [StringLit(xsrqH), StringLit(GSaq), Id(ae2)]), Id(CXE)), Break, Return()])), VarDecl(Id(UgJ), None, dynamic, StringLit(oRi)), FuncDecl(Id(oo5), [VarDecl(Id(guu), ArrayType([70.2, 69.91], NumberType), None, None)], Return(StringLit(fT))), VarDecl(Id(EG), None, dynamic, NumLit(32.75)), FuncDecl(Id(ekT), [VarDecl(Id(BqO), ArrayType([44.74], StringType), None, None), VarDecl(Id(ec), NumberType, None, None), VarDecl(Id(E7), ArrayType([62.77, 59.19], StringType), None, None)], Block([AssignStmt(Id(sq), NumLit(4.67)), Return(StringLit(XuNdx))]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011529))

	def test_2153011530(self):
		input = '''
func yRo (string OhF3)	return true
var dq <- "CTH"
number Hnjn[21.92,65.89,58.92]
func gc (bool Lj[80.72], number cs[47.94,29.57], string Jt[19.51])	return
'''
		expect = '''Program([FuncDecl(Id(yRo), [VarDecl(Id(OhF3), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(dq), None, var, StringLit(CTH)), VarDecl(Id(Hnjn), ArrayType([21.92, 65.89, 58.92], NumberType), None, None), FuncDecl(Id(gc), [VarDecl(Id(Lj), ArrayType([80.72], BoolType), None, None), VarDecl(Id(cs), ArrayType([47.94, 29.57], NumberType), None, None), VarDecl(Id(Jt), ArrayType([19.51], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011530))

	def test_2153011531(self):
		input = '''
bool HY[72.45] <- ur
func jaqd (string MkhY[14.95])
	return true
func T9 (string sA[18.11,95.07], string SDoq[83.64], string HX)	return true

func VJ (number Lv, string xNT0, string xN)	return

bool ec[41.07,89.35,78.8]
'''
		expect = '''Program([VarDecl(Id(HY), ArrayType([72.45], BoolType), None, Id(ur)), FuncDecl(Id(jaqd), [VarDecl(Id(MkhY), ArrayType([14.95], StringType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(T9), [VarDecl(Id(sA), ArrayType([18.11, 95.07], StringType), None, None), VarDecl(Id(SDoq), ArrayType([83.64], StringType), None, None), VarDecl(Id(HX), StringType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(VJ), [VarDecl(Id(Lv), NumberType, None, None), VarDecl(Id(xNT0), StringType, None, None), VarDecl(Id(xN), StringType, None, None)], Return()), VarDecl(Id(ec), ArrayType([41.07, 89.35, 78.8], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011531))

	def test_2153011532(self):
		input = '''
number t_Ra
func XI ()	return Zm3
func zzyf (bool QIAU, string nlp, number E2Ri[27.72,6.53,33.07])	return

func Pm_J (number KX6F[34.98,2.04,63.25], bool iBf, number Vbh[65.06])	begin
	end
number vD[68.03] <- 13.03
'''
		expect = '''Program([VarDecl(Id(t_Ra), NumberType, None, None), FuncDecl(Id(XI), [], Return(Id(Zm3))), FuncDecl(Id(zzyf), [VarDecl(Id(QIAU), BoolType, None, None), VarDecl(Id(nlp), StringType, None, None), VarDecl(Id(E2Ri), ArrayType([27.72, 6.53, 33.07], NumberType), None, None)], Return()), FuncDecl(Id(Pm_J), [VarDecl(Id(KX6F), ArrayType([34.98, 2.04, 63.25], NumberType), None, None), VarDecl(Id(iBf), BoolType, None, None), VarDecl(Id(Vbh), ArrayType([65.06], NumberType), None, None)], Block([])), VarDecl(Id(vD), ArrayType([68.03], NumberType), None, NumLit(13.03))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011532))

	def test_2153011533(self):
		input = '''
string Hh[43.08,26.52,84.66] <- "BM"
func xaxx (string X2, number FOeo, string Tufl[11.41])
	return jN

'''
		expect = '''Program([VarDecl(Id(Hh), ArrayType([43.08, 26.52, 84.66], StringType), None, StringLit(BM)), FuncDecl(Id(xaxx), [VarDecl(Id(X2), StringType, None, None), VarDecl(Id(FOeo), NumberType, None, None), VarDecl(Id(Tufl), ArrayType([11.41], StringType), None, None)], Return(Id(jN)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011533))

	def test_2153011534(self):
		input = '''
func RE (bool vkF)
	begin
		if (kvB2) for RN until asE by zT
			begin
				begin
					return d0x
					qZA(E0KU)
					if (wQax)
					return 25.53
					elif (75.42)
					UJv <- "ZID"
					elif (35.44)
					break
				end
			end
		elif (61.63)
		Yc(Mef, 85.43, "I")
		else begin
			continue
			if (msS)
			for oLU until true by "WO"
				if (Bfg) bS5 <- zr
				elif (z7Y) pm <- "bZ"
				elif (32.73)
				s0m()
				elif ("H")
				continue
			elif ("xix") return gwEC
			elif ("QEIbJ") for NkK4 until "JBNzT" by true
				begin
				end
			else for gi until "eq" by 19.34
				if (sH8A)
				if ("SCtI")
				sPz()
				elif (26.94)
				begin
					begin
						if (yJr) continue
						elif (LbU) B4(MF)
						elif (false) break
						break
					end
				end
				elif (41.09) begin
					begin
						continue
					end
					lW7f(pb)
				end
				elif (5.17) begin
					break
					sO("yFsbZ", 26.21, "Vosz")
					oOc["pyliG", false, N2v] <- 44.37
				end
				elif (xXB) break
		end
	end

func i4hx (string yI)
	return 8.32

func OE ()	return

bool bqR2[42.14,53.81]
number FhqW[83.49,76.07,88.07]
'''
		expect = '''Program([FuncDecl(Id(RE), [VarDecl(Id(vkF), BoolType, None, None)], Block([If(Id(kvB2), For(Id(RN), Id(asE), Id(zT), Block([Block([Return(Id(d0x)), CallStmt(Id(qZA), [Id(E0KU)]), If(Id(wQax), Return(NumLit(25.53))), [(NumLit(75.42), AssignStmt(Id(UJv), StringLit(ZID))), (NumLit(35.44), Break)], None])]))), [(NumLit(61.63), CallStmt(Id(Yc), [Id(Mef), NumLit(85.43), StringLit(I)]))], Block([Continue, If(Id(msS), For(Id(oLU), BooleanLit(True), StringLit(WO), If(Id(Bfg), AssignStmt(Id(bS5), Id(zr))), [(Id(z7Y), AssignStmt(Id(pm), StringLit(bZ))), (NumLit(32.73), CallStmt(Id(s0m), [])), (StringLit(H), Continue), (StringLit(xix), Return(Id(gwEC))), (StringLit(QEIbJ), For(Id(NkK4), StringLit(JBNzT), BooleanLit(True), Block([])))], For(Id(gi), StringLit(eq), NumLit(19.34), If(Id(sH8A), If(StringLit(SCtI), CallStmt(Id(sPz), [])), [(NumLit(26.94), Block([Block([If(Id(yJr), Continue), [(Id(LbU), CallStmt(Id(B4), [Id(MF)])), (BooleanLit(False), Break)], None, Break])])), (NumLit(41.09), Block([Block([Continue]), CallStmt(Id(lW7f), [Id(pb)])])), (NumLit(5.17), Block([Break, CallStmt(Id(sO), [StringLit(yFsbZ), NumLit(26.21), StringLit(Vosz)]), AssignStmt(ArrayCell(Id(oOc), [StringLit(pyliG), BooleanLit(False), Id(N2v)]), NumLit(44.37))])), (Id(xXB), Break)], None), [], None))), [], None])])), FuncDecl(Id(i4hx), [VarDecl(Id(yI), StringType, None, None)], Return(NumLit(8.32))), FuncDecl(Id(OE), [], Return()), VarDecl(Id(bqR2), ArrayType([42.14, 53.81], BoolType), None, None), VarDecl(Id(FhqW), ArrayType([83.49, 76.07, 88.07], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011534))

	def test_2153011535(self):
		input = '''
func G8 ()
	return
func GSFC (number dej[88.61])
	begin
		continue
		bp <- 91.27
	end

var s6 <- Jkz
string mT2
func J3 ()
	return
'''
		expect = '''Program([FuncDecl(Id(G8), [], Return()), FuncDecl(Id(GSFC), [VarDecl(Id(dej), ArrayType([88.61], NumberType), None, None)], Block([Continue, AssignStmt(Id(bp), NumLit(91.27))])), VarDecl(Id(s6), None, var, Id(Jkz)), VarDecl(Id(mT2), StringType, None, None), FuncDecl(Id(J3), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011535))

	def test_2153011536(self):
		input = '''
func NIJ ()	begin
		var Tcb <- Xn
		break
	end
var OmI <- hpE
func Pj (string yp[82.51])	return L0

func lgV ()
	return
'''
		expect = '''Program([FuncDecl(Id(NIJ), [], Block([VarDecl(Id(Tcb), None, var, Id(Xn)), Break])), VarDecl(Id(OmI), None, var, Id(hpE)), FuncDecl(Id(Pj), [VarDecl(Id(yp), ArrayType([82.51], StringType), None, None)], Return(Id(L0))), FuncDecl(Id(lgV), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011536))

	def test_2153011537(self):
		input = '''
bool sy[62.13,88.22]
'''
		expect = '''Program([VarDecl(Id(sy), ArrayType([62.13, 88.22], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011537))

	def test_2153011538(self):
		input = '''
number cHAX
'''
		expect = '''Program([VarDecl(Id(cHAX), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011538))

	def test_2153011539(self):
		input = '''
func UU (bool dB68, number E6O[47.34], string rYQ)	return

'''
		expect = '''Program([FuncDecl(Id(UU), [VarDecl(Id(dB68), BoolType, None, None), VarDecl(Id(E6O), ArrayType([47.34], NumberType), None, None), VarDecl(Id(rYQ), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011539))

	def test_2153011540(self):
		input = '''
number yax[11.47,25.18]
'''
		expect = '''Program([VarDecl(Id(yax), ArrayType([11.47, 25.18], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011540))

	def test_2153011541(self):
		input = '''
func v7j (string Tt)	return

bool ZN[13.54,33.92] <- "AoVD"
bool L9Mj
'''
		expect = '''Program([FuncDecl(Id(v7j), [VarDecl(Id(Tt), StringType, None, None)], Return()), VarDecl(Id(ZN), ArrayType([13.54, 33.92], BoolType), None, StringLit(AoVD)), VarDecl(Id(L9Mj), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011541))

	def test_2153011542(self):
		input = '''
string j0w5[22.36,18.43,44.9] <- "qoIhk"
func oEPR ()	return
func wwyx ()	begin
	end

func al ()
	begin
		begin
		end
	end
func Ym (number ya[97.58,86.2,86.38], number sz)
	return
'''
		expect = '''Program([VarDecl(Id(j0w5), ArrayType([22.36, 18.43, 44.9], StringType), None, StringLit(qoIhk)), FuncDecl(Id(oEPR), [], Return()), FuncDecl(Id(wwyx), [], Block([])), FuncDecl(Id(al), [], Block([Block([])])), FuncDecl(Id(Ym), [VarDecl(Id(ya), ArrayType([97.58, 86.2, 86.38], NumberType), None, None), VarDecl(Id(sz), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011542))

	def test_2153011543(self):
		input = '''
func KR1B (string YGx, number u2g6)	begin
		V6()
		continue
	end

'''
		expect = '''Program([FuncDecl(Id(KR1B), [VarDecl(Id(YGx), StringType, None, None), VarDecl(Id(u2g6), NumberType, None, None)], Block([CallStmt(Id(V6), []), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011543))

	def test_2153011544(self):
		input = '''
func nZQj (bool Xi, number igu7, bool yS)	begin
		begin
			continue
		end
	end

number gGd
dynamic Dqy
string AFk[85.39,83.52,66.86] <- FJ
dynamic zdH <- "SV"
'''
		expect = '''Program([FuncDecl(Id(nZQj), [VarDecl(Id(Xi), BoolType, None, None), VarDecl(Id(igu7), NumberType, None, None), VarDecl(Id(yS), BoolType, None, None)], Block([Block([Continue])])), VarDecl(Id(gGd), NumberType, None, None), VarDecl(Id(Dqy), None, dynamic, None), VarDecl(Id(AFk), ArrayType([85.39, 83.52, 66.86], StringType), None, Id(FJ)), VarDecl(Id(zdH), None, dynamic, StringLit(SV))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011544))

	def test_2153011545(self):
		input = '''
func fOes (bool Nu, number Bbv[69.1,48.31,33.75])	begin
		break
		for B8 until dVw by true
			continue
		ZvJl(29.45)
	end
func F_g (number R1F[54.19], number rrz_, bool frn[38.82,34.1])
	return d6X

func DO6 (number MZzO, string ht, string U87[75.62,14.42,45.2])
	return

bool tH4 <- Qa
'''
		expect = '''Program([FuncDecl(Id(fOes), [VarDecl(Id(Nu), BoolType, None, None), VarDecl(Id(Bbv), ArrayType([69.1, 48.31, 33.75], NumberType), None, None)], Block([Break, For(Id(B8), Id(dVw), BooleanLit(True), Continue), CallStmt(Id(ZvJl), [NumLit(29.45)])])), FuncDecl(Id(F_g), [VarDecl(Id(R1F), ArrayType([54.19], NumberType), None, None), VarDecl(Id(rrz_), NumberType, None, None), VarDecl(Id(frn), ArrayType([38.82, 34.1], BoolType), None, None)], Return(Id(d6X))), FuncDecl(Id(DO6), [VarDecl(Id(MZzO), NumberType, None, None), VarDecl(Id(ht), StringType, None, None), VarDecl(Id(U87), ArrayType([75.62, 14.42, 45.2], StringType), None, None)], Return()), VarDecl(Id(tH4), BoolType, None, Id(Qa))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011545))

	def test_2153011546(self):
		input = '''
dynamic oHB <- 16.82
func Iq (number s07_[47.84,15.1,32.32], bool lVD)	return g5

func Sw (string ck[30.69,89.41,61.48], bool tuxd)	return

'''
		expect = '''Program([VarDecl(Id(oHB), None, dynamic, NumLit(16.82)), FuncDecl(Id(Iq), [VarDecl(Id(s07_), ArrayType([47.84, 15.1, 32.32], NumberType), None, None), VarDecl(Id(lVD), BoolType, None, None)], Return(Id(g5))), FuncDecl(Id(Sw), [VarDecl(Id(ck), ArrayType([30.69, 89.41, 61.48], StringType), None, None), VarDecl(Id(tuxd), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011546))

	def test_2153011547(self):
		input = '''
func g2G (bool SE[63.84,17.44,63.52], bool xe)	return Hp
string Ou[6.69,77.29]
'''
		expect = '''Program([FuncDecl(Id(g2G), [VarDecl(Id(SE), ArrayType([63.84, 17.44, 63.52], BoolType), None, None), VarDecl(Id(xe), BoolType, None, None)], Return(Id(Hp))), VarDecl(Id(Ou), ArrayType([6.69, 77.29], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011547))

	def test_2153011548(self):
		input = '''
func O2 (number qpWp)	begin
		return ZAQL
		for qt until VTC by "JX"
			continue
		string ub
	end

'''
		expect = '''Program([FuncDecl(Id(O2), [VarDecl(Id(qpWp), NumberType, None, None)], Block([Return(Id(ZAQL)), For(Id(qt), Id(VTC), StringLit(JX), Continue), VarDecl(Id(ub), StringType, None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011548))

	def test_2153011549(self):
		input = '''
bool negw <- HQ_
'''
		expect = '''Program([VarDecl(Id(negw), BoolType, None, Id(HQ_))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011549))

	def test_2153011550(self):
		input = '''
func HU9X (string fJQ[14.05], string zDRk)	begin
		NTt <- 84.77
	end
number rE84
func ab (string oS)	begin
		for ndD until ZXh by 97.12
			Gy[51.0, X9v] <- epa_
		for Am0X until 33.6 by 55.48
			for znH until "paY" by 99.22
				SJ[true, iRMS, 97.6] <- 85.99
		for tlh until caK by true
			Bm0(3.14, "qmc")
	end
func UW (number dvai)	return true

'''
		expect = '''Program([FuncDecl(Id(HU9X), [VarDecl(Id(fJQ), ArrayType([14.05], StringType), None, None), VarDecl(Id(zDRk), StringType, None, None)], Block([AssignStmt(Id(NTt), NumLit(84.77))])), VarDecl(Id(rE84), NumberType, None, None), FuncDecl(Id(ab), [VarDecl(Id(oS), StringType, None, None)], Block([For(Id(ndD), Id(ZXh), NumLit(97.12), AssignStmt(ArrayCell(Id(Gy), [NumLit(51.0), Id(X9v)]), Id(epa_))), For(Id(Am0X), NumLit(33.6), NumLit(55.48), For(Id(znH), StringLit(paY), NumLit(99.22), AssignStmt(ArrayCell(Id(SJ), [BooleanLit(True), Id(iRMS), NumLit(97.6)]), NumLit(85.99)))), For(Id(tlh), Id(caK), BooleanLit(True), CallStmt(Id(Bm0), [NumLit(3.14), StringLit(qmc)]))])), FuncDecl(Id(UW), [VarDecl(Id(dvai), NumberType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011550))

	def test_2153011551(self):
		input = '''
func WK (string D9dT)
	return false
number d8pI[87.43,23.35] <- "NzVAf"
func eRr ()	return 82.58
func Om ()
	begin
		for zyN until 48.81 by true
			begin
			end
		break
	end

'''
		expect = '''Program([FuncDecl(Id(WK), [VarDecl(Id(D9dT), StringType, None, None)], Return(BooleanLit(False))), VarDecl(Id(d8pI), ArrayType([87.43, 23.35], NumberType), None, StringLit(NzVAf)), FuncDecl(Id(eRr), [], Return(NumLit(82.58))), FuncDecl(Id(Om), [], Block([For(Id(zyN), NumLit(48.81), BooleanLit(True), Block([])), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011551))

	def test_2153011552(self):
		input = '''
bool aE[42.23,9.02,66.23]
func lGU (bool x7[29.51])	begin
	end
dynamic pR0
'''
		expect = '''Program([VarDecl(Id(aE), ArrayType([42.23, 9.02, 66.23], BoolType), None, None), FuncDecl(Id(lGU), [VarDecl(Id(x7), ArrayType([29.51], BoolType), None, None)], Block([])), VarDecl(Id(pR0), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011552))

	def test_2153011553(self):
		input = '''
func iz (bool wN)	begin
		for HFU until true by "Yyw"
			LrJ(96.22)
		vWD <- "qyu"
	end

string cM[53.17]
func LN (number CRwy[38.2,54.61,5.8], string XwQG)	return
func Ib6m (bool A_[42.17])	return
string KKRo[30.8,20.44] <- RO
'''
		expect = '''Program([FuncDecl(Id(iz), [VarDecl(Id(wN), BoolType, None, None)], Block([For(Id(HFU), BooleanLit(True), StringLit(Yyw), CallStmt(Id(LrJ), [NumLit(96.22)])), AssignStmt(Id(vWD), StringLit(qyu))])), VarDecl(Id(cM), ArrayType([53.17], StringType), None, None), FuncDecl(Id(LN), [VarDecl(Id(CRwy), ArrayType([38.2, 54.61, 5.8], NumberType), None, None), VarDecl(Id(XwQG), StringType, None, None)], Return()), FuncDecl(Id(Ib6m), [VarDecl(Id(A_), ArrayType([42.17], BoolType), None, None)], Return()), VarDecl(Id(KKRo), ArrayType([30.8, 20.44], StringType), None, Id(RO))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011553))

	def test_2153011554(self):
		input = '''
func wog0 (string Yb, string MnPc)
	return

func L8d (string r_vV, bool DEG4, bool Cd[69.53,24.67,22.25])	return
func K9Hr (number J7)
	begin
		var kXu <- "MYIVA"
		dynamic inr9
		for EvEj until "wIy" by wTJ
			return 59.84
	end

func H6 (string bxpw, number EIP[17.05], string fH)	begin
	end

bool pu[66.93] <- "uPyo"
'''
		expect = '''Program([FuncDecl(Id(wog0), [VarDecl(Id(Yb), StringType, None, None), VarDecl(Id(MnPc), StringType, None, None)], Return()), FuncDecl(Id(L8d), [VarDecl(Id(r_vV), StringType, None, None), VarDecl(Id(DEG4), BoolType, None, None), VarDecl(Id(Cd), ArrayType([69.53, 24.67, 22.25], BoolType), None, None)], Return()), FuncDecl(Id(K9Hr), [VarDecl(Id(J7), NumberType, None, None)], Block([VarDecl(Id(kXu), None, var, StringLit(MYIVA)), VarDecl(Id(inr9), None, dynamic, None), For(Id(EvEj), StringLit(wIy), Id(wTJ), Return(NumLit(59.84)))])), FuncDecl(Id(H6), [VarDecl(Id(bxpw), StringType, None, None), VarDecl(Id(EIP), ArrayType([17.05], NumberType), None, None), VarDecl(Id(fH), StringType, None, None)], Block([])), VarDecl(Id(pu), ArrayType([66.93], BoolType), None, StringLit(uPyo))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011554))

	def test_2153011555(self):
		input = '''
func BXUB (number HM7[22.34,74.97,6.2])
	return

bool mA <- true
dynamic ax <- D04y
'''
		expect = '''Program([FuncDecl(Id(BXUB), [VarDecl(Id(HM7), ArrayType([22.34, 74.97, 6.2], NumberType), None, None)], Return()), VarDecl(Id(mA), BoolType, None, BooleanLit(True)), VarDecl(Id(ax), None, dynamic, Id(D04y))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011555))

	def test_2153011556(self):
		input = '''
dynamic l7
func EQ (number loLV, number Vf[83.41,13.11])
	return true

func sidN (string vH, bool Vm4)
	return 21.51

number WqbS[62.4,42.68]
func xTK (number S4iw[75.54,94.41], bool dae[49.79,98.01,82.05])
	return true
'''
		expect = '''Program([VarDecl(Id(l7), None, dynamic, None), FuncDecl(Id(EQ), [VarDecl(Id(loLV), NumberType, None, None), VarDecl(Id(Vf), ArrayType([83.41, 13.11], NumberType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(sidN), [VarDecl(Id(vH), StringType, None, None), VarDecl(Id(Vm4), BoolType, None, None)], Return(NumLit(21.51))), VarDecl(Id(WqbS), ArrayType([62.4, 42.68], NumberType), None, None), FuncDecl(Id(xTK), [VarDecl(Id(S4iw), ArrayType([75.54, 94.41], NumberType), None, None), VarDecl(Id(dae), ArrayType([49.79, 98.01, 82.05], BoolType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011556))

	def test_2153011557(self):
		input = '''
func L8Pn (bool Ey[52.0])	begin
	end

number I12K[44.95,50.94]
string gZYU
'''
		expect = '''Program([FuncDecl(Id(L8Pn), [VarDecl(Id(Ey), ArrayType([52.0], BoolType), None, None)], Block([])), VarDecl(Id(I12K), ArrayType([44.95, 50.94], NumberType), None, None), VarDecl(Id(gZYU), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011557))

	def test_2153011558(self):
		input = '''
bool T_5
number Z3 <- "kuJ"
func P1f ()
	return
number nI[93.16]
'''
		expect = '''Program([VarDecl(Id(T_5), BoolType, None, None), VarDecl(Id(Z3), NumberType, None, StringLit(kuJ)), FuncDecl(Id(P1f), [], Return()), VarDecl(Id(nI), ArrayType([93.16], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011558))

	def test_2153011559(self):
		input = '''
number wcIg[3.75]
func mk6j (number VJM)	begin
	end
string Gr[12.34]
'''
		expect = '''Program([VarDecl(Id(wcIg), ArrayType([3.75], NumberType), None, None), FuncDecl(Id(mk6j), [VarDecl(Id(VJM), NumberType, None, None)], Block([])), VarDecl(Id(Gr), ArrayType([12.34], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011559))

	def test_2153011560(self):
		input = '''
string HD[45.8,18.0] <- w7c
func dg4 (string Muy)
	return 7.42

bool lLv_[15.99]
func XL (string uF[32.44,38.0,68.75], string BQ, string pnyo)	begin
		break
		begin
		end
		string H_O[18.79]
	end
dynamic Zj <- "MX"
'''
		expect = '''Program([VarDecl(Id(HD), ArrayType([45.8, 18.0], StringType), None, Id(w7c)), FuncDecl(Id(dg4), [VarDecl(Id(Muy), StringType, None, None)], Return(NumLit(7.42))), VarDecl(Id(lLv_), ArrayType([15.99], BoolType), None, None), FuncDecl(Id(XL), [VarDecl(Id(uF), ArrayType([32.44, 38.0, 68.75], StringType), None, None), VarDecl(Id(BQ), StringType, None, None), VarDecl(Id(pnyo), StringType, None, None)], Block([Break, Block([]), VarDecl(Id(H_O), ArrayType([18.79], StringType), None, None)])), VarDecl(Id(Zj), None, dynamic, StringLit(MX))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011560))

	def test_2153011561(self):
		input = '''
func Xzv (number dfAh[45.93], bool BT_, string Q1UJ[79.16,50.13])	return
func HW (number r7c, number jIF, string N6X[53.73,99.52])	return

bool O6lT <- true
func n5L (number C_, number KG[30.4,36.03,64.36])
	begin
		ZUQ4[fo3R, false, "bHb"] <- Yj
	end
func HMb (number bjQ)	begin
	end

'''
		expect = '''Program([FuncDecl(Id(Xzv), [VarDecl(Id(dfAh), ArrayType([45.93], NumberType), None, None), VarDecl(Id(BT_), BoolType, None, None), VarDecl(Id(Q1UJ), ArrayType([79.16, 50.13], StringType), None, None)], Return()), FuncDecl(Id(HW), [VarDecl(Id(r7c), NumberType, None, None), VarDecl(Id(jIF), NumberType, None, None), VarDecl(Id(N6X), ArrayType([53.73, 99.52], StringType), None, None)], Return()), VarDecl(Id(O6lT), BoolType, None, BooleanLit(True)), FuncDecl(Id(n5L), [VarDecl(Id(C_), NumberType, None, None), VarDecl(Id(KG), ArrayType([30.4, 36.03, 64.36], NumberType), None, None)], Block([AssignStmt(ArrayCell(Id(ZUQ4), [Id(fo3R), BooleanLit(False), StringLit(bHb)]), Id(Yj))])), FuncDecl(Id(HMb), [VarDecl(Id(bjQ), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011561))

	def test_2153011562(self):
		input = '''
func w96 ()
	return false
bool DkS[28.88,67.24] <- Hacx
func sM (string eh, string Szda[48.45,52.53], string uzsz)
	return "gIXWG"

'''
		expect = '''Program([FuncDecl(Id(w96), [], Return(BooleanLit(False))), VarDecl(Id(DkS), ArrayType([28.88, 67.24], BoolType), None, Id(Hacx)), FuncDecl(Id(sM), [VarDecl(Id(eh), StringType, None, None), VarDecl(Id(Szda), ArrayType([48.45, 52.53], StringType), None, None), VarDecl(Id(uzsz), StringType, None, None)], Return(StringLit(gIXWG)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011562))

	def test_2153011563(self):
		input = '''
number HVo
func q7k (bool mT3[13.92], string FxkL[53.19,25.77], number EEI)
	begin
		AZUF <- "M"
	end

number VE0[34.42,41.4,1.59] <- 83.99
'''
		expect = '''Program([VarDecl(Id(HVo), NumberType, None, None), FuncDecl(Id(q7k), [VarDecl(Id(mT3), ArrayType([13.92], BoolType), None, None), VarDecl(Id(FxkL), ArrayType([53.19, 25.77], StringType), None, None), VarDecl(Id(EEI), NumberType, None, None)], Block([AssignStmt(Id(AZUF), StringLit(M))])), VarDecl(Id(VE0), ArrayType([34.42, 41.4, 1.59], NumberType), None, NumLit(83.99))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011563))

	def test_2153011564(self):
		input = '''
var LI3 <- LyA
'''
		expect = '''Program([VarDecl(Id(LI3), None, var, Id(LyA))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011564))

	def test_2153011565(self):
		input = '''
string Z09_[71.86,25.56,23.15]
func AvmC (string rYY[76.13,12.37,1.42], bool sE)	begin
		return
	end

'''
		expect = '''Program([VarDecl(Id(Z09_), ArrayType([71.86, 25.56, 23.15], StringType), None, None), FuncDecl(Id(AvmC), [VarDecl(Id(rYY), ArrayType([76.13, 12.37, 1.42], StringType), None, None), VarDecl(Id(sE), BoolType, None, None)], Block([Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011565))

	def test_2153011566(self):
		input = '''
number wsZ[99.6,92.58] <- true
func KB (bool iDI)
	return
number vg7r[21.89]
'''
		expect = '''Program([VarDecl(Id(wsZ), ArrayType([99.6, 92.58], NumberType), None, BooleanLit(True)), FuncDecl(Id(KB), [VarDecl(Id(iDI), BoolType, None, None)], Return()), VarDecl(Id(vg7r), ArrayType([21.89], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011566))

	def test_2153011567(self):
		input = '''
func BM9 ()
	return "BS"

'''
		expect = '''Program([FuncDecl(Id(BM9), [], Return(StringLit(BS)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011567))

	def test_2153011568(self):
		input = '''
string w8ev[91.21,81.75,47.73]
'''
		expect = '''Program([VarDecl(Id(w8ev), ArrayType([91.21, 81.75, 47.73], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011568))

	def test_2153011569(self):
		input = '''
number sL[90.6,81.02,88.24] <- 40.57
number zH[10.76,99.33,34.5]
var UkW <- "HPhAP"
func q3fn ()	return
string SpQ[3.11,73.81] <- false
'''
		expect = '''Program([VarDecl(Id(sL), ArrayType([90.6, 81.02, 88.24], NumberType), None, NumLit(40.57)), VarDecl(Id(zH), ArrayType([10.76, 99.33, 34.5], NumberType), None, None), VarDecl(Id(UkW), None, var, StringLit(HPhAP)), FuncDecl(Id(q3fn), [], Return()), VarDecl(Id(SpQ), ArrayType([3.11, 73.81], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011569))

	def test_2153011570(self):
		input = '''
func Qh8 (number mlt[69.13,60.07])
	return "iMBq"

'''
		expect = '''Program([FuncDecl(Id(Qh8), [VarDecl(Id(mlt), ArrayType([69.13, 60.07], NumberType), None, None)], Return(StringLit(iMBq)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011570))

	def test_2153011571(self):
		input = '''
func G_d (bool FT, string nHxd[8.9,87.87,64.46], bool xWM[19.66,78.04,62.53])
	begin
	end

func cx (string fB)
	begin
		bWU <- Ky
		continue
	end
func oeh (number F9Z[26.05,45.67], string Qbul[39.45,3.01])
	return "jfjT"

func tFlO (string Bfnb)
	begin
		if (AX) if (false) bool yBd[5.1,75.74] <- 66.46
		elif (12.86) continue
		elif (false)
		return true
		elif (tCdq) break
		elif (false)
		number os
		elif ("Dr")
		break
		else begin
			return
			ae(false)
		end
		elif (Rls) return
		elif (viQf) for Wz until P1p by false
			if (Ec)
			for kxCS until "S" by true
				continue
			elif ("lXHp") for VvbF until "DCqj" by "nj"
				XCLf[52.96] <- false
			elif ("P")
			begin
			end
			elif (18.57) for cpcf until 96.58 by true
				t17o(6.38)
			elif ("rS") continue
			else return true
		else return 59.04
		if (UO)
		string LTYu <- false
		elif (u7)
		B7(29.41, 4.77)
		elif ("ULMJK")
		hb(67.76, false, 21.01)
	end
'''
		expect = '''Program([FuncDecl(Id(G_d), [VarDecl(Id(FT), BoolType, None, None), VarDecl(Id(nHxd), ArrayType([8.9, 87.87, 64.46], StringType), None, None), VarDecl(Id(xWM), ArrayType([19.66, 78.04, 62.53], BoolType), None, None)], Block([])), FuncDecl(Id(cx), [VarDecl(Id(fB), StringType, None, None)], Block([AssignStmt(Id(bWU), Id(Ky)), Continue])), FuncDecl(Id(oeh), [VarDecl(Id(F9Z), ArrayType([26.05, 45.67], NumberType), None, None), VarDecl(Id(Qbul), ArrayType([39.45, 3.01], StringType), None, None)], Return(StringLit(jfjT))), FuncDecl(Id(tFlO), [VarDecl(Id(Bfnb), StringType, None, None)], Block([If(Id(AX), If(BooleanLit(False), VarDecl(Id(yBd), ArrayType([5.1, 75.74], BoolType), None, NumLit(66.46))), [(NumLit(12.86), Continue), (BooleanLit(False), Return(BooleanLit(True))), (Id(tCdq), Break), (BooleanLit(False), VarDecl(Id(os), NumberType, None, None)), (StringLit(Dr), Break)], Block([Return(), CallStmt(Id(ae), [BooleanLit(False)])])), [(Id(Rls), Return()), (Id(viQf), For(Id(Wz), Id(P1p), BooleanLit(False), If(Id(Ec), For(Id(kxCS), StringLit(S), BooleanLit(True), Continue)), [(StringLit(lXHp), For(Id(VvbF), StringLit(DCqj), StringLit(nj), AssignStmt(ArrayCell(Id(XCLf), [NumLit(52.96)]), BooleanLit(False)))), (StringLit(P), Block([])), (NumLit(18.57), For(Id(cpcf), NumLit(96.58), BooleanLit(True), CallStmt(Id(t17o), [NumLit(6.38)]))), (StringLit(rS), Continue)], Return(BooleanLit(True))))], Return(NumLit(59.04)), If(Id(UO), VarDecl(Id(LTYu), StringType, None, BooleanLit(False))), [(Id(u7), CallStmt(Id(B7), [NumLit(29.41), NumLit(4.77)])), (StringLit(ULMJK), CallStmt(Id(hb), [NumLit(67.76), BooleanLit(False), NumLit(21.01)]))], None]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011571))

	def test_2153011572(self):
		input = '''
func unj ()	return "X"
'''
		expect = '''Program([FuncDecl(Id(unj), [], Return(StringLit(X)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011572))

	def test_2153011573(self):
		input = '''
bool XQ7[81.17] <- PA
number tACy[35.88]
'''
		expect = '''Program([VarDecl(Id(XQ7), ArrayType([81.17], BoolType), None, Id(PA)), VarDecl(Id(tACy), ArrayType([35.88], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011573))

	def test_2153011574(self):
		input = '''
func oyZj (bool rb6w)	begin
		CL(ry, true, m2_2)
		if (false)
		if (LjMC) LV7u(27.43, true, "nWV")
		elif (false)
		T94E(v6w, false, false)
		elif ("MO")
		for qFV until true by oZFG
			EsI["lONy"] <- hgPG
		else for M5OU until "iLF" by false
			if (OyL) continue
			elif (CM)
			H7(true)
			elif (69.74) begin
			end
			elif (DGm)
			for kH until "g" by false
				return HuZC
		elif ("lUN")
		bool VRqs[67.79,35.94] <- qb
		NQ0("IHpA", "PiUz")
	end
func Hm (string Jv, number p6[89.69,46.01], bool qIm[91.22,87.03])	begin
		break
	end
func Do (number Sr, bool qAi[62.6,73.06], bool Wy[93.22])
	return
'''
		expect = '''Program([FuncDecl(Id(oyZj), [VarDecl(Id(rb6w), BoolType, None, None)], Block([CallStmt(Id(CL), [Id(ry), BooleanLit(True), Id(m2_2)]), If(BooleanLit(False), If(Id(LjMC), CallStmt(Id(LV7u), [NumLit(27.43), BooleanLit(True), StringLit(nWV)])), [(BooleanLit(False), CallStmt(Id(T94E), [Id(v6w), BooleanLit(False), BooleanLit(False)])), (StringLit(MO), For(Id(qFV), BooleanLit(True), Id(oZFG), AssignStmt(ArrayCell(Id(EsI), [StringLit(lONy)]), Id(hgPG))))], For(Id(M5OU), StringLit(iLF), BooleanLit(False), If(Id(OyL), Continue), [(Id(CM), CallStmt(Id(H7), [BooleanLit(True)])), (NumLit(69.74), Block([])), (Id(DGm), For(Id(kH), StringLit(g), BooleanLit(False), Return(Id(HuZC)))), (StringLit(lUN), VarDecl(Id(VRqs), ArrayType([67.79, 35.94], BoolType), None, Id(qb)))], None)), [], None, CallStmt(Id(NQ0), [StringLit(IHpA), StringLit(PiUz)])])), FuncDecl(Id(Hm), [VarDecl(Id(Jv), StringType, None, None), VarDecl(Id(p6), ArrayType([89.69, 46.01], NumberType), None, None), VarDecl(Id(qIm), ArrayType([91.22, 87.03], BoolType), None, None)], Block([Break])), FuncDecl(Id(Do), [VarDecl(Id(Sr), NumberType, None, None), VarDecl(Id(qAi), ArrayType([62.6, 73.06], BoolType), None, None), VarDecl(Id(Wy), ArrayType([93.22], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011574))

	def test_2153011575(self):
		input = '''
func fd ()
	return 37.71
dynamic r8u <- false
bool yrZ[94.44] <- false
'''
		expect = '''Program([FuncDecl(Id(fd), [], Return(NumLit(37.71))), VarDecl(Id(r8u), None, dynamic, BooleanLit(False)), VarDecl(Id(yrZ), ArrayType([94.44], BoolType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011575))

	def test_2153011576(self):
		input = '''
string Wo_ <- L1K
func Xl (bool zSN)
	return H_gG
func KroA (string FRFX, number aWW1[99.74,2.27,88.13])	return "sgHW"
string Zm[2.91,64.87,95.62] <- true
func Z5cW (string Vvv[51.98])
	return true
'''
		expect = '''Program([VarDecl(Id(Wo_), StringType, None, Id(L1K)), FuncDecl(Id(Xl), [VarDecl(Id(zSN), BoolType, None, None)], Return(Id(H_gG))), FuncDecl(Id(KroA), [VarDecl(Id(FRFX), StringType, None, None), VarDecl(Id(aWW1), ArrayType([99.74, 2.27, 88.13], NumberType), None, None)], Return(StringLit(sgHW))), VarDecl(Id(Zm), ArrayType([2.91, 64.87, 95.62], StringType), None, BooleanLit(True)), FuncDecl(Id(Z5cW), [VarDecl(Id(Vvv), ArrayType([51.98], StringType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011576))

	def test_2153011577(self):
		input = '''
func Seh ()	return Yp7
func kgg (string Bz, string oX)	begin
		break
	end
string Oe <- 46.67
'''
		expect = '''Program([FuncDecl(Id(Seh), [], Return(Id(Yp7))), FuncDecl(Id(kgg), [VarDecl(Id(Bz), StringType, None, None), VarDecl(Id(oX), StringType, None, None)], Block([Break])), VarDecl(Id(Oe), StringType, None, NumLit(46.67))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011577))

	def test_2153011578(self):
		input = '''
dynamic Vr9
number uQ[11.35,72.72] <- 89.27
bool jum[64.03,40.89]
dynamic Thcl <- 2.79
string Bwv
'''
		expect = '''Program([VarDecl(Id(Vr9), None, dynamic, None), VarDecl(Id(uQ), ArrayType([11.35, 72.72], NumberType), None, NumLit(89.27)), VarDecl(Id(jum), ArrayType([64.03, 40.89], BoolType), None, None), VarDecl(Id(Thcl), None, dynamic, NumLit(2.79)), VarDecl(Id(Bwv), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011578))

	def test_2153011579(self):
		input = '''
bool hHaz
number tpB <- wFv
'''
		expect = '''Program([VarDecl(Id(hHaz), BoolType, None, None), VarDecl(Id(tpB), NumberType, None, Id(wFv))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011579))

	def test_2153011580(self):
		input = '''
func Bee7 ()	return "JxXt"

'''
		expect = '''Program([FuncDecl(Id(Bee7), [], Return(StringLit(JxXt)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011580))

	def test_2153011581(self):
		input = '''
string ttC[93.46] <- false
func v0wy (string K070[10.33], string sbCk[43.71,38.26])	return

func nFb (number M8DP, number hss[8.7])	return "OKEz"

'''
		expect = '''Program([VarDecl(Id(ttC), ArrayType([93.46], StringType), None, BooleanLit(False)), FuncDecl(Id(v0wy), [VarDecl(Id(K070), ArrayType([10.33], StringType), None, None), VarDecl(Id(sbCk), ArrayType([43.71, 38.26], StringType), None, None)], Return()), FuncDecl(Id(nFb), [VarDecl(Id(M8DP), NumberType, None, None), VarDecl(Id(hss), ArrayType([8.7], NumberType), None, None)], Return(StringLit(OKEz)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011581))

	def test_2153011582(self):
		input = '''
bool si
string sgG <- "XJF"
bool uO <- M7
'''
		expect = '''Program([VarDecl(Id(si), BoolType, None, None), VarDecl(Id(sgG), StringType, None, StringLit(XJF)), VarDecl(Id(uO), BoolType, None, Id(M7))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011582))

	def test_2153011583(self):
		input = '''
func qru7 (string ayxF, string Q5_)
	begin
		for LJ until true by 65.17
			TUGe()
		begin
			begin
				return
				for IwoS until UX by false
					nKv <- 82.61
				break
			end
		end
		for YcfI until 76.49 by "ObuQ"
			return
	end

func VQz (string whxJ[1.96,22.08,64.72], bool AF[48.94,86.15], number WFS)
	begin
	end

func Dr (string Koi[89.8], bool fMIt[8.79,3.08,24.95], bool cR[81.26,28.98,14.42])
	begin
		begin
			Iq[56.73] <- "KhRD"
			return S1u
			break
		end
	end
'''
		expect = '''Program([FuncDecl(Id(qru7), [VarDecl(Id(ayxF), StringType, None, None), VarDecl(Id(Q5_), StringType, None, None)], Block([For(Id(LJ), BooleanLit(True), NumLit(65.17), CallStmt(Id(TUGe), [])), Block([Block([Return(), For(Id(IwoS), Id(UX), BooleanLit(False), AssignStmt(Id(nKv), NumLit(82.61))), Break])]), For(Id(YcfI), NumLit(76.49), StringLit(ObuQ), Return())])), FuncDecl(Id(VQz), [VarDecl(Id(whxJ), ArrayType([1.96, 22.08, 64.72], StringType), None, None), VarDecl(Id(AF), ArrayType([48.94, 86.15], BoolType), None, None), VarDecl(Id(WFS), NumberType, None, None)], Block([])), FuncDecl(Id(Dr), [VarDecl(Id(Koi), ArrayType([89.8], StringType), None, None), VarDecl(Id(fMIt), ArrayType([8.79, 3.08, 24.95], BoolType), None, None), VarDecl(Id(cR), ArrayType([81.26, 28.98, 14.42], BoolType), None, None)], Block([Block([AssignStmt(ArrayCell(Id(Iq), [NumLit(56.73)]), StringLit(KhRD)), Return(Id(S1u)), Break])]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011583))

	def test_2153011584(self):
		input = '''
func kTB (string Jol)
	return 2.17
'''
		expect = '''Program([FuncDecl(Id(kTB), [VarDecl(Id(Jol), StringType, None, None)], Return(NumLit(2.17)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011584))

	def test_2153011585(self):
		input = '''
bool P8cc[19.01,12.55,69.97]
number t5st <- 19.13
'''
		expect = '''Program([VarDecl(Id(P8cc), ArrayType([19.01, 12.55, 69.97], BoolType), None, None), VarDecl(Id(t5st), NumberType, None, NumLit(19.13))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011585))

	def test_2153011586(self):
		input = '''
func OT ()	begin
		YWNY <- true
		break
	end
string RVw4 <- "SLCc"
func BH (string LBk)	return true

'''
		expect = '''Program([FuncDecl(Id(OT), [], Block([AssignStmt(Id(YWNY), BooleanLit(True)), Break])), VarDecl(Id(RVw4), StringType, None, StringLit(SLCc)), FuncDecl(Id(BH), [VarDecl(Id(LBk), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011586))

	def test_2153011587(self):
		input = '''
string gYb[96.53]
'''
		expect = '''Program([VarDecl(Id(gYb), ArrayType([96.53], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011587))

	def test_2153011588(self):
		input = '''
func fq ()	begin
		bool ucq[9.93] <- false
		break
	end
func N6bY (number EOeY, string r8[91.36,14.4,97.66])
	begin
		break
		return
		return "VRR"
	end

func tQ (number olpE)
	return

func QzTN (number YAQQ)
	return

'''
		expect = '''Program([FuncDecl(Id(fq), [], Block([VarDecl(Id(ucq), ArrayType([9.93], BoolType), None, BooleanLit(False)), Break])), FuncDecl(Id(N6bY), [VarDecl(Id(EOeY), NumberType, None, None), VarDecl(Id(r8), ArrayType([91.36, 14.4, 97.66], StringType), None, None)], Block([Break, Return(), Return(StringLit(VRR))])), FuncDecl(Id(tQ), [VarDecl(Id(olpE), NumberType, None, None)], Return()), FuncDecl(Id(QzTN), [VarDecl(Id(YAQQ), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011588))

	def test_2153011589(self):
		input = '''
func TU (number Me[22.22])	return 29.79
number LrSC[66.03,91.61,4.93] <- "iBW"
dynamic aQdJ
number IS3[25.05,77.28,84.94] <- true
'''
		expect = '''Program([FuncDecl(Id(TU), [VarDecl(Id(Me), ArrayType([22.22], NumberType), None, None)], Return(NumLit(29.79))), VarDecl(Id(LrSC), ArrayType([66.03, 91.61, 4.93], NumberType), None, StringLit(iBW)), VarDecl(Id(aQdJ), None, dynamic, None), VarDecl(Id(IS3), ArrayType([25.05, 77.28, 84.94], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011589))

	def test_2153011590(self):
		input = '''
func MU9 (number wWr)
	begin
		for PEh5 until D8rb by 24.04
			return
		begin
			iPv9(59.92)
			i4(true, "k")
		end
	end

func VE (string zc, string UFh, number xGA[12.21])
	begin
	end
func E9l (bool vRkG[66.89,35.67,43.76])	begin
		return "QlDme"
	end
func ml1 (number ZmKK[51.15,12.32,61.65], bool If[7.68,52.5,87.16], string Oo)	begin
	end

'''
		expect = '''Program([FuncDecl(Id(MU9), [VarDecl(Id(wWr), NumberType, None, None)], Block([For(Id(PEh5), Id(D8rb), NumLit(24.04), Return()), Block([CallStmt(Id(iPv9), [NumLit(59.92)]), CallStmt(Id(i4), [BooleanLit(True), StringLit(k)])])])), FuncDecl(Id(VE), [VarDecl(Id(zc), StringType, None, None), VarDecl(Id(UFh), StringType, None, None), VarDecl(Id(xGA), ArrayType([12.21], NumberType), None, None)], Block([])), FuncDecl(Id(E9l), [VarDecl(Id(vRkG), ArrayType([66.89, 35.67, 43.76], BoolType), None, None)], Block([Return(StringLit(QlDme))])), FuncDecl(Id(ml1), [VarDecl(Id(ZmKK), ArrayType([51.15, 12.32, 61.65], NumberType), None, None), VarDecl(Id(If), ArrayType([7.68, 52.5, 87.16], BoolType), None, None), VarDecl(Id(Oo), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011590))

	def test_2153011591(self):
		input = '''
func F7of (bool MrF1[51.26])	begin
		break
		dynamic li <- "av"
	end

'''
		expect = '''Program([FuncDecl(Id(F7of), [VarDecl(Id(MrF1), ArrayType([51.26], BoolType), None, None)], Block([Break, VarDecl(Id(li), None, dynamic, StringLit(av))]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011591))

	def test_2153011592(self):
		input = '''
func hZTU (bool gh7I[33.57,9.95], number RQ[76.24])
	return "K"

bool ZEQ <- "Fgd"
var noi <- false
func BSG ()	begin
		return
		c2b <- "MNJPJ"
	end
'''
		expect = '''Program([FuncDecl(Id(hZTU), [VarDecl(Id(gh7I), ArrayType([33.57, 9.95], BoolType), None, None), VarDecl(Id(RQ), ArrayType([76.24], NumberType), None, None)], Return(StringLit(K))), VarDecl(Id(ZEQ), BoolType, None, StringLit(Fgd)), VarDecl(Id(noi), None, var, BooleanLit(False)), FuncDecl(Id(BSG), [], Block([Return(), AssignStmt(Id(c2b), StringLit(MNJPJ))]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011592))

	def test_2153011593(self):
		input = '''
number kw[33.77,59.39]
number Fae[80.53,53.24]
'''
		expect = '''Program([VarDecl(Id(kw), ArrayType([33.77, 59.39], NumberType), None, None), VarDecl(Id(Fae), ArrayType([80.53, 53.24], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 2153011593))

	def test_2153011594(self):
		input = '''
func isa ()
	begin
	end

func WloR (string wZW, number gT[9.93,89.12,41.13])
	return

func UbOx (bool bI[91.72,52.51], string rv, string Ge)
	return
func wIl ()
	return "foe"

'''
		expect = '''Program([FuncDecl(Id(isa), [], Block([])), FuncDecl(Id(WloR), [VarDecl(Id(wZW), StringType, None, None), VarDecl(Id(gT), ArrayType([9.93, 89.12, 41.13], NumberType), None, None)], Return()), FuncDecl(Id(UbOx), [VarDecl(Id(bI), ArrayType([91.72, 52.51], BoolType), None, None), VarDecl(Id(rv), StringType, None, None), VarDecl(Id(Ge), StringType, None, None)], Return()), FuncDecl(Id(wIl), [], Return(StringLit(foe)))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011594))

	def test_2153011595(self):
		input = '''
func UcFh (bool T_[10.89,17.62,65.25], bool ubS, bool fneQ)	return
func D9jy (bool o4Z)	begin
		for kD until Zbzv by 87.56
			GP("qh", false, "eGeF")
		qf5p[false] <- GyP
		for P3 until "BZrb" by "BWHL"
			r_ <- false
	end

'''
		expect = '''Program([FuncDecl(Id(UcFh), [VarDecl(Id(T_), ArrayType([10.89, 17.62, 65.25], BoolType), None, None), VarDecl(Id(ubS), BoolType, None, None), VarDecl(Id(fneQ), BoolType, None, None)], Return()), FuncDecl(Id(D9jy), [VarDecl(Id(o4Z), BoolType, None, None)], Block([For(Id(kD), Id(Zbzv), NumLit(87.56), CallStmt(Id(GP), [StringLit(qh), BooleanLit(False), StringLit(eGeF)])), AssignStmt(ArrayCell(Id(qf5p), [BooleanLit(False)]), Id(GyP)), For(Id(P3), StringLit(BZrb), StringLit(BWHL), AssignStmt(Id(r_), BooleanLit(False)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011595))

	def test_2153011596(self):
		input = '''
func i9N ()
	return

var cn <- Az
'''
		expect = '''Program([FuncDecl(Id(i9N), [], Return()), VarDecl(Id(cn), None, var, Id(Az))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011596))

	def test_2153011597(self):
		input = '''
func dSM (string Ud9)	begin
		bool CST[97.83,45.23] <- n38d
		cE(true, A26, 96.95)
		begin
			Ad1 <- m2tK
			for rf until false by pe
				for YPIs until "g" by 88.58
					for gjo until "m" by "HNul"
						if (true) number GZVM[54.66,82.08]
						elif (false)
						number PVV[79.99]
						else if (false) G_LW <- true
						elif (kFy)
						begin
						end
			for N9o until gT by false
				begin
				end
		end
	end

func zBUG (number DPi0[62.81])	return
func Z7lp ()
	return

'''
		expect = '''Program([FuncDecl(Id(dSM), [VarDecl(Id(Ud9), StringType, None, None)], Block([VarDecl(Id(CST), ArrayType([97.83, 45.23], BoolType), None, Id(n38d)), CallStmt(Id(cE), [BooleanLit(True), Id(A26), NumLit(96.95)]), Block([AssignStmt(Id(Ad1), Id(m2tK)), For(Id(rf), BooleanLit(False), Id(pe), For(Id(YPIs), StringLit(g), NumLit(88.58), For(Id(gjo), StringLit(m), StringLit(HNul), If(BooleanLit(True), VarDecl(Id(GZVM), ArrayType([54.66, 82.08], NumberType), None, None)), [(BooleanLit(False), VarDecl(Id(PVV), ArrayType([79.99], NumberType), None, None))], If(BooleanLit(False), AssignStmt(Id(G_LW), BooleanLit(True))), [(Id(kFy), Block([]))], None))), For(Id(N9o), Id(gT), BooleanLit(False), Block([]))])])), FuncDecl(Id(zBUG), [VarDecl(Id(DPi0), ArrayType([62.81], NumberType), None, None)], Return()), FuncDecl(Id(Z7lp), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011597))

	def test_2153011598(self):
		input = '''
func vEj ()	return
'''
		expect = '''Program([FuncDecl(Id(vEj), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 2153011598))

	def test_2153011599(self):
		input = '''
func XwTF ()	begin
		Tql()
		return
	end

'''
		expect = '''Program([FuncDecl(Id(XwTF), [], Block([CallStmt(Id(Tql), []), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 2153011599))
