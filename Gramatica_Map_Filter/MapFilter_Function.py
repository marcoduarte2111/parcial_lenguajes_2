import sys
from antlr4 import *
from MapFilterFunctionLexer import MapFilterFunctionLexer
from MapFilterFunctionParser import MapFilterFunctionParser
from MapFilterFunctionVisitor import MapFilterFunctionVisitor

from Visitor import Visitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = MapFilterFunctionLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MapFilterFunctionParser(token_stream)
    tree = parser.prog()

    #lisp_tree_str = tree.toStringTree(recog=parser)
    #print(lisp_tree_str)

    visitor = Visitor()
    visitor.visit(tree)
