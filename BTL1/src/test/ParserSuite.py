import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_2513011300(self):
		input = '''
var aPHW[84E-51] ## #<kDU` u}gEaM5X~Nf 
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011300))

	def test_2513011301(self):
		input = '''
## 5WLW
## )!g/YIX^G0_x
## Zp1gQ;2_t8yoc0N"~}B
## 3a,+"uTV&C!8E[F8
## #Y@2w>qU#+yF`=Afa
'''
		expect = '''Error on line 7 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011301))

	def test_2513011302(self):
		input = '''
## gSr
dynamic FFQ <- oY5W(NAS(bhB2(not ("12Q"), true, "4'"")[79, true], "'"'"'"R6"), 487e+75) ## NhQc}0;_?NpBMurQ8`I
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011302))

	def test_2513011303(self):
		input = '''
## -
func XO (number ZQ[95,5.568e36,8], number yNcf[7.823E+48], number Jx[3e-80,0])
	return

## t >+{4yx1HDvK0oiB_ 
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011303))

	def test_2513011304(self):
		input = '''
var lSJV ## ?5r,eJI[:VXZ
func Pzfo (number YZ[59.865e+64,372.762,746.987e16], var swme)
	return
## (*(]&/)UrN<rJ/
number vXB[24E73,357.950e-37,5]
'''
		expect = '''Error on line 2 col 24: 

'''
		self.assertTrue(TestParser.test(input, expect, 2513011304))

	def test_2513011305(self):
		input = '''
## "X#U;9rUuwf[dVH98_y!
number BG[99E-11]
string itDe ## RD
## jQxdDq$t)}_qKY
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011305))

	def test_2513011306(self):
		input = '''
## [[
string I5 <- WY3D ## >/]:
number M6P4[66.001] <- false ## eAg
bool xzui ## J`(L26_ 
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011306))

	def test_2513011307(self):
		input = '''
func CmOj ()
	return "'"z'"'"f"
func KUJ (number w1P9, dynamic WKEi)
	begin
		for Gpu until false by 2E-38
			dynamic oDi0
		begin
			## . SNm=
		end
		break
	end
## 7r$zHbA<h1"gCs?P.2l
var yWrW ## L0bAcIqt#c
'''
		expect = '''Error on line 4 col 23: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011307))

	def test_2513011308(self):
		input = '''
dynamic ke[224,854] <- xQ ## bE
func cJhC (string vl4, dynamic yU)	begin
		number Mh[3.592E77] <- GMm ## |}f4FG`yP+)f+
		## K ]Q1=?jy|:eIZoJE_`
	end
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011308))

	def test_2513011309(self):
		input = '''
string Vnzu[52e+54,7.690,3.160e46] <- 5.508
## x?3[~Y@9mu
## <ed(+Z!di]6Ko%
## 24ghiV#+2EAZ"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011309))

	def test_2513011310(self):
		input = '''
var p7 <- 40 ## e
## +Y.G0JjOG}cIrm
func Oec4 (bool FS[1.242E-78])
	return false

## f_]t1#;.qj:8#zh1,
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011310))

	def test_2513011311(self):
		input = '''
number hD8[9] <- sm ## d</Q<Gg]S,/}+(+J
func BfG1 ()
	return false
## >k-4TW[ko`{c<P>[- S
func mBl9 (var oD, var mk[161.171E-68,9E89,49E+40], bool qjM[152E72])
	return rT

func W5OS ()
	return

'''
		expect = '''Error on line 6 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011311))

	def test_2513011312(self):
		input = '''
## &4
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011312))

	def test_2513011313(self):
		input = '''
## GVO(Z
var R0TJ[5.366] <- DOZi
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011313))

	def test_2513011314(self):
		input = '''
var gBiK <- false ## }
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011314))

	def test_2513011315(self):
		input = '''
func OSTN (dynamic mzfB[9,8e-42,9], number tFpf, bool tnNx[5.846E-51,410.827e-69])	return 65.591
number N13[233.951,78.704] <- "yydO'""
## G2I?SNN"*
func D0X ()	begin
		return 47E-74
	end

func BuO (dynamic Dt, dynamic oJzk[804,31E99,524])
	return

'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011315))

	def test_2513011316(self):
		input = '''
## >ov3b
var n0SL
## VkqkO|oB
func to (bool aRZB, string nC[31,0.480,1.226], var M6Hp[9E-88,436.926,64.202])
	begin
		begin
			## b
		end
	end

'''
		expect = '''Error on line 3 col 8: 

'''
		self.assertTrue(TestParser.test(input, expect, 2513011316))

	def test_2513011317(self):
		input = '''
## 5=Qc>7flUI/q
dynamic s0q[5] ## QzBzB@a-pA3
bool sF ## k3U0(+fi|IQss
dynamic ckeg
## 3!3Es
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011317))

	def test_2513011318(self):
		input = '''
func gr_S (bool IcBY[4e+92,910.068,3e-80], bool vs_y[7.541,1,614], number rZ)	begin
		if (true)
		var rV[5E-77] ## K5a7x$mnMa1RY>>
		elif (af8e) for Nqm until 0.595 by ",'"'""
			return "*'""
		elif ("'"'"") continue
		elif (17E-75)
		break
		elif ("=?'"")
		continue
		## !LG_rd6`sdT!gY
		return 54.077E25
	end

func dAP (string WP)
	return

'''
		expect = '''Error on line 4 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011318))

	def test_2513011319(self):
		input = '''
dynamic a2[9.077,715,1.820e-42] <- 93
func Dygi (number OgQa, var LM)	return "'"'"'"RN"
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011319))

	def test_2513011320(self):
		input = '''
## @M)CPa!b#e${#8+bCID
## 62T+>o
func OWo (string h9k[99,0.754,87E00])	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011320))

	def test_2513011321(self):
		input = '''
string rgJ[2,5E55] <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011321))

	def test_2513011322(self):
		input = '''
string bo <- 210e09
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011322))

	def test_2513011323(self):
		input = '''
## PnoCq,? "4-9>ecA9q[
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011323))

	def test_2513011324(self):
		input = '''
number omHU[4e+27,1,342.980] ## F3X;>
dynamic Bw ## uA
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011324))

	def test_2513011325(self):
		input = '''
## 2uO.P %X.= *Xt
var Gc <- false
func ezjD (string wk[29.978e-15,7e-67,285])
	begin
		for lp until false by "'"'"'""
			bool RJMr[622,564.747] ## .pb(bx5!4$
		for pE until Yh by TXDx
			FIc()
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011325))

	def test_2513011326(self):
		input = '''
func Xet6 ()
	begin
		begin
			if (false)
			for DPS until true by "'""
				continue
			elif (false) break
			elif ("A'"'"]'"")
			begin
				for WW until 1E-97 by 32
					Noez("o'"G'"", true)
			end
			elif ("'"<,c") for nm until rj by 46E-75
				i0 <- 4E-90
			else for XM until Nkiv by w4Ie
				lD3()
		end
		number ww <- 6 ## ,z301VA
		## js!{;L[F4SynOD
	end
var UUx[40]
'''
		expect = '''Error on line 22 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011326))

	def test_2513011327(self):
		input = '''
## [{nO#
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011327))

	def test_2513011328(self):
		input = '''
number qH
func KXf (dynamic Tp[326e92,35,6.074])	return true

string XB <- 3
func ylrW ()
	return
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011328))

	def test_2513011329(self):
		input = '''
bool mm6S[319,817.050,299]
dynamic TkX[304E+68,390,76]
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011329))

	def test_2513011330(self):
		input = '''
## ]F.JC
func E0 (var lvFa, number Yld)	return
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011330))

	def test_2513011331(self):
		input = '''
## s
dynamic YiDy[64.770e99,41e-87,0E+74] ## k+CGzw
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011331))

	def test_2513011332(self):
		input = '''
## Pc9
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011332))

	def test_2513011333(self):
		input = '''
func Vy (bool tret, var KhkP)
	begin
		## KU&6sixCSYTBF>f 
		## ApR+VBU7aQ0k@w;&GY
		## 6
	end
func Wyk (bool Utu[8], var CTY)	begin
		## $EZvmu~Y%hB
		##  y
	end

## oyl6Iz!o0|s;uw[5H&8
bool Chig[90.202e46,813] <- 95E48 ## ,@Yv4F`><$~.S_
var RMLG[72e12,14.745,60] ## 2U6
'''
		expect = '''Error on line 2 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011333))

	def test_2513011334(self):
		input = '''
bool xug[608.633E90,63e+13,35.451e+99]
## fMH&|W~Rz~],A|xPZyGH
func tdH3 (var EJp[5,3.171e+10], dynamic U8o, string N1tb[681.716E+19,4.745,96.354])
	begin
		begin
			## AtCd
		end
		## uX~F95i&9F
		## !D&ig>Qqah888N#
	end

number yp[8] ## I~j#v.l</1y2J$3"UazF
'''
		expect = '''Error on line 4 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011334))

	def test_2513011335(self):
		input = '''
bool lBx ## u{X J{
string Cv ## bv*z?$4%
func PkCK (bool vCI[2], bool Xxu, number I4)
	return 76e04
## K;oXZTo=XL>*x
## ,]r85^8YHK],sz*}UjC8
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011335))

	def test_2513011336(self):
		input = '''
func akXb (string MXrU)
	return

## vhVN|$IpkbBtA`b
## }#s--J9[<K(%%v!Or
number WG[1.425E20,987.018E-03] <- vp
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011336))

	def test_2513011337(self):
		input = '''
## M>]3RBongw0@wL$b~g7
func wzXM (string bl, string Vg, string Ed[4e-37,29e-87])	begin
		## z[fIbO[C_LK%&g
		## mz |0sR_mY5
		continue
	end

func fC (number QWC)
	return nM

func QI (bool QdM[50,7.826])	return c1W
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011337))

	def test_2513011338(self):
		input = '''
func gf (dynamic yKk[4e97,618.093e-55,40.532E+84], number Qkkq[84.977,0], dynamic G2[874.254,770.297e+89,594E+63])
	begin
		## _KO/@4MU!i2soj:kq4)e
	end

func st (dynamic Za1, number ExH)	return

func CB ()	begin
		## s9S./H^mY
		## pQ
	end
bool I3KR <- "'"'"k!x" ## a,>H+Cw.Q-$?/~sT U
## x#A4{%6f
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011338))

	def test_2513011339(self):
		input = '''
## w[)k
## Iz
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011339))

	def test_2513011340(self):
		input = '''
## :`nrTwI,jDxHxp
func oPgr ()	return 6.803e+76

## Q(_gx
func KSp ()	return "s'""

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011340))

	def test_2513011341(self):
		input = '''
## A{F2K ~
func OXtX (var IVp)	begin
	end
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011341))

	def test_2513011342(self):
		input = '''
## P
## V%e50b^X5|WL[j!ucq96
func xO ()	return cd

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011342))

	def test_2513011343(self):
		input = '''
func bWOB (dynamic o6o, string w5_P[2E36,761.415,5.891E92], dynamic WLS)	begin
		## a?ZzPn4{&
	end
## *$qX>{%t^g0UrjP
func ZXED (var A5[65,8.487E-10], number za7c[246e+51,698])
	begin
		var Y_i[62]
	end

bool SgC ## /#rgiU{N=!B{{e-cZ
func DRnz (string R8K)	return 6

'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011343))

	def test_2513011344(self):
		input = '''
string fQUo[3.535,3.207,47.105] <- true ## pKzxJ=
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011344))

	def test_2513011345(self):
		input = '''
func ifJ (number cb[59,6.863,282.927], bool mu3[2E+94,781e-42], bool eQ)
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011345))

	def test_2513011346(self):
		input = '''
## xSxulw(0n"q?hg
string NZ <- 821
dynamic D2H ## %
func VI (number Z4ma, dynamic cpNj)	return false

func EC3k ()
	return

'''
		expect = '''Error on line 5 col 22: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011346))

	def test_2513011347(self):
		input = '''
number zhG[86e-96,9,1.055] ## )OOwDJ_TAN
## QJZ:SWI/z`c?
func uRr (var q6va)	return false

dynamic Nz[93.000e-01,174.895E+27,7.662]
bool M4 ## :=kBB{aA{,"Bw4z7H
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011347))

	def test_2513011348(self):
		input = '''
func To (var Xk[693e-35,31.971,98.122e30])
	return

## 30$OxXRhwz}0
## TVzM2)+^lOR3tex:
dynamic YhS[31.760E+58] <- 171.248 ## LR 
func mkTv (number qK6[9.031,68.347e-29,2.066], bool uMW_, string MC8v[48.126e-80])
	return

'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011348))

	def test_2513011349(self):
		input = '''
## %ow
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011349))

	def test_2513011350(self):
		input = '''
## t="T@b"Q
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011350))

	def test_2513011351(self):
		input = '''
var O6[169.982] <- "'"" ## .;U:CMF$=c3K1
dynamic mKBK[76,484.214E-52,51]
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011351))

	def test_2513011352(self):
		input = '''
func R6Y (number oR0E[61,7e+44,238E+73], string JeJP[153.508E+87])
	return

## (Sx7f
## #!yJS
number ah[8.563,76.835e+18] ## Eam
number b4cy <- "R'"(" ## V%=ln;Zf41*e/(
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011352))

	def test_2513011353(self):
		input = '''
number LUP[55E-96]
dynamic NI3[87.792e+22,5E-06] <- true
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011353))

	def test_2513011354(self):
		input = '''
## _<(fxnL
func kg (number J_7, number u8X, var TUEE)	begin
	end

number i6Vd
var cOiI <- "'"x"
## ]eL5
'''
		expect = '''Error on line 3 col 33: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011354))

	def test_2513011355(self):
		input = '''
func wt ()
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011355))

	def test_2513011356(self):
		input = '''
## h-!SIRi%]"Y
## R
func YuV ()
	begin
		## zw )NRLK1>Lw
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011356))

	def test_2513011357(self):
		input = '''
var GIO[2,65,81] <- 683.800e91 ## %gYk+m1
func oK (string JId, var ENUl[475.441,11E93])
	return "p'"J'""

dynamic H6 ## w_~O*( <7{E/
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011357))

	def test_2513011358(self):
		input = '''
## 8_StaKDl}Lg<HoE0H
## E$bjJ <_gH1
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011358))

	def test_2513011359(self):
		input = '''
## pA@?)TR|R3
string BE2 <- "g7R"
func Rj10 (bool aw[850,71e-81,83e66], var MRO[943])	return
var cuXF[752.778e25,8E99,487.825e-38] ## s"wj|h
## umy
'''
		expect = '''Error on line 4 col 38: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011359))

	def test_2513011360(self):
		input = '''
## YUyBaN9
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011360))

	def test_2513011361(self):
		input = '''
## md4*Q0mv5
number sL0N[67.455,574,56.615] <- 478
var HqDI <- true
func FTz ()
	return ARSY
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011361))

	def test_2513011362(self):
		input = '''
## GS<wHNF0JdT
func bs (var iOwx[12.333,9,586e70], var YlI[427e+36,3.561,7.196])
	return

dynamic EO <- false ## tbIx+FXk;v:
func RAeD (dynamic Idg)	begin
		## @Nff,J`td !Xv[4eQMO
	end

'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011362))

	def test_2513011363(self):
		input = '''
func wq ()	return "Ocu("

## tT}#P6:`a+c;R&j
func pJLX ()	begin
		for qGSd until 1.165e28 by "'""
			continue
		## nvAG9h-j-f*)=
		continue
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011363))

	def test_2513011364(self):
		input = '''
## ?K4dcb`naGBo6#
## NxE}c-
var VFd <- "-"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011364))

	def test_2513011365(self):
		input = '''
## ^ [GG
func e0 (string ji, bool F_[81.048E83,7.534,6.268])
	begin
		OAt(false)[208.329, true] <- true
		## O.Xjf$HzF{F2Ce#K
		## RbiP
	end

## ^^A(NHZ#|
number EqV <- true ## ]8r/ Ah@VWXS00@{T
'''
		expect = '''Error on line 5 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011365))

	def test_2513011366(self):
		input = '''
## ncgCc%aW1)l@f2^k#
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011366))

	def test_2513011367(self):
		input = '''
func tg (bool A1ww[69.871], var KDJ, string fo9S)
	begin
		begin
		end
		## o!5nnxa+
	end
## 9"Nwk!3
'''
		expect = '''Error on line 2 col 28: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011367))

	def test_2513011368(self):
		input = '''
func ND ()	return
number URJ <- true ## eZ-wpwk`!_l,(hwQ?
func QZXJ (dynamic Md[6.041], string LWI, dynamic Om7)	return

func B5w ()
	return true
'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011368))

	def test_2513011369(self):
		input = '''
string xft[2.033E-47,686,66]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011369))

	def test_2513011370(self):
		input = '''
number pG[7e-41] ## tx3.$Y
func tryR (dynamic YG[434e+93,752.199e+37,99e10])	return RYQu
## FE)*^zq
## lhT
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011370))

	def test_2513011371(self):
		input = '''
number VPW[7.930,80.982,6] <- "6= '""
## (``
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011371))

	def test_2513011372(self):
		input = '''
func kIs (bool wyOO[50,4.066E47])	begin
		break
		## V
	end

func ABB (number yJ)	return Lkg

var Sod
bool xM
## F=GYpXW1gYWn/-PjK(,
'''
		expect = '''Error on line 9 col 7: 

'''
		self.assertTrue(TestParser.test(input, expect, 2513011372))

	def test_2513011373(self):
		input = '''
func ou7 (var qEw, string bfOW[0.160E+27], dynamic OX[13.610])	return sS
number Iero[114] <- "'"S'"f'"" ## Z=*Bjhu?Fc$]nBR]^2gW
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011373))

	def test_2513011374(self):
		input = '''
string kqZe ## rndB<Q|
dynamic hq[854,6.918] <- j4
func OL (dynamic pj, number i8H2, bool t98)	begin
		## 4pON
	end
func gLS (bool fFaD, string DT, number IR[80.820E-01])	return false

'''
		expect = '''Error on line 3 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011374))

	def test_2513011375(self):
		input = '''
## O]J
dynamic eNhU[12e+56,515.236] <- "@"
number XN <- "[Z'"'"("
dynamic Fg[28]
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011375))

	def test_2513011376(self):
		input = '''
## w{[hEoufU/_U%]{i
func PpWL (dynamic hU, number o0, number xzT)	begin
		if (WD)
		number bOW[88.084,848,733.681] <- "'"2,|"
		elif (143E+79)
		return
		elif ("a'"")
		nze4(XHJV, "/'"'"C*")[619.058E-49, 307.564e+05] <- knqm
		elif (57.613E+79)
		mOJ[false] <- ")X'"u"
		elif (KN)
		YT4E <- "o'"Dw'""
		else continue
		## kyLtwM,P@2%K_
	end
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011376))

	def test_2513011377(self):
		input = '''
func Wt7C ()	return "'""
## cdO#C$q.E.}l/!+n
func Sx0 (var J27[700E+32])	return "'"'"d'"'""

## cXE#,tvD
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011377))

	def test_2513011378(self):
		input = '''
func Waoh (bool Lln[25.656])	return true

string aky <- kA ## >c,71;
## 5ZZh
## 2<m4EO}q<m2*t%C1h;X
## z
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011378))

	def test_2513011379(self):
		input = '''
## ?
func O9Z (var kGD[76.590e+20,773.095,13e75])	return
## z(O^.R`
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011379))

	def test_2513011380(self):
		input = '''
var sw[9E+20] <- 60
bool Fn5[8.842E-30,27] <- false
func CF3 ()
	begin
		## S(1jr[b.
		continue
	end
## uF1^.IA4aBQ#f
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011380))

	def test_2513011381(self):
		input = '''
func dYVS (bool wM, bool HLH[92.181,0,16.292e75])
	return 7.443

func bfY (bool CC4, var w1Ax, var AvI_[63e-49,2.336])	return
'''
		expect = '''Error on line 5 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011381))

	def test_2513011382(self):
		input = '''
bool jMnt
## rQ|
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011382))

	def test_2513011383(self):
		input = '''
## 0A
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011383))

	def test_2513011384(self):
		input = '''
dynamic k81 ## +EL1k5f
var Ksq[640.546,9E+34] <- FAst ## ~fY3p)yKV&7bc?aBl1<
## "z/p.!PIQCT
## uJ-
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011384))

	def test_2513011385(self):
		input = '''
dynamic jb[1.353] <- Bq2
## >o:Qt? WZ!6
## y`c
## RIVd&z/
## <zDTiaHgg
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011385))

	def test_2513011386(self):
		input = '''
dynamic GVyH[713.943,78,41]
func iup (string t8S)
	return 85e72
func Oj ()	return false
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011386))

	def test_2513011387(self):
		input = '''
func DGD ()	return "'"_"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011387))

	def test_2513011388(self):
		input = '''
string Wt <- oe ## C5+6YR%_tlBk7~!Ac
func nQl (string nbob[3E-47], dynamic DGUm)	begin
		## 91j3?isOS1jP
		return
		## BIZ4E[
	end
func xC (string SL, bool XcUX)
	return "5g'"h'""

'''
		expect = '''Error on line 3 col 30: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011388))

	def test_2513011389(self):
		input = '''
number oz5G <- sdK ## 51;JJ$8(YrhZj3`50`P
dynamic mq <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011389))

	def test_2513011390(self):
		input = '''
func Gj ()	return c2r
## 0"Lld
string W1[427,3e+41,364.004]
number f3j[692.953] <- GU7 ## <${g0:o
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011390))

	def test_2513011391(self):
		input = '''
func ZD (string eyCl, var zAm[75e+60,9.464e27])
	begin
	end

dynamic Bbv[987.079e-16,4]
'''
		expect = '''Error on line 2 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011391))

	def test_2513011392(self):
		input = '''
## K!0yR.4,}WK^LUC9Wi0?
func jd ()	return true

## 6
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011392))

	def test_2513011393(self):
		input = '''
## NP4E
## <|ZR+gek,c!>`P]-
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011393))

	def test_2513011394(self):
		input = '''
## X|4xc5
## ]
string q4u[65.895e-83] <- Bq
var g3ut ## {j)Dk8$
## iMrE`X_aL,`m{5g:}
'''
		expect = '''Error on line 5 col 19: 

'''
		self.assertTrue(TestParser.test(input, expect, 2513011394))

	def test_2513011395(self):
		input = '''
dynamic leB <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011395))

	def test_2513011396(self):
		input = '''
## ePn[^k^d!Tzd<KsN
bool ACmZ[82,292.815e32,447.909]
## bVyG`Q
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011396))

	def test_2513011397(self):
		input = '''
func tW9 (var CrET, bool NM, number Uxb)
	return
var QK[111] <- false ## 3.$sZ"$%;%X5MK42Ql[/
string lWQ <- qb
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011397))

	def test_2513011398(self):
		input = '''
## lzWqcLh*<
func kwup (bool eif)
	begin
		## {"Xu~RUo3veoo81PV<
		## 9Bc%-p !kK:
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011398))

	def test_2513011399(self):
		input = '''
var yc5[6,6E53,36.265e-68] ## hPFTuhMV:w
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011399))
