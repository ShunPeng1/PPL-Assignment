grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// ============== parser rules ===================

program						: (global_statement | empty_statement)* ;
							
// Statements
global_statement			: variable_declaration_statement
							| function_declaration_statement;

empty_statement				: NEWLINE;

local_statement				: variable_declaration_statement
							| assignment_statement 
							| if_statement
							//| for_statement
							//| break_statement
							//| continue_statement
							//| return_statement
							//| function_call_statement
							| block_statement;


assignment_statement		: IDENTIFIER ASSIGN expression ;


// Variable
variable_declaration_statement	: number_variable_declaration
								| boolean_variable_declaration
								| string_variable_declaration
								| dynamic_variable_declaration;

boolean_variable_declaration: VAR IDENTIFIER ASSIGN BOOLEAN_LIT ;
number_variable_declaration	: VAR IDENTIFIER ASSIGN NUMBER_LIT ;
string_variable_declaration	: VAR IDENTIFIER ASSIGN STRING_LIT ;
dynamic_variable_declaration: DYNAMIC IDENTIFIER ASSIGN expression ; // TODO Check again



// Function
function_declaration_statement	: FUNC IDENTIFIER LPAREN parameter_declaration? RPAREN NEWLINE // Declaration only
								 (function_body NEWLINE)?; // body definition might be empty
parameter_declaration       : variable_declaration_statement (COMMA variable_declaration_statement)* ;
function_body			   	: local_statement  // Can it have empty_statement in front or not due to body definition only?
							| return_statement
							| block_statement;
							
return_statement			: RETURN expression;

// Scope
block_statement				: BEGIN NEWLINE (local_statement)* END NEWLINE;
function_block_statement	: BEGIN NEWLINE (local_statement | return_statement)* END NEWLINE;

if_statement 				: IF expression relational_operator expression RETURN boolean_value ;


boolean_value 				: TRUE | FALSE ;

// Expression : based on the precedence and associativity

expression 					: string_expression
							| relational_expression
							| logical_expression
							| adding_expression
							| multiplying_expression
							| negation_expression
							| index_expression
							| number_literal
							| boolean_literal
							| string_literal
							| LPAREN expression RPAREN; 

string_expression 			: string_expression CONCATE string_literal // Binary Infix None Associative
							| string_literal;


relational_expression		: logical_expression relational_operator logical_expression // Binary Infix None Associative
							| logical_expression;

logical_expression			: logical_expression logic_operator adding_expression // Binary Infix Left Associative
							| adding_expression;

adding_expression			: adding_expression additive_operator multiplying_expression // Binary Infix Left Associative
							| multiplying_expression;

multiplying_expression		: multiplying_expression multiplicative_operator sign_expression // Binary Infix Left Associative
							| negation_expression; 

negation_expression			: NOT negation_expression // Unary Prefix Right Associative
							| sign_expression;

sign_expression				: additive_operator sign_expression; // Unary Prefix Right Associative
							//| ;// Index??

index_expression			: ; // TODO index operator

// Expression operator
relational_operator 		: LT | LE | GT | GE | EQUAL | NOT_EQUAL | STRING_EQUAL;
additive_operator 			: PLUS | MINUS ;
multiplicative_operator		: MULTIPLY | DIVIDE | MOD ;
logic_operator 				: AND | OR ;


// Literal
string_literal 				: STRING_LIT ;
number_literal 				: NUMBER_LIT ;
boolean_literal 			: BOOLEAN_LIT ;

// ============== lexer rules ===================

// Type Keywords
NUMBER_TYPE  	: 'number' ;
BOOLEAN_TYPE	: 'bool' ;
STRING_TYPE		: 'string' ;
VAR				: 'var' ;
DYNAMIC			: 'dynamic' ;

// Control Keywords
COMMENT			: '##' ~[\n\r\f]* -> skip;
NEWLINE 		: ('\r''\n'|'\n''\r'|'\r'|'\n')
{
print("NEWLINE")
self.text = self.text.replace('\r\n', '\n')
};
WHITESPACE		: [ \t\r\b\f]+ -> skip ; // skip spaces, tabs, newlines

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

BOOLEAN_LIT    	: TRUE | FALSE ;
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