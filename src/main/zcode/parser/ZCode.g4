grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program			: (EXPRESSION NEWLINE)* ;

EXPRESSION		: NUMBER;

COMMENT			: '##'.*? ;
NEWLINE 		: [\r\n]+ ;

NUMBER     		: [0-9]+'.'?[0-9]*([eE][+-]?[0-9]+)? ;
BOOLEAN			: 'true'|'false' ;

IDENTIFIER		: [a-z] [a-z0-9]*;

LPAREN			: '(' ;
RPAREN  	 	: ')' ;
LBRACK  	 	: '[' ;
RBRACK		   	: ']' ;
COMMA   		: ',' ;

PLUS     		: '+' ;
MINUS    		: '-' ;
MULTIPLY 		: '*' ;
DIVIDE   		: '/' ;
MOD      		: '%' ;

NOT      		: 'not' ;
AND      		: 'and' ;
OR       		: 'or' ;

EQUAL    		: '=' ;
ASSIGN   		: '<-' ;
NEQUAL   		: '!=' ;
LT       		: '<' ;
LE       		: '<=' ;
GT       		: '>' ;
GE       		: '>=' ;

CONCATE    		: '...' ;
STRING_EQUAL   	: '==' ;





STRING: '"' ( ~[\r\n"] | '\\' . )* '"' {
    // Custom code to handle the string token
    // You can access the matched text with getText() method
};

// Error rule for newline within a string
STRING_NEWLINE_ERROR: '"' ( ~['"\r\n] | '\\' . )* '\r'? '\n' {
    // Custom code to handle the error
    // You can print an error message or throw an exception
    throw new RuntimeException("Newline character found within a string");
};

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;