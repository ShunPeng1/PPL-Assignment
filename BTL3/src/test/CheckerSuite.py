import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_no_entry_point(self):
        input = """number a
        """
        expect = "No Entry Point"
        #self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redeclared_variable(self):
        input = """number a
        number a
        """
        expect = "Redeclared Variable: a"
        #self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclared_function(self):
        input = """
        func main() 
            return 0
        
        func main() 
            return 0
        """
        expect = "Redeclared Function: main"
        #self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclared_parameter(self):
        input = """
        func main(number a, number a) 
            return 0
        """
        expect = "Redeclared Parameter: a"
        #self.assertTrue(TestChecker.test(input, expect, 403))

    def test_variable_declare(self):
        input = """
            string s1
            bool b1
            string s2 <- "1"
            bool b2 <- true
        
        """
        expect = "No Entry Point"
        #self.assertTrue(TestChecker.test(input, expect, 404))

    def test_variable_declare_2(self):
        input = """
            string s2 <- "1" ... "2"
        """
        expect = "No Entry Point"
        #self.assertTrue(TestChecker.test(input, expect, 405))

    def test_variable_declare_3(self):
        input = """
            string s2 <- "1" ... 2
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., StringLit(1), NumLit(2.0)))"
        #self.assertTrue(TestChecker.test(input, expect, 406))

    def test_variable_declare_4(self):
        input = """
            number s2 <- "1" ... "2"
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(s2), NumberType, None, BinaryOp(..., StringLit(1), StringLit(2))))"
        #self.assertTrue(TestChecker.test(input, expect, 407))

    def test_variable_declare_5(self):
        input = """
            bool s2 <- ("1" ... "2") == ("12" ... "2") 
        """
        expect = "No Entry Point"
        #self.assertTrue(TestChecker.test(input, expect, 408))

    def test_variable_declare_6(self):
        input = """
            bool b1 <- true
            bool b2 <- true and b1
            bool b3 <- (true and not b1) and b2
        """
        expect = "No Entry Point"
        #self.assertTrue(TestChecker.test(input, expect, 409))

    def test_variable_declare_7(self):
        input = """
            bool b1 <- (true and not b1)
        """
        expect = "Undeclared Identifier: b1"
        #self.assertTrue(TestChecker.test(input, expect, 410))

    def test_variable_declare_7(self):
        input = """
            bool b1 <- true
        
            func main()
            begin 
                bool b2 <- b1 and (1 <= 3)
                return
            end
        """
        expect = "[]"
        #self.assertTrue(TestChecker.test(input, expect, 411))

    def test_variable_declare_8(self):
        input = """
            string s1 <- "1"
            string s2 <- "1" ... "2"
            string s3 <- s1 ... s2
        """
        expect = "No Entry Point"
        #self.assertTrue(TestChecker.test(input, expect, 412))
    

    def test_function_declare_1(self):
        input = """
            func foo(number a, number b)
                return 0

            func main() 
                return 0
        """
        expect = "[]"
        #self.assertTrue(TestChecker.test(input, expect, 413))
        
    def test_function_declare_2(self):
        input = """
            func foo(number a, number a)
                return 0

            func main() 
                return 0
        """
        expect = "Redeclared Parameter: a"
        #self.assertTrue(TestChecker.test(input, expect, 414))

    def test_function_declare_3(self):
        input = """
            func foo(number a, number b)
            
            func main() 
                return

            func foo(number c, number d)
                return 0
               """
        expect = "[]"
        #self.assertTrue(TestChecker.test(input, expect, 415))

    def test_function_declare_4(self):
        input = """
            func foo(number a, number b)
            
            func main() 
                return 0

            func foo(bool a, number b)
                return 0
               """

        expect = "Redeclared Function: foo"
        #self.assertTrue(TestChecker.test(input, expect, 416))

    def test_function_declare_5(self):
        input = """
            func foo(number a, number b)
            
            func main() 
                return 0

            func foo(number a, number b, number c)
                return 0
               """
        expect = "Redeclared Function: foo"
        #self.assertTrue(TestChecker.test(input, expect, 417))

    def test_function_declare_6(self):
        input = """
            func foo(number a, number b)
            
            func main() 
                return 0

            func foo(number a, number b)
                return 0

            func foo(number a, number b)
                return 0
               """
        expect = "Redeclared Function: foo"
        #self.assertTrue(TestChecker.test(input, expect, 418))

    def test_function_declare_7(self):
        input = """
            func foo(number a, number b)
            
            func main() 
                return 0

            func foo(number a, number b)
               """
        expect = "Redeclared Function: foo"
        #self.assertTrue(TestChecker.test(input, expect, 419))


    def test_inferring_type_1(self):
        input = """
            var a <- -1 + 1
            func main()
                return
        """
        expect = "[]"
        #self.assertTrue(TestChecker.test(input, expect, 420))

    def test_inferring_type_2(self):
        input = """
            var a <- 1 + true
            func main()
                return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), BooleanLit(True)))"
        #self.assertTrue(TestChecker.test(input, expect, 421))

    def test_inferring_type_3(self):
        input = """
            var a <- 1
            var b <- 1 + a
            var c <- -b <= a
            var d <- b and not c
            
            func main()
                return
            
        """
        expect = "Type Mismatch In Expression: BinaryOp(and, Id(b), UnaryOp(not, Id(c))))"
        #self.assertTrue(TestChecker.test(input, expect, 422))

    def test_inferring_type_4(self):
        input = """
            var a <- 1
            var c <- b <= a
            var d <- 1 + c
                
            func main()
            begin            
                return
            end
        """
        expect = "Undeclared Identifier: b"
        #self.assertTrue(TestChecker.test(input, expect, 423))

    def test_inferring_type_5(self):
        input = """
            var a <- 1
            var c <- a <= 1
            var d <- 1 + c
                
            func main()
            begin            
                return
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), Id(c)))"
        #self.assertTrue(TestChecker.test(input, expect, 424))

    def test_function_definition_1(self):
        input = """
            func foo(number a, number b)
                
            func main() 
                return 0
        """
        expect = "No Function Definition: foo"
        #self.assertTrue(TestChecker.test(input, expect, 425))

    def test_function_definition_2(self):
        input = """
            func main() 
            
        """
        expect = "No Function Definition: main"
        #self.assertTrue(TestChecker.test(input, expect, 426))


    def test_function_definition_3(self):
        input = """
            func main()
            
            func main() 
                return 0
        """
        expect = "[]"
        #self.assertTrue(TestChecker.test(input, expect, 427))

    def test_dynamic_type_1(self):
        input = """
            dynamic a
            dynamic b
            dynamic c <- a + b
            func main()
                return
        """
        expect = "[]"
        #self.assertTrue(TestChecker.test(input, expect, 428))

    def test_dynamic_type_2(self):
        input = """
            dynamic a
            dynamic b <- a
            func main()
                return
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, dynamic, Id(a))"
        #self.assertTrue(TestChecker.test(input, expect, 429))


    def test_dynamic_type_3(self):
        input = """
            dynamic a
            dynamic b
            dynamic c <- a + b
            dynamic d <- c and true

            func main()
                return
        """
        expect = "Type Mismatch In Expression: BinaryOp(and, Id(c), BooleanLit(True)))"
        #self.assertTrue(TestChecker.test(input, expect, 430))











    

        # KIEN TESTCASES
    def test441(self):
        input = """
number a <- 1 + "Hello"
func main()
    return
"""
        expect = "Type Mismatch In Expression: BinaryOp(+,NumLit(1.0),StringLit(Hello))"
        self.assertTrue(TestChecker.test(input, expect, 441))
    
    def test442(self):
        input = """
func f()

func main()
begin
    number x <- g(1, 2, 3)
end
"""
        expect = "Undeclared Function: g"
       #!self.assertTrue(TestChecker.test(input, expect, 442))
    
    def test443(self):
        input = """
number x
number y
func f()

func main()
    return
"""
        expect = "No Function Definition: f"
       #!self.assertTrue(TestChecker.test(input, expect, 443))
    
    def test444(self):
        input = """
func f()

number f
dynamic x
func main()
    return
"""
        expect = "Redeclared Variable: f"
       #!self.assertTrue(TestChecker.test(input, expect, 444))
    
    def test445(self):
        input = """
func f()
begin

end
dynamic a
number b
bool c
string d
"""
        expect = "No Entry Point"
       #!self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test446(self):
        input = """
func f(number x)
begin
    return f(x)
end

func main()
begin
    dynamic d <- f(10)
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(dynamic,Id(d),CallExpr(Id(f),[NumLit(10.0)]))"
       #!self.assertTrue(TestChecker.test(input, expect, 446))
    
    def test447(self):
        input = """
func f(number x)
begin
    return 1
end

func main()
begin
    f(2018)
end
"""
        expect = "Type Mismatch In Statement: Call(Id(f),[NumLit(2018.0)])"
       #!self.assertTrue(TestChecker.test(input, expect, 447))
    
    def test448(self):
        input = """
func main()
begin
    continue
end
"""
        expect = "Continue Not In Loop"
       #!self.assertTrue(TestChecker.test(input, expect, 448))
    
    def test449(self):
        input = """
func main()
begin
    break
end
"""
        expect = "Break Not In Loop"
       #!self.assertTrue(TestChecker.test(input, expect, 449))
    
    def test450(self):
        input = """
number x
number y
func add()
    return x + y

func main()
begin
    x <- readNumber()
    y <- readNumber()
    writeNumber(add())
end
"""
        expect = ""
       #!self.assertTrue(TestChecker.test(input, expect, 450))