grammar Expr11;

root
    : e EOF
    ;

// E -> E + T | T
e
    : e '+' t
    | t
    ;

// T -> T * F | F
t
    : t '*' f
    | f
    ;

// F -> id | num | (E)
f
    : ID
    | NUM
    | '(' e ')'
    ;

ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
NUM     : [0-9]+ ('.' [0-9]+)? ;
WS      : [ \t\r\n]+ -> skip ;
