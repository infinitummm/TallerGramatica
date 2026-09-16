# Generated from AmbiguousExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AmbiguousExprParser import AmbiguousExprParser
else:
    from AmbiguousExprParser import AmbiguousExprParser

# This class defines a complete generic visitor for a parse tree produced by AmbiguousExprParser.

class AmbiguousExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AmbiguousExprParser#root.
    def visitRoot(self, ctx:AmbiguousExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmbiguousExprParser#Add.
    def visitAdd(self, ctx:AmbiguousExprParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmbiguousExprParser#Mul.
    def visitMul(self, ctx:AmbiguousExprParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmbiguousExprParser#Num.
    def visitNum(self, ctx:AmbiguousExprParser.NumContext):
        return self.visitChildren(ctx)



del AmbiguousExprParser