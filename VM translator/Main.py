from Parser import Parser
from CodeWriter import CodeWriter
import sys
from time import sleep


def translate(filename):
	"""Given the filename of a single file,
	translate the vm commands into Hack
	assembly code and write it to an .asm file.
	"""
	parser = Parser(inFile=filename)  # Input file is a .vm file
	cw = CodeWriter(outFile=filename)  # Outputs to -> {filename}.asm

	while parser.hasMoreCommands():
		curr_cmd = parser.advance()
		curr_cmdType = parser.commandType(curr_cmd)

		if curr_cmdType in ('C_PUSH', 'C_POP'):
			curr_cmdArgs = curr_cmd.split(' ')
			cw.writePushPop(
				command=curr_cmdType,
				segment=curr_cmdArgs[1],
				i=curr_cmdArgs[2]
			)
		elif curr_cmdType == 'C_ARITHMETIC':
			cw.writeArithmetic(cmd=curr_cmd)
		elif curr_cmdType == 'C_LABEL':
			cw.writeLabel(cmd=curr_cmd)
		elif curr_cmdType == 'C_GOTO':
			cw.writeGoto(cmd=curr_cmd)
		elif curr_cmdType == 'C_IF':
			cw.writeIfgoto(cmd=curr_cmd)
		elif curr_cmdType == 'C_FUNCTION':
			# Eg. 'function SimpleFunction.test 2'
			curr_cmdArgs = curr_cmd.split(' ')
			cw.writeFunction(
				functionName=curr_cmdArgs[1],
				numLocals=int(curr_cmdArgs[2])
			)
		elif curr_cmdType == 'C_RETURN':
			cw.writeReturn()
		elif curr_cmdType == 'C_CALL':
			# Eg. 'call Bar.mult 2'
			curr_cmdArgs = curr_cmd.split(' ')
			cw.writeCall(
				functionName=curr_cmdArgs[1],
				numArgs=curr_cmdArgs[2]
			)

		print('____________')
		print(curr_cmd)
		print(curr_cmdType)

	cw.close()


# Should a 'single file' OR 'all files
# within a filepath' be translated?
# The first argument decides!
arg_1 = sys.argv[1]

if arg_1.endswith('.vm'):
	# A single .vm file should be translated
	single_vmFile = arg_1
	filename, _ = single_vmFile.split('.')
	translate(filename=filename)
else:
	# All .vm files within the specified
	# filepath should be translated
	filepath = arg_1
	exit('A filepath is supplied, what now? ... :)')
	...
