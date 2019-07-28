from Parser import *
from Codewriter import *


parser = Parser(inFile= "inFile.vm")
cw = Codewriter(outFile="outFile.asm")

parser.fileContainsAnInstr()

#############
### Translate

curr_instr = parser.get_nextIstr()

while curr_instr:

	# Handle the instruction
	...



	# Get next instr
	curr_instr = parser.get_nextIstr()

### Translate END
#################

