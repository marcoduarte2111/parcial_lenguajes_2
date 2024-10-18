import sys
from antlr4 import *
from CalculatorLexer import CalculatorLexer
from CalculatorParser import CalculatorParser
from CalculatorListener import CalculatorListener

class CalculatorEvalListener(CalculatorListener):
    def __init__(self):
        self.stack = []

    def exitExpr(self, ctx):
        if ctx.getChildCount() == 3:  # expr op expr
            right = self.stack.pop()
            left = self.stack.pop()
            op = ctx.getChild(1).getText()

            if op == '+':
                self.stack.append(left + right)
            elif op == '-':
                self.stack.append(left - right)
            elif op == '*':
                self.stack.append(left * right)
            elif op == '/':
                if right == 0:
                    raise ZeroDivisionError("Error: División por cero")
                self.stack.append(left / right)
        else:
            self.stack.append(float(ctx.getText()))

def evaluate(expression):
    input_stream = InputStream(expression)
    lexer = CalculatorLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalculatorParser(token_stream)
    tree = parser.expr()

    listener = CalculatorEvalListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener.stack.pop()

if __name__ == '__main__':
    try:
        expression = input("Ingrese la expresión a evaluar: ")
        result = evaluate(expression)
        print(f"Resultado: {result}")
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(f"Error: {e}")
