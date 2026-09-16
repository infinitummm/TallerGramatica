import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def ensure_antlr_generated(grammar_files, cwd):
    """Verifica y autogenera el código ANTLR si no está presente."""
    for g in grammar_files:
        prefix = g.replace(".g4", "")
        lexer_file = os.path.join(cwd, f"{prefix}Lexer.py")
        if not os.path.exists(lexer_file):
            print(f"==> Generando código ANTLR para {g} en {cwd}...")
            cmd = ["antlr4", "-Dlanguage=Python3", "-no-listener", "-visitor", g]
            subprocess.run(cmd, cwd=cwd, check=True)

def run_step(title, script_path, args, grammars, cwd):
    print("\n" + "=" * 75)
    print(f" >>> EJECUTANDO {title} <<<")
    print("=" * 75)
    ensure_antlr_generated(grammars, cwd)
    cmd = [sys.executable, script_path] + args
    res = subprocess.run(cmd, cwd=cwd)
    if res.returncode != 0:
        print(f"Aviso: El script en {cwd} terminó con código {res.returncode}")

def main():
    print("*" * 75)
    print(" QUIZ SINTÁCTICO - EJECUCIÓN COMPLETA (PUNTOS 1, 2 Y 3)")
    print(" Integrantes: Dylan Torres - Juan Gomez - Javier Rosero")
    print("*" * 75)

    # Punto 1
    p1_dir = os.path.join(BASE_DIR, "Punto_1")
    run_step("PUNTO 1 (Gramática Diapositiva 11 en Python con Pruebas)", "main.py", ["pruebas.txt"], ["Expr11.g4"], p1_dir)

    # Punto 2
    p2_dir = os.path.join(BASE_DIR, "Punto_2")
    run_step("PUNTO 2 (Comprobación de las Diferentes Formas de AST - Diapositiva 12)", "main.py", [], ["Expr12.g4"], p2_dir)

    # Punto 3
    p3_dir = os.path.join(BASE_DIR, "Punto_3")
    run_step("PUNTO 3 (Comprobación de Ambigüedad de la Gramática - Diapositiva 15)", "main.py", [], ["AmbiguousExpr.g4", "AmbiguousExprAlt.g4"], p3_dir)

    print("\n" + "*" * 75)
    print(" EJECUCIÓN DE TODOS LOS PUNTOS FINALIZADA CON ÉXITO")
    print("*" * 75)

if __name__ == "__main__":
    main()
