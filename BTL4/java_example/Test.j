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

.field static x [I

.method public <init>()V
  .limit stack 1
  .limit locals 1
  .line 2
  0: aload_0
  1: invokespecial java/lang/Object/<init>()V
  4: return
.end method

.method public static main([Ljava/lang/String;)V
  .limit stack 4
  .limit locals 3
  .line 7
  0: iconst_5
  1: newarray int
  3: dup
  4: iconst_0
  5: iconst_1
  6: iastore
  7: dup
  8: iconst_1
  9: iconst_2
  10: iastore
  11: dup
  12: iconst_2
  13: iconst_3
  14: iastore
  15: dup
  16: iconst_3
  17: iconst_4
  18: iastore
  19: dup
  20: iconst_4
  21: iconst_5
  22: iastore
  23: astore_1
  .line 9
  24: iconst_4
  25: istore_2
  .line 10
  26: aload_1
  27: iload_2
  28: iload_2
  29: iastore
  .line 12
  30: aload_1
  31: iconst_3
  32: iaload
  33: istore_2
  .line 13
  34: return
.end method

.method public static main2()V
  .limit stack 7
  .limit locals 2
  .line 17
  0: iconst_2
  1: anewarray [I
  4: dup
  5: iconst_0
  6: iconst_2
  7: newarray int
  9: dup
  10: iconst_0
  11: iconst_1
  12: iastore
  13: dup
  14: iconst_1
  15: iconst_2
  16: iastore
  17: aastore
  18: dup
  19: iconst_1
  20: iconst_2
  21: newarray int
  23: dup
  24: iconst_0
  25: iconst_3
  26: iastore
  27: dup
  28: iconst_1
  29: iconst_4
  30: iastore
  31: aastore
  32: astore_0
  .line 19
  33: aload_0
  34: iconst_0
  35: aaload
  36: iconst_1
  37: aload_0
  38: iconst_2
  39: aaload
  40: iconst_3
  41: iaload
  42: iastore
  .line 20
  43: aload_0
  44: iconst_1
  45: aload_0
  46: iconst_0
  47: aaload
  48: aastore
  .line 22
  49: iconst_2
  50: newarray int
  52: dup
  53: iconst_0
  54: iconst_1
  55: iastore
  56: dup
  57: iconst_1
  58: iconst_2
  59: iastore
  60: astore_1
  .line 23
  61: aload_0
  62: iconst_0
  63: aload_1
  64: aastore
  .line 24
  65: aload_0
  66: iconst_0
  67: aaload
  68: iconst_1
  69: iconst_2
  70: iastore
  .line 25
  71: return
.end method

.method public static main3()V
  .limit stack 3
  .limit locals 0
  .line 28
  0: getstatic Test/x [I
  3: iconst_0
  4: bipush 6
  6: iastore
  .line 30
  7: return
.end method

.method static <clinit>()V
  .limit stack 4
  .limit locals 0
  .line 4
  0: iconst_5
  1: newarray int
  3: dup
  4: iconst_0
  5: iconst_1
  6: iastore
  7: dup
  8: iconst_1
  9: iconst_2
  10: iastore
  11: dup
  12: iconst_2
  13: iconst_3
  14: iastore
  15: dup
  16: iconst_3
  17: iconst_4
  18: iastore
  19: dup
  20: iconst_4
  21: iconst_5
  22: iastore
  23: putstatic Test/x [I
  26: return
.end method

