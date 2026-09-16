# Generated from Expr12.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Expr12Parser import Expr12Parser
else:
    from Expr12Parser import Expr12Parser

# This class defines a complete generic visitor for a parse tree produced by Expr12Parser.

class Expr12Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Expr12Parser#root.
    def visitRoot(self, ctx:Expr12Parser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#Add.
    def visitAdd(self, ctx:Expr12Parser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#TermOnly.
    def visitTermOnly(self, ctx:Expr12Parser.TermOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#Mul.
    def visitMul(self, ctx:Expr12Parser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#FactorOnly.
    def visitFactorOnly(self, ctx:Expr12Parser.FactorOnlyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#Id.
    def visitId(self, ctx:Expr12Parser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#Num.
    def visitNum(self, ctx:Expr12Parser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#Parens.
    def visitParens(self, ctx:Expr12Parser.ParensContext):
        return self.visitChildren(ctx)



del Expr12Parser