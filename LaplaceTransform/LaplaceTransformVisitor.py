# Generated from LaplaceTransform.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceTransformParser import LaplaceTransformParser
else:
    from LaplaceTransformParser import LaplaceTransformParser

# This class defines a complete generic visitor for a parse tree produced by LaplaceTransformParser.

class LaplaceTransformVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LaplaceTransformParser#program.
    def visitProgram(self, ctx:LaplaceTransformParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#statement.
    def visitStatement(self, ctx:LaplaceTransformParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:LaplaceTransformParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#expression.
    def visitExpression(self, ctx:LaplaceTransformParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#laplaceTransform.
    def visitLaplaceTransform(self, ctx:LaplaceTransformParser.LaplaceTransformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#additionExpression.
    def visitAdditionExpression(self, ctx:LaplaceTransformParser.AdditionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#multiplicationExpression.
    def visitMultiplicationExpression(self, ctx:LaplaceTransformParser.MultiplicationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#powerExpression.
    def visitPowerExpression(self, ctx:LaplaceTransformParser.PowerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#atom.
    def visitAtom(self, ctx:LaplaceTransformParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#functionCall.
    def visitFunctionCall(self, ctx:LaplaceTransformParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceTransformParser#parameter.
    def visitParameter(self, ctx:LaplaceTransformParser.ParameterContext):
        return self.visitChildren(ctx)



del LaplaceTransformParser