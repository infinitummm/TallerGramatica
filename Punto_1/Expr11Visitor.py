# Generated from Expr11.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Expr11Parser import Expr11Parser
else:
    from Expr11Parser import Expr11Parser

# This class defines a complete generic visitor for a parse tree produced by Expr11Parser.

class Expr11Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Expr11Parser#root.
    def visitRoot(self, ctx:Expr11Parser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#Add.
    def visitAdd(self, ctx:Expr11Parser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#TermOnly.
    def visitTermOnly(self, ctx:Expr11Parser.TermOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#Mul.
    def visitMul(self, ctx:Expr11Parser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#FactorOnly.
    def visitFactorOnly(self, ctx:Expr11Parser.FactorOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#Id.
    def visitId(self, ctx:Expr11Parser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#Num.
    def visitNum(self, ctx:Expr11Parser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#Parens.
    def visitParens(self, ctx:Expr11Parser.ParensContext):
        return self.visitChildren(ctx)



del Expr11Parser