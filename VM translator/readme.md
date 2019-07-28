https://www.coursera.org/learn/nand2tetris2/lecture/qmJl3/unit-1-8-vm-translator-proposed-implementation

#VM Translator Design

- Parser
	| parses each VM cmd into its lexical elements
- CodeWriter
	| writes the assembly code that implements the parsed cmd
- Main
	| drives the process (VMTranslator)
_______________________________________

Main Logic:

Constructs a parser to handle the input file.
Constructs a CodeWriter to handle the output file.
Marches through the input file, parsing each line and
generating code from it.
