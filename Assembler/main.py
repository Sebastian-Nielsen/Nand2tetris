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
def translate_Ainstr_to_bin(a_instr: str) -> str:
	"""Takes an a-instruction as input. Sample inputs:
	:param '@xxx' (Look up associated address of the xxx
								 in the symbolTable and load it to the
								 A-register)
	:param '@204' (Load the constant to the A-register)
	:return 'binary representation of the a-instruction'
	"""
	# Remove '@'
	a_instr = a_instr[1:]

	if re.search(r'^[0-9]+$', a_instr):
		# a_instr is equal to a dec, eg. '@17'
		addr_dec = int(a_instr)
		addr_bin = parser.convertDecToBin(addr_dec)
		return addr_bin

	# Check if the label (@xxx) the xxx part already
	# has an address associated with it.
	if symbolTable.contains(a_instr):
		# The label is already in the symbolTable
		addr_dec = symbolTable.getAddress(a_instr)
		addr_bin = parser.convertDecToBin(addr_dec)
		return addr_bin

	else:
		# The label xxx from the a-instr '@xxx'
		# is not yet in the symbol table.
		# Add it to the symbol table, it must
		# a new variable!

		# Calculate the RAM addr of the var
		i = symbolTable.variablesEncountered
		addr_dec = 16 + i

		# Add the variable to the symbolTable
		symbolTable.add_entry(
			symbol=a_instr,   # eg. 'varName'
			address=addr_dec  # eg.    16
		)
		symbolTable.variablesEncountered += 1

		addr_bin = parser.convertDecToBin(addr_dec)
		return addr_bin
def translate_Cinstr_to_bin(c_instr: str) -> str:
	a = '111'
	c = parser.get_comp_bin(c_instr=c_instr)
	d = parser.get_dest_bin(c_instr=c_instr)
	j = parser.get_jump_bin(c_instr=c_instr)
	c_instr_bin = f"{a}{c}{d}{j}"
	return c_instr_bin

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
		curr_cmd_bin = translate_Cinstr_to_bin(c_instr=curr_cmd)
	elif curr_cmdType == 'A_COMMAND':
		curr_cmd_bin = translate_Ainstr_to_bin(a_instr=curr_cmd)

	# Make sure the curr_cmd_bin is 16 bits long
	curr_cmd_bin = curr_cmd_bin.zfill(16)

	outFile.write(curr_cmd_bin + '\n')