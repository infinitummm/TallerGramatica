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


    # Visit a parse tree produced by Expr12Parser#e.
    def visitE(self, ctx:Expr12Parser.EContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#t.
    def visitT(self, ctx:Expr12Parser.TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#f.
    def visitF(self, ctx:Expr12Parser.FContext):
        return self.visitChildren(ctx)



del Expr12Parser