grammar AmbiguousExpr;

// ============================================================
// Gramática de la Diapositiva 15 (Ambigua):
// E -> E + E
// E -> E * E
// E -> num
// ============================================================

root
    : expr EOF
    ;

expr
    : expr '+' expr # Add
    | expr '*' expr # Mul
    | NUM           # Num
    ;

NUM : [0-9]+ ('.' [0-9]+)? ;
WS  : [ \t\r\n]+ -> skip ;
