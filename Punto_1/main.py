import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from Expr11Lexer import Expr11Lexer
from Expr11Parser import Expr11Parser
from check_visitor import CheckVisitor

class SyntaxErrorCollector(ErrorListener):
    """Captura errores léxicos y sintácticos sin detener la ejecución."""
    def __init__(self):
        super().__init__()
        self.has_errors = False
        self.message = ""

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_errors = True
        self.message = f"Línea {line}:{column} -> {msg}"

def validate(expression: str, print_result: bool = True):
    """
    Valida una expresión utilizando el parser ANTLR y el Visitor.
    Retorna True si es ACEPTADA, False si es RECHAZADA.
    """
    expr_clean = expression.strip()
    if not expr_clean:
        if print_result:
            print("RECHAZADA (cadena vacía)")
        return False

    error_collector = SyntaxErrorCollector()

    input_stream = InputStream(expr_clean)
    lexer = Expr11Lexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_collector)

    token_stream = CommonTokenStream(lexer)
    parser = Expr11Parser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_collector)

    tree = parser.root()

    if error_collector.has_errors or parser.getNumberOfSyntaxErrors() > 0:
        if print_result:
            print(f"RECHAZADA ({error_collector.message})")
        return False

    visitor = CheckVisitor()
    accepted = visitor.visit(tree)

    if accepted:
        if print_result:
            print("ACEPTADA")
        return True
    else:
        if print_result:
            print("RECHAZADA (fallo estructural en Visitor)")
        return False

def run_tests_file(filename: str):
    print("=" * 60)
    print(f" Validando expresiones desde archivo: {filename}")
    print("=" * 60)
    if not os.path.exists(filename):
        print(f"Error: El archivo {filename} no existe.")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total = 0
    ok = 0
    fail = 0

    for line in lines:
        line_clean = line.strip()
        if not line_clean or line_clean.startswith('#'):
            if line_clean.startswith('#'):
                print(f"\n{line_clean}")
            continue

        total += 1
        print(f"{line_clean:<32} -> ", end="")
        if validate(line_clean, True):
            ok += 1
        else:
            fail += 1

    print("-" * 60)
    print(f"Total pruebas: {total} | Aceptadas: {ok} | Rechazadas: {fail}\n")

def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if os.path.isfile(arg):
            run_tests_file(arg)
            return
        else:
            expr = " ".join(sys.argv[1:])
            print(f"Expresión: \"{expr}\" -> ", end="")
            validate(expr, True)
            return

    # Demostración por defecto
    print("=" * 65)
    print(" PUNTO 1: Gramática de la Diapositiva 11 (Python 3)")
    print(" Reglas: E -> E + T | T,  T -> T * F | F,  F -> id | num | (E)")
    print(" Integrantes: Dylan Torres - Juan Gomez - Javier Rosero")
    print("=" * 65)

    if os.path.exists("pruebas.txt"):
        run_tests_file("pruebas.txt")

    if not sys.stdin.isatty():
        return

    print("-" * 65)
    print(" Modo Interactivo (escribe una expresión o 'salir' para terminar):")
    print("-" * 65)
    try:
        while True:
            line = input("expr> ").strip()
            if line.lower() in ["salir", "exit", "quit"]:
                print("Finalizando sesión.")
                break
            if not line:
                continue
            validate(line, True)
    except (EOFError, KeyboardInterrupt):
        print("\nSesión finalizada.")

if __name__ == "__main__":
    main()
