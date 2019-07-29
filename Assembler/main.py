"""
main.py drives the entire
translation process of the
assembler.
"""
from Parser import Parser

p = Parser(inFile="inFile.vm")

while p.hasCommands():
	p.advance()

