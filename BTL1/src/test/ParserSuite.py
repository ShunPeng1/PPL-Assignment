import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_2513011300(self):
		input = '''
dynamic Ov ## V[*hsh{#Hxrp;]Mon{[M
bool Q4 ## PN?>P1*ZN2lX(yHXv 
var xdf ## EpN@l@w>Z;$`yG$qA$X
'''
		expect = '''Error on line 4 col 30: 
'''
		self.assertTrue(TestParser.test(input, expect, 2513011300))

	def test_2513011301(self):
		input = '''
## )xAvi
func YX (var fXqL, string Oae, number e7)	begin
	end

## -.W9-1"t
## "^{a;kB,~z0*
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011301))

	def test_2513011302(self):
		input = '''
dynamic pBU <- (HgV(false, Ovsm) == "'"'"'"|'"" + 4.878e-66)
func iP ()
	return 231
## +UA
## /05@4`aoV(Tw8xeoC
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011302))

	def test_2513011303(self):
		input = '''
number eW[14,359E-66] <- "p_" ## ]uXzlE0s_]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011303))

	def test_2513011304(self):
		input = '''
## /KcCEwTwyj*o}.O[F>J
dynamic BpW[6,36E97]
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011304))

	def test_2513011305(self):
		input = '''
number Njr0 <- 3.684E-58
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011305))

	def test_2513011306(self):
		input = '''
number e9C <- "u'"a"
## xMbb!v9XU
string xx[9.906,49.409e-84] ## |N
## [ynl;u9R:t,utey
func yzH (string YhFh[799E+24], bool bM2[4,768], string It[5.721E85,0,143])
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011306))

	def test_2513011307(self):
		input = '''
## )(6T
## a(l
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011307))

	def test_2513011308(self):
		input = '''
## 5WAde>-r?;S#?GM##
## a-,
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011308))

	def test_2513011309(self):
		input = '''
func Ia ()
	return 2
## nV>$$O6Q~
bool E16h <- "'""
func LM (bool Em8[5.023e+36,9e-85], bool BiSH)	begin
		break
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011309))

	def test_2513011310(self):
		input = '''
func KE0Z (dynamic Vncd[4e-57,5])
	return 754.421

func ys (var iHCD[476,3.970e+84], dynamic EZ_[1.141], string WEe[45.188,77E35])
	return
bool faub[9,49] <- true ## %-<:F:Z$1%]A~%<yhW
var lSa <- false
bool iG
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011310))

	def test_2513011311(self):
		input = '''
## bvUTWx9&dtC8"Ka/Dm
number iwZ6 <- Z4Bn ## ?x22)$WVh4eaLB%dY
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011311))

	def test_2513011312(self):
		input = '''
## cRX%E]={LhK1b!4
func YF (bool pl[5.631,41.965])	begin
		begin
		end
	end

## N|X
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011312))

	def test_2513011313(self):
		input = '''
## 6>24;
func eart ()	begin
		## s4l$8}=ZG5Pkz
		## @eML;AYX
		begin
			Bhew()
			for uI until hz by Hg
				qu(Vrf)
		end
	end
number IOB[4,411e-00,0.114] ## `
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011313))

	def test_2513011314(self):
		input = '''
dynamic qS <- false ## (4^`nM_tnbS.
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011314))

	def test_2513011315(self):
		input = '''
## >_/)LthEH
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011315))

	def test_2513011316(self):
		input = '''
func sCT (bool fo45, dynamic mfCt[777], dynamic ly[523.040,3])	begin
	end

bool WZZI
## VU8>
func hU (number YuBx)	return "e'""

number x3rd[50.851E+83,96e-40]
'''
		expect = '''Error on line 2 col 21: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011316))

	def test_2513011317(self):
		input = '''
## *ugtT-^=?k_H
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011317))

	def test_2513011318(self):
		input = '''
## GY#
## 5A[L"jVo|y:@*
func wG (bool ZbtF, dynamic FA8[636.817E+32,539])	return true
'''
		expect = '''Error on line 4 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011318))

	def test_2513011319(self):
		input = '''
## ghh :L5we}+!Y^6%U_
string J6f <- 8.647 ## y9,"b{7VzT+!8s+
func PK ()
	begin
		## FD
		if (O_) begin
			## erw"Ht%Rz
			## C]odF_dLw_~e{$D{`)a
		end
		elif (p1e) begin
		end
		elif (Bhf)
		continue
		else for Cyhd until false by 0.863
			break
		## f
	end

## U"ZP}>v{5].T%DB
dynamic mL[903E-83] <- "M" ## +!z@X8SHgJ7Wn2qn9|I
'''
		expect = '''Error on line 21 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011319))

	def test_2513011320(self):
		input = '''
## T*6CRFkS6?(P
## JH^_a6mM)mPl./
## )3@Nw8@uFQk} tY
string SJ
func wVq (bool FOF, var A67f, string f1G4[78E+20,89.291E-30,9e-94])	return
'''
		expect = '''Error on line 6 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011320))

	def test_2513011321(self):
		input = '''
dynamic gc <- 2.108e-91 ## ifE
func q0Pq (dynamic t09R, string zyk[5.282E77,570.018E50])	return

number pgS[429e-81,2.311] <- ljw ## ^s+v%U!>nuy<^
func HI_C (number C3N, string eGC[36.597E+53,0E+54,6.458e+72], var dS8)
	return 10E43
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011321))

	def test_2513011322(self):
		input = '''
func hM6B ()	begin
		## aKcs@^p^;u
		for eymb until 357.323 by true
			begin
				## zfAHwCjX
			end
	end
func P2E0 (var xP, var oRu)	return tNrr
## ;KyNBA dde
'''
		expect = '''Error on line 9 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011322))

	def test_2513011323(self):
		input = '''
func Eu (number cWx[85,6.389])
	begin
		begin
			aGI(true, ap, 666.781)
			begin
				## R2
			end
		end
		qKuv(false)
		continue
	end
func Z2 (number x__m[290.346e-97,7])
	return ".'"'""
func e4_y ()
	begin
	end
func pf3 (string mf)	begin
		## T2G!]LqYII"R4
		if (sAv) BkNL(1.117)
		elif (Ye_)
		break
		elif ("J'"s'"")
		TXu("'"'"'"")
		elif (true)
		break
		elif ("'"'"") for BZ until hjF1 by SQ
			return 756E-29
		## stNA@GD9n
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011323))

	def test_2513011324(self):
		input = '''
## )`~wt]*l
func JJPp (bool Mqxi[9,48.399], var XN_8)
	begin
		## b|`z%pD/_Et~9-.5l~
		dVD_(false)
		bool wd <- "'"a'""
	end
## <Lw6o.uy*@2
'''
		expect = '''Error on line 3 col 32: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011324))

	def test_2513011325(self):
		input = '''
string NcSY[0,25e-86] <- false
func e9 ()
	return
func FG1 ()
	begin
		M6v(0)
		cuS(false, wGGE)
	end
## .#C_)arz@U<ezZ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011325))

	def test_2513011326(self):
		input = '''
## m7;jAh,S[,oVhs$-
func WWvC ()	begin
		## $G}O(ac$Us :wS
		lspn(kS4b)
	end
bool eyG <- "VT" ## rAC~pq#Bh(L/
func BYcY (bool cfpD, bool gUjm)	return mfEj

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011326))

	def test_2513011327(self):
		input = '''
string M_Yj[9,1.013] <- false
bool oL_H
string ZnY ## pF@(:A6zTQ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011327))

	def test_2513011328(self):
		input = '''
## 5rafK)eQl`f
## w>gKVL!ylG3:$2oBr1f
## nCO (FRJ}S05ly+QvyMt
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011328))

	def test_2513011329(self):
		input = '''
func xCBl (string PRL)
	begin
		CB(pm)
		## S<>
	end

var ilx6[144.058E23] <- KAsS ## M1=PhJW8X8)|&M;!y>~&
## }^=&t_8BJuv@:KG~
## 2/
## -PhJ:d|9aH[K&YVl
'''
		expect = '''Error on line 8 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011329))

	def test_2513011330(self):
		input = '''
## *6l$$5sn;X~sg
func lI (number t88r[768E-08,1,9.423e05], string AC[34.337E87], var TL)
	return
'''
		expect = '''Error on line 3 col 64: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011330))

	def test_2513011331(self):
		input = '''
dynamic eOK ## a]`<%
## 4?[:A4f
func vC (number YG, var hLFk[619.167,925.888], var Koj[9e-59,20])	begin
		d5(mc, k4)
	end

## Fqc
'''
		expect = '''Error on line 4 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011331))

	def test_2513011332(self):
		input = '''
func jc (number j2Oa[381.533,20.829E+71], var eeM[5.359e+11,82e84], dynamic Fnd)	begin
		## ?%!v~]T.s]/09>9y$
		## C?`2etY)
		break
	end

bool ZFs[3.384e-60] <- "bpnq"
func an (string Tvz, var M2jR[443.785,935.930E66], dynamic qGkq[450e-18])	return "'"g'""
func aVk (var L3q5)
	return 19.975e+55

func aY1s (string qsIv[851.726], number gYW[87], dynamic ePyl[860e86,543.930E+59,31.507])
	return
'''
		expect = '''Error on line 2 col 42: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011332))

	def test_2513011333(self):
		input = '''
func CHfy (number tIQ, bool EExr[6E59,78e45,892.065E+46], bool Z0[87E81,904.895])	return
## ~5x(h}^?E>}+*otE
var e5 <- true ## ^J`}>[NY]Xg^Q
func Bm (var aGNV, var LsHY[6.137E+72])
	return
'''
		expect = '''Error on line 5 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011333))

	def test_2513011334(self):
		input = '''
var NKBt[3E+20] ## j~t7
func RP (var W8i7, dynamic bjhi[7.071e+76,76e33], dynamic BiOF[5e+74,18e-34,6.390])	begin
		## pg,R)C&
		return "^'"'""
		X1kD <- false
	end

## V2feDLk6
func B9 (dynamic GFE[832E48,78.126e-86], string DR)	return true
func xL2u (number TK4b[121.992e84,71e+47,122E+68], dynamic yX6)	begin
	end

'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011334))

	def test_2513011335(self):
		input = '''
func O2 (string gtUk, number t4)
	return true
func eGn (dynamic RQZ)	return JGa
## Hn:L8
'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011335))

	def test_2513011336(self):
		input = '''
## -M@qryG&Mip5>c8b0yR
func Mk ()
	return true

func GQ (string Uhn, string eQ0[748.079E-47,458.371e-79,711.791], dynamic wG[9.198e+27,893E+41,26.435])	return l39
'''
		expect = '''Error on line 6 col 66: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011336))

	def test_2513011337(self):
		input = '''
func ENA (dynamic HFN, bool LXt[527.802,69.274E26,4.097E+30], string PEiR[1e-73,8.762E-40])	return "'"'"'"Y%"
dynamic OUDN[543.720E58,12E+19,602.697E-95]
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011337))

	def test_2513011338(self):
		input = '''
bool g_t[55E+63,4.210,32] ## SB
func Fn ()	return a4Bz
## ]&._?bQE
func aRG (var GeQ[290e-46,708.702e+44,128.048])	return

## 4q
'''
		expect = '''Error on line 5 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011338))

	def test_2513011339(self):
		input = '''
bool pjZ ## 11xGKuCiW78{
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011339))

	def test_2513011340(self):
		input = '''
bool IWsI ## M=A&Lh"DfmL>
dynamic WSM
var UmRJ[9e82,986e-11,274.606e-72] <- Ir8 ## KA[>Sh*5BWcDeO
bool abnO[80.831e89,6.643] <- "qs'"3" ## ao}/N,&$~.dCbS^s^^
## Q
'''
		expect = '''Error on line 4 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011340))

	def test_2513011341(self):
		input = '''
bool z5_ <- false
func eD ()
	begin
	end

## y`!KLilt6
## "R=oiv(
## Uv2t>}.=
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011341))

	def test_2513011342(self):
		input = '''
## 3g
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011342))

	def test_2513011343(self):
		input = '''
string QQ1h <- "L'"'"'"D"
dynamic EPe[8,6E98,5.757E-57] ## m4_2,#!/ry|Bvk<7;n
## t
number pp ## Q9_?qC=~o~Fc/,
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011343))

	def test_2513011344(self):
		input = '''
string au[672.214e-94,5E-87] <- NJ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011344))

	def test_2513011345(self):
		input = '''
## kD@/LGc1}m~
bool k3 <- 30 ## ~
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011345))

	def test_2513011346(self):
		input = '''
## 6)D?Z;n2M%i#Py1hb(>
var tdIX[313e+58,7.431e+85,2E59] ## 8v0G) m[xzF_
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011346))

	def test_2513011347(self):
		input = '''
func eYV (dynamic GXF)	return IY
bool KxI[52E+22,55e-99,5e-75] <- 72.440E+21 ## 3OI
## iPNv!R~hR6?/mxw= 7K@
func wqY ()
	return true

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011347))

	def test_2513011348(self):
		input = '''
##  x"
func SMbq (var nFz, string LdP2[9,0.638e+16,0])	return true
func AJ7 ()
	return
## diyW?Y8?jo
func e4F (number VR, bool FV)	return

'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011348))

	def test_2513011349(self):
		input = '''
## ES!+
bool MD <- false ## $73FB
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011349))

	def test_2513011350(self):
		input = '''
number IRT[405.138E+24,62,863.890] <- 59.717E+41
## s]l"D7/75$[ Z|m=?E2
## V]|~SSBRnR>B&dR5w9
bool OLf <- XQB
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011350))

	def test_2513011351(self):
		input = '''
bool UdF[40.217e+64,3.996,288.422] ## 7@H;1
func Hkc (number Q_v[4e-88])	return

## )x~S@]51)|g]/oeb
bool rE[94E64,322.750E-16,63.198] <- waC
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011351))

	def test_2513011352(self):
		input = '''
func lovr (string i0hO, string Wg)
	return vPGy
## %Jo*MHq4rH7Wt
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011352))

	def test_2513011353(self):
		input = '''
dynamic EXJY ## BP%$k36
func CAkA (dynamic NK_x)	return
bool GHf <- 362.503e03
func r4Ad ()	begin
		break
		begin
		end
	end
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011353))

	def test_2513011354(self):
		input = '''
var vrj[644] <- 46.166e79
## 8[>Xnz2A6H^mL
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011354))

	def test_2513011355(self):
		input = '''
## 61Y`MOAcj.K]+O
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011355))

	def test_2513011356(self):
		input = '''
## B@Rt0c=x@"O%
## eH,Jw_(?6Z{d3Ka=j0#;
string DO <- "<j" ## ms,;*lH;f]T^cn_M(y
func lFd ()
	return "a"

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011356))

	def test_2513011357(self):
		input = '''
## M_4/5iN&]"48I-
## 5T%
dynamic DZAm[367,6,7] <- 975.405e85
## *1RYOq0G{
func Py (var MtjA, var YX[238], number cZ[2.850,9,3E-52])	return Wu7
'''
		expect = '''Error on line 4 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011357))

	def test_2513011358(self):
		input = '''
func pN6I (dynamic eKan[17.895E+06], dynamic o_, number Kg[0.221,4])	return

## h8
## X/YMdx~x:L[
## ZV{<97q<
func kj (number k2oV, string yWG)	return
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011358))

	def test_2513011359(self):
		input = '''
string iVgx[3E-66]
func oMi8 (bool bQ[13e+82])
	return "j;'"'""
func BL (number Kutt, string Sng[42.295,21.907,7.422e+38])	begin
		begin
			break
			if (false) for FAsZ until a0z by "U'""
				return
			elif (253.572e+28)
			string t6K[497.632e+87,71e-46] ## 8}3y`*4)tFi}M9
			elif ("'"")
			j_a2(MYrd, 9.242)
			elif (true)
			return
			elif (5E-30)
			for yF until xJm by Oy
				begin
					RvA[true, iz] <- NP
					## |5u}wJDX@}^Q!
				end
			elif (true) e66s[false, 6E06] <- 3
		end
		## =bcd?!/f;`S+-/iAxT
	end

number U3zJ[0E-23,3.487,169e+14] <- 229.930 ## %?VF?N#r_@8{k9ny
## Z}5MW
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011359))

	def test_2513011360(self):
		input = '''
func PG_b (string fG_[9.360,7,843E06], var vtr4, string Ty2)	return
func jp0w ()
	return 0E20
func Bkp (string vf[55,6e-98,86], bool bAL[9.938])
	return
## H
'''
		expect = '''Error on line 2 col 39: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011360))

	def test_2513011361(self):
		input = '''
dynamic cAqF <- 453E16 ## 1X!
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011361))

	def test_2513011362(self):
		input = '''
## v}2+4l?!Mb,^0X3
## y8g*S[<ANq
## t2v"xs"I
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011362))

	def test_2513011363(self):
		input = '''
func Wm06 ()
	return

bool tX4[8.225] <- 870
func Qj ()	return 141.765e-49
string oVsi <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011363))

	def test_2513011364(self):
		input = '''
## 6HUXzQr<(O+o^g
func Oc1M (dynamic uB[435], dynamic t_qv, string qV1j[20.568,60])	begin
		## P
		continue
	end
number Ks5 <- "'""
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011364))

	def test_2513011365(self):
		input = '''
string LQ5[612.314,813e-89,7E34] ## t9@e*p
## JH]=ja`!]uH9=cs
## &$-#+$Eu<25:#s
var RE
## O6r%j)I#
'''
		expect = '''Error on line 5 col 6: 
'''
		self.assertTrue(TestParser.test(input, expect, 2513011365))

	def test_2513011366(self):
		input = '''
## p
func sho ()	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011366))

	def test_2513011367(self):
		input = '''
bool lG[416] <- 70
func HLg ()	return 37e+95

func d8 (dynamic sFj, bool RQ)
	return hO

func Da9e (dynamic Mix)
	begin
		RX(253E-70)
		## yMW
		if (false) for o9 until E0h by true
			q2Yi(kf5, "'"", W3)
		elif (881.974e39) for XRS until false by 371.321
			break
	end
'''
		expect = '''Error on line 5 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011367))

	def test_2513011368(self):
		input = '''
var bpNN[5.827E-32,329e+81,94e28] <- true
func yMI (string Y1, bool Em2l[14e+18])	return false

## |-[}Ss{*I![dWB
## (/
## )A/gme<8Lvp|r#hKWVg5
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011368))

	def test_2513011369(self):
		input = '''
dynamic wqG9 ## f
## #?7z=YO15:z*Tt
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011369))

	def test_2513011370(self):
		input = '''
## +TX|t:J=z7y kXa.r
## n-AL_$
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011370))

	def test_2513011371(self):
		input = '''
## R]$}=v65x/
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011371))

	def test_2513011372(self):
		input = '''
func bE (number GTI, dynamic Fw)
	begin
	end
dynamic mG[180.915,775.492,517e+29] ## <+i#0J[5DS?;lT
func Niw (bool H_[426])
	return
'''
		expect = '''Error on line 2 col 21: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011372))

	def test_2513011373(self):
		input = '''
func rWwi (dynamic c4rq, string bFwY[6E+97])
	return

var kxNI[19,6.180,61.131e+22] <- false ## KVE#%>!+CbluqvyO3N
## (7H<AxA;Fsv4)vD5u~/
func pC (bool rU, string E47c, dynamic bm[168.449E-18])	begin
	end
## N&a}8fLbu%IfVt!U+4S
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011373))

	def test_2513011374(self):
		input = '''
string YX4W <- true
var cu[63.621E+68,5,78E01] <- jh
string hApN
'''
		expect = '''Error on line 3 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011374))

	def test_2513011375(self):
		input = '''
bool KSsk[4.939]
dynamic fU5[9,26]
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011375))

	def test_2513011376(self):
		input = '''
string w70B ## E
## T/Y>p,s;FS"vh]7eTP~>
## &JPcEy<1Q^3o$M[]WkgC
bool aRt3[1,4.427e59] <- "'""
## Z-dM)ht,{.5
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011376))

	def test_2513011377(self):
		input = '''
func Gd_J (bool lx7A)
	return
## [&y]f}}3>
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011377))

	def test_2513011378(self):
		input = '''
func b5 (string NQ, number VBv, number Ecd[95e-85,1,38.522E89])	begin
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011378))

	def test_2513011379(self):
		input = '''
func QLR (var CE[969])	begin
		## }hp19PbL.L(0hg.J
	end

func hoJe (bool fN[712.660], var kZam[567.949E+29], var T1T)	return
number Zy[5] ## 5TPjf.pDt}/QJhpj:
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011379))

	def test_2513011380(self):
		input = '''
func IfV (bool Bol[6.048,82.848e-28], string tC[159.014e40,75.253,719], number ARL)	return
bool oA <- HE
## +vXMHaM`H+tTn{
## Rw#";%b4d^b.J
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011380))

	def test_2513011381(self):
		input = '''
func GTWb (string SPVT[209.471,17,856.248])	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011381))

	def test_2513011382(self):
		input = '''
string tXxf[48.903,16.685e-00] <- false ## j?y&/Ve[E8*wNHX
bool yO5f ## mP
## ([;x4w^,F#>+K:4oiA
var zXlm[666E+96]
string nih[295e+69,48E29,5] ## nEjk$.sX1,
'''
		expect = '''Error on line 5 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011382))

	def test_2513011383(self):
		input = '''
func dUG_ (bool EW[365.897,0E-16], dynamic fP)
	begin
		## .sISe@5V$t
	end
dynamic vrW[1.620] <- 598E-27
'''
		expect = '''Error on line 2 col 35: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011383))

	def test_2513011384(self):
		input = '''
bool zz[620E+28,64e-51,843.292] <- DsNL ## P]sR#n-9uY=I<#!B}Zg
number Hzh[329.824,232,653] ## waL8a
func EoKW (var XX5[203.832e17], number iQi[85.910E36,431.266])	return
func oz0w ()
	return

'''
		expect = '''Error on line 4 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011384))

	def test_2513011385(self):
		input = '''
func VoJf (number trih[8.052E-40,77,101E76], var Rum[4.629])	begin
		## 5$go*`cB?HFu_&4f
		ECbc(174, kWX7)
		## ^Q}xnsc
	end

dynamic Xt[74.403] <- 67.859e-13 ## H_w4gGyt| -qC
number tr9K
'''
		expect = '''Error on line 2 col 45: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011385))

	def test_2513011386(self):
		input = '''
dynamic JrQA ## 22?wsV)n~e5}:j7+
## ax>5q=
dynamic zz54 <- 1.264e-83
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011386))

	def test_2513011387(self):
		input = '''
string bdA ## giaE_AwybYI?7p$(,
## )%|>ZEOjCH_7
func eUP2 (dynamic xB1, number DfDe[95,944e+85,3], string T2RX)
	begin
		## n(DLT1D
	end

string jBJE[716.744] <- kb5q
func nF (dynamic SJ, var GDkD)	return 8E+91
'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011387))

	def test_2513011388(self):
		input = '''
func f2eV (var qx)	begin
		begin
			## j5z%:JBcCg1b/Y-pRq
			for xxFY until false by q5o
				if ("'"")
				YOc[18E+97, L3, true] <- fX
				elif (" ") TI("B'"'"", "=O^S'"", ":v'"'"#")
				elif ("'"")
				number gS[799E65,23.759e77,6.415e+40] <- false ## aY#
		end
		## M3Hw|B#N!5AR39
	end
## 5[pHNIsj5Mh<ro/d`yJ
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011388))

	def test_2513011389(self):
		input = '''
## j})q{G5GC#FwjNwLl=-F
var s4Ws
'''
		expect = '''Error on line 3 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 2513011389))

	def test_2513011390(self):
		input = '''
func fX (bool s1, var uDay[826], number p5Dr[3e12])	return false

dynamic LM <- true
func uKt ()
	return TfL

'''
		expect = '''Error on line 2 col 18: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011390))

	def test_2513011391(self):
		input = '''
func QCya (var k4[689.997,76e+22,0E+40], string PB[61])
	return

func nU (var FTg, var t5Wf[466.462])	return Gz

'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011391))

	def test_2513011392(self):
		input = '''
func WGZ (dynamic EZA[34], bool MXNC[4,968E-89,5.407e-84])
	return
## JLsdh]SD6R8geg.M
string sJ[2.578] ## h(;;kJn{8C5T
## .< >
bool xbmS[791.516] <- 1
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011392))

	def test_2513011393(self):
		input = '''
## 6_C`
func AgOe (dynamic eIW[930.255E-67])	return 47.919

## B)7hbn$p=
bool vt[34.412]
func aL72 ()	return
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011393))

	def test_2513011394(self):
		input = '''
bool eY <- jX ## U>o-
dynamic maN[3.548e+50,503.898,8] ## 2j2g[g
## 7jOC>o
func s8 (number rnFf[3.612])
	return
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011394))

	def test_2513011395(self):
		input = '''
bool ueA[1,5] ## [+U%
var Hes[3.132,88E71]
## Tbp(V/W{ ;x!VjV9A9#
number UNCY[2,389E12,15.463e-21] <- VMO
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011395))

	def test_2513011396(self):
		input = '''
func R0 (dynamic FA)
	begin
		## W)U;pr";>450/
		begin
		end
	end

## [~ak+Lcu
func HH (bool KP[679,405E-22,0E-40], bool RR, bool YN)
	return

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011396))

	def test_2513011397(self):
		input = '''
number K6w[273.999,12,9] ## MG)${+`rd%*IzAL:MsnW
func oqXa (var tx, string Be)	return

var Gd
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011397))

	def test_2513011398(self):
		input = '''
bool PZwa[23,35.007E+49] ## _cBd%faEASOh&}JR-
var Ici <- Ea_
number Pv <- XL
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011398))

	def test_2513011399(self):
		input = '''
## //`|5ra|`;
number M6f ## ud, D
func SJz (string cQ4Q[91.421], string aEQ[86e-00,54.695E+82], bool j4t)	return 793.360

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011399))
