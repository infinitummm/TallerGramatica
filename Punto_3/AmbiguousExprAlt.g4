grammar AmbiguousExprAlt;

root
    : expr EOF
    ;

// Invertimos el orden para forzar la segunda alternativa en ANTLR
expr
    : expr '*' expr # Mul
    | expr '+' expr # Add
    | NUM           # Num
    ;

NUM : [0-9]+ ('.' [0-9]+)? ;
WS  : [ \t\r\n]+ -> skip ;
