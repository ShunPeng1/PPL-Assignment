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
    
    def test_binary_op_1(self):
        input = """func main ()
        begin
            writeNumber(1 + 2)
        end
        """
        expect = "3.0"
        #self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_binary_op_2(self):
        input = """func main ()
        begin
            writeNumber(1 - 2)
        end
        """
        expect = "-1.0"
        #self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_binary_op_3(self):
        input = """func main ()
        begin
            writeNumber(1 * 2)
        end
        """
        expect = "2.0"
        #self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_binary_op_4(self):
        input = """func main ()
        begin
            writeNumber(1 / 2)
        end
        """
        expect = "0.5"
        #self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_binary_op_5(self):
        input = """func main ()
        begin
            writeNumber(1 % 2)
        end
        """
        expect = "1.0"
        #self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_binary_op_6(self):
        input = """func main ()
        begin
            writeBool(1 > 2)
        end
        """
        expect = "false"
        #self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_binary_op_7(self):
        input = """func main ()
        begin
            writeBool(1 < 2)
        end
        """
        expect = "true"
        #self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_binary_op_8(self):
        input = """func main ()
        begin
            writeBool(1 >= 2)
        end
        """
        expect = "false"
        #self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_binary_op_9(self):
        input = """func main ()
        begin
            writeBool(1 <= 2)
        end
        """
        expect = "true"
        #self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_binary_op_10(self):
        input = """func main ()
        begin
            writeBool(1 = 2)
        end
        """
        expect = "false"
        #self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_binary_op_11(self):
        input = """func main ()
        begin
            writeBool(1 != 2)
        end
        """
        expect = "true"
        #self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_binary_op_12(self):
        input = """func main ()
        begin
            var d <- "4" == "4"
            writeBool(d)
        end
        """
        expect = "true"
        #self.assertTrue(TestCodeGen.test(input, expect, 516))
    
    def test_binary_op_13(self):
        input = """func main ()
        begin
            string d <- "1" ... "2"
            writeString(d)
        end
        """
        expect = "12"
        #self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_binary_op_14(self):
        input = """func main ()
        begin
            writeBool(("1" ... "2") == ("1" ... "2"))
        end
        """
        expect = "true"
        #self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_binary_op_15(self):
        input = """func main ()
        begin
            writeBool("1" == "2")
        end
        """
        expect = "false"
        #self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_unary_op_1(self):
        input = """func main ()
        begin
            writeNumber(-1)
        end
        """
        expect = "-1.0"
        #self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_unary_op_2(self):
        input = """func main ()
        begin
            writeBool(not true)
        end
        """
        expect = "false"
        #self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_unary_op_3(self):
        input = """func main ()
        begin
            writeBool(not false)
        end
        """
        expect = "true"
        #self.assertTrue(TestCodeGen.test(input, expect, 522))
