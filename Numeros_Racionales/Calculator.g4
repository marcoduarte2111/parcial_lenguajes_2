// Calculator.g4
grammar Calculator;

// Reglas léxicas
PLUS: '+' ;
MINUS: '-' ;
MULT: '*' ;
DIV: '/' ;
LPAREN: '(' ;
RPAREN: ')' ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;
WS: [ \t\r\n]+ -> skip ;

// Reglas sintácticas
expr: expr op=('*'|'/') expr   
    | expr op=('+'|'-') expr   
    | '(' expr ')'             
    | NUMBER                   
    ;
