grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// ============== parser rules ===================

program			: (expression NEWLINE)* ;


expression		: NUMBER_LIT
				| EOF;

// Statements
statement					: declaration_statement
							| assignment_statement 
							| if_statement
							//| for_statement
							//| break_statement
							//| continue_statement
							//| return_statement
							//| function_call_statement
							| block_statement;


declaration_statement		: variable_declaration 
							| function_declaration;

assignment_statement		: IDENTIFIER ASSIGN expression ;


// Variable
variable_declaration		: number_variable_declaration
							| boolean_variable_declaration
							| string_variable_declaration
							| dynamic_variable_declaration;

boolean_variable_declaration: VAR IDENTIFIER ASSIGN boolean_expression ;
number_variable_declaration	: VAR IDENTIFIER ASSIGN NUMBER_LIT ;
string_variable_declaration	: VAR IDENTIFIER ASSIGN STRING_LIT ;
dynamic_variable_declaration: DYNAMIC IDENTIFIER ASSIGN expression ; // TODO Check again

boolean_expression : expression relational_operator expression ;





// ============== lexer rules ===================

// Type Keywords
NUMBER_TYPE  	: 'number' ;
BOOLEAN_TYPE	: 'bool' ;
STRING_TYPE		: 'string' ;
VAR				: 'var' ;
DYNAMIC			: 'dynamic' ;

// Control Keywords
COMMENT			: '##' ~[\n\r\f]* ;
NEWLINE 		: ('\r''\n'|'\n''\r'|'\r'|'\n')+?
{
print("NEWLINE")
self.text = self.text.replace('\r\n', '\n')
};
WHITESPACE		: [ \t\r\n\b\f]+ -> skip ; // skip spaces, tabs, newlines

// Scope
BEGIN			: 'begin' ;
END				: 'end' ;

// Function
FUNC			: 'func' ;
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
ASSIGN		: '<-' ;


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
NOT_EQUAL   		: '!=' ;
LT       		: '<' ;
LE       		: '<=' ;
GT       		: '>' ;
GE       		: '>=' ;

// String Operators
CONCATE    		: '...' ;
STRING_EQUAL   	: '==' ;



// Error
ERROR_CHAR: . 
{
raise ErrorToken(self.text)
};

UNCLOSE_STRING  : '"' (~['"\\] | '\\' ['\\nrtbf] | '\'"' | [\r\n] )* ('"'|EOF)
{
newlineIndex = self.text.find('\r\n') 
raise UncloseString(self.text[1:newlineIndex] if newlineIndex != -1 else self.text[1:]) # if end with \n else end with EOF
};

ILLEGAL_ESCAPE  : '"' (~['"\r\n] | '\\' ['\\nrtbf] | '\'"' )* '\\'~['\\nrtbf]
{
raise IllegalEscape(self.text[1:-1])
};