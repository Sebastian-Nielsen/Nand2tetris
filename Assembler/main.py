from SymbolTable import SymbolTable
from Parser import Parser
import re
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
		if line.startswith('('):
			line = line.strip()
			# We only care about the label
			# inbetween the paranthesis (XXX)
			label = line[1:-1]
			symbolTable.add_entry(
				symbol=label,
				address=lineNumber
			)
		elif parser.removeCommentsAndStrip(line=line) != '':
			lineNumber += 1
	# Remember to reset the file reader cursor
	file.seek(0)
	return

"""
main.py drives the entire
translation process of the
assembler.
"""
parser = Parser(inFile="inFile.asm")
symbolTable = SymbolTable()


#############
# FIRST PHASE
first_pass(parser.file)

#############
# SECOND PASS
outFile = open('outFile.hack', 'w')

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
		# Remove '@'
		curr_cmd = curr_cmd[1:]

		# If it's a decimal; convert it to bin
		if re.search(r'^[0-9]+$', curr_cmd):
			curr_cmd_bin = parser.convertDecToBin(
				dec=int(curr_cmd)
			)

		# Check if it's a label/variable that already
		# has an address associated with it
		elif symbolTable.contains(curr_cmd):
			# The label is already in the symbolTable
			addr_dec = symbolTable.getAddress(curr_cmd)
			addr_bin = parser.convertDecToBin(dec=addr_dec)
			curr_cmd_bin = addr_bin
		else:
			# The label is of a new variable not
			# yet added to the symbolTable.

			# Calculate the RAM addr of the var
			i = symbolTable.variablesEncountered
			addr_dec = 16 + i

			# Add the variable to the symbolTable
			symbolTable.add_entry(
				symbol=curr_cmd,
				address=addr_dec
			)
			symbolTable.variablesEncountered += 1

			addr_bin = parser.convertDecToBin(dec=addr_dec)
			curr_cmd_bin = addr_bin

	# Make sure the curr_cmd_bin is 16 bits long
	curr_cmd_bin = curr_cmd_bin.zfill(16)

	outFile.write(curr_cmd_bin + '\n')
	# print(parser.curr_cmd)
	# print(f"Machine language equivalent:   {curr_cmd_bin}")
