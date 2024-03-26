import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_number(self):
        input = """func main ()
        begin
            writeNumber(1)
        end
        """
        expect = "1.0"
        #self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_string(self):
        input = """func main ()
        begin
            writeString("Hello World")
        end
        """
        expect = "Hello World"
        #self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_boolean(self):
        input = """func main ()
        begin
            writeBool(true)
        end
        """
        expect = "true"
        #self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_decl(self):
        input = """func main ()
        begin
            var a <- 1
            writeNumber(a)
        end
        """
        expect = "1.0"
        #self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_decl_2(self):
        input = """
        
        var a <- 1
        func main ()
        begin
            dynamic b <- a
            writeNumber(b)
        end
        """
        expect = "1.0"
        #self.assertTrue(TestCodeGen.test(input, expect, 504))
    
    def test_binary_binary_op_1(self):
        input = """func main ()
        begin
            writeNumber(1 + 2)
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    