import random as rd
import numpy as np
import re
TOKENS = [
    '\n', 'true', 'false', 'number', 'bool', 'string', 'return', 'var', 'dynamic',
    'func', 'for', 'until', 'by', 'break', 'continue', 'if', 'else', 'elif', 'begin',
    'end', 'and', 'or', 'not', '+', '-', '*', '/', '%', '=', '<-', '!=', '<', '<=',
    '>', '>=', '...', '==', ',', '(', ')', '[', ']','IDENTIFIER','STRINGLIT','NUMLIT' 
]


def genString(length=10):
    seed = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    ans = ''
    for i in range(length):
        ans += seed[np.random.randint(len(seed))]
    return ans
def getParlist():
    num = np.random.randint(0,5)
    lex = []
    ans = []
    for i in range(num):
        iden = 'p'+genString(6)
        lex.append(iden)
        lex.append(',')
        ans.append(iden)
    if lex != []:
        lex = lex[:-1]
    ans = ','.join(ans)
    return ans,lex

def genStatement():
    statement = ['declare_func','declare_func','declare_var','declare_var','declare_var','assignment']
    ans = ""
    lex = []
    kind = statement[np.random.randint(len(statement))]
    if kind == 'declare_func':
        function_name = 'f'+genString(6)
        ans += f"func {function_name}("
        lex = lex + ['func', function_name, '(']
        para,paralex = getParlist()
        ans = ans + para + ') \\n begin \\n'
        lex = lex+paralex
        lex.append(')')
        lex.append('\\n')
        lex.append('begin')
        lex.append('\\n')
        body_statment, body_lex = genStatement()
        ans += body_statment
        lex = lex + body_lex
        ans += '\\n end'
        lex.append('\\n')
        lex.append('end')
    elif kind == 'declare_var':
        type_declare = ['var','dynamic','number','string','boolean']
        type_declare = type_declare[np.random.randint(len(type_declare))]
        iden = 'v'+genString(6)
        value = rd.randint(-3000,3000)
        lex = [type_declare,iden,'<-']
        if value<0:
            lex.append('-')
        lex.append(str(np.abs(value)))
        ans = type_declare + ' '+iden  +' <-' + str(value)
    elif kind == 'assignment':
        iden = 'v'+genString(6)
        value = rd.randint(-3000,3000)
        lex = [iden,'<-']
        if value<0:
            lex.append('-')
        lex.append(str(np.abs(value)))
        ans = iden  +' <-' + str(value)
    return ans,lex
def testcase(idx,input,expect,kind):
    if kind == "lexer":
        testcase = f"""
    def test_case_{idx}(self):
        input = \"\"\"{input}
    \"\"\"
        expect = "{expect}"
        try:
            self.assertTrue(TestLexer.test(input,expect,{100+idx}))
        except:
            print("fail testcase {idx}")
        """
        return testcase
    elif kind=='parser':
        testcase = f"""
    def test_case_{idx}(self):
        input = \"\"\"{input}
        \"\"\"
        expect = "{expect}"
        self.assertTrue(TestParser.test(input,expect,{200+idx}))
        """
        return testcase
    return ''
def createLexerTestCase(seed=142):
    np.random.seed(seed)
    rd.seed(seed)
    filename = "LexerSuite.py"
    ws = ['\n', ' ','\t', '\t',' ', ' ']
    with open(filename,mode='w') as f:
        f.write("""import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase): 
""")
        for idx in range(100):
            if idx<10: #first 10 testcase just about token
                expect = []
                num_tokens = rd.randint(1,100)
                code = ""
                for i in range(num_tokens):
                    token = TOKENS[np.random.randint(len(TOKENS))]
                    if token == '"':
                        continue
                    space = ws[np.random.randint(6)]
                    if space == '\n': expect.append('\\n')
                    if token == "STRINGLIT":
                        token = '"abcd"'
                        expect.append("abcd")
                    elif token == "NUMLIT":
                        decimal = ""
                        if np.random.uniform() < 0.5:
                            decimal = "."+str(np.random.randint(100))
                        exponent = ""
                        if np.random.uniform() < 0.5:
                            exponent = 'e' if  np.random.uniform() < 0.5 else 'E'
                            exponent += '-' if  np.random.uniform() < 0.5 else ''
                            exponent += str(np.random.randint(100)**2)
                        token = str(np.random.randint(142)) + decimal + exponent
                        expect.append(token)
                    elif token == "IDENTIFIER":
                        token = "a1"
                        expect.append(token)
                    elif token == '\n':
                        expect.append('\\n')
                    else:
                        expect.append(token)
                    code = code+space+token
                expect.append('\\n') 
                expect.append('<EOF>')
                f.write(testcase(idx,code,','.join(expect),'lexer'))
            elif idx>=10 and idx < 15: #about identifier
                iden = ['abc123','1ae','1.232eabc','abC1#','_abt']
                expect = [['abc123','\\n','<EOF>'],['1','ae','\\n','<EOF>'],['1.232','eabc','\\n','<EOF>'],
                          ['abC1','Error Token #'],['_abt','\\n','<EOF>']]
                f.write(testcase(idx,'dynamic '+iden[idx-10],','.join(['dynamic']+expect[idx-10]),'lexer'))
            elif idx>=15 and idx<20: # comment check
                blank = {i:"" for i in range(5)}
                expect = ["func","main","(",")","\\n","begin","\\n","##hello","\\n",'## \\"hello\\"',"\\n","var","a","<-", "## comment in string","\\n", "end","\\n",'\\n',"<EOF>"]
                blank[idx-15] = "## comment"
                code = f"""
{blank[0]}
func main()
begin {blank[1]}
             {blank[2]} ##hello
## "hello"
var a <- "## comment in string"    {blank[3]}
end
{blank[4]}"""
                if idx-15 == 0:
                    expect = ["## comment", "\\n"] + expect
                elif idx-15==1:
                    expect = expect[:6] + ["## comment"] + expect[6:]
                elif idx-15==2:
                    expect[7] = '## comment ##hello'
                elif idx-15==3:
                    expect = expect[:-5] + ["## comment"] + expect[-5:]
                elif idx-15==4:
                    expect = expect[:-2] + ["## comment"] + expect[-2:]
                expect = ["\\n"]+ expect
                if idx-15 > 0:
                    expect = ["\\n"]+ expect
                f.write(testcase(idx,code,','.join(expect),'lexer'))
            elif idx >= 20 and idx < 30: #string open check
                part1 = genString(4)
                part2 = "'\\\"" if np.random.randint(4) != 0 else '\\"'
                closequote = ['\\"','\\n\\"a',' a']
                part3 = closequote[np.random.randint(3)]
                input = f"string a<-\"{part1}{part2}s{part3}"
                expect = ["string", "a","<-"]
                if part2 == '\\"' :
                    expect.append(part1)
                    expect.append('s')
                else:
                    part1+= part2
                    part1+='s'
                if expect[-1]=='<-':
                    if part3 == '\\"':
                        expect.append(part1)
                        expect.append('\\n')
                        expect.append('<EOF>')
                    elif part3 == ' a':
                        part1+=part3
                        expect.append('Unclosed String: '+part1)
                    else:
                        expect.append('Unclosed String: '+part1)
                else: 
                    if part3 == ' a':
                        expect.append('a')
                        expect.append('\\n')
                        expect.append('<EOF>')
                    elif part3 == '\\n\\"a':
                        expect.append('\\n')
                        expect.append("Unclosed String: a")
                    else:
                        expect.append("Unclosed String: ")
                f.write(testcase(idx,input,','.join(expect),'lexer'))
            elif idx >=30 and idx <50: ##error token
                errorToken = ["'",'!',';','~','{','}','|','$','#','@','&','^']
                length = np.random.randint(10)
                input = ""
                expect = []
                for i in range(length):
                    token = TOKENS[np.random.randint(len(TOKENS))]
                    if token == '\n':
                        expect.append('\\n')
                        input += token
                    else:
                        expect.append(token)
                        input = input + ' ' + token
                errorTok = errorToken[np.random.randint(len(errorToken))]
                input = input + ' ' + errorTok
                expect.append("Error Token "+errorTok)
                f.write(testcase(idx,input,','.join(expect),'lexer'))
            elif idx >=50 and idx < 70: ### illegal escape
                errorEscape = ['a','c','d','e','#','|','?','~','(','A','z','9',
                               'u','-',' ','\\"',',','=','1','<']
                errorTok = errorEscape[np.random.randint(len(errorEscape))]
                content = genString(np.random.randint(10))
                input = f'string s <- \" {content} \\\\{errorTok} \"'
                expect = ['string','s','<-']
                expect.append("Illegal Escape In String:  "+content + ' \\\\'+errorTok)
                f.write(testcase(idx,input,','.join(expect),'lexer'))
            elif idx >= 70 and idx<80: ## like keyword
                keyword = TOKENS[np.random.randint(1,23)]
                input = keyword + genString(2)
                expect = [input,'\\n','<EOF>']
                f.write(testcase(idx,input,','.join(expect),'lexer'))
            else:
                input,expect = genStatement()
                expect+= ['\\n','<EOF>']
                f.write(testcase(idx,input,','.join(expect),'lexer'))


def main(seed=142):
    seed = input("Enter seed: ")
    createLexerTestCase(int(seed))

main()