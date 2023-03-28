from MyGrammarLexer import MyGrammarLexer
from AST import *
from SemanticAnalysisVisitor import *

def main(argv):
    input_stream = FileStream(argv)
    lexer = MyGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)

    # Create syntax tree
    syntaxTree = parser.prog()
    # Create AST
    ast = AST(syntaxTree)
    # Optimize the AST
    ast.optimize()
    # Create the symbol table
    symbolTable = SemanticAnalysisVisitor()
    # Visit the AST and look for errors
    try:
        symbolTable.visit(ast)
    except IndexError:
        if symbolTable.error == True:
            exit()
        else:
            print("IndexError")
    if symbolTable.error:
        exit()
    # Constant propagation and constant folding
    ast.constantPropagation(dict(), dict(), symbolTable.symbol_table)
    ast.constantFolding(symbolTable.symbol_table)
    # Initialise the symbol table after the constant folding
    ast.initialiseSymbolTable(symbolTable.symbol_table)
    # Print the AST in dot
    ast.printInDot()

    print(symbolTable.symbol_table.symbol_tables)

if __name__ == '__main__':
    main("test.c")