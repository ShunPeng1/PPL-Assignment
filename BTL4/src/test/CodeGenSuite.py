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
                var k <- fibo(i)
                writeNumber(k)
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
        #self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_return_5(self):
        input = """
        func foo (number i, bool a)
        begin
            return i
        end
        
        func main ()
        begin
            var i <- foo(69,true)
            writeNumber(i)
        end
        """
        expect = "69.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_return_6(self):
        input = """
        func foo (number i)
        begin
            if (i>=0)
                return 69
            else 
                return foo(i-1)
        end
        
        func main ()
        begin
            var i <- foo(10)
            writeNumber(i)
        end
        """
        expect = "69.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 545))

    
    def test_return_7(self):
        input = """
        func foo (number i)
        begin
            if (i>=0)
                return 69
            
            return foo(2)
        end
        
        func main ()
        begin
            var i <- foo(-2)
            writeNumber(i)
        end
        """
        expect = "69.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_return_8(self):
        input = """
        func foo (number i)
        begin
            if (i<0)
                return 69
            else
                return foo(i-1)
        end
        
        func main ()
        begin
            var i <- foo(10000)
            writeNumber(i)
        end
        """
        expect = "69.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_return_9(self):
        input = """
        func foo (number i)
        begin
            if (i<0)
                return "1"
            else
                return foo(i-2) ... foo(i-1)
        end
        
        func main ()
        begin
            var i <- foo(5)
            writeString(i)
        end
        """
        expect = "111111111111111111111\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_return_10(self):
        input = """
        func foo (number i)
        begin
            writeNumber(i)
        end
        
        func main ()
        begin
            var i <- 0
            for i until i >= 10 by 1
            begin
                foo(i)
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
        #self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_return_11(self):
        input = """
        func hanoi(number n, string source, string target, string auxiliary)

        func temp(number n, string source, string target, string auxiliary)
        begin
            hanoi(n, source, target, auxiliary)
        end

        func hanoi(number n, string source, string target, string auxiliary)
        begin
            if (n > 0) 
            begin
                temp(n - 1, source, auxiliary, target)
                var a <- "Move disk from " ... source
                var b <- " to " ... target
                writeString(a ... b)
                temp(n - 1, auxiliary, target, source)
            end
        end

        func main()
        begin
            hanoi(3, "A", "C", "B")
        end
        """
        expect = """Move disk from A to C
Move disk from A to B
Move disk from C to B
Move disk from A to C
Move disk from B to A
Move disk from B to C
Move disk from A to C
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_return_12(self):
        input = """
        func hanoi(number n, string source, string target, string auxiliary)
        begin
            if (n > 0) 
            begin
                hanoi(n - 1, source, auxiliary, target)
                var a <- "Move disk from " ... source
                var b <- " to " ... target
                writeString(a ... b)
                hanoi(n - 1, auxiliary, target, source)
            end
        end

        func main()
        begin
            hanoi(3, "A", "C", "B")
        end
        """
        expect = """Move disk from A to C
Move disk from A to B
Move disk from C to B
Move disk from A to C
Move disk from B to A
Move disk from B to C
Move disk from A to C
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 551))


    def test_array_1(self):
        input = """
        func main()
        begin
            number a[5] <- [1,2,3,4,5]
            var i <- 0
            for i until i > 5 by 1
                writeNumber(a[i])
        end
        """
        expect = """1.0
2.0
3.0
4.0
5.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_array_2(self):
        input = """
        func main()
        begin
            number a[5] <- [1,2,3,4,5]
            var i <- 0
            for i until i > 5 by 1
            begin
                a[i] <- i
                writeNumber(a[i])
            end
        end
        """
        expect = """0.0
1.0
2.0
3.0
4.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_array_3(self):
        input = """
        func main()
        begin
            number a[3,2] <- [[1,2],[3,4],[5,6]]
            var i <- 0
            for i until i >= 3 by 1
            begin
                var j <- 0
                for j until j >= 2 by 1
                begin
                    a[i,j] <- a[i,j] + 1
                    writeNumber(a[i,j])
                end
            end
        end
        """
        expect = """2.0
3.0
4.0
5.0
6.0
7.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_array_4(self):
        input = """
        func main()
        begin
            number a[3,2] <- [[1,2],[3,4],[5,6]]
            var k <- 0
            for k until k >= 3 by 1
            begin
                a[k] <- [ a[(k+1)%3,1] , a[(k+1)%3,0] ]
            end

            var i <- 0
            for i until i >= 3 by 1
            begin
                var j <- 0
                    
                for j until j >= 2 by 1
                begin
                    writeNumber(a[i,j])
                end
            end
        end
        """
        expect = """4.0
3.0
6.0
5.0
3.0
4.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_array_5(self):
        input = """
        func main()
        begin
            number a[3,2] <- [[1,2],[3,4],[5,6]]
            
            a[1] <- [7,8]
            writeNumber(a[1,0])
            writeNumber(a[1,1])
        end
        """
        expect = """7.0
8.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_array_6(self):
        input = """
        func main()
        begin
            number a[2,2,2] <- [[[1,2],[3,4]],[[7,8],[9, 10]]]
            var i <- 0
            for i until i >= 2 by 1
            begin
                var j <- 0
                for j until j >= 2 by 1
                begin
                    var k <- 0
                    for k until k >= 2 by 1
                    begin
                        a[i,j,k] <- a[i,j,k] * a[k,j,i] * a[j,i,k]
                        writeNumber(a[i,j,k])
                    end
                end
            end

        end
        """
        expect = """1.0
28.0
63.0
288.0
12348.0
18432.0
23328.0
1000.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_array_7(self):
        input = """
        func main()
        begin
            number a[2,2,2] <- [[[1,2],[3,4]],[[7,8],[9, 10]]]
            number b[2] <- [20,21]
            var i <- 0
            for i until i >= 2 by 1
            begin
                var j <- 0
                for j until j >= 2 by 1
                begin
                    a[i,j] <- b
                end
            end

            var k <- 0
            for k until k >= 2 by 1
            begin
                var l <- 0
                for l until l >= 2 by 1
                begin
                    var m <- 0
                    for m until m >= 2 by 1
                    begin
                        writeNumber(a[k,l,m])
                    end
                end
            end

            number c[2,2] <- [[31,32],[33,34]]
            var n <- 0
            for n until n >= 2 by 1
            begin
                a[n] <- c
            end

            var o <- 0
            for o until o >= 2 by 1
            begin
                var p <- 0
                for p until p >= 2 by 1
                begin
                    var q <- 0
                    for q until q >= 2 by 1
                    begin
                        writeNumber(a[o,p,q])
                    end
                end
            end
        end
        """
        expect = """20.0
21.0
20.0
21.0
20.0
21.0
20.0
21.0
31.0
32.0
33.0
34.0
31.0
32.0
33.0
34.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_array_8(self):
        input = """
        func foo(number a[2,2])
        begin
            var i <- 0
            for i until i >= 2 by 1
            begin
                var j <- 0
                for j until j >= 2 by 1
                begin
                    writeNumber(a[i,j])
                    
                    a[i,j] <- a[i,j] + 1
                end
            end
        end


        func main()
        begin
            number a[2,2] <- [[1,2],[3,4]]
            foo(a)
            foo(a)

            var i <- 0
            for i until i >= 2 by 1
            begin
                var j <- 0
                for j until j >= 2 by 1
                begin    
                    a[i,j] <- a[i,j] + 1
                end
            end

            foo(a)

        end
        """
        expect = """1.0
2.0
3.0
4.0
2.0
3.0
4.0
5.0
4.0
5.0
6.0
7.0
"""

        #self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_array_9(self):
        input = """
        func foo(number a[2,2])
        begin
            number b[2] <- [10,20]
            
            var i <- 0
            for i until i >= 2 by 1
            begin
                a[i] <- b
            end
        end


        func main()
        begin
            number a[2,2] <- [[1,2],[3,4]]
            foo(a)

            var i <- 0
            for i until i >= 2 by 1
            begin
                var j <- 0
                for j until j >= 2 by 1
                begin    
                    writeNumber(a[i,j])
                end
            end

        end
        """
        expect = """10.0
20.0
10.0
20.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_array_10(self):
        input = """
        func foo()
        begin
            number b[2] <- [10,20]
            return b
        end


        func main()
        begin
            number a[2,2] <- [[1,2],[3,4]]
            

            var i <- 0
            for i until i >= 2 by 1
            begin
                var j <- 0
                for j until j >= 2 by 1
                begin    
                    
                    a[i,j] <- foo()[j] + i + 1
                    writeNumber(a[i,j])
                end
            end

            var k <- 0
            for k until k >= 2 by 1
            begin
                var l <- 0
                for l until l >= 2 by 1
                begin    
                    a[k] <- foo() 
                    writeNumber(a[k,l])
                end
            end


        end
        """
        expect = """11.0
21.0
12.0
22.0
10.0
20.0
10.0
20.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_array_11(self):
        input = """
        number a[2,2] <- [[1,2],[3,4]]
        number b[2,2] <- [a[1],a[0]]


        func main()
        begin
    

            var i <- 0
            for i until i >= 2 by 1
            begin
                var j <- 0
                for j until j >= 2 by 1
                begin    
                
                    ##writeNumber(a[i,j])
                    ##writeNumber(b[i,j])
                    
                    a[i,j] <- b[i,j] + 1

                    writeNumber(a[i,j])
                end
            end



        end
        """
        expect = """4.0
5.0
5.0
6.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 562))


    def test_block_1(self):
        input = """
        func main()
        begin
            var i <- 0
            begin
                var i <- 1
                writeNumber(i)
            end
            writeNumber(i)
        end
        """
        expect = """1.0
0.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_block_2(self):
        input = """
        func main()
        begin
            var i <- 0
            begin
                i <- 1
                writeNumber(i)
            end
            writeNumber(i)
        end
        """
        expect = """1.0
1.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_block_3(self):
        input = """
        var i <- -1

        func main()
        begin
            writeNumber(i)
            var i <- 0
            begin
                var i <- 1
                begin
                    var i <- 2
                    writeNumber(i)
                end
                writeNumber(i)
            end
            writeNumber(i)
        end
        """
        expect = """-1.0
2.0
1.0
0.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_block_4(self):
        input = """
        var i <- "Hello"

        func main()
        begin
            writeString(i)
            var i <- 0
            begin
                var i <- true
                begin
                    number i[1] <- [2]
                    writeNumber(i[0])
                end
                writeBool(i)
            end
            writeNumber(i)
        end
        """
        expect = """Hello
2.0
true
0.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_block_5(self):
        input = """
        var i <- 5

        func main()
        begin
            writeNumber(i)
            
            for i until i >= 10 by 1
            begin
                writeNumber(i)
                var i <- i - 1
                writeNumber(i)
            end
            writeNumber(i)
        end
        """
        expect = """5.0
5.0
4.0
6.0
5.0
7.0
6.0
8.0
7.0
9.0
8.0
10.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_block_6(self):
        input = """
        var i <- 5

        func main()
        begin
            writeNumber(i)
            
            if (true)
                i <- 10
            
            writeNumber(i)
        end
        """
        expect = """5.0
10.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_block_7(self):
        input = """
        var i <- 5

        func main()
        begin
            writeNumber(i)
            
            if (true)
            begin
                var i <- 10
                writeNumber(i)
            end
            
            writeNumber(i)
        end
        """
        expect = """5.0
10.0
5.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 569))

    
    def test_block_8(self):
        input = """

        func foo(number i)
        begin
            writeNumber(i)
            if (i <= 0)
            begin
                number i <- 5
                return 69
            end
            else return foo(i-1)
            
        end
        
        func main()
        begin
            var i <- foo(5)
            writeNumber(i)
        end
        """
        expect = """5.0
4.0
3.0
2.0
1.0
0.0
69.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_block_9(self):
        input = """

        func foo(number i)
        begin
            writeNumber(i)
            if (i <= 0)
            begin
                var foo <- 69
                writeNumber(foo)
                return foo
            end
            else 
            begin
                return foo(i-1)
            end
        end
        
        func main()
        begin
            var i <- foo(5)
            writeNumber(i)
        end
        """
        expect = """5.0
4.0
3.0
2.0
1.0
0.0
69.0
69.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_block_10(self):
        input = """

        func foo(number foo)
        begin
            var foo <- foo + foo
            return foo
        end
        
        func main()
        begin
            var i <- foo(5)
            writeNumber(i)
        end
        """
        expect = """10.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_infer_1(self):
        input = """
        func main()
        begin
            dynamic a <- 1
            dynamic b <- 2
            dynamic c <- a + b
            writeNumber(c)
        end
        """
        expect = "3.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_infer_2(self):
        input = """
        func main()
        begin
            dynamic a 
            a <- 1

            writeNumber(a)
        end
        """
        expect = "1.0\n"
        #self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_infer_3(self):
        input = """
        dynamic a <- "Hello"

        func main()
        begin
            writeString(a)
            dynamic a 
            a <- 1

            dynamic b <- a
            writeNumber(b)

        end
        """
        expect = """Hello
1.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 575))
        
    def test_infer_4(self):
        input = """
        
        dynamic a
        dynamic b
        dynamic c
        
        func foo()
        func goo()
        func hoo()

        func main()
        begin
        
            writeNumber(a)
            writeBool(b)
            writeString(c)
            
            dynamic a
            dynamic b
            dynamic c
            
            writeNumber(a)
            writeBool(b)
            writeString(c)
            
            writeNumber(foo())
            writeBool(goo())
            writeString(hoo())


        end

        func foo()
            return 1
        func goo()
            return true
        func hoo()
            return "Hello"
        """
        expect = """0.0
false

0.0
false

1.0
true
Hello
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 576))


    def test_infer_5(self):
        input = """
        dynamic a <- 1
        dynamic b 
        func main()
        begin

            number c <- 1
            begin 
                number d <- 2
            end
            string e <- "e"
            string f <- "f"

            writeString(e ... f)

            for c until c >= 10 by 1
            begin
            
            end
            writeNumber(c)
            writeNumber(a)
            writeNumber(b)
        end
        """
        expect = """10.0
1.0
0.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_infer_6(self):
        input = """
        func main()
        begin
            number a[2]
            number b <- a[0]
        end
        """
        expect = """"""
        #!self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_loop_1(self):
        input = """
        func main()
        begin
            number i <- 0
            number a <- 1

            for i until i > 10 by a
            begin
                a <- a * 2
                writeNumber(a)
            end
                

            writeNumber(i)

        end
        """
        expect = """2.0
4.0
8.0
16.0
32.0
64.0
128.0
256.0
512.0
1024.0
2048.0
0.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    