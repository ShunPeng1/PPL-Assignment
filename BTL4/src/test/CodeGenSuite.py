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
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_boolean(self):
        input = """func main ()
        begin
            writeBool(true)
        end
        """
        expect = "true"
        #self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_boolean2(self):
        input = """func main ()
        begin
            writeBool(readBool())
        end
        """
        expect = ""
        #self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_number2(self):
        input = """func main ()
        begin
            writeNumber(readNumber())
        end
        """
        expect = ""
        #self.assertTrue(TestCodeGen.test(input, expect, 504))
    
    def test_string2(self):
        input = """func main ()
        begin
            writeString(readString())
        end
        """
        expect = ""
        #self.assertTrue(TestCodeGen.test(input, expect, 505))