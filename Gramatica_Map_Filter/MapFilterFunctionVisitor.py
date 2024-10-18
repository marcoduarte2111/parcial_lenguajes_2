# Generated from MapFilterFunction.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MapFilterFunctionParser import MapFilterFunctionParser
else:
    from MapFilterFunctionParser import MapFilterFunctionParser

# This class defines a complete generic visitor for a parse tree produced by MapFilterFunctionParser.

class MapFilterFunctionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MapFilterFunctionParser#prog.
    def visitProg(self, ctx:MapFilterFunctionParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterFunctionParser#stat.
    def visitStat(self, ctx:MapFilterFunctionParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterFunctionParser#mapFunction.
    def visitMapFunction(self, ctx:MapFilterFunctionParser.MapFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterFunctionParser#filterFunction.
    def visitFilterFunction(self, ctx:MapFilterFunctionParser.FilterFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterFunctionParser#iterable.
    def visitIterable(self, ctx:MapFilterFunctionParser.IterableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterFunctionParser#list.
    def visitList(self, ctx:MapFilterFunctionParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterFunctionParser#tuple.
    def visitTuple(self, ctx:MapFilterFunctionParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterFunctionParser#function.
    def visitFunction(self, ctx:MapFilterFunctionParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterFunctionParser#elements.
    def visitElements(self, ctx:MapFilterFunctionParser.ElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterFunctionParser#lambdaExpr.
    def visitLambdaExpr(self, ctx:MapFilterFunctionParser.LambdaExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterFunctionParser#op.
    def visitOp(self, ctx:MapFilterFunctionParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterFunctionParser#var.
    def visitVar(self, ctx:MapFilterFunctionParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MapFilterFunctionParser#expr.
    def visitExpr(self, ctx:MapFilterFunctionParser.ExprContext):
        return self.visitChildren(ctx)



del MapFilterFunctionParser