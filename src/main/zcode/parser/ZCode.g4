grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// ============== parser rules ===================


program						: ignore_statement_list? declaration_list? EOF;


declaration_list			: (ignore_statement_list_inline | declaration) declaration_list // Recursive
							| (ignore_statement_list_inline | declaration); // Only one declaration

declaration					: function_declaration_statement 
							| variable_declaration_statement; 

// Local statement

local_statement_single		: ignore_statement_list_inline? local_statement ignore_statement_list_inline?;

local_statement_list		: (ignore_statement_list_inline | local_statement) local_statement_list // Recursive
							| (ignore_statement_list_inline | local_statement);

local_statement				: variable_declaration_statement
							| if_statement
							| function_call_statement
							| for_statement
							| break_statement
							| continue_statement
							| block_statement
							| assignment_statement
							| return_statement;


// Ignore statement
ignore_statement_list_inline: NEWLINE ignore_statement_list
							| NEWLINE;
							
ignore_statement_list		: ignore_statement ignore_statement_list // Recursive
							| ignore_statement;

ignore_statement			: COMMENT | NEWLINE;

// Scope
block_statement				: BEGIN local_statement_list? END ;


// Variable
variable_declaration_statement	: basic_variable_declaration | array_declaration ;

basic_variable_declaration	: VAR IDENTIFIER ASSIGN expression // Must have initial value
							| (basic_type | DYNAMIC) IDENTIFIER (ASSIGN expression)?;
basic_type					: (NUMBER_TYPE | STRING_TYPE | BOOLEAN_TYPE) ;

// Array

array_declaration			: basic_type IDENTIFIER array_dimension (ASSIGN array_value)?;

array_dimension 			: LBRACK array_dimension_list RBRACK;
array_dimension_list 		: number_literal COMMA array_dimension_list // Recursive
							| number_literal;


array_value					: LBRACK array_value_expression_list RBRACK
							| LBRACK RBRACK // Empty array
							| expression;

array_value_expression_list	: expression COMMA array_value_expression_list // Recursive
							| array_value COMMA array_value
							| array_value
							| expression;



// Assignment

assignment_statement		: basic_variable_assignment
							| array_assignment;
basic_variable_assignment	: IDENTIFIER ASSIGN expression ;
array_assignment 			: array_access ASSIGN expression ;


// Function 
function_declaration_statement	: FUNC IDENTIFIER LPAREN parameter_part_recursive? RPAREN NEWLINE? // Declaration only
								 (function_body )? ; // body definition might be empty

function_body			   	: local_statement_single;

return_statement			: RETURN expression;

// Parameter
parameter_part_recursive    : parameter_declaration_statement COMMA parameter_part_recursive // Recursive
							| parameter_declaration_statement;
							
parameter_declaration_statement	: basic_parameter_declaration
								| array_parameter_declaration;
basic_parameter_declaration	: (DYNAMIC|basic_type) IDENTIFIER;
array_parameter_declaration	: basic_type IDENTIFIER array_dimension;

// If-Else
if_statement				: IF expression branch_body 
								(elif_recursive_statement)?
								(else_statement)? ;

elif_recursive_statement	: elif_statement elif_recursive_statement // Recursive
							| elif_statement;

elif_statement				: ELIF expression branch_body;
else_statement				: ELSE branch_body;
branch_body					: local_statement_single;


// Function call
function_call_statement		: IDENTIFIER LPAREN argument_part? RPAREN ;
argument_part				: expression COMMA argument_part // Recursive
							| expression;

// Loop
for_statement				: FOR IDENTIFIER UNTIL expression BY expression loop_body;
loop_body					: local_statement_single;

break_statement				: BREAK;
continue_statement			: CONTINUE;

// Expression : based on the precedence and associativity

expression 					: string_expression; // Highest precedence
							

string_expression 			: relational_expression CONCATE relational_expression // Binary Infix None Associative
							| relational_expression; // Next precedence


relational_expression		: logical_expression relational_operator logical_expression // Binary Infix None Associative
							| logical_expression; // Next precedence

logical_expression			: logical_expression logic_operator adding_expression // Binary Infix Left Associative
							| adding_expression; // Next precedence

adding_expression			: adding_expression additive_operator multiplying_expression // Binary Infix Left Associative
							| multiplying_expression; // Next precedence

multiplying_expression		: multiplying_expression multiplicative_operator negation_expression // Binary Infix Left Associative
							| negation_expression; // Next precedence

negation_expression			: NOT negation_expression // Unary Prefix Right Associative
							| sign_expression; // Next precedence

sign_expression				: additive_operator sign_expression // Unary Prefix Right Associative
							| element_expression; // Next precedence

element_expression 			: operand? index_expression  // Unary Postfix Left Associative
							| parenthesis_expression; // Next precedence

					

index_expression			: index_expression LBRACK array_index_access RBRACK // Unary Postfix Left Associative
							| LBRACK array_index_access RBRACK;

parenthesis_expression		: LPAREN expression RPAREN // Parenthesis
							| operand; // Next precedence

operand						: literal 
							| function_call_statement 
							| IDENTIFIER ;

// Array access
array_access				: IDENTIFIER index_expression; // Unary Postfix Left Associative
		
array_index_access			: expression COMMA array_index_access // Recursive
							| expression;

// Expression operator
relational_operator 		: LT | LE | GT | GE | EQUAL | NOT_EQUAL | STRING_EQUAL;
additive_operator 			: PLUS | MINUS ;
multiplicative_operator		: MULTIPLY | DIVIDE | MOD ;
logic_operator 				: AND | OR ;


// Literal
literal						: NUMBER_LIT | BOOLEAN_LIT | STRING_LIT;
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
COMMENT			: '##' ~[\n\r\f]* ;
NEWLINE 		: ('\r''\n'|'\n''\r'|'\r'|'\n')
{
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
NOT_EQUAL   	: '!=' ;
LT       		: '<' ;
LE       		: '<=' ;
GT       		: '>' ;
GE       		: '>=' ;

// String Operators
CONCATE    		: '...' ;
STRING_EQUAL   	: '==' ;

// Literal
IDENTIFIER		: [a-zA-Z_] [a-z0-9A-Z_]*;

NUMBER_LIT     	: NUMBER_INTERGER NUMBER_DECIMAL? NUMBER_EXPONENT? ;
fragment NUMBER_INTERGER 	: [0-9]+ ;
fragment NUMBER_DECIMAL 	: '.'[0-9]* ;
fragment NUMBER_EXPONENT 	: [eE][+-]?[0-9]+ ;

BOOLEAN_LIT    	: TRUE | FALSE ;
fragment TRUE      		: 'true' ;
fragment FALSE     		: 'false' ;

//Normal regex:  "([^\'\"\r\n\\]|\\['\\nrtbf]|'")*"
STRING_LIT 			: '"' (~['"\r\n\\] | '\\' ['\\nrtbf] | '\'"')* '"' {
self.text = self.text[1:-1]
};



// Error
ERROR_CHAR: . 
{
raise ErrorToken(self.text)
};

UNCLOSE_STRING  : '"' (~['"\\\t\b\f] | '\\' ['\\nrtbf] | '\'"' | [\r\n] )* ('"'|EOF)
{
newlineIndex = self.text.find('\r\n') 
raise UncloseString(self.text[1:newlineIndex] if newlineIndex != -1 else self.text[1:]) # if end with \n else end with EOF
};

ILLEGAL_ESCAPE  : '"' (~['"\\] | '\\' ['\\nrtbf] | '\'"' )* ('\\' ~['\\nrtbf] | [\t\b\f] | '\'' ~["])
{
raise IllegalEscape(self.text[1:])
};