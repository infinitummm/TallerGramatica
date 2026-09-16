from Expr11Visitor import Expr11Visitor

class CheckVisitor(Expr11Visitor):
    """
    Visitor que recorre el Parse Tree de la gramática de la diapositiva 11.
    Retorna True si toda la estructura del árbol es sintácticamente válida.
    """

    def visitRoot(self, ctx):
        if ctx is None or ctx.expr() is None:
            return False
        return self.visit(ctx.expr())

    def visitAdd(self, ctx):
        left = self.visit(ctx.expr())
        right = self.visit(ctx.term())
        return bool(left and right)

    def visitTermOnly(self, ctx):
        return self.visit(ctx.term())

    def visitMul(self, ctx):
        left = self.visit(ctx.term())
        right = self.visit(ctx.factor())
        return bool(left and right)

    def visitFactorOnly(self, ctx):
        return self.visit(ctx.factor())

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitId(self, ctx):
        return ctx.ID() is not None

    def visitNum(self, ctx):
        return ctx.NUM() is not None
