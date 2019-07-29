
class Codewriter:
	def __init__(self, outFile="outFile.asm"):
		self.outFile = open(outFile, 'w')
		self.addresses = self.address_dict()

	#######
	### API

	def writeArithmetic(self, command: str):
		""""""

	def write_push_pop(self,command,segment,i):
		"""
		Writes to the output file the assembly
		code that implements the given command,
		where command is either C_PUSH or C_POP

		:param
		command (C_PUSH or C_POP),
		segment (string), i
		index (int)
		"""
		## 'push constant 2' ##
		# command: 'C_PUSH'   #
		# segment: 'constant' #
		# index: 2            #
		#######################
		if command == 'C_PUSH':
			self.write(f"////////////////////")
			self.write(f"//push {segment} {i}")
			self.write(f"@A")
			self.write(f"D={i}")
			self.write(f"@SP")
			self.write(f"A=M")
			self.write(f"M=D    // *SP={i}")
			self.write(f"")
			self.write(f"@SP")
			self.write(f"M=M+1  // SP++")
		elif command == 'C_POP':
			self.write(f"")
		else:
			self.raise_unknown(command)


	def close(self):
		self.outFile.close()

	### END API
	###########
	def write(self, command):
		self.outFile.write(comand + '\n')

	def resolve_RAMaddress(self, segment, i):
		"""
		Accessing segment i should result in
		accessing RAM[segmentPointer + i]
		"""
		return

	def raise_unknown(self, command):
		raise ValueError(f"{command} is an invalid argument")

	def address_dict(self):
		return {
			'local': 'LCL',  # Base R1
			'argument': 'ARG',  # Base R2
			'this': 'THIS',  # Base R3
			'that': 'THAT',  # Base R4
			'pointer': 3,  # Edit R3, R4
			'temp': 5,  # Edit R5-12
			# R13-15 are free
			'static': 16,  # Edit R16-255
		}

