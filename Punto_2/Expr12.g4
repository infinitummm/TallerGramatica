grammar Expr12;


root
    : expr EOF
    ;

expr
    : expr '+' term   # Add
    | term            # TermOnly
    ;

term
    : term '*' factor # Mul
    | factor          # FactorOnly
    ;

factor
    : ID              # Id
    | NUM             # Num
    | '(' expr ')'    # Parens
    ;

ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
NUM     : [0-9]+ ('.' [0-9]+)? ;
WS      : [ \t\r\n]+ -> skip ;
