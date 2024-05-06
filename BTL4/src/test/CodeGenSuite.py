import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test0(self):
        # output function
        input = """func main ()
        begin
            writeNumber(1)
            writeString("aoisd")
            writeBool(true)
        end
        """
        expect = """1.0
aoisd
true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 500))
    
    def test1(self):
        # number operators
        input = """func main()
        begin
            writeNumber(12.34e1 + 4.289)
            writeNumber(4.3-5.8)
            writeNumber(2*1.6)
            writeNumber(4.5/3)
            writeNumber(7.5%3.5)
            writeNumber(-23)
            writeBool(2.3 < 2.0)
            writeBool(1.23 <= 1.04)
            writeBool(32.12 > 17.48e1)
            writeBool(12.38 >= 12.38)
            writeBool(2 = 2)
            writeBool(47.38 != 98.3)
        end
        """
        expect = """127.689
-1.5
3.2
1.5
0.5
-23.0
false
false
false
true
true
true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 501))
    
    def test2(self):
        # string operators
        input = """func main() begin
            writeString("abc")
            writeString("abc" ... "def")
            writeBool("sodi" == "oixc")
            writeBool("abc" == "abc")
        end
        """
        expect = """abc
abcdef
false
true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 502))
    
    def test3(self):
        # boolean operators
        input = """func main()
        begin
            writeBool(true and false)
            writeBool(true or false)
            writeBool(not true)
            writeBool((1.3*2.3 > 6.0 + 2.3) and ("abi" == "owie"))
        end
        """
        expect = """false
true
false
false
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 503))
    
    def test4(self):
        # variable declaration
        input = """
func main()
begin
    number x <- 4.9 + 7.5 % 3.5
    string s <- ("oasif" ... "iweo") ... "abcd"
    bool b <- 1.0 < 3.0
    writeNumber(x + 2)
    writeString(s)
    writeBool(b)
end
"""
        expect = """7.4
oasifiweoabcd
true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 504))
    
    def test5(self):
        # implicit variable
        input = """func main()
        begin
            var x1 <- 8.27
            var x2 <- 3.12 <= 4.5 - 1.34
            var x3 <- "oe[]; " ... "829 odo"
            dynamic x4 <- 12.3 != 38
            dynamic x5
            x5 <- true
            writeNumber(x1)
            writeBool(x2)
            writeString(x3)
            writeBool(x5)
            writeBool(x4)
        end
        """
        expect = """8.27
true
oe[]; 829 odo
true
true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 505))
    
    def test6(self):
        # global variable 1
        input = """number x
        string y
        bool z
        func main()
        begin
            x <- 12.3
            y <- "\\tHe says: \'\"no\'\".\\n"
            z <- 3.34 + 19.7 = 75.4 % 4.3
            writeNumber(x)
            writeString(y)
            writeBool(z)
        end
        """
        expect = """12.3
\tHe says: \'\"no\'\".\n
false
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 506))
    
    def test7(self):
        # global variable 2
        input = """
number t <- 4.5 - 2
var x <- "murasaki"
dynamic m <- 7.5 % 3
dynamic n
func main() begin
    writeNumber(t)
    writeString(x)
    writeNumber(m)
    n <- 1.334e2 < 100 + 31.89
    writeBool(n)
end
"""
        expect = """2.5
murasaki
1.5
false
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 507))
    
    def test8(self):
        # array 1
        input = """func main()
        begin
            number arr[3] <- [1,2,3]
            writeNumber(arr[0])
            arr[2] <- 4.2
            writeNumber(arr[2])
            var x_ <- arr[0] <= arr[1]
            writeBool(x_)
            string sarr[3] <- ["324", "324", "paos"]
            writeBool(sarr[0] == sarr[1])
            writeString(sarr[1] ... sarr[2])
            bool vis[2] <- [13 < 4.3, 9.51e2 > 100e-1]
            writeBool(vis[0] or vis[1])
            number mium[5]
            mium[0] <- 3.29 * 5
            mium[1] <- 7.5 % 3.5
            mium[2] <- (1.233e2 + 102e-1) * 0.7
            mium[3] <- (7.5 / 3 * 2 + 4.32) % 0.5
            mium[4] <- 1 + 2 + 3 + 4
            writeBool(mium[0] + mium[2] = mium[1])
        end
        """
        expect = """1.0
4.2
true
true
324paos
true
false
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 508))
    
    def test9(self):
        # array test 2
        input = """func main() begin
            var arr <- [1+4.3, 8.2*3%4, 47e-1]
            writeNumber(arr[1])
            arr[0] <- 57.5 / 5
            writeNumber(-arr[2]+arr[0])
            dynamic arr2 <- ["toi ", "di ", "hoc.\\n"]
            writeString((arr2[0] ... arr2[1]) ... arr2[2])
        end
        """
        expect = """0.5999985
6.8
toi di hoc.

"""
        #self.assertTrue(TestCodeGen.test(input, expect, 509))
    
    def test10(self):
        # array test 3
        input = """func main()
        begin
            number arr1[2,2] <- [[1e1,2],[4,5]]
            writeNumber(arr1[0,1])
            string arr2_[2,2]
            arr2_[0] <- ["abc", "def"]
            arr2_[1] <- ["123", "456"]
            writeString(arr2_[0,0] ... arr2_[1,0])
            string arr2[1,2,2]
            arr2[0,0,0] <- "abc"
            arr2[0,0,1] <- "def"
            arr2[0,1] <- ["123","456"]
            writeString(arr2[0,1,0] ... arr2[0,1,1])
            var x <- arr1[1]
            writeNumber(x[0])
        end
        """
        expect = """2.0
abc123
123456
4.0
"""
        self.assertTrue(TestCodeGen.test(input, expect, 510))
    
    def test11(self):
        # user-defined function 1
        input = """func foo1() return 1 + 0
        func foo2(number a) return 2.5 * a
        func foo3(string s1, string s2, number a)
        begin
            writeString(s1)
            writeString(s2 ... s1)
            writeBool((s1 == s2) and (a > 0))
        end
        func foo4(number a, bool b) return (a > 0) and b
        func main() begin
            writeNumber(foo1() + 2.5)
            writeNumber(foo2(2))
            var s1 <- "toi "
            var s2 <- "di hoc."
            var a <- -3.4 * -5.7 - 20
            foo3(s1, s2, a)
            writeBool(foo4(3, false))
        end
        """
        expect = """3.5
5.0
toi 
di hoc.toi 
false
false
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 511))
    
    def test12(self):
        # array test 4
        input = """dynamic b <- [3]
        func main()
        begin
            dynamic x <- [1,2,3]
            writeNumber(b[0])
            number xy[2,2,2] <- [[[1,2],[3,4]],[[5,6],[7,8]]]
            writeNumber(xy[0,0,0])
            xy[1,0] <- [4.5, 7.5-3]
        end
        """
        expect = """3.0
1.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 512))
    
    def test13(self):
        # user-defined function 2
        input = """func foo1()
        func foo2(number x, bool b)
        func main() begin
            writeNumber(foo1())
            var m <- 3.27 + 1.48 > 6
            writeBool(foo2(foo1(), m))
        end
        func foo1() return 23.48
        func foo2(number x, bool b)
        begin
            x <- x * x % 5
            return not b and (x > 10)
        end
        """
        expect = """23.48
false
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 513))
    
    def test14(self):
        # user-defined function 3
        input = """func foo(number a[5], string b) begin
            ##a[1] <- a[0] + 1
            writeString(b)
            return a[0] * 3.5
        end

        func main() begin
            var arr <- [2,3,4,5,6]
            var i <- foo(arr,"Hello!")
            writeNumber(i)
            writeNumber(arr[1])
        end
        """
        expect = """Hello!
7.0
3.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 514))
    
    def test15(self):
        # if statement 1
        input = """func main() begin
            var i <- 15
            if (i < 20) writeString("I\\'m here!")
            string a <- "abc"
            if (a == " abc") i <- i * 0.5
            else i <- i % 3
            writeNumber(i)
            number t <- 15
            if (t < 10) writeString("A")
            elif (t < 20) writeString("B")
            else writeString("C")
        end
        """
        expect = """I\'m here!
0.0
B
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 515))
    
    def test16(self):
        # if statement 2
        input = """func main()
        begin
            var i <- 14.73
            if (i < 15) begin
                var j <- 5.12
                i <- i + j
                writeNumber(i / 5 + -6.2)
            end
            elif (i < 30) begin
                writeBool(i + 15.3 >= 50)
            end
            elif (i < 35) begin
                var j <- "uio"
                writeString(j)
            end
            writeString("End program!\\n")
        end
        """
        expect = """-2.23
End program!

"""
        #self.assertTrue(TestCodeGen.test(input, expect, 516))
    
    def test17(self):
        input = """func foo(number x1, number x2, number x3)
        func main() begin
            var t <- foo(13, -5, -8)
            writeNumber(t / 2 / 2 + 1)
        end
        func foo(number x1, number x2, number x3)
        begin
            if ((x1 <= 0) and (x2 <= 0) and (x3 <= 0)) return x1 * x2 - x3
            elif ((x1 > 0) and (x2 > 0) and (x3 <= 0)) return x2 + x3 * x3
            elif ((x1 > 0) and (x2 <= 0) and (x3 <= 0)) return x2
            else begin
                number tmp <- x1 + x2
                return tmp % 2
            end
        end
        """
        expect = """-0.25
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 517))
    
    def test18(self):
        # for statement 1
        input = """func main()
        begin
            var i <- 0
            for i until i >= 5 by 1 writeNumber(i)
            writeNumber(i)
        end
        """
        expect = """0.0
1.0
2.0
3.0
4.0
0.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 518))
    
    def test19(self):
        # for statement 2
        input = """func main() begin
            var i <- 0
            for i until i >= 20 by 4
            begin
                writeBool(i >= 10)
            end
        end
        """
        expect = """false
false
false
true
true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 519))
    
    def test20(self):
        input = """func foo(bool arr[2])
        begin
            arr[0] <- 1.38 < 2
        end
        func main()
        begin
            var arr <- [false, false]
            foo(arr)
            writeBool(arr[0])
            writeBool(arr[1])
        end
        """
        expect = """true
false
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 520))
    
    def test21(self):
        input = """func foo(number arr[3], number x)
        begin
            arr[0] <- 3.5
            return x + 1
        end
        func main() begin
            number arr[3] <- [2.34, 89.5e-1, 5.06]
            var i <- foo(arr, arr[2])
            writeNumber(arr[0])
            writeNumber(i)
        end
        """
        expect = """3.5
6.06
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 521))
    
    def test22(self):
        input = """func foo(string sarr[5])
        func main() begin
            string sarr[5] <- ["abc","def","123","45","ewo"]
            var s <- foo(sarr)
            writeString(s)
        end
        func foo(string sarr[5]) begin
            dynamic i
            string s <- ""
            i <- 0
            for i until i >= 5 by 1 s <- s ... sarr[i]
            return s
        end
        """
        expect = """abcdef12345ewo
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 522))
    
    def test23(self):
        input = """func foo(number arr[5])
        begin
            arr[2] <- arr[3] * arr[1] - 5
        end
        func main() begin
            var arr <- [1,2,3,4,5]
            arr[0] <- arr[0] + 1
            foo(arr)
            writeNumber(arr[0])
            writeNumber(arr[2])
        end
        """
        expect = """2.0
3.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 523))
    
    def test24(self):
        input = """var x <- "String"
        func dmow(number a) begin
            writeString(x)
            x <- "3928"
            return a
        end
        func main() begin
            number t <- dmow(5)
            writeNumber(t + 3.4)
            writeString(x)
        end
        """
        expect = """String
8.4
3928
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 524))
    
    def test25(self):
        # global variable 3
        input = """number arr[3] <- [1.38, 4.85, 3.03]
        func main() begin
            arr[0] <- arr[0] * 2 + arr[2]
            writeBool(arr[0] >= arr[1]) 
        end
        """
        expect = """true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 525))
    
    def test26(self):
        input = """func foo() return [12.38, 49.53]
        func swap(number arr[2])
        begin
            var t <- arr[0]
            arr[0] <- arr[1]
            arr[1] <- t
        end
        func main() begin
            dynamic a
            a <- foo()
            swap(a)
            writeNumber(a[0])
            writeNumber(a[1])
        end
        """
        expect = """49.53
12.38
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 526))
    
    def test27(self):
        input = """number a <- 2.38
        func foo(number x) begin
            a <- x
        end
        func main() begin
            writeNumber(a)
            foo(5)
            writeNumber(a)
        end
        """
        expect = """2.38
5.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 527))
    
    def test28(self):
        input = """var arr <- [4.36, 5.07]
        func foo(number arr[2])
        func main() begin
            foo(arr)
            writeNumber(arr[0])
            writeNumber(arr[1])
        end
        func foo(number arr[2]) begin
            dynamic t <- arr[0]
            arr[0] <- arr[1]
            arr[1] <- t
        end
        """
        expect = """5.07
4.36
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 528))
    
    def test29(self):
        input = """dynamic vip
        number a[2,2]
        func main() begin
            vip <- 1
            a[0,0] <- vip
            a[0,1] <- vip+1
            a[1,0] <- vip+2
            a[1,1] <- vip+3
            writeBool(a[0,0]+a[1,1]=a[0,1]+a[1,0])
        end
        """
        expect = """true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 529))
    
    def test30(self):
        input = """string arr1[3,2]
        func main()
        begin
            var i <- 0
            number arr[1]
            arr[i] <- 4
            number arr2[2,2]
            arr2[0] <- [1,2]
            arr2[1] <- [1,2]
            arr1[0] <- ["3","\'\"3\'\""]
            arr1[1] <- ["3","\'\"3\'\""]
            arr1[2] <- ["3","\'\"3\'\""]
            writeBool((arr[0] = arr2[0,0]) or (arr1[1,0] == arr1[2,0]))
        end
        """
        expect = """true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 530))
    
    def test31(self):
        input = """func isPrime(number x)
        func main()
        begin
            number x <- 34
            if (isPrime(x)) writeString("Yes")
            else writeString("No")
        end
        func isPrime(number x) begin
            if (x <= 1) return false
            var i <- 2
            for i until i > x / 2 by 1
            begin
                if (x % i = 0) return false
            end
            return true
        end
        """
        expect = """No
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 531))
    
    def test32(self):
        input = """func areDivisors(number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
        func main() begin
            var num1 <- 49
            var num2 <- 7
            writeBool(areDivisors(num1, num2))
        end
        """
        expect = """true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 532))
    
    def test33(self):
        # scope
        input = """var t <- "38" ... "48"
        func main() begin
            writeString(t)
            var t <- ("123"..."456")..."7"
            begin
                writeString(t)
                var t <- "abcdef"
                begin
                    writeString(t)
                end
            end
            writeString(t)
        end
        """
        expect = """3848
1234567
abcdef
1234567
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 533))
    
    def test34(self):
        # break statement
        input = """func main() begin
            var i <- 0
            string arr[3] <- ["123","456","789"]
            for i until i >= 10 by 1 begin
                if (i = 3) break
                writeString(arr[i])
            end
        end
        """
        expect = """123
456
789
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 534))
    
    def test35(self):
        # continue statement
        input = """func main() begin
            var i <- 0
            for i until i >= 10 by 1 begin
                if ((i >= 4) and (i <= 7)) continue
                writeNumber(i+1)
            end
        end
        """
        expect = """1.0
2.0
3.0
4.0
9.0
10.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 535))
    
    def test36(self):
        input = """func main() return
        """
        expect = """"""
        #self.assertTrue(TestCodeGen.test(input, expect, 536))
    
    def test37(self):
        input = """func foo(number a[5], string b)
        begin
            var i <- 0
            for i until i >= 5 by 1 a[i] <- i * i + 5
            return -1
        end
        number arr[5]
        func main()
        begin
            string b <- "mommy"
            var t <- foo(arr, b)
            writeBool(t < 0)
            var i <- 0
            for i until i >= 5 by 1 writeNumber(arr[i])
        end
        """
        expect = """true
5.0
6.0
9.0
14.0
21.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 537))
    
    def test38(self):
        # complex indexing
        input = """func foo(number x) return x + 1
        func main() begin
            number a[5] <- [1,2,3,4,5]
            number b[2,3] <- [[0,1,2],[2,3,4]]
            a[4 - foo(2)] <- a[b[1,2]] / 2.5 + 1.5
            var i <- 0
            for i until i >= 5 by 1 writeNumber(a[i])
        end
        """
        expect = """1.0
3.5
3.0
4.0
5.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 538))
    
    def test39(self):
        input = """func main() begin
            bool t <- 1.38 + -4*0.25*-2.5 >= 5.38 - 3.46
            dynamic x
            if (t) begin
                x <- [[2,4],[6,8],[1,3],[5,7]]
                var i <- 3
                for i until i < 0 by -1
                begin
                    writeNumber(x[i,1] % x[i,0])
                end
            end
            else begin
            end
        end
        """
        expect = """2.0
0.0
2.0
0.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 539))
    
    def test40(self):
        input = """func _fari123(number x[5,1], string b)
        begin
            writeString(b)
            number arr[5]
            var i <- 0
            for i until i >= 5 by 1 arr[i] <- x[i,0]
            return arr
        end
        func main() begin
            dynamic h <- [[1],[2],[3],[4],[5]]
            var uma <- _fari123(h, "Hello World!\\t")
            var i <- 0
            for i until i > 4 by 1 writeNumber(uma[i])
        end
        """
        expect = """Hello World!\t
1.0
2.0
3.0
4.0
5.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 540))
    
    def test41(self):
        input = """number arr[5] <- [12,4,7,20,1]
        func sort(number arr[5])
        func main() begin
            sort(arr)
            var i <- 0
            for i until i >= 5 by 1 writeNumber(arr[i])
        end
        func sort(number arr[5]) begin
            var i <- 1
            for i until i >= 5 by 1
            begin
                var key <- arr[i]
                var j <- i - 1
                for j until not (j >= 0) by -1 begin
                    if (key > arr[j]) break
                    arr[j+1] <- arr[j]
                end
                arr[j+1] <- key
            end
        end
        """
        expect = """12.0
12.0
4.0
7.0
1.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 541))
    
    def test42(self):
        input = """func foo2(number x, number y)
        func foo1(number arr[2])
        dynamic t
        func main() begin
            t <- [12.38, 4.59e1]
            writeNumber(foo1(t))
        end
        func foo2(number x, number y) begin
            if (x < y) return x * --y
            elif (x = y) return x + y*2
            else return x - y
        end
        func foo1(number arr[2]) begin
            return foo2(arr[0], arr[1])
        end
        """
        expect = """568.242
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test43(self):
        input = """func main() begin
            var p <- [[1,3],[4,5],[5,6]]
            dynamic t <- 0
            for t until t >= 2 by 1 writeNumber(p[t,0]+p[t,1]*2)
        end
        """
        expect = """7.0
14.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 543))
    
    def test44(self):
        input = """string s <- ("dsi" ... "oe[]") ... ("od" ... "389")
        func main() begin
            writeBool(s == "1234589")
        end
        """
        expect = """false
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 544))
    
    def test45(self):
        input = """func main() begin
            bool arr[8] <- [true,true,false,true,false,false,true,true]
            var i <- 0
            dynamic b <- 12
            if (b < 14.5)
            begin
                for i until i >= 8 by 1
                begin
                    if (arr[i]) begin
                        b <- b + 1
                        var t <- b % 4
                        writeNumber(t)
                    end
                    else writeString("failed")
                end
            end
        end
        """
        expect = """1.0
2.0
failed
3.0
failed
failed
0.0
1.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 545))
    
    def test46(self):
        input = """func main()
        begin
            var arr <- [[ [ [1,2],[3,4] ] , [ [5,6],[7,8] ] ]]
            var t <- arr[0,1]
            writeNumber(t[1,0] + arr[0,0,0,1])
        end
        """
        expect = """9.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 546))
    
    def test47(self):
        input = """number t
        func main() begin
            t <- 3.48
            writeNumber(t-3.47*0.75)
            number arr[2,1,2]
            arr[0,0] <- [1,2]
            arr[1,0] <- [3,4]
            writeBool(arr[0,0,1] < arr[1,0,1])
        end
        ##func """
        expect = """0.87750006
true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 547))
    
    def test48(self):
        input = """func foo1(number arr[2])
func foo2(number a, number b)
dynamic xt
func main() begin
    xt <- [45, 18]
    writeNumber(foo1(xt))
end
func foo2(number a, number b) begin
    if (a < b) return a - -b
    elif (a = b) return a * b
    else return a % b
end
func foo1(number arr[2]) return foo2(arr[0],arr[1])
"""
        expect = """9.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 548))
    
    def test49(self):
        input = """func fio(number n)
        func main() begin
            number a <- 5
            writeString(fio(a) ... "\\n")
        end
        string t <- "abc"
        func fio(number n) begin
            string res <- ""
            var i <- 0
            for i until i >= n by 1 res <- res ... t
            return res
        end
        """
        expect = """abcabcabcabcabc

"""
        #self.assertTrue(TestCodeGen.test(input, expect, 549))
    
    def test50(self):
        input = """func main() begin
            number arr[3,4]
            dynamic u <- 1
            var j <- 0
            for j until j >= 4 by 1 begin
                var i <- 0
                for i until i >= 3 by 1 begin
                    arr[i,j] <- u
                    u <- u * 2
                end
            end
            writeNumber(arr[2,2])
        end
        """
        expect = """256.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 550))
    
    def test51(self):
        input = """func main() begin
            number i <- 47
            if (i > 15)
                if (i > 30) writeNumber(i * 1.52)
                elif (i > 26) writeString("OK")
                elif (i > 20) writeBool(i < 50)
                else writeBool(not (i=15))
            elif (i > 7) writeNumber(i - 40)
            else writeString("Done!")
        end
        """
        expect = """71.44
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 551))
    
    def test52(self):
        input = """## start
func foo1(string arr[3,3], string b) begin
    bool res <- true
    var i <- 0
    for i until i >= 3 by 1 begin
        var j <- 0
        for j until j >= 3 by 1
            res <- not (res and (arr[i,j] == b))
    end
    return res
end
func main() begin
    dynamic sar <- [["abc","def","ghi"],["jkl","mno","pqr"],["tuv","wxy","z00"]]
    var s <- "def"
    bool mi <- foo1(sar, s)
    writeBool(mi)
end
## end
"""
        expect = """true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 552))
    
    def test53(self):
        input = """func main() begin
            if (true)
            if (true)
            if (true)
            if (true)
            if (12 > 110)
            writeNumber(1)
            else writeNumber(0)
            else writeNumber(-1)
        end
        """
        expect = """0.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 553))
    
    def test54(self):
        input = """dynamic t <- true and (not false)
        number i <- 14.3793e5
        number y <- 0.00000001
        var s <- "a1b0c2d3e9f"
        func main() begin
            writeNumber(i / 100 + y * 100000)
            writeString(s)
            writeBool(not (t or t))
        end
        """
        expect = """14379.3
a1b0c2d3e9f
false
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 554))
    
    def test55(self):
        ## indexing function that returns array
        input = """func foo1(number a) return [a,a+1,a+2,a+3]
        func foo2() return ["ab","bc","cd"]
        func foo3() return [true, true, false]
        func main() begin
            number x <- 2*2.5%3+-1.5
            writeNumber(foo1(x)[2])
            writeString(foo2()[0])
            writeBool(foo3()[1])
        end
        """
        expect = """2.5
ab
true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 555))
    
    def test56(self):
        input = """func foo1(number x)
        func foo2(string s) begin
            writeString(s)
            writeBool(foo1(10))
        end
        func foo1(number x) return x * x > 256
        func main() begin
            foo2("Hello!\\t\\t")
        end
        """
        expect = """Hello!\t\t
false
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 556))
    
    def test57(self):
        input = """
func num1(number x[4,2], number y[2,2]) begin
    writeNumber(x[3,0] * y[0,1])
    x[0,1] <- x[0,1] + y[0,0] + -y[1,0]
end
dynamic u
number a <- 3.28 - 1.78
string s[2,2]
func foo2(string s, bool b) return (s=="asod") or not b and (a >= 0)
func main () begin
    u <- [[1,2],[3,4],[5,6],[7,8]]
    number v[2,2]
    v[0] <- [7.4, 2.91]
    v[1] <- [100e-2, 57e-1]
    writeBool(foo2("asod", 1.3 > 2))
    num1(u,v)
    writeNumber(u[0,1] % 1.5 % 2)
end
"""
        expect = """true
20.37
0.8999996
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 557))
    
    def test58(self):
        input = """func foo(number arr[10], number x) begin
            var i <- 0
            for i until i >= 10 by 1 begin
                if (arr[i] = x) return true
            end
            return false
        end
        func main() begin
            writeBool(foo([1,2,3,4,5,6,7,8,9,10], 7))
            writeBool(foo([1,2,3,4,5,6,7,8,9,10], 11))
        end
        """
        expect = """true
false
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 558))
    
    def test59(self):
        input = """func main() begin
            var i <- 1
            for i until i >= 10 by 1 begin
                var j <- 1
                for j until j >= 8 by 1 begin
                    var k <- 1
                    for k until k >= 6 by 1 begin
                        if (k >= 3) break
                        writeNumber(i*j*k)
                    end
                    if ((j >= 3) and (j < 6)) continue
                    writeNumber(j*i)
                end
                if (i = 2) break
                writeNumber(i)
            end
        end
        """
        expect = """1.0
2.0
1.0
2.0
4.0
2.0
3.0
6.0
4.0
8.0
5.0
10.0
6.0
12.0
6.0
7.0
14.0
7.0
1.0
2.0
4.0
2.0
4.0
8.0
4.0
6.0
12.0
8.0
16.0
10.0
20.0
12.0
24.0
12.0
14.0
28.0
14.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 559))
    
    def test60(self):
        input = """func foo(number n) return n + 0.5
        func main() begin
            number arr[5] <- [foo(1),foo(2),foo(3),foo(0),foo(0.5)]
            var i <- 0
            for i until i>=5 by 1 begin
                if ((i = 3) or (i = 0)) begin
                    writeString("skip")
                    continue
                end
                writeNumber(arr[i])
            end
            ## end of program
        end
        """
        expect = """skip
2.5
3.5
skip
1.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 560))
    
    def test61(self):
        input = """func foo(number n) return n + 0.5
        func _main() begin
            return [foo(4), foo(2*2.5), foo(1.0)]
        end
        func main() begin
            number arr[3] <- _main()
            writeNumber(arr[foo(0.5)])
        end
        """
        expect = """5.5
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 561))
    
    def test62(self):
        input = """func foo1(number x) return x * 2
        func foo2(number a, number b) return foo1(a+1) - foo1(b-2)
        number arr[2]
        func foo3(number arr[2]) return foo2(arr[1],arr[0])
        func main() begin
            arr[0] <- 14.37
            arr[1] <- arr[0] * 2.5 - 15
            writeNumber(foo3(arr))
        end
        """
        expect = """19.109999
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 562))
    
    def test63(self):
        input = """func foo() begin
            return 1
            return 0
        end
        func main() begin
            writeNumber(foo())
        end
        """
        expect = """1.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 563))
    
    def test64(self):
        input = """func main() begin
            var i <- 0
            for i until i >= 1 by 2 begin
                string s <- "\\tKhorman\\b"
                var j <- 0
                for j until j > 9 by 3 begin
                    if (i * j < 13) writeNumber(0)
                    elif (i * j < 30) writeNumber(1)
                    elif (i * j < 57) writeNumber (2)
                    else if (j >= 8) writeNumber(3)
                end
                writeString(s)
            end
        end
        """
        expect = """0.0
0.0
0.0
0.0
\tKhorman\b
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 564))
    
    def test65(self):
        input = """func oip(string arr[3])
        begin
            arr[0] <- "[][][]"
            arr[1] <- "help!\\n"
            arr[2] <- "\\tTeleport\\t"
            return -1
        end
        func main() begin
            string sarr[3]
            writeNumber(oip(sarr))
            writeString(sarr[0])
        end
        """
        expect = """-1.0
[][][]
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 565))
    
    def test66(self):
        input = """func foo1(number arr[3]) begin
            writeBool((arr[0]=arr[1]) and not (arr[1]+arr[2]>10))
            writeNumber(arr[0]+1.5)
            return arr[2] * 2
        end
        func foo2() begin
            number arr[3] <- [3,4,5]
            var t <- foo1(arr)
            return t + 3
        end
        func main() begin
            foo2()
        end
        """
        expect = """false
4.5
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 566))
    
    def test67(self):
        input = """func foo1(number a, number b)
        number m
        func foo2(number x) begin
            dynamic t
            t <- foo1(m, x)
        end
        func main() begin
            m <- 4
            foo2(7)
        end
        func foo1(number a, number b) begin
            writeNumber((a+-b)/4)
            writeString(("a"..."b")..."c")
            return a * b
        end
        """
        expect = """-0.75
abc
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 567))
    
    def test68(self):
        input = """func getMax(number arr[5])
        dynamic arr
        func main() begin
            arr <- [[42,28,50,16,37],[38,57,19,91,0],[10,85,29,51,68]]
            var i <- 0
            for i until i >= 3 by 1 writeNumber(getMax(arr[i]))
        end
        func getMax(number arr[5]) begin
            var i <- 1
            number max <- arr[0]
            for i until i > 5-1 by 1
                if (arr[i] > max) max <- arr[i]
            return max
        end
        """
        expect = """50.0
91.0
85.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 568))
    
    def test69(self):
        input = """var char_lst <- ["a","b","c","d","e","f"]
        func main() begin
            string s <- ""
            if (true) begin
                var i <- 0
                number j <- 6 - 1
                for i until i >= 10 by 3 begin
                    s <- s ... char_lst[j]
                    j <- j - 1
                end
            end
            writeString(s)
        end
        """
        expect = """fedc
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 569))
    
    def test70(self):
        input = """number arr[3,5] <- [[9,2,1,5,3],[2,9,1,5,6],[0,9,10,2,7]]
func sort(number arr[5])
func main() begin
    var i <- 0
    for i until i >= 3 by 1 sort(arr[i])
    var j <- 0
    for j until j >= 5 by 1 writeNumber(arr[1,j])
end
func sort(number arr[5]) begin
    var i <- 1
    for i until i >= 5 by 1
    begin
        var key <- arr[i]
        var j <- i - 1
        for j until not (j >= 0) by -1 begin
            if (key < arr[j]) break
            arr[j+1] <- arr[j]
        end
        arr[j+1] <- key
    end
end
"""
        expect = """2.0
9.0
1.0
1.0
6.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 570))
    
    def test71(self):
        input = """func main() begin
    dynamic a
    dynamic b
    b <- ["mno","xyz","ijk"]
    dynamic c <- ["123","456","789"]
    a <- ["abc","def","ghi"]
    string arr[3,3] <- [a,b,c]
    writeString(arr[0,1]...arr[2,0])
end
"""
        expect = """def123
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 571))
    
    def test72(self):
        input = """func tuva()
func fopoe(bool b) return tuva() and b
func main() begin
    bool s <- tuva()
    bool zd <- fopoe(true)
    writeBool(zd)
end
func tuva() begin
    writeString("\\\\\\\\")
    writeNumber(1.45 * 2 / 2)
    return true
end
"""
        expect = """\\\\
1.45
\\\\
1.45
true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 572))
    
    def test73(self):
        input = """number arr[3,4]
func eipo(number z) begin
    var i <- 0
    for i until i >= 3 by 1 begin
        number j <- 0
        for j until j >= 4 by 1 begin
            arr[i,j] <- z
            z <- z * 3
        end
    end
end
number to_ <- 1
func main() begin
    eipo(to_)
    var i <- 0
    for i until i >= 4 by 1 writeNumber(arr[1,i])
end
"""
        expect = """81.0
243.0
729.0
2187.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 573))
    
    def test74(self):
        input = """func amar() begin
    var noum <- [[["viop","donn8"],["tuio","k io"]], [["_mi_","eops"],["vi23","xi  "]]]
    noum[0,1] <- ["123","58d"]
    noum[1] <- [["d8","90sd"],["asdv","ei3_"]]
    writeString(noum[1,1,0] ... "\\n")
end
func main() begin
    amar()
    writeNumber(3.5*24.2)
end
"""
        expect = """asdv

84.700005
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 574))
    
    def test75(self):
        input = """func foo1()
        func foo2()
        func foo3()
        func main() begin
            foo2()
            writeString("OK!")
        end
        func foo1() begin
            foo3()
            writeString("\\tKharmani\\t")
            return 17.5 != 5.4 * 3.2
        end
        func foo2() begin
            dynamic z
            writeNumber(1.4*5)
            z <- foo1()
            writeBool(z)
        end
        func foo3() begin
            writeNumber(1)
            writeNumber(2)
            writeNumber(3)
        end
        """
        expect = """7.0
1.0
2.0
3.0
\tKharmani\t
true
OK!
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 575))
    
    def test76(self):
        input = """number aio[5] <- [5.8,2.13,100e-2,57e-1,0.14e1]
        func main() begin
            number sum <- 0
            var i <- 0
            for i until false by 2 begin
                if (i >= 5) break
                if (i % 2 != 0) continue
                sum <- sum + aio[i]
            end
            writeNumber(sum)
        end
        """
        expect = """8.2
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 576))
    
    def test77(self):
        input = """func foo(number a, bool b)
begin
    a <- 14.3
    b <- a > 15
end
func main()
begin
    number x <- 10
    bool y <- true
    foo(x,y)
    writeNumber(x)
    writeBool(y)
end
"""
        expect = """10.0
true
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 577))
    
    def test78(self):
        input = """dynamic t <- [14.5,98e-1,0.00121e4]
        func main() begin
            t[14 % 13] <- 10
            writeNumber(t[1])
            writeNumber(t[(2.5 + 1.5) / 2])
        end
        """
        expect = """10.0
12.1
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 578))
    
    def test79(self):
        input = """var oip <- [[[1,2,3]],[[5,1,8]]]
        func uteoip(number arr[2,1,3], number t)
        func main() begin
            number a <- 4.5
            a <- uteoip(oip, a)
            writeNumber(a)
        end
        func uteoip(number arr[2,1,3], number t) begin
            if (arr[0,0,2] > t)
            if (arr[1,0,1] = t)
            if (arr[0,0,0] + arr[1,0,2] != t)
            writeString("Yes\\n")
            return t
        end
        """
        expect = """4.5
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 579))
    
    def test80(self):
        input = """## alskdfjaposid soapdfi vcoxi we   asfdp
func manni()
func foo2()
func foo3()
func main() begin
    manni()
end
func foo3() return ["a","b","c","d","e","f","g","h","i","j"]
func manni() begin
    foo2()
end
func foo2() begin
    var list <- foo3()
    writeString(list[2*3+-4+1])
    return
end
"""
        expect = """d
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test81(self):
        input = """func foo(number n) begin
            var s <- 1
            var i <- 1
            for i until i > n by 1 s <- s * i
            return s
        end
        func main() begin
            number t <- foo(0)
            writeNumber(t)
            writeNumber(foo(4))
        end
        """
        expect = """1.0
24.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 581))
    
    def test82(self):
        input = """func main() begin
            if (true) number a <- 2
            number a <- 5
            writeNumber(a)
        end
        """
        expect = """5.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 582))
    
    def test83(self):
        input = """func main() begin
            var i <- 0
            for i until i >= 9 by 1 var t <- "asdfopiwer\\t"
            string t <- "342234"
            writeString(t..."d")
        end
        """
        expect = """342234d
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 583))
    
    def test84(self):
        input = """func foo1(number a)
        func foo2(number a)
        func foo3(number a)
        func main() begin
            writeNumber(foo1(2) + foo2(1))
        end
        func foo1(number a) begin
            return a*2 + foo2(a)
        end
        func foo2(number a) begin
            return a + foo3(a)
        end
        func foo3(number a) begin
            return a*3
        end
        """
        expect = """16.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test85(self):
        input = """func foo1()
        func foo2()
        func foo3()
        var arr <- [[foo1(), foo2()],[foo3(), foo1()]]
        func main() begin
            ##var arr <- [[foo1(), foo2()],[foo3(), foo1()]]
            arr[foo3()-foo1()] <- [foo2()*3,6.2]
            writeNumber(arr[1, 0])
        end
        func foo1() return 1
        func foo2() return 1.5
        func foo3() return 2
        """
        expect = """4.5
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 585))
    
    def test86(self):
        input = """func f(number n) return n + 1
        func f1(number a, number b, number c)
        func main() begin
            number x <- 0
            var a <- f(f(f(f(f(f(0))))))
            writeNumber(a)
            dynamic b <- f1(f(f(f(1))), f1(f(f(0)), f(f(1)), 1), f1(1,2,3))
            writeNumber(b)
        end
        func f1(number a, number b, number c) return (a+c)*b
        """
        expect = """6.0
108.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 586))
    
    def test87(self):
        input = """func f1(number n)
        func f2(number n)
        func f3(number n)
        func main() begin
            writeNumber(f1(1))
        end
        func f1(number n) begin
            return f3(f3(f3(n))) + f2(f3(f3(f3(n))))
        end
        func f2(number n) begin
            return f3(f3(n))
        end
        func f3(number n) begin
            return n
        end
        """
        expect = """2.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 587))
    
    def test88(self):
        input = """func foo1() return [1,2,3]
        number x[3] <- foo1()
        func main() begin
            writeNumber((x[0]+x[1]+x[2])/3)
        end
        """
        expect = """2.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 588))
    
    def test89(self):
        input = """func f1()
        func f2()
        func f3()
        func main() begin
            writeNumber(f1() + f2())
        end
        func f1() begin
            return f3() + f2()
        end
        func f2() begin
            return f3()
        end
        func f3() begin
            return 1
        end
        """
        expect = """3.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test90(self):
        input = """func f1() return "string"
        func f2(string s, number n) begin
            string res <- ""
            var i <- 0
            for i until i >= n by 1 res <- s ... res
            return res
        end
        string mio <- f2(f1(), 5)
        func main() begin
            writeString(mio)
        end
        """
        expect = """stringstringstringstringstring
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 590))
    
    def test91(self):
        input = """func average(number arr[10]) begin
    var i <- 0
    number sum <- 0
    for i until i >= 10 by 1 sum <- sum + arr[i]
    return sum / 10 
end
func rand(number x)
func main() begin
    number arr[10]
    var i <- 0
    var p <- 0
    for i until i >= 10 by 1 begin
        arr[i] <- rand(p)
        p <- rand(p)
    end
    i <- 0
    writeNumber(average(arr))
end
func rand(number x) begin
    return 1*x*x-1
end
"""
        expect = """-0.5
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test92(self):
        input = """func f1(number a, number b)
        func f2(number a)
        func f3()
        func main() begin
            dynamic u <- f2(2)
            writeNumber(u[0]+u[1])
        end
        func f1(number a, number b) return a + b
        func f2(number a) return [f3(),f1(a,a)]
        func f3() return f1(1,2)
        """
        expect = """7.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 592))
    
    def test93(self):
        input = """func foo()
        func main() begin
            foo(5)
        end
        func foo(number n) begin
            var i <- 0
            for i until i >= 5 by 1 begin
                if (i * 2.5 <= 8) begin
                    var j <- 0
                    for j until j >= 6 by 1 + j % 4 
                        if (j < 4) writeString("N")
                end
                else writeString("KO")
            end
        end
        """
        expect = """N
N
N
N
N
N
N
N
N
N
N
N
KO
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 593))
    
    def test94(self):
        input = """func f1() return 1
        func f2(number a) return a + f1()
        func f3(number b) return f2(b)
        func main() begin
            dynamic z
            z <- f3(4)
            writeNumber(z)
        end
        """
        expect = """5.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 594))
    
    def test95(self):
        input = """func mappa(string s[2,2], number a[2,2])
number ios[2,2]
func main() begin
    ios[0] <- [14, 18]
    ios[1] <- [23, 10]
    string sarr[2,2]
    sarr[0,0] <- "abc"
    sarr[0,1] <- "vui"
    sarr[1] <- ["z[e", "iopqw"]
    writeBool(mappa(sarr, ios))
end
func mappa(string s[2,2], number a[2,2]) begin
    return (s[1,0]==s[0,1]) and not (a[0,0] != a[0,1])
end
"""
        expect = """false
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 595))
    
    def test96(self):
        input = """func f1()
func f2(number n)
func foo1(number a, number b) return a * -b
func foo2() begin
    return foo1(f1(), f2(4))
end
func main() begin
    writeNumber(foo2())
end
func f1() return f2(5) + 1
func f2(number n) return n + 2
"""
        expect = """-48.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 596))
    
    def test97(self):
        input = """bool aiowap[3,2] <- [[true, 14 < 26e-1],["12930"=="4930",(1=1)and(4.5!=7)],[false,false]]
func main() begin
    var u <- aiowap[2,0] or not aiowap[0,1] and (aiowap[1,1] or aiowap[0,0])
    writeBool(u)
    writeString("See you next time!\\n")
end
"""
        expect = """true
See you next time!

"""
        #self.assertTrue(TestCodeGen.test(input, expect, 597))
    
    def test98(self):
        input = """func main() begin
    dynamic u
    writeNumber(14.5+5.7/3*4.5--5-9.5)
    u <- ["sopa8", "a239", "totot"]
    writeString(u[0])
    u[2.5 - 1.5] <- "zxcvo"
    writeString(u[1]...u[2])
end
"""
        expect = """18.55
sopa8
zxcvototot
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 598))
    
    def test99(self):
        input = """func fami(number arr1[3,3], number arr2[3,3]) begin
    number arr[3,3] <- [[0,0,0],[0,0,0],[0,0,0]]
    var i <- 0
    for i until i >= 3 by 1 begin
        var j <- 0
        for j until j >= 3 by 1 arr[i,j] <- arr1[i,j] + arr2[i,j]
    end
    return arr
end
func qpwo() return [[2,3,4],[5,6,7],[8,9,10]]
func main() begin
    number arr1[3,3] <- [[1,2,3],[4,5,6],[7,8,9]]
    number arr2[3,3] <- qpwo()
    dynamic t <- fami(arr2, arr1)
    var i <- 0
    for i until i >= 3 by 1 writeNumber(t[i,i])
end
"""
        expect = """3.0
11.0
19.0
"""
        #self.assertTrue(TestCodeGen.test(input, expect, 599))