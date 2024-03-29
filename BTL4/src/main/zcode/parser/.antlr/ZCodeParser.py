# Generated from c:/Users/PC/Downloads/PPL/PPL Assignment/BTL4/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,49,452,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,1,0,3,0,116,8,0,1,0,1,0,
        3,0,120,8,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,128,8,1,1,2,1,2,3,2,132,
        8,2,1,2,1,2,1,2,3,2,137,8,2,1,3,3,3,140,8,3,1,3,1,3,3,3,144,8,3,
        1,4,1,4,3,4,148,8,4,1,4,1,4,1,4,3,4,153,8,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        3,5,176,8,5,1,6,1,6,1,6,1,6,3,6,182,8,6,1,7,1,7,1,8,1,8,1,8,1,8,
        1,8,1,8,1,9,1,9,3,9,194,8,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,202,
        8,10,1,10,1,10,1,10,3,10,207,8,10,3,10,209,8,10,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,3,12,218,8,12,1,13,1,13,1,13,1,13,1,14,1,14,1,
        14,1,14,1,14,3,14,229,8,14,1,15,1,15,3,15,233,8,15,1,15,1,15,1,15,
        1,16,1,16,1,16,1,16,3,16,242,8,16,1,16,1,16,1,16,1,17,3,17,248,8,
        17,1,17,1,17,1,17,1,17,3,17,254,8,17,1,17,1,17,3,17,258,8,17,1,18,
        1,18,3,18,262,8,18,1,19,1,19,1,19,1,19,1,19,3,19,269,8,19,1,20,1,
        20,3,20,273,8,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,
        23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,3,24,292,8,24,1,25,1,25,1,
        25,1,25,1,26,1,26,1,26,3,26,301,8,26,1,27,1,27,1,27,1,27,1,28,1,
        28,1,29,1,29,1,29,3,29,312,8,29,1,29,1,29,1,30,1,30,1,30,3,30,319,
        8,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,3,31,328,8,31,1,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,34,1,34,1,35,1,35,1,36,
        1,36,1,37,1,37,1,37,1,37,1,37,3,37,351,8,37,1,38,1,38,1,38,1,38,
        1,38,3,38,358,8,38,1,39,1,39,1,39,1,39,1,39,1,39,1,39,5,39,367,8,
        39,10,39,12,39,370,9,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,5,40,
        379,8,40,10,40,12,40,382,9,40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,
        5,41,391,8,41,10,41,12,41,394,9,41,1,42,1,42,1,42,3,42,399,8,42,
        1,43,1,43,1,43,3,43,404,8,43,1,44,1,44,1,44,1,44,1,44,3,44,411,8,
        44,1,45,1,45,1,45,1,45,3,45,417,8,45,1,46,1,46,3,46,421,8,46,1,46,
        1,46,1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,48,1,48,3,48,434,8,48,
        1,49,1,49,1,50,1,50,1,51,1,51,1,52,1,52,1,53,1,53,1,54,1,54,1,55,
        1,55,1,56,1,56,1,56,0,3,78,80,82,57,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,
        66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,
        108,110,112,0,6,1,0,1,3,2,0,35,40,42,42,1,0,27,28,1,0,29,31,1,0,
        33,34,2,0,43,43,45,46,446,0,115,1,0,0,0,2,127,1,0,0,0,4,136,1,0,
        0,0,6,139,1,0,0,0,8,152,1,0,0,0,10,175,1,0,0,0,12,181,1,0,0,0,14,
        183,1,0,0,0,16,185,1,0,0,0,18,193,1,0,0,0,20,208,1,0,0,0,22,210,
        1,0,0,0,24,212,1,0,0,0,26,219,1,0,0,0,28,228,1,0,0,0,30,230,1,0,
        0,0,32,237,1,0,0,0,34,257,1,0,0,0,36,259,1,0,0,0,38,268,1,0,0,0,
        40,272,1,0,0,0,42,274,1,0,0,0,44,277,1,0,0,0,46,281,1,0,0,0,48,291,
        1,0,0,0,50,293,1,0,0,0,52,300,1,0,0,0,54,302,1,0,0,0,56,306,1,0,
        0,0,58,308,1,0,0,0,60,315,1,0,0,0,62,327,1,0,0,0,64,329,1,0,0,0,
        66,337,1,0,0,0,68,339,1,0,0,0,70,341,1,0,0,0,72,343,1,0,0,0,74,350,
        1,0,0,0,76,357,1,0,0,0,78,359,1,0,0,0,80,371,1,0,0,0,82,383,1,0,
        0,0,84,398,1,0,0,0,86,403,1,0,0,0,88,410,1,0,0,0,90,416,1,0,0,0,
        92,420,1,0,0,0,94,424,1,0,0,0,96,433,1,0,0,0,98,435,1,0,0,0,100,
        437,1,0,0,0,102,439,1,0,0,0,104,441,1,0,0,0,106,443,1,0,0,0,108,
        445,1,0,0,0,110,447,1,0,0,0,112,449,1,0,0,0,114,116,3,12,6,0,115,
        114,1,0,0,0,115,116,1,0,0,0,116,117,1,0,0,0,117,119,3,2,1,0,118,
        120,3,12,6,0,119,118,1,0,0,0,119,120,1,0,0,0,120,121,1,0,0,0,121,
        122,5,0,0,1,122,1,1,0,0,0,123,124,3,4,2,0,124,125,3,2,1,0,125,128,
        1,0,0,0,126,128,3,4,2,0,127,123,1,0,0,0,127,126,1,0,0,0,128,3,1,
        0,0,0,129,131,3,32,16,0,130,132,3,12,6,0,131,130,1,0,0,0,131,132,
        1,0,0,0,132,137,1,0,0,0,133,134,3,18,9,0,134,135,3,12,6,0,135,137,
        1,0,0,0,136,129,1,0,0,0,136,133,1,0,0,0,137,5,1,0,0,0,138,140,3,
        12,6,0,139,138,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,143,3,
        10,5,0,142,144,3,12,6,0,143,142,1,0,0,0,143,144,1,0,0,0,144,7,1,
        0,0,0,145,148,3,12,6,0,146,148,3,10,5,0,147,145,1,0,0,0,147,146,
        1,0,0,0,148,149,1,0,0,0,149,150,3,8,4,0,150,153,1,0,0,0,151,153,
        1,0,0,0,152,147,1,0,0,0,152,151,1,0,0,0,153,9,1,0,0,0,154,155,3,
        18,9,0,155,156,5,7,0,0,156,176,1,0,0,0,157,176,3,46,23,0,158,159,
        3,58,29,0,159,160,5,7,0,0,160,176,1,0,0,0,161,176,3,64,32,0,162,
        163,3,68,34,0,163,164,5,7,0,0,164,176,1,0,0,0,165,166,3,70,35,0,
        166,167,5,7,0,0,167,176,1,0,0,0,168,176,3,16,8,0,169,170,3,30,15,
        0,170,171,5,7,0,0,171,176,1,0,0,0,172,173,3,36,18,0,173,174,5,7,
        0,0,174,176,1,0,0,0,175,154,1,0,0,0,175,157,1,0,0,0,175,158,1,0,
        0,0,175,161,1,0,0,0,175,162,1,0,0,0,175,165,1,0,0,0,175,168,1,0,
        0,0,175,169,1,0,0,0,175,172,1,0,0,0,176,11,1,0,0,0,177,178,3,14,
        7,0,178,179,3,12,6,0,179,182,1,0,0,0,180,182,3,14,7,0,181,177,1,
        0,0,0,181,180,1,0,0,0,182,13,1,0,0,0,183,184,5,7,0,0,184,15,1,0,
        0,0,185,186,5,9,0,0,186,187,3,12,6,0,187,188,3,8,4,0,188,189,5,10,
        0,0,189,190,3,12,6,0,190,17,1,0,0,0,191,194,3,20,10,0,192,194,3,
        24,12,0,193,191,1,0,0,0,193,192,1,0,0,0,194,19,1,0,0,0,195,196,5,
        4,0,0,196,197,5,44,0,0,197,198,5,21,0,0,198,209,3,72,36,0,199,202,
        3,22,11,0,200,202,5,5,0,0,201,199,1,0,0,0,201,200,1,0,0,0,202,203,
        1,0,0,0,203,206,5,44,0,0,204,205,5,21,0,0,205,207,3,72,36,0,206,
        204,1,0,0,0,206,207,1,0,0,0,207,209,1,0,0,0,208,195,1,0,0,0,208,
        201,1,0,0,0,209,21,1,0,0,0,210,211,7,0,0,0,211,23,1,0,0,0,212,213,
        3,22,11,0,213,214,5,44,0,0,214,217,3,26,13,0,215,216,5,21,0,0,216,
        218,3,72,36,0,217,215,1,0,0,0,217,218,1,0,0,0,218,25,1,0,0,0,219,
        220,5,24,0,0,220,221,3,28,14,0,221,222,5,25,0,0,222,27,1,0,0,0,223,
        224,3,110,55,0,224,225,5,26,0,0,225,226,3,28,14,0,226,229,1,0,0,
        0,227,229,3,110,55,0,228,223,1,0,0,0,228,227,1,0,0,0,229,29,1,0,
        0,0,230,232,5,44,0,0,231,233,3,94,47,0,232,231,1,0,0,0,232,233,1,
        0,0,0,233,234,1,0,0,0,234,235,5,21,0,0,235,236,3,72,36,0,236,31,
        1,0,0,0,237,238,5,11,0,0,238,239,5,44,0,0,239,241,5,22,0,0,240,242,
        3,38,19,0,241,240,1,0,0,0,241,242,1,0,0,0,242,243,1,0,0,0,243,244,
        5,23,0,0,244,245,3,34,17,0,245,33,1,0,0,0,246,248,3,12,6,0,247,246,
        1,0,0,0,247,248,1,0,0,0,248,249,1,0,0,0,249,250,3,36,18,0,250,251,
        5,7,0,0,251,258,1,0,0,0,252,254,3,12,6,0,253,252,1,0,0,0,253,254,
        1,0,0,0,254,255,1,0,0,0,255,258,3,16,8,0,256,258,3,14,7,0,257,247,
        1,0,0,0,257,253,1,0,0,0,257,256,1,0,0,0,258,35,1,0,0,0,259,261,5,
        12,0,0,260,262,3,72,36,0,261,260,1,0,0,0,261,262,1,0,0,0,262,37,
        1,0,0,0,263,264,3,40,20,0,264,265,5,26,0,0,265,266,3,38,19,0,266,
        269,1,0,0,0,267,269,3,40,20,0,268,263,1,0,0,0,268,267,1,0,0,0,269,
        39,1,0,0,0,270,273,3,42,21,0,271,273,3,44,22,0,272,270,1,0,0,0,272,
        271,1,0,0,0,273,41,1,0,0,0,274,275,3,22,11,0,275,276,5,44,0,0,276,
        43,1,0,0,0,277,278,3,22,11,0,278,279,5,44,0,0,279,280,3,26,13,0,
        280,45,1,0,0,0,281,282,5,13,0,0,282,283,3,54,27,0,283,284,3,56,28,
        0,284,285,3,48,24,0,285,286,3,52,26,0,286,47,1,0,0,0,287,288,3,50,
        25,0,288,289,3,48,24,0,289,292,1,0,0,0,290,292,1,0,0,0,291,287,1,
        0,0,0,291,290,1,0,0,0,292,49,1,0,0,0,293,294,5,15,0,0,294,295,3,
        54,27,0,295,296,3,56,28,0,296,51,1,0,0,0,297,298,5,14,0,0,298,301,
        3,56,28,0,299,301,1,0,0,0,300,297,1,0,0,0,300,299,1,0,0,0,301,53,
        1,0,0,0,302,303,5,22,0,0,303,304,3,72,36,0,304,305,5,23,0,0,305,
        55,1,0,0,0,306,307,3,6,3,0,307,57,1,0,0,0,308,309,5,44,0,0,309,311,
        5,22,0,0,310,312,3,62,31,0,311,310,1,0,0,0,311,312,1,0,0,0,312,313,
        1,0,0,0,313,314,5,23,0,0,314,59,1,0,0,0,315,316,5,44,0,0,316,318,
        5,22,0,0,317,319,3,62,31,0,318,317,1,0,0,0,318,319,1,0,0,0,319,320,
        1,0,0,0,320,321,5,23,0,0,321,61,1,0,0,0,322,323,3,72,36,0,323,324,
        5,26,0,0,324,325,3,62,31,0,325,328,1,0,0,0,326,328,3,72,36,0,327,
        322,1,0,0,0,327,326,1,0,0,0,328,63,1,0,0,0,329,330,5,16,0,0,330,
        331,5,44,0,0,331,332,5,17,0,0,332,333,3,72,36,0,333,334,5,18,0,0,
        334,335,3,72,36,0,335,336,3,66,33,0,336,65,1,0,0,0,337,338,3,6,3,
        0,338,67,1,0,0,0,339,340,5,19,0,0,340,69,1,0,0,0,341,342,5,20,0,
        0,342,71,1,0,0,0,343,344,3,74,37,0,344,73,1,0,0,0,345,346,3,76,38,
        0,346,347,5,41,0,0,347,348,3,76,38,0,348,351,1,0,0,0,349,351,3,76,
        38,0,350,345,1,0,0,0,350,349,1,0,0,0,351,75,1,0,0,0,352,353,3,78,
        39,0,353,354,3,98,49,0,354,355,3,78,39,0,355,358,1,0,0,0,356,358,
        3,78,39,0,357,352,1,0,0,0,357,356,1,0,0,0,358,77,1,0,0,0,359,360,
        6,39,-1,0,360,361,3,80,40,0,361,368,1,0,0,0,362,363,10,2,0,0,363,
        364,3,104,52,0,364,365,3,80,40,0,365,367,1,0,0,0,366,362,1,0,0,0,
        367,370,1,0,0,0,368,366,1,0,0,0,368,369,1,0,0,0,369,79,1,0,0,0,370,
        368,1,0,0,0,371,372,6,40,-1,0,372,373,3,82,41,0,373,380,1,0,0,0,
        374,375,10,2,0,0,375,376,3,100,50,0,376,377,3,82,41,0,377,379,1,
        0,0,0,378,374,1,0,0,0,379,382,1,0,0,0,380,378,1,0,0,0,380,381,1,
        0,0,0,381,81,1,0,0,0,382,380,1,0,0,0,383,384,6,41,-1,0,384,385,3,
        84,42,0,385,392,1,0,0,0,386,387,10,2,0,0,387,388,3,102,51,0,388,
        389,3,84,42,0,389,391,1,0,0,0,390,386,1,0,0,0,391,394,1,0,0,0,392,
        390,1,0,0,0,392,393,1,0,0,0,393,83,1,0,0,0,394,392,1,0,0,0,395,396,
        5,32,0,0,396,399,3,84,42,0,397,399,3,86,43,0,398,395,1,0,0,0,398,
        397,1,0,0,0,399,85,1,0,0,0,400,401,5,28,0,0,401,404,3,86,43,0,402,
        404,3,88,44,0,403,400,1,0,0,0,403,402,1,0,0,0,404,87,1,0,0,0,405,
        406,5,22,0,0,406,407,3,72,36,0,407,408,5,23,0,0,408,411,1,0,0,0,
        409,411,3,90,45,0,410,405,1,0,0,0,410,409,1,0,0,0,411,89,1,0,0,0,
        412,417,3,106,53,0,413,417,3,60,30,0,414,417,5,44,0,0,415,417,3,
        92,46,0,416,412,1,0,0,0,416,413,1,0,0,0,416,414,1,0,0,0,416,415,
        1,0,0,0,417,91,1,0,0,0,418,421,3,60,30,0,419,421,5,44,0,0,420,418,
        1,0,0,0,420,419,1,0,0,0,420,421,1,0,0,0,421,422,1,0,0,0,422,423,
        3,94,47,0,423,93,1,0,0,0,424,425,5,24,0,0,425,426,3,96,48,0,426,
        427,5,25,0,0,427,95,1,0,0,0,428,429,3,72,36,0,429,430,5,26,0,0,430,
        431,3,96,48,0,431,434,1,0,0,0,432,434,3,72,36,0,433,428,1,0,0,0,
        433,432,1,0,0,0,434,97,1,0,0,0,435,436,7,1,0,0,436,99,1,0,0,0,437,
        438,7,2,0,0,438,101,1,0,0,0,439,440,7,3,0,0,440,103,1,0,0,0,441,
        442,7,4,0,0,442,105,1,0,0,0,443,444,7,5,0,0,444,107,1,0,0,0,445,
        446,5,46,0,0,446,109,1,0,0,0,447,448,5,45,0,0,448,111,1,0,0,0,449,
        450,5,43,0,0,450,113,1,0,0,0,41,115,119,127,131,136,139,143,147,
        152,175,181,193,201,206,208,217,228,232,241,247,253,257,261,268,
        272,291,300,311,318,327,350,357,368,380,392,398,403,410,416,420,
        433
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'number'", "'bool'", "'string'", "'var'", 
                     "'dynamic'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'begin'", "'end'", "'func'", "'return'", "'if'", "'else'", 
                     "'elif'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'<-'", "'('", "')'", "'['", "']'", "','", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", "'='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'...'", "'=='" ]

    symbolicNames = [ "<INVALID>", "NUMBER_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", 
                      "VAR", "DYNAMIC", "COMMENT", "NEWLINE", "WHITESPACE", 
                      "BEGIN", "END", "FUNC", "RETURN", "IF", "ELSE", "ELIF", 
                      "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "ASSIGN", 
                      "LPAREN", "RPAREN", "LBRACK", "RBRACK", "COMMA", "PLUS", 
                      "MINUS", "MULTIPLY", "DIVIDE", "MOD", "NOT", "AND", 
                      "OR", "EQUAL", "NOT_EQUAL", "LT", "LE", "GT", "GE", 
                      "CONCATE", "STRING_EQUAL", "BOOLEAN_LIT", "IDENTIFIER", 
                      "NUMBER_LIT", "STRING_LIT", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declaration_list = 1
    RULE_declaration = 2
    RULE_local_statement_single = 3
    RULE_local_statement_list = 4
    RULE_local_statement = 5
    RULE_newline_list = 6
    RULE_newline = 7
    RULE_block_statement = 8
    RULE_variable_declaration_statement = 9
    RULE_basic_variable_declaration = 10
    RULE_basic_type = 11
    RULE_array_declaration = 12
    RULE_array_dimension = 13
    RULE_array_dimension_list = 14
    RULE_assignment_statement = 15
    RULE_function_declaration = 16
    RULE_function_body = 17
    RULE_return_statement = 18
    RULE_parameter_part_recursive = 19
    RULE_parameter_declaration = 20
    RULE_basic_parameter_declaration = 21
    RULE_array_parameter_declaration = 22
    RULE_if_statement = 23
    RULE_elif_recursive_statement = 24
    RULE_elif_statement = 25
    RULE_else_statement = 26
    RULE_branch_condition = 27
    RULE_branch_body = 28
    RULE_function_call_statement = 29
    RULE_function_call_expression = 30
    RULE_argument_part = 31
    RULE_for_statement = 32
    RULE_loop_body = 33
    RULE_break_statement = 34
    RULE_continue_statement = 35
    RULE_expression = 36
    RULE_string_expression = 37
    RULE_relational_expression = 38
    RULE_logical_expression = 39
    RULE_adding_expression = 40
    RULE_multiplying_expression = 41
    RULE_negation_expression = 42
    RULE_sign_expression = 43
    RULE_parenthesis_expression = 44
    RULE_operand = 45
    RULE_array_literal = 46
    RULE_element_expression = 47
    RULE_index_operator = 48
    RULE_relational_operator = 49
    RULE_additive_operator = 50
    RULE_multiplicative_operator = 51
    RULE_logic_operator = 52
    RULE_literal = 53
    RULE_string_literal = 54
    RULE_number_literal = 55
    RULE_boolean_literal = 56

    ruleNames =  [ "program", "declaration_list", "declaration", "local_statement_single", 
                   "local_statement_list", "local_statement", "newline_list", 
                   "newline", "block_statement", "variable_declaration_statement", 
                   "basic_variable_declaration", "basic_type", "array_declaration", 
                   "array_dimension", "array_dimension_list", "assignment_statement", 
                   "function_declaration", "function_body", "return_statement", 
                   "parameter_part_recursive", "parameter_declaration", 
                   "basic_parameter_declaration", "array_parameter_declaration", 
                   "if_statement", "elif_recursive_statement", "elif_statement", 
                   "else_statement", "branch_condition", "branch_body", 
                   "function_call_statement", "function_call_expression", 
                   "argument_part", "for_statement", "loop_body", "break_statement", 
                   "continue_statement", "expression", "string_expression", 
                   "relational_expression", "logical_expression", "adding_expression", 
                   "multiplying_expression", "negation_expression", "sign_expression", 
                   "parenthesis_expression", "operand", "array_literal", 
                   "element_expression", "index_operator", "relational_operator", 
                   "additive_operator", "multiplicative_operator", "logic_operator", 
                   "literal", "string_literal", "number_literal", "boolean_literal" ]

    EOF = Token.EOF
    NUMBER_TYPE=1
    BOOLEAN_TYPE=2
    STRING_TYPE=3
    VAR=4
    DYNAMIC=5
    COMMENT=6
    NEWLINE=7
    WHITESPACE=8
    BEGIN=9
    END=10
    FUNC=11
    RETURN=12
    IF=13
    ELSE=14
    ELIF=15
    FOR=16
    UNTIL=17
    BY=18
    BREAK=19
    CONTINUE=20
    ASSIGN=21
    LPAREN=22
    RPAREN=23
    LBRACK=24
    RBRACK=25
    COMMA=26
    PLUS=27
    MINUS=28
    MULTIPLY=29
    DIVIDE=30
    MOD=31
    NOT=32
    AND=33
    OR=34
    EQUAL=35
    NOT_EQUAL=36
    LT=37
    LE=38
    GT=39
    GE=40
    CONCATE=41
    STRING_EQUAL=42
    BOOLEAN_LIT=43
    IDENTIFIER=44
    NUMBER_LIT=45
    STRING_LIT=46
    ERROR_CHAR=47
    UNCLOSE_STRING=48
    ILLEGAL_ESCAPE=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 114
                self.newline_list()


            self.state = 117
            self.declaration_list()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 118
                self.newline_list()


            self.state = 121
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationContext,0)


        def declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration_list" ):
                listener.enterDeclaration_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration_list" ):
                listener.exitDeclaration_list(self)




    def declaration_list(self):

        localctx = ZCodeParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration_list)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.declaration()
                self.state = 124
                self.declaration_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Function_declarationContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def variable_declaration_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declaration_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.function_declaration()
                self.state = 131
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 130
                    self.newline_list()


                pass
            elif token in [1, 2, 3, 4, 5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.variable_declaration_statement()
                self.state = 134
                self.newline_list()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_statement_singleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statementContext,0)


        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_local_statement_single

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_statement_single" ):
                listener.enterLocal_statement_single(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_statement_single" ):
                listener.exitLocal_statement_single(self)




    def local_statement_single(self):

        localctx = ZCodeParser.Local_statement_singleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_local_statement_single)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 138
                self.newline_list()


            self.state = 141
            self.local_statement()
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 142
                self.newline_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statement_listContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def local_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_local_statement_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_statement_list" ):
                listener.enterLocal_statement_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_statement_list" ):
                listener.exitLocal_statement_list(self)




    def local_statement_list(self):

        localctx = ZCodeParser.Local_statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_local_statement_list)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 7, 9, 12, 13, 16, 19, 20, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7]:
                    self.state = 145
                    self.newline_list()
                    pass
                elif token in [1, 2, 3, 4, 5, 9, 12, 13, 16, 19, 20, 44]:
                    self.state = 146
                    self.local_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 149
                self.local_statement_list()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Local_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declaration_statementContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def function_call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_local_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocal_statement" ):
                listener.enterLocal_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocal_statement" ):
                listener.exitLocal_statement(self)




    def local_statement(self):

        localctx = ZCodeParser.Local_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_local_statement)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.variable_declaration_statement()
                self.state = 155
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.function_call_statement()
                self.state = 159
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 162
                self.break_statement()
                self.state = 163
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 165
                self.continue_statement()
                self.state = 166
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 168
                self.block_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 169
                self.assignment_statement()
                self.state = 170
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 172
                self.return_statement()
                self.state = 173
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewline_list" ):
                listener.enterNewline_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewline_list" ):
                listener.exitNewline_list(self)




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_newline_list)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.newline()
                self.state = 178
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.newline()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_newline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewline" ):
                listener.enterNewline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewline" ):
                listener.exitNewline(self)




    def newline(self):

        localctx = ZCodeParser.NewlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(ZCodeParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def local_statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statement_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_statement" ):
                listener.enterBlock_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_statement" ):
                listener.exitBlock_statement(self)




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(ZCodeParser.BEGIN)
            self.state = 186
            self.newline_list()
            self.state = 187
            self.local_statement_list()
            self.state = 188
            self.match(ZCodeParser.END)
            self.state = 189
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declaration_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_variable_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Basic_variable_declarationContext,0)


        def array_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Array_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_declaration_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration_statement" ):
                listener.enterVariable_declaration_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration_statement" ):
                listener.exitVariable_declaration_statement(self)




    def variable_declaration_statement(self):

        localctx = ZCodeParser.Variable_declaration_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_variable_declaration_statement)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.basic_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.array_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def basic_type(self):
            return self.getTypedRuleContext(ZCodeParser.Basic_typeContext,0)


        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_basic_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasic_variable_declaration" ):
                listener.enterBasic_variable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasic_variable_declaration" ):
                listener.exitBasic_variable_declaration(self)




    def basic_variable_declaration(self):

        localctx = ZCodeParser.Basic_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_basic_variable_declaration)
        self._la = 0 # Token type
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(ZCodeParser.VAR)
                self.state = 196
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 197
                self.match(ZCodeParser.ASSIGN)
                self.state = 198
                self.expression()
                pass
            elif token in [1, 2, 3, 5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3]:
                    self.state = 199
                    self.basic_type()
                    pass
                elif token in [5]:
                    self.state = 200
                    self.match(ZCodeParser.DYNAMIC)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 203
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 204
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 205
                    self.expression()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_TYPE(self):
            return self.getToken(ZCodeParser.NUMBER_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(ZCodeParser.STRING_TYPE, 0)

        def BOOLEAN_TYPE(self):
            return self.getToken(ZCodeParser.BOOLEAN_TYPE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_basic_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasic_type" ):
                listener.enterBasic_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasic_type" ):
                listener.exitBasic_type(self)




    def basic_type(self):

        localctx = ZCodeParser.Basic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_basic_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_type(self):
            return self.getTypedRuleContext(ZCodeParser.Basic_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_dimension(self):
            return self.getTypedRuleContext(ZCodeParser.Array_dimensionContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_declaration" ):
                listener.enterArray_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_declaration" ):
                listener.exitArray_declaration(self)




    def array_declaration(self):

        localctx = ZCodeParser.Array_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.basic_type()
            self.state = 213
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 214
            self.array_dimension()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 215
                self.match(ZCodeParser.ASSIGN)
                self.state = 216
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_dimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def array_dimension_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_dimension_listContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_dimension

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_dimension" ):
                listener.enterArray_dimension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_dimension" ):
                listener.exitArray_dimension(self)




    def array_dimension(self):

        localctx = ZCodeParser.Array_dimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_array_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(ZCodeParser.LBRACK)
            self.state = 220
            self.array_dimension_list()
            self.state = 221
            self.match(ZCodeParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_dimension_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Number_literalContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def array_dimension_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_dimension_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_dimension_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_dimension_list" ):
                listener.enterArray_dimension_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_dimension_list" ):
                listener.exitArray_dimension_list(self)




    def array_dimension_list(self):

        localctx = ZCodeParser.Array_dimension_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_dimension_list)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.number_literal()
                self.state = 224
                self.match(ZCodeParser.COMMA)
                self.state = 225
                self.array_dimension_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.number_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def element_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Element_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_statement" ):
                listener.enterAssignment_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_statement" ):
                listener.exitAssignment_statement(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assignment_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 231
                self.element_expression()


            self.state = 234
            self.match(ZCodeParser.ASSIGN)
            self.state = 235
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def function_body(self):
            return self.getTypedRuleContext(ZCodeParser.Function_bodyContext,0)


        def parameter_part_recursive(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_part_recursiveContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declaration" ):
                listener.enterFunction_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declaration" ):
                listener.exitFunction_declaration(self)




    def function_declaration(self):

        localctx = ZCodeParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(ZCodeParser.FUNC)
            self.state = 238
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 239
            self.match(ZCodeParser.LPAREN)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
                self.state = 240
                self.parameter_part_recursive()


            self.state = 243
            self.match(ZCodeParser.RPAREN)
            self.state = 244
            self.function_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def newline(self):
            return self.getTypedRuleContext(ZCodeParser.NewlineContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_body" ):
                listener.enterFunction_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_body" ):
                listener.exitFunction_body(self)




    def function_body(self):

        localctx = ZCodeParser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_function_body)
        self._la = 0 # Token type
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 246
                    self.newline_list()


                self.state = 249
                self.return_statement()
                self.state = 250
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 252
                    self.newline_list()


                self.state = 255
                self.block_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 256
                self.newline()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(ZCodeParser.RETURN)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 131945979707392) != 0):
                self.state = 260
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_part_recursiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_declarationContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def parameter_part_recursive(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_part_recursiveContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_part_recursive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_part_recursive" ):
                listener.enterParameter_part_recursive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_part_recursive" ):
                listener.exitParameter_part_recursive(self)




    def parameter_part_recursive(self):

        localctx = ZCodeParser.Parameter_part_recursiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parameter_part_recursive)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.parameter_declaration()
                self.state = 264
                self.match(ZCodeParser.COMMA)
                self.state = 265
                self.parameter_part_recursive()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.parameter_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_parameter_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Basic_parameter_declarationContext,0)


        def array_parameter_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Array_parameter_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_declaration" ):
                listener.enterParameter_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_declaration" ):
                listener.exitParameter_declaration(self)




    def parameter_declaration(self):

        localctx = ZCodeParser.Parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_parameter_declaration)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.basic_parameter_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.array_parameter_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_parameter_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_type(self):
            return self.getTypedRuleContext(ZCodeParser.Basic_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_basic_parameter_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasic_parameter_declaration" ):
                listener.enterBasic_parameter_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasic_parameter_declaration" ):
                listener.exitBasic_parameter_declaration(self)




    def basic_parameter_declaration(self):

        localctx = ZCodeParser.Basic_parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_basic_parameter_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.basic_type()
            self.state = 275
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_parameter_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_type(self):
            return self.getTypedRuleContext(ZCodeParser.Basic_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_dimension(self):
            return self.getTypedRuleContext(ZCodeParser.Array_dimensionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_parameter_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_parameter_declaration" ):
                listener.enterArray_parameter_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_parameter_declaration" ):
                listener.exitArray_parameter_declaration(self)




    def array_parameter_declaration(self):

        localctx = ZCodeParser.Array_parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_array_parameter_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.basic_type()
            self.state = 278
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 279
            self.array_dimension()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def branch_condition(self):
            return self.getTypedRuleContext(ZCodeParser.Branch_conditionContext,0)


        def branch_body(self):
            return self.getTypedRuleContext(ZCodeParser.Branch_bodyContext,0)


        def elif_recursive_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_recursive_statementContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Else_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(ZCodeParser.IF)
            self.state = 282
            self.branch_condition()
            self.state = 283
            self.branch_body()
            self.state = 284
            self.elif_recursive_statement()
            self.state = 285
            self.else_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_recursive_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_statementContext,0)


        def elif_recursive_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_recursive_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_recursive_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_recursive_statement" ):
                listener.enterElif_recursive_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_recursive_statement" ):
                listener.exitElif_recursive_statement(self)




    def elif_recursive_statement(self):

        localctx = ZCodeParser.Elif_recursive_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elif_recursive_statement)
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.elif_statement()
                self.state = 288
                self.elif_recursive_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def branch_condition(self):
            return self.getTypedRuleContext(ZCodeParser.Branch_conditionContext,0)


        def branch_body(self):
            return self.getTypedRuleContext(ZCodeParser.Branch_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_statement" ):
                listener.enterElif_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_statement" ):
                listener.exitElif_statement(self)




    def elif_statement(self):

        localctx = ZCodeParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(ZCodeParser.ELIF)
            self.state = 294
            self.branch_condition()
            self.state = 295
            self.branch_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def branch_body(self):
            return self.getTypedRuleContext(ZCodeParser.Branch_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_statement" ):
                listener.enterElse_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_statement" ):
                listener.exitElse_statement(self)




    def else_statement(self):

        localctx = ZCodeParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_else_statement)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.match(ZCodeParser.ELSE)
                self.state = 298
                self.branch_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Branch_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_branch_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBranch_condition" ):
                listener.enterBranch_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBranch_condition" ):
                listener.exitBranch_condition(self)




    def branch_condition(self):

        localctx = ZCodeParser.Branch_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_branch_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(ZCodeParser.LPAREN)
            self.state = 303
            self.expression()
            self.state = 304
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Branch_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_statement_single(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statement_singleContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_branch_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBranch_body" ):
                listener.enterBranch_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBranch_body" ):
                listener.exitBranch_body(self)




    def branch_body(self):

        localctx = ZCodeParser.Branch_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_branch_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.local_statement_single()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def argument_part(self):
            return self.getTypedRuleContext(ZCodeParser.Argument_partContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_statement" ):
                listener.enterFunction_call_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_statement" ):
                listener.exitFunction_call_statement(self)




    def function_call_statement(self):

        localctx = ZCodeParser.Function_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_function_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 309
            self.match(ZCodeParser.LPAREN)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 131945979707392) != 0):
                self.state = 310
                self.argument_part()


            self.state = 313
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def argument_part(self):
            return self.getTypedRuleContext(ZCodeParser.Argument_partContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call_expression" ):
                listener.enterFunction_call_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call_expression" ):
                listener.exitFunction_call_expression(self)




    def function_call_expression(self):

        localctx = ZCodeParser.Function_call_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_function_call_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 316
            self.match(ZCodeParser.LPAREN)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 131945979707392) != 0):
                self.state = 317
                self.argument_part()


            self.state = 320
            self.match(ZCodeParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def argument_part(self):
            return self.getTypedRuleContext(ZCodeParser.Argument_partContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argument_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument_part" ):
                listener.enterArgument_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument_part" ):
                listener.exitArgument_part(self)




    def argument_part(self):

        localctx = ZCodeParser.Argument_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_argument_part)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.expression()
                self.state = 323
                self.match(ZCodeParser.COMMA)
                self.state = 324
                self.argument_part()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def loop_body(self):
            return self.getTypedRuleContext(ZCodeParser.Loop_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_statement" ):
                listener.enterFor_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_statement" ):
                listener.exitFor_statement(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(ZCodeParser.FOR)
            self.state = 330
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 331
            self.match(ZCodeParser.UNTIL)
            self.state = 332
            self.expression()
            self.state = 333
            self.match(ZCodeParser.BY)
            self.state = 334
            self.expression()
            self.state = 335
            self.loop_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def local_statement_single(self):
            return self.getTypedRuleContext(ZCodeParser.Local_statement_singleContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_loop_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_body" ):
                listener.enterLoop_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_body" ):
                listener.exitLoop_body(self)




    def loop_body(self):

        localctx = ZCodeParser.Loop_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_loop_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.local_statement_single()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_statement" ):
                listener.enterBreak_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_statement" ):
                listener.exitBreak_statement(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue_statement" ):
                listener.enterContinue_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue_statement" ):
                listener.exitContinue_statement(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_expression(self):
            return self.getTypedRuleContext(ZCodeParser.String_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.string_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Relational_expressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Relational_expressionContext,i)


        def CONCATE(self):
            return self.getToken(ZCodeParser.CONCATE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_string_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_expression" ):
                listener.enterString_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_expression" ):
                listener.exitString_expression(self)




    def string_expression(self):

        localctx = ZCodeParser.String_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_string_expression)
        try:
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.relational_expression()
                self.state = 346
                self.match(ZCodeParser.CONCATE)
                self.state = 347
                self.relational_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.relational_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Logical_expressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Logical_expressionContext,i)


        def relational_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Relational_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_relational_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational_expression" ):
                listener.enterRelational_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational_expression" ):
                listener.exitRelational_expression(self)




    def relational_expression(self):

        localctx = ZCodeParser.Relational_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_relational_expression)
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.logical_expression(0)
                self.state = 353
                self.relational_operator()
                self.state = 354
                self.logical_expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.logical_expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Adding_expressionContext,0)


        def logical_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Logical_expressionContext,0)


        def logic_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Logic_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_logical_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_expression" ):
                listener.enterLogical_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_expression" ):
                listener.exitLogical_expression(self)



    def logical_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Logical_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_logical_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.adding_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logical_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                    self.state = 362
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 363
                    self.logic_operator()
                    self.state = 364
                    self.adding_expression(0) 
                self.state = 370
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Adding_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Multiplying_expressionContext,0)


        def adding_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Adding_expressionContext,0)


        def additive_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Additive_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_adding_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdding_expression" ):
                listener.enterAdding_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdding_expression" ):
                listener.exitAdding_expression(self)



    def adding_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Adding_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_adding_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.multiplying_expression(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 380
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Adding_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expression)
                    self.state = 374
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 375
                    self.additive_operator()
                    self.state = 376
                    self.multiplying_expression(0) 
                self.state = 382
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def negation_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Negation_expressionContext,0)


        def multiplying_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Multiplying_expressionContext,0)


        def multiplicative_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Multiplicative_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_multiplying_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplying_expression" ):
                listener.enterMultiplying_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplying_expression" ):
                listener.exitMultiplying_expression(self)



    def multiplying_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Multiplying_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_multiplying_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.negation_expression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 392
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Multiplying_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expression)
                    self.state = 386
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 387
                    self.multiplicative_operator()
                    self.state = 388
                    self.negation_expression() 
                self.state = 394
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Negation_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def negation_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Negation_expressionContext,0)


        def sign_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_negation_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegation_expression" ):
                listener.enterNegation_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegation_expression" ):
                listener.exitNegation_expression(self)




    def negation_expression(self):

        localctx = ZCodeParser.Negation_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_negation_expression)
        try:
            self.state = 398
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.match(ZCodeParser.NOT)
                self.state = 396
                self.negation_expression()
                pass
            elif token in [22, 24, 28, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.sign_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def sign_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_expressionContext,0)


        def parenthesis_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Parenthesis_expressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSign_expression" ):
                listener.enterSign_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSign_expression" ):
                listener.exitSign_expression(self)




    def sign_expression(self):

        localctx = ZCodeParser.Sign_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_sign_expression)
        try:
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.match(ZCodeParser.MINUS)
                self.state = 401
                self.sign_expression()
                pass
            elif token in [22, 24, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.parenthesis_expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parenthesis_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ZCodeParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ZCodeParser.RPAREN, 0)

        def operand(self):
            return self.getTypedRuleContext(ZCodeParser.OperandContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parenthesis_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesis_expression" ):
                listener.enterParenthesis_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesis_expression" ):
                listener.exitParenthesis_expression(self)




    def parenthesis_expression(self):

        localctx = ZCodeParser.Parenthesis_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_parenthesis_expression)
        try:
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.match(ZCodeParser.LPAREN)
                self.state = 406
                self.expression()
                self.state = 407
                self.match(ZCodeParser.RPAREN)
                pass
            elif token in [24, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def function_call_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_expressionContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)




    def operand(self):

        localctx = ZCodeParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_operand)
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.function_call_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 415
                self.array_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Element_expressionContext,0)


        def function_call_expression(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_expressionContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_literal" ):
                listener.enterArray_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_literal" ):
                listener.exitArray_literal(self)




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 418
                self.function_call_expression()

            elif la_ == 2:
                self.state = 419
                self.match(ZCodeParser.IDENTIFIER)


            self.state = 422
            self.element_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(ZCodeParser.LBRACK, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def RBRACK(self):
            return self.getToken(ZCodeParser.RBRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_element_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement_expression" ):
                listener.enterElement_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement_expression" ):
                listener.exitElement_expression(self)




    def element_expression(self):

        localctx = ZCodeParser.Element_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_element_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(ZCodeParser.LBRACK)
            self.state = 425
            self.index_operator()
            self.state = 426
            self.match(ZCodeParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_operator(self):
            return self.getTypedRuleContext(ZCodeParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex_operator" ):
                listener.enterIndex_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex_operator" ):
                listener.exitIndex_operator(self)




    def index_operator(self):

        localctx = ZCodeParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_index_operator)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.expression()
                self.state = 429
                self.match(ZCodeParser.COMMA)
                self.state = 430
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def LE(self):
            return self.getToken(ZCodeParser.LE, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def GE(self):
            return self.getToken(ZCodeParser.GE, 0)

        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def STRING_EQUAL(self):
            return self.getToken(ZCodeParser.STRING_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relational_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational_operator" ):
                listener.enterRelational_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational_operator" ):
                listener.exitRelational_operator(self)




    def relational_operator(self):

        localctx = ZCodeParser.Relational_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_relational_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6562710028288) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Additive_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_additive_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive_operator" ):
                listener.enterAdditive_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive_operator" ):
                listener.exitAdditive_operator(self)




    def additive_operator(self):

        localctx = ZCodeParser.Additive_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_additive_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiplicative_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTIPLY(self):
            return self.getToken(ZCodeParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(ZCodeParser.DIVIDE, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_multiplicative_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative_operator" ):
                listener.enterMultiplicative_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative_operator" ):
                listener.exitMultiplicative_operator(self)




    def multiplicative_operator(self):

        localctx = ZCodeParser.Multiplicative_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_multiplicative_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3758096384) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logic_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_operator" ):
                listener.enterLogic_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_operator" ):
                listener.exitLogic_operator(self)




    def logic_operator(self):

        localctx = ZCodeParser.Logic_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_logic_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            _la = self._input.LA(1)
            if not(_la==33 or _la==34):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(ZCodeParser.BOOLEAN_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114349209288704) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_string_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_literal" ):
                listener.enterString_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_literal" ):
                listener.exitString_literal(self)




    def string_literal(self):

        localctx = ZCodeParser.String_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(ZCodeParser.STRING_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(ZCodeParser.NUMBER_LIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_number_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber_literal" ):
                listener.enterNumber_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber_literal" ):
                listener.exitNumber_literal(self)




    def number_literal(self):

        localctx = ZCodeParser.Number_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_number_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.match(ZCodeParser.NUMBER_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN_LIT(self):
            return self.getToken(ZCodeParser.BOOLEAN_LIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_boolean_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_literal" ):
                listener.enterBoolean_literal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_literal" ):
                listener.exitBoolean_literal(self)




    def boolean_literal(self):

        localctx = ZCodeParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_boolean_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(ZCodeParser.BOOLEAN_LIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[39] = self.logical_expression_sempred
        self._predicates[40] = self.adding_expression_sempred
        self._predicates[41] = self.multiplying_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def adding_expression_sempred(self, localctx:Adding_expressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expression_sempred(self, localctx:Multiplying_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




