# Generated from LaplaceTransform.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceTransformParser import LaplaceTransformParser
else:
    from LaplaceTransformParser import LaplaceTransformParser

# This class defines a complete listener for a parse tree produced by LaplaceTransformParser.
class LaplaceTransformListener(ParseTreeListener):

    # Enter a parse tree produced by LaplaceTransformParser#program.
    def enterProgram(self, ctx:LaplaceTransformParser.ProgramContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#program.
    def exitProgram(self, ctx:LaplaceTransformParser.ProgramContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#statement.
    def enterStatement(self, ctx:LaplaceTransformParser.StatementContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#statement.
    def exitStatement(self, ctx:LaplaceTransformParser.StatementContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:LaplaceTransformParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:LaplaceTransformParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#expression.
    def enterExpression(self, ctx:LaplaceTransformParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#expression.
    def exitExpression(self, ctx:LaplaceTransformParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#laplaceTransform.
    def enterLaplaceTransform(self, ctx:LaplaceTransformParser.LaplaceTransformContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#laplaceTransform.
    def exitLaplaceTransform(self, ctx:LaplaceTransformParser.LaplaceTransformContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#additionExpression.
    def enterAdditionExpression(self, ctx:LaplaceTransformParser.AdditionExpressionContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#additionExpression.
    def exitAdditionExpression(self, ctx:LaplaceTransformParser.AdditionExpressionContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#multiplicationExpression.
    def enterMultiplicationExpression(self, ctx:LaplaceTransformParser.MultiplicationExpressionContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#multiplicationExpression.
    def exitMultiplicationExpression(self, ctx:LaplaceTransformParser.MultiplicationExpressionContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#powerExpression.
    def enterPowerExpression(self, ctx:LaplaceTransformParser.PowerExpressionContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#powerExpression.
    def exitPowerExpression(self, ctx:LaplaceTransformParser.PowerExpressionContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#atom.
    def enterAtom(self, ctx:LaplaceTransformParser.AtomContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#atom.
    def exitAtom(self, ctx:LaplaceTransformParser.AtomContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#functionCall.
    def enterFunctionCall(self, ctx:LaplaceTransformParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#functionCall.
    def exitFunctionCall(self, ctx:LaplaceTransformParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by LaplaceTransformParser#parameter.
    def enterParameter(self, ctx:LaplaceTransformParser.ParameterContext):
        pass

    # Exit a parse tree produced by LaplaceTransformParser#parameter.
    def exitParameter(self, ctx:LaplaceTransformParser.ParameterContext):
        pass



del LaplaceTransformParser