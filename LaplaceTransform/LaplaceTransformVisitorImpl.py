from LaplaceTransformVisitor import LaplaceTransformVisitor
from LaplaceTransformParser import LaplaceTransformParser
import sympy as sp

class LaplaceTransformVisitorImpl(LaplaceTransformVisitor):
    def __init__(self):
        self.variables = {}
    
    def visitProgram(self, ctx: LaplaceTransformParser.ProgramContext):
        return [self.visit(statement) for statement in ctx.statement()]

    def visitFunctionDeclaration(self, ctx: LaplaceTransformParser.FunctionDeclarationContext):
        # Funciones personalizadas no son necesarias en este ejemplo, se pueden implementar si se requiere
        pass

    def visitExpression(self, ctx: LaplaceTransformParser.ExpressionContext):
        if ctx.laplaceTransform():
            return self.visit(ctx.laplaceTransform())
        return self.visit(ctx.additionExpression())

    def visitLaplaceTransform(self, ctx: LaplaceTransformParser.LaplaceTransformContext):
        expr = self.visit(ctx.additionExpression())
        t = sp.symbols('t')
        s = sp.symbols('s')
        return sp.laplace_transform(expr, t, s, noconds=True)

    def visitAdditionExpression(self, ctx: LaplaceTransformParser.AdditionExpressionContext):
        left = self.visit(ctx.multiplicationExpression(0))
        for i in range(1, len(ctx.multiplicationExpression())):
            right = self.visit(ctx.multiplicationExpression(i))
            if ctx.getChild(2 * i - 1).getText() == '+':
                left += right
            else:
                left -= right
        return left

    def visitMultiplicationExpression(self, ctx: LaplaceTransformParser.MultiplicationExpressionContext):
        left = self.visit(ctx.powerExpression(0))
        if left is None:  # Verificar si left es válido
            return None

        for i in range(1, len(ctx.powerExpression())):
            right = self.visit(ctx.powerExpression(i))
            if right is None:  # Verificar si right es válido
                continue
            if ctx.getChild(2 * i - 1).getText() == '*':
                left *= right
            else:
                left /= right
        return left

    def visitPowerExpression(self, ctx: LaplaceTransformParser.PowerExpressionContext):
        base = self.visit(ctx.atom(0))
        if ctx.atom(1) is not None:
            exponent = self.visit(ctx.atom(1))
            return base ** exponent
        return base

    def visitAtom(self, ctx: LaplaceTransformParser.AtomContext):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        elif ctx.ID():
            name = ctx.ID().getText()
            return sp.symbols(name)
        elif ctx.getChildCount() == 3:  # '(' expr ')'
            return self.visit(ctx.additionExpression())
        elif ctx.MINUS():
            return -self.visit(ctx.atom())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        return None  # Manejo de caso en que no se obtiene ningún valor

    def visitFunctionCall(self, ctx: LaplaceTransformParser.FunctionCallContext):
        func_name = ctx.ID().getText()
        args = [self.visit(arg) for arg in ctx.additionExpression()]

        if func_name == "sin":
            return sp.sin(*args)
        elif func_name == "cos":
            return sp.cos(*args)
        elif func_name == "tan":
            return sp.tan(*args)
        else:
            raise ValueError(f"Función no soportada: {func_name}")
