grammar CS;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        content = self.text[1:]
        if content.endswith('\r\n'):
            raise UncloseString(content[:-2])
        elif content.endswith('\n') or content.endswith('\r'):
            raise UncloseString(content[:-1])
        else:
            raise UncloseString(content)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(self.text[1:])
    elif tk == self.ERROR_TOKEN:
        raise ErrorToken(self.text)
    elif tk == self.STRING:
        self.text = self.text[1:-1]
        return super().emit()
    return super().emit()
}

// -------------------- Parser rules --------------------
program: (structDecl | funcDecl)* EOF ;
structDecl: 'struct' ID '{' (type ID ';')* '}' ';' ;
funcDecl: ('void' | type)? ID '(' (type ID (',' type ID)*)? ')' block ;
type: 'int' | 'float' | 'string' | ID ;
block: '{' (varDeclCore ';' | statement)* '}' ;
varDeclCore: ('auto' | type) ID ('=' expr)? ;
statement
    : 'if' '(' expr ')' statement ('else' statement)?
    | 'while' '(' expr ')' statement
    | 'for' '(' (varDeclCore | assignment)? ';' expr? ';' (assignment | update)? ')' statement
    | 'switch' '(' expr ')' '{' ('case' expr ':' statement*)* ('default' ':' statement*)? ('case' expr ':' statement*)* '}'
    | ('break' | 'continue') ';'
    | 'return' expr? ';'
    | (assignment | expr) ';'
    | block ;
accessed: (ID | callExpr | primary) ('.' ID)+ | ID ;
assignment: accessed '=' assignmentExpr ;
update: prefixExpr | postfixExpr | assignment ;
expr: assignmentExpr ;
assignmentExpr: accessed '=' assignmentExpr | logicOrExpr ;
logicOrExpr: logicAndExpr ('||' logicAndExpr)* ;
logicAndExpr: equalityExpr ('&&' equalityExpr)* ;
equalityExpr: relationalExpr (('==' | '!=') relationalExpr)* ;
relationalExpr: addExpr (('<' | '>' | '<=' | '>=') addExpr)* ;
addExpr: mulExpr (('+' | '-') mulExpr)* ;
mulExpr: unaryExpr (('*' | '/' | '%') unaryExpr)* ;
unaryExpr: ('!' | '-' | '+') unaryExpr | prefixExpr ;
prefixExpr: ('++' | '--') prefixExpr | postfixExpr ;
postfixExpr: (ID | callExpr | primary) ('.' ID)+ | callExpr | postfixExpr ('++' | '--') | primary ;
callExpr: primary '(' (expr (',' expr)*)? ')' ;
primary: '(' expr ')' | ID | INTLIT | FLOATLIT | STRING | '{' (expr (',' expr)*)? '}' ;


// -------------------- Lexer rules --------------------

// Whitespace & Comments
WS: [ \t\r\n\f]+ -> skip ;
BLOCK_COMMENT: '/*' .*? '*/' -> skip ;
LINE_COMMENT: '//' ~[\r\n]* -> skip ;

// Keywords
AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
IF: 'if';
INT: 'int';
RETURN: 'return';
STRING_TYPE: 'string';
STRUCT: 'struct';
SWITCH: 'switch';
VOID: 'void';
WHILE: 'while';

// Operators & Separators
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
AND: '&&';
OR: '||';
NOT: '!';
INC: '++';
DEC: '--';
ASSIGN: '=';
DOT: '.';
SEMI: ';';
COMMA: ',';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
COLON: ':';

// Literals
ID: [a-zA-Z_] [a-zA-Z0-9_]* ;

INTLIT: [0-9]+;

FLOATLIT: [0-9]+ '.' [0-9]* ( [eE] [+-]? [0-9]+ )?
        | [0-9]+ [eE] [+-]? [0-9]+
        | '.' [0-9]+ ( [eE] [+-]? [0-9]+ )?
        ;

fragment ESC_SEQ: '\\' [bfnrt"\\] ;

STRING: '"' ( ESC_SEQ | ~[\\"\r\n] )* '"' ;

ILLEGAL_ESCAPE: '"' ( ESC_SEQ | ~[\\"\r\n] )* '\\' ( ~[bfnrt"\\\r\n] | '"' ) ;

UNCLOSE_STRING: '"' ( ESC_SEQ | ~[\\"\r\n] )* '\\'? ( '\r\n' | '\n' | EOF ) ;

UNFINISHED_STRING: '"' ( ESC_SEQ | ~[\\"\r\n] )* -> type(UNCLOSE_STRING) ;

ERROR_TOKEN: . ;