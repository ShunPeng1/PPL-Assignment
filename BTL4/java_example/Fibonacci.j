; Fibonacci.j

; Generated by ClassFileAnalyzer (Can)
; Analyzer and Disassembler for Java class files
; (Jasmin syntax 2, http://jasmin.sourceforge.net)
;
; ClassFileAnalyzer, version 0.7.0 


.bytecode 61.0
.source Fibonacci.java
.class public Fibonacci
.super java/lang/Object

.method public <init>()V
  .limit stack 1
  .limit locals 1
  .line 1
  0: aload_0
  1: invokespecial java/lang/Object/<init>()V
  4: return
.end method

.method public static fibonacciRecursive(I)I
  .limit stack 3
  .limit locals 1
  .line 4
  0: iload_0
  1: iconst_1
  2: if_icmpgt Label7
  .line 5
  5: iload_0
  6: ireturn
Label7:
  .line 6
  7: iload_0
  8: iconst_1
  9: isub
  10: invokestatic Fibonacci/fibonacciRecursive(I)I
  13: iload_0
  14: iconst_2
  15: isub
  16: invokestatic Fibonacci/fibonacciRecursive(I)I
  19: iadd
  20: ireturn
  ; same_frame (frameNumber = 0)
  ; frame_type = 7, offset_delta = 7
  ; frame bytes: 7 
  .stack 
    offset 7
    .end stack
.end method

.method public static fibonacciDynamic(I)I
  .limit stack 6
  .limit locals 3
  .line 11
  0: iload_0
  1: iconst_1
  2: iadd
  3: newarray int
  5: astore_1
  .line 12
  6: aload_1
  7: iconst_0
  8: iconst_0
  9: iastore
  .line 13
  10: aload_1
  11: iconst_1
  12: iconst_1
  13: iastore
  .line 15
  14: iconst_2
  15: istore_2
Label16:
  16: iload_2
  17: iload_0
  18: if_icmpgt Label41
  .line 16
  21: aload_1
  22: iload_2
  23: aload_1
  24: iload_2
  25: iconst_1
  26: isub
  27: iaload
  28: aload_1
  29: iload_2
  30: iconst_2
  31: isub
  32: iaload
  33: iadd
  34: iastore
  .line 15
  35: iinc 2 1
  38: goto Label16
Label41:
  .line 19
  41: aload_1
  42: iload_0
  43: iaload
  44: ireturn
  ; append_frame (frameNumber = 0)
  ; frame_type = 253, offset_delta = 16
  ; frame bytes: 253 0 16 7 0 31 1 
  .stack 
    offset 16
    locals Object [I
    locals Integer
    .end stack
  ; chop_frame (frameNumber = 1)
  ; frame_type = 250, offset_delta = 24
  ; frame bytes: 250 0 24 
  .stack 
    offset 41
    locals Object [I
    .end stack
.end method

.method public static main([Ljava/lang/String;)V
  .limit stack 2
  .limit locals 2
  .line 23
  0: bipush 10
  2: istore_1
  .line 24
  3: getstatic java/lang/System/out Ljava/io/PrintStream;
  6: iload_1
  7: invokestatic Fibonacci/fibonacciRecursive(I)I
  10: invokevirtual java/io/PrintStream/println(I)V
  .line 25
  13: getstatic java/lang/System/out Ljava/io/PrintStream;
  16: iload_1
  17: invokestatic Fibonacci/fibonacciDynamic(I)I
  20: invokevirtual java/io/PrintStream/println(I)V
  .line 26
  23: return
.end method
