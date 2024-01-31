import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_2513011300(self):
		input = '''
func TBI ()	return AIi([[hg6(+ Gn, "f>'""), 932, true], false], 8)
## e
func Umq (bool fYk[67.175], string zw5E[8.548e42,3,0.072])	return kJhb
dynamic q_[195.175E32]
'''
		expect = '''Error on line 5 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011300))

	def test_2513011301(self):
		input = '''
func Ni1N (dynamic nDu)
	return "1'"'""

## I MVFg
string kl <- x9 ## Dq?}
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011301))

	def test_2513011302(self):
		input = '''
## 3Z(
func kud_ (string nE, bool Srtq[329,6,52.757e-70])
	return
number rL[9.153E+34] <- ml ## G.a8i<5!]KQw5!t.LWu0
bool Ys
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011302))

	def test_2513011303(self):
		input = '''
func Em3 (dynamic VN[9.992E29,0.107e95,33])
	begin
		## hPbFV_
	end

func LUwl (dynamic Yj[85e-81], number bk[775.384E+89], dynamic lVK)
	return
func to (number RdtS, var UMm)
	begin
		for d4Xd until false by false
			K74g(nmDq, 14, "_'"'"'"t")
	end
func IBt ()	begin
		sSs[65.326E-83, true, ViF7] <- true
		## oE|@M+#YR0$H7.m:.nw
		## qy_VAkt9WH
	end

bool d7g
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011303))

	def test_2513011304(self):
		input = '''
## dOQUV"Caq<2@
bool Mc <- l3
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011304))

	def test_2513011305(self):
		input = '''
var XQV[41.979,1E+16] ## qlkmZwzOb3*Zz
func bAI (var L1[691.469], string hxC[22,279,54e37], bool KqO[4,0,9e+88])
	return

'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011305))

	def test_2513011306(self):
		input = '''
func nL ()	return
bool md[678] ## ET4-Sb4E|l,2CWi}
## feZP
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011306))

	def test_2513011307(self):
		input = '''
func lkL (dynamic Y42R, string QoqN[71.788E-88])	return

## IPgv401jrxn>;eoV)M#
func dLUB ()	return C7Mv
bool ARi[5e59]
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011307))

	def test_2513011308(self):
		input = '''
## u>bsW5-^Vx5b2%s.wi~
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011308))

	def test_2513011309(self):
		input = '''
func HSNh (dynamic EB1j[15.891], number TYmP)
	return "Qj"
func INMf (number yH[49e93,37.474E-54], number ZkX)
	return 357.935e-41
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011309))

	def test_2513011310(self):
		input = '''
## 7u$Z
## Le`Nt>fEoi
## T+;?I-yZ*|6/}x
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011310))

	def test_2513011311(self):
		input = '''
number niMw[2e+47] <- "'"" ## }nxHd>wcnI9()
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011311))

	def test_2513011312(self):
		input = '''
string B_se <- odpS ## q
## <j7keZ0O6?D
func h4I (var cAj6[799,8.417])	return
func qaWI (bool XMBX[42E+65], string RM, var qO[3,6.519,584])
	begin
		number t35[442.652E+26,838,40e-68] <- true ## xZkE
		begin
		end
	end

## q #
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011312))

	def test_2513011313(self):
		input = '''
number H_[29,6.438]
## |44^N`H
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011313))

	def test_2513011314(self):
		input = '''
func lj (bool FjAz[22,67.338], dynamic Nw)	begin
	end
func Fi (var rC)
	return 87

string hJ[6,5.295,2.692E85] <- 162
'''
		expect = '''Error on line 2 col 31: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011314))

	def test_2513011315(self):
		input = '''
func L97 (string U3z2[72.114], var feD)
	begin
		RCuO("'"y")
		## m^;e
	end
string Ji[5.996E-93,145.295e-28,153.393] ## ?qn"Zf6GI>NN%oX|z<Rj
bool Tve4
## MKW?
'''
		expect = '''Error on line 2 col 31: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011315))

	def test_2513011316(self):
		input = '''
number x2B2[4e+73] ## @Bj ]4~AM
var y23 <- "n$'"kC" ## V!uc5I&j[skLV6
func aP7 (var Iuvs, dynamic FuG)	begin
		## RUEvgj6 7eJvE?"
		MJ[false, "'"M'"'"'"", ivgY] <- false
	end
## ek~<Z3dP
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011316))

	def test_2513011317(self):
		input = '''
## ng#*!kVXA{%H
var L2n
func uIPP (var KGgo[21E35])
	begin
		## 9(T
	end

## ;d${12{"OA$U
'''
		expect = '''Error on line 3 col 7: 

'''
		self.assertTrue(TestParser.test(input, expect, 2513011317))

	def test_2513011318(self):
		input = '''
## }e)th+PU-o+[q
func AlCP (number Xg[28.229])
	begin
		## ml";4P41?a4C:d
		L0["'"", true, "I'"'"'"c"] <- "'"&"
		## WT
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011318))

	def test_2513011319(self):
		input = '''
func vM2q (string W3eh[8e-26,119.787,21E15], string dC6)	begin
		number Whzj[0.045]
	end
string w4Q <- 490.334e+88
func cN7 (string EMC7[5.454E25,8,45.182E-16], string SxGn)	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011319))

	def test_2513011320(self):
		input = '''
## y1>Vot})3^t0?bD
func sxY (string ZgA, dynamic pB4[28.919e+32], bool Md)
	return BQXe
'''
		expect = '''Error on line 3 col 22: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011320))

	def test_2513011321(self):
		input = '''
number VY[0] <- 74.612e+42 ## (5hwO&aUXVS8a<j+1+2P
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011321))

	def test_2513011322(self):
		input = '''
bool H9B[66E+97,6,1.871] <- yIa ## Qvh[gj(L#7b"
func e9u (number DF, string xcl)
	return
## 2WBCE98
func R7 ()	begin
		continue
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011322))

	def test_2513011323(self):
		input = '''
bool mV
number XZq ## pg#K Z$jW~oD|S`
func qvpq (bool sS[4.322,56e+26,75E42], number VucP)
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011323))

	def test_2513011324(self):
		input = '''
var y_uN <- Ak
dynamic Cxo[5.534,834.196] ## y|OmF""v}{`(
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011324))

	def test_2513011325(self):
		input = '''
bool O7Xl <- "'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011325))

	def test_2513011326(self):
		input = '''
## MW1;`04>X|:K%DO(:X]L
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011326))

	def test_2513011327(self):
		input = '''
var Ykjz <- 81.181
## #alp~W}r;]8FN
func bzI ()
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011327))

	def test_2513011328(self):
		input = '''
func Za (number Yb[13e+43,13.562e-26], number q3[3e-96,5.947E-13], dynamic w5OV)	begin
		begin
			## c
			if (false)
			KA <- true
			elif ("p'"l3j") dynamic EMsq[574,674.315E55,77.621] <- QjR ## csg9k![jn[!S}R
			elif ("'"")
			string ID
			elif (482E+89) begin
				continue
				## Y|DJmp
				## d(vu_{[EI
			end
			elif (29.744E-05) return
		end
		## _(:{#&~d
	end

dynamic OD[7.647,860,4.731e+82]
dynamic OpCU[490.909e27] <- 20.404
## A~cL:
'''
		expect = '''Error on line 2 col 67: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011328))

	def test_2513011329(self):
		input = '''
func olb (var T1[58.448E-25], number mVAl[335,18,73], string Ib)	return

bool w7[7,42.793,18.686] <- k_Y3 ## vQ
bool Kd8q
func hIy ()
	return false
func hG9 (string LNCu[4.190])
	return
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011329))

	def test_2513011330(self):
		input = '''
func Azm (var vf, dynamic jpOc[7])
	begin
	end

func pi4q (number Ab[175E82,51e-48], dynamic Dy0[55,56.686e+34])	return

dynamic b5xO <- sT0
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011330))

	def test_2513011331(self):
		input = '''
## 5@]&&M
dynamic pgsu <- "'"n;"
func P8 (bool Uj[9.601,104,463.558], dynamic SBP, string q8[58E+03])	return

## ?4!Irw1>|5"K
func X6si ()
	begin
		## 6|QKGg+;tAVN`Yj4#6
		X4Dq[false] <- 59.628e-03
		msk(5)[cvS, true, 535e+25] <- "'"'"'"'""
	end
'''
		expect = '''Error on line 4 col 37: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011331))

	def test_2513011332(self):
		input = '''
func oHt ()
	return
var yHv
'''
		expect = '''Error on line 4 col 7: 

'''
		self.assertTrue(TestParser.test(input, expect, 2513011332))

	def test_2513011333(self):
		input = '''
func KXS ()
	begin
		for qN0M until vMeZ by BOnY
			gMy(8E74, vPd, "K'"'"'"4")[Qsmy, "H'""] <- 48
		## g:O(@<
	end
## pU6Bdnz
func Jz (number BSQ[3.634E+96,50.805], number nfzC[8.890,438.765e-15], bool xVti[848.562,8.034,157.621e29])
	return "'"1'"'""
bool xZ[405] ## L-7+3DL]O$"#CN!.I
'''
		expect = '''Error on line 5 col 29: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011333))

	def test_2513011334(self):
		input = '''
## uaD"jI=5bYVa.C4/72M
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011334))

	def test_2513011335(self):
		input = '''
dynamic Rv
## Xud"H4Vv
func gY (number Frye[38e+30,79.158,49.773e-03], dynamic xYbp[2E-59,3E91], bool zoiw)
	begin
		## g(5&.
		if ("'"'"'"]")
		break
		elif (dRVD) if (2E77)
		begin
		end
		elif (10.014)
		continue
		elif (6E+86) var qHxK ## zWop|:Y1BG4
		else string wW[2.250] <- n_G
		elif ("1'"")
		return false
		else return
		## 9hY +CD/,gaU:fa d
	end
'''
		expect = '''Error on line 4 col 48: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011335))

	def test_2513011336(self):
		input = '''
## pAim2{*U-l9
## B
bool bj6j[7.523e+07] <- true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011336))

	def test_2513011337(self):
		input = '''
var hZho[654.176e28] ## <q6lYg@$#X"N;Syt 
func t4 (dynamic pFO, dynamic t0e, bool FjM[9])	return "'"'"#PF"

## $T:V$
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011337))

	def test_2513011338(self):
		input = '''
var q2I6[0.631e97,208.004e-68,15e-34]
func nfuX ()	return

'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011338))

	def test_2513011339(self):
		input = '''
## 3d,c
bool IHn[49E+67,139.018e-75,92.120] ## jNP
## AfJ+>](w^>Z/:[
## >
dynamic wM
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011339))

	def test_2513011340(self):
		input = '''
## f}z6ZWlw$@flOD6$PaZ
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011340))

	def test_2513011341(self):
		input = '''
string VXa[53.790,0,59.167E-62] <- ",'""
var tn[65e84]
'''
		expect = '''Error on line 3 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011341))

	def test_2513011342(self):
		input = '''
## :0o4=qi/*3<M"asZrLC
## ok/}@3vcD
## Db5_2
## K@
'''
		expect = '''Error on line 6 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011342))

	def test_2513011343(self):
		input = '''
## Z
string SGB[9.407E59,508e-96]
string hpB <- true ## !zghh?k2{a
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011343))

	def test_2513011344(self):
		input = '''
var xc[43,760,952.631E-51] <- 8.026 ## ;
var Giib[80.550E+28] <- Zv7y
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011344))

	def test_2513011345(self):
		input = '''
dynamic GwA[72]
## +d2,XxhaP|LA7-mR{=
number kSm ## qWj]KK$dt(&
## l5Y"Puh 2+$,WE
string RQP <- ePOf ## 6La&RR:a)J2fwUY27ZM
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011345))

	def test_2513011346(self):
		input = '''
func Otn2 (string ql4j[74E64])	return true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011346))

	def test_2513011347(self):
		input = '''
## H64;-&)(xTYms?*z
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011347))

	def test_2513011348(self):
		input = '''
## "/
number F56T <- 894E-18
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011348))

	def test_2513011349(self):
		input = '''
## lO"1Bp8})qbd/
## 3v
func wz (number kF[649e88,3E-91,29e-91], bool dQ, bool KBi[616.733E-24,45.712E+79,1])
	begin
		if (true) continue
		elif (i9_M)
		begin
			## B6E?W3
		end
		elif (360.030E+38)
		break
		elif ("C'"8'"'"")
		if (2)
		continue
		elif ("'"X8")
		continue
		elif (CM) continue
		else begin
			IUr()
			break
		end
		else x0O6()
	end

## UW
## F6kHn@0uH`*F"B:
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011349))

	def test_2513011350(self):
		input = '''
func txr (bool EQ, dynamic L6r, number g6[775])
	return 0.273

## gFr=6S|1@osz+`|^f]j?
## ]Gq
## VC.
'''
		expect = '''Error on line 2 col 19: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011350))

	def test_2513011351(self):
		input = '''
bool tRQ <- 856.149e-64 ## /}Ph/vGQ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011351))

	def test_2513011352(self):
		input = '''
## 8yR y7|r
## S&o=z]l*w)
func xwva (var yxf[69,5.601,7E-66], bool m2[97])	return

'''
		expect = '''Error on line 4 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011352))

	def test_2513011353(self):
		input = '''
## -j1D
bool Oh[670] ## y><b*+B6eGV}D^^yyq:
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011353))

	def test_2513011354(self):
		input = '''
## cd-7GmgD**@vDS
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011354))

	def test_2513011355(self):
		input = '''
bool Obe[30.663e-66,6.071,7.919] <- rPf
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011355))

	def test_2513011356(self):
		input = '''
func gC (string yk6S[0E-18,29.784,55.613E47], dynamic EyX[47e-25,90E+07,74])	return 94.344
bool jo
## Pc@zz
'''
		expect = '''Error on line 2 col 46: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011356))

	def test_2513011357(self):
		input = '''
## E<#(WF/ccos,p2VO4A=
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011357))

	def test_2513011358(self):
		input = '''
number s97 ## :p2t;$
## X {d
## -j 25CZUB4`1`s
dynamic DU <- 14.779E-45
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011358))

	def test_2513011359(self):
		input = '''
## *iRH8zWH
func EV (number un[8.216,12,795.076])
	return "E"

dynamic Qi
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011359))

	def test_2513011360(self):
		input = '''
string WZ
var NI0[4.818]
## ZGZL3h
func KZ ()
	begin
	end

'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011360))

	def test_2513011361(self):
		input = '''
## vp/7/$4.Yc,Vc`Kcu-Tv
bool wd[99.824E+48] <- B796
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011361))

	def test_2513011362(self):
		input = '''
## Y vbK*):uK_
func k5 ()	return
func q5 ()	begin
	end
## uJj~U`"]2ONa
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011362))

	def test_2513011363(self):
		input = '''
func Vocr ()
	begin
		if (VY5i) gj("'"'"'"'"", Yi0)
		elif (PaE1)
		continue
		elif (CSO)
		begin
			return
			## ^"-oP+5rnc@*~
		end
		elif (false)
		continue
		elif (438e-04)
		var vc
		elif (600.959e+38)
		break
		else X_m <- 33.307
		## T*IG_1uZK
		if ("'"'"'"") if ("~l") begin
			ql()["3'"'"'""] <- "'"'"T'""
			## i=|s7oLQ
		end
		elif (zn) for H8 until "'"'"'"'"" by mHui
			wI9(hCpk, true, "'"u")
		elif ("'"g") if (Kr)
		md("y'"=Wh", "@'"", "w'"'"'"")
		elif (false) Hm9d(false)[HPEA, 99e19] <- "G_'"'""
		elif (8e-77) begin
			## D
			## ]yeyRsw-61
			break
		end
		elif ("'"'"'"C'"")
		O4(968, 644E-49, "'"")
		elif ("V") begin
			string Sof <- b3N ## H8x.o2_Be"qS
			begin
				for Qit until 0 by false
					SVD4(false, "D?Y", "K'"r'"")
				## F&OP@G]L
				## AZB1i}vY
			end
			## L0:^s$}rP/o"
		end
		else return
		elif ("S'"") break
		elif ("w`:?") iSt(74e+48, false)
		elif (Nt) yLL(n5, true)
		else string XjJ <- "'"'"'"'"f"
		elif (false)
		v0m("'"'"'"'"")[true] <- 88.160
		elif (uw6) continue
		elif (625E34) BS2_ <- true
		else for Ex until iNMg by "h'"Y!"
			break
	end
## KjY#:sNn8F+u:q0]X4zh
func gP (var w6s)	begin
		begin
			eA1F <- "'"'""
			return z9A
			##  o f
		end
	end
func pV5 (dynamic aZe[7.973E-20,52,683.282])
	begin
	end

'''
		expect = '''Error on line 15 col 8: 

'''
		self.assertTrue(TestParser.test(input, expect, 2513011363))

	def test_2513011364(self):
		input = '''
dynamic sG[3,1.421,945e96] ## On
## ZI#4wEVu2gL=ZGS
func LIr ()
	begin
		## 95ydQE
		## *Ap{U!X1$E0t
		continue
	end
## ~EhHTM
var eR[32.023,225.966E-91] <- 339E18
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011364))

	def test_2513011365(self):
		input = '''
func lWj ()	begin
		for EZ until "'"(" by "5'""
			break
		if (PwG) return
		elif (bROm)
		gJ()
		elif (GfW4)
		continue
		elif (67) if ("$YL")
		continue
		elif ("'"'"Q") bool mB[75e+79] <- 56.236E-10
		elif ("g")
		return "'"'"'"'""
		elif (590.462) break
		if (true) var RN[46e-95,7.391e+41,0E-91]
		elif ("%v'"'"'"") return "'"'"'""
		elif ("'"BF") if (PH) continue
		elif (46.298E+31) begin
		end
		elif (407.727e-68) break
		elif ("o") return
		elif ("z") break
		elif (TQIu) string rel[525.289,3,289.597] <- 102.936
		elif ("c'"$4'"")
		begin
			## P:P2z"9UpDQ+
		end
		elif (qw) bool KGQ
		else break
	end

bool Gyb <- RIv9
'''
		expect = '''Error on line 16 col 18: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011365))

	def test_2513011366(self):
		input = '''
## ["KGBnO<>g"$_2!LIWJ
func NTIK (var Qj[60], dynamic Ja)
	return
bool Te ## G7V=E+~*
## V
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011366))

	def test_2513011367(self):
		input = '''
## 6IcP>6F:=IP
## <_$<
## yb8~zB</~q4y`H$ !63
bool rdj
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011367))

	def test_2513011368(self):
		input = '''
bool n7[342]
## <f/FC)/!km
func hcx ()
	begin
		## Gd~x_|Ak
	end
bool ozxb <- Ti
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011368))

	def test_2513011369(self):
		input = '''
bool B7c ## L7rSjLFr5@jr-#@]eU
var Lg <- "'"'"'"'"'""
## mwWn%b(_xA:2:aQJ
func MbQE (number Qz, bool B0PD, var gL)	begin
		##  bF94*r%H&F
	end
## 1f,
'''
		expect = '''Error on line 5 col 33: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011369))

	def test_2513011370(self):
		input = '''
func clPr ()
	return false

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011370))

	def test_2513011371(self):
		input = '''
func afM (var g5x, var s5[34.665])	return "?"

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011371))

	def test_2513011372(self):
		input = '''
bool mzu6
## 427_CV#S5U$mE-l+jd7x
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011372))

	def test_2513011373(self):
		input = '''
func su (var FfHd[8.411e20,825])
	return true
func qd9 (dynamic rK9p, number deN)
	return Ic
func ygRa (bool m5Y, dynamic bn[97.029E96,9,870], string QXy)	return
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011373))

	def test_2513011374(self):
		input = '''
## $Z5d-1#LN
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011374))

	def test_2513011375(self):
		input = '''
## 6Qe
number hMcF[234.883E+19] <- 4E-80 ## rLMx{[+)(5KW}n
## `>/}e)| EVq6c
## ;i2=}y
func Cu (dynamic acq, bool xYIR)	return iyJ

'''
		expect = '''Error on line 6 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011375))

	def test_2513011376(self):
		input = '''
func jy (dynamic UM[2.947,399.031])	return false

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011376))

	def test_2513011377(self):
		input = '''
dynamic h5[75.792e30,22.541e-52] <- PLtq ## T
bool n2D <- 46.875 ## /~ lSIK
func SvwV (string vMiA)
	begin
		continue
		## YO
	end
## a&
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011377))

	def test_2513011378(self):
		input = '''
number OCwq <- 1.073 ## 73rXxd
var z7[7.070e59,38,8.450] <- 11e+34 ## tYO(YQEPGBh
## 5xE,@J
func fE (string xm[31.457e+28], bool jf[381.583e-55,0E57,4.251E-87], var jN[99.446,72.192e-27])
	return 53.907E-70
'''
		expect = '''Error on line 3 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011378))

	def test_2513011379(self):
		input = '''
func CZyj ()	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011379))

	def test_2513011380(self):
		input = '''
## 3[j:SvAL
func kGC ()
	begin
		gru <- false
		begin
			## C+*GW_
			## :Qp 7SMI8
		end
	end

## ^z
string QVBo[11,8.052] <- "p'"c'"w" ## -+(rc
## &W[Wl
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011380))

	def test_2513011381(self):
		input = '''
## ;v9nPR(vA@52JH7t
func O2 ()	begin
		mF()[false, true] <- A7q
	end
## I`dIU:M-.IX}RNm8=Ld
var Lr[78.222e+08,73.835,512.893]
'''
		expect = '''Error on line 4 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011381))

	def test_2513011382(self):
		input = '''
## Fk&Xe#GT,)
## ;aV!vAG%$V17b
func TO ()	return

## t>gb%BTd&SLV2.MZJ!9|
number lh <- "'"lM]N" ## PHzv(xQ`d
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011382))

	def test_2513011383(self):
		input = '''
## kPg(i=n,,H
var vO[80E60] ## ;upaKTR&U~18`G
## #I}2;iq.pWnrI([@kX^
dynamic dN[2e-35,0.744]
'''
		expect = '''Error on line 3 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011383))

	def test_2513011384(self):
		input = '''
## j`<r+$v1W|o-q
bool Xjt0 ## q/!
func vq0W (number iE[577e+46,3.340E-21], string HC, dynamic Umu_)	return 0
'''
		expect = '''Error on line 4 col 52: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011384))

	def test_2513011385(self):
		input = '''
dynamic RA4[9e-06,33.724e+13,79.560] <- 2
## /@E~UN/t
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011385))

	def test_2513011386(self):
		input = '''
string p7[0.844,5.229e+17,217.667] ## [4p*:gfl?*=M,?p
func CgG (number Ih[16.865,3.109,3.426E56], dynamic X_)
	return 366.878e-83
var hyNy ## T,K5OIz:fP
string ws ## r5#].R=ury:m?
'''
		expect = '''Error on line 3 col 44: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011386))

	def test_2513011387(self):
		input = '''
## -y #|VQ-Mivo[
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 2513011387))

	def test_2513011388(self):
		input = '''
dynamic YJv ## [bZq?Aa}Msk/}bZh!G(r
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011388))

	def test_2513011389(self):
		input = '''
string WtM ## =N5^Z[NC~C)O<ADS
func II (number S2, dynamic qAh[35,4.526E21,47.379E+28])	return

'''
		expect = '''Error on line 3 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011389))

	def test_2513011390(self):
		input = '''
func ZKfX (dynamic ip, number Ep7)	return
## `K8h<1Wy4wr;En
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011390))

	def test_2513011391(self):
		input = '''
## 3][0GH
func bhfL ()	return LQ9B

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011391))

	def test_2513011392(self):
		input = '''
string vB[4.686E+87,35] ## 66mJY!qm
## "aS%0
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011392))

	def test_2513011393(self):
		input = '''
## p)?OE}R,ZxPE1Nl=:Jv
func tFc (var UhO, var b8W)	return uCmc

'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011393))

	def test_2513011394(self):
		input = '''
string bmsv ## ssOyaU_E;k
## j_F_-Jta%
## <,C!fS={r ue
string l6YA[426.688,796E-53]
func Lb9 (var uw, dynamic oLa[22.921e+55,69.307E-34], string aHaw[4.471])
	return
'''
		expect = '''Error on line 6 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 2513011394))

	def test_2513011395(self):
		input = '''
func YT3 (string hZ, dynamic voxz[9.092e19,9.668], string FL)
	return 4.194

'''
		expect = '''Error on line 2 col 21: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011395))

	def test_2513011396(self):
		input = '''
func Oub (string YfT[766])
	return 1.591

## `X+9"v)IZX]e9S .
var we[22,422,78.455]
func S4 (var uG2[5.223E+61])
	return
'''
		expect = '''Error on line 6 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 2513011396))

	def test_2513011397(self):
		input = '''
var W5Jx <- "/V'"'"]" ## g
bool MuNU <- false ## t ]}n&y#FR
string JIN[91.773]
string OnV[9E09,2,54E-58] <- true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011397))

	def test_2513011398(self):
		input = '''
## Z *
func OLd (string FW, string sN, dynamic adz[16])	return false

func qO9 (number sm1G)
	return false

## N~j(G*;o!b,uI6cWP
'''
		expect = '''Error on line 3 col 32: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 2513011398))

	def test_2513011399(self):
		input = '''
func pu (number NQg[2.478,751e+87])	return
## 2l7w!
## 8MQy3<;
dynamic QVw <- "2'"'"'"m" ## OQ6k9ufg
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 2513011399))
