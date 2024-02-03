import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_2513011300(self):
		input = '''
func cz (bool RmAr[61e-29,5e30])
	return RTwJ

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011300))

	def test_2513011301(self):
		input = '''
func or (string zX)	return
func nSN (string zZq[2.809e34,4], bool RU, var O8)
	return brR((("M '""))) + dT

func XVfF (var Ge8, bool AS, string ra4G)
	begin
		begin
			## }
		end
	end

## Oze,Wep8
'''
		expect = '''Error on line 2 col 5: or'''
		self.assertTrue(TestParser.test(input, expect, 2513011301))

	def test_2513011302(self):
		input = '''
## N|#2b:HNLa0
## {P 
func yLQ5 (number U1[6.138E-40,772e-05], bool KLD)
	begin
		begin
			## -yZ_jJo:>nrPS
			## }dXdr!qD
			for KC until "'"i<" by t93v
				Rb_("{='"", "'"'"'"E")
		end
		## S/}Zxzwr0=&BGs+V
		## 82<]Hi
	end

dynamic LqJu[8e88,8.241,29E43] ## BX-oc]:HeM
var dwo[149.822e19]
'''
		expect = '''Error on line 16 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011302))

	def test_2513011303(self):
		input = '''
dynamic o2J <- false
dynamic s1[57E-90,201E-94,35]
dynamic X61 <- ss ## Rg$Ok0
var t39[660,72]
## cd,L+`qaY73?
'''
		expect = '''Error on line 3 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011303))

	def test_2513011304(self):
		input = '''
## H
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011304))

	def test_2513011305(self):
		input = '''
## (,)nPg
number M8[311.103e-64] ## +:9I&Y
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011305))

	def test_2513011306(self):
		input = '''
func Xxlr (bool lx[672.867e+55,0.944E32], var MEMl[737.853,19E-73,87.089E+71])	return Kb
bool Han[16,1.995e+09] ## n(2`nb}/~l {{sIB
## 1B9g}Z/HDS1/g$x~P
func zGxB ()
	return false
var ytEr[533,578.724e80,192] <- 26E+25 ## Wyn
'''
		expect = '''Error on line 2 col 42: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011306))

	def test_2513011307(self):
		input = '''
func enW (number xW, var TL, bool ik)	return

## EE4V:[Ur
## RKrtJLn0zSoa
## &ge!5m 0oe+
'''
		expect = '''Error on line 2 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011307))

	def test_2513011308(self):
		input = '''
## F"cu[M"(Ro?,
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011308))

	def test_2513011309(self):
		input = '''
var aXe ## 5}$qS6T`VpV<E
## Xoq
## R3L>UY=&}w%O
## U54
bool bV ## eicb/yqc=]ufL$EAN
'''
		expect = '''Error on line 2 col 24: 
'''
		self.assertTrue(TestParser.test(input, expect, 2513011309))

	def test_2513011310(self):
		input = '''
bool du[697.090E+07,8e-99,574.161e-22] <- 495.974 ## !z$%
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011310))

	def test_2513011311(self):
		input = '''
## 8tn35Ot&6QRjHC$
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011311))

	def test_2513011312(self):
		input = '''
## :.cF/4,xN
## ]LW6NG>JB
## /9
func NEx (dynamic qB0[851], dynamic Kbi[66E+30,57.028E11], number RbJ0[248E-23])	return "'"'"'"r'""

'''
		expect = '''Error on line 5 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011312))

	def test_2513011313(self):
		input = '''
bool Fri
bool f8bt ## C>!b&&3|
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011313))

	def test_2513011314(self):
		input = '''
## ~Rv>V,y
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011314))

	def test_2513011315(self):
		input = '''
func POiu (var un3, bool n8S0[91,38.177e+24,859.555], dynamic al)
	return V6S

'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011315))

	def test_2513011316(self):
		input = '''
string dm ## hY[yRUQ]&.P_3]7+7q2C
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011316))

	def test_2513011317(self):
		input = '''
func C4 (dynamic Zf, string Dq3e[6.294e+37])	begin
		## FKw7-mHKs?c>^[]Y
		break
	end

number WyAj <- "'"'"'"'"C"
number Dl <- true ## )8=e$FQhV5?%
func KJKi (number awj, dynamic Y5a)
	return TJv
func Y1 (var Kg, string alo[2.380])	return "s,V^"

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011317))

	def test_2513011318(self):
		input = '''
## !93H35lKFb_v1%u-
number cFOr
bool l7Y ## !7@n[qS>Dp7Z3uO:>
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011318))

	def test_2513011319(self):
		input = '''
## XiQ1m
func Xpbo (string S8J[855,193,898], number KE)
	begin
		number uAa
		for A0 until 838 by OI
			var STH[18.132e+41] ## #uZx{6b8St
		break
	end

'''
		expect = '''Error on line 7 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011319))

	def test_2513011320(self):
		input = '''
## hMt!v>ELfz{[s=& h4wF
## d&`W4u~C?wC&
## *?q&y/=o3~Tsk
bool FwC <- ";Aj"
var G6[7.914E23,672.300e71,7.192E+34] <- Kp
'''
		expect = '''Error on line 6 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011320))

	def test_2513011321(self):
		input = '''
func EV (number rEQ, var vrf[35.484])
	return vL1Z

'''
		expect = '''Error on line 2 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011321))

	def test_2513011322(self):
		input = '''
## lyJM5b6Y
func NML (bool R4qb)
	return true

func nZqd (dynamic sjuO[44,7,4], dynamic MA, dynamic CZ3S[16E29,4.207])
	return
func Na4 (var iujT[68], dynamic sI)	begin
		## upMnZ%&8BNi{2iFA
		if (77e41)
		continue
		elif (true)
		string ob0o ## ~^1i3NlY3RsEf,
		elif (false) begin
			begin
				## E%}n4!}cs
				## T&k EvBSfVo
			end
			bool RHlW ## xC.s
			Q6c7[BDzk] <- "YIBr"
		end
		elif ("'"") continue
		elif (VH) continue
		elif (true) dynamic Jp4y <- "0'"'""
		return
	end
## ;!Q7]^xa[rU0K+>nb
'''
		expect = '''Error on line 6 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011322))

	def test_2513011323(self):
		input = '''
## )"iw
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011323))

	def test_2513011324(self):
		input = '''
var iay ## fi
'''
		expect = '''Error on line 2 col 13: 
'''
		self.assertTrue(TestParser.test(input, expect, 2513011324))

	def test_2513011325(self):
		input = '''
func tF (bool qpAX[183E07,5], number NSVP[4.899,197e-61,1.563e-45])	return
dynamic XIC[11.993E+89,26.459] ## 2=qT 
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011325))

	def test_2513011326(self):
		input = '''
func xNh8 (var SzD[6e-81,97e-04])	return

func up ()	return jKL

string hp <- "'"'"D%" ## Q7Z{2K&q6,F&m
bool usM5 ## Gy2id&>3g=HE72sLN
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011326))

	def test_2513011327(self):
		input = '''
## JL{E{?:7m
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011327))

	def test_2513011328(self):
		input = '''
## x]0u)y
## m3!9"~>r+ |I
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011328))

	def test_2513011329(self):
		input = '''
var Er6m[86] <- "'",s" ## BG
func ZEgE (string KSyW[905.600], string qye, dynamic tf7[7.196E-88,3,2.284E+94])
	return Hv

func o5 (string bnmD[79.739E-89,9E63,91.049e-31])	begin
		## o]Qc
		break
	end
## w.6xz%VD"Zp$Wp`#
bool nASa[5,66,3.270E+90] ## Z]B/BG&VI/[JW-8t
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011329))

	def test_2513011330(self):
		input = '''
func NeLU (number ytr, bool Qs)
	begin
		return false
		break
	end
number pu_c[26] ## c
func KW5H (dynamic n7iH)
	begin
		## t_8[cE
	end
## zB!uteJ9J({
func ABKM (string kv2a[931,2.799e98])	return

'''
		expect = '''Error on line 8 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011330))

	def test_2513011331(self):
		input = '''
## 2n"$=}A0^OHS;
func Hc (bool LqZ[77])
	return

## 2_[p"(Uc.1
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011331))

	def test_2513011332(self):
		input = '''
func v0Dk (var aWN[875,445e+47,56])
	return HB
## K vD.K@!C&q|/~ImA-p
func eC ()
	return
dynamic HfvA
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011332))

	def test_2513011333(self):
		input = '''
func QAxY ()	return

func z15 ()
	return

func a5 (bool CEf6)	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011333))

	def test_2513011334(self):
		input = '''
func OGih (bool RO, bool zVTL[5], bool A5L[169.359E72])	begin
		for Y08z until EhYe by "2b'""
			var waEi[63.114E18,9] <- kV ## ~r7H&uG#DcV
		continue
		## $
	end

'''
		expect = '''Error on line 4 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011334))

	def test_2513011335(self):
		input = '''
## ~qx$)
## .,/SC1
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011335))

	def test_2513011336(self):
		input = '''
number LbqW <- M5K
## 4>JEV%p2^`|@8
func MyH (dynamic KO[8e10,768])
	begin
		## Q#H
	end

'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011336))

	def test_2513011337(self):
		input = '''
## g`
func GL ()
	return 425.252E-82

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011337))

	def test_2513011338(self):
		input = '''
## zUAJ IVMW26#xf:-
func e5j (var dz[844.388E-27,44.493,489e+50], dynamic gX, string as9s)	return

'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011338))

	def test_2513011339(self):
		input = '''
string eS <- pz ## RC@X,o=M,.R6f]-dAGV
string xp1F <- "'""
func wkP (dynamic XT[7.580E+09,9.275,333], dynamic ff)
	return
'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011339))

	def test_2513011340(self):
		input = '''
bool X8 <- 0
string M_[930E-13,5.675E+91,622] ## r|j-+
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011340))

	def test_2513011341(self):
		input = '''
func d7 ()	return

func GdWU ()	return

## dR>
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011341))

	def test_2513011342(self):
		input = '''
var GSw <- 77e+53 ## [&9HnzF&.4mu
##  s
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011342))

	def test_2513011343(self):
		input = '''
dynamic sJ <- false ## hSTNRmvOQtL5(Y>~*g
func yP (string lr5, number Qh[0e+55,8])	return tI

func ofO2 (bool daJi[939.263])
	return false
string Asl ## NJ)]Ph~1$B^T1.^
## c
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011343))

	def test_2513011344(self):
		input = '''
string yA_ ## DHdnCq
func SYRX (string DO7r[376.430e04])	return
## N2t*
## GvkxC19
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011344))

	def test_2513011345(self):
		input = '''
## nn[Mi?u=7aUSe=g=jl
func tVl0 (dynamic Rz[790e+09,340.463])
	begin
		## Dc8lEV-) W`tP9Q3Q
		nO(56E+42, "'"'"'"'"4", 1.439)
		string XS5k[91e+62] ## /KNzB$V4?U_g
	end

var vX <- "'"'"4" ## T
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011345))

	def test_2513011346(self):
		input = '''
number HV6H <- "'"'"!" ## 5RC4eLJLoF5vl
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011346))

	def test_2513011347(self):
		input = '''
bool B1DA[1e+99,958e68,80.924E+90]
func WV (var qu[55.485E89,8.821], var LI)	begin
		## J6cbgeC;=o;TRF|~3qI
		## 46jn
	end

'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011347))

	def test_2513011348(self):
		input = '''
func gjiL ()	return true

func RP9 ()	begin
		number ZpD <- 143
		continue
		continue
	end
bool C16[698e+74] <- "'"'"'"'"" ## 6W@7}.8${boSE
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011348))

	def test_2513011349(self):
		input = '''
dynamic apm[1.378E+48,72.144,9] ## E/<;?DHOx(BWTY
## m
## xx3`-F$Yx7A!S*,c2+
## ="|jWNSPN?<G:
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011349))

	def test_2513011350(self):
		input = '''
func uExD (var UP)
	begin
		## Gq7h5
	end

## 8I`VM5^Q5|YZ2}6)5
func Sy ()	begin
		## a~[t
		break
	end

func Wa (var pQ1T)
	return "('""
var jfq ## :1i
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011350))

	def test_2513011351(self):
		input = '''
string mQH6[57.933,7e-80] <- Jxs ## ]zg{
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011351))

	def test_2513011352(self):
		input = '''
number w1[14.951]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011352))

	def test_2513011353(self):
		input = '''
number Fjqc[762.838e-01,78] ## xg00J10={9jomx
number CGR1 <- "'":'"'"'""
number Bhcm <- true ## 25U}48r6*
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011353))

	def test_2513011354(self):
		input = '''
## AbjyW|
number Hufi[0] <- true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011354))

	def test_2513011355(self):
		input = '''
## DV_/Q-y~L
bool eX4 <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011355))

	def test_2513011356(self):
		input = '''
bool klU <- aTu0 ## 0:&y#FMqx?O
## b
## O3|QwnR.gwMb0*hZ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011356))

	def test_2513011357(self):
		input = '''
var ve[517.064,31] <- 5 ## QS,!@$%#QPVIt| 
string yRt <- "'"U'"."
dynamic tD[7.821e77,993] ## p2YC>^DW>v6|S%BJz
bool GSQ
number PZ[738.512,30.554e+86] <- 28E77
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011357))

	def test_2513011358(self):
		input = '''
func fvGz (string TMU[33E-54,53])	return MZGA

bool of
func nKUo (var O58k)	begin
		var yc
	end

'''
		expect = '''Error on line 5 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011358))

	def test_2513011359(self):
		input = '''
number q0ob[9] <- true ## ej|`hQ[1R}dMM,5tK";Q
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011359))

	def test_2513011360(self):
		input = '''
## ;$+%
## al$SIU?>ju*z
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011360))

	def test_2513011361(self):
		input = '''
## 7#yo:V
func Ds (dynamic j8)	begin
	end

string xJKh <- 862 ## r{eE
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011361))

	def test_2513011362(self):
		input = '''
## .F)?2!%LM
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011362))

	def test_2513011363(self):
		input = '''
## e#cB_6di2Jxnarv;NSlf
## dk-9l.K5fj}0CD[{Iv>
## ~ps#
func ns (string Fr, var mNs[82.636E-21])	return aFHE
number XITL <- VV ## za[-
'''
		expect = '''Error on line 5 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011363))

	def test_2513011364(self):
		input = '''
func Il9 (var rAF, dynamic hg1s[2,6.982], number W2L[4.081])	return true

func C9 (number GO, var zAl[460e43])
	return

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011364))

	def test_2513011365(self):
		input = '''
bool WxX <- 32.611E-96 ## MS+7g.9mF=>^5C!?
func bHPG (number efHX[774,62,7E+96], number R6h[16,281,5], number GG)
	return CvhD

## awzL,a1G]Tm7bQ^
var NA[647E-55] <- JW ## lWG(~m7:2&j6(S%,
'''
		expect = '''Error on line 7 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011365))

	def test_2513011366(self):
		input = '''
## ~
## DrZSEe?2CE>Lfw^-
bool obz
bool ks1
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011366))

	def test_2513011367(self):
		input = '''
## KK&SSydro,ryqXrh)iu
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011367))

	def test_2513011368(self):
		input = '''
string Jt
## Xf.mw6:WgT7s/
## [)wf,v.
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011368))

	def test_2513011369(self):
		input = '''
## Drui8PaxJH5Vx|
func vCb (number NLRF[9E24,301.346], var hGQ[947e+44,904,37.430e51], bool bb)	return
func lAX2 (number iDQ, dynamic i0f[531,6E+85,11E06], number iNG[328,557])	return

'''
		expect = '''Error on line 3 col 37: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011369))

	def test_2513011370(self):
		input = '''
string XVDW ## i8R`I/ 
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011370))

	def test_2513011371(self):
		input = '''
## %S
## :bPLqox[v|thdR@-
func bH (string tn0[824.700,957], string QLVy[541e-76,0.755])	begin
		## r07gk5>;~C#SoZ>QAF!;
		if ("'"r'"'"") begin
			## #wlBBlmY
			if ("K")
			break
			elif (5) begin
			end
			elif (true)
			continue
			elif (VjI)
			number laM <- "'"'"'"'"|" ## W]#Ovb$(~}d+
			elif (true)
			RH()
			elif (false) for oX4 until fhbj by "#'""
				return
			## @*;dM@?O
		end
		elif ("'"") CPN <- 3.872
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011371))

	def test_2513011372(self):
		input = '''
## x
string pPpb[19.211,3.268e-01,319.552E-09] <- "'"" ## U,$_<@m,PW}#
## ZJ=@)9H@,
func LH (dynamic y45)	return

## }MRRS:Vpr5B}&sJ
'''
		expect = '''Error on line 5 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011372))

	def test_2513011373(self):
		input = '''
dynamic Dzu ## N^~c5C.k
func qyiW (dynamic SY[7], number JFsK[2.705,756], var SG)	return
dynamic bzI
bool AaI9
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011373))

	def test_2513011374(self):
		input = '''
## oGnjF
## 1iu1/
## ,"RbLeHtv)Gsdo1]
func HuC (dynamic l1, var hA[433,420.882E67,46], var vfL[26.101,1.545,0.127])
	return 10e82
func a0bX (bool rn[91.504,943.639e+77])	begin
		gJM()
	end

'''
		expect = '''Error on line 5 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011374))

	def test_2513011375(self):
		input = '''
string C3[5.272] <- false
func S9T (number Ic6w[78.058e10,306e-29], bool Ee)
	return

func kDh2 (bool C_9, bool Ya[643e-21,54E+05,96E13], bool Af)
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011375))

	def test_2513011376(self):
		input = '''
var YJ ## G4~jhz/=z
number VpU <- true ## ;YWd 
func dwq (bool heK, number Rn2, string F8Dw)	begin
		## +N5>|e42</
		for XxwA until "m" by false
			begin
				if ("'"'"3")
				return
				elif (39E+17) continue
				else Pc9(js, false, "?'"'"")
				begin
				end
				## @
			end
	end

var EvG[22.820E+50] <- 59.643 ## U!%]JU=G
'''
		expect = '''Error on line 2 col 19: 
'''
		self.assertTrue(TestParser.test(input, expect, 2513011376))

	def test_2513011377(self):
		input = '''
string eGp <- "'""
dynamic mTxc[5.549E+61] <- 9e-12 ## -m,|EEEUAGv?;g8<B
## %Ct0XDS{t;WAg-{i
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011377))

	def test_2513011378(self):
		input = '''
func Xoz (var Mo, number IC[0E+61,71.104,16], var hs)	begin
		break
		return true
		for zpT_ until ")'"j" by true
			u3("*'"", true, true)
	end
dynamic Fc8
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011378))

	def test_2513011379(self):
		input = '''
bool Jn
## UWNS5k4PDD
## j
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011379))

	def test_2513011380(self):
		input = '''
func VW_ (dynamic Fj[26.823E+31])	return "'"'""
dynamic WQYd ## >Hm#Fz
## :"vZ&|oarkJ]TX4kDvgI
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011380))

	def test_2513011381(self):
		input = '''
string A0[2,7e-69,40.919e+98] <- ZB
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011381))

	def test_2513011382(self):
		input = '''
string zQ
## $v#2@EA-By=]&2K6
number aKu[271.106,32E+52] ## pT+WRc>Z"7|-4*
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011382))

	def test_2513011383(self):
		input = '''
## P5/ta<cCyLg}%[mBDnmI
bool MsC1 <- 3e40
bool Tx5 ## ~di5B
func Sly (var eZ)
	return

'''
		expect = '''Error on line 5 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011383))

	def test_2513011384(self):
		input = '''
func jpy0 (string Kzi[729.552e37], number iU5)	begin
		## 0D(q, drS ,QDEbx
		## |1c3.!H
		## jDY#>2@GFF
	end

number hfW <- 92.584E54 ## BD||)SD;Q;?(
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011384))

	def test_2513011385(self):
		input = '''
string EP[0.439E-84,3.666E-98]
number B2E[92E89]
## rYI!
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011385))

	def test_2513011386(self):
		input = '''
func sbQ9 ()	begin
	end
## @F:_W:Yk*96g,Bw#*
func h7PR ()	begin
		## -#zo
		begin
			begin
				if (929.146) i19(ATk)
				else eu[true, 3, true] <- 87
				return
			end
		end
		string ez5[21.900,4E54] ## ?8y+Vsdi7F#FQ2p
	end
## ,u}`"HRVsPsclI|R$y)i
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011386))

	def test_2513011387(self):
		input = '''
func KFPA (number Edp, bool S0[38], number uQq)
	return

func g1j (bool Obf[822.641,6.204,74.705E+84], var ON, dynamic ByRi)
	begin
		if (UYh) continue
		else for s2b until Na by false
			number zsVD ## B5K^Llj"E.,HE:
		## 2br/#4[K+iK?4{6[9
	end
## ho)vak3,841k0"ucp
'''
		expect = '''Error on line 5 col 46: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011387))

	def test_2513011388(self):
		input = '''
func PM (string uL6[509,12])
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011388))

	def test_2513011389(self):
		input = '''
## |WY"b}}z
bool ZE5I ## 4NeRZ=/o&
number jf <- HOIO ## 8Y XL3M&&4Ywr%#
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011389))

	def test_2513011390(self):
		input = '''
## p(OFTYqBssM_"YXJavC
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011390))

	def test_2513011391(self):
		input = '''
func by (var pm[544.858E+41,83])	return

## H/>T|RdB^8$>GM
var w307[2E83,905.809]
'''
		expect = '''Error on line 2 col 5: by'''
		self.assertTrue(TestParser.test(input, expect, 2513011391))

	def test_2513011392(self):
		input = '''
bool No1 <- 88.097
number FO[56,4e+85,185.398e-50] <- 5e75 ## He/ ,8J0Z
func rEa (bool P4[378,527E+16,2])
	begin
		## UFo:o
		## [(Pcq`Hj
		for IH until true by "<'""
			return
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011392))

	def test_2513011393(self):
		input = '''
func ZIpc (bool z6HM)	return 74.889e47
## _pt
func HNW (bool d1m, dynamic kDbZ, var NHme)
	return
string hHo[3.240E+48,7.457E83,1.919E91] <- true ## K!O$0BXNOg {AhZGiNr=
var ABS8[54.524,12E-29,1.999E+39] ## #:Df
'''
		expect = '''Error on line 4 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011393))

	def test_2513011394(self):
		input = '''
## &i`<$td> k1~4z|
## S&>l+ppGXeZ$*zPP
func xYE (number nC1[3.933,54.744E+89], bool qo, number rjq8[1E36,89.625,388.556E32])	begin
		## _duZ
		begin
		end
		## FL"f[jR##YCe
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011394))

	def test_2513011395(self):
		input = '''
func o0GY (dynamic S7f, bool GEpA)
	return false
string iiPd[67,581.002,23.009e-83] <- "kk0'""
func DBA (dynamic kA[70e-11,70.999], dynamic kZU[2.927], string wez6)	return true

func tfRK (var MrW8, dynamic yo_J[1,56,7.823])	return
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011395))

	def test_2513011396(self):
		input = '''
func ON75 (bool Bu[16E-56,72E03])
	return p42

number RrO[110,2E+61] <- "o'"SHY" ## d."f-e
func JgSM (dynamic BppP)
	return "'"4d^'""
## v)Ro6&C{xi}j?%h
bool FrPt[4.058] ## D0O=1Oak-3?)H=
'''
		expect = '''Error on line 6 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011396))

	def test_2513011397(self):
		input = '''
var i0[849.897e-86] ## I}r^l5wF3:y
func FH6 (bool JeF5[45.023], number QJ[564.318e+26,11.171])	return
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011397))

	def test_2513011398(self):
		input = '''
func UmJz (var EGnb, var pWN)	begin
		## c829Xbznsq[9kz7o
		begin
			## .2z]*u(vgAizwOHW?
			## B~K
			## hq)/*6Dgy)Ue?!
		end
		## Gi_x,QEAI>ZT^IY~
	end
## jd";P
## U
func Eq (number niqA[287.090E-26,4.323], number fe, var i8y)	return
number GVSf[98,57.164,89E53]
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011398))

	def test_2513011399(self):
		input = '''
## zY/3C@#I"B4
string Yh36 <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011399))
