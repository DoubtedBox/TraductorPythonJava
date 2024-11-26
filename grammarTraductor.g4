grammar grammarTraductor;

// LEXER RULES Palabras clave
DEF: 'def';
RETURN: 'return';

// Identificadores
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Constantes
CONT: [0-9]+;

// Operadores
PLUS: '+';
MINUS: '-';
MULT: '*';
DIVI: '/';
EQUALS: '=';

// Símbolos de puntuación
LPAREN: '(';
RPAREN: ')';
COLON: ':';
COMMA: ',';

// Espacios en blanco y saltos de línea
WS: [ ]+ -> skip;
INDENT: [\t]+;
NEWLINE: [\r\n]+;

// Comentarios
COMMENT: '#' ~[\r\n]* -> skip;

// Parser rulerexpr Regla principal (program)
program: (statement_root | function)*;

statement_root: statement NEWLINE+ | statement;
function: function_declaration NEWLINE code_block;

// Declaracion de la funcion
function_declaration: DEF ID LPAREN param_list RPAREN COLON;

// Lista de parametros vacia o separada por comas
param_list: param (COMMA param)* |;
param: ID;

// Bloque de codigo
code_block: (INDENT (statement NEWLINE | statement))+;

// Declaracion
statement: assignment | return_statement | function_call | expr;

// Asignacion
assignment: ID EQUALS expr;

// Retorno de variable
return_statement: RETURN (expr | ID);

// Expresiones: números, variables, y operaciones
expr: term ((PLUS | MINUS) term)*;

// Términos: productos y divisiones
term: factor ((MULT | DIVI) factor)*;

// Factores: constantes, identificadores y subexpresiones
factor: CONT | function_call | LPAREN expr RPAREN | ID;

// Llamada a una funcion
function_call: ID LPAREN arg_list RPAREN;

// Lista de argumentos (vacía o separada por comas)
arg_list: expr (COMMA expr)* |;