import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test401(self):
        input = """

func areDivisors(number num1, number num2)
    return ((num1 % num2 = 0) or (num2 % num1 = 0))
            
func main()
    begin
        var num1 <- readNumber()
        var num2 <- readNumber()
        if (areDivisors(num1, num2)) writeString("Yes")
        else writeString("No")
    end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test402(self):
        input = """

func isPrime(number x)

func main()
begin
    number x <- readNumber()
    if (isPrime(x)) writeString("Yes")
    else writeString("No")
end

func isPrime(number x)
begin
    if (x <= 1) return false
    var i <- 2
    for i until i > x / 2 by 1
        begin
            if (x % i = 0) return false
        end
    return true
end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test403(self):
        input = """

func main()

        """
        expect = "No Function Definition: main"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test404(self):
        input = """
 
func foo()
func main() return 

        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test405(self):
        input = """

func main() return 1

        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test406(self):
        input = """

func main(number a) return

        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test407(self):
        input = """

func main() begin
    break 
end 

        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test408(self):
        input = """

func main() begin
    continue
end

        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test409(self):
        input = """

func foo()
func foo() return

        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test410(self):
        input = """

func foo()
func foo()

        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test411(self):
        input = """

func foo() return 
func foo()

        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test412(self):
        input = """

func foo(number a) 
func foo(number b) return
func main() return

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test413(self):
        input = """

func foo(number a)
func foo(string a) return 

        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test414(self):
        input = """

func foo(number a, number a)
func foo(number a, string b) return 

        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test415(self):
        input = """

func foo(number a, number a)
func foo(number c, number k) return
func main() return 

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test416(self):
        input = """

func foo(number a, number a)
func foo(number b, number b) return

        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test417(self):
        input = """

dynamic a
number a 

        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test418(self):
        input = """

dynamic a 
func main() begin
    dynamic a
end 

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test419(self):
        input = """

dynamic a
func a()
func main() return 

        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test420(self):
        input = """

func a(number a) begin
    string a 
end 
func main() return

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test421(self):
        input = """

func main() begin
    dynamic a <- readNumber()
    writeNumber(a)

    dynamic b <- readBool()
    writeBool(b)

    dynamic c <- readString()
    writeString(c)
end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test422(self):
        input = """

func main() begin
    a <- readNumber()
end 

        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test423(self):
        input = """

func main() begin
    foo()
end

        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test424(self):
        input = """

func main() begin 
    var c <- c
end 

        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, var, Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test425(self):
        input = """

func main() begin
    dynamic d <- d 
end

        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(d), None, dynamic, Id(d))"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test426(self):
        input = """

func foo(number x, string y)
func foo(number x, number x) begin
end

        """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test427(self):
        input = """

func f(number x)

dynamic x <- f(2) + 1

func main()
begin
    return
end

        """
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test428(self):
        input = """

func f(number x[2, 3])
    return x[2]

func main()
begin
    number x[2, 3] <- [[1, 2, 3], [4, 5, 6]]
    writeNumber(f()[2])
end

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test429(self):
        input = """

func foo() begin
     return 1
     return "a"
end
func main() return

        """
        expect = "Type Mismatch In Statement: Return(StringLit(a))"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test430(self):
        input = """

func foo() begin
     number a
     if (true) number a
end
func main() return

        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test431(self):
        input = """

func f(number x)
begin
    if (x = 0) return 0
    elif (x = 1) return 1
    else return f(x - 1) + f(x - 2)
end
    
func main()
begin
    dynamic a
    number x <- f(a)
    a[0] <- [1, 2, 3]
end

        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test432(self):
        input = """

func foo() begin
    dynamic a
    dynamic x <- a == (a+2)
end
func main() return

        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test433(self):
        input = """

func main() begin
    dynamic x
    number a[3, 2] <- [[x], [x], [x]]
end

        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(x)), ArrayLit(Id(x)), ArrayLit(Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test434(self):
        input = """

dynamic a
string x[1] <- [a]
func main() return

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test435(self):
        input = """

func main() begin
    dynamic x
    dynamic y
    number a[2] <- [x,y]
    writeNumber(x)
    number k[1] <- y
end

        """
        expect = "Type Mismatch In Statement: VarDecl(Id(k), ArrayType([1.0], NumberType), None, Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test436(self):
        input = """

func main()
begin
    dynamic a
    dynamic b
    dynamic c
    number x[3, 2] <- [a, b, [c, 0]]
    a <- [1]
    b <- [3, 4]
    c <- 0
end

        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test437(self):
        input = """

func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic x <- [readNumber(), a, b, c]
    a <- 3
    b <- x[0]
    c <- a + b
end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test438(self):
        input = """

dynamic x
dynamic y
func main()
begin
    dynamic z
    dynamic arr <- [[1, x], [2, y], [3, z]]
    x <- 20
    y <- 30
    z <- "Hi"
end

        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(z), StringLit(Hi))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test439(self):
        input = """

dynamic a
func main()
begin
    var x <- [a, [1, 2, 3]]
    a <- [1, 9, 6]
    x <- [[3, 9, 6], [1, 3, 2]]
    writeNumber(x[0, 0])
end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test440(self):
        input = """

func main()
begin
    dynamic a
    dynamic b
    dynamic c
    dynamic d
    var x <- [a, b, c, [[1, 2, 3, 4], [5, 6, 7, 8]]]
    c[0] <- d
    d <- [0, 3, 1]
end

        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(d), ArrayLit(NumLit(0.0), NumLit(3.0), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test441(self):
        input = """

func main()
begin
    number arr[2, 2] <- [1, 2, 3, 4]
end

        """
        expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test442(self):
        input = """

func main()
begin
    number a[5]
    a[0] <- 1
    a[1] <- 2
    a[2] <- 3
    a[3] <- 4
    a[4] <- 5
    a <- 1
end

        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test443(self):
        input = """

func foo()
func foo2()
    return [1, 2, 3, 4, 5]
func main()
begin
    dynamic b
    number a[5]
    b <- a
    b <- foo2()
    b[1] <- foo()

end

func foo()
    return foo2()

        """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo2), []))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test444(self):
        input = """

func main() begin 
    if (true) return
    elif (false) return 1
    else return "a"
end

        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test445(self):
        input = """

func main() begin 
    dynamic i 
    return 1
    return i 
    number a[1] <- i
end 

        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0], NumberType), None, Id(i))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test446(self):
        input = """

func main()
begin
    number a[5] <- [1, 2, 3, 4]
end

        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test447(self):
        input = """

func main()
begin
    number a <- [1, 2, 3, 4, 5]
end

        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test448(self):
        input = """

func foo()
func main()
begin
    number a[3,2] <- [foo(), foo(), foo()]
    a[1] <- foo()
end

func foo() return [1, 2, 3]

        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test449(self):
        input = """

func f(number x)

func main()
begin
    dynamic d <- f(10)
end

func f(number x)
begin
    return f(x)
end

        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(d), None, dynamic, CallExpr(Id(f), [NumLit(10.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test450(self):
        input = """

func main()
begin 
    dynamic a
    a[0] <- [1,2,3]
end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test451(self):
        input = """

dynamic a <- a[0,1,2]
            
func main() return

        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, ArrayCell(Id(a), [NumLit(0.0), NumLit(1.0), NumLit(2.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test452(self):
        input = """

func a()
    return true

func main()
begin
    dynamic b <- a()
    dynamic c <- b()
end

        """
        expect = "Undeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test453(self):
        input = """

func main() 
begin
    dynamic x
    dynamic a <- [[[x]], [[[1]]]]
end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test454(self):
        input = """

func main() 
begin
    dynamic x
    dynamic y
    number a[2, 1] <- [[x], [y]]
end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test455(self):
        input = """

func main()
begin
    dynamic num
    bool arr <- num and (num > num)
end

        """
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(num), Id(num))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test456(self):
        input = """

func main()
begin
    dynamic num
    bool arr[2] <- [true, num and (num > num)]
end

        """
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(num), Id(num))"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test457(self):
        input = """

func a(number b)
        
func main()
begin
    number b <- a(10) + 1
end

func a(number b)
begin
    return "Type Mismatch"
end

        """
        expect = "Type Mismatch In Statement: Return(StringLit(Type Mismatch))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test458(self):
        input = """

func main()
begin
    number a[2,2]
    dynamic b <- a[1,2]
    dynamic c <- a[2]
    dynamic d <- a

    b <- 2
    c <- [b,2] 
    d <- [[1,2],[3,4]]
    d <- [[b,2],c]
    d <- [c,[b,[2]]]
end

        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(b), ArrayLit(NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test459(self):
        input = """

dynamic a
number b <- a[0]

        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test460(self):
        input = """

func foo()
func main() begin 
    var a <- foo()
end

        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test461(self):
        input = """

func foo() begin 
    if(true) begin 
        return 1
        return "a"
    end 
    elif (false) return true
end

func main() return

        """
        expect = "Type Mismatch In Statement: Return(StringLit(a))"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test462(self):
        input = """

func main() begin 
    number a 
    begin
        string a
        begin 
            bool a 
        end
    end
end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test463(self):
        input = """

func main() begin 
    dynamic a 
    dynamic x
    a <- [[[[[[1]]]]], [x]]
end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test464(self):
        input = """

func main()
func foo()
begin
    number a <- main()
end
func main() return

        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test465(self):
        input = """

func main()
begin
    dynamic a
    dynamic b
    dynamic c
    var arr <-[[a],[b],[c],[99]]
end    

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test466(self):
        input = """

dynamic a <- 1
dynamic b <- 1 + a
dynamic c <- -b <= a
dynamic d <- b and not c

func main() return

        """
        expect = "Type Mismatch In Expression: BinaryOp(and, Id(b), UnaryOp(not, Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test467(self):
        input = """

dynamic x
dynamic y 
dynamic a <- x ... y + x and y or x >= y

func main() return

        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(y), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test468(self):
        input = """

func foo() begin
    dynamic x
    dynamic y 
    dynamic a <- y and y + x
end

        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(y), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test469(self):
        input = """

func foo() begin
    dynamic x
    number a[1, 2] <- [x] 
    
    return x[1]
end

        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test470(self):
        input = """

func foo() begin
    dynamic x
    number a[1, 2] <- [[x]] 
end

        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([1.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test471(self):
        input = """

dynamic a
func foo() return a
func main()
begin
    number num <- foo()
end

        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test472(self):
        input = """

func foo() begin
    dynamic x
    var a <- x and true 
    return x
end

func main()
begin
    if (foo()) return
    else return
end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test473(self):
        input = """

func foo() begin
    dynamic i
    for i until i >= i by i
        return 0
end 

func main() return 

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test474(self):
        input = """

func foo() begin
    for i until i >= i by i
        return 0
end 

func main() return 

        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test475(self):
        input = """

func foo(number a)
begin
    dynamic b
    dynamic c <- foo(b) + 1
    b <- 1 + c
    if (a > 0)
        return b
    elif (a = 0)
        return c
    elif (a < 0)
        return 0    
    else
        return true
end

func main()
begin
    dynamic a <- foo(5) 
end

        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test476(self):
        input = """

func main()
begin
    for i until i >= 10 by 1
        break
end

        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test477(self):
        input = """

number a
number b
func main()
begin
    a <- 1 + 1
    a <- true
    return
end

        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test478(self):
        input = """

func foo()
    return
func main()
begin
    dynamic a
    foo(a)
    return
end

        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test479(self):
        input = """

func foo()
            
func main()
begin
    dynamic a <- foo()
    a <- 1
end

func foo() return 0

        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, CallExpr(Id(foo), []))"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test480(self):
        input = """

func foo()
            
func main()
begin
    dynamic a
    if (foo()) return true
    elif (a) return a
    else return foo()
end

func foo() return 0

        """
        expect = "Type Mismatch In Statement: Return(NumLit(0.0))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test481(self):
        input = """

func main()
begin
    number a[3, 2] <- [[1, 2], [3, 4], [5, 6]]
    a[1, 1] <- 1
    a[1] <- [1, 2]
    a[2] <- 1
end

        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test482(self):
        input = """

func foo()
func main()
begin
    dynamic b
    number a[3, 2] <- [foo(), b, [5,6]]
    b <- a[3]
    a[1, 1] <- b
end

func foo() return [1, 2, 3]

        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(1.0), NumLit(1.0)]), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test483(self):
        input = """

func fun() begin
    number a[3, 2]
    return [[1, 2], [3, 4]]
    return a
end
func main() return

        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test484(self):
        input = """

func fun() begin
    string a[2, 2, 3]
    return a
    return [["1", "2"], ["3", "4"]]
end
func main() return 

        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(ArrayLit(StringLit(1), StringLit(2)), ArrayLit(StringLit(3), StringLit(4))))"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test485(self):
        input = """

dynamic x
number a[3] <- [x, x, "1"]
func main()
begin
    x <- 1
end

        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(Id(x), Id(x), StringLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test486(self):
        input = """

dynamic x
number a[1, 1, 2, 2] <- [[[[1, 2], x]]]
func  main()
begin
    x <- [1, 2]
end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test487(self):
        input = """

dynamic x
number a[1, 1, 2, 2] <- [[[x, x]]]
func  main()
begin
    x <- [1, 2]
end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test488(self):
        input = """

func foo() begin
    dynamic x
    return [x]                
end
func main() return 

        """
        expect = "Type Cannot Be Inferred: Return(ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test489(self):
        input = """

func foo(number a[2, 2]) return 1
func main() begin
    dynamic x
    var a <- foo(x)
    x <- [1, 2]
end

        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), ArrayLit(NumLit(1.0), NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test490(self):
        input = """

func foo() begin
    dynamic x
    dynamic y
    return [[1], [2]]
    return [x, [y]]
    x <- [1]
    y <- x
end
func main() return

        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(y), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test491(self):
        input = """

dynamic a
func main() begin
    var b <- a[0]
end

        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, ArrayCell(Id(a), [NumLit(0.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test492(self):
        input = """

dynamic a
func main() begin
    string b <- a[0]
end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test493(self):
        input = """

string a
func main() begin
    number a <- a
end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test494(self):
        input = """

func main()
begin
    dynamic a
    dynamic c <- a[1,2] 
end

        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(c), None, dynamic, ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test495(self):
        input = """

func main()
begin
    dynamic a
    dynamic b 
    number arr[2, 2] <- [[a, b]]
end 

        """
        expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(a), Id(b))))"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test496(self):
        input = """

func main()
begin
    dynamic a
    var i <- a[2] ... 2152184
end

        """
        expect = "Type Mismatch In Expression: BinaryOp(..., ArrayCell(Id(a), [NumLit(2.0)]), NumLit(2152184.0))"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test497(self):
        input = """

func main()
begin
    dynamic x

    x <- (x = 1) or ("BKISC" == "best club")
end

        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), BinaryOp(or, BinaryOp(=, Id(x), NumLit(1.0)), BinaryOp(==, StringLit(BKISC), StringLit(best club))))"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test498(self):
        input = """

func foo(number arr[1, 2]) return
dynamic x
            
func main()
begin
    number b[1, 2]
    var a <- [[x, x]]
    a <- b
    return foo(a)
end

        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, ArrayLit(ArrayLit(Id(x), Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test499(self):
        input = """

func foo(number arr[1, 2]) return
dynamic x
            
func main()
begin
    number b[1, 2]
    dynamic a 
    a <- [[x, x]]
    a <- b
    return foo(a)
end

        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), ArrayLit(ArrayLit(Id(x), Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test500(self):
        input = """

func foo() return
func main()
begin
    dynamic x
    dynamic y
    dynamic z
      string a[3] <- [z, [[x, x], [y, [x]]]]
end

        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(x), Id(x)), ArrayLit(Id(y), ArrayLit(Id(x))))"
        self.assertTrue(TestChecker.test(input, expect, 500))

    def test501(self):
        input = """

func foo() return
func main()
begin
    dynamic x
    dynamic y
    dynamic z
      string a[3] <- [[x], x, z]
end

        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(Id(x)), Id(x), Id(z))"
        self.assertTrue(TestChecker.test(input, expect, 501))

    def test502(self):
        input = """
            dynamic a
            func main() begin
                string z[2]
                string x <- a[4]
                z[1] <- a[4]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 502))

    def test503(self):
        input = """
            dynamic a
            func main() begin
                string z[2]
                string x <- a[4]
                z <- a[4]
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 503))

