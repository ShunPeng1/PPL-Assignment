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
        expect = "Type Mismatch In Expression: BinaryOp(..., StringLit(1), NumLit(2.0))"
        #self.assertTrue(TestChecker.test(input, expect, 406))

    def test_variable_declare_4(self):
        input = """
            number s2 <- "1" ... "2"
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(s2), NumberType, None, BinaryOp(..., StringLit(1), StringLit(2)))"
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
                return 
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
                return 

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
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), BooleanLit(True))"
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
        expect = "Type Mismatch In Expression: BinaryOp(and, Id(b), UnaryOp(not, Id(c)))"
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
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), Id(c))"
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
                return 
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
        expect = "Type Mismatch In Expression: BinaryOp(and, Id(c), BooleanLit(True))"
        #self.assertTrue(TestChecker.test(input, expect, 430))


    def test_assign_statement_1(self):
        input = """
            number a
            number b
            func main()
            begin
                a <- b
                return
            end
        """
        expect = "[]"
        #self.assertTrue(TestChecker.test(input, expect, 431))

    def test_assign_statement_2(self):
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
        #self.assertTrue(TestChecker.test(input, expect, 432))

    def test_assign_statement_3(self):
        input = """
            dynamic a
            dynamic b
            func main()
            begin
                a <- 1 + 1
                a <- b
                return
            end
        """
        expect = "[]"
        #self.assertTrue(TestChecker.test(input, expect, 433))

    def test_assign_statement_4(self):
        input = """
            dynamic a
            dynamic b
            func main()
            begin
                a <- 1 + 1
                a <- b
                b <- true
                return
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), BooleanLit(True))"
        #self.assertTrue(TestChecker.test(input, expect, 434))

    def test_assign_statement_5(self):
        input = """
            dynamic a
            dynamic b
            dynamic c
            func main()
            begin
                c <- a + b 
                return
            end
        """
        expect = "[]"
        #self.assertTrue(TestChecker.test(input, expect, 435))

    def test_assign_statement_6(self):
        input = """
            dynamic a
            dynamic b
            dynamic c
            func main()
            begin
                c <- a + b 
                c <- true
                return
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c), BooleanLit(True))"
        #self.assertTrue(TestChecker.test(input, expect, 436))

    def test_if_statement_1(self):
        input = """
            number a
            number b
            func main()
            begin
                if (a < b) 
                    return
                elif (a > b) 
                    return
                else
                    return
            end
        """
        expect = "[]"
        #self.assertTrue(TestChecker.test(input, expect, 437))

    def test_if_statement_2(self):
        input = """
            dynamic a
            dynamic b
            func main()
            begin
                if (a) 
                    return
                elif (b) 
                    return
                else
                    a <- b
                    a <- 1
                    return
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(1.0))"
        #self.assertTrue(TestChecker.test(input, expect, 438))

    def test_callstmt_1(self):
        input = """
            func foo()
                return
            func main()
            begin
                foo()
                return
            end
        """
        expect = "[]"
        #self.assertTrue(TestChecker.test(input, expect, 439))

    def test_callstmt_2(self):
        input = """
            func foo(number a)
                return
            func main()
            begin
                dynamic a
                foo(a)
                a <- true
                return
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        #self.assertTrue(TestChecker.test(input, expect, 440))

    def test_callstmt_3(self):
        input = """
            func foo()
                return
            func main()
            begin
                dynamic foo
                foo()
                return
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        #self.assertTrue(TestChecker.test(input, expect, 441))
            
    def test_callstmt_4(self):
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
        #self.assertTrue(TestChecker.test(input, expect, 442))
    
    def test_callepxr_1(self):
        input = """
            func foo()
                return 0
            func main()
            begin
                foo()
                return
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        #self.assertTrue(TestChecker.test(input, expect, 443))

    def test_callepxr_2(self):
        input = """
            func foo()
                return 0
            func main()
            begin
                dynamic a <- foo()
                a <- true
            end
        """       
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        #self.assertTrue(TestChecker.test(input, expect, 444))

    def test_callepxr_3(self):
        input = """
            func foo()
                return 0
            func main()
            begin
                bool a <- foo()
            end
        """        
        
        expect = "Type Mismatch In Statement: VarDecl(Id(a), BoolType, None, CallExpr(Id(foo), []))"
        #self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test_callepxr_4(self):
        input = """
            func foo()
            
            func main()
            begin
                dynamic a <- foo()
                a <- 1
            end

            func foo()
                return 0
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, CallExpr(Id(foo), []))"
        #self.assertTrue(TestChecker.test(input, expect, 446))

    def test_callepxr_5(self):
        input = """
            func foo()
                return 0
            func foo2()
                return true
            func main()
            begin
                dynamic c <- foo2() + foo()

            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, CallExpr(Id(foo2), []), CallExpr(Id(foo), []))"
        #self.assertTrue(TestChecker.test(input, expect, 447))


    def test_callepxr_6(self):
        input = """
            func foo(number a)
            
            func main()
            begin
                number a <- foo(1)
            end

            func foo(number a)
                return true
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        #self.assertTrue(TestChecker.test(input, expect, 448))


    def test_callepxr_7(self):
        input = """
            func foo()
            begin
                if (true) 
                    return 0
                else 
                    return true
            end
            func main()
            begin
                dynamic a <- foo()
            end
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        #self.assertTrue(TestChecker.test(input, expect, 449))

    
    def test_callepxr_8(self):
        input = """
            func foo()
            begin
                return foo()
            end
            func main()
            begin
                number a <- foo()
            end
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(foo), []))"
        #self.assertTrue(TestChecker.test(input, expect, 450))


    def test_callepxr_9(self):
        input = """
            func foo(number a)
            begin
                if (a = 0)
                    return 0
                else
                    return foo(a - 1)        
            end

            func main()
            begin
                var a <- foo(5)
            end
        """
        expect = "[]"
        #self.assertTrue(TestChecker.test(input, expect, 451))


    def test_callepxr_10(self):
        input = """
            func foo(number a)

            func main()
            begin
                number a <- foo(5)
            end

            func foo(number a)
            begin
                if (a > 0)
                    return foo(a - 1)
                elif (a = 0)
                    return 0    
                else
                    return true

            end

        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        #self.assertTrue(TestChecker.test(input, expect, 452))

    def test_callepxr_11(self):
        input = """
            func foo(number a)

            func main()
            begin
                dynamic a <- foo(5) and true
            end

            func foo(number a)
            begin
                if (a > 0)
                    return foo(a - 1)
                elif (a = 0)
                    return true    
                else
                    return 0

            end

        """
        expect = "Type Mismatch In Statement: Return(NumLit(0.0))"
        #self.assertTrue(TestChecker.test(input, expect, 453))

    def test_callepxr_12(self):
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
        #self.assertTrue(TestChecker.test(input, expect, 454))

    def test_for_1(self):
        input = """
            func main()
            begin
                var i <- 0
                for i until i >= 10 by 1
                    return 0
            end
        """

        expect = "No Entry Point"
        #self.assertTrue(TestChecker.test(input, expect, 455))

    def test_for_2(self):
        input = """
            func main()
            begin
                dynamic i
                for i until i >= 10 by 1
                    return 
                break
            end
        """
        expect = "Break Not In Loop"
        #self.assertTrue(TestChecker.test(input, expect, 456))

    def test_for_3(self):
        input = """
            func main()
            begin
                for i until i >= 10 by 1
                    break
            end
        """
        expect = "Undeclared Identifier: i"
        #self.assertTrue(TestChecker.test(input, expect, 457))


    def test_for_4(self):
        input = """
            func main()
            begin
                dynamic i
                for i until i >= 10 by 1
                    continue
                continue
            end
        """
        expect = "Continue Not In Loop"
        #self.assertTrue(TestChecker.test(input, expect, 458))

    def test_for_5(self):
        input = """
            func main()
            begin
                dynamic i
                for i until i >= 10 by 1
                begin
                    for i until i >= 10 by 1
                    begin
                        continue
                        break
                    end
                    continue
                    break
                end
                break                
            end
        """
        expect = "Break Not In Loop"
        #self.assertTrue(TestChecker.test(input, expect, 459))

    def test_for_6(self):
        input = """
            func foo()
            func foo2()
            func foo3()

            func main()
            begin
                dynamic i
                dynamic j
                dynamic k
                dynamic l
                for i until j >= k by l
                begin
                    continue
                end
                var a <- i + j + k + l

                for i until foo by foo2
                begin
                    foo3()
                end

                number b <- foo2()
                bool c <- foo()
                
            end

            func foo()
                return true
            func foo2()
                return 1
            func foo3()
                return 0
        """
        expect = "Type Mismatch In Statement: Return(NumLit(0.0))"
        #self.assertTrue(TestChecker.test(input, expect, 460))


    def test_if_1(self):
        input = """
            func main()
            begin
                if (true)
                    return 0
                else
                    return true
            end
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        #self.assertTrue(TestChecker.test(input, expect, 461))

    def test_if_2(self):
        input = """
            func foo()
                return 0
            
            func main()
            begin
                if (foo())
                    return 0
                else
                    return 1
            end
        """
        expect = "Type Mismatch In Statement: If((CallExpr(Id(foo), []), Return(NumLit(0.0))), [], Return(NumLit(1.0)))"
        #self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test_if_3(self):
        input = """
            func foo()
            
            func main()
            begin
                dynamic a
                if (foo())
                    return true
                elif (a)
                    return a
                else
                    return foo()
            end

            func foo()
                return 0
        """
        expect = "Type Mismatch In Statement: Return(NumLit(0.0))"
        #self.assertTrue(TestChecker.test(input, expect, 463))

    def test_array_1(self):
        input = """
            func main()
            begin
                number a[5]
                a[0] <- 1
                a[1] <- 2
                a[2] <- 3
                a[3] <- 4
                a[4] <- 5
                a[5] <- 6
                a[6] <- true
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(6.0)]), BooleanLit(True))"
        #self.assertTrue(TestChecker.test(input, expect, 464))

    def test_array_2(self):
        input = """
            func main()
            begin
                number a[5]
                a[0] <- 1
                a[1] <- 2
                a[2] <- 3
                a[3] <- 4
                a[4] <- 5
                a[5] <- 6
                a <- 1
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(1.0))"
        #self.assertTrue(TestChecker.test(input, expect, 465))

    def test_array_3(self):
        input = """
            func main()
            begin
                dynamic b
                number a[5]
                a[0] <- 1
                a[1] <- 2
                a[2] <- 3
                a[3] <- 4
                a[4] <- 5
                a[5] <- 6
                b <- a[5]
                b <- true
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), BooleanLit(True))"
        #self.assertTrue(TestChecker.test(input, expect, 466))

    def test_array_4(self):
        input = """
            func main()
            begin
                dynamic b
                number a[5]
                a[0] <- 1
                a[1] <- 2
                a[2] <- 3
                a[3] <- 4
                a[4] <- 5
                a[5] <- 6
                b <- a
                b <- 1
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), NumLit(1.0))"
        #self.assertTrue(TestChecker.test(input, expect, 467))

    def test_array_5(self):
        input = """
            func foo()
            func foo2()
            func main()
            begin
                dynamic b
                number a[5]
                a[0] <- foo()
                b <- a
                b <- foo2()
            end

            func foo()
                return 0
            func foo2()
                return true
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        #self.assertTrue(TestChecker.test(input, expect, 468))

    def test_array_6(self):
        input = """
            func foo()
            func foo2()
                return [1,2,3,4,5]
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
        #self.assertTrue(TestChecker.test(input, expect, 469))

    def test_array_7(self):
        input = """
            func foo(number a[5])
                return a[5]
            func main()
            begin
                number a[5]
                dynamic b <- foo(a)
                b <- true
            end

        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), BooleanLit(True))"
        #self.assertTrue(TestChecker.test(input, expect, 470))

    def test_array_8(self):
        input = """
        
            func main()
            begin
                number a[5] <- [1,2,3,4]
 
            end

        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))"
        #self.assertTrue(TestChecker.test(input, expect, 471))

    def test_array_9(self):
        input = """
            func main()
            begin
                number a <- [1,2,3,4,5]
                
            end

        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
        #self.assertTrue(TestChecker.test(input, expect, 472))

    def test_array_10(self):
        input = """
            func foo()
                return [1,2,3,4,5]
            func main()
            begin
                
                dynamic a <- [1,2,3,4,5]
                number b[5] <- [1,2,3,4,5]
                dynamic c <- b 
                dynamic d <- foo()
            end
        """
        
        expect = "[]"
        #self.assertTrue(TestChecker.test(input, expect, 473))

    def test_array_11(self):
        input = """
            func foo(number a[3])
                return 2
            func main()
            begin
                number a[5] <- [1,2,3,4,5]
                a[3] <- foo(a) 
            end

        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(a)])"
        #self.assertTrue(TestChecker.test(input, expect, 474))

    def test_array_12(self):
        input = """
            func foo()
                return 2
            func foo2()
            func foo3()
            func main()
            begin
                dynamic b
                number a[5] <- [1+1,foo(), foo2(), b, foo3()]
                a[3] <- b
            end

            func foo2()
                return 0
            func foo3()
                return true
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(True))"
        #self.assertTrue(TestChecker.test(input, expect, 475))

    def test_array_13(self):
        input = """
            func main()
            begin
                number a[3,2] <- [[1,2],[3,4],[5,6]]
                a[1,1] <- 1
                a[1] <- [1,2]
                a[2] <- 1
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), NumLit(1.0))"
        #self.assertTrue(TestChecker.test(input, expect, 476))

    def test_array_14(self):
        input = """
            func main()
            begin
                number a[3,2] <- [[1,2],[3,4],[6]]
                
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0, 2.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(6.0))))"
        #self.assertTrue(TestChecker.test(input, expect, 477))


    def test_array_15(self):
        input = """
            func foo()
            func main()
            begin
                number a[3,2] <- [foo(), foo(), foo()]
                a[1] <- foo()
            end

            func foo()
                return [1,2,4]
        """
        expect = "Type Mismatch In Statement: Return(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(4.0)))"
        #self.assertTrue(TestChecker.test(input, expect, 478))

    def test_array_16(self):
        input = """
            func foo()
            func main()
            begin
                number a[3,2] <- [foo(), [3,4], [5,6]]
                a[1,1] <- foo()
            end

            func foo()
                return [1,2]
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(1.0), NumLit(1.0)]), CallExpr(Id(foo), []))"
        #self.assertTrue(TestChecker.test(input, expect, 479))

    def test_array_17(self):
        input = """
            func foo()
            func main()
            begin
                dynamic b
                number a[3,2] <- [foo(), b, [5,6]]
                b <- a[3]
                a[1,1] <- b
            end

            func foo()
                return [1,2,3]
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(1.0), NumLit(1.0)]), Id(b))"
        #self.assertTrue(TestChecker.test(input, expect, 480))






        # KIEN TESTCASES
    def test441(self):
        input = """
number a <- 1 + "Hello"
func main()
    return
"""
        expect = "Type Mismatch In Expression: BinaryOp(+,NumLit(1.0),StringLit(Hello))"
        #!self.assertTrue(TestChecker.test(input, expect, 441))
    
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