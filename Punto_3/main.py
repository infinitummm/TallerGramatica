import sys
from antlr4 import *
from antlr4.error.DiagnosticErrorListener import DiagnosticErrorListener
from antlr4.atn.PredictionMode import PredictionMode

from AmbiguousExprLexer import AmbiguousExprLexer
from AmbiguousExprParser import AmbiguousExprParser
from AmbiguousExprVisitor import AmbiguousExprVisitor

from AmbiguousExprAltLexer import AmbiguousExprAltLexer
from AmbiguousExprAltParser import AmbiguousExprAltParser
from AmbiguousExprAltVisitor import AmbiguousExprAltVisitor

class EvalVisitor1(AmbiguousExprVisitor):
    def visitRoot(self, ctx):
        return self.visit(ctx.expr())

    def visitAdd(self, ctx):
        return self.visit(ctx.expr(0)) + self.visit(ctx.expr(1))

    def visitMul(self, ctx):
        return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))

    def visitNum(self, ctx):
        return float(ctx.NUM().getText())

class EvalVisitor2(AmbiguousExprAltVisitor):
    def visitRoot(self, ctx):
        return self.visit(ctx.expr())

    def visitAdd(self, ctx):
        return self.visit(ctx.expr(0)) + self.visit(ctx.expr(1))

    def visitMul(self, ctx):
        return self.visit(ctx.expr(0)) * self.visit(ctx.expr(1))

    def visitNum(self, ctx):
        return float(ctx.NUM().getText())

def main():
    print("=" * 72)
    print(" PUNTO 3: Demostración de Ambigüedad de la Gramática (Diapositiva 15)")
    print(" Gramática: E -> E + E | E * E | num")
    print(" Integrantes: Dylan Torres - Juan Gomez - Javier Rosero")
    print("=" * 72)

    expr_test = "2 + 3 * 4"
    if len(sys.argv) > 1:
        expr_test = sys.argv[1]

    print(f"\nAnalizando la expresión ambigua canónica: \"{expr_test}\"\n")

    # =========================================================================
    # Árbol 1: Interpretación donde la Suma se agrupa primero (Diapositiva 16)
    # =========================================================================
    t1 = AmbiguousExprParser(CommonTokenStream(AmbiguousExprLexer(InputStream(expr_test)))).root()
    val1 = EvalVisitor1().visit(t1)

    # =========================================================================
    # Árbol 2: Interpretación donde el Producto se agrupa primero (Diapositiva 16)
    # =========================================================================
    t2 = AmbiguousExprAltParser(CommonTokenStream(AmbiguousExprAltLexer(InputStream(expr_test)))).root()
    val2 = EvalVisitor2().visit(t2)

    print("-" * 72)
    print(" [1] ÁRBOL DE ANÁLISIS 1: Interpretación (2 + 3) * 4")
    print("-" * 72)
    print("Derivación por la izquierda:")
    print("   E  =>  E * E")
    print("      =>  (E + E) * E")
    print("      =>  (2 + 3) * 4")
    print(f"\nValor numérico calculado: {val1}")
    print("\nEstructura en árbol (ASCII):")
    print("   └── OpBinario ('*')")
    print("       ├── OpBinario ('+')")
    print("       │   ├── Num (2)")
    print("       │   └── Num (3)")
    print("       └── Num (4)")

    print("\n" + "-" * 72)
    print(" [2] ÁRBOL DE ANÁLISIS 2: Interpretación 2 + (3 * 4)")
    print("-" * 72)
    print("Derivación por la izquierda:")
    print("   E  =>  E + E")
    print("      =>  2 + (E * E)")
    print("      =>  2 + (3 * 4)")
    print(f"\nValor numérico calculado: {val2}")
    print("\nEstructura en árbol (ASCII):")
    print("   └── OpBinario ('+')")
    print("       ├── Num (2)")
    print("       └── OpBinario ('*')")
    print("           ├── Num (3)")
    print("           └── Num (4)")

    print("\n" + "=" * 72)
    print(" CONCLUSIÓN FORMAL: LA GRAMÁTICA ES DEFINITIVAMENTE AMBIGUA")
    print("=" * 72)
    print(f"""
Para la misma cadena de entrada '{expr_test}', la gramática de la Diapositiva 15:
  1. Admite DOS árboles de derivación sintácticos completamente válidos.
  2. Produce DOS interpretaciones semánticas con resultados distintos:
     - Interpretación 1: {val1}
     - Interpretación 2: {val2}

¿Por qué ocurre esto?
Porque las producciones E -> E + E y E -> E * E:
  - NO definen niveles de precedencia (tratan a '+' y '*' al mismo nivel).
  - NO definen asociatividad clara (ambas son recursivas por izquierda y derecha).

¿Cómo se solucionó en la Diapositiva 11 y 12?
Estratificando la gramática en niveles (E -> E + T | T,  T -> T * F | F,  F -> ...),
lo que fuerza a que el producto se evalúe primero y garantiza un único árbol.
""")

if __name__ == "__main__":
    main()
