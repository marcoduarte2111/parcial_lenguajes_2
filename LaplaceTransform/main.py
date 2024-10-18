import sys
from antlr4 import *
from LaplaceTransformLexer import LaplaceTransformLexer
from LaplaceTransformParser import LaplaceTransformParser
from LaplaceTransformVisitorImpl import LaplaceTransformVisitorImpl

def main():
    # Lee la expresión desde la consola
    input_stream = InputStream(input("Ingrese una expresión para calcular su transformada de Laplace: "))

    # Configura el lexer y el parser
    lexer = LaplaceTransformLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LaplaceTransformParser(stream)
    tree = parser.program()

    # Visita el árbol sintáctico para calcular la transformada de Laplace
    visitor = LaplaceTransformVisitorImpl()
    result = visitor.visit(tree)

    # Imprime el resultado
    print("Transformada de Laplace:", result)

if __name__ == '__main__':
    main()
