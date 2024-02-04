import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_2513011300(self):
		input = '''
## c
dynamic U49[743.532e-25,64.868e-03,5E81] <- k5[BQh, 966E96] ## 6dG7?G`B:|jR
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011300))

	def test_2513011301(self):
		input = '''
func HTO3 ()
	return "0`"
bool Ppy[427,95.293E41,9.618e+67] <- "'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011301))

	def test_2513011302(self):
		input = '''
## c
## C)Xayc9b2`OA
## SLETHD{k1qm3GN:QXbO
func sSa (var Te9)
	return

'''
		expect = '''Error on line 5 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011302))

	def test_2513011303(self):
		input = '''
func TP3 (dynamic w0)	begin
		## ,WkIPQwZ0xN@J
		## `S18J+u6dz:-`{Ez[
	end
func AQ (var Rz5)
	begin
		## 7$M-
		## 3S(L_ZkK.$Zaz
		return "'"I"
	end

## CU,.Y^XUqh
bool kdN <- 4e-27
## |6(~Xzd}*"b<8lj,*m
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011303))

	def test_2513011304(self):
		input = '''
string a0L
## >vUHZ5zIppC`u
func Zt (bool ZS, string jN7R)
	return

## 5U#*2)li
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011304))

	def test_2513011305(self):
		input = '''
## 5i~vi`Vfs
string Lm6g[4] ## Qg
number h_GF[170.313e+03,124] <- true
number T2Q ## _|q
dynamic VtZE <- 951E+18
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011305))

	def test_2513011306(self):
		input = '''
func feCO (string MC6[796.453,4.826,4.292e-62], dynamic Bl[511.190,503,105], dynamic El)	return
## *`GXSkd<u?tyyn
var aL[26E+55,55,281] <- false
func y_ (var vOi[77.461e72], dynamic IZY)	return "'"'"9'"("
'''
		expect = '''Error on line 2 col 48: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011306))

	def test_2513011307(self):
		input = '''
number sx[891E-85,58.714E-01,81] ## h$ahGtF:GZDfX
func NLVj (var VZ[805.023,996.278e-37,39.232E-89], var IibM, dynamic Qo[6.103e45,44.975E+09])
	begin
		## @,&!%m~i,a@rpM`n&A
		return
	end

func LV8 (string Xlt[91], string FW[9.683,55e-91])	return
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011307))

	def test_2513011308(self):
		input = '''
## 8yn_ez,(:?
func Zk ()	return 50e-78

func b7oG (var vd[790e+46])
	return
var QYmz
'''
		expect = '''Error on line 5 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011308))

	def test_2513011309(self):
		input = '''
func SF (dynamic P8bR)	return "'"k'"Q'""
func JPVW (string JRM, dynamic Rz67[71,504e12,34.803])	return ",'"8'"'""

var cNZ[9.999E99,329.424,389e32]
bool rLVm[5E98,4e+94] <- 900 ## &8`A3
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011309))

	def test_2513011310(self):
		input = '''
## AzNpQ[&/8>v?JO)6L%:v
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011310))

	def test_2513011311(self):
		input = '''
## Y}@#^5
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011311))

	def test_2513011312(self):
		input = '''
string W45Z[567.934E-40,2.447E-95,6]
## 6d2bN0),qW-c&X
bool JDW[472.607E-52] ## irF.2!Kk0~%dE1q6HS
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011312))

	def test_2513011313(self):
		input = '''
func wkFY (number GZ[59.253E24,3e+15,41.441], string mNqr, string nwCI[7.540e73])
	begin
		continue
		## ()BjA{Jj|oIi
	end
func Gmln ()	return Bruw
## &m,sbHi#9f5d<j:{`!|
## ^8E_o"v
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011313))

	def test_2513011314(self):
		input = '''
## D}.P:
bool B1k[697E94] <- "inB" ## fnA<ThjcP
func yb (bool Q4)	return l2

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011314))

	def test_2513011315(self):
		input = '''
func OsS (dynamic iPSB[7.599,93.540E24,8e+56], string nGZ)	begin
		## ElM
	end

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011315))

	def test_2513011316(self):
		input = '''
string mr <- "q'":m>"
var ck1[94,222.404E-48]
var D_x5
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011316))

	def test_2513011317(self):
		input = '''
func BA ()	begin
		## 16
	end

func nM (dynamic TY[79.112E+43,8E-95])	return NgrN
'''
		expect = '''Error on line 6 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011317))

	def test_2513011318(self):
		input = '''
## 5"w;thHQ
func YOO (var yWpV)	return ma5

## sM #M&ZEzGf
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011318))

	def test_2513011319(self):
		input = '''
number q4w ## $DVI`UH
string t7 <- 39 ## t`j|qpW_}Nl|Zs2E|T
func Ix ()
	begin
	end
## V&pH:]crv{y
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011319))

	def test_2513011320(self):
		input = '''
func cz5 ()	return
## {U=DF,S^n7
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011320))

	def test_2513011321(self):
		input = '''
func j3vC ()
	return

var RmHg[571] ## t z
'''
		expect = '''Error on line 5 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011321))

	def test_2513011322(self):
		input = '''
func u8 (var KCt[81.099], number GjPh)	return "'"'"EXg"

'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011322))

	def test_2513011323(self):
		input = '''
func CNu (var cEB, number Kt[26.917], dynamic QxdS[1E-80,9.001,625])	begin
		continue
	end
func F5 (bool dtj[3,94])
	return
func GiUX (var jjS, var yL, var he[3])
	begin
		## &)S-`(nDxK1
		begin
		end
		## 5T1.!nRa
	end
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011323))

	def test_2513011324(self):
		input = '''
dynamic QQ[8.024E-68,55.189,88] ## ZZ`*8Q)!K2X
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011324))

	def test_2513011325(self):
		input = '''
## ;t`!U:mU:s@9${O
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011325))

	def test_2513011326(self):
		input = '''
func vFea (string jZE4)
	return "'"W'")"

string f00f[5e16,57.106,59e-66] <- "'"y"
func Ah (string biD[4,36e-10,944], dynamic JS)	return false

'''
		expect = '''Error on line 6 col 35: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011326))

	def test_2513011327(self):
		input = '''
func bKXY (bool pcN, number Zo[6.158e-72])
	return true
## ;fB*^
var N3[81,9.909E93] <- true ## NYY$(D}n
## xhdun_*RM:m[h@FQ
'''
		expect = '''Error on line 5 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011327))

	def test_2513011328(self):
		input = '''
var SNrl <- "'"AN'"!" ## r
func e6y (string IJfT[27,100.608E+81], bool NKZ[18.105e62,79.206,956.786])
	begin
		## 05^j9{jM}
		W03g <- UK
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011328))

	def test_2513011329(self):
		input = '''
string lc_i <- true
func jV (bool cNp[51.796,58.470E+18], bool o4W[58.757,2])	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011329))

	def test_2513011330(self):
		input = '''
## uPsfSbJ|@_5Gpr,f
bool FDZf[850] <- "U"
## a[/a6oF
string O9H[12.900,885,66.325]
func Je ()
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011330))

	def test_2513011331(self):
		input = '''
func RekW (string yCAp, bool ui[602e+81,67.658E+21,888.930])	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011331))

	def test_2513011332(self):
		input = '''
## f0f
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011332))

	def test_2513011333(self):
		input = '''
func oXj8 (var qjME[904.266E33], dynamic bb[240.675E+64])
	return "'""

func jk ()
	return

'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011333))

	def test_2513011334(self):
		input = '''
number RpC[139.475e-56]
func RfK (dynamic FK)
	return

'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011334))

	def test_2513011335(self):
		input = '''
func c5d (bool JUb3)
	return 39.624
func bN4 (bool WYx)	return

func p3 ()
	return 975.267
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011335))

	def test_2513011336(self):
		input = '''
func vc (string kV7)	return

bool GC3i[9.398,5E+40] <- "'""
func aBX ()
	return false

func bR6 (number HLY9[0.975,832.673E+08], string VH[594,6e-88,7.662e+57])
	return false

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011336))

	def test_2513011337(self):
		input = '''
## bVk+H]:tf6Wl9 <*HK
func woz (bool S1[44.062], string SB[34.268e-44,82.949E21])
	return "tjW"
string bNl[8e+45,4.105e31,45] <- false
number yO
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011337))

	def test_2513011338(self):
		input = '''
bool nqq5[1] <- true ## <VE#s*tF>ST"
## Ius*mZ|A]U7j%
## O[yh%PVqcH&3;Pr
var hjA
'''
		expect = '''Error on line 5 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 2513011338))

	def test_2513011339(self):
		input = '''
## <tW-1h kOJ^*@6|wA
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011339))

	def test_2513011340(self):
		input = '''
func AZu_ ()	return au_

func QO5 (var disV[5.973,6.532,991.201E+85], number Blj, bool Lpw)
	return true
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011340))

	def test_2513011341(self):
		input = '''
func dkJ ()	return false
## }&QTG?
var Tl[2e+75]
bool wekB ## JQ?sP5
'''
		expect = '''Error on line 4 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011341))

	def test_2513011342(self):
		input = '''
bool NV <- lOal
bool Eo[23] ## CsCjGqg7
func t0Z2 (var GD)
	return R2CY

'''
		expect = '''Error on line 4 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011342))

	def test_2513011343(self):
		input = '''
func Gw (var w8h[1e-72,33.835e-06])
	return
## *Z8=I
func QIR (number Vw[5], number uZSm[73.458], dynamic wk[42])	begin
		pL0()
		for oI8i until HD by true
			break
		yEYj(ZO, 79.549E+92)
	end

##  9>W7bB)
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011343))

	def test_2513011344(self):
		input = '''
func jn (string hdc, var A9Lw[87.898,8], bool uvs)
	return 58

dynamic HGa <- mN
dynamic K5ks[571] <- "]m'"0@"
'''
		expect = '''Error on line 2 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011344))

	def test_2513011345(self):
		input = '''
bool cVp ## q`@0=&m:TTS1,_ld2"
var hg[7e60] ## @6heKhQojVA7 ,p6s
func irmQ ()	begin
		## Y=<k$V"PqBHo.@
		if (P5)
		break
		elif (",:v'"")
		return Ox7
		elif (VmCp) break
		elif (Jto) iST()
		else continue
		continue
	end

'''
		expect = '''Error on line 3 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011345))

	def test_2513011346(self):
		input = '''
## U-#qI#N%dYh3_xU
number g8 ## m}fB]
## Se!$F949<*(qm*H
## 0+jT<(I))Iy
string KvZ0[99.544E59,52E+24,2E-97]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011346))

	def test_2513011347(self):
		input = '''
func U2_k ()
	return Dp0
## S$Bt5R1;K_|e
func ZHN ()
	begin
	end
var ox <- 574.445E-56 ## Ft.&AT]oo5
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011347))

	def test_2513011348(self):
		input = '''
## LIw
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011348))

	def test_2513011349(self):
		input = '''
## i
func E0 (bool MoD, string qgjP, var pp[9.806,526.666])	begin
		## WY%gqL~1`|];]&Dmq@
		gKTB[jZ, true, 244e-68] <- 893e-20
	end

'''
		expect = '''Error on line 3 col 32: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011349))

	def test_2513011350(self):
		input = '''
## @`-2"B
var ra[54e-71] <- false ## _D+VxE
'''
		expect = '''Error on line 3 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011350))

	def test_2513011351(self):
		input = '''
## G#Al?#@W
## kvwA.KD.tqK_)BUD0$
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011351))

	def test_2513011352(self):
		input = '''
## J1#+F0
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011352))

	def test_2513011353(self):
		input = '''
func Oj (var Y6, var v60[575e81,163.892e-11], number ron)
	return

func Sev ()	return

## _}!a^|8Od
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011353))

	def test_2513011354(self):
		input = '''
var xXo
## _!14
## fuR6x%
'''
		expect = '''Error on line 2 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 2513011354))

	def test_2513011355(self):
		input = '''
## >)%34
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011355))

	def test_2513011356(self):
		input = '''
dynamic XGs8
bool RY[333.365,71,152E-82]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011356))

	def test_2513011357(self):
		input = '''
var Uur ## =U|dVdGq^lAV5MsG)&8T
'''
		expect = '''Error on line 2 col 31: 
'''
		self.assertTrue(TestParser.test(input, expect, 2513011357))

	def test_2513011358(self):
		input = '''
## qdih~3gpm_
## z1&@I@,9*JLhCbYOu}F
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011358))

	def test_2513011359(self):
		input = '''
func JDi (dynamic c4qd[4.491e+92,5.008E+78,12.192], bool qQb[86e+67,97], dynamic UT_[798E-72])
	return "W"

var Y1Vu[48e+21] ## $2S;hBElSmd6?}gYLQyH
## M64nuJRU_bg%kei
var zUHq[79.484,2.453e41,96e+32] <- "'"'"b'"'""
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011359))

	def test_2513011360(self):
		input = '''
func Bp_ (dynamic kQ, string wiH, string JT1m)
	begin
	end
number qNp ## T
var ZaLf[42.921E92,288.065]
## N^n
## ,u%`
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011360))

	def test_2513011361(self):
		input = '''
## j&|C.{V
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011361))

	def test_2513011362(self):
		input = '''
var jzS[653E77,126,807.920E+84] <- false ## s
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011362))

	def test_2513011363(self):
		input = '''
## ?w
func pM (string NEXf[777.283,8])	return ALvH
func baNV (var MYHh, string j2Y)
	begin
	end
number P4g[8.043E-63,1.630E-27,2.777] <- eG ## b<$: J%%"9iJbN0E=4_
dynamic rDFx[585.286,2.677E68] ## /u}VH*R0F~.7CUBX$ul,
'''
		expect = '''Error on line 4 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011363))

	def test_2513011364(self):
		input = '''
## r5KBr"hkQ!
func wi ()
	begin
		## IX4Z@G$MPP1N4z~l@
	end
## HF"dAK(m,
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011364))

	def test_2513011365(self):
		input = '''
## P|Ks6q
func AIk ()	begin
		if (xj) NLd0 <- YbV
		elif (true) break
	end
## t)i
## SXm:yEB<Q6A
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011365))

	def test_2513011366(self):
		input = '''
## } 8Z2?hYD[#v.
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011366))

	def test_2513011367(self):
		input = '''
func qt ()
	begin
		continue
		bool hCp[3.731,4.715E+97]
		begin
			ULXT <- kH
			continue
		end
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011367))

	def test_2513011368(self):
		input = '''
dynamic Rud[15.642,5]
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011368))

	def test_2513011369(self):
		input = '''
## <Br
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011369))

	def test_2513011370(self):
		input = '''
number ZIp[315.493E-95,65] <- "+/'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011370))

	def test_2513011371(self):
		input = '''
## 4KDE5
## +.r%gw%Y
func VD (dynamic qHC)
	return
'''
		expect = '''Error on line 4 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011371))

	def test_2513011372(self):
		input = '''
var pVO[749,27.891,601.103E+64] ## 6=:3xwqT
string t71 <- j9
## t_/vl/mdB26%hFWJs<
string arhj[0e-72,2e36,290E-65] <- false
func Rjm (number iVg, var FE[202e85,735.057e16], var sy3[149.842e-43,509,12e-80])
	return "*'"V'"g"

'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011372))

	def test_2513011373(self):
		input = '''
func Ej0 (dynamic Iu[5e28], bool qqm, number Z3w[6e26])	begin
		## "(4!6n~vlcW
		## 3vcOwzrI/!)<]^Hk
	end
var Yb3a ## i;z0=A&
func U9h (string zBdz)
	return aA
## &q&gh&LSfeFH(CM
## j6HoDQub([q_r^
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011373))

	def test_2513011374(self):
		input = '''
func a75 (bool lJbh[1,601e-90], number uq)
	return

## rhM%R
func NeLd (dynamic ZSd[1e-76,232.583E+79])
	begin
		## 8DFnC
	end

dynamic cS[57,27,585.217E+72]
'''
		expect = '''Error on line 6 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011374))

	def test_2513011375(self):
		input = '''
var dJw8 <- 0.624E23
string H6
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011375))

	def test_2513011376(self):
		input = '''
bool QE[2.900] <- 3.990 ## R#fH$YN(8 %6$(Sh+fN
## Fd6srtJ.$swjKAFd]x@
bool dW[66,41] <- AJaL ## "ngJrCT
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011376))

	def test_2513011377(self):
		input = '''
func NbL0 (string BCZK)
	begin
		return 921E+61
		begin
		end
		## -ll=
	end
bool wk8R
number dZw[0e18,81.699,37.787] <- "'"'"8" ## 2PS
## ,HY8x{
func MN5 (var R4Z)	return
'''
		expect = '''Error on line 12 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011377))

	def test_2513011378(self):
		input = '''
func Jk (string trR7)
	return 597e09
func yf (string hb, var pAo6, var z0)
	begin
		hBU <- 656E+68
		for RrA6 until 688E+20 by 8.227e51
			if (true)
			uZj <- "('""
	end
string cs <- false
## JEbH.q73~tl}WbCg.T
func JPe ()	return "&'""
'''
		expect = '''Error on line 4 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011378))

	def test_2513011379(self):
		input = '''
var Mo <- 759.249E40
func Hk (number pAP[4e11,227,1])	begin
		## RV^a7%lJ;mrxW{-)rjd
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011379))

	def test_2513011380(self):
		input = '''
var QP9[1,7.203,65e-73]
## D!jL>~vxOo1ny_z
## kA"Nj $Gc)&^
func GoCW (number fYKM)	begin
		EtJJ(HZI, "C")[true, d23U] <- VS
	end

'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011380))

	def test_2513011381(self):
		input = '''
func Dl (bool tgI, bool jD)
	begin
		return
	end

## x13B/]7T4vlX9,
func Gu (number ILBz[5.425e-82,1], var NTl)
	return

string Xe2z[766.861E45,853.280e-37] <- 8e+26
## czp|)hA&:/BkGj NJ
'''
		expect = '''Error on line 8 col 35: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011381))

	def test_2513011382(self):
		input = '''
number RRqc[6.785E19]
func NSf8 (bool wLHk, string n7QK, bool U5V[884.210,10.357])
	return
number iH
## gzt<M?B|]yhfiX9gs
bool GMp <- 47.579 ## `a+- wJZq
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011382))

	def test_2513011383(self):
		input = '''
var wF[84,47.641] <- 82.805 ##  Al&V5bt!8Mr+p=.I@o 
var NGcj ## [Hm*7M=%X n?
## 4kHSb;>)`[I}l0J5F
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011383))

	def test_2513011384(self):
		input = '''
func r99 (bool jX8[0.918,808e+39], dynamic yj[862E+33,670.280,6.434e-54], string Ci7)
	return

func BZq_ (dynamic T5Cr[42.031E68], string x2P)	return
'''
		expect = '''Error on line 2 col 35: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011384))

	def test_2513011385(self):
		input = '''
func t8dJ (number zvu[154e+61,24.498E89,437.331E-42], bool sB0[3e+77,58.142e-42,880], dynamic Hga3)
	return

'''
		expect = '''Error on line 2 col 86: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011385))

	def test_2513011386(self):
		input = '''
func zA1 (string vSKd, string drLB[501.456E+51])
	return

## V=)1Ft`-MWx*
## ob
number zWZ
func ENl (bool my[9e+79,423,18.389E+88], dynamic u235[59.938,442.948E-47], var kQY[22,366.278])
	return
'''
		expect = '''Error on line 8 col 41: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011386))

	def test_2513011387(self):
		input = '''
func Q23M ()
	return gj
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011387))

	def test_2513011388(self):
		input = '''
dynamic Ci <- true
string Xqd
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011388))

	def test_2513011389(self):
		input = '''
## -{$-i-Kgk$w
dynamic Bk ## ?L
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011389))

	def test_2513011390(self):
		input = '''
func AZ (var CN7[7E+47,31.132e-96], bool nvgm[431])
	return

func CXa (string Gmo[86,42E+56], number Zesg[32.118,55.284e-90,378e-30], var OQCu)
	return
func cYt (var JL0n, bool MDM, bool mej)
	return 9.397
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011390))

	def test_2513011391(self):
		input = '''
## CfHodm-~p:q+oXTZ&
func cpi (string rbtC[62.902e+35,5.466E82,73.722])
	return
func vl (bool Ky[7,3])
	return
func Qydp (var RBU)	return
## F_=)I9+R ;=^2
'''
		expect = '''Error on line 7 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011391))

	def test_2513011392(self):
		input = '''
func Xd9 ()
	return Cl3w
func hMf (bool xRvB[45.973e95,4E+53,9.537E-54], string TOx[714], string qZ)
	return 9.486E-97
## ]$SdP$=3JI|RWGT(I
func J4 ()	return false
number xtDn[435.149e-67,8.591] <- 9e+53
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011392))

	def test_2513011393(self):
		input = '''
func Fgt (number jRH6)	return
## 1AW8@o*r&c&vkobK{}
func gD (number Zspv)	begin
		bool XX[4E-14] <- true
		vMVW <- false
	end
func w2I ()	begin
		## inINVBQJP!/NZ
		## n33$Yf:oz)0CM>[d3|]
		string dwA[74.445e+00] <- "x/a'""
	end

## UiDEU,h<A)&;O
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011393))

	def test_2513011394(self):
		input = '''
## O>Iv
func T3b ()	return 0E-60

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011394))

	def test_2513011395(self):
		input = '''
var Wgf[9.728,5.602] ## ]E8ZH38*b%GaM8>qy) 
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011395))

	def test_2513011396(self):
		input = '''
## %`c{2d$h@
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011396))

	def test_2513011397(self):
		input = '''
func foz ()	begin
	end
func nEd (string Alo)	return DEoz

string bqN[40] <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011397))

	def test_2513011398(self):
		input = '''
func iOt (dynamic gFnf[60.029,3], dynamic zCj[482.790], bool s0m[203E89])
	return

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011398))

	def test_2513011399(self):
		input = '''
bool Eb_[1,618,896.236E28]
## YM&fdx>k_8G
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011399))
