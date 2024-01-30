import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_600(self):
		input = '''
func qgJb (dynamic yL[49e+26,272], var jo7Q, var fXl[600.816E+92,783E+02,74.317E01])	return

func yL (var SIlw)
	begin
		continue
		## CezLZAX&e)
	end

func FPse (var tJe0[574,69])
	return
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 600))

	def test_601(self):
		input = '''
var XKTI[302] <- [["'"'"'"", I1xq[519.875, 84.323, 1], mmT]] ## -d#.?DSB(pz|
## kjL%r>_/
func Bvk (number Sh[3.225], bool tjB)	begin
		continue
	end

func Cs (number lneP[575], var mP[8e-70], number D8Ar[4,9.239e79,9.763E+26])	return

dynamic vf9P[3.152,747.644] <- 541.750
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 601))

	def test_602(self):
		input = '''
## p`O9w9=
dynamic TJ
## #v+5
func uTJ (number m4Y2[7,44.751E+94,8])	begin
		## [-8[K[e::<q)}Z5Z1
		begin
			## vhja
		end
		## BY@[`nQ
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 602))

	def test_603(self):
		input = '''
dynamic jh[55.987e91] <- true
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 603))

	def test_604(self):
		input = '''
## oa}DSlHsomj
var ne <- on
func g5 ()
	begin
		return
		break
		S_X("'"")
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 604))

	def test_605(self):
		input = '''
var pV
func za (var Es9[1e51])
	return false
'''
		expect = '''Error on line 2 col 6: 

'''
		self.assertTrue(TestParser.test(input, expect, 605))

	def test_606(self):
		input = '''
number zLeP[4,7.281E-64] ## x[x^tkeH!Hs2:
bool OQ8 <- WVa ## Qw@$
var pHB
bool fH <- J4a
string Cgs[187e94]
'''
		expect = '''Error on line 4 col 7: 

'''
		self.assertTrue(TestParser.test(input, expect, 606))

	def test_607(self):
		input = '''
var naO9 <- false
## Tc
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 607))

	def test_608(self):
		input = '''
## Ln2+^.oK,V~MI-PV
var NF
'''
		expect = '''Error on line 3 col 6: 

'''
		self.assertTrue(TestParser.test(input, expect, 608))

	def test_609(self):
		input = '''
var Dg
string qI[99,102.549e28,57] <- false ## 6fq3HD
'''
		expect = '''Error on line 2 col 6: 

'''
		self.assertTrue(TestParser.test(input, expect, 609))

	def test_610(self):
		input = '''
func NA ()
	begin
		dynamic xkQ2 <- true
		## @U!1(b"t~%dppOxnHyR=
		## 5Kmx!fX^@;d
	end

bool C2E ## $
func Jb (string GM, var dczE[39.928])
	begin
		## `J%A
	end
## yL~jMU!XhCykZ$
'''
		expect = '''Error on line 10 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 610))

	def test_611(self):
		input = '''
## U%
func UsX ()
	return true

func eJ (number eH[9])
	begin
		SLH("Nn'"", jz7, "'"'"1")
		## zu|B7PM&sZ
		## SwT6bkaSI9k^85VVU0
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 611))

	def test_612(self):
		input = '''
func VaOG ()
	return false

func LV9 (dynamic x47_[940.226,85E-39], dynamic DTw[2e-95], string ay)	return
## UmT[a:]ki+
'''
		expect = '''Error on line 5 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 612))

	def test_613(self):
		input = '''
## %<x*CK1<&4/T8
string pdi <- sM ## )5KT;pjR]n
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 613))

	def test_614(self):
		input = '''
func Y7p ()
	return
func htOI ()
	begin
		## -%;w<7G;JK]6La)i+A
		## SA[
	end
bool gs <- 124.182E-27 ## (=z
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 614))

	def test_615(self):
		input = '''
## ~i_kT"q
number YS_ <- 569.919
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 615))

	def test_616(self):
		input = '''
var Jf <- "q'"0"
dynamic z3YR[343] <- 20.653
## 8=3>7]L.al{{Mj
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 616))

	def test_617(self):
		input = '''
func Lz (var uS)
	return false

## ndM,2cQ_%|LN
number DF[65.596,72e+41,618.566] ## MuoPbh_0*k
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 617))

	def test_618(self):
		input = '''
func j7 ()	begin
	end

func mm (dynamic jgh[299E45,349.371E48], number yv)
	return
## )7{UZ(|
number QcSG
'''
		expect = '''Error on line 5 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 618))

	def test_619(self):
		input = '''
number xBUw[25.775,7.287,6]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 619))

	def test_620(self):
		input = '''
## r/sL>FTsY&V1>_ab^Z
func oU5 (var bAp[35.564,44.370], var Aeh9)
	return 5.190e-46

'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 620))

	def test_621(self):
		input = '''
bool h7K[173.899,4E-50,93.719e79] <- "+" ## ]V+ b
func UPf ()
	begin
	end

var tlL[577.734] ## $otB5#[hv?B
## 7 M[=#m6;e1(]g^"T
var ZT5w[77e91,639,95.782e+47] <- true ## j(eO
'''
		expect = '''Error on line 7 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 621))

	def test_622(self):
		input = '''
## yxb9Cr D{CA^1l.QFQ
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 622))

	def test_623(self):
		input = '''
func I4 (number sxyH)
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 623))

	def test_624(self):
		input = '''
string BVV[9E+14,506e90] ## V(BzS.r`
func Lgy (dynamic HQ, bool Cb)	return lnf
func ELit (var Afva[877.740E-47,2,679E97])
	begin
		return true
		e3("'"'"'"d", false, "'"vP")[true] <- ea
	end

func pbY (number gX_, number kTw[0E-12])
	return
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 624))

	def test_625(self):
		input = '''
func FIPr ()
	return oW

## myhXV
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 625))

	def test_626(self):
		input = '''
func pK4k (bool wOEe)
	return """

func wG (bool vKe6[870.118e+45,705], dynamic U2vx[5E13,2], var MBz_)	return
## #U=n}-R]{x_8x<g|
func sk_h (dynamic Vj, number i98v[7E-66,22], var Z2nK)
	return
'''
		expect = '''
'''
		self.assertTrue(TestParser.test(input, expect, 626))

	def test_627(self):
		input = '''
## {J3mb
string lo <- "'"X'" "
number gGF ## O-yV
## o6L(10)w|7{)2
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 627))

	def test_628(self):
		input = '''
bool gVn[710] <- k2
## !h})
func R5 (string ql, var Hd[869.278,54e-72,81e-70])	return 30.543E55

## C#=u
'''
		expect = '''Error on line 4 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 628))

	def test_629(self):
		input = '''
dynamic gwxy[865,759.217,2e-14] <- true ## 5
func CO ()	return

'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 629))

	def test_630(self):
		input = '''
## .[^o`m_
## JAs
func sjz (var y8[7], string QLQ[720.400e+54], var ADgR[984E-44])
	return

## >(=[R-j4J1 ;:XU2-/
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 630))

	def test_631(self):
		input = '''
## :^yC=~p5"H-`Z.T{^@
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 631))

	def test_632(self):
		input = '''
func Tb (bool rMas)
	return
func tzSg (bool N5p)	begin
		break
		HVJ(Swc)
		Ev(true, zFO, "'"'"'"'"'"")
	end

## l(
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 632))

	def test_633(self):
		input = '''
func Rx (var a_K[47])	return true

func QG (var dbB[4.092], var D3q)
	return
func Pksm (dynamic lK8[8e73], dynamic jjJ7[9.322E-35,71.257E-03,9.878e-93], number Ms_O)	return 79.713e34
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 633))

	def test_634(self):
		input = '''
func C5K (number cm4[776,28e+88])
	return
## "s
func Nc (number zfMO[13,3], string m7O0[27.316E29], string cK[672.323E-97,5e+09])	return "'"1'""
func nLc (bool qF, string FP, string Z4[89,859E-06])	return
dynamic xQ <- e8 ## ]8Z+wA]q+"dRyDY<i&b&
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 634))

	def test_635(self):
		input = '''
func zrKm (dynamic ZQ[101.202e46,3.719e43], bool womX[23.688,989.278])
	return
## r
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 635))

	def test_636(self):
		input = '''
func zj (number EKb2, string qtnb)	return
##  kJ
## ^ya!/GBUzN&8b`(AL&i
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 636))

	def test_637(self):
		input = '''
func aK1 (bool Va4J, string m5gA[968E75], string x9R[149.680E-11,215.485,7.253])
	begin
		return
		## 6e P|: 2G J=2tjD
		## b4|nEiFIL`P1HZ`7
	end

string EVS <- "'"'"" ## jjN8h/,qI=Wd8KLQ"n-
## ]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 637))

	def test_638(self):
		input = '''
var F_r ## z,=
## I&6"
'''
		expect = '''Error on line 2 col 14: 

'''
		self.assertTrue(TestParser.test(input, expect, 638))

	def test_639(self):
		input = '''
func tTN (var UYtt[3.254])	return

## }mWZ[Az#.EIi
number lF95 <- 339.238E+01 ## 9#6@`
func Fgqk (dynamic QuS[113.100e-97,998.531,37e00], dynamic r6j[27E+95,6])
	return

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 639))

	def test_640(self):
		input = '''
bool sM[609,4.751] <- "'"'"%" ## Jc
## 8Uja_rsz
## L Hi[(2u
string Zs[686.787] <- true ## MTkUhy-!I|3$A}
func xhud (string aQf[3e76], string pRyd)	begin
		cHg()
		return
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 640))

	def test_641(self):
		input = '''
func su7 (var sL[0.160], var s8[222,772e+17,76.284], dynamic TPP[810])
	return false

func sC1n (bool miSo[2.932,8e+19], dynamic fHa)
	return "'"R'"3"

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 641))

	def test_642(self):
		input = '''
## iI[I;
## xrlt7}INNL*-7WA6Vi
string yDKD <- "'"'"Umq"
## 6uJA
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 642))

	def test_643(self):
		input = '''
func c_t (dynamic Lfw, var Lm[9.190E+86], bool LJXE[985])
	begin
		XH(0e-58)
	end
var MaO[3E87,7,6.582] <- QZv ## aWX[bf#a#4s}
## &"}g]8gS1[
## aIMu>3EwjNCrH31;W!
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 643))

	def test_644(self):
		input = '''
func lMo (dynamic do)
	return "?Z'"jS"

var UYf0 <- true
dynamic n5oZ ## o
number UA[2E05] <- Cs ## u>4ld,;PnR?X@`_v;
func E_ (number q5H[9.269e85,0.237E-34,13])	return true

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 644))

	def test_645(self):
		input = '''
## Jr**}z9>vC,II42Na|T
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 645))

	def test_646(self):
		input = '''
## u8J#m&fP
func ZaW ()
	return

number dvTX ## EI&Vg&qEG8Qb`gTF_!%
string cz[0.735,4.320E93] <- 555
## (U?
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 646))

	def test_647(self):
		input = '''
func OwMc ()
	return
func Onc ()
	begin
	end

## jgNv
## 8> =9@WzDHj
string BV8
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 647))

	def test_648(self):
		input = '''
## )koP_&
dynamic lFf[4.722e26] ## 3;D$61vY?z
func hSqd (number zIYf, bool sJf[7.330e-68,443.715e71,23.136e+39], string mB)
	begin
		for g2 until "'"M'"" by YmV
			h34Y <- OZKj
	end
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 648))

	def test_649(self):
		input = '''
var KZl ## +*N
func CK3 (bool RMe, string dM, bool WDe[679e76,13e20])
	return
dynamic PU
string oBTO <- "'",T"
'''
		expect = '''Error on line 2 col 14: 

'''
		self.assertTrue(TestParser.test(input, expect, 649))

	def test_650(self):
		input = '''
## kDsr8GBw.SPd=F
bool ZP <- 10.771e+46
## 0#)ODA-|ZD8
func kfjw (string U2Bo, dynamic Ahmu[5.556e+35,950.789,5e+95])
	begin
		return
		break
	end
## CFnYA!{tqW16cE),4
'''
		expect = '''Error on line 5 col 24: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 650))

	def test_651(self):
		input = '''
var b6f[4.192E+71]
func gk (number djO3)	begin
		pG <- 78.879E+54
		continue
		## -f2Mj=
	end
## Uvt:~n|{e")
func AC (number yOlf, var GMt[292.466e00,3.288], dynamic i2[9E-29,70])	begin
		for mwx_ until 769 by 1.305e-73
			string qA[45,94,6.217E-13] <- "'"" ## [1f|BR:[HL<&i_l;/
	end
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 651))

	def test_652(self):
		input = '''
## ><2|yq=
func yTn ()	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 652))

	def test_653(self):
		input = '''
var RnR <- 507e84 ## ,pScb_
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 653))

	def test_654(self):
		input = '''
var yfN <- i1YG
func Iap4 (number KYpa[921E-00,177,28.511E75])
	begin
		## [k5
		## }2BDTcv9r9h-DX
	end
func az4 (dynamic tfL[410E81,774e70], bool WKt[1,52.667e41,4E+57])
	begin
		for A7CT until 62.795 by 5
			string pStP ## 2[k^uDEIc~{f3"w|
		## xi
	end

## p!4AD
'''
		expect = '''Error on line 8 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 654))

	def test_655(self):
		input = '''
bool zSzr[118.498,45] <- true
func TAZ (string xe[13.484E+76,549.545e-42], number nhA, var hk5)	return false

string wbZ
func Jn ()	return
func tTS (dynamic W0[0.350E50,9.615e83], var gI)
	return
'''
		expect = '''Error on line 3 col 57: var'''
		self.assertTrue(TestParser.test(input, expect, 655))

	def test_656(self):
		input = '''
string IIb4 ## }].Jj]b@f
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 656))

	def test_657(self):
		input = '''
func WqdF (number zz, dynamic tFRr[4.706])	begin
	end
func bo (bool Vo[26.841,55.862,0.793], bool W52[98], number Im)	return
var TIq ## wOUC=PaC1"
'''
		expect = '''Error on line 2 col 22: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 657))

	def test_658(self):
		input = '''
func siz (var e8[616.585,0], number fjkU[20e80,65.498,2.606], dynamic VYH[2])
	return

## C%Qw<qqutGMkDF
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 658))

	def test_659(self):
		input = '''
## >:<En+6wRF_{.J
## _~5ooPmedb0`A0bU
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 659))

	def test_660(self):
		input = '''
number Z4g <- 913 ## j"uy<
func i2gA ()	return

func vi (string nyU, number Xn[34.652E+29,71e+98,82.832], number OD[92.682e-20])	return

## (R@:ytRRH,
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 660))

	def test_661(self):
		input = '''
string Ejm <- uGag ## 2{LD-4S
## i&Ay$-bo^r^v
func jxp (var mD)
	begin
		begin
		end
		## xf<KXXx%7
		## 18m{-
	end

'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 661))

	def test_662(self):
		input = '''
func AHy (var WJn, string yTYs)
	return D4f

func vl (var f1R, string c4, bool AG0[62.754E-21])	return

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 662))

	def test_663(self):
		input = '''
var lGTE <- "'"" ## h-7
func J76 (number Nc, bool bp[22.791])
	return false

number CVR <- "'"'"{'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 663))

	def test_664(self):
		input = '''
## pk(*_i7J?8I#giICY.:g
## eEx@@}&B>
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 664))

	def test_665(self):
		input = '''
func xWGi ()	begin
	end

func XaSL (bool CB9[1.711], bool u1lQ, var jQ[815E-93])	begin
		## 0;
	end

## ^
number gppt[94]
func cPb (dynamic EeHm[12.078E+31])	return sNeA
'''
		expect = '''Error on line 5 col 39: var'''
		self.assertTrue(TestParser.test(input, expect, 665))

	def test_666(self):
		input = '''
func V5ow (dynamic z65h[26.159e+45,6e72], number n3o[30e+81,7], bool fGGx)	return "'"-g'"&"
## =dkZ
## (1fsiI
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 666))

	def test_667(self):
		input = '''
number rw <- true
## P@7Ds9V<O!Rt*/Imm
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 667))

	def test_668(self):
		input = '''
string Ft[8.821e03] <- Q4 ## -
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 668))

	def test_669(self):
		input = '''
## "O#o@?0B7,dG
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 669))

	def test_670(self):
		input = '''
string W5[51E36,0.765E42,997] <- AM
func xG ()	return "v^'";'""

func jj (dynamic Kppq, var n3, number fJ[60.258E+47,8])	return "'"'""

## vs*[MS^~^~r_`4)A
'''
		expect = '''Error on line 5 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 670))

	def test_671(self):
		input = '''
## 7_:d(beC< fFeB!{PNDJ
bool X7[80.717E+76] <- "'"G'">$"
number Pj
## ",oe
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 671))

	def test_672(self):
		input = '''
func D1zO ()	return tq
func QRNH (number RA2[5E-45,303e56], string cpYT, string D7T)
	begin
		## -*.w6QQg
	end
## @0QeInb
bool YM ## .E8{#RB6"C}_-WSx!ze
bool AwgT <- "'"h'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 672))

	def test_673(self):
		input = '''
dynamic wr1C[16] <- 654e+92
func U1 (number lE5[358.615,158.142e56], number N8ol[29.042E-22])	return true

func JBs ()
	begin
		Bwor(Hvf, rA, "Zf'"")
		## 9<E$DJt}sMne?]hb6<
	end

func qet (var sfBM)	begin
		begin
			var Rzz <- 6.811
			if true for bkRe until true by "'"g'""
				break
			elif "'"P" number xUMc <- 4 ## o*,]w=LI/01BloQPupgr
			elif "'"z'"g" for YW until Si83 by FUo
				if "k'"'"'"x" begin
					## i E/0s9=1<Z
					## }zmTTp`"3
				end
				else return
			elif "|'"" for QD until "y4D'"D" by "'"'"C"
				if 1 break
				elif false if 4.818 begin
					## :B&`%`]
				end
				elif "'"X" oHT()
				elif ":u'"'"" break
			elif true var rE5n <- "'"3_'"" ## Y.unU=03i,8PO
			elif gZ number ZO[328.074]
			else begin
			end
			if 65 for im until "'"'"v'"" by 7.479e+77
				for Zc until true by bjsM
					continue
			elif 4E-81 for yA2o until "%BY'"" by w6
				return false
			elif "G`a'"" if true if E6 gV <- 119.458e-65
			elif 15E-28 return false
			elif true KVR5(LcoM, "mQ", "#'"'"m")
			elif fEb for TQHN until "R'"'"d" by "'""
				begin
					return
					## "r8M6
					## Y?Q**Fcdhpm
				end
			elif 367.117e+85 FaSw()
			elif false for qso until 9E38 by Phw
				if ry for OjK until 27.647 by false
					dynamic sh[4e47,1e01]
				else begin
					for mB until Wn by "aw"
						if "'"'"@'"E" continue
						elif true eU(784.835E+16)[5.188e-18] <- "'"'"c'"'""
						elif false return D2p
						elif false L4L["'"'"'")", false, "'""] <- 1
						elif 1.633e19 return
						else var vWVV <- QY
					var EO <- Avc1
				end
			elif 6 continue
			elif "x" begin
				## 1-zw}dJjSB
				if 0 begin
					## 6w}.!3Z
					break
				end
				elif GS break
				elif zAmV continue
				else begin
					begin
						## L!.$z_
					end
				end
			end
			elif "'"Up" bVbJ()
			else return
			else begin
			end
		end
	end

string Yr5A[57,277E32] <- "uR'"'"'"" ## -@}+4C#H"Rej|
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 673))

	def test_674(self):
		input = '''
func Yr ()
	return "'""

func E_O (string Y3eV, bool vLm)	return true

dynamic koUO ## 9o;`"veL9rlv&ytd7%`
func cwv (dynamic qsr[46.977,58.010e-12])
	return false

'''
		expect = '''Error on line 8 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 674))

	def test_675(self):
		input = '''
func FWQU (string tRjE)
	return
## J!Q
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 675))

	def test_676(self):
		input = '''
## _;t[]:"MHyRFfx}@^
string tC[870] <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 676))

	def test_677(self):
		input = '''
var qJ <- false
func Atq (number VXi, var WrZJ)
	return
func iH (bool GuLW, number xTdn)
	return 9E-35

## .fxt
## fc+5=t&?etrMz*.*
'''
		expect = '''Error on line 3 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 677))

	def test_678(self):
		input = '''
func kkNA (string WS[6.813,6E19], number Qsm[411,318.445,101], number ReX[509e+71])	begin
		## <2A>TZUWte>uf
		## TiY&gf8)9=J8e1f/e
		wi <- Nbu
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 678))

	def test_679(self):
		input = '''
## =p2
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 679))

	def test_680(self):
		input = '''
func GF2r ()	begin
		## p0wB+MpbYJ#/H_
	end

## _T 6&svJtUWrZA+
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 680))

	def test_681(self):
		input = '''
## QVt7a%lk>l
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 681))

	def test_682(self):
		input = '''
func leYm (dynamic M5, number WL3, bool oRxt)
	begin
		if 882.376e-09 begin
			if 50.941 var wef <- 920.664E16 ## EB0^+h>*&_>."KO7;1w
			elif 690 begin
				## #L^h
			end
			else dynamic AYm[69.505e-31] ## [L/3(O.vR3drm!/vI,6
			AtMc <- 2
			begin
				if NR begin
					## oLN.6kP*v x=:qTRRnZ 
					## RR
				end
				elif true continue
				elif "R'"" wV0B(false)["r'"-'"", false] <- si8A
				elif false QG <- "F""
				elif 835.248 return yR9G
			end
		end
		elif "'"'"'"" continue
		elif 250e-41 hNX <- ZC
		elif wZqK for v5 until 31.585 by "'"~"
			for iyI until false by Yx2
				m5(true, "`!'"@'"")["BE'"=D", hVz] <- hk9
		elif "9'"#'"'"" if Ng_a continue
		elif "?" for cp until 8.586 by false
			for kH until u1 by OX9f
				break
		else v_pP("'"@", 262E-86, vUJ)
		elif 13.511 nTk_(29e80, 33.560e-72, false)
		## _L:L_
	end

func AHBR ()
	return
func zzc (var Ws0P, var Ci[75.577e+36,1.668,974])	return EF

'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 682))

	def test_683(self):
		input = '''
## Tw&DIcEe"z:vVC=)vXz3
var eAf[760,17.698] <- Jau
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 683))

	def test_684(self):
		input = '''
var aPpQ
string Bh5 ## nPk_ZB_V`vvm
'''
		expect = '''Error on line 2 col 8: 

'''
		self.assertTrue(TestParser.test(input, expect, 684))

	def test_685(self):
		input = '''
## %Ph,Z`"G&>i>9h}c
func Uq (var RI[216,2.762], string tCfQ)	return
func ng ()
	return

'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 685))

	def test_686(self):
		input = '''
func Aq ()
	begin
		## x$0
		## JD~_Bw~EBBWBI
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 686))

	def test_687(self):
		input = '''
## 6BJj:/p0OT/
var tTv[0.805E97] <- true ## xYEi_V+EYmJJ
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 687))

	def test_688(self):
		input = '''
string AYyA[94,8] <- 730
dynamic rg <- "a'"" ## ,nSH^cxo_D(.J
## 06<
func Kc (bool N4vt[3], dynamic J2oV[753,7e34,900.794E-39], var lgm)
	begin
		ua(51, false)
	end
'''
		expect = '''Error on line 5 col 23: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 688))

	def test_689(self):
		input = '''
func atAm ()
	begin
		continue
		if YAV var kJZn[60e69]
		elif "'"'"Q" return
		elif rLq y1K(U5)
		elif "'"'"B'"'"" if 4.980 mf <- "'""
		elif 21.608 break
		elif AbI_ continue
		elif aKeg continue
		elif rAk Fgsz("'"'"V")
		elif 67.863 continue
		string L1 <- nTI
	end

## `
string SpT ## ?
func m6 (var rdH7[155.328,76E+60])
	return "'""

## Gm<4m&8qvIj
'''
		expect = '''Error on line 5 col 5: YAV'''
		self.assertTrue(TestParser.test(input, expect, 689))

	def test_690(self):
		input = '''
func JgKE (number FX[2E-71,6.028])
	begin
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 690))

	def test_691(self):
		input = '''
func b6 (string V9X[271.520])	return 3e-49
dynamic tZ <- n0
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 691))

	def test_692(self):
		input = '''
func xuVY (var AC, dynamic Qdx[4e-95])
	begin
		## Wu
		begin
			return
		end
		## 03cSJ"ObY3vM|H
	end
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 692))

	def test_693(self):
		input = '''
bool J149[83.725e+38] ## -7y&;#OOw%./G~!^
func C7GN (dynamic uDtR, number vv, string R1[30.112e-38,272.018e-75])
	return
var Xi ## evm.0"W}LBt6
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 693))

	def test_694(self):
		input = '''
number voor <- 2
## m/~#U~pYcpARVP
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 694))

	def test_695(self):
		input = '''
func na (dynamic kYZ, bool ZSX[887.163e+39,0.141,33.924E-30], var Uo)
	return

bool Tz <- Wro ## k9Ksjo&9z4}^vx
bool PZbJ
dynamic SR ## ITJ_}LP@gj@4IU
func ip3 (bool u8L4[573], var PoX[276.164])
	begin
		## l0 @8
		LO("Hk+'"", true, "'"")
	end
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 695))

	def test_696(self):
		input = '''
number i3J ## i"~P5%v7*dqL0R_c
## }qU.
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 696))

	def test_697(self):
		input = '''
number eN[4E97,87,30.758E-64] ## 3QT
func onq (string pw[335E-95,90E-12,85E-02])
	begin
		break
		break
	end

func re (bool zJb0)
	return
dynamic CP2 <- 1e-60
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 697))

	def test_698(self):
		input = '''
## 4eyiVz[qqEKJJ~YB`1!q
## E7gF0:|06C
func viZy (string Jx)	return vrcl
func HXl ()
	begin
		YLn("v+q'"", 3.988)
		## F-_m
		return 30.520
	end

## Ix!e
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 698))

	def test_699(self):
		input = '''
bool el[70E-72] <- OcU ## Ro4dN(+MEEM?E8u)
func PFl9 (number Bw[66.605e-31,75.672e+60])	return 5.511

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 699))

	def test_700(self):
		input = '''
## ?dre0t
func K_W (string qun, string UGm)	begin
	end

## $34{m3R6c_7$/
## |NYv-W9OH17N
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 700))

	def test_701(self):
		input = '''
## F2E`+^"s9q`
## 9n%>|
var WEIl[56.820e+00,19.518] <- uxw ## t)jKQg[{=,wZ}.4S
'''
		expect = '''Error on line 4 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 701))

	def test_702(self):
		input = '''
number Fsb[143] ## G(g&u2zvo5s^%
dynamic DEA <- "'"'"'"#'"" ## v]D9ew
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 702))

	def test_703(self):
		input = '''
func VX (string sc[8.061E76,6E32,0e-95])
	return
string DfzU <- DVD ## &UKq+c8H3kN8*yiqseU5
string vsZn <- 46
## 8]q>abGJ#^n6BqjlMI>
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 703))

	def test_704(self):
		input = '''
var wFCf[1e+25]
func Qb (string iby, dynamic V_6D[18e+95], number KEm8)	return

'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 704))

	def test_705(self):
		input = '''
number vUq[402E-89,14.518] <- 96 ## 5Lr_5
func uwnm (number Nxn[70.937E+57,40.706], number jD, bool oD)
	return mu

func WoF (bool i2O)
	begin
		bool pwp[25] ## b8>
		## EPJFr9|
		begin
			## d#{L.9yq.>GwC6"!QD0
			return
		end
	end

## -wqN.gek6LHD;t
number Ps6[5,88e+48,29]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 705))

	def test_706(self):
		input = '''
## m~;DJ]8zX-=scd
bool nq6I ## e-.8_DxP;b*.3c19
number i13Z[7.802,8E-29,200.936] <- Jd ## t.fI
number HK
func aI (var SMF[397,2.800])
	return

'''
		expect = '''Error on line 6 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 706))

	def test_707(self):
		input = '''
## 8]^}|#nld]p`jQV)b8
## .{+AnX
func F9HJ (string qo4N[2.947e-14], dynamic tmg3, string eM5[0.457e57,8,35.241])
	return F0u5

'''
		expect = '''Error on line 4 col 35: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 707))

	def test_708(self):
		input = '''
func W4i ()
	return "'""
## 4bw6]0p"U
dynamic Eq <- k9 ## en19=d7
number MTty <- 0
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 708))

	def test_709(self):
		input = '''
## H~AD+Q
func kYR ()	return
func YL9N ()	return true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 709))

	def test_710(self):
		input = '''
number QBST[63]
## !WCAK/,X|1q3
func dX (number dUJ9[97.149,270.055e-04,962.651e+03], dynamic F4WS, string mkl)	return Fx6u

func mP (var mzd, bool mG, string PZw[158.679E-88])
	begin
	end

bool oXUJ
'''
		expect = '''Error on line 4 col 54: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 710))

	def test_711(self):
		input = '''
## M
var T_b[95.676,433.731,330.820e77] <- "'""
func TS_v (dynamic ZF[120e+49,5E35,31E65], var hYTv[182e79])	return
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 711))

	def test_712(self):
		input = '''
func cn (number M6J[48], var bj, var ydG[7,85])
	return false

## D~Y/C:F^Cb{$qlB`]X~
## |WTS88qy#%|
'''
		expect = '''Error on line 2 col 25: var'''
		self.assertTrue(TestParser.test(input, expect, 712))

	def test_713(self):
		input = '''
var em <- true
## #:SM>0Ub
func o6XR (dynamic cB8M[15E12,31.298])	return true

number W5y[1] <- "Btv'"" ## zM}[ wESh6DSl
'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 713))

	def test_714(self):
		input = '''
## Z9E7^;*/o20P
func rG (number pD38[9,440.270e19,485.121e+24])
	begin
		begin
			## uW4j&7H{`
			## pNNLP,1=kJAe}Hh#kT
			for ZFyA until true by "h'"X'"b"
				if "Oo" dynamic kDo[983E+35,26.598,0.806E39] ## YXJgO
				elif kqrk return
		end
		break
	end
func Di (var Cnw[45,405.933,994e-74], string FLN9, bool Bh3)	return
## 3>!83=Xb)%;ZT
'''
		expect = '''Error on line 9 col 7: Oo'''
		self.assertTrue(TestParser.test(input, expect, 714))

	def test_715(self):
		input = '''
## z7wl c
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 715))

	def test_716(self):
		input = '''
dynamic yfk[3,9.896]
dynamic DX[28e11,756.777e+31,70e+49] <- true
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 716))

	def test_717(self):
		input = '''
##  ZG/PeMw?/$/9D2
string NL <- RIlI
func jr (string NZZN, string x7[323E79,4e80,25E52])
	return false
string Jfv7 ## NYZA1
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 717))

	def test_718(self):
		input = '''
## P5&*
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 718))

	def test_719(self):
		input = '''
## bd*(43WY
## ,&MIPcx,6
## 6@h*FjT"K8oh4u6
var tv <- n2A ## +rl5SIhX-K,;PW
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 719))

	def test_720(self):
		input = '''
func Xo (var Tp6, var fwXA[1,6.099e+40,2E-55], string uA6)	return
var ym ## <LfV,Ts#_M_sP.]$Z_
string Ei3 <- "'"'"*GW"
number N_cB[735.640e-36] ## Tk4nQCP7&(nZB
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 720))

	def test_721(self):
		input = '''
## P
## f_^
## Z.
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 721))

	def test_722(self):
		input = '''
var A3 <- false
string Rp3 ## k>uxX/b`<ChH$ E
number PfI
string ZPqQ <- vT96 ## vIA49SZ_:^`(N8v
func jnp (string l6[23E-23,890E+65])	begin
		## FS doqg
		begin
			## j"~wd26+?P(.bYniUnO
		end
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 722))

	def test_723(self):
		input = '''
func lO (var vxNU)	return SK
func fgB (string EKq[9])	return
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 723))

	def test_724(self):
		input = '''
## Y<F"MJOld0Nu!}[|#rE
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 724))

	def test_725(self):
		input = '''
number zHCm <- 58e16
var dJ <- OSU
## 3>kGO`
## nhaH!ZKw<ZvC
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 725))

	def test_726(self):
		input = '''
func Pj (var ilW, var NqsU, dynamic zl[1.574,3e+87,0.315e+42])
	return "D"
func KLF (var JR[656.938,395], dynamic Sd2_)
	return
string oYH[65.112E-68,672]
func FN ()	begin
		## ZCCyv6cGIE=X
		continue
		bool RtsV
	end
## pn9^mDKDbE
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 726))

	def test_727(self):
		input = '''
func mn (var dMUj, bool iO[2.560E+67,402E88])	return cV
string ls[807.831e51,746.787e+80] <- FTqN ## f)t.1y)N;2HWA
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 727))

	def test_728(self):
		input = '''
func Xxic (var hDw)
	return
number MZM[485,3.884e53]
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 728))

	def test_729(self):
		input = '''
func rf (bool yGE)
	return "'""
func Rt (number E7[787,2E59], dynamic gD8[949E96,517.123E65,66], dynamic SNBJ)
	return

'''
		expect = '''Error on line 4 col 30: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 729))

	def test_730(self):
		input = '''
func Mq (var If4z[724], bool bbXu[813,2e+20,128.217e89])	return "'""

string pc
number FrG[14.353E-18,114.731] <- ";'"'"*"
func Br ()	return DU8

'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 730))

	def test_731(self):
		input = '''
## K6|@_((8vw
func y6 ()	return "'"'"J2"
func tc (var aQf[233.713,3.924], string QzJ, dynamic f9O[2])
	begin
		continue
		## fGR3>3Fu|}d
	end

'''
		expect = '''Error on line 4 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 731))

	def test_732(self):
		input = '''
## ~:
bool X1ya <- xuaF ## 2Z_
func Uz (bool qz[3.722e-93,1E+82,59.299E-41])
	begin
		## q
		Y8M(";", 81.235E-44, 153)
		## !J}*C:^N}
	end
func oj ()	begin
		for lkE4 until "I'"3'"" by ghR
			continue
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 732))

	def test_733(self):
		input = '''
func ldyi (var oU, number PND[2E-60,2,129], number oC)	return "1S"
func oDX (bool qa[5.502])
	return Y6l
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 733))

	def test_734(self):
		input = '''
func JK ()	return "z"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 734))

	def test_735(self):
		input = '''
## JH
## bhU!&%"R:o>d[sZ <(r
func YT (var YUS, number EGSF[5.819E41,7e+03,1], dynamic y6n[518E51,1,9E+84])	return
## v@a&Sz*n2MG
'''
		expect = '''Error on line 4 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 735))

	def test_736(self):
		input = '''
bool BY[26,661]
## sP 9~F
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 736))

	def test_737(self):
		input = '''
number Upx8[49,3e-61,106.748] <- 524.606
func f7qe (var JqcF[8,1.696E11,66.119e64])	return

func EAth (number lyy, dynamic YY, var nk5[27.677])	begin
		## .Wr5a1
		KsqN[604e+16, HCH, "'""] <- true
		CU(WYm_)
	end

func DTF (number CX6Q)	begin
		## NN&y
		return
		## S`nypQij)EwR_d2
	end
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 737))

	def test_738(self):
		input = '''
## iH#u!rw19T@aqG
dynamic y6[0,467.265]
var bHA
'''
		expect = '''Error on line 3 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 738))

	def test_739(self):
		input = '''
func CamP (string cr[224.183], dynamic i9, bool LrX)
	begin
		if "'"'"" ILYj <- 148.222e59
		else continue
	end
## ^Uyk6
## >W
'''
		expect = '''Error on line 2 col 31: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 739))

	def test_740(self):
		input = '''
func iI (string gdOs, dynamic VW3[8e85,399.728e66,3], number o6j4[7.216,54.893])
	begin
	end
## rfL+
## 2~]k=+ vqp
'''
		expect = '''Error on line 2 col 22: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 740))

	def test_741(self):
		input = '''
func UnhN ()
	return
dynamic H0 <- 22.730 ## Hy*Czd^7Q:$cCD
bool yt[2E94,87,898E19] <- wF ## T]op,_gs4>
func U5My (number Aiop, var MlY4)
	return

'''
		expect = '''Error on line 6 col 24: var'''
		self.assertTrue(TestParser.test(input, expect, 741))

	def test_742(self):
		input = '''
func M5v ()	begin
		## @e&D&^4<:_8Y$S
		bool a0[699.044e16,6E02] <- "V'"." ## Dl{nQA^
		return true
	end
func aL (string vp5[59e+95,91.577])
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 742))

	def test_743(self):
		input = '''
func Yf (dynamic KKx, bool ufc, dynamic zM)
	return 40.502e-51

var nm2D <- 40
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 743))

	def test_744(self):
		input = '''
bool elG <- 88.391E81 ## XG2!4#vlr`nxy!<j!
func IJl (dynamic Z8sS, var q4T)
	begin
	end

func Iybk (bool IIF, var qQas[946,9e-79], var ve[863.627E66,2.842e+97,611])	return
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 744))

	def test_745(self):
		input = '''
number OLj ## ;X+CG+87n/h;p4F-
func XP ()
	begin
		break
		continue
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 745))

	def test_746(self):
		input = '''
bool B_ <- 7.726
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 746))

	def test_747(self):
		input = '''
func pz2 (bool ISf)	return 79e+99

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 747))

	def test_748(self):
		input = '''
string TvP[46.696,58.669,247.844] <- yRfA
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 748))

	def test_749(self):
		input = '''
func Eg ()	begin
		## nDLM%UZAhkp"*?K3HC4;
		## =QA
		break
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 749))

	def test_750(self):
		input = '''
number VGJQ[1,11e-55,3]
func DY (dynamic iOpJ[779.273], dynamic KR)
	return o1

'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 750))

	def test_751(self):
		input = '''
func pKLE (dynamic g5Az[56.486], bool tCXk[30e+13], dynamic WP6[7e-74,97.647])
	begin
		bool uT[3.791,323,87.646] <- 7.821
	end
## &0c3wbA
func is (bool lD[7.653,217E-17], bool mOve)
	begin
	end
string jIW
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 751))

	def test_752(self):
		input = '''
func FID (number xb[285E05,90,27.102], bool OC[4,88])	return

string ggyB
string xvc <- "H'"'":" ## h?0GGO2~y{B5Sw|rhC2
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 752))

	def test_753(self):
		input = '''
func i4 (var yv)	return true
func pjB (var Zi4K, number OHY)	return 241E66

bool B8 <- 871.132e+99 ## =H6@Vg7TeCy/F_O}
## U51`me.9VyQe@Z!#4
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 753))

	def test_754(self):
		input = '''
number UPe
## Wy
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 754))

	def test_755(self):
		input = '''
## Z|8
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 755))

	def test_756(self):
		input = '''
## r.FFd4
bool kJAt <- 582.738
func ui (number YlUp)	return

dynamic JpYo <- 17.830
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 756))

	def test_757(self):
		input = '''
func DiMA (string XS, bool Jp[0])
	return false

var IZFq[6e+49] ## V][
'''
		expect = '''Error on line 5 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 757))

	def test_758(self):
		input = '''
func fc ()	begin
		begin
			begin
				## *7<}h>9^1,PR@(w
				## GhK
			end
		end
		continue
		begin
			break
			## ?+sDz+g}o#"2%<VVOby
		end
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 758))

	def test_759(self):
		input = '''
var lncq ## |
func AZyt ()
	return

func XD ()	begin
		## wdLy38PDT"uir!^&7
		bool mo[6.338,0E91] ## e)lK
	end
func SA8 (dynamic KIKW, bool Jd[33.464E-27,606E-47,529e48], dynamic TXx)	return
## !T
'''
		expect = '''Error on line 2 col 13: 

'''
		self.assertTrue(TestParser.test(input, expect, 759))

	def test_760(self):
		input = '''
## T&FWa>E2
func kdOO (var IuO, bool oEUk[86E+77,8e-95,994.928e49], bool wWY[8E80,1])	return

func cFIk ()	return

'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 760))

	def test_761(self):
		input = '''
func cPH_ ()	return QGR

## +%t/.W2k
string pIZ[7.813e16] ## *Im
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 761))

	def test_762(self):
		input = '''
## O,$fY?
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 762))

	def test_763(self):
		input = '''
## ^E=P8b9Sd,D8`hB0
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 763))

	def test_764(self):
		input = '''
func HbZ (var osy, number QYKy[46.067,7])	begin
	end
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 764))

	def test_765(self):
		input = '''
## r5]p/&n3(<N?
func ZxxI (var xmO, var YR[93,593], number NCM[19E-25,319e39])	begin
		MHwD(true, 28.816E+52, "G")
		wL(3, false, false)
	end

'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 765))

	def test_766(self):
		input = '''
func lUN (string KiI, bool YQ[5E-64])	begin
		## 1 2x?Mc2p#m~
		fuWG <- Y2
		## =4h+Y
	end
string ce[78.543e+85,31.993e81,5] <- XYRG
var LuNQ[1.884E-12,0,75.802]
'''
		expect = '''Error on line 8 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 766))

	def test_767(self):
		input = '''
func bu ()	begin
		## QDA!4tq2/EUe3
	end
## "nAXgap(-u4;bA"em
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 767))

	def test_768(self):
		input = '''
## pkU:",meum:XEq_7}
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 768))

	def test_769(self):
		input = '''
## +*/l-QyO,pd^$XDG(],]
func xL8 (var u7, number Yxi_, dynamic gfZj[87.035])	begin
		## lLlgz @t9<?
		## V&
		## M}eBymm%7tv&aDL4Qp
	end
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 769))

	def test_770(self):
		input = '''
func cr ()	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 770))

	def test_771(self):
		input = '''
var JS[6.273,13.426E62,49]
func k1s ()
	begin
	end

'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 771))

	def test_772(self):
		input = '''
dynamic XEd5 <- RwW ## KEHb`H
var ctT1[720.914E93,51,0] ## Q+
string fIq <- "'"" ## ?T,<f 6g>C@u3@>w8
## V6zVs1tmz{cMbcf Mx;
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 772))

	def test_773(self):
		input = '''
func JZXf (number pU5S, string dG9v, string wF)
	begin
	end

dynamic kS[33.778,874E+60]
var kV[729.495e+83] <- true ## 0t7
'''
		expect = '''Error on line 6 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 773))

	def test_774(self):
		input = '''
## .;L<yU
## _2*<DR-
number rQr[1E-51,0,6.816E+38] ## gV?F9_[==]]k41(:~Y1 
func OJ (var fk81[998.869,2E+47,9.337e+02])	return 124.608

'''
		expect = '''Error on line 5 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 774))

	def test_775(self):
		input = '''
## {{D>c*NER
## p0@;Gl:9N>
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 775))

	def test_776(self):
		input = '''
## Dn)}?bZ1nBcq/Dy9@O
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 776))

	def test_777(self):
		input = '''
## lag9c+EYX kJ(qS&~IK
dynamic Km
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 777))

	def test_778(self):
		input = '''
var Ms ## r]xJYW2W1K;veInql/:
'''
		expect = '''Error on line 2 col 29: 

'''
		self.assertTrue(TestParser.test(input, expect, 778))

	def test_779(self):
		input = '''
func A47O (dynamic VC7I[87.209,306E-80,9E+53])
	begin
	end
func fez (dynamic RrQ)	return "S'"'"K"

'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 779))

	def test_780(self):
		input = '''
func xnVE (bool bfi, bool g79[49,62.559e97,9e-76], var Er2[7E55,4.509,30.141E+34])
	return

## jV
'''
		expect = '''Error on line 2 col 51: var'''
		self.assertTrue(TestParser.test(input, expect, 780))

	def test_781(self):
		input = '''
number K2iy ## lfG)KG=Mb23Ap`L;R#k
func OI (var L0[62.018e93,834.801E-45], var bUJa)
	return false

string LF8W ## 3e|<6
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 781))

	def test_782(self):
		input = '''
var KG[45.903] ## ]g%X
func mnN ()	begin
		## i*
	end
number ngZ
dynamic ElNy
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 782))

	def test_783(self):
		input = '''
## -DpXF0G$
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 783))

	def test_784(self):
		input = '''
## k*N/PM&yQre_<
var qq <- 5.192 ## D$: Yg]^^-G4
## "
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 784))

	def test_785(self):
		input = '''
bool hAp ## l1kE]o7C)R5b;?R1<V
## Ce4~)~A9ju=
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 785))

	def test_786(self):
		input = '''
number ioZ[6.400,0.139] <- ll
## *E" S(>uJ EqI
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 786))

	def test_787(self):
		input = '''
## W}E[0
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 787))

	def test_788(self):
		input = '''
## &S$%d6!
## Qy$>6p03>U^
bool GdP
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 788))

	def test_789(self):
		input = '''
func dCC (string le)
	begin
	end
dynamic YB[1.350,80e57]
'''
		expect = '''Error on line 5 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 789))

	def test_790(self):
		input = '''
## U<3<0v:YL?)Xs:Xs
bool HL1h ## 5Qkt3r$F_
func hf_5 (number JAC[192.077E-74])
	begin
		## LWWYJ@ORc(x<
		## Pd;tr1;C4if
	end

## G,ihckIH
string s3h2[4,1,6.809E+83] ## S0Xh
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 790))

	def test_791(self):
		input = '''
## X+~PY
dynamic QsHH ## xC@{~
var k3[899,296e-31] ## Vr+J+VB$K
func xxKQ ()
	return
'''
		expect = '''Error on line 4 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 791))

	def test_792(self):
		input = '''
number bN[912E+33] ## `C(
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 792))

	def test_793(self):
		input = '''
func pSq (var OT, dynamic Cn[157E+00,7.233e-95])	begin
		string MS[42E05] <- "#'"!'"'""
		## 1"5f0
	end
## W
func Yf (dynamic oR, bool INJ, number E2)
	return

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 793))

	def test_794(self):
		input = '''
func mV (number PLyC, number zk[2e+92,31.724e-32,18.455e40])
	return
func utb ()
	return "i'"3'""

## 23YgdBj/,Jn9?KXtU,
bool HZ <- false ## 0
## S/lfTJQR
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 794))

	def test_795(self):
		input = '''
func qUbV (bool XX[33.319])
	return
bool QwAI
string jHw[82.096e-95,9E+23,12e+70]
var r4j <- q85R ## 5.5
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 795))

	def test_796(self):
		input = '''
func oDqY (dynamic GPdK, var JPPf, string o3)
	return 5

'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 796))

	def test_797(self):
		input = '''
func dy (var stDr[1.131e89,546.719e15])
	return 647.230

func K9ME (number Yk2, string ACr[9.496,42.736], var gcr[5.587])	return HRL
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 797))

	def test_798(self):
		input = '''
func o4v (bool F66, number U_l[5.183E+31])
	return O3K
## J_K4Sa`:!x7f7a
func Utv ()	begin
		## 3mM
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 798))

	def test_799(self):
		input = '''
number XL8F
func NQP (bool mt9x)	return

bool PWx ## Qm5rp}^t2Ay pej
func Hnv1 (bool VnG, number hbM[49E-91,76.525E-09,44.151])	begin
		break
		begin
		end
		return true
	end

func tM (number AJeb)
	return 20.851E-92
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 799))

	def test_800(self):
		input = '''
## iL]54+%"n5LT.j"2~mR%
dynamic a8 <- c9E
func mQG ()
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 800))

	def test_801(self):
		input = '''
func E1 ()
	begin
		##  !h8cFio(0bcaIC5#
		## YP}K#FzWm6-Z.|^
		## @-fVS_SJ^N%q(N<v
	end
func ns (var izPM[52,1e46,526e12])	begin
		## U,
		continue
		a0 <- ZHa
	end
string ICes[5.230e+54,811e40,9E+09] <- "%'";:'""
'''
		expect = '''Error on line 8 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 801))

	def test_802(self):
		input = '''
var rm7[81e-62,690.112e-01] <- 677.179E73
## X)#:D7A5|>XQ
func vS (var YP[5e24])	begin
		## 2I`g0<L%4
	end
func ejx (string NGIc, var hW, bool lZH_)
	return true

'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 802))

	def test_803(self):
		input = '''
func OY (string pFY, dynamic gFg, var bvC_)	return true

'''
		expect = '''Error on line 2 col 21: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 803))

	def test_804(self):
		input = '''
## }Si#Y
## hNR6*T8tJMub 12
string lE[0.347] <- 642.535E49 ## w5 kJJ`*eBDn6
## l|Ud%
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 804))

	def test_805(self):
		input = '''
## . ~9
string QC7N <- vKmp ## vy5:(8.j%"pLk)
string gG <- Ub ## vEv1l~%gR&jacO
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 805))

	def test_806(self):
		input = '''
## eLc2|0
## }I`~QB4T%n_;`i
func W0 (string HC, dynamic wwVK, number Qk)
	return false

func DRi (number JN0, bool rmh)	return false

'''
		expect = '''Error on line 4 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 806))

	def test_807(self):
		input = '''
var UJN[799.869,347e17]
dynamic sVd ## s-R=0([x/,/U{%9|
## w<OaD082g5.zRF
## +)>yR%c;!Ud9No
var ox6s <- true ## )vfH@(Gw/
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 807))

	def test_808(self):
		input = '''
##  h7>I,$voq1BNV*dkR2=
func s4 (string Hh[8e-66,30,2E-35])	begin
		continue
		break
		## N$>o
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 808))

	def test_809(self):
		input = '''
func HrU (var SaDZ[683e42], number h8, string uq)
	return 7
func VEs0 (string PUYX, var hHO)
	begin
	end

## 6f
string tp <- false
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 809))

	def test_810(self):
		input = '''
bool iloR <- 294.497E+69 ## -Te3
func cmW (string cEL[20e+67,1.421,578e-54], bool c2o7[84], string WC)
	begin
		LNMO <- 788.148E27
		nd12()
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 810))

	def test_811(self):
		input = '''
## Na|]aTq]EJEWeC
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 811))

	def test_812(self):
		input = '''
func fNr (dynamic UR0e[349,417.185,21e-62], var E3[1.849,597.684,920], var bK0E[549,8e+79,901.531e91])	return WU

## Q~0I+.7l$-?YG,<
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 812))

	def test_813(self):
		input = '''
func grh4 (number uY[3.871,48,59.102], string D0)	begin
		if 8.765 for H3om until "'"T'"" by "!F'""
			return
		elif nt return
		elif r4GL bool zU44[41.236e+50]
		elif Lt return
		elif "G" if "'"" begin
		end
		elif true begin
			ovhg(true, OU)
			m9t <- 5e01
			## 5{iRSuHrj;r8h>O#(?
		end
		else break
		## P
	end
var Hax
## vJ!x}uIn(ec~Za
number O8_ ## `BN~Il~>WN!
'''
		expect = '''Error on line 3 col 5: 8.765'''
		self.assertTrue(TestParser.test(input, expect, 813))

	def test_814(self):
		input = '''
var eR
func jB (string YOQ, var Zd)
	return

func Ea (dynamic RvpX[474.632,8,6.800])	begin
		## {-BML@
	end
## H09,k1#
'''
		expect = '''Error on line 2 col 6: 

'''
		self.assertTrue(TestParser.test(input, expect, 814))

	def test_815(self):
		input = '''
string rI[204e+62,666.632e14,380.596] <- TzCx ## Muz6l{m0l)##
bool TxC[171e-45,632E+46] <- false ## T<}>7<7M1?VC(
## V
func XI (var vA1, number jRIG[95e+69,53E-17,43e+43], var CC)
	return

'''
		expect = '''Error on line 5 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 815))

	def test_816(self):
		input = '''
## EvBykR[x u/NE
var w2l ## <mI=7b#ciC]DH
func Mn ()	return
'''
		expect = '''Error on line 3 col 24: 

'''
		self.assertTrue(TestParser.test(input, expect, 816))

	def test_817(self):
		input = '''
func dU ()
	begin
		continue
		## /7}R)
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 817))

	def test_818(self):
		input = '''
string GA01 <- HTZ ## }HRG5eHge%!uzv9n
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 818))

	def test_819(self):
		input = '''
number IVV <- false ## FC)A9_:qLjL
## ML0PZwR+z?>JR?Zv
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 819))

	def test_820(self):
		input = '''
## y!9z(m@hIr
func JhNH (number xW[20.232,132E70,35.133E26])
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 820))

	def test_821(self):
		input = '''
bool eHeR[669.277,6.363e-86] <- Mi9d
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 821))

	def test_822(self):
		input = '''
## tgV!W}.
func ervP (bool Z8)
	return
## (@~35&l~Zo(
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 822))

	def test_823(self):
		input = '''
func vRw (number eB, string j6ez[810.035e+74], dynamic S8Tj)
	return
func vU ()	return

func rKt (string LafE)	return false

func w6 (number l5D, number iRao, dynamic znW[47])	begin
		## Y3Z!d#d/@vk;m/GJ-jM
	end

'''
		expect = '''Error on line 2 col 47: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 823))

	def test_824(self):
		input = '''
func IML (dynamic R9)
	return 45.293e70
## Mn8%
func SOf ()
	begin
		continue
		## -xB#!v)Glh%rw8#GG
	end

func Eax (var aGJP)	return

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 824))

	def test_825(self):
		input = '''
dynamic n8 ## ~hEH=KF=%]rd*if-A{
func nNEA (dynamic aMTN)	return
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 825))

	def test_826(self):
		input = '''
func ZqL ()
	begin
		## :68 ?^!l dFCw
		continue
	end
func xAqs (string sMO, dynamic EAD, number Zu[798.467E-11,28])
	begin
		begin
			## X-5W*z=(dm-P
		end
	end

func zZK (string c7J[8.046,484.560e08,79.363E+36], bool kyf7[9,83], dynamic D0W)
	return
func N1 (string I47, var sdK[40.888,3.994], bool pF[852.950E-65])
	begin
		## `>@5 WB?{:zbn,f9|Q8
	end

string GCHh <- false
'''
		expect = '''Error on line 7 col 23: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 826))

	def test_827(self):
		input = '''
## s9{&Aa6,IhU`;-8;
func wf7 (string idL[0], bool j6)	begin
	end
## H2fz
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 827))

	def test_828(self):
		input = '''
string gW59[5E-25]
bool KYSk[62E-92] <- "'"'"'"G-" ## 0$~
dynamic QWH <- true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 828))

	def test_829(self):
		input = '''
number LNG[22,9.479E+24,4e+83] <- true ## >_NoDv#*ADGY
func XhX1 (number dU4)
	return
bool uL[42.960e-50,649e+21]
func sLS (number WP5J[9e42], bool BnsD[1.854E-92], dynamic nR[170.402,118])
	begin
		## ~
	end
'''
		expect = '''Error on line 6 col 51: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 829))

	def test_830(self):
		input = '''
string EbAI[3E-83,79E29,472E-29] <- false ## %5!:?4>D02z"tzv+
## fm)6
dynamic NJ ## d[6ksWB;)3xyK4cV$
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 830))

	def test_831(self):
		input = '''
## 5V
dynamic qv5K[246e-02,76.079E-35,9E+74] ## t@
## 6QQ}D]et?/1.1WD
## bVM$(v}m&lj!yvkKLg:
func IeFI ()	return jhtF
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 831))

	def test_832(self):
		input = '''
number ViPq ## M.ivY>[JS^&?
func zLv ()	return
func x_6 (var dNgc)
	return zS

'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 832))

	def test_833(self):
		input = '''
## =$.=J
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 833))

	def test_834(self):
		input = '''
func tC (bool AZqR[743e15,50,7e+74], bool Mp[156.253e93,7])	return

## 0X7y>=t@
dynamic Qz[195.983,38.242E+56,67] <- false
var gSO[0.575E-28,51] <- true ## !Nz
'''
		expect = '''Error on line 5 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 834))

	def test_835(self):
		input = '''
func gAn (number jE)
	begin
		## A7"=1:UmC+>eG+~YyV1
	end
func rVH (string ek, string qb[38.608e+04,2e-08], number yQ1)
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 835))

	def test_836(self):
		input = '''
## z
func V9 (string jwz[932e14])	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 836))

	def test_837(self):
		input = '''
## ahnZMYDw%%~E:W=fFT>3
## NbNj2;4j}!~:9M/La#
## oPH(;b
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 837))

	def test_838(self):
		input = '''
string ezmu[69.104E+52,49] <- false
## t
## U9fnr>39{B?),w0SkRMo
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 838))

	def test_839(self):
		input = '''
dynamic We0 <- true ## JWgmx}:|?<i%*
## K-+vP
## -K[ee3"cl=#@)O !KJy
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 839))

	def test_840(self):
		input = '''
## 2xh;
func vy ()	begin
		if true return
		else string A_5 <- true
	end

func utk (dynamic mr9F[70.307,4,440e96], dynamic fCkY, bool FcxH)	begin
		begin
			## o&IkB"
		end
		## "
	end
'''
		expect = '''Error on line 4 col 5: true'''
		self.assertTrue(TestParser.test(input, expect, 840))

	def test_841(self):
		input = '''
dynamic WrT <- omk ## kQ4LQ2|$4%<D&Jq/G
## -t>r7-]qS{[-Ra*Klwr
## T3p#w
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 841))

	def test_842(self):
		input = '''
## JoR@9*=mxDityU;C
dynamic gUKv
string k01X ## EQv+
dynamic Qg_[9E+70] <- 381E96 ## u9/.nLp`
dynamic ev
'''
		expect = '''Error on line 5 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 842))

	def test_843(self):
		input = '''
## *A?U#D|
var Suhf[628.338e+44] <- LBn ## +C_8_&B*,%s:7Lv<
dynamic NuY
dynamic VYL <- "8'"'"'"" ## q|7KTIFk
func zAi (dynamic RD[506.069,1], dynamic lZ51[57.879e-54,409E-70], number ik)	return 8
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 843))

	def test_844(self):
		input = '''
func fbm (string LXyK, dynamic Bi[40E+35,8,8], number gAfC[2.768])	return 143.924E+99
## ?VLot<JM;)5SP
## v!)AfJ5CGq05
## 0W/no9
## mqY!xN_5l2S9
'''
		expect = '''Error on line 2 col 23: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 844))

	def test_845(self):
		input = '''
func srj (number Jg, var mB[886.463,5,1], number pHvh)
	return 9.494

## t-^Wv7c[45#`-u
func jfY (string qq[8E+10,14.030E-40])
	return
'''
		expect = '''Error on line 2 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 845))

	def test_846(self):
		input = '''
func DY (dynamic n7OU[793.136,7.132], bool RF[666], dynamic si[65E70])	begin
	end
func age3 (number G9[40,32], dynamic Jx[55.307])
	return

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 846))

	def test_847(self):
		input = '''
func Af6 ()	return false

func fZrt (dynamic fQLN, number Sc[193.891E-38])
	begin
		break
		break
	end

## ~w,/Dc(m%)#p{@y
'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 847))

	def test_848(self):
		input = '''
number g3H
bool iMfC[4,606.657] ## =xuh4H~f>.2
## RrL>{LC$)$}-OC0f,n.
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 848))

	def test_849(self):
		input = '''
## P#~Y."8!1>s
func mz1 (dynamic Jw[41.303E17,8e-33,80.179])
	return 4E-81
bool Qw ## >sZrIF=VOo/)z
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 849))

	def test_850(self):
		input = '''
func gGHW (string pe[9], var cLQL[2.908,9,829.389], var Z1Us)	begin
		## F=XI!&md=#L^CPtryuh~
		## Z. {oD
		## V`;A
	end

## .
'''
		expect = '''Error on line 2 col 25: var'''
		self.assertTrue(TestParser.test(input, expect, 850))

	def test_851(self):
		input = '''
number Oz[9.340,9E+99,1.054e71] <- ""/'"" ## Oq;#
'''
		expect = '''\''''
		self.assertTrue(TestParser.test(input, expect, 851))

	def test_852(self):
		input = '''
var No[4,6.421e-74] <- false ## O
func JI1 ()	return false

'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 852))

	def test_853(self):
		input = '''
func Ev (string j99n[0])
	return

number DeM4[4.896,64.235,628.134] ## r#".R]~Utx/Gip;K6
func jY (bool ezyX[0.108,822.527E-37,70.284e-85], number he3)
	return rY

bool uX6W <- "k'"'"B"
## n9=R#
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 853))

	def test_854(self):
		input = '''
string Qt[0E+34] ## dIp
## }/i4g02&*??U628
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 854))

	def test_855(self):
		input = '''
func qeIT (number txc)
	begin
		D4()
		continue
	end
string Kf[980.464e70,0e53,1]
## z6iWm8
func Cjxs (var zq[3.651E06], number wfg[8E+82,53E54])	begin
		bool Fr
		VcD(7.148)[IAqm, "R[e'""] <- VkM
	end
## ZV4[XJ}[`8v?_"3#"
'''
		expect = '''Error on line 9 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 855))

	def test_856(self):
		input = '''
func KsW (dynamic GFB)
	begin
		## %?^fh$:<
	end

func sTcp ()
	return false

## I
func aAXS (number xV[1.400,0])
	return "+("
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 856))

	def test_857(self):
		input = '''
number QT
func EPW (var GXr, var Ta[0.163e-93,30E71])
	begin
		## xtd7l]g?4{Kyn
	end

dynamic lJlG[951]
## _$GGI}Fg(GD
bool bs ## Ms%xt
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 857))

	def test_858(self):
		input = '''
dynamic V3[90.696,442e+19] <- 559 ## $mf5M3psqM<:vP,@B7#m
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 858))

	def test_859(self):
		input = '''
## p(*F0>^bQ_mQPNd@d
dynamic U9p ## nzdS=
## Z)Y!Z,W=|#
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 859))

	def test_860(self):
		input = '''
## lD*QV(5%>xo
bool SFq[274.089e24,6.341,9.321e40]
## xdM~691@H
var Gt9j <- true
string AZfE
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 860))

	def test_861(self):
		input = '''
bool Vr_[78] <- r5a ## UAJRB0HiOu[rM6
func eFS (string Wn, bool Z7rs[9,1.399e-60], dynamic pHH5)	begin
		continue
	end

dynamic k4[14E+35,3.323] <- "'"W"
dynamic XZ ## *yW(
'''
		expect = '''Error on line 3 col 45: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 861))

	def test_862(self):
		input = '''
## 7^^3gJCS{>g(R3
string Wc <- false
func zJT (var sX[163,2,712E45])
	return

func wpuU (dynamic HP)	begin
		Wp["'"'""] <- Ajf
	end

func Vtrs ()	begin
		## S )|0h 
	end
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 862))

	def test_863(self):
		input = '''
func zcFC ()	return

func eY (number eTmh[493.537E-26,8e02], bool kvz[7,3,9.849], dynamic b9)
	return

## Xw
func fDd4 (bool vvI, string cUce[187.421e-68,83.473e+48], var L95)
	return

## DvpHrWEl^&9k.>3f
'''
		expect = '''Error on line 4 col 61: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 863))

	def test_864(self):
		input = '''
string Kb2[1.528E-44] <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 864))

	def test_865(self):
		input = '''
## GZ:N?HB
## h6bD9hBOwn KTjMgV*g
## %*+tuo98k8%$azaC]4n)
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 865))

	def test_866(self):
		input = '''
number rD[566.794] <- HCl5 ## |.<)yFZ:3cXdnX 6jq
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 866))

	def test_867(self):
		input = '''
## YgwZ9t-nBN]:IZO]G
string RowR <- hid8
number PF0G
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 867))

	def test_868(self):
		input = '''
## 0cuCs"fYywA8~/wn
var pXR ## oa6"5b8P/K Ha*=*ecpO
func RLF (string QFcw[9.768e-44,332])	return "k'""
'''
		expect = '''Error on line 3 col 31: 

'''
		self.assertTrue(TestParser.test(input, expect, 868))

	def test_869(self):
		input = '''
var HAg2
var AG9u[42e-33,65.766,495]
## =o?nbYlnqUeU{$yn311
'''
		expect = '''Error on line 2 col 8: 

'''
		self.assertTrue(TestParser.test(input, expect, 869))

	def test_870(self):
		input = '''
func gzaZ (var Txm, bool NHVb[9,861.670,636.388], var IL[643,335])
	return
## uVDM`
func jT ()	begin
	end

var x8
## .gcgstj&[QkWU1m|So<^
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 870))

	def test_871(self):
		input = '''
func OZaG (string Kj, string Zn[6.278])	return RFd
func ro8 (string r7l[0.808E62,461.254,636.396])	return "`"

## ES.~Q{G
var pc ## {>!SZ^c,zB:zIP`m3
'''
		expect = '''Error on line 6 col 27: 

'''
		self.assertTrue(TestParser.test(input, expect, 871))

	def test_872(self):
		input = '''
dynamic uz[751e+43,2.184E-75,46e27] <- C1
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 872))

	def test_873(self):
		input = '''
func hI8Y ()
	begin
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 873))

	def test_874(self):
		input = '''
func dEcG (bool a_v)	return

number Be ## Wa,#n
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 874))

	def test_875(self):
		input = '''
func DiHX ()
	return
## Th_4;H
func KTC (string MN_N[5.483e72,533e95,6.742])
	return

func oU (string W3P[796E+30,85.130], string alQV)	return ","
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 875))

	def test_876(self):
		input = '''
## J:Gx)c
number M_[4.836e+49,28.739] <- Jg
## P8p^
func w52i ()
	begin
		## PuIz ;:!"VcF.[MQ{|
		## /r/
		if 77 HYb(false, Tpw1, BCv)[57.680, FHe] <- "'"("
		elif "'"'"O'"" if false if "'"" BwN <- oCJv
		elif "'"$" return wl
		elif true sm(39E01, true, rZ7)
		elif true return false
		elif "'"-'"" return ":C'"'""
		elif "'")'"%" return 95
		else continue
		elif Et_O p6(13, Oyn)[15E71] <- kJx
		elif "&'"'"L'"" break
		elif false return false
		elif "U'"" I1c(2E+75, "'"E'"'"7", ""2'"")
		elif false dynamic z9_E
		elif true begin
			for tL30 until true by "*-E"
				Su <- VCn
			return "G4X'""
		end
	end

'''
		expect = '''Error on line 9 col 5: 77'''
		self.assertTrue(TestParser.test(input, expect, 876))

	def test_877(self):
		input = '''
func XaE (dynamic dfbB)	begin
		## i
	end

## v2i
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 877))

	def test_878(self):
		input = '''
## &k05XRzajhwX<Mu"
## :-sOCdXG^g:4+{d7/d<
bool lK <- 744.279 ## b_!ia
## RiJoF,nTC&<_]6{i&~QK
bool L6 ## 8La{ylB
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 878))

	def test_879(self):
		input = '''
func rPQ (string PXO8[24,948E+52])	begin
	end

func Fc4V (dynamic IC3Q)	return
var d6hi <- true ## dQ>x"x?;kVuVc:UcN%+7
## a0]{J]A=x
## FbyJd
'''
		expect = '''Error on line 5 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 879))

	def test_880(self):
		input = '''
string X9n[90.024,58,581] <- Qq3
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 880))

	def test_881(self):
		input = '''
func c5F (string q7qE, dynamic EP, var Hz)
	return
'''
		expect = '''Error on line 2 col 23: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 881))

	def test_882(self):
		input = '''
dynamic OU[5e+83,7.709e-59,63e+61]
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 882))

	def test_883(self):
		input = '''
var Rod
'''
		expect = '''Error on line 2 col 7: 

'''
		self.assertTrue(TestParser.test(input, expect, 883))

	def test_884(self):
		input = '''
func ud (var AMl[105.978,1])
	return 1.499
string rf3[43.255] <- "'"'"'"{?"
func aDro ()	return
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 884))

	def test_885(self):
		input = '''
var Cp
number bo8j ## =Mic?2ic8rjcpk0
'''
		expect = '''Error on line 2 col 6: 

'''
		self.assertTrue(TestParser.test(input, expect, 885))

	def test_886(self):
		input = '''
bool lJFN ## [Z~7Cg))VP
## vbH)>
func o8ah ()
	return

func Kzb (var N_[51,149.920,809e+19], dynamic x27M, dynamic ihjM)
	return

dynamic ak
'''
		expect = '''Error on line 7 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 886))

	def test_887(self):
		input = '''
func kpp (dynamic Qt[60.229e-49,0.634,3E+38])	return "'"_G'"["
func npq6 (number lN1L[51.668E+71])
	begin
		w5sn(591, Mip)
	end
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 887))

	def test_888(self):
		input = '''
func Fl ()	return 98.992
func GM (var m7[941,5.769,8.024E65], bool bQ0s, var m0)	begin
		## Y]Ilf`,=iww6
		if rSj continue
		elif sr number vWD[3.301E74,796,34.672] ## xo/ysalg8N
		elif "'"'"" bool VTW[337E+15,258,46e+72] <- "'"'"'""
		elif true qP2(75.614E+32)[false, QqG_, x5] <- 92.501
		elif false var pV[686.574,21,33] <- Qeoc
		elif "'"'"SH" for P_xt until "'"" by true
			break
	end

## n3w-*}CPs(zG#d!{
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 888))

	def test_889(self):
		input = '''
func fqMm (var vy, dynamic nySA, string UkIi[0.258])	return
bool FS ## Cd30*%}.F**MzW<QM#*
## qw+d(x|
string W6 ## &x5g 5PG/#x
## "F<F#RCr"b?|%}>
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 889))

	def test_890(self):
		input = '''
func Bo6P (string I9ub[140e-12])
	return true

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 890))

	def test_891(self):
		input = '''
## 9ne%s6b)[+#
bool cL[274,15.916,753.877E-16]
## Pi
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 891))

	def test_892(self):
		input = '''
dynamic nE <- 85.281
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 892))

	def test_893(self):
		input = '''
func O025 ()	return

## :M]vqxUs<pB>e1cc|vX#
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 893))

	def test_894(self):
		input = '''
string b8 <- false ## _!AJ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 894))

	def test_895(self):
		input = '''
func Oh3 ()	begin
		if false for o7F until ONs by IUD
			dynamic Zoqh ## |oD*w/Ws#E|T
		elif true if "'"'")*" for o5_s until ishc by pgGA
			begin
				if 99E-00 if 796E+21 string xOf2 <- "(" ## *w$rcU/^q|
				elif 43E74 F2TT("'"'"'"", "'"'"p")
				elif j5_A return
				elif 30e-24 for xGxB until "c" by true
					if k_qK h0z <- false
					else gRp4["'"D", false, 9] <- 6.652
				elif false TKYu()[DqaJ, false, false] <- "W'"'"'""
				elif false NYz <- "4@'"'""
				elif false Ws(25.739, piY1, 2.171E+84)
				## b>6>LB H_:1bFD&<Fn[Y
			end
		elif false aK(Fx, KA)[OzM0, "'"h"] <- "N'"7'"'""
		elif 35.649 if Rxp number S3zs <- false
		elif "'"'"'"'"" break
		elif false ie <- true
		else Gks("A'"'".'"")
		else return
		else continue
	end
## }V{7(j>]h|d
func cNB ()
	return "'"E'""

var Tln[57.669E94] ## S#RBZ[|(
'''
		expect = '''Error on line 3 col 5: false'''
		self.assertTrue(TestParser.test(input, expect, 895))

	def test_896(self):
		input = '''
dynamic CPPv[58E+25]
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 896))

	def test_897(self):
		input = '''
## R*1|2zR
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 897))

	def test_898(self):
		input = '''
## BXq<fm-9Ksc
string Cv[709] ## 9SJX1ej
func UY ()
	return false

bool VFZ
var a7 ## |se6ws[8@++YT
'''
		expect = '''Error on line 8 col 23: 

'''
		self.assertTrue(TestParser.test(input, expect, 898))

	def test_899(self):
		input = '''
func eKiO (number iib4[6e-45,91.234], string Rv[39.797e-76,713])	return

var VY8[5e-42,90.789e+25] <- 5.447E-30 ## wY6_`m,#g[8b8
## t/HE+
func F1sv ()	return oL
'''
		expect = '''Error on line 4 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 899))

	def test_900(self):
		input = '''
## 1r.sEU]?l{"^2wa6zU^
func aq (number Ojyb, string oe[72])
	return N3R

func dy (bool MCc[1.136E44])	return

number lLnw[53e95] <- 956E+66
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 900))

	def test_901(self):
		input = '''
func aQ (string bp1[7.263], var tRV)	return gp8E
func Hr ()	return false

##  .9>9x}Y
'''
		expect = '''Error on line 2 col 28: var'''
		self.assertTrue(TestParser.test(input, expect, 901))

	def test_902(self):
		input = '''
## >*Z_Q5iG3Y0}{
var vMFd[857.421] <- true ## o]hX`tJ
## ;&WMeZ5R
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 902))

	def test_903(self):
		input = '''
number HUSI[369] <- St
func mXD (string rLC2[26.132,95.680], dynamic rEu, bool DAA4[356.390E80,6.571E-09,1.511E+71])
	return

'''
		expect = '''Error on line 3 col 38: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 903))

	def test_904(self):
		input = '''
bool DEw[592,93E-26] <- j5I ## @"X>
## #k-qXlY8UFJ
string Ws1 <- 58.134E+81
number Ywi[499E+43] ## >4Ytvs6TKondBe
bool rzlW <- s5 ## 8 }U<
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 904))

	def test_905(self):
		input = '''
dynamic G1mV ## PQI)Nj8$[3,>TjH4.1oB
## LoerVZc"e&/
## wjh^=GA/x$Wvv^
## DxH
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 905))

	def test_906(self):
		input = '''
func vb ()
	return

func iO0 (bool w0)	return false

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 906))

	def test_907(self):
		input = '''
## JA&9?rQ[,9n1_aMiu
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 907))

	def test_908(self):
		input = '''
func RG (string IY[323.019E+54], string aFtZ[4])
	begin
		## .%^U1%Tje2Z@O-0M
		## Q[QFI
	end
## OBD5k;nFjm)Dr<:
## RW"(+J+*1[k:wrV!
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 908))

	def test_909(self):
		input = '''
func uOx ()
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 909))

	def test_910(self):
		input = '''
var ggi9[35,1.481e71,47.368] <- true
func fdKV (var Pl, string ox, bool xO)
	begin
	end
## I^vb
var pU[805,0.167] <- "n'"[;'"" ## NwNB{q|y6XOcmdHPD
string MF
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 910))

	def test_911(self):
		input = '''
func wm (bool g_G[685,83E+87,78.963e74], string FdkO)
	return
func xoc (number tuH)	return La
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 911))

	def test_912(self):
		input = '''
func c2hc ()	begin
		## 45J~HkVzG
		begin
		end
		## iM*,
	end
bool fjW
## )tKR_JtU>>$c
## HfVaPB^$:&
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 912))

	def test_913(self):
		input = '''
func cbs (string cDUl[66E02,555], number tVRT[5], number vK[8e-48,826.432e-95,74e+62])	return

## ,FyaL)|Z3Y/=E_n-h4|W
## 6v(W+
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 913))

	def test_914(self):
		input = '''
## b5/[VG?UF,`,/M
bool Ji1m[39.615,5,450E50] <- "'"='"6'""
func tp ()	return false

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 914))

	def test_915(self):
		input = '''
## n!Y)oT?S
number y1xU[91.809E+89]
func FHv (bool Dg[6])
	return
func gJ_Q ()	return 786.944E50
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 915))

	def test_916(self):
		input = '''
func X2mD (var iTWT, string IFy[708.236e+75,366.023,587.478], var wM)
	return 525.610
func x8 (bool xh_Z, string Lk, dynamic hms[78.659,420E-78,719.109])
	return

## sW&H-j&"iG*3dEq"
func ELE (bool fR)
	return
## {xq^pjz:?1
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 916))

	def test_917(self):
		input = '''
func UXif ()
	begin
		## yG6:]y`$]2jmtC%@
		zj[7.438] <- 5.893e+87
		begin
			y3()
			## @0uUX<?^,k?A<T
		end
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 917))

	def test_918(self):
		input = '''
func Bf0 (dynamic MA)	begin
		xUw("p")
		## lem$ePI
		## JSqE.OMs8pzBr{,%t;
	end

## z5^[T#&dsZ)!Hk.OM
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 918))

	def test_919(self):
		input = '''
func k4yP (bool VsPi)	begin
		begin
			URz <- N8F
			## gQivg}
		end
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 919))

	def test_920(self):
		input = '''
func C0h (bool elHF[53.097e03,234.636], bool iw)	return

func j0 (number ubBC[78,759], var wPHU[31.591E+57,9.571e+95,3.760E-14], string Sk3)
	return
bool Zwv[37]
func xQY (string Wdca[30,53.485e-14,1.345], dynamic ogX6, number rWX[240.034E72,996e-47])
	return 811.897E+68

'''
		expect = '''Error on line 4 col 30: var'''
		self.assertTrue(TestParser.test(input, expect, 920))

	def test_921(self):
		input = '''
dynamic HUHs[4.728,7e75] <- ft
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 921))

	def test_922(self):
		input = '''
## cWYVoOt|"a-}Z~k
func OvvG (string O76l, number b_, var Rtlu[138.673E+22,848.397,951.754])	return "%"
func iuX (dynamic IOQ, string StH[59], bool Tm)
	return

'''
		expect = '''Error on line 3 col 35: var'''
		self.assertTrue(TestParser.test(input, expect, 922))

	def test_923(self):
		input = '''
## N^?Z!Sk9#l(Ycu!Nu
## A:=I8[};D9PBeUK+io~9
func e8h (string A1t)
	begin
	end
## KL>Ogo^MemmH.,+e
dynamic uHC[3.184e53,0] <- 3.867
'''
		expect = '''Error on line 8 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 923))

	def test_924(self):
		input = '''
string AI8[959E+96,0.289]
## p/n
dynamic dQj
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 924))

	def test_925(self):
		input = '''
var extm <- false ## f{)n[uw]
string nLA <- Xu
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 925))

	def test_926(self):
		input = '''
func H9 (dynamic GjN, dynamic M99[308.740,9e+51,169.142])	return
func oDD (string OYCD[0,131.574e+98,52.244])	begin
		## 2B
	end
## >peKTXO-e*s
func vKAZ ()
	return

func iGbp ()
	return 502
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 926))

	def test_927(self):
		input = '''
## s(E7*R6&
## j}xE`poQSK
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 927))

	def test_928(self):
		input = '''
bool jaog
## #qwEMF)X-)UUe*q
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 928))

	def test_929(self):
		input = '''
number chh1 <- true ## ,rdxMNi/oS{f=%$cMhOh
number o0qQ[8.882e+34,280] ## O#>}>qc!
func gdO (dynamic yiA0[6e26])	begin
		RN()
		number mGe[586E+20,679e+25,6]
	end
func ko ()
	begin
		return 459e+50
		break
	end

'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 929))

	def test_930(self):
		input = '''
dynamic ciVw ## .W$$.
## #=2=I9uZ7B~[IY
func Fjp (bool Ktc, bool GL, bool RS9)	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 930))

	def test_931(self):
		input = '''
var DaX <- 16.127E-71 ## ;lc_a^F)/S=p,625Wf
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 931))

	def test_932(self):
		input = '''
## gzReoO2fo,P&Dm.=
## $ha+(w;}ub`
## BceN[dz]Bb 1@!Egg3u
bool DyN[79.969E+25,7,579e15] <- uVd
## 8
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 932))

	def test_933(self):
		input = '''
func Vv_ (number iQ0R[68.112], var qSvc, var PUI[3.269e-21])
	begin
		if "^'"y'"" for EaG until IQUQ by "'""
			begin
				A_Z(ymUx, 40)
				return 990.894E+04
			end
		elif "j" begin
		end
		elif false if 766 for DdE until false by false
			return true
		elif nFM dynamic IS ## ,+4b)#*;2<(
		elif PJ break
		elif false break
		elif "'"'"" continue
		elif 28e+53 for wR_ until gm6b by "^"
			var GqN[90.863,50.313,383e+43]
		elif AJ break
		else r7["'"K", true, "L}"] <- false
		hHN(VnC9, n7v, 94.758)
		continue
	end

## 5Vq3Q;lrCz8NH
func OH (var HxFv, string sDq)	return POh7
'''
		expect = '''Error on line 2 col 31: var'''
		self.assertTrue(TestParser.test(input, expect, 933))

	def test_934(self):
		input = '''
func JC ()	return gE_
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 934))

	def test_935(self):
		input = '''
func SK (var h7Rq[9e-71,26E94], var ye2[605,861e+23], string lICr)
	return
string o_c ## o7
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 935))

	def test_936(self):
		input = '''
## {T+Fz8%{dx(RBL7<S
dynamic PG[3.238E85] <- 981e+89 ## 0d101:W
func Tmz (var pCO, var n3)
	begin
		## !m16uA{)?
		## nR^%[ 5Pn0)uyb
	end

string R6r[2.981,55.419,961e+04] <- uG ## %^9X&AAm7d<B~L
'''
		expect = '''Error on line 3 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 936))

	def test_937(self):
		input = '''
## MgnA
func EM1u (string A4b)
	return
string mwMA ## L&
##  t<[ozE$q.<pIR}X@Rr
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 937))

	def test_938(self):
		input = '''
var JZ[66.485E06,900,184.839] <- true ## u9|M0
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 938))

	def test_939(self):
		input = '''
bool oW
func fLy (string ZRH[3,34], string Dn, dynamic DHQN[7.022,31e07])	return
## m
'''
		expect = '''Error on line 3 col 39: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 939))

	def test_940(self):
		input = '''
func Xg (bool q48M[4e37,139.259,24e+98], string vaU5, var aA)	return 1

## zNA5>r9{Wa5iJ!%"Ou~
## hBlxpjSd
'''
		expect = '''Error on line 2 col 54: var'''
		self.assertTrue(TestParser.test(input, expect, 940))

	def test_941(self):
		input = '''
func fq ()
	begin
		if 56.827 break
		else iR2(true)["'" ", 0e-74, "%'"}'"^"] <- Li1R
	end
func LiGs (number eIYk, string iMW)
	return
'''
		expect = '''Error on line 4 col 5: 56.827'''
		self.assertTrue(TestParser.test(input, expect, 941))

	def test_942(self):
		input = '''
number dpH[55.246e-09] <- VOn
func UKCI (var LR, var SkkJ[64E-23,8.562e-56], number eP[802,0e+97,616.334])
	return "9M"
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 942))

	def test_943(self):
		input = '''
## -~
var h3Xo[22.312e-17,106.530] ## %05QzHFMJfAs|SyhAlPU
## .aeH#MHmV/ 
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 943))

	def test_944(self):
		input = '''
var Yd ## 0s2%e<
## 6?Iw i*c,4E
dynamic tj ## p]bQ&x$H2V$<+,+zFt_
func Txi (var ocx, string TCc[139,0,56e73], bool jV)	begin
		## r8!sIxYkv$NA
	end
## ?$
'''
		expect = '''Error on line 2 col 16: 

'''
		self.assertTrue(TestParser.test(input, expect, 944))

	def test_945(self):
		input = '''
## KA>?-bN5j8l@N,0 1V7
func oA (bool i6xs, number LFX[0,31])	return true
number kp ## }og
## `p*
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 945))

	def test_946(self):
		input = '''
func bj3 (dynamic QRR, number gC[89e-85,5e+30,0.826E+10], string fz1N)	return 4.677E+51

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 946))

	def test_947(self):
		input = '''
## 3JV==x5@Rln?eR_
func YTA (var v9[8e+49], string lV[5,2.698], dynamic Ajv)
	return

func LRNj ()
	begin
	end
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 947))

	def test_948(self):
		input = '''
func nR (var qVB[2.612,76], number sS[48e+43,90.224])
	begin
		for nPwf until false by true
			number b6t <- "'"'""
		## lL)
	end

## +48cw4"`
func SJyt (bool yn0)	return "'""
## 3:L0F(Yz2|
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 948))

	def test_949(self):
		input = '''
bool e1[1.149e+60] ## I>v@=IRed5{{["
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 949))

	def test_950(self):
		input = '''
## D:6zyMu9G=*qn6lS~j+
func Xc (bool tOc, bool nl, bool SkXr[515e-08,986E26,6.881E+02])
	return "v"
func KqPI ()	return 8.347
## yA.cWbR,c{YDH=
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 950))

	def test_951(self):
		input = '''
## "uqG,@#[8DX2Q<
dynamic GEg_ <- oG
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 951))

	def test_952(self):
		input = '''
func Efpb ()	return "'"8'""

## a,
func KzI (bool T0[250E63])	begin
		## T) ->T"p?$ie&kK>z,
		if Wx qjiM()
		## )*/YI?I
	end

'''
		expect = '''Error on line 7 col 5: Wx'''
		self.assertTrue(TestParser.test(input, expect, 952))

	def test_953(self):
		input = '''
## L;%S=rR1a;{*Fi"0?yq
func vHqb (var ICE3)	return
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 953))

	def test_954(self):
		input = '''
func nxM (dynamic Ppa, string b2W[29,9,8])	begin
		## @
		YPJ(PU)
		## xc!aogF!}Mt*
	end
func H32Y (bool OV[21,2.831,703], number Pb6[1.461,74.055], string sw97[896e-80,43,124])
	begin
	end

func yJI ()
	return "FS"

## ~
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 954))

	def test_955(self):
		input = '''
## C7
string Xdy <- vL
dynamic a4k ## 5&+;;OT76jLa<
func el (dynamic op[92e+08,17,8.478e-64], var U1, dynamic mgQ[4.626E06])
	return
'''
		expect = '''Error on line 5 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 955))

	def test_956(self):
		input = '''
var H6yN <- false
func Z9 (dynamic WEt7, number hT, bool b1[74.634E+24])	return
var aIf <- XS ## e
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 956))

	def test_957(self):
		input = '''
func Xy ()
	return true

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 957))

	def test_958(self):
		input = '''
string Mez[904.868e-09,914.780,4.200] <- 3E+65
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 958))

	def test_959(self):
		input = '''
func p5Oj (dynamic T6U[5e+99,600e93,18.202e05], dynamic og6)
	begin
		i8("]", 9.623e53)
		break
	end
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 959))

	def test_960(self):
		input = '''
## {VGw/BVf[;Ipb<d
var FQ9e <- true ## GG
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 960))

	def test_961(self):
		input = '''
## l4bV:.D[e
func coe (number SMQz)	return

func mH (string adYw)	return 8E49
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 961))

	def test_962(self):
		input = '''
string bm[2E63,663,4] <- "'"I'"/'"" ## g|?x0?&=xoV
dynamic nTgd
string Kfu[8]
string fpV ## !0
number y4[746.512] <- "K'"o"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 962))

	def test_963(self):
		input = '''
## h2D4V{*6zhE/K5E0
func L47t (number tP)	begin
	end
func mp ()	return "'"AK"

func JP (number QSqd[2e-32,1.612], number KNwm[452.045,477E88], var XV[6E-92,25,700])	return true
'''
		expect = '''Error on line 7 col 64: var'''
		self.assertTrue(TestParser.test(input, expect, 963))

	def test_964(self):
		input = '''
## taP<d&>)
## Y{(xS%Tp",GD,FM>z
## )2v
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 964))

	def test_965(self):
		input = '''
## $
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 965))

	def test_966(self):
		input = '''
dynamic IL04 <- 510 ## X{Eh!Zwyd6kOlOtXD_/2
func Nhz6 (var y6P[97.138], var oYgw[88E-32,3], bool VVI3[0.681,377e-84,40.582])
	return
func F3d ()
	return 271.746E-06
func svjW ()	return "'"v"

func ro (string P3I)
	return
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 966))

	def test_967(self):
		input = '''
## d)[G
var Thkl[35,6.578E-68] <- 85.090
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 967))

	def test_968(self):
		input = '''
## stges DG%?ev6}C}x
func UD2 (var hwL[7.248,611.966], bool tNa[67e91], string QwA[4E-52])
	return Yao

'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 968))

	def test_969(self):
		input = '''
## E4k-X-`OiQyVD~l9Rq:T
dynamic B6 <- true ## ~M_Vr_/MEt]4}S
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 969))

	def test_970(self):
		input = '''
func PL37 (dynamic y9h, number fSB9[402e+68,226.161])	return 333e+61
## G5{F)nrDgL-7e%#
## ]
dynamic S6 ## I2|w:mUR<"O5pQ*{;
func Goj ()
	return "'""
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 970))

	def test_971(self):
		input = '''
## Wz
func rZSE ()
	begin
		break
		for Lf until rfF by N2Q
			gHg(9.051, 1.742e48, RAf)
	end

## 3Hy9sSn1{LDPBh
## B
## ()Z~0k;`&2>{V+
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 971))

	def test_972(self):
		input = '''
string VWp[5] ## 0W++`mF5pZ#iXC@4;UZ
## r~pS|6A
## [B&lhsC<S0SCJ
func rwq ()
	return 143e05
## Iy)dRdeH-.`
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 972))

	def test_973(self):
		input = '''
dynamic gco[9,449e-00,6] <- "dKv'"]" ## Z lRgCOhER4Y{!n%A%Z]
## X!XXj%b
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 973))

	def test_974(self):
		input = '''
func F2Tq ()	return
## X:
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 974))

	def test_975(self):
		input = '''
## .RfT>7m?n{$N^B|@i>gU
number qF <- "'"'"'"" ## NrHnH]qC
bool oc
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 975))

	def test_976(self):
		input = '''
func mU (string Iie)	return true

## -y9s=~%
## $ .iS68G^[UFmHJDV
func G_c2 (bool TUM, number jr)
	return true

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 976))

	def test_977(self):
		input = '''
func ojh5 (number c3J)
	begin
	end

## {|}jrPMxV
number o4BX[48.759,97,81.086e43] <- nG7d ## Am-;77?nAN@l_&Y`Q
## J
dynamic i3no[2,27.666,64.235e-92] ## fjvG{M;m%baf.=
'''
		expect = '''Error on line 9 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 977))

	def test_978(self):
		input = '''
func g6 (bool iap[9,60.174,46E-42], var r9Wy[0.628,6E-46,501.773], var Q_CA[562e-92,4])	begin
		if "bM'"'"" return
		elif s0 for j9x until "`'"-o" by false
			for TDO until "'"'"'"" by "B[o'"f"
				var Dzh[5.085,53e+75] <- 3.835
		elif Ig6 for VBk until "v" by 22E+97
			jM[true, oY, "'"n'"'""] <- true
		DMF["5v", true, true] <- MUNa
		## %38-[dAL,
	end

bool b1Y[41] ## $Wb{E&BHI*lMR.B*#D5
## 7_[JdoytgTjPJo_}D
'''
		expect = '''Error on line 2 col 36: var'''
		self.assertTrue(TestParser.test(input, expect, 978))

	def test_979(self):
		input = '''
func dd (var rAx[133.719e30])	return
number v6 <- true ## f+lrYk:j-=Dz
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 979))

	def test_980(self):
		input = '''
func Ft0 (number xP69, string e0)	return true
## Nn-W7}YN2
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 980))

	def test_981(self):
		input = '''
bool pR[63.481e+69] <- "G" ## ^U
## -.q.&}IK8&
dynamic YEq[8] <- true ## E(uZB- 3zP]W_
number GY1[29.049,2E-16,567] <- false
'''
		expect = '''Error on line 4 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 981))

	def test_982(self):
		input = '''
number rvY <- rpv ## vk9#%Sv*-&EWsC%K
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 982))

	def test_983(self):
		input = '''
func B1 (number ze, dynamic CPn[72.161,85,26.705], number dks)	return
dynamic OKel
'''
		expect = '''Error on line 2 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 983))

	def test_984(self):
		input = '''
## Vhg-cER@:qV$kDV
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 984))

	def test_985(self):
		input = '''
bool a6b <- 51e82 ## #e>.QJhWjx*k G^t0^v
dynamic sM[35.360E37] <- "m'"'"" ## PCN+DpsKWhb
'''
		expect = '''Error on line 3 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 985))

	def test_986(self):
		input = '''
## 4iDvZ#w]q,|~u7|+[8U
dynamic sk_[0]
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 986))

	def test_987(self):
		input = '''
dynamic aRc <- 64
func XXAr (number XDL, string v74, string VSOr[81.200,69,641])	return
## 6RXA(%[
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 987))

	def test_988(self):
		input = '''
## eVrwMu[:M_~[5tzLX@
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 988))

	def test_989(self):
		input = '''
## tEF6M<}G3bhq/w%kNnu
func xZYv ()
	return "'"i'""
## M
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 989))

	def test_990(self):
		input = '''
## e+!~E
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 990))

	def test_991(self):
		input = '''
dynamic n1Bk[78E98,7E81,3.295e-24] <- "'"'"Q" ## 0T= mETb,KmB
dynamic al[312.398,85.479E+54]
bool IRC ## -U4/XqFbp?WHJH0,T
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 991))

	def test_992(self):
		input = '''
## 6r>F[p9
func EL2 (var zDRH[999.199E57])
	return false

func ORAV ()
	begin
	end

func Cs6 ()	return

'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 992))

	def test_993(self):
		input = '''
## ,f"V(e?31=,/mTP
## hIw!|Zj~>_.?Ucx"bX
## A+_kb!bK%xA(bd
## 7fYyMUo%z%hJQSuDih.
'''
		expect = '''Error on line 6 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 993))

	def test_994(self):
		input = '''
var Xr0 <- "}'"|r" ## ; G&(%b#%/F1q
number A7ip[1.955E+11,90.344E17] <- "'""
bool tS[86.199E-01,32] <- kG ## AM-|ZNSY|K@*r]P*r
number BZ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 994))

	def test_995(self):
		input = '''
string ZL[76,79,151e-60] ## ,2|*>yG*_;,q
func NFKd ()	begin
		## {=`:7i(`KIe;%!h_1@mI
		Sz4[">'"'","] <- tga
		UfKN <- true
	end

dynamic i8n[34.062E+56] <- Xwv6 ## C{|d;N3925VHa$dp
'''
		expect = '''Error on line 9 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 995))

	def test_996(self):
		input = '''
## s
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 996))

	def test_997(self):
		input = '''
## PG$&+3:a#h7l@7qq
## =m
func d1 (dynamic kmw, var kw[7.607e+24,252.871,71.791e48], var RjG)
	begin
		if jix begin
			var nqX <- "?iB"
		end
		elif 65.282 begin
			Zn("X*'"wg", uj2, "'"")[0.400] <- fG
		end
		elif L4J5 begin
		end
		else bool KF <- "'"'"'""
		## n76@669H
		CTB()
	end
bool X8yq
'''
		expect = '''Error on line 4 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 997))

	def test_998(self):
		input = '''
var x57P ## [O4@@o)r:ky.
'''
		expect = '''Error on line 2 col 24: 

'''
		self.assertTrue(TestParser.test(input, expect, 998))

	def test_999(self):
		input = '''
func jFj (bool Mr6A, dynamic rfJF[7e65,47E+81,119.519], var fEd[52E+84,9.632E35])
	return
## st>_@O%6
bool NE[7.005,4.903E+64]
'''
		expect = '''Error on line 2 col 21: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 999))

	def test_1000(self):
		input = '''
func cvK1 (number e3aO)	begin
	end
var VDE2[56.429e-98,3E+05]
func vty ()
	return false

'''
		expect = '''Error on line 4 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1000))

	def test_1001(self):
		input = '''
func vWA (dynamic L2N, bool SnR)	return

## %bsS-x7c0MIEFn
bool Ypg[2E76] <- "'""
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1001))

	def test_1002(self):
		input = '''
func Ev (var tc[18], number WZ[868.156,2.815], number O5eS[18.921E-58,182E+43])
	return

## !L$p0r#2}@(?kL@
dynamic yqg ## tGl5Og)#ER! ;&2F{
dynamic oaP[31.901E+76,529,83] ## RF{_d`PU88M/HG`t
## 1"%-kTnPD
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1002))

	def test_1003(self):
		input = '''
func eqZl (string f8OK, string G6[42.932,76.323E+68], bool A228)
	return
## 5 IeJ]rFY_l
## M0`<-YB^"jW
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1003))

	def test_1004(self):
		input = '''
## ~%HeXU;BJoE,z&
## i|h
bool A_F[743.963,61.074E08,8.111]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1004))

	def test_1005(self):
		input = '''
## iTRhcbX3b9I{t9
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1005))

	def test_1006(self):
		input = '''
var Np[945,745E-59] <- 58
func yfq9 (var NaJ, string BTq0)	return

## *gkD3.i]wfeH#t
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1006))

	def test_1007(self):
		input = '''
bool mM[1e-64,92.226,7.366] <- "'"'"D'"'""
## ~;%_b^mz
string SB[3,0.290E+36] <- 13.199 ## pLc32Ty4<+~
var QTl <- cNJG
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1007))

	def test_1008(self):
		input = '''
func wN ()	return P3ct

## hz0
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1008))

	def test_1009(self):
		input = '''
func XYd (number WB, string qj9, bool sCWD)	return false

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1009))

	def test_1010(self):
		input = '''
dynamic Rq ## ]90<r*[C_jTd<xOQ$`
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1010))

	def test_1011(self):
		input = '''
func WKS ()
	begin
		## 3A
		## 9
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1011))

	def test_1012(self):
		input = '''
func K7nl (string cVQA[97e+05,185.869E+85], dynamic X4)	return
number LV6[58.953,39,14.844]
func PHZT ()	begin
		if "'"'"" tD <- false
		elif "." begin
			## */E9Sam(.^[%-3?
		end
		elif "('"]%" return
		elif "'"'"'"" var ySpb[9.206]
		elif 8.364 return 3e-92
		elif false for vKJz until "P'"t" by 4.760
			if NGM dynamic WOTn
			elif true break
			elif 72e13 if "s'"s" for zTtg until 282 by "1'"'"'""
				return
			elif "Xa'"'"" fz(false)[false, ",'"{Y>"] <- 339.236
			elif "'"" W1["'"'"`FR"] <- false
			else SU(false, 0.050)
			elif false return
			elif true number Er2D <- "'"9" ## =I|ON:VU!l4#GONv-eX
			elif JC46 nS <- "'"'"'"'"'""
		else return 18.815E48
	end

func AIkd (string B9z, bool Fu[40e+52], string u_[8.999e+60,18e+38,68])
	begin
	end

## S8-7(^yJjNdMRrJ.dnnB
'''
		expect = '''Error on line 2 col 44: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1012))

	def test_1013(self):
		input = '''
string t7vu[6.342E81]
## n|^m(4o=Ww`$~PY?Z
bool xd <- true
func fqQ (number v9VG[5E80], number i0[288,966.768,3E-97], bool EQ[28e-12,5.918])	begin
		## 2Kl5$k<i(TIX1
		for S6p until true by false
			continue
	end

## >/8?JBl1*u&:Xa! <(
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1013))

	def test_1014(self):
		input = '''
## yS h5<
string al[6.654,7.253,175e-19]
number BZP
string FIo <- "h0'""
## p
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1014))

	def test_1015(self):
		input = '''
var Dokb[6.728E95]
func xRW2 (bool pe[8.164,449.227e-66,79e+14], number jl, var iUGY)	return dKa

func EtH (string N1a, string uF8l)
	begin
	end

'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1015))

	def test_1016(self):
		input = '''
## ;9@*8v%
func q0z0 (number KJ7p)	begin
		continue
		## pyA3#(:{::5";5&J6(8
		begin
			## lku9S"v{^m/,Bw
			string zXhS <- "'"*QA"
		end
	end

bool HwBG[871,289.510,7.666E-91] <- 476.031 ## 0|W;}_0c+=C4-0@>L$0
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1016))

	def test_1017(self):
		input = '''
func ph3 (dynamic iG)	return
## ]DBN3;,Kvr}(1nm.;4x*
func AKHW (bool th[683.541e-63], number ShC[65e-59])
	return
dynamic yIM1[96e26] ## ;LMko/1Y`pR
func zvSW (number jg_P[6])
	return

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1017))

	def test_1018(self):
		input = '''
dynamic YJn
var n1Z <- true ## =T<{Vq&Do.
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1018))

	def test_1019(self):
		input = '''
func Mj (dynamic eF, var SEQg[3,0], number JR[372.413])	begin
	end

## rQ4uY`:G!-]kE3cD;B<
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1019))

	def test_1020(self):
		input = '''
## EU-}y?Mu<A
## KS-7sWVL="NvyK z>)
number UnA ## a/Ut^#?|J&CKiH~DSK,r
func fO (dynamic nv_b[88.344,27e+74,50E-81], dynamic Rib, var op[10.909,83e-45])	return

'''
		expect = '''Error on line 5 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1020))

	def test_1021(self):
		input = '''
## OH[=,#
string E5F <- k0p
func rUP (bool Yf[539e+75,382E12])
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1021))

	def test_1022(self):
		input = '''
dynamic zJ93[368] <- true
## %e9^`)2=a`
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1022))

	def test_1023(self):
		input = '''
func OVG ()	return FR
var T9
'''
		expect = '''Error on line 3 col 6: 

'''
		self.assertTrue(TestParser.test(input, expect, 1023))

	def test_1024(self):
		input = '''
## 3%Egw{vgzIG/IR
## &
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1024))

	def test_1025(self):
		input = '''
bool XcrI[510,9E+90] <- 699 ## 51>/
number CE
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1025))

	def test_1026(self):
		input = '''
## 9MRJ
## R3*a3
## v`.>v
number Sh1[29.939,97,9.655]
func wbd ()	return jJ

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1026))

	def test_1027(self):
		input = '''
## u]SY~
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1027))

	def test_1028(self):
		input = '''
## v;]#
func SW (dynamic UOs[92e62], string u7)
	begin
		if "'""Wv" if "'"'"j" if L6K fn1B[KV, 444] <- false
		elif 8.882 VZQ["'"=", STe0] <- 96e+15
		elif "e" TNi()
		elif 19 x8tx <- "k"
		elif d3 gM()["'"'"G7", 41.127e-45, 417.264] <- CPw
		elif zm CsOR[xqt, false, "'")'"'":"] <- 4.506e88
		elif "'"'"'"" for sB until true by "'"'"'""
			bool SN41 <- lK
		elif 7.770 begin
		end
		elif wWaJ return
		else zH[2, "'":"] <- "'"'"'""
		break
		for danN until 49.307 by cnwZ
			rM(true, FJOo, true)
	end

## 6Y8`F]I6;>
bool G7li[258,574.898,73.770] <- "E=R_" ## ";cPp
'''
		expect = '''Error on line 3 col 9: dynamic'''
		#self.assertTrue(TestParser.test(input, expect, 1028))

	def test_1029(self):
		input = '''
func irn (bool k1[11], bool M2d0, number Z4sO[6E13,751.041e-50,7.264e16])
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1029))

	def test_1030(self):
		input = '''
func Ym41 (string gmbP, number BV)
	begin
		## ca*P=QD&qIt&vi
	end
dynamic swyP <- 7
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1030))

	def test_1031(self):
		input = '''
func DdDf (dynamic ws3U, dynamic AEb)	return 4.938E+80
## }sZ@4g|:l> Z0*
func MD (var XT[81,0.902E31], bool joh2[247])	begin
	end
## tgtU7
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1031))

	def test_1032(self):
		input = '''
## *)J;#:rL-O]ctL<LAi
## xXiW,{_;];K-2
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1032))

	def test_1033(self):
		input = '''
## =_9@h,#r
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1033))

	def test_1034(self):
		input = '''
string x2q ## +-%J5V~/52h)RS0S
## R5oe|9JP
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1034))

	def test_1035(self):
		input = '''
var wMDn[76.126,5.144] <- dx
number It ## 7AroVSlAUZydv&>*Y6e
var wQjd[4E-97,36.498e85,53] <- false ## ~zn*Ac[^v*,=^nz8w
func vo (dynamic P2Q[8,36.806,5.847])	begin
		if 53e+58 break
		elif "'"}'"k" bool kA[5.529e-33,9,4.862E-52]
		elif rL MEk <- "'""
		elif 6 y9j3(536E-50, "'"", true)
		else continue
	end
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1035))

	def test_1036(self):
		input = '''
func yC1U (bool BbQS, var W9z6[6], bool WqP[77.580,70.884,814e+59])	begin
		## m]da~r
	end
## =w*lB3rg=tJn!y{.%o
## QfUh-&!GD!.rn41
var I7m
'''
		expect = '''Error on line 2 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 1036))

	def test_1037(self):
		input = '''
func Z7gf (number Y9i, number MFD)	return 8E+40
func UiAm (dynamic rGK_, string BvQ[879.190e+53,5.218])
	return

## xM [lP rS<
func oRW (var RM[69E56,1.005e+22,50.451], var qAg, var RZ5[682e-57])	begin
		## @
	end
## M<?MzEWBwW50Ct
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1037))

	def test_1038(self):
		input = '''
## b{Q
## M4h SRG8M
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1038))

	def test_1039(self):
		input = '''
## 6.9kq p f1:
dynamic vg7A[0E86] ## A%[>[=Tyi)Ll M15}y
func n8x4 (number W81z, number m7)	return
## 3"bRtml@Q@pu+BQwTM-
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1039))

	def test_1040(self):
		input = '''
## qty/dQUt
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1040))

	def test_1041(self):
		input = '''
var TrqS[65.472,463.149] ## n=-!@i%Ak+vn"zF%
## ,C7BSauo
## Ef_
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1041))

	def test_1042(self):
		input = '''
bool pV[8e-92]
## f
func pbK (dynamic Vr[9.490E44], dynamic Q7r[6.372e+76])	begin
		return "'""
	end

'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1042))

	def test_1043(self):
		input = '''
func mxT (bool V0P[2.517e02,16.357,27e-78])
	return ae22

string pOV ## Ov(jIia3/~:%JF
string Km <- "'"" ## 7&0Gnh,TQb7UD
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1043))

	def test_1044(self):
		input = '''
bool zi3[18.311,84.132E66,960.827] <- "5" ## noe?
bool ggtx[5,704.981E-65,40.652] <- rfM8 ## Q)]u2h+NdBJw]9(HK./z
bool HTj <- 66.148
## z|@uxLTj%9%
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1044))

	def test_1045(self):
		input = '''
func IK ()
	begin
		break
		wXi(685.400)
	end

dynamic uR1[8,59e68]
func ytyx (bool nfDK[991.512], number RT, bool UqG)	return true
## {]Q~a*M!:/
'''
		expect = '''Error on line 8 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1045))

	def test_1046(self):
		input = '''
func ph1e (var i8j, var Dm_8[276,471E+48], number Jvz)	return 16E09
func EDmv (var L0k[1,4.455])
	return true

func LdO (dynamic Kdht, string Zf[987.412])	begin
		var LoK[707e+25]
	end

'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1046))

	def test_1047(self):
		input = '''
dynamic oGC <- false
func XL4 (var ABpP[1.618], bool c2c, string ltg[737.913])	return

bool IvJa[197.261]
var p3 <- false
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1047))

	def test_1048(self):
		input = '''
number xK[5E+94,20E-63,1e+89]
## :}G>{oTd`YqVeMo/2
func ghvX (var tmlh[5.413,0.362,8.608], var uJ3g, number L2g)	begin
		return
		## sqah_
	end

bool unbj[7.637E25]
'''
		expect = '''Error on line 4 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1048))

	def test_1049(self):
		input = '''
func jA (number nv[165.001], dynamic JA[0.900e+14,992.402e+38], bool tDbM[49E+79,1e-31])	return

string UhW[88.004]
## (jpM/Q*:
## b{03341WI%|=|J
'''
		expect = '''Error on line 2 col 29: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1049))

	def test_1050(self):
		input = '''
string o1I[48.233,997E-69,830.512E+38] ## p`x6gDbw|Vb&UV
func sI ()	return
func dJ (bool gT[0e28,37e84,35.828E56], string LYAm[1.925E-95,3,4.149e62])
	return
string AG9[410.084] <- hw ## c&TeAd4N
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1050))

	def test_1051(self):
		input = '''
## )?cBxW(
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1051))

	def test_1052(self):
		input = '''
dynamic KuuW[149]
## eF3{SL6dx0
func Dfpo ()
	return ZM

bool Ko82[63] <- "*%'"4'"" ## dq^e(D-QTTCw/@tr0l
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1052))

	def test_1053(self):
		input = '''
## -d/{z<kV+#9w
## :[4A8fEyyS7,bmuu
var fkFU <- false
func rJhr (var Ls9M[68.938,26])
	return Db8

func LoWo (string ft)	return "'""
'''
		expect = '''Error on line 5 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1053))

	def test_1054(self):
		input = '''
## %kpV,2Gr
func tcy5 (bool sL, number PxvP, number OCQ)	begin
		Wr <- "'"'""
	end

## M
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1054))

	def test_1055(self):
		input = '''
string t4wf ## ;8&LF{?Rsfv3&{
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1055))

	def test_1056(self):
		input = '''
## qz,81ry>MexmA-6x@4
func n6s (var fIT[84.319E+82], string zu, number Yd6)
	return u_
## _
## %@R$j/R2;r<*c
func Uon (dynamic Ey)
	return true
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1056))

	def test_1057(self):
		input = '''
func F2p (number bcM, bool Cw[827.848,25,6e+77])
	begin
		begin
			begin
				kWm <- true
				## YWHe}
			end
			Pci()
		end
		return
	end

bool udKC[5,4E-96] <- "M'"'"$u" ## nsq
bool DJ ## ?hJ`i)+J0
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1057))

	def test_1058(self):
		input = '''
number hPg[65,8.944]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1058))

	def test_1059(self):
		input = '''
dynamic N6bf[872e51,8.137e+89,3]
## "2;o[SOJ
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1059))

	def test_1060(self):
		input = '''
bool CSn
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1060))

	def test_1061(self):
		input = '''
string gVrd[6] ## ;Rkl
## 9-,N_x_}]=hf1b5_o
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1061))

	def test_1062(self):
		input = '''
func nlY (bool tght, string aE[450])	return true
bool i147[23e-77,522.289,156E+38]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1062))

	def test_1063(self):
		input = '''
dynamic TPT ## >+X`oA#30ecI
func eds ()
	return true
func SN (string Rs0, number Ei9T, dynamic XmO)	begin
		for Eg1 until 248.270 by false
			break
		## t
	end
'''
		expect = '''Error on line 5 col 34: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1063))

	def test_1064(self):
		input = '''
func fr (bool lhJm)
	return
number c4rt <- 858.356 ## KQ#.v
var yk[138,43.460e-75,86.319] <- 6 ## Emlqby]>Qn1/zTGjS.
bool sDb <- oqXY ## 3%YbN_<us&*rsnMh`[2*
## nDTP+7sRM?lTo!Ww%u
'''
		expect = '''Error on line 5 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1064))

	def test_1065(self):
		input = '''
func XtvB (string zIeD[944])	return 5.606E-91
## QX"}qm@*^t{FgHmvQ
func zAD (var f0[590], dynamic j1Jr[7.769])
	return AVs

'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1065))

	def test_1066(self):
		input = '''
number THxy
string tm
bool Rp[676] <- 4.714e24
func sOP (var UCu8, dynamic dfs)	return false
func S0gA (number NwHk[0E-93], bool qonH[9.884e02,9])
	return
'''
		expect = '''Error on line 5 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1066))

	def test_1067(self):
		input = '''
func HQvV ()
	return oSH

bool pL <- "'":" ## `M99d.;:+<qLdRsF`m
func NiWv ()
	return

## :Qk
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1067))

	def test_1068(self):
		input = '''
## 5L$TgV4Y|@x/eH4x
func Hc ()	return Kg

## r].}pX[l"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1068))

	def test_1069(self):
		input = '''
string tG
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1069))

	def test_1070(self):
		input = '''
bool idpy ## ,
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1070))

	def test_1071(self):
		input = '''
bool Jfq[0.713E+72] ## W-z*vx-P<)[ &"=)jt
var whWk <- false
dynamic Wg[465.571,989.278e+85] <- 9e-12 ## "mm
'''
		expect = '''Error on line 4 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1071))

	def test_1072(self):
		input = '''
dynamic gC[6.935,768,40] <- true
func kvO (var RIf9[93.222e+18,4])	return 77

## 5%_Tir76yOXY
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1072))

	def test_1073(self):
		input = '''
## vvnfdOmM<q(]}
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1073))

	def test_1074(self):
		input = '''
dynamic Mg[90E+92,361.203,3.790] ## g3nI
string Pl[3.162E10,35,0e+69] ## -o.xb@@SG@+hDefNr>
func sb (bool XDQi)
	return true
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1074))

	def test_1075(self):
		input = '''
func qCI (number HF[7.245,4E60], dynamic zY[891.850], bool zIp0)	begin
		for pMP until "'"'"" by true
			string tA[936.019] <- false
		break
	end

func BU (dynamic gy0, bool E6, number E9qg)	return 0.481
'''
		expect = '''Error on line 2 col 33: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1075))

	def test_1076(self):
		input = '''
## :tnbQ6|zHGpv481QJag
number Ba3 <- "'"'"" ## ;
## %I(?Oy9mI
func gULu (var mA, string cbvb, dynamic c7P)
	return dW
'''
		expect = '''Error on line 5 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1076))

	def test_1077(self):
		input = '''
##  +m@NH
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1077))

	def test_1078(self):
		input = '''
## F|D=T#=
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1078))

	def test_1079(self):
		input = '''
func NGI (dynamic nW, bool nE9U[5.424E92,61.962E12], bool g8b[406e41,33.583,58.026])
	return
## 2;=/ %,YQ
## #x+ (`>`-b+]g>VChA
func kWF ()
	begin
		begin
			## .}qurfv&![Yzl4~VWv
		end
		## =A15V 5dP`~{
		return
	end

func PtTN ()
	return
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1079))

	def test_1080(self):
		input = '''
## Fy)@Fs
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1080))

	def test_1081(self):
		input = '''
## -VRTBh#i2G,mRx`esl
## CmWrE9uB
number Dn <- "'"z"
func yTMM ()	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1081))

	def test_1082(self):
		input = '''
var wBnW <- "!"
bool DrA[66.712E33,390] ## yKdu
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1082))

	def test_1083(self):
		input = '''
func Adj6 ()
	begin
		q8n("'"_'"", true, I2_)
		break
		## {.&4b2l.YB=R ?
	end

func xsL (dynamic rl, number zp6, string gj[57.569E-52])
	return

number efyw[2e18,40.857,51.693]
'''
		expect = '''Error on line 9 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1083))

	def test_1084(self):
		input = '''
func W2L (number xN[21E-16,23.698e+10], string Pr[3.145E82])
	return false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1084))

	def test_1085(self):
		input = '''
## (Y/dAD/)h,)`
## _01C:/~;[>CxhX^bd+U
number bm[994.938,9e+36]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1085))

	def test_1086(self):
		input = '''
## lsw P
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1086))

	def test_1087(self):
		input = '''
## <(A4~B}
bool Rq[0,53E38,30.565]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1087))

	def test_1088(self):
		input = '''
## P2ZrP2NyENKY-!
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1088))

	def test_1089(self):
		input = '''
## R: /M{l&C
func I2 (var DlD[890.657,37.715E+09], number vLD[5.324e59,39e79,1], dynamic XEI[123.738e-46,6.846,267])	return 184.589
## MYt
func Gv (number hV8[572.751,4.363,924.824])	begin
		## +
	end
## anNQzJ~4"M
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1089))

	def test_1090(self):
		input = '''
bool VOJ[5,18e-39] ## P,&?9=?
## >[Bd#]t<b<XP
func PALU (bool aVQ[18.157])
	return "u'""J'""

number HeZ5[92] <- "vuD$" ## 8)h
func Qi (bool Htz4[527.892e-39,4e-06,2])	return

'''
		expect = '''\''''
		self.assertTrue(TestParser.test(input, expect, 1090))

	def test_1091(self):
		input = '''
bool N1jr[0E+80,986.510e-50,73.949e77] <- hG
var Ze9K[4]
func bEK (bool ryVD, dynamic GG[28.396,5,12.696])	return

bool Qu
func Oba (bool sP[0,703,340E+07], var AN[0], var rL2)	begin
		## q6l,[
		if true if "'"'"'"o'"" begin
			## )Pz
			## f,3H?#PUgpfj_>UU(
		end
		elif false if 372.838 return
		elif true number rA ## sh1;3[Y I I!St
		elif "'"$A" return
		else pVRb()
		elif "b)" begin
			## jF
			## =+D7r0o)j[A(GXT
			## lnMj=96{9^Gq7)nD
		end
		else for od until "^" by false
			Vh_ <- qy
	end

'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1091))

	def test_1092(self):
		input = '''
func n_k ()
	return zU
func sg (var O5Rr[623.511,9], number uHO, var xf[140e-98])
	return

func CDIC (number i1, string FK, bool IC)	return
'''
		expect = '''Error on line 4 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1092))

	def test_1093(self):
		input = '''
dynamic Xx0 <- false ## -"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1093))

	def test_1094(self):
		input = '''
## .VDmcM>j
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1094))

	def test_1095(self):
		input = '''
## cGR"ue9Bn`usHL
func yWcg (string Nv0, string UC[42], number s6[631E+35,7,89.884E99])	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1095))

	def test_1096(self):
		input = '''
number y0vr[66,3e+30,612E-29] ## 7~&_
func mY (bool n4sJ[44.709E+72,16], string nyJP)
	begin
		## <"a1Nr?T5+e
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1096))

	def test_1097(self):
		input = '''
func oQ8 (bool tnlg, var rl[2.218E-58,8])	return

'''
		expect = '''Error on line 2 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 1097))

	def test_1098(self):
		input = '''
## i0D <jjhITaW
## r*3QabpN_-i8`z
## $p
func nL ()	begin
		## AS#8|Ve8fO;(U_>}2;d9
		begin
			## %)5&q1Ops~B)P$xMN2
			## u`P%lUzei
			## Q
		end
	end

func KGlG (var Uh[398.552E+75])	return "'"zB'""

'''
		expect = '''Error on line 14 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1098))

	def test_1099(self):
		input = '''
## F5IJmI9
## Z)N@jSGl7
dynamic qU[468]
func bpV (bool bqFf[22.765,44.280,98.621e61], number gfke)
	return "9'"'"'""

func SqV (bool kiN3[99.592,8E-32,9.468], var tCF, string nhu[42.658,782.440E53])
	begin
		begin
			## ]>
			## m
		end
	end

'''
		expect = '''Error on line 4 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1099))

