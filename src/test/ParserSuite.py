import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_600(self):
		input = '''
func VlSt (dynamic xg[74.463E+41,0], string BFkW, bool CD)
	return - [GB1R(["@'".3u"])[rL, QN5C], "B", false] == 582

string gkg9 <- o2t
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 600))

	def test_601(self):
		input = '''
func ZA3 ()	return

func at (string EZ, number zpJo, dynamic U9)
	begin
		break
		## b"y.o(1dJ
		uE()
	end
func u9Iy (string tmC[54], number QecL[3E-85], bool Eb)
	return k2R

'''
		expect = '''Error on line 4 col 33: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 601))

	def test_602(self):
		input = '''
bool Gb ## RA J?VT=IAa Qu
func fzuG (var mWG)	return true

func RNfJ (number DQi[73,938.665], dynamic oJ[7], var R0[0E21,73.561e-03])
	return
dynamic W4T[431.357e-48] <- 6.127e14
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 602))

	def test_603(self):
		input = '''
string xO[61.780e89,95.983]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 603))

	def test_604(self):
		input = '''
bool W_ <- false ## i,BqxKUuc"N]Q+
func XLD (number nPci[54.084])
	return 4.468E+04

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 604))

	def test_605(self):
		input = '''
func UN (number Vmu[438E+73,17.071])
	begin
		begin
			break
			## K+*T%4)v2^,g@hCZ
		end
		## l(3.{fAUE+jp
		for eZ until 9E-79 by "3'"'""
			continue
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 605))

	def test_606(self):
		input = '''
## U=&rCQ9i2(,ZcU
func q297 (number x4hi, bool ha)	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 606))

	def test_607(self):
		input = '''
string YX
var QQ
func KSDe ()
	return

'''
		expect = '''Error on line 3 col 6: 
'''
		self.assertTrue(TestParser.test(input, expect, 607))

	def test_608(self):
		input = '''
func VG ()
	return

func CB ()	return

var Vdt <- oL ## O%{sB[}E>+0Yxbl]bU
var ClkE
'''
		expect = '''Error on line 8 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 608))

	def test_609(self):
		input = '''
func hE (dynamic vY5w[752,440,383.698], bool mP[507e57])
	return
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 609))

	def test_610(self):
		input = '''
## p+{qd*87OFtFA
dynamic gFcX[4.949E-55] <- "x'"'"B" ## /`
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 610))

	def test_611(self):
		input = '''
var IGzm
string us7 <- 115.275
func y3xT ()
	begin
		## 1hR3
		## 9Jrz4ro,N&$k+`@9<w7-
	end
string noC[576.539,85.714E+55] <- "L'"'"u'"" ## GOTl|oBoH
string mt <- "m'"'"" ## xgle|F2B5H
'''
		expect = '''Error on line 2 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 611))

	def test_612(self):
		input = '''
bool RZpL[442.138E80,927E-81,64E02] <- false ## z8R1clTV..E
## K,(n
## 5=EQwIF
bool s1qh ## v[a`Qk
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 612))

	def test_613(self):
		input = '''
## ]1}b8M|xPLmgNe:l?.g|
## 4w0
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 613))

	def test_614(self):
		input = '''
func hh9 (bool uY[9,200.685,56.172e-77], number iVl[1.729E+64,82E-12,0.706])	return 583.890E-62
## 1pPo.YNfvCh
func xIWU (var Rsk, bool ux, string YrO7[36.364E99,1E-54])	begin
		## FW+rW
		break
	end
'''
		expect = '''Error on line 4 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 614))

	def test_615(self):
		input = '''
dynamic qdxh <- yP
## oAE^8
## pq%af7ns*9ie)D{5X:K%
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 615))

	def test_616(self):
		input = '''
func D9v (bool z3j[759.517], var YoP[5e+02,6])	return
'''
		expect = '''Error on line 2 col 29: var'''
		self.assertTrue(TestParser.test(input, expect, 616))

	def test_617(self):
		input = '''
## 5#Sp
number oUo5
func nz (number de)
	begin
	end
number MH[766.575,47.198E-70] <- false
dynamic WNHP
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 617))

	def test_618(self):
		input = '''
number Xn[576E-36] ## 0jnMaXSCV@M
var jm0w[91e-11] ## AY+ h^7sB;wTq:)([
## *+7wN9dFvLig//
var BJZ
bool LLj[9.256,730e23] ## 9lQ~5p@9NU
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 618))

	def test_619(self):
		input = '''
## NI4XF2qGLHq|H/9#T
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 619))

	def test_620(self):
		input = '''
## mA7uVX8XzfKo#|C>$j
## Bs.}-}qd+h+uD]FPiD<k
## #
bool xW[26e+20,5,9]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 620))

	def test_621(self):
		input = '''
## >v.-w~~bq3ri[9,]|5b
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 621))

	def test_622(self):
		input = '''
number P9
## 2)t8.
## ;)YI#~x(7FE0PW^
bool fLN <- P4zh ## j)t
string zs <- UruW ## kxy^;3DJ4Z4mtl*"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 622))

	def test_623(self):
		input = '''
var nUF[2.542,64.712E+86] ## @
## .7*ZWP{n].5M1j
number qpJ <- "'"" ## <8Dh5>!>El?4TuAmgj
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 623))

	def test_624(self):
		input = '''
bool iV1i[86,5E96,6.715] ## ~d.}3uJ_?F
bool tm ## t~5#w+)k7]VFy
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 624))

	def test_625(self):
		input = '''
## v"KR@g
## H)Q3Q4nuPr-8
## @i4c2 
## "M jE!|.Mq]:Z5
string hDEE[85.388e-63]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 625))

	def test_626(self):
		input = '''
var HCrB[2E-56] <- "'"'"'""
dynamic Dnn ## NL)8_&DA=lIXcGq1t"D
number sB6k
## ex.@
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 626))

	def test_627(self):
		input = '''
dynamic ygJ[1.319]
bool g_L ## <kDS{,~_] a7} Zkl7"
## ]D}o^{A;8Fci>Oa
## jGOliD[SwY-8}
bool Ev[653] ## U;~(Tudj"WME=
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 627))

	def test_628(self):
		input = '''
func xF49 (var g61, dynamic lOY[751e60,63.341E69])
	begin
		k4(cb1)
		oL("zT'"L", aYII)
	end
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 628))

	def test_629(self):
		input = '''
func ob (var Gw[4,8])	return
func EUZf (string KXh, number zOc)	return vFt
## ..d]sgL.mI=
var JtN <- false ## o+G`V]p[$H)W%
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 629))

	def test_630(self):
		input = '''
func ns (dynamic h4uU[896e-61], var iU, dynamic SV[4.814,38])	return
## ?N~eEFl2E??Hps2:
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 630))

	def test_631(self):
		input = '''
## S_Z[^rR#gs hca
## cogxoeR}!YnL:s
func ye ()	return

func wd (dynamic lZBe, bool li9H, var Bt)
	begin
		break
		break
		## ji=8ZlE/Caq;
	end
bool Fcf[1.789,93.520,9] <- false
'''
		expect = '''Error on line 6 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 631))

	def test_632(self):
		input = '''
func zO48 (dynamic BMyX[1])	begin
		## UL|$e@H_i9P2IzJ
	end

'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 632))

	def test_633(self):
		input = '''
number pc <- false ## y+|.d3y,UZY
number br[419.124e-85,758E+15,2]
## 3@;94v.~L:*P&t6-5.
## HHBCO|gk>D2v8@@9~s
var aq ## W:sN"sl<Xm
'''
		expect = '''Error on line 6 col 20: 
'''
		self.assertTrue(TestParser.test(input, expect, 633))

	def test_634(self):
		input = '''
## l3f$.p[g/Xb
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 634))

	def test_635(self):
		input = '''
func dPL ()
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 635))

	def test_636(self):
		input = '''
func un8u ()
	return ":e'""

dynamic oi7E[689e+16,42e37] ## !wLi9A97Q2F|J
func HJ ()
	return "'">L"
## fJF?K0
'''
		expect = '''Error on line 5 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 636))

	def test_637(self):
		input = '''
func ZW8 (number HC)
	return mil

func FMjG ()
	return

string p5A1[9.998,365E-78]
## L<mu~v{~
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 637))

	def test_638(self):
		input = '''
var be <- "!""
## g
## KAo3M~/cdf
'''
		expect = ''''''
		self.assertTrue(TestParser.test(input, expect, 638))

	def test_639(self):
		input = '''
## Q?IaM9OfwP(8LYn
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 639))

	def test_640(self):
		input = '''
## {@,wK
number qgJ[946,4e34,274e25] ## nJy2Tr|hdfW`;Q
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 640))

	def test_641(self):
		input = '''
func FCF (string lFM)
	return false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 641))

	def test_642(self):
		input = '''
bool PZbz[213,557.370E+87,943e-79] ## OHBauLIs|6#J[l Syn q
func N1Lj (bool ApLQ)	return true

## T@N}~P`n$
func JU (number xyKv[159.617,670.525,13.502E-74], number O2Je[448,9.714,4e-03], bool tI[94E89,865e-29,4.767])	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 642))

	def test_643(self):
		input = '''
## Mm&U
## .h@ss
dynamic JS
## 1MAlY1+
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 643))

	def test_644(self):
		input = '''
string XX8 <- "s4ye" ## ,iA31r};kj<J]zp+[v;
## Pt@ZHt%uhK
func zrK (dynamic mQe, var RTO, var h2)
	return

'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 644))

	def test_645(self):
		input = '''
func eIu ()
	return ja

bool O491[42.096,69,7] <- false ## ~!KbX7k*]3X%}(GC
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 645))

	def test_646(self):
		input = '''
func PQKK (dynamic p3W[672.218,1e-24,47.216], dynamic dO[227e+73], dynamic ln)	begin
		## -Re*d*
		dhNJ <- ZdP9
		## i^v}p,+_pEX
	end

string WF4[84.718,99.644E+44] <- false ## jUv0N!*zd1"
bool Rez <- false ## 3vg(:^/Z3jgK%=Y
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 646))

	def test_647(self):
		input = '''
func Evm ()
	return
## f T]7YLq]p
bool HpK[6E+88,4,785] ## g6+Dao,WAJ&dr.j
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 647))

	def test_648(self):
		input = '''
number oW <- kl ## G5T.<VxZ(wEUgR`)za%t
## q*6v7vAzO*j R2
## :%$21H1|]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 648))

	def test_649(self):
		input = '''
bool wOqR
bool aro ## J5g.]HQO
func RZn (string hw, bool y7)
	return false
var Y1
'''
		expect = '''Error on line 6 col 6: 
'''
		self.assertTrue(TestParser.test(input, expect, 649))

	def test_650(self):
		input = '''
## f/pe?AF
number s5e[0.570,352e72] <- 40.859
## #hQG;aacM-
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 650))

	def test_651(self):
		input = '''
## [$
bool EN7j[87,1]
## Ct&IAT^YQ~d-
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 651))

	def test_652(self):
		input = '''
number ldM
bool CRv <- "_='"K"
func ur (number gy[70,204E+91,95], string r2[4.115E-38], bool rNB)	begin
		## =gptl
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 652))

	def test_653(self):
		input = '''
bool PWCC <- gBNf
var hAoS <- true
func PFzT (bool DtRn[971e+68,1E47,532e+04])
	return
dynamic fr3J[262E-42]
func SPDc (var UJsR[45], string Fw6e[41e+64,2,32.616])	return

'''
		expect = '''Error on line 6 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 653))

	def test_654(self):
		input = '''
func pIsW (var LqE[53.484E+97], bool MU[4.635E36], var IzP)
	return 50E+23
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 654))

	def test_655(self):
		input = '''
string d8ks[5.094,1E93]
## MoV8<C0!Y!U
bool CL
## lN*=L7
## PPQdD
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 655))

	def test_656(self):
		input = '''
## B
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 656))

	def test_657(self):
		input = '''
## $8CyUB^> zST
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 657))

	def test_658(self):
		input = '''
dynamic FaLc
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 658))

	def test_659(self):
		input = '''
## ;?D;ya^>[<Tf+>k3V~
func U7Qs (dynamic QOs[3E+09])	return
func HDT (var nVt, number sE, number V2[59,292.009e66,960])	return "'"]'"i!"

## :1Qf@.RHl2f
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 659))

	def test_660(self):
		input = '''
number VO7u <- pCBY
## l:r K
func j1 (bool rlg2)
	begin
		## }H!@A
		for xioU until "'"xlb" by 1
			if 9E37 for mR until Q8 by yX
				if 21 for VCHU until true by 951.995
					t00E[Sk] <- "'"'"R"
				elif 863 qS4I(true, 9)
				elif "'"'"j=Q" return
				elif 667 continue
				elif 19 continue
				else return
			elif "," pCO(sGu3, false)
			elif false h0D("/'"'"3T")[false, "Bg'"'"", "'"8'""] <- false
			elif 15.845 IiE <- Alv
			elif "sEh" break
			else number UtL6[67e+56,9.246,7]
		## ~/7KHdc43I)q-Z
	end
number si
func s7 (var dC, string aGxj[770,7,4.761E56])
	return 76
'''
		expect = '''Error on line 8 col 6: 9E37'''
		self.assertTrue(TestParser.test(input, expect, 660))

	def test_661(self):
		input = '''
func MW (number fX[572,61.993,14.924])
	return "(-"

var JYfc[27.844e+89,61] <- false ## 4RMl)lz7KWPBU0
## czY.(gXj(WW`kpR_`c
'''
		expect = '''Error on line 5 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 661))

	def test_662(self):
		input = '''
## .S 0FOvDrKj
func ZW ()
	begin
	end
bool unWV[4.759e-05,9.778e37,234.716]
var h0[24.173] <- "R'""
func C9j (number P4[3.942E-28,100,60.493], var sQke[99e+55])
	return

'''
		expect = '''Error on line 7 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 662))

	def test_663(self):
		input = '''
dynamic WR5 <- 254.178e-53
## z6v,Z%}c*
func qZrK ()
	return

func sY ()
	begin
	end
## S3NNtq
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 663))

	def test_664(self):
		input = '''
dynamic UPi[6E+74,5,6.365e01]
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 664))

	def test_665(self):
		input = '''
## $f_w:euXHXz;V~Q)f
## *2}e,:z;e~mxH dW^QlP
number Jew <- VFL
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 665))

	def test_666(self):
		input = '''
## v<[w(0$=la
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 666))

	def test_667(self):
		input = '''
dynamic l4 <- 39.631 ## a]"&o35xX0k Ez"L9
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 667))

	def test_668(self):
		input = '''
func Cf (bool HEr, bool wSDR[58], var WQr[5,0])	return
string uNP <- 9.369 ## WJ}Y|Rz4I$3N|f8-U
bool FSf6[0.531E-34] ## ]eLP]
'''
		expect = '''Error on line 2 col 34: var'''
		self.assertTrue(TestParser.test(input, expect, 668))

	def test_669(self):
		input = '''
func UiS ()	return

func lHMu (dynamic H_0l[87.573e-47,5e48,993.577e+43])	return AXN
'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 669))

	def test_670(self):
		input = '''
## ^kwrtPdGu55s(^Gtco
func lVun ()
	return true

## 5o,<qWHwHWcam
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 670))

	def test_671(self):
		input = '''
number AxKI ## 4
func CDJ1 (string nErn[63E-99])
	return 38.834

string YVk0 ## N9.WJGu`&7M
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 671))

	def test_672(self):
		input = '''
## ~b#B
func MJAq (dynamic tw9[290,4.549], dynamic OtV)	return

func d9XP (string RenA[3e96])	return

func nZBE (var M9[72.135], var YFd)	return true

'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 672))

	def test_673(self):
		input = '''
## ;QvZGCF Q#Fi37my
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 673))

	def test_674(self):
		input = '''
dynamic rufb[20E+07,1.274e+80,3e-04]
## 9,cA4;4x
## **"
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 674))

	def test_675(self):
		input = '''
dynamic qPrk[88E-92,63.064e48] <- "'"'"'"'""
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 675))

	def test_676(self):
		input = '''
var LY4h[583E-47,96.591e+63,891.869] ## NLy1jfrqXg4+
string o6[54e-75,5.715,6.091e99]
bool Qvk[60,51e37] ## <QKuiy_
func k1K (string Yz)
	begin
		return Hy
		## >5j~g(cKAl>]`zJC9h&
		## g
	end

var zyS[89.769E+02]
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 676))

	def test_677(self):
		input = '''
## c?><L3
func ixu (dynamic Mv)	return
var xYa[7.896E-62] ## %?"B|TZa_A*
func RSk ()	return false

var qHfR <- "!e'"n'"" ## f8*^SL_dm3i
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 677))

	def test_678(self):
		input = '''
## {Q2OC=z2qK?
dynamic H9At
##  7m:=sP|,wDV:(`9pedD
func Ufy (string Kd60[3e+50])	return false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 678))

	def test_679(self):
		input = '''
bool dx[19.183E+63] ## n[^RT3"QGmnwR%dH(z
func Sfs (var c3G0[145.647e-72,44E+71,2])	return
bool Kg <- true
## u7&]GH!
## kr8+g
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 679))

	def test_680(self):
		input = '''
string EghB <- "'":'""
func MK8y (number S8FW[830e-92], string vs[7.521E+42], dynamic bwAp[81.422])
	begin
		begin
			## JAqDe
			for cLZ6 until 188.638 by "RPZ)r"
				for URYJ until jFH by "'"=z"
					kI("9'")'"")
			## )dC?>5FpSzZP_
		end
	end

func UR (number TPi[331.315e+81,83,235.979e93], number WyX)
	return

'''
		expect = '''Error on line 3 col 55: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 680))

	def test_681(self):
		input = '''
number FE5D <- sWiV
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 681))

	def test_682(self):
		input = '''
string Tfl
string GPv <- 7E38
bool rA
func aNCH ()	begin
		begin
			## X6m{g>8PjUV
		end
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 682))

	def test_683(self):
		input = '''
func qM ()	return
dynamic mH_u ## sePdGME=Mx--O2/;R
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 683))

	def test_684(self):
		input = '''
func CoV (var DWF, dynamic FZOn[49])	return
## Df2D,DWfhc>},
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 684))

	def test_685(self):
		input = '''
dynamic CVd[72.702,253e+09]
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 685))

	def test_686(self):
		input = '''
var SPL[2E+42,330] <- NoX
func Da (dynamic KU5)
	return

bool QWs[7E+59,115.092e+92]
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 686))

	def test_687(self):
		input = '''
func TH (var pXvv, bool flQm)	begin
	end
var VW37 ## DIuPD*&K#U~+L28CL5G+
## dH*fX
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 687))

	def test_688(self):
		input = '''
## EN/0a&
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 688))

	def test_689(self):
		input = '''
## -
## J/;?7*8
dynamic mUmy
string Zq4[4.702e17]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 689))

	def test_690(self):
		input = '''
string bv5N[3e-50] ## J
func OT (string aLoc[650.011e91,72.050E18,680], number kp)
	return
number mekD[82.442e+97,52.057,1] <- "4u" ## UC5*5K{pphw
bool FD <- false
## qlvhj~O3V~9@"v]|q}
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 690))

	def test_691(self):
		input = '''
## ]AjahnF
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 691))

	def test_692(self):
		input = '''
number aB ## {gR+_0
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 692))

	def test_693(self):
		input = '''
## wOQ}YB
string RDQs[7e+44,0E02] <- false ## ^P>(pQv@j]!6K5
## lL=b$zg:8-R6*dWs W;
func lYd (bool Qwfr[6.311], number Tsz)	return ZeG

string bP6D <- gck
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 693))

	def test_694(self):
		input = '''
bool l8g[26.757,943.039E46,687E20] <- "'"J'"5"
## !}^&,+`;(
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 694))

	def test_695(self):
		input = '''
## BOfP~*QwUolv
## C3-K{9
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 695))

	def test_696(self):
		input = '''
## f4RhaU[
## L2b_FEp
string UMJw[7E08,85,49e+25] <- "'"kJ"
number Jqz[49.815E-17,4E-08,73] ## T]u>VO-i
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 696))

	def test_697(self):
		input = '''
## Pn_ok<nNgkZ]h0
var Tq <- zV
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 697))

	def test_698(self):
		input = '''
number BKk[8.491e+78,9E-50] <- iso7 ## UJ0UkhEG*^Q
func rF8 ()	return 4e+26
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 698))

	def test_699(self):
		input = '''
bool pnt[647,6.337E+57] <- "'"'";'""
func VAV (var uuP3, bool is1, bool omxp[3E98,979E37])
	return 4.364
func DpfN ()	return true

bool CvD[364E+12,3.215,338E97] ## w_ulsf_
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 699))

	def test_700(self):
		input = '''
func P4s (dynamic sQj, string oGH)	begin
		continue
	end

## p*
## 9@s+c}g
number l9[544e-97,7,89] <- 397E+75 ## xU0AAa*i
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 700))

	def test_701(self):
		input = '''
number HUy
dynamic u_1_[108] <- 77.008E28 ## 8}(3(X
string uKGc
func JtF (string po, var Fk[0.626], number Nr7y)
	return
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 701))

	def test_702(self):
		input = '''
number WWuK[76.760E48,5e+94,407.948] <- "i'"]" ## x5Ym>4+
number ks ## y(AR650gD
func gK ()	return R8O

dynamic WaSq[51E11,38.035E+32,8] <- itW ## cxbu;e6xf7vwXZLs?wVV
var i7vR <- 769.325
'''
		expect = '''Error on line 6 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 702))

	def test_703(self):
		input = '''
func p8 (var II5r[40e32], var zYYc[0e+42,598.015,9])
	return 928.631E-11
string Hu7F[1,67.567] <- true ## h:#BLMYg_s8hX
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 703))

	def test_704(self):
		input = '''
dynamic wtKS <- RP03
## 8TG^#
## xAivUgDP:{xSMW
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 704))

	def test_705(self):
		input = '''
string ol <- eR ## v6r|,O&U~rB@e?
func yuj (string q2[25E+89,48e54,4.059e85])
	return 154
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 705))

	def test_706(self):
		input = '''
## K%tq
## iW3zZ~!gqE53!HJR 
## NQi|P%vbg<r$ah#
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 706))

	def test_707(self):
		input = '''
## {#j1 sr^o{6r<G$
func wd (dynamic RYh[6,692E-54])	return dP
func Bv (bool u8Y5, number t753)	return
func XcV ()
	begin
	end
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 707))

	def test_708(self):
		input = '''
bool Xkc <- true
func Amjb (dynamic uF, number J4VW[9.452E+17], var Nkji[8E32,988.103E+56,6.431])
	return "I'"'"'"'""
func wet (number sm[6.702E+40,31,75e73])	return

number t_E ## =N#
## x
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 708))

	def test_709(self):
		input = '''
## m/g$}BjnQ33d
number s2AO <- false
## X!
##  ~uwSSQjb
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 709))

	def test_710(self):
		input = '''
## !#Iz
func ceA (bool ddU[43e36], bool T5z[870.115e66,79.725,39.337], bool ne)	begin
		## 0se2
		## I`i 9g)sAMMH>!5F`l9o
		if Vh number dbL[953.617E44,600.282] ## fw3g95"
		elif 998E47 break
		elif false H4("U", DZ)
		elif SbFh bool IK ## ![qO7D<_z$"c7^(1vY6n
		else if "M'"69" begin
		end
	end
'''
		expect = '''Error on line 6 col 5: Vh'''
		self.assertTrue(TestParser.test(input, expect, 710))

	def test_711(self):
		input = '''
dynamic ujm9 <- "["
number gC[62.488] <- 5
func MR2 ()	begin
		## #uT?7Nx}C
		CmM(4.207E-62, 708.631E-15, E9)
		## =M;o
	end
## l/
bool Wr_S[50e09] ## b/(3B({g+ G"10d!|
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 711))

	def test_712(self):
		input = '''
## n6% ;m)<%&9q(I]LS1[
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 712))

	def test_713(self):
		input = '''
string xZF <- false ## ?KtEckv`_dMm;}5.
var wH6[854] <- 9.952E-70 ## $)HL}M}+RS=?/<@K1>C
## H+USD%/<7d,S;#E$18
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 713))

	def test_714(self):
		input = '''
dynamic u3[7.336,953e+02,58.079e-46]
number bVd[1E-57,6.069,75e22] <- false
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 714))

	def test_715(self):
		input = '''
bool fDz ## .kN&7"
## bw_xt
number pvJi[860,505.516,60.070e-47] ## 4@lnn
## ITe!
var X6b8[0E-40,246E32] <- vQjB ## 5
'''
		expect = '''Error on line 6 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 715))

	def test_716(self):
		input = '''
func PZQ (var sj[608,75E+80], var sgy[6,14e98,387E-57])
	begin
		## ,+swDM2C
		begin
			## I9;m&/N#qX*
			MsY(true, y_o)
			if 124.407e-76 for KSl until true by wv
				continue
			elif false if Hamd for wNGc until false by "'"'"'"^"
				number UK[884.803]
			elif "'"'"'"'"" dynamic FRM[202,308e-42] <- "'"3'"" ## "68+!h(R,@]
			elif "'"'"'"" break
			else return
			elif EsPE continue
		end
	end
func QCZ (bool kbg[923,702.206E-61,725E+73], bool hQlp)	begin
		## d&$C&PfO~&^w
		## G3
		## yph=Kl{s#k<<R~^
	end

func Z_l0 (number AMHy[82.365E43])	return

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 716))

	def test_717(self):
		input = '''
## g!PPo8MgL)1
##  ;#i%qNY~/vr[
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 717))

	def test_718(self):
		input = '''
## yO
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 718))

	def test_719(self):
		input = '''
string rxzj ## zS5Z0.Ns_F%#rk{m
dynamic rn[3] <- 371.627 ## |moRP  z#2<>xXN40A;j
'''
		expect = '''Error on line 3 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 719))

	def test_720(self):
		input = '''
## AFUH+
string afZ[2.133E-78,2e+37,92] <- "@g'"0&" ## <rS(bp0jpO/=M,E[
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 720))

	def test_721(self):
		input = '''
func xT9 (dynamic kY6M[6,612], string zK_, number Wy4[0.502,2.290])	return
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 721))

	def test_722(self):
		input = '''
func BKg4 (number W8V[13.477], number EE0[8.680,63,24.655e77], string q6x)
	return

number zlVT ## Lp$t4"{
func wAe (string nkw, var IDZc, string pz6)	return 217

'''
		expect = '''Error on line 6 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 722))

	def test_723(self):
		input = '''
string TGei <- "B'"I`'"" ## +R$iP2
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 723))

	def test_724(self):
		input = '''
func N9Jk (dynamic yU[7e-87,6e-16], string azm[5.896E-33,29.703])	return
number tg6[21E74] <- DO
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 724))

	def test_725(self):
		input = '''
func n6AC (string xtq)
	return
func DcS (bool h1, dynamic SgI)
	begin
		## /@
	end

## Sh
'''
		expect = '''Error on line 4 col 19: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 725))

	def test_726(self):
		input = '''
var hPb <- true
var Uzx ## f<6Y#6bh?J
string AaN7[218.915,26e-29] <- "='"'"'"4"
'''
		expect = '''Error on line 3 col 21: 
'''
		self.assertTrue(TestParser.test(input, expect, 726))

	def test_727(self):
		input = '''
func q0f (var m1E, number dn2[0E-82,9.722e+43])	return zQG

## vk/~1b67y6jyTwb
## |}Bv|
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 727))

	def test_728(self):
		input = '''
var IaM3 <- "'"'"'"'""
dynamic G0[5.456e68] ## X 
var DuAI[7.380] ## p-wK:Ui6w&
##  L"JgvIyz-_L:y=U
string pOx[4.303e-81,57.838E92,27e-96]
'''
		expect = '''Error on line 3 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 728))

	def test_729(self):
		input = '''
func Nf8 (dynamic ga, string ptI[0.726], dynamic M8d)
	return false

func ruO (var wx[7e-46], dynamic Ul1)	begin
	end
## F=a2a^*U
func FgZ4 (bool KZY5, dynamic urP)
	begin
		## CXM8ds{
		break
		if "/G" if I6k if z_4 wMM()[true, cpZC] <- B3e
		elif "%'"" dynamic PtjM[7e+80]
		elif false continue
		elif 521.724 continue
		else return 9
		elif false for steh until 9.530 by DFi2
			zC(false)
		elif true continue
		elif 1 begin
			## uO#,|h~ev
			## by~gS#W,
		end
		elif true iXj()
		elif false string yS5 <- 71.721
		else begin
			for SVx until obfG by "+'"H'""
				continue
			##  2%GSw23yoLl"B9=}3W
		end
	end
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 729))

	def test_730(self):
		input = '''
func Cs (string MY, string D8[391.318,63e+70], dynamic f8i[713.878E-08,59.628E-01])
	begin
	end
func bVQu ()	return
## 1Y_,Pa&t?1A>pPIouq
## Df#H2GV
## 5%|M3hd
'''
		expect = '''Error on line 2 col 47: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 730))

	def test_731(self):
		input = '''
## Dp=p?,u`l{69 C,r3Hy
func BpCp (dynamic Nb, var OSgq[427])	begin
		return false
		begin
			## $h4~,1q6$Er!8a!
		end
	end

var WSCe[5.125,93E+88]
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 731))

	def test_732(self):
		input = '''
## VTC|LaY
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 732))

	def test_733(self):
		input = '''
func b43s ()	return 7e+72
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 733))

	def test_734(self):
		input = '''
var wn
func o7R (string ji7[4e+00,3,98.753E69], dynamic Oxv, var y7_[58.580,9e27,494])
	return PbK

## +.)J[H
func P_N ()
	return
func zcAy (number DG, number tq7k, bool Ry[4.690,11])	begin
		## kU2XrE
	end
'''
		expect = '''Error on line 2 col 6: 
'''
		self.assertTrue(TestParser.test(input, expect, 734))

	def test_735(self):
		input = '''
## o[3W
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 735))

	def test_736(self):
		input = '''
func LBGC (number CE, dynamic X8_[2E13,673.426,8e11], bool P5)	return 89.474

'''
		expect = '''Error on line 2 col 22: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 736))

	def test_737(self):
		input = '''
## va,cNq..m]#4[4><3[
## Tf};=
func PKf (dynamic x3[11e+23,939.902])	return

func o2PM (var ycp[8.001E-30], bool Kia_[1.519,189.720e-45], number pSi)
	begin
	end
'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 737))

	def test_738(self):
		input = '''
## R-4VymZXQ09`I 
func sdg (dynamic aRwc[5,893.839], dynamic W9)	begin
		rj(true)
		if true string Xk[7]
		elif false XL(niak)
		elif geyB hu()["Fasrb", 51] <- true
		elif "+'"UEd" begin
			## L WQBZ@Ab9O
		end
		elif "'"'"S" gg("'"yO'"", 86.115, oi)
		else continue
	end
func pXv (bool kw)
	return

func Ld ()
	return 1E71
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 738))

	def test_739(self):
		input = '''
## M|7#I/G@+ugK9
func es (number WEBQ)
	return KJ
func efU (string n3, bool IC, var Nu)	return PJ
## J#^KlVWI
## D/>A;.|W
'''
		expect = '''Error on line 5 col 30: var'''
		self.assertTrue(TestParser.test(input, expect, 739))

	def test_740(self):
		input = '''
## JoV WnX
func qXnR (bool XK, number s8S4, dynamic D9[446,312.486e-92,208.582])	begin
	end
'''
		expect = '''Error on line 3 col 33: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 740))

	def test_741(self):
		input = '''
func sQT7 ()
	return "h~"
func yyc (var VU[51.185e-95], bool Dy3r, string PTOw)	return false
func Di (bool YokZ[733,399e76,1e24], number SfU[4,578])	begin
		## yX6xP7Z
	end
string YP_B[5.237,10.451e-59,67.523E-28] <- true
func Co (number FtSi[135.577e78,82.392])
	return "'"'":"
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 741))

	def test_742(self):
		input = '''
string CRGY[4.124,78E-65,880.362] <- phu
func DEo (number iKu, string gBT1[64.589e-83,2.811E+28,528.155], number nV)	begin
		begin
			return
		end
		Uy["wi'"r", "A>G"] <- "h"
		for u1o until lS1j by true
			continue
	end
number Foc <- "'"='"dz"
## UhYWbT9
dynamic HWtn[70.642] ## ZoDYkw3mu
'''
		expect = '''Error on line 13 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 742))

	def test_743(self):
		input = '''
func tC (var Hx0[152.661e81,4,39E-42], string cB[951e-97,6.137,53.626E+54], number on8[22e-98,50.979e-27,168.134e-36])	begin
		begin
			## 0^)%"zec}K`|o
			## 9Xvgtn@C"jiu2#i8ED
		end
		## RFq
	end

func Kpbu (dynamic cezY)	return 65E65

func a6q3 (dynamic B78s, bool SS[763.567,85e+07], var uUH)	return

'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 743))

	def test_744(self):
		input = '''
## fAG
## TJGu`QV$%L2L
bool qffD[545,64.571e+22]
## <qb
## JBGR
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 744))

	def test_745(self):
		input = '''
func Rsh ()
	return
func Jwn (var dFB, number EhDb[24,6.040E+95,493], bool ZQO[904E83,603.802,18.936])
	begin
		## 5ByL N
	end
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 745))

	def test_746(self):
		input = '''
## +;J~wHy ^3hQ{z^1{
## `ISWw4QE!
var F598[540e38,2.793e22,0.162]
var AmAV[85.420e+39,81] ## 6njDnGu(a
'''
		expect = '''Error on line 4 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 746))

	def test_747(self):
		input = '''
## clIUa<GMc
## vu|SK)n+^+*(3qt*
func T6N (bool yjo, string Dwe)	return false

## %VlEg>+_EQ~rc4
## f05=@Ak}&
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 747))

	def test_748(self):
		input = '''
func I_qw (var M8)	return

dynamic nGE[332.541] <- 73
## k>ar
## AcGGn
func nW ()	return
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 748))

	def test_749(self):
		input = '''
## F,oK|9<glKu/yJW&R
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 749))

	def test_750(self):
		input = '''
## "?<s5Bx)( k;G28z!
## Rql}
number pNP
func UV ()
	return

bool nRc[30E-58] <- 4.105
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 750))

	def test_751(self):
		input = '''
func NTs (dynamic Jr)
	return 132
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 751))

	def test_752(self):
		input = '''
var tFFe[7,174] ##  
## [-0SEg|4T]WO!dOn
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 752))

	def test_753(self):
		input = '''
func WG (string vaE, string M_[369.362,3.985], bool SA[883e77,91,239])
	begin
		## BM32]aep(#_5=4*Car
		for oUqH until 46.020E12 by pkwz
			E4("'"'"'"", MH_, false)
		## lcO
	end
bool krJo[74,508,636E-22] <- 18.630 ## aKLAunh
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 753))

	def test_754(self):
		input = '''
dynamic XXE[3.722,0.093,884] ## EYxdQC
func sTND (var eJ[35], bool Bq, bool GsP[12.312,34.863])	return azA
func e8 (string UHc3[2E+88])
	return true
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 754))

	def test_755(self):
		input = '''
## f@f6
func oaZd (number vKd[1,2E-07,4], string H_x3[2,9e-65,34])
	return

number kTQg ## @P[&n/xxcQ
func HXE (number UO, number WDB5)	begin
		bool BQA <- 80.098 ## )I3M
		for Gn_j until "'"g" by false
			N2("H'"", false)
		break
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 755))

	def test_756(self):
		input = '''
string ghhN[2E-38,75.382E-55] ## Fp.0Xu|1ba/X
bool gD[6.233,79.354,193E62] <- EYDt ## #ovvI
bool Fs <- cp2
string HbP[2,312.365,4.483E+08] <- M2U
dynamic GXcF
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 756))

	def test_757(self):
		input = '''
func ysu_ (bool EJ[69e-25,466.371,311], var rz[33,61.991e-51,5.103], dynamic xxvQ[0E60,37e-96])
	return q5u
func m9G (string LilB[5E+27,6e40,5e-37])	return "'""
'''
		expect = '''Error on line 2 col 40: var'''
		self.assertTrue(TestParser.test(input, expect, 757))

	def test_758(self):
		input = '''
func QCC (bool YJ[930.127E75])	return ZT8
func mM ()	return "('""

func HX (bool Ta)
	begin
		return
		## a0Y~u7|d*T^bhZ
		## aOA)v/Al~
	end

## G1tth53!-JRfr5#Jr
func QTw (string SB[56.502], dynamic TZ)
	return true

'''
		expect = '''Error on line 13 col 29: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 758))

	def test_759(self):
		input = '''
string ut[41e+97,44.697,37.995]
var Jt <- Jqsm ## DM}R#0S?E*3cFrcZUO
dynamic fo ## 3S!Co`;cG0bVC}"RG
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 759))

	def test_760(self):
		input = '''
## ;*|w+nCx(t2];YyA=
dynamic TTQ <- cnPt ## Lcs
## Nj0(2BG[rW9CmL9m%pmU
## SD:q)!
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 760))

	def test_761(self):
		input = '''
## ]d?~f(T6m
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 761))

	def test_762(self):
		input = '''
func BSF (dynamic Rj)
	return "F'"md'""
var RV[6.798,265E+57,56] <- 3e18
func QQ ()	begin
		continue
		if false break
		DY_M <- 96
	end
## MR$$A,3Aq
dynamic n4D <- xlh ## tVG{pV<az+
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 762))

	def test_763(self):
		input = '''
number AuoG <- rd ## e
func uiR (number kybv, var DX4B, string itG)	begin
	end

'''
		expect = '''Error on line 3 col 23: var'''
		self.assertTrue(TestParser.test(input, expect, 763))

	def test_764(self):
		input = '''
dynamic hKqg[657.530E38,23.533,84.206] <- "+A&d" ## {Yo,YGc`?;#;3dK#M
dynamic Ey7a[19,0] <- HFT ## ASp%<SUjPrJ~])
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 764))

	def test_765(self):
		input = '''
## Y2@]byqqc)"g)5IvX
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 765))

	def test_766(self):
		input = '''
var DmCq[373,69.814,605]
func wn (dynamic Ua[7], string Jo)	return
string fSs[878,807.391,45.476E+07] <- 12
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 766))

	def test_767(self):
		input = '''
dynamic vy[7,879,46.533] ## l/6t(BYDe- FkA
number eVJ <- "'"" ## 7^0oZ
func bXX ()	begin
		var X2DD[754.966E+38,520E38,4.588] ## 4lbq@~(p:%uG@U)o
		## _.,Ht-{vNmbVHLWMg>bg
		ITE()
	end
## GNITp) gFL=
func qfZ0 ()	return false

'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 767))

	def test_768(self):
		input = '''
var lwkK[415.222,208E08,7.366]
number zKx
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 768))

	def test_769(self):
		input = '''
bool HG ## HrL{*:gr]{5IPyqjt~
## j=Q<)dM!
func UeG ()
	return "zf"
func rUpc (number fR[8.158,22.129,73.531], dynamic wxF[883.054e+12,149e19,282e13], bool Hp)
	return XVSF

'''
		expect = '''Error on line 6 col 43: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 769))

	def test_770(self):
		input = '''
var HbM[7.799E+05,8.315E-39] <- bg
bool dI <- "'"T'"'""
bool Ez[886.166e-08,25e+35]
number KC
string VrN[321E09,6.419E+33,72.969]
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 770))

	def test_771(self):
		input = '''
func yl ()	return false
func TO9 (number LZXO, var nDd)
	begin
	end

'''
		expect = '''Error on line 3 col 23: var'''
		self.assertTrue(TestParser.test(input, expect, 771))

	def test_772(self):
		input = '''
string ECV1 ## hmLXi@n ]oW10U&]+s]p
## ,(v3uWk]y1MQ)
func Su9 (var yoU[8.014,1E-57,6.330E59])
	begin
		continue
		## ;Y?bV)9]E
	end
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 772))

	def test_773(self):
		input = '''
var Smz
number fOw[88.035] <- "F" ## 9&
func YUj ()	begin
	end
'''
		expect = '''Error on line 2 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 773))

	def test_774(self):
		input = '''
string GrL <- 13.251 ## OgYQDf$
var TQAz[43] <- ax5 ## "apW3v{0
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 774))

	def test_775(self):
		input = '''
string g32U[71E+34,0.856] ## wO/R-,/nP,Y`#LN
dynamic NiT[528e82,5e92] ## 5*o8Z
bool tu ## W.r8jW
## [} $W_gY5U%f{T%
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 775))

	def test_776(self):
		input = '''
dynamic Ba
func DQwQ (string TgDS)
	return uA

## >>*
## -w1/mp8u
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 776))

	def test_777(self):
		input = '''
bool Ctw <- "U'"'"'"M"
number ga6 ## 1iI^k]c5Gy3Jj:V8hKG
## *ZAv"gM/`SNs><(SUNv
##  k]Pj 
func xYtu (dynamic u9qs, string LFsX[466E38,2.283,13], dynamic NA)
	begin
		break
		## J>w[m*,<R+iQ7!zs1-:6
		## cNqDq0w3|2X.[<I:
	end
'''
		expect = '''Error on line 6 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 777))

	def test_778(self):
		input = '''
func ZOK (dynamic oh, string Eehk, number jH[493.561e15,17.034E-29,806.197E+16])	return mwhl
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 778))

	def test_779(self):
		input = '''
func iEgK (dynamic Tw)
	return

number gc[2,0.950E-45,156] <- y1
var JA[28,920e64,701.803] <- 58.318e09 ## 0
dynamic yuug[188.570E-97,11.178e-39,48.304]
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 779))

	def test_780(self):
		input = '''
## 4n2
## 2(AKh(O.O+"
## gSJLL<2s/a~D4Gy4*~
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 780))

	def test_781(self):
		input = '''
func eZ7p ()	begin
	end
number Kp <- true
number Q8zD <- true ## k|>J}
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 781))

	def test_782(self):
		input = '''
dynamic Mv ## x=k*
func Biz (dynamic pqt7)	begin
	end
dynamic aq ## .$}!4^~az-,;Cbi[*a*l
string oJME <- vf ## 6Aw}5G-Ja$OQ
func Du (var u_3q, string EDpi)	begin
		break
	end
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 782))

	def test_783(self):
		input = '''
## %jcFc:.8r
func U5 (bool v7[315.889e89,67e45,4], number Pk, string lf[6])
	begin
	end

## a~.|
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 783))

	def test_784(self):
		input = '''
var wPc <- true
## =uP.2J$p&E)SQ#HtvJ 
func dHE (dynamic ff[6,56.845e00,67.707e+85])	return

'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 784))

	def test_785(self):
		input = '''
func iy (bool HC[0,2])	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 785))

	def test_786(self):
		input = '''
func LV (bool SXj2, dynamic og)
	return

string Gxk[1e-22,3,2e+91] <- false ## eW}p6-2n(
func AXyB ()	return

string Gk4e[57.995]
'''
		expect = '''Error on line 2 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 786))

	def test_787(self):
		input = '''
## ^+HC ZU4kT0wAHQz
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 787))

	def test_788(self):
		input = '''
bool J8Jm
dynamic h9 <- "'"Dj"
string lI[854.908E+35,5.706] <- "N'"'"'"" ## >()j0Aj#_3qE
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 788))

	def test_789(self):
		input = '''
bool yah[992]
func kd (dynamic pg, string wOAh[920,2.677,9.902])
	return "'"p"
bool WY[202E84] ## vJoPwo
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 789))

	def test_790(self):
		input = '''
func AKt (bool z4oE[523e-37])
	return vt3

func WBkv ()	begin
		## Z9;;%KLi5
	end
dynamic A_ <- 1.511 ## nrGd 5x
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 790))

	def test_791(self):
		input = '''
## |g~*vZ>T8i=4YO
func ty (bool MoF, dynamic xFDX, bool IHrh[187.812E-52,39,1e81])
	return AG
func Mi (dynamic V3, var RXIS, var PV)	return 9.438

'''
		expect = '''Error on line 3 col 19: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 791))

	def test_792(self):
		input = '''
## JK
string Bgw[4.282e-30,49.011]
var WM5z[9.799E59] <- false
'''
		expect = '''Error on line 4 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 792))

	def test_793(self):
		input = '''
string tRrE <- oN
func nf (var tx)
	return OrZE
## Rh6[qX!u$>q|2zY|
func e7ZA (dynamic ED[6E+39], bool zQQ_)
	begin
		## X`)7`G
	end
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 793))

	def test_794(self):
		input = '''
func NM (string tqnU, var T9L[34])
	return KJ

## (Oy .M;!
func qbu (dynamic o4q[135,5e51], string md, number OPP[552E+27,33.087,68.227])	return false
## ^nv%Tj#u`Gw^dd8Y)RC2
'''
		expect = '''Error on line 2 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 794))

	def test_795(self):
		input = '''
var smRM[0E+00,494.856e41,65e-95] ## ;+W@
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 795))

	def test_796(self):
		input = '''
func Ax (dynamic tY23[3e+82,107.135e-01,2], dynamic zpEM, bool Tsl4)	return

bool A7D[0.967,56.276e43]
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 796))

	def test_797(self):
		input = '''
## Eeq|[C
string eoc[498,8,8] <- UKmg ## [9B}de
number U_[792.698,767,974.466] <- false
## cj
## w^m"/apxF*
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 797))

	def test_798(self):
		input = '''
dynamic Zgu[53.783,53.432,7E+88] <- 20.257 ## @7b"?#3YL
func rSwQ (dynamic Ki[2], string bd1[5,71.411], string XeS)
	return POv
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 798))

	def test_799(self):
		input = '''
## cs=jm
func CIiK (bool zS6[77.692E80,24])
	begin
		for mS9 until 681.059E+61 by De
			continue
	end

## YUGsjU[wl{t,=8?.49"}
## k,&uH(K(1$hA
## tYsf
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 799))

	def test_800(self):
		input = '''
number dq8[6,0.738,84]
func Vu (bool Ew[23.016])	return
## K:0"
## .x`>
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 800))

	def test_801(self):
		input = '''
func IB (string YKX, bool guD)	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 801))

	def test_802(self):
		input = '''
## s{"zipeSVL
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 802))

	def test_803(self):
		input = '''
## 0_xY=4sp{9d"Vw
func Y5 (dynamic fJjg[92,1.739e+50,153e+12])
	begin
		## )-91>:p?j`6nFZ#
		string DQ2[57.477e44,25.738,7.534e+35] <- true ## L@.O|:WM2
	end

'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 803))

	def test_804(self):
		input = '''
number Eq[134,2E+99,45e-39] <- ";"
func bT (dynamic TKy[167,8.137,4e-10])	return 5.830e-34
## 4^&
func KCUw (number H7[29.713])	return PlB
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 804))

	def test_805(self):
		input = '''
func RFRB ()	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 805))

	def test_806(self):
		input = '''
var ebP[537e-90] ## 3
dynamic tqt[859.184,189.711] <- 98.021e21
var E8
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 806))

	def test_807(self):
		input = '''
string dUzW[653e+66,40,0E-89]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 807))

	def test_808(self):
		input = '''
var qIPS
func g9 ()	return

## K1NYUr<jc5z(wKD
number wa[649.409,73E49] <- false
func QQS ()
	return

'''
		expect = '''Error on line 2 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 808))

	def test_809(self):
		input = '''
## V@
func sdDz ()
	return

func NMsD (number GQQ, string w1[54.711E+15,315,32.942E32])	return LN2b
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 809))

	def test_810(self):
		input = '''
## !k3&||Gjmt4%x@;I_u./
var GW4m[57e+47,9.383E-91,231.253e-05] <- true ## XF2)78=ua[Nw
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 810))

	def test_811(self):
		input = '''
bool TMxp[380,0.753] ## 5.Qvc}6ZAU%+"On
dynamic qEL[93.498,750.229]
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 811))

	def test_812(self):
		input = '''
## 7xbf
## cmBl{FdTQ
func n0j ()	begin
	end

## H6
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 812))

	def test_813(self):
		input = '''
func SdL (number nEeg, string Jar5)	return

## |
## >S6Mbi=G-k8K+k{
var CwU <- 10E+29 ## 3]729&R8UA
number tY
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 813))

	def test_814(self):
		input = '''
dynamic ksV[0.653,477.653,2] ## w!QEU!$U-m&Y(BH
func Hq (string ZrVw, string cfB)
	begin
		REj8(299.001E+50, "Y'"'"", "'"L'"")
		## F}}
	end

'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 814))

	def test_815(self):
		input = '''
dynamic Vn <- XWX
func or ()	begin
		string eCy[5.561e-81]
		for K7lZ until 50.527 by yeLI
			bool txm7 <- Rp1 ## ~aE`2rIl>0pVy 
		## B[hsR`+=C,25PHST
	end
## c,j1~a{BP12P
## Z7+ m5-JY 3p[p!"
'''
		expect = '''Error on line 3 col 5: or'''
		self.assertTrue(TestParser.test(input, expect, 815))

	def test_816(self):
		input = '''
string Ncd[297.599] <- 0.300 ## &A^ B#,hzU&*>H3V?pb&
var rn <- true ## aXHm
string zNtW
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 816))

	def test_817(self):
		input = '''
bool spog
## bC3&:TxI<f+o"B2u5B 
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 817))

	def test_818(self):
		input = '''
func nRGg (dynamic rU[7E60])
	begin
	end

dynamic SUu[78.512,519.950,18.163E14] ## ~RU}+ze^,)C"cCV$
## e4T8)kYQo-@}RF{d$"|
string cHG ## ,SvGa
## XV8DC@3x$=.5.pH#}*Kh
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 818))

	def test_819(self):
		input = '''
func HIu (string Z9, dynamic iY)
	return

number pbZh[293.976,338.251,7.150E-68] ## [nfz
func IdU1 ()	begin
		break
	end
func wWt ()	return

'''
		expect = '''Error on line 2 col 21: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 819))

	def test_820(self):
		input = '''
## &JS$bu<`Q2Imt
## U9e.]6C;V"N_Hj$5Ul*1
## %`sN>&L
number gT ## :sxG6[=&,W)qR1[.1
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 820))

	def test_821(self):
		input = '''
number EpYn ## <I^PcYiAqt|
func l0 (number Dt[598.190e-28])
	return "'"'"F!"

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 821))

	def test_822(self):
		input = '''
number dzYb[0.604,6e53]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 822))

	def test_823(self):
		input = '''
dynamic AY0 <- true ## VtCidIu
func GX ()	return

func oh (bool nFct, number Bw3)	return true

func wJBK (var ygbv, bool KE[7])	return
## kF_U^FU>prJ:%|jx
'''
		expect = '''Error on line 7 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 823))

	def test_824(self):
		input = '''
number r2Z[3e-09,8.252e30,4] <- B9Gt ## xxiH
## =C(W%9"}TM:/<{t)5Oa
func t_7 (dynamic s7[91.926,313,73E-37])	return
'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 824))

	def test_825(self):
		input = '''
func QlJ (var gra8)	return "'"'"'"h'""

## F,~Dttl6l@e`Ji0b{H2Q
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 825))

	def test_826(self):
		input = '''
## D96ZM:AIF/?8
func HP ()	return 539.583
func lL ()	return 1.308
func Rd ()
	begin
		VYJZ[54.019E-22] <- false
	end

## %]fV$lv=;nPR
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 826))

	def test_827(self):
		input = '''
func vcc (dynamic klR[404,74e+00], number tFWw, var EIi[386,4.234,711.367e-48])	return
## F9Ifr6;2qG8QIW*P=_
## @@indK]um$X
## d
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 827))

	def test_828(self):
		input = '''
var rR <- 81 ## uVh1V^
func pBVB (bool JP[99.904], string YDS)	return "r'"SC"
## LhV!Ok! 8$p5m
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 828))

	def test_829(self):
		input = '''
## &heep$RTfWu8sYI
func x80x (var nvux)	begin
	end
var Z5D <- false
## HO-CWGa
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 829))

	def test_830(self):
		input = '''
bool TwP ## ^r%XCe
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 830))

	def test_831(self):
		input = '''
## "A%8Y_9wRU)Zs
var TFXQ ## /& x^)
func Da (number Qu[0.692e+53,57E-70,997.492E+16], var FuF)	begin
		return Wm
		for vsc until "C" by true
			if "*'"'"'"'"" continue
			elif true ug <- true
			elif "_'"'"c" dynamic fQcH[266.974E-80] ## v[
		break
	end

'''
		expect = '''Error on line 3 col 18: 
'''
		self.assertTrue(TestParser.test(input, expect, 831))

	def test_832(self):
		input = '''
func NB0 (number xkK[12.004,193,22E33])	begin
		## pqsaa1"1
	end

func Sp8 (string MM[7.311], number xP, var T4[78e+00,275])	begin
		return true
		## aess;
		continue
	end

var D2kx[55E-25,3.881,59] <- bs2J
string Fg[509] ## (|vf[a(*cQ
## Ro5t7
'''
		expect = '''Error on line 6 col 39: var'''
		self.assertTrue(TestParser.test(input, expect, 832))

	def test_833(self):
		input = '''
func lz7 (dynamic KS, dynamic TXd[508E31,75.941,153E-20])	return

func XDl (var btBW[8.716E05], bool v8sD, var A_)	return
func MU (number Y1g[360.725E-08,37e68,7.641e+95], bool q8ZM[2.491E-22,59.700e-21], string GK)
	return

dynamic Zm[8]
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 833))

	def test_834(self):
		input = '''
func EIk ()
	return "HN'"'""

var gDwW[76.319E46,5.909] <- false
'''
		expect = '''Error on line 5 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 834))

	def test_835(self):
		input = '''
var fi[10,102E-25] ## U.7K/fKn}q
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 835))

	def test_836(self):
		input = '''
## 7<OL!
## &uS|!}
dynamic x3Y[4.473E+74] <- true
'''
		expect = '''Error on line 4 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 836))

	def test_837(self):
		input = '''
func GpC (var XdXK[40e-35,83], string eLrA)	return
func zz (dynamic Lkoj[981.197], var DUF)
	return "vB*8"
func O4e ()
	begin
		## ` -"%%EUB
		if K6k4 jEL <- false
		elif fpTU m6_K <- "O8x"
		elif 1.094E72 dynamic eLX <- false
		elif 40 begin
			## Qhu3ba""=37y-2PnO)4
			## f!s
		end
		elif 53.744e77 if 283E+30 break
		elif 31e73 U4(true)
		elif "'"'"" break
		elif false nkR(926)
		return
	end
var EWVL ## TB#0eEX=G:mJ>
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 837))

	def test_838(self):
		input = '''
number rG <- "'""
bool vVjZ[6.299,91.603,96E85]
bool FE <- "56" ## XQ@ZXYthn,e tZ)6]
## I[QEb:%"#f/6b(L1)[A(
func LF ()
	return "#'"p'"F"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 838))

	def test_839(self):
		input = '''
func CBOg (string Rh)
	begin
		## .>~<-yTs<gabj
		return
		## Nb<O
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 839))

	def test_840(self):
		input = '''
## o?u*)0i`" Ng/IG8
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 840))

	def test_841(self):
		input = '''
## Vcv-JW{I&
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 841))

	def test_842(self):
		input = '''
## n{ v%{3C}r&ZMNw_!CRf
## Dt;Xy6)EL]"
dynamic GH <- true ## oOtz!80NE5VY)Pl1
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 842))

	def test_843(self):
		input = '''
func uho (var MqmF[845.767,7.666], var tny, var dZ2[562E-12])	begin
		break
		mpU[false] <- 1
	end
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 843))

	def test_844(self):
		input = '''
## w|Rj
## 2T -m
var nCr[0] <- "'"q'"_M"
'''
		expect = '''Error on line 4 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 844))

	def test_845(self):
		input = '''
func G2 ()	return

## SQ{/Z
## Nhg@FCRvZ[gkdK
var pCK <- true ## osqyv)cj(T-$Z7-2-E
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 845))

	def test_846(self):
		input = '''
bool Yj[156E-87]
## =
bool RUt4 <- true ## EI]}
## < :rE""2J
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 846))

	def test_847(self):
		input = '''
func Zx (number cT, var Id17[77.061,6], string k6I[77])
	return "'"'""
var Pec <- false
## } Ml#69$dLPq{{Mh^vwi
## cV
'''
		expect = '''Error on line 2 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 847))

	def test_848(self):
		input = '''
dynamic N0y[38.979e00,46.855e37,67e+12]
func qmPu ()	begin
		## ,#X{O@5+WnrdXg` _Yj
		## [z0bB(Y?SBGo3
		## ?TDuz@H>_2:q+bSp
	end

'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 848))

	def test_849(self):
		input = '''
dynamic pR[209,7]
func ThKC (number NRr9[9E+90,85], number uh4[27.033E+66,932,3.085E+04], dynamic Sh2P[65e61,31.392,3.527])
	return true
number PmV[2E+12] <- T96
dynamic aa[95,334e-50,97E+42] ## W<t`e6p%{H6tb
## P9>]MHZ$H4o>xxfP,k;
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 849))

	def test_850(self):
		input = '''
func bs (dynamic PFdE[3,992e-74])
	return 2

func Kr (string sc[46E-48,29])	return
func gJP8 (number u7, bool Thi_[27,50], var Vd)
	return
var YTJ <- true
number O6 <- 504.081
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 850))

	def test_851(self):
		input = '''
func y0g (var v0b, number y7C1[8E+71], bool PMj[1E18])
	return

string qeQq <- SkL
func RIhU (dynamic RR1)
	begin
	end
## gWf
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 851))

	def test_852(self):
		input = '''
var FT[25.235E-35,420.342,70.299] ## u;A;4wY9
var Yc5A[75,18E+48]
string Gq <- 5 ## foq;fiAA$Co_"H
var eDu_[5.099E-53] ## ~tTsA
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 852))

	def test_853(self):
		input = '''
## $BuThXp|JW~8
## )vA*
func KJLt ()	begin
		## N^Ul/+]h3MmtK/
		## |c/-DVi^s 4)*o,^
	end

## c
## (KoPPJw
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 853))

	def test_854(self):
		input = '''
## rutT~.Z>KzAqb
string Fj21[46.760e02,59.782,9e06] <- false ## Z/]Ha
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 854))

	def test_855(self):
		input = '''
bool F4tZ
func vI (string CIRh[25,35,9])
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 855))

	def test_856(self):
		input = '''
## >l5xy|#PDLX
## n
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 856))

	def test_857(self):
		input = '''
func YAb (bool fp)
	return
string hIrI <- 296.558
func CV (var f04, number EJH, number SmHg[8e25,49.184])	return

'''
		expect = '''Error on line 5 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 857))

	def test_858(self):
		input = '''
func otR (var vYCO, bool FWw)	return

dynamic ThJm[1.394E+98] <- true
var lQ[621.285e+63,916E+34,5E+23]
func piy7 (var vSXg)	begin
		## y/T3Qs7grj
		if false break
		elif fZ5 return 90
	end

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 858))

	def test_859(self):
		input = '''
func H9y (var InV_, var YA[35,77.499,57E+93], var JwF[34.547,9.362])	return
func gc ()
	begin
		continue
	end

##  <Y
## z{#Z<M
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 859))

	def test_860(self):
		input = '''
string SGkx[71E-49] <- false
## r[lhJ#:"S`hOX}ThP
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 860))

	def test_861(self):
		input = '''
string iz[60.437,91E-96]
## Fs
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 861))

	def test_862(self):
		input = '''
## Tcf==`5Yu*[5mE
func p6L ()
	return

## tyk3qWS=P<
bool k12[15E65]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 862))

	def test_863(self):
		input = '''
bool vka8 <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 863))

	def test_864(self):
		input = '''
func VI (number yGC, dynamic P8WU[409.781,157])	return
string VyNa[337E+20,9E-24,73.752] <- true ## 9!-k_|OI
bool WKH[355,58.893E+89] <- false ## uQ?z2mN7^Uu0J"VL|<
'''
		expect = '''Error on line 2 col 21: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 864))

	def test_865(self):
		input = '''
dynamic adOb[4] <- "'"@"
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 865))

	def test_866(self):
		input = '''
func CA (bool h9)
	begin
		## -GS
		begin
			number Eb[273.517e21,29.503e-77] <- "xK'"'"'""
			if false break
			elif 35.590 begin
			end
			elif cV56 for nNI_ until KxX by 1
				continue
			elif "'"8" BHJ()["'"2'"v", true] <- Zp4q
			elif 0 jT7o(4E49, false)
			elif true begin
			end
			if true break
			else return "'"'"'"i["
		end
	end
number IN[762E81] <- "x'"o" ## ux:=8h[:o0ImUd+
func ah (bool QWn)
	return

'''
		expect = '''Error on line 7 col 6: false'''
		self.assertTrue(TestParser.test(input, expect, 866))

	def test_867(self):
		input = '''
dynamic bs ## 5TdLaX*OM&n,iIUHc*mb
func BO (var RM1, dynamic kUth[97.217e-48,99.438e+39,33.076])
	return b_GQ
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 867))

	def test_868(self):
		input = '''
## $NkV;1JzR#
func R8 (number S8, string e0[780.498E-41,1.946,67.958])
	return
var SDxC[2e-98]
'''
		expect = '''Error on line 5 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 868))

	def test_869(self):
		input = '''
var vxgb <- 6.876
## >g1VVz8Qz~Wuk9>g
dynamic iLaO[17e-58] ## @0g"![Cyl0L>%KqP<(.
'''
		expect = '''Error on line 4 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 869))

	def test_870(self):
		input = '''
string g5[509E+82,0E+31,30E+13] <- 5.315E+41 ## }cKlwC0..;+S:{%/QG
number H_hW[4.254e-43,90E+65]
number tWoz
## SCW1dp(z
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 870))

	def test_871(self):
		input = '''
func EbSh (number vL[652.782])
	return
func qSJ ()	return "X^'"'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 871))

	def test_872(self):
		input = '''
var JGtU[7E+54] ## SKJwH
number kD8T[68e+65,673e-25,64] ## *sK|nWGIBn
## ZCPf_
var Vsd ## |!Rk}mx3=}T^k
## vT#A@o0uGThn~n`=J
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 872))

	def test_873(self):
		input = '''
## jRp?c7O#WMZ-W
## 3WBQgz<}E?vJ &M
## 7Y&%J]7VN
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 873))

	def test_874(self):
		input = '''
func j0wA (dynamic vxeb)	return false

func ato (bool SF, number IwRf, bool e26T[638.131E12,226.491,2.390E-61])	begin
		for oC until ghY by true
			begin
			end
	end
## pNn
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 874))

	def test_875(self):
		input = '''
func Ro (var kZW[371.449e93], string h5e)
	return false
## (N*+VL1"%lhEL;
dynamic YT6a ## ZM%#*gEC@q=(bL?+
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 875))

	def test_876(self):
		input = '''
func dH3Y (bool uIuy[58,90], number O9[179e+79,47.127E+91])	return "'"z<"
func IU ()
	return 334
func ag (dynamic YtK, dynamic uicf[776,4.390e57,463.910e+20], string Sn[49.924e64,6,76])
	return X3
func IOY4 (bool j6c[5.009E+21,0e+32,78e+88])	return "'"'"O'"'""
func Kc (bool uP, dynamic kQvG)
	begin
	end
'''
		expect = '''Error on line 5 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 876))

	def test_877(self):
		input = '''
func HDRg ()	return

func qX (string xCq[510.040,29.346,5], var P_[9e-02], bool QVo)	begin
	end
var jyL[3.153E+93,8.697,431.806E+33] ## -]3N=]wmDNYU<0Yoya
## WM.1u
## s>I4k#rsL u
'''
		expect = '''Error on line 4 col 39: var'''
		self.assertTrue(TestParser.test(input, expect, 877))

	def test_878(self):
		input = '''
## k
bool qm[77.829] ## yj
var Gfy[383.439,6E78,69.993] <- "v'"" ## .^$yP:/p/b3{~O:
'''
		expect = '''Error on line 4 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 878))

	def test_879(self):
		input = '''
## aXxHjW
dynamic ysc <- "'">" ## ,,8ASjpI{$"uD
func BFV (var fN, string yA0[36.671,8e40,93.441], number OB8M[994.117e+22])	return
bool yy6I <- QSp4 ## @[Cuc~pq"%^`]xem
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 879))

	def test_880(self):
		input = '''
## +`oth|<
string ZoB ## S%%
var dXm ## L>.iI
## +=5({CXSK
## Q!>1@wFGT
'''
		expect = '''Error on line 4 col 16: 
'''
		self.assertTrue(TestParser.test(input, expect, 880))

	def test_881(self):
		input = '''
var a6 <- true ## Q+tY!
## 3]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 881))

	def test_882(self):
		input = '''
number H2Z0 <- 7.729E+48 ## CA
## MK$Kk
## 6;))LMn$u
## pR83B@RSyQIhbU1+TZ!3
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 882))

	def test_883(self):
		input = '''
number ZdrM ## ~Gg<kra.ihMZCvEsx
## >.[{$R
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 883))

	def test_884(self):
		input = '''
func RoRQ ()	return 7.854E-43
## YAi@<t`z
func m0 (var kfm)	return gY

func Sz (bool GX5H[73e-45,541E+83,75], bool Cd)	return true
func xK1J (bool DPZ[707.652e37], bool j9Zj[23,11E-62,547], dynamic ob)	return true
'''
		expect = '''Error on line 4 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 884))

	def test_885(self):
		input = '''
number T1 <- "'"" ## k:tVadr? Hivd#y}[X}
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 885))

	def test_886(self):
		input = '''
var PZY8
## d4AesEh#q/Tew)b0(
'''
		expect = '''Error on line 2 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 886))

	def test_887(self):
		input = '''
func rm8 ()
	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 887))

	def test_888(self):
		input = '''
## 6oxj|#
func jGS (string zoSK[2,300e-27,644.020], number fVm)	return

## U
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 888))

	def test_889(self):
		input = '''
func a9 (var vBRq[7,6,6.037], string o2i, bool ksqn)	begin
		return "'"^'"'""
		## ry@(z%U@(Gw|PZd7?X
		qJX(true, "'"y'"'"|", true)
	end

## 48JYAb6g
var x6 <- 9.993
func KEtI (number ZR[410,627.374e+99])
	begin
		## |CG7
		## a
		if Ag2 begin
		end
	end
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 889))

	def test_890(self):
		input = '''
func dBd (bool dRTz[5])
	return 76.456E83
string zNA[391.980,29] <- "'"'"?"
bool GUjx[644.872E+65] <- false
func eIJr ()	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 890))

	def test_891(self):
		input = '''
number dD[7.005] ## iK5U(@
func jD (dynamic F_E, number rdg[996.821], var edx5[5.024e-37,82E48,6e+07])
	return ZN

## hc>MELAs
number le[62e-99,2.538e94] ## o|%_$6k :
dynamic nJ <- "'"'"" ## BY
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 891))

	def test_892(self):
		input = '''
dynamic k4e
bool Fu ## XTX<>1
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 892))

	def test_893(self):
		input = '''
func knie (dynamic hT, string mPH[8E68], var jHI)	begin
		## ;71DJjSc+NvY
		## OsiUe0o|3Mn5q-8x,y
		var MpX2 <- false ## g`
	end
## J5>u:+7V
func HfC (bool eJ[626,346.986e-07])	return false
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 893))

	def test_894(self):
		input = '''
number jwD6[8.404] <- 898E05
number fzq <- yoP ## uAc$*x/
## ,=qk 67WyF
dynamic Uz ## 1;=GdT
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 894))

	def test_895(self):
		input = '''
number Krt[73.184e-30] ## qehb"feG)k3lm_jB}a@
bool tZ5
func ex (var NbTr[7,5.454])
	return 6e+85
## AS}(wEFiK>~
## TH9?<#
'''
		expect = '''Error on line 4 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 895))

	def test_896(self):
		input = '''
func dX2_ (number e04Z[52,568.942,817], var WHAl)
	return LlMb
string fcL2[0.172E-92]
func pW (var fPG, number f2, number bqO)	return 378.292e54

dynamic jm <- true ## O
'''
		expect = '''Error on line 2 col 40: var'''
		self.assertTrue(TestParser.test(input, expect, 896))

	def test_897(self):
		input = '''
## U*R1g=
## 2[xWOi"PA
## l5$bQw[qv4w!
func T3 (number FDE, string hLNV)
	begin
		## gxK);KrUkJc;(Kc%p
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 897))

	def test_898(self):
		input = '''
## #<4+
## )@amX_8
func RCm7 ()
	begin
		number Gg <- oFy
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 898))

	def test_899(self):
		input = '''
## 3&KjL*Ns
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 899))

	def test_900(self):
		input = '''
bool LNLO[7E06] ## 9-:]~@xePV!f:|Vk&i
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 900))

	def test_901(self):
		input = '''
string UDY[6,143E+59] ## pb@35UJ.
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 901))

	def test_902(self):
		input = '''
dynamic o0[71.791E-49,85e+64,66.192e+90] <- z0m
var e7W5[545.391E+33] <- false ## g
## K>=x.p`/xP4^f
func Y_g ()
	begin
	end
func UiT9 (dynamic NBz)	return 63.591e22
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 902))

	def test_903(self):
		input = '''
var GlZ[281E77,660]
string rl[11.739e68,42,9] <- lv_v
var UX[86.076] ## Y%2XF@(dlsO
## 7v/]KL!
var QS <- 0e+02 ## #Q
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 903))

	def test_904(self):
		input = '''
func tYo (var aALP[873.941], string i5B[51E+50], bool It)
	return "='"Z"
func SlpC ()	return
dynamic de17 <- "'"W'"'"T" ## |aXvYN* Q hX%uVq[0
## zJu2nR
## rl-|v
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 904))

	def test_905(self):
		input = '''
## K:^
func iaps (var ZuL, string No[7E-88,42,6])
	return false
var Ud <- true
## LKJ"`Iyyn^`6T]ow
dynamic itU2 <- 57e+99
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 905))

	def test_906(self):
		input = '''
dynamic n5[56.070,11.488E+18,764.242] <- 35.464
number xCfJ[31.531E+45] <- false
string ib ## {+:b>b?Ps.2@
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 906))

	def test_907(self):
		input = '''
## 8o3gb|x}>,3CxT
dynamic zRmK[7.683e-45,2E07] <- QOqy ## gk$Xh{
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 907))

	def test_908(self):
		input = '''
func fDZ (var LWv, dynamic Ubzp, var bBIl[70])	begin
		B6Gd <- CpDW
	end
## QDX+fKDP7Wm}HmOo
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 908))

	def test_909(self):
		input = '''
## U5b+[X+~{/.T7nnK#Y
dynamic Gl7L[39,4.575,49.675E-45] <- D5 ## `oea.kRRd4 5Rx
bool Wm[449e03,0E-22,472] <- BiR ## ;[1n1D8_-KBv6
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 909))

	def test_910(self):
		input = '''
func SbH (dynamic CVp[358.919,268E-21])
	return
## 8cF-^s<W_Gb
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 910))

	def test_911(self):
		input = '''
## X@0!FC89?V!,zGrUwRB
var LPg[66.886,0.174]
bool P3 <- 71
number Zl[57] ##  4;,~L/
## Pf%<.!b%
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 911))

	def test_912(self):
		input = '''
func dwlG (string x2kp[94,879.849,99], string RL8Y)
	return 8E73

func B4hh ()	return

## 8{[~MVV5uX-o}fcy8
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 912))

	def test_913(self):
		input = '''
## PWYoBo-X+z.*i
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 913))

	def test_914(self):
		input = '''
## ?SOM%
bool jUN
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 914))

	def test_915(self):
		input = '''
## a]{b:IH
bool NY[54.533e-42,359E-15]
string CDD ## z.,Dn=0oj(I8Nv.
## | (8QfV?"y
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 915))

	def test_916(self):
		input = '''
## t;iAs7>bEmVlZ
## W+e29[B>+Nd,
func tk1H (bool Dme, string oZ)
	return

## Rl|k8P+^].hi^bua
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 916))

	def test_917(self):
		input = '''
## HR%ll^^hLaLJ3PI
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 917))

	def test_918(self):
		input = '''
string wcg[7E-42,127E-74,60.515E85] <- false ## @$^A!,]uF$d
## 487*)|h+)87[lwvA
## Xr@
## WL&VCtq~8MBTh:}y$
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 918))

	def test_919(self):
		input = '''
func B_O (var sYHf, dynamic WlM, number tr8E)
	begin
		for Iks until s7m by o0s
			break
	end

## fN8QCgMg/cbQeu
## &C$/
var ggVD[6e+59] <- false
func snc (bool xT0[38])
	return

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 919))

	def test_920(self):
		input = '''
func FU ()
	return
number yU2[988.758e-71,871] ## Ld{kR:AOM7O1PU
var b1K[37E27]
## l("LYCFT
'''
		expect = '''Error on line 5 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 920))

	def test_921(self):
		input = '''
func IazK (dynamic uR[4,47,87.909e+22])
	return "('"'"H"

var nH2I[44,84.729E87]
## H&95I/-/t>3Av/Z+5kX
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 921))

	def test_922(self):
		input = '''
func mGj0 (dynamic Fyl, var wE[590])	return

dynamic c8C[7.048e-05,5E26,1.077] <- "'"" ## ^OqLo3dS<+@s?a~0>
## rI:}?F7y
func hS0 (dynamic U8[102.116e+31], number rr8C[4e-30])
	return
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 922))

	def test_923(self):
		input = '''
func P8a_ (dynamic sJ)
	return false
## =&^)(yj97Z
dynamic db <- true ## LW^Ji}AN
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 923))

	def test_924(self):
		input = '''
func GWfq (number YJ[7.933,8,635.819E+67])	begin
		## N8pL$cuC
		number Bc[63e-30]
		## Az
	end

number yXR ## d4Lh%j;~iR4~
dynamic GG
func dZmN ()
	begin
		begin
		end
		if "'"l['"J" begin
			begin
				if true for PQOd until 6 by Plgq
					if true begin
					end
					elif "oL" break
					elif IqpD continue
					else for W3Y until "'"{'"'"" by ")'"-'""
						TV4U(4.370e+55, "'"'"'"=", "'"'"'"")
				else if DoS bool cBl <- 2E-66 ## .sIPh
				elif 68.892e+21 ueo(true)
				elif false Yv()
				elif "'"'"'"" continue
			end
		end
		elif Bto for Upv until false by UHdV
			ZfQ()[true] <- J8
		else Q6(false)
		## Y#1
	end
'''
		expect = '''Error on line 14 col 5: '"l['"J'''
		self.assertTrue(TestParser.test(input, expect, 924))

	def test_925(self):
		input = '''
## FYIu4<M~
bool ug
string hLr <- e78r
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 925))

	def test_926(self):
		input = '''
## k,#^*ia
func gK3 ()
	return

## $k
var eM ## vo Z>p$^SrcOo,>
'''
		expect = '''Error on line 7 col 25: 
'''
		self.assertTrue(TestParser.test(input, expect, 926))

	def test_927(self):
		input = '''
func MRFA ()
	begin
		if true number Gc3I[7,47] ## &!9T_PnT4+iy@
		elif "N" Zl3()
		elif 697.569 return "3fe'""
		elif "'"'"" if false break
		elif "'"" string c0R <- "tV'"'":"
		elif false break
		else begin
			## rM
		end
		else YyqO <- false
		## 9?ql[6jWGs4fZ}
		continue
	end
func ZK (bool Wf)	begin
		break
		## H,b<4KpN #}!)
		return Esa7
	end

bool YCbV[3,68.506]
'''
		expect = '''Error on line 4 col 5: true'''
		self.assertTrue(TestParser.test(input, expect, 927))

	def test_928(self):
		input = '''
## .k"/e
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 928))

	def test_929(self):
		input = '''
number xZKE ## 9%`BVG3UJ
func f1p (string BOn, var uZ, var lFz[99.815e+98,631,28])	return LB
'''
		expect = '''Error on line 3 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 929))

	def test_930(self):
		input = '''
## dV0SQgM  Iyh
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 930))

	def test_931(self):
		input = '''
var Uy[10E-58,550E98] ## >u;d4
## Aj3UrjIfd@O2yJ,g
func NZSE (string UrM[432E-62], bool gv, dynamic Ng1Q[2])
	begin
		## :gk"DyxB~4hQ
		## n-rH&rg47o{8=
		## (mg%$
	end
## v|;
func Gu ()
	return false
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 931))

	def test_932(self):
		input = '''
## CY>%a>(M%g7lKj?B.|`D
number TQx <- "2"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 932))

	def test_933(self):
		input = '''
bool qA[8.093] ## hsm*F6m<%nT.hl_~
func r1 (string bphP[25E-07,1.910,195])
	begin
		## PG
	end
## %oS^.E?z 9OS{
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 933))

	def test_934(self):
		input = '''
func gJ2 (var X2hq[578.083e69,266,71], dynamic dlt4)	begin
		## R{p,YHVeI.3
		continue
	end
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 934))

	def test_935(self):
		input = '''
func lP9 (dynamic E3, string Xd[9,97.194,9.725], bool iXcT[389])
	return

func IOXm (number EP[7.466E60,24E+81])
	return false
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 935))

	def test_936(self):
		input = '''
func Umxn ()	begin
		## ^p#ze,2wZ#<!}Mz8)
		## qPycTH`,$p5G<n
	end
## -K
func DrKq (var ad1[15.737])
	begin
		break
		return
		## S_]~5}1o
	end
'''
		expect = '''Error on line 7 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 936))

	def test_937(self):
		input = '''
## /{y8}?%H_ZNQw#tz
var H8GH[479.020E+67,760.531] <- 608
bool BdK2 <- "$'"'"6'"" ## SF0F(!QfvRpl
var hjv9[0e+92]
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 937))

	def test_938(self):
		input = '''
func Pl9f (number Dnp[58E-38,6.831])
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 938))

	def test_939(self):
		input = '''
func bl8X (bool Kd, number GMj, dynamic oL)	begin
	end
string cwfl[1E80]
## z)K/r>TWR/j*>pw
## y|s
'''
		expect = '''Error on line 2 col 32: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 939))

	def test_940(self):
		input = '''
string XtM[54.649e-01] ## W1dIV^=&*B}{9*pFi#u
string h9eX[261.587,465.573]
## OOo|S;?P8p9QAn}*
var vl <- false
string RTg[363E+57,45.745] <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 940))

	def test_941(self):
		input = '''
dynamic X8 <- false ## LRm
var ikH5 <- "j'"$(|"
func J1d (bool vE[72.960e47,3.094], bool MkNa, string wHNv[2.512,74.576])	return
func d0 ()
	return Qy
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 941))

	def test_942(self):
		input = '''
func QhT ()	return "'"'"'""

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 942))

	def test_943(self):
		input = '''
number DDR <- true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 943))

	def test_944(self):
		input = '''
## {`=mn
func sn (bool PMmX[742,38.962], dynamic aV8, dynamic h_[611.190,54.383])
	return e6Dg
func z087 (dynamic CO)
	return

number Fjv[20E+06] <- cTn
## `=;w387?
'''
		expect = '''Error on line 3 col 32: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 944))

	def test_945(self):
		input = '''
func sA (string MfP[9e+71,14e07], var sF, bool dXWc)
	begin
		for tMf until CVB by 8E-14
			for adY until "'"" by HrGn
				continue
		## uJ.+qNDq742ve 
	end
func Qn (string PjAo)
	return
func o2 (bool vZgN[3e98,60.438], string XER[40,5.646], var w3)
	return 5

## -O?
'''
		expect = '''Error on line 2 col 34: var'''
		self.assertTrue(TestParser.test(input, expect, 945))

	def test_946(self):
		input = '''
dynamic yx[3.434,90e-74] <- 4.398 ## h#R
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 946))

	def test_947(self):
		input = '''
dynamic jB <- "'"'"" ## 2N`^~=S$ vsNF
func zg (bool Fs_E[6.769,976.726E34,62])
	return
number QPI6[7.512e76] <- false
## DZ%Y#ou&G72LK:K2a7Dg
## kO{9D=y
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 947))

	def test_948(self):
		input = '''
func Bi (number A1EV[88.198,94,55.011E43], dynamic fAo7)	return
## bs.h)pe)`qg.M^u,7r
'''
		expect = '''Error on line 2 col 43: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 948))

	def test_949(self):
		input = '''
func t3 ()	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 949))

	def test_950(self):
		input = '''
number l6[42.944,238.017]
func vAy (bool EVm, number b1Hw[9,7.042,44], string mLS)	return

func ZHLm ()
	begin
		## z!6n2G@KQ8QRa(qI$"`
		continue
		bool w5
	end

## yd
## 57
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 950))

	def test_951(self):
		input = '''
number xYNH[8.921,3.656E-71] <- GPk5
func qRqa (string sZS[69E+49,84.530,5e-24])	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 951))

	def test_952(self):
		input = '''
func RiF ()
	return

dynamic PA <- "%" ## 8I}!?fBx
number r3u[15.091,57] <- false ## 2hTk&FLb4`Un
var Fkw[3.316e30,8.859]
##  jBYY";tN"LT/
'''
		expect = '''Error on line 7 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 952))

	def test_953(self):
		input = '''
func ODlY ()	return "'"'"{.g"

## W662s0{m_]4W96a" t}q
dynamic uuLJ ## BaLZXWZk/I9I>]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 953))

	def test_954(self):
		input = '''
## &mUou[>Y
string WvJ[4.920,716] <- 8.083E34
string Oe1U <- false ## >-
func xwd (number NVA[525.375,653,67.449])	return KmT

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 954))

	def test_955(self):
		input = '''
string zUjF[878,43.180] <- 0
func Ux (string Gl_, var jhN, var Ma[2.164])
	return "-K)"

'''
		expect = '''Error on line 3 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 955))

	def test_956(self):
		input = '''
var I9F[3.485,945,5.220E-78] <- true
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 956))

	def test_957(self):
		input = '''
string LQir[22.977e58] <- false
## :d9iOh{~sN@zL|
number r5pw ## G)
bool pEQ5 <- "'")'"'"t" ## Zf41J|=F
string YTjc[8E-33,418.493E+68,67]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 957))

	def test_958(self):
		input = '''
string R5[50,39e-15] <- vDu
var Wyiw[79E-94] ## vdT[[ip/IYvJCZw
## V<O{vCG}G{4
func AGac (string veWw[439.479e+87,6.508E-65], number Dux[94.649,90])
	return true

'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 958))

	def test_959(self):
		input = '''
## uLTuj??w*t8@{<
string Crl[27E18]
func WoI2 (string uR4A)	begin
		## ;X-H*O
		for OLzu until ""zK" by q71
			QENc(true, false, false)
		## ]~zoGT/I7k9+s|r>
	end

'''
		expect = ''' by q71'''
		self.assertTrue(TestParser.test(input, expect, 959))

	def test_960(self):
		input = '''
## 4d{!wlg
bool XDVR ## C]
func o8z ()
	return "'"'"'"'""
string Ia_O[2] <- "'"c{'"P" ## {%+BVOsT/&~Fdzx
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 960))

	def test_961(self):
		input = '''
var MWR <- fOO ## l?rjw
bool GnVu
## 5M:kuq/{:(9fv!*dh
number c7U[60.653] ## pA9
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 961))

	def test_962(self):
		input = '''
number QR8P <- rZO
var Gqop[9.249E+22,0.102,306] <- 39.016E33
func AxRv (bool KqX, string qB[93.831,5e01], var Qh3[317,64.796e+13])	return

dynamic E5DI[807.202e43,43.540] <- "B'"'""
## vyAO
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 962))

	def test_963(self):
		input = '''
dynamic me3[28.442,63E+37] <- 9
bool p4 <- "L'"'""
## Swdm!2#~Vi
## 1l@w`)@@f9AO `J6/"
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 963))

	def test_964(self):
		input = '''
bool lB ## Nz4jfg~r*CW
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 964))

	def test_965(self):
		input = '''
func P_ET ()	begin
		for d0Pm until false by kPfF
			return true
		## #c2y?"o
		##  G^piM-f(!_(uKhEYnc
	end
var Rq
## ]~Os[ o1b/
func aS (string Kp_H[9.414,9,5.931E-81], var Miui[0E-17,777.463e+94])	return false

'''
		expect = '''Error on line 8 col 6: 
'''
		self.assertTrue(TestParser.test(input, expect, 965))

	def test_966(self):
		input = '''
## w
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 966))

	def test_967(self):
		input = '''
func Eyb5 (dynamic s6y0)
	return 84
string Xcj[9.424,58E60,57E-79]
## Z8eJ,YL(KqzUE5O:{
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 967))

	def test_968(self):
		input = '''
## *"}hUyh3%
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 968))

	def test_969(self):
		input = '''
## %Bv6q,EiHCe+m
func xoz (var q5[49E-40,2.666E-92], var yhk[871], number F33[5.226])
	return

## 5`tS*{AMaF
func RNr ()
	return "@'"('"'""

## l^q=ahg3DavPE
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 969))

	def test_970(self):
		input = '''
bool ZM_
dynamic zTd
## M?nQ.GMi``)VL2bJ
func XTqn ()
	begin
		begin
		end
		## p~aw-4v3{6<
		## x[q
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 970))

	def test_971(self):
		input = '''
number xI ## DK#(RFH6nT)
func p4or ()	begin
	end

## 78|[az}#(WS
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 971))

	def test_972(self):
		input = '''
## e1[
func wth (string z5C, var Kn[14,90.948])	begin
	end
func clAz (number mYC[626e+73,11E+36,135e-43])
	begin
	end
'''
		expect = '''Error on line 3 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 972))

	def test_973(self):
		input = '''
## hiqa{D1J4QO
string ppv <- 7.652
func BTfJ ()	return
## !KZo1?AcnC7N?I_! W
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 973))

	def test_974(self):
		input = '''
func O7uS ()
	return
number N4[8.021,17E30,555] <- "'"'"" ## eB
func N7 (string Pbe, var tz, number KHZ4)	return
'''
		expect = '''Error on line 5 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 974))

	def test_975(self):
		input = '''
## .JuF}j/SLUJ4ZNO/G
bool Di <- YiSY ## H%=3$jEZ3DD&q
string f_
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 975))

	def test_976(self):
		input = '''
func D4c ()
	return

func ld (dynamic GUn)
	return true
## 0y)QdJS
'''
		expect = '''Error on line 5 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 976))

	def test_977(self):
		input = '''
number w_aO[897E-50,8,673e-82]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 977))

	def test_978(self):
		input = '''
dynamic Pkd[105e+04,60E+02,86.466] <- true
func AZ ()	return
## mQ4H&u6
## C?F
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 978))

	def test_979(self):
		input = '''
func cy (dynamic LwYz, number cZ)
	return "'""

## /V"3Dr_Ds2(sbGj
number kJ8[1E+12]
func DGSi (string pQ[9e+82], string D10[626.893e+08,445.510e+23], bool E1pL[28])	return
func jMu (dynamic W2c[31,553e49,871], bool bbgE[2.372E-05], dynamic ejwu[82e-90])	begin
	end

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 979))

	def test_980(self):
		input = '''
func g5 (string MoU3, bool ot[8.166,943.753e79])
	return false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 980))

	def test_981(self):
		input = '''
func IN ()
	return

string wHqk[0e-29,90e-73,4E+83] ## kLKY[N#znk`YIc!
## GDUy>pf9Xk>!
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 981))

	def test_982(self):
		input = '''
func Rfy4 ()
	return 910E-67

dynamic xVV6 ## y0
## heH}IbC*Cc0WR6;i|i=
dynamic t1y <- 55E-51 ## t}1Bz!H0%INJ7@
var fY[10.581]
'''
		expect = '''Error on line 8 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 982))

	def test_983(self):
		input = '''
func ULO (bool w7, dynamic P8q, number MTzf[422E-03,6.160e+75,32E-01])
	return

string L3 <- 17e+06
## xpYx7(?U4/
'''
		expect = '''Error on line 2 col 19: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 983))

	def test_984(self):
		input = '''
string Ny[9] ## )RllYhF
## M>u{u9kmpT2NU%"
number xWTp[0E-18] ## /Z(F^s{."S9
## 8``<A8YX
## O
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 984))

	def test_985(self):
		input = '''
dynamic j4 <- "'":'"'"o"
bool QYCP <- 2e-11 ## $@j{5n
## WP$quoC{i; k
bool sV
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 985))

	def test_986(self):
		input = '''
## ]iXH?`T*>!
func liJ0 (var Rf[2.820e+70])	begin
		if false continue
		else break
		## HNCqH"|s?U
		## U!LEl "u*
	end
## @tr
number Ix <- "'""
## UF,CV63E`u*!Z_3sA/`+
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 986))

	def test_987(self):
		input = '''
func zX ()
	return "'"'""

## -4$W?L9 [exVqG
## chE]Y]QX?3*kl/`{^C
func IEye (var Ptq[22E59], bool zuQ[389,4.201], string rfo)	return
'''
		expect = '''Error on line 7 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 987))

	def test_988(self):
		input = '''
dynamic ru <- true ## 71P*.bx
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 988))

	def test_989(self):
		input = '''
## h.(#Z8dPPZ|vE`Lm
## GU~1]H
func W7Ra ()	return
func K1uw (dynamic J7q[91,303,8.795])	return
'''
		expect = '''Error on line 5 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 989))

	def test_990(self):
		input = '''
## JPu9IVh^
## " sibDQS(#7~j
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 990))

	def test_991(self):
		input = '''
func iw (dynamic UqCz)
	return

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 991))

	def test_992(self):
		input = '''
string GcJ[894E47,71E-66,29.339e34] <- 86
bool Pst <- "~" ## 4Sm5hil+p/F]eJOP
##  XjbJh;rV|D^|P} hb
func HL (string etxt)
	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 992))

	def test_993(self):
		input = '''
## |h150TyY+R
func kVzD (var pl[710], string KX)
	return
string t5 <- IUu
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 993))

	def test_994(self):
		input = '''
number Dpn[98] <- false
string fH_ <- "k'""
func QcB (dynamic nrZX[2E-26], var pXG5, string iXX)	return

func cJCv (bool np[2.259e84], dynamic ZKP[2,47E+17])
	return

func fUh (number kp[6.333,602.417E+84], var dE3[51E-46,528,91.488e+44], dynamic pde[4E-42,0.657e72])	begin
		continue
		if "*'"#'"!" for dPi until "*'"" by true
			C8(HMcH, pLn)
		elif true ZVp[false, false] <- nOR
		elif true continue
		elif true break
		elif true kl()
		elif 769.793 begin
			var iZ4F <- 5e-81 ## Of<o-:-"a
		end
	end

'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 994))

	def test_995(self):
		input = '''
func Ux8 (var UWD[276.946e73,840.235E+34])
	return
number vf
string dHG ## FR7
func VSWu ()
	return

func QZ (number TC9e, number RTLE, dynamic vV[91.638,46.111,33.627E72])
	begin
	end
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 995))

	def test_996(self):
		input = '''
dynamic sI[617E+20] <- MQ ## xjk$&0|3!
func xQ9a (var UT[45.071])
	return

'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 996))

	def test_997(self):
		input = '''
## #j@i2.+[y6
## F.4iK%(fXHrc)nQZ]tA
## V"SrYN_:
bool RoFq <- ht
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 997))

	def test_998(self):
		input = '''
## ?z8&$=Zbj^
func VU (var KGw[31.179E+33], string Xh[6.087,172,6])
	begin
		## dULW!xy 62^Bw`%u
	end
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 998))

	def test_999(self):
		input = '''
var W1 <- "'"" ## |crU*0@3V2Y7wdNC)C
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 999))

	def test_1000(self):
		input = '''
func zHKN ()
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1000))

	def test_1001(self):
		input = '''
number yK ## 3yq"UX{O[
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1001))

	def test_1002(self):
		input = '''
## J}S_O
## Jwu&rfmYh5C-
func i2QO (dynamic ex0[3.137,2.865], string dJ[81.732,416.452e57], dynamic b2G[6.498e+33])
	return
'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1002))

	def test_1003(self):
		input = '''
## XXbVV4
## ~:#+F
## /q^C K@nK|y>3;%E%pnN
func YKpZ ()	return

bool ysWF
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1003))

	def test_1004(self):
		input = '''
## 5$#yNpD|~w]F@
func E4g (string S9Z4, string iwm, var DY[404,8e95])
	return
number xm[465.498,11,42.358] ## Brh
func um (string FW[9], number bQST, string X5uD[5e+99,7E+90,6E-00])
	begin
	end

'''
		expect = '''Error on line 3 col 35: var'''
		self.assertTrue(TestParser.test(input, expect, 1004))

	def test_1005(self):
		input = '''
func WF (bool OTVi[1e+97,705.011], dynamic Ub[9.952E70,4,72E-80])
	begin
		## #8n[y{|V.(WQldu)
		## BKt]4R
		bool AfEK[187.286,99] ## ,Y7DM7da+uih.HHGs"F
	end
var fiY0 <- true
bool WDM[48.643,30e+28] ## Xm#rJ(H^+1A}lb&AgWD/
## 8-bYjcC#oO 8cq#E
'''
		expect = '''Error on line 2 col 35: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1005))

	def test_1006(self):
		input = '''
func Gv (string JVV[9.076E-38,3,75], var Gie5, dynamic D9s[37.580E60,3.306e96,639])
	return
string WW6w[3.349E-31,591e-31] <- false ## ajl1-6M$?7n*]F=<Lo
## uv7rqvKE9`gSHY
string L0Us ## #Ph,"=Te]I"Nx
'''
		expect = '''Error on line 2 col 37: var'''
		self.assertTrue(TestParser.test(input, expect, 1006))

	def test_1007(self):
		input = '''
dynamic nM[3.730,45,48]
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1007))

	def test_1008(self):
		input = '''
dynamic UQ <- Ofb4
bool DX_
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1008))

	def test_1009(self):
		input = '''
dynamic zi[476.115e83,4.134,354.273] ## 8FFf5.SdS$m
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1009))

	def test_1010(self):
		input = '''
## qd,
## }`}/%_YsfYo^j0cB?
func e1 (string v9Nr)	return false

number mccc[19E12,29.759e-63] <- C6
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1010))

	def test_1011(self):
		input = '''
func dWYf (string vpm)
	begin
		## m0^ul&9mb)4we0MBu.
		## s+Sg$DC2EsN9SzQJ6
		begin
			## (k/XU+`>M0v""
			for mn until "'"'"p" by true
				for Aw until false by false
					begin
					end
		end
	end
## H9/(eh`YC$HU`mf!1[
func PD (bool ZT0, bool fU, var klS)	begin
	end
bool D_ ## :Q<)aB
'''
		expect = '''Error on line 15 col 28: var'''
		self.assertTrue(TestParser.test(input, expect, 1011))

	def test_1012(self):
		input = '''
func y1I (dynamic t75F, var Iu, string pPMd)	return
## 24uAFk;lgZ8uzK_
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1012))

	def test_1013(self):
		input = '''
## ROVhzlP|e7/4v/
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1013))

	def test_1014(self):
		input = '''
func mZU8 ()	return true

number Sq[417.950,3,20E-10]
## C>r5
## +y
## 68K
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1014))

	def test_1015(self):
		input = '''
## 2O
## 9o*?&m?e:+
var kO
## 1V)F*j
## ZYAMnd;ep~NJF 
'''
		expect = '''Error on line 4 col 6: 
'''
		self.assertTrue(TestParser.test(input, expect, 1015))

	def test_1016(self):
		input = '''
func sqJK ()	begin
		## .
		break
	end

## gCw|-b@&e@C},4`)"6cv
## ^AuJdUfDX#)"-
string ui <- hr6l ## ?*L$hB3&?
## uC@mAR`"W]uON%:!`
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1016))

	def test_1017(self):
		input = '''
func C7 ()	return

## ]fE
func mR (bool DSry, number YSbq, bool S0)	return nI

## ~:uJ$D6hO;I:MWJ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1017))

	def test_1018(self):
		input = '''
func xj (number h_SD)
	begin
		continue
	end
func ZfL (bool i9, string bK)
	begin
		break
		OCw("'":'"d'"", "'"y", 7E-41)
	end

## Se<GT%f0R&/n4jDhu<zE
## =(m2s+JE}<Of~uc
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1018))

	def test_1019(self):
		input = '''
func fk ()	return true
## (98lyuu&]8YK&
func Zv (dynamic OLs[5.862e+45])	return

## `OgK<O3tN
func QOX (var WOO, var du5W[35.727e-60,46.331], number h6a)
	begin
		for ItF until false by oRD
			for eo5 until BBY by "'""
				break
	end

'''
		expect = '''Error on line 4 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1019))

	def test_1020(self):
		input = '''
func gBOA (string NPv9[272.711], bool Pjw[241.719,959e35,60e+45], number HiA[78.036E23,5])
	return 4

var uI9f ## mqygi=a<>EQm*
'''
		expect = '''Error on line 5 col 25: 
'''
		self.assertTrue(TestParser.test(input, expect, 1020))

	def test_1021(self):
		input = '''
func ZLns (dynamic zm8[14E+84,425.862E44,4e-64], dynamic sN, bool vGUb[920.450e-25,882E45])
	begin
	end

'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1021))

	def test_1022(self):
		input = '''
## h !jis8fL4QgQs2eH
func mB (string cc)
	begin
		## T[mwaXs)+tRCHN+Qysk
		## a!t?S7Pl<YZ{
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1022))

	def test_1023(self):
		input = '''
bool xLt[26]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1023))

	def test_1024(self):
		input = '''
func Gi (var ri9T[7.836], number Hj[944], bool nt[129.195e92,5.405])
	return

## i]e
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1024))

	def test_1025(self):
		input = '''
## +]n owFC z{UrJ{RaGz
string KF[67] ## Ns-aI+I}6~C.3W@DIpJ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1025))

	def test_1026(self):
		input = '''
func Kdz ()
	begin
		for AKZ until wM6w by G5e
			if ugjB p0[false, "'"'"'"'"q"] <- yY0
			elif 18.126e+54 number cM[87.364,49.145] ## lXt-}9nojoiD+?b+bn(
			elif true begin
				## &[WdJD,IMFW
				HG_J(2.416E68, z3rt)
			end
			elif 58.171 ZYe <- OtG
			elif 78e38 continue
			elif "&V'"'"'"" SW <- 75.782
		## J.=a1CO@my}+
	end

## <%zWmWh;Zg=
'''
		expect = '''Error on line 5 col 6: ugjB'''
		self.assertTrue(TestParser.test(input, expect, 1026))

	def test_1027(self):
		input = '''
## X/YDoS
bool RYP[1e79] <- 550
number X5[7.436E-96] ## 8Ml"[(F^"d>.f
func m2 (var aqSJ)
	return

'''
		expect = '''Error on line 5 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1027))

	def test_1028(self):
		input = '''
## !*KP>Hx^u$ 11N<!*H-
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1028))

	def test_1029(self):
		input = '''
func xB (number ZMY, number iN98, string fn[49])
	return qi
## {$mG
bool oF ## IkYpLD0qV/a0
dynamic BA[87] <- j8
'''
		expect = '''Error on line 6 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1029))

	def test_1030(self):
		input = '''
func g69 (bool lxfM[137e-09], dynamic LK7, dynamic fQp[6,56e+76,1e-96])	return
func zw2 (bool Bi, dynamic SmoX[402E+68,1.756,0.211e+85], string eA[8.577,84E78,598.217e+00])
	return true
## )K%L]cEo>07:
## {5>GC ,:Gp6S^Y
bool H4D
'''
		expect = '''Error on line 2 col 30: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1030))

	def test_1031(self):
		input = '''
dynamic O8m <- false ## 6+A&j&5O
func o_ (dynamic ByM[7.084])	return 75.627

func hjT ()	return true
func BHn4 (var YdVF)	begin
	end

## :)AGVR^2]"c
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1031))

	def test_1032(self):
		input = '''
var ST7[0.264,1E25] <- 6.986E-22 ## K]-w Usib#D/97
## m$Gx,eqE{
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1032))

	def test_1033(self):
		input = '''
## 9a="{C#E`x-W3
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1033))

	def test_1034(self):
		input = '''
## NL,
number k7[14.940,5.563E66] <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1034))

	def test_1035(self):
		input = '''
## fs>+
## jj
func Tk8 (var H6V)	return "'"'"'"'"8"
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1035))

	def test_1036(self):
		input = '''
string naz7 <- "l'"S" ## <7
bool kQf[4,29e09] ## F/fHiJOT
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1036))

	def test_1037(self):
		input = '''
## _B7[Yt?LtOr]t"nDY"l
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1037))

	def test_1038(self):
		input = '''
func Ord (string NYE)	begin
		## M}IdCgA6x)hLwfsW(~C
		begin
		end
		Jm7(pJ0, "'"'"E'"", true)[true, D0k5] <- false
	end
## }EK[.ya|gdqw*^
func Osaf (var Nc[815,317], dynamic bKeC[1.145])	return
'''
		expect = '''Error on line 9 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1038))

	def test_1039(self):
		input = '''
## `fgco66F)zJ
func ADp0 (bool xqs7[6E+76,29.674])	return jW
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1039))

	def test_1040(self):
		input = '''
## mP{#f+}7j
## g2g}[+o]m#*.juwL 3|m
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1040))

	def test_1041(self):
		input = '''
## O^|"[ K|{H)>
number Osc1 <- "+60'"8"
## Mhxdn..?4VIf[DfG
## )%`LUa%}VP6+u#I
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1041))

	def test_1042(self):
		input = '''
func QWr ()	return oaq
## BUVR_Y[0kd/?Cqu6SQ
## vz!m;Urn2* Sw[ObsJx~
string qKvy[9.736,34.657E-18]
func AEJ (bool e8Y, string dr[710.494e14,507e26,9.124E95], string Ao)
	return lj

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1042))

	def test_1043(self):
		input = '''
## ,+t
## V^gp&+W&
bool opC <- "'"Q" ## I.h"%
func Hth ()
	return

func YmW0 (bool QQd[5])	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1043))

	def test_1044(self):
		input = '''
bool bFf[64,46.284e-99,6.414E-74] <- c8_ ## H&
bool jd
func MMW (dynamic LGha[4e25,1.672,7.225], number A3)
	return

'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1044))

	def test_1045(self):
		input = '''
dynamic r2s[2e+79,5e-30,15.918E-63] <- "i," ## 4P^Q_/c4{b#BZw-%
func ntR (number Nv, string z8o[1e+30,846,6], dynamic G0)
	return
dynamic x6E6 <- V0i7
## R&e3LM
func pWko ()	begin
		## ]MP|_B*p~0!&>_Z@n@&&
	end

'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1045))

	def test_1046(self):
		input = '''
## T=1}_)FRGZm}!:w>urR
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1046))

	def test_1047(self):
		input = '''
func pNb1 (string Hx)	return
## qo
dynamic yjP <- 9
number zLj[16E+15] <- false ## 7keUocO{&t<M>4?HR!
bool Jrtq[55] <- LI3
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1047))

	def test_1048(self):
		input = '''
var OLHU[5.841E-54,62E+62,8e-52] ## X^]s(V:D8~)=r+@
func DdVS (number qS, string sv[484e38,92.252], dynamic JlP[57.612,98])
	return
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1048))

	def test_1049(self):
		input = '''
## 3/(
## u
func B3b (dynamic Yj_M, dynamic ALAJ)
	begin
		for HWC until "8{" by true
			string akT ## @/]0#7
		## I
		return AoVm
	end
func nT (number omk[135,896.911e39,7.690E+37])	return Ns

'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1049))

	def test_1050(self):
		input = '''
dynamic S7
func Tn ()	return false

var hjs
var yQZX <- i5g
'''
		expect = '''Error on line 5 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 1050))

	def test_1051(self):
		input = '''
func iF (string lso, dynamic J3)	begin
		begin
			bool Qr0 ## :.G3<[QB4i3T
		end
		## fc6jm[^:aZ87Y0;We3
		## %`{k[ZR%Uy~Q^
	end

var jZ[35E44] <- "{Y&'"" ## o~tKq"D
## -Np2;r[h?[9[E<@1iMM"
bool f7G_[53,503,0.356]
## G14[0oo-j5/}M-=gu
'''
		expect = '''Error on line 2 col 21: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1051))

	def test_1052(self):
		input = '''
## y|K5y-M|!FvY!:f
## =qG}&=Wbl`
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1052))

	def test_1053(self):
		input = '''
func R6b ()
	return
var a0c[6]
func WO2 (bool Qh[1.669,0E+85,65.799], number CH)	return false
bool y9D <- false ## D#nH
string nn <- NrvJ
'''
		expect = '''Error on line 4 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1053))

	def test_1054(self):
		input = '''
func BfD (var s_[877e+49], bool jdc, number HV)
	return XDfH
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1054))

	def test_1055(self):
		input = '''
func gzFy (var y4d9, var wvOr[838.893,5,9])
	return

bool bugv[5,372.852E-86] <- 90.526E89 ## (:"Ur0i!/k
var CWV[666.843,6.231e-35,0E+74] <- ITKh ## A~&_tn:>
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1055))

	def test_1056(self):
		input = '''
## <1ao.nT]FMuXZ_
## .^0NgBqsW[c/=>nk,%Y
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1056))

	def test_1057(self):
		input = '''
func o16 (bool TO, bool Kl)
	begin
		## Fg@)Q3?
	end

number WhlC
func AC2m (var X_[554E+23,82])	return

## ?z?vth0Ec7P)s<k6s{7
'''
		expect = '''Error on line 8 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1057))

	def test_1058(self):
		input = '''
## NhO|DyA?//2Jj"$YI~{
dynamic Ff <- 43.657e-44 ## .Z8~qFw)4b|~ROHeFf
func bjf ()
	begin
		continue
		X5[nb] <- false
		## *#"ts&8
	end
var pk ## M}!C$yTL~Q^C*1F@
var k8[704.582E+47] <- false ## ]ZZl([F7:y7XL
'''
		expect = '''Error on line 10 col 26: 
'''
		self.assertTrue(TestParser.test(input, expect, 1058))

	def test_1059(self):
		input = '''
func i0 (var My)	begin
		var q_RB[417.216e-02,95e+14,691] <- false
		begin
			## xD(dz
			## ckOb
		end
		## }M3|z
	end

dynamic nZ9 <- 558.978E76 ## @e
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1059))

	def test_1060(self):
		input = '''
func ZABx ()	return
## CSl?_eTex7ivq
func rd ()
	return pa

func IH (dynamic mD, bool WrMk[6E15,1.235E+69,204E+69], number SU[378,435.232,5.980e-74])
	begin
	end

'''
		expect = '''Error on line 7 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1060))

	def test_1061(self):
		input = '''
func bx (number EY, dynamic ZCo[932,50.228E-75])	return 422e+89

func nC (string yP7l, var No[82])	begin
		nD("'"dC'"", false, true)
		break
	end

'''
		expect = '''Error on line 2 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1061))

	def test_1062(self):
		input = '''
func IO (bool hxz1[280E76], number sij[747.702E-61], var XTr)
	begin
		## h`mjM{0ofSeiHncp2I
	end

string RV[1.732e+66] <- true
## ,&gR
'''
		expect = '''Error on line 2 col 53: var'''
		self.assertTrue(TestParser.test(input, expect, 1062))

	def test_1063(self):
		input = '''
func GxV ()
	begin
	end
## [n$n"G0O"P
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1063))

	def test_1064(self):
		input = '''
## Y#{|&"_9&&QSM
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1064))

	def test_1065(self):
		input = '''
## *]J=Px:(A5gmO6Z06F_a
func ob (number pJ)	return

## -vLh!D7CNi~vM/~9
func YFmG (dynamic mHll, var JI, string Z2[53,7E-01,977])
	begin
		## 2
		## 90AT:C.Mwjq&?@JI?vo
		begin
			YP()
		end
	end

## ehiY)MJ
'''
		expect = '''Error on line 6 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1065))

	def test_1066(self):
		input = '''
## bxkdA_K{pvJ[U$
string tfc <- false ## 6MIP-&X
number E8[1,7.001E-83] <- false ## w,a"Z3a
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1066))

	def test_1067(self):
		input = '''
## *
## :G<6$Y{38b
func IAwp ()
	return "]5"

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1067))

	def test_1068(self):
		input = '''
## I,<*Q(
func krp (string WqE[70.521,745E43])
	return 47E+14

string HC <- 35.535 ## WqwKlS.t`Y#r`e~"$
## 1e4v7RpYzb*G5m
## 7`&Kra&
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1068))

	def test_1069(self):
		input = '''
## Kc=V.
## $_
func qu (bool OTh[2.192,800.680,38E88], var DG[45E28,716.766e+63], bool Hzi)
	begin
		## HhH!PQM
		if 3 for rvtX until 941e-46 by "'"'"'""
			TkA[true, false, WYl] <- 9.469E-47
		elif 309.018 return
		elif true DvN <- 48.912
		elif true begin
			if true continue
			elif 9.333 continue
			else begin
				## SM&E~,
				break
				## +raeHD=J,~7P"6
			end
		end
		elif true return "4~'"o'""
		elif "K'"" s9[IaiZ, true] <- 3.717e+51
		else return
	end
## _6w
func c2 (var Fg[29e+79], number Pv0[689.758,354,895.706e-42], bool Z7f[7E+69,5.186E-67,4])
	begin
	end
'''
		expect = '''Error on line 4 col 40: var'''
		self.assertTrue(TestParser.test(input, expect, 1069))

	def test_1070(self):
		input = '''
number Yxt1 <- "P3" ## 7t:}Ya"5/?9)X_:z#bJ1
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1070))

	def test_1071(self):
		input = '''
func jR ()
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1071))

	def test_1072(self):
		input = '''
## 3
dynamic Bex5 ## 1qkrsl9%{OJDu:H"3h
func Ww ()	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1072))

	def test_1073(self):
		input = '''
dynamic H8B8[21.505e-80,4E18,53e+06] ## )PAn0&U8bFE;
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1073))

	def test_1074(self):
		input = '''
func nHar ()	return true
## os|>Iaz :b:Ud/X
func zFe ()	return
## JyKU@a8f6U(LOMJ9
## + y<-)q3J6)Ju48H"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1074))

	def test_1075(self):
		input = '''
number nty
func RLlT (number bsG5[79,1.351e48,572.368], dynamic SDjO, dynamic L82)
	return
func qyX (bool vOaU)
	return GY2v
## uF_VkmF`F<PWhIxa]8
'''
		expect = '''Error on line 3 col 45: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1075))

	def test_1076(self):
		input = '''
string w8[6,67.689] <- 93
## H6e4=N~PT cvz @8k.
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1076))

	def test_1077(self):
		input = '''
func MqG (bool s7zF)
	return w7
dynamic fX8 <- 0.632E53 ## !9
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1077))

	def test_1078(self):
		input = '''
func MG7 (var TQn, bool Ust, string IuCf[657.365,323.738])
	return 511

## o
func Aq4s (var PLEp[976.888,335.538,0.890E+23])	return
func us (var W_tx[7E-23])	begin
		## Sl#
		## q
	end

## 3kb^:`R%Y2d275EWv48
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1078))

	def test_1079(self):
		input = '''
func VK (number RI)	return 3.055
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1079))

	def test_1080(self):
		input = '''
func OTBv (number MI, string la[6E+78,16.051], dynamic SOpI)	begin
	end
var Mi_v
dynamic dDMA[526E+21,8e68,80.059] <- 80.316E+70 ## +g[dTtbc
'''
		expect = '''Error on line 2 col 47: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1080))

	def test_1081(self):
		input = '''
func CW (number hOH[52,88.744,291], string XE[584])	begin
		## *rf[01uq"c${Xh
		## ;jbNn9LZ
		dynamic At ## 0`)d)f>L88~oxCa[K
	end

func IZy (dynamic fSSx[1E+54,0E-55,47.977])	return VIhl
func TWcy (dynamic tbh[72.461E96], number RvZ)	begin
		## s@ok
	end

func c5pe (number kLGF[96.298e10])
	return ";"
'''
		expect = '''Error on line 8 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1081))

	def test_1082(self):
		input = '''
var AkAj
'''
		expect = '''Error on line 2 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 1082))

	def test_1083(self):
		input = '''
## 8gEl[C008pc*X0
number jP <- ""|'""
## YFPh!G|i]U|]8FQ]
string iJvH
func hqn (string JRJ[23], dynamic vIt[9.182])
	return "'"'"R"

'''
		expect = '''|'''
		self.assertTrue(TestParser.test(input, expect, 1083))

	def test_1084(self):
		input = '''
## f;G
func dtD ()
	begin
		## ^l
		## ,7U~Ae5v+
		for o2 until false by 4.756e91
			I0E()
	end

## C
func mXB_ (dynamic tvUm, var ccT[4e+41,8.913,0E+47])	return
'''
		expect = '''Error on line 12 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1084))

	def test_1085(self):
		input = '''
func n9yA (number XUY[537.615,95e-21,39], bool OQ[68,32e60,9], dynamic ic)
	return "'"'""

bool Ie0 ## vNV_o:!$J?
## -;w]+xd4v)o.3-._B]
func v93V (var ZPl)	begin
		return
		## b}-Do)
		## 4zdD/h|f<uM
	end
'''
		expect = '''Error on line 2 col 63: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1085))

	def test_1086(self):
		input = '''
## {
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1086))

	def test_1087(self):
		input = '''
## ,z0o(
## Foee| yD^]2H
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1087))

	def test_1088(self):
		input = '''
## q1[t8h.1
func uDgW (var w9a[17.447E+28,284.325E-59,92], number lt6a, number NSE[3.793E+72])
	begin
		## [L
		## nkzx23)w
		## =P48w9iokM`ruAJBha&
	end

## uf
number nPVg[33,7E+47,558.040E-65] ## BFz/ Y
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1088))

	def test_1089(self):
		input = '''
var EN[52.598,6,258e+21] <- "'"'"'"O'"" ## 6,&BC@PB*R!
## DM-
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1089))

	def test_1090(self):
		input = '''
dynamic KlU[383.025E09,56.769e-55,2.404e48]
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1090))

	def test_1091(self):
		input = '''
func Ote (var WY8S[1.624E+78,78.356,5.225e+56], bool rz[321e-75,416.583,3E-19], dynamic WDM)
	return false

## bY4>
## sjz5MG}?rMf4nD4!ic>
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1091))

	def test_1092(self):
		input = '''
func Cr (var r1D, bool JpLT[722])	return
dynamic WZ
func IW (bool DvZ[9E37], string jNH, var JhpM)	begin
		## f
		## "P~=Y^rEdlSzIUBpg#V#
		JPmW(rnj, 917e+93)
	end
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1092))

	def test_1093(self):
		input = '''
func GR (bool Ts, bool ZdO)
	return
## :V3mT8l`xPE]xiuHmZ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1093))

	def test_1094(self):
		input = '''
## G_R}NgQY|%r5{4KFk
## `4?
## X|wLycOh_c
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1094))

	def test_1095(self):
		input = '''
## q::@f.+0eE
string PMK[0.411] ## Jm;,
func Rz (bool sqv[5.691], number yr)
	begin
		## BxJ} bx}{**u
		## _lI4J`:]h g$o2
		begin
			bool ZW3
			eC <- Qw8R
			for xox until xN by ddU
				return
		end
	end
var BX[60.421,51.572e+96] <- 3E74
'''
		expect = '''Error on line 15 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1095))

	def test_1096(self):
		input = '''
string s7[95.143] <- "%"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1096))

	def test_1097(self):
		input = '''
## c`-vfbgPh
func H3d ()
	return
## /MJ#H{tg*M
## {|&o/9sH
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1097))

	def test_1098(self):
		input = '''
## /YI;4fGP%/ziLAe
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1098))

	def test_1099(self):
		input = '''
## WCeHW;ek(GqpaUW6k0
func P7Vp ()
	return

## *6O9?|CX$qmwto^f
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1099))
