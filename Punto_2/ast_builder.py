from Expr12Visitor import Expr12Visitor
from ast_nodes import BinaryOpNode, NumNode, IdNode

class ASTBuilderVisitor(Expr12Visitor):
    """
    Visitor que convierte el Parse Tree concreto de ANTLR
    en un Árbol de Sintaxis Abstracta (AST) limpio y semántico.
    """

    def visitRoot(self, ctx):
        return self.visit(ctx.expr())

    def visitAdd(self, ctx):
        left = self.visit(ctx.expr())
        right = self.visit(ctx.term())
        return BinaryOpNode('+', left, right)

    def visitTermOnly(self, ctx):
        return self.visit(ctx.term())

    def visitMul(self, ctx):
        left = self.visit(ctx.term())
        right = self.visit(ctx.factor())
        return BinaryOpNode('*', left, right)

    def visitFactorOnly(self, ctx):
        return self.visit(ctx.factor())

    def visitParens(self, ctx):
        # Los paréntesis alteran la precedencia pero NO son nodos en el AST
        return self.visit(ctx.expr())

    def visitId(self, ctx):
        return IdNode(ctx.ID().getText())

    def visitNum(self, ctx):
        text = ctx.NUM().getText()
        val = float(text)
        return NumNode(val)
