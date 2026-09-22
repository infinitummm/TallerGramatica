from Expr12Visitor import Expr12Visitor
from ast_nodes import BinaryOpNode, NumNode, IdNode

class ASTBuilderVisitor(Expr12Visitor):
    """
    Visitor que convierte el Parse Tree concreto de ANTLR
    en un Arbol de Sintaxis Abstracta (AST) limpio y semantico.
    Utiliza la gramatica exacta: E -> E + T | T, T -> T * F | F, F -> id | num | (E)
    """

    def visitRoot(self, ctx):
        return self.visit(ctx.e())

    def visitE(self, ctx):
        if ctx.e():
            left = self.visit(ctx.e())
            right = self.visit(ctx.t())
            return BinaryOpNode('+', left, right)
        return self.visit(ctx.t())

    def visitT(self, ctx):
        if ctx.t():
            left = self.visit(ctx.t())
            right = self.visit(ctx.f())
            return BinaryOpNode('*', left, right)
        return self.visit(ctx.f())

    def visitF(self, ctx):
        if ctx.e():
            # Los parentesis alteran la precedencia pero se omiten en el AST
            return self.visit(ctx.e())
        if ctx.ID():
            return IdNode(ctx.ID().getText())
        if ctx.NUM():
            text = ctx.NUM().getText()
            return NumNode(float(text))
