; Test.j

; Generated by ClassFileAnalyzer (Can)
; Analyzer and Disassembler for Java class files
; (Jasmin syntax 2, http://jasmin.sourceforge.net)
;
; ClassFileAnalyzer, version 0.7.0 


.bytecode 61.0
.source Test.java
.class public Test
.super java/lang/Object

.method public <init>()V
  .limit stack 1
  .limit locals 1
  .line 2
  0: aload_0
  1: invokespecial java/lang/Object/<init>()V
  4: return
.end method

.method public static foo([I)V
  .limit stack 0
  .limit locals 1
  .line 7
  0: return
.end method

.method public static main([Ljava/lang/String;)V
  .limit stack 2
  .limit locals 5
  .line 11
  0: fconst_1
  1: fstore_1
  .line 12
  2: fconst_2
  3: fstore_2
  .line 13
  4: ldc 3.0
  6: fstore_3
  .line 15
  7: fload_1
  8: fload_2
  9: fmul
  10: fload_3
  11: fsub
  12: fstore 4
  .line 18
  14: return
.end method

