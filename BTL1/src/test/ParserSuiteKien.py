import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_200(self):
		input = '''
## }58+b&
func b8Op (dynamic Emr, number fH[7,6.394E+68,355.016e80], bool U0[96,6.667,33])	return
bool fdG[1] <- T8Os() ## psW@*
'''
		expect = '''Error on line 4 col 0: bool'''
		self.assertTrue(TestParser.test(input, expect, 200))

	def test_201(self):
		input = '''
## m).Gn=E|O!sq3KzX
func sx (string ss[70e-47])	begin
		## tboc
		## a`CZhq8)pTZ{Lo
		Xz <- (ANAG())
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 201))

	def test_202(self):
		input = '''
## /q
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 202))

	def test_203(self):
		input = '''
## tnD
## kW- 0BY{:[Ynl)F1/9B
dynamic jmOb[2,6.733E+44,8.640] <- [15, "E'" '"z", "[p'"'";"]
var t4S[9e-68,5e+71] ## VLw^3x?_mvA:E4
## Eec+
'''
		expect = '''Error on line 4 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 203))

	def test_204(self):
		input = '''
## P=6
## 3qO=(yB
func kwDh ()
	return

func DsU (dynamic Nm0e, var Z7v)	return

'''
		expect = '''Error on line 7 col 24: var'''
		self.assertTrue(TestParser.test(input, expect, 204))

	def test_205(self):
		input = '''
func wQ_ (number yXV, string elok, number kAHB)	return false

func pw (var jc4)
	return
string kQY[290.309e-77]
string UI
'''
		expect = '''Error on line 4 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 205))

	def test_206(self):
		input = '''
## 3Pt8
dynamic Oiu <- "y'"'"" ## Ho:4GcD!eDEdn
## Jl:2yW5QNA-
func nJwJ (var Pp[66.481e+54])	return 8.345

'''
		expect = '''Error on line 3 col 23: ## Ho:4GcD!eDEdn'''
		self.assertTrue(TestParser.test(input, expect, 206))

	def test_207(self):
		input = '''
## Cz,(0
dynamic om <- 99.620E15 ## %$9JDrj|
## <V+
func yN (var Pn[2,1.151e09], number wA3[2,1e-73])
	return false

## dS**r%"/pt$
'''
		expect = '''Error on line 3 col 24: ## %$9JDrj|'''
		self.assertTrue(TestParser.test(input, expect, 207))

	def test_208(self):
		input = '''
string SIYI <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 208))

	def test_209(self):
		input = '''
##  H%-uzQVm{VA$H)*$
number wWGF <- "0'"'"s" ##  r50|K8
'''
		expect = '''Error on line 3 col 24: ##  r50|K8'''
		self.assertTrue(TestParser.test(input, expect, 209))

	def test_210(self):
		input = '''
## 8]w}d
func bzX ()
	begin
	end

func oeQ (number tSi)
	return 596E+70
func XI (bool JEU[590.231e+67,1.604,9.182])
	return k_Ox
bool SL <- PW ## ,)|Dw{dsE9}W_/
'''
		expect = '''Error on line 11 col 14: ## ,)|Dw{dsE9}W_/'''
		self.assertTrue(TestParser.test(input, expect, 210))

	def test_211(self):
		input = '''
bool OXo ## I
func L70 (var jyhx, var Fqby)
	begin
		## #{_l
	end
## x.m=^zpOr{zkG<}
'''
		expect = '''Error on line 2 col 9: ## I'''
		self.assertTrue(TestParser.test(input, expect, 211))

	def test_212(self):
		input = '''
func dEH (bool P9f[50,33.851e42], dynamic j7ub[91,42.580,99.126], bool uw)	return
func yT (var gGUB[88e-93,27], var dgq[63.617e+66], dynamic mum8)	begin
		## ^fh"!e6}sn *Q&Xv
		begin
			return "'"|P"
		end
		## X-}K1(um9dNX
	end

## M.??rnHFOH"}yb oN*
## mS7By!GQ/^{Buatuf59
func wYc (var VN, bool xR[1e38,46.270,790.902], string LK0[3.309e13,6.177E61])	return true

'''
		expect = '''Error on line 2 col 46: ['''
		self.assertTrue(TestParser.test(input, expect, 212))

	def test_213(self):
		input = '''
func yz (dynamic SF[499,336E-63])	return
dynamic hB[878.187E-06] ## <mA&X>m
'''
		expect = '''Error on line 2 col 19: ['''
		self.assertTrue(TestParser.test(input, expect, 213))

	def test_214(self):
		input = '''
func bn (string Ao0, dynamic x25i, bool o2)	begin
	end
var aw[56.114] <- "'"," ## Kpj&+POis&1
## ;8QwGkuT"a
## M{9V ,wWKG<_
func nhJ (number irRC, var dl[7E22])
	begin
	end

'''
		expect = '''Error on line 4 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 214))

	def test_215(self):
		input = '''
var GIF[622.405] <- PsNg
dynamic QIkl
## #ZT=6=%/J+f
## AqAt(>#V/U7L{zC
dynamic QTRP[51E+09,8e-09] <- true ## 8$%.%xUTHeIJX
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 215))

	def test_216(self):
		input = '''
func pI ()	return
var Zas <- false ## Y?9fhVKp7mhzKo|9
number jE[32,71.154e+63,63] <- true ## `Mbf[-rp8w]Km
## J_{C;fq!y&]3j|[*(h
## y[(M=1KrlOfT
'''
		expect = '''Error on line 3 col 0: var'''
		self.assertTrue(TestParser.test(input, expect, 216))

	def test_217(self):
		input = '''
dynamic Le
func LHL9 (number TcXg, number rU[8e97,58E-16,5.209e-86], string JAt[3E-69,10.782e-65,96.841])	begin
		## F0)$*1*a.$EY8VtY/
	end

func cTq ()	return
'''
		expect = '''Error on line 8 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 217))

	def test_218(self):
		input = '''
## 9oU .75gH-[`j, EkYv8
## {HPJ?.rm8!w7WB
## %Fc}Q433k&>8G]
func wI (string lPe6)	return "'"/'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 218))

	def test_219(self):
		input = '''
func gb (bool NG[5,258.493e47,456.639e+90])	begin
		vE <- "'""
		## L@_^<G1
	end

number LM_5 ## ]4jBO(W.rh@
## o
dynamic BLo
var z8qR[247.354,28,3]
'''
		expect = '''Error on line 7 col 12: ## ]4jBO(W.rh@'''
		self.assertTrue(TestParser.test(input, expect, 219))

	def test_220(self):
		input = '''
var hX4[55] <- Ikw ## t7pf]>(/Bh@<
number nL_u[1e66] ## !:$Q1El(55?d0[8McG, 
func qT ()	return

'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 220))

	def test_221(self):
		input = '''
## ,
## -/lN
## @Cy}{c[D
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 221))

	def test_222(self):
		input = '''
dynamic aW2Q[3.938]
## ZC@RK9+&;%{`-
func yRkL ()
	begin
	end
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 222))

	def test_223(self):
		input = '''
bool Ufp[50.947,3.374E+91,1.325] <- BE ## q7z2:sc
func MgY ()	begin
	end

func kMsR (var ly, var fsE[38.909E+75,279])
	begin
		## B -(&$"g53G~"N;QF1t
	end

## 8k[x7>u4)
'''
		expect = '''Error on line 2 col 39: ## q7z2:sc'''
		self.assertTrue(TestParser.test(input, expect, 223))

	def test_224(self):
		input = '''
func Ak (bool QXG, string bOFX[183E-98], dynamic t3)	return 90
## RQd`$9G
func Me (number PHi, var VP[722,891.576,75], dynamic HGe)
	begin
	end
func Cs (var QmY, number eRF)	return "'"6<'"r"

'''
		expect = '''Error on line 4 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 224))

	def test_225(self):
		input = '''
number fYWO[2e62,5] <- true
func VpEF (string y0s)	begin
		if true begin
			if false
			continue
			elif e8z for RnH until "X" by c5
				YTT()
			elif GW
			continue
			elif SH
			continue
			elif "'"'"" continue
			else yxt(wL)
			break
		end
		elif ZysH
		continue
		else return
		if 631E+49
		OV <- false
		elif j00u
		continue
		elif "D" wUT(q5, "f'"", "H'"'"k-")
		elif 954.352 return
		elif true if xFwT continue
		elif "pZ"
		if 4
		continue
		elif "'"" if 0
		break
		elif 268E-22 string CE2
		elif true ZMS()
		elif Rq
		if "c'""
		number wSjx[1.586] ## we|eXA9D-kV?x
		elif 71.734 var cShK[146e+79,67.936,72E36] ## LCoDfO"*/Rj
		elif true qfK <- "#_b'"'""
		elif true
		UTbs <- false
		elif "{%B"
		break
		elif "'"|l"
		if "'"" n7z <- "-1="
		elif false number xiIm
		elif 80e88 for SO until F1 by "nxo'"'""
			LZ["NCu"] <- true
		elif hY
		bZM(AW)
		else if e1m
		begin
			## /%;y]%c)e
		end
		elif "'":>" break
		for ZSV until Zfl by "'"X'"'""
			var IA ## H5=+
	end

## sh.IiU@9K(=g`I&Fdi
dynamic Zg_0[120] ## EV1P"Y}E>rmbh9
'''
		expect = '''Error on line 20 col 2: if'''
		self.assertTrue(TestParser.test(input, expect, 225))

	def test_226(self):
		input = '''
## |
## w(8F7<bP="=YO6"$
bool R2Y[3E80] <- 85E+00
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 226))

	def test_227(self):
		input = '''
## xxT6D8JcP]-&T&tG
## D]@b
bool lJR
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 227))

	def test_228(self):
		input = '''
func dYe (var su9, number SaK)
	begin
		## QtS(ELALwA
		## 6
	end
func Yv0l (bool oD)
	begin
	end

var PFh[8E+99] <- true ## YLnO$(gA<]V@~e;$:P~v
func khM (var qgY)	return 0

## c/P`lPq$2| EGYp
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 228))

	def test_229(self):
		input = '''
func tBng (number tm7c[9.061,43.520,22.844], string iF7[3.442E+16,4E+07,9.647e-61])	begin
	end
var WYp[136,73,84e-62]
func bMd ()	begin
	end

## Z(:]!
func mIA2 (bool yx)	begin
		## _Q0E_,,zQN//S
		qI()
		## PVEe$3VIVfBm4Hq
	end
'''
		expect = '''Error on line 4 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 229))

	def test_230(self):
		input = '''
## _9`
func hlaj ()
	return "'"a'"'"'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 230))

	def test_231(self):
		input = '''
string lcpS[133] <- false
func bG ()
	begin
		for sj65 until true by 49E+55
			break
		## S.K_l
	end

string s0Y <- "C3" ## C
func nu ()	return
var QO[960.962,64.378E-94]
'''
		expect = '''Error on line 10 col 19: ## C'''
		self.assertTrue(TestParser.test(input, expect, 231))

	def test_232(self):
		input = '''
bool fJW <- true ## ,>
func SDU (bool J7uL, bool p90[101,5e54], bool Vr)	return
## }5mO6{
dynamic lQu <- true ## H}IX2
'''
		expect = '''Error on line 2 col 17: ## ,>'''
		self.assertTrue(TestParser.test(input, expect, 232))

	def test_233(self):
		input = '''
bool eU ## K"}&SO$EX(L@a<EBF
'''
		expect = '''Error on line 2 col 8: ## K"}&SO$EX(L@a<EBF'''
		self.assertTrue(TestParser.test(input, expect, 233))

	def test_234(self):
		input = '''
## >V~TPC
## u6h6#zTO7(cQLb
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 234))

	def test_235(self):
		input = '''
string OGE <- Vej ## "!h?`9-ol0WpB>%PeOM
## )exj3uOCdmef+E
## d"s}GG(WHa3J
func Tt1 ()
	return

## 9+[ofP,6B"
'''
		expect = '''Error on line 2 col 18: ## "!h?`9-ol0WpB>%PeOM'''
		self.assertTrue(TestParser.test(input, expect, 235))

	def test_236(self):
		input = '''
func YjjI (var pe, string Blb)	return false
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 236))

	def test_237(self):
		input = '''
string lx7B
string CrA ## MGs4^@K#c9Fbl&
'''
		expect = '''Error on line 3 col 11: ## MGs4^@K#c9Fbl&'''
		self.assertTrue(TestParser.test(input, expect, 237))

	def test_238(self):
		input = '''
string gTb <- true ## e
func WB (number EfVF, number Vax, number zS[449.030])	return SB
'''
		expect = '''Error on line 2 col 19: ## e'''
		self.assertTrue(TestParser.test(input, expect, 238))

	def test_239(self):
		input = '''
func C95 (var npo, bool nF, string n_3)	return "'"Ce"
func js ()	begin
		return bUV
		continue
		if "=@'"J" MN5z(844e-84, true)
		elif "a'"'"" break
		else GD <- HPR
	end

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 239))

	def test_240(self):
		input = '''
## 29+M6
func en_e (bool w3GU[91.409E69], dynamic yFK[191], string Yiv[92.835e56,90e+61])	begin
		bJrZ <- true
		begin
		end
		## SRT#^{{~%
	end
var ZI[39.024,0.472E-65,790] <- true
## Z%]
'''
		expect = '''Error on line 3 col 44: ['''
		self.assertTrue(TestParser.test(input, expect, 240))

	def test_241(self):
		input = '''
## h5)^~x
func qpJ (bool kXiG[28.015E-36,9.313,4.328], bool K5j)
	begin
		JzwN(false)
		bool KL[2E23]
		## MgHs7}/sE8CY%213a 
	end
func tD (string bc[1.818E54], dynamic QAC[7e-45,420.123])	return "'"{"

'''
		expect = '''Error on line 9 col 41: ['''
		self.assertTrue(TestParser.test(input, expect, 241))

	def test_242(self):
		input = '''
## <$#|+DV(UgV
func tC ()	begin
	end

bool t1d ## 9xE.qI8
bool v8_W <- 1.007E+48 ## 3E?BBml2ZAx?|!G+aD
bool yJ <- yF
'''
		expect = '''Error on line 6 col 9: ## 9xE.qI8'''
		self.assertTrue(TestParser.test(input, expect, 242))

	def test_243(self):
		input = '''
func Ff ()	return
func m88 ()
	begin
	end

var K8
'''
		expect = '''Error on line 3 col 0: func'''
		self.assertTrue(TestParser.test(input, expect, 243))

	def test_244(self):
		input = '''
func cG7 (bool MS, number wqD3, bool a8g)
	return 65.619e+40

var UHDp
'''
		expect = '''Error on line 5 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 244))

	def test_245(self):
		input = '''
dynamic pL <- true ## 3`H
bool anyb[963.430E-80,4E99] <- 413.242E-28 ## !C%y==&:eB
'''
		expect = '''Error on line 2 col 19: ## 3`H'''
		self.assertTrue(TestParser.test(input, expect, 245))

	def test_246(self):
		input = '''
string Sf
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 246))

	def test_247(self):
		input = '''
dynamic F0hg ## iu=S
## 8-M
func pGJ (string iml[45.721,8.955E-04], bool vKqz[99], number HqRj[18.878E+25,119.935])	return true

func pIw ()
	begin
	end
func jI3 (bool lbUi, var dQ[909.725e-40,6.590,29.677E-86])	return
'''
		expect = '''Error on line 2 col 13: ## iu=S'''
		self.assertTrue(TestParser.test(input, expect, 247))

	def test_248(self):
		input = '''
func uJd7 ()
	begin
		## 7TF%5"#8Qd-Rh
		## O&1JJ/cE<gFp
		break
	end

string hvIa <- 3.308 ## Sel^+*67?
## (:
'''
		expect = '''Error on line 9 col 21: ## Sel^+*67?'''
		self.assertTrue(TestParser.test(input, expect, 248))

	def test_249(self):
		input = '''
## Pd
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 249))

	def test_250(self):
		input = '''
## xp:l
var q5[51.082,81E39,1e+38] ## r(5k^
'''
		expect = '''Error on line 3 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 250))

	def test_251(self):
		input = '''
## @^>H>F)kqr$[.BaAI_
## /toe]sP|JpmTSy[`W]l,
number bND[0.639E+01,72.237,4.961] ## A=t;
'''
		expect = '''Error on line 4 col 35: ## A=t;'''
		self.assertTrue(TestParser.test(input, expect, 251))

	def test_252(self):
		input = '''
func Iah (var WOr6)	return
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 252))

	def test_253(self):
		input = '''
bool OIpv ## Tt+4Mu
func HwO (number ozbr[78,536], number Cch[8.674e-65,62e-63])
	return 32.418e57

func g1eg (string wiN[66.130e-35,460.769e44,7.393])	return 74e37

number BKOp
'''
		expect = '''Error on line 2 col 10: ## Tt+4Mu'''
		self.assertTrue(TestParser.test(input, expect, 253))

	def test_254(self):
		input = '''
func V4 (number swvH[2.918,823.089E-89,1.277e+25])	return

## Nvrayo2X")hn@`W
func wmvl (number gnX, var Nfc)	begin
		## ,,nIvY;N6t$
	end
func yn (var Ei[0,52E+76,381], dynamic k5, number rj9)	begin
	end
'''
		expect = '''Error on line 5 col 23: var'''
		self.assertTrue(TestParser.test(input, expect, 254))

	def test_255(self):
		input = '''
## $G1mjz9F;"df35:;_|_
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 255))

	def test_256(self):
		input = '''
## Cx.fV/J9CR)
number qnq[54.124E+50] ## %dt
## YH?h9ar3z43[[
string z2i
'''
		expect = '''Error on line 3 col 23: ## %dt'''
		self.assertTrue(TestParser.test(input, expect, 256))

	def test_257(self):
		input = '''
## qIlo1fBZSmomxqY
var i5L[13E+23,90.615E85] <- "'""
## <X,;p8$Je6!2Jr`sA3<3
number c1J
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 257))

	def test_258(self):
		input = '''
## Xk~`6xtthHvn PL(e!
func Kh9 (number GwFg[437.067])	return true
func m2 ()
	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 258))

	def test_259(self):
		input = '''
func Cf (var fw[0.021])
	begin
	end
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 259))

	def test_260(self):
		input = '''
var de1[7.579] ## hH=_~ve]2RH9k8!s{r
bool Tc28 <- true
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 260))

	def test_261(self):
		input = '''
number d3[485] <- "r'"'"'"P"
func kjn (string LaLi[28.946e+52,49.271], bool Szm)	return BLa4
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 261))

	def test_262(self):
		input = '''
string fA[0e+48,0.490] <- true
func nU7 (string O_, string T41H, number u9h_[634])	begin
	end
func mVcU (number F7, bool iXtT[5e+97,7e+92])	return true

## *oxF
## :+9E%_k$I6|)+[@OFml
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 262))

	def test_263(self):
		input = '''
func OEk (number vhvp, bool uS[49.872E+26])
	begin
		if 290
		begin
			## >X&H;:i
			## euWIaSC1;=ZYRCH?@[
		end
		elif "'""
		break
		elif "A" return "CW'"'""
		elif false begin
			## |To*d/~FfYh8#J7!
			## Qxe|[EL0~-"c5tkD
			## oZ02TZ<o{eOD,PAJ/f
		end
		elif 132
		begin
			## +Qvts~BRi:
			begin
				## cg,g}/~=ce${
				## v
			end
			return RPi
		end
		else begin
			## b0;h7tby>bf
			## 3JnC2HNGp@"B7H+c,
		end
		dynamic b1 ## )%nV8y"?inJh?
	end
func Qr ()
	begin
		continue
		## XH{|lwioT9a
		## Wu)u ];d>Yn%c
	end
## 0.-O
func L5_z (var A4M[5e-22,4.566,641.058], dynamic vOa[56.994,30.234,8])
	return
'''
		expect = '''Error on line 30 col 13: ## )%nV8y"?inJh?'''
		self.assertTrue(TestParser.test(input, expect, 263))

	def test_264(self):
		input = '''
## aniy3#
number BElW
## uw~Q.)HJ:.p$=B2(i
## @
## 1O"sawUW8w(Pg
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 264))

	def test_265(self):
		input = '''
## q,{FP4[RBo
var f6[260e+03]
## kpgl/
'''
		expect = '''Error on line 3 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 265))

	def test_266(self):
		input = '''
func WDgb (var wY)
	begin
		## C(E(#_
		yPl(PhTE, 640.832, false)
	end

func R0m (var bOwu)
	return true

dynamic to <- L3
func GR (number Bbrk, var Cv_[31e07,0e42], bool rVr)
	return

## yf>Lc+|
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 266))

	def test_267(self):
		input = '''
func Pj ()
	return

number O6[238,381E+76]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 267))

	def test_268(self):
		input = '''
string iU <- 62.367 ## oTk;dp
func Tm_ ()
	return 8E16

'''
		expect = '''Error on line 2 col 20: ## oTk;dp'''
		self.assertTrue(TestParser.test(input, expect, 268))

	def test_269(self):
		input = '''
string X_pb ## 3BdM?[4o<@ $66, :@
## "d5X^K T<m,WA7,?nHx
'''
		expect = '''Error on line 2 col 12: ## 3BdM?[4o<@ $66, :@'''
		self.assertTrue(TestParser.test(input, expect, 269))

	def test_270(self):
		input = '''
func V8 (string Md, number MU[19e60,91.759,828], string yT0[539,1.291E91])
	begin
		## XP
	end

## c[n*oDG_uYj}Z /r-!
## 3PF(FzrhI)"uE
func gI (dynamic Mf, number ZyL, bool O6[8.542e73,602.688e+64])	return
number gVd <- "W'"ECL"
'''
		expect = '''Error on line 10 col 0: number'''
		self.assertTrue(TestParser.test(input, expect, 270))

	def test_271(self):
		input = '''
dynamic Ukl[54.095e24,8.845] <- "'"'"'"'"" ## WJ85j
bool wr[53.602]
func Z2D (number F5[88.443,748.863e+70,9.520], string bIOb)	return

## n6g1_)<1$y<cgrs?[u
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 271))

	def test_272(self):
		input = '''
## Wrxx<R1biNl2[VyIPpO(
string rVJv[301.113,9] <- nBZ ## [*C[#Bt*Tz9S+c~QCnl{
'''
		expect = '''Error on line 3 col 30: ## [*C[#Bt*Tz9S+c~QCnl{'''
		self.assertTrue(TestParser.test(input, expect, 272))

	def test_273(self):
		input = '''
func CYo (string JK6[88.295e-49,321e+31,81.571e+15])	return 2.736

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 273))

	def test_274(self):
		input = '''
## 2f_4=m+s|=xE9D g`A[v
func Hr7R (number p4WH, string qT[1.150E-63,273.647])	return 242.145

## >|P
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 274))

	def test_275(self):
		input = '''
var jS[29,2.489,6] <- 7e+40
## %?]!&w5" D
## 9{gh0
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 275))

	def test_276(self):
		input = '''
func jH (string exP5)
	return "Lhy"

var lE[625e+02] ## s1,Rc
func JtQ (var js[8.333E+06,35E+23], var RZG, bool GQ3)	return 772.019e-77
'''
		expect = '''Error on line 5 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 276))

	def test_277(self):
		input = '''
func g5 (var jO2s)
	begin
		for tZ until 491 by "J'"}|"
			return
	end

bool ECS[65.263E-33,81] ## T~2(-X#sB
dynamic aZs[6e82,9e-98,4.741e+92] <- "!" ## !M3?g6
## I1L5(HBL9L5dFH
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 277))

	def test_278(self):
		input = '''
dynamic CfRq[65e+82,42e81,5E04] ## u$;Sc52
## XIU3+fjdwQ%]{
## 9
dynamic XrPQ[0E67,8]
func QQ (bool O2k[7])
	return d8
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 278))

	def test_279(self):
		input = '''
func fej6 (dynamic qh, number Xs[1,633.370E-34])	begin
		WB()["['"'"'"'"", y5y] <- "'"'""
		break
	end

## ;bhRRU?g]P0EA*
## |vt
## ?C44AB% h
## ;@YN}*b2Xq^
'''
		expect = '''Error on line 3 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 279))

	def test_280(self):
		input = '''
dynamic xfr4[22.251] <- FfDg ## m9[XMod
number CIEu[6.302] <- true
func P_tQ ()	begin
		## 71q-
		## 8e/b[dnEv
		## F%QN!vE~<M< @H
	end

'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 280))

	def test_281(self):
		input = '''
func Ao ()
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 281))

	def test_282(self):
		input = '''
## />D?pUa
## oK+L|L/M,;2zCTE
number MlhX
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 282))

	def test_283(self):
		input = '''
func f42Z (number jkHf)	begin
		## &c-`bb)}U9>
	end

dynamic pvA
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 283))

	def test_284(self):
		input = '''
func eY (string K8Se, number rk, string RXZL[7,197,3E68])	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 284))

	def test_285(self):
		input = '''
func EiE (string d8A[701,454E87], var B6[76], dynamic C9Xx)	return

bool eJcE[0E+67,269.923,75.397] ## jr|K["O#E_
dynamic fYS[62.329e-03]
func l2HW (bool bKk1)	begin
		begin
			break
			break
			## A
		end
	end

func sde (var Efo[767])
	return
'''
		expect = '''Error on line 2 col 34: var'''
		self.assertTrue(TestParser.test(input, expect, 285))

	def test_286(self):
		input = '''
func yh (number aXd, string auz, dynamic EF[0,194.269])
	begin
		## }0q"#R
		## Vqvd6tp-Zg2f1yT
		d0HD(fc, false, false)
	end

## &
'''
		expect = '''Error on line 2 col 43: ['''
		self.assertTrue(TestParser.test(input, expect, 286))

	def test_287(self):
		input = '''
## 7b9u)W; hX2-w
func MWX (number IAts)	begin
		## SA$?D5d
	end

var ix <- Ak8y
func lhll (string s1[87.531E26,9E-70], number WO4w, string AV_x)
	return 87.099
dynamic nEB <- "w" ## 1Us,UcdJ
'''
		expect = '''Error on line 10 col 19: ## 1Us,UcdJ'''
		self.assertTrue(TestParser.test(input, expect, 287))

	def test_288(self):
		input = '''
## /`4!o "qx+*2
var g80
## wxAbH+2":RV/71$Rwe
'''
		expect = '''Error on line 3 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 288))

	def test_289(self):
		input = '''
## Hrr
bool H_08 <- true ## X,mZ"8SX$"wE&eFX.j
## mnBR39[Pe-^Y$)y*
func Luo (number Em, var uPGM)	return "]'","
func ZES (dynamic fpa6[672.488E-00,0.281e-43], string BE, number F8)
	return 1
'''
		expect = '''Error on line 3 col 18: ## X,mZ"8SX$"wE&eFX.j'''
		self.assertTrue(TestParser.test(input, expect, 289))

	def test_290(self):
		input = '''
bool MvIp[857,994] <- "'"" ## B
string Is0h[279e+45,13.541e-81] <- false ## )@R t k^L<:0KK8Qa(H
## ,:
'''
		expect = '''Error on line 2 col 27: ## B'''
		self.assertTrue(TestParser.test(input, expect, 290))

	def test_291(self):
		input = '''
## =4f_FnrBin
## ;k@.GR}ugBC5,Ec
## }[er3Q,;]cRddQ<
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 291))

	def test_292(self):
		input = '''
## _!+mxMa0Ee^mx:h%^a;}
func mc (var PB, bool vAq[527.176,60.921,377e27], var N8c[77,858.063,1.216E-30])
	return

## |
number WO0[4,6E09,1e69] <- "'"" ## (yS#<LBk
number Ngt <- 87e+23 ## }Y
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 292))

	def test_293(self):
		input = '''
var IA5k <- 12.640E+51 ## _
func WqP (bool dR, number pm, var fd[79.341E-72])	begin
	end

## :ieuq0SVN
func t8BG (var nVjr[26.335,150.187e54])	begin
		## "vK:Za
		## ~Q%F!x
	end
## J=
'''
		expect = '''Error on line 2 col 23: ## _'''
		self.assertTrue(TestParser.test(input, expect, 293))

	def test_294(self):
		input = '''
var vRL <- true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 294))

	def test_295(self):
		input = '''
## C}rxj*.RjV2FiMPn
func uN ()
	return
## w+#;B22
number I25Y[9] <- "'"" ## HA34&rvDEYn$Bx$y!73%
'''
		expect = '''Error on line 5 col 0: ## w+#;B22'''
		self.assertTrue(TestParser.test(input, expect, 295))

	def test_296(self):
		input = '''
## F!Snqk~cC
dynamic AcU[15.367] <- 776.261
## Lx6k_P>#8/
func j4jH (bool de, dynamic WR)	return
##  
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 296))

	def test_297(self):
		input = '''
bool yItN[9.143,300.000e26] <- x8 ## PJZ|JaTJ6,?33#g8.
dynamic mnIf ## F_8L
## @#b~=/Rd
## LMoxwQx^uY
## :E.90`HL?3P1]Rw.
'''
		expect = '''Error on line 2 col 34: ## PJZ|JaTJ6,?33#g8.'''
		self.assertTrue(TestParser.test(input, expect, 297))

	def test_298(self):
		input = '''
## DTAr#
func RcFh ()	return true
## GXm*Nr7)HnGDJ=LOEckG
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 298))

	def test_299(self):
		input = '''
func lk (bool LW[4,7e-10])
	return
## `_%fFIA!s:
'''
		expect = '''Error on line 4 col 0: ## `_%fFIA!s:'''
		self.assertTrue(TestParser.test(input, expect, 299))
