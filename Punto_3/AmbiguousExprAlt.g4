grammar AmbiguousExprAlt;

root
    : e EOF
    ;

// Invertimos el orden para forzar la segunda alternativa en ANTLR
e
    : e '*' e # Mul
    | e '+' e # Add
    | NUM     # Num
    ;

NUM : [0-9]+ ('.' [0-9]+)? ;
WS  : [ \t\r\n]+ -> skip ;
