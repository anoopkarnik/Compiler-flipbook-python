from lex import *
from emit import *
from parser import *
import sys

def main():
    print("Flip book Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()

    lexer = Lexer(input)
    emitter = Emitter("out.py")
    parser = Parser(lexer, emitter)

    parser.program()
    emitter.writeFile()
    print("Compiling completed.")

main()
