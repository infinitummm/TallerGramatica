grammar Expr11;



root
    : expr EOF
    ;

// E -> E + T | T
expr
    : expr '+' term   # Add
    | term            # TermOnly
    ;

// T -> T * F | F
term
    : term '*' factor # Mul
    | factor          # FactorOnly
    ;

// F -> id | num | ( E )
factor
    : ID              # Id
    | NUM             # Num
    | '(' expr ')'    # Parens
    ;


ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
NUM     : [0-9]+ ('.' [0-9]+)? ;
WS      : [ \t\r\n]+ -> skip ;
