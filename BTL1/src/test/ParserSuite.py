import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_2513011300(self):
		input = '''
var ke_p[3,0.751] ## 1E~Ah.}F
func T8C ()	begin
		for ea until [- Q8I5([GiO()]), "d9+'"", 4] by true
			begin
				for YJ1G until 5.386E83 by "[B"
					for Etw until false by yzNJ
						var Mlv[8]
			end
		JRb()
	end
## B
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011300))

	def test_2513011301(self):
		input = '''
## Z.z"Bl;=i;bPtJ*d^
func nUK (number qRJ6, var S3Z, dynamic scr[998])	begin
		begin
			## .G%$TB{fYCK3)r^Sn9
		end
		break
	end

dynamic Ac[505]
func mC8 (bool i30D, string Ax[547,58.594E-19], number be)	begin
		## ku(&dY]
		for I1 until 675 by JU
			return dc
	end

'''
		expect = '''Error on line 3 col 23: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011301))

	def test_2513011302(self):
		input = '''
## ~H<P
func oTWa (string Nf7[1.333e+66,983E21], dynamic SPl, dynamic vz[25.293E-63])
	begin
	end
func dy (string NFij)
	return

## %gEwv^
func LeM (bool tXJm)
	return true

'''
		expect = '''Error on line 3 col 41: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011302))

	def test_2513011303(self):
		input = '''
func RHCz (bool aGs, number b1Uj[579E76], string c1nt)
	begin
		continue
		return "&v'"W'""
	end
## L1uD.w3>U
## ma1xW4=k{fQ
## K3IAWoUT|Fc_Yt
func zyg (bool UKAB, number GAL, number LiCl[1.360,5e+94,94.287])
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011303))

	def test_2513011304(self):
		input = '''
## [zAy ;tA C_>
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011304))

	def test_2513011305(self):
		input = '''
## Z6i.fLk6)haW-NONU5h
string DN <- "'""
func Ap3 ()	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011305))

	def test_2513011306(self):
		input = '''
func sFF (dynamic S2k_, var Md[5.665E+72,47.856e02,70e83])	return "'""

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011306))

	def test_2513011307(self):
		input = '''
## A@Lqn@5;C}&
## Lc~h@}o_7Af3zw?hd{
string oD[3.979E-07,3E+18]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011307))

	def test_2513011308(self):
		input = '''
func Qz (dynamic sa)
	return "G"

bool VHt <- jV4 ## .|zKwHUG[,"K4
func XXj (dynamic Y38, var y51[1.392,354.791E-95,0e+81], var kb5)
	begin
	end

string y1
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011308))

	def test_2513011309(self):
		input = '''
string m45O ## #q:p.Ig.?0C712
bool pf ## C~]%
## QA#($8X)CZ0+bq:YrAiD
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011309))

	def test_2513011310(self):
		input = '''
func cDs (number RJi0)
	return
## .K-~tfuW7GA[TTI?
## u[xL<,39rKV!d;
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011310))

	def test_2513011311(self):
		input = '''
## a*U,j@PTvGt=nCv?J"{
dynamic NlMs[78.121e-70,72] <- x2 ## p
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011311))

	def test_2513011312(self):
		input = '''
func zlmn (number f1o[76e+49,783.709])	return

## S(byG
func tvyw ()
	return bJja

dynamic RDs <- 4.821 ## /K<S>%cdv!a
bool JnG <- true ## BW:
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011312))

	def test_2513011313(self):
		input = '''
var zj
## $#]JM?L#6n..SA$**S}-
string Hw2j[3e-74]
'''
		expect = '''Error on line 2 col 6: 

'''
		self.assertTrue(TestParser.test(input, expect, 2513011313))

	def test_2513011314(self):
		input = '''
## *y(9&+Q26>YD_D9iM,5
string Jt
func k8c8 ()
	return Cp

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011314))

	def test_2513011315(self):
		input = '''
## U|GXioR{_k>
func KTj (bool e1ji[9E+49], number hjF, string wR5)
	return
func CO7 (var PB, var I4o[66.358], dynamic xyUE)	begin
	end

func vtf (dynamic FKoO[64,30.572e-14,3e+91], var K6, dynamic exye[0.517E-23])
	return
'''
		expect = '''Error on line 5 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011315))

	def test_2513011316(self):
		input = '''
dynamic F_TP[3.931,82e+68]
## Iq
func xwOE (bool IG, string ml)
	return "'"j]'"'""

'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011316))

	def test_2513011317(self):
		input = '''
func xW (dynamic AL[21.172,91], var EER2, var IcN)	begin
		## sM8qho1Bi[5]7_`od{5
		## I?OE{q2)gkdlt~I:
	end

dynamic Ozf[24e22,950.187,7.125e57] <- false ## tK_Pt/t|%DTXH_wPA)-
string AJ <- qL8 ##  qS+ieK
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011317))

	def test_2513011318(self):
		input = '''
func CpQj (dynamic Ue[6.067E-48,82], var f5J[936.424E+63,231.244E14,40e+37])	return
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011318))

	def test_2513011319(self):
		input = '''
number n66[425.420,158E50,793] ## &
## 9/Zsq5Yur5
func Ok6H (bool yoR[87.493E83], bool lKs[3e+58], string E2[44.225E-00])
	return Y7Q

## ^7`0
func FX (string tFZ)	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011319))

	def test_2513011320(self):
		input = '''
bool E4D[867.611e-02,543,20.666e17] <- VHo
bool azU5[74,9]
func y7 ()
	return
## |5>Sy<8Cysrsh
## }-|R
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011320))

	def test_2513011321(self):
		input = '''
func mVui (bool bs, var U4QG[304.404e-96,61E63], number kvUc[993,53])
	return M4

var yy ## A?9]5yhZ7%y!
'''
		expect = '''Error on line 2 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011321))

	def test_2513011322(self):
		input = '''
number zF6
number SP ## *#]Zk#HV6@
## 8]n<
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011322))

	def test_2513011323(self):
		input = '''
func zxX (var mEM3[34E-28,82.396,2.660], bool d3Q[2.088E-70,2e+59,841.368])
	begin
		## Rox}9YFLAP;
		qb(yLS7, "g'"{M")
	end

## Z(uOeG5odg+][JttL9O#
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011323))

	def test_2513011324(self):
		input = '''
## E
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011324))

	def test_2513011325(self):
		input = '''
func m4oi (number rLt, string Xj)	return

## iM?hQY0`NI!
func SQ8 (string QEbn[52.444], number ro[0,125.146,1e-16])
	begin
		begin
			break
			## ,
		end
		## N,/7b:6@+ZC{HN
	end
number L99[359e-74,477E-49] ## m+X.N_{8>/O#
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011325))

	def test_2513011326(self):
		input = '''
## "4eJK3UiqR=0 }|}-<<
## ,M?h!WncQ
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011326))

	def test_2513011327(self):
		input = '''
func RTae (bool xm, number aWF[647.619E+37,30], var zpL_)	return
string m_Ss <- d7 ## Eg^K^]G7 Kn#tW^b+
func Am0X (string SBJH, dynamic Fn)	begin
	end

dynamic dkW <- 678
## `_zW>n
'''
		expect = '''Error on line 2 col 48: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011327))

	def test_2513011328(self):
		input = '''
func Ho ()
	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011328))

	def test_2513011329(self):
		input = '''
## OTvZ^_8+Gf&Xg
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011329))

	def test_2513011330(self):
		input = '''
number d7 <- true ## O{JmG)2aO-UD!;#Y
## fvDz;c6
func kd5 (string Qv5K, bool XI3S)
	return false

## ?g-7e)Qs
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011330))

	def test_2513011331(self):
		input = '''
number otQn <- Rju
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011331))

	def test_2513011332(self):
		input = '''
## L)(o
func gxc (var xd0, var VShT)	begin
		var jh[82]
		## <L7=:
	end

'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011332))

	def test_2513011333(self):
		input = '''
## |lY+Q?J68u-,AH
func lU2 (bool Mq[26.492], string sQ83, dynamic BtQf)	begin
		## wzY4wrG
	end
## ]Y_SsWU!<9src39
'''
		expect = '''Error on line 3 col 40: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011333))

	def test_2513011334(self):
		input = '''
## i-y
string ZD8Y[8.635E+91,30e+20] <- Jf12
## gqsy[@%bl1
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011334))

	def test_2513011335(self):
		input = '''
string Xca[86] <- true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011335))

	def test_2513011336(self):
		input = '''
func WfG (dynamic VBQ, dynamic Rz[82.550E70,336.106], string vq[424,38,852e76])
	return

func VaZU (number bQ[0.358,2.131], bool cJoZ[605], dynamic vz[51E+86,40])	return vM
func PBDv (dynamic uT[393.608e58], number BF, var fPy)	return

## Mp}-R?7TS`G2
## V#
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011336))

	def test_2513011337(self):
		input = '''
## [fph,
func nVro (string Odu)
	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011337))

	def test_2513011338(self):
		input = '''
string LS <- 408 ## sm7BBW;~wr
func eAq (var lRGE)	return

## (w
number cF <- "'"'"3'"" ## ^=7hJK_H8={k7]`
bool wFR <- "'""
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011338))

	def test_2513011339(self):
		input = '''
## *#".(S<5V}61O
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011339))

	def test_2513011340(self):
		input = '''
## lJ9@6;b}I2bf(j|_M9zn
number VCE <- "'"'"E" ## %>T%)uUJE
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011340))

	def test_2513011341(self):
		input = '''
## j8+O*n5*na7T=9@
bool iv1x
## Rp^+BtSPF]7uWQ#}+:i
func KQPm (string mTJ[922.040,274.504E76,1.966E-34], var OKz[3.035,1.362E10], bool HDo6[8E+71,34,9])	return
func pu (bool lXK, bool rcr2, number nUq)	begin
		## 6
		## aP,e;!hc]a)ZdG
	end
'''
		expect = '''Error on line 5 col 53: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011341))

	def test_2513011342(self):
		input = '''
var D_2A[71,7] <- "'"B'"R"
dynamic oT[984.122e+79] ## C%
number o3F[20] <- false ## M*wd;
## euAvcLS2cEZ~7
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011342))

	def test_2513011343(self):
		input = '''
func az3 (number Ah)	return 86.406e+58
## &48#jlj>-P#
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011343))

	def test_2513011344(self):
		input = '''
## [9i
## eJR3"v*n[>I7Gzn~f$a
func tw ()	return 1

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011344))

	def test_2513011345(self):
		input = '''
## LU8HghqM>b]8yEf]Gw<
func uV (var Qwv)
	begin
	end

string C5[37.494,1.441,6.305] <- true ## !P#`NEeg^JP
## l>Q0^fym
func abVw (var vKLa)	return 439.106

'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011345))

	def test_2513011346(self):
		input = '''
string KhY[288.340,4E+84,10.080e11] <- Y5
bool Ni[82.067,0.966] ## a@66V$[(Uxr=|
## 4dDNRgq
var Zy[8.736e-09,290.576e-01] <- "'"*'"Z" ## s=O"
'''
		expect = '''Error on line 5 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011346))

	def test_2513011347(self):
		input = '''
## p&xm{
func YI (dynamic mo)	return
var Ku5n ## 4YXXFCYqZi6T
func lO5 ()	return
## d-s^{Oq
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011347))

	def test_2513011348(self):
		input = '''
string X1 <- "x,#'"F" ## Rr
## 324g~oSSi?EAUDX`L
## sV^2#T(l
var MAv <- true
## Ih<
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011348))

	def test_2513011349(self):
		input = '''
## %n
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011349))

	def test_2513011350(self):
		input = '''
## S43
func O7A ()
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011350))

	def test_2513011351(self):
		input = '''
bool frKl <- true ## cd<sTn`APeurW
number Sr
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011351))

	def test_2513011352(self):
		input = '''
func NZk (dynamic fU)	begin
	end
func xUU (var SjO4[654e+15,50E35,1.625], string C9yR[69,71.497e91,36.351E70], dynamic j6[1.409E-48])
	return

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011352))

	def test_2513011353(self):
		input = '''
func ss (bool Rd6, var IUgx, number ZLv[51.866,378.613])
	begin
		## &KHv1&etkqMm|FKin
		## BLt){inh0]
	end
string JNqB
'''
		expect = '''Error on line 2 col 19: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011353))

	def test_2513011354(self):
		input = '''
func pm (dynamic w6qA[0e+21,772.981], number brw)	return

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011354))

	def test_2513011355(self):
		input = '''
## [C(-}
## P4Ch<h
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011355))

	def test_2513011356(self):
		input = '''
func nj (bool y2j, number Ppb[69.172e-39], bool eC)
	begin
		break
		break
		return
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011356))

	def test_2513011357(self):
		input = '''
string VMB <- "ya" ## <qGL,IOBU+_g#?fw{#
number YV[1e05,92e+38,4.584] <- " '"" ## :KxHSLP{8}iK~Hb/rd
func U5Ef (dynamic PqdJ, var NlM[0.719E+78,25E+01,9])	return false

bool KpNR ## =
'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011357))

	def test_2513011358(self):
		input = '''
bool Bgw[9,624e85] ## k+*823%<M@f[O~
func H5h (number F7, string zqw)	begin
		begin
			return false
		end
		begin
			number kea7 ## >2)`
			if (false) break
			elif (U8)
			continue
			elif (true) break
			elif (false) for Rk until 788.138E99 by true
				break
			elif (xgb) if (false) ywMR(602e85)
			elif (2.783E04)
			continue
			else geyx(47, XoQQ)
		end
	end

func nUPn (number nxn[1,34.705E82], dynamic Se19, bool yyGW)
	return true

## A
## ,$Fb
'''
		expect = '''Error on line 22 col 36: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011358))

	def test_2513011359(self):
		input = '''
## d:$zU&2F.Um,
dynamic Lw ## Tnqo-R8Z$a NWh0:c
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011359))

	def test_2513011360(self):
		input = '''
## ^Fi:1TemQ<)dS4^gtET
func y0gU (bool aZa[60.834e+42,62.127E69])	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011360))

	def test_2513011361(self):
		input = '''
bool bPEI <- false
func j_6 (number q2)	return j8P
func u6zq (dynamic nuF5[72.777e81,560,72], var OCBI, number lATj[3e49,7E+49,69])	return byd

## pq7)
'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011361))

	def test_2513011362(self):
		input = '''
func nZf ()
	return 96E+60
## |&%Zc3$
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011362))

	def test_2513011363(self):
		input = '''
func V1QC (dynamic Rn, var vhD[28E50,234.082e-26], string K2q)	return
func ZbBc (bool M3, var S2[2.066e67,865])
	return 9e+88

number yKB <- 609.859e40
func C_r (var eG[70.642], bool S6e)
	return false
var NN[694.513E90,2.956] <- "'"'"'"?" ## ^c:j:zl
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011363))

	def test_2513011364(self):
		input = '''
string hidx[3,508e-31,82] <- 90.436
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011364))

	def test_2513011365(self):
		input = '''
func pBPD (dynamic Jqf[18E47,531E+12], bool qN[2E+42,788E-92])	return TxZ
bool tO8 <- 78.043 ## UNZn+7!sY=
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011365))

	def test_2513011366(self):
		input = '''
func FGO (number ps, dynamic asY)	return

func Nd (var Wos)
	return
'''
		expect = '''Error on line 2 col 21: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011366))

	def test_2513011367(self):
		input = '''
dynamic l6 <- wL
func kXFY (number yv)	return 2e49
func dTa1 (string YDG3, number hcW[858,2E00], dynamic zpLG[498.482,527])
	return false
'''
		expect = '''Error on line 4 col 46: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011367))

	def test_2513011368(self):
		input = '''
## 2x=v5|^&VX8
func uI (bool zPe6[20E63], number f68[62,5.682e-89], string NZ[68E+81])
	begin
	end
func utu ()
	begin
		## eA|QAn1#`ep?yaJ
		## FsWUrQl
		fsE1(l26D)[true] <- 92.357e98
	end

func pL7 (string mJOT, bool d4[3.158], bool GAP8[626.180,3E-32])	return true
dynamic nA[2.331e-25,8E+13,1.509E+00]
'''
		expect = '''Error on line 10 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011368))

	def test_2513011369(self):
		input = '''
func mNi (number Ahn, bool ww, number cRpd)
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011369))

	def test_2513011370(self):
		input = '''
func uXWf (number yb, dynamic Z65, dynamic XE)	return

number UcVT <- "Y'"bp"
func RUD ()	return 5e-22
func Y6AE ()
	return "'""

func i3V ()	return
'''
		expect = '''Error on line 2 col 22: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011370))

	def test_2513011371(self):
		input = '''
func BQEq (bool B9, number RO, bool Utd[8.397,8E42,259.489E-60])
	return OX
string KpVB[36.804,0.117E57] <- "$" ## qrUlMN~#4p6 %Z- >yQ
func J6V (number DS)	return QI

func Z2Ew ()
	begin
		return "'""
		break
		## U
	end

## DXi(zlU=EO^ZfH1
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011371))

	def test_2513011372(self):
		input = '''
number Wg8Z[303.067] <- false
## 4n!Z
func sp (bool s7J[9e68,15,59.012E+63])
	return 1.606

## A8D~
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011372))

	def test_2513011373(self):
		input = '''
dynamic iFy[0] ## x_7ns"V
func UVFH (dynamic Kba[0.843,31.793E38], number Cwul)
	begin
	end
func WlC4 (number mA5)	return true

'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011373))

	def test_2513011374(self):
		input = '''
## wt
## ;r1KL+1e6#7
## w#2
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011374))

	def test_2513011375(self):
		input = '''
## /cY(
func kmN (bool Xk[376,66e-63])	begin
		if (zfS)
		dm7X(wR, false, 39.397)
	end

## ~NT>
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011375))

	def test_2513011376(self):
		input = '''
dynamic BkPP[619.595] ## #]HgsG{,0
dynamic U9 <- 9e-25
number BJGZ[7] <- true ## -;B`^|!h>qIPdg_v
var uBFc ## N,vp7@48BB "t@XKg4
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011376))

	def test_2513011377(self):
		input = '''
number CVEk <- KPDu ## `PY`bEnb
## >t=F2v/.$)1B7Mkx
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011377))

	def test_2513011378(self):
		input = '''
func Bn2Z ()	return

dynamic Je6T <- "'"'"'"'""
## i7baFxbN:@:XH#@a7/8,
## ,gH]5>
## ,
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011378))

	def test_2513011379(self):
		input = '''
## Ae
## S)g
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011379))

	def test_2513011380(self):
		input = '''
## p<A*&$5
dynamic Ama[476] <- "P-RO," ## C]=gZWy~-
func szK_ ()
	begin
	end

## B1
func cbq (number HP[922e+45,4.325E18], number uWR[4], bool WuU[60,2,946.730E+95])	return true
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011380))

	def test_2513011381(self):
		input = '''
func jIY (var WBaC)
	begin
		## (Y,7::p9JLw#i|!88b
		if (8e22) return
		elif (79) continue
	end
func MJSx (var QoX9[31E-63], bool Ex)	return

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011381))

	def test_2513011382(self):
		input = '''
## {prKhL/GHg#QIj
string ySp8[8.919,0.425] <- 23e-89 ## YWbJPtOW4:iKBM(:O
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011382))

	def test_2513011383(self):
		input = '''
func olJa (string es, var GJO, dynamic Jgnl[0e-33,1.485,320])	return
'''
		expect = '''Error on line 2 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011383))

	def test_2513011384(self):
		input = '''
func Yp9 (dynamic Omam, dynamic DK)
	return
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011384))

	def test_2513011385(self):
		input = '''
number Hjd <- nkU ## Q1op!_.IDxwi21W0Vbd
## @A+
bool PfXO[75.712E-99,0.849E52,8.684] <- Zjx1 ## BV/:dKZMlc28L&G
## 7*}*h@fL
## X$6
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011385))

	def test_2513011386(self):
		input = '''
## V8FZ7"`m
func i5nI (dynamic F2nH, number HEl[23E76,10e-66], dynamic BLB)	return
## )]zCJ&):`Xm:
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011386))

	def test_2513011387(self):
		input = '''
func d2 ()
	return uBkH
## >X
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011387))

	def test_2513011388(self):
		input = '''
## R"[YiM-nYD
bool yt[725,7E31,41]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011388))

	def test_2513011389(self):
		input = '''
## *<7(#nz&-V .Gxe
number O17G <- 68
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011389))

	def test_2513011390(self):
		input = '''
## q
## iwBI6/n-x4M<{)?
bool jMS[0.277,6.308e70]
string zjy4 ## |iCEsc}mW0Q:`WYz
func NR (bool QKwA, dynamic Q70[5.065E-19,8E-96])	begin
		if ("h'"|'"")
		for yWeZ until false by 4
			break
		elif ("'"")
		rkn(RhYH, 303E01, CP)
		elif (0E-34)
		continue
		elif (true)
		U9(iQ4, " ;")
		elif (true) string uvj9 <- ax
		elif (27.901)
		return kE3
		else B89(omS, false, 5.098)
		## d)
		continue
	end

'''
		expect = '''Error on line 6 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011390))

	def test_2513011391(self):
		input = '''
func oEi4 ()	return Dn

## KVV
func IOb (number z_Q[678,450E+65,40.360E-06])	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011391))

	def test_2513011392(self):
		input = '''
##  w}Z`l
func UKvS (dynamic dne[7], string sUAO)
	begin
		if (true) begin
		end
		elif (998.391) if ("O'"")
		break
		elif (false) if ("~'"$'"") continue
		elif (xX)
		for Eq until 223e+59 by 6e-03
			break
		elif (true)
		break
		elif (7.150E+82)
		miJ()[96e+98, ht, dqii] <- ZHG
		elif (778.288)
		qazt <- 1
		elif (false) kS(true)[true, "2w'"l", false] <- false
		## imW$*00!),l[mw@Pnkw
	end

func Ea9 (bool Sl2, var KD[3e+11], number A1Lp)
	return
bool uda5
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011392))

	def test_2513011393(self):
		input = '''
func PviV (string sEWF[17.377E-54,1,286.534E50], number QuMC)
	begin
		## oZk9D$
	end
dynamic opIW ## P
dynamic FBk <- Z8Y
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011393))

	def test_2513011394(self):
		input = '''
func xv2h (string brM)	return false

## w]aH
var QLpu ## 8MU3]I(3<(#
'''
		expect = '''Error on line 5 col 23: 

'''
		self.assertTrue(TestParser.test(input, expect, 2513011394))

	def test_2513011395(self):
		input = '''
## a5lJE4gmz1
## $
func qydI (bool Wv, dynamic c9)
	begin
		continue
		## ;4i33
		## KX`pUL`}K$=cP
	end
## 9BF?x=Yfy{{p{gs~
'''
		expect = '''Error on line 4 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011395))

	def test_2513011396(self):
		input = '''
func cgl (bool kqVI)
	return
var iYU6[322.579,83E84,38] <- Qd
func i84 (number Ph[12E55], number RxOw)
	return
dynamic UzY[952,320.539e92,654]
## a317g9dL
'''
		expect = '''Error on line 4 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011396))

	def test_2513011397(self):
		input = '''
## ?;-:x}aE8"Ubq
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011397))

	def test_2513011398(self):
		input = '''
string nEya[4E-73] <- TwM ## 95X?y| fP*h3"M ]U>8
## ,lc I6Ayl?[ijwo|crBw
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011398))

	def test_2513011399(self):
		input = '''
func oXV (bool HMLV, string OGq)	begin
		OA("D", false)
		gHQO()
		## />,,~Z
	end
## K*SbQ;g83}_F4,NJ{
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011399))


	def test_2513011400(self):
		input = '''
func areDivisors(number num1, number num2)
    return ((num1 % num2 == 0) or (num2 % num1 == 0))

func main()
begin
    var num1 <- readNumber()
    var num2 <- readNumber()
    
	if (areDivisors(num1, num2)) writeString("Yes")
    else writeString("No")
end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011400))

	def test_2513011401(self):
		input = '''
func isPrime(number x)

func main()
begin
    number x <- readNumber()
    if (isPrime(x)) writeString("Yes")
    else writeString("No")
end

func isPrime(number x)
begin
    if (x <= 1) return false
    var i <- 2
    for i until i > x / 2 by 1
    begin    
		if (x % i == 0) return false
    end
    return true
end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011401))
