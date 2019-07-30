import re
comp = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
    }
dest = {
    "null": "000",
    "M": "001",
    "D": "010",
    "A": "100",
    "MD": "011",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
    }
jump = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
    }
# table of symbols used in assembly code, initialized to include
# standard ones
symbolTable = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576,
    }
for i in range(16):
	symbolTable[f"R{i}"] = i
variableTable = {}


def firstPass() -> None:
	"""
	Strip comments & emtpy lines.
	Add Labels to the symbolTable.
	"""
	infile = open("file.asm", "r")
	outfile = open("file1(noWhitespaceAndLabels).tmp", "w")

	lineNumber = 0
	for line in infile:
		line = line.strip()

		# Ignore whitespace;  Don't write them to the new file
		if line == '' or line.startswith("//"):
			continue

		# If inline comment, remove it
		inlineComment = re.search(r'//.*', line)
		if inlineComment:
			line = line[0:inlineComment.span()[0]].strip()
			outfile.write(line + '\n')
			lineNumber += 1
			continue

		# Label
		elif line.startswith("("):
			# Add the jump label to the symbol table.
			label = line[1:-1]
			symbolTable[label] = lineNumber

		else:
			outfile.write(line + '\n')
			lineNumber += 1

	infile.close()
	outfile.close()
	return

def handlePredefinedSymbols():
	infile  = open("file1(noWhitespaceAndLabels).tmp", 'r')
	outfile = open("file2(NoPredefinedSymbols).tmp", 'w')

	for line in infile:
		line = line.strip()
		if line.startswith('@') and line[1:] in symbolTable:
			# The pre-defined symbol's memory address value
			memoryAddress_dec = symbolTable[ line[1:] ]
			memoryAddress_bin = bin(memoryAddress_dec)[2:].zfill(16)
			line = '{}\n'.format( memoryAddress_bin )
			outfile.write(line)
		else:
			outfile.write(line + '\n')

	infile.close()
	outfile.close()
	return

def handleVariables():
	"""
	replace variables with memory addresses
	starting from address 16 and onward.
	If the "variable" "points" to a label
	then
	"""
	infile  = open("file2(NoPredefinedSymbols).tmp", 'r')
	outfile = open("file3(VariablesNowAbinInstructions).tmp", 'w')

	variableCount = 0

	for line in infile:
		line = line.strip()

		# If not an a-instruction
		# (or if the a-instruction is already translated into binary)
		# Skip it
		if not line.startswith('@'):
			outfile.write(line + '\n')
			continue

		# Make sure we are dealing with a variable (@example) and not (@2, @0, or @3)
		if line[1].isdigit():
			outfile.write(line + '\n')
			continue

		# The variabel name is the same as a label
		if line[1:] in symbolTable:
			labelVariable = line[1:]
			# Get the line number of the label
			lineNumber_dec = symbolTable[ labelVariable ]
			lineNumber_bin = bin(lineNumber_dec)[2:].zfill(16)
			outfile.write(lineNumber_bin + '\n')

		else:
			# It is NOT a variable that "points" to a label
			varName = line[1:]
			if varName in variableTable:
				# Variable is already in variableTable
				memoryAddress_dec = variableTable[varName]

			else:
				# Add the variable to variableTable
				memoryAddress_dec = 16 + variableCount
				variableTable[varName] = memoryAddress_dec  # Variables are allocated memory address 16 and onward
				variableCount += 1

			memoryAddress_bin = bin(memoryAddress_dec)[2:].zfill(16)
			outfile.write(memoryAddress_bin + '\n')

	infile.close()
	outfile.close()

def handleAinstructions():
	infile = open("file3(VariablesNowAbinInstructions).tmp", 'r')
	outfile = open("file4(allAinstructions[ASM]convertedToBinary).tmp", 'w')

	for line in infile:
		line = line.strip()

		if not line.startswith('@'):
			outfile.write(line + '\n')
			continue

		memoryAddress_dec = int(line[1:])
		memoryAddress_bin = bin(memoryAddress_dec)[2:].zfill(16)

		outfile.write(memoryAddress_bin + '\n')

	infile.close()
	outfile.close()
	return

def handleCinstructions():
	infile = open("file4(allAinstructions[ASM]convertedToBinary).tmp", 'r')
	outfile = open("file5.hack", 'w')

	for line in infile:
		line = line.strip()

		if not ('=' in line) and not (';' in line):
			# Not a c-instruction; skip line
			outfile.write(line + '\n')
			continue

		dest_asm = comp_asm = jump_asm = 'null'
		if '=' in line: (dest_asm, comp_asm) = line.split('=')
		if ';' in line: (comp_asm, jump_asm) = line.split(';')

		# Construct the c binary machine language command
		cInstruction = f"111{ comp[comp_asm] }{ dest[dest_asm] }{ jump[jump_asm] }"
		outfile.write(cInstruction + '\n')

	infile.close()
	outfile.close()
	return


"""
1. firstPass
Deletes whitespaces and labels. As labels are removed, they
are added to the symbolTable. The label string is the key,
and the value is the linenumber at which the label was declared.
Note that whitespaces are ignored (deleted, so they increase the lineNumber,
neither does previously found labels, as they too are ignored (deleted).  
2. handlePredefinedSymbols
3. 

"""

if __name__ == "__main__":
	# Step 1
	# input:  file.asm
	firstPass()
	# output: file1(noWhitespaceAndLabels).tmp

	# Step 2
	# input:  file1(noWhitespaceAndLabels).tmp
	handlePredefinedSymbols()
	# output: file2(NoPredefinedSymbols).tmp

	# Step 3
	# input:  file2(NoPredefinedSymbols).tmp
	handleVariables()
	# output: file3(VariablesNowAbinInstructions).tmp

	# Step 4
	# input:  file3(VariablesNowAbinInstructions).tmp
	handleAinstructions()
	# output: file4(allAinstructions[ASM]convertedToBinary).tmp

	# Step 5
	# input:  file4(allAinstructions[ASM]convertedToBinary).tmp
	handleCinstructions()
	# output: file5.hack
