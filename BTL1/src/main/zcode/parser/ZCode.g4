grammar ZCode;
// Student : Banh Tan Thuan
// Student ID : 2153011
// Class : CC03
@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// ============== parser rules ===================


program						: newline_list? declaration_list newline_list? EOF;


declaration_list			: declaration declaration_list // Recursive
							| declaration; // At least one declaration
							

declaration					: function_declaration newline_list?
							| variable_declaration_statement newline_list; 

// Local statement

local_statement_single		: newline_list? local_statement newline_list?;

local_statement_list		: (newline_list|local_statement) local_statement_list // Recursive
							| ; // Empty statement list


local_statement				: variable_declaration_statement NEWLINE
							| if_statement 
							| function_call_statement NEWLINE
							| for_statement 
							| break_statement NEWLINE
							| continue_statement NEWLINE
							| block_statement
							| assignment_statement NEWLINE
							| return_statement NEWLINE;


// Ignore statement
							
newline_list				: newline newline_list // Recursive
							| newline;

newline						: NEWLINE;


// Scope
block_statement				: BEGIN newline_list local_statement_list END newline_list ;


// Variable
variable_declaration_statement	: basic_variable_declaration | array_declaration ;

basic_variable_declaration	: VAR IDENTIFIER ASSIGN expression // Must have initial value
							| (basic_type | DYNAMIC) IDENTIFIER (ASSIGN expression)?;
basic_type					: (NUMBER_TYPE | STRING_TYPE | BOOLEAN_TYPE) ;

// Array

array_declaration			: basic_type IDENTIFIER array_dimension (ASSIGN expression)?;

array_dimension 			: LBRACK array_dimension_list RBRACK;
array_dimension_list 		: number_literal COMMA array_dimension_list // Recursive
							| number_literal;


// Assignment

assignment_statement		: IDENTIFIER element_expression? ASSIGN expression;

// Function 
function_declaration		: FUNC IDENTIFIER LPAREN parameter_part_recursive? RPAREN function_body ; // Declaration onlu or body definition might be empty

function_body			   	: newline_list? return_statement NEWLINE
							| newline_list? block_statement
							| newline;
							
return_statement			: RETURN expression?;

// Parameter
parameter_part_recursive    : parameter_declaration COMMA parameter_part_recursive // Recursive
							| parameter_declaration;
							
parameter_declaration		: basic_parameter_declaration
							| array_parameter_declaration;
basic_parameter_declaration	: basic_type IDENTIFIER;
array_parameter_declaration	: basic_type IDENTIFIER array_dimension;

// If-Else
if_statement				: IF branch_condition branch_body 
								elif_recursive_statement
								else_statement ;

elif_recursive_statement	: elif_statement elif_recursive_statement // Recursive
							| ;

elif_statement				: ELIF branch_condition branch_body;
else_statement				: ELSE branch_body
							| ;
							
branch_condition			: LPAREN expression RPAREN;
branch_body					: local_statement_single;


// Function call
function_call_statement		: IDENTIFIER LPAREN argument_part? RPAREN ;
function_call_expression	: IDENTIFIER LPAREN argument_part? RPAREN ;
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

sign_expression				: MINUS sign_expression // Unary Prefix Right Associative
							| parenthesis_expression; // Next precedence

parenthesis_expression		: LPAREN expression RPAREN // Parenthesis
							| operand; // Next precedence

operand						: literal 
							| function_call_expression 
							| IDENTIFIER 
							| array_literal;

// Array access
array_literal 				: (function_call_expression | IDENTIFIER)? element_expression ; // Unary Postfix Left Associative
						
element_expression			: LBRACK index_operator RBRACK; 

index_operator				: expression COMMA index_operator // Recursive
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
COMMENT			: '##' ~[\n\r\f]* -> skip;

NEWLINE 		: ('\r\n'|'\n')
{
self.text = self.text.replace('\r', '')
};

WHITESPACE		: [ \t\b\f]+ -> skip ; // skip spaces, tabs, newlines

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


BOOLEAN_LIT    	: TRUE | FALSE ;
fragment TRUE      		: 'true' ;
fragment FALSE     		: 'false' ;

// Literal
IDENTIFIER		: [a-zA-Z_] [a-z0-9A-Z_]*;

NUMBER_LIT     	: NUMBER_INTERGER NUMBER_DECIMAL? NUMBER_EXPONENT? ;
fragment NUMBER_INTERGER 	: [0-9]+ ;
fragment NUMBER_DECIMAL 	: '.'[0-9]* ;
fragment NUMBER_EXPONENT 	: [eE][+-]?[0-9]+ ;


//Normal regex:  "([^\'\"\r\n\\]|\\['\\nrtbf]|'")*"
STRING_LIT 			: '"' (~['"\r\n\\\f] | [\\] ['\\nrtbf] | ['](~[\r\n\\\f\b])?)* '"' {
self.text = self.text[1:-1]
};



// Error
ERROR_CHAR: . 
/*!!*/{
raise ErrorToken(self.text)
}
//*/
;


UNCLOSE_STRING  : '"' (~['"\\] | [\\] ['\\nrtbf] | ['](~[\\\f\b])? )* ('"' | EOF)
{

index = len(self.text)
if self.text.find('\r') != -1:
	index = min(index, self.text.find('\r'))
if self.text.find('\n') != -1:
	index = min(index, self.text.find('\n'))
if self.text.find('\f') != -1:
	index = min(index, self.text.find('\f'))

raise UncloseString(self.text[1:index] if index != len(self.text) else self.text[1:]) # if end with \n else end with EOF
};


ILLEGAL_ESCAPE  : '"'  (~['"\\] | [\\]. | ['](~[\\\f\b])? )* ('"' | EOF)
{

end_index = -1
for i in range(1, len(self.text)):
    if self.text[i-1] != '\\' and  self.text[i] == '\\' and self.text[i+1] not in '\\nrtbf':
        end_index = i + 2
        break


#print("Original text: ", self.text, ", Fix: ", self.text[1:end_index])
raise IllegalEscape(self.text[1:end_index])

};

