def first_pass(file):
	""":param Takes a file that is
	already opened in read mode.
	_________Descrip_________
	Iterates through all lines,
	whenever a label is found;
	add it to the symbol table.
	"""
	lineNumber = 0
	for line in file.readlines():
		if line.startswidth('('):
			line = line.strip()
			# We only care about the label
			# inbetween the paranthesis (XXX)
			label = line[1:-1]
			SymbolTable[label] = lineNumber

		lineNumber += 1
	# Remember to reset the file reader cursor
	file.seek(0)
	return
"""
main.py drives the entire
translation process of the
assembler.
"""
from Parser import Parser
from SymbolTable import SymbolTable

p = Parser(inFile="inFile.vm")
symbolTable = SymbolTable()

"""Phase one
Go through all lines; whenever
a label is found; add it to 
the symbol table. 
"""
first_pass(p.file)


#############
# SECOND PASS

while parser.hasMoreCommands():
	# Set 'next_cmd' to 'curr_cmd'
	curr_cmd = parser.advance()
	curr_cmdType = parser.commandType(curr_cmd)

	if curr_cmdType == 'C_COMMAND':
		a = '111'
		c = parser.get_comp_bin(c_instr=curr_cmd)
		d = parser.get_dest_bin(c_instr=curr_cmd)
		j = parser.get_jump_bin(c_instr=curr_cmd)
		curr_cmd_bin = f"{a}{c}{d}{j}"

	elif curr_cmdType == 'A_COMMAND':
		# Check if it's a label that already
		# has an address associated with it
		if symbolTable.contains(curr_cmd):
			# Remove the '@'
			curr_cmd = curr_cmd[1:]
			# The label is already in the symbolTable
			addr = symbolTable.getAddress(curr_cmd)
			curr_cmd_bin = f"@{addr}"
		else:
			# The label is of a new variable not
			# yet added to the symbolTable.
			i = symbolTable.variablesEncountered
			symbolTable.add_entry(
				symbol=curr_cmd,
				addr=16 + i
			)

	elif curr_cmdType == 'L_COMMAND':
		...

	print(parser.curr_cmd)
	print(parser.commandType(parser.curr_cmd))
	print(f"Machine language equivalent:   {curr_cmd_bin}")
	print('__________________')
