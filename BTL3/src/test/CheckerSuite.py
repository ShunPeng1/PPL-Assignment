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
                bool b2 <- b1 and (1 <= 3)
                return 0
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
                return 0

            func foo(number a, number b)
                return 0
               """
        expect = "[]"
        self.assertTrue(TestChecker.test(input, expect, 415))