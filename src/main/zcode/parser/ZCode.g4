grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// parser rules

program			: (EXPRESSION NEWLINE)* ;

EXPRESSION		: NUMBER
				| ERROR_CHAR;


FUNCTION        : IDENTIFIER LPAREN (EXPRESSION (COMMA EXPRESSION)*)? RPAREN ;


// ============== lexer rules ===================

// Type Keywords
NUMBER_TYPE  	: 'number' ;
BOOLEAN_TYPE	: 'bool' ;
STRING_TYPE		: 'string' ;
VAR				: 'var' ;
DYNAMIC			: 'dynamic' ;

// Control Keywords
COMMENT			: '##'.*? ;
NEWLINE 		: [\r\n]+ ;
WHITESPACE		: [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

BEGIN			: 'begin' ;
END				: 'end' ;
RETURN			: 'return' ;

// If-Else
IF				: 'if' ;
ELSE			: 'else' ;
ELIF			: 'elif' ;

// Loop
FOR				: 'for' ;
UNTIL			: 'until' ;
BY				: 'by' ;
BREAK			: 'break' ;
CONTINUE		: 'continue' ;


// Literal
IDENTIFIER		: [a-z] [a-z0-9]*;
NUMBER     		: [0-9]+'.'?[0-9]*([eE][+-]?[0-9]+)? ;

TRUE      		: 'true' ;
FALSE     		: 'false' ;

//Normal regex:  "([^\'\"\r\n\\]|\\['\\nrtbf]|'")*"
STRING : '"' (~['"\r\n\\] | '\\' ['\\nrtbf] | '\'"')* '"' ;

// Punctuation
LPAREN			: '(' ;
RPAREN  	 	: ')' ;
LBRACK  	 	: '[' ;
RBRACK		   	: ']' ;
COMMA   		: ',' ;

// Arithmetic Operators
PLUS     		: '+' ;
MINUS    		: '-' ;
MULTIPLY 		: '*' ;
DIVIDE   		: '/' ;
MOD      		: '%' ;

// Logic Operators
NOT      		: 'not' ;
AND      		: 'and' ;
OR       		: 'or' ;

// Relational Operators
EQUAL    		: '=' ;
ASSIGN   		: '<-' ;
NEQUAL   		: '!=' ;
LT       		: '<' ;
LE       		: '<=' ;
GT       		: '>' ;
GE       		: '>=' ;

// String Operators
CONCATE    		: '...' ;
STRING_EQUAL   	: '==' ;



// Error
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;