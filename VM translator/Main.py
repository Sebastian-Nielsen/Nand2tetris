from Parser import Parser
from CodeWriter import CodeWriter
from os import listdir, path
import sys, os


class Main:

	def __init__(self, filepath):
		self.cw = CodeWriter(outFile='outFile')
		self.cw.writeInit()

		self.parse_files(filepath)

		print(f"Files that is to be translated: {self.vm_filenames}")

		# Note: filename does not include '.vm'
		for filename in self.vm_filenames:
			self.translate(filename=filename)

		self.cw.close()

	def parse_files(self, filepath):
		"""The filepath can either point to a single file
		or a folder.
		If it points to a single file, then
			self.vm_filenames = [vmFilename]
		else, if it points to a folder, then
			self.vm_filenames = [*all_vm_filenames_in_specified_folder*]
		"""
		if filepath.endswith('.vm'):
			# A single .vm file is to be translated
			vmFile = filepath  # eg. 'fibonacci.vm'
			filename = vmFile.split('.')[0]
			self.vm_filenames = [filename]
			return
		else:
			# All .vm files in the folder is to be translated
			if filepath == '/':
				filepath = os.getcwd()

			all_files = listdir(filepath)

			self.vm_filenames = [
				file.split('.')[0]
				for file in all_files if file.endswith('.vm')
			]
			return

	def translate(self, filename):
		"""!important  >>A CodeWriter (cw) instance
		must be initialized before calling translate<<

		Given the filename of a single file,
		translate the vm commands into Hack
		assembly code and -- using cw -- write
		the assembly code to an .asm file. The name
		of the .asm file was specified when initializing
		the CodeWriter (cw) instance.
		"""
		print(f"Currently translating: '{filename}'")
		parser = Parser(inFile=filename)  # Input file is a .vm file
		self.cw.set_vmFilename(filename=filename)

		while parser.hasMoreCommands():
			curr_cmd = parser.advance()
			curr_cmdType = parser.commandType(curr_cmd)

			if curr_cmdType in ('C_PUSH', 'C_POP'):
				curr_cmdArgs = curr_cmd.split(' ')
				self.cw.writePushPop(
					command=curr_cmdType,
					segment=curr_cmdArgs[1],
					i=curr_cmdArgs[2]
				)
			elif curr_cmdType == 'C_ARITHMETIC':
				self.cw.writeArithmetic(cmd=curr_cmd)
			elif curr_cmdType == 'C_LABEL':
				self.cw.writeLabel(cmd=curr_cmd)
			elif curr_cmdType == 'C_GOTO':
				self.cw.writeGoto(cmd=curr_cmd)
			elif curr_cmdType == 'C_IF':
				self.cw.writeIfgoto(cmd=curr_cmd)
			elif curr_cmdType == 'C_FUNCTION':
				# Eg. 'function SimpleFunction.test 2'
				curr_cmdArgs = curr_cmd.split(' ')
				self.cw.writeFunction(
					functionName=curr_cmdArgs[1],
					numLocals=int(curr_cmdArgs[2])
				)
			elif curr_cmdType == 'C_RETURN':
				self.cw.writeReturn()
			elif curr_cmdType == 'C_CALL':
				# Eg. 'call Bar.mult 2'
				curr_cmdArgs = curr_cmd.split(' ')
				self.cw.writeCall(
					functionName=curr_cmdArgs[1],
					numArgs=curr_cmdArgs[2]
				)

			print('____________')
			print(curr_cmd)
			print(curr_cmdType)


if __name__ == '__main__':
	filepath = sys.argv[1]
	Main(filepath)
