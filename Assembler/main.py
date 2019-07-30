"""
main.py drives the entire
translation process of the
assembler.
"""
from Parser import Parser

p = Parser(inFile="inFile.vm")

"""Phase one
Remove all comments.
Add all the labels' linenumber
to the symbolTable. NOTE:
Comments and other labels doesn't 
increase the line number.
"""