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

// Expression
boolean_expression : expression relational_operator expression ;

// Function
function_declaration        : FUNC IDENTIFIER LPAREN (variable_declaration (COMMA variable_declaration)*)? RPAREN ;


// scope
block_statement				: BEGIN (statement NEWLINE)* END ;


if_statement 				: IF expression relational_operator expression RETURN boolean_value ;


boolean_value 				: TRUE | FALSE ;

// Expression : based on the precedence and associativity



string_expression 			: string_expression CONCATE string_expression // Binary Infix None Associative
							| string_expression;

relational_expression		: logical_expression relational_operator logical_expression // Binary Infix None Associative
							| logical_expression;

logical_expression			: logical_expression logic_operator adding_expression // Binary Infix Left Associative
							| adding_expression;

adding_expression			: adding_expression additive_operator multiplying_expression // Binary Infix Left Associative
							| multiplying_expression;

multiplying_expression		: multiplying_expression multiplicative_operator sign_expression // Binary Infix Left Associative
							| sign_expression; 

negation_expression			: NOT negation_expression // Unary Prefix Right Associative
							| string_expression;

sign_expression				: additive_operator sign_expression; // Unary Prefix Right Associative
							//| ;// Index??


// TODO index operator
index_expression			: ;

// Expression operator
relational_operator 		: LT | LE | GT | GE | EQUAL | NOT_EQUAL | STRING_EQUAL;
additive_operator 			: PLUS | MINUS ;
multiplicative_operator		: MULTIPLY | DIVIDE | MOD ;
logic_operator 				: AND | OR ;




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