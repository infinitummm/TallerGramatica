grammar AmbiguousExpr;

// ============================================================
// Gramatica de la Diapositiva 15 (Ambigua):
// E -> E + E
// E -> E * E
// E -> num
// ============================================================

root
    : e EOF
    ;

e
    : e '+' e # Add
    | e '*' e # Mul
    | NUM     # Num
    ;

NUM : [0-9]+ ('.' [0-9]+)? ;
WS  : [ \t\r\n]+ -> skip ;
