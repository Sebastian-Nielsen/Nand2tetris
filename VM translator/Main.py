from Parser import Parser
from CodeWriter import CodeWriter
import sys

# Don't include the file name of the currently
# running file, namely, "..fullPath../main.py"
# args = sys.argv[1:]
# print(args)
# exit()

parser = Parser(inFile ="inFile.vm"  )
cw = CodeWriter(outFile="outFile.asm")


while parser.hasMoreCommands():
	curr_cmd = parser.advance()
	curr_cmdType = parser.commandType(curr_cmd)

	if curr_cmdType in ('C_PUSH', 'C_POP'):
		curr_cmdArgs = curr_cmd.split(' ')
		cw.write_push_pop(
			command=curr_cmdType,
			segment=curr_cmdArgs[1],
			i=curr_cmdArgs[2]
		)
	elif curr_cmdType == 'C_ARITHMETIC':
		cw.writeArithmetic(command=curr_cmd)


	print('____________')
	print(curr_cmd)
	print(curr_cmdType)

cw.close()