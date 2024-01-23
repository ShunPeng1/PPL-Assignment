import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_KeyWord_Operators_Separators(self):
        """test KeyWord Operators Separators"""
        
        ##^ test KeyWord
        input = "true false number bool string return var dynamic func for until by break continue if else elif begin end not and or"
        expect = "true,false,number,bool,string,return,var,dynamic,func,for,until,by,break,continue,if,else,elif,begin,end,not,and,or,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,101))
        
        ##^ test Operators
        input = "+-*/%= <- != < <= > >= ... =="
        expect = "+,-,*,/,%,=,<-,!=,<,<=,>,>=,...,==,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,102))

        ##^ test Separators
        input = "[(,,)]"
        expect = "[,(,,,,,),],<EOF>"
        self.assertTrue(TestLexer.test(input,expect,103))
        
        ##^ test fail toán tử
        input = "&"
        expect = "Error Token &"
        self.assertTrue(TestLexer.test(input,expect,104))
        
        input = "#"
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input,expect,105))
        
    def test_Identifiers(self):
        """test Identifiers"""
        ##^ test true ID
        self.assertTrue(TestLexer.test("A _ a az AZ aZ _a a_ a1 _1 A1", "A,_,a,az,AZ,aZ,_a,a_,a1,_1,A1,<EOF>", 106))     

        ##^ test false ID
        self.assertTrue(TestLexer.test("1Tienc", "1,Tienc,<EOF>", 107))
        self.assertTrue(TestLexer.test("11Tienc", "11,Tienc,<EOF>", 108))
        
    def test_Literal(self):
        """test Identifiers"""   
        
        ##^ test NUMBER_LIT    
        input = "0 -0 199 001 012. 12. 0. 12.3 12.3e3 12.3e-30 2.e3 0.e-30 31e+3 31e-3 0e+3 0e-3"
        expect = "0,-,0,199,001,012.,12.,0.,12.3,12.3e3,12.3e-30,2.e3,0.e-30,31e+3,31e-3,0e+3,0e-3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,109))
        ##^ fail NUMBER_LIT
        self.assertTrue(TestLexer.test(".12e-3","Error Token .",110))
        self.assertTrue(TestLexer.test("12.2h-3","12.2,h,-,3,<EOF>",111))
        
        ##^ test STRING_LIT 
        input = """ "Vo  Tien" """ # kiểm tra bình thường
        expect = "Vo  Tien,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,112))
        self.assertTrue(TestLexer.test(""" "" """,",<EOF>",113)) # chuỗi rỗng
        
        ##^ kiểm tra các kí tự cho phép
        input = """ "\\b \\f \\r \\n \\t \\\\ Vo \\b \\f \\r \\n \\t \\\\  Tien \\b \\f \\r \\n \\t \\\\" """
        expect = "\\b \\f \\r \\n \\t \\\\ Vo \\b \\f \\r \\n \\t \\\\  Tien \\b \\f \\r \\n \\t \\\\,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,114))
        self.assertTrue(TestLexer.test(""" "'"Vo '" Tien '"" ""","'\"Vo '\" Tien '\",<EOF>",115))
        
        ##^ kiểm tra lỗi Unclosed String
        self.assertTrue(TestLexer.test(""" "Vo \n" """, "Unclosed String: Vo ", 116))
        self.assertTrue(TestLexer.test(""" "Vo \n Tien" """, "Unclosed String: Vo ", 117))
        self.assertTrue(TestLexer.test(""" "Vo  """, "Unclosed String: Vo  ", 118))
        self.assertTrue(TestLexer.test(""" "Vo \\n \n """, "Unclosed String: Vo \\n ", 119))
        self.assertTrue(TestLexer.test(""" "Vo \\n \\b """, "Unclosed String: Vo \\n \\b ", 120))
        
        ##^ kiểm tra lỗi Illegal Escape
        #self.assertTrue(TestLexer.test(""" "Tien \t \n" """, "Illegal Escape In String: Tien 	", 121))
        self.assertTrue(TestLexer.test(""" "Tien \f \n ccc" """, "Illegal Escape In String: Tien \f", 122))
        self.assertTrue(TestLexer.test(""" "Tien \\1  """, "Illegal Escape In String: Tien \\1", 123))
        self.assertTrue(TestLexer.test(""" "Tien \\2 \\n \n """, "Illegal Escape In String: Tien \\2", 124))
        self.assertTrue(TestLexer.test(""" "Tien \\e \\n \\r """, "Illegal Escape In String: Tien \\e", 125))        
        self.assertTrue(TestLexer.test(""" "Tien \\321 \\n \\r """, "Illegal Escape In String: Tien \\3", 126))
        self.assertTrue(TestLexer.test(""" "Tien \\"1 " """, "Illegal Escape In String: Tien \\\"", 127))          
        self.assertTrue(TestLexer.test(""" "Tien ' " " """, "Illegal Escape In String: Tien ' ", 128))
        self.assertTrue(TestLexer.test(""" "Tien \\' ""1 """, "Tien \\' ,Unclosed String: 1 ", 129))  
        
    def test_Comments_newline(self):
        """test Comments và newline""" 
        self.assertTrue(TestLexer.test("## Vo tien","## Vo tien,<EOF>",130))    
        self.assertTrue(TestLexer.test("###","###,<EOF>",131)) 
        self.assertTrue(TestLexer.test("a##1","a,##1,<EOF>",132)) 
        self.assertTrue(TestLexer.test("a#","a,Error Token #",133))    
        self.assertTrue(TestLexer.test("a\n##1\nb","a,\n,##1,\n,b,<EOF>",134))  
        self.assertTrue(TestLexer.test("a\n\n\n#","a,\n,\n,\n,Error Token #",135))     

    def test_shun(self):
        input = " var ShunPeng <- true and \"true\" or 1"
        expect = "var,ShunPeng,<-,true,and,true,or,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 199))
        
        input = """var VoTien <- a()()
        """
        expect = """var,VoTien,<-,a,(,),(,),\n,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 198))  
        

        input = """ 
            var VoTien
        """
        expect = "\n,var,VoTien,\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 197))   

    def test_khang(self):
          
        input = '''"\f'"\n\t"'''
        expected = "UnclosedString: \f'"
        self.assertTrue(TestLexer.test(input, expected, 21530111001))
