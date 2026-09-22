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


    # Visit a parse tree produced by Expr11Parser#e.
    def visitE(self, ctx:Expr11Parser.EContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#t.
    def visitT(self, ctx:Expr11Parser.TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#f.
    def visitF(self, ctx:Expr11Parser.FContext):
        return self.visitChildren(ctx)



del Expr11Parser