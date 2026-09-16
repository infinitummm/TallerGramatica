# Generated from AmbiguousExprAlt.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AmbiguousExprAltParser import AmbiguousExprAltParser
else:
    from AmbiguousExprAltParser import AmbiguousExprAltParser

# This class defines a complete generic visitor for a parse tree produced by AmbiguousExprAltParser.

class AmbiguousExprAltVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AmbiguousExprAltParser#root.
    def visitRoot(self, ctx:AmbiguousExprAltParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmbiguousExprAltParser#Add.
    def visitAdd(self, ctx:AmbiguousExprAltParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmbiguousExprAltParser#Mul.
    def visitMul(self, ctx:AmbiguousExprAltParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AmbiguousExprAltParser#Num.
    def visitNum(self, ctx:AmbiguousExprAltParser.NumContext):
        return self.visitChildren(ctx)



del AmbiguousExprAltParser