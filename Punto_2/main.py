import sys
from antlr4 import *
from Expr12Lexer import Expr12Lexer
from Expr12Parser import Expr12Parser
from ast_builder import ASTBuilderVisitor

def count_cst_nodes(tree):
    """Cuenta el número de nodos del Parse Tree concreto de ANTLR."""
    count = 1
    for i in range(tree.getChildCount()):
        count += count_cst_nodes(tree.getChild(i))
    return count

def analyze_expression(expr_str: str, label: str = ""):
    print("=" * 65)
    if label:
        print(f" {label}")
    print(f" Expresión de entrada:  \"{expr_str}\"")
    print("=" * 65)

    input_stream = InputStream(expr_str)
    lexer = Expr12Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Expr12Parser(token_stream)
    cst_tree = parser.root()

    # 1. Información del Parse Tree (Diapositiva 12)
    cst_node_count = count_cst_nodes(cst_tree)
    print(f"\n[1] Parse Tree (CST - Diapositiva 12):")
    print(f"    - Nodos totales en CST: {cst_node_count}")
    print(f"    - Estructura LISP de ANTLR: {cst_tree.toStringTree(recog=parser)}")

    # 2. Construcción del AST (Diapositiva 13)
    visitor = ASTBuilderVisitor()
    ast_tree = visitor.visit(cst_tree)
    ast_node_count = ast_tree.count_nodes()

    print(f"\n[2] Abstract Syntax Tree (AST - Diapositiva 13):")
    print(f"    - Nodos totales en AST: {ast_node_count}  (Reducción de {(1 - ast_node_count/cst_node_count)*100:.1f}% de nodos)")
    print(f"    - Notación S-Expression (Prefija): {ast_tree.to_sexpr()}")
    print(f"    - Valor evaluado semántico:        {ast_tree.evaluate()}")

    print(f"\n[3] Representación Gráfica del AST:")
    print(ast_tree.to_ascii_tree(prefix="    "))

    return ast_tree

def main():
    print("=" * 70)
    print(" PUNTO 2: Comprobación de las Diferentes Formas de AST")
    print(" Gramática Diapositiva 12: E -> E + T | T,  T -> T * F | F,  F -> id|num|(E)")
    print(" Integrantes: Dylan Torres - Juan Gomez - Javier Rosero")
    print("=" * 70)

    # 1. Ejemplo canónico de la Diapositiva 12 y 13: 3 + 4 * 5
    ast1 = analyze_expression("3 + 4 * 5", "CASO A: Precedencia Natural (* sobre +) - Diapositivas 12 y 13")

    # 2. Ejemplo con paréntesis: (3 + 4) * 5
    ast2 = analyze_expression("(3 + 4) * 5", "CASO B: Precedencia Alterada con Paréntesis (+ sobre *)")

    # 3. Ejemplo con asociatividad a la izquierda: 3 + 4 + 5
    ast3 = analyze_expression("3 + 4 + 5", "CASO C: Asociatividad a la Izquierda (Misma precedencia)")

    # 4. Ejemplo mixto con identificadores: a + b * c
    ast4 = analyze_expression("a + b * c", "CASO D: Expresión con Variables (Diapositiva 31)")

    # Comparación Conceptual
    print("\n" + "#" * 70)
    print(" CONCLUSIONES TEÓRICAS SOBRE LAS FORMAS DE AST (Diapositivas 12 a 14)")
    print("#" * 70)
    print("""
1. Unicidad del AST para una misma cadena:
   - Para '3 + 4 * 5', la gramática de la diapositiva 12 produce EXACTAMENTE
     UN AST: (+ 3 (* 4 5)).
   - Es IMPOSIBLE obtener (* (+ 3 4) 5) sin paréntesis, demostrando que la
     gramática de la diapositiva 12 NO es ambigua.

2. Cambio de forma mediante paréntesis:
   - Los paréntesis no aparecen como nodos en el AST (se eliminan por ser sintácticos).
   - Su función es reestructurar la jerarquía del AST: en '(3 + 4) * 5', el
     nodo '*' pasa a ser la raíz y '+' pasa al subárbol izquierdo.

3. Eficiencia: Parse Tree (Slide 12) vs AST (Slide 13):
   - El Parse Tree conserva no-terminales intermedios (E, T, F), comas y paréntesis.
   - El AST conserva ÚNICAMENTE operadores ('+', '*') y operandos (3, 4, 5),
     reduciendo drásticamente la memoria y facilitando la generación de código.
""")

if __name__ == "__main__":
    main()
