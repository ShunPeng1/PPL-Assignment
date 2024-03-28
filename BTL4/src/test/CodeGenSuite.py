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
        expect = "1.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_string(self):
        input = """func main ()
        begin
            writeString("Hello World")
        end
        """
        expect = "Hello World\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_boolean(self):
        input = """func main ()
        begin
            writeBool(true)
        end
        """
        expect = "true\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_decl(self):
        input = """func main ()
        begin
            var a <- 1
            writeNumber(a)
        end
        """
        expect = "1.0\n"
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
        expect = "1.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 504))
    
    def test_binary_op_1(self):
        input = """func main ()
        begin
            writeNumber(1 + 2)
        end
        """
        expect = "3.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_binary_op_2(self):
        input = """func main ()
        begin
            writeNumber(1 - 2)
        end
        """
        expect = "-1.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_binary_op_3(self):
        input = """func main ()
        begin
            writeNumber(1 * 2)
        end
        """
        expect = "2.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_binary_op_4(self):
        input = """func main ()
        begin
            writeNumber(1 / 2)
        end
        """
        expect = "0.5\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_binary_op_5(self):
        input = """func main ()
        begin
            writeNumber(1 % 2)
        end
        """
        expect = "1.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_binary_op_6(self):
        input = """func main ()
        begin
            writeBool(1 > 2)
        end
        """
        expect = "false\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_binary_op_7(self):
        input = """func main ()
        begin
            writeBool(1 < 2)
        end
        """
        expect = "true\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_binary_op_8(self):
        input = """func main ()
        begin
            writeBool(1 >= 2)
        end
        """
        expect = "false\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_binary_op_9(self):
        input = """func main ()
        begin
            writeBool(1 <= 2)
        end
        """
        expect = "true\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_binary_op_10(self):
        input = """func main ()
        begin
            writeBool(1 = 2)
        end
        """
        expect = "false\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_binary_op_11(self):
        input = """func main ()
        begin
            writeBool(1 != 2)
        end
        """
        expect = "true\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_binary_op_12(self):
        input = """func main ()
        begin
            var d <- "4" == "4"
            writeBool(d)
        end
        """
        expect = "true\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 516))
    
    def test_binary_op_13(self):
        input = """func main ()
        begin
            string d <- "1" ... "2"
            writeString(d)
        end
        """
        expect = "12\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_binary_op_14(self):
        input = """func main ()
        begin
            writeBool(("1" ... "2") == ("1" ... "2"))
        end
        """
        expect = "true\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_binary_op_15(self):
        input = """func main ()
        begin
            writeBool("1" == "2")
        end
        """
        expect = "false\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_unary_op_1(self):
        input = """func main ()
        begin
            writeNumber(-1)
        end
        """
        expect = "-1.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_unary_op_2(self):
        input = """func main ()
        begin
            writeBool(not true)
        end
        """
        expect = "false\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_unary_op_3(self):
        input = """func main ()
        begin
            writeBool(not false)
        end
        """
        expect = "true\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 522))


    def test_unary_assign_1(self):
        input = """func main ()
        begin
            var a <- 1
            a <- -a
            writeNumber(a)
        end
        """
        expect = "-1.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_unary_assign_2(self):
        input = """
        var a <- true
        func main ()
        begin
            
            a <- not a
            writeBool(a)
        end
        """
        expect = "false\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_unary_assign_3(self):
        input = """
        var a <- false
        var b <- not a
        func main ()
        begin
            writeBool(a)
            writeBool(b)

            b <- not b
            writeBool(b)
            a <- not a
            writeBool(a)
            var c <- a and (not b) and (false or true)

            writeBool(c)
        end
        """
        expect = """false
true
false
true
true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_if_1(self):
        input = """func main ()
        begin
            if (true)
                writeNumber(1)
            else 
                writeNumber(2)
        end
        """
        expect = "1.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_if_2(self):
        input = """
        func main ()
        begin
            if (false)
                writeNumber(1)
            else 
                writeNumber(2)
        end
        """
        expect = "2.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_if_3(self):
        input = """func main ()
        begin
            if (false)
                writeNumber(1)
            elif (true)
                writeNumber(2)
            else 
                writeNumber(3)
        end
        """
        expect = "2.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_if_4(self):
        input = """func main ()
        begin
            if (false)
                writeNumber(1)
            elif (false)
                writeNumber(2)
            else 
                writeNumber(3)
        end
        """
        expect = "3.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_if_5(self):
        input = """func main ()
        begin
            if (false)
                writeNumber(1)
            elif (false)
                writeNumber(2)
            elif (true)
                writeNumber(3)
            else 
                writeNumber(4)
        end
        """
        expect = "3.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_if_6(self):
        input = """func main ()
        begin
            if (false)
                writeNumber(1)
            elif (false)
                writeNumber(2)
            elif (false)
                writeNumber(3)
            else 
                writeNumber(4)
        end
        """
        expect = "4.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_if_7(self):
        input = """func main ()
        begin
            if (false)
                writeNumber(1)
            writeNumber(4)   
        end
        """
        expect = "4.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_if_8(self):
        input = """func main ()
        begin
            if (false)
                writeNumber(1)
            elif (false)
                writeNumber(2)
            elif (false)
                writeNumber(3)
            writeNumber(4)
        end
        """
        expect = "4.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_for_1(self):
        input = """func main ()
        begin
            var i <- 0
            for i until i >= 10 by 1
                writeNumber(i)
             
        end
        """
        expect = """0.0
1.0
2.0
3.0
4.0
5.0
6.0
7.0
8.0
9.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_for_2(self):  
        input = """func main ()
        begin
            var i <- 5
            for i until i <= -5 by -1
                writeNumber(i)
             
        end
        """
        expect = """5.0
4.0
3.0
2.0
1.0
0.0
-1.0
-2.0
-3.0
-4.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 535))


    def test_for_3(self):
        input = """func main ()
        begin
            var i <- 0
            for i until i >= 10 by 1
            begin
                if (i = 4)
                    break
                    
                writeNumber(i)
            end
        end
        """
        expect = """0.0
1.0
2.0
3.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_for_4(self):
        input = """func main ()
        begin
            var i <- 0
            for i until i >= 10 by 1
            begin
                if (i <= 7)
                    continue
                    
                writeNumber(i)
            end
        end
        """
        expect = """8.0
9.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_for_5(self):
        input = """func main ()
        begin
            var i <- 0
            for i until i >= 3 by 1
            begin       
                var j <- 0   
                for j until j >= 3 by 1
                begin
                    writeNumber(i)
                    writeNumber(j)
                end
            end
        end
        """
        expect = """0.0
0.0
0.0
1.0
0.0
2.0
1.0
0.0
1.0
1.0
1.0
2.0
2.0
0.0
2.0
1.0
2.0
2.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 538))


    def test_for_6(self):
        input = """func main ()
        begin
            var i <- 0
            for i until i > 15 by 1
            begin
                if (i <= 7)
                    continue
                else if (i > 12)
                    break
                    
                writeNumber(i)
                if (i % 3 = 0)
                    writeString(" - divisible by 3")
            end
        end
        """
        expect = """8.0
9.0
 - divisible by 3
10.0
11.0
12.0
 - divisible by 3
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 539))

    
    def test_return_1(self):
        input = """func main ()
        begin
            writeNumber(1)
            return
            writeNumber(2)
        end
        """
        expect = "1.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_return_2(self):
        input = """
        func main ()
        begin
            var i <- 0
            for i until i > 10 by 1
            begin
                writeNumber(i)
                if (i = 5)
                    return
            end
        end
        """
        expect = """0.0
1.0
2.0
3.0
4.0
5.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_return_3(self):
        input = """
        func foo ()
            return true
        func goo ()
            return 1
            

        func main ()
        begin
            var i <- goo()
            for i until not foo() by goo()
            begin
                writeNumber(i)
                if (i = 5)
                    return
                
            end
        end
        """
        expect = """1.0
2.0
3.0
4.0
5.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_return_4(self):
        input = """
        func fibo(number n)
        begin
            if (n <= 1)
                return n
            return fibo(n - 1) + fibo(n - 2)
        end

        func main ()
        begin
            var i <- 0
            for i until i >= 10 by 1
            begin
                writeNumber(fibo(i))
            end
        end     
        """
        expect = """0.0
1.0
1.0
2.0
3.0
5.0
8.0
13.0
21.0
34.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 543))