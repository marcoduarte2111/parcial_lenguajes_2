# Generated from Calculator.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete listener for a parse tree produced by CalculatorParser.
class CalculatorListener(ParseTreeListener):

    # Enter a parse tree produced by CalculatorParser#expr.
    def enterExpr(self, ctx:CalculatorParser.ExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#expr.
    def exitExpr(self, ctx:CalculatorParser.ExprContext):
        pass



del CalculatorParser