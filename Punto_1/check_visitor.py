from Expr11Visitor import Expr11Visitor

class CheckVisitor(Expr11Visitor):
    """
    Visitor que recorre el Parse Tree de la gramatica exacta de la diapositiva 11:
    E -> E + T | T
    T -> T * F | F
    F -> id | num | (E)
    """

    def visitRoot(self, ctx):
        if ctx is None or ctx.e() is None:
            return False
        return self.visit(ctx.e())

    def visitE(self, ctx):
        if ctx.e():
            return bool(self.visit(ctx.e()) and self.visit(ctx.t()))
        return self.visit(ctx.t())

    def visitT(self, ctx):
        if ctx.t():
            return bool(self.visit(ctx.t()) and self.visit(ctx.f()))
        return self.visit(ctx.f())

    def visitF(self, ctx):
        if ctx.e():
            return self.visit(ctx.e())
        if ctx.ID():
            return True
        if ctx.NUM():
            return True
        return False
