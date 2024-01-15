grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// ============== parser rules ===================

program			: (expression NEWLINE)* ;

function        : IDENTIFIER LPAREN (expression (COMMA expression)*)? RPAREN ;

expression		: NUMBER_LIT
				| EOF;

boolean_expression : expression relational_operator expression ;

if_statement : IF expression relational_operator expression RETURN boolean_value ;

relational_operator : LT | LE | GT | GE | EQUAL | NEQUAL ;

boolean_value : TRUE | FALSE ;


// ============== lexer rules ===================

// Type Keywords
NUMBER_TYPE  	: 'number' ;
BOOLEAN_TYPE	: 'bool' ;
STRING_TYPE		: 'string' ;
VAR				: 'var' ;
DYNAMIC			: 'dynamic' ;

// Control Keywords
COMMENT			: '##' ~[\n\r\f]* ;
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
IDENTIFIER		: [a-zA-Z_] [a-z0-9A-Z_]*;

NUMBER_LIT     	: NUMBER_INTERGER NUMBER_DECIMAL? NUMBER_EXPONENT? ;
fragment NUMBER_INTERGER 	: [0-9]+ ;
fragment NUMBER_DECIMAL 	: '.'[0-9]* ;
fragment NUMBER_EXPONENT 	: [eE][+-]?[0-9]+ ;

TRUE      		: 'true' ;
FALSE     		: 'false' ;

//Normal regex:  "([^\'\"\r\n\\]|\\['\\nrtbf]|'")*"
STRING_LIT 			: '"' (~['"\r\n\\] | '\\' ['\\nrtbf] | '\'"')* '"' {self.text = self.text[1:-1];};

// Assignment
ASSIGNMENT		: '<-' ;


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

UNCLOSE_STRING  : '"' (~['"\r\n\\] | '\\' ['\\nrtbf] | '\'"')* (EOF | NEWLINE) 
{
	raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE  : '"' (~['"\r\n\\] | '\\' ~['\\nrtbf] | '\'"')* 
{
	raise IllegalEscape(self.text[1:])
};