import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase): 

    def test_case_0(self):
        input = """	>	not not not	%	< ...
-	) >= for	!=	true	string	/ 99	string	%	end a1
or 
 return /	=	begin	a1	[ !=	return and ) end dynamic 
	==
    """
        expect = ">,not,not,not,%,<,...,\n,-,),>=,for,!=,true,string,/,99,string,%,end,a1,\n,or,\n,return,/,=,begin,a1,[,!=,return,and,),end,dynamic,\n,==,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,100))
        except:
            print("fail testcase 0")
        
    def test_case_1(self):
        input = """	/ /
<= ...
end % not	or
% <=
begin	continue	return for )	for or	+	> 36.54 ,
return - "abcd" elif	] var
else for true	until true	=	bool a1
continue
else	== ,	
	95 until == % break break false
(	< return until by	% !=	%	end	)
begin	for
/ func
% if	-	< dynamic if
>=	break end >=	)
    """
        expect = "/,/,\n,<=,...,\n,end,%,not,or,\n,%,<=,\n,begin,continue,return,for,),for,or,+,>,36.54,,,\n,return,-,abcd,elif,],var,\n,else,for,true,until,true,=,bool,a1,\n,continue,\n,else,==,,,\n,95,until,==,%,break,break,false,\n,(,<,return,until,by,%,!=,%,end,),\n,begin,for,\n,/,func,\n,%,if,-,<,dynamic,if,\n,>=,break,end,>=,),\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,101))
        except:
            print("fail testcase 1")
        
    def test_case_2(self):
        input = """ *
    """
        expect = "*,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,102))
        except:
            print("fail testcase 2")
        
    def test_case_3(self):
        input = """	end ... return	<-	until break	break 117.39 return	or )
... *	== <	"abcd" /	begin == false	<
break	begin	< / %
>	var
return
false
number a1	==	"abcd"	true
    """
        expect = "end,...,return,<-,until,break,break,117.39,return,or,),\n,...,*,==,<,abcd,/,begin,==,false,<,\n,break,begin,<,/,%,\n,>,var,\n,return,\n,false,\n,number,a1,==,abcd,true,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,103))
        except:
            print("fail testcase 3")
        
    def test_case_4(self):
        input = """	, a1
"abcd" until return begin
for and continue %
%
<
% if
not break != number return 

end else (	continue	=
- == elif -	a1 <-	99E-6561
else elif bool
)	>

 != if = false	or func
func
    """
        expect = ",,a1,\n,abcd,until,return,begin,\n,for,and,continue,%,\n,%,\n,<,\n,%,if,\n,not,break,!=,number,return,\n,\n,end,else,(,continue,=,\n,-,==,elif,-,a1,<-,99E-6561,\n,else,elif,bool,\n,),>,\n,\n,!=,if,=,false,or,func,\n,func,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,104))
        except:
            print("fail testcase 4")
        
    def test_case_5(self):
        input = """
(
)
"abcd"
and	true else	string func	>=	% var
] 

%
false	( ]	not <-
/	
	*
a1	)	by	< return
+ 
 >= false	var ( return )
    """
        expect = "\n,(,\n,),\n,abcd,\n,and,true,else,string,func,>=,%,var,\n,],\n,\n,%,\n,false,(,],not,<-,\n,/,\n,*,\n,a1,),by,<,return,\n,+,\n,>=,false,var,(,return,),\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,105))
        except:
            print("fail testcase 5")
        
    def test_case_6(self):
        input = """
dynamic - / <=
var	end
]	string / <-
    """
        expect = "\n,dynamic,-,/,<=,\n,var,end,\n,],string,/,<-,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,106))
        except:
            print("fail testcase 6")
        
    def test_case_7(self):
        input = """	and	, 
 for	break	or until >=	break	number	% dynamic ,	<= for ...	func a1 , string
until
-	true
not 52 number !=	( break else	[ true <-
)	by - + for
+ -
or
return	%	< begin	"abcd" dynamic
continue "abcd" or func = else for true
    """
        expect = "and,,,\n,for,break,or,until,>=,break,number,%,dynamic,,,<=,for,...,func,a1,,,string,\n,until,\n,-,true,\n,not,52,number,!=,(,break,else,[,true,<-,\n,),by,-,+,for,\n,+,-,\n,or,\n,return,%,<,begin,abcd,dynamic,\n,continue,abcd,or,func,=,else,for,true,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,107))
        except:
            print("fail testcase 7")
        
    def test_case_8(self):
        input = """ ) / begin and string	*	string	continue	return <-	var elif	elif	for	"abcd"	] (
!=	*	else if 86.83E-256 or	break	/ +
)	var !=
!=	dynamic	false true	var false var
, ] >=
<= =
...
    """
        expect = "),/,begin,and,string,*,string,continue,return,<-,var,elif,elif,for,abcd,],(,\n,!=,*,else,if,86.83E-256,or,break,/,+,\n,),var,!=,\n,!=,dynamic,false,true,var,false,var,\n,,,],>=,\n,<=,=,\n,...,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,108))
        except:
            print("fail testcase 8")
        
    def test_case_9(self):
        input = """ ] <=
"abcd" by if a1 or
<- <-
+	func	!= false begin	break	
	func
[	var continue /	until
until	] - string ) by	break -	== - not or func
dynamic not	bool ) elif >=
var	(	var "abcd"
return	<-	elif	- <- <=	begin and ) == <= elif !=
]	by	and
[	by
%	<- end a1 , else "abcd"	+	==	return !=	and
/	<- ,	a1
=	>
var	else
    """
        expect = "],<=,\n,abcd,by,if,a1,or,\n,<-,<-,\n,+,func,!=,false,begin,break,\n,func,\n,[,var,continue,/,until,\n,until,],-,string,),by,break,-,==,-,not,or,func,\n,dynamic,not,bool,),elif,>=,\n,var,(,var,abcd,\n,return,<-,elif,-,<-,<=,begin,and,),==,<=,elif,!=,\n,],by,and,\n,[,by,\n,%,<-,end,a1,,,else,abcd,+,==,return,!=,and,\n,/,<-,,,a1,\n,=,>,\n,var,else,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,109))
        except:
            print("fail testcase 9")
        
    def test_case_10(self):
        input = """dynamic abc123
    """
        expect = "dynamic,abc123,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,110))
        except:
            print("fail testcase 10")
        
    def test_case_11(self):
        input = """dynamic 1ae
    """
        expect = "dynamic,1,ae,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,111))
        except:
            print("fail testcase 11")
        
    def test_case_12(self):
        input = """dynamic 1.232eabc
    """
        expect = "dynamic,1.232,eabc,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,112))
        except:
            print("fail testcase 12")
        
    def test_case_13(self):
        input = """dynamic abC1#
    """
        expect = "dynamic,abC1,Error Token #"
        try:
            self.assertTrue(TestLexer.test(input,expect,113))
        except:
            print("fail testcase 13")
        
    def test_case_14(self):
        input = """dynamic _abt
    """
        expect = "dynamic,_abt,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,114))
        except:
            print("fail testcase 14")
        
    def test_case_15(self):
        input = """
## comment
func main()
begin 
              ##hello
## "hello"
var a <- "## comment in string"    
end

    """
        expect = "\n,## comment,\n,func,main,(,),\n,begin,\n,##hello,\n,## \"hello\",\n,var,a,<-,## comment in string,\n,end,\n,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,115))
        except:
            print("fail testcase 15")
        
    def test_case_16(self):
        input = """

func main()
begin ## comment
              ##hello
## "hello"
var a <- "## comment in string"    
end

    """
        expect = "\n,\n,func,main,(,),\n,begin,## comment,\n,##hello,\n,## \"hello\",\n,var,a,<-,## comment in string,\n,end,\n,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,116))
        except:
            print("fail testcase 16")
        
    def test_case_17(self):
        input = """

func main()
begin 
             ## comment ##hello
## "hello"
var a <- "## comment in string"    
end

    """
        expect = "\n,\n,func,main,(,),\n,begin,\n,## comment ##hello,\n,## \"hello\",\n,var,a,<-,## comment in string,\n,end,\n,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,117))
        except:
            print("fail testcase 17")
        
    def test_case_18(self):
        input = """

func main()
begin 
              ##hello
## "hello"
var a <- "## comment in string"    ## comment
end

    """
        expect = "\n,\n,func,main,(,),\n,begin,\n,##hello,\n,## \"hello\",\n,var,a,<-,## comment in string,## comment,\n,end,\n,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,118))
        except:
            print("fail testcase 18")
        
    def test_case_19(self):
        input = """

func main()
begin 
              ##hello
## "hello"
var a <- "## comment in string"    
end
## comment
    """
        expect = "\n,\n,func,main,(,),\n,begin,\n,##hello,\n,## \"hello\",\n,var,a,<-,## comment in string,\n,end,\n,## comment,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,119))
        except:
            print("fail testcase 19")
        
    def test_case_20(self):
        input = """string a<-"FDCn\"s\n\"a
    """
        expect = "string,a,<-,FDCn,s,\n,Unclosed String: a"
        try:
            self.assertTrue(TestLexer.test(input,expect,120))
        except:
            print("fail testcase 20")
        
    def test_case_21(self):
        input = """string a<-"zxXY'\"s\"
    """
        expect = "string,a,<-,zxXY'\"s,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,121))
        except:
            print("fail testcase 21")
        
    def test_case_22(self):
        input = """string a<-"YWrC\"s\"
    """
        expect = "string,a,<-,YWrC,s,Unclosed String: "
        try:
            self.assertTrue(TestLexer.test(input,expect,122))
        except:
            print("fail testcase 22")
        
    def test_case_23(self):
        input = """string a<-"Ue1v'\"s\"
    """
        expect = "string,a,<-,Ue1v'\"s,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,123))
        except:
            print("fail testcase 23")
        
    def test_case_24(self):
        input = """string a<-"heOq\"s\n\"a
    """
        expect = "string,a,<-,heOq,s,\n,Unclosed String: a"
        try:
            self.assertTrue(TestLexer.test(input,expect,124))
        except:
            print("fail testcase 24")
        
    def test_case_25(self):
        input = """string a<-"AqTf'\"s a
    """
        expect = "string,a,<-,Unclosed String: AqTf'\"s a"
        try:
            self.assertTrue(TestLexer.test(input,expect,125))
        except:
            print("fail testcase 25")
        
    def test_case_26(self):
        input = """string a<-"gRPM'\"s a
    """
        expect = "string,a,<-,Unclosed String: gRPM'\"s a"
        try:
            self.assertTrue(TestLexer.test(input,expect,126))
        except:
            print("fail testcase 26")
        
    def test_case_27(self):
        input = """string a<-"BKlx'\"s\n\"a
    """
        expect = "string,a,<-,Unclosed String: BKlx'\"s"
        try:
            self.assertTrue(TestLexer.test(input,expect,127))
        except:
            print("fail testcase 27")
        
    def test_case_28(self):
        input = """string a<-"uOZV'\"s\n\"a
    """
        expect = "string,a,<-,Unclosed String: uOZV'\"s"
        try:
            self.assertTrue(TestLexer.test(input,expect,128))
        except:
            print("fail testcase 28")
        
    def test_case_29(self):
        input = """string a<-"Mvbs'\"s\n\"a
    """
        expect = "string,a,<-,Unclosed String: Mvbs'\"s"
        try:
            self.assertTrue(TestLexer.test(input,expect,129))
        except:
            print("fail testcase 29")
        
    def test_case_30(self):
        input = """ ] var <- dynamic return by dynamic string elif &
    """
        expect = "],var,<-,dynamic,return,by,dynamic,string,elif,Error Token &"
        try:
            self.assertTrue(TestLexer.test(input,expect,130))
        except:
            print("fail testcase 30")
        
    def test_case_31(self):
        input = """ dynamic return ... else '
    """
        expect = "dynamic,return,...,else,Error Token '"
        try:
            self.assertTrue(TestLexer.test(input,expect,131))
        except:
            print("fail testcase 31")
        
    def test_case_32(self):
        input = """ ;
    """
        expect = "Error Token ;"
        try:
            self.assertTrue(TestLexer.test(input,expect,132))
        except:
            print("fail testcase 32")
        
    def test_case_33(self):
        input = """ !
    """
        expect = "Error Token !"
        try:
            self.assertTrue(TestLexer.test(input,expect,133))
        except:
            print("fail testcase 33")
        
    def test_case_34(self):
        input = """ < var
 ) or < }
    """
        expect = "<,var,\n,),or,<,Error Token }"
        try:
            self.assertTrue(TestLexer.test(input,expect,134))
        except:
            print("fail testcase 34")
        
    def test_case_35(self):
        input = """ break not number by true by if {
    """
        expect = "break,not,number,by,true,by,if,Error Token {"
        try:
            self.assertTrue(TestLexer.test(input,expect,135))
        except:
            print("fail testcase 35")
        
    def test_case_36(self):
        input = """ false continue != }
    """
        expect = "false,continue,!=,Error Token }"
        try:
            self.assertTrue(TestLexer.test(input,expect,136))
        except:
            print("fail testcase 36")
        
    def test_case_37(self):
        input = """ bool >= return
 STRINGLIT continue string begin &
    """
        expect = "bool,>=,return,\n,STRINGLIT,continue,string,begin,Error Token &"
        try:
            self.assertTrue(TestLexer.test(input,expect,137))
        except:
            print("fail testcase 37")
        
    def test_case_38(self):
        input = """ dynamic bool false for $
    """
        expect = "dynamic,bool,false,for,Error Token $"
        try:
            self.assertTrue(TestLexer.test(input,expect,138))
        except:
            print("fail testcase 38")
        
    def test_case_39(self):
        input = """ ( dynamic for or NUMLIT ^
    """
        expect = "(,dynamic,for,or,NUMLIT,Error Token ^"
        try:
            self.assertTrue(TestLexer.test(input,expect,139))
        except:
            print("fail testcase 39")
        
    def test_case_40(self):
        input = """ -

 NUMLIT = ~
    """
        expect = "-,\n,\n,NUMLIT,=,Error Token ~"
        try:
            self.assertTrue(TestLexer.test(input,expect,140))
        except:
            print("fail testcase 40")
        
    def test_case_41(self):
        input = """ IDENTIFIER <= |
    """
        expect = "IDENTIFIER,<=,Error Token |"
        try:
            self.assertTrue(TestLexer.test(input,expect,141))
        except:
            print("fail testcase 41")
        
    def test_case_42(self):
        input = """ for ... == $
    """
        expect = "for,...,==,Error Token $"
        try:
            self.assertTrue(TestLexer.test(input,expect,142))
        except:
            print("fail testcase 42")
        
    def test_case_43(self):
        input = """ func false == begin <= not {
    """
        expect = "func,false,==,begin,<=,not,Error Token {"
        try:
            self.assertTrue(TestLexer.test(input,expect,143))
        except:
            print("fail testcase 43")
        
    def test_case_44(self):
        input = """ string <= + break $
    """
        expect = "string,<=,+,break,Error Token $"
        try:
            self.assertTrue(TestLexer.test(input,expect,144))
        except:
            print("fail testcase 44")
        
    def test_case_45(self):
        input = """ ... ... == #
    """
        expect = "...,...,==,Error Token #"
        try:
            self.assertTrue(TestLexer.test(input,expect,145))
        except:
            print("fail testcase 45")
        
    def test_case_46(self):
        input = """ }
    """
        expect = "Error Token }"
        try:
            self.assertTrue(TestLexer.test(input,expect,146))
        except:
            print("fail testcase 46")
        
    def test_case_47(self):
        input = """ for number number }
    """
        expect = "for,number,number,Error Token }"
        try:
            self.assertTrue(TestLexer.test(input,expect,147))
        except:
            print("fail testcase 47")
        
    def test_case_48(self):
        input = """ STRINGLIT and !
    """
        expect = "STRINGLIT,and,Error Token !"
        try:
            self.assertTrue(TestLexer.test(input,expect,148))
        except:
            print("fail testcase 48")
        
    def test_case_49(self):
        input = """ begin > <- = elif false {
    """
        expect = "begin,>,<-,=,elif,false,Error Token {"
        try:
            self.assertTrue(TestLexer.test(input,expect,149))
        except:
            print("fail testcase 49")
        
    def test_case_50(self):
        input = """string s <- " h51 \\# "
    """
        expect = "string,s,<-,Illegal Escape In String:  h51 \\#"
        try:
            self.assertTrue(TestLexer.test(input,expect,150))
        except:
            print("fail testcase 50")
        
    def test_case_51(self):
        input = """string s <- " l306L \\- "
    """
        expect = "string,s,<-,Illegal Escape In String:  l306L \\-"
        try:
            self.assertTrue(TestLexer.test(input,expect,151))
        except:
            print("fail testcase 51")
        
    def test_case_52(self):
        input = """string s <- " ct8Odwgm \\= "
    """
        expect = "string,s,<-,Illegal Escape In String:  ct8Odwgm \\="
        try:
            self.assertTrue(TestLexer.test(input,expect,152))
        except:
            print("fail testcase 52")
        
    def test_case_53(self):
        input = """string s <- " 0hqUGbIFX \\9 "
    """
        expect = "string,s,<-,Illegal Escape In String:  0hqUGbIFX \\9"
        try:
            self.assertTrue(TestLexer.test(input,expect,153))
        except:
            print("fail testcase 53")
        
    def test_case_54(self):
        input = """string s <- " U6IvgP \\# "
    """
        expect = "string,s,<-,Illegal Escape In String:  U6IvgP \\#"
        try:
            self.assertTrue(TestLexer.test(input,expect,154))
        except:
            print("fail testcase 54")
        
    def test_case_55(self):
        input = """string s <- " Qi81 \\u "
    """
        expect = "string,s,<-,Illegal Escape In String:  Qi81 \\u"
        try:
            self.assertTrue(TestLexer.test(input,expect,155))
        except:
            print("fail testcase 55")
        
    def test_case_56(self):
        input = """string s <- " l \\~ "
    """
        expect = "string,s,<-,Illegal Escape In String:  l \\~"
        try:
            self.assertTrue(TestLexer.test(input,expect,156))
        except:
            print("fail testcase 56")
        
    def test_case_57(self):
        input = """string s <- " fQdcrV \\= "
    """
        expect = "string,s,<-,Illegal Escape In String:  fQdcrV \\="
        try:
            self.assertTrue(TestLexer.test(input,expect,157))
        except:
            print("fail testcase 57")
        
    def test_case_58(self):
        input = """string s <- " mWJVg5nu \\d "
    """
        expect = "string,s,<-,Illegal Escape In String:  mWJVg5nu \\d"
        try:
            self.assertTrue(TestLexer.test(input,expect,158))
        except:
            print("fail testcase 58")
        
    def test_case_59(self):
        input = """string s <- " IdnGrpgns \\c "
    """
        expect = "string,s,<-,Illegal Escape In String:  IdnGrpgns \\c"
        try:
            self.assertTrue(TestLexer.test(input,expect,159))
        except:
            print("fail testcase 59")
        
    def test_case_60(self):
        input = """string s <- " ofwd \\1 "
    """
        expect = "string,s,<-,Illegal Escape In String:  ofwd \\1"
        try:
            self.assertTrue(TestLexer.test(input,expect,160))
        except:
            print("fail testcase 60")
        
    def test_case_61(self):
        input = """string s <- " wW \\| "
    """
        expect = "string,s,<-,Illegal Escape In String:  wW \\|"
        try:
            self.assertTrue(TestLexer.test(input,expect,161))
        except:
            print("fail testcase 61")
        
    def test_case_62(self):
        input = """string s <- "  \\1 "
    """
        expect = "string,s,<-,Illegal Escape In String:   \\1"
        try:
            self.assertTrue(TestLexer.test(input,expect,162))
        except:
            print("fail testcase 62")
        
    def test_case_63(self):
        input = """string s <- " 6 \\| "
    """
        expect = "string,s,<-,Illegal Escape In String:  6 \\|"
        try:
            self.assertTrue(TestLexer.test(input,expect,163))
        except:
            print("fail testcase 63")
        
    def test_case_64(self):
        input = """string s <- "  \\1 "
    """
        expect = "string,s,<-,Illegal Escape In String:   \\1"
        try:
            self.assertTrue(TestLexer.test(input,expect,164))
        except:
            print("fail testcase 64")
        
    def test_case_65(self):
        input = """string s <- " HtLmTM \\= "
    """
        expect = "string,s,<-,Illegal Escape In String:  HtLmTM \\="
        try:
            self.assertTrue(TestLexer.test(input,expect,165))
        except:
            print("fail testcase 65")
        
    def test_case_66(self):
        input = """string s <- " 257fC \\e "
    """
        expect = "string,s,<-,Illegal Escape In String:  257fC \\e"
        try:
            self.assertTrue(TestLexer.test(input,expect,166))
        except:
            print("fail testcase 66")
        
    def test_case_67(self):
        input = """string s <- " Cg \\= "
    """
        expect = "string,s,<-,Illegal Escape In String:  Cg \\="
        try:
            self.assertTrue(TestLexer.test(input,expect,167))
        except:
            print("fail testcase 67")
        
    def test_case_68(self):
        input = """string s <- " m0 \\u "
    """
        expect = "string,s,<-,Illegal Escape In String:  m0 \\u"
        try:
            self.assertTrue(TestLexer.test(input,expect,168))
        except:
            print("fail testcase 68")
        
    def test_case_69(self):
        input = """string s <- " 244zp \\< "
    """
        expect = "string,s,<-,Illegal Escape In String:  244zp \\<"
        try:
            self.assertTrue(TestLexer.test(input,expect,169))
        except:
            print("fail testcase 69")
        
    def test_case_70(self):
        input = """stringQF
    """
        expect = "stringQF,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,170))
        except:
            print("fail testcase 70")
        
    def test_case_71(self):
        input = """continueb2
    """
        expect = "continueb2,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,171))
        except:
            print("fail testcase 71")
        
    def test_case_72(self):
        input = """breakDM
    """
        expect = "breakDM,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,172))
        except:
            print("fail testcase 72")
        
    def test_case_73(self):
        input = """andgl
    """
        expect = "andgl,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,173))
        except:
            print("fail testcase 73")
        
    def test_case_74(self):
        input = """iftA
    """
        expect = "iftA,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,174))
        except:
            print("fail testcase 74")
        
    def test_case_75(self):
        input = """numberLG
    """
        expect = "numberLG,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,175))
        except:
            print("fail testcase 75")
        
    def test_case_76(self):
        input = """ifkw
    """
        expect = "ifkw,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,176))
        except:
            print("fail testcase 76")
        
    def test_case_77(self):
        input = """dynamicua
    """
        expect = "dynamicua,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,177))
        except:
            print("fail testcase 77")
        
    def test_case_78(self):
        input = """truecd
    """
        expect = "truecd,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,178))
        except:
            print("fail testcase 78")
        
    def test_case_79(self):
        input = """varJ5
    """
        expect = "varJ5,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,179))
        except:
            print("fail testcase 79")
        
    def test_case_80(self):
        input = """string vZptxOH <--150
    """
        expect = "string,vZptxOH,<-,-,150,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,180))
        except:
            print("fail testcase 80")
        
    def test_case_81(self):
        input = """boolean vcU0dD8 <--860
    """
        expect = "boolean,vcU0dD8,<-,-,860,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,181))
        except:
            print("fail testcase 81")
        
    def test_case_82(self):
        input = """var vIz73ja <--85
    """
        expect = "var,vIz73ja,<-,-,85,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,182))
        except:
            print("fail testcase 82")
        
    def test_case_83(self):
        input = """vIpxhBU <--1251
    """
        expect = "vIpxhBU,<-,-,1251,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,183))
        except:
            print("fail testcase 83")
        
    def test_case_84(self):
        input = """var vr2esSl <--740
    """
        expect = "var,vr2esSl,<-,-,740,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,184))
        except:
            print("fail testcase 84")
        
    def test_case_85(self):
        input = """string v8l1xDa <--170
    """
        expect = "string,v8l1xDa,<-,-,170,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,185))
        except:
            print("fail testcase 85")
        
    def test_case_86(self):
        input = """number vrcEf7b <-547
    """
        expect = "number,vrcEf7b,<-,547,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,186))
        except:
            print("fail testcase 86")
        
    def test_case_87(self):
        input = """vepNpvB <--292
    """
        expect = "vepNpvB,<-,-,292,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,187))
        except:
            print("fail testcase 87")
        
    def test_case_88(self):
        input = """boolean v6iKuDh <-1836
    """
        expect = "boolean,v6iKuDh,<-,1836,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,188))
        except:
            print("fail testcase 88")
        
    def test_case_89(self):
        input = """string vtxYExG <-1232
    """
        expect = "string,vtxYExG,<-,1232,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,189))
        except:
            print("fail testcase 89")
        
    def test_case_90(self):
        input = """var v2CsCjf <--1223
    """
        expect = "var,v2CsCjf,<-,-,1223,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,190))
        except:
            print("fail testcase 90")
        
    def test_case_91(self):
        input = """vn3ZlBY <-157
    """
        expect = "vn3ZlBY,<-,157,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,191))
        except:
            print("fail testcase 91")
        
    def test_case_92(self):
        input = """func f4M0KwY() \n begin \ndynamic vfdY4xd <-1932\n end
    """
        expect = "func,f4M0KwY,(,),\n,begin,\n,dynamic,vfdY4xd,<-,1932,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,192))
        except:
            print("fail testcase 92")
        
    def test_case_93(self):
        input = """vtxITOS <-350
    """
        expect = "vtxITOS,<-,350,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,193))
        except:
            print("fail testcase 93")
        
    def test_case_94(self):
        input = """func fnOkPoK() \n begin \nstring vqa7cdc <--2138\n end
    """
        expect = "func,fnOkPoK,(,),\n,begin,\n,string,vqa7cdc,<-,-,2138,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,194))
        except:
            print("fail testcase 94")
        
    def test_case_95(self):
        input = """vW0L4bp <-2092
    """
        expect = "vW0L4bp,<-,2092,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,195))
        except:
            print("fail testcase 95")
        
    def test_case_96(self):
        input = """var v4eDx4O <--858
    """
        expect = "var,v4eDx4O,<-,-,858,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,196))
        except:
            print("fail testcase 96")
        
    def test_case_97(self):
        input = """func foJki3t(puiEk1b,paiCdMm) \n begin \nvoL6H8P <-2292\n end
    """
        expect = "func,foJki3t,(,puiEk1b,,,paiCdMm,),\n,begin,\n,voL6H8P,<-,2292,\n,end,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,197))
        except:
            print("fail testcase 97")
        
    def test_case_98(self):
        input = """vIaFpjP <--403
    """
        expect = "vIaFpjP,<-,-,403,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,198))
        except:
            print("fail testcase 98")
        
    def test_case_99(self):
        input = """var vsw927L <-559
    """
        expect = "var,vsw927L,<-,559,\n,<EOF>"
        try:
            self.assertTrue(TestLexer.test(input,expect,199))
        except:
            print("fail testcase 99")
        