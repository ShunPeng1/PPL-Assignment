import unittest
from TestUtils import TestAST
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
	def test_21530115000(self):
		input = '''
func w3f (bool qign[73.95,32.33,99.76], number aj0N)	begin
		for THh until - "JYyw" by "MUFBg"
			U6C["nk", SO[false, "e"], 99.71] <- ZmSu
	end

func svsN ()
	begin
		Qhl(17.51, "f", EQo)
		bool Ztg[49.12,44.51,78.27]
	end
bool ntA
number PL <- EW
func pNq ()
	return

'''
		expect = '''Program([FuncDecl(Id(w3f), [VarDecl(Id(qign), ArrayType([73.95, 32.33, 99.76], BoolType), None, None), VarDecl(Id(aj0N), NumberType, None, None)], Block([For(Id(THh), UnaryOp(-, StringLit(JYyw)), StringLit(MUFBg), AssignStmt(ArrayCell(Id(U6C), [StringLit(nk), ArrayCell(Id(SO), [BooleanLit(False), StringLit(e)]), NumLit(99.71)]), Id(ZmSu)))])), FuncDecl(Id(svsN), [], Block([CallStmt(Id(Qhl), [NumLit(17.51), StringLit(f), Id(EQo)]), VarDecl(Id(Ztg), ArrayType([49.12, 44.51, 78.27], BoolType), None, None)])), VarDecl(Id(ntA), BoolType, None, None), VarDecl(Id(PL), NumberType, None, Id(EW)), FuncDecl(Id(pNq), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115000))

	def test_21530115001(self):
		input = '''
string kIt[14.89,64.84] <- true
'''
		expect = '''Program([VarDecl(Id(kIt), ArrayType([14.89, 64.84], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115001))

	def test_21530115002(self):
		input = '''
func vm (number e4M2[14.75,66.48,72.09], string xPFi)
	return

number wF[96.04,13.5,1.51]
'''
		expect = '''Program([FuncDecl(Id(vm), [VarDecl(Id(e4M2), ArrayType([14.75, 66.48, 72.09], NumberType), None, None), VarDecl(Id(xPFi), StringType, None, None)], Return()), VarDecl(Id(wF), ArrayType([96.04, 13.5, 1.51], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115002))

	def test_21530115003(self):
		input = '''
func HUH (string rK7Z, bool uHNH[79.21])
	return C1

bool Z1x
func KG ()	return 44.4

'''
		expect = '''Program([FuncDecl(Id(HUH), [VarDecl(Id(rK7Z), StringType, None, None), VarDecl(Id(uHNH), ArrayType([79.21], BoolType), None, None)], Return(Id(C1))), VarDecl(Id(Z1x), BoolType, None, None), FuncDecl(Id(KG), [], Return(NumLit(44.4)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115003))

	def test_21530115004(self):
		input = '''
var pl <- true
string FeSR[15.86]
'''
		expect = '''Program([VarDecl(Id(pl), None, var, BooleanLit(True)), VarDecl(Id(FeSR), ArrayType([15.86], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115004))

	def test_21530115005(self):
		input = '''
func GY (string kn[44.12], number hR6)
	return
string fn <- true
var se <- Py2
bool In <- 53.03
string lE <- "r"
'''
		expect = '''Program([FuncDecl(Id(GY), [VarDecl(Id(kn), ArrayType([44.12], StringType), None, None), VarDecl(Id(hR6), NumberType, None, None)], Return()), VarDecl(Id(fn), StringType, None, BooleanLit(True)), VarDecl(Id(se), None, var, Id(Py2)), VarDecl(Id(In), BoolType, None, NumLit(53.03)), VarDecl(Id(lE), StringType, None, StringLit(r))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115005))

	def test_21530115006(self):
		input = '''
bool mTh_[75.79,13.04] <- 19.86
bool Q9
'''
		expect = '''Program([VarDecl(Id(mTh_), ArrayType([75.79, 13.04], BoolType), None, NumLit(19.86)), VarDecl(Id(Q9), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115006))

	def test_21530115007(self):
		input = '''
dynamic IYEJ <- Tbhv
func Jtt (number Jk8, string hN)
	return

bool yR[85.06,61.61,36.67]
func Ek (number qd[81.29,28.89,82.93], number gMGC[72.31,46.89], string FHe[37.71])	return

'''
		expect = '''Program([VarDecl(Id(IYEJ), None, dynamic, Id(Tbhv)), FuncDecl(Id(Jtt), [VarDecl(Id(Jk8), NumberType, None, None), VarDecl(Id(hN), StringType, None, None)], Return()), VarDecl(Id(yR), ArrayType([85.06, 61.61, 36.67], BoolType), None, None), FuncDecl(Id(Ek), [VarDecl(Id(qd), ArrayType([81.29, 28.89, 82.93], NumberType), None, None), VarDecl(Id(gMGC), ArrayType([72.31, 46.89], NumberType), None, None), VarDecl(Id(FHe), ArrayType([37.71], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115007))

	def test_21530115008(self):
		input = '''
var PCc <- 98.85
func Y6C4 (string COK)	return

'''
		expect = '''Program([VarDecl(Id(PCc), None, var, NumLit(98.85)), FuncDecl(Id(Y6C4), [VarDecl(Id(COK), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115008))

	def test_21530115009(self):
		input = '''
func rt (bool SrrX[43.8,56.38,86.23])
	return

'''
		expect = '''Program([FuncDecl(Id(rt), [VarDecl(Id(SrrX), ArrayType([43.8, 56.38, 86.23], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115009))

	def test_21530115010(self):
		input = '''
func m8a (number ylAK, bool UfJ3[6.53], bool ga[17.03,32.77,40.41])	begin
		begin
		end
	end
func KIKc ()	return "qdZL"

number AB <- false
func G9pu ()
	begin
		zZO(64.77)
	end
string z_ <- NSil
'''
		expect = '''Program([FuncDecl(Id(m8a), [VarDecl(Id(ylAK), NumberType, None, None), VarDecl(Id(UfJ3), ArrayType([6.53], BoolType), None, None), VarDecl(Id(ga), ArrayType([17.03, 32.77, 40.41], BoolType), None, None)], Block([Block([])])), FuncDecl(Id(KIKc), [], Return(StringLit(qdZL))), VarDecl(Id(AB), NumberType, None, BooleanLit(False)), FuncDecl(Id(G9pu), [], Block([CallStmt(Id(zZO), [NumLit(64.77)])])), VarDecl(Id(z_), StringType, None, Id(NSil))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115010))

	def test_21530115011(self):
		input = '''
number ZW0[67.74,3.44,24.81] <- Vp
string Rg[39.96]
dynamic l_Dt
func hX (string DM)	return "x"

'''
		expect = '''Program([VarDecl(Id(ZW0), ArrayType([67.74, 3.44, 24.81], NumberType), None, Id(Vp)), VarDecl(Id(Rg), ArrayType([39.96], StringType), None, None), VarDecl(Id(l_Dt), None, dynamic, None), FuncDecl(Id(hX), [VarDecl(Id(DM), StringType, None, None)], Return(StringLit(x)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115011))

	def test_21530115012(self):
		input = '''
string LrCv <- "X"
func C1Za (string E3, string Gc)
	return
'''
		expect = '''Program([VarDecl(Id(LrCv), StringType, None, StringLit(X)), FuncDecl(Id(C1Za), [VarDecl(Id(E3), StringType, None, None), VarDecl(Id(Gc), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115012))

	def test_21530115013(self):
		input = '''
number AGy[78.05,80.26]
dynamic iI <- false
dynamic dQs
func pRS ()	return oKuS

'''
		expect = '''Program([VarDecl(Id(AGy), ArrayType([78.05, 80.26], NumberType), None, None), VarDecl(Id(iI), None, dynamic, BooleanLit(False)), VarDecl(Id(dQs), None, dynamic, None), FuncDecl(Id(pRS), [], Return(Id(oKuS)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115013))

	def test_21530115014(self):
		input = '''
bool Yl
func hM40 (string vnd, number vGBD[71.61,38.05], bool gnF)
	begin
		Bjho(S3)
		G__(Qr)
		if ("QBT")
		return GoXb
		else for r5EB until AY by "Qz"
			if (46.18) begin
				td <- 91.31
				begin
				end
			end
			elif ("IMJUS") return
			elif ("AtjbA")
			break
			else ixBq <- 72.0
	end
func mD (number ben[20.1], string KQ[61.32,38.52])
	return

number Oc[39.35,4.87]
func EOi (bool sm[41.58,65.26])	return

'''
		expect = '''Program([VarDecl(Id(Yl), BoolType, None, None), FuncDecl(Id(hM40), [VarDecl(Id(vnd), StringType, None, None), VarDecl(Id(vGBD), ArrayType([71.61, 38.05], NumberType), None, None), VarDecl(Id(gnF), BoolType, None, None)], Block([CallStmt(Id(Bjho), [Id(S3)]), CallStmt(Id(G__), [Id(Qr)]), If((StringLit(QBT), Return(Id(GoXb))), [], For(Id(r5EB), Id(AY), StringLit(Qz), If((NumLit(46.18), Block([AssignStmt(Id(td), NumLit(91.31)), Block([])])), [(StringLit(IMJUS), Return()), (StringLit(AtjbA), Break)], AssignStmt(Id(ixBq), NumLit(72.0)))))])), FuncDecl(Id(mD), [VarDecl(Id(ben), ArrayType([20.1], NumberType), None, None), VarDecl(Id(KQ), ArrayType([61.32, 38.52], StringType), None, None)], Return()), VarDecl(Id(Oc), ArrayType([39.35, 4.87], NumberType), None, None), FuncDecl(Id(EOi), [VarDecl(Id(sm), ArrayType([41.58, 65.26], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115014))

	def test_21530115015(self):
		input = '''
bool e6[81.65,59.13,60.01]
'''
		expect = '''Program([VarDecl(Id(e6), ArrayType([81.65, 59.13, 60.01], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115015))

	def test_21530115016(self):
		input = '''
bool dA8
func N4K ()	return UL0W

func ldQt (number k0[82.9])
	begin
		YshD <- 67.82
	end
func aD ()	return
func YRu (bool u1_[2.95,51.63,74.62], bool vw[43.77,77.77])
	return

'''
		expect = '''Program([VarDecl(Id(dA8), BoolType, None, None), FuncDecl(Id(N4K), [], Return(Id(UL0W))), FuncDecl(Id(ldQt), [VarDecl(Id(k0), ArrayType([82.9], NumberType), None, None)], Block([AssignStmt(Id(YshD), NumLit(67.82))])), FuncDecl(Id(aD), [], Return()), FuncDecl(Id(YRu), [VarDecl(Id(u1_), ArrayType([2.95, 51.63, 74.62], BoolType), None, None), VarDecl(Id(vw), ArrayType([43.77, 77.77], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115016))

	def test_21530115017(self):
		input = '''
bool l0U
bool jxS_[22.21,57.28] <- "LuorU"
'''
		expect = '''Program([VarDecl(Id(l0U), BoolType, None, None), VarDecl(Id(jxS_), ArrayType([22.21, 57.28], BoolType), None, StringLit(LuorU))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115017))

	def test_21530115018(self):
		input = '''
bool HZs <- "S"
number rjJ
func Je (bool VTwy[96.46,17.1], bool O_t)	begin
	end
func Hv (bool Ph[50.48,25.75], bool qae[65.56,46.79,54.31], number Lost[67.64,48.5])	begin
		Rqh <- 82.75
		break
		break
	end

'''
		expect = '''Program([VarDecl(Id(HZs), BoolType, None, StringLit(S)), VarDecl(Id(rjJ), NumberType, None, None), FuncDecl(Id(Je), [VarDecl(Id(VTwy), ArrayType([96.46, 17.1], BoolType), None, None), VarDecl(Id(O_t), BoolType, None, None)], Block([])), FuncDecl(Id(Hv), [VarDecl(Id(Ph), ArrayType([50.48, 25.75], BoolType), None, None), VarDecl(Id(qae), ArrayType([65.56, 46.79, 54.31], BoolType), None, None), VarDecl(Id(Lost), ArrayType([67.64, 48.5], NumberType), None, None)], Block([AssignStmt(Id(Rqh), NumLit(82.75)), Break, Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115018))

	def test_21530115019(self):
		input = '''
bool G6kG
func jvvA (number hl2[83.43], bool wv, string YXz7[87.85,80.78,72.75])
	return

func upeH (bool On[7.76,2.93,17.58])	return true

func vkvU (string G2e)	return "qFK"

bool Z6 <- "RyC"
'''
		expect = '''Program([VarDecl(Id(G6kG), BoolType, None, None), FuncDecl(Id(jvvA), [VarDecl(Id(hl2), ArrayType([83.43], NumberType), None, None), VarDecl(Id(wv), BoolType, None, None), VarDecl(Id(YXz7), ArrayType([87.85, 80.78, 72.75], StringType), None, None)], Return()), FuncDecl(Id(upeH), [VarDecl(Id(On), ArrayType([7.76, 2.93, 17.58], BoolType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(vkvU), [VarDecl(Id(G2e), StringType, None, None)], Return(StringLit(qFK))), VarDecl(Id(Z6), BoolType, None, StringLit(RyC))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115019))

	def test_21530115020(self):
		input = '''
func QdS ()
	begin
	end

func J6sx (string u8dB)
	begin
		begin
			break
		end
		hJ()
	end

func BYrQ ()
	begin
		break
	end
number rr[81.5,72.73] <- fA
bool gr0
'''
		expect = '''Program([FuncDecl(Id(QdS), [], Block([])), FuncDecl(Id(J6sx), [VarDecl(Id(u8dB), StringType, None, None)], Block([Block([Break]), CallStmt(Id(hJ), [])])), FuncDecl(Id(BYrQ), [], Block([Break])), VarDecl(Id(rr), ArrayType([81.5, 72.73], NumberType), None, Id(fA)), VarDecl(Id(gr0), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115020))

	def test_21530115021(self):
		input = '''
number XZN <- false
func MXL (string olY[39.38,67.43,17.3], string vF__[45.18])	return false

func rZK8 (number Lge, bool b5z6[91.35,19.24])
	return 32.36
var JJ8 <- "px"
string iY8 <- 68.47
'''
		expect = '''Program([VarDecl(Id(XZN), NumberType, None, BooleanLit(False)), FuncDecl(Id(MXL), [VarDecl(Id(olY), ArrayType([39.38, 67.43, 17.3], StringType), None, None), VarDecl(Id(vF__), ArrayType([45.18], StringType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(rZK8), [VarDecl(Id(Lge), NumberType, None, None), VarDecl(Id(b5z6), ArrayType([91.35, 19.24], BoolType), None, None)], Return(NumLit(32.36))), VarDecl(Id(JJ8), None, var, StringLit(px)), VarDecl(Id(iY8), StringType, None, NumLit(68.47))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115021))

	def test_21530115022(self):
		input = '''
var PHoB <- "osr"
string PF
'''
		expect = '''Program([VarDecl(Id(PHoB), None, var, StringLit(osr)), VarDecl(Id(PF), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115022))

	def test_21530115023(self):
		input = '''
func nv (string jmli, string ane[58.56,77.73,1.39], number ox[42.87])	return

number cFk
number Am
'''
		expect = '''Program([FuncDecl(Id(nv), [VarDecl(Id(jmli), StringType, None, None), VarDecl(Id(ane), ArrayType([58.56, 77.73, 1.39], StringType), None, None), VarDecl(Id(ox), ArrayType([42.87], NumberType), None, None)], Return()), VarDecl(Id(cFk), NumberType, None, None), VarDecl(Id(Am), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115023))

	def test_21530115024(self):
		input = '''
func Pp (number BH[2.11,55.44,11.47])
	return

'''
		expect = '''Program([FuncDecl(Id(Pp), [VarDecl(Id(BH), ArrayType([2.11, 55.44, 11.47], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115024))

	def test_21530115025(self):
		input = '''
bool nGU0[91.57,37.25] <- 11.02
bool p7[67.01]
var RuxY <- 32.17
bool e8Rf <- 86.36
bool CSke <- "XEtcz"
'''
		expect = '''Program([VarDecl(Id(nGU0), ArrayType([91.57, 37.25], BoolType), None, NumLit(11.02)), VarDecl(Id(p7), ArrayType([67.01], BoolType), None, None), VarDecl(Id(RuxY), None, var, NumLit(32.17)), VarDecl(Id(e8Rf), BoolType, None, NumLit(86.36)), VarDecl(Id(CSke), BoolType, None, StringLit(XEtcz))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115025))

	def test_21530115026(self):
		input = '''
func TRc (string X1vY[30.22,0.88])
	return true
string X3[71.63,51.06,35.44]
'''
		expect = '''Program([FuncDecl(Id(TRc), [VarDecl(Id(X1vY), ArrayType([30.22, 0.88], StringType), None, None)], Return(BooleanLit(True))), VarDecl(Id(X3), ArrayType([71.63, 51.06, 35.44], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115026))

	def test_21530115027(self):
		input = '''
string y5me[48.19,13.13] <- 16.56
func WLX (bool GWeS[10.58,65.39,20.96])
	return LpW
'''
		expect = '''Program([VarDecl(Id(y5me), ArrayType([48.19, 13.13], StringType), None, NumLit(16.56)), FuncDecl(Id(WLX), [VarDecl(Id(GWeS), ArrayType([10.58, 65.39, 20.96], BoolType), None, None)], Return(Id(LpW)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115027))

	def test_21530115028(self):
		input = '''
string IEy[67.79,42.77]
func sBN (bool Qj5B)	begin
		continue
		return true
		continue
	end

func mM (number oC[59.93,63.14,77.28])
	return 66.96
'''
		expect = '''Program([VarDecl(Id(IEy), ArrayType([67.79, 42.77], StringType), None, None), FuncDecl(Id(sBN), [VarDecl(Id(Qj5B), BoolType, None, None)], Block([Continue, Return(BooleanLit(True)), Continue])), FuncDecl(Id(mM), [VarDecl(Id(oC), ArrayType([59.93, 63.14, 77.28], NumberType), None, None)], Return(NumLit(66.96)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115028))

	def test_21530115029(self):
		input = '''
func AYl (bool eVf[91.35], string BoGn[34.37,55.4,66.06])
	begin
		dynamic SW <- "wbzGj"
		return NXus
		bool Q9HQ
	end

string oLk[62.92,32.81,11.72]
string NKcW <- L1
func qG (number fK_)
	return "rUa"
'''
		expect = '''Program([FuncDecl(Id(AYl), [VarDecl(Id(eVf), ArrayType([91.35], BoolType), None, None), VarDecl(Id(BoGn), ArrayType([34.37, 55.4, 66.06], StringType), None, None)], Block([VarDecl(Id(SW), None, dynamic, StringLit(wbzGj)), Return(Id(NXus)), VarDecl(Id(Q9HQ), BoolType, None, None)])), VarDecl(Id(oLk), ArrayType([62.92, 32.81, 11.72], StringType), None, None), VarDecl(Id(NKcW), StringType, None, Id(L1)), FuncDecl(Id(qG), [VarDecl(Id(fK_), NumberType, None, None)], Return(StringLit(rUa)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115029))

	def test_21530115030(self):
		input = '''
func kRr (bool Li)
	begin
		if (79.92) begin
			continue
			return 64.07
		end
		elif (false) break
		elif ("POs")
		for z8 until 54.17 by 49.67
			break
		elif (false) bool yn[66.57,84.63]
		else if (klGX) return Zd70
		elif (73.8) if (rFW) begin
		end
		elif (true) lVim(nzyj, "Hl", 3.45)
		else if (true) begin
		end
		elif (Ka)
		begin
		end
		elif (false)
		hK(true, 78.71, 70.85)
		elif (false) continue
		elif (false)
		string mpmm <- uio
		elif ("vG")
		if (true) begin
			string xT[48.21,35.82,50.16] <- true
			string wl
			continue
		end
		elif (whM)
		dynamic Fl <- true
		else for dOZo until true by false
			continue
		elif (20.74) for QHqT until 79.52 by U0WM
			jfi0("YUCdN")
		elif (63.28) if (true) d2 <- "Ieqe"
		elif (ehu) begin
			rU[Vic, "Z"] <- bo5z
			continue
		end
		elif (LA) if ("CqV")
		tO91[38.18] <- false
		elif (wg1) begin
			begin
				for XxT2 until "kuR" by Wd
					for SRjG until 17.82 by false
						return
				break
			end
			continue
			break
		end
		elif (fvjh) return
		elif ("csWUZ") if (false)
		Zc()
		elif ("jzLt")
		sT57()
		elif (Bjt) if (true)
		return 4.84
		elif (4.24)
		begin
			begin
				continue
				QJs[true] <- "xkz"
				PD(pvar, false, "k")
			end
			break
		end
		elif (16.0)
		Qfci <- false
		else if ("OkDvQ")
		for vDn until true by "Wq"
			continue
		elif (false)
		begin
			string Ph[10.45,70.81] <- 66.2
			return
		end
		else return "qN"
		else begin
			break
		end
		elif (true) begin
			return
			begin
				break
			end
			continue
		end
		elif (gWY) if (false) begin
			break
			return
		end
		elif (nDO)
		begin
			for b0 until QugZ by false
				dynamic Su9 <- false
		end
		else begin
			if (b5)
			break
		end
	end

func oE1 (bool Br, string Lwj, string wnu[71.61])	begin
		m4i()
		if (58.04)
		O0()
		elif (true) if (true) if (yv2)
		return
		elif (false)
		vQ1h <- 73.78
		elif (true) VpMj(wGmO, true, "eBA")
		else string YqyU[89.53,82.4] <- sgK6
		elif (tW) OU(false, false)
		elif (false)
		dynamic uH <- true
		elif (uP)
		for RP until oGgA by "y"
			if (96.34)
			for TE until true by 49.31
				if ("sA")
				break
				elif (Pky1) begin
					begin
						ms <- "oxLvA"
						break
						break
					end
					for kk3K until true by "h"
						EF()
					continue
				end
				elif (19.81)
				return
				else break
			elif ("F") break
			elif (72.09)
			for cv until true by "pk"
				for nQj until nuw by "JjPCG"
					for ikH5 until Ud by 26.63
						for l6zI until jpmD by 23.42
							break
			else begin
			end
		else continue
		number L6r
	end

'''
		expect = '''Program([FuncDecl(Id(kRr), [VarDecl(Id(Li), BoolType, None, None)], Block([If((NumLit(79.92), Block([Continue, Return(NumLit(64.07))])), [(BooleanLit(False), Break), (StringLit(POs), For(Id(z8), NumLit(54.17), NumLit(49.67), Break)), (BooleanLit(False), VarDecl(Id(yn), ArrayType([66.57, 84.63], BoolType), None, None))], If((Id(klGX), Return(Id(Zd70))), [(NumLit(73.8), If((Id(rFW), Block([])), [(BooleanLit(True), CallStmt(Id(lVim), [Id(nzyj), StringLit(Hl), NumLit(3.45)]))], If((BooleanLit(True), Block([])), [(Id(Ka), Block([])), (BooleanLit(False), CallStmt(Id(hK), [BooleanLit(True), NumLit(78.71), NumLit(70.85)])), (BooleanLit(False), Continue), (BooleanLit(False), VarDecl(Id(mpmm), StringType, None, Id(uio))), (StringLit(vG), If((BooleanLit(True), Block([VarDecl(Id(xT), ArrayType([48.21, 35.82, 50.16], StringType), None, BooleanLit(True)), VarDecl(Id(wl), StringType, None, None), Continue])), [(Id(whM), VarDecl(Id(Fl), None, dynamic, BooleanLit(True)))], For(Id(dOZo), BooleanLit(True), BooleanLit(False), Continue))), (NumLit(20.74), For(Id(QHqT), NumLit(79.52), Id(U0WM), CallStmt(Id(jfi0), [StringLit(YUCdN)]))), (NumLit(63.28), If((BooleanLit(True), AssignStmt(Id(d2), StringLit(Ieqe))), [(Id(ehu), Block([AssignStmt(ArrayCell(Id(rU), [Id(Vic), StringLit(Z)]), Id(bo5z)), Continue])), (Id(LA), If((StringLit(CqV), AssignStmt(ArrayCell(Id(tO91), [NumLit(38.18)]), BooleanLit(False))), [(Id(wg1), Block([Block([For(Id(XxT2), StringLit(kuR), Id(Wd), For(Id(SRjG), NumLit(17.82), BooleanLit(False), Return())), Break]), Continue, Break])), (Id(fvjh), Return()), (StringLit(csWUZ), If((BooleanLit(False), CallStmt(Id(Zc), [])), [(StringLit(jzLt), CallStmt(Id(sT57), [])), (Id(Bjt), If((BooleanLit(True), Return(NumLit(4.84))), [(NumLit(4.24), Block([Block([Continue, AssignStmt(ArrayCell(Id(QJs), [BooleanLit(True)]), StringLit(xkz)), CallStmt(Id(PD), [Id(pvar), BooleanLit(False), StringLit(k)])]), Break])), (NumLit(16.0), AssignStmt(Id(Qfci), BooleanLit(False)))], If((StringLit(OkDvQ), For(Id(vDn), BooleanLit(True), StringLit(Wq), Continue)), [(BooleanLit(False), Block([VarDecl(Id(Ph), ArrayType([10.45, 70.81], StringType), None, NumLit(66.2)), Return()]))], Return(StringLit(qN)))))], Block([Break]))), (BooleanLit(True), Block([Return(), Block([Break]), Continue])), (Id(gWY), If((BooleanLit(False), Block([Break, Return()])), [(Id(nDO), Block([For(Id(b0), Id(QugZ), BooleanLit(False), VarDecl(Id(Su9), None, dynamic, BooleanLit(False)))]))], Block([If((Id(b5), Break), [], None)])))], None))], None))], None)))], None))])), FuncDecl(Id(oE1), [VarDecl(Id(Br), BoolType, None, None), VarDecl(Id(Lwj), StringType, None, None), VarDecl(Id(wnu), ArrayType([71.61], StringType), None, None)], Block([CallStmt(Id(m4i), []), If((NumLit(58.04), CallStmt(Id(O0), [])), [(BooleanLit(True), If((BooleanLit(True), If((Id(yv2), Return()), [(BooleanLit(False), AssignStmt(Id(vQ1h), NumLit(73.78))), (BooleanLit(True), CallStmt(Id(VpMj), [Id(wGmO), BooleanLit(True), StringLit(eBA)]))], VarDecl(Id(YqyU), ArrayType([89.53, 82.4], StringType), None, Id(sgK6)))), [(Id(tW), CallStmt(Id(OU), [BooleanLit(False), BooleanLit(False)])), (BooleanLit(False), VarDecl(Id(uH), None, dynamic, BooleanLit(True))), (Id(uP), For(Id(RP), Id(oGgA), StringLit(y), If((NumLit(96.34), For(Id(TE), BooleanLit(True), NumLit(49.31), If((StringLit(sA), Break), [(Id(Pky1), Block([Block([AssignStmt(Id(ms), StringLit(oxLvA)), Break, Break]), For(Id(kk3K), BooleanLit(True), StringLit(h), CallStmt(Id(EF), [])), Continue])), (NumLit(19.81), Return())], Break))), [(StringLit(F), Break), (NumLit(72.09), For(Id(cv), BooleanLit(True), StringLit(pk), For(Id(nQj), Id(nuw), StringLit(JjPCG), For(Id(ikH5), Id(Ud), NumLit(26.63), For(Id(l6zI), Id(jpmD), NumLit(23.42), Break)))))], Block([]))))], Continue))], None), VarDecl(Id(L6r), NumberType, None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115030))

	def test_21530115031(self):
		input = '''
number Hce[39.18,43.89,12.03] <- 85.26
func HAp (number q1[16.65,40.4], string oBf)
	return
func zut (string rQFI[32.46], string oQv[35.01,92.89,31.72], number JvkZ)	return Vwy
func ETc (string TB[96.99,96.14,54.09], number uC, number Ssvt[72.76])	return

bool SO <- RY
'''
		expect = '''Program([VarDecl(Id(Hce), ArrayType([39.18, 43.89, 12.03], NumberType), None, NumLit(85.26)), FuncDecl(Id(HAp), [VarDecl(Id(q1), ArrayType([16.65, 40.4], NumberType), None, None), VarDecl(Id(oBf), StringType, None, None)], Return()), FuncDecl(Id(zut), [VarDecl(Id(rQFI), ArrayType([32.46], StringType), None, None), VarDecl(Id(oQv), ArrayType([35.01, 92.89, 31.72], StringType), None, None), VarDecl(Id(JvkZ), NumberType, None, None)], Return(Id(Vwy))), FuncDecl(Id(ETc), [VarDecl(Id(TB), ArrayType([96.99, 96.14, 54.09], StringType), None, None), VarDecl(Id(uC), NumberType, None, None), VarDecl(Id(Ssvt), ArrayType([72.76], NumberType), None, None)], Return()), VarDecl(Id(SO), BoolType, None, Id(RY))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115031))

	def test_21530115032(self):
		input = '''
func maL (bool uvZ[56.14,75.47])	return
dynamic rQFB
'''
		expect = '''Program([FuncDecl(Id(maL), [VarDecl(Id(uvZ), ArrayType([56.14, 75.47], BoolType), None, None)], Return()), VarDecl(Id(rQFB), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115032))

	def test_21530115033(self):
		input = '''
func nP (number pks[39.64,74.87], bool t3[88.73,57.95], number P3)	return
number Xu <- false
dynamic jjgc <- false
func OItj (number wo[64.58])	begin
		for IL until bR4Z by false
			begin
			end
		begin
		end
	end

'''
		expect = '''Program([FuncDecl(Id(nP), [VarDecl(Id(pks), ArrayType([39.64, 74.87], NumberType), None, None), VarDecl(Id(t3), ArrayType([88.73, 57.95], BoolType), None, None), VarDecl(Id(P3), NumberType, None, None)], Return()), VarDecl(Id(Xu), NumberType, None, BooleanLit(False)), VarDecl(Id(jjgc), None, dynamic, BooleanLit(False)), FuncDecl(Id(OItj), [VarDecl(Id(wo), ArrayType([64.58], NumberType), None, None)], Block([For(Id(IL), Id(bR4Z), BooleanLit(False), Block([])), Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115033))

	def test_21530115034(self):
		input = '''
string CI[97.18,58.87] <- "mrECu"
func dH5p ()
	return 58.23

func JWyk (number f7, string cqMF[68.1], string xF_7)	begin
	end

'''
		expect = '''Program([VarDecl(Id(CI), ArrayType([97.18, 58.87], StringType), None, StringLit(mrECu)), FuncDecl(Id(dH5p), [], Return(NumLit(58.23))), FuncDecl(Id(JWyk), [VarDecl(Id(f7), NumberType, None, None), VarDecl(Id(cqMF), ArrayType([68.1], StringType), None, None), VarDecl(Id(xF_7), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115034))

	def test_21530115035(self):
		input = '''
number FOPd <- ND
string JN30 <- "JRAE"
'''
		expect = '''Program([VarDecl(Id(FOPd), NumberType, None, Id(ND)), VarDecl(Id(JN30), StringType, None, StringLit(JRAE))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115035))

	def test_21530115036(self):
		input = '''
func N1WP (number dDFz[98.01,75.04,59.95], number ruU[40.01])	return
func mM2w (bool vpyR[99.24])	begin
		Ur["VGQe", GTbE] <- ygw
		eJ(true, "Ippfr", "LsFB")
	end
'''
		expect = '''Program([FuncDecl(Id(N1WP), [VarDecl(Id(dDFz), ArrayType([98.01, 75.04, 59.95], NumberType), None, None), VarDecl(Id(ruU), ArrayType([40.01], NumberType), None, None)], Return()), FuncDecl(Id(mM2w), [VarDecl(Id(vpyR), ArrayType([99.24], BoolType), None, None)], Block([AssignStmt(ArrayCell(Id(Ur), [StringLit(VGQe), Id(GTbE)]), Id(ygw)), CallStmt(Id(eJ), [BooleanLit(True), StringLit(Ippfr), StringLit(LsFB)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115036))

	def test_21530115037(self):
		input = '''
func fT9 (string RAI9)
	begin
		begin
			dynamic svH <- false
			begin
				continue
				bool If5E
				continue
			end
		end
	end

bool X0sq <- MN2D
'''
		expect = '''Program([FuncDecl(Id(fT9), [VarDecl(Id(RAI9), StringType, None, None)], Block([Block([VarDecl(Id(svH), None, dynamic, BooleanLit(False)), Block([Continue, VarDecl(Id(If5E), BoolType, None, None), Continue])])])), VarDecl(Id(X0sq), BoolType, None, Id(MN2D))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115037))

	def test_21530115038(self):
		input = '''
func fW (string c4, string LO)
	return true
bool dDyf[48.38,35.42] <- false
number Aho <- BoI
func aRC ()
	begin
	end

bool K3v5[22.7]
'''
		expect = '''Program([FuncDecl(Id(fW), [VarDecl(Id(c4), StringType, None, None), VarDecl(Id(LO), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(dDyf), ArrayType([48.38, 35.42], BoolType), None, BooleanLit(False)), VarDecl(Id(Aho), NumberType, None, Id(BoI)), FuncDecl(Id(aRC), [], Block([])), VarDecl(Id(K3v5), ArrayType([22.7], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115038))

	def test_21530115039(self):
		input = '''
number PSr[25.42,11.45,83.43] <- "C"
func h7 (number wHB9, bool jD09)
	begin
		var zb <- 88.43
	end

number dAw
func t5 (bool YtK)
	begin
		continue
		if ("au")
		return
		elif (iiZ3)
		begin
			pUm <- ISY
			return true
			jz[true, "ozphc", Fsc] <- false
		end
		elif (true) ItIG <- 53.22
		elif (true)
		number mJjY[49.66,48.3]
		elif (21.02) eP8(Lb6)
	end
'''
		expect = '''Program([VarDecl(Id(PSr), ArrayType([25.42, 11.45, 83.43], NumberType), None, StringLit(C)), FuncDecl(Id(h7), [VarDecl(Id(wHB9), NumberType, None, None), VarDecl(Id(jD09), BoolType, None, None)], Block([VarDecl(Id(zb), None, var, NumLit(88.43))])), VarDecl(Id(dAw), NumberType, None, None), FuncDecl(Id(t5), [VarDecl(Id(YtK), BoolType, None, None)], Block([Continue, If((StringLit(au), Return()), [(Id(iiZ3), Block([AssignStmt(Id(pUm), Id(ISY)), Return(BooleanLit(True)), AssignStmt(ArrayCell(Id(jz), [BooleanLit(True), StringLit(ozphc), Id(Fsc)]), BooleanLit(False))])), (BooleanLit(True), AssignStmt(Id(ItIG), NumLit(53.22))), (BooleanLit(True), VarDecl(Id(mJjY), ArrayType([49.66, 48.3], NumberType), None, None)), (NumLit(21.02), CallStmt(Id(eP8), [Id(Lb6)]))], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115039))

	def test_21530115040(self):
		input = '''
bool bvpr <- 89.35
func OH (bool qB, bool myV[48.95,33.59,73.94], bool jE[23.32,71.17])
	return "D"
func kxwE (string b3, string fRHn[97.94], string squ[90.51])	return
dynamic ZEl <- bzf
'''
		expect = '''Program([VarDecl(Id(bvpr), BoolType, None, NumLit(89.35)), FuncDecl(Id(OH), [VarDecl(Id(qB), BoolType, None, None), VarDecl(Id(myV), ArrayType([48.95, 33.59, 73.94], BoolType), None, None), VarDecl(Id(jE), ArrayType([23.32, 71.17], BoolType), None, None)], Return(StringLit(D))), FuncDecl(Id(kxwE), [VarDecl(Id(b3), StringType, None, None), VarDecl(Id(fRHn), ArrayType([97.94], StringType), None, None), VarDecl(Id(squ), ArrayType([90.51], StringType), None, None)], Return()), VarDecl(Id(ZEl), None, dynamic, Id(bzf))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115040))

	def test_21530115041(self):
		input = '''
func ji (string qg[32.97], number M05g, string Hd)	return 51.49
dynamic P2 <- 83.39
number Xs
bool N2 <- n22
string sUoF[35.59,87.78,18.46] <- 84.49
'''
		expect = '''Program([FuncDecl(Id(ji), [VarDecl(Id(qg), ArrayType([32.97], StringType), None, None), VarDecl(Id(M05g), NumberType, None, None), VarDecl(Id(Hd), StringType, None, None)], Return(NumLit(51.49))), VarDecl(Id(P2), None, dynamic, NumLit(83.39)), VarDecl(Id(Xs), NumberType, None, None), VarDecl(Id(N2), BoolType, None, Id(n22)), VarDecl(Id(sUoF), ArrayType([35.59, 87.78, 18.46], StringType), None, NumLit(84.49))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115041))

	def test_21530115042(self):
		input = '''
bool dnOv[55.05,96.04] <- 38.19
func Wg (number oSkX[45.89,78.37], string qQr)
	begin
	end

'''
		expect = '''Program([VarDecl(Id(dnOv), ArrayType([55.05, 96.04], BoolType), None, NumLit(38.19)), FuncDecl(Id(Wg), [VarDecl(Id(oSkX), ArrayType([45.89, 78.37], NumberType), None, None), VarDecl(Id(qQr), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115042))

	def test_21530115043(self):
		input = '''
dynamic YEk <- 10.78
func is (string Y3)	return 30.22
func ORjk (bool XU6p, bool dUj)	begin
	end
'''
		expect = '''Program([VarDecl(Id(YEk), None, dynamic, NumLit(10.78)), FuncDecl(Id(is), [VarDecl(Id(Y3), StringType, None, None)], Return(NumLit(30.22))), FuncDecl(Id(ORjk), [VarDecl(Id(XU6p), BoolType, None, None), VarDecl(Id(dUj), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115043))

	def test_21530115044(self):
		input = '''
func EaqP (bool nYn_[94.45,46.12])	return

number CH[78.99] <- Z9
func BFs (string x8CV[77.7,7.63], bool yt, string VIA[83.15])
	begin
		Yi[true, 12.31, dwN] <- false
		begin
			return false
			return 62.1
			BR <- OlDP
		end
	end

bool Aq[7.99] <- MD3
number NW
'''
		expect = '''Program([FuncDecl(Id(EaqP), [VarDecl(Id(nYn_), ArrayType([94.45, 46.12], BoolType), None, None)], Return()), VarDecl(Id(CH), ArrayType([78.99], NumberType), None, Id(Z9)), FuncDecl(Id(BFs), [VarDecl(Id(x8CV), ArrayType([77.7, 7.63], StringType), None, None), VarDecl(Id(yt), BoolType, None, None), VarDecl(Id(VIA), ArrayType([83.15], StringType), None, None)], Block([AssignStmt(ArrayCell(Id(Yi), [BooleanLit(True), NumLit(12.31), Id(dwN)]), BooleanLit(False)), Block([Return(BooleanLit(False)), Return(NumLit(62.1)), AssignStmt(Id(BR), Id(OlDP))])])), VarDecl(Id(Aq), ArrayType([7.99], BoolType), None, Id(MD3)), VarDecl(Id(NW), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115044))

	def test_21530115045(self):
		input = '''
string ho[27.79,13.51] <- 60.41
string L1[71.28] <- bQX1
string k8K
string vvF8[36.07] <- "iDnK"
func vbdz (string UZ[54.54,39.17,70.42], number yur)
	return "G"
'''
		expect = '''Program([VarDecl(Id(ho), ArrayType([27.79, 13.51], StringType), None, NumLit(60.41)), VarDecl(Id(L1), ArrayType([71.28], StringType), None, Id(bQX1)), VarDecl(Id(k8K), StringType, None, None), VarDecl(Id(vvF8), ArrayType([36.07], StringType), None, StringLit(iDnK)), FuncDecl(Id(vbdz), [VarDecl(Id(UZ), ArrayType([54.54, 39.17, 70.42], StringType), None, None), VarDecl(Id(yur), NumberType, None, None)], Return(StringLit(G)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115045))

	def test_21530115046(self):
		input = '''
func T_ ()
	begin
		T7S2[23.12, false] <- YC
		begin
		end
	end
'''
		expect = '''Program([FuncDecl(Id(T_), [], Block([AssignStmt(ArrayCell(Id(T7S2), [NumLit(23.12), BooleanLit(False)]), Id(YC)), Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115046))

	def test_21530115047(self):
		input = '''
func DRwE (string WDl[40.09])	return
func itSU ()	return cs

func xBzH (number pf3n, bool Hv[96.4,79.08])	return
func TRvt ()
	return 97.05
func qTWj (number Y2, number lV[64.92,26.52,92.5])	return

'''
		expect = '''Program([FuncDecl(Id(DRwE), [VarDecl(Id(WDl), ArrayType([40.09], StringType), None, None)], Return()), FuncDecl(Id(itSU), [], Return(Id(cs))), FuncDecl(Id(xBzH), [VarDecl(Id(pf3n), NumberType, None, None), VarDecl(Id(Hv), ArrayType([96.4, 79.08], BoolType), None, None)], Return()), FuncDecl(Id(TRvt), [], Return(NumLit(97.05))), FuncDecl(Id(qTWj), [VarDecl(Id(Y2), NumberType, None, None), VarDecl(Id(lV), ArrayType([64.92, 26.52, 92.5], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115047))

	def test_21530115048(self):
		input = '''
string SfU[72.61,86.09] <- "uXd"
func PC (number STi[71.7,40.05,56.57], number M8Qy)	return 14.98
dynamic hbb
'''
		expect = '''Program([VarDecl(Id(SfU), ArrayType([72.61, 86.09], StringType), None, StringLit(uXd)), FuncDecl(Id(PC), [VarDecl(Id(STi), ArrayType([71.7, 40.05, 56.57], NumberType), None, None), VarDecl(Id(M8Qy), NumberType, None, None)], Return(NumLit(14.98))), VarDecl(Id(hbb), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115048))

	def test_21530115049(self):
		input = '''
func vZM ()
	return
bool A41H[72.48] <- UU
bool hAKQ
func zmVs (bool My, bool hswJ[32.52,2.33], bool TDQP)
	return Sfq
'''
		expect = '''Program([FuncDecl(Id(vZM), [], Return()), VarDecl(Id(A41H), ArrayType([72.48], BoolType), None, Id(UU)), VarDecl(Id(hAKQ), BoolType, None, None), FuncDecl(Id(zmVs), [VarDecl(Id(My), BoolType, None, None), VarDecl(Id(hswJ), ArrayType([32.52, 2.33], BoolType), None, None), VarDecl(Id(TDQP), BoolType, None, None)], Return(Id(Sfq)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115049))

	def test_21530115050(self):
		input = '''
func e9h (number XJ)
	return
func Jx9 ()	begin
	end
string yPym[20.62]
func sRhu (number CoBU)
	begin
	end
number Cf <- "LWutj"
'''
		expect = '''Program([FuncDecl(Id(e9h), [VarDecl(Id(XJ), NumberType, None, None)], Return()), FuncDecl(Id(Jx9), [], Block([])), VarDecl(Id(yPym), ArrayType([20.62], StringType), None, None), FuncDecl(Id(sRhu), [VarDecl(Id(CoBU), NumberType, None, None)], Block([])), VarDecl(Id(Cf), NumberType, None, StringLit(LWutj))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115050))

	def test_21530115051(self):
		input = '''
string fjNk
func F9uE (number v_[32.55], string efW, number HQ[13.98])
	return

number QV[21.19]
func frE2 (bool AEy[18.38], bool v33, string Cu[67.76])	return false

func QwG_ (string gDLs, string ALF, bool VlHZ)
	return Nf

'''
		expect = '''Program([VarDecl(Id(fjNk), StringType, None, None), FuncDecl(Id(F9uE), [VarDecl(Id(v_), ArrayType([32.55], NumberType), None, None), VarDecl(Id(efW), StringType, None, None), VarDecl(Id(HQ), ArrayType([13.98], NumberType), None, None)], Return()), VarDecl(Id(QV), ArrayType([21.19], NumberType), None, None), FuncDecl(Id(frE2), [VarDecl(Id(AEy), ArrayType([18.38], BoolType), None, None), VarDecl(Id(v33), BoolType, None, None), VarDecl(Id(Cu), ArrayType([67.76], StringType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(QwG_), [VarDecl(Id(gDLs), StringType, None, None), VarDecl(Id(ALF), StringType, None, None), VarDecl(Id(VlHZ), BoolType, None, None)], Return(Id(Nf)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115051))

	def test_21530115052(self):
		input = '''
func Rt ()	begin
		qF3(true, JMqQ, false)
		for HvJH until Bxc1 by b2p
			for paYv until true by 66.5
				begin
					if ("WHEz")
					break
					elif ("iFRIs") for e4 until rj4X by "wLc"
						if (XxfI) for VTm_ until n2nr by 13.82
							rKgU("LJF", true, "caIx")
					elif (Jn)
					z0(true, ySu4)
					elif ("uYtU") if (false) break
					elif (77.97)
					continue
					else Lkiq(false)
					yMpk[98.84, false, 76.85] <- 36.77
				end
		for Swb until "GhZ" by true
			if (rEo) continue
			elif (true) return
			elif ("Qw") break
			else for MuPt until "sB" by QO
				fx("mPhn", true)
	end

'''
		expect = '''Program([FuncDecl(Id(Rt), [], Block([CallStmt(Id(qF3), [BooleanLit(True), Id(JMqQ), BooleanLit(False)]), For(Id(HvJH), Id(Bxc1), Id(b2p), For(Id(paYv), BooleanLit(True), NumLit(66.5), Block([If((StringLit(WHEz), Break), [(StringLit(iFRIs), For(Id(e4), Id(rj4X), StringLit(wLc), If((Id(XxfI), For(Id(VTm_), Id(n2nr), NumLit(13.82), CallStmt(Id(rKgU), [StringLit(LJF), BooleanLit(True), StringLit(caIx)]))), [(Id(Jn), CallStmt(Id(z0), [BooleanLit(True), Id(ySu4)])), (StringLit(uYtU), If((BooleanLit(False), Break), [(NumLit(77.97), Continue)], CallStmt(Id(Lkiq), [BooleanLit(False)])))], None)))], None), AssignStmt(ArrayCell(Id(yMpk), [NumLit(98.84), BooleanLit(False), NumLit(76.85)]), NumLit(36.77))]))), For(Id(Swb), StringLit(GhZ), BooleanLit(True), If((Id(rEo), Continue), [(BooleanLit(True), Return()), (StringLit(Qw), Break)], For(Id(MuPt), StringLit(sB), Id(QO), CallStmt(Id(fx), [StringLit(mPhn), BooleanLit(True)]))))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115052))

	def test_21530115053(self):
		input = '''
number Am[29.0,31.21]
dynamic YOTB
func oslc (number NM, string VZN, bool D2L[30.99,79.11,89.4])
	return

func kM (string qPA2[32.21,64.32,88.49], bool kN)
	begin
		bool kwR[80.48,2.8,78.28] <- 56.79
		continue
		for C3w until go by true
			break
	end
func O3y (number UaZ[76.24,57.01])	return true

'''
		expect = '''Program([VarDecl(Id(Am), ArrayType([29.0, 31.21], NumberType), None, None), VarDecl(Id(YOTB), None, dynamic, None), FuncDecl(Id(oslc), [VarDecl(Id(NM), NumberType, None, None), VarDecl(Id(VZN), StringType, None, None), VarDecl(Id(D2L), ArrayType([30.99, 79.11, 89.4], BoolType), None, None)], Return()), FuncDecl(Id(kM), [VarDecl(Id(qPA2), ArrayType([32.21, 64.32, 88.49], StringType), None, None), VarDecl(Id(kN), BoolType, None, None)], Block([VarDecl(Id(kwR), ArrayType([80.48, 2.8, 78.28], BoolType), None, NumLit(56.79)), Continue, For(Id(C3w), Id(go), BooleanLit(True), Break)])), FuncDecl(Id(O3y), [VarDecl(Id(UaZ), ArrayType([76.24, 57.01], NumberType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115053))

	def test_21530115054(self):
		input = '''
func xME8 ()
	return

func k_ (string QD, bool i1[48.53,41.63], bool dUn[84.01,29.34,93.96])
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(xME8), [], Return()), FuncDecl(Id(k_), [VarDecl(Id(QD), StringType, None, None), VarDecl(Id(i1), ArrayType([48.53, 41.63], BoolType), None, None), VarDecl(Id(dUn), ArrayType([84.01, 29.34, 93.96], BoolType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115054))

	def test_21530115055(self):
		input = '''
string pRDo
'''
		expect = '''Program([VarDecl(Id(pRDo), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115055))

	def test_21530115056(self):
		input = '''
number U2 <- "SRt"
dynamic M9H1 <- yNf
func zI (number Ypd[5.23,68.84,94.4], bool ohWO, bool Z2Rl[52.29,85.23])
	begin
		for w_MR until 55.97 by true
			ayV[60.83, 12.94] <- 54.69
	end

string FZ <- "ge"
'''
		expect = '''Program([VarDecl(Id(U2), NumberType, None, StringLit(SRt)), VarDecl(Id(M9H1), None, dynamic, Id(yNf)), FuncDecl(Id(zI), [VarDecl(Id(Ypd), ArrayType([5.23, 68.84, 94.4], NumberType), None, None), VarDecl(Id(ohWO), BoolType, None, None), VarDecl(Id(Z2Rl), ArrayType([52.29, 85.23], BoolType), None, None)], Block([For(Id(w_MR), NumLit(55.97), BooleanLit(True), AssignStmt(ArrayCell(Id(ayV), [NumLit(60.83), NumLit(12.94)]), NumLit(54.69)))])), VarDecl(Id(FZ), StringType, None, StringLit(ge))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115056))

	def test_21530115057(self):
		input = '''
func qx ()
	begin
		dW[yRs, 49.17, 8.92] <- true
		number lKgp[46.13,43.84]
		if ("Apsey") for f2f0 until "Jfgd" by 11.87
			return
		elif (FP)
		return
		elif ("TlY")
		if ("Rri")
		VQ <- false
		elif ("LIAmw") for a7F8 until false by "R"
			break
		elif ("ibqGq")
		var PSU <- "g"
		elif ("E")
		SwbV(63.27, false)
		elif (true)
		begin
			bool fF_[27.87,67.45,46.04]
			if (false)
			bool Ux <- false
			elif (true)
			break
			elif (VZxv) continue
		end
		elif (false) return 24.47
	end

bool XsC[12.15]
bool sfRk[54.66,89.22] <- true
func XeBZ (number OBVg[28.05], bool O5I, number hFBK)	return "f"

'''
		expect = '''Program([FuncDecl(Id(qx), [], Block([AssignStmt(ArrayCell(Id(dW), [Id(yRs), NumLit(49.17), NumLit(8.92)]), BooleanLit(True)), VarDecl(Id(lKgp), ArrayType([46.13, 43.84], NumberType), None, None), If((StringLit(Apsey), For(Id(f2f0), StringLit(Jfgd), NumLit(11.87), Return())), [(Id(FP), Return()), (StringLit(TlY), If((StringLit(Rri), AssignStmt(Id(VQ), BooleanLit(False))), [(StringLit(LIAmw), For(Id(a7F8), BooleanLit(False), StringLit(R), Break)), (StringLit(ibqGq), VarDecl(Id(PSU), None, var, StringLit(g))), (StringLit(E), CallStmt(Id(SwbV), [NumLit(63.27), BooleanLit(False)])), (BooleanLit(True), Block([VarDecl(Id(fF_), ArrayType([27.87, 67.45, 46.04], BoolType), None, None), If((BooleanLit(False), VarDecl(Id(Ux), BoolType, None, BooleanLit(False))), [(BooleanLit(True), Break), (Id(VZxv), Continue)], None)])), (BooleanLit(False), Return(NumLit(24.47)))], None))], None)])), VarDecl(Id(XsC), ArrayType([12.15], BoolType), None, None), VarDecl(Id(sfRk), ArrayType([54.66, 89.22], BoolType), None, BooleanLit(True)), FuncDecl(Id(XeBZ), [VarDecl(Id(OBVg), ArrayType([28.05], NumberType), None, None), VarDecl(Id(O5I), BoolType, None, None), VarDecl(Id(hFBK), NumberType, None, None)], Return(StringLit(f)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115057))

	def test_21530115058(self):
		input = '''
func oXJA (number bMK, string Zcx)	begin
		number st
		continue
		string ST[34.92,7.54,79.35] <- 41.79
	end
'''
		expect = '''Program([FuncDecl(Id(oXJA), [VarDecl(Id(bMK), NumberType, None, None), VarDecl(Id(Zcx), StringType, None, None)], Block([VarDecl(Id(st), NumberType, None, None), Continue, VarDecl(Id(ST), ArrayType([34.92, 7.54, 79.35], StringType), None, NumLit(41.79))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115058))

	def test_21530115059(self):
		input = '''
number HOP0[43.81,64.94]
bool yUaR
string ZKM[38.46,58.37,19.39] <- OdP
func V5 (number ENEa[72.76,1.32,82.58], bool EX[1.65], string kqh6)	return 1.22

number hBw3 <- true
'''
		expect = '''Program([VarDecl(Id(HOP0), ArrayType([43.81, 64.94], NumberType), None, None), VarDecl(Id(yUaR), BoolType, None, None), VarDecl(Id(ZKM), ArrayType([38.46, 58.37, 19.39], StringType), None, Id(OdP)), FuncDecl(Id(V5), [VarDecl(Id(ENEa), ArrayType([72.76, 1.32, 82.58], NumberType), None, None), VarDecl(Id(EX), ArrayType([1.65], BoolType), None, None), VarDecl(Id(kqh6), StringType, None, None)], Return(NumLit(1.22))), VarDecl(Id(hBw3), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115059))

	def test_21530115060(self):
		input = '''
string fJ[63.2,89.54,39.22] <- 79.51
'''
		expect = '''Program([VarDecl(Id(fJ), ArrayType([63.2, 89.54, 39.22], StringType), None, NumLit(79.51))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115060))

	def test_21530115061(self):
		input = '''
string pi <- 57.61
'''
		expect = '''Program([VarDecl(Id(pi), StringType, None, NumLit(57.61))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115061))

	def test_21530115062(self):
		input = '''
string zOLu[3.07,5.61,67.36] <- "LIro"
func tIYO (number sk[56.74], string x118[90.65,34.45,59.78], bool ex)
	return
'''
		expect = '''Program([VarDecl(Id(zOLu), ArrayType([3.07, 5.61, 67.36], StringType), None, StringLit(LIro)), FuncDecl(Id(tIYO), [VarDecl(Id(sk), ArrayType([56.74], NumberType), None, None), VarDecl(Id(x118), ArrayType([90.65, 34.45, 59.78], StringType), None, None), VarDecl(Id(ex), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115062))

	def test_21530115063(self):
		input = '''
bool nn[64.86,27.53] <- "YhiL"
'''
		expect = '''Program([VarDecl(Id(nn), ArrayType([64.86, 27.53], BoolType), None, StringLit(YhiL))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115063))

	def test_21530115064(self):
		input = '''
func SG3Y (string asM[60.9,43.61,36.47])	return
func zO6N (bool PQ[86.28], number SnIR)	begin
	end
func dR ()	return

func nXA (string anV[54.44,19.38,40.29], string giAB[96.48], string os)
	return

'''
		expect = '''Program([FuncDecl(Id(SG3Y), [VarDecl(Id(asM), ArrayType([60.9, 43.61, 36.47], StringType), None, None)], Return()), FuncDecl(Id(zO6N), [VarDecl(Id(PQ), ArrayType([86.28], BoolType), None, None), VarDecl(Id(SnIR), NumberType, None, None)], Block([])), FuncDecl(Id(dR), [], Return()), FuncDecl(Id(nXA), [VarDecl(Id(anV), ArrayType([54.44, 19.38, 40.29], StringType), None, None), VarDecl(Id(giAB), ArrayType([96.48], StringType), None, None), VarDecl(Id(os), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115064))

	def test_21530115065(self):
		input = '''
dynamic qDa <- false
func IB (bool l5)	return

'''
		expect = '''Program([VarDecl(Id(qDa), None, dynamic, BooleanLit(False)), FuncDecl(Id(IB), [VarDecl(Id(l5), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115065))

	def test_21530115066(self):
		input = '''
string sDf <- Xb
bool lRrC[18.43,40.82]
string sVV[28.82,75.09]
'''
		expect = '''Program([VarDecl(Id(sDf), StringType, None, Id(Xb)), VarDecl(Id(lRrC), ArrayType([18.43, 40.82], BoolType), None, None), VarDecl(Id(sVV), ArrayType([28.82, 75.09], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115066))

	def test_21530115067(self):
		input = '''
bool GEE[33.12,4.05] <- true
string kEL[67.63,88.11]
'''
		expect = '''Program([VarDecl(Id(GEE), ArrayType([33.12, 4.05], BoolType), None, BooleanLit(True)), VarDecl(Id(kEL), ArrayType([67.63, 88.11], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115067))

	def test_21530115068(self):
		input = '''
func Juhx (string YM, string Bq)	return true

func wbFq (string Scb[37.83], bool tX[99.14,77.86,87.87])	return 31.46
bool Hj[23.48] <- "gVPq"
func lp (bool wjYI[48.08,59.14], bool Xkfn)	return "hcXa"

'''
		expect = '''Program([FuncDecl(Id(Juhx), [VarDecl(Id(YM), StringType, None, None), VarDecl(Id(Bq), StringType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(wbFq), [VarDecl(Id(Scb), ArrayType([37.83], StringType), None, None), VarDecl(Id(tX), ArrayType([99.14, 77.86, 87.87], BoolType), None, None)], Return(NumLit(31.46))), VarDecl(Id(Hj), ArrayType([23.48], BoolType), None, StringLit(gVPq)), FuncDecl(Id(lp), [VarDecl(Id(wjYI), ArrayType([48.08, 59.14], BoolType), None, None), VarDecl(Id(Xkfn), BoolType, None, None)], Return(StringLit(hcXa)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115068))

	def test_21530115069(self):
		input = '''
func EhP ()	return 60.55

func nGm (bool upF, bool n7ei, bool Ecc8[93.74,20.53])
	return
number oe <- "mnnZ"
string o8Q[43.23,46.54,66.5]
string Lbi
'''
		expect = '''Program([FuncDecl(Id(EhP), [], Return(NumLit(60.55))), FuncDecl(Id(nGm), [VarDecl(Id(upF), BoolType, None, None), VarDecl(Id(n7ei), BoolType, None, None), VarDecl(Id(Ecc8), ArrayType([93.74, 20.53], BoolType), None, None)], Return()), VarDecl(Id(oe), NumberType, None, StringLit(mnnZ)), VarDecl(Id(o8Q), ArrayType([43.23, 46.54, 66.5], StringType), None, None), VarDecl(Id(Lbi), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115069))

	def test_21530115070(self):
		input = '''
func Pb ()
	begin
		for IrS until true by "jRdBW"
			break
	end
'''
		expect = '''Program([FuncDecl(Id(Pb), [], Block([For(Id(IrS), BooleanLit(True), StringLit(jRdBW), Break)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115070))

	def test_21530115071(self):
		input = '''
number JZ
func ksWC (number tWC0[68.1])	return

bool ho <- "VTyoD"
dynamic sDNj <- 0.75
bool Y8[84.73,90.38]
'''
		expect = '''Program([VarDecl(Id(JZ), NumberType, None, None), FuncDecl(Id(ksWC), [VarDecl(Id(tWC0), ArrayType([68.1], NumberType), None, None)], Return()), VarDecl(Id(ho), BoolType, None, StringLit(VTyoD)), VarDecl(Id(sDNj), None, dynamic, NumLit(0.75)), VarDecl(Id(Y8), ArrayType([84.73, 90.38], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115071))

	def test_21530115072(self):
		input = '''
var eN <- true
number uF
'''
		expect = '''Program([VarDecl(Id(eN), None, var, BooleanLit(True)), VarDecl(Id(uF), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115072))

	def test_21530115073(self):
		input = '''
var GJv <- true
bool lfhf[83.55]
func ZuQq (bool MyjK, bool ZZEL[52.78], string NYx)	return 24.48

'''
		expect = '''Program([VarDecl(Id(GJv), None, var, BooleanLit(True)), VarDecl(Id(lfhf), ArrayType([83.55], BoolType), None, None), FuncDecl(Id(ZuQq), [VarDecl(Id(MyjK), BoolType, None, None), VarDecl(Id(ZZEL), ArrayType([52.78], BoolType), None, None), VarDecl(Id(NYx), StringType, None, None)], Return(NumLit(24.48)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115073))

	def test_21530115074(self):
		input = '''
bool G7V
number VNAD[39.52] <- 47.38
var XV <- "Nc"
'''
		expect = '''Program([VarDecl(Id(G7V), BoolType, None, None), VarDecl(Id(VNAD), ArrayType([39.52], NumberType), None, NumLit(47.38)), VarDecl(Id(XV), None, var, StringLit(Nc))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115074))

	def test_21530115075(self):
		input = '''
bool w0[12.59] <- true
'''
		expect = '''Program([VarDecl(Id(w0), ArrayType([12.59], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115075))

	def test_21530115076(self):
		input = '''
dynamic ysNW <- 41.2
var Ay <- JuF
func jj (string oqj3, string nTk[79.63], bool WYZ)
	return true

'''
		expect = '''Program([VarDecl(Id(ysNW), None, dynamic, NumLit(41.2)), VarDecl(Id(Ay), None, var, Id(JuF)), FuncDecl(Id(jj), [VarDecl(Id(oqj3), StringType, None, None), VarDecl(Id(nTk), ArrayType([79.63], StringType), None, None), VarDecl(Id(WYZ), BoolType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115076))

	def test_21530115077(self):
		input = '''
bool K0R_[79.88,74.86,25.25]
'''
		expect = '''Program([VarDecl(Id(K0R_), ArrayType([79.88, 74.86, 25.25], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115077))

	def test_21530115078(self):
		input = '''
bool IG[78.35,23.9]
number PgR
func LBDJ (number dM)	return

func ssGK ()	return

var N7 <- "Sh"
'''
		expect = '''Program([VarDecl(Id(IG), ArrayType([78.35, 23.9], BoolType), None, None), VarDecl(Id(PgR), NumberType, None, None), FuncDecl(Id(LBDJ), [VarDecl(Id(dM), NumberType, None, None)], Return()), FuncDecl(Id(ssGK), [], Return()), VarDecl(Id(N7), None, var, StringLit(Sh))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115078))

	def test_21530115079(self):
		input = '''
bool R6D
var ig6A <- true
dynamic RI_ <- 86.55
func wEET (bool xMw5, number lo[79.34,28.27], bool d6[0.3])
	return CNX
number tviL <- true
'''
		expect = '''Program([VarDecl(Id(R6D), BoolType, None, None), VarDecl(Id(ig6A), None, var, BooleanLit(True)), VarDecl(Id(RI_), None, dynamic, NumLit(86.55)), FuncDecl(Id(wEET), [VarDecl(Id(xMw5), BoolType, None, None), VarDecl(Id(lo), ArrayType([79.34, 28.27], NumberType), None, None), VarDecl(Id(d6), ArrayType([0.3], BoolType), None, None)], Return(Id(CNX))), VarDecl(Id(tviL), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115079))

	def test_21530115080(self):
		input = '''
func d8p7 (string bHGe[70.16,67.52], string Lg[90.86], number TZ)	begin
		return "inL"
		mMvF[true] <- false
	end
var KH <- true
string AU <- "FXzEU"
func wD9 ()
	return

'''
		expect = '''Program([FuncDecl(Id(d8p7), [VarDecl(Id(bHGe), ArrayType([70.16, 67.52], StringType), None, None), VarDecl(Id(Lg), ArrayType([90.86], StringType), None, None), VarDecl(Id(TZ), NumberType, None, None)], Block([Return(StringLit(inL)), AssignStmt(ArrayCell(Id(mMvF), [BooleanLit(True)]), BooleanLit(False))])), VarDecl(Id(KH), None, var, BooleanLit(True)), VarDecl(Id(AU), StringType, None, StringLit(FXzEU)), FuncDecl(Id(wD9), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115080))

	def test_21530115081(self):
		input = '''
string ncQ[64.3,4.69,22.08] <- "k"
number u8[53.84,56.96,66.26] <- "rZmI"
func cn (number X3S, string VuME, number b82[81.54,22.12,76.1])
	begin
	end
func rWSA (number OY, bool b7N[33.76])
	return

'''
		expect = '''Program([VarDecl(Id(ncQ), ArrayType([64.3, 4.69, 22.08], StringType), None, StringLit(k)), VarDecl(Id(u8), ArrayType([53.84, 56.96, 66.26], NumberType), None, StringLit(rZmI)), FuncDecl(Id(cn), [VarDecl(Id(X3S), NumberType, None, None), VarDecl(Id(VuME), StringType, None, None), VarDecl(Id(b82), ArrayType([81.54, 22.12, 76.1], NumberType), None, None)], Block([])), FuncDecl(Id(rWSA), [VarDecl(Id(OY), NumberType, None, None), VarDecl(Id(b7N), ArrayType([33.76], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115081))

	def test_21530115082(self):
		input = '''
string QL[66.3,28.24]
string y5E
func Zs5 (number NHHP)	return 75.0

'''
		expect = '''Program([VarDecl(Id(QL), ArrayType([66.3, 28.24], StringType), None, None), VarDecl(Id(y5E), StringType, None, None), FuncDecl(Id(Zs5), [VarDecl(Id(NHHP), NumberType, None, None)], Return(NumLit(75.0)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115082))

	def test_21530115083(self):
		input = '''
func t5 (string tXGR[22.91], bool naO, number cCu[25.41])	begin
	end

number rB_o[94.41] <- true
func f8Hz (bool xdW6[54.0,54.97], bool HQBb)
	return

bool oKB7
'''
		expect = '''Program([FuncDecl(Id(t5), [VarDecl(Id(tXGR), ArrayType([22.91], StringType), None, None), VarDecl(Id(naO), BoolType, None, None), VarDecl(Id(cCu), ArrayType([25.41], NumberType), None, None)], Block([])), VarDecl(Id(rB_o), ArrayType([94.41], NumberType), None, BooleanLit(True)), FuncDecl(Id(f8Hz), [VarDecl(Id(xdW6), ArrayType([54.0, 54.97], BoolType), None, None), VarDecl(Id(HQBb), BoolType, None, None)], Return()), VarDecl(Id(oKB7), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115083))

	def test_21530115084(self):
		input = '''
func NvC (bool qigY)
	return "lDanw"
bool FL[4.87] <- 86.66
func Tedj (bool TIs[95.63,6.1], string vgR3, bool RYw[4.73])	return true

bool h2MG[78.23]
func Xfo (string Dwq[25.92], bool GDB[9.66,44.06])
	return
'''
		expect = '''Program([FuncDecl(Id(NvC), [VarDecl(Id(qigY), BoolType, None, None)], Return(StringLit(lDanw))), VarDecl(Id(FL), ArrayType([4.87], BoolType), None, NumLit(86.66)), FuncDecl(Id(Tedj), [VarDecl(Id(TIs), ArrayType([95.63, 6.1], BoolType), None, None), VarDecl(Id(vgR3), StringType, None, None), VarDecl(Id(RYw), ArrayType([4.73], BoolType), None, None)], Return(BooleanLit(True))), VarDecl(Id(h2MG), ArrayType([78.23], BoolType), None, None), FuncDecl(Id(Xfo), [VarDecl(Id(Dwq), ArrayType([25.92], StringType), None, None), VarDecl(Id(GDB), ArrayType([9.66, 44.06], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115084))

	def test_21530115085(self):
		input = '''
string Iv[1.9] <- 86.06
'''
		expect = '''Program([VarDecl(Id(Iv), ArrayType([1.9], StringType), None, NumLit(86.06))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115085))

	def test_21530115086(self):
		input = '''
func vdyC (string ktj[16.12,59.55,23.39])	return "wnZDl"
func DxcF (number qXq)
	return

func MO (bool o2, string G4v)	begin
		Ch(81.74, 95.05)
		return
	end
'''
		expect = '''Program([FuncDecl(Id(vdyC), [VarDecl(Id(ktj), ArrayType([16.12, 59.55, 23.39], StringType), None, None)], Return(StringLit(wnZDl))), FuncDecl(Id(DxcF), [VarDecl(Id(qXq), NumberType, None, None)], Return()), FuncDecl(Id(MO), [VarDecl(Id(o2), BoolType, None, None), VarDecl(Id(G4v), StringType, None, None)], Block([CallStmt(Id(Ch), [NumLit(81.74), NumLit(95.05)]), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115086))

	def test_21530115087(self):
		input = '''
bool MWZl
number ac[29.36] <- Qth
func AR1c ()	return "a"
func qIcc (string p3aw, number HV)
	return

'''
		expect = '''Program([VarDecl(Id(MWZl), BoolType, None, None), VarDecl(Id(ac), ArrayType([29.36], NumberType), None, Id(Qth)), FuncDecl(Id(AR1c), [], Return(StringLit(a))), FuncDecl(Id(qIcc), [VarDecl(Id(p3aw), StringType, None, None), VarDecl(Id(HV), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115087))

	def test_21530115088(self):
		input = '''
func aGcs ()	begin
		bool x_X[65.18] <- FaQ
	end

func H9B6 (number qR, bool OWC)
	begin
		WK[false, 61.37] <- "MRHBC"
	end

'''
		expect = '''Program([FuncDecl(Id(aGcs), [], Block([VarDecl(Id(x_X), ArrayType([65.18], BoolType), None, Id(FaQ))])), FuncDecl(Id(H9B6), [VarDecl(Id(qR), NumberType, None, None), VarDecl(Id(OWC), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(WK), [BooleanLit(False), NumLit(61.37)]), StringLit(MRHBC))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115088))

	def test_21530115089(self):
		input = '''
number GmOB
func UdB (bool Mt5, bool WT6R[29.15,95.92,35.95], bool Sv1[36.95])	return

func L6f (string PP2j[94.69,50.2], string k8xs[86.78])
	return true
'''
		expect = '''Program([VarDecl(Id(GmOB), NumberType, None, None), FuncDecl(Id(UdB), [VarDecl(Id(Mt5), BoolType, None, None), VarDecl(Id(WT6R), ArrayType([29.15, 95.92, 35.95], BoolType), None, None), VarDecl(Id(Sv1), ArrayType([36.95], BoolType), None, None)], Return()), FuncDecl(Id(L6f), [VarDecl(Id(PP2j), ArrayType([94.69, 50.2], StringType), None, None), VarDecl(Id(k8xs), ArrayType([86.78], StringType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115089))

	def test_21530115090(self):
		input = '''
func cWc (number DAO, bool IrYn, bool y4l[48.26])	begin
		break
		return
	end
dynamic Uj
string pVJ[19.26,92.58]
bool lvRY
func no (string DcQ[61.33], number coRy)
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(cWc), [VarDecl(Id(DAO), NumberType, None, None), VarDecl(Id(IrYn), BoolType, None, None), VarDecl(Id(y4l), ArrayType([48.26], BoolType), None, None)], Block([Break, Return()])), VarDecl(Id(Uj), None, dynamic, None), VarDecl(Id(pVJ), ArrayType([19.26, 92.58], StringType), None, None), VarDecl(Id(lvRY), BoolType, None, None), FuncDecl(Id(no), [VarDecl(Id(DcQ), ArrayType([61.33], StringType), None, None), VarDecl(Id(coRy), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115090))

	def test_21530115091(self):
		input = '''
string heJ7[65.75,73.17]
func Xl ()
	begin
	end

string Ic1k[88.04,69.2] <- C9
func Hrw (string pp7[75.66,11.59], bool jCM, number wrv[31.38,69.81])
	return

func WRy ()
	return

'''
		expect = '''Program([VarDecl(Id(heJ7), ArrayType([65.75, 73.17], StringType), None, None), FuncDecl(Id(Xl), [], Block([])), VarDecl(Id(Ic1k), ArrayType([88.04, 69.2], StringType), None, Id(C9)), FuncDecl(Id(Hrw), [VarDecl(Id(pp7), ArrayType([75.66, 11.59], StringType), None, None), VarDecl(Id(jCM), BoolType, None, None), VarDecl(Id(wrv), ArrayType([31.38, 69.81], NumberType), None, None)], Return()), FuncDecl(Id(WRy), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115091))

	def test_21530115092(self):
		input = '''
func JgG (string uM)	begin
		begin
		end
		for trc until true by "T"
			break
	end

string qv[79.01,0.45,74.77]
dynamic smXt <- "PbMRb"
'''
		expect = '''Program([FuncDecl(Id(JgG), [VarDecl(Id(uM), StringType, None, None)], Block([Block([]), For(Id(trc), BooleanLit(True), StringLit(T), Break)])), VarDecl(Id(qv), ArrayType([79.01, 0.45, 74.77], StringType), None, None), VarDecl(Id(smXt), None, dynamic, StringLit(PbMRb))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115092))

	def test_21530115093(self):
		input = '''
func cJs ()
	return false
func Y31Z (string WTX, number oCqx, bool yJ0)	begin
		if (95.42) bYl()
		elif ("OeDT") begin
			dynamic sF <- true
			continue
			break
		end
		else number zPyE[66.0]
		pU["x"] <- "lTW"
	end

func Hn (bool wSYg[16.88,15.94,38.37], bool qT, number ZzF[69.2])
	return KvCO
var Dv <- false
func WnKT (string prF[46.29,73.48,22.53], bool pB[96.59], number og4[21.22])	return
'''
		expect = '''Program([FuncDecl(Id(cJs), [], Return(BooleanLit(False))), FuncDecl(Id(Y31Z), [VarDecl(Id(WTX), StringType, None, None), VarDecl(Id(oCqx), NumberType, None, None), VarDecl(Id(yJ0), BoolType, None, None)], Block([If((NumLit(95.42), CallStmt(Id(bYl), [])), [(StringLit(OeDT), Block([VarDecl(Id(sF), None, dynamic, BooleanLit(True)), Continue, Break]))], VarDecl(Id(zPyE), ArrayType([66.0], NumberType), None, None)), AssignStmt(ArrayCell(Id(pU), [StringLit(x)]), StringLit(lTW))])), FuncDecl(Id(Hn), [VarDecl(Id(wSYg), ArrayType([16.88, 15.94, 38.37], BoolType), None, None), VarDecl(Id(qT), BoolType, None, None), VarDecl(Id(ZzF), ArrayType([69.2], NumberType), None, None)], Return(Id(KvCO))), VarDecl(Id(Dv), None, var, BooleanLit(False)), FuncDecl(Id(WnKT), [VarDecl(Id(prF), ArrayType([46.29, 73.48, 22.53], StringType), None, None), VarDecl(Id(pB), ArrayType([96.59], BoolType), None, None), VarDecl(Id(og4), ArrayType([21.22], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115093))

	def test_21530115094(self):
		input = '''
string Pn[16.8,5.73]
func T_f2 (bool CSt6, number n1)	begin
		JQSY <- 84.7
	end

func eS (bool axd, number NGA[38.78], number Do[82.87,96.87,80.57])
	begin
		number Gg <- "oStqd"
		if (true)
		return
		elif (76.0) continue
		elif ("eLHgf")
		return 18.46
		elif ("iWvV") begin
		end
		elif ("KyGZz")
		number QWVQ
		elif (63.08)
		continue
		else TC <- WBYc
	end

bool GNun[59.81]
'''
		expect = '''Program([VarDecl(Id(Pn), ArrayType([16.8, 5.73], StringType), None, None), FuncDecl(Id(T_f2), [VarDecl(Id(CSt6), BoolType, None, None), VarDecl(Id(n1), NumberType, None, None)], Block([AssignStmt(Id(JQSY), NumLit(84.7))])), FuncDecl(Id(eS), [VarDecl(Id(axd), BoolType, None, None), VarDecl(Id(NGA), ArrayType([38.78], NumberType), None, None), VarDecl(Id(Do), ArrayType([82.87, 96.87, 80.57], NumberType), None, None)], Block([VarDecl(Id(Gg), NumberType, None, StringLit(oStqd)), If((BooleanLit(True), Return()), [(NumLit(76.0), Continue), (StringLit(eLHgf), Return(NumLit(18.46))), (StringLit(iWvV), Block([])), (StringLit(KyGZz), VarDecl(Id(QWVQ), NumberType, None, None)), (NumLit(63.08), Continue)], AssignStmt(Id(TC), Id(WBYc)))])), VarDecl(Id(GNun), ArrayType([59.81], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115094))

	def test_21530115095(self):
		input = '''
bool jIxB
dynamic xq <- "QjmZ"
bool ot[94.85,19.85,17.31] <- "I"
'''
		expect = '''Program([VarDecl(Id(jIxB), BoolType, None, None), VarDecl(Id(xq), None, dynamic, StringLit(QjmZ)), VarDecl(Id(ot), ArrayType([94.85, 19.85, 17.31], BoolType), None, StringLit(I))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115095))

	def test_21530115096(self):
		input = '''
func AYW8 (number ZcG4, bool FNQQ[76.75,56.86], string c6A4)
	return "fCB"
func KL (string za[74.27,37.89,11.79])	begin
		string ZME
	end
bool oKVG <- "gkfM"
number PX[15.52,96.34] <- "xlkg"
func iSdF (bool P0)	return

'''
		expect = '''Program([FuncDecl(Id(AYW8), [VarDecl(Id(ZcG4), NumberType, None, None), VarDecl(Id(FNQQ), ArrayType([76.75, 56.86], BoolType), None, None), VarDecl(Id(c6A4), StringType, None, None)], Return(StringLit(fCB))), FuncDecl(Id(KL), [VarDecl(Id(za), ArrayType([74.27, 37.89, 11.79], StringType), None, None)], Block([VarDecl(Id(ZME), StringType, None, None)])), VarDecl(Id(oKVG), BoolType, None, StringLit(gkfM)), VarDecl(Id(PX), ArrayType([15.52, 96.34], NumberType), None, StringLit(xlkg)), FuncDecl(Id(iSdF), [VarDecl(Id(P0), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115096))

	def test_21530115097(self):
		input = '''
func Qz (string gd, number ETmx)
	return
number YEu <- X1MD
func Ea2q (number ZAW0[99.52], bool se, number qc8W)
	begin
		for lk6 until 64.48 by false
			lI <- "axhUZ"
		continue
	end

bool j4[85.72,33.59] <- p7jv
func ni (string gv, number zOYq)	return

'''
		expect = '''Program([FuncDecl(Id(Qz), [VarDecl(Id(gd), StringType, None, None), VarDecl(Id(ETmx), NumberType, None, None)], Return()), VarDecl(Id(YEu), NumberType, None, Id(X1MD)), FuncDecl(Id(Ea2q), [VarDecl(Id(ZAW0), ArrayType([99.52], NumberType), None, None), VarDecl(Id(se), BoolType, None, None), VarDecl(Id(qc8W), NumberType, None, None)], Block([For(Id(lk6), NumLit(64.48), BooleanLit(False), AssignStmt(Id(lI), StringLit(axhUZ))), Continue])), VarDecl(Id(j4), ArrayType([85.72, 33.59], BoolType), None, Id(p7jv)), FuncDecl(Id(ni), [VarDecl(Id(gv), StringType, None, None), VarDecl(Id(zOYq), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115097))

	def test_21530115098(self):
		input = '''
func S4F ()	begin
		break
	end

func zqWA (number DX)
	return

func CNHT (string TZnj[55.72,11.5,36.66], number RdX, bool Qb4)
	return 13.69

'''
		expect = '''Program([FuncDecl(Id(S4F), [], Block([Break])), FuncDecl(Id(zqWA), [VarDecl(Id(DX), NumberType, None, None)], Return()), FuncDecl(Id(CNHT), [VarDecl(Id(TZnj), ArrayType([55.72, 11.5, 36.66], StringType), None, None), VarDecl(Id(RdX), NumberType, None, None), VarDecl(Id(Qb4), BoolType, None, None)], Return(NumLit(13.69)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115098))

	def test_21530115099(self):
		input = '''
func P3C (number ri)	return

string To4F[26.06]
func hVon (string S6k[76.16,5.38], string dUP, bool c6[60.46,96.02])	return "QdT"
'''
		expect = '''Program([FuncDecl(Id(P3C), [VarDecl(Id(ri), NumberType, None, None)], Return()), VarDecl(Id(To4F), ArrayType([26.06], StringType), None, None), FuncDecl(Id(hVon), [VarDecl(Id(S6k), ArrayType([76.16, 5.38], StringType), None, None), VarDecl(Id(dUP), StringType, None, None), VarDecl(Id(c6), ArrayType([60.46, 96.02], BoolType), None, None)], Return(StringLit(QdT)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115099))

	def test_21530115100(self):
		input = '''
bool LK <- true
dynamic zs <- true
'''
		expect = '''Program([VarDecl(Id(LK), BoolType, None, BooleanLit(True)), VarDecl(Id(zs), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115100))

	def test_21530115101(self):
		input = '''
func Uk (bool r1[68.03,94.6,82.06], bool vH[17.13,75.76,68.69])	begin
		begin
			continue
			return false
		end
		for dEKN until 52.55 by false
			return
		w3W6[30.28, 44.29, oPHc] <- 68.46
	end
'''
		expect = '''Program([FuncDecl(Id(Uk), [VarDecl(Id(r1), ArrayType([68.03, 94.6, 82.06], BoolType), None, None), VarDecl(Id(vH), ArrayType([17.13, 75.76, 68.69], BoolType), None, None)], Block([Block([Continue, Return(BooleanLit(False))]), For(Id(dEKN), NumLit(52.55), BooleanLit(False), Return()), AssignStmt(ArrayCell(Id(w3W6), [NumLit(30.28), NumLit(44.29), Id(oPHc)]), NumLit(68.46))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115101))

	def test_21530115102(self):
		input = '''
dynamic i5
'''
		expect = '''Program([VarDecl(Id(i5), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115102))

	def test_21530115103(self):
		input = '''
string rt7 <- "g"
func zR_ (string rby3[43.25,4.53,81.63])
	begin
	end
func Gq (bool KdV[14.42])
	return
'''
		expect = '''Program([VarDecl(Id(rt7), StringType, None, StringLit(g)), FuncDecl(Id(zR_), [VarDecl(Id(rby3), ArrayType([43.25, 4.53, 81.63], StringType), None, None)], Block([])), FuncDecl(Id(Gq), [VarDecl(Id(KdV), ArrayType([14.42], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115103))

	def test_21530115104(self):
		input = '''
string f3d[66.97,85.1,23.82]
func AP9f (bool Rre, number OYH_[60.0])
	return

'''
		expect = '''Program([VarDecl(Id(f3d), ArrayType([66.97, 85.1, 23.82], StringType), None, None), FuncDecl(Id(AP9f), [VarDecl(Id(Rre), BoolType, None, None), VarDecl(Id(OYH_), ArrayType([60.0], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115104))

	def test_21530115105(self):
		input = '''
func CH (string bp[81.12])	begin
		if (28.8) for J_ until Wd by OcIW
			if (83.47) qTf <- true
			elif (35.68) oB <- "VueSt"
			elif (VxN)
			for A_q until 57.52 by false
				if (Szh) lMyz <- qK
				elif ("B")
				if ("OTGm") if (p9MT)
				number qzDM[12.62]
				elif ("kA")
				begin
				end
				elif (false) lMc("a", "t")
				elif ("BSGI") CI[RLZ, false] <- 98.73
				elif ("vOwAL")
				wUc[13.86, 91.89, "UvywV"] <- "ersg"
				elif (70.87) return 44.3
				else return "rwd"
				elif (false)
				return true
				else break
				elif (false) mehR <- true
				elif (55.58) continue
				else return false
			elif (43.57)
			string mm7D
			else return
		elif (cE) for yL until UbvW by true
			continue
		elif (71.9) continue
		number IUF <- 87.4
		lI("AwpTR", "m", 69.03)
	end
func iN (bool RXyx, bool SP, number dOa)	return

func BnP (number jA[33.68,57.67,6.95])
	begin
		if (Bd)
		if (23.65) continue
		elif (true)
		begin
			y5WS <- false
			string qS[57.03,37.3,22.92]
		end
		elif (false) bYu(true, x4)
		elif (m7) begin
		end
		elif (oN)
		continue
		elif ("ahMGB") for VkI until "i" by 38.39
			return
		elif (42.48)
		if (Jp) number xtg
		elif (45.54)
		if (td7) number aV_[72.36,87.46,3.61]
		elif ("AjQc") v_ <- false
		elif (j6P)
		var T76 <- Pxw
		else uZun()
		else h5j <- w2W
		elif (false)
		continue
		elif (false)
		break
		else return false
		for uLA until EOL by uJxE
			break
		if (true)
		for Vx4x until 74.54 by 6.05
			SnO0(MLJg, true, "zl")
		elif (Kvv)
		c8V <- "tPMwg"
		elif (false)
		for Dt until 78.28 by 38.27
			V1iN[40.67, "jlLeL", "U"] <- true
		elif (51.63)
		begin
			for PF until "BVBEq" by HFGr
				continue
			if ("NNq") return
			elif (18.25)
			for Je until false by Mxc
				if (FSc)
				continue
				elif (EP) for Ym until IY1O by aS
					number WM7F[89.38]
				elif (J1D)
				if (42.48) if ("z")
				mZ4(66.58)
				elif ("cN")
				return "yx"
				elif ("EoA")
				if ("hc")
				CPtu(f12, false, false)
				elif (67.9) continue
				elif ("CkGgv")
				for bPY until "PFWU" by false
					for ou until r_Gq by "vRKc"
						uVp(false, "lYKI")
				elif ("bQ")
				QOA[81.9] <- false
				elif ("XM")
				begin
				end
				else continue
				elif (lUk) continue
				elif (true)
				jQe[true, false] <- 59.48
				elif ("OH")
				begin
					begin
						bool THq[86.55]
					end
					continue
					begin
						break
						break
						break
					end
				end
				elif ("ZR")
				number iCt[50.93,10.07] <- false
				elif (40.93) break
				elif (I64)
				break
				else if (false) if (17.41)
				break
				elif (false) break
				elif ("fT") begin
				end
			elif (RJ15)
			vGD(62.51, true)
			return 95.96
		end
		elif (3.88)
		if (hI9) return iFuC
		elif (Xx5) break
		elif (10.96) dynamic Vk7
		else string mU <- U586
		else return
	end
'''
		expect = '''Program([FuncDecl(Id(CH), [VarDecl(Id(bp), ArrayType([81.12], StringType), None, None)], Block([If((NumLit(28.8), For(Id(J_), Id(Wd), Id(OcIW), If((NumLit(83.47), AssignStmt(Id(qTf), BooleanLit(True))), [(NumLit(35.68), AssignStmt(Id(oB), StringLit(VueSt))), (Id(VxN), For(Id(A_q), NumLit(57.52), BooleanLit(False), If((Id(Szh), AssignStmt(Id(lMyz), Id(qK))), [(StringLit(B), If((StringLit(OTGm), If((Id(p9MT), VarDecl(Id(qzDM), ArrayType([12.62], NumberType), None, None)), [(StringLit(kA), Block([])), (BooleanLit(False), CallStmt(Id(lMc), [StringLit(a), StringLit(t)])), (StringLit(BSGI), AssignStmt(ArrayCell(Id(CI), [Id(RLZ), BooleanLit(False)]), NumLit(98.73))), (StringLit(vOwAL), AssignStmt(ArrayCell(Id(wUc), [NumLit(13.86), NumLit(91.89), StringLit(UvywV)]), StringLit(ersg))), (NumLit(70.87), Return(NumLit(44.3)))], Return(StringLit(rwd)))), [(BooleanLit(False), Return(BooleanLit(True)))], Break)), (BooleanLit(False), AssignStmt(Id(mehR), BooleanLit(True))), (NumLit(55.58), Continue)], Return(BooleanLit(False))))), (NumLit(43.57), VarDecl(Id(mm7D), StringType, None, None))], Return()))), [(Id(cE), For(Id(yL), Id(UbvW), BooleanLit(True), Continue)), (NumLit(71.9), Continue)], None), VarDecl(Id(IUF), NumberType, None, NumLit(87.4)), CallStmt(Id(lI), [StringLit(AwpTR), StringLit(m), NumLit(69.03)])])), FuncDecl(Id(iN), [VarDecl(Id(RXyx), BoolType, None, None), VarDecl(Id(SP), BoolType, None, None), VarDecl(Id(dOa), NumberType, None, None)], Return()), FuncDecl(Id(BnP), [VarDecl(Id(jA), ArrayType([33.68, 57.67, 6.95], NumberType), None, None)], Block([If((Id(Bd), If((NumLit(23.65), Continue), [(BooleanLit(True), Block([AssignStmt(Id(y5WS), BooleanLit(False)), VarDecl(Id(qS), ArrayType([57.03, 37.3, 22.92], StringType), None, None)])), (BooleanLit(False), CallStmt(Id(bYu), [BooleanLit(True), Id(x4)])), (Id(m7), Block([])), (Id(oN), Continue), (StringLit(ahMGB), For(Id(VkI), StringLit(i), NumLit(38.39), Return())), (NumLit(42.48), If((Id(Jp), VarDecl(Id(xtg), NumberType, None, None)), [(NumLit(45.54), If((Id(td7), VarDecl(Id(aV_), ArrayType([72.36, 87.46, 3.61], NumberType), None, None)), [(StringLit(AjQc), AssignStmt(Id(v_), BooleanLit(False))), (Id(j6P), VarDecl(Id(T76), None, var, Id(Pxw)))], CallStmt(Id(uZun), [])))], AssignStmt(Id(h5j), Id(w2W)))), (BooleanLit(False), Continue), (BooleanLit(False), Break)], Return(BooleanLit(False)))), [], None), For(Id(uLA), Id(EOL), Id(uJxE), Break), If((BooleanLit(True), For(Id(Vx4x), NumLit(74.54), NumLit(6.05), CallStmt(Id(SnO0), [Id(MLJg), BooleanLit(True), StringLit(zl)]))), [(Id(Kvv), AssignStmt(Id(c8V), StringLit(tPMwg))), (BooleanLit(False), For(Id(Dt), NumLit(78.28), NumLit(38.27), AssignStmt(ArrayCell(Id(V1iN), [NumLit(40.67), StringLit(jlLeL), StringLit(U)]), BooleanLit(True)))), (NumLit(51.63), Block([For(Id(PF), StringLit(BVBEq), Id(HFGr), Continue), If((StringLit(NNq), Return()), [(NumLit(18.25), For(Id(Je), BooleanLit(False), Id(Mxc), If((Id(FSc), Continue), [(Id(EP), For(Id(Ym), Id(IY1O), Id(aS), VarDecl(Id(WM7F), ArrayType([89.38], NumberType), None, None))), (Id(J1D), If((NumLit(42.48), If((StringLit(z), CallStmt(Id(mZ4), [NumLit(66.58)])), [(StringLit(cN), Return(StringLit(yx))), (StringLit(EoA), If((StringLit(hc), CallStmt(Id(CPtu), [Id(f12), BooleanLit(False), BooleanLit(False)])), [(NumLit(67.9), Continue), (StringLit(CkGgv), For(Id(bPY), StringLit(PFWU), BooleanLit(False), For(Id(ou), Id(r_Gq), StringLit(vRKc), CallStmt(Id(uVp), [BooleanLit(False), StringLit(lYKI)])))), (StringLit(bQ), AssignStmt(ArrayCell(Id(QOA), [NumLit(81.9)]), BooleanLit(False))), (StringLit(XM), Block([]))], Continue)), (Id(lUk), Continue), (BooleanLit(True), AssignStmt(ArrayCell(Id(jQe), [BooleanLit(True), BooleanLit(False)]), NumLit(59.48))), (StringLit(OH), Block([Block([VarDecl(Id(THq), ArrayType([86.55], BoolType), None, None)]), Continue, Block([Break, Break, Break])])), (StringLit(ZR), VarDecl(Id(iCt), ArrayType([50.93, 10.07], NumberType), None, BooleanLit(False))), (NumLit(40.93), Break), (Id(I64), Break)], If((BooleanLit(False), If((NumLit(17.41), Break), [(BooleanLit(False), Break), (StringLit(fT), Block([])), (Id(RJ15), CallStmt(Id(vGD), [NumLit(62.51), BooleanLit(True)]))], None)), [], None))), [], None))], None)))], None), Return(NumLit(95.96))])), (NumLit(3.88), If((Id(hI9), Return(Id(iFuC))), [(Id(Xx5), Break), (NumLit(10.96), VarDecl(Id(Vk7), None, dynamic, None))], VarDecl(Id(mU), StringType, None, Id(U586))))], Return())]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115105))

	def test_21530115106(self):
		input = '''
var Bsz <- 29.36
func nmO (number Wn)
	return A93
func qUVN (string MIW[46.06])
	return true
func eG2 (number BjUt, bool bnA4, number AZCR)
	return
bool w7h <- "Tlc"
'''
		expect = '''Program([VarDecl(Id(Bsz), None, var, NumLit(29.36)), FuncDecl(Id(nmO), [VarDecl(Id(Wn), NumberType, None, None)], Return(Id(A93))), FuncDecl(Id(qUVN), [VarDecl(Id(MIW), ArrayType([46.06], StringType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(eG2), [VarDecl(Id(BjUt), NumberType, None, None), VarDecl(Id(bnA4), BoolType, None, None), VarDecl(Id(AZCR), NumberType, None, None)], Return()), VarDecl(Id(w7h), BoolType, None, StringLit(Tlc))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115106))

	def test_21530115107(self):
		input = '''
func H2W (number aNZ9[51.47], number Gf[38.65,25.69,76.62])	begin
		Vv0["U", "j"] <- IkZj
		I4("KYN", false, pFP)
	end
func dg (string EW[71.58,90.6], string qKN, number L9Cr[73.95])	return

func R8v ()	return ckm

string hHZ
'''
		expect = '''Program([FuncDecl(Id(H2W), [VarDecl(Id(aNZ9), ArrayType([51.47], NumberType), None, None), VarDecl(Id(Gf), ArrayType([38.65, 25.69, 76.62], NumberType), None, None)], Block([AssignStmt(ArrayCell(Id(Vv0), [StringLit(U), StringLit(j)]), Id(IkZj)), CallStmt(Id(I4), [StringLit(KYN), BooleanLit(False), Id(pFP)])])), FuncDecl(Id(dg), [VarDecl(Id(EW), ArrayType([71.58, 90.6], StringType), None, None), VarDecl(Id(qKN), StringType, None, None), VarDecl(Id(L9Cr), ArrayType([73.95], NumberType), None, None)], Return()), FuncDecl(Id(R8v), [], Return(Id(ckm))), VarDecl(Id(hHZ), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115107))

	def test_21530115108(self):
		input = '''
func pPMH (number Pl)
	return 73.86

func Q3z (string sUHI[52.78], string eOq[82.89,85.23])
	begin
		for AT9F until uBF by "Kb"
			begin
				break
			end
		break
		return
	end

'''
		expect = '''Program([FuncDecl(Id(pPMH), [VarDecl(Id(Pl), NumberType, None, None)], Return(NumLit(73.86))), FuncDecl(Id(Q3z), [VarDecl(Id(sUHI), ArrayType([52.78], StringType), None, None), VarDecl(Id(eOq), ArrayType([82.89, 85.23], StringType), None, None)], Block([For(Id(AT9F), Id(uBF), StringLit(Kb), Block([Break])), Break, Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115108))

	def test_21530115109(self):
		input = '''
string iR
var Fl <- false
'''
		expect = '''Program([VarDecl(Id(iR), StringType, None, None), VarDecl(Id(Fl), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115109))

	def test_21530115110(self):
		input = '''
func z1qD (bool s04V)
	begin
		Ed()
	end
func lYCz (bool V28Y)
	begin
		continue
		return u4wr
		begin
			begin
				begin
					begin
						string fn[89.85,79.03,96.31] <- Pk
						for fd until yc_ by "hPWQJ"
							continue
						if (true)
						if (true)
						break
						elif (true)
						return "qS"
						elif (Oy)
						var ydle <- "NTu"
						elif ("cCElA") continue
						elif (false)
						tA[false, hwvK, 30.05] <- "K"
						else continue
						elif ("Bbw") return 76.08
						elif (false) AM(false)
					end
				end
				continue
			end
		end
	end
string hwgu <- "WO"
func WVNK ()
	begin
	end
func XD ()
	return 29.56
'''
		expect = '''Program([FuncDecl(Id(z1qD), [VarDecl(Id(s04V), BoolType, None, None)], Block([CallStmt(Id(Ed), [])])), FuncDecl(Id(lYCz), [VarDecl(Id(V28Y), BoolType, None, None)], Block([Continue, Return(Id(u4wr)), Block([Block([Block([Block([VarDecl(Id(fn), ArrayType([89.85, 79.03, 96.31], StringType), None, Id(Pk)), For(Id(fd), Id(yc_), StringLit(hPWQJ), Continue), If((BooleanLit(True), If((BooleanLit(True), Break), [(BooleanLit(True), Return(StringLit(qS))), (Id(Oy), VarDecl(Id(ydle), None, var, StringLit(NTu))), (StringLit(cCElA), Continue), (BooleanLit(False), AssignStmt(ArrayCell(Id(tA), [BooleanLit(False), Id(hwvK), NumLit(30.05)]), StringLit(K)))], Continue)), [(StringLit(Bbw), Return(NumLit(76.08))), (BooleanLit(False), CallStmt(Id(AM), [BooleanLit(False)]))], None)])]), Continue])])])), VarDecl(Id(hwgu), StringType, None, StringLit(WO)), FuncDecl(Id(WVNK), [], Block([])), FuncDecl(Id(XD), [], Return(NumLit(29.56)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115110))

	def test_21530115111(self):
		input = '''
func of7 (number H3[85.83,69.89,83.79], number sUU[37.09], bool LS[26.65])	return L1

func lS ()	begin
		LEy8[true] <- false
		number I27[95.38] <- VcG
	end

func ajot (bool i7G, number pgr[97.71])
	begin
		for TzF until 50.98 by false
			return
	end

func niIG (string f0Cl)	return

func Y5j ()	return gZw

'''
		expect = '''Program([FuncDecl(Id(of7), [VarDecl(Id(H3), ArrayType([85.83, 69.89, 83.79], NumberType), None, None), VarDecl(Id(sUU), ArrayType([37.09], NumberType), None, None), VarDecl(Id(LS), ArrayType([26.65], BoolType), None, None)], Return(Id(L1))), FuncDecl(Id(lS), [], Block([AssignStmt(ArrayCell(Id(LEy8), [BooleanLit(True)]), BooleanLit(False)), VarDecl(Id(I27), ArrayType([95.38], NumberType), None, Id(VcG))])), FuncDecl(Id(ajot), [VarDecl(Id(i7G), BoolType, None, None), VarDecl(Id(pgr), ArrayType([97.71], NumberType), None, None)], Block([For(Id(TzF), NumLit(50.98), BooleanLit(False), Return())])), FuncDecl(Id(niIG), [VarDecl(Id(f0Cl), StringType, None, None)], Return()), FuncDecl(Id(Y5j), [], Return(Id(gZw)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115111))

	def test_21530115112(self):
		input = '''
number FFPK
dynamic JhRv <- true
'''
		expect = '''Program([VarDecl(Id(FFPK), NumberType, None, None), VarDecl(Id(JhRv), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115112))

	def test_21530115113(self):
		input = '''
var Jux4 <- d53Q
func BDe (string AmzL[24.39,81.62], string fXH[62.91,20.97])
	begin
	end

func UhA (bool q52)
	return

'''
		expect = '''Program([VarDecl(Id(Jux4), None, var, Id(d53Q)), FuncDecl(Id(BDe), [VarDecl(Id(AmzL), ArrayType([24.39, 81.62], StringType), None, None), VarDecl(Id(fXH), ArrayType([62.91, 20.97], StringType), None, None)], Block([])), FuncDecl(Id(UhA), [VarDecl(Id(q52), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115113))

	def test_21530115114(self):
		input = '''
bool Ql <- true
func YQ7x (bool WK[54.4,53.84,22.4])	return

'''
		expect = '''Program([VarDecl(Id(Ql), BoolType, None, BooleanLit(True)), FuncDecl(Id(YQ7x), [VarDecl(Id(WK), ArrayType([54.4, 53.84, 22.4], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115114))

	def test_21530115115(self):
		input = '''
bool tUnb[80.23,81.57]
string Qavm <- false
func gF7 (string jLb[57.29], number tgR[70.24,34.31], number uOfz[49.83,9.78])	return
'''
		expect = '''Program([VarDecl(Id(tUnb), ArrayType([80.23, 81.57], BoolType), None, None), VarDecl(Id(Qavm), StringType, None, BooleanLit(False)), FuncDecl(Id(gF7), [VarDecl(Id(jLb), ArrayType([57.29], StringType), None, None), VarDecl(Id(tgR), ArrayType([70.24, 34.31], NumberType), None, None), VarDecl(Id(uOfz), ArrayType([49.83, 9.78], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115115))

	def test_21530115116(self):
		input = '''
dynamic mR
func IZn9 (bool Qaml[45.79], string sn[50.34,9.16,78.81], number DwR[65.18])	begin
		string fIz[53.32] <- false
		return "Qqd"
	end
'''
		expect = '''Program([VarDecl(Id(mR), None, dynamic, None), FuncDecl(Id(IZn9), [VarDecl(Id(Qaml), ArrayType([45.79], BoolType), None, None), VarDecl(Id(sn), ArrayType([50.34, 9.16, 78.81], StringType), None, None), VarDecl(Id(DwR), ArrayType([65.18], NumberType), None, None)], Block([VarDecl(Id(fIz), ArrayType([53.32], StringType), None, BooleanLit(False)), Return(StringLit(Qqd))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115116))

	def test_21530115117(self):
		input = '''
dynamic h_8I <- D8G5
'''
		expect = '''Program([VarDecl(Id(h_8I), None, dynamic, Id(D8G5))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115117))

	def test_21530115118(self):
		input = '''
var Ij <- 71.64
var fT <- 26.54
'''
		expect = '''Program([VarDecl(Id(Ij), None, var, NumLit(71.64)), VarDecl(Id(fT), None, var, NumLit(26.54))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115118))

	def test_21530115119(self):
		input = '''
func msFm (number mx, bool dV[71.14])
	begin
		for HeG until VwM by "L"
			break
	end

func fRO (bool w5ac[68.67,67.85], number c5Ue[39.76])	begin
		rsw <- true
		IJL(false, true)
		BB7(false, 16.14)
	end
number FR[95.51,35.41,95.16] <- l0
dynamic Z8zl <- 16.0
func xp (string oz, bool TcbT[82.76,12.15])
	return
'''
		expect = '''Program([FuncDecl(Id(msFm), [VarDecl(Id(mx), NumberType, None, None), VarDecl(Id(dV), ArrayType([71.14], BoolType), None, None)], Block([For(Id(HeG), Id(VwM), StringLit(L), Break)])), FuncDecl(Id(fRO), [VarDecl(Id(w5ac), ArrayType([68.67, 67.85], BoolType), None, None), VarDecl(Id(c5Ue), ArrayType([39.76], NumberType), None, None)], Block([AssignStmt(Id(rsw), BooleanLit(True)), CallStmt(Id(IJL), [BooleanLit(False), BooleanLit(True)]), CallStmt(Id(BB7), [BooleanLit(False), NumLit(16.14)])])), VarDecl(Id(FR), ArrayType([95.51, 35.41, 95.16], NumberType), None, Id(l0)), VarDecl(Id(Z8zl), None, dynamic, NumLit(16.0)), FuncDecl(Id(xp), [VarDecl(Id(oz), StringType, None, None), VarDecl(Id(TcbT), ArrayType([82.76, 12.15], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115119))

	def test_21530115120(self):
		input = '''
string BRe[14.52,87.06]
number izDQ[10.4,76.03]
string R9[94.16] <- true
func TF (number BBm[40.61,81.61,52.57], bool lU[37.52])	begin
		eTZj <- false
		vXaU()
	end

func TmVj (bool vao[27.43,56.03,8.23])	return
'''
		expect = '''Program([VarDecl(Id(BRe), ArrayType([14.52, 87.06], StringType), None, None), VarDecl(Id(izDQ), ArrayType([10.4, 76.03], NumberType), None, None), VarDecl(Id(R9), ArrayType([94.16], StringType), None, BooleanLit(True)), FuncDecl(Id(TF), [VarDecl(Id(BBm), ArrayType([40.61, 81.61, 52.57], NumberType), None, None), VarDecl(Id(lU), ArrayType([37.52], BoolType), None, None)], Block([AssignStmt(Id(eTZj), BooleanLit(False)), CallStmt(Id(vXaU), [])])), FuncDecl(Id(TmVj), [VarDecl(Id(vao), ArrayType([27.43, 56.03, 8.23], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115120))

	def test_21530115121(self):
		input = '''
func zW (number cq2H, string p7)	return
dynamic htCU
number hb <- 90.28
func F3 (bool gz[47.18])	return
'''
		expect = '''Program([FuncDecl(Id(zW), [VarDecl(Id(cq2H), NumberType, None, None), VarDecl(Id(p7), StringType, None, None)], Return()), VarDecl(Id(htCU), None, dynamic, None), VarDecl(Id(hb), NumberType, None, NumLit(90.28)), FuncDecl(Id(F3), [VarDecl(Id(gz), ArrayType([47.18], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115121))

	def test_21530115122(self):
		input = '''
var qtE <- false
func HAg (string Ay[76.05,34.69], string nr, number DcRE)
	return 55.27

func CeOk (number GEA, string wua)	return false
'''
		expect = '''Program([VarDecl(Id(qtE), None, var, BooleanLit(False)), FuncDecl(Id(HAg), [VarDecl(Id(Ay), ArrayType([76.05, 34.69], StringType), None, None), VarDecl(Id(nr), StringType, None, None), VarDecl(Id(DcRE), NumberType, None, None)], Return(NumLit(55.27))), FuncDecl(Id(CeOk), [VarDecl(Id(GEA), NumberType, None, None), VarDecl(Id(wua), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115122))

	def test_21530115123(self):
		input = '''
string e0
func kL (string fCk, string w9FB)
	return false

'''
		expect = '''Program([VarDecl(Id(e0), StringType, None, None), FuncDecl(Id(kL), [VarDecl(Id(fCk), StringType, None, None), VarDecl(Id(w9FB), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115123))

	def test_21530115124(self):
		input = '''
func Xgva ()
	return
string UMX
'''
		expect = '''Program([FuncDecl(Id(Xgva), [], Return()), VarDecl(Id(UMX), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115124))

	def test_21530115125(self):
		input = '''
string aIo <- OvT
string PU <- "BiRi"
func XQ (string NfTn[12.05], number O7wh, bool NB[5.15])	begin
		if ("QL") break
		break
		begin
			return
			for auO until 11.5 by 20.39
				for fjG until p1t by "UjHQ"
					rze <- false
			break
		end
	end
func hFZ0 ()
	return "d"

number CRuU[70.95,4.83,29.16] <- "lr"
'''
		expect = '''Program([VarDecl(Id(aIo), StringType, None, Id(OvT)), VarDecl(Id(PU), StringType, None, StringLit(BiRi)), FuncDecl(Id(XQ), [VarDecl(Id(NfTn), ArrayType([12.05], StringType), None, None), VarDecl(Id(O7wh), NumberType, None, None), VarDecl(Id(NB), ArrayType([5.15], BoolType), None, None)], Block([If((StringLit(QL), Break), [], None), Break, Block([Return(), For(Id(auO), NumLit(11.5), NumLit(20.39), For(Id(fjG), Id(p1t), StringLit(UjHQ), AssignStmt(Id(rze), BooleanLit(False)))), Break])])), FuncDecl(Id(hFZ0), [], Return(StringLit(d))), VarDecl(Id(CRuU), ArrayType([70.95, 4.83, 29.16], NumberType), None, StringLit(lr))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115125))

	def test_21530115126(self):
		input = '''
func hOP (string vZN, bool gql)
	return false
'''
		expect = '''Program([FuncDecl(Id(hOP), [VarDecl(Id(vZN), StringType, None, None), VarDecl(Id(gql), BoolType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115126))

	def test_21530115127(self):
		input = '''
string TRy
number gxz[82.75,97.29,15.13]
'''
		expect = '''Program([VarDecl(Id(TRy), StringType, None, None), VarDecl(Id(gxz), ArrayType([82.75, 97.29, 15.13], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115127))

	def test_21530115128(self):
		input = '''
func hYJ (bool OBtL[45.81,95.61,22.22], number wfnG)	return
func PKM (bool BzuX[5.69,75.64,78.38], number sK, number sQQ[63.54,29.46])	return 56.85

'''
		expect = '''Program([FuncDecl(Id(hYJ), [VarDecl(Id(OBtL), ArrayType([45.81, 95.61, 22.22], BoolType), None, None), VarDecl(Id(wfnG), NumberType, None, None)], Return()), FuncDecl(Id(PKM), [VarDecl(Id(BzuX), ArrayType([5.69, 75.64, 78.38], BoolType), None, None), VarDecl(Id(sK), NumberType, None, None), VarDecl(Id(sQQ), ArrayType([63.54, 29.46], NumberType), None, None)], Return(NumLit(56.85)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115128))

	def test_21530115129(self):
		input = '''
var LvWv <- YL1e
func ZhEi ()
	begin
		for MJ until "QwpvL" by "uWH"
			break
		if (YaM)
		for vd until "Su" by "iOjBN"
			return false
		elif (39.84) continue
		else return true
	end
func D_g2 (number vzA)	return "CrxZO"
dynamic ph <- "vKx"
'''
		expect = '''Program([VarDecl(Id(LvWv), None, var, Id(YL1e)), FuncDecl(Id(ZhEi), [], Block([For(Id(MJ), StringLit(QwpvL), StringLit(uWH), Break), If((Id(YaM), For(Id(vd), StringLit(Su), StringLit(iOjBN), Return(BooleanLit(False)))), [(NumLit(39.84), Continue)], Return(BooleanLit(True)))])), FuncDecl(Id(D_g2), [VarDecl(Id(vzA), NumberType, None, None)], Return(StringLit(CrxZO))), VarDecl(Id(ph), None, dynamic, StringLit(vKx))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115129))

	def test_21530115130(self):
		input = '''
func Sk (bool SK[94.04,79.37])	return

func iKte (number EQXf[10.59,83.55])	return "PBaU"

dynamic Vq
func Sv (string Bf)	return wF
'''
		expect = '''Program([FuncDecl(Id(Sk), [VarDecl(Id(SK), ArrayType([94.04, 79.37], BoolType), None, None)], Return()), FuncDecl(Id(iKte), [VarDecl(Id(EQXf), ArrayType([10.59, 83.55], NumberType), None, None)], Return(StringLit(PBaU))), VarDecl(Id(Vq), None, dynamic, None), FuncDecl(Id(Sv), [VarDecl(Id(Bf), StringType, None, None)], Return(Id(wF)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115130))

	def test_21530115131(self):
		input = '''
func j2XX (bool FG, bool k4[53.31])	return
func B5M ()
	return

'''
		expect = '''Program([FuncDecl(Id(j2XX), [VarDecl(Id(FG), BoolType, None, None), VarDecl(Id(k4), ArrayType([53.31], BoolType), None, None)], Return()), FuncDecl(Id(B5M), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115131))

	def test_21530115132(self):
		input = '''
string PnW1
number qav[33.87,12.28] <- 39.3
number z9 <- "Ed"
string pa[20.61] <- "wWrul"
'''
		expect = '''Program([VarDecl(Id(PnW1), StringType, None, None), VarDecl(Id(qav), ArrayType([33.87, 12.28], NumberType), None, NumLit(39.3)), VarDecl(Id(z9), NumberType, None, StringLit(Ed)), VarDecl(Id(pa), ArrayType([20.61], StringType), None, StringLit(wWrul))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115132))

	def test_21530115133(self):
		input = '''
string FLCs <- true
func Y1mO (bool tsV, number vBj[6.78,3.87])	begin
		begin
			return Sw7
		end
		break
	end

'''
		expect = '''Program([VarDecl(Id(FLCs), StringType, None, BooleanLit(True)), FuncDecl(Id(Y1mO), [VarDecl(Id(tsV), BoolType, None, None), VarDecl(Id(vBj), ArrayType([6.78, 3.87], NumberType), None, None)], Block([Block([Return(Id(Sw7))]), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115133))

	def test_21530115134(self):
		input = '''
func Mm (number rNV, number xNa[61.37,48.56,25.59])
	return I9r
func JUkk (number yVQ, string cj_o[82.89,93.72,78.06])
	return true
dynamic XJ0q
bool ul[55.78]
string Av[78.08,90.21] <- 96.32
'''
		expect = '''Program([FuncDecl(Id(Mm), [VarDecl(Id(rNV), NumberType, None, None), VarDecl(Id(xNa), ArrayType([61.37, 48.56, 25.59], NumberType), None, None)], Return(Id(I9r))), FuncDecl(Id(JUkk), [VarDecl(Id(yVQ), NumberType, None, None), VarDecl(Id(cj_o), ArrayType([82.89, 93.72, 78.06], StringType), None, None)], Return(BooleanLit(True))), VarDecl(Id(XJ0q), None, dynamic, None), VarDecl(Id(ul), ArrayType([55.78], BoolType), None, None), VarDecl(Id(Av), ArrayType([78.08, 90.21], StringType), None, NumLit(96.32))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115134))

	def test_21530115135(self):
		input = '''
var O36 <- false
bool FK[77.16,13.65] <- "G"
bool XG <- 68.94
'''
		expect = '''Program([VarDecl(Id(O36), None, var, BooleanLit(False)), VarDecl(Id(FK), ArrayType([77.16, 13.65], BoolType), None, StringLit(G)), VarDecl(Id(XG), BoolType, None, NumLit(68.94))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115135))

	def test_21530115136(self):
		input = '''
func Ax (number QUYU, string uNr[6.91])
	return false
func w6l (number lV[46.73,91.47,82.1], string kf[39.04,5.9,67.96], bool qC0)	return 51.61
bool gGG <- false
var rPdc <- 69.42
'''
		expect = '''Program([FuncDecl(Id(Ax), [VarDecl(Id(QUYU), NumberType, None, None), VarDecl(Id(uNr), ArrayType([6.91], StringType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(w6l), [VarDecl(Id(lV), ArrayType([46.73, 91.47, 82.1], NumberType), None, None), VarDecl(Id(kf), ArrayType([39.04, 5.9, 67.96], StringType), None, None), VarDecl(Id(qC0), BoolType, None, None)], Return(NumLit(51.61))), VarDecl(Id(gGG), BoolType, None, BooleanLit(False)), VarDecl(Id(rPdc), None, var, NumLit(69.42))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115136))

	def test_21530115137(self):
		input = '''
func oov (number VWW[43.74,68.13], bool TQNJ, string RR)	return 45.79
dynamic xhan <- false
number qM4y[5.55,72.27] <- EWAb
'''
		expect = '''Program([FuncDecl(Id(oov), [VarDecl(Id(VWW), ArrayType([43.74, 68.13], NumberType), None, None), VarDecl(Id(TQNJ), BoolType, None, None), VarDecl(Id(RR), StringType, None, None)], Return(NumLit(45.79))), VarDecl(Id(xhan), None, dynamic, BooleanLit(False)), VarDecl(Id(qM4y), ArrayType([5.55, 72.27], NumberType), None, Id(EWAb))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115137))

	def test_21530115138(self):
		input = '''
string GVBb[48.49,57.27]
bool SR <- "NMeHi"
'''
		expect = '''Program([VarDecl(Id(GVBb), ArrayType([48.49, 57.27], StringType), None, None), VarDecl(Id(SR), BoolType, None, StringLit(NMeHi))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115138))

	def test_21530115139(self):
		input = '''
dynamic zR48
func r7h (bool HjMH, bool Htx[26.11])
	return

string ul8[31.19,93.16,13.89] <- 15.41
number JTh <- "dQN"
func Lm ()
	return TbDy
'''
		expect = '''Program([VarDecl(Id(zR48), None, dynamic, None), FuncDecl(Id(r7h), [VarDecl(Id(HjMH), BoolType, None, None), VarDecl(Id(Htx), ArrayType([26.11], BoolType), None, None)], Return()), VarDecl(Id(ul8), ArrayType([31.19, 93.16, 13.89], StringType), None, NumLit(15.41)), VarDecl(Id(JTh), NumberType, None, StringLit(dQN)), FuncDecl(Id(Lm), [], Return(Id(TbDy)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115139))

	def test_21530115140(self):
		input = '''
bool bka <- true
number U4
func EaVF (bool GE8[80.41,29.63])	return
func WPc (number XNh[1.07,29.7,30.72], bool E3k, number RZG)
	return

'''
		expect = '''Program([VarDecl(Id(bka), BoolType, None, BooleanLit(True)), VarDecl(Id(U4), NumberType, None, None), FuncDecl(Id(EaVF), [VarDecl(Id(GE8), ArrayType([80.41, 29.63], BoolType), None, None)], Return()), FuncDecl(Id(WPc), [VarDecl(Id(XNh), ArrayType([1.07, 29.7, 30.72], NumberType), None, None), VarDecl(Id(E3k), BoolType, None, None), VarDecl(Id(RZG), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115140))

	def test_21530115141(self):
		input = '''
number wMl
string s57
func ke ()	begin
		number wc0[3.42]
		break
	end

func Hx ()	return false

'''
		expect = '''Program([VarDecl(Id(wMl), NumberType, None, None), VarDecl(Id(s57), StringType, None, None), FuncDecl(Id(ke), [], Block([VarDecl(Id(wc0), ArrayType([3.42], NumberType), None, None), Break])), FuncDecl(Id(Hx), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115141))

	def test_21530115142(self):
		input = '''
func Saw ()	begin
		for Bo until "CFxK" by Le
			if (Xuys)
			number KOmn
		sIW(true, uWw, Kz)
	end
var Cb <- 61.58
string gaJa <- false
'''
		expect = '''Program([FuncDecl(Id(Saw), [], Block([For(Id(Bo), StringLit(CFxK), Id(Le), If((Id(Xuys), VarDecl(Id(KOmn), NumberType, None, None)), [], None)), CallStmt(Id(sIW), [BooleanLit(True), Id(uWw), Id(Kz)])])), VarDecl(Id(Cb), None, var, NumLit(61.58)), VarDecl(Id(gaJa), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115142))

	def test_21530115143(self):
		input = '''
func VJc (number BUAn[83.73,63.18], number aAqR[57.95,84.95], number aK3[31.47,12.63,54.45])
	begin
		begin
			return
			begin
				continue
				return
			end
		end
		break
		nRQ <- "dgxUS"
	end

func wJ (number wSnh, string jJar[78.86], number Ubs[25.52,0.81,23.46])
	return Tf

string Ab[7.81,47.72] <- 69.02
func z6 (number f8, string Vo[93.49,48.72,63.33])
	return QA

func Ex ()	return 98.7
'''
		expect = '''Program([FuncDecl(Id(VJc), [VarDecl(Id(BUAn), ArrayType([83.73, 63.18], NumberType), None, None), VarDecl(Id(aAqR), ArrayType([57.95, 84.95], NumberType), None, None), VarDecl(Id(aK3), ArrayType([31.47, 12.63, 54.45], NumberType), None, None)], Block([Block([Return(), Block([Continue, Return()])]), Break, AssignStmt(Id(nRQ), StringLit(dgxUS))])), FuncDecl(Id(wJ), [VarDecl(Id(wSnh), NumberType, None, None), VarDecl(Id(jJar), ArrayType([78.86], StringType), None, None), VarDecl(Id(Ubs), ArrayType([25.52, 0.81, 23.46], NumberType), None, None)], Return(Id(Tf))), VarDecl(Id(Ab), ArrayType([7.81, 47.72], StringType), None, NumLit(69.02)), FuncDecl(Id(z6), [VarDecl(Id(f8), NumberType, None, None), VarDecl(Id(Vo), ArrayType([93.49, 48.72, 63.33], StringType), None, None)], Return(Id(QA))), FuncDecl(Id(Ex), [], Return(NumLit(98.7)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115143))

	def test_21530115144(self):
		input = '''
number CMWZ[59.34] <- "r"
'''
		expect = '''Program([VarDecl(Id(CMWZ), ArrayType([59.34], NumberType), None, StringLit(r))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115144))

	def test_21530115145(self):
		input = '''
number qVvS <- 66.4
string ZhZ
bool LEzF <- 41.98
func bSP (number LO[24.23,82.39,27.29], string cKYI)	begin
		for dYBV until OB by hE
			for dZo until false by true
				for dsN until 0.1 by "Ayy"
					return
		if (true) break
		elif (true) string PCg[69.51,12.3]
		elif ("Snbrf") break
		elif ("R")
		YK1u("M", 41.96)
		elif (NJLw)
		continue
		elif (false) continue
	end
func KpD ()	begin
		cUqm["xEltM", 98.67] <- true
		continue
	end

'''
		expect = '''Program([VarDecl(Id(qVvS), NumberType, None, NumLit(66.4)), VarDecl(Id(ZhZ), StringType, None, None), VarDecl(Id(LEzF), BoolType, None, NumLit(41.98)), FuncDecl(Id(bSP), [VarDecl(Id(LO), ArrayType([24.23, 82.39, 27.29], NumberType), None, None), VarDecl(Id(cKYI), StringType, None, None)], Block([For(Id(dYBV), Id(OB), Id(hE), For(Id(dZo), BooleanLit(False), BooleanLit(True), For(Id(dsN), NumLit(0.1), StringLit(Ayy), Return()))), If((BooleanLit(True), Break), [(BooleanLit(True), VarDecl(Id(PCg), ArrayType([69.51, 12.3], StringType), None, None)), (StringLit(Snbrf), Break), (StringLit(R), CallStmt(Id(YK1u), [StringLit(M), NumLit(41.96)])), (Id(NJLw), Continue), (BooleanLit(False), Continue)], None)])), FuncDecl(Id(KpD), [], Block([AssignStmt(ArrayCell(Id(cUqm), [StringLit(xEltM), NumLit(98.67)]), BooleanLit(True)), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115145))

	def test_21530115146(self):
		input = '''
string zto7[6.48,78.23] <- 44.31
string Ng[74.16,85.16]
func ZdEu (number VjA[2.8,93.91])	begin
		if (99.0)
		break
		elif (GhVh) break
		elif (false) continue
		elif (Koq9)
		AbwA <- vBQv
		elif (true)
		continue
	end
func y0 (number Sdy, bool UT3S[0.47], number wD4[47.7,36.08,13.42])	return

'''
		expect = '''Program([VarDecl(Id(zto7), ArrayType([6.48, 78.23], StringType), None, NumLit(44.31)), VarDecl(Id(Ng), ArrayType([74.16, 85.16], StringType), None, None), FuncDecl(Id(ZdEu), [VarDecl(Id(VjA), ArrayType([2.8, 93.91], NumberType), None, None)], Block([If((NumLit(99.0), Break), [(Id(GhVh), Break), (BooleanLit(False), Continue), (Id(Koq9), AssignStmt(Id(AbwA), Id(vBQv))), (BooleanLit(True), Continue)], None)])), FuncDecl(Id(y0), [VarDecl(Id(Sdy), NumberType, None, None), VarDecl(Id(UT3S), ArrayType([0.47], BoolType), None, None), VarDecl(Id(wD4), ArrayType([47.7, 36.08, 13.42], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115146))

	def test_21530115147(self):
		input = '''
var KyZ <- "M"
bool A3M[39.57,47.22,83.15]
'''
		expect = '''Program([VarDecl(Id(KyZ), None, var, StringLit(M)), VarDecl(Id(A3M), ArrayType([39.57, 47.22, 83.15], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115147))

	def test_21530115148(self):
		input = '''
func B_wn (bool to, bool HzpP, bool WjV[38.74])
	return fp
'''
		expect = '''Program([FuncDecl(Id(B_wn), [VarDecl(Id(to), BoolType, None, None), VarDecl(Id(HzpP), BoolType, None, None), VarDecl(Id(WjV), ArrayType([38.74], BoolType), None, None)], Return(Id(fp)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115148))

	def test_21530115149(self):
		input = '''
bool pU2
string t6np[89.24,84.48,10.12] <- b9pa
func Vq ()	return

bool eYWl[69.36]
bool uvML[56.49]
'''
		expect = '''Program([VarDecl(Id(pU2), BoolType, None, None), VarDecl(Id(t6np), ArrayType([89.24, 84.48, 10.12], StringType), None, Id(b9pa)), FuncDecl(Id(Vq), [], Return()), VarDecl(Id(eYWl), ArrayType([69.36], BoolType), None, None), VarDecl(Id(uvML), ArrayType([56.49], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115149))

	def test_21530115150(self):
		input = '''
number CBIb <- 49.47
func paLV ()
	return
func g1cx (bool Sr9)
	begin
		continue
		begin
		end
		for hOi until EoD0 by 34.44
			break
	end
'''
		expect = '''Program([VarDecl(Id(CBIb), NumberType, None, NumLit(49.47)), FuncDecl(Id(paLV), [], Return()), FuncDecl(Id(g1cx), [VarDecl(Id(Sr9), BoolType, None, None)], Block([Continue, Block([]), For(Id(hOi), Id(EoD0), NumLit(34.44), Break)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115150))

	def test_21530115151(self):
		input = '''
func sZ1 ()
	return

bool lsTW[90.39]
'''
		expect = '''Program([FuncDecl(Id(sZ1), [], Return()), VarDecl(Id(lsTW), ArrayType([90.39], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115151))

	def test_21530115152(self):
		input = '''
string cj
string Z7[32.76,46.14] <- QXL3
'''
		expect = '''Program([VarDecl(Id(cj), StringType, None, None), VarDecl(Id(Z7), ArrayType([32.76, 46.14], StringType), None, Id(QXL3))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115152))

	def test_21530115153(self):
		input = '''
string dsT[48.75,18.86,33.82]
'''
		expect = '''Program([VarDecl(Id(dsT), ArrayType([48.75, 18.86, 33.82], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115153))

	def test_21530115154(self):
		input = '''
func D0qc ()	begin
		for Me72 until chg by Kr6
			begin
				break
			end
		if (Pv) if (FQV)
		begin
		end
		elif (false)
		return
		elif (false) if (35.44)
		break
		elif (hTF) bool Tk[9.32] <- "ZcHT"
		elif ("Yv") if ("fTi")
		break
		elif (mKF)
		for ctgS until 67.41 by true
			return
		elif (VFk) continue
		elif (vJr)
		begin
			for oGg until 7.5 by "a"
				continue
			if (ON6) if (32.69) ktN[29.72, QUaQ, "mJL"] <- 76.89
			elif (nWWm) SfO["Eg", "QThii"] <- false
			elif ("Gp") GO28[Iz, Rq] <- false
			elif (true) if (true)
			pQ()
			elif (false)
			return false
			else return 63.34
			elif (false)
			continue
			elif (90.22) if ("BwuWa")
			var VgBA <- "uF"
			elif (Ss) for Qo5 until "PgxC" by eeV
				continue
			elif (aO)
			begin
				return
				return 82.73
				bx[true, false, false] <- true
			end
		end
		elif (32.61)
		continue
		elif (87.47)
		return lm
		else break
		continue
	end
'''
		expect = '''Program([FuncDecl(Id(D0qc), [], Block([For(Id(Me72), Id(chg), Id(Kr6), Block([Break])), If((Id(Pv), If((Id(FQV), Block([])), [(BooleanLit(False), Return()), (BooleanLit(False), If((NumLit(35.44), Break), [(Id(hTF), VarDecl(Id(Tk), ArrayType([9.32], BoolType), None, StringLit(ZcHT))), (StringLit(Yv), If((StringLit(fTi), Break), [(Id(mKF), For(Id(ctgS), NumLit(67.41), BooleanLit(True), Return())), (Id(VFk), Continue), (Id(vJr), Block([For(Id(oGg), NumLit(7.5), StringLit(a), Continue), If((Id(ON6), If((NumLit(32.69), AssignStmt(ArrayCell(Id(ktN), [NumLit(29.72), Id(QUaQ), StringLit(mJL)]), NumLit(76.89))), [(Id(nWWm), AssignStmt(ArrayCell(Id(SfO), [StringLit(Eg), StringLit(QThii)]), BooleanLit(False))), (StringLit(Gp), AssignStmt(ArrayCell(Id(GO28), [Id(Iz), Id(Rq)]), BooleanLit(False))), (BooleanLit(True), If((BooleanLit(True), CallStmt(Id(pQ), [])), [(BooleanLit(False), Return(BooleanLit(False)))], Return(NumLit(63.34)))), (BooleanLit(False), Continue), (NumLit(90.22), If((StringLit(BwuWa), VarDecl(Id(VgBA), None, var, StringLit(uF))), [(Id(Ss), For(Id(Qo5), StringLit(PgxC), Id(eeV), Continue)), (Id(aO), Block([Return(), Return(NumLit(82.73)), AssignStmt(ArrayCell(Id(bx), [BooleanLit(True), BooleanLit(False), BooleanLit(False)]), BooleanLit(True))]))], None))], None)), [], None)])), (NumLit(32.61), Continue), (NumLit(87.47), Return(Id(lm)))], Break))], None))], None)), [], None), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115154))

	def test_21530115155(self):
		input = '''
var FL <- "kWc"
func MIo (bool nAk[57.65], string qZl, bool qyT[24.67])	return jJjL

var n3 <- false
'''
		expect = '''Program([VarDecl(Id(FL), None, var, StringLit(kWc)), FuncDecl(Id(MIo), [VarDecl(Id(nAk), ArrayType([57.65], BoolType), None, None), VarDecl(Id(qZl), StringType, None, None), VarDecl(Id(qyT), ArrayType([24.67], BoolType), None, None)], Return(Id(jJjL))), VarDecl(Id(n3), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115155))

	def test_21530115156(self):
		input = '''
func zL ()	begin
		begin
			continue
			rVK(dGB, 85.45, 7.89)
			for R6 until 34.01 by gII
				string eW8
		end
		fT()
		myO["CZ", "tQ"] <- "L"
	end
'''
		expect = '''Program([FuncDecl(Id(zL), [], Block([Block([Continue, CallStmt(Id(rVK), [Id(dGB), NumLit(85.45), NumLit(7.89)]), For(Id(R6), NumLit(34.01), Id(gII), VarDecl(Id(eW8), StringType, None, None))]), CallStmt(Id(fT), []), AssignStmt(ArrayCell(Id(myO), [StringLit(CZ), StringLit(tQ)]), StringLit(L))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115156))

	def test_21530115157(self):
		input = '''
dynamic KUOc
func So0 ()	return "DWCzn"
dynamic OBP8
'''
		expect = '''Program([VarDecl(Id(KUOc), None, dynamic, None), FuncDecl(Id(So0), [], Return(StringLit(DWCzn))), VarDecl(Id(OBP8), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115157))

	def test_21530115158(self):
		input = '''
func MiIF ()
	return "P"
number Qi0X[15.58] <- 14.19
'''
		expect = '''Program([FuncDecl(Id(MiIF), [], Return(StringLit(P))), VarDecl(Id(Qi0X), ArrayType([15.58], NumberType), None, NumLit(14.19))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115158))

	def test_21530115159(self):
		input = '''
bool n2[91.18,33.14,78.74] <- "Rn"
var QSMS <- 37.65
bool sdmY[92.71,73.58,30.03] <- 62.07
number zwd_[29.64,29.78] <- 37.07
'''
		expect = '''Program([VarDecl(Id(n2), ArrayType([91.18, 33.14, 78.74], BoolType), None, StringLit(Rn)), VarDecl(Id(QSMS), None, var, NumLit(37.65)), VarDecl(Id(sdmY), ArrayType([92.71, 73.58, 30.03], BoolType), None, NumLit(62.07)), VarDecl(Id(zwd_), ArrayType([29.64, 29.78], NumberType), None, NumLit(37.07))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115159))

	def test_21530115160(self):
		input = '''
string aY9 <- "lAPm"
'''
		expect = '''Program([VarDecl(Id(aY9), StringType, None, StringLit(lAPm))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115160))

	def test_21530115161(self):
		input = '''
func AZL (string P10[47.58])	return
dynamic Tee
func Gy (number dt0H[49.41,99.9,94.73])
	return

'''
		expect = '''Program([FuncDecl(Id(AZL), [VarDecl(Id(P10), ArrayType([47.58], StringType), None, None)], Return()), VarDecl(Id(Tee), None, dynamic, None), FuncDecl(Id(Gy), [VarDecl(Id(dt0H), ArrayType([49.41, 99.9, 94.73], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115161))

	def test_21530115162(self):
		input = '''
func G85H ()	return true
func WDNy ()
	return

func hE ()	return false

'''
		expect = '''Program([FuncDecl(Id(G85H), [], Return(BooleanLit(True))), FuncDecl(Id(WDNy), [], Return()), FuncDecl(Id(hE), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115162))

	def test_21530115163(self):
		input = '''
string URl[50.87] <- 3.19
string WFQ[53.02] <- false
'''
		expect = '''Program([VarDecl(Id(URl), ArrayType([50.87], StringType), None, NumLit(3.19)), VarDecl(Id(WFQ), ArrayType([53.02], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115163))

	def test_21530115164(self):
		input = '''
bool owJw[23.32,4.0] <- XG3q
bool eo
bool V6
'''
		expect = '''Program([VarDecl(Id(owJw), ArrayType([23.32, 4.0], BoolType), None, Id(XG3q)), VarDecl(Id(eo), BoolType, None, None), VarDecl(Id(V6), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115164))

	def test_21530115165(self):
		input = '''
func ac_G (bool HyMA, number lGR9[89.38])
	begin
		continue
		if (60.92) break
		elif (true)
		gp("acS", false)
		else if (66.42)
		if (98.68) dynamic gSwq <- "uOnm"
		elif (30.5)
		for I8 until true by cXNo
			if (true) if (true) pzGI[Fkm, false] <- 98.95
			elif (SA) return
			elif ("Rx") if (56.55) continue
			elif (21.54) begin
				continue
			end
			elif (Ll)
			lZ9 <- "fXcd"
			elif (Cpul)
			break
			elif (false)
			begin
				begin
					f8(false, false, dzQ)
				end
				continue
				begin
					UH(true, "rbk", fGJM)
					Ghk()
					wxM(fObJ)
				end
			end
			elif (true) iilD <- 81.08
			else MEtU <- false
			elif (false)
			for mNmO until "A" by y9hQ
				return
			elif (93.87)
			bool DJ4[68.8,64.1,15.37] <- 88.72
			elif (F8Gt) begin
				ghqZ <- "g"
				return
				pd(true, "HdUnM", Qb)
			end
			else for fC until "sYum" by true
				break
			elif (BtQ)
			if (true)
			begin
				continue
				return
			end
			elif ("nFY") tCE()
			elif (false)
			break
			elif (13.74) break
			elif ("ir") bool ebDk <- "yYqtZ"
			else break
		elif ("IKu") break
		elif (18.72) break
		elif (YoM)
		return
		elif (true) continue
		else number VD[9.93]
		elif ("LN")
		string gfI2[25.94] <- true
		elif ("njC")
		break
		elif ("J") for nsT until "ngk" by false
			continue
		elif (false) bool z9[19.24] <- tB
		else dynamic Pf1
	end
number VHf <- fsSJ
func DU (string Cq[6.65,96.03,89.27], bool o0Eo)
	begin
		continue
		for J_b until "m" by false
			eCt <- 87.3
		break
	end
func oJe (string pLP7, string uh5S)	return

'''
		expect = '''Program([FuncDecl(Id(ac_G), [VarDecl(Id(HyMA), BoolType, None, None), VarDecl(Id(lGR9), ArrayType([89.38], NumberType), None, None)], Block([Continue, If((NumLit(60.92), Break), [(BooleanLit(True), CallStmt(Id(gp), [StringLit(acS), BooleanLit(False)]))], If((NumLit(66.42), If((NumLit(98.68), VarDecl(Id(gSwq), None, dynamic, StringLit(uOnm))), [(NumLit(30.5), For(Id(I8), BooleanLit(True), Id(cXNo), If((BooleanLit(True), If((BooleanLit(True), AssignStmt(ArrayCell(Id(pzGI), [Id(Fkm), BooleanLit(False)]), NumLit(98.95))), [(Id(SA), Return()), (StringLit(Rx), If((NumLit(56.55), Continue), [(NumLit(21.54), Block([Continue])), (Id(Ll), AssignStmt(Id(lZ9), StringLit(fXcd))), (Id(Cpul), Break), (BooleanLit(False), Block([Block([CallStmt(Id(f8), [BooleanLit(False), BooleanLit(False), Id(dzQ)])]), Continue, Block([CallStmt(Id(UH), [BooleanLit(True), StringLit(rbk), Id(fGJM)]), CallStmt(Id(Ghk), []), CallStmt(Id(wxM), [Id(fObJ)])])])), (BooleanLit(True), AssignStmt(Id(iilD), NumLit(81.08)))], AssignStmt(Id(MEtU), BooleanLit(False)))), (BooleanLit(False), For(Id(mNmO), StringLit(A), Id(y9hQ), Return())), (NumLit(93.87), VarDecl(Id(DJ4), ArrayType([68.8, 64.1, 15.37], BoolType), None, NumLit(88.72))), (Id(F8Gt), Block([AssignStmt(Id(ghqZ), StringLit(g)), Return(), CallStmt(Id(pd), [BooleanLit(True), StringLit(HdUnM), Id(Qb)])]))], For(Id(fC), StringLit(sYum), BooleanLit(True), Break))), [(Id(BtQ), If((BooleanLit(True), Block([Continue, Return()])), [(StringLit(nFY), CallStmt(Id(tCE), [])), (BooleanLit(False), Break), (NumLit(13.74), Break), (StringLit(ir), VarDecl(Id(ebDk), BoolType, None, StringLit(yYqtZ)))], Break)), (StringLit(IKu), Break), (NumLit(18.72), Break), (Id(YoM), Return()), (BooleanLit(True), Continue)], VarDecl(Id(VD), ArrayType([9.93], NumberType), None, None)))), (StringLit(LN), VarDecl(Id(gfI2), ArrayType([25.94], StringType), None, BooleanLit(True))), (StringLit(njC), Break), (StringLit(J), For(Id(nsT), StringLit(ngk), BooleanLit(False), Continue)), (BooleanLit(False), VarDecl(Id(z9), ArrayType([19.24], BoolType), None, Id(tB)))], VarDecl(Id(Pf1), None, dynamic, None))), [], None))])), VarDecl(Id(VHf), NumberType, None, Id(fsSJ)), FuncDecl(Id(DU), [VarDecl(Id(Cq), ArrayType([6.65, 96.03, 89.27], StringType), None, None), VarDecl(Id(o0Eo), BoolType, None, None)], Block([Continue, For(Id(J_b), StringLit(m), BooleanLit(False), AssignStmt(Id(eCt), NumLit(87.3))), Break])), FuncDecl(Id(oJe), [VarDecl(Id(pLP7), StringType, None, None), VarDecl(Id(uh5S), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115165))

	def test_21530115166(self):
		input = '''
func bHV (number r4L[95.57,69.82])
	begin
		number DD <- pdMm
	end
bool EqG[43.0,27.1]
func fBos ()
	return I91
string j7PL[54.69,33.75,50.62]
'''
		expect = '''Program([FuncDecl(Id(bHV), [VarDecl(Id(r4L), ArrayType([95.57, 69.82], NumberType), None, None)], Block([VarDecl(Id(DD), NumberType, None, Id(pdMm))])), VarDecl(Id(EqG), ArrayType([43.0, 27.1], BoolType), None, None), FuncDecl(Id(fBos), [], Return(Id(I91))), VarDecl(Id(j7PL), ArrayType([54.69, 33.75, 50.62], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115166))

	def test_21530115167(self):
		input = '''
func phu ()
	begin
		return
		break
	end
dynamic lKoc <- 21.12
func vfIU (bool poyO, bool j4Ju[6.1,29.23])
	begin
		continue
		break
		N1NA(78.17)
	end
var Aok <- "He"
string Su[42.91,47.35]
'''
		expect = '''Program([FuncDecl(Id(phu), [], Block([Return(), Break])), VarDecl(Id(lKoc), None, dynamic, NumLit(21.12)), FuncDecl(Id(vfIU), [VarDecl(Id(poyO), BoolType, None, None), VarDecl(Id(j4Ju), ArrayType([6.1, 29.23], BoolType), None, None)], Block([Continue, Break, CallStmt(Id(N1NA), [NumLit(78.17)])])), VarDecl(Id(Aok), None, var, StringLit(He)), VarDecl(Id(Su), ArrayType([42.91, 47.35], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115167))

	def test_21530115168(self):
		input = '''
func yIEB (number w4k[16.22,18.24], string O4B[4.9,87.25,98.74])
	begin
		return
	end
func bx4W (string eCgJ[76.65])	return Y6Iz

func r3 (bool urx)	return false

'''
		expect = '''Program([FuncDecl(Id(yIEB), [VarDecl(Id(w4k), ArrayType([16.22, 18.24], NumberType), None, None), VarDecl(Id(O4B), ArrayType([4.9, 87.25, 98.74], StringType), None, None)], Block([Return()])), FuncDecl(Id(bx4W), [VarDecl(Id(eCgJ), ArrayType([76.65], StringType), None, None)], Return(Id(Y6Iz))), FuncDecl(Id(r3), [VarDecl(Id(urx), BoolType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115168))

	def test_21530115169(self):
		input = '''
string pej[8.8] <- "UNNlf"
func NRwT (number q0[46.8,64.32,26.11])
	return nTO

number Gu[33.71]
'''
		expect = '''Program([VarDecl(Id(pej), ArrayType([8.8], StringType), None, StringLit(UNNlf)), FuncDecl(Id(NRwT), [VarDecl(Id(q0), ArrayType([46.8, 64.32, 26.11], NumberType), None, None)], Return(Id(nTO))), VarDecl(Id(Gu), ArrayType([33.71], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115169))

	def test_21530115170(self):
		input = '''
func Sj (number eP, bool Dj[9.84], number t4)
	return
bool ZRt[40.87,55.99]
number kE
bool rfaJ <- sP
'''
		expect = '''Program([FuncDecl(Id(Sj), [VarDecl(Id(eP), NumberType, None, None), VarDecl(Id(Dj), ArrayType([9.84], BoolType), None, None), VarDecl(Id(t4), NumberType, None, None)], Return()), VarDecl(Id(ZRt), ArrayType([40.87, 55.99], BoolType), None, None), VarDecl(Id(kE), NumberType, None, None), VarDecl(Id(rfaJ), BoolType, None, Id(sP))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115170))

	def test_21530115171(self):
		input = '''
number nv <- F7BK
func kwZo (number Ph, string ZA, bool Rgl[52.85])
	begin
		string SAa
		break
	end
'''
		expect = '''Program([VarDecl(Id(nv), NumberType, None, Id(F7BK)), FuncDecl(Id(kwZo), [VarDecl(Id(Ph), NumberType, None, None), VarDecl(Id(ZA), StringType, None, None), VarDecl(Id(Rgl), ArrayType([52.85], BoolType), None, None)], Block([VarDecl(Id(SAa), StringType, None, None), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115171))

	def test_21530115172(self):
		input = '''
func bdfZ (string fHUu, bool lKSP)
	return
func WVhO (string GFLN)	begin
		if ("fW")
		for pH until true by ae
			U3X(29.8)
		elif (true) wn(78.44, "Zyuk")
		elif (aR) return true
		elif (cZvG)
		string M1HC
		elif (31.83)
		begin
			IkT[83.69, "WPhf"] <- 12.98
		end
	end
'''
		expect = '''Program([FuncDecl(Id(bdfZ), [VarDecl(Id(fHUu), StringType, None, None), VarDecl(Id(lKSP), BoolType, None, None)], Return()), FuncDecl(Id(WVhO), [VarDecl(Id(GFLN), StringType, None, None)], Block([If((StringLit(fW), For(Id(pH), BooleanLit(True), Id(ae), CallStmt(Id(U3X), [NumLit(29.8)]))), [(BooleanLit(True), CallStmt(Id(wn), [NumLit(78.44), StringLit(Zyuk)])), (Id(aR), Return(BooleanLit(True))), (Id(cZvG), VarDecl(Id(M1HC), StringType, None, None)), (NumLit(31.83), Block([AssignStmt(ArrayCell(Id(IkT), [NumLit(83.69), StringLit(WPhf)]), NumLit(12.98))]))], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115172))

	def test_21530115173(self):
		input = '''
bool qI3J[79.09]
func Ji (number Ub8T[94.07,78.67,71.57], bool r6HG[40.12], bool qVEA[47.21,2.66,74.66])
	begin
		for HePO until "idiT" by 66.6
			zf7[Un] <- ne
	end

number TJ[63.96,52.31] <- "DIRl"
string vL6[84.3]
'''
		expect = '''Program([VarDecl(Id(qI3J), ArrayType([79.09], BoolType), None, None), FuncDecl(Id(Ji), [VarDecl(Id(Ub8T), ArrayType([94.07, 78.67, 71.57], NumberType), None, None), VarDecl(Id(r6HG), ArrayType([40.12], BoolType), None, None), VarDecl(Id(qVEA), ArrayType([47.21, 2.66, 74.66], BoolType), None, None)], Block([For(Id(HePO), StringLit(idiT), NumLit(66.6), AssignStmt(ArrayCell(Id(zf7), [Id(Un)]), Id(ne)))])), VarDecl(Id(TJ), ArrayType([63.96, 52.31], NumberType), None, StringLit(DIRl)), VarDecl(Id(vL6), ArrayType([84.3], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115173))

	def test_21530115174(self):
		input = '''
func Gl ()
	begin
		for MI5g until false by wON
			NMs0[87.08] <- BV
	end

func Tm ()	begin
		if (36.91)
		for q61 until aat7 by "R"
			begin
			end
		elif (A1) return
		else continue
		var lBb <- true
		if (false) X53 <- true
		elif (RU)
		break
		elif ("y")
		continue
		elif (false)
		if (true) if ("PnqOQ")
		if (59.31)
		Kp[false] <- bVbk
		elif (true)
		SjA(fAAe, "Ohmky")
		elif (false) break
		elif (false)
		begin
			begin
				if (Qkkh) return
				elif (false) bool Va9N[10.5,28.0] <- "zwMC"
				elif ("xmgz") number sOv[9.01,79.36]
				elif (33.18) for pk until "kjE" by 78.15
					number FpZ[78.67] <- js
				elif (76.74)
				if (false) if (true)
				return ELRP
				elif (vPqe) begin
					return Kxb
					if ("wCVum") La8()
					elif (85.95) return
					elif (mnEq) eg1(false, true, 69.31)
					else I7 <- false
					bz19(true, 65.14, "kKC")
				end
				elif ("yI") for dc until "qAk" by 55.38
					uYss["zbxvM", false, 37.08] <- 38.28
				else break
			end
		end
		elif (true) Wm[Xk2U, IK, KAO1] <- b3
		elif (false) Hi9Q(Q8)
		elif (43.68)
		if (true) zc[CxK, 7.14, "NFnHl"] <- Xkgc
		elif ("dd") string kZ[94.33,16.79]
		elif (yN) continue
		elif (true)
		for fo3 until true by false
			return true
		else begin
		end
		elif ("Z")
		string OwRH[17.67]
		elif (36.81) cy(48.33, 1.4, Ec)
		elif (CW3d)
		begin
			break
			Dl4()
		end
		elif (36.95)
		bool kL <- 52.35
		else for J31g until "Um" by pAF
			lUo(16.36, 55.73)
	end

bool oL[21.86]
'''
		expect = '''Program([FuncDecl(Id(Gl), [], Block([For(Id(MI5g), BooleanLit(False), Id(wON), AssignStmt(ArrayCell(Id(NMs0), [NumLit(87.08)]), Id(BV)))])), FuncDecl(Id(Tm), [], Block([If((NumLit(36.91), For(Id(q61), Id(aat7), StringLit(R), Block([]))), [(Id(A1), Return())], Continue), VarDecl(Id(lBb), None, var, BooleanLit(True)), If((BooleanLit(False), AssignStmt(Id(X53), BooleanLit(True))), [(Id(RU), Break), (StringLit(y), Continue), (BooleanLit(False), If((BooleanLit(True), If((StringLit(PnqOQ), If((NumLit(59.31), AssignStmt(ArrayCell(Id(Kp), [BooleanLit(False)]), Id(bVbk))), [(BooleanLit(True), CallStmt(Id(SjA), [Id(fAAe), StringLit(Ohmky)])), (BooleanLit(False), Break), (BooleanLit(False), Block([Block([If((Id(Qkkh), Return()), [(BooleanLit(False), VarDecl(Id(Va9N), ArrayType([10.5, 28.0], BoolType), None, StringLit(zwMC))), (StringLit(xmgz), VarDecl(Id(sOv), ArrayType([9.01, 79.36], NumberType), None, None)), (NumLit(33.18), For(Id(pk), StringLit(kjE), NumLit(78.15), VarDecl(Id(FpZ), ArrayType([78.67], NumberType), None, Id(js)))), (NumLit(76.74), If((BooleanLit(False), If((BooleanLit(True), Return(Id(ELRP))), [(Id(vPqe), Block([Return(Id(Kxb)), If((StringLit(wCVum), CallStmt(Id(La8), [])), [(NumLit(85.95), Return()), (Id(mnEq), CallStmt(Id(eg1), [BooleanLit(False), BooleanLit(True), NumLit(69.31)]))], AssignStmt(Id(I7), BooleanLit(False))), CallStmt(Id(bz19), [BooleanLit(True), NumLit(65.14), StringLit(kKC)])])), (StringLit(yI), For(Id(dc), StringLit(qAk), NumLit(55.38), AssignStmt(ArrayCell(Id(uYss), [StringLit(zbxvM), BooleanLit(False), NumLit(37.08)]), NumLit(38.28))))], Break)), [], None))], None)])])), (BooleanLit(True), AssignStmt(ArrayCell(Id(Wm), [Id(Xk2U), Id(IK), Id(KAO1)]), Id(b3))), (BooleanLit(False), CallStmt(Id(Hi9Q), [Id(Q8)])), (NumLit(43.68), If((BooleanLit(True), AssignStmt(ArrayCell(Id(zc), [Id(CxK), NumLit(7.14), StringLit(NFnHl)]), Id(Xkgc))), [(StringLit(dd), VarDecl(Id(kZ), ArrayType([94.33, 16.79], StringType), None, None)), (Id(yN), Continue), (BooleanLit(True), For(Id(fo3), BooleanLit(True), BooleanLit(False), Return(BooleanLit(True))))], Block([]))), (StringLit(Z), VarDecl(Id(OwRH), ArrayType([17.67], StringType), None, None)), (NumLit(36.81), CallStmt(Id(cy), [NumLit(48.33), NumLit(1.4), Id(Ec)])), (Id(CW3d), Block([Break, CallStmt(Id(Dl4), [])])), (NumLit(36.95), VarDecl(Id(kL), BoolType, None, NumLit(52.35)))], For(Id(J31g), StringLit(Um), Id(pAF), CallStmt(Id(lUo), [NumLit(16.36), NumLit(55.73)])))), [], None)), [], None))], None)])), VarDecl(Id(oL), ArrayType([21.86], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115174))

	def test_21530115175(self):
		input = '''
bool Ls
number MyPF[13.15,41.46,80.2]
func TZ (bool Qtd, string cphq)
	begin
	end
number c6[14.81] <- 22.25
'''
		expect = '''Program([VarDecl(Id(Ls), BoolType, None, None), VarDecl(Id(MyPF), ArrayType([13.15, 41.46, 80.2], NumberType), None, None), FuncDecl(Id(TZ), [VarDecl(Id(Qtd), BoolType, None, None), VarDecl(Id(cphq), StringType, None, None)], Block([])), VarDecl(Id(c6), ArrayType([14.81], NumberType), None, NumLit(22.25))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115175))

	def test_21530115176(self):
		input = '''
var xNl <- false
func La ()	return

dynamic TFeO
'''
		expect = '''Program([VarDecl(Id(xNl), None, var, BooleanLit(False)), FuncDecl(Id(La), [], Return()), VarDecl(Id(TFeO), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115176))

	def test_21530115177(self):
		input = '''
var Gwlt <- YXC
bool nu <- true
bool wdxt <- "KUM"
string dU <- false
'''
		expect = '''Program([VarDecl(Id(Gwlt), None, var, Id(YXC)), VarDecl(Id(nu), BoolType, None, BooleanLit(True)), VarDecl(Id(wdxt), BoolType, None, StringLit(KUM)), VarDecl(Id(dU), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115177))

	def test_21530115178(self):
		input = '''
string dWYT[65.51] <- 44.95
func Pm (string jrQ)
	begin
	end

func ooJj (string wZAB[19.23], number Py[4.05,8.53,90.04])
	return 24.95
'''
		expect = '''Program([VarDecl(Id(dWYT), ArrayType([65.51], StringType), None, NumLit(44.95)), FuncDecl(Id(Pm), [VarDecl(Id(jrQ), StringType, None, None)], Block([])), FuncDecl(Id(ooJj), [VarDecl(Id(wZAB), ArrayType([19.23], StringType), None, None), VarDecl(Id(Py), ArrayType([4.05, 8.53, 90.04], NumberType), None, None)], Return(NumLit(24.95)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115178))

	def test_21530115179(self):
		input = '''
var G20 <- true
func r4K9 ()	begin
		for Dk until true by 6.0
			if (22.07)
			for ps until Q2F by CsVP
				break
			elif (IVZ_) return oCQ
			elif (true) continue
			elif (false) continue
			elif (LK)
			zEwJ <- false
			else begin
				begin
					return
				end
				return Cvc
			end
	end
func azz ()	return true
bool Mr2[64.11,67.29] <- DT
number g2
'''
		expect = '''Program([VarDecl(Id(G20), None, var, BooleanLit(True)), FuncDecl(Id(r4K9), [], Block([For(Id(Dk), BooleanLit(True), NumLit(6.0), If((NumLit(22.07), For(Id(ps), Id(Q2F), Id(CsVP), Break)), [(Id(IVZ_), Return(Id(oCQ))), (BooleanLit(True), Continue), (BooleanLit(False), Continue), (Id(LK), AssignStmt(Id(zEwJ), BooleanLit(False)))], Block([Block([Return()]), Return(Id(Cvc))])))])), FuncDecl(Id(azz), [], Return(BooleanLit(True))), VarDecl(Id(Mr2), ArrayType([64.11, 67.29], BoolType), None, Id(DT)), VarDecl(Id(g2), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115179))

	def test_21530115180(self):
		input = '''
string uDd <- true
func XQp ()
	begin
		break
	end
func MI ()	return
func Ph (string pj2[84.88,60.01], string YV)	begin
		break
		for cH until FC by false
			begin
				JV2 <- SDR3
				begin
				end
				break
			end
		break
	end
dynamic R3WZ
'''
		expect = '''Program([VarDecl(Id(uDd), StringType, None, BooleanLit(True)), FuncDecl(Id(XQp), [], Block([Break])), FuncDecl(Id(MI), [], Return()), FuncDecl(Id(Ph), [VarDecl(Id(pj2), ArrayType([84.88, 60.01], StringType), None, None), VarDecl(Id(YV), StringType, None, None)], Block([Break, For(Id(cH), Id(FC), BooleanLit(False), Block([AssignStmt(Id(JV2), Id(SDR3)), Block([]), Break])), Break])), VarDecl(Id(R3WZ), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115180))

	def test_21530115181(self):
		input = '''
bool K5c[79.82]
func mr ()	return
func Q0X (string a6FR)	return true
'''
		expect = '''Program([VarDecl(Id(K5c), ArrayType([79.82], BoolType), None, None), FuncDecl(Id(mr), [], Return()), FuncDecl(Id(Q0X), [VarDecl(Id(a6FR), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115181))

	def test_21530115182(self):
		input = '''
string uj <- 85.49
number EB
number L7[14.23,39.25,33.09] <- 57.55
func KV ()	return

'''
		expect = '''Program([VarDecl(Id(uj), StringType, None, NumLit(85.49)), VarDecl(Id(EB), NumberType, None, None), VarDecl(Id(L7), ArrayType([14.23, 39.25, 33.09], NumberType), None, NumLit(57.55)), FuncDecl(Id(KV), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115182))

	def test_21530115183(self):
		input = '''
bool yB[64.44,42.69] <- false
'''
		expect = '''Program([VarDecl(Id(yB), ArrayType([64.44, 42.69], BoolType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115183))

	def test_21530115184(self):
		input = '''
func DgH (string HT[48.29,0.27])
	begin
		return false
	end

dynamic Vs
func dyW1 (number zU[52.34,55.74,19.32])
	return
var I24 <- "whj"
func yipg (number Gr[17.85], number Xn[51.68,66.72])	begin
		return
		uwzS()
	end

'''
		expect = '''Program([FuncDecl(Id(DgH), [VarDecl(Id(HT), ArrayType([48.29, 0.27], StringType), None, None)], Block([Return(BooleanLit(False))])), VarDecl(Id(Vs), None, dynamic, None), FuncDecl(Id(dyW1), [VarDecl(Id(zU), ArrayType([52.34, 55.74, 19.32], NumberType), None, None)], Return()), VarDecl(Id(I24), None, var, StringLit(whj)), FuncDecl(Id(yipg), [VarDecl(Id(Gr), ArrayType([17.85], NumberType), None, None), VarDecl(Id(Xn), ArrayType([51.68, 66.72], NumberType), None, None)], Block([Return(), CallStmt(Id(uwzS), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115184))

	def test_21530115185(self):
		input = '''
number q_ <- true
string C3o[20.89,79.47,34.22] <- 29.48
bool yBv[26.48,13.02,47.87]
'''
		expect = '''Program([VarDecl(Id(q_), NumberType, None, BooleanLit(True)), VarDecl(Id(C3o), ArrayType([20.89, 79.47, 34.22], StringType), None, NumLit(29.48)), VarDecl(Id(yBv), ArrayType([26.48, 13.02, 47.87], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115185))

	def test_21530115186(self):
		input = '''
func A2 (bool Ab3)	return
bool cszV <- "fKXF"
'''
		expect = '''Program([FuncDecl(Id(A2), [VarDecl(Id(Ab3), BoolType, None, None)], Return()), VarDecl(Id(cszV), BoolType, None, StringLit(fKXF))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115186))

	def test_21530115187(self):
		input = '''
func Cs0 (string dTO[73.81], string rXE)
	return

'''
		expect = '''Program([FuncDecl(Id(Cs0), [VarDecl(Id(dTO), ArrayType([73.81], StringType), None, None), VarDecl(Id(rXE), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115187))

	def test_21530115188(self):
		input = '''
func ZTj (bool GHlW[98.34,92.75], string aO2[72.84])	return
func Jq (string TWA[50.93,65.62,15.34], string Mh0)	return true
number d11C[28.93,83.19,21.42]
'''
		expect = '''Program([FuncDecl(Id(ZTj), [VarDecl(Id(GHlW), ArrayType([98.34, 92.75], BoolType), None, None), VarDecl(Id(aO2), ArrayType([72.84], StringType), None, None)], Return()), FuncDecl(Id(Jq), [VarDecl(Id(TWA), ArrayType([50.93, 65.62, 15.34], StringType), None, None), VarDecl(Id(Mh0), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(d11C), ArrayType([28.93, 83.19, 21.42], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115188))

	def test_21530115189(self):
		input = '''
func HHA (number Aa2[75.45,3.44])
	return

func MQ8 (string s1Fb[4.39,84.64,52.75], bool nX, number ZfP[21.41,50.09])	return
var ZcY <- true
bool BO <- fj
'''
		expect = '''Program([FuncDecl(Id(HHA), [VarDecl(Id(Aa2), ArrayType([75.45, 3.44], NumberType), None, None)], Return()), FuncDecl(Id(MQ8), [VarDecl(Id(s1Fb), ArrayType([4.39, 84.64, 52.75], StringType), None, None), VarDecl(Id(nX), BoolType, None, None), VarDecl(Id(ZfP), ArrayType([21.41, 50.09], NumberType), None, None)], Return()), VarDecl(Id(ZcY), None, var, BooleanLit(True)), VarDecl(Id(BO), BoolType, None, Id(fj))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115189))

	def test_21530115190(self):
		input = '''
func MVH (bool GXih, bool W3PE[53.14,58.22])	return A8

number e33[35.52,17.85,57.93]
func Aia (number FOFT, bool nTO, bool kfpA[31.58,24.66])
	return
number Yo[28.95,25.8,22.9]
func G6U (number wNZ[18.51], number XwN[75.53,91.5,18.79], number wgMr)	return "InGh"
'''
		expect = '''Program([FuncDecl(Id(MVH), [VarDecl(Id(GXih), BoolType, None, None), VarDecl(Id(W3PE), ArrayType([53.14, 58.22], BoolType), None, None)], Return(Id(A8))), VarDecl(Id(e33), ArrayType([35.52, 17.85, 57.93], NumberType), None, None), FuncDecl(Id(Aia), [VarDecl(Id(FOFT), NumberType, None, None), VarDecl(Id(nTO), BoolType, None, None), VarDecl(Id(kfpA), ArrayType([31.58, 24.66], BoolType), None, None)], Return()), VarDecl(Id(Yo), ArrayType([28.95, 25.8, 22.9], NumberType), None, None), FuncDecl(Id(G6U), [VarDecl(Id(wNZ), ArrayType([18.51], NumberType), None, None), VarDecl(Id(XwN), ArrayType([75.53, 91.5, 18.79], NumberType), None, None), VarDecl(Id(wgMr), NumberType, None, None)], Return(StringLit(InGh)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115190))

	def test_21530115191(self):
		input = '''
func o1Q (bool yAZ, string cK, string pZa[93.4])
	return
number xh
func dJ (number Ze[64.32,83.0,72.53], bool M7[44.71], number JT)
	return

bool CCX <- true
func rE (string G4[43.59,44.55,78.54], string P0fZ)
	return

'''
		expect = '''Program([FuncDecl(Id(o1Q), [VarDecl(Id(yAZ), BoolType, None, None), VarDecl(Id(cK), StringType, None, None), VarDecl(Id(pZa), ArrayType([93.4], StringType), None, None)], Return()), VarDecl(Id(xh), NumberType, None, None), FuncDecl(Id(dJ), [VarDecl(Id(Ze), ArrayType([64.32, 83.0, 72.53], NumberType), None, None), VarDecl(Id(M7), ArrayType([44.71], BoolType), None, None), VarDecl(Id(JT), NumberType, None, None)], Return()), VarDecl(Id(CCX), BoolType, None, BooleanLit(True)), FuncDecl(Id(rE), [VarDecl(Id(G4), ArrayType([43.59, 44.55, 78.54], StringType), None, None), VarDecl(Id(P0fZ), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115191))

	def test_21530115192(self):
		input = '''
number cTR
func egZz (string nHG9[37.96], number HdB[17.85])	return 73.49
string UWRp[76.71] <- "Ib"
'''
		expect = '''Program([VarDecl(Id(cTR), NumberType, None, None), FuncDecl(Id(egZz), [VarDecl(Id(nHG9), ArrayType([37.96], StringType), None, None), VarDecl(Id(HdB), ArrayType([17.85], NumberType), None, None)], Return(NumLit(73.49))), VarDecl(Id(UWRp), ArrayType([76.71], StringType), None, StringLit(Ib))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115192))

	def test_21530115193(self):
		input = '''
string qrV[44.25] <- "Q"
func dMD ()	begin
	end

dynamic cWfl <- 23.58
'''
		expect = '''Program([VarDecl(Id(qrV), ArrayType([44.25], StringType), None, StringLit(Q)), FuncDecl(Id(dMD), [], Block([])), VarDecl(Id(cWfl), None, dynamic, NumLit(23.58))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115193))

	def test_21530115194(self):
		input = '''
func t8i (string xYs[72.93,66.08])
	return
'''
		expect = '''Program([FuncDecl(Id(t8i), [VarDecl(Id(xYs), ArrayType([72.93, 66.08], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115194))

	def test_21530115195(self):
		input = '''
func zsjF (number pa)	return false

func PxBx ()
	return "Fefh"
string ZBMx
number Wa[18.14] <- "pPPz"
func R_H (number Ym, number c6cA[48.3,79.92,44.08], number mNJ)	begin
	end

'''
		expect = '''Program([FuncDecl(Id(zsjF), [VarDecl(Id(pa), NumberType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(PxBx), [], Return(StringLit(Fefh))), VarDecl(Id(ZBMx), StringType, None, None), VarDecl(Id(Wa), ArrayType([18.14], NumberType), None, StringLit(pPPz)), FuncDecl(Id(R_H), [VarDecl(Id(Ym), NumberType, None, None), VarDecl(Id(c6cA), ArrayType([48.3, 79.92, 44.08], NumberType), None, None), VarDecl(Id(mNJ), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115195))

	def test_21530115196(self):
		input = '''
var Su9 <- "NzQD"
func Kj (bool lun)	return

string qR6q[95.93,37.94,66.96] <- true
string c1f
var jXL <- 31.37
'''
		expect = '''Program([VarDecl(Id(Su9), None, var, StringLit(NzQD)), FuncDecl(Id(Kj), [VarDecl(Id(lun), BoolType, None, None)], Return()), VarDecl(Id(qR6q), ArrayType([95.93, 37.94, 66.96], StringType), None, BooleanLit(True)), VarDecl(Id(c1f), StringType, None, None), VarDecl(Id(jXL), None, var, NumLit(31.37))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115196))

	def test_21530115197(self):
		input = '''
func oq ()
	return "uder"

func z9 (number y1[50.71], string sllS, bool PG[58.55,36.96,2.21])
	return "OEm"
bool uDtM <- false
var WwR <- 15.53
func Fhxu (bool qkZo[92.15,61.59])
	return
'''
		expect = '''Program([FuncDecl(Id(oq), [], Return(StringLit(uder))), FuncDecl(Id(z9), [VarDecl(Id(y1), ArrayType([50.71], NumberType), None, None), VarDecl(Id(sllS), StringType, None, None), VarDecl(Id(PG), ArrayType([58.55, 36.96, 2.21], BoolType), None, None)], Return(StringLit(OEm))), VarDecl(Id(uDtM), BoolType, None, BooleanLit(False)), VarDecl(Id(WwR), None, var, NumLit(15.53)), FuncDecl(Id(Fhxu), [VarDecl(Id(qkZo), ArrayType([92.15, 61.59], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115197))

	def test_21530115198(self):
		input = '''
func R_G4 (number JLP[52.49], string m9, bool lHz[36.65,78.96])
	return

var NY <- true
'''
		expect = '''Program([FuncDecl(Id(R_G4), [VarDecl(Id(JLP), ArrayType([52.49], NumberType), None, None), VarDecl(Id(m9), StringType, None, None), VarDecl(Id(lHz), ArrayType([36.65, 78.96], BoolType), None, None)], Return()), VarDecl(Id(NY), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115198))

	def test_21530115199(self):
		input = '''
bool RKsK[52.59] <- 81.65
bool wk6Y[63.9,24.12,32.24]
func uK (string Uk[32.78])
	return 47.32
'''
		expect = '''Program([VarDecl(Id(RKsK), ArrayType([52.59], BoolType), None, NumLit(81.65)), VarDecl(Id(wk6Y), ArrayType([63.9, 24.12, 32.24], BoolType), None, None), FuncDecl(Id(uK), [VarDecl(Id(Uk), ArrayType([32.78], StringType), None, None)], Return(NumLit(47.32)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115199))

	def test_21530115200(self):
		input = '''
string W9NU <- dz
func tK1G ()
	return SCrB
'''
		expect = '''Program([VarDecl(Id(W9NU), StringType, None, Id(dz)), FuncDecl(Id(tK1G), [], Return(Id(SCrB)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115200))

	def test_21530115201(self):
		input = '''
var Js <- true
number SE_
'''
		expect = '''Program([VarDecl(Id(Js), None, var, BooleanLit(True)), VarDecl(Id(SE_), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115201))

	def test_21530115202(self):
		input = '''
func NNs ()	return PSE
string r3iT[71.59] <- qv
bool ngsG[82.98,40.84]
'''
		expect = '''Program([FuncDecl(Id(NNs), [], Return(Id(PSE))), VarDecl(Id(r3iT), ArrayType([71.59], StringType), None, Id(qv)), VarDecl(Id(ngsG), ArrayType([82.98, 40.84], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115202))

	def test_21530115203(self):
		input = '''
number Ww[39.43,57.91,17.72] <- "auEwA"
'''
		expect = '''Program([VarDecl(Id(Ww), ArrayType([39.43, 57.91, 17.72], NumberType), None, StringLit(auEwA))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115203))

	def test_21530115204(self):
		input = '''
func jJT (string hc5x, bool C0, bool vS)	return
func EiE6 (string Tfm[70.25,47.83,75.46])	return 62.63

bool GDTs[53.85,96.43]
bool OV <- "Nkwd"
bool GZuN[15.12,8.51,6.86] <- Md7
'''
		expect = '''Program([FuncDecl(Id(jJT), [VarDecl(Id(hc5x), StringType, None, None), VarDecl(Id(C0), BoolType, None, None), VarDecl(Id(vS), BoolType, None, None)], Return()), FuncDecl(Id(EiE6), [VarDecl(Id(Tfm), ArrayType([70.25, 47.83, 75.46], StringType), None, None)], Return(NumLit(62.63))), VarDecl(Id(GDTs), ArrayType([53.85, 96.43], BoolType), None, None), VarDecl(Id(OV), BoolType, None, StringLit(Nkwd)), VarDecl(Id(GZuN), ArrayType([15.12, 8.51, 6.86], BoolType), None, Id(Md7))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115204))

	def test_21530115205(self):
		input = '''
func gX (number eHk, string Y4zU[9.51,80.98,59.69], bool xsiC)
	return

func fb ()	return

'''
		expect = '''Program([FuncDecl(Id(gX), [VarDecl(Id(eHk), NumberType, None, None), VarDecl(Id(Y4zU), ArrayType([9.51, 80.98, 59.69], StringType), None, None), VarDecl(Id(xsiC), BoolType, None, None)], Return()), FuncDecl(Id(fb), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115205))

	def test_21530115206(self):
		input = '''
number MoX <- AE
func js (number yLY)	return

'''
		expect = '''Program([VarDecl(Id(MoX), NumberType, None, Id(AE)), FuncDecl(Id(js), [VarDecl(Id(yLY), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115206))

	def test_21530115207(self):
		input = '''
func aPl (number eJuI, bool Ii2I[65.41,86.42,28.68], string KNc[94.41,82.96,35.24])
	return

func vd (bool dX[87.23,78.88], bool JA[89.32,14.26,11.32])
	begin
		E0()
		break
	end

func h1ID (string XmX)	return fWB
number QXsn <- 33.14
'''
		expect = '''Program([FuncDecl(Id(aPl), [VarDecl(Id(eJuI), NumberType, None, None), VarDecl(Id(Ii2I), ArrayType([65.41, 86.42, 28.68], BoolType), None, None), VarDecl(Id(KNc), ArrayType([94.41, 82.96, 35.24], StringType), None, None)], Return()), FuncDecl(Id(vd), [VarDecl(Id(dX), ArrayType([87.23, 78.88], BoolType), None, None), VarDecl(Id(JA), ArrayType([89.32, 14.26, 11.32], BoolType), None, None)], Block([CallStmt(Id(E0), []), Break])), FuncDecl(Id(h1ID), [VarDecl(Id(XmX), StringType, None, None)], Return(Id(fWB))), VarDecl(Id(QXsn), NumberType, None, NumLit(33.14))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115207))

	def test_21530115208(self):
		input = '''
func zQ0 (number Y__h[69.66], string XxyQ[21.05,17.2])	return
func tEiQ (bool Zy)	return
func Er (number pMq[52.15,15.94])	return AA
func IVu (number a09[48.56], number oLn, bool pg2[1.52,78.36,78.82])	begin
		begin
			break
			break
			string e0[56.17,92.38]
		end
		break
		break
	end

string d6P[57.41] <- 8.85
'''
		expect = '''Program([FuncDecl(Id(zQ0), [VarDecl(Id(Y__h), ArrayType([69.66], NumberType), None, None), VarDecl(Id(XxyQ), ArrayType([21.05, 17.2], StringType), None, None)], Return()), FuncDecl(Id(tEiQ), [VarDecl(Id(Zy), BoolType, None, None)], Return()), FuncDecl(Id(Er), [VarDecl(Id(pMq), ArrayType([52.15, 15.94], NumberType), None, None)], Return(Id(AA))), FuncDecl(Id(IVu), [VarDecl(Id(a09), ArrayType([48.56], NumberType), None, None), VarDecl(Id(oLn), NumberType, None, None), VarDecl(Id(pg2), ArrayType([1.52, 78.36, 78.82], BoolType), None, None)], Block([Block([Break, Break, VarDecl(Id(e0), ArrayType([56.17, 92.38], StringType), None, None)]), Break, Break])), VarDecl(Id(d6P), ArrayType([57.41], StringType), None, NumLit(8.85))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115208))

	def test_21530115209(self):
		input = '''
func ry ()
	return true
func O6Bp (string Td)
	return UIrP

bool OLkE
dynamic Y_J <- "xRj"
'''
		expect = '''Program([FuncDecl(Id(ry), [], Return(BooleanLit(True))), FuncDecl(Id(O6Bp), [VarDecl(Id(Td), StringType, None, None)], Return(Id(UIrP))), VarDecl(Id(OLkE), BoolType, None, None), VarDecl(Id(Y_J), None, dynamic, StringLit(xRj))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115209))

	def test_21530115210(self):
		input = '''
func Nxt (number jWp)
	return
func jiV (bool J0un, number ow)	return
'''
		expect = '''Program([FuncDecl(Id(Nxt), [VarDecl(Id(jWp), NumberType, None, None)], Return()), FuncDecl(Id(jiV), [VarDecl(Id(J0un), BoolType, None, None), VarDecl(Id(ow), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115210))

	def test_21530115211(self):
		input = '''
func gKxU ()
	return 64.6
number UQm <- "x"
bool Ad[82.84,76.11]
bool tmt[65.76]
dynamic cD3d <- true
'''
		expect = '''Program([FuncDecl(Id(gKxU), [], Return(NumLit(64.6))), VarDecl(Id(UQm), NumberType, None, StringLit(x)), VarDecl(Id(Ad), ArrayType([82.84, 76.11], BoolType), None, None), VarDecl(Id(tmt), ArrayType([65.76], BoolType), None, None), VarDecl(Id(cD3d), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115211))

	def test_21530115212(self):
		input = '''
func Pq (number Sy, bool Ntvf, bool KMT[90.23])
	begin
		cf[eAac, UY, true] <- "Rygn"
		begin
			number xte[3.17,48.77] <- true
		end
		break
	end

func P2 ()	return uOs
'''
		expect = '''Program([FuncDecl(Id(Pq), [VarDecl(Id(Sy), NumberType, None, None), VarDecl(Id(Ntvf), BoolType, None, None), VarDecl(Id(KMT), ArrayType([90.23], BoolType), None, None)], Block([AssignStmt(ArrayCell(Id(cf), [Id(eAac), Id(UY), BooleanLit(True)]), StringLit(Rygn)), Block([VarDecl(Id(xte), ArrayType([3.17, 48.77], NumberType), None, BooleanLit(True))]), Break])), FuncDecl(Id(P2), [], Return(Id(uOs)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115212))

	def test_21530115213(self):
		input = '''
string cCKn[5.2,81.78] <- true
func rUF (string Lw, bool sL_T)	begin
	end
func My (string Ddj3, number ANOL[33.28,95.83,29.76], string Mb[83.51,62.96,44.38])	return
string Rpsv[79.85,40.41] <- 39.6
'''
		expect = '''Program([VarDecl(Id(cCKn), ArrayType([5.2, 81.78], StringType), None, BooleanLit(True)), FuncDecl(Id(rUF), [VarDecl(Id(Lw), StringType, None, None), VarDecl(Id(sL_T), BoolType, None, None)], Block([])), FuncDecl(Id(My), [VarDecl(Id(Ddj3), StringType, None, None), VarDecl(Id(ANOL), ArrayType([33.28, 95.83, 29.76], NumberType), None, None), VarDecl(Id(Mb), ArrayType([83.51, 62.96, 44.38], StringType), None, None)], Return()), VarDecl(Id(Rpsv), ArrayType([79.85, 40.41], StringType), None, NumLit(39.6))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115213))

	def test_21530115214(self):
		input = '''
number KZj[91.97,11.81,91.99] <- "o"
bool N_j
bool SGtb <- false
func LQ ()	begin
		begin
		end
		continue
		return
	end

string Nic
'''
		expect = '''Program([VarDecl(Id(KZj), ArrayType([91.97, 11.81, 91.99], NumberType), None, StringLit(o)), VarDecl(Id(N_j), BoolType, None, None), VarDecl(Id(SGtb), BoolType, None, BooleanLit(False)), FuncDecl(Id(LQ), [], Block([Block([]), Continue, Return()])), VarDecl(Id(Nic), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115214))

	def test_21530115215(self):
		input = '''
func xh2G (number lBe)
	return
'''
		expect = '''Program([FuncDecl(Id(xh2G), [VarDecl(Id(lBe), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115215))

	def test_21530115216(self):
		input = '''
func Wx (number Z2H, number X4w[50.67,36.02,4.78], string dY6)
	begin
	end
dynamic kE4 <- false
'''
		expect = '''Program([FuncDecl(Id(Wx), [VarDecl(Id(Z2H), NumberType, None, None), VarDecl(Id(X4w), ArrayType([50.67, 36.02, 4.78], NumberType), None, None), VarDecl(Id(dY6), StringType, None, None)], Block([])), VarDecl(Id(kE4), None, dynamic, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115216))

	def test_21530115217(self):
		input = '''
bool Fc0[55.41,1.57,67.05]
'''
		expect = '''Program([VarDecl(Id(Fc0), ArrayType([55.41, 1.57, 67.05], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115217))

	def test_21530115218(self):
		input = '''
number PB <- mnu
string MWdd <- "kQ"
bool Wv[6.86,20.0,57.51] <- gJ
var Ns <- false
'''
		expect = '''Program([VarDecl(Id(PB), NumberType, None, Id(mnu)), VarDecl(Id(MWdd), StringType, None, StringLit(kQ)), VarDecl(Id(Wv), ArrayType([6.86, 20.0, 57.51], BoolType), None, Id(gJ)), VarDecl(Id(Ns), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115218))

	def test_21530115219(self):
		input = '''
bool SrEO[91.4,45.23]
bool nPy
number NSHz[9.44,90.26,71.99]
'''
		expect = '''Program([VarDecl(Id(SrEO), ArrayType([91.4, 45.23], BoolType), None, None), VarDecl(Id(nPy), BoolType, None, None), VarDecl(Id(NSHz), ArrayType([9.44, 90.26, 71.99], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115219))

	def test_21530115220(self):
		input = '''
number AWD[2.17,43.48,35.1] <- "z"
func aIj (number H0B, string NTi9, bool dV[13.47])
	return df

func TlzX (number Wbh, number LZ6[96.21,55.43,55.98], number jvx[59.79,56.46])
	begin
		number D9XO[46.35,11.64]
		return BsbL
		return
	end
'''
		expect = '''Program([VarDecl(Id(AWD), ArrayType([2.17, 43.48, 35.1], NumberType), None, StringLit(z)), FuncDecl(Id(aIj), [VarDecl(Id(H0B), NumberType, None, None), VarDecl(Id(NTi9), StringType, None, None), VarDecl(Id(dV), ArrayType([13.47], BoolType), None, None)], Return(Id(df))), FuncDecl(Id(TlzX), [VarDecl(Id(Wbh), NumberType, None, None), VarDecl(Id(LZ6), ArrayType([96.21, 55.43, 55.98], NumberType), None, None), VarDecl(Id(jvx), ArrayType([59.79, 56.46], NumberType), None, None)], Block([VarDecl(Id(D9XO), ArrayType([46.35, 11.64], NumberType), None, None), Return(Id(BsbL)), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115220))

	def test_21530115221(self):
		input = '''
func ju (string TMO[13.64,74.75,36.81], string l88[88.26,19.19])	return "GbAU"

func dpMd ()
	return

number w6[28.93]
'''
		expect = '''Program([FuncDecl(Id(ju), [VarDecl(Id(TMO), ArrayType([13.64, 74.75, 36.81], StringType), None, None), VarDecl(Id(l88), ArrayType([88.26, 19.19], StringType), None, None)], Return(StringLit(GbAU))), FuncDecl(Id(dpMd), [], Return()), VarDecl(Id(w6), ArrayType([28.93], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115221))

	def test_21530115222(self):
		input = '''
number CmjS
func Ajgw (number ORZ[69.73], bool pA_m, number qeY[20.62])
	return true

'''
		expect = '''Program([VarDecl(Id(CmjS), NumberType, None, None), FuncDecl(Id(Ajgw), [VarDecl(Id(ORZ), ArrayType([69.73], NumberType), None, None), VarDecl(Id(pA_m), BoolType, None, None), VarDecl(Id(qeY), ArrayType([20.62], NumberType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115222))

	def test_21530115223(self):
		input = '''
bool C2[19.45]
func w7 (string YL, number ox[18.74,36.32], bool R2[84.8,16.17,67.02])	begin
		NK("yk", Di)
		return mYN
	end
func Q306 ()
	return

func xjAi (number YzhB[35.64])	begin
		continue
		RS[true] <- "leolG"
		continue
	end

func f4 ()
	begin
		break
		return
		continue
	end

'''
		expect = '''Program([VarDecl(Id(C2), ArrayType([19.45], BoolType), None, None), FuncDecl(Id(w7), [VarDecl(Id(YL), StringType, None, None), VarDecl(Id(ox), ArrayType([18.74, 36.32], NumberType), None, None), VarDecl(Id(R2), ArrayType([84.8, 16.17, 67.02], BoolType), None, None)], Block([CallStmt(Id(NK), [StringLit(yk), Id(Di)]), Return(Id(mYN))])), FuncDecl(Id(Q306), [], Return()), FuncDecl(Id(xjAi), [VarDecl(Id(YzhB), ArrayType([35.64], NumberType), None, None)], Block([Continue, AssignStmt(ArrayCell(Id(RS), [BooleanLit(True)]), StringLit(leolG)), Continue])), FuncDecl(Id(f4), [], Block([Break, Return(), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115223))

	def test_21530115224(self):
		input = '''
func mO (string Ul)
	begin
	end
func q30 (string j0e[78.72])
	return Jf

func t8 (number bI9x[71.35,70.27,43.37], number lh, string ZP[90.87,2.52])
	return

func kI ()	return 65.35

func OUDZ (bool kG1X[71.66], bool vmI, number K3Vg)
	return 25.84

'''
		expect = '''Program([FuncDecl(Id(mO), [VarDecl(Id(Ul), StringType, None, None)], Block([])), FuncDecl(Id(q30), [VarDecl(Id(j0e), ArrayType([78.72], StringType), None, None)], Return(Id(Jf))), FuncDecl(Id(t8), [VarDecl(Id(bI9x), ArrayType([71.35, 70.27, 43.37], NumberType), None, None), VarDecl(Id(lh), NumberType, None, None), VarDecl(Id(ZP), ArrayType([90.87, 2.52], StringType), None, None)], Return()), FuncDecl(Id(kI), [], Return(NumLit(65.35))), FuncDecl(Id(OUDZ), [VarDecl(Id(kG1X), ArrayType([71.66], BoolType), None, None), VarDecl(Id(vmI), BoolType, None, None), VarDecl(Id(K3Vg), NumberType, None, None)], Return(NumLit(25.84)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115224))

	def test_21530115225(self):
		input = '''
func N31A ()	return
dynamic ZD
number tu[70.69] <- false
'''
		expect = '''Program([FuncDecl(Id(N31A), [], Return()), VarDecl(Id(ZD), None, dynamic, None), VarDecl(Id(tu), ArrayType([70.69], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115225))

	def test_21530115226(self):
		input = '''
dynamic Mi <- 66.34
string PEWH[26.03,22.97,26.67] <- "q"
bool G9[82.12]
bool FO[86.74,82.01]
bool APhl[45.63,85.5]
'''
		expect = '''Program([VarDecl(Id(Mi), None, dynamic, NumLit(66.34)), VarDecl(Id(PEWH), ArrayType([26.03, 22.97, 26.67], StringType), None, StringLit(q)), VarDecl(Id(G9), ArrayType([82.12], BoolType), None, None), VarDecl(Id(FO), ArrayType([86.74, 82.01], BoolType), None, None), VarDecl(Id(APhl), ArrayType([45.63, 85.5], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115226))

	def test_21530115227(self):
		input = '''
func jb61 (number tdaC, number qUcC[88.79,4.58])	return 8.81
var fCAs <- VDfC
'''
		expect = '''Program([FuncDecl(Id(jb61), [VarDecl(Id(tdaC), NumberType, None, None), VarDecl(Id(qUcC), ArrayType([88.79, 4.58], NumberType), None, None)], Return(NumLit(8.81))), VarDecl(Id(fCAs), None, var, Id(VDfC))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115227))

	def test_21530115228(self):
		input = '''
number lN_n[58.08,10.57] <- 75.58
bool A4V2[97.41,52.72]
func ASQ (string XWx[27.23,89.68], number l_[7.08,83.38], bool w5wz[29.15])
	begin
		begin
			bool q4r
			return
		end
		return XiSl
	end
string s1[75.91,70.16] <- true
number Qb[20.09,41.75] <- 9.69
'''
		expect = '''Program([VarDecl(Id(lN_n), ArrayType([58.08, 10.57], NumberType), None, NumLit(75.58)), VarDecl(Id(A4V2), ArrayType([97.41, 52.72], BoolType), None, None), FuncDecl(Id(ASQ), [VarDecl(Id(XWx), ArrayType([27.23, 89.68], StringType), None, None), VarDecl(Id(l_), ArrayType([7.08, 83.38], NumberType), None, None), VarDecl(Id(w5wz), ArrayType([29.15], BoolType), None, None)], Block([Block([VarDecl(Id(q4r), BoolType, None, None), Return()]), Return(Id(XiSl))])), VarDecl(Id(s1), ArrayType([75.91, 70.16], StringType), None, BooleanLit(True)), VarDecl(Id(Qb), ArrayType([20.09, 41.75], NumberType), None, NumLit(9.69))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115228))

	def test_21530115229(self):
		input = '''
bool OyE[7.91]
func qhb ()
	return "guG"

'''
		expect = '''Program([VarDecl(Id(OyE), ArrayType([7.91], BoolType), None, None), FuncDecl(Id(qhb), [], Return(StringLit(guG)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115229))

	def test_21530115230(self):
		input = '''
number yYzp
string vD[37.09] <- false
func rofL ()	return
'''
		expect = '''Program([VarDecl(Id(yYzp), NumberType, None, None), VarDecl(Id(vD), ArrayType([37.09], StringType), None, BooleanLit(False)), FuncDecl(Id(rofL), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115230))

	def test_21530115231(self):
		input = '''
bool Oqf
'''
		expect = '''Program([VarDecl(Id(Oqf), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115231))

	def test_21530115232(self):
		input = '''
string PcN5[84.01,70.96,40.5]
'''
		expect = '''Program([VarDecl(Id(PcN5), ArrayType([84.01, 70.96, 40.5], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115232))

	def test_21530115233(self):
		input = '''
func h5 (string rih[64.01], bool VAM0)
	begin
		continue
		begin
		end
		if (true)
		if ("P")
		return 40.57
		elif (false) string S7[50.82,75.26] <- azS
		else var wD_E <- false
		elif (Gm) bool Fn <- false
		elif (Ka8y) if (CG0) string LvG6[86.41,23.21,81.63]
		elif ("B")
		HK5()
		else bool T6[86.04,34.25,27.87]
	end

'''
		expect = '''Program([FuncDecl(Id(h5), [VarDecl(Id(rih), ArrayType([64.01], StringType), None, None), VarDecl(Id(VAM0), BoolType, None, None)], Block([Continue, Block([]), If((BooleanLit(True), If((StringLit(P), Return(NumLit(40.57))), [(BooleanLit(False), VarDecl(Id(S7), ArrayType([50.82, 75.26], StringType), None, Id(azS)))], VarDecl(Id(wD_E), None, var, BooleanLit(False)))), [(Id(Gm), VarDecl(Id(Fn), BoolType, None, BooleanLit(False))), (Id(Ka8y), If((Id(CG0), VarDecl(Id(LvG6), ArrayType([86.41, 23.21, 81.63], StringType), None, None)), [(StringLit(B), CallStmt(Id(HK5), []))], VarDecl(Id(T6), ArrayType([86.04, 34.25, 27.87], BoolType), None, None)))], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115233))

	def test_21530115234(self):
		input = '''
func KO (number DN[83.19], number xe, string n73)
	begin
		break
	end

dynamic gMr4
func vr3 (bool cl)	begin
	end

func w4 (string ulyW, bool cJ)
	begin
		number TsI[74.81,64.45]
		break
		Vy4M <- "RzRSG"
	end
number ZF2[36.04] <- false
'''
		expect = '''Program([FuncDecl(Id(KO), [VarDecl(Id(DN), ArrayType([83.19], NumberType), None, None), VarDecl(Id(xe), NumberType, None, None), VarDecl(Id(n73), StringType, None, None)], Block([Break])), VarDecl(Id(gMr4), None, dynamic, None), FuncDecl(Id(vr3), [VarDecl(Id(cl), BoolType, None, None)], Block([])), FuncDecl(Id(w4), [VarDecl(Id(ulyW), StringType, None, None), VarDecl(Id(cJ), BoolType, None, None)], Block([VarDecl(Id(TsI), ArrayType([74.81, 64.45], NumberType), None, None), Break, AssignStmt(Id(Vy4M), StringLit(RzRSG))])), VarDecl(Id(ZF2), ArrayType([36.04], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115234))

	def test_21530115235(self):
		input = '''
func uyOi (number ZE5[23.4,96.81,89.18], string b4x)	begin
		VWY(false, "k")
		bool dX[14.85] <- 61.39
		Gg <- true
	end
number vZDB[8.08,60.0] <- QZL
number XB2F[81.36]
func Eb (bool vwB, number eJNg)
	return
bool New[11.37,95.81] <- 88.92
'''
		expect = '''Program([FuncDecl(Id(uyOi), [VarDecl(Id(ZE5), ArrayType([23.4, 96.81, 89.18], NumberType), None, None), VarDecl(Id(b4x), StringType, None, None)], Block([CallStmt(Id(VWY), [BooleanLit(False), StringLit(k)]), VarDecl(Id(dX), ArrayType([14.85], BoolType), None, NumLit(61.39)), AssignStmt(Id(Gg), BooleanLit(True))])), VarDecl(Id(vZDB), ArrayType([8.08, 60.0], NumberType), None, Id(QZL)), VarDecl(Id(XB2F), ArrayType([81.36], NumberType), None, None), FuncDecl(Id(Eb), [VarDecl(Id(vwB), BoolType, None, None), VarDecl(Id(eJNg), NumberType, None, None)], Return()), VarDecl(Id(New), ArrayType([11.37, 95.81], BoolType), None, NumLit(88.92))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115235))

	def test_21530115236(self):
		input = '''
bool h8
func Ywia ()
	return 11.63
func o6 (bool AK_, bool xgYL[47.87,20.45], bool bQ[21.41,67.32])	return 79.98

number aCJS
func ZUPc (number As)	return
'''
		expect = '''Program([VarDecl(Id(h8), BoolType, None, None), FuncDecl(Id(Ywia), [], Return(NumLit(11.63))), FuncDecl(Id(o6), [VarDecl(Id(AK_), BoolType, None, None), VarDecl(Id(xgYL), ArrayType([47.87, 20.45], BoolType), None, None), VarDecl(Id(bQ), ArrayType([21.41, 67.32], BoolType), None, None)], Return(NumLit(79.98))), VarDecl(Id(aCJS), NumberType, None, None), FuncDecl(Id(ZUPc), [VarDecl(Id(As), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115236))

	def test_21530115237(self):
		input = '''
bool cJ
dynamic quJ <- svoj
func tr ()
	begin
		return yjf
		u9[42.42, 42.01, lj3Z] <- true
	end

func qn ()	begin
	end
'''
		expect = '''Program([VarDecl(Id(cJ), BoolType, None, None), VarDecl(Id(quJ), None, dynamic, Id(svoj)), FuncDecl(Id(tr), [], Block([Return(Id(yjf)), AssignStmt(ArrayCell(Id(u9), [NumLit(42.42), NumLit(42.01), Id(lj3Z)]), BooleanLit(True))])), FuncDecl(Id(qn), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115237))

	def test_21530115238(self):
		input = '''
func iD (bool aD)	return "L"
func gy (number r8S[34.69,87.45,20.77], bool Ci)	return

func gnS ()
	begin
		var DRz <- LU
	end

bool x4 <- "hNT"
'''
		expect = '''Program([FuncDecl(Id(iD), [VarDecl(Id(aD), BoolType, None, None)], Return(StringLit(L))), FuncDecl(Id(gy), [VarDecl(Id(r8S), ArrayType([34.69, 87.45, 20.77], NumberType), None, None), VarDecl(Id(Ci), BoolType, None, None)], Return()), FuncDecl(Id(gnS), [], Block([VarDecl(Id(DRz), None, var, Id(LU))])), VarDecl(Id(x4), BoolType, None, StringLit(hNT))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115238))

	def test_21530115239(self):
		input = '''
func uZ (string H0U[30.11])	return

'''
		expect = '''Program([FuncDecl(Id(uZ), [VarDecl(Id(H0U), ArrayType([30.11], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115239))

	def test_21530115240(self):
		input = '''
bool Auy[22.9,43.19,31.38] <- yk98
bool ywvE
'''
		expect = '''Program([VarDecl(Id(Auy), ArrayType([22.9, 43.19, 31.38], BoolType), None, Id(yk98)), VarDecl(Id(ywvE), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115240))

	def test_21530115241(self):
		input = '''
string Pk[12.95,37.71]
func wf (string FY3[86.34,1.64,28.13])
	begin
		begin
			continue
			continue
			continue
		end
		begin
			fP["JWCC", ofe] <- "OLIJ"
		end
	end

func diJd (bool HYp)
	begin
		bool wui[88.56,38.36]
		B2B <- 99.6
		continue
	end
func pK ()	return
string oK <- false
'''
		expect = '''Program([VarDecl(Id(Pk), ArrayType([12.95, 37.71], StringType), None, None), FuncDecl(Id(wf), [VarDecl(Id(FY3), ArrayType([86.34, 1.64, 28.13], StringType), None, None)], Block([Block([Continue, Continue, Continue]), Block([AssignStmt(ArrayCell(Id(fP), [StringLit(JWCC), Id(ofe)]), StringLit(OLIJ))])])), FuncDecl(Id(diJd), [VarDecl(Id(HYp), BoolType, None, None)], Block([VarDecl(Id(wui), ArrayType([88.56, 38.36], BoolType), None, None), AssignStmt(Id(B2B), NumLit(99.6)), Continue])), FuncDecl(Id(pK), [], Return()), VarDecl(Id(oK), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115241))

	def test_21530115242(self):
		input = '''
bool WwCs
'''
		expect = '''Program([VarDecl(Id(WwCs), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115242))

	def test_21530115243(self):
		input = '''
string kJ <- 13.93
number gsEi
dynamic Yn <- IS9a
'''
		expect = '''Program([VarDecl(Id(kJ), StringType, None, NumLit(13.93)), VarDecl(Id(gsEi), NumberType, None, None), VarDecl(Id(Yn), None, dynamic, Id(IS9a))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115243))

	def test_21530115244(self):
		input = '''
func hM (string N2)
	begin
	end

func bU (number wmZ2[29.88], string q7, bool wqf)
	begin
		for OaJ until true by true
			number DBs[31.25]
	end

func I15n (string Ii)
	return

'''
		expect = '''Program([FuncDecl(Id(hM), [VarDecl(Id(N2), StringType, None, None)], Block([])), FuncDecl(Id(bU), [VarDecl(Id(wmZ2), ArrayType([29.88], NumberType), None, None), VarDecl(Id(q7), StringType, None, None), VarDecl(Id(wqf), BoolType, None, None)], Block([For(Id(OaJ), BooleanLit(True), BooleanLit(True), VarDecl(Id(DBs), ArrayType([31.25], NumberType), None, None))])), FuncDecl(Id(I15n), [VarDecl(Id(Ii), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115244))

	def test_21530115245(self):
		input = '''
func sb ()
	begin
	end

func kXDc (string FNc[81.9])
	return "HdkQ"
bool nSTe[37.37]
func fdn (number ls)
	return
'''
		expect = '''Program([FuncDecl(Id(sb), [], Block([])), FuncDecl(Id(kXDc), [VarDecl(Id(FNc), ArrayType([81.9], StringType), None, None)], Return(StringLit(HdkQ))), VarDecl(Id(nSTe), ArrayType([37.37], BoolType), None, None), FuncDecl(Id(fdn), [VarDecl(Id(ls), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115245))

	def test_21530115246(self):
		input = '''
func Flz (number AHVF, string aGHt[39.97,73.59], bool Zv[26.92,53.51,10.1])	return 68.45
func gKeN ()
	return

func YZ (bool IA[44.58,42.59])	return

number ri[58.0] <- "Bsz"
'''
		expect = '''Program([FuncDecl(Id(Flz), [VarDecl(Id(AHVF), NumberType, None, None), VarDecl(Id(aGHt), ArrayType([39.97, 73.59], StringType), None, None), VarDecl(Id(Zv), ArrayType([26.92, 53.51, 10.1], BoolType), None, None)], Return(NumLit(68.45))), FuncDecl(Id(gKeN), [], Return()), FuncDecl(Id(YZ), [VarDecl(Id(IA), ArrayType([44.58, 42.59], BoolType), None, None)], Return()), VarDecl(Id(ri), ArrayType([58.0], NumberType), None, StringLit(Bsz))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115246))

	def test_21530115247(self):
		input = '''
number OS[78.71]
number oma2
bool IJ
'''
		expect = '''Program([VarDecl(Id(OS), ArrayType([78.71], NumberType), None, None), VarDecl(Id(oma2), NumberType, None, None), VarDecl(Id(IJ), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115247))

	def test_21530115248(self):
		input = '''
bool wvT <- "xMZm"
func UCjr (bool Juc, bool IDi[42.9])	return
'''
		expect = '''Program([VarDecl(Id(wvT), BoolType, None, StringLit(xMZm)), FuncDecl(Id(UCjr), [VarDecl(Id(Juc), BoolType, None, None), VarDecl(Id(IDi), ArrayType([42.9], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115248))

	def test_21530115249(self):
		input = '''
func Ijrv (number d7Bz)	begin
		Xv[Db, NEsu, true] <- "fl"
		for rVIn until P4Bx by false
			continue
	end
func LG (bool civq, bool lB[46.78,17.91,34.88], number H2[34.05])	return
string vVj0[71.54] <- xb
'''
		expect = '''Program([FuncDecl(Id(Ijrv), [VarDecl(Id(d7Bz), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(Xv), [Id(Db), Id(NEsu), BooleanLit(True)]), StringLit(fl)), For(Id(rVIn), Id(P4Bx), BooleanLit(False), Continue)])), FuncDecl(Id(LG), [VarDecl(Id(civq), BoolType, None, None), VarDecl(Id(lB), ArrayType([46.78, 17.91, 34.88], BoolType), None, None), VarDecl(Id(H2), ArrayType([34.05], NumberType), None, None)], Return()), VarDecl(Id(vVj0), ArrayType([71.54], StringType), None, Id(xb))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115249))

	def test_21530115250(self):
		input = '''
string vRA[87.03] <- "KPUnX"
func ED ()
	return 9.42
func uc (number T6Q, bool IU5r, number lo[25.02,47.67,41.7])
	return

func dM4 (string XuoI, bool pR[26.53,8.63], number AV1N)
	return
'''
		expect = '''Program([VarDecl(Id(vRA), ArrayType([87.03], StringType), None, StringLit(KPUnX)), FuncDecl(Id(ED), [], Return(NumLit(9.42))), FuncDecl(Id(uc), [VarDecl(Id(T6Q), NumberType, None, None), VarDecl(Id(IU5r), BoolType, None, None), VarDecl(Id(lo), ArrayType([25.02, 47.67, 41.7], NumberType), None, None)], Return()), FuncDecl(Id(dM4), [VarDecl(Id(XuoI), StringType, None, None), VarDecl(Id(pR), ArrayType([26.53, 8.63], BoolType), None, None), VarDecl(Id(AV1N), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115250))

	def test_21530115251(self):
		input = '''
func jh (string z44k[1.05], string o5R)	begin
		Kx5Y["lLwGm", "diCxr"] <- true
		number f5c8[25.04,46.92] <- "ILerP"
		yR("g")
	end
'''
		expect = '''Program([FuncDecl(Id(jh), [VarDecl(Id(z44k), ArrayType([1.05], StringType), None, None), VarDecl(Id(o5R), StringType, None, None)], Block([AssignStmt(ArrayCell(Id(Kx5Y), [StringLit(lLwGm), StringLit(diCxr)]), BooleanLit(True)), VarDecl(Id(f5c8), ArrayType([25.04, 46.92], NumberType), None, StringLit(ILerP)), CallStmt(Id(yR), [StringLit(g)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115251))

	def test_21530115252(self):
		input = '''
string a46[68.73]
func uneo (bool Z1o4, bool EF[77.87,98.58])	return "h"

'''
		expect = '''Program([VarDecl(Id(a46), ArrayType([68.73], StringType), None, None), FuncDecl(Id(uneo), [VarDecl(Id(Z1o4), BoolType, None, None), VarDecl(Id(EF), ArrayType([77.87, 98.58], BoolType), None, None)], Return(StringLit(h)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115252))

	def test_21530115253(self):
		input = '''
dynamic qHB5
func i5Z (string ApGG, bool Ls2S[99.79,56.35,86.61], string MTjy[75.34,62.66,34.76])
	return "adwJa"
number gt[91.15,1.6]
number vE[37.49] <- "MWi"
func gR4 (string Spy[62.25], bool afu[93.98])
	begin
		return
		qcPA[45.0] <- 61.27
	end
'''
		expect = '''Program([VarDecl(Id(qHB5), None, dynamic, None), FuncDecl(Id(i5Z), [VarDecl(Id(ApGG), StringType, None, None), VarDecl(Id(Ls2S), ArrayType([99.79, 56.35, 86.61], BoolType), None, None), VarDecl(Id(MTjy), ArrayType([75.34, 62.66, 34.76], StringType), None, None)], Return(StringLit(adwJa))), VarDecl(Id(gt), ArrayType([91.15, 1.6], NumberType), None, None), VarDecl(Id(vE), ArrayType([37.49], NumberType), None, StringLit(MWi)), FuncDecl(Id(gR4), [VarDecl(Id(Spy), ArrayType([62.25], StringType), None, None), VarDecl(Id(afu), ArrayType([93.98], BoolType), None, None)], Block([Return(), AssignStmt(ArrayCell(Id(qcPA), [NumLit(45.0)]), NumLit(61.27))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115253))

	def test_21530115254(self):
		input = '''
func cKL ()	return "U"
func pvT (bool NXSa, number czD[70.58,11.18,68.56], bool G1RZ[90.98,83.72,15.36])	return false
func v2CW (string UiFh[6.71,45.71], bool rgqg)
	return IwxZ
func py (bool EU[92.16,22.62])	begin
		X0T("r", K1O)
	end
'''
		expect = '''Program([FuncDecl(Id(cKL), [], Return(StringLit(U))), FuncDecl(Id(pvT), [VarDecl(Id(NXSa), BoolType, None, None), VarDecl(Id(czD), ArrayType([70.58, 11.18, 68.56], NumberType), None, None), VarDecl(Id(G1RZ), ArrayType([90.98, 83.72, 15.36], BoolType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(v2CW), [VarDecl(Id(UiFh), ArrayType([6.71, 45.71], StringType), None, None), VarDecl(Id(rgqg), BoolType, None, None)], Return(Id(IwxZ))), FuncDecl(Id(py), [VarDecl(Id(EU), ArrayType([92.16, 22.62], BoolType), None, None)], Block([CallStmt(Id(X0T), [StringLit(r), Id(K1O)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115254))

	def test_21530115255(self):
		input = '''
func uCL (bool c8[68.38,9.19])	begin
		return XW
	end
func KhUM (string u6Q)
	return "Za"

'''
		expect = '''Program([FuncDecl(Id(uCL), [VarDecl(Id(c8), ArrayType([68.38, 9.19], BoolType), None, None)], Block([Return(Id(XW))])), FuncDecl(Id(KhUM), [VarDecl(Id(u6Q), StringType, None, None)], Return(StringLit(Za)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115255))

	def test_21530115256(self):
		input = '''
func wx ()
	return "dTW"
func Xue (number TZEC[86.35,97.01])	return

var FlA <- 30.43
'''
		expect = '''Program([FuncDecl(Id(wx), [], Return(StringLit(dTW))), FuncDecl(Id(Xue), [VarDecl(Id(TZEC), ArrayType([86.35, 97.01], NumberType), None, None)], Return()), VarDecl(Id(FlA), None, var, NumLit(30.43))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115256))

	def test_21530115257(self):
		input = '''
func ey (bool ez[92.37,83.34], bool ULL2[90.5,88.17,92.36], number wFg[33.39,0.83])	return "Emq"
'''
		expect = '''Program([FuncDecl(Id(ey), [VarDecl(Id(ez), ArrayType([92.37, 83.34], BoolType), None, None), VarDecl(Id(ULL2), ArrayType([90.5, 88.17, 92.36], BoolType), None, None), VarDecl(Id(wFg), ArrayType([33.39, 0.83], NumberType), None, None)], Return(StringLit(Emq)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115257))

	def test_21530115258(self):
		input = '''
func Ivsf (number JG, number u6Ff[33.44])
	begin
		string ac6[8.55]
	end
func NgN ()	begin
		begin
			for FdL0 until true by "webq"
				break
			begin
				return
				number x3Is <- "aLx"
				begin
					dynamic ELFQ <- true
					bool HbU[25.34,61.83]
				end
			end
		end
		return
	end
func I9 (number G6)	return

'''
		expect = '''Program([FuncDecl(Id(Ivsf), [VarDecl(Id(JG), NumberType, None, None), VarDecl(Id(u6Ff), ArrayType([33.44], NumberType), None, None)], Block([VarDecl(Id(ac6), ArrayType([8.55], StringType), None, None)])), FuncDecl(Id(NgN), [], Block([Block([For(Id(FdL0), BooleanLit(True), StringLit(webq), Break), Block([Return(), VarDecl(Id(x3Is), NumberType, None, StringLit(aLx)), Block([VarDecl(Id(ELFQ), None, dynamic, BooleanLit(True)), VarDecl(Id(HbU), ArrayType([25.34, 61.83], BoolType), None, None)])])]), Return()])), FuncDecl(Id(I9), [VarDecl(Id(G6), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115258))

	def test_21530115259(self):
		input = '''
bool MO4[13.65,80.69]
'''
		expect = '''Program([VarDecl(Id(MO4), ArrayType([13.65, 80.69], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115259))

	def test_21530115260(self):
		input = '''
func w4 (number cEyW, bool Ue4Z[92.98,92.68])	return
number hEQ[87.72]
func GXE (string ke0c)
	return 45.56

string SS
'''
		expect = '''Program([FuncDecl(Id(w4), [VarDecl(Id(cEyW), NumberType, None, None), VarDecl(Id(Ue4Z), ArrayType([92.98, 92.68], BoolType), None, None)], Return()), VarDecl(Id(hEQ), ArrayType([87.72], NumberType), None, None), FuncDecl(Id(GXE), [VarDecl(Id(ke0c), StringType, None, None)], Return(NumLit(45.56))), VarDecl(Id(SS), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115260))

	def test_21530115261(self):
		input = '''
func TA (bool kJ)
	begin
		break
	end

func Zp0i (string H2)
	begin
		if (IB)
		return 59.43
		elif (Lq)
		continue
		elif ("MoWLT") if ("Vkw")
		Nftl(DK, 28.52, DeD)
		elif ("FxLF") KKFu[FUK, "IC"] <- false
		elif (UGP)
		break
		elif ("UzZ") ML(8.21, Sa)
		elif (46.87) string qHHW <- 56.49
		else continue
		elif ("Bvxhv")
		string loX8[48.71,44.06,23.38] <- true
		elif ("Ye") bool h_
		break
	end

'''
		expect = '''Program([FuncDecl(Id(TA), [VarDecl(Id(kJ), BoolType, None, None)], Block([Break])), FuncDecl(Id(Zp0i), [VarDecl(Id(H2), StringType, None, None)], Block([If((Id(IB), Return(NumLit(59.43))), [(Id(Lq), Continue), (StringLit(MoWLT), If((StringLit(Vkw), CallStmt(Id(Nftl), [Id(DK), NumLit(28.52), Id(DeD)])), [(StringLit(FxLF), AssignStmt(ArrayCell(Id(KKFu), [Id(FUK), StringLit(IC)]), BooleanLit(False))), (Id(UGP), Break), (StringLit(UzZ), CallStmt(Id(ML), [NumLit(8.21), Id(Sa)])), (NumLit(46.87), VarDecl(Id(qHHW), StringType, None, NumLit(56.49)))], Continue)), (StringLit(Bvxhv), VarDecl(Id(loX8), ArrayType([48.71, 44.06, 23.38], StringType), None, BooleanLit(True))), (StringLit(Ye), VarDecl(Id(h_), BoolType, None, None))], None), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115261))

	def test_21530115262(self):
		input = '''
func efL ()	return
func iSpo (number KVC, number GEV)
	begin
		aF(P2, 68.45, 0.39)
		hf9C <- 27.96
	end

'''
		expect = '''Program([FuncDecl(Id(efL), [], Return()), FuncDecl(Id(iSpo), [VarDecl(Id(KVC), NumberType, None, None), VarDecl(Id(GEV), NumberType, None, None)], Block([CallStmt(Id(aF), [Id(P2), NumLit(68.45), NumLit(0.39)]), AssignStmt(Id(hf9C), NumLit(27.96))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115262))

	def test_21530115263(self):
		input = '''
string CK[22.47] <- "If"
dynamic tADh
func BFD7 (string vwE8[94.05], bool eG[81.76])	return
'''
		expect = '''Program([VarDecl(Id(CK), ArrayType([22.47], StringType), None, StringLit(If)), VarDecl(Id(tADh), None, dynamic, None), FuncDecl(Id(BFD7), [VarDecl(Id(vwE8), ArrayType([94.05], StringType), None, None), VarDecl(Id(eG), ArrayType([81.76], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115263))

	def test_21530115264(self):
		input = '''
var KoW <- HgBN
number IRiR[12.16,49.05] <- "J"
'''
		expect = '''Program([VarDecl(Id(KoW), None, var, Id(HgBN)), VarDecl(Id(IRiR), ArrayType([12.16, 49.05], NumberType), None, StringLit(J))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115264))

	def test_21530115265(self):
		input = '''
string aR <- "Tn"
number l3Xv[9.41,17.08,43.34] <- "q"
func XJwv ()	return DHt
func KKA (bool wP5[67.74,69.04,56.65], number SN, string Xlmt[54.35,29.82,19.92])	return JPw
func qx ()	begin
	end
'''
		expect = '''Program([VarDecl(Id(aR), StringType, None, StringLit(Tn)), VarDecl(Id(l3Xv), ArrayType([9.41, 17.08, 43.34], NumberType), None, StringLit(q)), FuncDecl(Id(XJwv), [], Return(Id(DHt))), FuncDecl(Id(KKA), [VarDecl(Id(wP5), ArrayType([67.74, 69.04, 56.65], BoolType), None, None), VarDecl(Id(SN), NumberType, None, None), VarDecl(Id(Xlmt), ArrayType([54.35, 29.82, 19.92], StringType), None, None)], Return(Id(JPw))), FuncDecl(Id(qx), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115265))

	def test_21530115266(self):
		input = '''
string mcm
dynamic ko
bool EZWE
'''
		expect = '''Program([VarDecl(Id(mcm), StringType, None, None), VarDecl(Id(ko), None, dynamic, None), VarDecl(Id(EZWE), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115266))

	def test_21530115267(self):
		input = '''
func Z5bb (number qb4)
	return UfEo
'''
		expect = '''Program([FuncDecl(Id(Z5bb), [VarDecl(Id(qb4), NumberType, None, None)], Return(Id(UfEo)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115267))

	def test_21530115268(self):
		input = '''
func Na ()
	return
'''
		expect = '''Program([FuncDecl(Id(Na), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115268))

	def test_21530115269(self):
		input = '''
string AvBR[73.45,74.5]
func nX5 (string NhP, number Cw)	return

'''
		expect = '''Program([VarDecl(Id(AvBR), ArrayType([73.45, 74.5], StringType), None, None), FuncDecl(Id(nX5), [VarDecl(Id(NhP), StringType, None, None), VarDecl(Id(Cw), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115269))

	def test_21530115270(self):
		input = '''
string Re[36.18,28.14] <- false
'''
		expect = '''Program([VarDecl(Id(Re), ArrayType([36.18, 28.14], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115270))

	def test_21530115271(self):
		input = '''
string r0b[4.59] <- "NTixD"
func PPQ (bool G7IE[37.76,40.13,32.56], bool pv4q, number v8[72.37,8.76,37.96])	return

func hE ()
	return "uCfc"
func hde8 ()
	return "S"
var XY <- OaA
'''
		expect = '''Program([VarDecl(Id(r0b), ArrayType([4.59], StringType), None, StringLit(NTixD)), FuncDecl(Id(PPQ), [VarDecl(Id(G7IE), ArrayType([37.76, 40.13, 32.56], BoolType), None, None), VarDecl(Id(pv4q), BoolType, None, None), VarDecl(Id(v8), ArrayType([72.37, 8.76, 37.96], NumberType), None, None)], Return()), FuncDecl(Id(hE), [], Return(StringLit(uCfc))), FuncDecl(Id(hde8), [], Return(StringLit(S))), VarDecl(Id(XY), None, var, Id(OaA))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115271))

	def test_21530115272(self):
		input = '''
string CX[79.77,21.65] <- l4
func BHtR (bool Vh2[42.09], string PF[62.03,9.88,59.15])	return
string WiX <- "QOay"
func XA (number RE)
	return vS
'''
		expect = '''Program([VarDecl(Id(CX), ArrayType([79.77, 21.65], StringType), None, Id(l4)), FuncDecl(Id(BHtR), [VarDecl(Id(Vh2), ArrayType([42.09], BoolType), None, None), VarDecl(Id(PF), ArrayType([62.03, 9.88, 59.15], StringType), None, None)], Return()), VarDecl(Id(WiX), StringType, None, StringLit(QOay)), FuncDecl(Id(XA), [VarDecl(Id(RE), NumberType, None, None)], Return(Id(vS)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115272))

	def test_21530115273(self):
		input = '''
bool JG2V
bool DlM_[76.98,1.19] <- true
bool n9V[39.23] <- Cnp
func OB (string uZov, bool gkYj)	begin
	end
'''
		expect = '''Program([VarDecl(Id(JG2V), BoolType, None, None), VarDecl(Id(DlM_), ArrayType([76.98, 1.19], BoolType), None, BooleanLit(True)), VarDecl(Id(n9V), ArrayType([39.23], BoolType), None, Id(Cnp)), FuncDecl(Id(OB), [VarDecl(Id(uZov), StringType, None, None), VarDecl(Id(gkYj), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115273))

	def test_21530115274(self):
		input = '''
func y6Hr (string r_2[49.38])	begin
		break
		begin
			return
		end
	end
func EL (number sYoq[55.77], bool z0L9[77.56,51.01], string QcL)
	return "lZ"

number eux6[12.18,10.29,33.76]
'''
		expect = '''Program([FuncDecl(Id(y6Hr), [VarDecl(Id(r_2), ArrayType([49.38], StringType), None, None)], Block([Break, Block([Return()])])), FuncDecl(Id(EL), [VarDecl(Id(sYoq), ArrayType([55.77], NumberType), None, None), VarDecl(Id(z0L9), ArrayType([77.56, 51.01], BoolType), None, None), VarDecl(Id(QcL), StringType, None, None)], Return(StringLit(lZ))), VarDecl(Id(eux6), ArrayType([12.18, 10.29, 33.76], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115274))

	def test_21530115275(self):
		input = '''
func T1M (number wt)	return

func dJ (string li[24.28,12.61,11.57])
	return

func kEv (bool Nx[64.42,5.86,35.15], number w1eg, string gSkj)	begin
		continue
		begin
		end
		break
	end

number aq <- 74.13
func PAz (bool dJr)
	return true

'''
		expect = '''Program([FuncDecl(Id(T1M), [VarDecl(Id(wt), NumberType, None, None)], Return()), FuncDecl(Id(dJ), [VarDecl(Id(li), ArrayType([24.28, 12.61, 11.57], StringType), None, None)], Return()), FuncDecl(Id(kEv), [VarDecl(Id(Nx), ArrayType([64.42, 5.86, 35.15], BoolType), None, None), VarDecl(Id(w1eg), NumberType, None, None), VarDecl(Id(gSkj), StringType, None, None)], Block([Continue, Block([]), Break])), VarDecl(Id(aq), NumberType, None, NumLit(74.13)), FuncDecl(Id(PAz), [VarDecl(Id(dJr), BoolType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115275))

	def test_21530115276(self):
		input = '''
func fo ()
	return false
dynamic dy9l <- bh
func gw (bool UkT7, bool Krg[63.26,97.81])
	return true
string IXJ[34.17,29.47,61.43] <- 52.35
string Uu[98.78,30.23,48.39]
'''
		expect = '''Program([FuncDecl(Id(fo), [], Return(BooleanLit(False))), VarDecl(Id(dy9l), None, dynamic, Id(bh)), FuncDecl(Id(gw), [VarDecl(Id(UkT7), BoolType, None, None), VarDecl(Id(Krg), ArrayType([63.26, 97.81], BoolType), None, None)], Return(BooleanLit(True))), VarDecl(Id(IXJ), ArrayType([34.17, 29.47, 61.43], StringType), None, NumLit(52.35)), VarDecl(Id(Uu), ArrayType([98.78, 30.23, 48.39], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115276))

	def test_21530115277(self):
		input = '''
func OQ8F (number Ld0I, bool QL[66.49,77.08,4.02], string xgS)
	return
func YK1j (bool raHZ[67.55,81.95,34.81], bool w1o)
	begin
		for x25Q until 4.63 by true
			number fmP <- "d"
		R0h[i7uk] <- 43.21
	end
bool QLSz <- false
'''
		expect = '''Program([FuncDecl(Id(OQ8F), [VarDecl(Id(Ld0I), NumberType, None, None), VarDecl(Id(QL), ArrayType([66.49, 77.08, 4.02], BoolType), None, None), VarDecl(Id(xgS), StringType, None, None)], Return()), FuncDecl(Id(YK1j), [VarDecl(Id(raHZ), ArrayType([67.55, 81.95, 34.81], BoolType), None, None), VarDecl(Id(w1o), BoolType, None, None)], Block([For(Id(x25Q), NumLit(4.63), BooleanLit(True), VarDecl(Id(fmP), NumberType, None, StringLit(d))), AssignStmt(ArrayCell(Id(R0h), [Id(i7uk)]), NumLit(43.21))])), VarDecl(Id(QLSz), BoolType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115277))

	def test_21530115278(self):
		input = '''
func VNCM (string sWT)	begin
		number OD[85.58,57.97] <- FGIK
		if (false)
		var wHT <- 75.76
		elif (be)
		continue
		elif ("h")
		begin
			if (FK2Z) for aY until "RJrA" by true
				if (f8I)
				if (mg)
				Umn(false, YDI)
				elif (EI) GdI <- 88.47
			elif (false)
			string YuG[75.42] <- s1
			elif (true)
			break
			elif (true)
			return
			elif (Nd) WpYF <- 36.41
			else return 76.47
		end
		elif (82.62) if ("MOh") for EPE until "hBVX" by "pE"
			continue
		elif ("SJwcx")
		continue
		elif (61.4) for c3 until true by true
			continue
		elif (68.34) Xqo("XAOFJ", 23.29)
		else for qPx4 until true by u5
			for bS until sem by 45.71
				begin
					SFlr <- true
					continue
					if (Asr) break
					elif (49.58)
					if (true)
					begin
						kS99()
						if (true) bool pu[89.22] <- false
						else begin
							for mvuU until false by false
								break
							continue
							SCt <- true
						end
					end
					elif ("MQ")
					Mw(false, Wt, false)
					else Xg7("h")
					elif ("g") kLAc[37.44] <- false
					else break
				end
		else Qm()
	end
func alAS ()	return "n"

'''
		expect = '''Program([FuncDecl(Id(VNCM), [VarDecl(Id(sWT), StringType, None, None)], Block([VarDecl(Id(OD), ArrayType([85.58, 57.97], NumberType), None, Id(FGIK)), If((BooleanLit(False), VarDecl(Id(wHT), None, var, NumLit(75.76))), [(Id(be), Continue), (StringLit(h), Block([If((Id(FK2Z), For(Id(aY), StringLit(RJrA), BooleanLit(True), If((Id(f8I), If((Id(mg), CallStmt(Id(Umn), [BooleanLit(False), Id(YDI)])), [(Id(EI), AssignStmt(Id(GdI), NumLit(88.47))), (BooleanLit(False), VarDecl(Id(YuG), ArrayType([75.42], StringType), None, Id(s1))), (BooleanLit(True), Break), (BooleanLit(True), Return()), (Id(Nd), AssignStmt(Id(WpYF), NumLit(36.41)))], Return(NumLit(76.47)))), [], None))), [], None)])), (NumLit(82.62), If((StringLit(MOh), For(Id(EPE), StringLit(hBVX), StringLit(pE), Continue)), [(StringLit(SJwcx), Continue), (NumLit(61.4), For(Id(c3), BooleanLit(True), BooleanLit(True), Continue)), (NumLit(68.34), CallStmt(Id(Xqo), [StringLit(XAOFJ), NumLit(23.29)]))], For(Id(qPx4), BooleanLit(True), Id(u5), For(Id(bS), Id(sem), NumLit(45.71), Block([AssignStmt(Id(SFlr), BooleanLit(True)), Continue, If((Id(Asr), Break), [(NumLit(49.58), If((BooleanLit(True), Block([CallStmt(Id(kS99), []), If((BooleanLit(True), VarDecl(Id(pu), ArrayType([89.22], BoolType), None, BooleanLit(False))), [], Block([For(Id(mvuU), BooleanLit(False), BooleanLit(False), Break), Continue, AssignStmt(Id(SCt), BooleanLit(True))]))])), [(StringLit(MQ), CallStmt(Id(Mw), [BooleanLit(False), Id(Wt), BooleanLit(False)]))], CallStmt(Id(Xg7), [StringLit(h)]))), (StringLit(g), AssignStmt(ArrayCell(Id(kLAc), [NumLit(37.44)]), BooleanLit(False)))], Break)])))))], CallStmt(Id(Qm), []))])), FuncDecl(Id(alAS), [], Return(StringLit(n)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115278))

	def test_21530115279(self):
		input = '''
number MA[74.11,96.04,18.57] <- 14.41
func Fi (string dDii, string Vp)
	begin
		k2[false] <- 96.63
		for Dx until false by pCX
			return
		begin
			number Jca[19.04,60.31] <- true
			continue
			continue
		end
	end
func Ij ()
	begin
		DX <- GYjd
	end

number EsLI[6.65]
'''
		expect = '''Program([VarDecl(Id(MA), ArrayType([74.11, 96.04, 18.57], NumberType), None, NumLit(14.41)), FuncDecl(Id(Fi), [VarDecl(Id(dDii), StringType, None, None), VarDecl(Id(Vp), StringType, None, None)], Block([AssignStmt(ArrayCell(Id(k2), [BooleanLit(False)]), NumLit(96.63)), For(Id(Dx), BooleanLit(False), Id(pCX), Return()), Block([VarDecl(Id(Jca), ArrayType([19.04, 60.31], NumberType), None, BooleanLit(True)), Continue, Continue])])), FuncDecl(Id(Ij), [], Block([AssignStmt(Id(DX), Id(GYjd))])), VarDecl(Id(EsLI), ArrayType([6.65], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115279))

	def test_21530115280(self):
		input = '''
func yzj (bool EfEi, string Cz)
	return true
bool Lej
func TSD5 (number HE, bool QDO, bool YIJ)	return

'''
		expect = '''Program([FuncDecl(Id(yzj), [VarDecl(Id(EfEi), BoolType, None, None), VarDecl(Id(Cz), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(Lej), BoolType, None, None), FuncDecl(Id(TSD5), [VarDecl(Id(HE), NumberType, None, None), VarDecl(Id(QDO), BoolType, None, None), VarDecl(Id(YIJ), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115280))

	def test_21530115281(self):
		input = '''
string usEw[68.31,78.23,57.67] <- false
'''
		expect = '''Program([VarDecl(Id(usEw), ArrayType([68.31, 78.23, 57.67], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115281))

	def test_21530115282(self):
		input = '''
func J0aQ ()	begin
		break
	end
func LNNc (string oN[29.01,73.43,37.99], string DS, string sma[61.24,55.61,40.08])	begin
		if (false) break
		elif (true)
		number g5z[74.01,2.33,70.63]
		else for Ud until "D" by false
			break
		break
		return "WdFnG"
	end
func IYc (bool gqb[30.92,76.39], string lwFZ[66.84,48.29,89.45])	return "V"

'''
		expect = '''Program([FuncDecl(Id(J0aQ), [], Block([Break])), FuncDecl(Id(LNNc), [VarDecl(Id(oN), ArrayType([29.01, 73.43, 37.99], StringType), None, None), VarDecl(Id(DS), StringType, None, None), VarDecl(Id(sma), ArrayType([61.24, 55.61, 40.08], StringType), None, None)], Block([If((BooleanLit(False), Break), [(BooleanLit(True), VarDecl(Id(g5z), ArrayType([74.01, 2.33, 70.63], NumberType), None, None))], For(Id(Ud), StringLit(D), BooleanLit(False), Break)), Break, Return(StringLit(WdFnG))])), FuncDecl(Id(IYc), [VarDecl(Id(gqb), ArrayType([30.92, 76.39], BoolType), None, None), VarDecl(Id(lwFZ), ArrayType([66.84, 48.29, 89.45], StringType), None, None)], Return(StringLit(V)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115282))

	def test_21530115283(self):
		input = '''
func Myg (bool yyi)
	begin
		for HJO3 until 67.62 by false
			begin
			end
		DOej(30.0, true)
	end
func XH (bool Zoh, string oq59, number ZpJu)	return
func WWzF (number AqTz[87.0,45.44,69.7], number qJB[26.69])	return 51.2

'''
		expect = '''Program([FuncDecl(Id(Myg), [VarDecl(Id(yyi), BoolType, None, None)], Block([For(Id(HJO3), NumLit(67.62), BooleanLit(False), Block([])), CallStmt(Id(DOej), [NumLit(30.0), BooleanLit(True)])])), FuncDecl(Id(XH), [VarDecl(Id(Zoh), BoolType, None, None), VarDecl(Id(oq59), StringType, None, None), VarDecl(Id(ZpJu), NumberType, None, None)], Return()), FuncDecl(Id(WWzF), [VarDecl(Id(AqTz), ArrayType([87.0, 45.44, 69.7], NumberType), None, None), VarDecl(Id(qJB), ArrayType([26.69], NumberType), None, None)], Return(NumLit(51.2)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115283))

	def test_21530115284(self):
		input = '''
number Makq[25.21,48.11,64.2] <- "zSASZ"
'''
		expect = '''Program([VarDecl(Id(Makq), ArrayType([25.21, 48.11, 64.2], NumberType), None, StringLit(zSASZ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115284))

	def test_21530115285(self):
		input = '''
string dV[36.23,54.36,34.57] <- false
func Xjh (string t6MN[69.59])
	return

'''
		expect = '''Program([VarDecl(Id(dV), ArrayType([36.23, 54.36, 34.57], StringType), None, BooleanLit(False)), FuncDecl(Id(Xjh), [VarDecl(Id(t6MN), ArrayType([69.59], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115285))

	def test_21530115286(self):
		input = '''
bool du
func EX (string OpC[65.85,39.59])
	begin
		begin
			begin
				break
				continue
				continue
			end
		end
	end
number Pub[96.2,92.82] <- MnT
'''
		expect = '''Program([VarDecl(Id(du), BoolType, None, None), FuncDecl(Id(EX), [VarDecl(Id(OpC), ArrayType([65.85, 39.59], StringType), None, None)], Block([Block([Block([Break, Continue, Continue])])])), VarDecl(Id(Pub), ArrayType([96.2, 92.82], NumberType), None, Id(MnT))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115286))

	def test_21530115287(self):
		input = '''
bool ntsJ <- 12.03
bool RC <- bBs
string XEbJ[62.48] <- 36.45
'''
		expect = '''Program([VarDecl(Id(ntsJ), BoolType, None, NumLit(12.03)), VarDecl(Id(RC), BoolType, None, Id(bBs)), VarDecl(Id(XEbJ), ArrayType([62.48], StringType), None, NumLit(36.45))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115287))

	def test_21530115288(self):
		input = '''
func VO (number sqe[36.85], string cYt[31.88,55.27,29.94], number wR)
	return ZB
func TvbJ (number KKbZ[28.93])
	begin
		number K78I[78.8]
		PT7X()
		continue
	end
number cee[35.59,1.68,62.97] <- "f"
number t9u[27.81,50.2,47.95] <- false
'''
		expect = '''Program([FuncDecl(Id(VO), [VarDecl(Id(sqe), ArrayType([36.85], NumberType), None, None), VarDecl(Id(cYt), ArrayType([31.88, 55.27, 29.94], StringType), None, None), VarDecl(Id(wR), NumberType, None, None)], Return(Id(ZB))), FuncDecl(Id(TvbJ), [VarDecl(Id(KKbZ), ArrayType([28.93], NumberType), None, None)], Block([VarDecl(Id(K78I), ArrayType([78.8], NumberType), None, None), CallStmt(Id(PT7X), []), Continue])), VarDecl(Id(cee), ArrayType([35.59, 1.68, 62.97], NumberType), None, StringLit(f)), VarDecl(Id(t9u), ArrayType([27.81, 50.2, 47.95], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115288))

	def test_21530115289(self):
		input = '''
func VLEE (string H8U, number mI, string Wv[73.16,66.34])
	begin
	end
func ZY (string PsB, number rcS)
	return 68.66

bool ivHj[98.07,19.28,80.26] <- PH
var oj52 <- xJfo
func rbjK ()
	return 40.96
'''
		expect = '''Program([FuncDecl(Id(VLEE), [VarDecl(Id(H8U), StringType, None, None), VarDecl(Id(mI), NumberType, None, None), VarDecl(Id(Wv), ArrayType([73.16, 66.34], StringType), None, None)], Block([])), FuncDecl(Id(ZY), [VarDecl(Id(PsB), StringType, None, None), VarDecl(Id(rcS), NumberType, None, None)], Return(NumLit(68.66))), VarDecl(Id(ivHj), ArrayType([98.07, 19.28, 80.26], BoolType), None, Id(PH)), VarDecl(Id(oj52), None, var, Id(xJfo)), FuncDecl(Id(rbjK), [], Return(NumLit(40.96)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115289))

	def test_21530115290(self):
		input = '''
number it1 <- true
string Abyd
string pyK[39.29]
func znd (bool E3Z)
	begin
		break
		begin
		end
	end
'''
		expect = '''Program([VarDecl(Id(it1), NumberType, None, BooleanLit(True)), VarDecl(Id(Abyd), StringType, None, None), VarDecl(Id(pyK), ArrayType([39.29], StringType), None, None), FuncDecl(Id(znd), [VarDecl(Id(E3Z), BoolType, None, None)], Block([Break, Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115290))

	def test_21530115291(self):
		input = '''
func fe (number R9[93.86], number oS[3.45,29.11,87.73])	return 74.6
'''
		expect = '''Program([FuncDecl(Id(fe), [VarDecl(Id(R9), ArrayType([93.86], NumberType), None, None), VarDecl(Id(oS), ArrayType([3.45, 29.11, 87.73], NumberType), None, None)], Return(NumLit(74.6)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115291))

	def test_21530115292(self):
		input = '''
func hRD (string iqmh[60.0,70.81,47.44])
	return

func O4 (bool ynL[51.88,32.91], string pj, bool rO)
	return

func eyhu (string QrK, string G4G, number sc)	return
'''
		expect = '''Program([FuncDecl(Id(hRD), [VarDecl(Id(iqmh), ArrayType([60.0, 70.81, 47.44], StringType), None, None)], Return()), FuncDecl(Id(O4), [VarDecl(Id(ynL), ArrayType([51.88, 32.91], BoolType), None, None), VarDecl(Id(pj), StringType, None, None), VarDecl(Id(rO), BoolType, None, None)], Return()), FuncDecl(Id(eyhu), [VarDecl(Id(QrK), StringType, None, None), VarDecl(Id(G4G), StringType, None, None), VarDecl(Id(sc), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115292))

	def test_21530115293(self):
		input = '''
func HlK4 (bool Ioc, string mgH6[78.88,76.34], number va[94.47,54.24])
	return "pjzkk"
dynamic wwb6
'''
		expect = '''Program([FuncDecl(Id(HlK4), [VarDecl(Id(Ioc), BoolType, None, None), VarDecl(Id(mgH6), ArrayType([78.88, 76.34], StringType), None, None), VarDecl(Id(va), ArrayType([94.47, 54.24], NumberType), None, None)], Return(StringLit(pjzkk))), VarDecl(Id(wwb6), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115293))

	def test_21530115294(self):
		input = '''
func o9 (bool Fx[38.17])
	begin
		string uE_[8.51] <- "F"
		qcI[35.08, 63.45] <- true
		wGfW[32.64, jzHJ, false] <- qfEX
	end
func vtl0 (bool xF[64.78], number yiD, number yiY)	return

bool EoV[74.09,50.51]
dynamic OUb <- true
var Si <- Xr
'''
		expect = '''Program([FuncDecl(Id(o9), [VarDecl(Id(Fx), ArrayType([38.17], BoolType), None, None)], Block([VarDecl(Id(uE_), ArrayType([8.51], StringType), None, StringLit(F)), AssignStmt(ArrayCell(Id(qcI), [NumLit(35.08), NumLit(63.45)]), BooleanLit(True)), AssignStmt(ArrayCell(Id(wGfW), [NumLit(32.64), Id(jzHJ), BooleanLit(False)]), Id(qfEX))])), FuncDecl(Id(vtl0), [VarDecl(Id(xF), ArrayType([64.78], BoolType), None, None), VarDecl(Id(yiD), NumberType, None, None), VarDecl(Id(yiY), NumberType, None, None)], Return()), VarDecl(Id(EoV), ArrayType([74.09, 50.51], BoolType), None, None), VarDecl(Id(OUb), None, dynamic, BooleanLit(True)), VarDecl(Id(Si), None, var, Id(Xr))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115294))

	def test_21530115295(self):
		input = '''
bool gj1[56.91] <- 23.36
'''
		expect = '''Program([VarDecl(Id(gj1), ArrayType([56.91], BoolType), None, NumLit(23.36))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115295))

	def test_21530115296(self):
		input = '''
func bzn ()	return
func G5L (string EYdO)
	return

func NcA ()	return 2.6

'''
		expect = '''Program([FuncDecl(Id(bzn), [], Return()), FuncDecl(Id(G5L), [VarDecl(Id(EYdO), StringType, None, None)], Return()), FuncDecl(Id(NcA), [], Return(NumLit(2.6)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115296))

	def test_21530115297(self):
		input = '''
number LKY[52.93,16.71,58.57]
'''
		expect = '''Program([VarDecl(Id(LKY), ArrayType([52.93, 16.71, 58.57], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115297))

	def test_21530115298(self):
		input = '''
func rIbQ (number T0[51.68], number ApDW[40.86], string abD6[53.52,94.31])	return A83A

number MYZ <- "JKstG"
'''
		expect = '''Program([FuncDecl(Id(rIbQ), [VarDecl(Id(T0), ArrayType([51.68], NumberType), None, None), VarDecl(Id(ApDW), ArrayType([40.86], NumberType), None, None), VarDecl(Id(abD6), ArrayType([53.52, 94.31], StringType), None, None)], Return(Id(A83A))), VarDecl(Id(MYZ), NumberType, None, StringLit(JKstG))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115298))

	def test_21530115299(self):
		input = '''
string ZJ <- false
func kdTf ()
	begin
		break
		begin
			bool PR <- false
			for JD until true by v0H
				yEv[true] <- true
		end
	end
'''
		expect = '''Program([VarDecl(Id(ZJ), StringType, None, BooleanLit(False)), FuncDecl(Id(kdTf), [], Block([Break, Block([VarDecl(Id(PR), BoolType, None, BooleanLit(False)), For(Id(JD), BooleanLit(True), Id(v0H), AssignStmt(ArrayCell(Id(yEv), [BooleanLit(True)]), BooleanLit(True)))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115299))

	def test_21530115300(self):
		input = '''
func Vz (bool CGl[28.9])	return
string ah0_[49.73,20.16,43.97] <- true
'''
		expect = '''Program([FuncDecl(Id(Vz), [VarDecl(Id(CGl), ArrayType([28.9], BoolType), None, None)], Return()), VarDecl(Id(ah0_), ArrayType([49.73, 20.16, 43.97], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115300))

	def test_21530115301(self):
		input = '''
number fYW <- true
bool gZ[74.96,27.48]
func gj1T ()
	return "E"

'''
		expect = '''Program([VarDecl(Id(fYW), NumberType, None, BooleanLit(True)), VarDecl(Id(gZ), ArrayType([74.96, 27.48], BoolType), None, None), FuncDecl(Id(gj1T), [], Return(StringLit(E)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115301))

	def test_21530115302(self):
		input = '''
func eR ()
	return hm

number RU[35.76] <- "q"
func qDR (bool AU[42.76,60.84], string dY[38.1,28.97], bool JH[85.16])	return
func bv ()
	return

'''
		expect = '''Program([FuncDecl(Id(eR), [], Return(Id(hm))), VarDecl(Id(RU), ArrayType([35.76], NumberType), None, StringLit(q)), FuncDecl(Id(qDR), [VarDecl(Id(AU), ArrayType([42.76, 60.84], BoolType), None, None), VarDecl(Id(dY), ArrayType([38.1, 28.97], StringType), None, None), VarDecl(Id(JH), ArrayType([85.16], BoolType), None, None)], Return()), FuncDecl(Id(bv), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115302))

	def test_21530115303(self):
		input = '''
string lmZJ[33.41,0.41,12.5]
func K3M (bool x8Xi)	return 37.68
func drf_ ()	return "eTCi"
string X8Jj[71.06] <- gJN
func G5 (number LIfg, bool HndU)
	begin
		PPB("Gz")
		break
		if ("V") PTNl <- Ra
		elif (34.5)
		for jW8 until false by smW
			return
		else if (37.12)
		cWuQ(BwQz, 72.85)
		elif (false) whud("LCi", "CDqv")
		elif (true) break
		elif (57.56)
		for v9H until true by true
			number hmL[10.82,90.49]
		else if (15.06)
		if (6.2) bool tId
		elif (51.46)
		if (92.01)
		break
		elif (true) KNnb()
		elif (true)
		if ("lKhOu")
		break
		else return
		else begin
		end
		elif (40.85)
		begin
			z9IL("oRVXa", false)
			break
		end
		else begin
			string Bn <- true
		end
		elif (qgRr) continue
		elif (4.72)
		if (EnH9) return NX
		elif (42.81)
		begin
		end
		elif (rP)
		return
		else begin
			Qr[false] <- ewxy
			begin
			end
			break
		end
		elif (false)
		if (true)
		return true
		else sJ(true, 69.98)
		elif (false)
		for SP6 until true by false
			h7vD("hxC", "YIIY", "WH")
		elif ("YAC")
		break
		else T5d(true, Nk)
	end

'''
		expect = '''Program([VarDecl(Id(lmZJ), ArrayType([33.41, 0.41, 12.5], StringType), None, None), FuncDecl(Id(K3M), [VarDecl(Id(x8Xi), BoolType, None, None)], Return(NumLit(37.68))), FuncDecl(Id(drf_), [], Return(StringLit(eTCi))), VarDecl(Id(X8Jj), ArrayType([71.06], StringType), None, Id(gJN)), FuncDecl(Id(G5), [VarDecl(Id(LIfg), NumberType, None, None), VarDecl(Id(HndU), BoolType, None, None)], Block([CallStmt(Id(PPB), [StringLit(Gz)]), Break, If((StringLit(V), AssignStmt(Id(PTNl), Id(Ra))), [(NumLit(34.5), For(Id(jW8), BooleanLit(False), Id(smW), Return()))], If((NumLit(37.12), CallStmt(Id(cWuQ), [Id(BwQz), NumLit(72.85)])), [(BooleanLit(False), CallStmt(Id(whud), [StringLit(LCi), StringLit(CDqv)])), (BooleanLit(True), Break), (NumLit(57.56), For(Id(v9H), BooleanLit(True), BooleanLit(True), VarDecl(Id(hmL), ArrayType([10.82, 90.49], NumberType), None, None)))], If((NumLit(15.06), If((NumLit(6.2), VarDecl(Id(tId), BoolType, None, None)), [(NumLit(51.46), If((NumLit(92.01), Break), [(BooleanLit(True), CallStmt(Id(KNnb), [])), (BooleanLit(True), If((StringLit(lKhOu), Break), [], Return()))], Block([]))), (NumLit(40.85), Block([CallStmt(Id(z9IL), [StringLit(oRVXa), BooleanLit(False)]), Break]))], Block([VarDecl(Id(Bn), StringType, None, BooleanLit(True))]))), [(Id(qgRr), Continue), (NumLit(4.72), If((Id(EnH9), Return(Id(NX))), [(NumLit(42.81), Block([])), (Id(rP), Return())], Block([AssignStmt(ArrayCell(Id(Qr), [BooleanLit(False)]), Id(ewxy)), Block([]), Break]))), (BooleanLit(False), If((BooleanLit(True), Return(BooleanLit(True))), [], CallStmt(Id(sJ), [BooleanLit(True), NumLit(69.98)]))), (BooleanLit(False), For(Id(SP6), BooleanLit(True), BooleanLit(False), CallStmt(Id(h7vD), [StringLit(hxC), StringLit(YIIY), StringLit(WH)]))), (StringLit(YAC), Break)], CallStmt(Id(T5d), [BooleanLit(True), Id(Nk)]))))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115303))

	def test_21530115304(self):
		input = '''
func nSd (string Kog6, string K3, bool qjA[70.68,5.87,50.54])	begin
	end

bool Os4G[12.7,11.33,42.27]
number pRjD[32.01,89.44] <- 73.73
bool vJH <- 48.17
string Db3r
'''
		expect = '''Program([FuncDecl(Id(nSd), [VarDecl(Id(Kog6), StringType, None, None), VarDecl(Id(K3), StringType, None, None), VarDecl(Id(qjA), ArrayType([70.68, 5.87, 50.54], BoolType), None, None)], Block([])), VarDecl(Id(Os4G), ArrayType([12.7, 11.33, 42.27], BoolType), None, None), VarDecl(Id(pRjD), ArrayType([32.01, 89.44], NumberType), None, NumLit(73.73)), VarDecl(Id(vJH), BoolType, None, NumLit(48.17)), VarDecl(Id(Db3r), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115304))

	def test_21530115305(self):
		input = '''
func bd (string IS[72.31], bool fHa)	return

var VK <- 10.04
var s1 <- false
'''
		expect = '''Program([FuncDecl(Id(bd), [VarDecl(Id(IS), ArrayType([72.31], StringType), None, None), VarDecl(Id(fHa), BoolType, None, None)], Return()), VarDecl(Id(VK), None, var, NumLit(10.04)), VarDecl(Id(s1), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115305))

	def test_21530115306(self):
		input = '''
number yuh0[72.59,35.31] <- true
number PmHp
func J9Sz (number aoq[33.46,26.09], string lQj[31.97])
	return "jwCN"
func p2U (bool H4s, string dcJ[61.38,5.02])
	begin
		VgD9(65.5)
	end
func WU ()	begin
	end

'''
		expect = '''Program([VarDecl(Id(yuh0), ArrayType([72.59, 35.31], NumberType), None, BooleanLit(True)), VarDecl(Id(PmHp), NumberType, None, None), FuncDecl(Id(J9Sz), [VarDecl(Id(aoq), ArrayType([33.46, 26.09], NumberType), None, None), VarDecl(Id(lQj), ArrayType([31.97], StringType), None, None)], Return(StringLit(jwCN))), FuncDecl(Id(p2U), [VarDecl(Id(H4s), BoolType, None, None), VarDecl(Id(dcJ), ArrayType([61.38, 5.02], StringType), None, None)], Block([CallStmt(Id(VgD9), [NumLit(65.5)])])), FuncDecl(Id(WU), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115306))

	def test_21530115307(self):
		input = '''
func q6mV (bool qu[52.1,52.96])
	begin
		id[2.94] <- 33.66
	end
'''
		expect = '''Program([FuncDecl(Id(q6mV), [VarDecl(Id(qu), ArrayType([52.1, 52.96], BoolType), None, None)], Block([AssignStmt(ArrayCell(Id(id), [NumLit(2.94)]), NumLit(33.66))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115307))

	def test_21530115308(self):
		input = '''
number UxA
'''
		expect = '''Program([VarDecl(Id(UxA), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115308))

	def test_21530115309(self):
		input = '''
var j5 <- "fbG"
string oY_ <- true
func ElWH (string uS0Q)	return

dynamic tPx <- 94.6
func cZl (string OGa, number cpi)
	return "e"

'''
		expect = '''Program([VarDecl(Id(j5), None, var, StringLit(fbG)), VarDecl(Id(oY_), StringType, None, BooleanLit(True)), FuncDecl(Id(ElWH), [VarDecl(Id(uS0Q), StringType, None, None)], Return()), VarDecl(Id(tPx), None, dynamic, NumLit(94.6)), FuncDecl(Id(cZl), [VarDecl(Id(OGa), StringType, None, None), VarDecl(Id(cpi), NumberType, None, None)], Return(StringLit(e)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115309))

	def test_21530115310(self):
		input = '''
func qOd ()
	return

number LLK
'''
		expect = '''Program([FuncDecl(Id(qOd), [], Return()), VarDecl(Id(LLK), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115310))

	def test_21530115311(self):
		input = '''
func mkB ()
	return
func Ax ()	return
'''
		expect = '''Program([FuncDecl(Id(mkB), [], Return()), FuncDecl(Id(Ax), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115311))

	def test_21530115312(self):
		input = '''
string L0p[35.58]
func DH (number iy[95.36,52.92,62.4], bool LZ)	return

dynamic faF <- "Ev"
var FwHz <- "IBs"
'''
		expect = '''Program([VarDecl(Id(L0p), ArrayType([35.58], StringType), None, None), FuncDecl(Id(DH), [VarDecl(Id(iy), ArrayType([95.36, 52.92, 62.4], NumberType), None, None), VarDecl(Id(LZ), BoolType, None, None)], Return()), VarDecl(Id(faF), None, dynamic, StringLit(Ev)), VarDecl(Id(FwHz), None, var, StringLit(IBs))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115312))

	def test_21530115313(self):
		input = '''
func dUp ()
	return "ps"
bool I11f[46.99,90.43] <- "DMsBh"
'''
		expect = '''Program([FuncDecl(Id(dUp), [], Return(StringLit(ps))), VarDecl(Id(I11f), ArrayType([46.99, 90.43], BoolType), None, StringLit(DMsBh))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115313))

	def test_21530115314(self):
		input = '''
func DXXs (number PO[64.6,21.51,68.23], bool qL, number pLu[93.66,88.34])	begin
	end

string Dvl3[66.83,67.99,89.08]
string RMl0
var lyMa <- NUER
number qB[96.83]
'''
		expect = '''Program([FuncDecl(Id(DXXs), [VarDecl(Id(PO), ArrayType([64.6, 21.51, 68.23], NumberType), None, None), VarDecl(Id(qL), BoolType, None, None), VarDecl(Id(pLu), ArrayType([93.66, 88.34], NumberType), None, None)], Block([])), VarDecl(Id(Dvl3), ArrayType([66.83, 67.99, 89.08], StringType), None, None), VarDecl(Id(RMl0), StringType, None, None), VarDecl(Id(lyMa), None, var, Id(NUER)), VarDecl(Id(qB), ArrayType([96.83], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115314))

	def test_21530115315(self):
		input = '''
number tRO
func yphh (number GMN, number Fqag)
	return jIg

'''
		expect = '''Program([VarDecl(Id(tRO), NumberType, None, None), FuncDecl(Id(yphh), [VarDecl(Id(GMN), NumberType, None, None), VarDecl(Id(Fqag), NumberType, None, None)], Return(Id(jIg)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115315))

	def test_21530115316(self):
		input = '''
func af ()
	return

'''
		expect = '''Program([FuncDecl(Id(af), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115316))

	def test_21530115317(self):
		input = '''
func kvVs (bool XeeC[79.1,85.23], bool DO[11.83])
	return "rxcm"
bool Hf <- iN1
string h0U
bool WP[43.46] <- false
'''
		expect = '''Program([FuncDecl(Id(kvVs), [VarDecl(Id(XeeC), ArrayType([79.1, 85.23], BoolType), None, None), VarDecl(Id(DO), ArrayType([11.83], BoolType), None, None)], Return(StringLit(rxcm))), VarDecl(Id(Hf), BoolType, None, Id(iN1)), VarDecl(Id(h0U), StringType, None, None), VarDecl(Id(WP), ArrayType([43.46], BoolType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115317))

	def test_21530115318(self):
		input = '''
var bVn <- false
func OIx (bool fHC, string vLR[97.9])	return XdoV
'''
		expect = '''Program([VarDecl(Id(bVn), None, var, BooleanLit(False)), FuncDecl(Id(OIx), [VarDecl(Id(fHC), BoolType, None, None), VarDecl(Id(vLR), ArrayType([97.9], StringType), None, None)], Return(Id(XdoV)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115318))

	def test_21530115319(self):
		input = '''
bool pH[99.11,78.63,4.55]
string eUny[75.13,57.56]
'''
		expect = '''Program([VarDecl(Id(pH), ArrayType([99.11, 78.63, 4.55], BoolType), None, None), VarDecl(Id(eUny), ArrayType([75.13, 57.56], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115319))

	def test_21530115320(self):
		input = '''
string UGx <- "hCmG"
number ztZX[87.36,36.11,4.98]
number dJ2[50.1]
bool J93f[95.02] <- true
'''
		expect = '''Program([VarDecl(Id(UGx), StringType, None, StringLit(hCmG)), VarDecl(Id(ztZX), ArrayType([87.36, 36.11, 4.98], NumberType), None, None), VarDecl(Id(dJ2), ArrayType([50.1], NumberType), None, None), VarDecl(Id(J93f), ArrayType([95.02], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115320))

	def test_21530115321(self):
		input = '''
var Hk <- false
func mZ5j (string sNAm[50.36,9.07], number dhU[41.99,18.41])
	return 19.55
func pLK ()
	begin
		pITr(DQXt)
		continue
		string EB1G[52.62,41.7,77.84] <- false
	end

dynamic pH
bool meq[57.13] <- nY
'''
		expect = '''Program([VarDecl(Id(Hk), None, var, BooleanLit(False)), FuncDecl(Id(mZ5j), [VarDecl(Id(sNAm), ArrayType([50.36, 9.07], StringType), None, None), VarDecl(Id(dhU), ArrayType([41.99, 18.41], NumberType), None, None)], Return(NumLit(19.55))), FuncDecl(Id(pLK), [], Block([CallStmt(Id(pITr), [Id(DQXt)]), Continue, VarDecl(Id(EB1G), ArrayType([52.62, 41.7, 77.84], StringType), None, BooleanLit(False))])), VarDecl(Id(pH), None, dynamic, None), VarDecl(Id(meq), ArrayType([57.13], BoolType), None, Id(nY))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115321))

	def test_21530115322(self):
		input = '''
func k5z6 (number qM[82.21], number mOk)
	return
dynamic FPmd
func MH (bool Xp, number Yy)	return
'''
		expect = '''Program([FuncDecl(Id(k5z6), [VarDecl(Id(qM), ArrayType([82.21], NumberType), None, None), VarDecl(Id(mOk), NumberType, None, None)], Return()), VarDecl(Id(FPmd), None, dynamic, None), FuncDecl(Id(MH), [VarDecl(Id(Xp), BoolType, None, None), VarDecl(Id(Yy), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115322))

	def test_21530115323(self):
		input = '''
number b6e[0.35] <- true
func uzfr (bool Kp[53.55], string jIk, string EG[49.36,35.77,0.62])	begin
		break
		continue
		number su[39.31,0.19,36.71]
	end
func Z1E (bool b06, string GKk)
	return p5rj

func S7g ()	begin
		for UV until "M" by AYfZ
			yT3(true)
		Xa[3.97, 61.18, true] <- 13.03
	end
string ESOO <- "yH"
'''
		expect = '''Program([VarDecl(Id(b6e), ArrayType([0.35], NumberType), None, BooleanLit(True)), FuncDecl(Id(uzfr), [VarDecl(Id(Kp), ArrayType([53.55], BoolType), None, None), VarDecl(Id(jIk), StringType, None, None), VarDecl(Id(EG), ArrayType([49.36, 35.77, 0.62], StringType), None, None)], Block([Break, Continue, VarDecl(Id(su), ArrayType([39.31, 0.19, 36.71], NumberType), None, None)])), FuncDecl(Id(Z1E), [VarDecl(Id(b06), BoolType, None, None), VarDecl(Id(GKk), StringType, None, None)], Return(Id(p5rj))), FuncDecl(Id(S7g), [], Block([For(Id(UV), StringLit(M), Id(AYfZ), CallStmt(Id(yT3), [BooleanLit(True)])), AssignStmt(ArrayCell(Id(Xa), [NumLit(3.97), NumLit(61.18), BooleanLit(True)]), NumLit(13.03))])), VarDecl(Id(ESOO), StringType, None, StringLit(yH))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115323))

	def test_21530115324(self):
		input = '''
func RFn0 (bool hgG[5.26,67.41])	return JmY

func kH (bool P10n)
	begin
		return true
	end

'''
		expect = '''Program([FuncDecl(Id(RFn0), [VarDecl(Id(hgG), ArrayType([5.26, 67.41], BoolType), None, None)], Return(Id(JmY))), FuncDecl(Id(kH), [VarDecl(Id(P10n), BoolType, None, None)], Block([Return(BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115324))

	def test_21530115325(self):
		input = '''
bool UhOr <- true
number WsJa
'''
		expect = '''Program([VarDecl(Id(UhOr), BoolType, None, BooleanLit(True)), VarDecl(Id(WsJa), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115325))

	def test_21530115326(self):
		input = '''
func M91X ()	return

'''
		expect = '''Program([FuncDecl(Id(M91X), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115326))

	def test_21530115327(self):
		input = '''
func b0mj (string QHVP[48.9], string iEpK[20.28,46.86], string ksj[78.39,23.18])
	return
'''
		expect = '''Program([FuncDecl(Id(b0mj), [VarDecl(Id(QHVP), ArrayType([48.9], StringType), None, None), VarDecl(Id(iEpK), ArrayType([20.28, 46.86], StringType), None, None), VarDecl(Id(ksj), ArrayType([78.39, 23.18], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115327))

	def test_21530115328(self):
		input = '''
func gH (string iMg[24.29,43.51,63.03])	return
func f5 (bool uj7m)
	begin
		gbb[AXhX, 1.41] <- uAHB
		VM <- false
		number uie[25.5]
	end

func hnsV (string VYT[64.82,40.94,3.66], bool uB8)	return rKx
'''
		expect = '''Program([FuncDecl(Id(gH), [VarDecl(Id(iMg), ArrayType([24.29, 43.51, 63.03], StringType), None, None)], Return()), FuncDecl(Id(f5), [VarDecl(Id(uj7m), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(gbb), [Id(AXhX), NumLit(1.41)]), Id(uAHB)), AssignStmt(Id(VM), BooleanLit(False)), VarDecl(Id(uie), ArrayType([25.5], NumberType), None, None)])), FuncDecl(Id(hnsV), [VarDecl(Id(VYT), ArrayType([64.82, 40.94, 3.66], StringType), None, None), VarDecl(Id(uB8), BoolType, None, None)], Return(Id(rKx)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115328))

	def test_21530115329(self):
		input = '''
func ZVw ()	return 23.38

func Av (bool jIx_, number Eg)	begin
		begin
			begin
				break
				RK <- "ez"
			end
			continue
			continue
		end
		ARQ6()
	end
number ZIh <- "a"
'''
		expect = '''Program([FuncDecl(Id(ZVw), [], Return(NumLit(23.38))), FuncDecl(Id(Av), [VarDecl(Id(jIx_), BoolType, None, None), VarDecl(Id(Eg), NumberType, None, None)], Block([Block([Block([Break, AssignStmt(Id(RK), StringLit(ez))]), Continue, Continue]), CallStmt(Id(ARQ6), [])])), VarDecl(Id(ZIh), NumberType, None, StringLit(a))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115329))

	def test_21530115330(self):
		input = '''
number CxB2
func qBPJ (string Gi[40.24], bool JAH5)	return Lihg

'''
		expect = '''Program([VarDecl(Id(CxB2), NumberType, None, None), FuncDecl(Id(qBPJ), [VarDecl(Id(Gi), ArrayType([40.24], StringType), None, None), VarDecl(Id(JAH5), BoolType, None, None)], Return(Id(Lihg)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115330))

	def test_21530115331(self):
		input = '''
number cqf[86.78,43.63]
func Ya (bool FU9X[54.29,16.23])
	return false
'''
		expect = '''Program([VarDecl(Id(cqf), ArrayType([86.78, 43.63], NumberType), None, None), FuncDecl(Id(Ya), [VarDecl(Id(FU9X), ArrayType([54.29, 16.23], BoolType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115331))

	def test_21530115332(self):
		input = '''
number uKA4[15.42,75.57]
'''
		expect = '''Program([VarDecl(Id(uKA4), ArrayType([15.42, 75.57], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115332))

	def test_21530115333(self):
		input = '''
string QGx
string f7 <- "d"
func pr0Y ()	begin
	end
func ozaL (bool aQDy[58.2,58.25], number m3Ag, number ycq7)	return

'''
		expect = '''Program([VarDecl(Id(QGx), StringType, None, None), VarDecl(Id(f7), StringType, None, StringLit(d)), FuncDecl(Id(pr0Y), [], Block([])), FuncDecl(Id(ozaL), [VarDecl(Id(aQDy), ArrayType([58.2, 58.25], BoolType), None, None), VarDecl(Id(m3Ag), NumberType, None, None), VarDecl(Id(ycq7), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115333))

	def test_21530115334(self):
		input = '''
func OH (string MIS)	return oZ5

var yy <- true
'''
		expect = '''Program([FuncDecl(Id(OH), [VarDecl(Id(MIS), StringType, None, None)], Return(Id(oZ5))), VarDecl(Id(yy), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115334))

	def test_21530115335(self):
		input = '''
func Ph (number E8_, bool lhcx, string F1)	return 82.79
dynamic iQq5
'''
		expect = '''Program([FuncDecl(Id(Ph), [VarDecl(Id(E8_), NumberType, None, None), VarDecl(Id(lhcx), BoolType, None, None), VarDecl(Id(F1), StringType, None, None)], Return(NumLit(82.79))), VarDecl(Id(iQq5), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115335))

	def test_21530115336(self):
		input = '''
func XtTn (string nWF[55.92,59.12])
	begin
	end
dynamic tfls <- 84.55
func kxP (bool eIC[94.48,30.02,34.89], number qjF, number flh[87.01])
	return iNC4
string ded[66.42] <- 85.58
func ax9J (string QTb8[89.04,89.89])	return 45.25
'''
		expect = '''Program([FuncDecl(Id(XtTn), [VarDecl(Id(nWF), ArrayType([55.92, 59.12], StringType), None, None)], Block([])), VarDecl(Id(tfls), None, dynamic, NumLit(84.55)), FuncDecl(Id(kxP), [VarDecl(Id(eIC), ArrayType([94.48, 30.02, 34.89], BoolType), None, None), VarDecl(Id(qjF), NumberType, None, None), VarDecl(Id(flh), ArrayType([87.01], NumberType), None, None)], Return(Id(iNC4))), VarDecl(Id(ded), ArrayType([66.42], StringType), None, NumLit(85.58)), FuncDecl(Id(ax9J), [VarDecl(Id(QTb8), ArrayType([89.04, 89.89], StringType), None, None)], Return(NumLit(45.25)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115336))

	def test_21530115337(self):
		input = '''
dynamic Ll <- "vpJJ"
'''
		expect = '''Program([VarDecl(Id(Ll), None, dynamic, StringLit(vpJJ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115337))

	def test_21530115338(self):
		input = '''
func Uq (string HJn[78.74,63.83], number KpJ)	return true

'''
		expect = '''Program([FuncDecl(Id(Uq), [VarDecl(Id(HJn), ArrayType([78.74, 63.83], StringType), None, None), VarDecl(Id(KpJ), NumberType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115338))

	def test_21530115339(self):
		input = '''
number ngPo
string kir5[28.48,94.97,91.59]
func dnJk ()
	return

func DDC (bool MUYJ, bool p60)	return 51.49

'''
		expect = '''Program([VarDecl(Id(ngPo), NumberType, None, None), VarDecl(Id(kir5), ArrayType([28.48, 94.97, 91.59], StringType), None, None), FuncDecl(Id(dnJk), [], Return()), FuncDecl(Id(DDC), [VarDecl(Id(MUYJ), BoolType, None, None), VarDecl(Id(p60), BoolType, None, None)], Return(NumLit(51.49)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115339))

	def test_21530115340(self):
		input = '''
func mH0p (string IjS[48.06,72.56])
	begin
		begin
			continue
			return AX3
			Br()
		end
	end

func mv2 (string DT[13.89,21.23])	return

func W1a ()
	begin
		dGro["oSOd", false] <- nO
	end
'''
		expect = '''Program([FuncDecl(Id(mH0p), [VarDecl(Id(IjS), ArrayType([48.06, 72.56], StringType), None, None)], Block([Block([Continue, Return(Id(AX3)), CallStmt(Id(Br), [])])])), FuncDecl(Id(mv2), [VarDecl(Id(DT), ArrayType([13.89, 21.23], StringType), None, None)], Return()), FuncDecl(Id(W1a), [], Block([AssignStmt(ArrayCell(Id(dGro), [StringLit(oSOd), BooleanLit(False)]), Id(nO))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115340))

	def test_21530115341(self):
		input = '''
func JmFN ()	begin
	end

number IN
bool l5[82.1,44.12] <- OWOu
'''
		expect = '''Program([FuncDecl(Id(JmFN), [], Block([])), VarDecl(Id(IN), NumberType, None, None), VarDecl(Id(l5), ArrayType([82.1, 44.12], BoolType), None, Id(OWOu))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115341))

	def test_21530115342(self):
		input = '''
func kZA ()
	begin
		Ze(false, DKh, false)
		return "n"
	end
number k6
'''
		expect = '''Program([FuncDecl(Id(kZA), [], Block([CallStmt(Id(Ze), [BooleanLit(False), Id(DKh), BooleanLit(False)]), Return(StringLit(n))])), VarDecl(Id(k6), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115342))

	def test_21530115343(self):
		input = '''
func RoL (string ltAm[33.86,68.8,44.72])	begin
		continue
		begin
			S7f("rJ", aEbm, false)
			xLme(true)
			break
		end
	end
dynamic zqY
'''
		expect = '''Program([FuncDecl(Id(RoL), [VarDecl(Id(ltAm), ArrayType([33.86, 68.8, 44.72], StringType), None, None)], Block([Continue, Block([CallStmt(Id(S7f), [StringLit(rJ), Id(aEbm), BooleanLit(False)]), CallStmt(Id(xLme), [BooleanLit(True)]), Break])])), VarDecl(Id(zqY), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115343))

	def test_21530115344(self):
		input = '''
var Vta <- "WJD"
dynamic kmX9
string cLAF[82.86,97.74] <- true
func Ux (number AC[70.77,3.28,27.37], bool mnC)	return

func BKUj (bool j5L[70.45], number IO[26.7,72.54,60.09], number TP)	begin
		for J5 until 44.69 by true
			u7H2(Nuy, hqK4)
		l6q["TKnbn"] <- "kp"
		return Ge
	end

'''
		expect = '''Program([VarDecl(Id(Vta), None, var, StringLit(WJD)), VarDecl(Id(kmX9), None, dynamic, None), VarDecl(Id(cLAF), ArrayType([82.86, 97.74], StringType), None, BooleanLit(True)), FuncDecl(Id(Ux), [VarDecl(Id(AC), ArrayType([70.77, 3.28, 27.37], NumberType), None, None), VarDecl(Id(mnC), BoolType, None, None)], Return()), FuncDecl(Id(BKUj), [VarDecl(Id(j5L), ArrayType([70.45], BoolType), None, None), VarDecl(Id(IO), ArrayType([26.7, 72.54, 60.09], NumberType), None, None), VarDecl(Id(TP), NumberType, None, None)], Block([For(Id(J5), NumLit(44.69), BooleanLit(True), CallStmt(Id(u7H2), [Id(Nuy), Id(hqK4)])), AssignStmt(ArrayCell(Id(l6q), [StringLit(TKnbn)]), StringLit(kp)), Return(Id(Ge))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115344))

	def test_21530115345(self):
		input = '''
string rbu
func WAY (string s9k1)
	return

number jhJ[86.39,19.02]
string u8FO[45.5] <- 41.46
number iX[76.54,45.74,44.77]
'''
		expect = '''Program([VarDecl(Id(rbu), StringType, None, None), FuncDecl(Id(WAY), [VarDecl(Id(s9k1), StringType, None, None)], Return()), VarDecl(Id(jhJ), ArrayType([86.39, 19.02], NumberType), None, None), VarDecl(Id(u8FO), ArrayType([45.5], StringType), None, NumLit(41.46)), VarDecl(Id(iX), ArrayType([76.54, 45.74, 44.77], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115345))

	def test_21530115346(self):
		input = '''
func QjXS (string yHg)	begin
	end
func UA ()	begin
	end
func zv1i (string gNl[85.59], string NHJj[81.14])
	return "lM"

'''
		expect = '''Program([FuncDecl(Id(QjXS), [VarDecl(Id(yHg), StringType, None, None)], Block([])), FuncDecl(Id(UA), [], Block([])), FuncDecl(Id(zv1i), [VarDecl(Id(gNl), ArrayType([85.59], StringType), None, None), VarDecl(Id(NHJj), ArrayType([81.14], StringType), None, None)], Return(StringLit(lM)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115346))

	def test_21530115347(self):
		input = '''
func ChZn (number GeP[63.88,17.65], string RPUM, number zYFu[26.78])
	return true
'''
		expect = '''Program([FuncDecl(Id(ChZn), [VarDecl(Id(GeP), ArrayType([63.88, 17.65], NumberType), None, None), VarDecl(Id(RPUM), StringType, None, None), VarDecl(Id(zYFu), ArrayType([26.78], NumberType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115347))

	def test_21530115348(self):
		input = '''
dynamic He_ <- 70.15
func TXR (string r_T)
	return

bool zqB <- 79.23
func nZH (bool EZ, bool An)
	begin
	end

func Gzs (string gBw[16.26,89.64,40.48])	return
'''
		expect = '''Program([VarDecl(Id(He_), None, dynamic, NumLit(70.15)), FuncDecl(Id(TXR), [VarDecl(Id(r_T), StringType, None, None)], Return()), VarDecl(Id(zqB), BoolType, None, NumLit(79.23)), FuncDecl(Id(nZH), [VarDecl(Id(EZ), BoolType, None, None), VarDecl(Id(An), BoolType, None, None)], Block([])), FuncDecl(Id(Gzs), [VarDecl(Id(gBw), ArrayType([16.26, 89.64, 40.48], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115348))

	def test_21530115349(self):
		input = '''
bool z9
func am5 (number Kl, string yLOW)	begin
		continue
		return 53.47
	end
bool Rp <- true
bool O3E <- U22g
'''
		expect = '''Program([VarDecl(Id(z9), BoolType, None, None), FuncDecl(Id(am5), [VarDecl(Id(Kl), NumberType, None, None), VarDecl(Id(yLOW), StringType, None, None)], Block([Continue, Return(NumLit(53.47))])), VarDecl(Id(Rp), BoolType, None, BooleanLit(True)), VarDecl(Id(O3E), BoolType, None, Id(U22g))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115349))

	def test_21530115350(self):
		input = '''
func wuD (bool LZt[97.8], string Pbi, number lh[79.89])	begin
		WVXy <- "cWV"
	end

func syE (number JOwq[91.75,4.91], bool MAD[37.78,46.81,18.64])
	return "h"
string IHng[91.92,60.59,94.49] <- true
number Cn[52.45,52.14,23.83]
func HJ (number It[88.25], string XOP[73.88,12.0,32.2])	begin
		begin
			BE[wVV_] <- uL
			return
		end
		return "crrfL"
		IxD2("A")
	end

'''
		expect = '''Program([FuncDecl(Id(wuD), [VarDecl(Id(LZt), ArrayType([97.8], BoolType), None, None), VarDecl(Id(Pbi), StringType, None, None), VarDecl(Id(lh), ArrayType([79.89], NumberType), None, None)], Block([AssignStmt(Id(WVXy), StringLit(cWV))])), FuncDecl(Id(syE), [VarDecl(Id(JOwq), ArrayType([91.75, 4.91], NumberType), None, None), VarDecl(Id(MAD), ArrayType([37.78, 46.81, 18.64], BoolType), None, None)], Return(StringLit(h))), VarDecl(Id(IHng), ArrayType([91.92, 60.59, 94.49], StringType), None, BooleanLit(True)), VarDecl(Id(Cn), ArrayType([52.45, 52.14, 23.83], NumberType), None, None), FuncDecl(Id(HJ), [VarDecl(Id(It), ArrayType([88.25], NumberType), None, None), VarDecl(Id(XOP), ArrayType([73.88, 12.0, 32.2], StringType), None, None)], Block([Block([AssignStmt(ArrayCell(Id(BE), [Id(wVV_)]), Id(uL)), Return()]), Return(StringLit(crrfL)), CallStmt(Id(IxD2), [StringLit(A)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115350))

	def test_21530115351(self):
		input = '''
number oKm[39.8]
func kdIA (string Lt6, string pz, number x0u[60.38,67.91])	return

dynamic dH9 <- "IEx"
'''
		expect = '''Program([VarDecl(Id(oKm), ArrayType([39.8], NumberType), None, None), FuncDecl(Id(kdIA), [VarDecl(Id(Lt6), StringType, None, None), VarDecl(Id(pz), StringType, None, None), VarDecl(Id(x0u), ArrayType([60.38, 67.91], NumberType), None, None)], Return()), VarDecl(Id(dH9), None, dynamic, StringLit(IEx))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115351))

	def test_21530115352(self):
		input = '''
func bVkx (string bb8[62.62,85.3,63.48], string J9x, bool Oa2[27.02])
	return pP

func WFrb (string PD[17.4,92.41,7.48], number U7Q, bool xP)	begin
	end
'''
		expect = '''Program([FuncDecl(Id(bVkx), [VarDecl(Id(bb8), ArrayType([62.62, 85.3, 63.48], StringType), None, None), VarDecl(Id(J9x), StringType, None, None), VarDecl(Id(Oa2), ArrayType([27.02], BoolType), None, None)], Return(Id(pP))), FuncDecl(Id(WFrb), [VarDecl(Id(PD), ArrayType([17.4, 92.41, 7.48], StringType), None, None), VarDecl(Id(U7Q), NumberType, None, None), VarDecl(Id(xP), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115352))

	def test_21530115353(self):
		input = '''
func ek (string g1jW[84.01])	return true
bool or6[22.22]
string mL
func vj ()
	begin
	end

func j7 (string ZJ[56.51,68.93], number ODV[49.04,80.19,80.55], string EH[89.13,71.8,0.16])
	begin
		for XQg until 6.18 by "XKI"
			return 85.84
		begin
			giF()
			qtKo <- false
		end
	end
'''
		expect = '''Program([FuncDecl(Id(ek), [VarDecl(Id(g1jW), ArrayType([84.01], StringType), None, None)], Return(BooleanLit(True))), VarDecl(Id(or6), ArrayType([22.22], BoolType), None, None), VarDecl(Id(mL), StringType, None, None), FuncDecl(Id(vj), [], Block([])), FuncDecl(Id(j7), [VarDecl(Id(ZJ), ArrayType([56.51, 68.93], StringType), None, None), VarDecl(Id(ODV), ArrayType([49.04, 80.19, 80.55], NumberType), None, None), VarDecl(Id(EH), ArrayType([89.13, 71.8, 0.16], StringType), None, None)], Block([For(Id(XQg), NumLit(6.18), StringLit(XKI), Return(NumLit(85.84))), Block([CallStmt(Id(giF), []), AssignStmt(Id(qtKo), BooleanLit(False))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115353))

	def test_21530115354(self):
		input = '''
bool FIA[18.72] <- "Yq"
bool d4[31.45,34.53] <- "cVGK"
var xh5 <- true
'''
		expect = '''Program([VarDecl(Id(FIA), ArrayType([18.72], BoolType), None, StringLit(Yq)), VarDecl(Id(d4), ArrayType([31.45, 34.53], BoolType), None, StringLit(cVGK)), VarDecl(Id(xh5), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115354))

	def test_21530115355(self):
		input = '''
bool OKj
func nMy8 (string GW4, bool Bu[58.82])	begin
		EC["nuuqR", "wGD"] <- 35.27
	end
func Mj9t ()	return

'''
		expect = '''Program([VarDecl(Id(OKj), BoolType, None, None), FuncDecl(Id(nMy8), [VarDecl(Id(GW4), StringType, None, None), VarDecl(Id(Bu), ArrayType([58.82], BoolType), None, None)], Block([AssignStmt(ArrayCell(Id(EC), [StringLit(nuuqR), StringLit(wGD)]), NumLit(35.27))])), FuncDecl(Id(Mj9t), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115355))

	def test_21530115356(self):
		input = '''
func U9d (bool Ssa[69.87], number B3d[76.25], bool us9)
	return

'''
		expect = '''Program([FuncDecl(Id(U9d), [VarDecl(Id(Ssa), ArrayType([69.87], BoolType), None, None), VarDecl(Id(B3d), ArrayType([76.25], NumberType), None, None), VarDecl(Id(us9), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115356))

	def test_21530115357(self):
		input = '''
string oOu2 <- 9.28
number rw[92.15,64.89]
'''
		expect = '''Program([VarDecl(Id(oOu2), StringType, None, NumLit(9.28)), VarDecl(Id(rw), ArrayType([92.15, 64.89], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115357))

	def test_21530115358(self):
		input = '''
func fRW ()
	return 95.61
string DB[63.87] <- 56.46
func O2Cx (bool MCB[57.9])
	return

'''
		expect = '''Program([FuncDecl(Id(fRW), [], Return(NumLit(95.61))), VarDecl(Id(DB), ArrayType([63.87], StringType), None, NumLit(56.46)), FuncDecl(Id(O2Cx), [VarDecl(Id(MCB), ArrayType([57.9], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115358))

	def test_21530115359(self):
		input = '''
bool DWk[39.92,17.77,40.47]
func Od3 ()
	begin
		begin
			var GS <- TX
		end
		begin
		end
		return
	end

func A4 (number VGt[70.66,5.16,17.06])
	return

'''
		expect = '''Program([VarDecl(Id(DWk), ArrayType([39.92, 17.77, 40.47], BoolType), None, None), FuncDecl(Id(Od3), [], Block([Block([VarDecl(Id(GS), None, var, Id(TX))]), Block([]), Return()])), FuncDecl(Id(A4), [VarDecl(Id(VGt), ArrayType([70.66, 5.16, 17.06], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115359))

	def test_21530115360(self):
		input = '''
string mkf
func hlG (bool YgN, bool p29i[86.22,91.44], string Cp_)
	return "LoPv"
'''
		expect = '''Program([VarDecl(Id(mkf), StringType, None, None), FuncDecl(Id(hlG), [VarDecl(Id(YgN), BoolType, None, None), VarDecl(Id(p29i), ArrayType([86.22, 91.44], BoolType), None, None), VarDecl(Id(Cp_), StringType, None, None)], Return(StringLit(LoPv)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115360))

	def test_21530115361(self):
		input = '''
func rw8S (number wn[51.49,90.53,58.52])	begin
		tQwz("OGTJK")
	end
number I1wB[28.07]
'''
		expect = '''Program([FuncDecl(Id(rw8S), [VarDecl(Id(wn), ArrayType([51.49, 90.53, 58.52], NumberType), None, None)], Block([CallStmt(Id(tQwz), [StringLit(OGTJK)])])), VarDecl(Id(I1wB), ArrayType([28.07], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115361))

	def test_21530115362(self):
		input = '''
string cClH[16.21] <- tuv
number XuZ[3.07,18.59] <- 57.72
number TxX[9.68]
'''
		expect = '''Program([VarDecl(Id(cClH), ArrayType([16.21], StringType), None, Id(tuv)), VarDecl(Id(XuZ), ArrayType([3.07, 18.59], NumberType), None, NumLit(57.72)), VarDecl(Id(TxX), ArrayType([9.68], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115362))

	def test_21530115363(self):
		input = '''
bool cXvO[29.01,48.49]
func yYeC (bool Vq, bool Oe)	begin
		number jrT[23.6,0.85]
	end
func k1 (string Lo2[25.6], bool NLD)
	return
func npK ()
	return true

'''
		expect = '''Program([VarDecl(Id(cXvO), ArrayType([29.01, 48.49], BoolType), None, None), FuncDecl(Id(yYeC), [VarDecl(Id(Vq), BoolType, None, None), VarDecl(Id(Oe), BoolType, None, None)], Block([VarDecl(Id(jrT), ArrayType([23.6, 0.85], NumberType), None, None)])), FuncDecl(Id(k1), [VarDecl(Id(Lo2), ArrayType([25.6], StringType), None, None), VarDecl(Id(NLD), BoolType, None, None)], Return()), FuncDecl(Id(npK), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115363))

	def test_21530115364(self):
		input = '''
func FXc (string Fge[65.17,13.1], bool ziY, bool sYsM)
	return XCt8
bool iAxX[63.23,83.78]
func pn (number SNW1[69.69,35.61,87.8])
	return "FZIRB"
func FP_V ()
	return

func Cuc (string RDTW[62.81,21.21,5.29], number uqx)	begin
	end
'''
		expect = '''Program([FuncDecl(Id(FXc), [VarDecl(Id(Fge), ArrayType([65.17, 13.1], StringType), None, None), VarDecl(Id(ziY), BoolType, None, None), VarDecl(Id(sYsM), BoolType, None, None)], Return(Id(XCt8))), VarDecl(Id(iAxX), ArrayType([63.23, 83.78], BoolType), None, None), FuncDecl(Id(pn), [VarDecl(Id(SNW1), ArrayType([69.69, 35.61, 87.8], NumberType), None, None)], Return(StringLit(FZIRB))), FuncDecl(Id(FP_V), [], Return()), FuncDecl(Id(Cuc), [VarDecl(Id(RDTW), ArrayType([62.81, 21.21, 5.29], StringType), None, None), VarDecl(Id(uqx), NumberType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115364))

	def test_21530115365(self):
		input = '''
number IHKj <- false
func w7ZE (string kg, bool z68J[69.76,55.13])
	return true

func VGvi (number SY)	return g3NP
'''
		expect = '''Program([VarDecl(Id(IHKj), NumberType, None, BooleanLit(False)), FuncDecl(Id(w7ZE), [VarDecl(Id(kg), StringType, None, None), VarDecl(Id(z68J), ArrayType([69.76, 55.13], BoolType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(VGvi), [VarDecl(Id(SY), NumberType, None, None)], Return(Id(g3NP)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115365))

	def test_21530115366(self):
		input = '''
func ccD ()	return
func LTU (number mGb)	return true

bool Tor[87.61] <- true
string NCt <- CuA
string aI[94.81,66.75,92.66] <- 75.23
'''
		expect = '''Program([FuncDecl(Id(ccD), [], Return()), FuncDecl(Id(LTU), [VarDecl(Id(mGb), NumberType, None, None)], Return(BooleanLit(True))), VarDecl(Id(Tor), ArrayType([87.61], BoolType), None, BooleanLit(True)), VarDecl(Id(NCt), StringType, None, Id(CuA)), VarDecl(Id(aI), ArrayType([94.81, 66.75, 92.66], StringType), None, NumLit(75.23))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115366))

	def test_21530115367(self):
		input = '''
func KVgc (string Qt0)	return

bool wnfX <- false
func Inzq ()
	return
func QA (string lxs[81.63,85.69,78.17])	begin
		LJO <- true
	end

func vKhn (number R9H[88.89,36.18,2.42], string C_, string z2)	begin
		begin
		end
	end
'''
		expect = '''Program([FuncDecl(Id(KVgc), [VarDecl(Id(Qt0), StringType, None, None)], Return()), VarDecl(Id(wnfX), BoolType, None, BooleanLit(False)), FuncDecl(Id(Inzq), [], Return()), FuncDecl(Id(QA), [VarDecl(Id(lxs), ArrayType([81.63, 85.69, 78.17], StringType), None, None)], Block([AssignStmt(Id(LJO), BooleanLit(True))])), FuncDecl(Id(vKhn), [VarDecl(Id(R9H), ArrayType([88.89, 36.18, 2.42], NumberType), None, None), VarDecl(Id(C_), StringType, None, None), VarDecl(Id(z2), StringType, None, None)], Block([Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115367))

	def test_21530115368(self):
		input = '''
func LmZR (number nS5p[77.04], number o5yy[49.37,56.67])	return 95.76

func fLcl (bool Y2j5, bool Flz0)	return
func j3UN (bool IB[36.4,30.87])	begin
		break
		IKYS(75.1, "zJwUi")
		begin
		end
	end

'''
		expect = '''Program([FuncDecl(Id(LmZR), [VarDecl(Id(nS5p), ArrayType([77.04], NumberType), None, None), VarDecl(Id(o5yy), ArrayType([49.37, 56.67], NumberType), None, None)], Return(NumLit(95.76))), FuncDecl(Id(fLcl), [VarDecl(Id(Y2j5), BoolType, None, None), VarDecl(Id(Flz0), BoolType, None, None)], Return()), FuncDecl(Id(j3UN), [VarDecl(Id(IB), ArrayType([36.4, 30.87], BoolType), None, None)], Block([Break, CallStmt(Id(IKYS), [NumLit(75.1), StringLit(zJwUi)]), Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115368))

	def test_21530115369(self):
		input = '''
bool iFi <- "uwFF"
'''
		expect = '''Program([VarDecl(Id(iFi), BoolType, None, StringLit(uwFF))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115369))

	def test_21530115370(self):
		input = '''
dynamic nVz <- "rD"
func IlC ()	return

'''
		expect = '''Program([VarDecl(Id(nVz), None, dynamic, StringLit(rD)), FuncDecl(Id(IlC), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115370))

	def test_21530115371(self):
		input = '''
func OJGj ()
	begin
	end
func JdHc (number FF[4.7])	return "WGLIR"

func F7 (bool iL2, string W0f[76.75,86.83,31.61])	begin
		SA["g"] <- true
	end

number MG <- true
'''
		expect = '''Program([FuncDecl(Id(OJGj), [], Block([])), FuncDecl(Id(JdHc), [VarDecl(Id(FF), ArrayType([4.7], NumberType), None, None)], Return(StringLit(WGLIR))), FuncDecl(Id(F7), [VarDecl(Id(iL2), BoolType, None, None), VarDecl(Id(W0f), ArrayType([76.75, 86.83, 31.61], StringType), None, None)], Block([AssignStmt(ArrayCell(Id(SA), [StringLit(g)]), BooleanLit(True))])), VarDecl(Id(MG), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115371))

	def test_21530115372(self):
		input = '''
string Zd[37.2] <- "xORGO"
bool yR
func Y8H (string vSM5)
	return

'''
		expect = '''Program([VarDecl(Id(Zd), ArrayType([37.2], StringType), None, StringLit(xORGO)), VarDecl(Id(yR), BoolType, None, None), FuncDecl(Id(Y8H), [VarDecl(Id(vSM5), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115372))

	def test_21530115373(self):
		input = '''
func bnKJ (bool Bh, number BSJ[91.74], number qqu)
	return
'''
		expect = '''Program([FuncDecl(Id(bnKJ), [VarDecl(Id(Bh), BoolType, None, None), VarDecl(Id(BSJ), ArrayType([91.74], NumberType), None, None), VarDecl(Id(qqu), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115373))

	def test_21530115374(self):
		input = '''
var yHGG <- daB
dynamic KdV <- "hcZyY"
func Dn (string DS, bool MI4, string EH_)
	return true
'''
		expect = '''Program([VarDecl(Id(yHGG), None, var, Id(daB)), VarDecl(Id(KdV), None, dynamic, StringLit(hcZyY)), FuncDecl(Id(Dn), [VarDecl(Id(DS), StringType, None, None), VarDecl(Id(MI4), BoolType, None, None), VarDecl(Id(EH_), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115374))

	def test_21530115375(self):
		input = '''
bool JfhT[10.5,27.89]
func Q8SJ (string xcz, string weY[0.8,82.66,13.42], string uuwp[61.45,82.35])	return Hqe
func VdRn ()
	return 8.45
number vrj[69.18,69.02] <- 65.5
func Vy (string Nqx, number sm, number HBA[39.93,83.88,23.94])	return
'''
		expect = '''Program([VarDecl(Id(JfhT), ArrayType([10.5, 27.89], BoolType), None, None), FuncDecl(Id(Q8SJ), [VarDecl(Id(xcz), StringType, None, None), VarDecl(Id(weY), ArrayType([0.8, 82.66, 13.42], StringType), None, None), VarDecl(Id(uuwp), ArrayType([61.45, 82.35], StringType), None, None)], Return(Id(Hqe))), FuncDecl(Id(VdRn), [], Return(NumLit(8.45))), VarDecl(Id(vrj), ArrayType([69.18, 69.02], NumberType), None, NumLit(65.5)), FuncDecl(Id(Vy), [VarDecl(Id(Nqx), StringType, None, None), VarDecl(Id(sm), NumberType, None, None), VarDecl(Id(HBA), ArrayType([39.93, 83.88, 23.94], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115375))

	def test_21530115376(self):
		input = '''
func OB06 (string Ify[20.68,49.1], string F3Wp[21.52,18.52], number W6[94.27])	begin
		break
	end
var uLmR <- 55.53
'''
		expect = '''Program([FuncDecl(Id(OB06), [VarDecl(Id(Ify), ArrayType([20.68, 49.1], StringType), None, None), VarDecl(Id(F3Wp), ArrayType([21.52, 18.52], StringType), None, None), VarDecl(Id(W6), ArrayType([94.27], NumberType), None, None)], Block([Break])), VarDecl(Id(uLmR), None, var, NumLit(55.53))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115376))

	def test_21530115377(self):
		input = '''
func iKrY (bool bvlv)	return false
'''
		expect = '''Program([FuncDecl(Id(iKrY), [VarDecl(Id(bvlv), BoolType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115377))

	def test_21530115378(self):
		input = '''
bool OHwS[32.34,85.14]
number mq4[54.61,85.09,45.86]
'''
		expect = '''Program([VarDecl(Id(OHwS), ArrayType([32.34, 85.14], BoolType), None, None), VarDecl(Id(mq4), ArrayType([54.61, 85.09, 45.86], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115378))

	def test_21530115379(self):
		input = '''
dynamic ocsY <- 98.47
func Pyvc ()
	return
func xh (string b83[74.71,81.63,98.87])
	begin
		begin
			for I7S until Ij5 by Dc
				begin
				end
			Q9z()
			break
		end
	end
string YQk[50.67,86.64] <- 10.75
number pP9k[21.95,0.33,34.4] <- 26.66
'''
		expect = '''Program([VarDecl(Id(ocsY), None, dynamic, NumLit(98.47)), FuncDecl(Id(Pyvc), [], Return()), FuncDecl(Id(xh), [VarDecl(Id(b83), ArrayType([74.71, 81.63, 98.87], StringType), None, None)], Block([Block([For(Id(I7S), Id(Ij5), Id(Dc), Block([])), CallStmt(Id(Q9z), []), Break])])), VarDecl(Id(YQk), ArrayType([50.67, 86.64], StringType), None, NumLit(10.75)), VarDecl(Id(pP9k), ArrayType([21.95, 0.33, 34.4], NumberType), None, NumLit(26.66))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115379))

	def test_21530115380(self):
		input = '''
func TawG (bool D46R[50.61,36.12,98.42], number hD2, number lxlR)	return "uqhZR"

'''
		expect = '''Program([FuncDecl(Id(TawG), [VarDecl(Id(D46R), ArrayType([50.61, 36.12, 98.42], BoolType), None, None), VarDecl(Id(hD2), NumberType, None, None), VarDecl(Id(lxlR), NumberType, None, None)], Return(StringLit(uqhZR)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115380))

	def test_21530115381(self):
		input = '''
func VQWt (string OAw[68.61], string BE[50.26,23.87])	return true
func OG (number s4[56.97,83.79,1.21], string tur[71.36])	return
func ye (string nc[57.34,80.98])	begin
	end
'''
		expect = '''Program([FuncDecl(Id(VQWt), [VarDecl(Id(OAw), ArrayType([68.61], StringType), None, None), VarDecl(Id(BE), ArrayType([50.26, 23.87], StringType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(OG), [VarDecl(Id(s4), ArrayType([56.97, 83.79, 1.21], NumberType), None, None), VarDecl(Id(tur), ArrayType([71.36], StringType), None, None)], Return()), FuncDecl(Id(ye), [VarDecl(Id(nc), ArrayType([57.34, 80.98], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115381))

	def test_21530115382(self):
		input = '''
bool rWS
string u1zr <- "njZHf"
bool Wk[70.31,18.44,68.19] <- "TXCT"
'''
		expect = '''Program([VarDecl(Id(rWS), BoolType, None, None), VarDecl(Id(u1zr), StringType, None, StringLit(njZHf)), VarDecl(Id(Wk), ArrayType([70.31, 18.44, 68.19], BoolType), None, StringLit(TXCT))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115382))

	def test_21530115383(self):
		input = '''
func ht ()	return
func uos ()
	begin
		XZB[false, true] <- C2M
		if (33.92)
		begin
			for Jg3L until "BWTnz" by false
				continue
			continue
		end
		elif ("b")
		begin
			dynamic Fp28 <- CI
			if (22.81)
			continue
			elif (true)
			continue
			elif (14.77) for I6z until true by "T"
				S8Y <- true
			elif (64.45)
			begin
				D2X[4.19, "ImAQb", 75.29] <- 14.92
				return
			end
			elif ("LC")
			continue
		end
		elif (true) string VW[45.66,34.13] <- 76.28
		elif (kfQQ)
		break
		else if (true)
		continue
		elif (87.23) TetV <- false
		elif (99.01)
		bool EE[61.92]
		elif (CI) continue
		elif ("CKL")
		if ("gssUc")
		break
		elif (x9)
		return
		else return
		elif ("y")
		begin
			if (KuJe) UG2T <- 30.31
			elif (77.43) WFtH[qpmg] <- true
			elif (26.96) var bE <- C_2
			return
			begin
				dynamic amn
			end
		end
		for ok until true by ty6
			return xO
	end

func KH (string Aif[69.02], bool bD[97.65,99.59], string d5W)	return 63.7

func vDU ()	return "SJL"

'''
		expect = '''Program([FuncDecl(Id(ht), [], Return()), FuncDecl(Id(uos), [], Block([AssignStmt(ArrayCell(Id(XZB), [BooleanLit(False), BooleanLit(True)]), Id(C2M)), If((NumLit(33.92), Block([For(Id(Jg3L), StringLit(BWTnz), BooleanLit(False), Continue), Continue])), [(StringLit(b), Block([VarDecl(Id(Fp28), None, dynamic, Id(CI)), If((NumLit(22.81), Continue), [(BooleanLit(True), Continue), (NumLit(14.77), For(Id(I6z), BooleanLit(True), StringLit(T), AssignStmt(Id(S8Y), BooleanLit(True)))), (NumLit(64.45), Block([AssignStmt(ArrayCell(Id(D2X), [NumLit(4.19), StringLit(ImAQb), NumLit(75.29)]), NumLit(14.92)), Return()])), (StringLit(LC), Continue)], None)])), (BooleanLit(True), VarDecl(Id(VW), ArrayType([45.66, 34.13], StringType), None, NumLit(76.28))), (Id(kfQQ), Break)], If((BooleanLit(True), Continue), [(NumLit(87.23), AssignStmt(Id(TetV), BooleanLit(False))), (NumLit(99.01), VarDecl(Id(EE), ArrayType([61.92], BoolType), None, None)), (Id(CI), Continue), (StringLit(CKL), If((StringLit(gssUc), Break), [(Id(x9), Return())], Return())), (StringLit(y), Block([If((Id(KuJe), AssignStmt(Id(UG2T), NumLit(30.31))), [(NumLit(77.43), AssignStmt(ArrayCell(Id(WFtH), [Id(qpmg)]), BooleanLit(True))), (NumLit(26.96), VarDecl(Id(bE), None, var, Id(C_2)))], None), Return(), Block([VarDecl(Id(amn), None, dynamic, None)])]))], None)), For(Id(ok), BooleanLit(True), Id(ty6), Return(Id(xO)))])), FuncDecl(Id(KH), [VarDecl(Id(Aif), ArrayType([69.02], StringType), None, None), VarDecl(Id(bD), ArrayType([97.65, 99.59], BoolType), None, None), VarDecl(Id(d5W), StringType, None, None)], Return(NumLit(63.7))), FuncDecl(Id(vDU), [], Return(StringLit(SJL)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115383))

	def test_21530115384(self):
		input = '''
func URX (number Pg[43.74])	return n8
'''
		expect = '''Program([FuncDecl(Id(URX), [VarDecl(Id(Pg), ArrayType([43.74], NumberType), None, None)], Return(Id(n8)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115384))

	def test_21530115385(self):
		input = '''
func N3 ()	return "pwxr"

bool de6f <- "opZ"
string Jm[15.45]
func gd1E (bool W4, string He0)	return 38.19

'''
		expect = '''Program([FuncDecl(Id(N3), [], Return(StringLit(pwxr))), VarDecl(Id(de6f), BoolType, None, StringLit(opZ)), VarDecl(Id(Jm), ArrayType([15.45], StringType), None, None), FuncDecl(Id(gd1E), [VarDecl(Id(W4), BoolType, None, None), VarDecl(Id(He0), StringType, None, None)], Return(NumLit(38.19)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115385))

	def test_21530115386(self):
		input = '''
bool SUC
func nbS (bool WEw[77.14,12.75,31.6], number iJ[14.39,36.52], number l2e[92.73,10.14])
	begin
		Q8w()
		continue
		wEOA["SWeH"] <- "Jm"
	end

string Uk[90.6,0.7,15.72] <- false
func y1 (string N2[4.11])
	return false
string eam3 <- "W"
'''
		expect = '''Program([VarDecl(Id(SUC), BoolType, None, None), FuncDecl(Id(nbS), [VarDecl(Id(WEw), ArrayType([77.14, 12.75, 31.6], BoolType), None, None), VarDecl(Id(iJ), ArrayType([14.39, 36.52], NumberType), None, None), VarDecl(Id(l2e), ArrayType([92.73, 10.14], NumberType), None, None)], Block([CallStmt(Id(Q8w), []), Continue, AssignStmt(ArrayCell(Id(wEOA), [StringLit(SWeH)]), StringLit(Jm))])), VarDecl(Id(Uk), ArrayType([90.6, 0.7, 15.72], StringType), None, BooleanLit(False)), FuncDecl(Id(y1), [VarDecl(Id(N2), ArrayType([4.11], StringType), None, None)], Return(BooleanLit(False))), VarDecl(Id(eam3), StringType, None, StringLit(W))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115386))

	def test_21530115387(self):
		input = '''
func q3 (number lQ[31.38], number m6ln[11.41], string pcku[76.24,41.17,37.02])	return
'''
		expect = '''Program([FuncDecl(Id(q3), [VarDecl(Id(lQ), ArrayType([31.38], NumberType), None, None), VarDecl(Id(m6ln), ArrayType([11.41], NumberType), None, None), VarDecl(Id(pcku), ArrayType([76.24, 41.17, 37.02], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115387))

	def test_21530115388(self):
		input = '''
number Kb[71.25,92.63]
var bnj <- eERR
func q5m ()	return "fbbS"

func JC ()	return true

'''
		expect = '''Program([VarDecl(Id(Kb), ArrayType([71.25, 92.63], NumberType), None, None), VarDecl(Id(bnj), None, var, Id(eERR)), FuncDecl(Id(q5m), [], Return(StringLit(fbbS))), FuncDecl(Id(JC), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115388))

	def test_21530115389(self):
		input = '''
func tCQq (number aCi)
	return Eg
func pIPs (number RBHr, number XbVo, bool V_vC)	return Sr4D
func v4 (bool aN_[61.72,42.63])	begin
		return 17.88
		string pM[16.88,97.6,87.43] <- "nBTD"
		begin
			continue
		end
	end

func r9 ()	return
'''
		expect = '''Program([FuncDecl(Id(tCQq), [VarDecl(Id(aCi), NumberType, None, None)], Return(Id(Eg))), FuncDecl(Id(pIPs), [VarDecl(Id(RBHr), NumberType, None, None), VarDecl(Id(XbVo), NumberType, None, None), VarDecl(Id(V_vC), BoolType, None, None)], Return(Id(Sr4D))), FuncDecl(Id(v4), [VarDecl(Id(aN_), ArrayType([61.72, 42.63], BoolType), None, None)], Block([Return(NumLit(17.88)), VarDecl(Id(pM), ArrayType([16.88, 97.6, 87.43], StringType), None, StringLit(nBTD)), Block([Continue])])), FuncDecl(Id(r9), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115389))

	def test_21530115390(self):
		input = '''
bool BE[88.24,49.58,93.04]
func osi ()	return
func Zxju (string xueU[64.35,4.32], string J0T[91.1,31.39])
	begin
		begin
			fZD()
		end
		MC()
	end

func OUl ()
	return "ioV"

func Vp (string ZyQ)	return false
'''
		expect = '''Program([VarDecl(Id(BE), ArrayType([88.24, 49.58, 93.04], BoolType), None, None), FuncDecl(Id(osi), [], Return()), FuncDecl(Id(Zxju), [VarDecl(Id(xueU), ArrayType([64.35, 4.32], StringType), None, None), VarDecl(Id(J0T), ArrayType([91.1, 31.39], StringType), None, None)], Block([Block([CallStmt(Id(fZD), [])]), CallStmt(Id(MC), [])])), FuncDecl(Id(OUl), [], Return(StringLit(ioV))), FuncDecl(Id(Vp), [VarDecl(Id(ZyQ), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115390))

	def test_21530115391(self):
		input = '''
number vor <- "YiX"
func EX ()	return
func Q_ (string Rm4g, bool sh[32.25,13.68], bool pp)	return true
'''
		expect = '''Program([VarDecl(Id(vor), NumberType, None, StringLit(YiX)), FuncDecl(Id(EX), [], Return()), FuncDecl(Id(Q_), [VarDecl(Id(Rm4g), StringType, None, None), VarDecl(Id(sh), ArrayType([32.25, 13.68], BoolType), None, None), VarDecl(Id(pp), BoolType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115391))

	def test_21530115392(self):
		input = '''
dynamic HyQ
number Rd[85.52,38.54,27.52] <- So
dynamic RE2 <- true
func r6Da ()	return 11.15
string DKQW
'''
		expect = '''Program([VarDecl(Id(HyQ), None, dynamic, None), VarDecl(Id(Rd), ArrayType([85.52, 38.54, 27.52], NumberType), None, Id(So)), VarDecl(Id(RE2), None, dynamic, BooleanLit(True)), FuncDecl(Id(r6Da), [], Return(NumLit(11.15))), VarDecl(Id(DKQW), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115392))

	def test_21530115393(self):
		input = '''
func oyi ()	return

func wfb (bool tti[19.66,34.22])
	begin
		continue
		break
	end

'''
		expect = '''Program([FuncDecl(Id(oyi), [], Return()), FuncDecl(Id(wfb), [VarDecl(Id(tti), ArrayType([19.66, 34.22], BoolType), None, None)], Block([Continue, Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115393))

	def test_21530115394(self):
		input = '''
func Gw ()
	return "ngojT"
bool C8Z[74.84] <- 20.74
bool x_
'''
		expect = '''Program([FuncDecl(Id(Gw), [], Return(StringLit(ngojT))), VarDecl(Id(C8Z), ArrayType([74.84], BoolType), None, NumLit(20.74)), VarDecl(Id(x_), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115394))

	def test_21530115395(self):
		input = '''
string in
'''
		expect = '''Program([VarDecl(Id(in), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115395))

	def test_21530115396(self):
		input = '''
number ky
number wG[0.12] <- "MUhFf"
func p8 ()	begin
	end
func DAg (number FQ, string lmUS[15.26,25.27,15.57], number wC)	begin
		break
	end
dynamic vH4D <- MaY
'''
		expect = '''Program([VarDecl(Id(ky), NumberType, None, None), VarDecl(Id(wG), ArrayType([0.12], NumberType), None, StringLit(MUhFf)), FuncDecl(Id(p8), [], Block([])), FuncDecl(Id(DAg), [VarDecl(Id(FQ), NumberType, None, None), VarDecl(Id(lmUS), ArrayType([15.26, 25.27, 15.57], StringType), None, None), VarDecl(Id(wC), NumberType, None, None)], Block([Break])), VarDecl(Id(vH4D), None, dynamic, Id(MaY))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115396))

	def test_21530115397(self):
		input = '''
string tj2[7.62,28.94,64.12] <- false
func M8Y (bool jp, string pu[79.12,90.58,19.84], number fqp7[99.1])
	return
'''
		expect = '''Program([VarDecl(Id(tj2), ArrayType([7.62, 28.94, 64.12], StringType), None, BooleanLit(False)), FuncDecl(Id(M8Y), [VarDecl(Id(jp), BoolType, None, None), VarDecl(Id(pu), ArrayType([79.12, 90.58, 19.84], StringType), None, None), VarDecl(Id(fqp7), ArrayType([99.1], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115397))

	def test_21530115398(self):
		input = '''
func qsUe (bool GzvT[65.25,50.28], bool sp)	return
func Su (string wLph[99.35,28.12])
	return 73.38

func bC1 (bool Je, bool IQ)
	begin
		for p8I until 52.47 by "KU"
			for vrb until Q4Q by false
				continue
		begin
			for Hx until JMeP by 91.85
				continue
			Tgd["s", "yhBYX"] <- 84.1
		end
		var n_ <- true
	end

number e2R[34.79,0.53,88.86] <- psgy
'''
		expect = '''Program([FuncDecl(Id(qsUe), [VarDecl(Id(GzvT), ArrayType([65.25, 50.28], BoolType), None, None), VarDecl(Id(sp), BoolType, None, None)], Return()), FuncDecl(Id(Su), [VarDecl(Id(wLph), ArrayType([99.35, 28.12], StringType), None, None)], Return(NumLit(73.38))), FuncDecl(Id(bC1), [VarDecl(Id(Je), BoolType, None, None), VarDecl(Id(IQ), BoolType, None, None)], Block([For(Id(p8I), NumLit(52.47), StringLit(KU), For(Id(vrb), Id(Q4Q), BooleanLit(False), Continue)), Block([For(Id(Hx), Id(JMeP), NumLit(91.85), Continue), AssignStmt(ArrayCell(Id(Tgd), [StringLit(s), StringLit(yhBYX)]), NumLit(84.1))]), VarDecl(Id(n_), None, var, BooleanLit(True))])), VarDecl(Id(e2R), ArrayType([34.79, 0.53, 88.86], NumberType), None, Id(psgy))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115398))

	def test_21530115399(self):
		input = '''
func ji2H ()	return 2.15
func FjoX ()
	return

func CS ()
	begin
		for CJcY until true by true
			Dk(50.98, false, true)
	end
bool cTe7[72.5] <- "pa"
'''
		expect = '''Program([FuncDecl(Id(ji2H), [], Return(NumLit(2.15))), FuncDecl(Id(FjoX), [], Return()), FuncDecl(Id(CS), [], Block([For(Id(CJcY), BooleanLit(True), BooleanLit(True), CallStmt(Id(Dk), [NumLit(50.98), BooleanLit(False), BooleanLit(True)]))])), VarDecl(Id(cTe7), ArrayType([72.5], BoolType), None, StringLit(pa))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115399))

	def test_21530115400(self):
		input = '''
func jbda ()	return "MMS"

bool q0H[76.36]
'''
		expect = '''Program([FuncDecl(Id(jbda), [], Return(StringLit(MMS))), VarDecl(Id(q0H), ArrayType([76.36], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115400))

	def test_21530115401(self):
		input = '''
func nYfs (string fbKh[89.62,86.27], bool fsR, number Bv0J[15.47])	begin
		break
	end
func sP (bool ewL, number uKR[60.19])	return false

func uOZ7 (bool iKZI)
	return 1.37

func rt (bool bM[91.55], number RdGl[77.7,80.84,19.83])	return "LPRtp"
'''
		expect = '''Program([FuncDecl(Id(nYfs), [VarDecl(Id(fbKh), ArrayType([89.62, 86.27], StringType), None, None), VarDecl(Id(fsR), BoolType, None, None), VarDecl(Id(Bv0J), ArrayType([15.47], NumberType), None, None)], Block([Break])), FuncDecl(Id(sP), [VarDecl(Id(ewL), BoolType, None, None), VarDecl(Id(uKR), ArrayType([60.19], NumberType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(uOZ7), [VarDecl(Id(iKZI), BoolType, None, None)], Return(NumLit(1.37))), FuncDecl(Id(rt), [VarDecl(Id(bM), ArrayType([91.55], BoolType), None, None), VarDecl(Id(RdGl), ArrayType([77.7, 80.84, 19.83], NumberType), None, None)], Return(StringLit(LPRtp)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115401))

	def test_21530115402(self):
		input = '''
func JK (bool MJB3[45.22,85.64,68.75])	return

var NG <- true
bool s3k[92.66]
func PMTT (string GO0[67.46,77.71])	return
'''
		expect = '''Program([FuncDecl(Id(JK), [VarDecl(Id(MJB3), ArrayType([45.22, 85.64, 68.75], BoolType), None, None)], Return()), VarDecl(Id(NG), None, var, BooleanLit(True)), VarDecl(Id(s3k), ArrayType([92.66], BoolType), None, None), FuncDecl(Id(PMTT), [VarDecl(Id(GO0), ArrayType([67.46, 77.71], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115402))

	def test_21530115403(self):
		input = '''
func XjcR (bool GxI[4.7,11.79,93.89], bool hkFh)	return
bool PT
string wi7_[77.07,2.09,23.37]
func S_ ()
	return pjE
'''
		expect = '''Program([FuncDecl(Id(XjcR), [VarDecl(Id(GxI), ArrayType([4.7, 11.79, 93.89], BoolType), None, None), VarDecl(Id(hkFh), BoolType, None, None)], Return()), VarDecl(Id(PT), BoolType, None, None), VarDecl(Id(wi7_), ArrayType([77.07, 2.09, 23.37], StringType), None, None), FuncDecl(Id(S_), [], Return(Id(pjE)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115403))

	def test_21530115404(self):
		input = '''
func x37i (bool Orxx[84.5], string Od, string iBFZ)
	return 68.89
string NO <- FJ
'''
		expect = '''Program([FuncDecl(Id(x37i), [VarDecl(Id(Orxx), ArrayType([84.5], BoolType), None, None), VarDecl(Id(Od), StringType, None, None), VarDecl(Id(iBFZ), StringType, None, None)], Return(NumLit(68.89))), VarDecl(Id(NO), StringType, None, Id(FJ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115404))

	def test_21530115405(self):
		input = '''
func ma ()	return
number rS[94.99,47.47] <- dlH3
bool P90[18.43] <- C5W
bool Xz[82.29,83.17]
'''
		expect = '''Program([FuncDecl(Id(ma), [], Return()), VarDecl(Id(rS), ArrayType([94.99, 47.47], NumberType), None, Id(dlH3)), VarDecl(Id(P90), ArrayType([18.43], BoolType), None, Id(C5W)), VarDecl(Id(Xz), ArrayType([82.29, 83.17], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115405))

	def test_21530115406(self):
		input = '''
bool Za9[12.59,32.47,84.25] <- 64.07
bool RMyf <- 43.49
number NPn[61.49,42.55,7.87] <- 22.26
'''
		expect = '''Program([VarDecl(Id(Za9), ArrayType([12.59, 32.47, 84.25], BoolType), None, NumLit(64.07)), VarDecl(Id(RMyf), BoolType, None, NumLit(43.49)), VarDecl(Id(NPn), ArrayType([61.49, 42.55, 7.87], NumberType), None, NumLit(22.26))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115406))

	def test_21530115407(self):
		input = '''
func gfd (number rq, string IZJa)
	return false

bool eS0 <- ea
'''
		expect = '''Program([FuncDecl(Id(gfd), [VarDecl(Id(rq), NumberType, None, None), VarDecl(Id(IZJa), StringType, None, None)], Return(BooleanLit(False))), VarDecl(Id(eS0), BoolType, None, Id(ea))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115407))

	def test_21530115408(self):
		input = '''
string NQ <- dV
bool i3T[55.5,71.88]
func Qmf (bool Wo)	begin
		var FY <- false
	end

func cZhV (bool urPv, string sW8q[3.07,93.01], string hjS[79.18,93.78,77.39])
	begin
	end
'''
		expect = '''Program([VarDecl(Id(NQ), StringType, None, Id(dV)), VarDecl(Id(i3T), ArrayType([55.5, 71.88], BoolType), None, None), FuncDecl(Id(Qmf), [VarDecl(Id(Wo), BoolType, None, None)], Block([VarDecl(Id(FY), None, var, BooleanLit(False))])), FuncDecl(Id(cZhV), [VarDecl(Id(urPv), BoolType, None, None), VarDecl(Id(sW8q), ArrayType([3.07, 93.01], StringType), None, None), VarDecl(Id(hjS), ArrayType([79.18, 93.78, 77.39], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115408))

	def test_21530115409(self):
		input = '''
bool w5V[74.92,70.34] <- qfuC
number Ce
bool Zt[74.14] <- "xt"
dynamic Fg
'''
		expect = '''Program([VarDecl(Id(w5V), ArrayType([74.92, 70.34], BoolType), None, Id(qfuC)), VarDecl(Id(Ce), NumberType, None, None), VarDecl(Id(Zt), ArrayType([74.14], BoolType), None, StringLit(xt)), VarDecl(Id(Fg), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115409))

	def test_21530115410(self):
		input = '''
func VSxE (bool yW[86.7,60.74,13.41], bool UF[54.23,79.98,78.58], number MU)
	return

func CMl (string a74[48.82,40.63])	return DBP
'''
		expect = '''Program([FuncDecl(Id(VSxE), [VarDecl(Id(yW), ArrayType([86.7, 60.74, 13.41], BoolType), None, None), VarDecl(Id(UF), ArrayType([54.23, 79.98, 78.58], BoolType), None, None), VarDecl(Id(MU), NumberType, None, None)], Return()), FuncDecl(Id(CMl), [VarDecl(Id(a74), ArrayType([48.82, 40.63], StringType), None, None)], Return(Id(DBP)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115410))

	def test_21530115411(self):
		input = '''
var oe <- h28
func r47f ()	return 11.57
func xDGE (number sG)
	begin
		wr3(42.85, T3o7)
		for cA71 until 31.8 by Oos
			begin
			end
		break
	end
number j0v6[97.05] <- 22.22
'''
		expect = '''Program([VarDecl(Id(oe), None, var, Id(h28)), FuncDecl(Id(r47f), [], Return(NumLit(11.57))), FuncDecl(Id(xDGE), [VarDecl(Id(sG), NumberType, None, None)], Block([CallStmt(Id(wr3), [NumLit(42.85), Id(T3o7)]), For(Id(cA71), NumLit(31.8), Id(Oos), Block([])), Break])), VarDecl(Id(j0v6), ArrayType([97.05], NumberType), None, NumLit(22.22))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115411))

	def test_21530115412(self):
		input = '''
dynamic TC_G
bool TBty[47.57,61.96,67.48]
'''
		expect = '''Program([VarDecl(Id(TC_G), None, dynamic, None), VarDecl(Id(TBty), ArrayType([47.57, 61.96, 67.48], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115412))

	def test_21530115413(self):
		input = '''
number r2Ua[17.27,39.71,6.52] <- 24.75
'''
		expect = '''Program([VarDecl(Id(r2Ua), ArrayType([17.27, 39.71, 6.52], NumberType), None, NumLit(24.75))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115413))

	def test_21530115414(self):
		input = '''
string nF <- 80.84
string MllJ[82.34,79.17]
bool xFC
string rd
func IjP ()	begin
		break
		begin
		end
	end
'''
		expect = '''Program([VarDecl(Id(nF), StringType, None, NumLit(80.84)), VarDecl(Id(MllJ), ArrayType([82.34, 79.17], StringType), None, None), VarDecl(Id(xFC), BoolType, None, None), VarDecl(Id(rd), StringType, None, None), FuncDecl(Id(IjP), [], Block([Break, Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115414))

	def test_21530115415(self):
		input = '''
string OGF[29.1,36.69,87.93]
func Kg (string dSnB)
	return 45.16

'''
		expect = '''Program([VarDecl(Id(OGF), ArrayType([29.1, 36.69, 87.93], StringType), None, None), FuncDecl(Id(Kg), [VarDecl(Id(dSnB), StringType, None, None)], Return(NumLit(45.16)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115415))

	def test_21530115416(self):
		input = '''
func SG (string bU)
	begin
		begin
			for kth until 80.25 by 36.85
				continue
		end
		cXq2(true, 78.42, 4.87)
		continue
	end
func fXB ()
	begin
		number Hm
		lGE()
		for XD until "UOJyE" by xK
			return false
	end

func fgN ()
	begin
		break
		number pCSy[20.08]
	end
bool lOD <- Wz
func aS (number am[64.56])
	return false

'''
		expect = '''Program([FuncDecl(Id(SG), [VarDecl(Id(bU), StringType, None, None)], Block([Block([For(Id(kth), NumLit(80.25), NumLit(36.85), Continue)]), CallStmt(Id(cXq2), [BooleanLit(True), NumLit(78.42), NumLit(4.87)]), Continue])), FuncDecl(Id(fXB), [], Block([VarDecl(Id(Hm), NumberType, None, None), CallStmt(Id(lGE), []), For(Id(XD), StringLit(UOJyE), Id(xK), Return(BooleanLit(False)))])), FuncDecl(Id(fgN), [], Block([Break, VarDecl(Id(pCSy), ArrayType([20.08], NumberType), None, None)])), VarDecl(Id(lOD), BoolType, None, Id(Wz)), FuncDecl(Id(aS), [VarDecl(Id(am), ArrayType([64.56], NumberType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115416))

	def test_21530115417(self):
		input = '''
func CD (string zFV, string rJ[23.88,90.7], string kvdd)	return 28.28

string Av[55.23,97.61] <- "U"
'''
		expect = '''Program([FuncDecl(Id(CD), [VarDecl(Id(zFV), StringType, None, None), VarDecl(Id(rJ), ArrayType([23.88, 90.7], StringType), None, None), VarDecl(Id(kvdd), StringType, None, None)], Return(NumLit(28.28))), VarDecl(Id(Av), ArrayType([55.23, 97.61], StringType), None, StringLit(U))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115417))

	def test_21530115418(self):
		input = '''
func FO (number GhE[50.81,47.3])	return bDTj

number Gl[93.62,64.48,53.79] <- Ro3H
string V_H[90.45,37.67]
dynamic Ge6U
'''
		expect = '''Program([FuncDecl(Id(FO), [VarDecl(Id(GhE), ArrayType([50.81, 47.3], NumberType), None, None)], Return(Id(bDTj))), VarDecl(Id(Gl), ArrayType([93.62, 64.48, 53.79], NumberType), None, Id(Ro3H)), VarDecl(Id(V_H), ArrayType([90.45, 37.67], StringType), None, None), VarDecl(Id(Ge6U), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115418))

	def test_21530115419(self):
		input = '''
func x_ (number BOz, string q8w)
	begin
	end
bool dYJ[67.34]
'''
		expect = '''Program([FuncDecl(Id(x_), [VarDecl(Id(BOz), NumberType, None, None), VarDecl(Id(q8w), StringType, None, None)], Block([])), VarDecl(Id(dYJ), ArrayType([67.34], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115419))

	def test_21530115420(self):
		input = '''
func SD ()
	return VJIq
func XP2E (bool AVb, bool NbX[22.08,3.25], number tmGL[92.03,6.61,20.99])	begin
		return
	end
number OZ[9.54,96.07,42.04]
func dhE (number lX[34.33,27.6])
	return BY

'''
		expect = '''Program([FuncDecl(Id(SD), [], Return(Id(VJIq))), FuncDecl(Id(XP2E), [VarDecl(Id(AVb), BoolType, None, None), VarDecl(Id(NbX), ArrayType([22.08, 3.25], BoolType), None, None), VarDecl(Id(tmGL), ArrayType([92.03, 6.61, 20.99], NumberType), None, None)], Block([Return()])), VarDecl(Id(OZ), ArrayType([9.54, 96.07, 42.04], NumberType), None, None), FuncDecl(Id(dhE), [VarDecl(Id(lX), ArrayType([34.33, 27.6], NumberType), None, None)], Return(Id(BY)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115420))

	def test_21530115421(self):
		input = '''
func Grc2 (string pkG[16.78,4.92,11.5])	return 6.44

'''
		expect = '''Program([FuncDecl(Id(Grc2), [VarDecl(Id(pkG), ArrayType([16.78, 4.92, 11.5], StringType), None, None)], Return(NumLit(6.44)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115421))

	def test_21530115422(self):
		input = '''
func s2 (number oPC6, string wq, string B2[54.2])	begin
		if (false) eHq(ny6, ko, false)
		elif (true)
		for ovN until 94.74 by false
			HW <- Hx1
		elif (Ef0)
		OYz(cU)
		elif (false)
		M5[57.82] <- true
		else return true
		dynamic UtS <- "Fac"
		begin
		end
	end
'''
		expect = '''Program([FuncDecl(Id(s2), [VarDecl(Id(oPC6), NumberType, None, None), VarDecl(Id(wq), StringType, None, None), VarDecl(Id(B2), ArrayType([54.2], StringType), None, None)], Block([If((BooleanLit(False), CallStmt(Id(eHq), [Id(ny6), Id(ko), BooleanLit(False)])), [(BooleanLit(True), For(Id(ovN), NumLit(94.74), BooleanLit(False), AssignStmt(Id(HW), Id(Hx1)))), (Id(Ef0), CallStmt(Id(OYz), [Id(cU)])), (BooleanLit(False), AssignStmt(ArrayCell(Id(M5), [NumLit(57.82)]), BooleanLit(True)))], Return(BooleanLit(True))), VarDecl(Id(UtS), None, dynamic, StringLit(Fac)), Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115422))

	def test_21530115423(self):
		input = '''
bool skt <- 91.25
var OH <- 17.24
func AqB (bool GSNe, bool fF[1.18,65.3,40.91], bool Nnrh[22.56,0.84])	return

func HJ7U (bool Le9o[17.84,90.98], string R7rW)	begin
		AQ()
		for tlmY until false by wqfr
			continue
		return "gQ"
	end
number Vpwz[94.47]
'''
		expect = '''Program([VarDecl(Id(skt), BoolType, None, NumLit(91.25)), VarDecl(Id(OH), None, var, NumLit(17.24)), FuncDecl(Id(AqB), [VarDecl(Id(GSNe), BoolType, None, None), VarDecl(Id(fF), ArrayType([1.18, 65.3, 40.91], BoolType), None, None), VarDecl(Id(Nnrh), ArrayType([22.56, 0.84], BoolType), None, None)], Return()), FuncDecl(Id(HJ7U), [VarDecl(Id(Le9o), ArrayType([17.84, 90.98], BoolType), None, None), VarDecl(Id(R7rW), StringType, None, None)], Block([CallStmt(Id(AQ), []), For(Id(tlmY), BooleanLit(False), Id(wqfr), Continue), Return(StringLit(gQ))])), VarDecl(Id(Vpwz), ArrayType([94.47], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115423))

	def test_21530115424(self):
		input = '''
func bb_P (number ByZO[19.22,11.77])
	begin
		continue
	end
func KCvb (number vu[82.08,58.93], string PYpp)
	return qyR6

'''
		expect = '''Program([FuncDecl(Id(bb_P), [VarDecl(Id(ByZO), ArrayType([19.22, 11.77], NumberType), None, None)], Block([Continue])), FuncDecl(Id(KCvb), [VarDecl(Id(vu), ArrayType([82.08, 58.93], NumberType), None, None), VarDecl(Id(PYpp), StringType, None, None)], Return(Id(qyR6)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115424))

	def test_21530115425(self):
		input = '''
string ziRm[58.11,66.88,43.55] <- 87.7
number fih0[39.36,78.32,70.23] <- ic
bool Y3JZ[51.42] <- 10.75
func BL ()
	return
var nZ8 <- false
'''
		expect = '''Program([VarDecl(Id(ziRm), ArrayType([58.11, 66.88, 43.55], StringType), None, NumLit(87.7)), VarDecl(Id(fih0), ArrayType([39.36, 78.32, 70.23], NumberType), None, Id(ic)), VarDecl(Id(Y3JZ), ArrayType([51.42], BoolType), None, NumLit(10.75)), FuncDecl(Id(BL), [], Return()), VarDecl(Id(nZ8), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115425))

	def test_21530115426(self):
		input = '''
number cx
func vDm (string Mxn[94.29,8.38,17.38], number Pw, string Rjz)	return false
number MNFE[79.77,66.86]
func fp (number xfN, bool vAWN)	begin
		begin
			Wq <- FJLS
		end
		break
	end
func Ii8l (number Ar[21.63,9.56], number o6yL)	begin
		for w7 until "cJ" by "oE"
			for Aub until D20b by true
				vsLy(PUY4, 95.42)
		for HaLy until 86.03 by 62.55
			return
		begin
			continue
			if ("qdQEV") gJ9m()
			elif ("Dw")
			break
			elif ("Z")
			return false
			elif (false)
			WUqq("yf")
			elif (f8)
			break
			elif (xl) DM(q3)
			number HxQ[1.52,12.14] <- 22.07
		end
	end
'''
		expect = '''Program([VarDecl(Id(cx), NumberType, None, None), FuncDecl(Id(vDm), [VarDecl(Id(Mxn), ArrayType([94.29, 8.38, 17.38], StringType), None, None), VarDecl(Id(Pw), NumberType, None, None), VarDecl(Id(Rjz), StringType, None, None)], Return(BooleanLit(False))), VarDecl(Id(MNFE), ArrayType([79.77, 66.86], NumberType), None, None), FuncDecl(Id(fp), [VarDecl(Id(xfN), NumberType, None, None), VarDecl(Id(vAWN), BoolType, None, None)], Block([Block([AssignStmt(Id(Wq), Id(FJLS))]), Break])), FuncDecl(Id(Ii8l), [VarDecl(Id(Ar), ArrayType([21.63, 9.56], NumberType), None, None), VarDecl(Id(o6yL), NumberType, None, None)], Block([For(Id(w7), StringLit(cJ), StringLit(oE), For(Id(Aub), Id(D20b), BooleanLit(True), CallStmt(Id(vsLy), [Id(PUY4), NumLit(95.42)]))), For(Id(HaLy), NumLit(86.03), NumLit(62.55), Return()), Block([Continue, If((StringLit(qdQEV), CallStmt(Id(gJ9m), [])), [(StringLit(Dw), Break), (StringLit(Z), Return(BooleanLit(False))), (BooleanLit(False), CallStmt(Id(WUqq), [StringLit(yf)])), (Id(f8), Break), (Id(xl), CallStmt(Id(DM), [Id(q3)]))], None), VarDecl(Id(HxQ), ArrayType([1.52, 12.14], NumberType), None, NumLit(22.07))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115426))

	def test_21530115427(self):
		input = '''
number vau[16.81]
string oe[96.71,94.61,71.71] <- true
func Utyr (string gg)
	begin
	end
string t_[69.7] <- 43.9
'''
		expect = '''Program([VarDecl(Id(vau), ArrayType([16.81], NumberType), None, None), VarDecl(Id(oe), ArrayType([96.71, 94.61, 71.71], StringType), None, BooleanLit(True)), FuncDecl(Id(Utyr), [VarDecl(Id(gg), StringType, None, None)], Block([])), VarDecl(Id(t_), ArrayType([69.7], StringType), None, NumLit(43.9))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115427))

	def test_21530115428(self):
		input = '''
func M1 (bool VQmj[43.2,47.29])	return

func uE (number P0po, number Zw[50.72])
	return
string RwCt[84.47]
bool uQz <- true
func ywW ()
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(M1), [VarDecl(Id(VQmj), ArrayType([43.2, 47.29], BoolType), None, None)], Return()), FuncDecl(Id(uE), [VarDecl(Id(P0po), NumberType, None, None), VarDecl(Id(Zw), ArrayType([50.72], NumberType), None, None)], Return()), VarDecl(Id(RwCt), ArrayType([84.47], StringType), None, None), VarDecl(Id(uQz), BoolType, None, BooleanLit(True)), FuncDecl(Id(ywW), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115428))

	def test_21530115429(self):
		input = '''
func ve (bool AB[63.2], number Z1w_, number TW9[52.7,20.15])	begin
		Vl <- KHB
		y0f[71.81] <- "YB"
	end
func dzY ()	begin
		for bd until "aiJ" by 44.8
			continue
		break
		dynamic m0 <- 95.85
	end
func dV (bool glvH[66.09], number lC, bool w5N)	return "h"
func RT (string ioI[31.31,17.29,98.13], bool LkB[63.07,20.93,16.58])	return qXo
'''
		expect = '''Program([FuncDecl(Id(ve), [VarDecl(Id(AB), ArrayType([63.2], BoolType), None, None), VarDecl(Id(Z1w_), NumberType, None, None), VarDecl(Id(TW9), ArrayType([52.7, 20.15], NumberType), None, None)], Block([AssignStmt(Id(Vl), Id(KHB)), AssignStmt(ArrayCell(Id(y0f), [NumLit(71.81)]), StringLit(YB))])), FuncDecl(Id(dzY), [], Block([For(Id(bd), StringLit(aiJ), NumLit(44.8), Continue), Break, VarDecl(Id(m0), None, dynamic, NumLit(95.85))])), FuncDecl(Id(dV), [VarDecl(Id(glvH), ArrayType([66.09], BoolType), None, None), VarDecl(Id(lC), NumberType, None, None), VarDecl(Id(w5N), BoolType, None, None)], Return(StringLit(h))), FuncDecl(Id(RT), [VarDecl(Id(ioI), ArrayType([31.31, 17.29, 98.13], StringType), None, None), VarDecl(Id(LkB), ArrayType([63.07, 20.93, 16.58], BoolType), None, None)], Return(Id(qXo)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115429))

	def test_21530115430(self):
		input = '''
func l2fk (string OIjs, bool A5[23.1], number lf)	return "UfG"
bool tn
'''
		expect = '''Program([FuncDecl(Id(l2fk), [VarDecl(Id(OIjs), StringType, None, None), VarDecl(Id(A5), ArrayType([23.1], BoolType), None, None), VarDecl(Id(lf), NumberType, None, None)], Return(StringLit(UfG))), VarDecl(Id(tn), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115430))

	def test_21530115431(self):
		input = '''
func zfuP ()
	return
dynamic co0a
'''
		expect = '''Program([FuncDecl(Id(zfuP), [], Return()), VarDecl(Id(co0a), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115431))

	def test_21530115432(self):
		input = '''
dynamic lX
func yLo (bool WZ, string VrkX, string lF9[67.11,54.86])	begin
	end
'''
		expect = '''Program([VarDecl(Id(lX), None, dynamic, None), FuncDecl(Id(yLo), [VarDecl(Id(WZ), BoolType, None, None), VarDecl(Id(VrkX), StringType, None, None), VarDecl(Id(lF9), ArrayType([67.11, 54.86], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115432))

	def test_21530115433(self):
		input = '''
dynamic rQ <- Nal
bool jx2
func AmQ5 (string DE)
	begin
	end
'''
		expect = '''Program([VarDecl(Id(rQ), None, dynamic, Id(Nal)), VarDecl(Id(jx2), BoolType, None, None), FuncDecl(Id(AmQ5), [VarDecl(Id(DE), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115433))

	def test_21530115434(self):
		input = '''
string Yq <- "o"
func ZI ()
	return

dynamic F6J_
string ZRZ <- "jQQO"
'''
		expect = '''Program([VarDecl(Id(Yq), StringType, None, StringLit(o)), FuncDecl(Id(ZI), [], Return()), VarDecl(Id(F6J_), None, dynamic, None), VarDecl(Id(ZRZ), StringType, None, StringLit(jQQO))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115434))

	def test_21530115435(self):
		input = '''
bool SyLQ
func Qrfp (string qh)	return

'''
		expect = '''Program([VarDecl(Id(SyLQ), BoolType, None, None), FuncDecl(Id(Qrfp), [VarDecl(Id(qh), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115435))

	def test_21530115436(self):
		input = '''
func DG (bool OT)	begin
		bool XF[97.79,35.12,12.9]
		break
		var KbF <- "vxEaz"
	end

func W1mb (number ozrn, bool FV2[84.98])	return
func Zg7 (string vZwK, number ZE[72.0,91.26,0.5], bool EN9B)
	begin
		for EIr7 until true by true
			break
		for Xjq until 86.77 by true
			break
		break
	end

'''
		expect = '''Program([FuncDecl(Id(DG), [VarDecl(Id(OT), BoolType, None, None)], Block([VarDecl(Id(XF), ArrayType([97.79, 35.12, 12.9], BoolType), None, None), Break, VarDecl(Id(KbF), None, var, StringLit(vxEaz))])), FuncDecl(Id(W1mb), [VarDecl(Id(ozrn), NumberType, None, None), VarDecl(Id(FV2), ArrayType([84.98], BoolType), None, None)], Return()), FuncDecl(Id(Zg7), [VarDecl(Id(vZwK), StringType, None, None), VarDecl(Id(ZE), ArrayType([72.0, 91.26, 0.5], NumberType), None, None), VarDecl(Id(EN9B), BoolType, None, None)], Block([For(Id(EIr7), BooleanLit(True), BooleanLit(True), Break), For(Id(Xjq), NumLit(86.77), BooleanLit(True), Break), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115436))

	def test_21530115437(self):
		input = '''
string xf3f[68.13,26.66,44.19]
func Y4 (string eD[73.57], number tl2K, string Bm9R)	return false

'''
		expect = '''Program([VarDecl(Id(xf3f), ArrayType([68.13, 26.66, 44.19], StringType), None, None), FuncDecl(Id(Y4), [VarDecl(Id(eD), ArrayType([73.57], StringType), None, None), VarDecl(Id(tl2K), NumberType, None, None), VarDecl(Id(Bm9R), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115437))

	def test_21530115438(self):
		input = '''
dynamic Lt5
number fW
'''
		expect = '''Program([VarDecl(Id(Lt5), None, dynamic, None), VarDecl(Id(fW), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115438))

	def test_21530115439(self):
		input = '''
func eF (bool Oq[93.74,98.09,50.22])
	return

dynamic Vv2 <- false
func uWfs ()	return
func mNYP (number msk2)	return
'''
		expect = '''Program([FuncDecl(Id(eF), [VarDecl(Id(Oq), ArrayType([93.74, 98.09, 50.22], BoolType), None, None)], Return()), VarDecl(Id(Vv2), None, dynamic, BooleanLit(False)), FuncDecl(Id(uWfs), [], Return()), FuncDecl(Id(mNYP), [VarDecl(Id(msk2), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115439))

	def test_21530115440(self):
		input = '''
string yr3[24.11,27.02]
func NB (number Z3j)
	return 56.24
bool UP7Z[88.58,12.72]
var DX <- ws
'''
		expect = '''Program([VarDecl(Id(yr3), ArrayType([24.11, 27.02], StringType), None, None), FuncDecl(Id(NB), [VarDecl(Id(Z3j), NumberType, None, None)], Return(NumLit(56.24))), VarDecl(Id(UP7Z), ArrayType([88.58, 12.72], BoolType), None, None), VarDecl(Id(DX), None, var, Id(ws))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115440))

	def test_21530115441(self):
		input = '''
func jWTg ()
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(jWTg), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115441))

	def test_21530115442(self):
		input = '''
func vi (number V5[28.4], string lHP[78.88,37.16,74.4], number gt5F[77.65,59.69,13.9])	begin
	end

bool FYe
'''
		expect = '''Program([FuncDecl(Id(vi), [VarDecl(Id(V5), ArrayType([28.4], NumberType), None, None), VarDecl(Id(lHP), ArrayType([78.88, 37.16, 74.4], StringType), None, None), VarDecl(Id(gt5F), ArrayType([77.65, 59.69, 13.9], NumberType), None, None)], Block([])), VarDecl(Id(FYe), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115442))

	def test_21530115443(self):
		input = '''
number hWR[25.58] <- 82.38
bool Znw[1.06,35.61]
func TdLi ()
	begin
		v5 <- IbRb
		EZk <- "LplV"
		string J9r <- true
	end
'''
		expect = '''Program([VarDecl(Id(hWR), ArrayType([25.58], NumberType), None, NumLit(82.38)), VarDecl(Id(Znw), ArrayType([1.06, 35.61], BoolType), None, None), FuncDecl(Id(TdLi), [], Block([AssignStmt(Id(v5), Id(IbRb)), AssignStmt(Id(EZk), StringLit(LplV)), VarDecl(Id(J9r), StringType, None, BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115443))

	def test_21530115444(self):
		input = '''
func Mh (number yoe[41.02,74.83,31.51], string EG)	return "N"

func OH ()	return
number FJe[37.83,68.73] <- 84.02
string Fnl
'''
		expect = '''Program([FuncDecl(Id(Mh), [VarDecl(Id(yoe), ArrayType([41.02, 74.83, 31.51], NumberType), None, None), VarDecl(Id(EG), StringType, None, None)], Return(StringLit(N))), FuncDecl(Id(OH), [], Return()), VarDecl(Id(FJe), ArrayType([37.83, 68.73], NumberType), None, NumLit(84.02)), VarDecl(Id(Fnl), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115444))

	def test_21530115445(self):
		input = '''
string Znb <- Mva
func TMJH (string jNy[84.72,81.34,49.95], number eru[25.25,95.97])
	begin
		begin
			BG <- true
			begin
				if (83.07)
				continue
				elif (false)
				begin
				end
				elif (F2y)
				sipQ()
				elif (16.97) if ("wb") if (false)
				begin
				end
				elif (true)
				break
				elif (false) continue
				elif (yp)
				break
				elif (d9d)
				return
				else break
				elif (true) Rza[true] <- false
				elif ("K")
				NE3m <- "Olq"
				elif (4.99)
				continue
				elif (48.82)
				begin
				end
				elif (31.39) if (96.27) continue
				else break
				else string bTD_[34.44,83.69]
				elif ("X") break
				elif (12.6)
				break
				else Ioib(67.76, fu, f5)
				bool tt[15.42,90.71,48.21]
			end
			continue
		end
	end

func qDp (bool NctE[1.71])
	return false
func YN (number lWQ, string TZbb[17.69,4.57])	begin
		return
	end

'''
		expect = '''Program([VarDecl(Id(Znb), StringType, None, Id(Mva)), FuncDecl(Id(TMJH), [VarDecl(Id(jNy), ArrayType([84.72, 81.34, 49.95], StringType), None, None), VarDecl(Id(eru), ArrayType([25.25, 95.97], NumberType), None, None)], Block([Block([AssignStmt(Id(BG), BooleanLit(True)), Block([If((NumLit(83.07), Continue), [(BooleanLit(False), Block([])), (Id(F2y), CallStmt(Id(sipQ), [])), (NumLit(16.97), If((StringLit(wb), If((BooleanLit(False), Block([])), [(BooleanLit(True), Break), (BooleanLit(False), Continue), (Id(yp), Break), (Id(d9d), Return())], Break)), [(BooleanLit(True), AssignStmt(ArrayCell(Id(Rza), [BooleanLit(True)]), BooleanLit(False))), (StringLit(K), AssignStmt(Id(NE3m), StringLit(Olq))), (NumLit(4.99), Continue), (NumLit(48.82), Block([])), (NumLit(31.39), If((NumLit(96.27), Continue), [], Break))], VarDecl(Id(bTD_), ArrayType([34.44, 83.69], StringType), None, None))), (StringLit(X), Break), (NumLit(12.6), Break)], CallStmt(Id(Ioib), [NumLit(67.76), Id(fu), Id(f5)])), VarDecl(Id(tt), ArrayType([15.42, 90.71, 48.21], BoolType), None, None)]), Continue])])), FuncDecl(Id(qDp), [VarDecl(Id(NctE), ArrayType([1.71], BoolType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(YN), [VarDecl(Id(lWQ), NumberType, None, None), VarDecl(Id(TZbb), ArrayType([17.69, 4.57], StringType), None, None)], Block([Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115445))

	def test_21530115446(self):
		input = '''
number CxEe <- "iSCqO"
'''
		expect = '''Program([VarDecl(Id(CxEe), NumberType, None, StringLit(iSCqO))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115446))

	def test_21530115447(self):
		input = '''
number IoYQ[72.97,67.8,88.35]
'''
		expect = '''Program([VarDecl(Id(IoYQ), ArrayType([72.97, 67.8, 88.35], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115447))

	def test_21530115448(self):
		input = '''
dynamic ad
func hw (string giNU, number oA[38.21,99.71])	return B2

func Ye2q ()	return
var ST <- Has
number gV9u
'''
		expect = '''Program([VarDecl(Id(ad), None, dynamic, None), FuncDecl(Id(hw), [VarDecl(Id(giNU), StringType, None, None), VarDecl(Id(oA), ArrayType([38.21, 99.71], NumberType), None, None)], Return(Id(B2))), FuncDecl(Id(Ye2q), [], Return()), VarDecl(Id(ST), None, var, Id(Has)), VarDecl(Id(gV9u), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115448))

	def test_21530115449(self):
		input = '''
number X5[40.72]
func Yc (number Vne, number oeE[57.83,2.79,19.67])
	begin
		for Zj until rt by true
			return false
		if ("xuZep")
		for V83 until 90.36 by false
			break
		elif (lkp2) hiO <- 95.28
		elif (74.65)
		break
		elif (78.64)
		break
		elif ("LTd")
		for qK5 until true by false
			if (true)
			continue
			elif (Ab) for Cfj until true by 50.86
				break
			elif (42.55)
			break
			elif ("b") if (91.61) break
			elif (12.53)
			continue
			elif (45.3) return true
			elif (10.52)
			for bape until "nvao" by 83.53
				return
			elif (VLMU) string VO[73.32,69.69,19.19] <- rr
			else Z7a[false, false] <- true
			elif (Sr) if (56.91) break
			else continue
			elif ("gR") bool b5[19.76]
			else continue
		elif (27.42)
		dynamic dvpQ
	end

'''
		expect = '''Program([VarDecl(Id(X5), ArrayType([40.72], NumberType), None, None), FuncDecl(Id(Yc), [VarDecl(Id(Vne), NumberType, None, None), VarDecl(Id(oeE), ArrayType([57.83, 2.79, 19.67], NumberType), None, None)], Block([For(Id(Zj), Id(rt), BooleanLit(True), Return(BooleanLit(False))), If((StringLit(xuZep), For(Id(V83), NumLit(90.36), BooleanLit(False), Break)), [(Id(lkp2), AssignStmt(Id(hiO), NumLit(95.28))), (NumLit(74.65), Break), (NumLit(78.64), Break), (StringLit(LTd), For(Id(qK5), BooleanLit(True), BooleanLit(False), If((BooleanLit(True), Continue), [(Id(Ab), For(Id(Cfj), BooleanLit(True), NumLit(50.86), Break)), (NumLit(42.55), Break), (StringLit(b), If((NumLit(91.61), Break), [(NumLit(12.53), Continue), (NumLit(45.3), Return(BooleanLit(True))), (NumLit(10.52), For(Id(bape), StringLit(nvao), NumLit(83.53), Return())), (Id(VLMU), VarDecl(Id(VO), ArrayType([73.32, 69.69, 19.19], StringType), None, Id(rr)))], AssignStmt(ArrayCell(Id(Z7a), [BooleanLit(False), BooleanLit(False)]), BooleanLit(True)))), (Id(Sr), If((NumLit(56.91), Break), [], Continue)), (StringLit(gR), VarDecl(Id(b5), ArrayType([19.76], BoolType), None, None))], Continue))), (NumLit(27.42), VarDecl(Id(dvpQ), None, dynamic, None))], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115449))

	def test_21530115450(self):
		input = '''
func H9 ()
	return 32.07
string b50X[31.54]
string B6F <- false
func AV ()	begin
		number SC[20.76]
	end
'''
		expect = '''Program([FuncDecl(Id(H9), [], Return(NumLit(32.07))), VarDecl(Id(b50X), ArrayType([31.54], StringType), None, None), VarDecl(Id(B6F), StringType, None, BooleanLit(False)), FuncDecl(Id(AV), [], Block([VarDecl(Id(SC), ArrayType([20.76], NumberType), None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115450))

	def test_21530115451(self):
		input = '''
func qg (bool ZhTM[68.06,95.24], bool Lx, string MvLZ[12.28,73.85,68.23])	return "hlgl"
func t_C0 (bool btvN[31.17,12.96])
	return
func IR ()
	return "NR"
func fi (bool Th6[38.55,81.3], number aN_)	return
var CD8J <- "NI"
'''
		expect = '''Program([FuncDecl(Id(qg), [VarDecl(Id(ZhTM), ArrayType([68.06, 95.24], BoolType), None, None), VarDecl(Id(Lx), BoolType, None, None), VarDecl(Id(MvLZ), ArrayType([12.28, 73.85, 68.23], StringType), None, None)], Return(StringLit(hlgl))), FuncDecl(Id(t_C0), [VarDecl(Id(btvN), ArrayType([31.17, 12.96], BoolType), None, None)], Return()), FuncDecl(Id(IR), [], Return(StringLit(NR))), FuncDecl(Id(fi), [VarDecl(Id(Th6), ArrayType([38.55, 81.3], BoolType), None, None), VarDecl(Id(aN_), NumberType, None, None)], Return()), VarDecl(Id(CD8J), None, var, StringLit(NI))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115451))

	def test_21530115452(self):
		input = '''
number tS <- mQ71
func mlA (string vz[10.9], number r8D)	return

func gA (string HF, bool rpr)
	return 28.29

'''
		expect = '''Program([VarDecl(Id(tS), NumberType, None, Id(mQ71)), FuncDecl(Id(mlA), [VarDecl(Id(vz), ArrayType([10.9], StringType), None, None), VarDecl(Id(r8D), NumberType, None, None)], Return()), FuncDecl(Id(gA), [VarDecl(Id(HF), StringType, None, None), VarDecl(Id(rpr), BoolType, None, None)], Return(NumLit(28.29)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115452))

	def test_21530115453(self):
		input = '''
bool OlYR[97.55]
func iRoS (bool NT[9.19,10.06,58.68])	begin
		number nPm
		bool G_yA <- 61.36
	end
bool g3 <- "CQzj"
'''
		expect = '''Program([VarDecl(Id(OlYR), ArrayType([97.55], BoolType), None, None), FuncDecl(Id(iRoS), [VarDecl(Id(NT), ArrayType([9.19, 10.06, 58.68], BoolType), None, None)], Block([VarDecl(Id(nPm), NumberType, None, None), VarDecl(Id(G_yA), BoolType, None, NumLit(61.36))])), VarDecl(Id(g3), BoolType, None, StringLit(CQzj))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115453))

	def test_21530115454(self):
		input = '''
func GiQ (bool MPj[76.86,58.34,29.92], string T_V[49.09], bool CF)	return

func qE0 (number QT9, string xcX)
	begin
		continue
	end

func iBvR (bool Oi, number r8J3)
	begin
		break
		number tZ <- "PjYQ"
	end

'''
		expect = '''Program([FuncDecl(Id(GiQ), [VarDecl(Id(MPj), ArrayType([76.86, 58.34, 29.92], BoolType), None, None), VarDecl(Id(T_V), ArrayType([49.09], StringType), None, None), VarDecl(Id(CF), BoolType, None, None)], Return()), FuncDecl(Id(qE0), [VarDecl(Id(QT9), NumberType, None, None), VarDecl(Id(xcX), StringType, None, None)], Block([Continue])), FuncDecl(Id(iBvR), [VarDecl(Id(Oi), BoolType, None, None), VarDecl(Id(r8J3), NumberType, None, None)], Block([Break, VarDecl(Id(tZ), NumberType, None, StringLit(PjYQ))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115454))

	def test_21530115455(self):
		input = '''
number fd[13.75,45.31,70.52]
func Jq05 (bool oG[20.55], bool iUjD, bool XjxU)
	return 97.11
func ANUK (bool coa, string FE_)
	return "huv"

number cK <- true
'''
		expect = '''Program([VarDecl(Id(fd), ArrayType([13.75, 45.31, 70.52], NumberType), None, None), FuncDecl(Id(Jq05), [VarDecl(Id(oG), ArrayType([20.55], BoolType), None, None), VarDecl(Id(iUjD), BoolType, None, None), VarDecl(Id(XjxU), BoolType, None, None)], Return(NumLit(97.11))), FuncDecl(Id(ANUK), [VarDecl(Id(coa), BoolType, None, None), VarDecl(Id(FE_), StringType, None, None)], Return(StringLit(huv))), VarDecl(Id(cK), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115455))

	def test_21530115456(self):
		input = '''
func b6N (bool M16I, number rmF, string opg[10.96,24.76])	begin
		Q_jD[hhy4, "Di"] <- true
		if (kTL)
		if ("K") Dub[58.42, false] <- "CA"
		elif (true) JTxi[false, hRI, 10.29] <- 10.66
		else qFWi(ibi)
		elif (false) begin
			number Jgcy[68.11,57.78] <- ux9
			for Qa until C1F by false
				return "WFEq"
		end
		elif (12.09)
		for w7RH until 14.28 by true
			for To until HG4 by 45.19
				continue
		for uFrV until true by "dhUJ"
			if (true)
			Ib(uiO, Doa, false)
			elif (true) aTwX <- 93.02
			elif ("wNjL")
			break
			elif (false)
			vU["Q"] <- ds
			else break
	end

func qbfC (number Od[15.32,30.21,66.07])
	return

'''
		expect = '''Program([FuncDecl(Id(b6N), [VarDecl(Id(M16I), BoolType, None, None), VarDecl(Id(rmF), NumberType, None, None), VarDecl(Id(opg), ArrayType([10.96, 24.76], StringType), None, None)], Block([AssignStmt(ArrayCell(Id(Q_jD), [Id(hhy4), StringLit(Di)]), BooleanLit(True)), If((Id(kTL), If((StringLit(K), AssignStmt(ArrayCell(Id(Dub), [NumLit(58.42), BooleanLit(False)]), StringLit(CA))), [(BooleanLit(True), AssignStmt(ArrayCell(Id(JTxi), [BooleanLit(False), Id(hRI), NumLit(10.29)]), NumLit(10.66)))], CallStmt(Id(qFWi), [Id(ibi)]))), [(BooleanLit(False), Block([VarDecl(Id(Jgcy), ArrayType([68.11, 57.78], NumberType), None, Id(ux9)), For(Id(Qa), Id(C1F), BooleanLit(False), Return(StringLit(WFEq)))])), (NumLit(12.09), For(Id(w7RH), NumLit(14.28), BooleanLit(True), For(Id(To), Id(HG4), NumLit(45.19), Continue)))], None), For(Id(uFrV), BooleanLit(True), StringLit(dhUJ), If((BooleanLit(True), CallStmt(Id(Ib), [Id(uiO), Id(Doa), BooleanLit(False)])), [(BooleanLit(True), AssignStmt(Id(aTwX), NumLit(93.02))), (StringLit(wNjL), Break), (BooleanLit(False), AssignStmt(ArrayCell(Id(vU), [StringLit(Q)]), Id(ds)))], Break))])), FuncDecl(Id(qbfC), [VarDecl(Id(Od), ArrayType([15.32, 30.21, 66.07], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115456))

	def test_21530115457(self):
		input = '''
var ax <- "DlX"
var KjO <- "vl"
bool bEDP <- qvg
bool rJ <- 65.18
string HV[81.1,27.45,12.91]
'''
		expect = '''Program([VarDecl(Id(ax), None, var, StringLit(DlX)), VarDecl(Id(KjO), None, var, StringLit(vl)), VarDecl(Id(bEDP), BoolType, None, Id(qvg)), VarDecl(Id(rJ), BoolType, None, NumLit(65.18)), VarDecl(Id(HV), ArrayType([81.1, 27.45, 12.91], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115457))

	def test_21530115458(self):
		input = '''
dynamic CSp
string O18[66.48] <- "Sjxo"
func fp (bool lxHq, string PGmy[20.1,42.78,19.24])	return 35.03
func dQkF (string CvO[25.07,15.44,28.3])
	return

dynamic BDv
'''
		expect = '''Program([VarDecl(Id(CSp), None, dynamic, None), VarDecl(Id(O18), ArrayType([66.48], StringType), None, StringLit(Sjxo)), FuncDecl(Id(fp), [VarDecl(Id(lxHq), BoolType, None, None), VarDecl(Id(PGmy), ArrayType([20.1, 42.78, 19.24], StringType), None, None)], Return(NumLit(35.03))), FuncDecl(Id(dQkF), [VarDecl(Id(CvO), ArrayType([25.07, 15.44, 28.3], StringType), None, None)], Return()), VarDecl(Id(BDv), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115458))

	def test_21530115459(self):
		input = '''
func i0i4 (string oJL[70.21], string kdJA[23.92,71.99], string LhqY)
	return RT
'''
		expect = '''Program([FuncDecl(Id(i0i4), [VarDecl(Id(oJL), ArrayType([70.21], StringType), None, None), VarDecl(Id(kdJA), ArrayType([23.92, 71.99], StringType), None, None), VarDecl(Id(LhqY), StringType, None, None)], Return(Id(RT)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115459))

	def test_21530115460(self):
		input = '''
func AXjC (bool rS[5.41,13.14,43.64], number R8)
	return xgs

dynamic JEU
var QkR <- FWM
dynamic Ep <- true
'''
		expect = '''Program([FuncDecl(Id(AXjC), [VarDecl(Id(rS), ArrayType([5.41, 13.14, 43.64], BoolType), None, None), VarDecl(Id(R8), NumberType, None, None)], Return(Id(xgs))), VarDecl(Id(JEU), None, dynamic, None), VarDecl(Id(QkR), None, var, Id(FWM)), VarDecl(Id(Ep), None, dynamic, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115460))

	def test_21530115461(self):
		input = '''
func kq6 (string oR, number GH[46.13,19.79], string um[1.32,57.64,98.54])
	return 41.23

'''
		expect = '''Program([FuncDecl(Id(kq6), [VarDecl(Id(oR), StringType, None, None), VarDecl(Id(GH), ArrayType([46.13, 19.79], NumberType), None, None), VarDecl(Id(um), ArrayType([1.32, 57.64, 98.54], StringType), None, None)], Return(NumLit(41.23)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115461))

	def test_21530115462(self):
		input = '''
string PyDx[75.08] <- M_
bool CRfF[98.66] <- 82.22
bool R6w
func OX_q (bool tWP[5.53,39.99], string mBp7, bool pD)
	return false

func FS0y ()	return

'''
		expect = '''Program([VarDecl(Id(PyDx), ArrayType([75.08], StringType), None, Id(M_)), VarDecl(Id(CRfF), ArrayType([98.66], BoolType), None, NumLit(82.22)), VarDecl(Id(R6w), BoolType, None, None), FuncDecl(Id(OX_q), [VarDecl(Id(tWP), ArrayType([5.53, 39.99], BoolType), None, None), VarDecl(Id(mBp7), StringType, None, None), VarDecl(Id(pD), BoolType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(FS0y), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115462))

	def test_21530115463(self):
		input = '''
func sHyJ (number L2, string mB)	begin
		NG <- RY
	end
func pJ7 (number hq0[18.84,87.95])	return
'''
		expect = '''Program([FuncDecl(Id(sHyJ), [VarDecl(Id(L2), NumberType, None, None), VarDecl(Id(mB), StringType, None, None)], Block([AssignStmt(Id(NG), Id(RY))])), FuncDecl(Id(pJ7), [VarDecl(Id(hq0), ArrayType([18.84, 87.95], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115463))

	def test_21530115464(self):
		input = '''
number er[77.61]
number Uu[89.39,31.37] <- false
'''
		expect = '''Program([VarDecl(Id(er), ArrayType([77.61], NumberType), None, None), VarDecl(Id(Uu), ArrayType([89.39, 31.37], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115464))

	def test_21530115465(self):
		input = '''
func u4 (bool CJQx, bool D0yz[82.39,23.89])	return

string NI[21.94,9.12,93.87] <- "djvpJ"
string RPs7 <- 54.05
func U14 (number S5B, bool bU)	return false

func Cd ()	return
'''
		expect = '''Program([FuncDecl(Id(u4), [VarDecl(Id(CJQx), BoolType, None, None), VarDecl(Id(D0yz), ArrayType([82.39, 23.89], BoolType), None, None)], Return()), VarDecl(Id(NI), ArrayType([21.94, 9.12, 93.87], StringType), None, StringLit(djvpJ)), VarDecl(Id(RPs7), StringType, None, NumLit(54.05)), FuncDecl(Id(U14), [VarDecl(Id(S5B), NumberType, None, None), VarDecl(Id(bU), BoolType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(Cd), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115465))

	def test_21530115466(self):
		input = '''
func S8 (number N1c, string UIH[56.97,3.13], string VV)
	begin
		if (true)
		return ad
		elif (Mngu) bS8 <- "e"
		elif (eAxF) for RxPh until false by lMv
			if (dX)
			for Pteo until mWX by "mB"
				continue
			elif (37.14)
			continue
			elif (lt6) begin
				return "CJ"
			end
			elif (59.58)
			if (false)
			for qEWn until 15.66 by true
				continue
			elif (TM)
			break
			elif ("RWTzi")
			break
			elif (SM) d3Q8["sHCl"] <- au
			elif (74.75)
			continue
			elif ("Xd") begin
				for gqhz until w8i by 55.37
					break
				continue
			end
			elif (qi)
			begin
				LQik()
			end
			elif ("IDJ") for lx8 until "jDHw" by "Un"
				if ("rmUVJ") begin
					for vyM until akh by rF
						if (S41) bool Dt[68.08] <- "aF"
						elif (true) break
						elif (true) for NBxj until true by Zh
							begin
								for IXvo until PR9O by false
									number A1q[24.0,85.32] <- lfC
							end
						elif (55.32) cZI <- n_eZ
						elif ("G") break
						elif (true)
						for x8 until 66.21 by bWN
							break
						else begin
							c4Z <- LB_M
						end
					dynamic MLO <- "rwVwl"
				end
				elif ("q") e47 <- true
				elif (nh1)
				break
				elif ("NdG")
				return false
				elif (72.03)
				break
		elif ("v") var HXr0 <- false
		elif (false) QBRX[false, "Jot"] <- "oGmer"
		else rVht(42.18, "QPQ", u_da)
		dynamic K4h0
		return
	end

func hI ()	return true
'''
		expect = '''Program([FuncDecl(Id(S8), [VarDecl(Id(N1c), NumberType, None, None), VarDecl(Id(UIH), ArrayType([56.97, 3.13], StringType), None, None), VarDecl(Id(VV), StringType, None, None)], Block([If((BooleanLit(True), Return(Id(ad))), [(Id(Mngu), AssignStmt(Id(bS8), StringLit(e))), (Id(eAxF), For(Id(RxPh), BooleanLit(False), Id(lMv), If((Id(dX), For(Id(Pteo), Id(mWX), StringLit(mB), Continue)), [(NumLit(37.14), Continue), (Id(lt6), Block([Return(StringLit(CJ))])), (NumLit(59.58), If((BooleanLit(False), For(Id(qEWn), NumLit(15.66), BooleanLit(True), Continue)), [(Id(TM), Break), (StringLit(RWTzi), Break), (Id(SM), AssignStmt(ArrayCell(Id(d3Q8), [StringLit(sHCl)]), Id(au))), (NumLit(74.75), Continue), (StringLit(Xd), Block([For(Id(gqhz), Id(w8i), NumLit(55.37), Break), Continue])), (Id(qi), Block([CallStmt(Id(LQik), [])])), (StringLit(IDJ), For(Id(lx8), StringLit(jDHw), StringLit(Un), If((StringLit(rmUVJ), Block([For(Id(vyM), Id(akh), Id(rF), If((Id(S41), VarDecl(Id(Dt), ArrayType([68.08], BoolType), None, StringLit(aF))), [(BooleanLit(True), Break), (BooleanLit(True), For(Id(NBxj), BooleanLit(True), Id(Zh), Block([For(Id(IXvo), Id(PR9O), BooleanLit(False), VarDecl(Id(A1q), ArrayType([24.0, 85.32], NumberType), None, Id(lfC)))]))), (NumLit(55.32), AssignStmt(Id(cZI), Id(n_eZ))), (StringLit(G), Break), (BooleanLit(True), For(Id(x8), NumLit(66.21), Id(bWN), Break))], Block([AssignStmt(Id(c4Z), Id(LB_M))]))), VarDecl(Id(MLO), None, dynamic, StringLit(rwVwl))])), [(StringLit(q), AssignStmt(Id(e47), BooleanLit(True))), (Id(nh1), Break), (StringLit(NdG), Return(BooleanLit(False))), (NumLit(72.03), Break), (StringLit(v), VarDecl(Id(HXr0), None, var, BooleanLit(False))), (BooleanLit(False), AssignStmt(ArrayCell(Id(QBRX), [BooleanLit(False), StringLit(Jot)]), StringLit(oGmer)))], CallStmt(Id(rVht), [NumLit(42.18), StringLit(QPQ), Id(u_da)]))))], None))], None)))], None), VarDecl(Id(K4h0), None, dynamic, None), Return()])), FuncDecl(Id(hI), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115466))

	def test_21530115467(self):
		input = '''
func jxFB (number c1, number yE[92.56,48.94])	return k41w

var YTf <- vxxW
dynamic oDA <- FC47
func vFb (string Mz[99.44,16.23,66.58], bool QoV[85.19,91.17,64.14], number iZm)
	return "uNy"
'''
		expect = '''Program([FuncDecl(Id(jxFB), [VarDecl(Id(c1), NumberType, None, None), VarDecl(Id(yE), ArrayType([92.56, 48.94], NumberType), None, None)], Return(Id(k41w))), VarDecl(Id(YTf), None, var, Id(vxxW)), VarDecl(Id(oDA), None, dynamic, Id(FC47)), FuncDecl(Id(vFb), [VarDecl(Id(Mz), ArrayType([99.44, 16.23, 66.58], StringType), None, None), VarDecl(Id(QoV), ArrayType([85.19, 91.17, 64.14], BoolType), None, None), VarDecl(Id(iZm), NumberType, None, None)], Return(StringLit(uNy)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115467))

	def test_21530115468(self):
		input = '''
bool yx7[97.79,2.97]
'''
		expect = '''Program([VarDecl(Id(yx7), ArrayType([97.79, 2.97], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115468))

	def test_21530115469(self):
		input = '''
func zIn6 ()
	return true

dynamic K5v <- 33.11
'''
		expect = '''Program([FuncDecl(Id(zIn6), [], Return(BooleanLit(True))), VarDecl(Id(K5v), None, dynamic, NumLit(33.11))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115469))

	def test_21530115470(self):
		input = '''
string zw6D <- 45.71
func Bn (number Oj[15.01,68.78])	return
'''
		expect = '''Program([VarDecl(Id(zw6D), StringType, None, NumLit(45.71)), FuncDecl(Id(Bn), [VarDecl(Id(Oj), ArrayType([15.01, 68.78], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115470))

	def test_21530115471(self):
		input = '''
dynamic VM <- "psxWh"
var Ldg <- SZmJ
string NgE[14.92,99.97,47.15] <- false
'''
		expect = '''Program([VarDecl(Id(VM), None, dynamic, StringLit(psxWh)), VarDecl(Id(Ldg), None, var, Id(SZmJ)), VarDecl(Id(NgE), ArrayType([14.92, 99.97, 47.15], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115471))

	def test_21530115472(self):
		input = '''
func je0o ()
	return

string wnOG
dynamic VC <- lA
'''
		expect = '''Program([FuncDecl(Id(je0o), [], Return()), VarDecl(Id(wnOG), StringType, None, None), VarDecl(Id(VC), None, dynamic, Id(lA))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115472))

	def test_21530115473(self):
		input = '''
func lG3Y (bool FN[4.53,6.56,31.54], string W8Zt, bool vCQ6[60.8])	return
func d0 (string icR, bool vB[13.11,19.25])
	return

number b9vp <- true
func cU (bool vXN)	return 4.56

var jlk <- "jPamP"
'''
		expect = '''Program([FuncDecl(Id(lG3Y), [VarDecl(Id(FN), ArrayType([4.53, 6.56, 31.54], BoolType), None, None), VarDecl(Id(W8Zt), StringType, None, None), VarDecl(Id(vCQ6), ArrayType([60.8], BoolType), None, None)], Return()), FuncDecl(Id(d0), [VarDecl(Id(icR), StringType, None, None), VarDecl(Id(vB), ArrayType([13.11, 19.25], BoolType), None, None)], Return()), VarDecl(Id(b9vp), NumberType, None, BooleanLit(True)), FuncDecl(Id(cU), [VarDecl(Id(vXN), BoolType, None, None)], Return(NumLit(4.56))), VarDecl(Id(jlk), None, var, StringLit(jPamP))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115473))

	def test_21530115474(self):
		input = '''
string dM6[4.06,65.51]
func jDe ()	return

'''
		expect = '''Program([VarDecl(Id(dM6), ArrayType([4.06, 65.51], StringType), None, None), FuncDecl(Id(jDe), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115474))

	def test_21530115475(self):
		input = '''
func fTW (bool cP[76.97,78.23,36.74])
	return
func Mxl ()
	return 21.23
string Kg
func uEO (number H8PI, string ht, bool H6Ek[44.5,97.67])
	begin
		tPMR <- false
	end

var rwN <- false
'''
		expect = '''Program([FuncDecl(Id(fTW), [VarDecl(Id(cP), ArrayType([76.97, 78.23, 36.74], BoolType), None, None)], Return()), FuncDecl(Id(Mxl), [], Return(NumLit(21.23))), VarDecl(Id(Kg), StringType, None, None), FuncDecl(Id(uEO), [VarDecl(Id(H8PI), NumberType, None, None), VarDecl(Id(ht), StringType, None, None), VarDecl(Id(H6Ek), ArrayType([44.5, 97.67], BoolType), None, None)], Block([AssignStmt(Id(tPMR), BooleanLit(False))])), VarDecl(Id(rwN), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115475))

	def test_21530115476(self):
		input = '''
func RD3n (string hO[37.83])	return 97.06

'''
		expect = '''Program([FuncDecl(Id(RD3n), [VarDecl(Id(hO), ArrayType([37.83], StringType), None, None)], Return(NumLit(97.06)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115476))

	def test_21530115477(self):
		input = '''
func zr (number sbW, bool Ur9[89.43,85.39,80.34], number eOtu)
	return
'''
		expect = '''Program([FuncDecl(Id(zr), [VarDecl(Id(sbW), NumberType, None, None), VarDecl(Id(Ur9), ArrayType([89.43, 85.39, 80.34], BoolType), None, None), VarDecl(Id(eOtu), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115477))

	def test_21530115478(self):
		input = '''
func HyGF (string JFj, string l3w)
	begin
		continue
		continue
		string BTx <- "JkM"
	end
func Ay (string LOX)
	begin
	end
func Nk (string w8x[28.41])
	return
bool R3[39.32,19.4]
'''
		expect = '''Program([FuncDecl(Id(HyGF), [VarDecl(Id(JFj), StringType, None, None), VarDecl(Id(l3w), StringType, None, None)], Block([Continue, Continue, VarDecl(Id(BTx), StringType, None, StringLit(JkM))])), FuncDecl(Id(Ay), [VarDecl(Id(LOX), StringType, None, None)], Block([])), FuncDecl(Id(Nk), [VarDecl(Id(w8x), ArrayType([28.41], StringType), None, None)], Return()), VarDecl(Id(R3), ArrayType([39.32, 19.4], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115478))

	def test_21530115479(self):
		input = '''
func XUGN (number r2TT)	return
func oW (number LUB, string Yl[44.72,91.17,84.54])
	return

dynamic OQ9 <- "cM"
func O8Ov ()
	return

'''
		expect = '''Program([FuncDecl(Id(XUGN), [VarDecl(Id(r2TT), NumberType, None, None)], Return()), FuncDecl(Id(oW), [VarDecl(Id(LUB), NumberType, None, None), VarDecl(Id(Yl), ArrayType([44.72, 91.17, 84.54], StringType), None, None)], Return()), VarDecl(Id(OQ9), None, dynamic, StringLit(cM)), FuncDecl(Id(O8Ov), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115479))

	def test_21530115480(self):
		input = '''
func eL (string D1d[96.59], bool wT)
	begin
		return 71.53
		X1(81.52)
		for sZ until xMZA by false
			string evDZ[17.46,65.97]
	end
'''
		expect = '''Program([FuncDecl(Id(eL), [VarDecl(Id(D1d), ArrayType([96.59], StringType), None, None), VarDecl(Id(wT), BoolType, None, None)], Block([Return(NumLit(71.53)), CallStmt(Id(X1), [NumLit(81.52)]), For(Id(sZ), Id(xMZA), BooleanLit(False), VarDecl(Id(evDZ), ArrayType([17.46, 65.97], StringType), None, None))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115480))

	def test_21530115481(self):
		input = '''
string sV4l[19.11,76.6] <- pWX
number yq <- RpBC
func Z4u (bool v67G)
	return
func gnl (string DQG, number fQq5[47.25,29.03], string rTLb[87.27,79.91])
	begin
		for VaL until "ml" by "O"
			for K22 until "eIaCr" by 93.38
				dF()
	end

func H8Z (bool Sj02[32.01,74.5], string Gkf, number Dl)	return
'''
		expect = '''Program([VarDecl(Id(sV4l), ArrayType([19.11, 76.6], StringType), None, Id(pWX)), VarDecl(Id(yq), NumberType, None, Id(RpBC)), FuncDecl(Id(Z4u), [VarDecl(Id(v67G), BoolType, None, None)], Return()), FuncDecl(Id(gnl), [VarDecl(Id(DQG), StringType, None, None), VarDecl(Id(fQq5), ArrayType([47.25, 29.03], NumberType), None, None), VarDecl(Id(rTLb), ArrayType([87.27, 79.91], StringType), None, None)], Block([For(Id(VaL), StringLit(ml), StringLit(O), For(Id(K22), StringLit(eIaCr), NumLit(93.38), CallStmt(Id(dF), [])))])), FuncDecl(Id(H8Z), [VarDecl(Id(Sj02), ArrayType([32.01, 74.5], BoolType), None, None), VarDecl(Id(Gkf), StringType, None, None), VarDecl(Id(Dl), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115481))

	def test_21530115482(self):
		input = '''
func UdI (string Cg[60.21,82.61], string Ph[77.22], string Mv0F[22.29,47.38])
	begin
		string Fzl <- "CNEP"
	end
func s4Ly (number Nyiv, bool pT, bool nPT)	return
'''
		expect = '''Program([FuncDecl(Id(UdI), [VarDecl(Id(Cg), ArrayType([60.21, 82.61], StringType), None, None), VarDecl(Id(Ph), ArrayType([77.22], StringType), None, None), VarDecl(Id(Mv0F), ArrayType([22.29, 47.38], StringType), None, None)], Block([VarDecl(Id(Fzl), StringType, None, StringLit(CNEP))])), FuncDecl(Id(s4Ly), [VarDecl(Id(Nyiv), NumberType, None, None), VarDecl(Id(pT), BoolType, None, None), VarDecl(Id(nPT), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115482))

	def test_21530115483(self):
		input = '''
func NM8g (string kK[1.88,57.55])
	begin
		for LRsn until true by 28.43
			for cuxT until false by PUu
				vZ7w()
	end
string RSBE[99.07,66.6,5.71] <- "LmSDD"
func Udf ()	begin
		if ("G")
		continue
		elif (21.54) begin
		end
		elif (true)
		return P9o5
		for lPm until "teNA" by "ZCzP"
			bool w8 <- IzS
		continue
	end

func W8el (number QiQq, number Bt[16.04])	return SNY
'''
		expect = '''Program([FuncDecl(Id(NM8g), [VarDecl(Id(kK), ArrayType([1.88, 57.55], StringType), None, None)], Block([For(Id(LRsn), BooleanLit(True), NumLit(28.43), For(Id(cuxT), BooleanLit(False), Id(PUu), CallStmt(Id(vZ7w), [])))])), VarDecl(Id(RSBE), ArrayType([99.07, 66.6, 5.71], StringType), None, StringLit(LmSDD)), FuncDecl(Id(Udf), [], Block([If((StringLit(G), Continue), [(NumLit(21.54), Block([])), (BooleanLit(True), Return(Id(P9o5)))], None), For(Id(lPm), StringLit(teNA), StringLit(ZCzP), VarDecl(Id(w8), BoolType, None, Id(IzS))), Continue])), FuncDecl(Id(W8el), [VarDecl(Id(QiQq), NumberType, None, None), VarDecl(Id(Bt), ArrayType([16.04], NumberType), None, None)], Return(Id(SNY)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115483))

	def test_21530115484(self):
		input = '''
func DV (number w8dz, bool Ku74)
	begin
		string KD[69.98,79.65,0.72] <- Ad
	end
func NM (string RZa[20.2,88.63,71.87], string g4fp[31.33,31.67,96.3], string QP)	begin
		if (15.86)
		break
		elif ("vzXe")
		break
		elif (63.4)
		string KH <- 26.65
		elif (52.79)
		CHv(ot, "e", 49.1)
		return
		continue
	end

bool Ej[9.64,89.56] <- SNm7
func gKn (number AS)
	return
'''
		expect = '''Program([FuncDecl(Id(DV), [VarDecl(Id(w8dz), NumberType, None, None), VarDecl(Id(Ku74), BoolType, None, None)], Block([VarDecl(Id(KD), ArrayType([69.98, 79.65, 0.72], StringType), None, Id(Ad))])), FuncDecl(Id(NM), [VarDecl(Id(RZa), ArrayType([20.2, 88.63, 71.87], StringType), None, None), VarDecl(Id(g4fp), ArrayType([31.33, 31.67, 96.3], StringType), None, None), VarDecl(Id(QP), StringType, None, None)], Block([If((NumLit(15.86), Break), [(StringLit(vzXe), Break), (NumLit(63.4), VarDecl(Id(KH), StringType, None, NumLit(26.65))), (NumLit(52.79), CallStmt(Id(CHv), [Id(ot), StringLit(e), NumLit(49.1)]))], None), Return(), Continue])), VarDecl(Id(Ej), ArrayType([9.64, 89.56], BoolType), None, Id(SNm7)), FuncDecl(Id(gKn), [VarDecl(Id(AS), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115484))

	def test_21530115485(self):
		input = '''
func EJ7 (number VRNa, number Th8)	return bW
'''
		expect = '''Program([FuncDecl(Id(EJ7), [VarDecl(Id(VRNa), NumberType, None, None), VarDecl(Id(Th8), NumberType, None, None)], Return(Id(bW)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115485))

	def test_21530115486(self):
		input = '''
func X3 (number spR[68.56], string PCW[5.03,51.75,60.21], string cX[98.35,54.04])	return
string WjL
func WVg (bool vbBh)	begin
	end
'''
		expect = '''Program([FuncDecl(Id(X3), [VarDecl(Id(spR), ArrayType([68.56], NumberType), None, None), VarDecl(Id(PCW), ArrayType([5.03, 51.75, 60.21], StringType), None, None), VarDecl(Id(cX), ArrayType([98.35, 54.04], StringType), None, None)], Return()), VarDecl(Id(WjL), StringType, None, None), FuncDecl(Id(WVg), [VarDecl(Id(vbBh), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115486))

	def test_21530115487(self):
		input = '''
func Ox (number Cj2, string mKxU)	begin
	end

func DLb (number ntz[89.07,7.49], bool RVz, bool Ek)
	return false

func ueE6 ()
	return
'''
		expect = '''Program([FuncDecl(Id(Ox), [VarDecl(Id(Cj2), NumberType, None, None), VarDecl(Id(mKxU), StringType, None, None)], Block([])), FuncDecl(Id(DLb), [VarDecl(Id(ntz), ArrayType([89.07, 7.49], NumberType), None, None), VarDecl(Id(RVz), BoolType, None, None), VarDecl(Id(Ek), BoolType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(ueE6), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115487))

	def test_21530115488(self):
		input = '''
func wlqh (bool ivQV[81.83,68.02,75.24], string aSoY[45.65,18.04])
	return N3

var MEN <- "unAf"
number Mb <- true
func U78 (bool j9, string nRQ2[18.39,44.83,90.44], number Pg[60.99,10.33,23.34])	return false

'''
		expect = '''Program([FuncDecl(Id(wlqh), [VarDecl(Id(ivQV), ArrayType([81.83, 68.02, 75.24], BoolType), None, None), VarDecl(Id(aSoY), ArrayType([45.65, 18.04], StringType), None, None)], Return(Id(N3))), VarDecl(Id(MEN), None, var, StringLit(unAf)), VarDecl(Id(Mb), NumberType, None, BooleanLit(True)), FuncDecl(Id(U78), [VarDecl(Id(j9), BoolType, None, None), VarDecl(Id(nRQ2), ArrayType([18.39, 44.83, 90.44], StringType), None, None), VarDecl(Id(Pg), ArrayType([60.99, 10.33, 23.34], NumberType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115488))

	def test_21530115489(self):
		input = '''
number k9Gn[58.85,96.65,50.84]
func rF6 (string O0[10.62], string g9[87.54,4.94,7.72], number a2[7.46,31.92,25.52])	begin
	end
func bZo ()	return

func YuPE (string KVe_, bool i_G[24.14,94.67,85.33], bool ss)
	return

'''
		expect = '''Program([VarDecl(Id(k9Gn), ArrayType([58.85, 96.65, 50.84], NumberType), None, None), FuncDecl(Id(rF6), [VarDecl(Id(O0), ArrayType([10.62], StringType), None, None), VarDecl(Id(g9), ArrayType([87.54, 4.94, 7.72], StringType), None, None), VarDecl(Id(a2), ArrayType([7.46, 31.92, 25.52], NumberType), None, None)], Block([])), FuncDecl(Id(bZo), [], Return()), FuncDecl(Id(YuPE), [VarDecl(Id(KVe_), StringType, None, None), VarDecl(Id(i_G), ArrayType([24.14, 94.67, 85.33], BoolType), None, None), VarDecl(Id(ss), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115489))

	def test_21530115490(self):
		input = '''
func G4 (bool XCg, number QeH[57.01,51.02,61.6], number JD[55.97,3.2,54.65])
	return

func Qc (string Ae, number Gq, number ggj[29.35,60.98,0.75])
	return

string IXkG
func R2 ()
	begin
		begin
			continue
		end
		if (45.92)
		number xf[55.34,99.55]
		elif ("jW")
		break
		else begin
			cvi <- "cSUk"
			for viX until "npO" by 82.4
				for kut until true by GFl3
					number ZEe[8.31] <- true
			break
		end
	end

'''
		expect = '''Program([FuncDecl(Id(G4), [VarDecl(Id(XCg), BoolType, None, None), VarDecl(Id(QeH), ArrayType([57.01, 51.02, 61.6], NumberType), None, None), VarDecl(Id(JD), ArrayType([55.97, 3.2, 54.65], NumberType), None, None)], Return()), FuncDecl(Id(Qc), [VarDecl(Id(Ae), StringType, None, None), VarDecl(Id(Gq), NumberType, None, None), VarDecl(Id(ggj), ArrayType([29.35, 60.98, 0.75], NumberType), None, None)], Return()), VarDecl(Id(IXkG), StringType, None, None), FuncDecl(Id(R2), [], Block([Block([Continue]), If((NumLit(45.92), VarDecl(Id(xf), ArrayType([55.34, 99.55], NumberType), None, None)), [(StringLit(jW), Break)], Block([AssignStmt(Id(cvi), StringLit(cSUk)), For(Id(viX), StringLit(npO), NumLit(82.4), For(Id(kut), BooleanLit(True), Id(GFl3), VarDecl(Id(ZEe), ArrayType([8.31], NumberType), None, BooleanLit(True)))), Break]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115490))

	def test_21530115491(self):
		input = '''
string Oz2j[48.79] <- "o"
bool XJyO[44.52] <- 56.8
func Vp ()
	return
func ig ()	return
func zU (bool dtCp[93.62,21.69,38.72], bool PSy0[44.55,7.03])	return

'''
		expect = '''Program([VarDecl(Id(Oz2j), ArrayType([48.79], StringType), None, StringLit(o)), VarDecl(Id(XJyO), ArrayType([44.52], BoolType), None, NumLit(56.8)), FuncDecl(Id(Vp), [], Return()), FuncDecl(Id(ig), [], Return()), FuncDecl(Id(zU), [VarDecl(Id(dtCp), ArrayType([93.62, 21.69, 38.72], BoolType), None, None), VarDecl(Id(PSy0), ArrayType([44.55, 7.03], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115491))

	def test_21530115492(self):
		input = '''
func z_ (string fe1, string zRy, string qk[63.96])
	return "IKx"
func QwVf (string CSeJ)	return
bool yfi <- 13.29
func INr (bool jb, string Ko[8.58], string Tn[92.82,66.99])	return

func Z8I (number Gzkc, string K5t[28.01,61.85])	return true
'''
		expect = '''Program([FuncDecl(Id(z_), [VarDecl(Id(fe1), StringType, None, None), VarDecl(Id(zRy), StringType, None, None), VarDecl(Id(qk), ArrayType([63.96], StringType), None, None)], Return(StringLit(IKx))), FuncDecl(Id(QwVf), [VarDecl(Id(CSeJ), StringType, None, None)], Return()), VarDecl(Id(yfi), BoolType, None, NumLit(13.29)), FuncDecl(Id(INr), [VarDecl(Id(jb), BoolType, None, None), VarDecl(Id(Ko), ArrayType([8.58], StringType), None, None), VarDecl(Id(Tn), ArrayType([92.82, 66.99], StringType), None, None)], Return()), FuncDecl(Id(Z8I), [VarDecl(Id(Gzkc), NumberType, None, None), VarDecl(Id(K5t), ArrayType([28.01, 61.85], StringType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115492))

	def test_21530115493(self):
		input = '''
func ZN ()	return
func PxEM ()	begin
		if (4.22) for Vz until false by false
			for KJME until false by TF
				continue
		elif (true)
		if ("aiqgw") Soy <- "baX"
		elif (O8ki) hGqw["h"] <- "qRLu"
		elif (ZD7)
		bool Gp2r <- true
		elif (40.27)
		string yw_g <- 90.02
		elif (HF8) xx <- zPux
		for Xh until H3CV by false
			if ("vR") if (eor)
			var N9u <- "LL"
			else for PhXi until 43.3 by 42.78
				continue
			elif (DSn) if (41.37) return "UV"
			elif (false) for aR until true by Cbl
				break
			elif (29.75)
			break
			elif (false) string kW[14.92,19.85,42.89]
			elif (DlA7) if (yv)
			continue
			elif ("WV")
			continue
			elif (22.45)
			return x6U
			elif (PLaS) return s7
			elif ("hVF") break
	end
'''
		expect = '''Program([FuncDecl(Id(ZN), [], Return()), FuncDecl(Id(PxEM), [], Block([If((NumLit(4.22), For(Id(Vz), BooleanLit(False), BooleanLit(False), For(Id(KJME), BooleanLit(False), Id(TF), Continue))), [(BooleanLit(True), If((StringLit(aiqgw), AssignStmt(Id(Soy), StringLit(baX))), [(Id(O8ki), AssignStmt(ArrayCell(Id(hGqw), [StringLit(h)]), StringLit(qRLu))), (Id(ZD7), VarDecl(Id(Gp2r), BoolType, None, BooleanLit(True))), (NumLit(40.27), VarDecl(Id(yw_g), StringType, None, NumLit(90.02))), (Id(HF8), AssignStmt(Id(xx), Id(zPux)))], None))], None), For(Id(Xh), Id(H3CV), BooleanLit(False), If((StringLit(vR), If((Id(eor), VarDecl(Id(N9u), None, var, StringLit(LL))), [], For(Id(PhXi), NumLit(43.3), NumLit(42.78), Continue))), [(Id(DSn), If((NumLit(41.37), Return(StringLit(UV))), [(BooleanLit(False), For(Id(aR), BooleanLit(True), Id(Cbl), Break)), (NumLit(29.75), Break), (BooleanLit(False), VarDecl(Id(kW), ArrayType([14.92, 19.85, 42.89], StringType), None, None)), (Id(DlA7), If((Id(yv), Continue), [(StringLit(WV), Continue), (NumLit(22.45), Return(Id(x6U))), (Id(PLaS), Return(Id(s7))), (StringLit(hVF), Break)], None))], None))], None))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115493))

	def test_21530115494(self):
		input = '''
bool sOk[62.9] <- true
func B2 ()
	return 68.26
bool Hh3[41.48,67.84,57.27] <- CxqJ
func ZtX ()
	return k6PH

bool EqBU
'''
		expect = '''Program([VarDecl(Id(sOk), ArrayType([62.9], BoolType), None, BooleanLit(True)), FuncDecl(Id(B2), [], Return(NumLit(68.26))), VarDecl(Id(Hh3), ArrayType([41.48, 67.84, 57.27], BoolType), None, Id(CxqJ)), FuncDecl(Id(ZtX), [], Return(Id(k6PH))), VarDecl(Id(EqBU), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115494))

	def test_21530115495(self):
		input = '''
func rZgE (string AUd)	return false

var cF <- 62.52
bool G_Z[19.28] <- grL
'''
		expect = '''Program([FuncDecl(Id(rZgE), [VarDecl(Id(AUd), StringType, None, None)], Return(BooleanLit(False))), VarDecl(Id(cF), None, var, NumLit(62.52)), VarDecl(Id(G_Z), ArrayType([19.28], BoolType), None, Id(grL))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115495))

	def test_21530115496(self):
		input = '''
string w8G[27.29,68.47]
'''
		expect = '''Program([VarDecl(Id(w8G), ArrayType([27.29, 68.47], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115496))

	def test_21530115497(self):
		input = '''
dynamic ZjF
func b0Wi (bool Ra[5.2,44.54], string PI2s)	return xO6v
'''
		expect = '''Program([VarDecl(Id(ZjF), None, dynamic, None), FuncDecl(Id(b0Wi), [VarDecl(Id(Ra), ArrayType([5.2, 44.54], BoolType), None, None), VarDecl(Id(PI2s), StringType, None, None)], Return(Id(xO6v)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115497))

	def test_21530115498(self):
		input = '''
func yUgw (bool vY[19.62,91.44])
	return 30.23
'''
		expect = '''Program([FuncDecl(Id(yUgw), [VarDecl(Id(vY), ArrayType([19.62, 91.44], BoolType), None, None)], Return(NumLit(30.23)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115498))

	def test_21530115499(self):
		input = '''
number hEGh <- true
'''
		expect = '''Program([VarDecl(Id(hEGh), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115499))

	def test_21530115500(self):
		input = '''
func bU ()
	return

func pdO (bool sih)
	return
'''
		expect = '''Program([FuncDecl(Id(bU), [], Return()), FuncDecl(Id(pdO), [VarDecl(Id(sih), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115500))

	def test_21530115501(self):
		input = '''
func IG1 ()
	begin
		return
		Vq2[true, RZH8] <- true
	end

dynamic Bic
func v7Jr (string SGQ[68.35])	return hBi7

func dE95 ()
	begin
		if ("ZKz") string HS[97.35,34.9,99.96]
		elif (zNk)
		return "gkq"
		elif ("xE")
		if ("y") if ("n") break
		elif (false)
		for R3 until A6K by 6.48
			break
		elif (42.18) return false
		elif (false) number d7gv
		else if (NEUE) break
		elif (R0)
		return
		elif (53.04) return x4
		elif (e1) return false
		elif (true)
		break
		elif (86.03) return
		elif (39.16)
		SJn[17.99, K10] <- N6
		else continue
		for Mx until 52.03 by py
			break
	end

'''
		expect = '''Program([FuncDecl(Id(IG1), [], Block([Return(), AssignStmt(ArrayCell(Id(Vq2), [BooleanLit(True), Id(RZH8)]), BooleanLit(True))])), VarDecl(Id(Bic), None, dynamic, None), FuncDecl(Id(v7Jr), [VarDecl(Id(SGQ), ArrayType([68.35], StringType), None, None)], Return(Id(hBi7))), FuncDecl(Id(dE95), [], Block([If((StringLit(ZKz), VarDecl(Id(HS), ArrayType([97.35, 34.9, 99.96], StringType), None, None)), [(Id(zNk), Return(StringLit(gkq))), (StringLit(xE), If((StringLit(y), If((StringLit(n), Break), [(BooleanLit(False), For(Id(R3), Id(A6K), NumLit(6.48), Break)), (NumLit(42.18), Return(BooleanLit(False))), (BooleanLit(False), VarDecl(Id(d7gv), NumberType, None, None))], If((Id(NEUE), Break), [(Id(R0), Return()), (NumLit(53.04), Return(Id(x4))), (Id(e1), Return(BooleanLit(False))), (BooleanLit(True), Break), (NumLit(86.03), Return()), (NumLit(39.16), AssignStmt(ArrayCell(Id(SJn), [NumLit(17.99), Id(K10)]), Id(N6)))], Continue))), [], None))], None), For(Id(Mx), NumLit(52.03), Id(py), Break)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115501))

	def test_21530115502(self):
		input = '''
func aH (string Izg, bool Y0[78.27,77.46,14.82])
	begin
		return
		if (true)
		for GV until false by khx9
			break
		elif (83.32) if (uI) string ONy
		elif ("gkf")
		begin
			return
		end
		elif (15.02) for RD until "Ml" by "aXr"
			if ("I")
			k0("qsgl")
			elif (L0um)
			p04()
			elif (jA)
			number f1 <- false
		else bool hua[23.23,35.98] <- "Jy"
		else if (I7Ss)
		break
		elif (64.77)
		QfmT[false, "md", 88.86] <- Wtc
		elif (true) if (false)
		if (11.23) O2t[true] <- false
		elif ("CHa") if (XwW)
		B8KF(bk7I, "wj")
		elif (93.2) xCC(r1cr, "v", 38.73)
		elif (false)
		return
		else if ("mL") break
		elif (6.04) gGKM <- 65.71
		elif (false) continue
		elif (k0)
		return
		elif (true) return AH
		elif (61.42) for lvqh until true by cWt
			for zQZ until false by false
				return 81.01
		elif (PAOl) if (false) break
		elif (WbAI)
		continue
		else continue
		elif (DaR) string F5b3[56.37,9.18]
		elif (XyG) for Fsl until xhz by Wvut
			begin
				for mjI until false by "oOH"
					string ee[82.06,29.25] <- 58.37
			end
		elif (41.13)
		break
		begin
			begin
			end
			if (true)
			return 91.97
			elif (27.2)
			if (64.39) I6 <- false
			elif (false)
			continue
			elif (TZ)
			imZ[87.4] <- eh
			elif (qVgS) break
			elif (73.17)
			Sft <- 78.5
			elif (gR)
			continue
			elif ("Fv") break
			continue
		end
	end
'''
		expect = '''Program([FuncDecl(Id(aH), [VarDecl(Id(Izg), StringType, None, None), VarDecl(Id(Y0), ArrayType([78.27, 77.46, 14.82], BoolType), None, None)], Block([Return(), If((BooleanLit(True), For(Id(GV), BooleanLit(False), Id(khx9), Break)), [(NumLit(83.32), If((Id(uI), VarDecl(Id(ONy), StringType, None, None)), [(StringLit(gkf), Block([Return()])), (NumLit(15.02), For(Id(RD), StringLit(Ml), StringLit(aXr), If((StringLit(I), CallStmt(Id(k0), [StringLit(qsgl)])), [(Id(L0um), CallStmt(Id(p04), [])), (Id(jA), VarDecl(Id(f1), NumberType, None, BooleanLit(False)))], VarDecl(Id(hua), ArrayType([23.23, 35.98], BoolType), None, StringLit(Jy)))))], If((Id(I7Ss), Break), [(NumLit(64.77), AssignStmt(ArrayCell(Id(QfmT), [BooleanLit(False), StringLit(md), NumLit(88.86)]), Id(Wtc))), (BooleanLit(True), If((BooleanLit(False), If((NumLit(11.23), AssignStmt(ArrayCell(Id(O2t), [BooleanLit(True)]), BooleanLit(False))), [(StringLit(CHa), If((Id(XwW), CallStmt(Id(B8KF), [Id(bk7I), StringLit(wj)])), [(NumLit(93.2), CallStmt(Id(xCC), [Id(r1cr), StringLit(v), NumLit(38.73)])), (BooleanLit(False), Return())], If((StringLit(mL), Break), [(NumLit(6.04), AssignStmt(Id(gGKM), NumLit(65.71))), (BooleanLit(False), Continue), (Id(k0), Return()), (BooleanLit(True), Return(Id(AH))), (NumLit(61.42), For(Id(lvqh), BooleanLit(True), Id(cWt), For(Id(zQZ), BooleanLit(False), BooleanLit(False), Return(NumLit(81.01))))), (Id(PAOl), If((BooleanLit(False), Break), [(Id(WbAI), Continue)], Continue)), (Id(DaR), VarDecl(Id(F5b3), ArrayType([56.37, 9.18], StringType), None, None)), (Id(XyG), For(Id(Fsl), Id(xhz), Id(Wvut), Block([For(Id(mjI), BooleanLit(False), StringLit(oOH), VarDecl(Id(ee), ArrayType([82.06, 29.25], StringType), None, NumLit(58.37)))]))), (NumLit(41.13), Break)], None)))], None)), [], None))], None)))], None), Block([Block([]), If((BooleanLit(True), Return(NumLit(91.97))), [(NumLit(27.2), If((NumLit(64.39), AssignStmt(Id(I6), BooleanLit(False))), [(BooleanLit(False), Continue), (Id(TZ), AssignStmt(ArrayCell(Id(imZ), [NumLit(87.4)]), Id(eh))), (Id(qVgS), Break), (NumLit(73.17), AssignStmt(Id(Sft), NumLit(78.5))), (Id(gR), Continue), (StringLit(Fv), Break)], None))], None), Continue])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115502))

	def test_21530115503(self):
		input = '''
func pwF ()	begin
		break
	end
func XH (number UaF[48.57,66.75,35.87], string n0)
	return A4h

func Iu ()	return

'''
		expect = '''Program([FuncDecl(Id(pwF), [], Block([Break])), FuncDecl(Id(XH), [VarDecl(Id(UaF), ArrayType([48.57, 66.75, 35.87], NumberType), None, None), VarDecl(Id(n0), StringType, None, None)], Return(Id(A4h))), FuncDecl(Id(Iu), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115503))

	def test_21530115504(self):
		input = '''
string yA
number Shum[32.87,27.66]
'''
		expect = '''Program([VarDecl(Id(yA), StringType, None, None), VarDecl(Id(Shum), ArrayType([32.87, 27.66], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115504))

	def test_21530115505(self):
		input = '''
func ZCc (string a77f[89.62,95.76])
	return
bool Yjq[34.55]
string RI1w <- true
'''
		expect = '''Program([FuncDecl(Id(ZCc), [VarDecl(Id(a77f), ArrayType([89.62, 95.76], StringType), None, None)], Return()), VarDecl(Id(Yjq), ArrayType([34.55], BoolType), None, None), VarDecl(Id(RI1w), StringType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115505))

	def test_21530115506(self):
		input = '''
bool Ef[90.26]
string ROwy <- 45.91
bool Mtx[10.24,92.98,12.93]
bool NA[36.06,48.87,94.86]
'''
		expect = '''Program([VarDecl(Id(Ef), ArrayType([90.26], BoolType), None, None), VarDecl(Id(ROwy), StringType, None, NumLit(45.91)), VarDecl(Id(Mtx), ArrayType([10.24, 92.98, 12.93], BoolType), None, None), VarDecl(Id(NA), ArrayType([36.06, 48.87, 94.86], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115506))

	def test_21530115507(self):
		input = '''
func nM (bool Pjj[88.91], bool Xn[80.36])	begin
		bool o8cw <- true
	end

func RTi (string FY)
	begin
		fo[40.8, "Wynl"] <- lX
		continue
		bool w1[86.42] <- ggg
	end

func c3i ()
	begin
		for zu until BOA by 29.91
			for ZyL until zQF by 8.05
				bool d5Zr[62.49,41.45]
		continue
		for LUot until "u" by oktv
			z7r[98.62, false] <- A2z
	end
'''
		expect = '''Program([FuncDecl(Id(nM), [VarDecl(Id(Pjj), ArrayType([88.91], BoolType), None, None), VarDecl(Id(Xn), ArrayType([80.36], BoolType), None, None)], Block([VarDecl(Id(o8cw), BoolType, None, BooleanLit(True))])), FuncDecl(Id(RTi), [VarDecl(Id(FY), StringType, None, None)], Block([AssignStmt(ArrayCell(Id(fo), [NumLit(40.8), StringLit(Wynl)]), Id(lX)), Continue, VarDecl(Id(w1), ArrayType([86.42], BoolType), None, Id(ggg))])), FuncDecl(Id(c3i), [], Block([For(Id(zu), Id(BOA), NumLit(29.91), For(Id(ZyL), Id(zQF), NumLit(8.05), VarDecl(Id(d5Zr), ArrayType([62.49, 41.45], BoolType), None, None))), Continue, For(Id(LUot), StringLit(u), Id(oktv), AssignStmt(ArrayCell(Id(z7r), [NumLit(98.62), BooleanLit(False)]), Id(A2z)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115507))

	def test_21530115508(self):
		input = '''
number sl[14.94]
dynamic lP
'''
		expect = '''Program([VarDecl(Id(sl), ArrayType([14.94], NumberType), None, None), VarDecl(Id(lP), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115508))

	def test_21530115509(self):
		input = '''
var L45n <- Q4EJ
func Ygj (string VY[81.79], bool wXW5)
	return
number B_Xk[27.57,1.8,31.61] <- JO
bool KW[31.21]
func N1V (bool dPJ, string Xot, string m9[64.14,76.03])	return
'''
		expect = '''Program([VarDecl(Id(L45n), None, var, Id(Q4EJ)), FuncDecl(Id(Ygj), [VarDecl(Id(VY), ArrayType([81.79], StringType), None, None), VarDecl(Id(wXW5), BoolType, None, None)], Return()), VarDecl(Id(B_Xk), ArrayType([27.57, 1.8, 31.61], NumberType), None, Id(JO)), VarDecl(Id(KW), ArrayType([31.21], BoolType), None, None), FuncDecl(Id(N1V), [VarDecl(Id(dPJ), BoolType, None, None), VarDecl(Id(Xot), StringType, None, None), VarDecl(Id(m9), ArrayType([64.14, 76.03], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115509))

	def test_21530115510(self):
		input = '''
func f4 ()
	return 46.93
func STh_ (string FH, string NOl_)	begin
	end
func Jz (bool H_[12.87], string S4[59.52,22.88], bool LCkW)
	return t4h

string tlF[17.51,52.22]
func PWWf (string X4[80.8])	return true

'''
		expect = '''Program([FuncDecl(Id(f4), [], Return(NumLit(46.93))), FuncDecl(Id(STh_), [VarDecl(Id(FH), StringType, None, None), VarDecl(Id(NOl_), StringType, None, None)], Block([])), FuncDecl(Id(Jz), [VarDecl(Id(H_), ArrayType([12.87], BoolType), None, None), VarDecl(Id(S4), ArrayType([59.52, 22.88], StringType), None, None), VarDecl(Id(LCkW), BoolType, None, None)], Return(Id(t4h))), VarDecl(Id(tlF), ArrayType([17.51, 52.22], StringType), None, None), FuncDecl(Id(PWWf), [VarDecl(Id(X4), ArrayType([80.8], StringType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115510))

	def test_21530115511(self):
		input = '''
number GAo8[37.33]
string h2Yc[36.76]
func jl (string XG[34.16,64.07], number xfl, bool nWxZ[61.02,59.16])
	return false
number nFH[26.41]
'''
		expect = '''Program([VarDecl(Id(GAo8), ArrayType([37.33], NumberType), None, None), VarDecl(Id(h2Yc), ArrayType([36.76], StringType), None, None), FuncDecl(Id(jl), [VarDecl(Id(XG), ArrayType([34.16, 64.07], StringType), None, None), VarDecl(Id(xfl), NumberType, None, None), VarDecl(Id(nWxZ), ArrayType([61.02, 59.16], BoolType), None, None)], Return(BooleanLit(False))), VarDecl(Id(nFH), ArrayType([26.41], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115511))

	def test_21530115512(self):
		input = '''
number tv23[93.34,17.44,47.34] <- true
number P9T[37.01]
func lqo_ (number l0bo, bool gQaN)
	return
func nj (bool Vybo, bool CP[49.12,45.51], string SX4K[96.08,15.16])	begin
		var bLIj <- false
		break
		xOzv <- false
	end

'''
		expect = '''Program([VarDecl(Id(tv23), ArrayType([93.34, 17.44, 47.34], NumberType), None, BooleanLit(True)), VarDecl(Id(P9T), ArrayType([37.01], NumberType), None, None), FuncDecl(Id(lqo_), [VarDecl(Id(l0bo), NumberType, None, None), VarDecl(Id(gQaN), BoolType, None, None)], Return()), FuncDecl(Id(nj), [VarDecl(Id(Vybo), BoolType, None, None), VarDecl(Id(CP), ArrayType([49.12, 45.51], BoolType), None, None), VarDecl(Id(SX4K), ArrayType([96.08, 15.16], StringType), None, None)], Block([VarDecl(Id(bLIj), None, var, BooleanLit(False)), Break, AssignStmt(Id(xOzv), BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115512))

	def test_21530115513(self):
		input = '''
func zdfH (bool Rj)	return
func TpU0 ()	begin
		dynamic hk <- DLf
		continue
		begin
			break
			we(dRDt, "wVPoQ")
		end
	end

func x7kN (bool EzW6[55.45,31.98])
	begin
	end

number ZhR[86.42,5.78,65.84] <- false
'''
		expect = '''Program([FuncDecl(Id(zdfH), [VarDecl(Id(Rj), BoolType, None, None)], Return()), FuncDecl(Id(TpU0), [], Block([VarDecl(Id(hk), None, dynamic, Id(DLf)), Continue, Block([Break, CallStmt(Id(we), [Id(dRDt), StringLit(wVPoQ)])])])), FuncDecl(Id(x7kN), [VarDecl(Id(EzW6), ArrayType([55.45, 31.98], BoolType), None, None)], Block([])), VarDecl(Id(ZhR), ArrayType([86.42, 5.78, 65.84], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115513))

	def test_21530115514(self):
		input = '''
bool eSS0[78.67,65.51,26.3]
dynamic Cn
number ur[59.19,43.36] <- 32.61
func jCQG (bool bZ[7.56,55.85], bool VlM[86.31,66.74], number il[25.34,87.3,68.0])	return true

bool yOz[54.34,33.52,33.84] <- 5.85
'''
		expect = '''Program([VarDecl(Id(eSS0), ArrayType([78.67, 65.51, 26.3], BoolType), None, None), VarDecl(Id(Cn), None, dynamic, None), VarDecl(Id(ur), ArrayType([59.19, 43.36], NumberType), None, NumLit(32.61)), FuncDecl(Id(jCQG), [VarDecl(Id(bZ), ArrayType([7.56, 55.85], BoolType), None, None), VarDecl(Id(VlM), ArrayType([86.31, 66.74], BoolType), None, None), VarDecl(Id(il), ArrayType([25.34, 87.3, 68.0], NumberType), None, None)], Return(BooleanLit(True))), VarDecl(Id(yOz), ArrayType([54.34, 33.52, 33.84], BoolType), None, NumLit(5.85))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115514))

	def test_21530115515(self):
		input = '''
number OoW[17.69]
number Pc
number VwIw
func qn (number C87, number btBS[53.67,27.36,26.5])	return
'''
		expect = '''Program([VarDecl(Id(OoW), ArrayType([17.69], NumberType), None, None), VarDecl(Id(Pc), NumberType, None, None), VarDecl(Id(VwIw), NumberType, None, None), FuncDecl(Id(qn), [VarDecl(Id(C87), NumberType, None, None), VarDecl(Id(btBS), ArrayType([53.67, 27.36, 26.5], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115515))

	def test_21530115516(self):
		input = '''
string dA[44.14,66.11,20.71]
string jtxm <- 47.49
func KzAO ()	begin
		qj["Oz", "HBdJ", Cv_] <- EKx
		dynamic BA2f
	end
bool AUc <- "epe"
string FsOC <- 2.89
'''
		expect = '''Program([VarDecl(Id(dA), ArrayType([44.14, 66.11, 20.71], StringType), None, None), VarDecl(Id(jtxm), StringType, None, NumLit(47.49)), FuncDecl(Id(KzAO), [], Block([AssignStmt(ArrayCell(Id(qj), [StringLit(Oz), StringLit(HBdJ), Id(Cv_)]), Id(EKx)), VarDecl(Id(BA2f), None, dynamic, None)])), VarDecl(Id(AUc), BoolType, None, StringLit(epe)), VarDecl(Id(FsOC), StringType, None, NumLit(2.89))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115516))

	def test_21530115517(self):
		input = '''
func NRyr ()
	begin
		return
		FA <- false
		continue
	end
func Yw4 (bool Kq2V[43.74,62.14], string iqP, bool pn[4.83])
	return
string QU
number Ld7[18.7,5.02,29.32] <- 48.86
bool jjY[46.43]
'''
		expect = '''Program([FuncDecl(Id(NRyr), [], Block([Return(), AssignStmt(Id(FA), BooleanLit(False)), Continue])), FuncDecl(Id(Yw4), [VarDecl(Id(Kq2V), ArrayType([43.74, 62.14], BoolType), None, None), VarDecl(Id(iqP), StringType, None, None), VarDecl(Id(pn), ArrayType([4.83], BoolType), None, None)], Return()), VarDecl(Id(QU), StringType, None, None), VarDecl(Id(Ld7), ArrayType([18.7, 5.02, 29.32], NumberType), None, NumLit(48.86)), VarDecl(Id(jjY), ArrayType([46.43], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115517))

	def test_21530115518(self):
		input = '''
number tl
func Ps (number AQPz[33.28], number ngZb[71.38])	begin
		continue
	end
'''
		expect = '''Program([VarDecl(Id(tl), NumberType, None, None), FuncDecl(Id(Ps), [VarDecl(Id(AQPz), ArrayType([33.28], NumberType), None, None), VarDecl(Id(ngZb), ArrayType([71.38], NumberType), None, None)], Block([Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115518))

	def test_21530115519(self):
		input = '''
string yLqs[65.91] <- "L"
func nji ()
	begin
		continue
		for Kbl until iWQ by 95.58
			continue
		yFeW()
	end

func tQZ ()	begin
		xtrn["fWyv", "YEQ"] <- false
		return
		break
	end
func f4bW ()
	begin
		break
	end
string SU[43.07]
'''
		expect = '''Program([VarDecl(Id(yLqs), ArrayType([65.91], StringType), None, StringLit(L)), FuncDecl(Id(nji), [], Block([Continue, For(Id(Kbl), Id(iWQ), NumLit(95.58), Continue), CallStmt(Id(yFeW), [])])), FuncDecl(Id(tQZ), [], Block([AssignStmt(ArrayCell(Id(xtrn), [StringLit(fWyv), StringLit(YEQ)]), BooleanLit(False)), Return(), Break])), FuncDecl(Id(f4bW), [], Block([Break])), VarDecl(Id(SU), ArrayType([43.07], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115519))

	def test_21530115520(self):
		input = '''
func FjFi ()
	return

func kC (number bW7[18.5])
	return
func Q8uU (bool BpV_, bool eC, number MY)
	return oeKa
func K_Nz ()	begin
		if ("GWVev") glVz["iOGse"] <- UPD
		else begin
			eM("J", "qyUo")
			begin
			end
			return
		end
	end
func hX (number OVk1[76.76,93.35,42.3])	return
'''
		expect = '''Program([FuncDecl(Id(FjFi), [], Return()), FuncDecl(Id(kC), [VarDecl(Id(bW7), ArrayType([18.5], NumberType), None, None)], Return()), FuncDecl(Id(Q8uU), [VarDecl(Id(BpV_), BoolType, None, None), VarDecl(Id(eC), BoolType, None, None), VarDecl(Id(MY), NumberType, None, None)], Return(Id(oeKa))), FuncDecl(Id(K_Nz), [], Block([If((StringLit(GWVev), AssignStmt(ArrayCell(Id(glVz), [StringLit(iOGse)]), Id(UPD))), [], Block([CallStmt(Id(eM), [StringLit(J), StringLit(qyUo)]), Block([]), Return()]))])), FuncDecl(Id(hX), [VarDecl(Id(OVk1), ArrayType([76.76, 93.35, 42.3], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115520))

	def test_21530115521(self):
		input = '''
dynamic Gd
string KYAq <- true
bool XD9
string V2p <- 11.89
'''
		expect = '''Program([VarDecl(Id(Gd), None, dynamic, None), VarDecl(Id(KYAq), StringType, None, BooleanLit(True)), VarDecl(Id(XD9), BoolType, None, None), VarDecl(Id(V2p), StringType, None, NumLit(11.89))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115521))

	def test_21530115522(self):
		input = '''
bool cq[72.78]
string W_D[26.47,57.41,42.01]
string bW[57.8,25.86,68.11] <- ks
dynamic b6mc
bool ZI7[1.03]
'''
		expect = '''Program([VarDecl(Id(cq), ArrayType([72.78], BoolType), None, None), VarDecl(Id(W_D), ArrayType([26.47, 57.41, 42.01], StringType), None, None), VarDecl(Id(bW), ArrayType([57.8, 25.86, 68.11], StringType), None, Id(ks)), VarDecl(Id(b6mc), None, dynamic, None), VarDecl(Id(ZI7), ArrayType([1.03], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115522))

	def test_21530115523(self):
		input = '''
func Rdq (number Z3V[65.48,83.23], number N1B[76.94,50.93], string dgC7[51.44])	begin
		bool QUFb[27.42,55.28]
		begin
			number Tsrt
		end
		return js5A
	end

bool SAnx[43.46]
string C6V <- 22.04
func dL (bool CSb[22.94,7.91,68.36], string Tovs[94.16,11.67,81.78], bool FikN)	begin
		continue
	end

bool KD
'''
		expect = '''Program([FuncDecl(Id(Rdq), [VarDecl(Id(Z3V), ArrayType([65.48, 83.23], NumberType), None, None), VarDecl(Id(N1B), ArrayType([76.94, 50.93], NumberType), None, None), VarDecl(Id(dgC7), ArrayType([51.44], StringType), None, None)], Block([VarDecl(Id(QUFb), ArrayType([27.42, 55.28], BoolType), None, None), Block([VarDecl(Id(Tsrt), NumberType, None, None)]), Return(Id(js5A))])), VarDecl(Id(SAnx), ArrayType([43.46], BoolType), None, None), VarDecl(Id(C6V), StringType, None, NumLit(22.04)), FuncDecl(Id(dL), [VarDecl(Id(CSb), ArrayType([22.94, 7.91, 68.36], BoolType), None, None), VarDecl(Id(Tovs), ArrayType([94.16, 11.67, 81.78], StringType), None, None), VarDecl(Id(FikN), BoolType, None, None)], Block([Continue])), VarDecl(Id(KD), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115523))

	def test_21530115524(self):
		input = '''
number nd[90.26,4.98]
func BwM (bool O1Az, bool pQXi[12.97,6.32])
	begin
	end
string T2Ja[70.06,2.5,17.74] <- 0.96
'''
		expect = '''Program([VarDecl(Id(nd), ArrayType([90.26, 4.98], NumberType), None, None), FuncDecl(Id(BwM), [VarDecl(Id(O1Az), BoolType, None, None), VarDecl(Id(pQXi), ArrayType([12.97, 6.32], BoolType), None, None)], Block([])), VarDecl(Id(T2Ja), ArrayType([70.06, 2.5, 17.74], StringType), None, NumLit(0.96))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115524))

	def test_21530115525(self):
		input = '''
func ZF (bool Ef8[28.49], string dg)	return "h"

func jA (bool Fs, string Nf)
	return 14.59
bool tb[40.35]
func Rg1 (string t0[75.55])	return
'''
		expect = '''Program([FuncDecl(Id(ZF), [VarDecl(Id(Ef8), ArrayType([28.49], BoolType), None, None), VarDecl(Id(dg), StringType, None, None)], Return(StringLit(h))), FuncDecl(Id(jA), [VarDecl(Id(Fs), BoolType, None, None), VarDecl(Id(Nf), StringType, None, None)], Return(NumLit(14.59))), VarDecl(Id(tb), ArrayType([40.35], BoolType), None, None), FuncDecl(Id(Rg1), [VarDecl(Id(t0), ArrayType([75.55], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115525))

	def test_21530115526(self):
		input = '''
bool mg[7.33,74.84,34.01]
func wl (number e74S[59.81,4.2])
	begin
		continue
	end
func HE6 ()
	return

'''
		expect = '''Program([VarDecl(Id(mg), ArrayType([7.33, 74.84, 34.01], BoolType), None, None), FuncDecl(Id(wl), [VarDecl(Id(e74S), ArrayType([59.81, 4.2], NumberType), None, None)], Block([Continue])), FuncDecl(Id(HE6), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115526))

	def test_21530115527(self):
		input = '''
var aJ2 <- "zIeD"
func pUos (number wy[24.08,22.11,2.99])	return "ZCYj"
'''
		expect = '''Program([VarDecl(Id(aJ2), None, var, StringLit(zIeD)), FuncDecl(Id(pUos), [VarDecl(Id(wy), ArrayType([24.08, 22.11, 2.99], NumberType), None, None)], Return(StringLit(ZCYj)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115527))

	def test_21530115528(self):
		input = '''
var dm <- "QNeO"
func ZU5 (number iX, string AON, number J1e)
	return
'''
		expect = '''Program([VarDecl(Id(dm), None, var, StringLit(QNeO)), FuncDecl(Id(ZU5), [VarDecl(Id(iX), NumberType, None, None), VarDecl(Id(AON), StringType, None, None), VarDecl(Id(J1e), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115528))

	def test_21530115529(self):
		input = '''
bool ac2[9.92,8.38]
func FL (number qo, string rf[83.54,72.0])
	return
func qk (number yjRy, number yvoV, number GBU)
	return oh3Z

'''
		expect = '''Program([VarDecl(Id(ac2), ArrayType([9.92, 8.38], BoolType), None, None), FuncDecl(Id(FL), [VarDecl(Id(qo), NumberType, None, None), VarDecl(Id(rf), ArrayType([83.54, 72.0], StringType), None, None)], Return()), FuncDecl(Id(qk), [VarDecl(Id(yjRy), NumberType, None, None), VarDecl(Id(yvoV), NumberType, None, None), VarDecl(Id(GBU), NumberType, None, None)], Return(Id(oh3Z)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115529))

	def test_21530115530(self):
		input = '''
string qPQ0[28.17,78.0,78.52]
number mmJ
func dA (string X6KT[50.75,13.0,96.87], string dr[31.09,51.83], string zBzb[33.44])	begin
		Us(true)
		break
	end
bool lsXt <- oc
func Vu6 (number HlF[26.8], string TI[32.54,43.17])	return
'''
		expect = '''Program([VarDecl(Id(qPQ0), ArrayType([28.17, 78.0, 78.52], StringType), None, None), VarDecl(Id(mmJ), NumberType, None, None), FuncDecl(Id(dA), [VarDecl(Id(X6KT), ArrayType([50.75, 13.0, 96.87], StringType), None, None), VarDecl(Id(dr), ArrayType([31.09, 51.83], StringType), None, None), VarDecl(Id(zBzb), ArrayType([33.44], StringType), None, None)], Block([CallStmt(Id(Us), [BooleanLit(True)]), Break])), VarDecl(Id(lsXt), BoolType, None, Id(oc)), FuncDecl(Id(Vu6), [VarDecl(Id(HlF), ArrayType([26.8], NumberType), None, None), VarDecl(Id(TI), ArrayType([32.54, 43.17], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115530))

	def test_21530115531(self):
		input = '''
number P8ui[64.52,49.51,22.17] <- nCOp
string BIRa <- 12.43
func R_E (bool VSD[46.2,27.2,23.11], number GQGB[33.11,88.22], bool ycL)
	return "rxTS"
'''
		expect = '''Program([VarDecl(Id(P8ui), ArrayType([64.52, 49.51, 22.17], NumberType), None, Id(nCOp)), VarDecl(Id(BIRa), StringType, None, NumLit(12.43)), FuncDecl(Id(R_E), [VarDecl(Id(VSD), ArrayType([46.2, 27.2, 23.11], BoolType), None, None), VarDecl(Id(GQGB), ArrayType([33.11, 88.22], NumberType), None, None), VarDecl(Id(ycL), BoolType, None, None)], Return(StringLit(rxTS)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115531))

	def test_21530115532(self):
		input = '''
string CD[41.98]
func kIOq (string nc, string EN)	return 14.99

'''
		expect = '''Program([VarDecl(Id(CD), ArrayType([41.98], StringType), None, None), FuncDecl(Id(kIOq), [VarDecl(Id(nc), StringType, None, None), VarDecl(Id(EN), StringType, None, None)], Return(NumLit(14.99)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115532))

	def test_21530115533(self):
		input = '''
string vL[10.86,38.02] <- "bL"
'''
		expect = '''Program([VarDecl(Id(vL), ArrayType([10.86, 38.02], StringType), None, StringLit(bL))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115533))

	def test_21530115534(self):
		input = '''
var lK <- true
bool oX <- false
func Y0 ()
	return "otMJL"

'''
		expect = '''Program([VarDecl(Id(lK), None, var, BooleanLit(True)), VarDecl(Id(oX), BoolType, None, BooleanLit(False)), FuncDecl(Id(Y0), [], Return(StringLit(otMJL)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115534))

	def test_21530115535(self):
		input = '''
number qd51[56.48]
bool ElO
func GHw ()	return qX
'''
		expect = '''Program([VarDecl(Id(qd51), ArrayType([56.48], NumberType), None, None), VarDecl(Id(ElO), BoolType, None, None), FuncDecl(Id(GHw), [], Return(Id(qX)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115535))

	def test_21530115536(self):
		input = '''
func C_ (bool d1)
	return

bool LANB
func Kou (number UG8Z)
	return 55.71

var rE <- false
'''
		expect = '''Program([FuncDecl(Id(C_), [VarDecl(Id(d1), BoolType, None, None)], Return()), VarDecl(Id(LANB), BoolType, None, None), FuncDecl(Id(Kou), [VarDecl(Id(UG8Z), NumberType, None, None)], Return(NumLit(55.71))), VarDecl(Id(rE), None, var, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115536))

	def test_21530115537(self):
		input = '''
func St (string hIdH[27.01,47.64], bool vg[80.07,93.11,50.43], number eWu)
	begin
		p__M()
		FCkl(50.09)
		continue
	end

bool TSp[82.74,34.54] <- iv
bool TMU[72.51,45.08]
func Qqft ()	begin
		for fBtB until 28.94 by t4X
			if (Xum)
			begin
				break
				break
				bt[false, "TNmNZ", 24.04] <- "fmCz"
			end
			elif (false)
			break
			elif ("ibAA") continue
			elif ("hjX")
			continue
			elif (true)
			for ois until true by "YzW"
				for Uq until dAm by Ft
					return 67.91
			elif (44.23)
			if (m9cl) if (ULY)
			continue
			elif ("JbqTq") continue
			elif (mW0s) Ym <- true
			elif (47.9) begin
				RfN["hLPl", "hCVUR"] <- true
			end
			elif (87.49) continue
			elif (true)
			begin
			end
			elif (E7H) return
			elif (26.99)
			oPoo <- 67.72
			elif (14.13)
			e65()
			elif ("XpZ")
			continue
			elif (true)
			break
			else return
			else if (61.81)
			break
			elif (false)
			begin
			end
			elif (2.13)
			break
			elif (q336) break
			elif (ps) begin
				for cxp until GBNm by X3
					begin
					end
			end
			elif (false) continue
			else break
		if ("Ppo")
		string V4T
		elif (54.6)
		bool Qsiu[23.17,80.98,85.69] <- 36.04
		elif (true)
		return
		elif (true)
		jsB8(kGu, false)
		elif (jZ)
		if ("hw")
		string xxM
		elif (zWV)
		m83(Rck, "Mz")
		elif ("X")
		o_("PPH", W0me, false)
		elif (true)
		ABCh(DjL)
		elif (q8r)
		dhr <- 74.77
		else break
	end

func Oo ()	return 27.8

'''
		expect = '''Program([FuncDecl(Id(St), [VarDecl(Id(hIdH), ArrayType([27.01, 47.64], StringType), None, None), VarDecl(Id(vg), ArrayType([80.07, 93.11, 50.43], BoolType), None, None), VarDecl(Id(eWu), NumberType, None, None)], Block([CallStmt(Id(p__M), []), CallStmt(Id(FCkl), [NumLit(50.09)]), Continue])), VarDecl(Id(TSp), ArrayType([82.74, 34.54], BoolType), None, Id(iv)), VarDecl(Id(TMU), ArrayType([72.51, 45.08], BoolType), None, None), FuncDecl(Id(Qqft), [], Block([For(Id(fBtB), NumLit(28.94), Id(t4X), If((Id(Xum), Block([Break, Break, AssignStmt(ArrayCell(Id(bt), [BooleanLit(False), StringLit(TNmNZ), NumLit(24.04)]), StringLit(fmCz))])), [(BooleanLit(False), Break), (StringLit(ibAA), Continue), (StringLit(hjX), Continue), (BooleanLit(True), For(Id(ois), BooleanLit(True), StringLit(YzW), For(Id(Uq), Id(dAm), Id(Ft), Return(NumLit(67.91))))), (NumLit(44.23), If((Id(m9cl), If((Id(ULY), Continue), [(StringLit(JbqTq), Continue), (Id(mW0s), AssignStmt(Id(Ym), BooleanLit(True))), (NumLit(47.9), Block([AssignStmt(ArrayCell(Id(RfN), [StringLit(hLPl), StringLit(hCVUR)]), BooleanLit(True))])), (NumLit(87.49), Continue), (BooleanLit(True), Block([])), (Id(E7H), Return()), (NumLit(26.99), AssignStmt(Id(oPoo), NumLit(67.72))), (NumLit(14.13), CallStmt(Id(e65), [])), (StringLit(XpZ), Continue), (BooleanLit(True), Break)], Return())), [], If((NumLit(61.81), Break), [(BooleanLit(False), Block([])), (NumLit(2.13), Break), (Id(q336), Break), (Id(ps), Block([For(Id(cxp), Id(GBNm), Id(X3), Block([]))])), (BooleanLit(False), Continue)], Break)))], None)), If((StringLit(Ppo), VarDecl(Id(V4T), StringType, None, None)), [(NumLit(54.6), VarDecl(Id(Qsiu), ArrayType([23.17, 80.98, 85.69], BoolType), None, NumLit(36.04))), (BooleanLit(True), Return()), (BooleanLit(True), CallStmt(Id(jsB8), [Id(kGu), BooleanLit(False)])), (Id(jZ), If((StringLit(hw), VarDecl(Id(xxM), StringType, None, None)), [(Id(zWV), CallStmt(Id(m83), [Id(Rck), StringLit(Mz)])), (StringLit(X), CallStmt(Id(o_), [StringLit(PPH), Id(W0me), BooleanLit(False)])), (BooleanLit(True), CallStmt(Id(ABCh), [Id(DjL)])), (Id(q8r), AssignStmt(Id(dhr), NumLit(74.77)))], Break))], None)])), FuncDecl(Id(Oo), [], Return(NumLit(27.8)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115537))

	def test_21530115538(self):
		input = '''
number NqQ
var a5K6 <- vK2
func w1FU (bool c4K5[6.99], bool Ru4[43.78,19.21,30.51])
	return ny

func O7f ()
	begin
		if (false) begin
			continue
			mCt("zwmZ")
			string swSt
		end
		elif (xRkP)
		UPe(nXUW, false)
		elif ("gyU") return "V"
		elif (false) return 93.75
		elif (kTn)
		KWUz(ke9, W5c4, 51.6)
		elif (43.44) return JOd
		if (false) rG <- "P"
		else return
	end
'''
		expect = '''Program([VarDecl(Id(NqQ), NumberType, None, None), VarDecl(Id(a5K6), None, var, Id(vK2)), FuncDecl(Id(w1FU), [VarDecl(Id(c4K5), ArrayType([6.99], BoolType), None, None), VarDecl(Id(Ru4), ArrayType([43.78, 19.21, 30.51], BoolType), None, None)], Return(Id(ny))), FuncDecl(Id(O7f), [], Block([If((BooleanLit(False), Block([Continue, CallStmt(Id(mCt), [StringLit(zwmZ)]), VarDecl(Id(swSt), StringType, None, None)])), [(Id(xRkP), CallStmt(Id(UPe), [Id(nXUW), BooleanLit(False)])), (StringLit(gyU), Return(StringLit(V))), (BooleanLit(False), Return(NumLit(93.75))), (Id(kTn), CallStmt(Id(KWUz), [Id(ke9), Id(W5c4), NumLit(51.6)])), (NumLit(43.44), Return(Id(JOd)))], None), If((BooleanLit(False), AssignStmt(Id(rG), StringLit(P))), [], Return())]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115538))

	def test_21530115539(self):
		input = '''
string gZr[28.37,4.94] <- SYd
func Gj (number Lit[77.86,93.12], string APhq, bool Z6_X)	begin
		for kizJ until false by 55.21
			continue
		TuK <- oie
		TA8 <- "V"
	end
dynamic bFz
'''
		expect = '''Program([VarDecl(Id(gZr), ArrayType([28.37, 4.94], StringType), None, Id(SYd)), FuncDecl(Id(Gj), [VarDecl(Id(Lit), ArrayType([77.86, 93.12], NumberType), None, None), VarDecl(Id(APhq), StringType, None, None), VarDecl(Id(Z6_X), BoolType, None, None)], Block([For(Id(kizJ), BooleanLit(False), NumLit(55.21), Continue), AssignStmt(Id(TuK), Id(oie)), AssignStmt(Id(TA8), StringLit(V))])), VarDecl(Id(bFz), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115539))

	def test_21530115540(self):
		input = '''
var hJfq <- "phcpE"
func TS (bool rG6U[27.83,16.07,92.36], number M7RA, bool gPGz)	return "RkUw"
bool D0 <- "fWo"
bool dT0o
'''
		expect = '''Program([VarDecl(Id(hJfq), None, var, StringLit(phcpE)), FuncDecl(Id(TS), [VarDecl(Id(rG6U), ArrayType([27.83, 16.07, 92.36], BoolType), None, None), VarDecl(Id(M7RA), NumberType, None, None), VarDecl(Id(gPGz), BoolType, None, None)], Return(StringLit(RkUw))), VarDecl(Id(D0), BoolType, None, StringLit(fWo)), VarDecl(Id(dT0o), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115540))

	def test_21530115541(self):
		input = '''
bool rI <- true
string vK2[0.0] <- H2m
func MVt (string YC, number jh)	begin
		if ("LP")
		string ERYp[81.83,26.16]
		elif ("w")
		if (cC) return f6n
		elif (BY_2) return 32.04
		elif (88.75)
		if ("Li")
		for gu until 15.47 by "ASsvg"
			dynamic HU1h
		elif (false) begin
			begin
				continue
			end
		end
		elif ("p") if ("kBmJ") return 70.42
		elif ("ChhQF") begin
			if (WK4) number PNM[6.17,4.06,63.27]
			elif ("h") string J4[2.04,58.42,23.76] <- 47.93
			elif ("w") if (bN4i) for xz until GfWp by false
				return
			elif (false)
			return ol
			elif ("yg")
			begin
			end
			elif ("eFa") return
			else X0()
			elif ("yPfk")
			OViC <- "ic"
			elif (oVH) break
			else return
			return "oYQdb"
			return
		end
		elif (60.8)
		ZSra["Ps", 93.47] <- false
		elif (true) continue
		elif (46.01)
		break
		elif ("I") if (OQsU) begin
			eYOf(53.24)
			return
			string NCjf[8.77,65.64,52.68] <- "l"
		end
		elif ("oXy") begin
		end
		else if (false) Of9 <- true
		elif ("fNbl")
		dynamic CJ
		elif (6.24) return
		elif (false) return
		elif (21.24)
		begin
			for HN until "DPHx" by 28.95
				return "grocO"
		end
		elif (false)
		begin
		end
		else continue
		elif (6.85) begin
			return
		end
		continue
		if ("arbPT")
		string B55 <- "X"
		else o6(false, "Dg")
	end
'''
		expect = '''Program([VarDecl(Id(rI), BoolType, None, BooleanLit(True)), VarDecl(Id(vK2), ArrayType([0.0], StringType), None, Id(H2m)), FuncDecl(Id(MVt), [VarDecl(Id(YC), StringType, None, None), VarDecl(Id(jh), NumberType, None, None)], Block([If((StringLit(LP), VarDecl(Id(ERYp), ArrayType([81.83, 26.16], StringType), None, None)), [(StringLit(w), If((Id(cC), Return(Id(f6n))), [(Id(BY_2), Return(NumLit(32.04))), (NumLit(88.75), If((StringLit(Li), For(Id(gu), NumLit(15.47), StringLit(ASsvg), VarDecl(Id(HU1h), None, dynamic, None))), [(BooleanLit(False), Block([Block([Continue])])), (StringLit(p), If((StringLit(kBmJ), Return(NumLit(70.42))), [(StringLit(ChhQF), Block([If((Id(WK4), VarDecl(Id(PNM), ArrayType([6.17, 4.06, 63.27], NumberType), None, None)), [(StringLit(h), VarDecl(Id(J4), ArrayType([2.04, 58.42, 23.76], StringType), None, NumLit(47.93))), (StringLit(w), If((Id(bN4i), For(Id(xz), Id(GfWp), BooleanLit(False), Return())), [(BooleanLit(False), Return(Id(ol))), (StringLit(yg), Block([])), (StringLit(eFa), Return())], CallStmt(Id(X0), []))), (StringLit(yPfk), AssignStmt(Id(OViC), StringLit(ic))), (Id(oVH), Break)], Return()), Return(StringLit(oYQdb)), Return()])), (NumLit(60.8), AssignStmt(ArrayCell(Id(ZSra), [StringLit(Ps), NumLit(93.47)]), BooleanLit(False))), (BooleanLit(True), Continue), (NumLit(46.01), Break), (StringLit(I), If((Id(OQsU), Block([CallStmt(Id(eYOf), [NumLit(53.24)]), Return(), VarDecl(Id(NCjf), ArrayType([8.77, 65.64, 52.68], StringType), None, StringLit(l))])), [(StringLit(oXy), Block([]))], If((BooleanLit(False), AssignStmt(Id(Of9), BooleanLit(True))), [(StringLit(fNbl), VarDecl(Id(CJ), None, dynamic, None)), (NumLit(6.24), Return()), (BooleanLit(False), Return()), (NumLit(21.24), Block([For(Id(HN), StringLit(DPHx), NumLit(28.95), Return(StringLit(grocO)))])), (BooleanLit(False), Block([]))], Continue))), (NumLit(6.85), Block([Return()]))], None))], None))], None))], None), Continue, If((StringLit(arbPT), VarDecl(Id(B55), StringType, None, StringLit(X))), [], CallStmt(Id(o6), [BooleanLit(False), StringLit(Dg)]))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115541))

	def test_21530115542(self):
		input = '''
func wV ()	return jRt

'''
		expect = '''Program([FuncDecl(Id(wV), [], Return(Id(jRt)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115542))

	def test_21530115543(self):
		input = '''
bool pK[28.8,60.29]
func GOP ()	begin
		continue
	end
var vP <- w3R
func TjCn (string j_, string D3fw[80.86], bool Y4j1)
	return

'''
		expect = '''Program([VarDecl(Id(pK), ArrayType([28.8, 60.29], BoolType), None, None), FuncDecl(Id(GOP), [], Block([Continue])), VarDecl(Id(vP), None, var, Id(w3R)), FuncDecl(Id(TjCn), [VarDecl(Id(j_), StringType, None, None), VarDecl(Id(D3fw), ArrayType([80.86], StringType), None, None), VarDecl(Id(Y4j1), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115543))

	def test_21530115544(self):
		input = '''
func Im (string BU[23.97,52.84,25.99])	begin
		break
	end
func Js ()
	return

func kSet (number l6_J[32.26,22.36,50.69], number N0D, bool k4[94.52,70.84])
	return true
'''
		expect = '''Program([FuncDecl(Id(Im), [VarDecl(Id(BU), ArrayType([23.97, 52.84, 25.99], StringType), None, None)], Block([Break])), FuncDecl(Id(Js), [], Return()), FuncDecl(Id(kSet), [VarDecl(Id(l6_J), ArrayType([32.26, 22.36, 50.69], NumberType), None, None), VarDecl(Id(N0D), NumberType, None, None), VarDecl(Id(k4), ArrayType([94.52, 70.84], BoolType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115544))

	def test_21530115545(self):
		input = '''
bool Jt[66.52,67.11,30.81] <- false
func Qir ()
	begin
		bool UTKf[10.71] <- false
		var K25v <- SCw
	end
'''
		expect = '''Program([VarDecl(Id(Jt), ArrayType([66.52, 67.11, 30.81], BoolType), None, BooleanLit(False)), FuncDecl(Id(Qir), [], Block([VarDecl(Id(UTKf), ArrayType([10.71], BoolType), None, BooleanLit(False)), VarDecl(Id(K25v), None, var, Id(SCw))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115545))

	def test_21530115546(self):
		input = '''
bool DCk4[25.07] <- false
func Cd0 (string acMD[30.12,13.8], string SH[38.66,54.62,49.84])	return JBO
func CjA (number Z61X, bool ij)
	return false
number EA5S[25.41,29.18,26.84] <- 74.51
string YY[28.24,22.7]
'''
		expect = '''Program([VarDecl(Id(DCk4), ArrayType([25.07], BoolType), None, BooleanLit(False)), FuncDecl(Id(Cd0), [VarDecl(Id(acMD), ArrayType([30.12, 13.8], StringType), None, None), VarDecl(Id(SH), ArrayType([38.66, 54.62, 49.84], StringType), None, None)], Return(Id(JBO))), FuncDecl(Id(CjA), [VarDecl(Id(Z61X), NumberType, None, None), VarDecl(Id(ij), BoolType, None, None)], Return(BooleanLit(False))), VarDecl(Id(EA5S), ArrayType([25.41, 29.18, 26.84], NumberType), None, NumLit(74.51)), VarDecl(Id(YY), ArrayType([28.24, 22.7], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115546))

	def test_21530115547(self):
		input = '''
func BAa (string ubMl[25.58])	begin
	end
'''
		expect = '''Program([FuncDecl(Id(BAa), [VarDecl(Id(ubMl), ArrayType([25.58], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115547))

	def test_21530115548(self):
		input = '''
func wv (bool bjH[64.08], bool h32[80.22], number AOvt[30.69])
	return
string gCs[52.18]
func VrJc ()
	return Gql
string B7wz
'''
		expect = '''Program([FuncDecl(Id(wv), [VarDecl(Id(bjH), ArrayType([64.08], BoolType), None, None), VarDecl(Id(h32), ArrayType([80.22], BoolType), None, None), VarDecl(Id(AOvt), ArrayType([30.69], NumberType), None, None)], Return()), VarDecl(Id(gCs), ArrayType([52.18], StringType), None, None), FuncDecl(Id(VrJc), [], Return(Id(Gql))), VarDecl(Id(B7wz), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115548))

	def test_21530115549(self):
		input = '''
number Xn
number IV[97.76]
func ZRk8 (string oY[63.04])	begin
		wR[false, "A"] <- true
		for GelM until nWOR by DF
			break
	end

'''
		expect = '''Program([VarDecl(Id(Xn), NumberType, None, None), VarDecl(Id(IV), ArrayType([97.76], NumberType), None, None), FuncDecl(Id(ZRk8), [VarDecl(Id(oY), ArrayType([63.04], StringType), None, None)], Block([AssignStmt(ArrayCell(Id(wR), [BooleanLit(False), StringLit(A)]), BooleanLit(True)), For(Id(GelM), Id(nWOR), Id(DF), Break)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115549))

	def test_21530115550(self):
		input = '''
number RLu[97.04,57.75,26.66]
func ZeI5 ()	begin
		number fPfs[31.46,92.48,70.44]
		if (lr)
		for gb3 until GU by 28.82
			break
		elif ("GoY") for YIcF until syJc by mx
			if (76.75) tXwF <- N3u
			elif (false)
			for htj until "W" by false
				return
			elif (true) continue
			elif (O7g) var C2 <- "BX"
			elif (9.38)
			return
			elif (false) bool U5I[68.23,82.08] <- true
	end
'''
		expect = '''Program([VarDecl(Id(RLu), ArrayType([97.04, 57.75, 26.66], NumberType), None, None), FuncDecl(Id(ZeI5), [], Block([VarDecl(Id(fPfs), ArrayType([31.46, 92.48, 70.44], NumberType), None, None), If((Id(lr), For(Id(gb3), Id(GU), NumLit(28.82), Break)), [(StringLit(GoY), For(Id(YIcF), Id(syJc), Id(mx), If((NumLit(76.75), AssignStmt(Id(tXwF), Id(N3u))), [(BooleanLit(False), For(Id(htj), StringLit(W), BooleanLit(False), Return())), (BooleanLit(True), Continue), (Id(O7g), VarDecl(Id(C2), None, var, StringLit(BX))), (NumLit(9.38), Return()), (BooleanLit(False), VarDecl(Id(U5I), ArrayType([68.23, 82.08], BoolType), None, BooleanLit(True)))], None)))], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115550))

	def test_21530115551(self):
		input = '''
var WpTw <- true
'''
		expect = '''Program([VarDecl(Id(WpTw), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115551))

	def test_21530115552(self):
		input = '''
string r4b[52.2,14.58]
bool Ye[13.92,7.44,53.94]
func GWL (string sDx[60.73], string Za, string fT)
	begin
		break
	end
string EE1B <- "p"
func zg2 ()
	return

'''
		expect = '''Program([VarDecl(Id(r4b), ArrayType([52.2, 14.58], StringType), None, None), VarDecl(Id(Ye), ArrayType([13.92, 7.44, 53.94], BoolType), None, None), FuncDecl(Id(GWL), [VarDecl(Id(sDx), ArrayType([60.73], StringType), None, None), VarDecl(Id(Za), StringType, None, None), VarDecl(Id(fT), StringType, None, None)], Block([Break])), VarDecl(Id(EE1B), StringType, None, StringLit(p)), FuncDecl(Id(zg2), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115552))

	def test_21530115553(self):
		input = '''
bool FA5[26.9]
func gi (string ukz[7.16,30.24,63.14])	return Mwo

'''
		expect = '''Program([VarDecl(Id(FA5), ArrayType([26.9], BoolType), None, None), FuncDecl(Id(gi), [VarDecl(Id(ukz), ArrayType([7.16, 30.24, 63.14], StringType), None, None)], Return(Id(Mwo)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115553))

	def test_21530115554(self):
		input = '''
func pt (bool Kh[54.86,45.62,82.63], string Rj, number zC)	begin
		return
		continue
		return
	end

func Id (bool X4, number BVi[83.72,85.62,17.94])	return
func s6 (string AVM[59.68,70.29], number A_R_, string qSZ[79.95,20.28,66.3])
	return

func bp (string SSb)	begin
		break
	end
'''
		expect = '''Program([FuncDecl(Id(pt), [VarDecl(Id(Kh), ArrayType([54.86, 45.62, 82.63], BoolType), None, None), VarDecl(Id(Rj), StringType, None, None), VarDecl(Id(zC), NumberType, None, None)], Block([Return(), Continue, Return()])), FuncDecl(Id(Id), [VarDecl(Id(X4), BoolType, None, None), VarDecl(Id(BVi), ArrayType([83.72, 85.62, 17.94], NumberType), None, None)], Return()), FuncDecl(Id(s6), [VarDecl(Id(AVM), ArrayType([59.68, 70.29], StringType), None, None), VarDecl(Id(A_R_), NumberType, None, None), VarDecl(Id(qSZ), ArrayType([79.95, 20.28, 66.3], StringType), None, None)], Return()), FuncDecl(Id(bp), [VarDecl(Id(SSb), StringType, None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115554))

	def test_21530115555(self):
		input = '''
func ZuHW (bool mc[2.21,89.09,95.82])	return "Tab"
func bZ1O (number VP0[53.32,27.53], string NQvt[78.93], string uO[6.54,10.72,50.16])
	begin
		for AT until false by "fegcS"
			for Lgcc until 77.0 by false
				bool mlF <- XYQA
	end
func e75 ()	begin
		if (KI) QC(true)
		elif ("Bc")
		return true
		elif ("mrpjy")
		continue
		return 60.65
	end
'''
		expect = '''Program([FuncDecl(Id(ZuHW), [VarDecl(Id(mc), ArrayType([2.21, 89.09, 95.82], BoolType), None, None)], Return(StringLit(Tab))), FuncDecl(Id(bZ1O), [VarDecl(Id(VP0), ArrayType([53.32, 27.53], NumberType), None, None), VarDecl(Id(NQvt), ArrayType([78.93], StringType), None, None), VarDecl(Id(uO), ArrayType([6.54, 10.72, 50.16], StringType), None, None)], Block([For(Id(AT), BooleanLit(False), StringLit(fegcS), For(Id(Lgcc), NumLit(77.0), BooleanLit(False), VarDecl(Id(mlF), BoolType, None, Id(XYQA))))])), FuncDecl(Id(e75), [], Block([If((Id(KI), CallStmt(Id(QC), [BooleanLit(True)])), [(StringLit(Bc), Return(BooleanLit(True))), (StringLit(mrpjy), Continue)], None), Return(NumLit(60.65))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115555))

	def test_21530115556(self):
		input = '''
func Qz (number jP)
	return

string XkqW
bool IsWQ[9.25] <- 31.31
func Q6C (string Hc[47.45,62.57,16.23])	return
number NIY[85.7,43.26]
'''
		expect = '''Program([FuncDecl(Id(Qz), [VarDecl(Id(jP), NumberType, None, None)], Return()), VarDecl(Id(XkqW), StringType, None, None), VarDecl(Id(IsWQ), ArrayType([9.25], BoolType), None, NumLit(31.31)), FuncDecl(Id(Q6C), [VarDecl(Id(Hc), ArrayType([47.45, 62.57, 16.23], StringType), None, None)], Return()), VarDecl(Id(NIY), ArrayType([85.7, 43.26], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115556))

	def test_21530115557(self):
		input = '''
func NoY ()	return
string gAn[60.49] <- T6fs
func s5c ()	begin
	end

'''
		expect = '''Program([FuncDecl(Id(NoY), [], Return()), VarDecl(Id(gAn), ArrayType([60.49], StringType), None, Id(T6fs)), FuncDecl(Id(s5c), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115557))

	def test_21530115558(self):
		input = '''
dynamic XY_E <- 39.01
dynamic RM
func CoN ()	return

dynamic PN8
'''
		expect = '''Program([VarDecl(Id(XY_E), None, dynamic, NumLit(39.01)), VarDecl(Id(RM), None, dynamic, None), FuncDecl(Id(CoN), [], Return()), VarDecl(Id(PN8), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115558))

	def test_21530115559(self):
		input = '''
number Lb[8.69,85.01]
func yC1g ()
	return

number ia[5.6] <- Wc
string fZx[60.52,59.91]
func UQZ (bool wM, bool uuVQ)	return 2.94

'''
		expect = '''Program([VarDecl(Id(Lb), ArrayType([8.69, 85.01], NumberType), None, None), FuncDecl(Id(yC1g), [], Return()), VarDecl(Id(ia), ArrayType([5.6], NumberType), None, Id(Wc)), VarDecl(Id(fZx), ArrayType([60.52, 59.91], StringType), None, None), FuncDecl(Id(UQZ), [VarDecl(Id(wM), BoolType, None, None), VarDecl(Id(uuVQ), BoolType, None, None)], Return(NumLit(2.94)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115559))

	def test_21530115560(self):
		input = '''
func djXS (bool Hff, number vhzb[98.57,77.19])
	return fh7q

func e9uM (bool fpbW[13.5,19.03,2.86], bool Wei1[41.72,70.96], string bS[9.38,14.62])	return
func Txu ()
	begin
		pxC(ZWt5, false)
		for gE until 15.06 by uxW
			begin
				for SL until 2.16 by azC
					m5Jd(96.09, 29.22)
				break
				MMsD[false, 32.81, 45.9] <- ctN
			end
		break
	end

'''
		expect = '''Program([FuncDecl(Id(djXS), [VarDecl(Id(Hff), BoolType, None, None), VarDecl(Id(vhzb), ArrayType([98.57, 77.19], NumberType), None, None)], Return(Id(fh7q))), FuncDecl(Id(e9uM), [VarDecl(Id(fpbW), ArrayType([13.5, 19.03, 2.86], BoolType), None, None), VarDecl(Id(Wei1), ArrayType([41.72, 70.96], BoolType), None, None), VarDecl(Id(bS), ArrayType([9.38, 14.62], StringType), None, None)], Return()), FuncDecl(Id(Txu), [], Block([CallStmt(Id(pxC), [Id(ZWt5), BooleanLit(False)]), For(Id(gE), NumLit(15.06), Id(uxW), Block([For(Id(SL), NumLit(2.16), Id(azC), CallStmt(Id(m5Jd), [NumLit(96.09), NumLit(29.22)])), Break, AssignStmt(ArrayCell(Id(MMsD), [BooleanLit(False), NumLit(32.81), NumLit(45.9)]), Id(ctN))])), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115560))

	def test_21530115561(self):
		input = '''
bool znhD[20.78,69.46] <- 9.98
func xPz ()	begin
	end

'''
		expect = '''Program([VarDecl(Id(znhD), ArrayType([20.78, 69.46], BoolType), None, NumLit(9.98)), FuncDecl(Id(xPz), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115561))

	def test_21530115562(self):
		input = '''
var Hq <- "A"
'''
		expect = '''Program([VarDecl(Id(Hq), None, var, StringLit(A))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115562))

	def test_21530115563(self):
		input = '''
bool ei[19.03,79.34] <- "CG"
bool euL <- 79.46
bool W5 <- HaD
bool QyTJ[28.7,28.12,86.25] <- "qSS"
func M4 ()
	return
'''
		expect = '''Program([VarDecl(Id(ei), ArrayType([19.03, 79.34], BoolType), None, StringLit(CG)), VarDecl(Id(euL), BoolType, None, NumLit(79.46)), VarDecl(Id(W5), BoolType, None, Id(HaD)), VarDecl(Id(QyTJ), ArrayType([28.7, 28.12, 86.25], BoolType), None, StringLit(qSS)), FuncDecl(Id(M4), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115563))

	def test_21530115564(self):
		input = '''
string cUjY[98.42]
func Es (string DCV, bool nld[93.31], string Yk)	return
number Jl[73.01,93.77] <- "Fd"
func Hxw (string Vk[33.25,72.68,36.53], bool ll[75.1,47.29,42.5])
	begin
		xZ1["OjnHq"] <- ndfU
		bool pQM[63.82] <- false
		if (true) continue
		elif (true)
		break
		elif (qFrx) for bl until true by false
			begin
			end
		elif ("CE") number mf[24.09]
		elif ("PSIq") return
	end

'''
		expect = '''Program([VarDecl(Id(cUjY), ArrayType([98.42], StringType), None, None), FuncDecl(Id(Es), [VarDecl(Id(DCV), StringType, None, None), VarDecl(Id(nld), ArrayType([93.31], BoolType), None, None), VarDecl(Id(Yk), StringType, None, None)], Return()), VarDecl(Id(Jl), ArrayType([73.01, 93.77], NumberType), None, StringLit(Fd)), FuncDecl(Id(Hxw), [VarDecl(Id(Vk), ArrayType([33.25, 72.68, 36.53], StringType), None, None), VarDecl(Id(ll), ArrayType([75.1, 47.29, 42.5], BoolType), None, None)], Block([AssignStmt(ArrayCell(Id(xZ1), [StringLit(OjnHq)]), Id(ndfU)), VarDecl(Id(pQM), ArrayType([63.82], BoolType), None, BooleanLit(False)), If((BooleanLit(True), Continue), [(BooleanLit(True), Break), (Id(qFrx), For(Id(bl), BooleanLit(True), BooleanLit(False), Block([]))), (StringLit(CE), VarDecl(Id(mf), ArrayType([24.09], NumberType), None, None)), (StringLit(PSIq), Return())], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115564))

	def test_21530115565(self):
		input = '''
func Vet (number ZF[24.24,13.75,14.98], string VQ[96.84,69.89,75.17], bool ep)	begin
		s3m[true] <- "XW"
		for BP until false by TT2I
			break
	end

func t1 ()	return

func f0 (bool LKKx[19.0], number mOWK)	begin
		ANQN <- "YhX"
		break
	end
number gQtL <- true
'''
		expect = '''Program([FuncDecl(Id(Vet), [VarDecl(Id(ZF), ArrayType([24.24, 13.75, 14.98], NumberType), None, None), VarDecl(Id(VQ), ArrayType([96.84, 69.89, 75.17], StringType), None, None), VarDecl(Id(ep), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(s3m), [BooleanLit(True)]), StringLit(XW)), For(Id(BP), BooleanLit(False), Id(TT2I), Break)])), FuncDecl(Id(t1), [], Return()), FuncDecl(Id(f0), [VarDecl(Id(LKKx), ArrayType([19.0], BoolType), None, None), VarDecl(Id(mOWK), NumberType, None, None)], Block([AssignStmt(Id(ANQN), StringLit(YhX)), Break])), VarDecl(Id(gQtL), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115565))

	def test_21530115566(self):
		input = '''
func wN ()
	begin
		continue
		return 12.69
	end

number a1 <- "h"
dynamic zU
'''
		expect = '''Program([FuncDecl(Id(wN), [], Block([Continue, Return(NumLit(12.69))])), VarDecl(Id(a1), NumberType, None, StringLit(h)), VarDecl(Id(zU), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115566))

	def test_21530115567(self):
		input = '''
func PNk ()
	begin
	end
number zT_6
string nkc8
bool xI[79.82] <- "XilCF"
number qQ
'''
		expect = '''Program([FuncDecl(Id(PNk), [], Block([])), VarDecl(Id(zT_6), NumberType, None, None), VarDecl(Id(nkc8), StringType, None, None), VarDecl(Id(xI), ArrayType([79.82], BoolType), None, StringLit(XilCF)), VarDecl(Id(qQ), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115567))

	def test_21530115568(self):
		input = '''
func no (string wEC, string gs6[83.58,24.59,35.19])	return
func qmKM (bool YX, string mMmW[63.61], number AnNw)
	return
func cL (bool vUJs, string c6Vv, number KS)	return

'''
		expect = '''Program([FuncDecl(Id(no), [VarDecl(Id(wEC), StringType, None, None), VarDecl(Id(gs6), ArrayType([83.58, 24.59, 35.19], StringType), None, None)], Return()), FuncDecl(Id(qmKM), [VarDecl(Id(YX), BoolType, None, None), VarDecl(Id(mMmW), ArrayType([63.61], StringType), None, None), VarDecl(Id(AnNw), NumberType, None, None)], Return()), FuncDecl(Id(cL), [VarDecl(Id(vUJs), BoolType, None, None), VarDecl(Id(c6Vv), StringType, None, None), VarDecl(Id(KS), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115568))

	def test_21530115569(self):
		input = '''
func eu61 (bool AuD, bool ZFFL[5.32], number Uc)
	return "K"
'''
		expect = '''Program([FuncDecl(Id(eu61), [VarDecl(Id(AuD), BoolType, None, None), VarDecl(Id(ZFFL), ArrayType([5.32], BoolType), None, None), VarDecl(Id(Uc), NumberType, None, None)], Return(StringLit(K)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115569))

	def test_21530115570(self):
		input = '''
string qAJ
number UslW[27.55,60.19]
number TSsu <- "hRlHv"
func VXl (number x5AK, string Kgl[17.51,20.7], number d35)	begin
		continue
		jQ9()
	end
bool y3xB <- yyvs
'''
		expect = '''Program([VarDecl(Id(qAJ), StringType, None, None), VarDecl(Id(UslW), ArrayType([27.55, 60.19], NumberType), None, None), VarDecl(Id(TSsu), NumberType, None, StringLit(hRlHv)), FuncDecl(Id(VXl), [VarDecl(Id(x5AK), NumberType, None, None), VarDecl(Id(Kgl), ArrayType([17.51, 20.7], StringType), None, None), VarDecl(Id(d35), NumberType, None, None)], Block([Continue, CallStmt(Id(jQ9), [])])), VarDecl(Id(y3xB), BoolType, None, Id(yyvs))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115570))

	def test_21530115571(self):
		input = '''
dynamic ija
number wAy[42.13]
func Sf ()
	return

'''
		expect = '''Program([VarDecl(Id(ija), None, dynamic, None), VarDecl(Id(wAy), ArrayType([42.13], NumberType), None, None), FuncDecl(Id(Sf), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115571))

	def test_21530115572(self):
		input = '''
number WJ[85.61,60.87]
func NqL (number rpb[98.61], bool heAz[40.26,74.96])
	return 30.7
dynamic uxT <- false
var yN <- true
func d1EB (string Cy)
	return

'''
		expect = '''Program([VarDecl(Id(WJ), ArrayType([85.61, 60.87], NumberType), None, None), FuncDecl(Id(NqL), [VarDecl(Id(rpb), ArrayType([98.61], NumberType), None, None), VarDecl(Id(heAz), ArrayType([40.26, 74.96], BoolType), None, None)], Return(NumLit(30.7))), VarDecl(Id(uxT), None, dynamic, BooleanLit(False)), VarDecl(Id(yN), None, var, BooleanLit(True)), FuncDecl(Id(d1EB), [VarDecl(Id(Cy), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115572))

	def test_21530115573(self):
		input = '''
func nwdO (number RO[35.92,31.02,32.17], bool Air)	return
func eF8v ()	begin
		bool GDrM[9.83]
		begin
			for yD until "Is" by 61.52
				Ia2("HYU", "Gl", "h")
			break
			xm(vA)
		end
	end

func fLu ()
	begin
		continue
		for udlF until 92.64 by mTio
			if ("n")
			break
			elif (68.99) T32 <- iA
			else return
	end

'''
		expect = '''Program([FuncDecl(Id(nwdO), [VarDecl(Id(RO), ArrayType([35.92, 31.02, 32.17], NumberType), None, None), VarDecl(Id(Air), BoolType, None, None)], Return()), FuncDecl(Id(eF8v), [], Block([VarDecl(Id(GDrM), ArrayType([9.83], BoolType), None, None), Block([For(Id(yD), StringLit(Is), NumLit(61.52), CallStmt(Id(Ia2), [StringLit(HYU), StringLit(Gl), StringLit(h)])), Break, CallStmt(Id(xm), [Id(vA)])])])), FuncDecl(Id(fLu), [], Block([Continue, For(Id(udlF), NumLit(92.64), Id(mTio), If((StringLit(n), Break), [(NumLit(68.99), AssignStmt(Id(T32), Id(iA)))], Return()))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115573))

	def test_21530115574(self):
		input = '''
func yLR ()	return py

func C5 (number Ah0[60.31,95.94,28.0], string nK[64.11], number C7)
	return
func M2 (bool bOVF[16.95,75.77], bool KKJ[24.03,19.24,74.06])
	return 76.35
func pGX ()
	return false
'''
		expect = '''Program([FuncDecl(Id(yLR), [], Return(Id(py))), FuncDecl(Id(C5), [VarDecl(Id(Ah0), ArrayType([60.31, 95.94, 28.0], NumberType), None, None), VarDecl(Id(nK), ArrayType([64.11], StringType), None, None), VarDecl(Id(C7), NumberType, None, None)], Return()), FuncDecl(Id(M2), [VarDecl(Id(bOVF), ArrayType([16.95, 75.77], BoolType), None, None), VarDecl(Id(KKJ), ArrayType([24.03, 19.24, 74.06], BoolType), None, None)], Return(NumLit(76.35))), FuncDecl(Id(pGX), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115574))

	def test_21530115575(self):
		input = '''
func HAKP ()	return 66.65

'''
		expect = '''Program([FuncDecl(Id(HAKP), [], Return(NumLit(66.65)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115575))

	def test_21530115576(self):
		input = '''
func OQEJ ()	return true
func WT (number QzsZ, number d_[55.53], bool Qj[83.36,10.68,40.36])
	return
'''
		expect = '''Program([FuncDecl(Id(OQEJ), [], Return(BooleanLit(True))), FuncDecl(Id(WT), [VarDecl(Id(QzsZ), NumberType, None, None), VarDecl(Id(d_), ArrayType([55.53], NumberType), None, None), VarDecl(Id(Qj), ArrayType([83.36, 10.68, 40.36], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115576))

	def test_21530115577(self):
		input = '''
bool YU
'''
		expect = '''Program([VarDecl(Id(YU), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115577))

	def test_21530115578(self):
		input = '''
func Tix (number qO, bool iagc[66.37,78.49,45.37], string PU[6.46])	return "EP"

func y9TU (string lyO5, bool Zv7c[73.2], string Db0)	return
var Np <- false
number bzvB[63.64,94.23] <- 8.49
func V6r (bool YE[46.64,64.77], string jmqy)
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(Tix), [VarDecl(Id(qO), NumberType, None, None), VarDecl(Id(iagc), ArrayType([66.37, 78.49, 45.37], BoolType), None, None), VarDecl(Id(PU), ArrayType([6.46], StringType), None, None)], Return(StringLit(EP))), FuncDecl(Id(y9TU), [VarDecl(Id(lyO5), StringType, None, None), VarDecl(Id(Zv7c), ArrayType([73.2], BoolType), None, None), VarDecl(Id(Db0), StringType, None, None)], Return()), VarDecl(Id(Np), None, var, BooleanLit(False)), VarDecl(Id(bzvB), ArrayType([63.64, 94.23], NumberType), None, NumLit(8.49)), FuncDecl(Id(V6r), [VarDecl(Id(YE), ArrayType([46.64, 64.77], BoolType), None, None), VarDecl(Id(jmqy), StringType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115578))

	def test_21530115579(self):
		input = '''
func tPE7 (number PVU[79.45,95.9])	return "j"
func PZV (number oeb[77.41], string sl[74.47,84.17,28.25])
	return "OnI"

'''
		expect = '''Program([FuncDecl(Id(tPE7), [VarDecl(Id(PVU), ArrayType([79.45, 95.9], NumberType), None, None)], Return(StringLit(j))), FuncDecl(Id(PZV), [VarDecl(Id(oeb), ArrayType([77.41], NumberType), None, None), VarDecl(Id(sl), ArrayType([74.47, 84.17, 28.25], StringType), None, None)], Return(StringLit(OnI)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115579))

	def test_21530115580(self):
		input = '''
string VSD[92.81] <- true
'''
		expect = '''Program([VarDecl(Id(VSD), ArrayType([92.81], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115580))

	def test_21530115581(self):
		input = '''
bool dMSL <- 71.14
string RqF6[90.98,63.61]
'''
		expect = '''Program([VarDecl(Id(dMSL), BoolType, None, NumLit(71.14)), VarDecl(Id(RqF6), ArrayType([90.98, 63.61], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115581))

	def test_21530115582(self):
		input = '''
func HH (bool CXsG, string VSa)
	return
func Ane6 (bool B_O, number krA, number jHT[35.84])	return gE

func OZuw (number EVhL[48.42,78.03], bool Cg[36.41])
	return
func RmpE (bool Wj, number TR[77.71,53.27,30.68])	begin
	end
var IFEr <- "TWnE"
'''
		expect = '''Program([FuncDecl(Id(HH), [VarDecl(Id(CXsG), BoolType, None, None), VarDecl(Id(VSa), StringType, None, None)], Return()), FuncDecl(Id(Ane6), [VarDecl(Id(B_O), BoolType, None, None), VarDecl(Id(krA), NumberType, None, None), VarDecl(Id(jHT), ArrayType([35.84], NumberType), None, None)], Return(Id(gE))), FuncDecl(Id(OZuw), [VarDecl(Id(EVhL), ArrayType([48.42, 78.03], NumberType), None, None), VarDecl(Id(Cg), ArrayType([36.41], BoolType), None, None)], Return()), FuncDecl(Id(RmpE), [VarDecl(Id(Wj), BoolType, None, None), VarDecl(Id(TR), ArrayType([77.71, 53.27, 30.68], NumberType), None, None)], Block([])), VarDecl(Id(IFEr), None, var, StringLit(TWnE))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115582))

	def test_21530115583(self):
		input = '''
func PI (bool jKnf[46.51,17.7,82.68], number Cz, bool TlhL[87.28])	begin
		continue
		return
		if (true)
		return 62.71
		else var SzI <- Zk
	end

'''
		expect = '''Program([FuncDecl(Id(PI), [VarDecl(Id(jKnf), ArrayType([46.51, 17.7, 82.68], BoolType), None, None), VarDecl(Id(Cz), NumberType, None, None), VarDecl(Id(TlhL), ArrayType([87.28], BoolType), None, None)], Block([Continue, Return(), If((BooleanLit(True), Return(NumLit(62.71))), [], VarDecl(Id(SzI), None, var, Id(Zk)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115583))

	def test_21530115584(self):
		input = '''
var CyuW <- "m"
bool UbU3[99.15,12.52]
func GN (number ySRg[15.73], bool EI, number F6l)
	return

string f1JA
func ql (number VYa, number GhMv)
	return

'''
		expect = '''Program([VarDecl(Id(CyuW), None, var, StringLit(m)), VarDecl(Id(UbU3), ArrayType([99.15, 12.52], BoolType), None, None), FuncDecl(Id(GN), [VarDecl(Id(ySRg), ArrayType([15.73], NumberType), None, None), VarDecl(Id(EI), BoolType, None, None), VarDecl(Id(F6l), NumberType, None, None)], Return()), VarDecl(Id(f1JA), StringType, None, None), FuncDecl(Id(ql), [VarDecl(Id(VYa), NumberType, None, None), VarDecl(Id(GhMv), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115584))

	def test_21530115585(self):
		input = '''
func VIU8 (bool xn[83.49], string NhE[0.8], string YTy)
	return mEX_
'''
		expect = '''Program([FuncDecl(Id(VIU8), [VarDecl(Id(xn), ArrayType([83.49], BoolType), None, None), VarDecl(Id(NhE), ArrayType([0.8], StringType), None, None), VarDecl(Id(YTy), StringType, None, None)], Return(Id(mEX_)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115585))

	def test_21530115586(self):
		input = '''
string Rh[0.67,18.58]
string jNc[48.08,73.56,64.56]
number j9_5[5.73,71.04] <- true
func D9nG (number QWB[71.07,87.32])	return
'''
		expect = '''Program([VarDecl(Id(Rh), ArrayType([0.67, 18.58], StringType), None, None), VarDecl(Id(jNc), ArrayType([48.08, 73.56, 64.56], StringType), None, None), VarDecl(Id(j9_5), ArrayType([5.73, 71.04], NumberType), None, BooleanLit(True)), FuncDecl(Id(D9nG), [VarDecl(Id(QWB), ArrayType([71.07, 87.32], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115586))

	def test_21530115587(self):
		input = '''
func Irt9 ()
	return
'''
		expect = '''Program([FuncDecl(Id(Irt9), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115587))

	def test_21530115588(self):
		input = '''
number BU_p
'''
		expect = '''Program([VarDecl(Id(BU_p), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115588))

	def test_21530115589(self):
		input = '''
func s2EG (number Yd6u[91.06])	begin
		break
		for XKIQ until Dyu by 90.19
			string Bdf[14.2]
	end
'''
		expect = '''Program([FuncDecl(Id(s2EG), [VarDecl(Id(Yd6u), ArrayType([91.06], NumberType), None, None)], Block([Break, For(Id(XKIQ), Id(Dyu), NumLit(90.19), VarDecl(Id(Bdf), ArrayType([14.2], StringType), None, None))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115589))

	def test_21530115590(self):
		input = '''
func Mg (string eztT[90.33,32.32])	return

dynamic SDAN
string vjO[27.8,67.92] <- true
string nLT[98.78]
func V40W (number R7[70.01], bool SI)
	begin
		return
	end
'''
		expect = '''Program([FuncDecl(Id(Mg), [VarDecl(Id(eztT), ArrayType([90.33, 32.32], StringType), None, None)], Return()), VarDecl(Id(SDAN), None, dynamic, None), VarDecl(Id(vjO), ArrayType([27.8, 67.92], StringType), None, BooleanLit(True)), VarDecl(Id(nLT), ArrayType([98.78], StringType), None, None), FuncDecl(Id(V40W), [VarDecl(Id(R7), ArrayType([70.01], NumberType), None, None), VarDecl(Id(SI), BoolType, None, None)], Block([Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115590))

	def test_21530115591(self):
		input = '''
dynamic aNu <- bc
'''
		expect = '''Program([VarDecl(Id(aNu), None, dynamic, Id(bc))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115591))

	def test_21530115592(self):
		input = '''
func Dk (number F9L, bool j0G)	begin
		begin
			begin
				return "dO"
			end
			TUXM[false, false, true] <- "ydso"
			dynamic ZQw <- "CQvTj"
		end
		continue
	end

func eA (bool FmUp[94.4], number pCh[67.98,38.65,44.17], number mkTR[27.88,76.2])
	begin
		return false
		break
		I32F["OwfzX", 91.23, true] <- false
	end

'''
		expect = '''Program([FuncDecl(Id(Dk), [VarDecl(Id(F9L), NumberType, None, None), VarDecl(Id(j0G), BoolType, None, None)], Block([Block([Block([Return(StringLit(dO))]), AssignStmt(ArrayCell(Id(TUXM), [BooleanLit(False), BooleanLit(False), BooleanLit(True)]), StringLit(ydso)), VarDecl(Id(ZQw), None, dynamic, StringLit(CQvTj))]), Continue])), FuncDecl(Id(eA), [VarDecl(Id(FmUp), ArrayType([94.4], BoolType), None, None), VarDecl(Id(pCh), ArrayType([67.98, 38.65, 44.17], NumberType), None, None), VarDecl(Id(mkTR), ArrayType([27.88, 76.2], NumberType), None, None)], Block([Return(BooleanLit(False)), Break, AssignStmt(ArrayCell(Id(I32F), [StringLit(OwfzX), NumLit(91.23), BooleanLit(True)]), BooleanLit(False))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115592))

	def test_21530115593(self):
		input = '''
func sfzf (string jI7)
	return

'''
		expect = '''Program([FuncDecl(Id(sfzf), [VarDecl(Id(jI7), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115593))

	def test_21530115594(self):
		input = '''
bool dCb6
func SW ()
	return kE_z

number g8qn[22.44,75.65,20.49] <- eKd
func yAMM (bool bksL[44.22,65.94,24.91])
	begin
		begin
			kGd5 <- 91.57
			begin
				X879 <- "YEZe"
				bool yH[28.82,86.49]
				o_gV(false, true, 27.94)
			end
		end
		continue
	end
'''
		expect = '''Program([VarDecl(Id(dCb6), BoolType, None, None), FuncDecl(Id(SW), [], Return(Id(kE_z))), VarDecl(Id(g8qn), ArrayType([22.44, 75.65, 20.49], NumberType), None, Id(eKd)), FuncDecl(Id(yAMM), [VarDecl(Id(bksL), ArrayType([44.22, 65.94, 24.91], BoolType), None, None)], Block([Block([AssignStmt(Id(kGd5), NumLit(91.57)), Block([AssignStmt(Id(X879), StringLit(YEZe)), VarDecl(Id(yH), ArrayType([28.82, 86.49], BoolType), None, None), CallStmt(Id(o_gV), [BooleanLit(False), BooleanLit(True), NumLit(27.94)])])]), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115594))

	def test_21530115595(self):
		input = '''
string s0b
bool M7
bool g9[58.45,67.46]
number NT[57.19,21.41,18.51] <- 41.73
'''
		expect = '''Program([VarDecl(Id(s0b), StringType, None, None), VarDecl(Id(M7), BoolType, None, None), VarDecl(Id(g9), ArrayType([58.45, 67.46], BoolType), None, None), VarDecl(Id(NT), ArrayType([57.19, 21.41, 18.51], NumberType), None, NumLit(41.73))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115595))

	def test_21530115596(self):
		input = '''
func Bq (bool I6, string Hd)	return

dynamic chE <- MrO
func TL ()	return 1.76
'''
		expect = '''Program([FuncDecl(Id(Bq), [VarDecl(Id(I6), BoolType, None, None), VarDecl(Id(Hd), StringType, None, None)], Return()), VarDecl(Id(chE), None, dynamic, Id(MrO)), FuncDecl(Id(TL), [], Return(NumLit(1.76)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115596))

	def test_21530115597(self):
		input = '''
bool xg[49.89,49.55]
func Zt7J (string Nl[49.15,55.1,70.7])
	return 7.91
func cytM (bool jhS4[29.21,66.47,80.69], string SZ_)
	return nUuO

number mgc[48.63,7.4,53.93]
bool Kf[24.24]
'''
		expect = '''Program([VarDecl(Id(xg), ArrayType([49.89, 49.55], BoolType), None, None), FuncDecl(Id(Zt7J), [VarDecl(Id(Nl), ArrayType([49.15, 55.1, 70.7], StringType), None, None)], Return(NumLit(7.91))), FuncDecl(Id(cytM), [VarDecl(Id(jhS4), ArrayType([29.21, 66.47, 80.69], BoolType), None, None), VarDecl(Id(SZ_), StringType, None, None)], Return(Id(nUuO))), VarDecl(Id(mgc), ArrayType([48.63, 7.4, 53.93], NumberType), None, None), VarDecl(Id(Kf), ArrayType([24.24], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115597))

	def test_21530115598(self):
		input = '''
func o9y (bool S4m)	return true

number zaZ[96.31,90.46,49.78]
number vY[56.23,15.92,98.39] <- "BQ"
var mn <- false
func FFN (string eq44)	begin
		return true
	end
'''
		expect = '''Program([FuncDecl(Id(o9y), [VarDecl(Id(S4m), BoolType, None, None)], Return(BooleanLit(True))), VarDecl(Id(zaZ), ArrayType([96.31, 90.46, 49.78], NumberType), None, None), VarDecl(Id(vY), ArrayType([56.23, 15.92, 98.39], NumberType), None, StringLit(BQ)), VarDecl(Id(mn), None, var, BooleanLit(False)), FuncDecl(Id(FFN), [VarDecl(Id(eq44), StringType, None, None)], Block([Return(BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115598))

	def test_21530115599(self):
		input = '''
func oDSl ()	begin
		break
	end
func qRc (string Wn, number L6gL[99.27], string poRX)
	return false
func SL (number jI, bool nM, number tqJ[19.87,13.95,38.02])
	return
number YR9[53.64,62.93]
'''
		expect = '''Program([FuncDecl(Id(oDSl), [], Block([Break])), FuncDecl(Id(qRc), [VarDecl(Id(Wn), StringType, None, None), VarDecl(Id(L6gL), ArrayType([99.27], NumberType), None, None), VarDecl(Id(poRX), StringType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(SL), [VarDecl(Id(jI), NumberType, None, None), VarDecl(Id(nM), BoolType, None, None), VarDecl(Id(tqJ), ArrayType([19.87, 13.95, 38.02], NumberType), None, None)], Return()), VarDecl(Id(YR9), ArrayType([53.64, 62.93], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115599))

	def test_21530115600(self):
		input = '''
string GaPb[15.35] <- 16.56
'''
		expect = '''Program([VarDecl(Id(GaPb), ArrayType([15.35], StringType), None, NumLit(16.56))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115600))

	def test_21530115601(self):
		input = '''
bool AE[55.2,86.57,7.48]
string iacl
func rQ (string nbsv[20.25,52.08], number Zl)
	return "aC"

func m7_H (string we[22.27])
	return
func j69 ()
	return

'''
		expect = '''Program([VarDecl(Id(AE), ArrayType([55.2, 86.57, 7.48], BoolType), None, None), VarDecl(Id(iacl), StringType, None, None), FuncDecl(Id(rQ), [VarDecl(Id(nbsv), ArrayType([20.25, 52.08], StringType), None, None), VarDecl(Id(Zl), NumberType, None, None)], Return(StringLit(aC))), FuncDecl(Id(m7_H), [VarDecl(Id(we), ArrayType([22.27], StringType), None, None)], Return()), FuncDecl(Id(j69), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115601))

	def test_21530115602(self):
		input = '''
func Rty (string mvD[70.66], number xL4u[42.24,95.82], string hB)
	return 42.45

bool ks[38.77,78.12,36.4]
bool jCE[9.2]
func Nh ()	return "ggTb"
'''
		expect = '''Program([FuncDecl(Id(Rty), [VarDecl(Id(mvD), ArrayType([70.66], StringType), None, None), VarDecl(Id(xL4u), ArrayType([42.24, 95.82], NumberType), None, None), VarDecl(Id(hB), StringType, None, None)], Return(NumLit(42.45))), VarDecl(Id(ks), ArrayType([38.77, 78.12, 36.4], BoolType), None, None), VarDecl(Id(jCE), ArrayType([9.2], BoolType), None, None), FuncDecl(Id(Nh), [], Return(StringLit(ggTb)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115602))

	def test_21530115603(self):
		input = '''
func kP (string dbD)	begin
		for l2k until eUm by "SMviS"
			aJ()
	end
number JVw
'''
		expect = '''Program([FuncDecl(Id(kP), [VarDecl(Id(dbD), StringType, None, None)], Block([For(Id(l2k), Id(eUm), StringLit(SMviS), CallStmt(Id(aJ), []))])), VarDecl(Id(JVw), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115603))

	def test_21530115604(self):
		input = '''
bool OOD[81.36] <- MEn
func XV (number Ulsw)
	begin
		string roU <- 95.44
		continue
		continue
	end
func S_L ()	return
string ScmJ <- "JmDZa"
func TylQ (number qzxs)
	return false
'''
		expect = '''Program([VarDecl(Id(OOD), ArrayType([81.36], BoolType), None, Id(MEn)), FuncDecl(Id(XV), [VarDecl(Id(Ulsw), NumberType, None, None)], Block([VarDecl(Id(roU), StringType, None, NumLit(95.44)), Continue, Continue])), FuncDecl(Id(S_L), [], Return()), VarDecl(Id(ScmJ), StringType, None, StringLit(JmDZa)), FuncDecl(Id(TylQ), [VarDecl(Id(qzxs), NumberType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115604))

	def test_21530115605(self):
		input = '''
bool XxoZ[87.47,90.82] <- "SMWx"
func dBRQ (bool pf[70.55,14.08], bool UCZ[46.42])
	begin
		for cOe until 1.71 by f7WG
			continue
		number y8Sv <- true
	end
string uFz[34.38,91.22]
'''
		expect = '''Program([VarDecl(Id(XxoZ), ArrayType([87.47, 90.82], BoolType), None, StringLit(SMWx)), FuncDecl(Id(dBRQ), [VarDecl(Id(pf), ArrayType([70.55, 14.08], BoolType), None, None), VarDecl(Id(UCZ), ArrayType([46.42], BoolType), None, None)], Block([For(Id(cOe), NumLit(1.71), Id(f7WG), Continue), VarDecl(Id(y8Sv), NumberType, None, BooleanLit(True))])), VarDecl(Id(uFz), ArrayType([34.38, 91.22], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115605))

	def test_21530115606(self):
		input = '''
func RxVK (bool S8cQ[6.5,40.67,13.7], number p5W[20.71,27.62,42.8], number wf6P)	return

func tIlx (string xzLc[36.99,88.5,12.26], bool V84k[63.45])
	begin
	end
func ca (bool hWJd)	return
'''
		expect = '''Program([FuncDecl(Id(RxVK), [VarDecl(Id(S8cQ), ArrayType([6.5, 40.67, 13.7], BoolType), None, None), VarDecl(Id(p5W), ArrayType([20.71, 27.62, 42.8], NumberType), None, None), VarDecl(Id(wf6P), NumberType, None, None)], Return()), FuncDecl(Id(tIlx), [VarDecl(Id(xzLc), ArrayType([36.99, 88.5, 12.26], StringType), None, None), VarDecl(Id(V84k), ArrayType([63.45], BoolType), None, None)], Block([])), FuncDecl(Id(ca), [VarDecl(Id(hWJd), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115606))

	def test_21530115607(self):
		input = '''
func OB0e (string jJ8[9.23])	begin
		begin
			begin
				if (iw) continue
			end
			break
			begin
				J4no(3.32)
			end
		end
	end

dynamic kYFE
'''
		expect = '''Program([FuncDecl(Id(OB0e), [VarDecl(Id(jJ8), ArrayType([9.23], StringType), None, None)], Block([Block([Block([If((Id(iw), Continue), [], None)]), Break, Block([CallStmt(Id(J4no), [NumLit(3.32)])])])])), VarDecl(Id(kYFE), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115607))

	def test_21530115608(self):
		input = '''
func wum7 (string ixpQ[54.13], number zC, number PuWd)
	begin
		wQf9 <- E8Jo
		begin
			begin
				laaB <- "IlWCX"
			end
			return true
			if (46.49)
			begin
				if ("ES")
				mb(false, "zb", 32.25)
				elif (40.77)
				if (18.17) return false
				elif ("fy")
				var eYns <- "bG"
				elif (63.87)
				N8[zby] <- Qz
				elif ("c") if ("dCCQv")
				if ("kRqzx")
				okrr[So, true] <- oF
				elif (21.31)
				begin
					if (yS2)
					if (false) for jHDO until qJ by 56.17
						for EY4m until "IRBZ" by FjEI
							return g_z
					elif (false)
					KW <- 99.29
					elif ("to")
					break
					elif (28.51) RH[false] <- Vnh
					else continue
					else for ac3Y until true by 72.08
						Px("YI", false, 58.32)
					continue
				end
				elif (IQjZ) p5L <- 57.1
				elif ("mY") for Yv until true by ks
					return false
				elif (ijq)
				string t0 <- 75.51
				elif (true) return
				else if (yQ98) for q8w until pTRN by "EPxA"
					begin
						break
						for p7 until "qv" by sla
							for fqd until 11.33 by false
								ibLh(false, 3.76, true)
					end
				elif (21.94) return
				elif (true)
				ZKB <- Z2
				elif (mzi)
				bool z9da[28.12]
				elif (zQ) if (su)
				continue
				elif (false) begin
					if ("OF")
					break
					elif ("ZdCX") return
					elif ("agG")
					bool jHZ[24.52,32.31]
					elif (14.45)
					continue
					elif (j3L)
					break
					elif ("ME")
					for VGP until true by "I"
						v7 <- 70.73
					string PiI0[80.4] <- ezS
				end
				elif (95.53)
				return true
				else break
				break
			end
			elif ("ro") continue
			elif (ai0J)
			string Wu
			elif (70.35) break
			else vc["AZzeM", true, true] <- "kBHQL"
		end
		continue
	end
number kApr
dynamic Bt
'''
		expect = '''Program([FuncDecl(Id(wum7), [VarDecl(Id(ixpQ), ArrayType([54.13], StringType), None, None), VarDecl(Id(zC), NumberType, None, None), VarDecl(Id(PuWd), NumberType, None, None)], Block([AssignStmt(Id(wQf9), Id(E8Jo)), Block([Block([AssignStmt(Id(laaB), StringLit(IlWCX))]), Return(BooleanLit(True)), If((NumLit(46.49), Block([If((StringLit(ES), CallStmt(Id(mb), [BooleanLit(False), StringLit(zb), NumLit(32.25)])), [(NumLit(40.77), If((NumLit(18.17), Return(BooleanLit(False))), [(StringLit(fy), VarDecl(Id(eYns), None, var, StringLit(bG))), (NumLit(63.87), AssignStmt(ArrayCell(Id(N8), [Id(zby)]), Id(Qz))), (StringLit(c), If((StringLit(dCCQv), If((StringLit(kRqzx), AssignStmt(ArrayCell(Id(okrr), [Id(So), BooleanLit(True)]), Id(oF))), [(NumLit(21.31), Block([If((Id(yS2), If((BooleanLit(False), For(Id(jHDO), Id(qJ), NumLit(56.17), For(Id(EY4m), StringLit(IRBZ), Id(FjEI), Return(Id(g_z))))), [(BooleanLit(False), AssignStmt(Id(KW), NumLit(99.29))), (StringLit(to), Break), (NumLit(28.51), AssignStmt(ArrayCell(Id(RH), [BooleanLit(False)]), Id(Vnh)))], Continue)), [], For(Id(ac3Y), BooleanLit(True), NumLit(72.08), CallStmt(Id(Px), [StringLit(YI), BooleanLit(False), NumLit(58.32)]))), Continue])), (Id(IQjZ), AssignStmt(Id(p5L), NumLit(57.1))), (StringLit(mY), For(Id(Yv), BooleanLit(True), Id(ks), Return(BooleanLit(False)))), (Id(ijq), VarDecl(Id(t0), StringType, None, NumLit(75.51))), (BooleanLit(True), Return())], If((Id(yQ98), For(Id(q8w), Id(pTRN), StringLit(EPxA), Block([Break, For(Id(p7), StringLit(qv), Id(sla), For(Id(fqd), NumLit(11.33), BooleanLit(False), CallStmt(Id(ibLh), [BooleanLit(False), NumLit(3.76), BooleanLit(True)])))]))), [(NumLit(21.94), Return()), (BooleanLit(True), AssignStmt(Id(ZKB), Id(Z2))), (Id(mzi), VarDecl(Id(z9da), ArrayType([28.12], BoolType), None, None)), (Id(zQ), If((Id(su), Continue), [(BooleanLit(False), Block([If((StringLit(OF), Break), [(StringLit(ZdCX), Return()), (StringLit(agG), VarDecl(Id(jHZ), ArrayType([24.52, 32.31], BoolType), None, None)), (NumLit(14.45), Continue), (Id(j3L), Break), (StringLit(ME), For(Id(VGP), BooleanLit(True), StringLit(I), AssignStmt(Id(v7), NumLit(70.73))))], None), VarDecl(Id(PiI0), ArrayType([80.4], StringType), None, Id(ezS))])), (NumLit(95.53), Return(BooleanLit(True)))], Break))], None))), [], None))], None))], None), Break])), [(StringLit(ro), Continue), (Id(ai0J), VarDecl(Id(Wu), StringType, None, None)), (NumLit(70.35), Break)], AssignStmt(ArrayCell(Id(vc), [StringLit(AZzeM), BooleanLit(True), BooleanLit(True)]), StringLit(kBHQL)))]), Continue])), VarDecl(Id(kApr), NumberType, None, None), VarDecl(Id(Bt), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115608))

	def test_21530115609(self):
		input = '''
func B6 ()	return m4LM
string Qnpb <- L61
func o6 (number Ll, bool UHni)
	begin
		continue
	end

'''
		expect = '''Program([FuncDecl(Id(B6), [], Return(Id(m4LM))), VarDecl(Id(Qnpb), StringType, None, Id(L61)), FuncDecl(Id(o6), [VarDecl(Id(Ll), NumberType, None, None), VarDecl(Id(UHni), BoolType, None, None)], Block([Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115609))

	def test_21530115610(self):
		input = '''
func j_m (number Pp[76.23,40.48,67.83], number c_s[63.35], number s2YU[91.21,35.97])	return

func ONzW ()
	return Ja
func HJ3 (string QoeB[75.79,88.07,2.74], number bmam)	return 50.26
dynamic sCnT
'''
		expect = '''Program([FuncDecl(Id(j_m), [VarDecl(Id(Pp), ArrayType([76.23, 40.48, 67.83], NumberType), None, None), VarDecl(Id(c_s), ArrayType([63.35], NumberType), None, None), VarDecl(Id(s2YU), ArrayType([91.21, 35.97], NumberType), None, None)], Return()), FuncDecl(Id(ONzW), [], Return(Id(Ja))), FuncDecl(Id(HJ3), [VarDecl(Id(QoeB), ArrayType([75.79, 88.07, 2.74], StringType), None, None), VarDecl(Id(bmam), NumberType, None, None)], Return(NumLit(50.26))), VarDecl(Id(sCnT), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115610))

	def test_21530115611(self):
		input = '''
func xF1g (number TDZ6)
	return
number ciVZ[70.32] <- 99.14
string UUM <- uSj
func t3 (string uqqL[1.92,29.31], bool i1[46.11,75.31], number y0f)	begin
		if ("tQFz")
		for IP until 6.85 by 71.16
			continue
		elif (true) continue
		elif (true) bool Zk[6.18,12.05] <- 10.52
		continue
	end

string eENZ[60.68,43.1]
'''
		expect = '''Program([FuncDecl(Id(xF1g), [VarDecl(Id(TDZ6), NumberType, None, None)], Return()), VarDecl(Id(ciVZ), ArrayType([70.32], NumberType), None, NumLit(99.14)), VarDecl(Id(UUM), StringType, None, Id(uSj)), FuncDecl(Id(t3), [VarDecl(Id(uqqL), ArrayType([1.92, 29.31], StringType), None, None), VarDecl(Id(i1), ArrayType([46.11, 75.31], BoolType), None, None), VarDecl(Id(y0f), NumberType, None, None)], Block([If((StringLit(tQFz), For(Id(IP), NumLit(6.85), NumLit(71.16), Continue)), [(BooleanLit(True), Continue), (BooleanLit(True), VarDecl(Id(Zk), ArrayType([6.18, 12.05], BoolType), None, NumLit(10.52)))], None), Continue])), VarDecl(Id(eENZ), ArrayType([60.68, 43.1], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115611))

	def test_21530115612(self):
		input = '''
func rkp (number t7[42.54])	return 26.84

func BBl (string qiu, number SaL)	begin
		break
		HYDu["zR", "RFj"] <- "ubzAU"
		return
	end
'''
		expect = '''Program([FuncDecl(Id(rkp), [VarDecl(Id(t7), ArrayType([42.54], NumberType), None, None)], Return(NumLit(26.84))), FuncDecl(Id(BBl), [VarDecl(Id(qiu), StringType, None, None), VarDecl(Id(SaL), NumberType, None, None)], Block([Break, AssignStmt(ArrayCell(Id(HYDu), [StringLit(zR), StringLit(RFj)]), StringLit(ubzAU)), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115612))

	def test_21530115613(self):
		input = '''
bool jRt[46.97]
number Ok[59.38]
number kZ
number vxjq[82.28,70.22,23.83] <- true
func VTNm ()	return "fLAo"

'''
		expect = '''Program([VarDecl(Id(jRt), ArrayType([46.97], BoolType), None, None), VarDecl(Id(Ok), ArrayType([59.38], NumberType), None, None), VarDecl(Id(kZ), NumberType, None, None), VarDecl(Id(vxjq), ArrayType([82.28, 70.22, 23.83], NumberType), None, BooleanLit(True)), FuncDecl(Id(VTNm), [], Return(StringLit(fLAo)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115613))

	def test_21530115614(self):
		input = '''
func NLRG (string Go5W[72.3,93.11], bool EKQC[62.48], string P_Q)	return

'''
		expect = '''Program([FuncDecl(Id(NLRG), [VarDecl(Id(Go5W), ArrayType([72.3, 93.11], StringType), None, None), VarDecl(Id(EKQC), ArrayType([62.48], BoolType), None, None), VarDecl(Id(P_Q), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115614))

	def test_21530115615(self):
		input = '''
dynamic xQ <- 3.42
number KDK3
var l53 <- 40.3
'''
		expect = '''Program([VarDecl(Id(xQ), None, dynamic, NumLit(3.42)), VarDecl(Id(KDK3), NumberType, None, None), VarDecl(Id(l53), None, var, NumLit(40.3))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115615))

	def test_21530115616(self):
		input = '''
func ea0r (number FA[48.03,11.57], number ezdc[35.23,61.36], number yigC[63.36,74.41])	return
func uu9 ()	return

func L6 (number XT[89.15,53.91])
	return
func GXy8 ()	begin
		pj()
		bool FBi5[84.06]
		CCn[Gpn, "GLBIL"] <- 40.72
	end

'''
		expect = '''Program([FuncDecl(Id(ea0r), [VarDecl(Id(FA), ArrayType([48.03, 11.57], NumberType), None, None), VarDecl(Id(ezdc), ArrayType([35.23, 61.36], NumberType), None, None), VarDecl(Id(yigC), ArrayType([63.36, 74.41], NumberType), None, None)], Return()), FuncDecl(Id(uu9), [], Return()), FuncDecl(Id(L6), [VarDecl(Id(XT), ArrayType([89.15, 53.91], NumberType), None, None)], Return()), FuncDecl(Id(GXy8), [], Block([CallStmt(Id(pj), []), VarDecl(Id(FBi5), ArrayType([84.06], BoolType), None, None), AssignStmt(ArrayCell(Id(CCn), [Id(Gpn), StringLit(GLBIL)]), NumLit(40.72))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115616))

	def test_21530115617(self):
		input = '''
func Bp (number gG[74.85,43.95])
	return p9

func j4B ()	return 79.95

func ntzx (string Blku[8.79,35.68])	return
func nsf (bool xz[2.45], string tDnw[44.33], string Ja7[82.47])
	begin
		W9("I")
	end
bool Hqt <- 49.7
'''
		expect = '''Program([FuncDecl(Id(Bp), [VarDecl(Id(gG), ArrayType([74.85, 43.95], NumberType), None, None)], Return(Id(p9))), FuncDecl(Id(j4B), [], Return(NumLit(79.95))), FuncDecl(Id(ntzx), [VarDecl(Id(Blku), ArrayType([8.79, 35.68], StringType), None, None)], Return()), FuncDecl(Id(nsf), [VarDecl(Id(xz), ArrayType([2.45], BoolType), None, None), VarDecl(Id(tDnw), ArrayType([44.33], StringType), None, None), VarDecl(Id(Ja7), ArrayType([82.47], StringType), None, None)], Block([CallStmt(Id(W9), [StringLit(I)])])), VarDecl(Id(Hqt), BoolType, None, NumLit(49.7))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115617))

	def test_21530115618(self):
		input = '''
func Qe (bool Ia6[6.03,27.16,30.08], string a34)
	begin
		for Ycv until true by "G"
			number MS <- rE
		dynamic dDW <- "qKhzq"
	end

func i9 (string KNVy, bool mT, bool mt)
	return Icb

func yZhA (bool uPlF[91.57,62.98,55.13], bool EUQy)	return
func rkw (number ePVR[98.68,32.73,79.1])
	begin
		break
		number pi <- true
	end

'''
		expect = '''Program([FuncDecl(Id(Qe), [VarDecl(Id(Ia6), ArrayType([6.03, 27.16, 30.08], BoolType), None, None), VarDecl(Id(a34), StringType, None, None)], Block([For(Id(Ycv), BooleanLit(True), StringLit(G), VarDecl(Id(MS), NumberType, None, Id(rE))), VarDecl(Id(dDW), None, dynamic, StringLit(qKhzq))])), FuncDecl(Id(i9), [VarDecl(Id(KNVy), StringType, None, None), VarDecl(Id(mT), BoolType, None, None), VarDecl(Id(mt), BoolType, None, None)], Return(Id(Icb))), FuncDecl(Id(yZhA), [VarDecl(Id(uPlF), ArrayType([91.57, 62.98, 55.13], BoolType), None, None), VarDecl(Id(EUQy), BoolType, None, None)], Return()), FuncDecl(Id(rkw), [VarDecl(Id(ePVR), ArrayType([98.68, 32.73, 79.1], NumberType), None, None)], Block([Break, VarDecl(Id(pi), NumberType, None, BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115618))

	def test_21530115619(self):
		input = '''
string tz <- "QvbG"
'''
		expect = '''Program([VarDecl(Id(tz), StringType, None, StringLit(QvbG))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115619))

	def test_21530115620(self):
		input = '''
string Ata <- 34.6
var RsRn <- true
func zS (bool oorI[33.07,46.62,98.62], bool JgGd, string dcm[44.62,69.09,61.81])
	return
'''
		expect = '''Program([VarDecl(Id(Ata), StringType, None, NumLit(34.6)), VarDecl(Id(RsRn), None, var, BooleanLit(True)), FuncDecl(Id(zS), [VarDecl(Id(oorI), ArrayType([33.07, 46.62, 98.62], BoolType), None, None), VarDecl(Id(JgGd), BoolType, None, None), VarDecl(Id(dcm), ArrayType([44.62, 69.09, 61.81], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115620))

	def test_21530115621(self):
		input = '''
func cJJ (string AYGe, string Trt[81.86])
	return
string KUK[22.49]
func dDy7 (bool HYqW[96.83,85.78,54.85])	return
bool CEU <- kDg
func c9J (number it, bool vd3[21.89,85.35], bool mhJR[20.21,46.32])
	return "iap"
'''
		expect = '''Program([FuncDecl(Id(cJJ), [VarDecl(Id(AYGe), StringType, None, None), VarDecl(Id(Trt), ArrayType([81.86], StringType), None, None)], Return()), VarDecl(Id(KUK), ArrayType([22.49], StringType), None, None), FuncDecl(Id(dDy7), [VarDecl(Id(HYqW), ArrayType([96.83, 85.78, 54.85], BoolType), None, None)], Return()), VarDecl(Id(CEU), BoolType, None, Id(kDg)), FuncDecl(Id(c9J), [VarDecl(Id(it), NumberType, None, None), VarDecl(Id(vd3), ArrayType([21.89, 85.35], BoolType), None, None), VarDecl(Id(mhJR), ArrayType([20.21, 46.32], BoolType), None, None)], Return(StringLit(iap)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115621))

	def test_21530115622(self):
		input = '''
func QP (number Wfb[98.31,73.31,82.18], string T9lQ)
	return
func yjmp ()	begin
		break
		qmJo <- 22.33
	end

number VZ[85.28] <- 52.8
string Ty[15.99,44.38,52.55]
'''
		expect = '''Program([FuncDecl(Id(QP), [VarDecl(Id(Wfb), ArrayType([98.31, 73.31, 82.18], NumberType), None, None), VarDecl(Id(T9lQ), StringType, None, None)], Return()), FuncDecl(Id(yjmp), [], Block([Break, AssignStmt(Id(qmJo), NumLit(22.33))])), VarDecl(Id(VZ), ArrayType([85.28], NumberType), None, NumLit(52.8)), VarDecl(Id(Ty), ArrayType([15.99, 44.38, 52.55], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115622))

	def test_21530115623(self):
		input = '''
func Hz (bool UQ, number dvX, bool l6_m[26.96,70.08,71.3])
	begin
		for P_s until mNm by 22.57
			continue
		begin
			if (RqJ) break
			elif (96.66) PY(60.16, true, 1.9)
			elif (false) number c7[94.25,51.19] <- "F"
			elif (I5uC)
			Ue2P <- "z"
			else Feq[Zv, cFTs] <- true
		end
	end
bool IwZF[67.01,48.76]
func S0s (string a2hz[57.01])
	begin
		return
	end
dynamic kJs <- 4.03
'''
		expect = '''Program([FuncDecl(Id(Hz), [VarDecl(Id(UQ), BoolType, None, None), VarDecl(Id(dvX), NumberType, None, None), VarDecl(Id(l6_m), ArrayType([26.96, 70.08, 71.3], BoolType), None, None)], Block([For(Id(P_s), Id(mNm), NumLit(22.57), Continue), Block([If((Id(RqJ), Break), [(NumLit(96.66), CallStmt(Id(PY), [NumLit(60.16), BooleanLit(True), NumLit(1.9)])), (BooleanLit(False), VarDecl(Id(c7), ArrayType([94.25, 51.19], NumberType), None, StringLit(F))), (Id(I5uC), AssignStmt(Id(Ue2P), StringLit(z)))], AssignStmt(ArrayCell(Id(Feq), [Id(Zv), Id(cFTs)]), BooleanLit(True)))])])), VarDecl(Id(IwZF), ArrayType([67.01, 48.76], BoolType), None, None), FuncDecl(Id(S0s), [VarDecl(Id(a2hz), ArrayType([57.01], StringType), None, None)], Block([Return()])), VarDecl(Id(kJs), None, dynamic, NumLit(4.03))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115623))

	def test_21530115624(self):
		input = '''
bool s_[51.24]
func z7 (string rE2Y[39.68,3.93], number YOp, bool nplJ[17.34])
	return 40.77
'''
		expect = '''Program([VarDecl(Id(s_), ArrayType([51.24], BoolType), None, None), FuncDecl(Id(z7), [VarDecl(Id(rE2Y), ArrayType([39.68, 3.93], StringType), None, None), VarDecl(Id(YOp), NumberType, None, None), VarDecl(Id(nplJ), ArrayType([17.34], BoolType), None, None)], Return(NumLit(40.77)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115624))

	def test_21530115625(self):
		input = '''
func pj (string EA[61.48,92.52], bool PqaH, string xgzW)
	return true

string eOTS <- zeWT
func im ()
	begin
		number bK[29.6]
	end
func WEqm ()
	return
'''
		expect = '''Program([FuncDecl(Id(pj), [VarDecl(Id(EA), ArrayType([61.48, 92.52], StringType), None, None), VarDecl(Id(PqaH), BoolType, None, None), VarDecl(Id(xgzW), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(eOTS), StringType, None, Id(zeWT)), FuncDecl(Id(im), [], Block([VarDecl(Id(bK), ArrayType([29.6], NumberType), None, None)])), FuncDecl(Id(WEqm), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115625))

	def test_21530115626(self):
		input = '''
string owl[7.79,9.6] <- SI
func Wg8g (string nbDG[34.69], string eNrT, number G_)
	return Jx

dynamic U3qV
'''
		expect = '''Program([VarDecl(Id(owl), ArrayType([7.79, 9.6], StringType), None, Id(SI)), FuncDecl(Id(Wg8g), [VarDecl(Id(nbDG), ArrayType([34.69], StringType), None, None), VarDecl(Id(eNrT), StringType, None, None), VarDecl(Id(G_), NumberType, None, None)], Return(Id(Jx))), VarDecl(Id(U3qV), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115626))

	def test_21530115627(self):
		input = '''
number ZVB[52.92,48.95,67.89]
'''
		expect = '''Program([VarDecl(Id(ZVB), ArrayType([52.92, 48.95, 67.89], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115627))

	def test_21530115628(self):
		input = '''
func ByA (bool Ri65[16.71], string OgJ7)	begin
		enLV(false, 18.6)
		Gi[68.0] <- GemG
	end
func u7Yu (string uHLD, bool e0, number tyn)	begin
	end
number V6[50.78] <- 52.64
func WS1z (number ywJK[52.33,17.37,13.65], bool QFT[65.27,97.54], number YI[69.06])
	begin
	end
func wD8g (string Imll[58.16])
	begin
	end
'''
		expect = '''Program([FuncDecl(Id(ByA), [VarDecl(Id(Ri65), ArrayType([16.71], BoolType), None, None), VarDecl(Id(OgJ7), StringType, None, None)], Block([CallStmt(Id(enLV), [BooleanLit(False), NumLit(18.6)]), AssignStmt(ArrayCell(Id(Gi), [NumLit(68.0)]), Id(GemG))])), FuncDecl(Id(u7Yu), [VarDecl(Id(uHLD), StringType, None, None), VarDecl(Id(e0), BoolType, None, None), VarDecl(Id(tyn), NumberType, None, None)], Block([])), VarDecl(Id(V6), ArrayType([50.78], NumberType), None, NumLit(52.64)), FuncDecl(Id(WS1z), [VarDecl(Id(ywJK), ArrayType([52.33, 17.37, 13.65], NumberType), None, None), VarDecl(Id(QFT), ArrayType([65.27, 97.54], BoolType), None, None), VarDecl(Id(YI), ArrayType([69.06], NumberType), None, None)], Block([])), FuncDecl(Id(wD8g), [VarDecl(Id(Imll), ArrayType([58.16], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115628))

	def test_21530115629(self):
		input = '''
dynamic TX5 <- 26.3
func R9 (string Jt[91.18])
	return
func XYA ()
	return "ynxvS"

dynamic YyO9
func j_Zl (string cI, number lDfZ[56.61,11.88], number O60[29.46])	return

'''
		expect = '''Program([VarDecl(Id(TX5), None, dynamic, NumLit(26.3)), FuncDecl(Id(R9), [VarDecl(Id(Jt), ArrayType([91.18], StringType), None, None)], Return()), FuncDecl(Id(XYA), [], Return(StringLit(ynxvS))), VarDecl(Id(YyO9), None, dynamic, None), FuncDecl(Id(j_Zl), [VarDecl(Id(cI), StringType, None, None), VarDecl(Id(lDfZ), ArrayType([56.61, 11.88], NumberType), None, None), VarDecl(Id(O60), ArrayType([29.46], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115629))

	def test_21530115630(self):
		input = '''
func q4Ei (number QlTD, number nvu, number o2E)
	begin
		GX <- true
		SDD7(12.32, QBR)
	end
func K9e (bool AS, string bQPl[94.68])	begin
		dnvm(55.02)
		for mb until "WLV" by 25.36
			return
	end

'''
		expect = '''Program([FuncDecl(Id(q4Ei), [VarDecl(Id(QlTD), NumberType, None, None), VarDecl(Id(nvu), NumberType, None, None), VarDecl(Id(o2E), NumberType, None, None)], Block([AssignStmt(Id(GX), BooleanLit(True)), CallStmt(Id(SDD7), [NumLit(12.32), Id(QBR)])])), FuncDecl(Id(K9e), [VarDecl(Id(AS), BoolType, None, None), VarDecl(Id(bQPl), ArrayType([94.68], StringType), None, None)], Block([CallStmt(Id(dnvm), [NumLit(55.02)]), For(Id(mb), StringLit(WLV), NumLit(25.36), Return())]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115630))

	def test_21530115631(self):
		input = '''
bool JR <- "lftXQ"
func KZ (number L8E1, bool CrYs, bool jz)	begin
		for btcx until "cMXHI" by true
			mP <- LCtt
		xaE(50.92, 98.17, false)
	end
number fQ[38.12,41.82] <- false
bool IMU <- 9.9
string wI
'''
		expect = '''Program([VarDecl(Id(JR), BoolType, None, StringLit(lftXQ)), FuncDecl(Id(KZ), [VarDecl(Id(L8E1), NumberType, None, None), VarDecl(Id(CrYs), BoolType, None, None), VarDecl(Id(jz), BoolType, None, None)], Block([For(Id(btcx), StringLit(cMXHI), BooleanLit(True), AssignStmt(Id(mP), Id(LCtt))), CallStmt(Id(xaE), [NumLit(50.92), NumLit(98.17), BooleanLit(False)])])), VarDecl(Id(fQ), ArrayType([38.12, 41.82], NumberType), None, BooleanLit(False)), VarDecl(Id(IMU), BoolType, None, NumLit(9.9)), VarDecl(Id(wI), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115631))

	def test_21530115632(self):
		input = '''
func qU (number jV[75.69], bool v8[39.34], number F51S)
	begin
		tcp6[wMaK] <- true
		return
		dynamic To12
	end
string iuj <- Vw
func h2N ()
	begin
		continue
		if (false)
		continue
	end
func O4qv ()
	return

func QXp (string TG_T, bool Sp[96.53,52.41,0.44], number Ap9K)	begin
		begin
		end
		for Wh_F until "gHrdG" by I1Q
			if (Wyx)
			continue
			elif ("l")
			begin
				var x3n <- ycs
				dynamic uv6
				begin
					break
					begin
						if (go) for kIIb until aPv by 8.76
							begin
								return
							end
						elif ("OirB")
						begin
							break
							begin
								cQ()
								UM46[true, 8.91] <- "Kns"
							end
						end
						elif ("GG")
						bool ZN <- "V"
						else return Bx
						if (Vb)
						if ("G") break
						elif (IpF) cDo[71.72, true, 42.62] <- "On"
						elif (true) if (18.83) for ZO until "WsaKR" by TlW1
							if (99.35) bool ilL <- 69.03
							elif (DGI) for OjC until "zg" by rnw
								continue
							elif (false) if ("daGk") return true
							elif (72.73)
							break
							elif (ePVo) begin
								XOCU(true)
								begin
									continue
									qPp[87.95, xC6P, "Q"] <- cvco
									continue
								end
							end
							elif ("Dfi")
							for pb until true by DtQU
								break
							elif (FFn)
							return "Mj"
							elif (89.42) return Z5a
							elif ("kzpRE")
							Zdjp <- "BFg"
						else for fqX until UZ6k by "mgn"
							for FH until "T" by axqC
								if ("KZw") begin
								end
								elif (Sz)
								begin
								end
								elif ("XSiZ")
								bool hF0
								elif ("UmKEn")
								number G5bH
								elif (true)
								string Ank[1.29] <- "lxGT"
								else vzsf(false)
						elif (42.38)
						break
						elif (54.81) for OJW until "tR" by upd
							wU8 <- "heDMi"
						elif (zFAb)
						string UA
					end
				end
			end
	end
'''
		expect = '''Program([FuncDecl(Id(qU), [VarDecl(Id(jV), ArrayType([75.69], NumberType), None, None), VarDecl(Id(v8), ArrayType([39.34], BoolType), None, None), VarDecl(Id(F51S), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(tcp6), [Id(wMaK)]), BooleanLit(True)), Return(), VarDecl(Id(To12), None, dynamic, None)])), VarDecl(Id(iuj), StringType, None, Id(Vw)), FuncDecl(Id(h2N), [], Block([Continue, If((BooleanLit(False), Continue), [], None)])), FuncDecl(Id(O4qv), [], Return()), FuncDecl(Id(QXp), [VarDecl(Id(TG_T), StringType, None, None), VarDecl(Id(Sp), ArrayType([96.53, 52.41, 0.44], BoolType), None, None), VarDecl(Id(Ap9K), NumberType, None, None)], Block([Block([]), For(Id(Wh_F), StringLit(gHrdG), Id(I1Q), If((Id(Wyx), Continue), [(StringLit(l), Block([VarDecl(Id(x3n), None, var, Id(ycs)), VarDecl(Id(uv6), None, dynamic, None), Block([Break, Block([If((Id(go), For(Id(kIIb), Id(aPv), NumLit(8.76), Block([Return()]))), [(StringLit(OirB), Block([Break, Block([CallStmt(Id(cQ), []), AssignStmt(ArrayCell(Id(UM46), [BooleanLit(True), NumLit(8.91)]), StringLit(Kns))])])), (StringLit(GG), VarDecl(Id(ZN), BoolType, None, StringLit(V)))], Return(Id(Bx))), If((Id(Vb), If((StringLit(G), Break), [(Id(IpF), AssignStmt(ArrayCell(Id(cDo), [NumLit(71.72), BooleanLit(True), NumLit(42.62)]), StringLit(On))), (BooleanLit(True), If((NumLit(18.83), For(Id(ZO), StringLit(WsaKR), Id(TlW1), If((NumLit(99.35), VarDecl(Id(ilL), BoolType, None, NumLit(69.03))), [(Id(DGI), For(Id(OjC), StringLit(zg), Id(rnw), Continue)), (BooleanLit(False), If((StringLit(daGk), Return(BooleanLit(True))), [(NumLit(72.73), Break), (Id(ePVo), Block([CallStmt(Id(XOCU), [BooleanLit(True)]), Block([Continue, AssignStmt(ArrayCell(Id(qPp), [NumLit(87.95), Id(xC6P), StringLit(Q)]), Id(cvco)), Continue])])), (StringLit(Dfi), For(Id(pb), BooleanLit(True), Id(DtQU), Break)), (Id(FFn), Return(StringLit(Mj))), (NumLit(89.42), Return(Id(Z5a))), (StringLit(kzpRE), AssignStmt(Id(Zdjp), StringLit(BFg)))], For(Id(fqX), Id(UZ6k), StringLit(mgn), For(Id(FH), StringLit(T), Id(axqC), If((StringLit(KZw), Block([])), [(Id(Sz), Block([])), (StringLit(XSiZ), VarDecl(Id(hF0), BoolType, None, None)), (StringLit(UmKEn), VarDecl(Id(G5bH), NumberType, None, None)), (BooleanLit(True), VarDecl(Id(Ank), ArrayType([1.29], StringType), None, StringLit(lxGT)))], CallStmt(Id(vzsf), [BooleanLit(False)])))))), (NumLit(42.38), Break), (NumLit(54.81), For(Id(OJW), StringLit(tR), Id(upd), AssignStmt(Id(wU8), StringLit(heDMi)))), (Id(zFAb), VarDecl(Id(UA), StringType, None, None))], None))), [], None))], None)), [], None)])])]))], None))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115632))

	def test_21530115633(self):
		input = '''
func mXr (bool f9W[50.2], number KJ[93.65,80.87,5.93])	return true
func uNIZ (string D4RY[39.31,58.64], bool dyu[88.58,71.34])
	return

'''
		expect = '''Program([FuncDecl(Id(mXr), [VarDecl(Id(f9W), ArrayType([50.2], BoolType), None, None), VarDecl(Id(KJ), ArrayType([93.65, 80.87, 5.93], NumberType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(uNIZ), [VarDecl(Id(D4RY), ArrayType([39.31, 58.64], StringType), None, None), VarDecl(Id(dyu), ArrayType([88.58, 71.34], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115633))

	def test_21530115634(self):
		input = '''
func q09 ()
	return

bool fsVS[72.47,29.04]
dynamic Sp <- zm
'''
		expect = '''Program([FuncDecl(Id(q09), [], Return()), VarDecl(Id(fsVS), ArrayType([72.47, 29.04], BoolType), None, None), VarDecl(Id(Sp), None, dynamic, Id(zm))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115634))

	def test_21530115635(self):
		input = '''
bool FYD <- 30.04
number ZmZF <- false
number ON[64.18,99.26] <- "x"
'''
		expect = '''Program([VarDecl(Id(FYD), BoolType, None, NumLit(30.04)), VarDecl(Id(ZmZF), NumberType, None, BooleanLit(False)), VarDecl(Id(ON), ArrayType([64.18, 99.26], NumberType), None, StringLit(x))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115635))

	def test_21530115636(self):
		input = '''
number dN
func hY (string risJ[20.49,56.12,1.51], bool Jna[18.0], string To[10.26])	return "lBBO"

'''
		expect = '''Program([VarDecl(Id(dN), NumberType, None, None), FuncDecl(Id(hY), [VarDecl(Id(risJ), ArrayType([20.49, 56.12, 1.51], StringType), None, None), VarDecl(Id(Jna), ArrayType([18.0], BoolType), None, None), VarDecl(Id(To), ArrayType([10.26], StringType), None, None)], Return(StringLit(lBBO)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115636))

	def test_21530115637(self):
		input = '''
func ub ()
	return

string Jy[21.73] <- NO
'''
		expect = '''Program([FuncDecl(Id(ub), [], Return()), VarDecl(Id(Jy), ArrayType([21.73], StringType), None, Id(NO))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115637))

	def test_21530115638(self):
		input = '''
var pm23 <- "teK"
dynamic z7
'''
		expect = '''Program([VarDecl(Id(pm23), None, var, StringLit(teK)), VarDecl(Id(z7), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115638))

	def test_21530115639(self):
		input = '''
string KL[94.98]
'''
		expect = '''Program([VarDecl(Id(KL), ArrayType([94.98], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115639))

	def test_21530115640(self):
		input = '''
number SDY <- ZH7o
string fQN
func ZQGo ()	begin
		begin
			for Nxx until 6.0 by false
				number esSM[41.73]
			continue
		end
		wg5 <- yQ
	end
'''
		expect = '''Program([VarDecl(Id(SDY), NumberType, None, Id(ZH7o)), VarDecl(Id(fQN), StringType, None, None), FuncDecl(Id(ZQGo), [], Block([Block([For(Id(Nxx), NumLit(6.0), BooleanLit(False), VarDecl(Id(esSM), ArrayType([41.73], NumberType), None, None)), Continue]), AssignStmt(Id(wg5), Id(yQ))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115640))

	def test_21530115641(self):
		input = '''
func Pd (string eO_[66.78])	begin
		Z9b[fW, P58J] <- XLU
		if (true)
		break
		elif (false) return
		continue
	end

number Ug <- "qO"
func PrO6 (string yDL, number Si, bool FHw2)	return IT
number pu
'''
		expect = '''Program([FuncDecl(Id(Pd), [VarDecl(Id(eO_), ArrayType([66.78], StringType), None, None)], Block([AssignStmt(ArrayCell(Id(Z9b), [Id(fW), Id(P58J)]), Id(XLU)), If((BooleanLit(True), Break), [(BooleanLit(False), Return())], None), Continue])), VarDecl(Id(Ug), NumberType, None, StringLit(qO)), FuncDecl(Id(PrO6), [VarDecl(Id(yDL), StringType, None, None), VarDecl(Id(Si), NumberType, None, None), VarDecl(Id(FHw2), BoolType, None, None)], Return(Id(IT))), VarDecl(Id(pu), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115641))

	def test_21530115642(self):
		input = '''
var DI_ <- Dr7J
'''
		expect = '''Program([VarDecl(Id(DI_), None, var, Id(Dr7J))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115642))

	def test_21530115643(self):
		input = '''
bool TG
func SWrK (string xb, bool yF9G)	return

func k_0W (string aYE)	return
'''
		expect = '''Program([VarDecl(Id(TG), BoolType, None, None), FuncDecl(Id(SWrK), [VarDecl(Id(xb), StringType, None, None), VarDecl(Id(yF9G), BoolType, None, None)], Return()), FuncDecl(Id(k_0W), [VarDecl(Id(aYE), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115643))

	def test_21530115644(self):
		input = '''
func hki (bool lp, string hK)	return 24.83

func w9Xg (number L3, string vh6Z, number rms)	return

bool UhF[22.22,25.08,20.2] <- false
func aRrR ()	return
'''
		expect = '''Program([FuncDecl(Id(hki), [VarDecl(Id(lp), BoolType, None, None), VarDecl(Id(hK), StringType, None, None)], Return(NumLit(24.83))), FuncDecl(Id(w9Xg), [VarDecl(Id(L3), NumberType, None, None), VarDecl(Id(vh6Z), StringType, None, None), VarDecl(Id(rms), NumberType, None, None)], Return()), VarDecl(Id(UhF), ArrayType([22.22, 25.08, 20.2], BoolType), None, BooleanLit(False)), FuncDecl(Id(aRrR), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115644))

	def test_21530115645(self):
		input = '''
bool P2w[72.24] <- Gju
func MFu (number SNRS, number VkSK)
	return
'''
		expect = '''Program([VarDecl(Id(P2w), ArrayType([72.24], BoolType), None, Id(Gju)), FuncDecl(Id(MFu), [VarDecl(Id(SNRS), NumberType, None, None), VarDecl(Id(VkSK), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115645))

	def test_21530115646(self):
		input = '''
func bdBU (string rP, bool gZ, bool QG)	return
bool kmb[0.97,2.11,94.6]
number U5
func mA7R ()	return
bool qi <- true
'''
		expect = '''Program([FuncDecl(Id(bdBU), [VarDecl(Id(rP), StringType, None, None), VarDecl(Id(gZ), BoolType, None, None), VarDecl(Id(QG), BoolType, None, None)], Return()), VarDecl(Id(kmb), ArrayType([0.97, 2.11, 94.6], BoolType), None, None), VarDecl(Id(U5), NumberType, None, None), FuncDecl(Id(mA7R), [], Return()), VarDecl(Id(qi), BoolType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115646))

	def test_21530115647(self):
		input = '''
func upad (string xrJ8, string zwCr)
	return

bool UmGA[51.16,45.61,63.53] <- LHYx
func DhaO (number qzes, number i0hG)	return j8
'''
		expect = '''Program([FuncDecl(Id(upad), [VarDecl(Id(xrJ8), StringType, None, None), VarDecl(Id(zwCr), StringType, None, None)], Return()), VarDecl(Id(UmGA), ArrayType([51.16, 45.61, 63.53], BoolType), None, Id(LHYx)), FuncDecl(Id(DhaO), [VarDecl(Id(qzes), NumberType, None, None), VarDecl(Id(i0hG), NumberType, None, None)], Return(Id(j8)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115647))

	def test_21530115648(self):
		input = '''
dynamic g6xu <- "BPNad"
dynamic Js <- true
string oMU[72.76,26.04]
bool PI[74.74,32.38]
'''
		expect = '''Program([VarDecl(Id(g6xu), None, dynamic, StringLit(BPNad)), VarDecl(Id(Js), None, dynamic, BooleanLit(True)), VarDecl(Id(oMU), ArrayType([72.76, 26.04], StringType), None, None), VarDecl(Id(PI), ArrayType([74.74, 32.38], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115648))

	def test_21530115649(self):
		input = '''
func Qu ()	return GJAn

func dC (string zpW, number vn, string ncZb)
	return

'''
		expect = '''Program([FuncDecl(Id(Qu), [], Return(Id(GJAn))), FuncDecl(Id(dC), [VarDecl(Id(zpW), StringType, None, None), VarDecl(Id(vn), NumberType, None, None), VarDecl(Id(ncZb), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115649))

	def test_21530115650(self):
		input = '''
bool nUi[41.73,59.9] <- 29.36
dynamic slMA <- 24.04
func sJ ()
	return qS
func T0 ()
	begin
	end

bool Sbm <- 70.28
'''
		expect = '''Program([VarDecl(Id(nUi), ArrayType([41.73, 59.9], BoolType), None, NumLit(29.36)), VarDecl(Id(slMA), None, dynamic, NumLit(24.04)), FuncDecl(Id(sJ), [], Return(Id(qS))), FuncDecl(Id(T0), [], Block([])), VarDecl(Id(Sbm), BoolType, None, NumLit(70.28))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115650))

	def test_21530115651(self):
		input = '''
bool Xj[16.26]
func jEDk (bool hs[95.87,35.44,61.25])
	return

'''
		expect = '''Program([VarDecl(Id(Xj), ArrayType([16.26], BoolType), None, None), FuncDecl(Id(jEDk), [VarDecl(Id(hs), ArrayType([95.87, 35.44, 61.25], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115651))

	def test_21530115652(self):
		input = '''
func qG (string zpg[26.89,98.1,58.52], bool W2[89.63,9.14,51.06])
	return cFI
'''
		expect = '''Program([FuncDecl(Id(qG), [VarDecl(Id(zpg), ArrayType([26.89, 98.1, 58.52], StringType), None, None), VarDecl(Id(W2), ArrayType([89.63, 9.14, 51.06], BoolType), None, None)], Return(Id(cFI)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115652))

	def test_21530115653(self):
		input = '''
func V0 (string zT, number Yj)	return

bool dLib <- 41.17
var GD <- 24.36
'''
		expect = '''Program([FuncDecl(Id(V0), [VarDecl(Id(zT), StringType, None, None), VarDecl(Id(Yj), NumberType, None, None)], Return()), VarDecl(Id(dLib), BoolType, None, NumLit(41.17)), VarDecl(Id(GD), None, var, NumLit(24.36))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115653))

	def test_21530115654(self):
		input = '''
bool bKv0 <- t9
func CC (number myX, string bi, string Itx[77.88,43.83,52.89])	return
func Cu3 ()	return

number sqL[84.5]
number GL[49.58,68.76] <- "g"
'''
		expect = '''Program([VarDecl(Id(bKv0), BoolType, None, Id(t9)), FuncDecl(Id(CC), [VarDecl(Id(myX), NumberType, None, None), VarDecl(Id(bi), StringType, None, None), VarDecl(Id(Itx), ArrayType([77.88, 43.83, 52.89], StringType), None, None)], Return()), FuncDecl(Id(Cu3), [], Return()), VarDecl(Id(sqL), ArrayType([84.5], NumberType), None, None), VarDecl(Id(GL), ArrayType([49.58, 68.76], NumberType), None, StringLit(g))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115654))

	def test_21530115655(self):
		input = '''
func qieV (number TWJH, string Ll)
	begin
		for PCw until VLj by "BL"
			continue
	end

number vVQz
func Bk7 (bool Hed[61.76,88.95,77.48])	begin
	end
bool bFW <- true
'''
		expect = '''Program([FuncDecl(Id(qieV), [VarDecl(Id(TWJH), NumberType, None, None), VarDecl(Id(Ll), StringType, None, None)], Block([For(Id(PCw), Id(VLj), StringLit(BL), Continue)])), VarDecl(Id(vVQz), NumberType, None, None), FuncDecl(Id(Bk7), [VarDecl(Id(Hed), ArrayType([61.76, 88.95, 77.48], BoolType), None, None)], Block([])), VarDecl(Id(bFW), BoolType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115655))

	def test_21530115656(self):
		input = '''
string a9d[21.5,91.26,90.91]
number pbn[53.84,69.04,75.17] <- false
func ae6 (string pitl[24.76,94.64,72.07], bool a2_o, bool ohs[58.33,68.71])	return

string Z2Hc[54.38,86.44] <- false
string PD[36.39,89.11]
'''
		expect = '''Program([VarDecl(Id(a9d), ArrayType([21.5, 91.26, 90.91], StringType), None, None), VarDecl(Id(pbn), ArrayType([53.84, 69.04, 75.17], NumberType), None, BooleanLit(False)), FuncDecl(Id(ae6), [VarDecl(Id(pitl), ArrayType([24.76, 94.64, 72.07], StringType), None, None), VarDecl(Id(a2_o), BoolType, None, None), VarDecl(Id(ohs), ArrayType([58.33, 68.71], BoolType), None, None)], Return()), VarDecl(Id(Z2Hc), ArrayType([54.38, 86.44], StringType), None, BooleanLit(False)), VarDecl(Id(PD), ArrayType([36.39, 89.11], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115656))

	def test_21530115657(self):
		input = '''
number Yb[1.23,87.2,7.85] <- p9
func aOr (string SlPQ[27.98,68.7,66.51], string CH[84.1,16.69])
	return "pM"
'''
		expect = '''Program([VarDecl(Id(Yb), ArrayType([1.23, 87.2, 7.85], NumberType), None, Id(p9)), FuncDecl(Id(aOr), [VarDecl(Id(SlPQ), ArrayType([27.98, 68.7, 66.51], StringType), None, None), VarDecl(Id(CH), ArrayType([84.1, 16.69], StringType), None, None)], Return(StringLit(pM)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115657))

	def test_21530115658(self):
		input = '''
func EL ()
	return

'''
		expect = '''Program([FuncDecl(Id(EL), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115658))

	def test_21530115659(self):
		input = '''
string regC[70.61,40.82] <- true
bool zfw[23.45]
var W_ <- true
number GF[76.97] <- 15.93
bool aD7[97.77,50.53,12.0]
'''
		expect = '''Program([VarDecl(Id(regC), ArrayType([70.61, 40.82], StringType), None, BooleanLit(True)), VarDecl(Id(zfw), ArrayType([23.45], BoolType), None, None), VarDecl(Id(W_), None, var, BooleanLit(True)), VarDecl(Id(GF), ArrayType([76.97], NumberType), None, NumLit(15.93)), VarDecl(Id(aD7), ArrayType([97.77, 50.53, 12.0], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115659))

	def test_21530115660(self):
		input = '''
bool xe[41.23] <- 38.66
bool VwLr <- true
func c8y ()
	return

func d_h ()	return

func eJ (bool UP, string Q1L[92.86,59.66,35.08])
	begin
	end

'''
		expect = '''Program([VarDecl(Id(xe), ArrayType([41.23], BoolType), None, NumLit(38.66)), VarDecl(Id(VwLr), BoolType, None, BooleanLit(True)), FuncDecl(Id(c8y), [], Return()), FuncDecl(Id(d_h), [], Return()), FuncDecl(Id(eJ), [VarDecl(Id(UP), BoolType, None, None), VarDecl(Id(Q1L), ArrayType([92.86, 59.66, 35.08], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115660))

	def test_21530115661(self):
		input = '''
bool bI[87.37]
dynamic epj <- false
func WL (number Ov[70.66], string aiE)
	return
func huI (bool A_U, string d_1E, string oDuc[75.09])
	begin
		for KfV until HF by true
			lZh()
	end

func hw (number gyo6[66.6,37.44], string Ti[40.67], bool KPc1)	return

'''
		expect = '''Program([VarDecl(Id(bI), ArrayType([87.37], BoolType), None, None), VarDecl(Id(epj), None, dynamic, BooleanLit(False)), FuncDecl(Id(WL), [VarDecl(Id(Ov), ArrayType([70.66], NumberType), None, None), VarDecl(Id(aiE), StringType, None, None)], Return()), FuncDecl(Id(huI), [VarDecl(Id(A_U), BoolType, None, None), VarDecl(Id(d_1E), StringType, None, None), VarDecl(Id(oDuc), ArrayType([75.09], StringType), None, None)], Block([For(Id(KfV), Id(HF), BooleanLit(True), CallStmt(Id(lZh), []))])), FuncDecl(Id(hw), [VarDecl(Id(gyo6), ArrayType([66.6, 37.44], NumberType), None, None), VarDecl(Id(Ti), ArrayType([40.67], StringType), None, None), VarDecl(Id(KPc1), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115661))

	def test_21530115662(self):
		input = '''
dynamic dRe <- LY1
func a4 (bool OO[28.91,78.11], bool IuzA, number akD[82.67,40.47,30.98])
	begin
		if (IOy) gsp()
		else return
	end

'''
		expect = '''Program([VarDecl(Id(dRe), None, dynamic, Id(LY1)), FuncDecl(Id(a4), [VarDecl(Id(OO), ArrayType([28.91, 78.11], BoolType), None, None), VarDecl(Id(IuzA), BoolType, None, None), VarDecl(Id(akD), ArrayType([82.67, 40.47, 30.98], NumberType), None, None)], Block([If((Id(IOy), CallStmt(Id(gsp), [])), [], Return())]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115662))

	def test_21530115663(self):
		input = '''
string i7
'''
		expect = '''Program([VarDecl(Id(i7), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115663))

	def test_21530115664(self):
		input = '''
string eF[47.92,100.0,81.44] <- 93.44
'''
		expect = '''Program([VarDecl(Id(eF), ArrayType([47.92, 100.0, 81.44], StringType), None, NumLit(93.44))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115664))

	def test_21530115665(self):
		input = '''
string UkMG[12.83,89.49] <- H1Ep
func ZtX ()	return CZz

bool GF[75.59,90.42]
'''
		expect = '''Program([VarDecl(Id(UkMG), ArrayType([12.83, 89.49], StringType), None, Id(H1Ep)), FuncDecl(Id(ZtX), [], Return(Id(CZz))), VarDecl(Id(GF), ArrayType([75.59, 90.42], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115665))

	def test_21530115666(self):
		input = '''
bool LS[42.5]
number Lx[6.43]
number y8y5
number a_[77.03,30.23] <- "teK"
'''
		expect = '''Program([VarDecl(Id(LS), ArrayType([42.5], BoolType), None, None), VarDecl(Id(Lx), ArrayType([6.43], NumberType), None, None), VarDecl(Id(y8y5), NumberType, None, None), VarDecl(Id(a_), ArrayType([77.03, 30.23], NumberType), None, StringLit(teK))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115666))

	def test_21530115667(self):
		input = '''
bool tqs[66.13] <- 27.03
dynamic p_V <- "zpl"
number Xi[36.65] <- m7I
'''
		expect = '''Program([VarDecl(Id(tqs), ArrayType([66.13], BoolType), None, NumLit(27.03)), VarDecl(Id(p_V), None, dynamic, StringLit(zpl)), VarDecl(Id(Xi), ArrayType([36.65], NumberType), None, Id(m7I))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115667))

	def test_21530115668(self):
		input = '''
number rOYW
func NPq0 (number o496, bool CKz[59.84,72.16,31.36])	begin
		continue
		t2("p", 77.4)
		continue
	end
func bn17 (bool rty[74.64,12.04])	begin
		if (A_) kjdf("trA", true)
		begin
			if (Gk)
			break
			elif (LR)
			if (86.56) return
			elif (true) break
			elif (true) bool er[80.2,37.36]
			else VxS()
			elif (44.81) continue
			elif (false) NF(57.24, 23.64)
			elif (77.39)
			begin
				for c5V until Oni by oh
					break
				for wEMp until zoJN by true
					if (false) continue
					elif ("o")
					begin
						break
						begin
							continue
						end
					end
					elif (Ri) gj[true, "CQiO"] <- EA
					elif (false) mz0F[98.08] <- Acci
					else Sr[true, "s"] <- mU
			end
			else Bh(61.67, 8.44)
			bL(22.0, 72.52, 19.2)
		end
		JW(false)
	end

func Imc (bool P93[90.42], string vq, bool dKO[53.45,57.43,42.5])	return KuYi
func f0s (string lu, number a1ib[48.79,62.38], string rD6[54.06,31.41,47.71])	return

'''
		expect = '''Program([VarDecl(Id(rOYW), NumberType, None, None), FuncDecl(Id(NPq0), [VarDecl(Id(o496), NumberType, None, None), VarDecl(Id(CKz), ArrayType([59.84, 72.16, 31.36], BoolType), None, None)], Block([Continue, CallStmt(Id(t2), [StringLit(p), NumLit(77.4)]), Continue])), FuncDecl(Id(bn17), [VarDecl(Id(rty), ArrayType([74.64, 12.04], BoolType), None, None)], Block([If((Id(A_), CallStmt(Id(kjdf), [StringLit(trA), BooleanLit(True)])), [], None), Block([If((Id(Gk), Break), [(Id(LR), If((NumLit(86.56), Return()), [(BooleanLit(True), Break), (BooleanLit(True), VarDecl(Id(er), ArrayType([80.2, 37.36], BoolType), None, None))], CallStmt(Id(VxS), []))), (NumLit(44.81), Continue), (BooleanLit(False), CallStmt(Id(NF), [NumLit(57.24), NumLit(23.64)])), (NumLit(77.39), Block([For(Id(c5V), Id(Oni), Id(oh), Break), For(Id(wEMp), Id(zoJN), BooleanLit(True), If((BooleanLit(False), Continue), [(StringLit(o), Block([Break, Block([Continue])])), (Id(Ri), AssignStmt(ArrayCell(Id(gj), [BooleanLit(True), StringLit(CQiO)]), Id(EA))), (BooleanLit(False), AssignStmt(ArrayCell(Id(mz0F), [NumLit(98.08)]), Id(Acci)))], AssignStmt(ArrayCell(Id(Sr), [BooleanLit(True), StringLit(s)]), Id(mU))))]))], CallStmt(Id(Bh), [NumLit(61.67), NumLit(8.44)])), CallStmt(Id(bL), [NumLit(22.0), NumLit(72.52), NumLit(19.2)])]), CallStmt(Id(JW), [BooleanLit(False)])])), FuncDecl(Id(Imc), [VarDecl(Id(P93), ArrayType([90.42], BoolType), None, None), VarDecl(Id(vq), StringType, None, None), VarDecl(Id(dKO), ArrayType([53.45, 57.43, 42.5], BoolType), None, None)], Return(Id(KuYi))), FuncDecl(Id(f0s), [VarDecl(Id(lu), StringType, None, None), VarDecl(Id(a1ib), ArrayType([48.79, 62.38], NumberType), None, None), VarDecl(Id(rD6), ArrayType([54.06, 31.41, 47.71], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115668))

	def test_21530115669(self):
		input = '''
number olK[82.67] <- 8.59
func il (string cR[66.36,46.65], bool zvh[38.55,33.17])	return

number cjd
dynamic R54 <- 0.8
bool bu[78.56,8.5] <- 6.36
'''
		expect = '''Program([VarDecl(Id(olK), ArrayType([82.67], NumberType), None, NumLit(8.59)), FuncDecl(Id(il), [VarDecl(Id(cR), ArrayType([66.36, 46.65], StringType), None, None), VarDecl(Id(zvh), ArrayType([38.55, 33.17], BoolType), None, None)], Return()), VarDecl(Id(cjd), NumberType, None, None), VarDecl(Id(R54), None, dynamic, NumLit(0.8)), VarDecl(Id(bu), ArrayType([78.56, 8.5], BoolType), None, NumLit(6.36))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115669))

	def test_21530115670(self):
		input = '''
func wjq (number pT[65.04])	return
'''
		expect = '''Program([FuncDecl(Id(wjq), [VarDecl(Id(pT), ArrayType([65.04], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115670))

	def test_21530115671(self):
		input = '''
var arng <- false
string oey[98.21,79.82,58.9]
func Yoa (bool KGA, number mmEH[7.1,2.76], string rn)
	return 61.42
func XB (bool EcNj)	begin
		if (lPN) return
		elif (eWn) begin
			break
			Qi <- op
			uWf()
		end
		continue
	end

'''
		expect = '''Program([VarDecl(Id(arng), None, var, BooleanLit(False)), VarDecl(Id(oey), ArrayType([98.21, 79.82, 58.9], StringType), None, None), FuncDecl(Id(Yoa), [VarDecl(Id(KGA), BoolType, None, None), VarDecl(Id(mmEH), ArrayType([7.1, 2.76], NumberType), None, None), VarDecl(Id(rn), StringType, None, None)], Return(NumLit(61.42))), FuncDecl(Id(XB), [VarDecl(Id(EcNj), BoolType, None, None)], Block([If((Id(lPN), Return()), [(Id(eWn), Block([Break, AssignStmt(Id(Qi), Id(op)), CallStmt(Id(uWf), [])]))], None), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115671))

	def test_21530115672(self):
		input = '''
func DTg (string dF9s[51.49,36.96], number R2VE)	begin
		break
		for NEnw until "PIt" by false
			begin
				return
				if (64.77)
				aNrq()
				elif (AuI)
				var Scly <- true
				else nNkT[64.53, false, true] <- "XuZx"
			end
	end
func AVI (string LKF, number bqCA[79.18,62.84,76.6], bool dw[98.34,82.11])	return
var RC <- MVG
bool kK[34.39]
func xC4G (number bV5[68.37,30.88,93.72])
	return
'''
		expect = '''Program([FuncDecl(Id(DTg), [VarDecl(Id(dF9s), ArrayType([51.49, 36.96], StringType), None, None), VarDecl(Id(R2VE), NumberType, None, None)], Block([Break, For(Id(NEnw), StringLit(PIt), BooleanLit(False), Block([Return(), If((NumLit(64.77), CallStmt(Id(aNrq), [])), [(Id(AuI), VarDecl(Id(Scly), None, var, BooleanLit(True)))], AssignStmt(ArrayCell(Id(nNkT), [NumLit(64.53), BooleanLit(False), BooleanLit(True)]), StringLit(XuZx)))]))])), FuncDecl(Id(AVI), [VarDecl(Id(LKF), StringType, None, None), VarDecl(Id(bqCA), ArrayType([79.18, 62.84, 76.6], NumberType), None, None), VarDecl(Id(dw), ArrayType([98.34, 82.11], BoolType), None, None)], Return()), VarDecl(Id(RC), None, var, Id(MVG)), VarDecl(Id(kK), ArrayType([34.39], BoolType), None, None), FuncDecl(Id(xC4G), [VarDecl(Id(bV5), ArrayType([68.37, 30.88, 93.72], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115672))

	def test_21530115673(self):
		input = '''
func zci (string oox, number vyA[50.02,73.98], number yp[95.39])	return "LwoBt"
'''
		expect = '''Program([FuncDecl(Id(zci), [VarDecl(Id(oox), StringType, None, None), VarDecl(Id(vyA), ArrayType([50.02, 73.98], NumberType), None, None), VarDecl(Id(yp), ArrayType([95.39], NumberType), None, None)], Return(StringLit(LwoBt)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115673))

	def test_21530115674(self):
		input = '''
string IC
number rH[70.6]
number Qs0E[59.25,62.4] <- 49.39
bool qT95[83.94] <- "m"
'''
		expect = '''Program([VarDecl(Id(IC), StringType, None, None), VarDecl(Id(rH), ArrayType([70.6], NumberType), None, None), VarDecl(Id(Qs0E), ArrayType([59.25, 62.4], NumberType), None, NumLit(49.39)), VarDecl(Id(qT95), ArrayType([83.94], BoolType), None, StringLit(m))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115674))

	def test_21530115675(self):
		input = '''
func whT (string N9[13.34,66.06,37.82], number A_b)
	return

func bFm (number Kil, string iQ, number g_y)
	begin
		begin
			string KXj[3.71,70.28,89.14] <- N0
		end
		for mxn1 until "iqH" by EiV
			iN <- 23.26
		string gQI[30.55,18.45]
	end
'''
		expect = '''Program([FuncDecl(Id(whT), [VarDecl(Id(N9), ArrayType([13.34, 66.06, 37.82], StringType), None, None), VarDecl(Id(A_b), NumberType, None, None)], Return()), FuncDecl(Id(bFm), [VarDecl(Id(Kil), NumberType, None, None), VarDecl(Id(iQ), StringType, None, None), VarDecl(Id(g_y), NumberType, None, None)], Block([Block([VarDecl(Id(KXj), ArrayType([3.71, 70.28, 89.14], StringType), None, Id(N0))]), For(Id(mxn1), StringLit(iqH), Id(EiV), AssignStmt(Id(iN), NumLit(23.26))), VarDecl(Id(gQI), ArrayType([30.55, 18.45], StringType), None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115675))

	def test_21530115676(self):
		input = '''
func gRi ()
	return false

'''
		expect = '''Program([FuncDecl(Id(gRi), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115676))

	def test_21530115677(self):
		input = '''
func li ()	return
bool g7PQ[14.92,35.39] <- 51.47
number vlV2 <- "MJEyJ"
func n2rn (string J_Lx[35.13,91.44], number UPcS, number c9ib)
	return "vHkH"

func nC ()	return false
'''
		expect = '''Program([FuncDecl(Id(li), [], Return()), VarDecl(Id(g7PQ), ArrayType([14.92, 35.39], BoolType), None, NumLit(51.47)), VarDecl(Id(vlV2), NumberType, None, StringLit(MJEyJ)), FuncDecl(Id(n2rn), [VarDecl(Id(J_Lx), ArrayType([35.13, 91.44], StringType), None, None), VarDecl(Id(UPcS), NumberType, None, None), VarDecl(Id(c9ib), NumberType, None, None)], Return(StringLit(vHkH))), FuncDecl(Id(nC), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115677))

	def test_21530115678(self):
		input = '''
number hOG[35.12,1.8] <- "KRN"
func fC (string XiJ5[77.0,15.74], bool qaH[66.33,17.07])	return "jvV"
'''
		expect = '''Program([VarDecl(Id(hOG), ArrayType([35.12, 1.8], NumberType), None, StringLit(KRN)), FuncDecl(Id(fC), [VarDecl(Id(XiJ5), ArrayType([77.0, 15.74], StringType), None, None), VarDecl(Id(qaH), ArrayType([66.33, 17.07], BoolType), None, None)], Return(StringLit(jvV)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115678))

	def test_21530115679(self):
		input = '''
func Z9 (string vS, bool gcV[48.06,1.13,84.93], string bo_5[73.17,37.74])	begin
		break
		break
	end

bool Z1d
func LWgZ (number O1Y[84.33], bool j_EE[38.82,74.17])	return true

func MLWF (bool nhWX[66.22,39.31], number h2q[84.56])	return

'''
		expect = '''Program([FuncDecl(Id(Z9), [VarDecl(Id(vS), StringType, None, None), VarDecl(Id(gcV), ArrayType([48.06, 1.13, 84.93], BoolType), None, None), VarDecl(Id(bo_5), ArrayType([73.17, 37.74], StringType), None, None)], Block([Break, Break])), VarDecl(Id(Z1d), BoolType, None, None), FuncDecl(Id(LWgZ), [VarDecl(Id(O1Y), ArrayType([84.33], NumberType), None, None), VarDecl(Id(j_EE), ArrayType([38.82, 74.17], BoolType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(MLWF), [VarDecl(Id(nhWX), ArrayType([66.22, 39.31], BoolType), None, None), VarDecl(Id(h2q), ArrayType([84.56], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115679))

	def test_21530115680(self):
		input = '''
func NCFS (number mD_[16.0,39.18], number neP)	return

'''
		expect = '''Program([FuncDecl(Id(NCFS), [VarDecl(Id(mD_), ArrayType([16.0, 39.18], NumberType), None, None), VarDecl(Id(neP), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115680))

	def test_21530115681(self):
		input = '''
func b8h_ (number rE)	begin
	end

dynamic yqa <- 50.88
number Dxz[49.64,91.92,28.72] <- FZ4j
func mLx ()
	return true
bool JJ39[59.15,60.75] <- true
'''
		expect = '''Program([FuncDecl(Id(b8h_), [VarDecl(Id(rE), NumberType, None, None)], Block([])), VarDecl(Id(yqa), None, dynamic, NumLit(50.88)), VarDecl(Id(Dxz), ArrayType([49.64, 91.92, 28.72], NumberType), None, Id(FZ4j)), FuncDecl(Id(mLx), [], Return(BooleanLit(True))), VarDecl(Id(JJ39), ArrayType([59.15, 60.75], BoolType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115681))

	def test_21530115682(self):
		input = '''
func i9 (bool Hj, bool KwON)	return

func pS (number vEIK, number I8Qz)
	return "g"
dynamic JjG4 <- 90.71
func TX (number E62R[50.09,34.46], number QTKr[17.28])
	return
'''
		expect = '''Program([FuncDecl(Id(i9), [VarDecl(Id(Hj), BoolType, None, None), VarDecl(Id(KwON), BoolType, None, None)], Return()), FuncDecl(Id(pS), [VarDecl(Id(vEIK), NumberType, None, None), VarDecl(Id(I8Qz), NumberType, None, None)], Return(StringLit(g))), VarDecl(Id(JjG4), None, dynamic, NumLit(90.71)), FuncDecl(Id(TX), [VarDecl(Id(E62R), ArrayType([50.09, 34.46], NumberType), None, None), VarDecl(Id(QTKr), ArrayType([17.28], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115682))

	def test_21530115683(self):
		input = '''
bool kXjV <- Gu4
string BS60[58.22,67.19,74.44] <- 44.55
bool Rl[99.25] <- 3.63
func c3 ()	return

'''
		expect = '''Program([VarDecl(Id(kXjV), BoolType, None, Id(Gu4)), VarDecl(Id(BS60), ArrayType([58.22, 67.19, 74.44], StringType), None, NumLit(44.55)), VarDecl(Id(Rl), ArrayType([99.25], BoolType), None, NumLit(3.63)), FuncDecl(Id(c3), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115683))

	def test_21530115684(self):
		input = '''
func W0m ()
	return "Yey"

func YXy (bool ep, number Jn)
	return
string an[37.58] <- kT
func CI9 (number P3, bool gG, string OU[21.35,88.51])	return 35.5
'''
		expect = '''Program([FuncDecl(Id(W0m), [], Return(StringLit(Yey))), FuncDecl(Id(YXy), [VarDecl(Id(ep), BoolType, None, None), VarDecl(Id(Jn), NumberType, None, None)], Return()), VarDecl(Id(an), ArrayType([37.58], StringType), None, Id(kT)), FuncDecl(Id(CI9), [VarDecl(Id(P3), NumberType, None, None), VarDecl(Id(gG), BoolType, None, None), VarDecl(Id(OU), ArrayType([21.35, 88.51], StringType), None, None)], Return(NumLit(35.5)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115684))

	def test_21530115685(self):
		input = '''
bool nEZi[89.55,38.83,43.28]
dynamic WSb
'''
		expect = '''Program([VarDecl(Id(nEZi), ArrayType([89.55, 38.83, 43.28], BoolType), None, None), VarDecl(Id(WSb), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115685))

	def test_21530115686(self):
		input = '''
bool EcF[58.38] <- true
string a_g <- "Uemjx"
func ZFc (string cUWR[26.9,26.87,92.3], number To[71.58], number vdF[59.71,38.56,22.1])
	return
'''
		expect = '''Program([VarDecl(Id(EcF), ArrayType([58.38], BoolType), None, BooleanLit(True)), VarDecl(Id(a_g), StringType, None, StringLit(Uemjx)), FuncDecl(Id(ZFc), [VarDecl(Id(cUWR), ArrayType([26.9, 26.87, 92.3], StringType), None, None), VarDecl(Id(To), ArrayType([71.58], NumberType), None, None), VarDecl(Id(vdF), ArrayType([59.71, 38.56, 22.1], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115686))

	def test_21530115687(self):
		input = '''
string uvV3[24.83] <- 32.86
bool lg8D
'''
		expect = '''Program([VarDecl(Id(uvV3), ArrayType([24.83], StringType), None, NumLit(32.86)), VarDecl(Id(lg8D), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115687))

	def test_21530115688(self):
		input = '''
string zy1[31.63,57.59,44.9] <- WCt
bool Mu1x <- "F"
bool QAo <- "DeHsW"
dynamic vWke
'''
		expect = '''Program([VarDecl(Id(zy1), ArrayType([31.63, 57.59, 44.9], StringType), None, Id(WCt)), VarDecl(Id(Mu1x), BoolType, None, StringLit(F)), VarDecl(Id(QAo), BoolType, None, StringLit(DeHsW)), VarDecl(Id(vWke), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115688))

	def test_21530115689(self):
		input = '''
number Cc[48.53]
func yDlf ()	return
func qh7X (bool ESO[55.91,90.1], string SqE[40.97,37.09,12.27])	return
'''
		expect = '''Program([VarDecl(Id(Cc), ArrayType([48.53], NumberType), None, None), FuncDecl(Id(yDlf), [], Return()), FuncDecl(Id(qh7X), [VarDecl(Id(ESO), ArrayType([55.91, 90.1], BoolType), None, None), VarDecl(Id(SqE), ArrayType([40.97, 37.09, 12.27], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115689))

	def test_21530115690(self):
		input = '''
number MXS2[32.78] <- false
func krD ()
	return
number eP[98.14,33.86] <- w4Ts
'''
		expect = '''Program([VarDecl(Id(MXS2), ArrayType([32.78], NumberType), None, BooleanLit(False)), FuncDecl(Id(krD), [], Return()), VarDecl(Id(eP), ArrayType([98.14, 33.86], NumberType), None, Id(w4Ts))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115690))

	def test_21530115691(self):
		input = '''
func Qg ()
	return "Y"

string HnB[1.91] <- O6
func fS (number FU[52.75])
	return
'''
		expect = '''Program([FuncDecl(Id(Qg), [], Return(StringLit(Y))), VarDecl(Id(HnB), ArrayType([1.91], StringType), None, Id(O6)), FuncDecl(Id(fS), [VarDecl(Id(FU), ArrayType([52.75], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115691))

	def test_21530115692(self):
		input = '''
func xJ (number Ba)
	return MNpI
func G2LX (string aPy, bool lI)
	begin
		break
	end

'''
		expect = '''Program([FuncDecl(Id(xJ), [VarDecl(Id(Ba), NumberType, None, None)], Return(Id(MNpI))), FuncDecl(Id(G2LX), [VarDecl(Id(aPy), StringType, None, None), VarDecl(Id(lI), BoolType, None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115692))

	def test_21530115693(self):
		input = '''
func c59U ()	return

func dtp ()	begin
		return F77
	end

number OR9g[6.54,7.54,87.27]
func FD (string gH[69.61,2.33], string uZ[73.68,30.48], number zFn)
	return 90.57
func siU (string OAxD, string pi[71.1,10.39,5.7], string H5)	begin
		continue
		break
	end

'''
		expect = '''Program([FuncDecl(Id(c59U), [], Return()), FuncDecl(Id(dtp), [], Block([Return(Id(F77))])), VarDecl(Id(OR9g), ArrayType([6.54, 7.54, 87.27], NumberType), None, None), FuncDecl(Id(FD), [VarDecl(Id(gH), ArrayType([69.61, 2.33], StringType), None, None), VarDecl(Id(uZ), ArrayType([73.68, 30.48], StringType), None, None), VarDecl(Id(zFn), NumberType, None, None)], Return(NumLit(90.57))), FuncDecl(Id(siU), [VarDecl(Id(OAxD), StringType, None, None), VarDecl(Id(pi), ArrayType([71.1, 10.39, 5.7], StringType), None, None), VarDecl(Id(H5), StringType, None, None)], Block([Continue, Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115693))

	def test_21530115694(self):
		input = '''
var PkWu <- 14.34
func XY ()
	return "ncRal"
dynamic zkXb
'''
		expect = '''Program([VarDecl(Id(PkWu), None, var, NumLit(14.34)), FuncDecl(Id(XY), [], Return(StringLit(ncRal))), VarDecl(Id(zkXb), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115694))

	def test_21530115695(self):
		input = '''
func Wev (bool t5Xa[83.48,51.3,91.88], bool qXG, number S9zf[84.41])
	begin
		Qj[86.07, "GmZI", 55.48] <- OZm
		if (false)
		continue
		elif (Rg)
		continue
		else number tRfE[21.03]
		BW()
	end
bool nj <- uu
string tSIV[45.9,7.18,68.77] <- true
bool Sqkk
'''
		expect = '''Program([FuncDecl(Id(Wev), [VarDecl(Id(t5Xa), ArrayType([83.48, 51.3, 91.88], BoolType), None, None), VarDecl(Id(qXG), BoolType, None, None), VarDecl(Id(S9zf), ArrayType([84.41], NumberType), None, None)], Block([AssignStmt(ArrayCell(Id(Qj), [NumLit(86.07), StringLit(GmZI), NumLit(55.48)]), Id(OZm)), If((BooleanLit(False), Continue), [(Id(Rg), Continue)], VarDecl(Id(tRfE), ArrayType([21.03], NumberType), None, None)), CallStmt(Id(BW), [])])), VarDecl(Id(nj), BoolType, None, Id(uu)), VarDecl(Id(tSIV), ArrayType([45.9, 7.18, 68.77], StringType), None, BooleanLit(True)), VarDecl(Id(Sqkk), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115695))

	def test_21530115696(self):
		input = '''
var vLx <- true
string QG44[82.79,12.94,67.15]
func AdEd (string Y8[63.93,84.6,34.13], number oiS, bool Atvn)
	begin
		SL0[t7W, 93.35, 63.2] <- 44.17
	end
number TZBI
'''
		expect = '''Program([VarDecl(Id(vLx), None, var, BooleanLit(True)), VarDecl(Id(QG44), ArrayType([82.79, 12.94, 67.15], StringType), None, None), FuncDecl(Id(AdEd), [VarDecl(Id(Y8), ArrayType([63.93, 84.6, 34.13], StringType), None, None), VarDecl(Id(oiS), NumberType, None, None), VarDecl(Id(Atvn), BoolType, None, None)], Block([AssignStmt(ArrayCell(Id(SL0), [Id(t7W), NumLit(93.35), NumLit(63.2)]), NumLit(44.17))])), VarDecl(Id(TZBI), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115696))

	def test_21530115697(self):
		input = '''
func Ef (bool J4[26.62,19.4,17.7])
	begin
		FpA(n_, 5.28)
		begin
			continue
			begin
			end
			begin
			end
		end
		W0h[Pp, Fv, "B"] <- true
	end

func piU ()	return
bool ZbG[41.43,43.17,23.54]
'''
		expect = '''Program([FuncDecl(Id(Ef), [VarDecl(Id(J4), ArrayType([26.62, 19.4, 17.7], BoolType), None, None)], Block([CallStmt(Id(FpA), [Id(n_), NumLit(5.28)]), Block([Continue, Block([]), Block([])]), AssignStmt(ArrayCell(Id(W0h), [Id(Pp), Id(Fv), StringLit(B)]), BooleanLit(True))])), FuncDecl(Id(piU), [], Return()), VarDecl(Id(ZbG), ArrayType([41.43, 43.17, 23.54], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115697))

	def test_21530115698(self):
		input = '''
dynamic Xqc <- "FoJj"
'''
		expect = '''Program([VarDecl(Id(Xqc), None, dynamic, StringLit(FoJj))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115698))

	def test_21530115699(self):
		input = '''
func h0a (string tAh[96.05,27.67,87.99], number vd[90.12])	return V7G

func fiv ()	begin
	end

'''
		expect = '''Program([FuncDecl(Id(h0a), [VarDecl(Id(tAh), ArrayType([96.05, 27.67, 87.99], StringType), None, None), VarDecl(Id(vd), ArrayType([90.12], NumberType), None, None)], Return(Id(V7G))), FuncDecl(Id(fiv), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115699))

	def test_21530115700(self):
		input = '''
string Kw <- RUH
number wOMZ
var K9 <- true
'''
		expect = '''Program([VarDecl(Id(Kw), StringType, None, Id(RUH)), VarDecl(Id(wOMZ), NumberType, None, None), VarDecl(Id(K9), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115700))

	def test_21530115701(self):
		input = '''
func XDfd (bool GlA[33.89,22.92,37.19])	return
func COnj ()	return
'''
		expect = '''Program([FuncDecl(Id(XDfd), [VarDecl(Id(GlA), ArrayType([33.89, 22.92, 37.19], BoolType), None, None)], Return()), FuncDecl(Id(COnj), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115701))

	def test_21530115702(self):
		input = '''
dynamic WJo0
func AScR (string YR[45.28], string I5_, number TB[62.37,75.05,0.53])	begin
		for TL until 98.66 by 51.34
			string bzS[48.39] <- 71.47
		ftc("kwOgt")
	end
'''
		expect = '''Program([VarDecl(Id(WJo0), None, dynamic, None), FuncDecl(Id(AScR), [VarDecl(Id(YR), ArrayType([45.28], StringType), None, None), VarDecl(Id(I5_), StringType, None, None), VarDecl(Id(TB), ArrayType([62.37, 75.05, 0.53], NumberType), None, None)], Block([For(Id(TL), NumLit(98.66), NumLit(51.34), VarDecl(Id(bzS), ArrayType([48.39], StringType), None, NumLit(71.47))), CallStmt(Id(ftc), [StringLit(kwOgt)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115702))

	def test_21530115703(self):
		input = '''
number LB <- ITjc
func IStH (bool e9h)	return
'''
		expect = '''Program([VarDecl(Id(LB), NumberType, None, Id(ITjc)), FuncDecl(Id(IStH), [VarDecl(Id(e9h), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115703))

	def test_21530115704(self):
		input = '''
dynamic jXUf
func PuV (bool VmW[70.09,65.36,34.09], number w0SC[42.28,35.0,89.85])
	return
string FV[0.86]
'''
		expect = '''Program([VarDecl(Id(jXUf), None, dynamic, None), FuncDecl(Id(PuV), [VarDecl(Id(VmW), ArrayType([70.09, 65.36, 34.09], BoolType), None, None), VarDecl(Id(w0SC), ArrayType([42.28, 35.0, 89.85], NumberType), None, None)], Return()), VarDecl(Id(FV), ArrayType([0.86], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115704))

	def test_21530115705(self):
		input = '''
bool Kb6 <- J0r
func YMI (string Bg[28.14,71.02,59.28], number dg4[30.45,1.66,31.46])	begin
		return
		dynamic yEfk <- 74.17
	end
func U47 (string qSnq[16.94,92.51,87.16], number j95)	return false

'''
		expect = '''Program([VarDecl(Id(Kb6), BoolType, None, Id(J0r)), FuncDecl(Id(YMI), [VarDecl(Id(Bg), ArrayType([28.14, 71.02, 59.28], StringType), None, None), VarDecl(Id(dg4), ArrayType([30.45, 1.66, 31.46], NumberType), None, None)], Block([Return(), VarDecl(Id(yEfk), None, dynamic, NumLit(74.17))])), FuncDecl(Id(U47), [VarDecl(Id(qSnq), ArrayType([16.94, 92.51, 87.16], StringType), None, None), VarDecl(Id(j95), NumberType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115705))

	def test_21530115706(self):
		input = '''
bool Dxh[69.99,18.8] <- 70.47
bool gIc <- false
func BXxw (string iIaW[97.72,38.87,67.82], number Nv)	begin
	end

func WWJ ()
	return 56.45

'''
		expect = '''Program([VarDecl(Id(Dxh), ArrayType([69.99, 18.8], BoolType), None, NumLit(70.47)), VarDecl(Id(gIc), BoolType, None, BooleanLit(False)), FuncDecl(Id(BXxw), [VarDecl(Id(iIaW), ArrayType([97.72, 38.87, 67.82], StringType), None, None), VarDecl(Id(Nv), NumberType, None, None)], Block([])), FuncDecl(Id(WWJ), [], Return(NumLit(56.45)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115706))

	def test_21530115707(self):
		input = '''
dynamic fadC <- true
number AN
bool XQ4f[83.12,50.65,11.11]
bool pgqY[78.83,98.4] <- 18.9
'''
		expect = '''Program([VarDecl(Id(fadC), None, dynamic, BooleanLit(True)), VarDecl(Id(AN), NumberType, None, None), VarDecl(Id(XQ4f), ArrayType([83.12, 50.65, 11.11], BoolType), None, None), VarDecl(Id(pgqY), ArrayType([78.83, 98.4], BoolType), None, NumLit(18.9))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115707))

	def test_21530115708(self):
		input = '''
func MH (number au[33.75,56.8], bool MKKR, number hM)
	return bNE

'''
		expect = '''Program([FuncDecl(Id(MH), [VarDecl(Id(au), ArrayType([33.75, 56.8], NumberType), None, None), VarDecl(Id(MKKR), BoolType, None, None), VarDecl(Id(hM), NumberType, None, None)], Return(Id(bNE)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115708))

	def test_21530115709(self):
		input = '''
string Jx1[71.76]
'''
		expect = '''Program([VarDecl(Id(Jx1), ArrayType([71.76], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115709))

	def test_21530115710(self):
		input = '''
func g2 ()
	begin
		if (true)
		break
		elif (brzz)
		if (LKjR) bool kMK <- true
		else begin
			J2(67.37)
			dePg <- true
		end
		elif ("vSbW")
		if (true)
		begin
			for xak until "MTRWK" by false
				D9Xr(FkNU, 42.03)
		end
		elif (Pji) continue
		elif (45.2) va[true, true, 80.85] <- true
		elif (false) return
		elif ("dW") continue
		else return
		elif ("Esapq")
		number ioXn[24.53,62.25] <- true
		elif (true) if (F9zu) for Zo until "begOJ" by SX3
			ce8i()
		elif (pCDd)
		av <- 15.93
		elif (97.07) xvH(h1s, "srRRk", 6.13)
		elif (z7)
		if (true)
		for pjks until 14.6 by true
			return
		elif (M1)
		begin
			bool W4[68.86] <- 73.23
		end
		elif (true)
		Rc1["cj", 31.52, HK] <- 78.74
		elif (false) continue
		elif ("fW")
		for RyG until false by false
			dW["aq"] <- 20.27
	end
dynamic QwCC
'''
		expect = '''Program([FuncDecl(Id(g2), [], Block([If((BooleanLit(True), Break), [(Id(brzz), If((Id(LKjR), VarDecl(Id(kMK), BoolType, None, BooleanLit(True))), [], Block([CallStmt(Id(J2), [NumLit(67.37)]), AssignStmt(Id(dePg), BooleanLit(True))]))), (StringLit(vSbW), If((BooleanLit(True), Block([For(Id(xak), StringLit(MTRWK), BooleanLit(False), CallStmt(Id(D9Xr), [Id(FkNU), NumLit(42.03)]))])), [(Id(Pji), Continue), (NumLit(45.2), AssignStmt(ArrayCell(Id(va), [BooleanLit(True), BooleanLit(True), NumLit(80.85)]), BooleanLit(True))), (BooleanLit(False), Return()), (StringLit(dW), Continue)], Return())), (StringLit(Esapq), VarDecl(Id(ioXn), ArrayType([24.53, 62.25], NumberType), None, BooleanLit(True))), (BooleanLit(True), If((Id(F9zu), For(Id(Zo), StringLit(begOJ), Id(SX3), CallStmt(Id(ce8i), []))), [(Id(pCDd), AssignStmt(Id(av), NumLit(15.93))), (NumLit(97.07), CallStmt(Id(xvH), [Id(h1s), StringLit(srRRk), NumLit(6.13)])), (Id(z7), If((BooleanLit(True), For(Id(pjks), NumLit(14.6), BooleanLit(True), Return())), [(Id(M1), Block([VarDecl(Id(W4), ArrayType([68.86], BoolType), None, NumLit(73.23))])), (BooleanLit(True), AssignStmt(ArrayCell(Id(Rc1), [StringLit(cj), NumLit(31.52), Id(HK)]), NumLit(78.74))), (BooleanLit(False), Continue), (StringLit(fW), For(Id(RyG), BooleanLit(False), BooleanLit(False), AssignStmt(ArrayCell(Id(dW), [StringLit(aq)]), NumLit(20.27))))], None))], None))], None)])), VarDecl(Id(QwCC), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115710))

	def test_21530115711(self):
		input = '''
func l8 (bool VN2)	return wfu

string LGs[87.11] <- true
func TeT (bool BE[94.93,36.27])
	begin
		continue
	end

dynamic cfH
'''
		expect = '''Program([FuncDecl(Id(l8), [VarDecl(Id(VN2), BoolType, None, None)], Return(Id(wfu))), VarDecl(Id(LGs), ArrayType([87.11], StringType), None, BooleanLit(True)), FuncDecl(Id(TeT), [VarDecl(Id(BE), ArrayType([94.93, 36.27], BoolType), None, None)], Block([Continue])), VarDecl(Id(cfH), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115711))

	def test_21530115712(self):
		input = '''
bool oSa
dynamic SXpn <- "r"
'''
		expect = '''Program([VarDecl(Id(oSa), BoolType, None, None), VarDecl(Id(SXpn), None, dynamic, StringLit(r))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115712))

	def test_21530115713(self):
		input = '''
string Gq
func nSPR (string xRN4)
	begin
	end

func BI_N ()	begin
		Ij8j()
		L0 <- 43.89
		Zcfj(WMn9, 80.5)
	end
dynamic pg
string TX
'''
		expect = '''Program([VarDecl(Id(Gq), StringType, None, None), FuncDecl(Id(nSPR), [VarDecl(Id(xRN4), StringType, None, None)], Block([])), FuncDecl(Id(BI_N), [], Block([CallStmt(Id(Ij8j), []), AssignStmt(Id(L0), NumLit(43.89)), CallStmt(Id(Zcfj), [Id(WMn9), NumLit(80.5)])])), VarDecl(Id(pg), None, dynamic, None), VarDecl(Id(TX), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115713))

	def test_21530115714(self):
		input = '''
bool DzU6 <- aBUp
'''
		expect = '''Program([VarDecl(Id(DzU6), BoolType, None, Id(aBUp))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115714))

	def test_21530115715(self):
		input = '''
bool uJa6[10.64,12.87,62.03] <- false
dynamic yy
bool TFR[20.6,41.7,62.66] <- "qjF"
func eS ()	begin
	end

func FhSC (string mJ[30.21])	begin
		return
		return true
		TAs_ <- 14.82
	end

'''
		expect = '''Program([VarDecl(Id(uJa6), ArrayType([10.64, 12.87, 62.03], BoolType), None, BooleanLit(False)), VarDecl(Id(yy), None, dynamic, None), VarDecl(Id(TFR), ArrayType([20.6, 41.7, 62.66], BoolType), None, StringLit(qjF)), FuncDecl(Id(eS), [], Block([])), FuncDecl(Id(FhSC), [VarDecl(Id(mJ), ArrayType([30.21], StringType), None, None)], Block([Return(), Return(BooleanLit(True)), AssignStmt(Id(TAs_), NumLit(14.82))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115715))

	def test_21530115716(self):
		input = '''
func e7 (number UCrM)	return "rgwe"
bool Hbrn
func o4L ()
	return OBgC

func Orsq ()	return

'''
		expect = '''Program([FuncDecl(Id(e7), [VarDecl(Id(UCrM), NumberType, None, None)], Return(StringLit(rgwe))), VarDecl(Id(Hbrn), BoolType, None, None), FuncDecl(Id(o4L), [], Return(Id(OBgC))), FuncDecl(Id(Orsq), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115716))

	def test_21530115717(self):
		input = '''
bool QD[25.39]
func GwJh (number uJ7[94.45])	begin
	end
var nz <- pvQ
number yNEf <- "YwGb"
func t4sN (string kdZ[70.6,92.19,53.16])	begin
	end

'''
		expect = '''Program([VarDecl(Id(QD), ArrayType([25.39], BoolType), None, None), FuncDecl(Id(GwJh), [VarDecl(Id(uJ7), ArrayType([94.45], NumberType), None, None)], Block([])), VarDecl(Id(nz), None, var, Id(pvQ)), VarDecl(Id(yNEf), NumberType, None, StringLit(YwGb)), FuncDecl(Id(t4sN), [VarDecl(Id(kdZ), ArrayType([70.6, 92.19, 53.16], StringType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115717))

	def test_21530115718(self):
		input = '''
func ta (number TRJ0, number IkUt[29.29,78.61])
	begin
		return
	end

number qqS[44.83] <- 23.82
func OOkA (string gA[41.73,13.71,57.75], number h4cJ, string Sg[63.94])
	begin
		qL(false)
		dynamic N9Lh
	end

number aX[9.57,97.54,6.23] <- true
'''
		expect = '''Program([FuncDecl(Id(ta), [VarDecl(Id(TRJ0), NumberType, None, None), VarDecl(Id(IkUt), ArrayType([29.29, 78.61], NumberType), None, None)], Block([Return()])), VarDecl(Id(qqS), ArrayType([44.83], NumberType), None, NumLit(23.82)), FuncDecl(Id(OOkA), [VarDecl(Id(gA), ArrayType([41.73, 13.71, 57.75], StringType), None, None), VarDecl(Id(h4cJ), NumberType, None, None), VarDecl(Id(Sg), ArrayType([63.94], StringType), None, None)], Block([CallStmt(Id(qL), [BooleanLit(False)]), VarDecl(Id(N9Lh), None, dynamic, None)])), VarDecl(Id(aX), ArrayType([9.57, 97.54, 6.23], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115718))

	def test_21530115719(self):
		input = '''
string Ju[18.25] <- 97.05
bool e7o[88.57,89.8,39.91] <- "Lyc"
bool umGO <- 6.05
'''
		expect = '''Program([VarDecl(Id(Ju), ArrayType([18.25], StringType), None, NumLit(97.05)), VarDecl(Id(e7o), ArrayType([88.57, 89.8, 39.91], BoolType), None, StringLit(Lyc)), VarDecl(Id(umGO), BoolType, None, NumLit(6.05))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115719))

	def test_21530115720(self):
		input = '''
number xr[34.81,97.22] <- ABhw
func GpOH ()	return m8YL

bool ICd[35.61,61.06] <- "H"
func PWn ()	begin
		break
		if ("oSbuh") number hnDS
		elif ("RzRfR")
		Kh(52.04)
		elif (qpyb) Es6 <- 45.32
		else begin
			QnTe()
			continue
		end
		hS(MDki)
	end
'''
		expect = '''Program([VarDecl(Id(xr), ArrayType([34.81, 97.22], NumberType), None, Id(ABhw)), FuncDecl(Id(GpOH), [], Return(Id(m8YL))), VarDecl(Id(ICd), ArrayType([35.61, 61.06], BoolType), None, StringLit(H)), FuncDecl(Id(PWn), [], Block([Break, If((StringLit(oSbuh), VarDecl(Id(hnDS), NumberType, None, None)), [(StringLit(RzRfR), CallStmt(Id(Kh), [NumLit(52.04)])), (Id(qpyb), AssignStmt(Id(Es6), NumLit(45.32)))], Block([CallStmt(Id(QnTe), []), Continue])), CallStmt(Id(hS), [Id(MDki)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115720))

	def test_21530115721(self):
		input = '''
number mr[91.68,72.77,8.66]
func ew (string L8N, string CMAj[6.16,51.62,67.04], string SVXi)
	return false

var g1y <- 65.85
func T8DB ()
	return false

string u9fa <- 74.3
'''
		expect = '''Program([VarDecl(Id(mr), ArrayType([91.68, 72.77, 8.66], NumberType), None, None), FuncDecl(Id(ew), [VarDecl(Id(L8N), StringType, None, None), VarDecl(Id(CMAj), ArrayType([6.16, 51.62, 67.04], StringType), None, None), VarDecl(Id(SVXi), StringType, None, None)], Return(BooleanLit(False))), VarDecl(Id(g1y), None, var, NumLit(65.85)), FuncDecl(Id(T8DB), [], Return(BooleanLit(False))), VarDecl(Id(u9fa), StringType, None, NumLit(74.3))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115721))

	def test_21530115722(self):
		input = '''
bool iO
'''
		expect = '''Program([VarDecl(Id(iO), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115722))

	def test_21530115723(self):
		input = '''
func Vw (bool jwW, string Vw1[17.73,54.39])
	return
'''
		expect = '''Program([FuncDecl(Id(Vw), [VarDecl(Id(jwW), BoolType, None, None), VarDecl(Id(Vw1), ArrayType([17.73, 54.39], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115723))

	def test_21530115724(self):
		input = '''
string YgXf <- ql0
func jnfE (string N62N)
	begin
	end

func OQ (string HMQ[39.37])	return 48.99

func ZB ()
	return false

bool hQd3[63.44,61.16,10.97]
'''
		expect = '''Program([VarDecl(Id(YgXf), StringType, None, Id(ql0)), FuncDecl(Id(jnfE), [VarDecl(Id(N62N), StringType, None, None)], Block([])), FuncDecl(Id(OQ), [VarDecl(Id(HMQ), ArrayType([39.37], StringType), None, None)], Return(NumLit(48.99))), FuncDecl(Id(ZB), [], Return(BooleanLit(False))), VarDecl(Id(hQd3), ArrayType([63.44, 61.16, 10.97], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115724))

	def test_21530115725(self):
		input = '''
func D8BL (bool ZAW[44.5,42.51], string htyd)	begin
		for FT until true by "eAVWp"
			if (qT0) for G4Tl until false by "Zw"
				if (92.35) for ycp until 7.33 by kIuV
					if (GRve) begin
					end
				elif (true)
				for Qc until AoPc by false
					return
				elif (B2C)
				begin
					nx[true, 92.17, Oj9i] <- 69.32
					VLCg(true, Kjt)
					begin
						return FkZG
						b7k[32.42, "B"] <- 13.88
					end
				end
				elif (QW) for SM8k until false by 88.39
					H9[85.42, 23.16, "r"] <- nO
				elif (PY2)
				dynamic WqQ0 <- "TIyZL"
				else begin
					gm("LBLMW", lo)
				end
			elif (58.88)
			TEbM()
			elif (true)
			if (false) break
			elif (Pn) hz <- Yxu
			elif (43.1)
			W44u[true, Suvl, 6.23] <- RP8D
			elif (false)
			continue
			elif (true) for Jw0 until true by AU
				continue
			else for Pq until oOY by 77.02
				for zIKY until uQf by "qzd"
					for VKYS until lm by b0fF
						for bS until false by 59.77
							for dW until HX by zk
								for XSV2 until true by "LcB"
									if (qZPq) Z3(54.6, "Jo", ZG2)
									elif ("m")
									yU()
									elif ("fIJGv") break
									elif (71.92)
									number nsP2[20.58,94.85,7.94]
									elif (xcRH) break
									else if (true) begin
										bool pP[9.14] <- true
										begin
											continue
											string lKE[32.59,80.92,92.8]
											VhGi <- lHf
										end
									end
									elif (false)
									break
									elif (Gm7_)
									break
									elif (71.9) string Yr8
									elif ("F")
									break
									else for H_D9 until "GyI" by 25.64
										begin
										end
		lE()
	end

func yX ()	return

'''
		expect = '''Program([FuncDecl(Id(D8BL), [VarDecl(Id(ZAW), ArrayType([44.5, 42.51], BoolType), None, None), VarDecl(Id(htyd), StringType, None, None)], Block([For(Id(FT), BooleanLit(True), StringLit(eAVWp), If((Id(qT0), For(Id(G4Tl), BooleanLit(False), StringLit(Zw), If((NumLit(92.35), For(Id(ycp), NumLit(7.33), Id(kIuV), If((Id(GRve), Block([])), [(BooleanLit(True), For(Id(Qc), Id(AoPc), BooleanLit(False), Return())), (Id(B2C), Block([AssignStmt(ArrayCell(Id(nx), [BooleanLit(True), NumLit(92.17), Id(Oj9i)]), NumLit(69.32)), CallStmt(Id(VLCg), [BooleanLit(True), Id(Kjt)]), Block([Return(Id(FkZG)), AssignStmt(ArrayCell(Id(b7k), [NumLit(32.42), StringLit(B)]), NumLit(13.88))])])), (Id(QW), For(Id(SM8k), BooleanLit(False), NumLit(88.39), AssignStmt(ArrayCell(Id(H9), [NumLit(85.42), NumLit(23.16), StringLit(r)]), Id(nO)))), (Id(PY2), VarDecl(Id(WqQ0), None, dynamic, StringLit(TIyZL)))], Block([CallStmt(Id(gm), [StringLit(LBLMW), Id(lo)])])))), [(NumLit(58.88), CallStmt(Id(TEbM), [])), (BooleanLit(True), If((BooleanLit(False), Break), [(Id(Pn), AssignStmt(Id(hz), Id(Yxu))), (NumLit(43.1), AssignStmt(ArrayCell(Id(W44u), [BooleanLit(True), Id(Suvl), NumLit(6.23)]), Id(RP8D))), (BooleanLit(False), Continue), (BooleanLit(True), For(Id(Jw0), BooleanLit(True), Id(AU), Continue))], For(Id(Pq), Id(oOY), NumLit(77.02), For(Id(zIKY), Id(uQf), StringLit(qzd), For(Id(VKYS), Id(lm), Id(b0fF), For(Id(bS), BooleanLit(False), NumLit(59.77), For(Id(dW), Id(HX), Id(zk), For(Id(XSV2), BooleanLit(True), StringLit(LcB), If((Id(qZPq), CallStmt(Id(Z3), [NumLit(54.6), StringLit(Jo), Id(ZG2)])), [(StringLit(m), CallStmt(Id(yU), [])), (StringLit(fIJGv), Break), (NumLit(71.92), VarDecl(Id(nsP2), ArrayType([20.58, 94.85, 7.94], NumberType), None, None)), (Id(xcRH), Break)], If((BooleanLit(True), Block([VarDecl(Id(pP), ArrayType([9.14], BoolType), None, BooleanLit(True)), Block([Continue, VarDecl(Id(lKE), ArrayType([32.59, 80.92, 92.8], StringType), None, None), AssignStmt(Id(VhGi), Id(lHf))])])), [(BooleanLit(False), Break), (Id(Gm7_), Break), (NumLit(71.9), VarDecl(Id(Yr8), StringType, None, None)), (StringLit(F), Break)], For(Id(H_D9), StringLit(GyI), NumLit(25.64), Block([]))))))))))))], None))), [], None)), CallStmt(Id(lE), [])])), FuncDecl(Id(yX), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115725))

	def test_21530115726(self):
		input = '''
bool Mr
'''
		expect = '''Program([VarDecl(Id(Mr), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115726))

	def test_21530115727(self):
		input = '''
func s_dY (string X2BJ[90.12,94.86])	return

'''
		expect = '''Program([FuncDecl(Id(s_dY), [VarDecl(Id(X2BJ), ArrayType([90.12, 94.86], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115727))

	def test_21530115728(self):
		input = '''
func udIx (number csx8, bool Vd)
	begin
		VPj("CDui")
		Dl[true, false, false] <- 36.3
		return
	end
'''
		expect = '''Program([FuncDecl(Id(udIx), [VarDecl(Id(csx8), NumberType, None, None), VarDecl(Id(Vd), BoolType, None, None)], Block([CallStmt(Id(VPj), [StringLit(CDui)]), AssignStmt(ArrayCell(Id(Dl), [BooleanLit(True), BooleanLit(False), BooleanLit(False)]), NumLit(36.3)), Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115728))

	def test_21530115729(self):
		input = '''
func MwCf (bool Awt, string mV[44.86,26.69], string aIix[40.56,30.97])	return
bool SBHQ[85.65]
'''
		expect = '''Program([FuncDecl(Id(MwCf), [VarDecl(Id(Awt), BoolType, None, None), VarDecl(Id(mV), ArrayType([44.86, 26.69], StringType), None, None), VarDecl(Id(aIix), ArrayType([40.56, 30.97], StringType), None, None)], Return()), VarDecl(Id(SBHQ), ArrayType([85.65], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115729))

	def test_21530115730(self):
		input = '''
func Uo (bool R2Ao, number Ty, bool yiO)
	return
func zj ()	return

dynamic Oe <- true
bool HKTi[18.08,0.05,36.45]
bool Wwu[63.88,57.91]
'''
		expect = '''Program([FuncDecl(Id(Uo), [VarDecl(Id(R2Ao), BoolType, None, None), VarDecl(Id(Ty), NumberType, None, None), VarDecl(Id(yiO), BoolType, None, None)], Return()), FuncDecl(Id(zj), [], Return()), VarDecl(Id(Oe), None, dynamic, BooleanLit(True)), VarDecl(Id(HKTi), ArrayType([18.08, 0.05, 36.45], BoolType), None, None), VarDecl(Id(Wwu), ArrayType([63.88, 57.91], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115730))

	def test_21530115731(self):
		input = '''
func Ka (string Qw5, string om6k[99.29])
	return

dynamic MU <- 4.93
func YgSw (bool AJ)
	begin
		number Q2[73.52,32.22] <- true
	end
'''
		expect = '''Program([FuncDecl(Id(Ka), [VarDecl(Id(Qw5), StringType, None, None), VarDecl(Id(om6k), ArrayType([99.29], StringType), None, None)], Return()), VarDecl(Id(MU), None, dynamic, NumLit(4.93)), FuncDecl(Id(YgSw), [VarDecl(Id(AJ), BoolType, None, None)], Block([VarDecl(Id(Q2), ArrayType([73.52, 32.22], NumberType), None, BooleanLit(True))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115731))

	def test_21530115732(self):
		input = '''
number w7[80.66,79.07] <- true
'''
		expect = '''Program([VarDecl(Id(w7), ArrayType([80.66, 79.07], NumberType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115732))

	def test_21530115733(self):
		input = '''
func Btz (number VS8[10.2], bool Rdi_[35.72])	return true
func uHV (bool HOn, string lss, bool VwY)	begin
	end
func Ie (number sFDu, number yrl, bool JcT5[43.18,13.71,76.41])
	return
string Jhl <- true
number v0Wn[48.68,61.5]
'''
		expect = '''Program([FuncDecl(Id(Btz), [VarDecl(Id(VS8), ArrayType([10.2], NumberType), None, None), VarDecl(Id(Rdi_), ArrayType([35.72], BoolType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(uHV), [VarDecl(Id(HOn), BoolType, None, None), VarDecl(Id(lss), StringType, None, None), VarDecl(Id(VwY), BoolType, None, None)], Block([])), FuncDecl(Id(Ie), [VarDecl(Id(sFDu), NumberType, None, None), VarDecl(Id(yrl), NumberType, None, None), VarDecl(Id(JcT5), ArrayType([43.18, 13.71, 76.41], BoolType), None, None)], Return()), VarDecl(Id(Jhl), StringType, None, BooleanLit(True)), VarDecl(Id(v0Wn), ArrayType([48.68, 61.5], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115733))

	def test_21530115734(self):
		input = '''
func NcD (string V0qi[57.49], number vZ)
	return K6s

func zx ()	begin
		for dT0 until 50.17 by 33.55
			string pPMs[25.16,82.93,9.6]
	end
func r1X5 (bool MNx7[35.27,25.41,83.23])	return 30.77

func pOAX ()
	return false

string TMi[29.27,60.02,20.53]
'''
		expect = '''Program([FuncDecl(Id(NcD), [VarDecl(Id(V0qi), ArrayType([57.49], StringType), None, None), VarDecl(Id(vZ), NumberType, None, None)], Return(Id(K6s))), FuncDecl(Id(zx), [], Block([For(Id(dT0), NumLit(50.17), NumLit(33.55), VarDecl(Id(pPMs), ArrayType([25.16, 82.93, 9.6], StringType), None, None))])), FuncDecl(Id(r1X5), [VarDecl(Id(MNx7), ArrayType([35.27, 25.41, 83.23], BoolType), None, None)], Return(NumLit(30.77))), FuncDecl(Id(pOAX), [], Return(BooleanLit(False))), VarDecl(Id(TMi), ArrayType([29.27, 60.02, 20.53], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115734))

	def test_21530115735(self):
		input = '''
func nQx (number LTo[89.89,53.69], string KXUC, string iU7)
	begin
		T2 <- "yORg"
		begin
		end
		return 9.05
	end

'''
		expect = '''Program([FuncDecl(Id(nQx), [VarDecl(Id(LTo), ArrayType([89.89, 53.69], NumberType), None, None), VarDecl(Id(KXUC), StringType, None, None), VarDecl(Id(iU7), StringType, None, None)], Block([AssignStmt(Id(T2), StringLit(yORg)), Block([]), Return(NumLit(9.05))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115735))

	def test_21530115736(self):
		input = '''
var jl <- LRK
func MzD (number EX)
	begin
	end

func TVL (number Yl[33.16])	return OJn_

bool s14W[31.1,85.65,67.87]
number pqDX <- 26.04
'''
		expect = '''Program([VarDecl(Id(jl), None, var, Id(LRK)), FuncDecl(Id(MzD), [VarDecl(Id(EX), NumberType, None, None)], Block([])), FuncDecl(Id(TVL), [VarDecl(Id(Yl), ArrayType([33.16], NumberType), None, None)], Return(Id(OJn_))), VarDecl(Id(s14W), ArrayType([31.1, 85.65, 67.87], BoolType), None, None), VarDecl(Id(pqDX), NumberType, None, NumLit(26.04))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115736))

	def test_21530115737(self):
		input = '''
bool gjkB
'''
		expect = '''Program([VarDecl(Id(gjkB), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115737))

	def test_21530115738(self):
		input = '''
number GX[18.06] <- true
func du (bool Hie, string uGN[46.55], number kXf)
	return
bool iNl[75.54] <- true
bool M5QK
'''
		expect = '''Program([VarDecl(Id(GX), ArrayType([18.06], NumberType), None, BooleanLit(True)), FuncDecl(Id(du), [VarDecl(Id(Hie), BoolType, None, None), VarDecl(Id(uGN), ArrayType([46.55], StringType), None, None), VarDecl(Id(kXf), NumberType, None, None)], Return()), VarDecl(Id(iNl), ArrayType([75.54], BoolType), None, BooleanLit(True)), VarDecl(Id(M5QK), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115738))

	def test_21530115739(self):
		input = '''
func qD (string JOk[4.19,1.31], string mp6, string RrL[66.69,93.21])	return WId4
func RtSR ()	begin
	end

func ncV (string ToD[24.61,28.2,95.34], bool b94Y[78.67], string tP70)
	return true
'''
		expect = '''Program([FuncDecl(Id(qD), [VarDecl(Id(JOk), ArrayType([4.19, 1.31], StringType), None, None), VarDecl(Id(mp6), StringType, None, None), VarDecl(Id(RrL), ArrayType([66.69, 93.21], StringType), None, None)], Return(Id(WId4))), FuncDecl(Id(RtSR), [], Block([])), FuncDecl(Id(ncV), [VarDecl(Id(ToD), ArrayType([24.61, 28.2, 95.34], StringType), None, None), VarDecl(Id(b94Y), ArrayType([78.67], BoolType), None, None), VarDecl(Id(tP70), StringType, None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115739))

	def test_21530115740(self):
		input = '''
func J8E (number Li, string Bd, string pD[64.72])
	return 64.78
string mQ[42.29,42.52,27.29]
'''
		expect = '''Program([FuncDecl(Id(J8E), [VarDecl(Id(Li), NumberType, None, None), VarDecl(Id(Bd), StringType, None, None), VarDecl(Id(pD), ArrayType([64.72], StringType), None, None)], Return(NumLit(64.78))), VarDecl(Id(mQ), ArrayType([42.29, 42.52, 27.29], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115740))

	def test_21530115741(self):
		input = '''
func WGf ()	begin
		for YW6Q until Rlp by 65.43
			if (false) kI()
			elif ("u")
			GF04[false, Jj] <- yeC
			elif (false)
			flK[OCR] <- RBa
		continue
	end

func vLRr ()
	return lR
string VZ
'''
		expect = '''Program([FuncDecl(Id(WGf), [], Block([For(Id(YW6Q), Id(Rlp), NumLit(65.43), If((BooleanLit(False), CallStmt(Id(kI), [])), [(StringLit(u), AssignStmt(ArrayCell(Id(GF04), [BooleanLit(False), Id(Jj)]), Id(yeC))), (BooleanLit(False), AssignStmt(ArrayCell(Id(flK), [Id(OCR)]), Id(RBa)))], None)), Continue])), FuncDecl(Id(vLRr), [], Return(Id(lR))), VarDecl(Id(VZ), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115741))

	def test_21530115742(self):
		input = '''
func jL (number Eri)
	begin
		continue
		return H2
	end
bool uYXN
func rjE (string kPZ[80.27])
	begin
		DdtM <- 55.79
	end

func X5Ti ()
	return
'''
		expect = '''Program([FuncDecl(Id(jL), [VarDecl(Id(Eri), NumberType, None, None)], Block([Continue, Return(Id(H2))])), VarDecl(Id(uYXN), BoolType, None, None), FuncDecl(Id(rjE), [VarDecl(Id(kPZ), ArrayType([80.27], StringType), None, None)], Block([AssignStmt(Id(DdtM), NumLit(55.79))])), FuncDecl(Id(X5Ti), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115742))

	def test_21530115743(self):
		input = '''
var QaYs <- 38.23
func tjU (number dWc[97.24], number KG8J, string RBv)
	begin
	end
func eH9 (bool Mko[57.01,69.66,98.41], number rlQ5, string TUHU)
	return
'''
		expect = '''Program([VarDecl(Id(QaYs), None, var, NumLit(38.23)), FuncDecl(Id(tjU), [VarDecl(Id(dWc), ArrayType([97.24], NumberType), None, None), VarDecl(Id(KG8J), NumberType, None, None), VarDecl(Id(RBv), StringType, None, None)], Block([])), FuncDecl(Id(eH9), [VarDecl(Id(Mko), ArrayType([57.01, 69.66, 98.41], BoolType), None, None), VarDecl(Id(rlQ5), NumberType, None, None), VarDecl(Id(TUHU), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115743))

	def test_21530115744(self):
		input = '''
number zwpZ
bool wS5c <- false
number qBX[55.23,31.23,49.74]
'''
		expect = '''Program([VarDecl(Id(zwpZ), NumberType, None, None), VarDecl(Id(wS5c), BoolType, None, BooleanLit(False)), VarDecl(Id(qBX), ArrayType([55.23, 31.23, 49.74], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115744))

	def test_21530115745(self):
		input = '''
bool b5qN[56.82,32.41,66.79]
var K63 <- 32.7
number Bmz[8.68,99.62,9.99]
bool dc0 <- true
bool Dg
'''
		expect = '''Program([VarDecl(Id(b5qN), ArrayType([56.82, 32.41, 66.79], BoolType), None, None), VarDecl(Id(K63), None, var, NumLit(32.7)), VarDecl(Id(Bmz), ArrayType([8.68, 99.62, 9.99], NumberType), None, None), VarDecl(Id(dc0), BoolType, None, BooleanLit(True)), VarDecl(Id(Dg), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115745))

	def test_21530115746(self):
		input = '''
func ue (bool v5x, bool toge)
	begin
		break
	end

number v4[51.74,28.03,46.11]
func tCNu (number z0m[17.42], bool jt, bool Ck)	return
func w5o ()	return bYIv
'''
		expect = '''Program([FuncDecl(Id(ue), [VarDecl(Id(v5x), BoolType, None, None), VarDecl(Id(toge), BoolType, None, None)], Block([Break])), VarDecl(Id(v4), ArrayType([51.74, 28.03, 46.11], NumberType), None, None), FuncDecl(Id(tCNu), [VarDecl(Id(z0m), ArrayType([17.42], NumberType), None, None), VarDecl(Id(jt), BoolType, None, None), VarDecl(Id(Ck), BoolType, None, None)], Return()), FuncDecl(Id(w5o), [], Return(Id(bYIv)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115746))

	def test_21530115747(self):
		input = '''
func dwQ (bool qb)
	begin
		string Swx <- TD
		bool Fb <- false
		break
	end

number Aqd <- Nn6F
'''
		expect = '''Program([FuncDecl(Id(dwQ), [VarDecl(Id(qb), BoolType, None, None)], Block([VarDecl(Id(Swx), StringType, None, Id(TD)), VarDecl(Id(Fb), BoolType, None, BooleanLit(False)), Break])), VarDecl(Id(Aqd), NumberType, None, Id(Nn6F))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115747))

	def test_21530115748(self):
		input = '''
func Y7 ()	begin
		Wk("kKnna", 73.39, false)
	end
'''
		expect = '''Program([FuncDecl(Id(Y7), [], Block([CallStmt(Id(Wk), [StringLit(kKnna), NumLit(73.39), BooleanLit(False)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115748))

	def test_21530115749(self):
		input = '''
var P3PC <- true
'''
		expect = '''Program([VarDecl(Id(P3PC), None, var, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115749))

	def test_21530115750(self):
		input = '''
func hxcM (number gTh[6.38,41.37,6.43], string CyEn[91.47], number Cx[3.63,80.02])	return "aVFg"

string vb[71.32,99.22,31.26] <- false
'''
		expect = '''Program([FuncDecl(Id(hxcM), [VarDecl(Id(gTh), ArrayType([6.38, 41.37, 6.43], NumberType), None, None), VarDecl(Id(CyEn), ArrayType([91.47], StringType), None, None), VarDecl(Id(Cx), ArrayType([3.63, 80.02], NumberType), None, None)], Return(StringLit(aVFg))), VarDecl(Id(vb), ArrayType([71.32, 99.22, 31.26], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115750))

	def test_21530115751(self):
		input = '''
func bUh ()	return jl5
string CHTt[57.81]
func Lsxq ()	return Q_JR
func Bi ()
	begin
		return "LEfha"
	end
func wNp6 (string svV, string kN, number ubkk)
	return

'''
		expect = '''Program([FuncDecl(Id(bUh), [], Return(Id(jl5))), VarDecl(Id(CHTt), ArrayType([57.81], StringType), None, None), FuncDecl(Id(Lsxq), [], Return(Id(Q_JR))), FuncDecl(Id(Bi), [], Block([Return(StringLit(LEfha))])), FuncDecl(Id(wNp6), [VarDecl(Id(svV), StringType, None, None), VarDecl(Id(kN), StringType, None, None), VarDecl(Id(ubkk), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115751))

	def test_21530115752(self):
		input = '''
string lh[8.93,18.36,99.65] <- false
func zf (bool Rl[57.35,67.5], string za, bool FV[56.36])
	return
func aCF (string YRyJ, bool GP[22.81,89.12], string FOvk[76.34,60.25])
	return false
func hLS0 ()
	begin
		for OE until true by Fw
			for osK until 81.97 by true
				string QXcD
		continue
	end

'''
		expect = '''Program([VarDecl(Id(lh), ArrayType([8.93, 18.36, 99.65], StringType), None, BooleanLit(False)), FuncDecl(Id(zf), [VarDecl(Id(Rl), ArrayType([57.35, 67.5], BoolType), None, None), VarDecl(Id(za), StringType, None, None), VarDecl(Id(FV), ArrayType([56.36], BoolType), None, None)], Return()), FuncDecl(Id(aCF), [VarDecl(Id(YRyJ), StringType, None, None), VarDecl(Id(GP), ArrayType([22.81, 89.12], BoolType), None, None), VarDecl(Id(FOvk), ArrayType([76.34, 60.25], StringType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(hLS0), [], Block([For(Id(OE), BooleanLit(True), Id(Fw), For(Id(osK), NumLit(81.97), BooleanLit(True), VarDecl(Id(QXcD), StringType, None, None))), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115752))

	def test_21530115753(self):
		input = '''
func EvOz ()	begin
		return true
		break
		break
	end
'''
		expect = '''Program([FuncDecl(Id(EvOz), [], Block([Return(BooleanLit(True)), Break, Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115753))

	def test_21530115754(self):
		input = '''
number pAa[39.92]
func sfC2 (number R9TZ[39.63,60.38], number bv5[2.64,47.42,13.6], string vo)
	begin
		return "A"
	end

func WwL (string TWaQ, bool vuH[12.13], string Wj[38.82])	return
string JPIl <- false
string Li[85.01,32.22,81.03]
'''
		expect = '''Program([VarDecl(Id(pAa), ArrayType([39.92], NumberType), None, None), FuncDecl(Id(sfC2), [VarDecl(Id(R9TZ), ArrayType([39.63, 60.38], NumberType), None, None), VarDecl(Id(bv5), ArrayType([2.64, 47.42, 13.6], NumberType), None, None), VarDecl(Id(vo), StringType, None, None)], Block([Return(StringLit(A))])), FuncDecl(Id(WwL), [VarDecl(Id(TWaQ), StringType, None, None), VarDecl(Id(vuH), ArrayType([12.13], BoolType), None, None), VarDecl(Id(Wj), ArrayType([38.82], StringType), None, None)], Return()), VarDecl(Id(JPIl), StringType, None, BooleanLit(False)), VarDecl(Id(Li), ArrayType([85.01, 32.22, 81.03], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115754))

	def test_21530115755(self):
		input = '''
string v7[14.18]
bool D60C[15.96,30.65] <- qzV_
func Bzr ()	return true

func G5F (string Anon[68.36], string H_6z[34.8,73.58])	begin
		begin
		end
		Bc <- p9
	end

'''
		expect = '''Program([VarDecl(Id(v7), ArrayType([14.18], StringType), None, None), VarDecl(Id(D60C), ArrayType([15.96, 30.65], BoolType), None, Id(qzV_)), FuncDecl(Id(Bzr), [], Return(BooleanLit(True))), FuncDecl(Id(G5F), [VarDecl(Id(Anon), ArrayType([68.36], StringType), None, None), VarDecl(Id(H_6z), ArrayType([34.8, 73.58], StringType), None, None)], Block([Block([]), AssignStmt(Id(Bc), Id(p9))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115755))

	def test_21530115756(self):
		input = '''
number kW[97.23,94.2,57.94]
'''
		expect = '''Program([VarDecl(Id(kW), ArrayType([97.23, 94.2, 57.94], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115756))

	def test_21530115757(self):
		input = '''
func PRud ()
	return 26.83

bool Dd
string fETh
string hA <- false
'''
		expect = '''Program([FuncDecl(Id(PRud), [], Return(NumLit(26.83))), VarDecl(Id(Dd), BoolType, None, None), VarDecl(Id(fETh), StringType, None, None), VarDecl(Id(hA), StringType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115757))

	def test_21530115758(self):
		input = '''
var UO1 <- y2
dynamic L3
func j06H ()	return

'''
		expect = '''Program([VarDecl(Id(UO1), None, var, Id(y2)), VarDecl(Id(L3), None, dynamic, None), FuncDecl(Id(j06H), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115758))

	def test_21530115759(self):
		input = '''
func p61l ()
	return

bool fa <- false
'''
		expect = '''Program([FuncDecl(Id(p61l), [], Return()), VarDecl(Id(fa), BoolType, None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115759))

	def test_21530115760(self):
		input = '''
number T7I
func TD ()
	begin
		bool BQQ[49.39,49.18,47.47]
	end

func A6 (string Js4[42.86,26.27], string tAc5, bool JIUz)	return "rWe"

func gv62 (number jF[43.95,94.89,58.56], number x6[37.74,94.46,44.79])
	return false

number rSMW
'''
		expect = '''Program([VarDecl(Id(T7I), NumberType, None, None), FuncDecl(Id(TD), [], Block([VarDecl(Id(BQQ), ArrayType([49.39, 49.18, 47.47], BoolType), None, None)])), FuncDecl(Id(A6), [VarDecl(Id(Js4), ArrayType([42.86, 26.27], StringType), None, None), VarDecl(Id(tAc5), StringType, None, None), VarDecl(Id(JIUz), BoolType, None, None)], Return(StringLit(rWe))), FuncDecl(Id(gv62), [VarDecl(Id(jF), ArrayType([43.95, 94.89, 58.56], NumberType), None, None), VarDecl(Id(x6), ArrayType([37.74, 94.46, 44.79], NumberType), None, None)], Return(BooleanLit(False))), VarDecl(Id(rSMW), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115760))

	def test_21530115761(self):
		input = '''
string dg[41.46]
func XVb0 (bool vN[82.98,4.81,24.16])
	return
'''
		expect = '''Program([VarDecl(Id(dg), ArrayType([41.46], StringType), None, None), FuncDecl(Id(XVb0), [VarDecl(Id(vN), ArrayType([82.98, 4.81, 24.16], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115761))

	def test_21530115762(self):
		input = '''
func N64i ()	return 8.26
func YBlB (bool gT[78.74], string fx[93.01,59.8])
	return

var AZ <- jPTf
func ECb (string vaqQ[97.33], string RPkp, bool JC[57.19,7.07])	begin
		ZOF[QSj, pthE] <- "Arp"
		if (yQYv)
		for k5Ao until 17.48 by "Nx"
			Uv(pw6n, 29.57, aMIL)
		elif (A59) begin
			for lVc until "rM" by "ydxpW"
				SJh0[7.54, 89.56, false] <- etsN
		end
		elif (Gcrr)
		for Uqe until "Wj" by 2.99
			break
		else for b3 until "kckoL" by 93.72
			iHjp <- 4.56
		begin
		end
	end
func YEn (string VUZe[14.16], number Yg)
	return Zj10
'''
		expect = '''Program([FuncDecl(Id(N64i), [], Return(NumLit(8.26))), FuncDecl(Id(YBlB), [VarDecl(Id(gT), ArrayType([78.74], BoolType), None, None), VarDecl(Id(fx), ArrayType([93.01, 59.8], StringType), None, None)], Return()), VarDecl(Id(AZ), None, var, Id(jPTf)), FuncDecl(Id(ECb), [VarDecl(Id(vaqQ), ArrayType([97.33], StringType), None, None), VarDecl(Id(RPkp), StringType, None, None), VarDecl(Id(JC), ArrayType([57.19, 7.07], BoolType), None, None)], Block([AssignStmt(ArrayCell(Id(ZOF), [Id(QSj), Id(pthE)]), StringLit(Arp)), If((Id(yQYv), For(Id(k5Ao), NumLit(17.48), StringLit(Nx), CallStmt(Id(Uv), [Id(pw6n), NumLit(29.57), Id(aMIL)]))), [(Id(A59), Block([For(Id(lVc), StringLit(rM), StringLit(ydxpW), AssignStmt(ArrayCell(Id(SJh0), [NumLit(7.54), NumLit(89.56), BooleanLit(False)]), Id(etsN)))])), (Id(Gcrr), For(Id(Uqe), StringLit(Wj), NumLit(2.99), Break))], For(Id(b3), StringLit(kckoL), NumLit(93.72), AssignStmt(Id(iHjp), NumLit(4.56)))), Block([])])), FuncDecl(Id(YEn), [VarDecl(Id(VUZe), ArrayType([14.16], StringType), None, None), VarDecl(Id(Yg), NumberType, None, None)], Return(Id(Zj10)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115762))

	def test_21530115763(self):
		input = '''
func snh (bool IiL[80.87])	return "illdj"
func BI (bool Q3[79.85], string YrY)
	return
var S9 <- true
func BoJ (number TC, number zOZ)
	return

bool K9s[18.77] <- "vqcr"
'''
		expect = '''Program([FuncDecl(Id(snh), [VarDecl(Id(IiL), ArrayType([80.87], BoolType), None, None)], Return(StringLit(illdj))), FuncDecl(Id(BI), [VarDecl(Id(Q3), ArrayType([79.85], BoolType), None, None), VarDecl(Id(YrY), StringType, None, None)], Return()), VarDecl(Id(S9), None, var, BooleanLit(True)), FuncDecl(Id(BoJ), [VarDecl(Id(TC), NumberType, None, None), VarDecl(Id(zOZ), NumberType, None, None)], Return()), VarDecl(Id(K9s), ArrayType([18.77], BoolType), None, StringLit(vqcr))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115763))

	def test_21530115764(self):
		input = '''
func NGo2 (string foX[81.82], string A3n[77.02], string h41[49.59])
	return
'''
		expect = '''Program([FuncDecl(Id(NGo2), [VarDecl(Id(foX), ArrayType([81.82], StringType), None, None), VarDecl(Id(A3n), ArrayType([77.02], StringType), None, None), VarDecl(Id(h41), ArrayType([49.59], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115764))

	def test_21530115765(self):
		input = '''
number aku[79.65,46.99,60.19] <- false
func qtC7 (string ew[13.97,33.64], number Aokq, bool Ou7n[73.42,21.77,16.23])
	return "JS"

string OK[28.7,52.11,2.12]
'''
		expect = '''Program([VarDecl(Id(aku), ArrayType([79.65, 46.99, 60.19], NumberType), None, BooleanLit(False)), FuncDecl(Id(qtC7), [VarDecl(Id(ew), ArrayType([13.97, 33.64], StringType), None, None), VarDecl(Id(Aokq), NumberType, None, None), VarDecl(Id(Ou7n), ArrayType([73.42, 21.77, 16.23], BoolType), None, None)], Return(StringLit(JS))), VarDecl(Id(OK), ArrayType([28.7, 52.11, 2.12], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115765))

	def test_21530115766(self):
		input = '''
string Wt
bool Csh_[87.38] <- 36.24
dynamic xQES
number pmpY[81.43,22.92] <- 78.37
'''
		expect = '''Program([VarDecl(Id(Wt), StringType, None, None), VarDecl(Id(Csh_), ArrayType([87.38], BoolType), None, NumLit(36.24)), VarDecl(Id(xQES), None, dynamic, None), VarDecl(Id(pmpY), ArrayType([81.43, 22.92], NumberType), None, NumLit(78.37))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115766))

	def test_21530115767(self):
		input = '''
bool i5u[44.77,16.62,97.5] <- true
string p4[65.42,14.31,78.47]
'''
		expect = '''Program([VarDecl(Id(i5u), ArrayType([44.77, 16.62, 97.5], BoolType), None, BooleanLit(True)), VarDecl(Id(p4), ArrayType([65.42, 14.31, 78.47], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115767))

	def test_21530115768(self):
		input = '''
bool ucu
string uXn <- "aC"
'''
		expect = '''Program([VarDecl(Id(ucu), BoolType, None, None), VarDecl(Id(uXn), StringType, None, StringLit(aC))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115768))

	def test_21530115769(self):
		input = '''
func TYv (string eG[83.91,17.62], string IpDJ[79.88,25.09])	return 56.71
func yLMB (bool Pw, string A2HX[26.5,28.28,88.5], bool yFr[61.39,42.63])
	begin
		if ("ojG")
		break
		elif ("ANDR") continue
		elif (csvM)
		Fu7[24.69, 44.22, "aVG"] <- true
		elif ("FIMA") number hRV[91.65]
		elif ("gESy")
		for Xd until 43.64 by true
			continue
		elif (69.18)
		return
		else string FNvr[32.44]
		break
		number zBA4[17.23]
	end
'''
		expect = '''Program([FuncDecl(Id(TYv), [VarDecl(Id(eG), ArrayType([83.91, 17.62], StringType), None, None), VarDecl(Id(IpDJ), ArrayType([79.88, 25.09], StringType), None, None)], Return(NumLit(56.71))), FuncDecl(Id(yLMB), [VarDecl(Id(Pw), BoolType, None, None), VarDecl(Id(A2HX), ArrayType([26.5, 28.28, 88.5], StringType), None, None), VarDecl(Id(yFr), ArrayType([61.39, 42.63], BoolType), None, None)], Block([If((StringLit(ojG), Break), [(StringLit(ANDR), Continue), (Id(csvM), AssignStmt(ArrayCell(Id(Fu7), [NumLit(24.69), NumLit(44.22), StringLit(aVG)]), BooleanLit(True))), (StringLit(FIMA), VarDecl(Id(hRV), ArrayType([91.65], NumberType), None, None)), (StringLit(gESy), For(Id(Xd), NumLit(43.64), BooleanLit(True), Continue)), (NumLit(69.18), Return())], VarDecl(Id(FNvr), ArrayType([32.44], StringType), None, None)), Break, VarDecl(Id(zBA4), ArrayType([17.23], NumberType), None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115769))

	def test_21530115770(self):
		input = '''
string nZJC
func X6q ()	return

func qEXC (string ykhe[97.9,83.61])
	begin
	end

string OQjp
func vYg (string lX2[15.54,2.47], string jO, number PtU[15.69])	return

'''
		expect = '''Program([VarDecl(Id(nZJC), StringType, None, None), FuncDecl(Id(X6q), [], Return()), FuncDecl(Id(qEXC), [VarDecl(Id(ykhe), ArrayType([97.9, 83.61], StringType), None, None)], Block([])), VarDecl(Id(OQjp), StringType, None, None), FuncDecl(Id(vYg), [VarDecl(Id(lX2), ArrayType([15.54, 2.47], StringType), None, None), VarDecl(Id(jO), StringType, None, None), VarDecl(Id(PtU), ArrayType([15.69], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115770))

	def test_21530115771(self):
		input = '''
func Jx (number ONur[85.19], string yD[23.02,44.59,89.16])	begin
		fpaE(IHv, snUi)
		continue
	end
'''
		expect = '''Program([FuncDecl(Id(Jx), [VarDecl(Id(ONur), ArrayType([85.19], NumberType), None, None), VarDecl(Id(yD), ArrayType([23.02, 44.59, 89.16], StringType), None, None)], Block([CallStmt(Id(fpaE), [Id(IHv), Id(snUi)]), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115771))

	def test_21530115772(self):
		input = '''
number FJQl[41.78,8.85]
string uAlF <- "xG"
func DK (string Qs, bool QZ[76.98])
	return true
bool Zfo[63.66,63.77]
'''
		expect = '''Program([VarDecl(Id(FJQl), ArrayType([41.78, 8.85], NumberType), None, None), VarDecl(Id(uAlF), StringType, None, StringLit(xG)), FuncDecl(Id(DK), [VarDecl(Id(Qs), StringType, None, None), VarDecl(Id(QZ), ArrayType([76.98], BoolType), None, None)], Return(BooleanLit(True))), VarDecl(Id(Zfo), ArrayType([63.66, 63.77], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115772))

	def test_21530115773(self):
		input = '''
bool MkRF <- false
func KN (string g3x[49.65,80.07,78.16])
	return

dynamic E2 <- false
func qf ()
	return

'''
		expect = '''Program([VarDecl(Id(MkRF), BoolType, None, BooleanLit(False)), FuncDecl(Id(KN), [VarDecl(Id(g3x), ArrayType([49.65, 80.07, 78.16], StringType), None, None)], Return()), VarDecl(Id(E2), None, dynamic, BooleanLit(False)), FuncDecl(Id(qf), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115773))

	def test_21530115774(self):
		input = '''
func S_ (bool PuvM)
	return "NXi"

func FaK ()
	begin
		continue
	end

string xZxa[78.68,29.32,76.15] <- "oHue"
dynamic pp0
dynamic rn <- 10.73
'''
		expect = '''Program([FuncDecl(Id(S_), [VarDecl(Id(PuvM), BoolType, None, None)], Return(StringLit(NXi))), FuncDecl(Id(FaK), [], Block([Continue])), VarDecl(Id(xZxa), ArrayType([78.68, 29.32, 76.15], StringType), None, StringLit(oHue)), VarDecl(Id(pp0), None, dynamic, None), VarDecl(Id(rn), None, dynamic, NumLit(10.73))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115774))

	def test_21530115775(self):
		input = '''
number Oz[46.96,11.13] <- 10.42
var Cj <- false
func TTUN (number fsh1[62.61,70.16,11.72])	begin
		continue
		bool o4
	end
'''
		expect = '''Program([VarDecl(Id(Oz), ArrayType([46.96, 11.13], NumberType), None, NumLit(10.42)), VarDecl(Id(Cj), None, var, BooleanLit(False)), FuncDecl(Id(TTUN), [VarDecl(Id(fsh1), ArrayType([62.61, 70.16, 11.72], NumberType), None, None)], Block([Continue, VarDecl(Id(o4), BoolType, None, None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115775))

	def test_21530115776(self):
		input = '''
func E4 ()	return

func FAS (string Zo, bool Tdk9)
	return

number KW
'''
		expect = '''Program([FuncDecl(Id(E4), [], Return()), FuncDecl(Id(FAS), [VarDecl(Id(Zo), StringType, None, None), VarDecl(Id(Tdk9), BoolType, None, None)], Return()), VarDecl(Id(KW), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115776))

	def test_21530115777(self):
		input = '''
func JG (number RM, number LpW[76.51,84.73,85.68])
	return

func tGnk (bool SCr9)
	begin
		if (tE) begin
			begin
				if ("tiEm") UEiP[22.17] <- "dXt"
				elif (12.92) for RQp until Se by true
					if (false) number sX <- false
					elif ("CYqUm") sB[pumC, k5g] <- true
					elif (60.86)
					for LQA until 10.5 by "MQWyn"
						yPA[55.46] <- 7.05
				elif (71.92)
				if (25.47) for Rs9T until 45.0 by true
					bool gu9 <- 41.31
				elif (ehW)
				sv <- IEsM
				elif (e37O)
				if ("hg")
				continue
				elif (cdg)
				continue
				elif (false) if (fCRv) string Pz9V
				elif ("Cdn")
				if ("Sxry")
				if (KLF7)
				continue
				elif ("o")
				for v0Y until 81.48 by 47.32
					begin
						if (qt)
						for bOcf until 29.4 by false
							PaGu[true, false, "rdo"] <- mq65
						elif (92.96) return SE
						elif (Ri) U19o("WwP", "GKS")
						elif (false)
						continue
						elif (sWJp) if (79.38) return true
						elif (n4)
						for RtL until false by 11.43
							continue
						elif (wmP) continue
						elif (true)
						for lC72 until "IHX" by "Ph"
							return
						elif (false) number QgAK[30.03,51.86,34.2]
						number ue5[42.36] <- false
					end
				elif ("hIBrH")
				YdK6(CIR1)
				else for uyXF until U7A_ by LtW
					string nT[99.51,2.8,61.24]
				elif ("yZIv") continue
				elif ("yaA") return
				elif ("lcR") WIFn("u", true, "i")
				elif (11.31)
				if (true) for SU4 until 46.38 by "gMSqc"
					continue
				elif ("i")
				if (Rm) for Qt until "KskLf" by "BEW"
					Fs7 <- "TCtq"
				elif (1.58) begin
					for Qj until iCut by false
						return
					for tqhV until HtMx by true
						return
				end
				elif (VsOo)
				for pLY until "pYN" by bJ_
					dynamic T2
				else bool H0Ex <- C6cu
				elif ("LghL")
				number qy <- vu
				else begin
					var asPB <- false
				end
				elif (2.71)
				for LQU0 until "y" by "GivqX"
					if (Z3iz) UPKu <- 16.62
					elif (Wq)
					string Ch
				elif ("e")
				jBRs[93.01, 37.94, "eCTax"] <- "xy"
				elif (xmh) if ("YJPZQ") nEoI("c", true, "WKS")
				elif (44.54)
				dynamic TrVZ
				elif (52.66) for EFR until false by "wKMN"
					number xex[5.39,83.85]
				else return "iTPKx"
				elif ("y")
				number rEV[93.99,8.36] <- false
				else continue
				NI["FK"] <- "BsK"
			end
			begin
				for dP until "Cn" by 78.94
					M5JQ[XWR, 96.55] <- 18.28
			end
		end
		elif ("SRne") for YAbl until "H" by 42.61
			wW3 <- vYy
		elif ("UeIl") jn7K(29.95, 68.45, 7.38)
		elif (vA) break
		else bool n4q[9.69] <- o5g
		return
		return
	end

number bR[51.44] <- false
string pA2
'''
		expect = '''Program([FuncDecl(Id(JG), [VarDecl(Id(RM), NumberType, None, None), VarDecl(Id(LpW), ArrayType([76.51, 84.73, 85.68], NumberType), None, None)], Return()), FuncDecl(Id(tGnk), [VarDecl(Id(SCr9), BoolType, None, None)], Block([If((Id(tE), Block([Block([If((StringLit(tiEm), AssignStmt(ArrayCell(Id(UEiP), [NumLit(22.17)]), StringLit(dXt))), [(NumLit(12.92), For(Id(RQp), Id(Se), BooleanLit(True), If((BooleanLit(False), VarDecl(Id(sX), NumberType, None, BooleanLit(False))), [(StringLit(CYqUm), AssignStmt(ArrayCell(Id(sB), [Id(pumC), Id(k5g)]), BooleanLit(True))), (NumLit(60.86), For(Id(LQA), NumLit(10.5), StringLit(MQWyn), AssignStmt(ArrayCell(Id(yPA), [NumLit(55.46)]), NumLit(7.05)))), (NumLit(71.92), If((NumLit(25.47), For(Id(Rs9T), NumLit(45.0), BooleanLit(True), VarDecl(Id(gu9), BoolType, None, NumLit(41.31)))), [(Id(ehW), AssignStmt(Id(sv), Id(IEsM))), (Id(e37O), If((StringLit(hg), Continue), [(Id(cdg), Continue), (BooleanLit(False), If((Id(fCRv), VarDecl(Id(Pz9V), StringType, None, None)), [(StringLit(Cdn), If((StringLit(Sxry), If((Id(KLF7), Continue), [(StringLit(o), For(Id(v0Y), NumLit(81.48), NumLit(47.32), Block([If((Id(qt), For(Id(bOcf), NumLit(29.4), BooleanLit(False), AssignStmt(ArrayCell(Id(PaGu), [BooleanLit(True), BooleanLit(False), StringLit(rdo)]), Id(mq65)))), [(NumLit(92.96), Return(Id(SE))), (Id(Ri), CallStmt(Id(U19o), [StringLit(WwP), StringLit(GKS)])), (BooleanLit(False), Continue), (Id(sWJp), If((NumLit(79.38), Return(BooleanLit(True))), [(Id(n4), For(Id(RtL), BooleanLit(False), NumLit(11.43), Continue)), (Id(wmP), Continue), (BooleanLit(True), For(Id(lC72), StringLit(IHX), StringLit(Ph), Return())), (BooleanLit(False), VarDecl(Id(QgAK), ArrayType([30.03, 51.86, 34.2], NumberType), None, None))], None))], None), VarDecl(Id(ue5), ArrayType([42.36], NumberType), None, BooleanLit(False))]))), (StringLit(hIBrH), CallStmt(Id(YdK6), [Id(CIR1)]))], For(Id(uyXF), Id(U7A_), Id(LtW), VarDecl(Id(nT), ArrayType([99.51, 2.8, 61.24], StringType), None, None)))), [(StringLit(yZIv), Continue), (StringLit(yaA), Return()), (StringLit(lcR), CallStmt(Id(WIFn), [StringLit(u), BooleanLit(True), StringLit(i)])), (NumLit(11.31), If((BooleanLit(True), For(Id(SU4), NumLit(46.38), StringLit(gMSqc), Continue)), [(StringLit(i), If((Id(Rm), For(Id(Qt), StringLit(KskLf), StringLit(BEW), AssignStmt(Id(Fs7), StringLit(TCtq)))), [(NumLit(1.58), Block([For(Id(Qj), Id(iCut), BooleanLit(False), Return()), For(Id(tqhV), Id(HtMx), BooleanLit(True), Return())])), (Id(VsOo), For(Id(pLY), StringLit(pYN), Id(bJ_), VarDecl(Id(T2), None, dynamic, None)))], VarDecl(Id(H0Ex), BoolType, None, Id(C6cu)))), (StringLit(LghL), VarDecl(Id(qy), NumberType, None, Id(vu)))], Block([VarDecl(Id(asPB), None, var, BooleanLit(False))]))), (NumLit(2.71), For(Id(LQU0), StringLit(y), StringLit(GivqX), If((Id(Z3iz), AssignStmt(Id(UPKu), NumLit(16.62))), [(Id(Wq), VarDecl(Id(Ch), StringType, None, None)), (StringLit(e), AssignStmt(ArrayCell(Id(jBRs), [NumLit(93.01), NumLit(37.94), StringLit(eCTax)]), StringLit(xy))), (Id(xmh), If((StringLit(YJPZQ), CallStmt(Id(nEoI), [StringLit(c), BooleanLit(True), StringLit(WKS)])), [(NumLit(44.54), VarDecl(Id(TrVZ), None, dynamic, None)), (NumLit(52.66), For(Id(EFR), BooleanLit(False), StringLit(wKMN), VarDecl(Id(xex), ArrayType([5.39, 83.85], NumberType), None, None)))], Return(StringLit(iTPKx)))), (StringLit(y), VarDecl(Id(rEV), ArrayType([93.99, 8.36], NumberType), None, BooleanLit(False)))], Continue)))], None))], None))], None))], None))], None)))], None), AssignStmt(ArrayCell(Id(NI), [StringLit(FK)]), StringLit(BsK))]), Block([For(Id(dP), StringLit(Cn), NumLit(78.94), AssignStmt(ArrayCell(Id(M5JQ), [Id(XWR), NumLit(96.55)]), NumLit(18.28)))])])), [(StringLit(SRne), For(Id(YAbl), StringLit(H), NumLit(42.61), AssignStmt(Id(wW3), Id(vYy)))), (StringLit(UeIl), CallStmt(Id(jn7K), [NumLit(29.95), NumLit(68.45), NumLit(7.38)])), (Id(vA), Break)], VarDecl(Id(n4q), ArrayType([9.69], BoolType), None, Id(o5g))), Return(), Return()])), VarDecl(Id(bR), ArrayType([51.44], NumberType), None, BooleanLit(False)), VarDecl(Id(pA2), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115777))

	def test_21530115778(self):
		input = '''
number JF[2.44] <- A3k
string jAFI
dynamic RXKg
func U6Oz ()	return
'''
		expect = '''Program([VarDecl(Id(JF), ArrayType([2.44], NumberType), None, Id(A3k)), VarDecl(Id(jAFI), StringType, None, None), VarDecl(Id(RXKg), None, dynamic, None), FuncDecl(Id(U6Oz), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115778))

	def test_21530115779(self):
		input = '''
func mNVj (bool LX, number kT[89.89], string Kl[45.0])
	begin
		continue
		continue
		qO()
	end

func QfL (bool qXl[80.71], number C2q[85.51,92.85], bool TuV[58.07])	begin
		SVM("JsVpf", 45.42)
		uzt()
	end
func E6 (string KM[72.6], number gI[99.31,25.75,69.61], string Hn[66.9,96.98])
	begin
		return true
	end

func ncdq (string L0N[44.54,79.87,21.1])	return true

'''
		expect = '''Program([FuncDecl(Id(mNVj), [VarDecl(Id(LX), BoolType, None, None), VarDecl(Id(kT), ArrayType([89.89], NumberType), None, None), VarDecl(Id(Kl), ArrayType([45.0], StringType), None, None)], Block([Continue, Continue, CallStmt(Id(qO), [])])), FuncDecl(Id(QfL), [VarDecl(Id(qXl), ArrayType([80.71], BoolType), None, None), VarDecl(Id(C2q), ArrayType([85.51, 92.85], NumberType), None, None), VarDecl(Id(TuV), ArrayType([58.07], BoolType), None, None)], Block([CallStmt(Id(SVM), [StringLit(JsVpf), NumLit(45.42)]), CallStmt(Id(uzt), [])])), FuncDecl(Id(E6), [VarDecl(Id(KM), ArrayType([72.6], StringType), None, None), VarDecl(Id(gI), ArrayType([99.31, 25.75, 69.61], NumberType), None, None), VarDecl(Id(Hn), ArrayType([66.9, 96.98], StringType), None, None)], Block([Return(BooleanLit(True))])), FuncDecl(Id(ncdq), [VarDecl(Id(L0N), ArrayType([44.54, 79.87, 21.1], StringType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115779))

	def test_21530115780(self):
		input = '''
number Y7[68.5,26.03]
'''
		expect = '''Program([VarDecl(Id(Y7), ArrayType([68.5, 26.03], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115780))

	def test_21530115781(self):
		input = '''
func Zoj (string DxG)	begin
	end
bool Vx[47.49]
string Mq[80.61,36.07]
func VAI9 (bool LI)	return
'''
		expect = '''Program([FuncDecl(Id(Zoj), [VarDecl(Id(DxG), StringType, None, None)], Block([])), VarDecl(Id(Vx), ArrayType([47.49], BoolType), None, None), VarDecl(Id(Mq), ArrayType([80.61, 36.07], StringType), None, None), FuncDecl(Id(VAI9), [VarDecl(Id(LI), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115781))

	def test_21530115782(self):
		input = '''
bool tC[38.16]
func xe (number Im[64.54,98.71])
	begin
		continue
		number oNA <- "JH"
	end

func sm (string I3C, number UCof[63.23,18.03,4.8], string FqH)	begin
		if (BbnD) continue
		elif (87.41)
		PgZs[96.42, 66.01] <- BvW
	end

number z130[14.91,55.59,96.53]
func E2Pf ()
	begin
		begin
			break
		end
		qMXy(HfO, true)
		begin
			if (8.64)
			var eq <- I0p
			else for Fx until IOL by "EA"
				return "gCaI"
			return
			if (false)
			for Yff until "LOolc" by 12.94
				ChJw <- "hhd"
			elif (false)
			u9 <- false
		end
	end
'''
		expect = '''Program([VarDecl(Id(tC), ArrayType([38.16], BoolType), None, None), FuncDecl(Id(xe), [VarDecl(Id(Im), ArrayType([64.54, 98.71], NumberType), None, None)], Block([Continue, VarDecl(Id(oNA), NumberType, None, StringLit(JH))])), FuncDecl(Id(sm), [VarDecl(Id(I3C), StringType, None, None), VarDecl(Id(UCof), ArrayType([63.23, 18.03, 4.8], NumberType), None, None), VarDecl(Id(FqH), StringType, None, None)], Block([If((Id(BbnD), Continue), [(NumLit(87.41), AssignStmt(ArrayCell(Id(PgZs), [NumLit(96.42), NumLit(66.01)]), Id(BvW)))], None)])), VarDecl(Id(z130), ArrayType([14.91, 55.59, 96.53], NumberType), None, None), FuncDecl(Id(E2Pf), [], Block([Block([Break]), CallStmt(Id(qMXy), [Id(HfO), BooleanLit(True)]), Block([If((NumLit(8.64), VarDecl(Id(eq), None, var, Id(I0p))), [], For(Id(Fx), Id(IOL), StringLit(EA), Return(StringLit(gCaI)))), Return(), If((BooleanLit(False), For(Id(Yff), StringLit(LOolc), NumLit(12.94), AssignStmt(Id(ChJw), StringLit(hhd)))), [(BooleanLit(False), AssignStmt(Id(u9), BooleanLit(False)))], None)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115782))

	def test_21530115783(self):
		input = '''
func qBYF (string N1, bool I20, number HD[66.92,99.57])
	return

'''
		expect = '''Program([FuncDecl(Id(qBYF), [VarDecl(Id(N1), StringType, None, None), VarDecl(Id(I20), BoolType, None, None), VarDecl(Id(HD), ArrayType([66.92, 99.57], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115783))

	def test_21530115784(self):
		input = '''
func t0ro (bool vp[1.48,88.44,47.71])	begin
	end

func ZH (number IhsW, string hI8K)	return "rer"
func cI (bool gSBo, string olbz[98.35])	return false

func jT (bool uHOu)	begin
		number pdWx[96.87,10.3,36.59] <- 91.77
		return "tY"
	end
func Je (number N_I, string Qqs[27.62,85.72])
	return
'''
		expect = '''Program([FuncDecl(Id(t0ro), [VarDecl(Id(vp), ArrayType([1.48, 88.44, 47.71], BoolType), None, None)], Block([])), FuncDecl(Id(ZH), [VarDecl(Id(IhsW), NumberType, None, None), VarDecl(Id(hI8K), StringType, None, None)], Return(StringLit(rer))), FuncDecl(Id(cI), [VarDecl(Id(gSBo), BoolType, None, None), VarDecl(Id(olbz), ArrayType([98.35], StringType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(jT), [VarDecl(Id(uHOu), BoolType, None, None)], Block([VarDecl(Id(pdWx), ArrayType([96.87, 10.3, 36.59], NumberType), None, NumLit(91.77)), Return(StringLit(tY))])), FuncDecl(Id(Je), [VarDecl(Id(N_I), NumberType, None, None), VarDecl(Id(Qqs), ArrayType([27.62, 85.72], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115784))

	def test_21530115785(self):
		input = '''
var nJ <- false
string oGgo[87.4]
bool Xh[58.59]
'''
		expect = '''Program([VarDecl(Id(nJ), None, var, BooleanLit(False)), VarDecl(Id(oGgo), ArrayType([87.4], StringType), None, None), VarDecl(Id(Xh), ArrayType([58.59], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115785))

	def test_21530115786(self):
		input = '''
bool GC[86.25]
func Lm (string Aow, number n_O[55.84,48.84])
	return "B"
'''
		expect = '''Program([VarDecl(Id(GC), ArrayType([86.25], BoolType), None, None), FuncDecl(Id(Lm), [VarDecl(Id(Aow), StringType, None, None), VarDecl(Id(n_O), ArrayType([55.84, 48.84], NumberType), None, None)], Return(StringLit(B)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115786))

	def test_21530115787(self):
		input = '''
string DhX
func BO (string LD, string Yqok)
	return

func FC (number IW3[47.21], string oLdZ, number PGsX)	return false

number eo
'''
		expect = '''Program([VarDecl(Id(DhX), StringType, None, None), FuncDecl(Id(BO), [VarDecl(Id(LD), StringType, None, None), VarDecl(Id(Yqok), StringType, None, None)], Return()), FuncDecl(Id(FC), [VarDecl(Id(IW3), ArrayType([47.21], NumberType), None, None), VarDecl(Id(oLdZ), StringType, None, None), VarDecl(Id(PGsX), NumberType, None, None)], Return(BooleanLit(False))), VarDecl(Id(eo), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115787))

	def test_21530115788(self):
		input = '''
bool vFs[91.36,11.89,17.35] <- "cmM"
func s9Ar (bool Ro2[98.69,45.52], number Lo[84.86,55.06,29.95])	return W3Q
number mV <- "VqDo"
string sb0[40.61] <- 40.72
'''
		expect = '''Program([VarDecl(Id(vFs), ArrayType([91.36, 11.89, 17.35], BoolType), None, StringLit(cmM)), FuncDecl(Id(s9Ar), [VarDecl(Id(Ro2), ArrayType([98.69, 45.52], BoolType), None, None), VarDecl(Id(Lo), ArrayType([84.86, 55.06, 29.95], NumberType), None, None)], Return(Id(W3Q))), VarDecl(Id(mV), NumberType, None, StringLit(VqDo)), VarDecl(Id(sb0), ArrayType([40.61], StringType), None, NumLit(40.72))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115788))

	def test_21530115789(self):
		input = '''
number LRd[76.06]
'''
		expect = '''Program([VarDecl(Id(LRd), ArrayType([76.06], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115789))

	def test_21530115790(self):
		input = '''
func p_Z (string IgK[77.51,1.37], bool WoD, number gsf)
	return true
func jKgF (bool IaV)	return
var Ir8G <- 3.4
'''
		expect = '''Program([FuncDecl(Id(p_Z), [VarDecl(Id(IgK), ArrayType([77.51, 1.37], StringType), None, None), VarDecl(Id(WoD), BoolType, None, None), VarDecl(Id(gsf), NumberType, None, None)], Return(BooleanLit(True))), FuncDecl(Id(jKgF), [VarDecl(Id(IaV), BoolType, None, None)], Return()), VarDecl(Id(Ir8G), None, var, NumLit(3.4))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115790))

	def test_21530115791(self):
		input = '''
number tfKO[36.39]
'''
		expect = '''Program([VarDecl(Id(tfKO), ArrayType([36.39], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115791))

	def test_21530115792(self):
		input = '''
number Pu0g[63.74] <- "kuWy"
bool vc[24.23,88.88,67.49] <- 59.13
func iKfb (bool psy, bool eux[72.64], string xUQB[62.3])	begin
		begin
		end
		return huXO
		break
	end
'''
		expect = '''Program([VarDecl(Id(Pu0g), ArrayType([63.74], NumberType), None, StringLit(kuWy)), VarDecl(Id(vc), ArrayType([24.23, 88.88, 67.49], BoolType), None, NumLit(59.13)), FuncDecl(Id(iKfb), [VarDecl(Id(psy), BoolType, None, None), VarDecl(Id(eux), ArrayType([72.64], BoolType), None, None), VarDecl(Id(xUQB), ArrayType([62.3], StringType), None, None)], Block([Block([]), Return(Id(huXO)), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115792))

	def test_21530115793(self):
		input = '''
func Fn ()	return vj9D
'''
		expect = '''Program([FuncDecl(Id(Fn), [], Return(Id(vj9D)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115793))

	def test_21530115794(self):
		input = '''
func kR9 (number RRKR)	return "dhki"

'''
		expect = '''Program([FuncDecl(Id(kR9), [VarDecl(Id(RRKR), NumberType, None, None)], Return(StringLit(dhki)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115794))

	def test_21530115795(self):
		input = '''
dynamic jP <- Mrf4
func hD (bool ta, bool vG[63.78,6.46,90.34])
	return kPZ

string ZtD1 <- 85.48
string qjFH <- "C"
'''
		expect = '''Program([VarDecl(Id(jP), None, dynamic, Id(Mrf4)), FuncDecl(Id(hD), [VarDecl(Id(ta), BoolType, None, None), VarDecl(Id(vG), ArrayType([63.78, 6.46, 90.34], BoolType), None, None)], Return(Id(kPZ))), VarDecl(Id(ZtD1), StringType, None, NumLit(85.48)), VarDecl(Id(qjFH), StringType, None, StringLit(C))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115795))

	def test_21530115796(self):
		input = '''
func x3M (bool dWa, bool i56d[89.78])	return "u"
func Ot6 (number RKMT[52.41], bool KGNC, string lk)	return "Wp"

func Ypw ()	begin
	end

string QQ
'''
		expect = '''Program([FuncDecl(Id(x3M), [VarDecl(Id(dWa), BoolType, None, None), VarDecl(Id(i56d), ArrayType([89.78], BoolType), None, None)], Return(StringLit(u))), FuncDecl(Id(Ot6), [VarDecl(Id(RKMT), ArrayType([52.41], NumberType), None, None), VarDecl(Id(KGNC), BoolType, None, None), VarDecl(Id(lk), StringType, None, None)], Return(StringLit(Wp))), FuncDecl(Id(Ypw), [], Block([])), VarDecl(Id(QQ), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115796))

	def test_21530115797(self):
		input = '''
func imM (bool TV9[59.71], bool WQ, bool jOD)	return

'''
		expect = '''Program([FuncDecl(Id(imM), [VarDecl(Id(TV9), ArrayType([59.71], BoolType), None, None), VarDecl(Id(WQ), BoolType, None, None), VarDecl(Id(jOD), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115797))

	def test_21530115798(self):
		input = '''
func BQ ()	begin
		vy[80.15] <- AyEG
		continue
	end

func SH8 (bool tAB[31.73], string cOD[48.02,36.29])
	return yTbf
number hQ9Q
'''
		expect = '''Program([FuncDecl(Id(BQ), [], Block([AssignStmt(ArrayCell(Id(vy), [NumLit(80.15)]), Id(AyEG)), Continue])), FuncDecl(Id(SH8), [VarDecl(Id(tAB), ArrayType([31.73], BoolType), None, None), VarDecl(Id(cOD), ArrayType([48.02, 36.29], StringType), None, None)], Return(Id(yTbf))), VarDecl(Id(hQ9Q), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115798))

	def test_21530115799(self):
		input = '''
func hs (bool qXD, string TKk[29.4])	return 61.62
string ASs[47.18,77.38]
number k5D[30.48,83.56,17.66] <- 14.25
func uNJ4 (number Kc, bool EE[51.24,87.34])
	return

'''
		expect = '''Program([FuncDecl(Id(hs), [VarDecl(Id(qXD), BoolType, None, None), VarDecl(Id(TKk), ArrayType([29.4], StringType), None, None)], Return(NumLit(61.62))), VarDecl(Id(ASs), ArrayType([47.18, 77.38], StringType), None, None), VarDecl(Id(k5D), ArrayType([30.48, 83.56, 17.66], NumberType), None, NumLit(14.25)), FuncDecl(Id(uNJ4), [VarDecl(Id(Kc), NumberType, None, None), VarDecl(Id(EE), ArrayType([51.24, 87.34], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115799))

	def test_21530115800(self):
		input = '''
string CME[97.71]
dynamic ps <- "Fu"
func wE_ ()
	begin
	end

'''
		expect = '''Program([VarDecl(Id(CME), ArrayType([97.71], StringType), None, None), VarDecl(Id(ps), None, dynamic, StringLit(Fu)), FuncDecl(Id(wE_), [], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115800))

	def test_21530115801(self):
		input = '''
func rU (number L9[43.53])
	begin
		rO <- sn9
		XG(false)
	end
func iF ()	return false
func p3E (bool NV[77.31], bool Wgxf[55.84,85.67], string s_)
	return "puvG"

var Gf <- jvTO
'''
		expect = '''Program([FuncDecl(Id(rU), [VarDecl(Id(L9), ArrayType([43.53], NumberType), None, None)], Block([AssignStmt(Id(rO), Id(sn9)), CallStmt(Id(XG), [BooleanLit(False)])])), FuncDecl(Id(iF), [], Return(BooleanLit(False))), FuncDecl(Id(p3E), [VarDecl(Id(NV), ArrayType([77.31], BoolType), None, None), VarDecl(Id(Wgxf), ArrayType([55.84, 85.67], BoolType), None, None), VarDecl(Id(s_), StringType, None, None)], Return(StringLit(puvG))), VarDecl(Id(Gf), None, var, Id(jvTO))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115801))

	def test_21530115802(self):
		input = '''
func Hvw (bool we[69.33,85.05,41.55], string HD)	return
func Og (number ICEO[12.18])
	begin
		for z2 until Hc2 by 13.27
			if (VixW)
			if ("C")
			continue
			else for IZ until 26.73 by "l"
				begin
					continue
					uicM <- kG_d
					for L1 until "Z" by yAHF
						return
				end
			elif (WHxU) lNv[31.48] <- 52.24
			elif (NS7)
			ja <- iB
			elif ("xwdq") break
			elif ("j") dv8 <- j9T
	end

'''
		expect = '''Program([FuncDecl(Id(Hvw), [VarDecl(Id(we), ArrayType([69.33, 85.05, 41.55], BoolType), None, None), VarDecl(Id(HD), StringType, None, None)], Return()), FuncDecl(Id(Og), [VarDecl(Id(ICEO), ArrayType([12.18], NumberType), None, None)], Block([For(Id(z2), Id(Hc2), NumLit(13.27), If((Id(VixW), If((StringLit(C), Continue), [], For(Id(IZ), NumLit(26.73), StringLit(l), Block([Continue, AssignStmt(Id(uicM), Id(kG_d)), For(Id(L1), StringLit(Z), Id(yAHF), Return())])))), [(Id(WHxU), AssignStmt(ArrayCell(Id(lNv), [NumLit(31.48)]), NumLit(52.24))), (Id(NS7), AssignStmt(Id(ja), Id(iB))), (StringLit(xwdq), Break), (StringLit(j), AssignStmt(Id(dv8), Id(j9T)))], None))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115802))

	def test_21530115803(self):
		input = '''
func dzT0 (bool ZooK[34.46,96.5,69.52], number Wc[67.06,30.67])	return

func Rmk9 (bool min)
	return

'''
		expect = '''Program([FuncDecl(Id(dzT0), [VarDecl(Id(ZooK), ArrayType([34.46, 96.5, 69.52], BoolType), None, None), VarDecl(Id(Wc), ArrayType([67.06, 30.67], NumberType), None, None)], Return()), FuncDecl(Id(Rmk9), [VarDecl(Id(min), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115803))

	def test_21530115804(self):
		input = '''
bool fz4 <- 79.32
number W82B[72.13,21.73]
'''
		expect = '''Program([VarDecl(Id(fz4), BoolType, None, NumLit(79.32)), VarDecl(Id(W82B), ArrayType([72.13, 21.73], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115804))

	def test_21530115805(self):
		input = '''
func KS (bool DEVh)	begin
		uT <- "lD"
		MlgV <- "sOQu"
	end

func Hvh ()
	return false
func jB7M (bool iNFC[38.39,61.69], bool WR88, number Fk[77.12,11.26,96.77])	return

'''
		expect = '''Program([FuncDecl(Id(KS), [VarDecl(Id(DEVh), BoolType, None, None)], Block([AssignStmt(Id(uT), StringLit(lD)), AssignStmt(Id(MlgV), StringLit(sOQu))])), FuncDecl(Id(Hvh), [], Return(BooleanLit(False))), FuncDecl(Id(jB7M), [VarDecl(Id(iNFC), ArrayType([38.39, 61.69], BoolType), None, None), VarDecl(Id(WR88), BoolType, None, None), VarDecl(Id(Fk), ArrayType([77.12, 11.26, 96.77], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115805))

	def test_21530115806(self):
		input = '''
func eP (bool PIlS[7.23], number E9[79.21,75.63], string cRg[59.14,68.19])	begin
		begin
			continue
		end
	end
'''
		expect = '''Program([FuncDecl(Id(eP), [VarDecl(Id(PIlS), ArrayType([7.23], BoolType), None, None), VarDecl(Id(E9), ArrayType([79.21, 75.63], NumberType), None, None), VarDecl(Id(cRg), ArrayType([59.14, 68.19], StringType), None, None)], Block([Block([Continue])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115806))

	def test_21530115807(self):
		input = '''
func wVUl ()
	return true

func FO (string Vq[67.82], string aEV9[99.7,66.3])	return
func bkXf (string hC[24.21,93.69,35.91])
	return "Eci"
'''
		expect = '''Program([FuncDecl(Id(wVUl), [], Return(BooleanLit(True))), FuncDecl(Id(FO), [VarDecl(Id(Vq), ArrayType([67.82], StringType), None, None), VarDecl(Id(aEV9), ArrayType([99.7, 66.3], StringType), None, None)], Return()), FuncDecl(Id(bkXf), [VarDecl(Id(hC), ArrayType([24.21, 93.69, 35.91], StringType), None, None)], Return(StringLit(Eci)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115807))

	def test_21530115808(self):
		input = '''
string mME[43.29,28.48,14.73] <- 88.13
var oQJ <- 24.88
bool p_ <- "SLNIc"
func VN (bool TFBz, string fx, string MEqk[38.8,62.68])
	return true

'''
		expect = '''Program([VarDecl(Id(mME), ArrayType([43.29, 28.48, 14.73], StringType), None, NumLit(88.13)), VarDecl(Id(oQJ), None, var, NumLit(24.88)), VarDecl(Id(p_), BoolType, None, StringLit(SLNIc)), FuncDecl(Id(VN), [VarDecl(Id(TFBz), BoolType, None, None), VarDecl(Id(fx), StringType, None, None), VarDecl(Id(MEqk), ArrayType([38.8, 62.68], StringType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115808))

	def test_21530115809(self):
		input = '''
bool AH <- 43.44
bool ab_r[8.97,0.15,93.6]
'''
		expect = '''Program([VarDecl(Id(AH), BoolType, None, NumLit(43.44)), VarDecl(Id(ab_r), ArrayType([8.97, 0.15, 93.6], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115809))

	def test_21530115810(self):
		input = '''
bool B8[53.56,73.77]
func dee (string Edr, string AIO6[66.91])
	return
func j_ (number Kfg, number GNl, string IVa)
	begin
		if (23.26) HeK("jbvSk", "gNZ")
		elif ("Juo")
		if (wTm) if (wd) Js <- "wXLFl"
		elif ("E") break
		elif (46.42) return
		elif (Ds8C) number Tf
		elif (aWo) begin
			begin
				continue
			end
			xVd[false, true] <- j_fR
			break
		end
		elif ("dV")
		for hBWT until true by vEX
			if (f1)
			for F1QC until "W" by 57.27
				aW[44.42, kgn, 21.84] <- "LME"
			elif ("tQxox")
			hw2m()
			elif ("OK") ut6(44.95, DF8)
			elif (PX) for l6I until "udQzB" by true
				YeC0()
			elif (false)
			fisg[Fa9, 13.67] <- "uYxd"
			else begin
				continue
				begin
				end
			end
		else T3rS <- "w"
		elif (75.31)
		continue
		elif ("ve")
		xf8(false, eQM)
		else begin
			break
			N3["w", "g"] <- 71.03
			begin
				for hc until true by qKnx
					return 95.69
				for ZY until false by false
					continue
				vfA[true, "iYLgW"] <- "Zd"
			end
		end
		var tu <- 73.07
	end
'''
		expect = '''Program([VarDecl(Id(B8), ArrayType([53.56, 73.77], BoolType), None, None), FuncDecl(Id(dee), [VarDecl(Id(Edr), StringType, None, None), VarDecl(Id(AIO6), ArrayType([66.91], StringType), None, None)], Return()), FuncDecl(Id(j_), [VarDecl(Id(Kfg), NumberType, None, None), VarDecl(Id(GNl), NumberType, None, None), VarDecl(Id(IVa), StringType, None, None)], Block([If((NumLit(23.26), CallStmt(Id(HeK), [StringLit(jbvSk), StringLit(gNZ)])), [(StringLit(Juo), If((Id(wTm), If((Id(wd), AssignStmt(Id(Js), StringLit(wXLFl))), [(StringLit(E), Break), (NumLit(46.42), Return()), (Id(Ds8C), VarDecl(Id(Tf), NumberType, None, None)), (Id(aWo), Block([Block([Continue]), AssignStmt(ArrayCell(Id(xVd), [BooleanLit(False), BooleanLit(True)]), Id(j_fR)), Break])), (StringLit(dV), For(Id(hBWT), BooleanLit(True), Id(vEX), If((Id(f1), For(Id(F1QC), StringLit(W), NumLit(57.27), AssignStmt(ArrayCell(Id(aW), [NumLit(44.42), Id(kgn), NumLit(21.84)]), StringLit(LME)))), [(StringLit(tQxox), CallStmt(Id(hw2m), [])), (StringLit(OK), CallStmt(Id(ut6), [NumLit(44.95), Id(DF8)])), (Id(PX), For(Id(l6I), StringLit(udQzB), BooleanLit(True), CallStmt(Id(YeC0), []))), (BooleanLit(False), AssignStmt(ArrayCell(Id(fisg), [Id(Fa9), NumLit(13.67)]), StringLit(uYxd)))], Block([Continue, Block([])]))))], AssignStmt(Id(T3rS), StringLit(w)))), [(NumLit(75.31), Continue), (StringLit(ve), CallStmt(Id(xf8), [BooleanLit(False), Id(eQM)]))], Block([Break, AssignStmt(ArrayCell(Id(N3), [StringLit(w), StringLit(g)]), NumLit(71.03)), Block([For(Id(hc), BooleanLit(True), Id(qKnx), Return(NumLit(95.69))), For(Id(ZY), BooleanLit(False), BooleanLit(False), Continue), AssignStmt(ArrayCell(Id(vfA), [BooleanLit(True), StringLit(iYLgW)]), StringLit(Zd))])])))], None), VarDecl(Id(tu), None, var, NumLit(73.07))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115810))

	def test_21530115811(self):
		input = '''
func i9 (string hTW, number nTc[67.35])	return q6

string to8D[28.42,8.29,66.59] <- 51.0
'''
		expect = '''Program([FuncDecl(Id(i9), [VarDecl(Id(hTW), StringType, None, None), VarDecl(Id(nTc), ArrayType([67.35], NumberType), None, None)], Return(Id(q6))), VarDecl(Id(to8D), ArrayType([28.42, 8.29, 66.59], StringType), None, NumLit(51.0))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115811))

	def test_21530115812(self):
		input = '''
string NQ6Y[5.2,94.31,5.88] <- "KAljx"
'''
		expect = '''Program([VarDecl(Id(NQ6Y), ArrayType([5.2, 94.31, 5.88], StringType), None, StringLit(KAljx))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115812))

	def test_21530115813(self):
		input = '''
bool Wx[78.96,60.12]
number acF
func NcAk (bool V2T[59.95,52.37,49.17], bool wS3H[61.75,5.49,42.8], number KmRn)
	begin
		return
	end

func dmTi (number S6u[34.22], number VUTc, bool HaLj)
	begin
	end
'''
		expect = '''Program([VarDecl(Id(Wx), ArrayType([78.96, 60.12], BoolType), None, None), VarDecl(Id(acF), NumberType, None, None), FuncDecl(Id(NcAk), [VarDecl(Id(V2T), ArrayType([59.95, 52.37, 49.17], BoolType), None, None), VarDecl(Id(wS3H), ArrayType([61.75, 5.49, 42.8], BoolType), None, None), VarDecl(Id(KmRn), NumberType, None, None)], Block([Return()])), FuncDecl(Id(dmTi), [VarDecl(Id(S6u), ArrayType([34.22], NumberType), None, None), VarDecl(Id(VUTc), NumberType, None, None), VarDecl(Id(HaLj), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115813))

	def test_21530115814(self):
		input = '''
func y3O5 ()
	return

bool hyOG
func F0FD ()
	return
number YS[41.86,62.77] <- 5.96
func tT1Q (bool ZUeA[95.14,72.79,56.97], string nplg, string co[72.36,38.13])
	return

'''
		expect = '''Program([FuncDecl(Id(y3O5), [], Return()), VarDecl(Id(hyOG), BoolType, None, None), FuncDecl(Id(F0FD), [], Return()), VarDecl(Id(YS), ArrayType([41.86, 62.77], NumberType), None, NumLit(5.96)), FuncDecl(Id(tT1Q), [VarDecl(Id(ZUeA), ArrayType([95.14, 72.79, 56.97], BoolType), None, None), VarDecl(Id(nplg), StringType, None, None), VarDecl(Id(co), ArrayType([72.36, 38.13], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115814))

	def test_21530115815(self):
		input = '''
bool H5[8.97] <- 14.18
string IY56 <- true
func OA_ (number Li, string m1z, string KW4[74.89,2.36])	return "nRcao"

bool iq7 <- "koOuY"
func tYE (bool ntF[24.26,67.62], number lxP[19.55,44.14])	return 17.62
'''
		expect = '''Program([VarDecl(Id(H5), ArrayType([8.97], BoolType), None, NumLit(14.18)), VarDecl(Id(IY56), StringType, None, BooleanLit(True)), FuncDecl(Id(OA_), [VarDecl(Id(Li), NumberType, None, None), VarDecl(Id(m1z), StringType, None, None), VarDecl(Id(KW4), ArrayType([74.89, 2.36], StringType), None, None)], Return(StringLit(nRcao))), VarDecl(Id(iq7), BoolType, None, StringLit(koOuY)), FuncDecl(Id(tYE), [VarDecl(Id(ntF), ArrayType([24.26, 67.62], BoolType), None, None), VarDecl(Id(lxP), ArrayType([19.55, 44.14], NumberType), None, None)], Return(NumLit(17.62)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115815))

	def test_21530115816(self):
		input = '''
func Puy (bool Tgt[40.96], number lUr, string A7z)	return
number ZX <- 52.39
func MEh (number jq[1.55,87.82], number jvP, bool GXS)	return
dynamic bhcW
'''
		expect = '''Program([FuncDecl(Id(Puy), [VarDecl(Id(Tgt), ArrayType([40.96], BoolType), None, None), VarDecl(Id(lUr), NumberType, None, None), VarDecl(Id(A7z), StringType, None, None)], Return()), VarDecl(Id(ZX), NumberType, None, NumLit(52.39)), FuncDecl(Id(MEh), [VarDecl(Id(jq), ArrayType([1.55, 87.82], NumberType), None, None), VarDecl(Id(jvP), NumberType, None, None), VarDecl(Id(GXS), BoolType, None, None)], Return()), VarDecl(Id(bhcW), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115816))

	def test_21530115817(self):
		input = '''
func vvw (bool VM[16.44])
	return

number O_M0[55.97]
string M3
'''
		expect = '''Program([FuncDecl(Id(vvw), [VarDecl(Id(VM), ArrayType([16.44], BoolType), None, None)], Return()), VarDecl(Id(O_M0), ArrayType([55.97], NumberType), None, None), VarDecl(Id(M3), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115817))

	def test_21530115818(self):
		input = '''
bool xB1[9.34,19.82]
dynamic RSZ <- "Caj"
'''
		expect = '''Program([VarDecl(Id(xB1), ArrayType([9.34, 19.82], BoolType), None, None), VarDecl(Id(RSZ), None, dynamic, StringLit(Caj))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115818))

	def test_21530115819(self):
		input = '''
func UBY (bool wiC6[21.31,96.99])
	return
'''
		expect = '''Program([FuncDecl(Id(UBY), [VarDecl(Id(wiC6), ArrayType([21.31, 96.99], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115819))

	def test_21530115820(self):
		input = '''
func itS (bool qWn[69.41,44.98])
	return
string u2F[7.5] <- yTz
number dvhY[89.33,95.51,77.09]
'''
		expect = '''Program([FuncDecl(Id(itS), [VarDecl(Id(qWn), ArrayType([69.41, 44.98], BoolType), None, None)], Return()), VarDecl(Id(u2F), ArrayType([7.5], StringType), None, Id(yTz)), VarDecl(Id(dvhY), ArrayType([89.33, 95.51, 77.09], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115820))

	def test_21530115821(self):
		input = '''
var peP <- "fNb"
number YOm
func ALRk ()
	return

func Ku4t ()	begin
		begin
		end
	end

'''
		expect = '''Program([VarDecl(Id(peP), None, var, StringLit(fNb)), VarDecl(Id(YOm), NumberType, None, None), FuncDecl(Id(ALRk), [], Return()), FuncDecl(Id(Ku4t), [], Block([Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115821))

	def test_21530115822(self):
		input = '''
func yzPm (number kBq, string nPln[77.81], bool p9[27.99,71.8,91.78])	return "R"
func ly ()	return
var l2r <- Asg
func gc (string RQz, bool wk[7.5,53.01], number yis[16.64,18.22])
	return false

func O39O (number f2)	begin
		ZCiz <- Z6
	end
'''
		expect = '''Program([FuncDecl(Id(yzPm), [VarDecl(Id(kBq), NumberType, None, None), VarDecl(Id(nPln), ArrayType([77.81], StringType), None, None), VarDecl(Id(p9), ArrayType([27.99, 71.8, 91.78], BoolType), None, None)], Return(StringLit(R))), FuncDecl(Id(ly), [], Return()), VarDecl(Id(l2r), None, var, Id(Asg)), FuncDecl(Id(gc), [VarDecl(Id(RQz), StringType, None, None), VarDecl(Id(wk), ArrayType([7.5, 53.01], BoolType), None, None), VarDecl(Id(yis), ArrayType([16.64, 18.22], NumberType), None, None)], Return(BooleanLit(False))), FuncDecl(Id(O39O), [VarDecl(Id(f2), NumberType, None, None)], Block([AssignStmt(Id(ZCiz), Id(Z6))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115822))

	def test_21530115823(self):
		input = '''
var ryUm <- 84.2
string Ay[47.55]
var GR <- "GxLg"
'''
		expect = '''Program([VarDecl(Id(ryUm), None, var, NumLit(84.2)), VarDecl(Id(Ay), ArrayType([47.55], StringType), None, None), VarDecl(Id(GR), None, var, StringLit(GxLg))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115823))

	def test_21530115824(self):
		input = '''
func ArEu (bool Hc[81.74,11.28,55.54])	return "CaRvx"

func JAoX (string ScN[46.27,49.38], bool AX[54.74,34.58])	return

string dfr[20.63,97.18] <- 35.5
'''
		expect = '''Program([FuncDecl(Id(ArEu), [VarDecl(Id(Hc), ArrayType([81.74, 11.28, 55.54], BoolType), None, None)], Return(StringLit(CaRvx))), FuncDecl(Id(JAoX), [VarDecl(Id(ScN), ArrayType([46.27, 49.38], StringType), None, None), VarDecl(Id(AX), ArrayType([54.74, 34.58], BoolType), None, None)], Return()), VarDecl(Id(dfr), ArrayType([20.63, 97.18], StringType), None, NumLit(35.5))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115824))

	def test_21530115825(self):
		input = '''
func vBB (bool Xg[94.46], bool Mk0X[79.56,59.35], bool sq)
	return true

string vT[74.85,75.16,65.94] <- 70.93
'''
		expect = '''Program([FuncDecl(Id(vBB), [VarDecl(Id(Xg), ArrayType([94.46], BoolType), None, None), VarDecl(Id(Mk0X), ArrayType([79.56, 59.35], BoolType), None, None), VarDecl(Id(sq), BoolType, None, None)], Return(BooleanLit(True))), VarDecl(Id(vT), ArrayType([74.85, 75.16, 65.94], StringType), None, NumLit(70.93))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115825))

	def test_21530115826(self):
		input = '''
string gVlZ[40.68] <- false
'''
		expect = '''Program([VarDecl(Id(gVlZ), ArrayType([40.68], StringType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115826))

	def test_21530115827(self):
		input = '''
string GWQ[83.38] <- true
func H2 (string Bu[30.49,41.37,18.26])
	return h86

func R4S (number w8p)	return

'''
		expect = '''Program([VarDecl(Id(GWQ), ArrayType([83.38], StringType), None, BooleanLit(True)), FuncDecl(Id(H2), [VarDecl(Id(Bu), ArrayType([30.49, 41.37, 18.26], StringType), None, None)], Return(Id(h86))), FuncDecl(Id(R4S), [VarDecl(Id(w8p), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115827))

	def test_21530115828(self):
		input = '''
func BRbH (number Vx[27.97])
	begin
		break
	end
'''
		expect = '''Program([FuncDecl(Id(BRbH), [VarDecl(Id(Vx), ArrayType([27.97], NumberType), None, None)], Block([Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115828))

	def test_21530115829(self):
		input = '''
var mqo2 <- "ScvI"
var yH <- "VRqv"
number CN[51.24,15.33] <- "A"
'''
		expect = '''Program([VarDecl(Id(mqo2), None, var, StringLit(ScvI)), VarDecl(Id(yH), None, var, StringLit(VRqv)), VarDecl(Id(CN), ArrayType([51.24, 15.33], NumberType), None, StringLit(A))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115829))

	def test_21530115830(self):
		input = '''
func bMvQ ()
	return false
bool KHKn
'''
		expect = '''Program([FuncDecl(Id(bMvQ), [], Return(BooleanLit(False))), VarDecl(Id(KHKn), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115830))

	def test_21530115831(self):
		input = '''
func KN ()	return
func LR (number IZ[3.38], string Be[2.37,11.96])	return
func u8c (bool VVCo[65.2,73.39], string Pgrj)	begin
		if (39.88)
		return false
		d_(HDoc, "MEby", true)
	end
func im (string XKH4, string kx, number hQx)	return bVN

'''
		expect = '''Program([FuncDecl(Id(KN), [], Return()), FuncDecl(Id(LR), [VarDecl(Id(IZ), ArrayType([3.38], NumberType), None, None), VarDecl(Id(Be), ArrayType([2.37, 11.96], StringType), None, None)], Return()), FuncDecl(Id(u8c), [VarDecl(Id(VVCo), ArrayType([65.2, 73.39], BoolType), None, None), VarDecl(Id(Pgrj), StringType, None, None)], Block([If((NumLit(39.88), Return(BooleanLit(False))), [], None), CallStmt(Id(d_), [Id(HDoc), StringLit(MEby), BooleanLit(True)])])), FuncDecl(Id(im), [VarDecl(Id(XKH4), StringType, None, None), VarDecl(Id(kx), StringType, None, None), VarDecl(Id(hQx), NumberType, None, None)], Return(Id(bVN)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115831))

	def test_21530115832(self):
		input = '''
func SzOr (bool UsQ5[92.37])
	return

string deE5[31.08] <- "pl"
number V4[91.96,16.31]
'''
		expect = '''Program([FuncDecl(Id(SzOr), [VarDecl(Id(UsQ5), ArrayType([92.37], BoolType), None, None)], Return()), VarDecl(Id(deE5), ArrayType([31.08], StringType), None, StringLit(pl)), VarDecl(Id(V4), ArrayType([91.96, 16.31], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115832))

	def test_21530115833(self):
		input = '''
func ppl (bool kSN5)
	return

func gGN2 (number axb[97.92,49.86], number aCWg[49.27,53.57,42.17])
	begin
		for U3J until true by Knbr
			return false
	end
func d4J (number tp[15.93,32.27,32.81])	return 73.41

func QMvy ()	return

func Yx (number HS, number WV[27.98,85.92])
	return 78.26

'''
		expect = '''Program([FuncDecl(Id(ppl), [VarDecl(Id(kSN5), BoolType, None, None)], Return()), FuncDecl(Id(gGN2), [VarDecl(Id(axb), ArrayType([97.92, 49.86], NumberType), None, None), VarDecl(Id(aCWg), ArrayType([49.27, 53.57, 42.17], NumberType), None, None)], Block([For(Id(U3J), BooleanLit(True), Id(Knbr), Return(BooleanLit(False)))])), FuncDecl(Id(d4J), [VarDecl(Id(tp), ArrayType([15.93, 32.27, 32.81], NumberType), None, None)], Return(NumLit(73.41))), FuncDecl(Id(QMvy), [], Return()), FuncDecl(Id(Yx), [VarDecl(Id(HS), NumberType, None, None), VarDecl(Id(WV), ArrayType([27.98, 85.92], NumberType), None, None)], Return(NumLit(78.26)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115833))

	def test_21530115834(self):
		input = '''
func jXZ (string yo)
	begin
		number HkBK[72.35,92.52]
	end
func kJSh (string Z6)
	return
'''
		expect = '''Program([FuncDecl(Id(jXZ), [VarDecl(Id(yo), StringType, None, None)], Block([VarDecl(Id(HkBK), ArrayType([72.35, 92.52], NumberType), None, None)])), FuncDecl(Id(kJSh), [VarDecl(Id(Z6), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115834))

	def test_21530115835(self):
		input = '''
func SG (number GU[34.33,28.83])	return "Oyc"

func OvAR (bool Ac[87.66])	return true

'''
		expect = '''Program([FuncDecl(Id(SG), [VarDecl(Id(GU), ArrayType([34.33, 28.83], NumberType), None, None)], Return(StringLit(Oyc))), FuncDecl(Id(OvAR), [VarDecl(Id(Ac), ArrayType([87.66], BoolType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115835))

	def test_21530115836(self):
		input = '''
number JjFn[31.31,14.82,65.66] <- false
func xp (number pC[80.89,48.63])	return

number mh5d[54.66,31.73,96.94] <- "vTA"
string zR
number ARMz[64.16,36.44,16.68]
'''
		expect = '''Program([VarDecl(Id(JjFn), ArrayType([31.31, 14.82, 65.66], NumberType), None, BooleanLit(False)), FuncDecl(Id(xp), [VarDecl(Id(pC), ArrayType([80.89, 48.63], NumberType), None, None)], Return()), VarDecl(Id(mh5d), ArrayType([54.66, 31.73, 96.94], NumberType), None, StringLit(vTA)), VarDecl(Id(zR), StringType, None, None), VarDecl(Id(ARMz), ArrayType([64.16, 36.44, 16.68], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115836))

	def test_21530115837(self):
		input = '''
bool snS[10.09,97.35,24.97] <- true
func AA (number aOlf, bool Ic)	return

var VZb <- "otUH"
func KV (number ylA, bool tI[95.69,90.99,51.78])	return
'''
		expect = '''Program([VarDecl(Id(snS), ArrayType([10.09, 97.35, 24.97], BoolType), None, BooleanLit(True)), FuncDecl(Id(AA), [VarDecl(Id(aOlf), NumberType, None, None), VarDecl(Id(Ic), BoolType, None, None)], Return()), VarDecl(Id(VZb), None, var, StringLit(otUH)), FuncDecl(Id(KV), [VarDecl(Id(ylA), NumberType, None, None), VarDecl(Id(tI), ArrayType([95.69, 90.99, 51.78], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115837))

	def test_21530115838(self):
		input = '''
string VkKu[89.03,81.56,96.31]
bool ToS[27.13,88.97,3.2] <- IbKj
func TD9h ()
	begin
		return
	end
'''
		expect = '''Program([VarDecl(Id(VkKu), ArrayType([89.03, 81.56, 96.31], StringType), None, None), VarDecl(Id(ToS), ArrayType([27.13, 88.97, 3.2], BoolType), None, Id(IbKj)), FuncDecl(Id(TD9h), [], Block([Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115838))

	def test_21530115839(self):
		input = '''
func jdTJ (bool HjA[98.51], string p7DA[42.2,54.75], number bS)
	begin
		begin
			xnmG("OQD", "J", 99.3)
			for iM until "q" by "g"
				d2 <- true
		end
		break
	end
func bj ()
	return false

'''
		expect = '''Program([FuncDecl(Id(jdTJ), [VarDecl(Id(HjA), ArrayType([98.51], BoolType), None, None), VarDecl(Id(p7DA), ArrayType([42.2, 54.75], StringType), None, None), VarDecl(Id(bS), NumberType, None, None)], Block([Block([CallStmt(Id(xnmG), [StringLit(OQD), StringLit(J), NumLit(99.3)]), For(Id(iM), StringLit(q), StringLit(g), AssignStmt(Id(d2), BooleanLit(True)))]), Break])), FuncDecl(Id(bj), [], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115839))

	def test_21530115840(self):
		input = '''
number RvvW[88.6,73.04]
func jwK (number gA, bool LT, bool UzU)	return 45.26
func pF (string nq[8.59], string PTHG)
	return
bool Tl1 <- y2C
'''
		expect = '''Program([VarDecl(Id(RvvW), ArrayType([88.6, 73.04], NumberType), None, None), FuncDecl(Id(jwK), [VarDecl(Id(gA), NumberType, None, None), VarDecl(Id(LT), BoolType, None, None), VarDecl(Id(UzU), BoolType, None, None)], Return(NumLit(45.26))), FuncDecl(Id(pF), [VarDecl(Id(nq), ArrayType([8.59], StringType), None, None), VarDecl(Id(PTHG), StringType, None, None)], Return()), VarDecl(Id(Tl1), BoolType, None, Id(y2C))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115840))

	def test_21530115841(self):
		input = '''
func Vl (bool C0c, number ixID)	return 18.27

func f2z (bool gtt)
	return 76.47

'''
		expect = '''Program([FuncDecl(Id(Vl), [VarDecl(Id(C0c), BoolType, None, None), VarDecl(Id(ixID), NumberType, None, None)], Return(NumLit(18.27))), FuncDecl(Id(f2z), [VarDecl(Id(gtt), BoolType, None, None)], Return(NumLit(76.47)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115841))

	def test_21530115842(self):
		input = '''
func eAW ()	return 68.12

number xCc[0.13] <- 22.64
number zUd[70.5,34.95] <- false
func Wi0C (string doz6[34.57,34.99,98.26])	return "ShCEk"
func Yl6 (number gAEt[16.51,1.74,12.0])	return "H"

'''
		expect = '''Program([FuncDecl(Id(eAW), [], Return(NumLit(68.12))), VarDecl(Id(xCc), ArrayType([0.13], NumberType), None, NumLit(22.64)), VarDecl(Id(zUd), ArrayType([70.5, 34.95], NumberType), None, BooleanLit(False)), FuncDecl(Id(Wi0C), [VarDecl(Id(doz6), ArrayType([34.57, 34.99, 98.26], StringType), None, None)], Return(StringLit(ShCEk))), FuncDecl(Id(Yl6), [VarDecl(Id(gAEt), ArrayType([16.51, 1.74, 12.0], NumberType), None, None)], Return(StringLit(H)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115842))

	def test_21530115843(self):
		input = '''
dynamic EEDy <- hb6E
string BRDC[33.9,33.61] <- Tjui
dynamic kqg <- dLep
func jWNk (string vVWn)
	return

'''
		expect = '''Program([VarDecl(Id(EEDy), None, dynamic, Id(hb6E)), VarDecl(Id(BRDC), ArrayType([33.9, 33.61], StringType), None, Id(Tjui)), VarDecl(Id(kqg), None, dynamic, Id(dLep)), FuncDecl(Id(jWNk), [VarDecl(Id(vVWn), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115843))

	def test_21530115844(self):
		input = '''
number Ho[48.29,64.96] <- Ffx
number onU[86.46] <- 56.93
number Dz <- 79.71
func xW_I ()
	return

func j8F2 (number s2J3[92.6,56.05,71.97], string J0Z)	return r4
'''
		expect = '''Program([VarDecl(Id(Ho), ArrayType([48.29, 64.96], NumberType), None, Id(Ffx)), VarDecl(Id(onU), ArrayType([86.46], NumberType), None, NumLit(56.93)), VarDecl(Id(Dz), NumberType, None, NumLit(79.71)), FuncDecl(Id(xW_I), [], Return()), FuncDecl(Id(j8F2), [VarDecl(Id(s2J3), ArrayType([92.6, 56.05, 71.97], NumberType), None, None), VarDecl(Id(J0Z), StringType, None, None)], Return(Id(r4)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115844))

	def test_21530115845(self):
		input = '''
string lLBM[47.24,26.5,57.91]
func axk (number De[56.15,94.57], number xq6, number fg[2.73])
	return
var MIJ <- B1F3
number is[15.3,44.66]
bool F3SW[47.31,95.59,33.99]
'''
		expect = '''Program([VarDecl(Id(lLBM), ArrayType([47.24, 26.5, 57.91], StringType), None, None), FuncDecl(Id(axk), [VarDecl(Id(De), ArrayType([56.15, 94.57], NumberType), None, None), VarDecl(Id(xq6), NumberType, None, None), VarDecl(Id(fg), ArrayType([2.73], NumberType), None, None)], Return()), VarDecl(Id(MIJ), None, var, Id(B1F3)), VarDecl(Id(is), ArrayType([15.3, 44.66], NumberType), None, None), VarDecl(Id(F3SW), ArrayType([47.31, 95.59, 33.99], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115845))

	def test_21530115846(self):
		input = '''
func e4 (number rYu, bool DV[30.22])	return 82.21

func dpw (bool pctR)
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(e4), [VarDecl(Id(rYu), NumberType, None, None), VarDecl(Id(DV), ArrayType([30.22], BoolType), None, None)], Return(NumLit(82.21))), FuncDecl(Id(dpw), [VarDecl(Id(pctR), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115846))

	def test_21530115847(self):
		input = '''
var Txn3 <- PN
bool G3VM[27.21,50.03] <- nn6i
func B4 (string sJe)	return

'''
		expect = '''Program([VarDecl(Id(Txn3), None, var, Id(PN)), VarDecl(Id(G3VM), ArrayType([27.21, 50.03], BoolType), None, Id(nn6i)), FuncDecl(Id(B4), [VarDecl(Id(sJe), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115847))

	def test_21530115848(self):
		input = '''
func jMC (number vqN[4.18], number DNQ[66.14,45.05])
	return

number HwR[22.07] <- fr2
func Knbg (number KFt, number AuI[97.91,58.49])
	return
func GZ ()	begin
		Uqr <- "k"
		continue
	end

number Ff0a <- aDN
'''
		expect = '''Program([FuncDecl(Id(jMC), [VarDecl(Id(vqN), ArrayType([4.18], NumberType), None, None), VarDecl(Id(DNQ), ArrayType([66.14, 45.05], NumberType), None, None)], Return()), VarDecl(Id(HwR), ArrayType([22.07], NumberType), None, Id(fr2)), FuncDecl(Id(Knbg), [VarDecl(Id(KFt), NumberType, None, None), VarDecl(Id(AuI), ArrayType([97.91, 58.49], NumberType), None, None)], Return()), FuncDecl(Id(GZ), [], Block([AssignStmt(Id(Uqr), StringLit(k)), Continue])), VarDecl(Id(Ff0a), NumberType, None, Id(aDN))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115848))

	def test_21530115849(self):
		input = '''
func KJ (number Z4[47.23,40.41], string wl, bool F9)
	begin
		break
		bj <- LD
		continue
	end
'''
		expect = '''Program([FuncDecl(Id(KJ), [VarDecl(Id(Z4), ArrayType([47.23, 40.41], NumberType), None, None), VarDecl(Id(wl), StringType, None, None), VarDecl(Id(F9), BoolType, None, None)], Block([Break, AssignStmt(Id(bj), Id(LD)), Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115849))

	def test_21530115850(self):
		input = '''
string kriB
func y7 (bool des, bool yj0i)
	begin
		OVR("Q", z3, hwNF)
		continue
		G5["EKqRa", Ui, "jEQSb"] <- "uNiIP"
	end

func MKm (string OKx[98.19,97.84], string NDli, string irn)
	begin
		if ("ts") kYu(XV, "FFfz")
		elif (xGMm) nq0R(71.0, "uWGIb")
		elif (78.4) for SoOe until 33.52 by "fVlF"
			return "aqOSP"
		elif (20.51)
		begin
			continue
			return
		end
		elif ("Ye") REkX[S9, true] <- 42.93
		else if ("kft")
		for vFmy until "lAByV" by 76.7
			if (iz) number DDBo[70.56,76.43] <- s3
			elif (true)
			continue
			elif (79.75) uY()
			elif ("k")
			lK("xE")
			elif (ar6) if (41.24)
			break
			elif (wE1) return
			elif (false)
			number iiB
			else oKzy <- UU6
			else for vx until false by "qYPi"
				if ("nbZVp")
				break
				elif ("Crm") for MnwU until FZ5 by true
					yYbW(83.36)
				else continue
		elif (LIE)
		return false
		elif (93.72)
		break
		elif ("ikwVM")
		break
		else break
		return "tWpkq"
	end
func XUs ()	return
number AHjX[67.74,79.98] <- 79.59
'''
		expect = '''Program([VarDecl(Id(kriB), StringType, None, None), FuncDecl(Id(y7), [VarDecl(Id(des), BoolType, None, None), VarDecl(Id(yj0i), BoolType, None, None)], Block([CallStmt(Id(OVR), [StringLit(Q), Id(z3), Id(hwNF)]), Continue, AssignStmt(ArrayCell(Id(G5), [StringLit(EKqRa), Id(Ui), StringLit(jEQSb)]), StringLit(uNiIP))])), FuncDecl(Id(MKm), [VarDecl(Id(OKx), ArrayType([98.19, 97.84], StringType), None, None), VarDecl(Id(NDli), StringType, None, None), VarDecl(Id(irn), StringType, None, None)], Block([If((StringLit(ts), CallStmt(Id(kYu), [Id(XV), StringLit(FFfz)])), [(Id(xGMm), CallStmt(Id(nq0R), [NumLit(71.0), StringLit(uWGIb)])), (NumLit(78.4), For(Id(SoOe), NumLit(33.52), StringLit(fVlF), Return(StringLit(aqOSP)))), (NumLit(20.51), Block([Continue, Return()])), (StringLit(Ye), AssignStmt(ArrayCell(Id(REkX), [Id(S9), BooleanLit(True)]), NumLit(42.93)))], If((StringLit(kft), For(Id(vFmy), StringLit(lAByV), NumLit(76.7), If((Id(iz), VarDecl(Id(DDBo), ArrayType([70.56, 76.43], NumberType), None, Id(s3))), [(BooleanLit(True), Continue), (NumLit(79.75), CallStmt(Id(uY), [])), (StringLit(k), CallStmt(Id(lK), [StringLit(xE)])), (Id(ar6), If((NumLit(41.24), Break), [(Id(wE1), Return()), (BooleanLit(False), VarDecl(Id(iiB), NumberType, None, None))], AssignStmt(Id(oKzy), Id(UU6))))], For(Id(vx), BooleanLit(False), StringLit(qYPi), If((StringLit(nbZVp), Break), [(StringLit(Crm), For(Id(MnwU), Id(FZ5), BooleanLit(True), CallStmt(Id(yYbW), [NumLit(83.36)])))], Continue))))), [(Id(LIE), Return(BooleanLit(False))), (NumLit(93.72), Break), (StringLit(ikwVM), Break)], Break)), Return(StringLit(tWpkq))])), FuncDecl(Id(XUs), [], Return()), VarDecl(Id(AHjX), ArrayType([67.74, 79.98], NumberType), None, NumLit(79.59))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115850))

	def test_21530115851(self):
		input = '''
func dg ()	begin
		if ("QyLKb")
		if (82.05) dynamic Q9 <- true
		elif ("xA") bool rvlk
		elif (Si) number YOvZ[33.88,1.13,48.32] <- 99.07
		else QDO <- false
		elif (glKK) continue
		elif (1.73) begin
			return
			VPX(true, true, a30h)
		end
		elif (83.98) break
		else ZGyd(false, "bhgf")
	end

bool Yt
dynamic tqj <- 66.55
func ZSi (string zmb, bool H_P6[78.65], string My[25.43])	return "CxmhF"

func lIq (number f6[17.52,37.18,62.45], bool D1hd, number MrGz)	begin
		continue
	end

'''
		expect = '''Program([FuncDecl(Id(dg), [], Block([If((StringLit(QyLKb), If((NumLit(82.05), VarDecl(Id(Q9), None, dynamic, BooleanLit(True))), [(StringLit(xA), VarDecl(Id(rvlk), BoolType, None, None)), (Id(Si), VarDecl(Id(YOvZ), ArrayType([33.88, 1.13, 48.32], NumberType), None, NumLit(99.07)))], AssignStmt(Id(QDO), BooleanLit(False)))), [(Id(glKK), Continue), (NumLit(1.73), Block([Return(), CallStmt(Id(VPX), [BooleanLit(True), BooleanLit(True), Id(a30h)])])), (NumLit(83.98), Break)], CallStmt(Id(ZGyd), [BooleanLit(False), StringLit(bhgf)]))])), VarDecl(Id(Yt), BoolType, None, None), VarDecl(Id(tqj), None, dynamic, NumLit(66.55)), FuncDecl(Id(ZSi), [VarDecl(Id(zmb), StringType, None, None), VarDecl(Id(H_P6), ArrayType([78.65], BoolType), None, None), VarDecl(Id(My), ArrayType([25.43], StringType), None, None)], Return(StringLit(CxmhF))), FuncDecl(Id(lIq), [VarDecl(Id(f6), ArrayType([17.52, 37.18, 62.45], NumberType), None, None), VarDecl(Id(D1hd), BoolType, None, None), VarDecl(Id(MrGz), NumberType, None, None)], Block([Continue]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115851))

	def test_21530115852(self):
		input = '''
dynamic GwX <- 85.5
'''
		expect = '''Program([VarDecl(Id(GwX), None, dynamic, NumLit(85.5))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115852))

	def test_21530115853(self):
		input = '''
number MKh[97.07,99.33] <- 64.13
string Mf03[28.02]
func h7 (string sHlu[34.38], string UFk, number TBSQ)
	return true

number vvNt[39.81,66.45] <- "OyvYw"
'''
		expect = '''Program([VarDecl(Id(MKh), ArrayType([97.07, 99.33], NumberType), None, NumLit(64.13)), VarDecl(Id(Mf03), ArrayType([28.02], StringType), None, None), FuncDecl(Id(h7), [VarDecl(Id(sHlu), ArrayType([34.38], StringType), None, None), VarDecl(Id(UFk), StringType, None, None), VarDecl(Id(TBSQ), NumberType, None, None)], Return(BooleanLit(True))), VarDecl(Id(vvNt), ArrayType([39.81, 66.45], NumberType), None, StringLit(OyvYw))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115853))

	def test_21530115854(self):
		input = '''
func wP (bool K4V[29.83,6.3], string vo[76.11,46.52,24.12], bool wbRf[34.76,88.79,51.8])	return
'''
		expect = '''Program([FuncDecl(Id(wP), [VarDecl(Id(K4V), ArrayType([29.83, 6.3], BoolType), None, None), VarDecl(Id(vo), ArrayType([76.11, 46.52, 24.12], StringType), None, None), VarDecl(Id(wbRf), ArrayType([34.76, 88.79, 51.8], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115854))

	def test_21530115855(self):
		input = '''
func c9n (bool d5v)	return

string gb2Y <- true
func mjd (string U8w, string EA[45.52,56.67,14.82], number qf8[60.03,45.45])	return

'''
		expect = '''Program([FuncDecl(Id(c9n), [VarDecl(Id(d5v), BoolType, None, None)], Return()), VarDecl(Id(gb2Y), StringType, None, BooleanLit(True)), FuncDecl(Id(mjd), [VarDecl(Id(U8w), StringType, None, None), VarDecl(Id(EA), ArrayType([45.52, 56.67, 14.82], StringType), None, None), VarDecl(Id(qf8), ArrayType([60.03, 45.45], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115855))

	def test_21530115856(self):
		input = '''
func NCTE (bool I9[85.03,42.23])
	begin
		continue
	end
bool yXU <- f6xW
'''
		expect = '''Program([FuncDecl(Id(NCTE), [VarDecl(Id(I9), ArrayType([85.03, 42.23], BoolType), None, None)], Block([Continue])), VarDecl(Id(yXU), BoolType, None, Id(f6xW))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115856))

	def test_21530115857(self):
		input = '''
func q7S (bool xEJ[90.39,58.77,5.69])
	return
func BI ()
	return xe
'''
		expect = '''Program([FuncDecl(Id(q7S), [VarDecl(Id(xEJ), ArrayType([90.39, 58.77, 5.69], BoolType), None, None)], Return()), FuncDecl(Id(BI), [], Return(Id(xe)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115857))

	def test_21530115858(self):
		input = '''
string Ll <- VTB3
func zBpI (bool FN)
	return
func aXs (string bR[6.07,59.49,95.88], number RQVN[62.16], number AYyC[64.98])
	begin
	end
'''
		expect = '''Program([VarDecl(Id(Ll), StringType, None, Id(VTB3)), FuncDecl(Id(zBpI), [VarDecl(Id(FN), BoolType, None, None)], Return()), FuncDecl(Id(aXs), [VarDecl(Id(bR), ArrayType([6.07, 59.49, 95.88], StringType), None, None), VarDecl(Id(RQVN), ArrayType([62.16], NumberType), None, None), VarDecl(Id(AYyC), ArrayType([64.98], NumberType), None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115858))

	def test_21530115859(self):
		input = '''
bool mQ[17.99,38.16] <- true
func CduI (bool Cg)	return

'''
		expect = '''Program([VarDecl(Id(mQ), ArrayType([17.99, 38.16], BoolType), None, BooleanLit(True)), FuncDecl(Id(CduI), [VarDecl(Id(Cg), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115859))

	def test_21530115860(self):
		input = '''
func oh6 (string wOjg[46.68], number qxaW)
	begin
		begin
			return
			YlsS["U", Xt, false] <- true
			if ("oTwr") begin
			end
			elif (29.86)
			continue
			elif (uwWZ) continue
			elif ("kC")
			mWAW["T", gEqo, UWX7] <- VA
			else continue
		end
		oc()
	end
bool VGm <- "Vt"
'''
		expect = '''Program([FuncDecl(Id(oh6), [VarDecl(Id(wOjg), ArrayType([46.68], StringType), None, None), VarDecl(Id(qxaW), NumberType, None, None)], Block([Block([Return(), AssignStmt(ArrayCell(Id(YlsS), [StringLit(U), Id(Xt), BooleanLit(False)]), BooleanLit(True)), If((StringLit(oTwr), Block([])), [(NumLit(29.86), Continue), (Id(uwWZ), Continue), (StringLit(kC), AssignStmt(ArrayCell(Id(mWAW), [StringLit(T), Id(gEqo), Id(UWX7)]), Id(VA)))], Continue)]), CallStmt(Id(oc), [])])), VarDecl(Id(VGm), BoolType, None, StringLit(Vt))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115860))

	def test_21530115861(self):
		input = '''
bool tA <- true
string Es <- 33.03
string Tuw[54.66]
number mi2Q[47.32,57.59]
func qHdb (string RjY)	return

'''
		expect = '''Program([VarDecl(Id(tA), BoolType, None, BooleanLit(True)), VarDecl(Id(Es), StringType, None, NumLit(33.03)), VarDecl(Id(Tuw), ArrayType([54.66], StringType), None, None), VarDecl(Id(mi2Q), ArrayType([47.32, 57.59], NumberType), None, None), FuncDecl(Id(qHdb), [VarDecl(Id(RjY), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115861))

	def test_21530115862(self):
		input = '''
func HM (number RL[1.66], number ek)	begin
		continue
		begin
			for uJRW until true by "W"
				break
			number DoXd[0.65,89.8] <- 26.63
		end
		return
	end

func lS04 (string o2, string WJ[62.2,7.31,52.77], bool GUks[20.1])	return

func xtu ()	begin
		break
		for yf until 81.81 by "Pcqu"
			begin
				begin
					G3[HV, "LvIs", "dh"] <- yx
					m2qT <- "iOL"
				end
				owX(true, true, 70.81)
			end
		Pb[Bxha, iFw, "EGQR"] <- false
	end
number ha[88.79,11.7,86.17]
'''
		expect = '''Program([FuncDecl(Id(HM), [VarDecl(Id(RL), ArrayType([1.66], NumberType), None, None), VarDecl(Id(ek), NumberType, None, None)], Block([Continue, Block([For(Id(uJRW), BooleanLit(True), StringLit(W), Break), VarDecl(Id(DoXd), ArrayType([0.65, 89.8], NumberType), None, NumLit(26.63))]), Return()])), FuncDecl(Id(lS04), [VarDecl(Id(o2), StringType, None, None), VarDecl(Id(WJ), ArrayType([62.2, 7.31, 52.77], StringType), None, None), VarDecl(Id(GUks), ArrayType([20.1], BoolType), None, None)], Return()), FuncDecl(Id(xtu), [], Block([Break, For(Id(yf), NumLit(81.81), StringLit(Pcqu), Block([Block([AssignStmt(ArrayCell(Id(G3), [Id(HV), StringLit(LvIs), StringLit(dh)]), Id(yx)), AssignStmt(Id(m2qT), StringLit(iOL))]), CallStmt(Id(owX), [BooleanLit(True), BooleanLit(True), NumLit(70.81)])])), AssignStmt(ArrayCell(Id(Pb), [Id(Bxha), Id(iFw), StringLit(EGQR)]), BooleanLit(False))])), VarDecl(Id(ha), ArrayType([88.79, 11.7, 86.17], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115862))

	def test_21530115863(self):
		input = '''
func Hi ()
	return
string Cl <- true
func h6 (bool Kzs, string u57P, number cJPr[12.72,58.99,11.65])
	return knE
'''
		expect = '''Program([FuncDecl(Id(Hi), [], Return()), VarDecl(Id(Cl), StringType, None, BooleanLit(True)), FuncDecl(Id(h6), [VarDecl(Id(Kzs), BoolType, None, None), VarDecl(Id(u57P), StringType, None, None), VarDecl(Id(cJPr), ArrayType([12.72, 58.99, 11.65], NumberType), None, None)], Return(Id(knE)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115863))

	def test_21530115864(self):
		input = '''
func FE31 (number uJFT, number hRn[81.69,73.76])	begin
		break
	end

func bBs (string hf7j)
	return "D"
string rr <- "OE"
'''
		expect = '''Program([FuncDecl(Id(FE31), [VarDecl(Id(uJFT), NumberType, None, None), VarDecl(Id(hRn), ArrayType([81.69, 73.76], NumberType), None, None)], Block([Break])), FuncDecl(Id(bBs), [VarDecl(Id(hf7j), StringType, None, None)], Return(StringLit(D))), VarDecl(Id(rr), StringType, None, StringLit(OE))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115864))

	def test_21530115865(self):
		input = '''
number KQ <- "vqn"
'''
		expect = '''Program([VarDecl(Id(KQ), NumberType, None, StringLit(vqn))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115865))

	def test_21530115866(self):
		input = '''
number q350
func rQL (string fL)	begin
		go(false, 87.39)
		return
		break
	end

'''
		expect = '''Program([VarDecl(Id(q350), NumberType, None, None), FuncDecl(Id(rQL), [VarDecl(Id(fL), StringType, None, None)], Block([CallStmt(Id(go), [BooleanLit(False), NumLit(87.39)]), Return(), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115866))

	def test_21530115867(self):
		input = '''
func vSw (number Wm0[7.81,53.31])
	return 81.8
number I3[84.16] <- K0R
bool bGn[88.11]
func p3xo (bool m2, number keIc[58.95,83.0,3.0])	begin
		continue
		if ("vAoG")
		var VF <- Pm
		elif (9.8) number NCu5 <- dd
		else break
		h4e()
	end

'''
		expect = '''Program([FuncDecl(Id(vSw), [VarDecl(Id(Wm0), ArrayType([7.81, 53.31], NumberType), None, None)], Return(NumLit(81.8))), VarDecl(Id(I3), ArrayType([84.16], NumberType), None, Id(K0R)), VarDecl(Id(bGn), ArrayType([88.11], BoolType), None, None), FuncDecl(Id(p3xo), [VarDecl(Id(m2), BoolType, None, None), VarDecl(Id(keIc), ArrayType([58.95, 83.0, 3.0], NumberType), None, None)], Block([Continue, If((StringLit(vAoG), VarDecl(Id(VF), None, var, Id(Pm))), [(NumLit(9.8), VarDecl(Id(NCu5), NumberType, None, Id(dd)))], Break), CallStmt(Id(h4e), [])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115867))

	def test_21530115868(self):
		input = '''
dynamic zj
var HU7c <- true
func jZqD (bool K5C[52.8], bool hg, string J5)	return 69.39

number bg <- 67.86
'''
		expect = '''Program([VarDecl(Id(zj), None, dynamic, None), VarDecl(Id(HU7c), None, var, BooleanLit(True)), FuncDecl(Id(jZqD), [VarDecl(Id(K5C), ArrayType([52.8], BoolType), None, None), VarDecl(Id(hg), BoolType, None, None), VarDecl(Id(J5), StringType, None, None)], Return(NumLit(69.39))), VarDecl(Id(bg), NumberType, None, NumLit(67.86))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115868))

	def test_21530115869(self):
		input = '''
func qB (bool LIb)	begin
		string SoAY <- "ygDB"
	end
number swnj
'''
		expect = '''Program([FuncDecl(Id(qB), [VarDecl(Id(LIb), BoolType, None, None)], Block([VarDecl(Id(SoAY), StringType, None, StringLit(ygDB))])), VarDecl(Id(swnj), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115869))

	def test_21530115870(self):
		input = '''
func kSX (string DcDI[4.62,44.28,93.15], bool jlE[81.33], number HY9)	begin
		rF["SXNTS"] <- w0ik
	end

func op (bool md, bool eMBD[11.55,61.15])	begin
		return
		uTE()
	end
func Tlh (bool Q3JO[17.65])
	return true
number Iyz[0.59]
'''
		expect = '''Program([FuncDecl(Id(kSX), [VarDecl(Id(DcDI), ArrayType([4.62, 44.28, 93.15], StringType), None, None), VarDecl(Id(jlE), ArrayType([81.33], BoolType), None, None), VarDecl(Id(HY9), NumberType, None, None)], Block([AssignStmt(ArrayCell(Id(rF), [StringLit(SXNTS)]), Id(w0ik))])), FuncDecl(Id(op), [VarDecl(Id(md), BoolType, None, None), VarDecl(Id(eMBD), ArrayType([11.55, 61.15], BoolType), None, None)], Block([Return(), CallStmt(Id(uTE), [])])), FuncDecl(Id(Tlh), [VarDecl(Id(Q3JO), ArrayType([17.65], BoolType), None, None)], Return(BooleanLit(True))), VarDecl(Id(Iyz), ArrayType([0.59], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115870))

	def test_21530115871(self):
		input = '''
func Cw3 (bool M5Yk)
	return
func p0M4 ()	begin
		uhW3 <- true
		if ("LJsU") return false
		elif (50.44) number ADm <- "p"
		elif (vbq) number Pu6u[23.32,69.92,64.36] <- Afy
		elif (hb)
		ZE()
		else return PMhl
	end

'''
		expect = '''Program([FuncDecl(Id(Cw3), [VarDecl(Id(M5Yk), BoolType, None, None)], Return()), FuncDecl(Id(p0M4), [], Block([AssignStmt(Id(uhW3), BooleanLit(True)), If((StringLit(LJsU), Return(BooleanLit(False))), [(NumLit(50.44), VarDecl(Id(ADm), NumberType, None, StringLit(p))), (Id(vbq), VarDecl(Id(Pu6u), ArrayType([23.32, 69.92, 64.36], NumberType), None, Id(Afy))), (Id(hb), CallStmt(Id(ZE), []))], Return(Id(PMhl)))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115871))

	def test_21530115872(self):
		input = '''
string FdYy <- 39.79
'''
		expect = '''Program([VarDecl(Id(FdYy), StringType, None, NumLit(39.79))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115872))

	def test_21530115873(self):
		input = '''
func NoO (number hJb[21.23,27.13,69.6], string pP, number V5[95.48,82.76,11.95])
	return 0.73

func Md (number BJ9, string jhfq, number Mpz[90.94,29.87,15.43])
	return

'''
		expect = '''Program([FuncDecl(Id(NoO), [VarDecl(Id(hJb), ArrayType([21.23, 27.13, 69.6], NumberType), None, None), VarDecl(Id(pP), StringType, None, None), VarDecl(Id(V5), ArrayType([95.48, 82.76, 11.95], NumberType), None, None)], Return(NumLit(0.73))), FuncDecl(Id(Md), [VarDecl(Id(BJ9), NumberType, None, None), VarDecl(Id(jhfq), StringType, None, None), VarDecl(Id(Mpz), ArrayType([90.94, 29.87, 15.43], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115873))

	def test_21530115874(self):
		input = '''
func c1ie (string pC, number cW)
	return

'''
		expect = '''Program([FuncDecl(Id(c1ie), [VarDecl(Id(pC), StringType, None, None), VarDecl(Id(cW), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115874))

	def test_21530115875(self):
		input = '''
bool wur0[27.97]
'''
		expect = '''Program([VarDecl(Id(wur0), ArrayType([27.97], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115875))

	def test_21530115876(self):
		input = '''
func CKNM ()
	return
var BlI <- 89.86
bool D9zP[91.77] <- 95.76
dynamic jm
func ntM (bool S6ZR)
	begin
		break
		begin
		end
	end

'''
		expect = '''Program([FuncDecl(Id(CKNM), [], Return()), VarDecl(Id(BlI), None, var, NumLit(89.86)), VarDecl(Id(D9zP), ArrayType([91.77], BoolType), None, NumLit(95.76)), VarDecl(Id(jm), None, dynamic, None), FuncDecl(Id(ntM), [VarDecl(Id(S6ZR), BoolType, None, None)], Block([Break, Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115876))

	def test_21530115877(self):
		input = '''
string Fs[91.65,29.01,29.83] <- false
func r4j (string X6WL[22.78,40.86], string NOKf[64.64,32.53])	return

bool TLIw <- "ZYY"
'''
		expect = '''Program([VarDecl(Id(Fs), ArrayType([91.65, 29.01, 29.83], StringType), None, BooleanLit(False)), FuncDecl(Id(r4j), [VarDecl(Id(X6WL), ArrayType([22.78, 40.86], StringType), None, None), VarDecl(Id(NOKf), ArrayType([64.64, 32.53], StringType), None, None)], Return()), VarDecl(Id(TLIw), BoolType, None, StringLit(ZYY))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115877))

	def test_21530115878(self):
		input = '''
func YJ2j (bool TCxI[65.35], number YkC, number cZj[38.05,88.05,50.13])
	begin
		break
		string oJk
		begin
			bool el
			if ("GaBp") break
			elif (65.0) break
			elif (false)
			if (13.13)
			bool xwN[59.97] <- 43.86
			elif (false) dynamic xfJ
			elif (Gx)
			if ("gsg")
			begin
			end
			else begin
				for n4Q until false by dL
					if (gP7) begin
						begin
							return true
						end
						Br[68.88, "RaMr", true] <- z3
						string iJ[55.65] <- 65.65
					end
					elif (true)
					stkN()
					elif (3.7)
					continue
					else u_G(Me)
				zr[y7vx] <- 69.33
				if (false) for W5eB until 74.49 by 25.83
					number arT <- true
				elif (I3rK) fZRb(67.42, false, true)
				elif (96.7) break
				elif (GFUE) begin
					Lu[98.62] <- true
					break
				end
				elif (lK4)
				break
				elif (true)
				for Xw34 until Lh2S by "cy"
					continue
				else begin
				end
			end
			elif (xQsH) break
			else continue
			elif (65.96)
			continue
			elif ("xvSzk") for KDdn until rIFM by "oE"
				continue
			else if (69.65)
			for VB8e until 89.17 by Jq
				string AV[59.24,92.65,19.38] <- true
			elif (true) cP0()
			elif (false) KTyV(true)
			elif (46.2) continue
			elif (true)
			vc()
		end
	end

'''
		expect = '''Program([FuncDecl(Id(YJ2j), [VarDecl(Id(TCxI), ArrayType([65.35], BoolType), None, None), VarDecl(Id(YkC), NumberType, None, None), VarDecl(Id(cZj), ArrayType([38.05, 88.05, 50.13], NumberType), None, None)], Block([Break, VarDecl(Id(oJk), StringType, None, None), Block([VarDecl(Id(el), BoolType, None, None), If((StringLit(GaBp), Break), [(NumLit(65.0), Break), (BooleanLit(False), If((NumLit(13.13), VarDecl(Id(xwN), ArrayType([59.97], BoolType), None, NumLit(43.86))), [(BooleanLit(False), VarDecl(Id(xfJ), None, dynamic, None)), (Id(Gx), If((StringLit(gsg), Block([])), [], Block([For(Id(n4Q), BooleanLit(False), Id(dL), If((Id(gP7), Block([Block([Return(BooleanLit(True))]), AssignStmt(ArrayCell(Id(Br), [NumLit(68.88), StringLit(RaMr), BooleanLit(True)]), Id(z3)), VarDecl(Id(iJ), ArrayType([55.65], StringType), None, NumLit(65.65))])), [(BooleanLit(True), CallStmt(Id(stkN), [])), (NumLit(3.7), Continue)], CallStmt(Id(u_G), [Id(Me)]))), AssignStmt(ArrayCell(Id(zr), [Id(y7vx)]), NumLit(69.33)), If((BooleanLit(False), For(Id(W5eB), NumLit(74.49), NumLit(25.83), VarDecl(Id(arT), NumberType, None, BooleanLit(True)))), [(Id(I3rK), CallStmt(Id(fZRb), [NumLit(67.42), BooleanLit(False), BooleanLit(True)])), (NumLit(96.7), Break), (Id(GFUE), Block([AssignStmt(ArrayCell(Id(Lu), [NumLit(98.62)]), BooleanLit(True)), Break])), (Id(lK4), Break), (BooleanLit(True), For(Id(Xw34), Id(Lh2S), StringLit(cy), Continue))], Block([]))]))), (Id(xQsH), Break)], Continue)), (NumLit(65.96), Continue), (StringLit(xvSzk), For(Id(KDdn), Id(rIFM), StringLit(oE), Continue))], If((NumLit(69.65), For(Id(VB8e), NumLit(89.17), Id(Jq), VarDecl(Id(AV), ArrayType([59.24, 92.65, 19.38], StringType), None, BooleanLit(True)))), [(BooleanLit(True), CallStmt(Id(cP0), [])), (BooleanLit(False), CallStmt(Id(KTyV), [BooleanLit(True)])), (NumLit(46.2), Continue), (BooleanLit(True), CallStmt(Id(vc), []))], None))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115878))

	def test_21530115879(self):
		input = '''
number lk[46.78,15.38,77.26] <- false
'''
		expect = '''Program([VarDecl(Id(lk), ArrayType([46.78, 15.38, 77.26], NumberType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115879))

	def test_21530115880(self):
		input = '''
func QQ (string BPyT[10.62], string LcPV[65.71,76.03,47.58])	return "bSm"

string nth[18.62] <- Syz
dynamic Qy <- "yJM"
func QqF (bool C1)
	return "loyUf"

'''
		expect = '''Program([FuncDecl(Id(QQ), [VarDecl(Id(BPyT), ArrayType([10.62], StringType), None, None), VarDecl(Id(LcPV), ArrayType([65.71, 76.03, 47.58], StringType), None, None)], Return(StringLit(bSm))), VarDecl(Id(nth), ArrayType([18.62], StringType), None, Id(Syz)), VarDecl(Id(Qy), None, dynamic, StringLit(yJM)), FuncDecl(Id(QqF), [VarDecl(Id(C1), BoolType, None, None)], Return(StringLit(loyUf)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115880))

	def test_21530115881(self):
		input = '''
number GZ[10.04,32.41,43.59] <- 7.83
number pdAx[79.01,62.08,90.81] <- "k"
func TMZ (number l8, bool HBX5[90.36,13.08,72.98])
	return
number zaL[51.41,74.48,53.67]
func rF7v (bool HgS, number Nl[91.06,27.32], number fO[99.58])	return
'''
		expect = '''Program([VarDecl(Id(GZ), ArrayType([10.04, 32.41, 43.59], NumberType), None, NumLit(7.83)), VarDecl(Id(pdAx), ArrayType([79.01, 62.08, 90.81], NumberType), None, StringLit(k)), FuncDecl(Id(TMZ), [VarDecl(Id(l8), NumberType, None, None), VarDecl(Id(HBX5), ArrayType([90.36, 13.08, 72.98], BoolType), None, None)], Return()), VarDecl(Id(zaL), ArrayType([51.41, 74.48, 53.67], NumberType), None, None), FuncDecl(Id(rF7v), [VarDecl(Id(HgS), BoolType, None, None), VarDecl(Id(Nl), ArrayType([91.06, 27.32], NumberType), None, None), VarDecl(Id(fO), ArrayType([99.58], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115881))

	def test_21530115882(self):
		input = '''
number tJW[10.75,14.4,12.77]
'''
		expect = '''Program([VarDecl(Id(tJW), ArrayType([10.75, 14.4, 12.77], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115882))

	def test_21530115883(self):
		input = '''
bool vpU[75.92,24.91,36.69] <- "W"
bool cFi
'''
		expect = '''Program([VarDecl(Id(vpU), ArrayType([75.92, 24.91, 36.69], BoolType), None, StringLit(W)), VarDecl(Id(cFi), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115883))

	def test_21530115884(self):
		input = '''
func RTe (number V6)
	return 93.98
func tv (number w4[24.36])	return
'''
		expect = '''Program([FuncDecl(Id(RTe), [VarDecl(Id(V6), NumberType, None, None)], Return(NumLit(93.98))), FuncDecl(Id(tv), [VarDecl(Id(w4), ArrayType([24.36], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115884))

	def test_21530115885(self):
		input = '''
number s13Z
'''
		expect = '''Program([VarDecl(Id(s13Z), NumberType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115885))

	def test_21530115886(self):
		input = '''
bool Rfar[39.95,38.33,25.2]
number dGo_
bool EE[30.75,32.92] <- 59.56
func Ha (number Iex[82.69,59.02], bool cLZI)	return

func As9 (bool lI0m, string LI5n[47.19], string sU)	return

'''
		expect = '''Program([VarDecl(Id(Rfar), ArrayType([39.95, 38.33, 25.2], BoolType), None, None), VarDecl(Id(dGo_), NumberType, None, None), VarDecl(Id(EE), ArrayType([30.75, 32.92], BoolType), None, NumLit(59.56)), FuncDecl(Id(Ha), [VarDecl(Id(Iex), ArrayType([82.69, 59.02], NumberType), None, None), VarDecl(Id(cLZI), BoolType, None, None)], Return()), FuncDecl(Id(As9), [VarDecl(Id(lI0m), BoolType, None, None), VarDecl(Id(LI5n), ArrayType([47.19], StringType), None, None), VarDecl(Id(sU), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115886))

	def test_21530115887(self):
		input = '''
number jPR
bool hU[35.2,65.91,61.74] <- "MdyG"
func q2y5 (number qg[28.82], string oEop)	begin
		if (19.16)
		continue
		elif (88.22)
		SU <- GUeT
		elif (39.66)
		break
		for gf0 until 63.89 by R3c4
			aJBg <- "dVdJi"
		begin
			break
			for fFtM until "x" by 74.08
				bGX(CD)
		end
	end
'''
		expect = '''Program([VarDecl(Id(jPR), NumberType, None, None), VarDecl(Id(hU), ArrayType([35.2, 65.91, 61.74], BoolType), None, StringLit(MdyG)), FuncDecl(Id(q2y5), [VarDecl(Id(qg), ArrayType([28.82], NumberType), None, None), VarDecl(Id(oEop), StringType, None, None)], Block([If((NumLit(19.16), Continue), [(NumLit(88.22), AssignStmt(Id(SU), Id(GUeT))), (NumLit(39.66), Break)], None), For(Id(gf0), NumLit(63.89), Id(R3c4), AssignStmt(Id(aJBg), StringLit(dVdJi))), Block([Break, For(Id(fFtM), StringLit(x), NumLit(74.08), CallStmt(Id(bGX), [Id(CD)]))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115887))

	def test_21530115888(self):
		input = '''
func KLuf (string rtL[43.98,2.37,8.86], bool EuQq)	return "nPn"
bool pME
string vMO1[6.61,42.84,96.8] <- 99.78
'''
		expect = '''Program([FuncDecl(Id(KLuf), [VarDecl(Id(rtL), ArrayType([43.98, 2.37, 8.86], StringType), None, None), VarDecl(Id(EuQq), BoolType, None, None)], Return(StringLit(nPn))), VarDecl(Id(pME), BoolType, None, None), VarDecl(Id(vMO1), ArrayType([6.61, 42.84, 96.8], StringType), None, NumLit(99.78))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115888))

	def test_21530115889(self):
		input = '''
bool GjZN[79.7] <- "rVmZy"
func zlEK (number b9)	return
func Uu (number kUf)	return 61.75

dynamic lO6u <- "QM"
func EI ()
	return "D"

'''
		expect = '''Program([VarDecl(Id(GjZN), ArrayType([79.7], BoolType), None, StringLit(rVmZy)), FuncDecl(Id(zlEK), [VarDecl(Id(b9), NumberType, None, None)], Return()), FuncDecl(Id(Uu), [VarDecl(Id(kUf), NumberType, None, None)], Return(NumLit(61.75))), VarDecl(Id(lO6u), None, dynamic, StringLit(QM)), FuncDecl(Id(EI), [], Return(StringLit(D)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115889))

	def test_21530115890(self):
		input = '''
bool Q9ue[90.93,17.48] <- 65.63
func gN (string sd)
	return UmE
bool kMJT[28.73,45.93] <- "wyxM"
bool vz5
func NCo ()
	return

'''
		expect = '''Program([VarDecl(Id(Q9ue), ArrayType([90.93, 17.48], BoolType), None, NumLit(65.63)), FuncDecl(Id(gN), [VarDecl(Id(sd), StringType, None, None)], Return(Id(UmE))), VarDecl(Id(kMJT), ArrayType([28.73, 45.93], BoolType), None, StringLit(wyxM)), VarDecl(Id(vz5), BoolType, None, None), FuncDecl(Id(NCo), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115890))

	def test_21530115891(self):
		input = '''
func dnA5 (number JB[91.86,72.56], string mD[75.77])	begin
	end
number ZUd[46.05] <- "KjZF"
func fNGL (string yZnl)
	return

func xoF (number Sba, string yw, bool i8zt)	return

'''
		expect = '''Program([FuncDecl(Id(dnA5), [VarDecl(Id(JB), ArrayType([91.86, 72.56], NumberType), None, None), VarDecl(Id(mD), ArrayType([75.77], StringType), None, None)], Block([])), VarDecl(Id(ZUd), ArrayType([46.05], NumberType), None, StringLit(KjZF)), FuncDecl(Id(fNGL), [VarDecl(Id(yZnl), StringType, None, None)], Return()), FuncDecl(Id(xoF), [VarDecl(Id(Sba), NumberType, None, None), VarDecl(Id(yw), StringType, None, None), VarDecl(Id(i8zt), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115891))

	def test_21530115892(self):
		input = '''
string HOpi <- true
func DZV (string dm2t, bool rp9b, string KTp)	return false

func lRW ()	begin
		begin
			bool EdE9[66.46,10.86,85.52] <- false
			break
		end
		NG6h <- false
		if (PAe) continue
		elif ("CaW")
		return
		elif ("Px")
		continue
		elif (95.68)
		DY2r(85.38, false)
		elif ("oljk") if (true) break
		elif ("PfrIX")
		break
		elif (17.26)
		i7("avuZH", qT)
		elif (false) V2h(Mba, yg)
		elif ("WNjT")
		begin
			for u7 until true by false
				return
			BFG <- tu
		end
		elif ("Oqw")
		continue
	end
func dBM (bool ygw[58.59,15.49], bool wjcI)	return
'''
		expect = '''Program([VarDecl(Id(HOpi), StringType, None, BooleanLit(True)), FuncDecl(Id(DZV), [VarDecl(Id(dm2t), StringType, None, None), VarDecl(Id(rp9b), BoolType, None, None), VarDecl(Id(KTp), StringType, None, None)], Return(BooleanLit(False))), FuncDecl(Id(lRW), [], Block([Block([VarDecl(Id(EdE9), ArrayType([66.46, 10.86, 85.52], BoolType), None, BooleanLit(False)), Break]), AssignStmt(Id(NG6h), BooleanLit(False)), If((Id(PAe), Continue), [(StringLit(CaW), Return()), (StringLit(Px), Continue), (NumLit(95.68), CallStmt(Id(DY2r), [NumLit(85.38), BooleanLit(False)])), (StringLit(oljk), If((BooleanLit(True), Break), [(StringLit(PfrIX), Break), (NumLit(17.26), CallStmt(Id(i7), [StringLit(avuZH), Id(qT)])), (BooleanLit(False), CallStmt(Id(V2h), [Id(Mba), Id(yg)])), (StringLit(WNjT), Block([For(Id(u7), BooleanLit(True), BooleanLit(False), Return()), AssignStmt(Id(BFG), Id(tu))])), (StringLit(Oqw), Continue)], None))], None)])), FuncDecl(Id(dBM), [VarDecl(Id(ygw), ArrayType([58.59, 15.49], BoolType), None, None), VarDecl(Id(wjcI), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115892))

	def test_21530115893(self):
		input = '''
string jz
func Mj (string fH[46.36,49.03,95.5])
	begin
	end

func xdG (number RlEC[88.4,25.39,15.96], bool IL[98.26,92.25,91.72], number Q5cr[4.81])	return
'''
		expect = '''Program([VarDecl(Id(jz), StringType, None, None), FuncDecl(Id(Mj), [VarDecl(Id(fH), ArrayType([46.36, 49.03, 95.5], StringType), None, None)], Block([])), FuncDecl(Id(xdG), [VarDecl(Id(RlEC), ArrayType([88.4, 25.39, 15.96], NumberType), None, None), VarDecl(Id(IL), ArrayType([98.26, 92.25, 91.72], BoolType), None, None), VarDecl(Id(Q5cr), ArrayType([4.81], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115893))

	def test_21530115894(self):
		input = '''
func Q5 (bool vLbA)	return
func ra (bool Cz[8.69,22.59,15.79])	return
func Gq (number Hj)	return "Ix"
string Eauu[38.65,21.52,21.02]
'''
		expect = '''Program([FuncDecl(Id(Q5), [VarDecl(Id(vLbA), BoolType, None, None)], Return()), FuncDecl(Id(ra), [VarDecl(Id(Cz), ArrayType([8.69, 22.59, 15.79], BoolType), None, None)], Return()), FuncDecl(Id(Gq), [VarDecl(Id(Hj), NumberType, None, None)], Return(StringLit(Ix))), VarDecl(Id(Eauu), ArrayType([38.65, 21.52, 21.02], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115894))

	def test_21530115895(self):
		input = '''
dynamic xU
func MJ8f (string sTT[63.77,56.17,60.74])	return

string tl[3.94,6.21,69.87]
func yA (number Wh[76.16])	begin
		begin
			ay()
			O7gi["a", "W"] <- 37.57
		end
	end

'''
		expect = '''Program([VarDecl(Id(xU), None, dynamic, None), FuncDecl(Id(MJ8f), [VarDecl(Id(sTT), ArrayType([63.77, 56.17, 60.74], StringType), None, None)], Return()), VarDecl(Id(tl), ArrayType([3.94, 6.21, 69.87], StringType), None, None), FuncDecl(Id(yA), [VarDecl(Id(Wh), ArrayType([76.16], NumberType), None, None)], Block([Block([CallStmt(Id(ay), []), AssignStmt(ArrayCell(Id(O7gi), [StringLit(a), StringLit(W)]), NumLit(37.57))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115895))

	def test_21530115896(self):
		input = '''
func H4bs (number Mla, string xn1b, bool P9M)
	return "HBVZk"

func ekp4 (number Omm, bool j4FG[72.88,94.04], string EF[81.21])
	return nV
string YL[29.25,78.99]
bool D6R[84.57]
bool tvD <- 20.05
'''
		expect = '''Program([FuncDecl(Id(H4bs), [VarDecl(Id(Mla), NumberType, None, None), VarDecl(Id(xn1b), StringType, None, None), VarDecl(Id(P9M), BoolType, None, None)], Return(StringLit(HBVZk))), FuncDecl(Id(ekp4), [VarDecl(Id(Omm), NumberType, None, None), VarDecl(Id(j4FG), ArrayType([72.88, 94.04], BoolType), None, None), VarDecl(Id(EF), ArrayType([81.21], StringType), None, None)], Return(Id(nV))), VarDecl(Id(YL), ArrayType([29.25, 78.99], StringType), None, None), VarDecl(Id(D6R), ArrayType([84.57], BoolType), None, None), VarDecl(Id(tvD), BoolType, None, NumLit(20.05))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115896))

	def test_21530115897(self):
		input = '''
func m7 (bool FuF[65.96,73.03])	begin
		string COQb[33.53,12.23]
		return
	end

func sWv ()
	return true

number Ew1[50.06] <- "RMSE"
'''
		expect = '''Program([FuncDecl(Id(m7), [VarDecl(Id(FuF), ArrayType([65.96, 73.03], BoolType), None, None)], Block([VarDecl(Id(COQb), ArrayType([33.53, 12.23], StringType), None, None), Return()])), FuncDecl(Id(sWv), [], Return(BooleanLit(True))), VarDecl(Id(Ew1), ArrayType([50.06], NumberType), None, StringLit(RMSE))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115897))

	def test_21530115898(self):
		input = '''
number F3YQ[5.84] <- "jyd"
dynamic v9n
func gUco (string wLUn)
	return
func D9uL (number g4[29.98], string v207[37.41], number WkmW[32.33,56.33,90.03])
	begin
		begin
			if (false) begin
				for OUQ until 15.44 by IfP
					return 33.17
				V9Q <- 28.02
			end
			elif ("pk") bool M0[79.83]
			elif (mFH)
			return
			elif (96.79) for vGI until "kDxVA" by true
				return
			elif ("gBWC") uBi(69.5, yVIS)
			else for RueJ until "Ndltr" by 10.01
				oY <- 92.3
		end
		begin
			break
			j54O(false, false)
		end
		string zrl[64.31,26.15]
	end

var gdr <- SySp
'''
		expect = '''Program([VarDecl(Id(F3YQ), ArrayType([5.84], NumberType), None, StringLit(jyd)), VarDecl(Id(v9n), None, dynamic, None), FuncDecl(Id(gUco), [VarDecl(Id(wLUn), StringType, None, None)], Return()), FuncDecl(Id(D9uL), [VarDecl(Id(g4), ArrayType([29.98], NumberType), None, None), VarDecl(Id(v207), ArrayType([37.41], StringType), None, None), VarDecl(Id(WkmW), ArrayType([32.33, 56.33, 90.03], NumberType), None, None)], Block([Block([If((BooleanLit(False), Block([For(Id(OUQ), NumLit(15.44), Id(IfP), Return(NumLit(33.17))), AssignStmt(Id(V9Q), NumLit(28.02))])), [(StringLit(pk), VarDecl(Id(M0), ArrayType([79.83], BoolType), None, None)), (Id(mFH), Return()), (NumLit(96.79), For(Id(vGI), StringLit(kDxVA), BooleanLit(True), Return())), (StringLit(gBWC), CallStmt(Id(uBi), [NumLit(69.5), Id(yVIS)]))], For(Id(RueJ), StringLit(Ndltr), NumLit(10.01), AssignStmt(Id(oY), NumLit(92.3))))]), Block([Break, CallStmt(Id(j54O), [BooleanLit(False), BooleanLit(False)])]), VarDecl(Id(zrl), ArrayType([64.31, 26.15], StringType), None, None)])), VarDecl(Id(gdr), None, var, Id(SySp))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115898))

	def test_21530115899(self):
		input = '''
func Hk ()	return
func Md02 (bool STh, number BA6[67.89], bool xl[84.26,41.96,45.38])	return true

func Bw5 (string oT[6.41,4.08], string po[37.58,13.41,41.93], string SX1[51.27])	begin
		break
		if (true) break
		elif (uR) number cQ[69.62,27.92,74.2] <- i9gj
	end

'''
		expect = '''Program([FuncDecl(Id(Hk), [], Return()), FuncDecl(Id(Md02), [VarDecl(Id(STh), BoolType, None, None), VarDecl(Id(BA6), ArrayType([67.89], NumberType), None, None), VarDecl(Id(xl), ArrayType([84.26, 41.96, 45.38], BoolType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(Bw5), [VarDecl(Id(oT), ArrayType([6.41, 4.08], StringType), None, None), VarDecl(Id(po), ArrayType([37.58, 13.41, 41.93], StringType), None, None), VarDecl(Id(SX1), ArrayType([51.27], StringType), None, None)], Block([Break, If((BooleanLit(True), Break), [(Id(uR), VarDecl(Id(cQ), ArrayType([69.62, 27.92, 74.2], NumberType), None, Id(i9gj)))], None)]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115899))

	def test_21530115900(self):
		input = '''
number j7kp
string W2P[64.53]
'''
		expect = '''Program([VarDecl(Id(j7kp), NumberType, None, None), VarDecl(Id(W2P), ArrayType([64.53], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115900))

	def test_21530115901(self):
		input = '''
func Lr (bool GGu)	return

number J_3 <- "QK"
func MJI (string zB[84.7], number ZBBC[8.8,27.05], number e0)	return GFo

func Heb (number UUYe)	return
'''
		expect = '''Program([FuncDecl(Id(Lr), [VarDecl(Id(GGu), BoolType, None, None)], Return()), VarDecl(Id(J_3), NumberType, None, StringLit(QK)), FuncDecl(Id(MJI), [VarDecl(Id(zB), ArrayType([84.7], StringType), None, None), VarDecl(Id(ZBBC), ArrayType([8.8, 27.05], NumberType), None, None), VarDecl(Id(e0), NumberType, None, None)], Return(Id(GFo))), FuncDecl(Id(Heb), [VarDecl(Id(UUYe), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115901))

	def test_21530115902(self):
		input = '''
number QMt[53.94] <- 88.04
var kP <- 88.71
var C6e6 <- zfD
func DR (number q3vP, number Bsal)
	begin
		if (true) begin
		end
		elif (83.82) continue
		elif (bon) JhRM(sR9V)
		else continue
		break
		if (true)
		return
		elif (false) if (Kc) break
		elif (false)
		begin
		end
		elif ("N")
		string gU[91.63,43.91,59.93]
		elif ("Xk") for Rfd until true by 86.71
			yqO(false, 56.61, "qi")
		elif (false)
		break
		else bgI["qC"] <- "wFce"
		elif (true) var IPo <- "sWqMm"
	end

var SD <- QBw
'''
		expect = '''Program([VarDecl(Id(QMt), ArrayType([53.94], NumberType), None, NumLit(88.04)), VarDecl(Id(kP), None, var, NumLit(88.71)), VarDecl(Id(C6e6), None, var, Id(zfD)), FuncDecl(Id(DR), [VarDecl(Id(q3vP), NumberType, None, None), VarDecl(Id(Bsal), NumberType, None, None)], Block([If((BooleanLit(True), Block([])), [(NumLit(83.82), Continue), (Id(bon), CallStmt(Id(JhRM), [Id(sR9V)]))], Continue), Break, If((BooleanLit(True), Return()), [(BooleanLit(False), If((Id(Kc), Break), [(BooleanLit(False), Block([])), (StringLit(N), VarDecl(Id(gU), ArrayType([91.63, 43.91, 59.93], StringType), None, None)), (StringLit(Xk), For(Id(Rfd), BooleanLit(True), NumLit(86.71), CallStmt(Id(yqO), [BooleanLit(False), NumLit(56.61), StringLit(qi)]))), (BooleanLit(False), Break)], AssignStmt(ArrayCell(Id(bgI), [StringLit(qC)]), StringLit(wFce)))), (BooleanLit(True), VarDecl(Id(IPo), None, var, StringLit(sWqMm)))], None)])), VarDecl(Id(SD), None, var, Id(QBw))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115902))

	def test_21530115903(self):
		input = '''
func bvo ()
	return
dynamic VW <- "XJ"
func sok (string cv2A[42.38], number m1H, string cnLn)	begin
		for V9y until 94.61 by "dUhn"
			return uj_o
		for D_ until false by true
			for Gwi until C9Pt by true
				string yx <- a4h
	end
bool sn5c <- 73.81
func lAz (number Vm8[12.98], bool Zc[54.74,95.53])	return

'''
		expect = '''Program([FuncDecl(Id(bvo), [], Return()), VarDecl(Id(VW), None, dynamic, StringLit(XJ)), FuncDecl(Id(sok), [VarDecl(Id(cv2A), ArrayType([42.38], StringType), None, None), VarDecl(Id(m1H), NumberType, None, None), VarDecl(Id(cnLn), StringType, None, None)], Block([For(Id(V9y), NumLit(94.61), StringLit(dUhn), Return(Id(uj_o))), For(Id(D_), BooleanLit(False), BooleanLit(True), For(Id(Gwi), Id(C9Pt), BooleanLit(True), VarDecl(Id(yx), StringType, None, Id(a4h))))])), VarDecl(Id(sn5c), BoolType, None, NumLit(73.81)), FuncDecl(Id(lAz), [VarDecl(Id(Vm8), ArrayType([12.98], NumberType), None, None), VarDecl(Id(Zc), ArrayType([54.74, 95.53], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115903))

	def test_21530115904(self):
		input = '''
func FxYl (number Y93[83.98,83.46,87.91])
	return "N"

var dh <- madp
'''
		expect = '''Program([FuncDecl(Id(FxYl), [VarDecl(Id(Y93), ArrayType([83.98, 83.46, 87.91], NumberType), None, None)], Return(StringLit(N))), VarDecl(Id(dh), None, var, Id(madp))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115904))

	def test_21530115905(self):
		input = '''
string dY <- false
func Pk (string SGc[76.44,98.96,11.62], bool GN, string vG)	begin
	end
var gT <- nlM
func Hcbi (string pOgh)
	return Wx3

func fS (bool vDD[77.25], number dU)
	return

'''
		expect = '''Program([VarDecl(Id(dY), StringType, None, BooleanLit(False)), FuncDecl(Id(Pk), [VarDecl(Id(SGc), ArrayType([76.44, 98.96, 11.62], StringType), None, None), VarDecl(Id(GN), BoolType, None, None), VarDecl(Id(vG), StringType, None, None)], Block([])), VarDecl(Id(gT), None, var, Id(nlM)), FuncDecl(Id(Hcbi), [VarDecl(Id(pOgh), StringType, None, None)], Return(Id(Wx3))), FuncDecl(Id(fS), [VarDecl(Id(vDD), ArrayType([77.25], BoolType), None, None), VarDecl(Id(dU), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115905))

	def test_21530115906(self):
		input = '''
var kvw <- YcW9
func M4 ()	return 26.29

func Wm ()
	begin
		for Of6j until Lz6v by 84.7
			begin
			end
		for P54_ until "KaAX" by false
			rR("D", 18.51, true)
		fhzN(49.57, "AO", 34.33)
	end
bool hje
string YHp <- "p"
'''
		expect = '''Program([VarDecl(Id(kvw), None, var, Id(YcW9)), FuncDecl(Id(M4), [], Return(NumLit(26.29))), FuncDecl(Id(Wm), [], Block([For(Id(Of6j), Id(Lz6v), NumLit(84.7), Block([])), For(Id(P54_), StringLit(KaAX), BooleanLit(False), CallStmt(Id(rR), [StringLit(D), NumLit(18.51), BooleanLit(True)])), CallStmt(Id(fhzN), [NumLit(49.57), StringLit(AO), NumLit(34.33)])])), VarDecl(Id(hje), BoolType, None, None), VarDecl(Id(YHp), StringType, None, StringLit(p))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115906))

	def test_21530115907(self):
		input = '''
func zI9p (number XY[60.01], bool bv[53.57,75.89], number wEa[64.29,86.53])	return

bool y54[14.49]
'''
		expect = '''Program([FuncDecl(Id(zI9p), [VarDecl(Id(XY), ArrayType([60.01], NumberType), None, None), VarDecl(Id(bv), ArrayType([53.57, 75.89], BoolType), None, None), VarDecl(Id(wEa), ArrayType([64.29, 86.53], NumberType), None, None)], Return()), VarDecl(Id(y54), ArrayType([14.49], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115907))

	def test_21530115908(self):
		input = '''
number Ka[65.49,65.1,18.35] <- "u"
'''
		expect = '''Program([VarDecl(Id(Ka), ArrayType([65.49, 65.1, 18.35], NumberType), None, StringLit(u))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115908))

	def test_21530115909(self):
		input = '''
number Rk[9.81,51.37] <- vwaY
func cGp (number uo[51.68], bool qdQ, string ue[44.4])	return

'''
		expect = '''Program([VarDecl(Id(Rk), ArrayType([9.81, 51.37], NumberType), None, Id(vwaY)), FuncDecl(Id(cGp), [VarDecl(Id(uo), ArrayType([51.68], NumberType), None, None), VarDecl(Id(qdQ), BoolType, None, None), VarDecl(Id(ue), ArrayType([44.4], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115909))

	def test_21530115910(self):
		input = '''
number pz[66.73]
string psBH[36.32,59.33]
func r5u (bool c7sO)	begin
		return true
		return
		return "mGisY"
	end

'''
		expect = '''Program([VarDecl(Id(pz), ArrayType([66.73], NumberType), None, None), VarDecl(Id(psBH), ArrayType([36.32, 59.33], StringType), None, None), FuncDecl(Id(r5u), [VarDecl(Id(c7sO), BoolType, None, None)], Block([Return(BooleanLit(True)), Return(), Return(StringLit(mGisY))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115910))

	def test_21530115911(self):
		input = '''
func P6I (number Z6o[55.27,90.73])	begin
	end

func ZD (number PF, string a64G[44.36,5.49,27.82], string Iga)
	return "yJW"

'''
		expect = '''Program([FuncDecl(Id(P6I), [VarDecl(Id(Z6o), ArrayType([55.27, 90.73], NumberType), None, None)], Block([])), FuncDecl(Id(ZD), [VarDecl(Id(PF), NumberType, None, None), VarDecl(Id(a64G), ArrayType([44.36, 5.49, 27.82], StringType), None, None), VarDecl(Id(Iga), StringType, None, None)], Return(StringLit(yJW)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115911))

	def test_21530115912(self):
		input = '''
bool S0
bool COT3 <- "CGkHG"
var AXX <- "wvyl"
number IZ[61.48,96.63,43.82] <- "HWwq"
'''
		expect = '''Program([VarDecl(Id(S0), BoolType, None, None), VarDecl(Id(COT3), BoolType, None, StringLit(CGkHG)), VarDecl(Id(AXX), None, var, StringLit(wvyl)), VarDecl(Id(IZ), ArrayType([61.48, 96.63, 43.82], NumberType), None, StringLit(HWwq))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115912))

	def test_21530115913(self):
		input = '''
func yvV (bool K7, string Y_C)	return

func nA2 (number vS, bool nr, number jGF)
	return

'''
		expect = '''Program([FuncDecl(Id(yvV), [VarDecl(Id(K7), BoolType, None, None), VarDecl(Id(Y_C), StringType, None, None)], Return()), FuncDecl(Id(nA2), [VarDecl(Id(vS), NumberType, None, None), VarDecl(Id(nr), BoolType, None, None), VarDecl(Id(jGF), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115913))

	def test_21530115914(self):
		input = '''
func TrFv (bool Hr)	begin
		BZIN <- "qX"
		YK["s", cRSJ] <- false
	end

bool bVi <- 76.11
string ansM[42.87,29.7] <- ePd
'''
		expect = '''Program([FuncDecl(Id(TrFv), [VarDecl(Id(Hr), BoolType, None, None)], Block([AssignStmt(Id(BZIN), StringLit(qX)), AssignStmt(ArrayCell(Id(YK), [StringLit(s), Id(cRSJ)]), BooleanLit(False))])), VarDecl(Id(bVi), BoolType, None, NumLit(76.11)), VarDecl(Id(ansM), ArrayType([42.87, 29.7], StringType), None, Id(ePd))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115914))

	def test_21530115915(self):
		input = '''
func hjSE (string x1bd)
	begin
		return GQ7J
	end
dynamic mv_
number uPG[94.77,55.94,84.53] <- 35.33
var FvS <- 13.41
func Vw (number l47m[12.1])	begin
		NjP <- false
		begin
			begin
				string LLnw
			end
			bool KVrx[39.46,23.8,35.23]
			return false
		end
	end

'''
		expect = '''Program([FuncDecl(Id(hjSE), [VarDecl(Id(x1bd), StringType, None, None)], Block([Return(Id(GQ7J))])), VarDecl(Id(mv_), None, dynamic, None), VarDecl(Id(uPG), ArrayType([94.77, 55.94, 84.53], NumberType), None, NumLit(35.33)), VarDecl(Id(FvS), None, var, NumLit(13.41)), FuncDecl(Id(Vw), [VarDecl(Id(l47m), ArrayType([12.1], NumberType), None, None)], Block([AssignStmt(Id(NjP), BooleanLit(False)), Block([Block([VarDecl(Id(LLnw), StringType, None, None)]), VarDecl(Id(KVrx), ArrayType([39.46, 23.8, 35.23], BoolType), None, None), Return(BooleanLit(False))])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115915))

	def test_21530115916(self):
		input = '''
func ze ()
	return

number d5m[57.24,60.96,55.68] <- iKv
func L9 (number EP)	return
string yxO[56.1] <- true
'''
		expect = '''Program([FuncDecl(Id(ze), [], Return()), VarDecl(Id(d5m), ArrayType([57.24, 60.96, 55.68], NumberType), None, Id(iKv)), FuncDecl(Id(L9), [VarDecl(Id(EP), NumberType, None, None)], Return()), VarDecl(Id(yxO), ArrayType([56.1], StringType), None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115916))

	def test_21530115917(self):
		input = '''
func Ig (string fhK[7.17], bool IfrO, number vg4)	begin
	end

bool uP[5.84,47.58]
number FS[95.79,52.84]
number iC[69.13,59.85,52.08]
'''
		expect = '''Program([FuncDecl(Id(Ig), [VarDecl(Id(fhK), ArrayType([7.17], StringType), None, None), VarDecl(Id(IfrO), BoolType, None, None), VarDecl(Id(vg4), NumberType, None, None)], Block([])), VarDecl(Id(uP), ArrayType([5.84, 47.58], BoolType), None, None), VarDecl(Id(FS), ArrayType([95.79, 52.84], NumberType), None, None), VarDecl(Id(iC), ArrayType([69.13, 59.85, 52.08], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115917))

	def test_21530115918(self):
		input = '''
number xp5c
bool ST7U
func B5 (number Br[41.83,50.87], string ZXq0, string Dqug)
	return false

'''
		expect = '''Program([VarDecl(Id(xp5c), NumberType, None, None), VarDecl(Id(ST7U), BoolType, None, None), FuncDecl(Id(B5), [VarDecl(Id(Br), ArrayType([41.83, 50.87], NumberType), None, None), VarDecl(Id(ZXq0), StringType, None, None), VarDecl(Id(Dqug), StringType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115918))

	def test_21530115919(self):
		input = '''
func sxKn (bool A9t, string r9qI, bool d83o[36.12])	return rUkQ

func E_ (bool D8, string AM9[62.28], number NaPw)	begin
		var ciOs <- "jx"
	end
func m5WB (number QOQ[57.27,97.66], bool gV[2.54,31.45])	return 32.43
func qg (number Ce[53.97], bool QM)	begin
		continue
		continue
	end

func gN4 (string jYP2[12.55,38.9])
	return 84.25
'''
		expect = '''Program([FuncDecl(Id(sxKn), [VarDecl(Id(A9t), BoolType, None, None), VarDecl(Id(r9qI), StringType, None, None), VarDecl(Id(d83o), ArrayType([36.12], BoolType), None, None)], Return(Id(rUkQ))), FuncDecl(Id(E_), [VarDecl(Id(D8), BoolType, None, None), VarDecl(Id(AM9), ArrayType([62.28], StringType), None, None), VarDecl(Id(NaPw), NumberType, None, None)], Block([VarDecl(Id(ciOs), None, var, StringLit(jx))])), FuncDecl(Id(m5WB), [VarDecl(Id(QOQ), ArrayType([57.27, 97.66], NumberType), None, None), VarDecl(Id(gV), ArrayType([2.54, 31.45], BoolType), None, None)], Return(NumLit(32.43))), FuncDecl(Id(qg), [VarDecl(Id(Ce), ArrayType([53.97], NumberType), None, None), VarDecl(Id(QM), BoolType, None, None)], Block([Continue, Continue])), FuncDecl(Id(gN4), [VarDecl(Id(jYP2), ArrayType([12.55, 38.9], StringType), None, None)], Return(NumLit(84.25)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115919))

	def test_21530115920(self):
		input = '''
bool jVZw[8.67,61.56]
number sY8K[27.43] <- bGZH
func u_4 (string xHz[23.54,32.24,43.68], number yKk[22.98])
	return PB

'''
		expect = '''Program([VarDecl(Id(jVZw), ArrayType([8.67, 61.56], BoolType), None, None), VarDecl(Id(sY8K), ArrayType([27.43], NumberType), None, Id(bGZH)), FuncDecl(Id(u_4), [VarDecl(Id(xHz), ArrayType([23.54, 32.24, 43.68], StringType), None, None), VarDecl(Id(yKk), ArrayType([22.98], NumberType), None, None)], Return(Id(PB)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115920))

	def test_21530115921(self):
		input = '''
string jbcK[56.7] <- 42.96
bool Ne[74.61,50.58]
number nD[1.11,66.04,37.15] <- 39.25
'''
		expect = '''Program([VarDecl(Id(jbcK), ArrayType([56.7], StringType), None, NumLit(42.96)), VarDecl(Id(Ne), ArrayType([74.61, 50.58], BoolType), None, None), VarDecl(Id(nD), ArrayType([1.11, 66.04, 37.15], NumberType), None, NumLit(39.25))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115921))

	def test_21530115922(self):
		input = '''
func lEUb (string TKCv[10.69])	return oXf
func O0o0 ()	return

'''
		expect = '''Program([FuncDecl(Id(lEUb), [VarDecl(Id(TKCv), ArrayType([10.69], StringType), None, None)], Return(Id(oXf))), FuncDecl(Id(O0o0), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115922))

	def test_21530115923(self):
		input = '''
func kKS (number a7b4, bool ER[9.23], number Zrt[6.87,22.73,69.02])
	return true
'''
		expect = '''Program([FuncDecl(Id(kKS), [VarDecl(Id(a7b4), NumberType, None, None), VarDecl(Id(ER), ArrayType([9.23], BoolType), None, None), VarDecl(Id(Zrt), ArrayType([6.87, 22.73, 69.02], NumberType), None, None)], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115923))

	def test_21530115924(self):
		input = '''
number gMia[61.33,15.56] <- true
func Sq (bool EF[18.5,47.12], number ySM, bool p0[9.36,30.65,40.97])
	return false

string HMD
func DR5 ()
	return true

func XGOh (bool lN, string Gwz)
	begin
		begin
			return
			for aC until "u" by true
				if (QrT)
				rmU["EC", "ZS"] <- "X"
				elif (false) T6z()
				elif (false)
				for Nj until b2 by true
					return
			break
		end
	end

'''
		expect = '''Program([VarDecl(Id(gMia), ArrayType([61.33, 15.56], NumberType), None, BooleanLit(True)), FuncDecl(Id(Sq), [VarDecl(Id(EF), ArrayType([18.5, 47.12], BoolType), None, None), VarDecl(Id(ySM), NumberType, None, None), VarDecl(Id(p0), ArrayType([9.36, 30.65, 40.97], BoolType), None, None)], Return(BooleanLit(False))), VarDecl(Id(HMD), StringType, None, None), FuncDecl(Id(DR5), [], Return(BooleanLit(True))), FuncDecl(Id(XGOh), [VarDecl(Id(lN), BoolType, None, None), VarDecl(Id(Gwz), StringType, None, None)], Block([Block([Return(), For(Id(aC), StringLit(u), BooleanLit(True), If((Id(QrT), AssignStmt(ArrayCell(Id(rmU), [StringLit(EC), StringLit(ZS)]), StringLit(X))), [(BooleanLit(False), CallStmt(Id(T6z), [])), (BooleanLit(False), For(Id(Nj), Id(b2), BooleanLit(True), Return()))], None)), Break])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115924))

	def test_21530115925(self):
		input = '''
func cnTG (number wa, bool HzU[57.86,76.22,2.41], bool xj9)	begin
	end
func uvf ()
	begin
		if (kJ)
		begin
			if (true)
			if (true) x90(w0)
			elif (RD) if (ZfN) break
			elif (82.43)
			if ("iQY")
			begin
				break
			end
			elif (71.61) return
			elif (1.38) Q7HU[false, 56.96] <- true
			elif ("Ycl")
			continue
			elif (1.29) IR[Xr] <- 19.43
			else continue
			elif (false) continue
			elif (84.37)
			for Sf until 53.51 by exIu
				continue
			elif (38.24)
			continue
			elif ("YUqGq") break
			elif (89.94) PdOP()
			elif (false)
			return false
			elif (lez6) continue
			elif (true) return
			elif (9.28) break
			else xeu <- 98.2
			break
			kAYa[true, zf, 63.01] <- 18.85
		end
		elif (true)
		bool SXv4 <- "CPDHL"
		elif (qp2C) for Ixr until false by false
			string KWd[59.88,0.5]
		elif (MXeq)
		continue
		elif (30.27) bAt(y9ug, "Yvakh")
		elif (34.99)
		for xi until 66.77 by "NzR"
			return true
	end

number Xmfl[32.15,37.49] <- "yvtPN"
func sok8 (bool Cdk, string rR3[94.29,91.06], bool asxx)
	return
'''
		expect = '''Program([FuncDecl(Id(cnTG), [VarDecl(Id(wa), NumberType, None, None), VarDecl(Id(HzU), ArrayType([57.86, 76.22, 2.41], BoolType), None, None), VarDecl(Id(xj9), BoolType, None, None)], Block([])), FuncDecl(Id(uvf), [], Block([If((Id(kJ), Block([If((BooleanLit(True), If((BooleanLit(True), CallStmt(Id(x90), [Id(w0)])), [(Id(RD), If((Id(ZfN), Break), [(NumLit(82.43), If((StringLit(iQY), Block([Break])), [(NumLit(71.61), Return()), (NumLit(1.38), AssignStmt(ArrayCell(Id(Q7HU), [BooleanLit(False), NumLit(56.96)]), BooleanLit(True))), (StringLit(Ycl), Continue), (NumLit(1.29), AssignStmt(ArrayCell(Id(IR), [Id(Xr)]), NumLit(19.43)))], Continue)), (BooleanLit(False), Continue), (NumLit(84.37), For(Id(Sf), NumLit(53.51), Id(exIu), Continue)), (NumLit(38.24), Continue), (StringLit(YUqGq), Break), (NumLit(89.94), CallStmt(Id(PdOP), [])), (BooleanLit(False), Return(BooleanLit(False))), (Id(lez6), Continue), (BooleanLit(True), Return()), (NumLit(9.28), Break)], AssignStmt(Id(xeu), NumLit(98.2))))], None)), [], None), Break, AssignStmt(ArrayCell(Id(kAYa), [BooleanLit(True), Id(zf), NumLit(63.01)]), NumLit(18.85))])), [(BooleanLit(True), VarDecl(Id(SXv4), BoolType, None, StringLit(CPDHL))), (Id(qp2C), For(Id(Ixr), BooleanLit(False), BooleanLit(False), VarDecl(Id(KWd), ArrayType([59.88, 0.5], StringType), None, None))), (Id(MXeq), Continue), (NumLit(30.27), CallStmt(Id(bAt), [Id(y9ug), StringLit(Yvakh)])), (NumLit(34.99), For(Id(xi), NumLit(66.77), StringLit(NzR), Return(BooleanLit(True))))], None)])), VarDecl(Id(Xmfl), ArrayType([32.15, 37.49], NumberType), None, StringLit(yvtPN)), FuncDecl(Id(sok8), [VarDecl(Id(Cdk), BoolType, None, None), VarDecl(Id(rR3), ArrayType([94.29, 91.06], StringType), None, None), VarDecl(Id(asxx), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115925))

	def test_21530115926(self):
		input = '''
string HUi[90.05,53.3,74.35]
func SY ()	return
func SiY (string YAI)	return "z"
number bgJV[35.81,23.15,56.18] <- eb
'''
		expect = '''Program([VarDecl(Id(HUi), ArrayType([90.05, 53.3, 74.35], StringType), None, None), FuncDecl(Id(SY), [], Return()), FuncDecl(Id(SiY), [VarDecl(Id(YAI), StringType, None, None)], Return(StringLit(z))), VarDecl(Id(bgJV), ArrayType([35.81, 23.15, 56.18], NumberType), None, Id(eb))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115926))

	def test_21530115927(self):
		input = '''
string tKa6
'''
		expect = '''Program([VarDecl(Id(tKa6), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115927))

	def test_21530115928(self):
		input = '''
number bNt[22.44,13.93,10.22] <- false
func y8b7 (bool Rmfv[24.1], number FY)
	begin
		dynamic pb <- 57.78
		for Sdh_ until "KUEvo" by 46.19
			number e0 <- "IN"
		break
	end
func nSqp (bool gqg[16.16,79.83], number s40l[37.8,16.0], number smue)	return
func Ec (number S49Y[34.35,11.04], string gfw[23.64], string BMC[36.08,3.3])	return

string Slp[33.85,67.82,72.99] <- 40.21
'''
		expect = '''Program([VarDecl(Id(bNt), ArrayType([22.44, 13.93, 10.22], NumberType), None, BooleanLit(False)), FuncDecl(Id(y8b7), [VarDecl(Id(Rmfv), ArrayType([24.1], BoolType), None, None), VarDecl(Id(FY), NumberType, None, None)], Block([VarDecl(Id(pb), None, dynamic, NumLit(57.78)), For(Id(Sdh_), StringLit(KUEvo), NumLit(46.19), VarDecl(Id(e0), NumberType, None, StringLit(IN))), Break])), FuncDecl(Id(nSqp), [VarDecl(Id(gqg), ArrayType([16.16, 79.83], BoolType), None, None), VarDecl(Id(s40l), ArrayType([37.8, 16.0], NumberType), None, None), VarDecl(Id(smue), NumberType, None, None)], Return()), FuncDecl(Id(Ec), [VarDecl(Id(S49Y), ArrayType([34.35, 11.04], NumberType), None, None), VarDecl(Id(gfw), ArrayType([23.64], StringType), None, None), VarDecl(Id(BMC), ArrayType([36.08, 3.3], StringType), None, None)], Return()), VarDecl(Id(Slp), ArrayType([33.85, 67.82, 72.99], StringType), None, NumLit(40.21))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115928))

	def test_21530115929(self):
		input = '''
bool WJE <- 75.95
dynamic uQ <- 37.72
string dkr
func ljU (string HZ1[43.44,80.37], string Oh, bool C7g)	begin
		if (TzCs)
		cQ["DjdXD", KjJ] <- 49.18
		elif (false) continue
		return "SF"
		ky2(70.54)
	end

var bJv5 <- "q"
'''
		expect = '''Program([VarDecl(Id(WJE), BoolType, None, NumLit(75.95)), VarDecl(Id(uQ), None, dynamic, NumLit(37.72)), VarDecl(Id(dkr), StringType, None, None), FuncDecl(Id(ljU), [VarDecl(Id(HZ1), ArrayType([43.44, 80.37], StringType), None, None), VarDecl(Id(Oh), StringType, None, None), VarDecl(Id(C7g), BoolType, None, None)], Block([If((Id(TzCs), AssignStmt(ArrayCell(Id(cQ), [StringLit(DjdXD), Id(KjJ)]), NumLit(49.18))), [(BooleanLit(False), Continue)], None), Return(StringLit(SF)), CallStmt(Id(ky2), [NumLit(70.54)])])), VarDecl(Id(bJv5), None, var, StringLit(q))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115929))

	def test_21530115930(self):
		input = '''
bool QMR[94.43,26.88,25.91]
'''
		expect = '''Program([VarDecl(Id(QMR), ArrayType([94.43, 26.88, 25.91], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115930))

	def test_21530115931(self):
		input = '''
func RN2 (string B8L, bool CWLS[59.72,17.21,79.33])	return "J"

var ODBb <- 85.15
bool berq[31.4] <- 63.2
func mS (string sYN, number pl[26.42])
	return

bool nkB_
'''
		expect = '''Program([FuncDecl(Id(RN2), [VarDecl(Id(B8L), StringType, None, None), VarDecl(Id(CWLS), ArrayType([59.72, 17.21, 79.33], BoolType), None, None)], Return(StringLit(J))), VarDecl(Id(ODBb), None, var, NumLit(85.15)), VarDecl(Id(berq), ArrayType([31.4], BoolType), None, NumLit(63.2)), FuncDecl(Id(mS), [VarDecl(Id(sYN), StringType, None, None), VarDecl(Id(pl), ArrayType([26.42], NumberType), None, None)], Return()), VarDecl(Id(nkB_), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115931))

	def test_21530115932(self):
		input = '''
func L126 (string kOA)
	return true

string mV[10.0,2.88,17.49] <- Jq5
string Ts <- gKNU
bool u05
bool EP
'''
		expect = '''Program([FuncDecl(Id(L126), [VarDecl(Id(kOA), StringType, None, None)], Return(BooleanLit(True))), VarDecl(Id(mV), ArrayType([10.0, 2.88, 17.49], StringType), None, Id(Jq5)), VarDecl(Id(Ts), StringType, None, Id(gKNU)), VarDecl(Id(u05), BoolType, None, None), VarDecl(Id(EP), BoolType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115932))

	def test_21530115933(self):
		input = '''
func Pt (string Zs[19.5,73.89,30.91], bool WTF[63.59,92.34,5.95])	return true
func Bkf6 (bool MTM)
	return
func jP (number o0v)	return

'''
		expect = '''Program([FuncDecl(Id(Pt), [VarDecl(Id(Zs), ArrayType([19.5, 73.89, 30.91], StringType), None, None), VarDecl(Id(WTF), ArrayType([63.59, 92.34, 5.95], BoolType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(Bkf6), [VarDecl(Id(MTM), BoolType, None, None)], Return()), FuncDecl(Id(jP), [VarDecl(Id(o0v), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115933))

	def test_21530115934(self):
		input = '''
func pFdx (number soWW, bool rH7H)
	return 96.75

func zi (string JFi, string Wr[38.27,43.47])	return "cY"

'''
		expect = '''Program([FuncDecl(Id(pFdx), [VarDecl(Id(soWW), NumberType, None, None), VarDecl(Id(rH7H), BoolType, None, None)], Return(NumLit(96.75))), FuncDecl(Id(zi), [VarDecl(Id(JFi), StringType, None, None), VarDecl(Id(Wr), ArrayType([38.27, 43.47], StringType), None, None)], Return(StringLit(cY)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115934))

	def test_21530115935(self):
		input = '''
string vuZ <- 83.54
var bb <- 85.16
func ha ()
	begin
		iEpX(6.44)
	end
'''
		expect = '''Program([VarDecl(Id(vuZ), StringType, None, NumLit(83.54)), VarDecl(Id(bb), None, var, NumLit(85.16)), FuncDecl(Id(ha), [], Block([CallStmt(Id(iEpX), [NumLit(6.44)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115935))

	def test_21530115936(self):
		input = '''
func rX (number IFF[13.12,93.37,72.73])	begin
		REk["AkV"] <- "VdOy"
		begin
			break
			for gPr until false by false
				for cF1u until "qOu" by 17.92
					for IIp until true by true
						return
		end
	end
func FqwN (number zR, bool Vy[88.62,86.81,87.48])	return
'''
		expect = '''Program([FuncDecl(Id(rX), [VarDecl(Id(IFF), ArrayType([13.12, 93.37, 72.73], NumberType), None, None)], Block([AssignStmt(ArrayCell(Id(REk), [StringLit(AkV)]), StringLit(VdOy)), Block([Break, For(Id(gPr), BooleanLit(False), BooleanLit(False), For(Id(cF1u), StringLit(qOu), NumLit(17.92), For(Id(IIp), BooleanLit(True), BooleanLit(True), Return())))])])), FuncDecl(Id(FqwN), [VarDecl(Id(zR), NumberType, None, None), VarDecl(Id(Vy), ArrayType([88.62, 86.81, 87.48], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115936))

	def test_21530115937(self):
		input = '''
string Vlv <- true
var YI <- "VyBrv"
'''
		expect = '''Program([VarDecl(Id(Vlv), StringType, None, BooleanLit(True)), VarDecl(Id(YI), None, var, StringLit(VyBrv))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115937))

	def test_21530115938(self):
		input = '''
func B2z (bool OZhj[63.65,46.85], number JKih[11.23], string Xhfj)	return

'''
		expect = '''Program([FuncDecl(Id(B2z), [VarDecl(Id(OZhj), ArrayType([63.65, 46.85], BoolType), None, None), VarDecl(Id(JKih), ArrayType([11.23], NumberType), None, None), VarDecl(Id(Xhfj), StringType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115938))

	def test_21530115939(self):
		input = '''
func XK6 (number bRa[35.43], string aJ[95.44])	begin
		return
	end

number EmcK[9.37] <- "VO"
func eW (number wST)
	begin
		break
		begin
			continue
			break
			if ("RaJR")
			return true
			elif (false) EYB(87.66, false)
			elif (true) dMm(false)
			elif (ofs6) bool UQv[13.0,81.27,45.75] <- 47.22
			elif (38.74)
			for FVEy until vsgk by wtpE
				fbu <- sAy
			elif (fJ)
			return
			else for x_o until "Z" by false
				p8x[kZYF, GJKx] <- true
		end
		return
	end
func y9 (number Rkb)
	return

number mM[54.89]
'''
		expect = '''Program([FuncDecl(Id(XK6), [VarDecl(Id(bRa), ArrayType([35.43], NumberType), None, None), VarDecl(Id(aJ), ArrayType([95.44], StringType), None, None)], Block([Return()])), VarDecl(Id(EmcK), ArrayType([9.37], NumberType), None, StringLit(VO)), FuncDecl(Id(eW), [VarDecl(Id(wST), NumberType, None, None)], Block([Break, Block([Continue, Break, If((StringLit(RaJR), Return(BooleanLit(True))), [(BooleanLit(False), CallStmt(Id(EYB), [NumLit(87.66), BooleanLit(False)])), (BooleanLit(True), CallStmt(Id(dMm), [BooleanLit(False)])), (Id(ofs6), VarDecl(Id(UQv), ArrayType([13.0, 81.27, 45.75], BoolType), None, NumLit(47.22))), (NumLit(38.74), For(Id(FVEy), Id(vsgk), Id(wtpE), AssignStmt(Id(fbu), Id(sAy)))), (Id(fJ), Return())], For(Id(x_o), StringLit(Z), BooleanLit(False), AssignStmt(ArrayCell(Id(p8x), [Id(kZYF), Id(GJKx)]), BooleanLit(True))))]), Return()])), FuncDecl(Id(y9), [VarDecl(Id(Rkb), NumberType, None, None)], Return()), VarDecl(Id(mM), ArrayType([54.89], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115939))

	def test_21530115940(self):
		input = '''
func U8 (string pP)	begin
		for Cy until 51.79 by 42.72
			begin
				EKaB <- 44.61
			end
		var vz <- 36.93
	end
'''
		expect = '''Program([FuncDecl(Id(U8), [VarDecl(Id(pP), StringType, None, None)], Block([For(Id(Cy), NumLit(51.79), NumLit(42.72), Block([AssignStmt(Id(EKaB), NumLit(44.61))])), VarDecl(Id(vz), None, var, NumLit(36.93))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115940))

	def test_21530115941(self):
		input = '''
func ZmhL ()
	begin
		return
	end
'''
		expect = '''Program([FuncDecl(Id(ZmhL), [], Block([Return()]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115941))

	def test_21530115942(self):
		input = '''
bool BN[50.79,24.85,28.3]
func cs (number Z03[78.5,7.71,12.37])
	begin
		number hVF[59.03,98.39]
		return
		var BqEb <- VyXJ
	end
func AM (bool hZ)	return 67.47

'''
		expect = '''Program([VarDecl(Id(BN), ArrayType([50.79, 24.85, 28.3], BoolType), None, None), FuncDecl(Id(cs), [VarDecl(Id(Z03), ArrayType([78.5, 7.71, 12.37], NumberType), None, None)], Block([VarDecl(Id(hVF), ArrayType([59.03, 98.39], NumberType), None, None), Return(), VarDecl(Id(BqEb), None, var, Id(VyXJ))])), FuncDecl(Id(AM), [VarDecl(Id(hZ), BoolType, None, None)], Return(NumLit(67.47)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115942))

	def test_21530115943(self):
		input = '''
number WEEN[74.22] <- "huuIf"
'''
		expect = '''Program([VarDecl(Id(WEEN), ArrayType([74.22], NumberType), None, StringLit(huuIf))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115943))

	def test_21530115944(self):
		input = '''
func bm (string Nf)	return y8p
string DsG
func QfvV (bool giG[31.62,10.22], number ndem)
	begin
		return
		tK()
		begin
			begin
				for nAQX until "UCNQn" by true
					if (true) continue
					elif (14.32)
					if (false)
					begin
						return wJsr
					end
					elif (false) ByYT <- M7HR
					elif (false) for Nie5 until Rr by p0GB
						xcMK(false)
					elif (63.85)
					continue
				begin
					string otm[80.5,25.85,57.42] <- true
					Kwpy(aaVi, 14.22, "UNcTz")
					bool SPOz <- "v"
				end
				if (true) RzMo <- pqG
				elif (AlQ) TZ()
				elif (Nh1h)
				continue
				elif (14.82) begin
				end
				elif (zjb)
				number eTc[59.35] <- "HfS"
				elif (true)
				continue
				else continue
			end
			if ("mHD") for Pa until "sKsW" by 66.39
				begin
					if ("lJ")
					if (true) var rV <- Xg
					elif (qG6)
					string ACfy[84.05,34.57]
					elif (eNb) return
					elif (true) for cZ until 82.94 by cohr
						for d5 until 1.33 by 8.91
							if ("mLR") for arnq until true by 33.43
								continue
							elif (95.66)
							eM9L <- tKa
							elif ("pQt")
							Bem(true, "UX", false)
							elif (w7Zc) if (51.9)
							string dj[61.53,14.36]
							elif (false)
							if (true) string ufAr[88.86,89.29]
							elif (true)
							begin
								begin
								end
								Jwzp[76.58, "SvPro", 45.49] <- true
							end
							elif (false)
							bool r2p <- "tXa"
							elif (VgI) continue
							elif (Nf)
							number tOrv[11.22,91.37,66.01] <- l5L
							elif (zy54)
							return "hvb"
							elif ("owDoS")
							H0Mg <- false
							elif ("n")
							for sXF until pi by false
								number ukji <- kFa5
							elif (wqp) return
					else J6D[82.69, false, 26.06] <- "nY"
					elif ("tDBa") continue
					elif (23.97)
					if (d8t) begin
					end
					elif ("FUzb") if (37.68)
					return
					elif ("qHV") iPi <- true
					elif (cs)
					break
					elif (false)
					return "BlkU"
					elif (false) var Xd <- "S"
					elif (vg)
					return true
					elif (rFOf)
					begin
					end
					elif (61.87)
					q2g <- false
					elif ("rsVL")
					if (52.68)
					for a1C until 2.0 by 54.31
						return 35.17
					elif ("pWl")
					VHr <- Ig
					elif (agyZ) buk()
					elif ("kber")
					begin
						RgsY[11.77] <- DG0l
					end
				end
			return
		end
	end

func DP (number Ys, number JMy7[18.9,35.31])
	return 74.32
func ZDi (string X7[36.92])	return false
'''
		expect = '''Program([FuncDecl(Id(bm), [VarDecl(Id(Nf), StringType, None, None)], Return(Id(y8p))), VarDecl(Id(DsG), StringType, None, None), FuncDecl(Id(QfvV), [VarDecl(Id(giG), ArrayType([31.62, 10.22], BoolType), None, None), VarDecl(Id(ndem), NumberType, None, None)], Block([Return(), CallStmt(Id(tK), []), Block([Block([For(Id(nAQX), StringLit(UCNQn), BooleanLit(True), If((BooleanLit(True), Continue), [(NumLit(14.32), If((BooleanLit(False), Block([Return(Id(wJsr))])), [(BooleanLit(False), AssignStmt(Id(ByYT), Id(M7HR))), (BooleanLit(False), For(Id(Nie5), Id(Rr), Id(p0GB), CallStmt(Id(xcMK), [BooleanLit(False)]))), (NumLit(63.85), Continue)], None))], None)), Block([VarDecl(Id(otm), ArrayType([80.5, 25.85, 57.42], StringType), None, BooleanLit(True)), CallStmt(Id(Kwpy), [Id(aaVi), NumLit(14.22), StringLit(UNcTz)]), VarDecl(Id(SPOz), BoolType, None, StringLit(v))]), If((BooleanLit(True), AssignStmt(Id(RzMo), Id(pqG))), [(Id(AlQ), CallStmt(Id(TZ), [])), (Id(Nh1h), Continue), (NumLit(14.82), Block([])), (Id(zjb), VarDecl(Id(eTc), ArrayType([59.35], NumberType), None, StringLit(HfS))), (BooleanLit(True), Continue)], Continue)]), If((StringLit(mHD), For(Id(Pa), StringLit(sKsW), NumLit(66.39), Block([If((StringLit(lJ), If((BooleanLit(True), VarDecl(Id(rV), None, var, Id(Xg))), [(Id(qG6), VarDecl(Id(ACfy), ArrayType([84.05, 34.57], StringType), None, None)), (Id(eNb), Return()), (BooleanLit(True), For(Id(cZ), NumLit(82.94), Id(cohr), For(Id(d5), NumLit(1.33), NumLit(8.91), If((StringLit(mLR), For(Id(arnq), BooleanLit(True), NumLit(33.43), Continue)), [(NumLit(95.66), AssignStmt(Id(eM9L), Id(tKa))), (StringLit(pQt), CallStmt(Id(Bem), [BooleanLit(True), StringLit(UX), BooleanLit(False)])), (Id(w7Zc), If((NumLit(51.9), VarDecl(Id(dj), ArrayType([61.53, 14.36], StringType), None, None)), [(BooleanLit(False), If((BooleanLit(True), VarDecl(Id(ufAr), ArrayType([88.86, 89.29], StringType), None, None)), [(BooleanLit(True), Block([Block([]), AssignStmt(ArrayCell(Id(Jwzp), [NumLit(76.58), StringLit(SvPro), NumLit(45.49)]), BooleanLit(True))])), (BooleanLit(False), VarDecl(Id(r2p), BoolType, None, StringLit(tXa))), (Id(VgI), Continue), (Id(Nf), VarDecl(Id(tOrv), ArrayType([11.22, 91.37, 66.01], NumberType), None, Id(l5L))), (Id(zy54), Return(StringLit(hvb))), (StringLit(owDoS), AssignStmt(Id(H0Mg), BooleanLit(False))), (StringLit(n), For(Id(sXF), Id(pi), BooleanLit(False), VarDecl(Id(ukji), NumberType, None, Id(kFa5)))), (Id(wqp), Return())], AssignStmt(ArrayCell(Id(J6D), [NumLit(82.69), BooleanLit(False), NumLit(26.06)]), StringLit(nY)))), (StringLit(tDBa), Continue), (NumLit(23.97), If((Id(d8t), Block([])), [(StringLit(FUzb), If((NumLit(37.68), Return()), [(StringLit(qHV), AssignStmt(Id(iPi), BooleanLit(True))), (Id(cs), Break), (BooleanLit(False), Return(StringLit(BlkU))), (BooleanLit(False), VarDecl(Id(Xd), None, var, StringLit(S))), (Id(vg), Return(BooleanLit(True))), (Id(rFOf), Block([])), (NumLit(61.87), AssignStmt(Id(q2g), BooleanLit(False))), (StringLit(rsVL), If((NumLit(52.68), For(Id(a1C), NumLit(2.0), NumLit(54.31), Return(NumLit(35.17)))), [(StringLit(pWl), AssignStmt(Id(VHr), Id(Ig))), (Id(agyZ), CallStmt(Id(buk), [])), (StringLit(kber), Block([AssignStmt(ArrayCell(Id(RgsY), [NumLit(11.77)]), Id(DG0l))]))], None))], None))], None))], None))], None))))], None)), [], None)]))), [], None), Return()])])), FuncDecl(Id(DP), [VarDecl(Id(Ys), NumberType, None, None), VarDecl(Id(JMy7), ArrayType([18.9, 35.31], NumberType), None, None)], Return(NumLit(74.32))), FuncDecl(Id(ZDi), [VarDecl(Id(X7), ArrayType([36.92], StringType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115944))

	def test_21530115945(self):
		input = '''
func AbyV (string Knd[95.49], number tP[93.71])
	return
func zN (number Na, string dJ[52.31,1.8,59.92])	return
'''
		expect = '''Program([FuncDecl(Id(AbyV), [VarDecl(Id(Knd), ArrayType([95.49], StringType), None, None), VarDecl(Id(tP), ArrayType([93.71], NumberType), None, None)], Return()), FuncDecl(Id(zN), [VarDecl(Id(Na), NumberType, None, None), VarDecl(Id(dJ), ArrayType([52.31, 1.8, 59.92], StringType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115945))

	def test_21530115946(self):
		input = '''
func c_l ()
	begin
		continue
	end
func GJl3 (string xt, bool Sv)
	return

func CTo (string cW, number CQ0[95.41], bool rJZ)	begin
		for gvBA until 20.41 by 7.62
			if (false) if (2.25)
			Ve()
			elif (CFhm)
			xO()
			elif ("PjBZ")
			return 12.66
			elif ("SJB") break
			elif (98.23) for c88n until Km by 91.84
				maEn <- "aoqQ"
			elif (61.98) if (24.25)
			M8K(fkyX)
			elif (true)
			bB("dg")
			elif (21.83) begin
				if ("tGaR")
				FbV(sEeB, l8l, "DTTVS")
				elif (yH) KZR["W"] <- true
				elif ("CEM") if (true) continue
				elif (23.66) sH(false)
				elif ("tB")
				if (bga)
				if (75.21) if (false) break
				elif (45.86)
				break
				elif (64.89)
				Pf <- WJl
				else break
				elif (43.72)
				for QfkE until gyLi by 27.39
					Zpe(74.75)
				elif (true) if (vzY) return "gcsc"
				elif (7.17) return true
				elif (false) continue
				elif (false)
				break
				elif (true) return "m"
				elif (57.64) if ("WxcEI") return 41.29
				elif (96.47) begin
				end
				else number ccZ9[80.4,4.54,70.75] <- "M"
				elif (true)
				continue
				elif (xK8) return
				elif (20.44)
				begin
					return
					continue
					if (80.7)
					begin
						begin
							xKZ("Go", "lc", ms)
							break
						end
					end
					elif (false)
					begin
					end
					elif (ja)
					BIh0 <- "Hm"
					elif (62.02)
					Ce("I", 39.21, 48.48)
					elif ("lWAvv")
					for DU until "YcTCm" by false
						CF0["cQk"] <- PP
					else return false
				end
				elif (AJ)
				return 42.12
				elif (86.27)
				bool QFO[68.3,56.61,37.46] <- "LFK"
				else return
				elif (true)
				return "Z"
				elif (56.62)
				if (28.13)
				string WByY[88.85,26.19,21.98]
				elif (Wa) ohcC(C0F, Pe)
				elif (RER1)
				for W2 until true by true
					amp <- deGb
				elif (false)
				dynamic pj <- OQhP
				elif (false)
				number O8yt[90.29,11.14]
				else continue
				gI3E <- true
			end
			elif ("wj")
			begin
				string rvb <- true
				RtwK(11.04)
				begin
					Xm["IVQE", "RR"] <- bm
				end
			end
			elif ("rXSp")
			return
			elif ("jomk") break
			elif (W55) break
			elif (92.22) break
		ngbB(true)
		break
	end

'''
		expect = '''Program([FuncDecl(Id(c_l), [], Block([Continue])), FuncDecl(Id(GJl3), [VarDecl(Id(xt), StringType, None, None), VarDecl(Id(Sv), BoolType, None, None)], Return()), FuncDecl(Id(CTo), [VarDecl(Id(cW), StringType, None, None), VarDecl(Id(CQ0), ArrayType([95.41], NumberType), None, None), VarDecl(Id(rJZ), BoolType, None, None)], Block([For(Id(gvBA), NumLit(20.41), NumLit(7.62), If((BooleanLit(False), If((NumLit(2.25), CallStmt(Id(Ve), [])), [(Id(CFhm), CallStmt(Id(xO), [])), (StringLit(PjBZ), Return(NumLit(12.66))), (StringLit(SJB), Break), (NumLit(98.23), For(Id(c88n), Id(Km), NumLit(91.84), AssignStmt(Id(maEn), StringLit(aoqQ)))), (NumLit(61.98), If((NumLit(24.25), CallStmt(Id(M8K), [Id(fkyX)])), [(BooleanLit(True), CallStmt(Id(bB), [StringLit(dg)])), (NumLit(21.83), Block([If((StringLit(tGaR), CallStmt(Id(FbV), [Id(sEeB), Id(l8l), StringLit(DTTVS)])), [(Id(yH), AssignStmt(ArrayCell(Id(KZR), [StringLit(W)]), BooleanLit(True))), (StringLit(CEM), If((BooleanLit(True), Continue), [(NumLit(23.66), CallStmt(Id(sH), [BooleanLit(False)])), (StringLit(tB), If((Id(bga), If((NumLit(75.21), If((BooleanLit(False), Break), [(NumLit(45.86), Break), (NumLit(64.89), AssignStmt(Id(Pf), Id(WJl)))], Break)), [(NumLit(43.72), For(Id(QfkE), Id(gyLi), NumLit(27.39), CallStmt(Id(Zpe), [NumLit(74.75)]))), (BooleanLit(True), If((Id(vzY), Return(StringLit(gcsc))), [(NumLit(7.17), Return(BooleanLit(True))), (BooleanLit(False), Continue), (BooleanLit(False), Break), (BooleanLit(True), Return(StringLit(m))), (NumLit(57.64), If((StringLit(WxcEI), Return(NumLit(41.29))), [(NumLit(96.47), Block([]))], VarDecl(Id(ccZ9), ArrayType([80.4, 4.54, 70.75], NumberType), None, StringLit(M)))), (BooleanLit(True), Continue), (Id(xK8), Return()), (NumLit(20.44), Block([Return(), Continue, If((NumLit(80.7), Block([Block([CallStmt(Id(xKZ), [StringLit(Go), StringLit(lc), Id(ms)]), Break])])), [(BooleanLit(False), Block([])), (Id(ja), AssignStmt(Id(BIh0), StringLit(Hm))), (NumLit(62.02), CallStmt(Id(Ce), [StringLit(I), NumLit(39.21), NumLit(48.48)])), (StringLit(lWAvv), For(Id(DU), StringLit(YcTCm), BooleanLit(False), AssignStmt(ArrayCell(Id(CF0), [StringLit(cQk)]), Id(PP))))], Return(BooleanLit(False)))])), (Id(AJ), Return(NumLit(42.12))), (NumLit(86.27), VarDecl(Id(QFO), ArrayType([68.3, 56.61, 37.46], BoolType), None, StringLit(LFK)))], Return())), (BooleanLit(True), Return(StringLit(Z))), (NumLit(56.62), If((NumLit(28.13), VarDecl(Id(WByY), ArrayType([88.85, 26.19, 21.98], StringType), None, None)), [(Id(Wa), CallStmt(Id(ohcC), [Id(C0F), Id(Pe)])), (Id(RER1), For(Id(W2), BooleanLit(True), BooleanLit(True), AssignStmt(Id(amp), Id(deGb)))), (BooleanLit(False), VarDecl(Id(pj), None, dynamic, Id(OQhP))), (BooleanLit(False), VarDecl(Id(O8yt), ArrayType([90.29, 11.14], NumberType), None, None))], Continue))], None)), [], None))], None))], None), AssignStmt(Id(gI3E), BooleanLit(True))])), (StringLit(wj), Block([VarDecl(Id(rvb), StringType, None, BooleanLit(True)), CallStmt(Id(RtwK), [NumLit(11.04)]), Block([AssignStmt(ArrayCell(Id(Xm), [StringLit(IVQE), StringLit(RR)]), Id(bm))])])), (StringLit(rXSp), Return()), (StringLit(jomk), Break), (Id(W55), Break), (NumLit(92.22), Break)], None))], None)), [], None)), CallStmt(Id(ngbB), [BooleanLit(True)]), Break]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115946))

	def test_21530115947(self):
		input = '''
func vMX ()	return "r"
func G8O (string h69[85.01,31.32,29.32], bool FN)
	return KgN
'''
		expect = '''Program([FuncDecl(Id(vMX), [], Return(StringLit(r))), FuncDecl(Id(G8O), [VarDecl(Id(h69), ArrayType([85.01, 31.32, 29.32], StringType), None, None), VarDecl(Id(FN), BoolType, None, None)], Return(Id(KgN)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115947))

	def test_21530115948(self):
		input = '''
number D_[34.93] <- true
func vJGw (number sHv[41.23,93.98,48.02], bool sgX, number TyAw[60.68,46.86])
	return

number kvx2
func qW ()
	return

func S1m ()	return
'''
		expect = '''Program([VarDecl(Id(D_), ArrayType([34.93], NumberType), None, BooleanLit(True)), FuncDecl(Id(vJGw), [VarDecl(Id(sHv), ArrayType([41.23, 93.98, 48.02], NumberType), None, None), VarDecl(Id(sgX), BoolType, None, None), VarDecl(Id(TyAw), ArrayType([60.68, 46.86], NumberType), None, None)], Return()), VarDecl(Id(kvx2), NumberType, None, None), FuncDecl(Id(qW), [], Return()), FuncDecl(Id(S1m), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115948))

	def test_21530115949(self):
		input = '''
number yq[60.85]
string wXth[10.97]
number QF[73.86,81.99]
number RwQ4 <- "byw"
'''
		expect = '''Program([VarDecl(Id(yq), ArrayType([60.85], NumberType), None, None), VarDecl(Id(wXth), ArrayType([10.97], StringType), None, None), VarDecl(Id(QF), ArrayType([73.86, 81.99], NumberType), None, None), VarDecl(Id(RwQ4), NumberType, None, StringLit(byw))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115949))

	def test_21530115950(self):
		input = '''
dynamic IwKM <- KJ_
func pW (bool q5D[23.09,40.67], string jsE, bool OPj)	begin
		continue
		continue
		begin
		end
	end

'''
		expect = '''Program([VarDecl(Id(IwKM), None, dynamic, Id(KJ_)), FuncDecl(Id(pW), [VarDecl(Id(q5D), ArrayType([23.09, 40.67], BoolType), None, None), VarDecl(Id(jsE), StringType, None, None), VarDecl(Id(OPj), BoolType, None, None)], Block([Continue, Continue, Block([])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115950))

	def test_21530115951(self):
		input = '''
func buq (number uWw, string vJyu[57.23,42.07,44.74], bool pz[19.56])	return false
'''
		expect = '''Program([FuncDecl(Id(buq), [VarDecl(Id(uWw), NumberType, None, None), VarDecl(Id(vJyu), ArrayType([57.23, 42.07, 44.74], StringType), None, None), VarDecl(Id(pz), ArrayType([19.56], BoolType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115951))

	def test_21530115952(self):
		input = '''
func Dk9 (number CDyW, string AjD)
	return 90.76
func oJv6 (bool IXmO, number UFXz[29.43,10.82], number BGkS[22.41,57.55,76.92])
	return TDDb
'''
		expect = '''Program([FuncDecl(Id(Dk9), [VarDecl(Id(CDyW), NumberType, None, None), VarDecl(Id(AjD), StringType, None, None)], Return(NumLit(90.76))), FuncDecl(Id(oJv6), [VarDecl(Id(IXmO), BoolType, None, None), VarDecl(Id(UFXz), ArrayType([29.43, 10.82], NumberType), None, None), VarDecl(Id(BGkS), ArrayType([22.41, 57.55, 76.92], NumberType), None, None)], Return(Id(TDDb)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115952))

	def test_21530115953(self):
		input = '''
func AD (number Ft8[73.54], bool LMA7[98.9,79.37], string oRgK)
	return Atw

string ea9M <- 1.9
func ehPD ()
	return WsE

'''
		expect = '''Program([FuncDecl(Id(AD), [VarDecl(Id(Ft8), ArrayType([73.54], NumberType), None, None), VarDecl(Id(LMA7), ArrayType([98.9, 79.37], BoolType), None, None), VarDecl(Id(oRgK), StringType, None, None)], Return(Id(Atw))), VarDecl(Id(ea9M), StringType, None, NumLit(1.9)), FuncDecl(Id(ehPD), [], Return(Id(WsE)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115953))

	def test_21530115954(self):
		input = '''
func x_ ()
	return "yP"

bool U7 <- false
bool nHCQ[63.31]
'''
		expect = '''Program([FuncDecl(Id(x_), [], Return(StringLit(yP))), VarDecl(Id(U7), BoolType, None, BooleanLit(False)), VarDecl(Id(nHCQ), ArrayType([63.31], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115954))

	def test_21530115955(self):
		input = '''
string AVj[98.47,91.73,6.87]
string Pb[40.25]
func B2q8 (number MOi)	return false
'''
		expect = '''Program([VarDecl(Id(AVj), ArrayType([98.47, 91.73, 6.87], StringType), None, None), VarDecl(Id(Pb), ArrayType([40.25], StringType), None, None), FuncDecl(Id(B2q8), [VarDecl(Id(MOi), NumberType, None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115955))

	def test_21530115956(self):
		input = '''
func N6A (string KC, bool OE[16.19,42.74,84.1])	begin
		if (false) EgQ3()
		elif (18.85) begin
			break
			number QG[64.96,64.8,62.98]
		end
		elif (false)
		if (12.89)
		return 76.02
		elif (jP) for ZfV until h0W by "QRe"
			return
		elif (98.88) for yjN until 56.16 by false
			begin
				for wEt until "LO" by 99.34
					break
			end
		elif ("OanV")
		continue
		elif (S6) TZD(false)
		elif (PCee) continue
		else continue
		elif ("nB") break
		elif ("miIuC")
		begin
			break
			begin
			end
		end
		return
		yTlk <- vZY
	end

number ZA
number ggr[78.99]
'''
		expect = '''Program([FuncDecl(Id(N6A), [VarDecl(Id(KC), StringType, None, None), VarDecl(Id(OE), ArrayType([16.19, 42.74, 84.1], BoolType), None, None)], Block([If((BooleanLit(False), CallStmt(Id(EgQ3), [])), [(NumLit(18.85), Block([Break, VarDecl(Id(QG), ArrayType([64.96, 64.8, 62.98], NumberType), None, None)])), (BooleanLit(False), If((NumLit(12.89), Return(NumLit(76.02))), [(Id(jP), For(Id(ZfV), Id(h0W), StringLit(QRe), Return())), (NumLit(98.88), For(Id(yjN), NumLit(56.16), BooleanLit(False), Block([For(Id(wEt), StringLit(LO), NumLit(99.34), Break)]))), (StringLit(OanV), Continue), (Id(S6), CallStmt(Id(TZD), [BooleanLit(False)])), (Id(PCee), Continue)], Continue)), (StringLit(nB), Break), (StringLit(miIuC), Block([Break, Block([])]))], None), Return(), AssignStmt(Id(yTlk), Id(vZY))])), VarDecl(Id(ZA), NumberType, None, None), VarDecl(Id(ggr), ArrayType([78.99], NumberType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115956))

	def test_21530115957(self):
		input = '''
func UK (bool Knt, bool FKM[29.77,82.31], number RN_[97.44,73.43,91.71])
	return

'''
		expect = '''Program([FuncDecl(Id(UK), [VarDecl(Id(Knt), BoolType, None, None), VarDecl(Id(FKM), ArrayType([29.77, 82.31], BoolType), None, None), VarDecl(Id(RN_), ArrayType([97.44, 73.43, 91.71], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115957))

	def test_21530115958(self):
		input = '''
func h9 ()	return 34.82

number LS <- true
string SW
'''
		expect = '''Program([FuncDecl(Id(h9), [], Return(NumLit(34.82))), VarDecl(Id(LS), NumberType, None, BooleanLit(True)), VarDecl(Id(SW), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115958))

	def test_21530115959(self):
		input = '''
bool PFC_[63.04] <- "IgJ"
var Txg <- Jy
func p0j (string seq, string Z2kw, number WQr)
	return
'''
		expect = '''Program([VarDecl(Id(PFC_), ArrayType([63.04], BoolType), None, StringLit(IgJ)), VarDecl(Id(Txg), None, var, Id(Jy)), FuncDecl(Id(p0j), [VarDecl(Id(seq), StringType, None, None), VarDecl(Id(Z2kw), StringType, None, None), VarDecl(Id(WQr), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115959))

	def test_21530115960(self):
		input = '''
var n9Mr <- 84.31
number G9g <- true
'''
		expect = '''Program([VarDecl(Id(n9Mr), None, var, NumLit(84.31)), VarDecl(Id(G9g), NumberType, None, BooleanLit(True))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115960))

	def test_21530115961(self):
		input = '''
func BQF (string f33p, number ob[8.26], number K05)	return k9j

func ywM ()	return 28.67

'''
		expect = '''Program([FuncDecl(Id(BQF), [VarDecl(Id(f33p), StringType, None, None), VarDecl(Id(ob), ArrayType([8.26], NumberType), None, None), VarDecl(Id(K05), NumberType, None, None)], Return(Id(k9j))), FuncDecl(Id(ywM), [], Return(NumLit(28.67)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115961))

	def test_21530115962(self):
		input = '''
func s9 ()
	return
func QB (bool i9Ib)	return 62.18
number OGZ8
func gJm (number YkDS[82.22,89.65,36.74], string yA5)	return "zZAqR"
'''
		expect = '''Program([FuncDecl(Id(s9), [], Return()), FuncDecl(Id(QB), [VarDecl(Id(i9Ib), BoolType, None, None)], Return(NumLit(62.18))), VarDecl(Id(OGZ8), NumberType, None, None), FuncDecl(Id(gJm), [VarDecl(Id(YkDS), ArrayType([82.22, 89.65, 36.74], NumberType), None, None), VarDecl(Id(yA5), StringType, None, None)], Return(StringLit(zZAqR)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115962))

	def test_21530115963(self):
		input = '''
dynamic BI5 <- "R"
'''
		expect = '''Program([VarDecl(Id(BI5), None, dynamic, StringLit(R))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115963))

	def test_21530115964(self):
		input = '''
func hg33 (string gU, number F2)
	return ci

func T_ (number SVBV)
	return "gcJrx"

'''
		expect = '''Program([FuncDecl(Id(hg33), [VarDecl(Id(gU), StringType, None, None), VarDecl(Id(F2), NumberType, None, None)], Return(Id(ci))), FuncDecl(Id(T_), [VarDecl(Id(SVBV), NumberType, None, None)], Return(StringLit(gcJrx)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115964))

	def test_21530115965(self):
		input = '''
func hnLC ()	return

'''
		expect = '''Program([FuncDecl(Id(hnLC), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115965))

	def test_21530115966(self):
		input = '''
number eDS[2.74,26.89] <- false
func wAg (bool jG[57.0,44.24], string Hu[80.52])
	return kr0
func w1pU (string VJW[36.48])	begin
	end
func bv (bool HT, number P7K, string UXb)
	return
func OEmx (number n0Z[30.57])
	return false
'''
		expect = '''Program([VarDecl(Id(eDS), ArrayType([2.74, 26.89], NumberType), None, BooleanLit(False)), FuncDecl(Id(wAg), [VarDecl(Id(jG), ArrayType([57.0, 44.24], BoolType), None, None), VarDecl(Id(Hu), ArrayType([80.52], StringType), None, None)], Return(Id(kr0))), FuncDecl(Id(w1pU), [VarDecl(Id(VJW), ArrayType([36.48], StringType), None, None)], Block([])), FuncDecl(Id(bv), [VarDecl(Id(HT), BoolType, None, None), VarDecl(Id(P7K), NumberType, None, None), VarDecl(Id(UXb), StringType, None, None)], Return()), FuncDecl(Id(OEmx), [VarDecl(Id(n0Z), ArrayType([30.57], NumberType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115966))

	def test_21530115967(self):
		input = '''
number pw3j[94.43,36.75,24.95]
bool De[9.61,24.18] <- false
'''
		expect = '''Program([VarDecl(Id(pw3j), ArrayType([94.43, 36.75, 24.95], NumberType), None, None), VarDecl(Id(De), ArrayType([9.61, 24.18], BoolType), None, BooleanLit(False))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115967))

	def test_21530115968(self):
		input = '''
string scN[74.89,10.15]
number nEiy
func WFbI ()
	return

'''
		expect = '''Program([VarDecl(Id(scN), ArrayType([74.89, 10.15], StringType), None, None), VarDecl(Id(nEiy), NumberType, None, None), FuncDecl(Id(WFbI), [], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115968))

	def test_21530115969(self):
		input = '''
bool hnn[24.36,0.06] <- 77.6
func oBpM (number j9M[82.24], string DUK[59.61,42.54])	return
number HpW[59.79]
func JdO (bool EYQW[78.01,90.45,32.34])
	return
bool y_[82.51,12.06,13.69] <- 37.13
'''
		expect = '''Program([VarDecl(Id(hnn), ArrayType([24.36, 0.06], BoolType), None, NumLit(77.6)), FuncDecl(Id(oBpM), [VarDecl(Id(j9M), ArrayType([82.24], NumberType), None, None), VarDecl(Id(DUK), ArrayType([59.61, 42.54], StringType), None, None)], Return()), VarDecl(Id(HpW), ArrayType([59.79], NumberType), None, None), FuncDecl(Id(JdO), [VarDecl(Id(EYQW), ArrayType([78.01, 90.45, 32.34], BoolType), None, None)], Return()), VarDecl(Id(y_), ArrayType([82.51, 12.06, 13.69], BoolType), None, NumLit(37.13))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115969))

	def test_21530115970(self):
		input = '''
func seaf (string F_Zs)
	return 73.39
bool akCk <- true
string nD <- "EESUB"
'''
		expect = '''Program([FuncDecl(Id(seaf), [VarDecl(Id(F_Zs), StringType, None, None)], Return(NumLit(73.39))), VarDecl(Id(akCk), BoolType, None, BooleanLit(True)), VarDecl(Id(nD), StringType, None, StringLit(EESUB))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115970))

	def test_21530115971(self):
		input = '''
bool KFVm
func kGc ()
	begin
	end
bool Xa <- o4pF
func Ae (number St[83.95,32.68,3.19])	return false

'''
		expect = '''Program([VarDecl(Id(KFVm), BoolType, None, None), FuncDecl(Id(kGc), [], Block([])), VarDecl(Id(Xa), BoolType, None, Id(o4pF)), FuncDecl(Id(Ae), [VarDecl(Id(St), ArrayType([83.95, 32.68, 3.19], NumberType), None, None)], Return(BooleanLit(False)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115971))

	def test_21530115972(self):
		input = '''
number Fw6[31.92]
dynamic an <- "VZZ"
'''
		expect = '''Program([VarDecl(Id(Fw6), ArrayType([31.92], NumberType), None, None), VarDecl(Id(an), None, dynamic, StringLit(VZZ))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115972))

	def test_21530115973(self):
		input = '''
dynamic Ea
dynamic y9 <- 54.66
'''
		expect = '''Program([VarDecl(Id(Ea), None, dynamic, None), VarDecl(Id(y9), None, dynamic, NumLit(54.66))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115973))

	def test_21530115974(self):
		input = '''
func Ly (string D9w, string gzh[58.05,75.63], bool Va)	return
'''
		expect = '''Program([FuncDecl(Id(Ly), [VarDecl(Id(D9w), StringType, None, None), VarDecl(Id(gzh), ArrayType([58.05, 75.63], StringType), None, None), VarDecl(Id(Va), BoolType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115974))

	def test_21530115975(self):
		input = '''
string NCcw[38.75,40.99]
number EOO[21.0,21.67]
func JzGK (bool fyC[71.03], string njWz, number PwUk[72.54,3.13,39.64])	return 71.49
func B_N (bool lTO[64.31])
	return 99.69

'''
		expect = '''Program([VarDecl(Id(NCcw), ArrayType([38.75, 40.99], StringType), None, None), VarDecl(Id(EOO), ArrayType([21.0, 21.67], NumberType), None, None), FuncDecl(Id(JzGK), [VarDecl(Id(fyC), ArrayType([71.03], BoolType), None, None), VarDecl(Id(njWz), StringType, None, None), VarDecl(Id(PwUk), ArrayType([72.54, 3.13, 39.64], NumberType), None, None)], Return(NumLit(71.49))), FuncDecl(Id(B_N), [VarDecl(Id(lTO), ArrayType([64.31], BoolType), None, None)], Return(NumLit(99.69)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115975))

	def test_21530115976(self):
		input = '''
func HuSc ()	return 16.11
func WE4 (string i1)
	return Ew

func Mku (string ed[37.11], bool Xp9T, bool dO6[71.29])
	return

'''
		expect = '''Program([FuncDecl(Id(HuSc), [], Return(NumLit(16.11))), FuncDecl(Id(WE4), [VarDecl(Id(i1), StringType, None, None)], Return(Id(Ew))), FuncDecl(Id(Mku), [VarDecl(Id(ed), ArrayType([37.11], StringType), None, None), VarDecl(Id(Xp9T), BoolType, None, None), VarDecl(Id(dO6), ArrayType([71.29], BoolType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115976))

	def test_21530115977(self):
		input = '''
func bui (number YnJ)	return

string yoL <- false
func ZTF (string OY[20.89,50.61], bool cV1x[53.61,11.17], string rkE[23.55,66.25,13.01])	return 16.74

func zZcV (string Aus, number fJW, string Qa)	begin
		M64z[false, "USZuE"] <- true
		bY("aTT", "qPRBr")
	end
'''
		expect = '''Program([FuncDecl(Id(bui), [VarDecl(Id(YnJ), NumberType, None, None)], Return()), VarDecl(Id(yoL), StringType, None, BooleanLit(False)), FuncDecl(Id(ZTF), [VarDecl(Id(OY), ArrayType([20.89, 50.61], StringType), None, None), VarDecl(Id(cV1x), ArrayType([53.61, 11.17], BoolType), None, None), VarDecl(Id(rkE), ArrayType([23.55, 66.25, 13.01], StringType), None, None)], Return(NumLit(16.74))), FuncDecl(Id(zZcV), [VarDecl(Id(Aus), StringType, None, None), VarDecl(Id(fJW), NumberType, None, None), VarDecl(Id(Qa), StringType, None, None)], Block([AssignStmt(ArrayCell(Id(M64z), [BooleanLit(False), StringLit(USZuE)]), BooleanLit(True)), CallStmt(Id(bY), [StringLit(aTT), StringLit(qPRBr)])]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115977))

	def test_21530115978(self):
		input = '''
func fFJG ()	begin
		continue
		czcM <- "olEyh"
		if ("Bw") number xmeL <- "L"
		elif ("d")
		continue
		elif (Ir8)
		zJQ7(Qku)
		elif (true)
		break
		elif (true) return
		else for QTe until 76.84 by false
			for Jtc until "Hj" by 99.84
				for bX until pA9A by 53.15
					for iz until 29.28 by true
						R5T <- 72.75
	end
'''
		expect = '''Program([FuncDecl(Id(fFJG), [], Block([Continue, AssignStmt(Id(czcM), StringLit(olEyh)), If((StringLit(Bw), VarDecl(Id(xmeL), NumberType, None, StringLit(L))), [(StringLit(d), Continue), (Id(Ir8), CallStmt(Id(zJQ7), [Id(Qku)])), (BooleanLit(True), Break), (BooleanLit(True), Return())], For(Id(QTe), NumLit(76.84), BooleanLit(False), For(Id(Jtc), StringLit(Hj), NumLit(99.84), For(Id(bX), Id(pA9A), NumLit(53.15), For(Id(iz), NumLit(29.28), BooleanLit(True), AssignStmt(Id(R5T), NumLit(72.75)))))))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115978))

	def test_21530115979(self):
		input = '''
bool S2b[98.36,35.99,42.81]
bool qpH[69.11] <- OurX
string ZU[48.74,95.19,1.28] <- false
number Gq[40.59,21.35,83.61]
number hX <- vNg
'''
		expect = '''Program([VarDecl(Id(S2b), ArrayType([98.36, 35.99, 42.81], BoolType), None, None), VarDecl(Id(qpH), ArrayType([69.11], BoolType), None, Id(OurX)), VarDecl(Id(ZU), ArrayType([48.74, 95.19, 1.28], StringType), None, BooleanLit(False)), VarDecl(Id(Gq), ArrayType([40.59, 21.35, 83.61], NumberType), None, None), VarDecl(Id(hX), NumberType, None, Id(vNg))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115979))

	def test_21530115980(self):
		input = '''
bool R5[51.73,54.6,99.82] <- "L"
func XQoP (string el[31.7,37.08,72.44], number wN[71.29,7.11], string eI)	begin
		SP(gviV, true)
		for R5t until "RFtR" by true
			return
		var Cht <- 53.81
	end

'''
		expect = '''Program([VarDecl(Id(R5), ArrayType([51.73, 54.6, 99.82], BoolType), None, StringLit(L)), FuncDecl(Id(XQoP), [VarDecl(Id(el), ArrayType([31.7, 37.08, 72.44], StringType), None, None), VarDecl(Id(wN), ArrayType([71.29, 7.11], NumberType), None, None), VarDecl(Id(eI), StringType, None, None)], Block([CallStmt(Id(SP), [Id(gviV), BooleanLit(True)]), For(Id(R5t), StringLit(RFtR), BooleanLit(True), Return()), VarDecl(Id(Cht), None, var, NumLit(53.81))]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115980))

	def test_21530115981(self):
		input = '''
number iw <- QA
string cmyQ[38.71,98.75,98.25] <- 57.08
'''
		expect = '''Program([VarDecl(Id(iw), NumberType, None, Id(QA)), VarDecl(Id(cmyQ), ArrayType([38.71, 98.75, 98.25], StringType), None, NumLit(57.08))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115981))

	def test_21530115982(self):
		input = '''
func wQ ()
	begin
		break
		begin
		end
	end
string os[57.11,88.4,80.41] <- aw
func O3E (number w0b, number bOZ[97.81,23.24,97.94])
	return
'''
		expect = '''Program([FuncDecl(Id(wQ), [], Block([Break, Block([])])), VarDecl(Id(os), ArrayType([57.11, 88.4, 80.41], StringType), None, Id(aw)), FuncDecl(Id(O3E), [VarDecl(Id(w0b), NumberType, None, None), VarDecl(Id(bOZ), ArrayType([97.81, 23.24, 97.94], NumberType), None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115982))

	def test_21530115983(self):
		input = '''
number hu_b
func Sy (string A0B[61.59,42.91], bool ab)
	begin
		continue
	end
var S8v <- true
func PpPL ()
	return true

'''
		expect = '''Program([VarDecl(Id(hu_b), NumberType, None, None), FuncDecl(Id(Sy), [VarDecl(Id(A0B), ArrayType([61.59, 42.91], StringType), None, None), VarDecl(Id(ab), BoolType, None, None)], Block([Continue])), VarDecl(Id(S8v), None, var, BooleanLit(True)), FuncDecl(Id(PpPL), [], Return(BooleanLit(True)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115983))

	def test_21530115984(self):
		input = '''
func Es (number t0G[46.69], string EgDH, number UQH8[90.65])
	return 7.07
number mBw <- 77.43
string UQ94[36.26,52.98,3.7]
'''
		expect = '''Program([FuncDecl(Id(Es), [VarDecl(Id(t0G), ArrayType([46.69], NumberType), None, None), VarDecl(Id(EgDH), StringType, None, None), VarDecl(Id(UQH8), ArrayType([90.65], NumberType), None, None)], Return(NumLit(7.07))), VarDecl(Id(mBw), NumberType, None, NumLit(77.43)), VarDecl(Id(UQ94), ArrayType([36.26, 52.98, 3.7], StringType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115984))

	def test_21530115985(self):
		input = '''
func Zxey (bool GtWi[26.56,57.04,75.34], number Wx, string Tmyr[99.79])	return true

func XdDa (number T4Ip[58.01])	return
func gaOD (number onn)	return "lOV"

func Du ()	begin
		continue
		begin
			begin
			end
			break
		end
	end

func SQx4 ()
	return 1.04
'''
		expect = '''Program([FuncDecl(Id(Zxey), [VarDecl(Id(GtWi), ArrayType([26.56, 57.04, 75.34], BoolType), None, None), VarDecl(Id(Wx), NumberType, None, None), VarDecl(Id(Tmyr), ArrayType([99.79], StringType), None, None)], Return(BooleanLit(True))), FuncDecl(Id(XdDa), [VarDecl(Id(T4Ip), ArrayType([58.01], NumberType), None, None)], Return()), FuncDecl(Id(gaOD), [VarDecl(Id(onn), NumberType, None, None)], Return(StringLit(lOV))), FuncDecl(Id(Du), [], Block([Continue, Block([Block([]), Break])])), FuncDecl(Id(SQx4), [], Return(NumLit(1.04)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115985))

	def test_21530115986(self):
		input = '''
func mJ6 (string vK[33.96], number p6W[48.63,21.36,50.98], bool KnLz)	return "zgq"
bool EOR
func QsB ()
	begin
	end

string yT3[97.1,63.92] <- "LHkc"
bool Oq[94.77,60.75]
'''
		expect = '''Program([FuncDecl(Id(mJ6), [VarDecl(Id(vK), ArrayType([33.96], StringType), None, None), VarDecl(Id(p6W), ArrayType([48.63, 21.36, 50.98], NumberType), None, None), VarDecl(Id(KnLz), BoolType, None, None)], Return(StringLit(zgq))), VarDecl(Id(EOR), BoolType, None, None), FuncDecl(Id(QsB), [], Block([])), VarDecl(Id(yT3), ArrayType([97.1, 63.92], StringType), None, StringLit(LHkc)), VarDecl(Id(Oq), ArrayType([94.77, 60.75], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115986))

	def test_21530115987(self):
		input = '''
bool Bmi[66.99,43.7] <- 96.97
bool f3Fl[0.72,68.38]
func rPp ()	return UfD

string gFF[81.05,93.29,0.03] <- 81.54
'''
		expect = '''Program([VarDecl(Id(Bmi), ArrayType([66.99, 43.7], BoolType), None, NumLit(96.97)), VarDecl(Id(f3Fl), ArrayType([0.72, 68.38], BoolType), None, None), FuncDecl(Id(rPp), [], Return(Id(UfD))), VarDecl(Id(gFF), ArrayType([81.05, 93.29, 0.03], StringType), None, NumLit(81.54))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115987))

	def test_21530115988(self):
		input = '''
func EIGO (string imr, number NldR, string oDnS[24.1])
	begin
		break
	end
var qo <- hK
bool LKR <- "tNCu"
bool km[0.97]
func qOr (string d6, bool Yqwx)
	begin
	end

'''
		expect = '''Program([FuncDecl(Id(EIGO), [VarDecl(Id(imr), StringType, None, None), VarDecl(Id(NldR), NumberType, None, None), VarDecl(Id(oDnS), ArrayType([24.1], StringType), None, None)], Block([Break])), VarDecl(Id(qo), None, var, Id(hK)), VarDecl(Id(LKR), BoolType, None, StringLit(tNCu)), VarDecl(Id(km), ArrayType([0.97], BoolType), None, None), FuncDecl(Id(qOr), [VarDecl(Id(d6), StringType, None, None), VarDecl(Id(Yqwx), BoolType, None, None)], Block([]))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115988))

	def test_21530115989(self):
		input = '''
func Vy (bool d2w[88.81])	return "Xjdo"

func CqC (string ID, string Vpb)
	begin
		IixL["krG", 95.74, wmnC] <- mci
		for Uk until false by 52.37
			if (Ny) continue
	end

func Xcq ()
	return 41.16

func I0M ()
	return "X"
bool HA[55.83,35.06,40.37]
'''
		expect = '''Program([FuncDecl(Id(Vy), [VarDecl(Id(d2w), ArrayType([88.81], BoolType), None, None)], Return(StringLit(Xjdo))), FuncDecl(Id(CqC), [VarDecl(Id(ID), StringType, None, None), VarDecl(Id(Vpb), StringType, None, None)], Block([AssignStmt(ArrayCell(Id(IixL), [StringLit(krG), NumLit(95.74), Id(wmnC)]), Id(mci)), For(Id(Uk), BooleanLit(False), NumLit(52.37), If((Id(Ny), Continue), [], None))])), FuncDecl(Id(Xcq), [], Return(NumLit(41.16))), FuncDecl(Id(I0M), [], Return(StringLit(X))), VarDecl(Id(HA), ArrayType([55.83, 35.06, 40.37], BoolType), None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115989))

	def test_21530115990(self):
		input = '''
string Cu[21.61] <- true
func Yi (bool bEam, string QSz[40.81,71.07])	return "clwl"

'''
		expect = '''Program([VarDecl(Id(Cu), ArrayType([21.61], StringType), None, BooleanLit(True)), FuncDecl(Id(Yi), [VarDecl(Id(bEam), BoolType, None, None), VarDecl(Id(QSz), ArrayType([40.81, 71.07], StringType), None, None)], Return(StringLit(clwl)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115990))

	def test_21530115991(self):
		input = '''
func Jrh ()	begin
		return
	end
dynamic oZ56 <- "gqSYK"
'''
		expect = '''Program([FuncDecl(Id(Jrh), [], Block([Return()])), VarDecl(Id(oZ56), None, dynamic, StringLit(gqSYK))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115991))

	def test_21530115992(self):
		input = '''
func kG ()	begin
	end

func Nu4z (number J06, number UW[98.58], string k9u)
	return
func Pdf8 ()
	begin
		return
	end

dynamic UZ
'''
		expect = '''Program([FuncDecl(Id(kG), [], Block([])), FuncDecl(Id(Nu4z), [VarDecl(Id(J06), NumberType, None, None), VarDecl(Id(UW), ArrayType([98.58], NumberType), None, None), VarDecl(Id(k9u), StringType, None, None)], Return()), FuncDecl(Id(Pdf8), [], Block([Return()])), VarDecl(Id(UZ), None, dynamic, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115992))

	def test_21530115993(self):
		input = '''
var MB <- UNvG
func b56 (string i5O)	return 92.89

func kc5I (string OFit, string TQk[29.08])	return "e"

'''
		expect = '''Program([VarDecl(Id(MB), None, var, Id(UNvG)), FuncDecl(Id(b56), [VarDecl(Id(i5O), StringType, None, None)], Return(NumLit(92.89))), FuncDecl(Id(kc5I), [VarDecl(Id(OFit), StringType, None, None), VarDecl(Id(TQk), ArrayType([29.08], StringType), None, None)], Return(StringLit(e)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115993))

	def test_21530115994(self):
		input = '''
string SoA[9.86,45.71] <- "lauZ"
func yV ()
	return 64.96

'''
		expect = '''Program([VarDecl(Id(SoA), ArrayType([9.86, 45.71], StringType), None, StringLit(lauZ)), FuncDecl(Id(yV), [], Return(NumLit(64.96)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115994))

	def test_21530115995(self):
		input = '''
var cS <- 70.76
string RC[65.81,80.71,26.08]
func hO (bool DNbH, string WX, bool pMd0[79.49,64.0])
	return
string AvBw
'''
		expect = '''Program([VarDecl(Id(cS), None, var, NumLit(70.76)), VarDecl(Id(RC), ArrayType([65.81, 80.71, 26.08], StringType), None, None), FuncDecl(Id(hO), [VarDecl(Id(DNbH), BoolType, None, None), VarDecl(Id(WX), StringType, None, None), VarDecl(Id(pMd0), ArrayType([79.49, 64.0], BoolType), None, None)], Return()), VarDecl(Id(AvBw), StringType, None, None)])'''
		self.assertTrue(TestAST.test(input, expect, 21530115995))

	def test_21530115996(self):
		input = '''
func O3D ()
	return 5.48
dynamic ct <- "hjoFQ"
func OdXj (number oq, bool kR[66.25,55.63])
	begin
	end
bool ICL[18.26,64.48]
func wPVr (number yP)	return ghJ2

'''
		expect = '''Program([FuncDecl(Id(O3D), [], Return(NumLit(5.48))), VarDecl(Id(ct), None, dynamic, StringLit(hjoFQ)), FuncDecl(Id(OdXj), [VarDecl(Id(oq), NumberType, None, None), VarDecl(Id(kR), ArrayType([66.25, 55.63], BoolType), None, None)], Block([])), VarDecl(Id(ICL), ArrayType([18.26, 64.48], BoolType), None, None), FuncDecl(Id(wPVr), [VarDecl(Id(yP), NumberType, None, None)], Return(Id(ghJ2)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115996))

	def test_21530115997(self):
		input = '''
string KnR[41.86] <- FQjO
func iNo (bool mZ[48.58])	return
string at6[20.37]
func Hb ()	return "s"

'''
		expect = '''Program([VarDecl(Id(KnR), ArrayType([41.86], StringType), None, Id(FQjO)), FuncDecl(Id(iNo), [VarDecl(Id(mZ), ArrayType([48.58], BoolType), None, None)], Return()), VarDecl(Id(at6), ArrayType([20.37], StringType), None, None), FuncDecl(Id(Hb), [], Return(StringLit(s)))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115997))

	def test_21530115998(self):
		input = '''
func hD3X ()	return 38.29

func zKJt ()
	return
func KoER (bool dg[80.18,34.59], bool vcMM, string ONG[79.34,78.85])	return
number uzqE[61.76,40.1]
func UuIL (bool bzZ, number u9md)	return
'''
		expect = '''Program([FuncDecl(Id(hD3X), [], Return(NumLit(38.29))), FuncDecl(Id(zKJt), [], Return()), FuncDecl(Id(KoER), [VarDecl(Id(dg), ArrayType([80.18, 34.59], BoolType), None, None), VarDecl(Id(vcMM), BoolType, None, None), VarDecl(Id(ONG), ArrayType([79.34, 78.85], StringType), None, None)], Return()), VarDecl(Id(uzqE), ArrayType([61.76, 40.1], NumberType), None, None), FuncDecl(Id(UuIL), [VarDecl(Id(bzZ), BoolType, None, None), VarDecl(Id(u9md), NumberType, None, None)], Return())])'''
		self.assertTrue(TestAST.test(input, expect, 21530115998))

	def test_21530115999(self):
		input = '''
func S8 (number jJRA[54.37,50.78], number vG[23.87], number ZQ[52.62,10.27,12.72])
	return ly

bool oOQ[9.69,59.07,21.1] <- yud
'''
		expect = '''Program([FuncDecl(Id(S8), [VarDecl(Id(jJRA), ArrayType([54.37, 50.78], NumberType), None, None), VarDecl(Id(vG), ArrayType([23.87], NumberType), None, None), VarDecl(Id(ZQ), ArrayType([52.62, 10.27, 12.72], NumberType), None, None)], Return(Id(ly))), VarDecl(Id(oOQ), ArrayType([9.69, 59.07, 21.1], BoolType), None, Id(yud))])'''
		self.assertTrue(TestAST.test(input, expect, 21530115999))
