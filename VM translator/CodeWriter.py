class CodeWriter:
	def __init__(self, outFile="outFile.asm"):
		self.file = open(outFile, 'w')
		self.addresses = self.address_dict()

	#######
	### API
	def writeArithmetic(self, command: str):
		"""
		Writes the assembly code that is the
		translation of the given arithmetic cmd.
		:param command (string),
		"""
		if command == 'add':
			self.write(f"////////////////////")
			self.write(f"// add")
			# After 'self.pop_stack_twice()'
			# SP = SP - 2
			# RAM[13] = top    stack value
			# D       = second stack value
			self.pop_stack_twice()
			# Add RAM[13] and D
			self.write(f"@R13     ")
			self.write(f"D=D+M    ")
			# Push 'D' to the stack
			# (wherever the SP points to)
			self.write(f"@SP     ")
			self.write(f"A=M     ")
			self.write(f"M=D     ")
			self.increment_SP()
		elif command == 'sub':
			self.write(f"////////////////////")
			self.write(f"// sub")
			# After 'self.pop_stack_twice()'
			# SP = SP - 2
			# RAM[13] = top    stack value
			# D       = second stack value
			self.pop_stack_twice()
			# sub RAM[13] from D
			self.write(f"@R13     ")
			self.write(f"D=D-M    ")
			# Push 'D' to the stack
			# (wherever the SP points to)
			self.write(f"@SP     ")
			self.write(f"A=M     ")
			self.write(f"M=D     ")
			self.increment_SP()
		elif command == 'neg':
			self.write(f"////////////////////")
			self.write(f"// neg")
			# After 'self.pop_stack_into_D()'
			# SP = SP - 1
			# D = top stack value
			self.pop_stack_into_D()
			# Negate 'D' -> sub D from 0
			self.write(f"D=-D    ")
			# Push 'D' to the stack
			# (wherever the SP points to)
			self.write(f"@SP     ")
			self.write(f"A=M     ")
			self.write(f"M=D     ")
			self.increment_SP()
		elif command == 'and':
			self.write(f"////////////////////")
			self.write(f"// and")
			# After 'self.pop_stack_twice()'
			# SP = SP - 2
			# RAM[13] = top    stack value
			# D       = second stack value
			self.pop_stack_twice()
			# and "RAM[13] og D"
			self.write(f"@R13     ")
			self.write(f"D=D&M    ")
			# Push 'D' to the stack
			# (wherever the SP points to)
			self.write(f"@SP     ")
			self.write(f"A=M     ")
			self.write(f"M=D     ")
			self.increment_SP()
		elif command == 'or':
			self.write(f"////////////////////")
			self.write(f"// or")
			# After 'self.pop_stack_twice()'
			# SP = SP - 2
			# RAM[13] = top    stack value
			# D       = second stack value
			self.pop_stack_twice()
			# or "RAM[13] og D"
			self.write(f"@R13     ")
			self.write(f"D=D|M    ")
			# Push 'D' to the stack
			# (wherever the SP points to)
			self.write(f"@SP     ")
			self.write(f"A=M     ")
			self.write(f"M=D     ")
			self.increment_SP()
		elif command == 'not':
			self.write(f"////////////////////")
			self.write(f"// not")
			# After 'self.pop_stack_twice()'
			# SP = SP - 2
			# RAM[13] = top    stack value
			# D       = second stack value
			self.pop_stack_into_D()
			# perform 'not' on "D"
			self.write(f"@R13    ")
			self.write(f"D=!D    ")
			# Push 'D' to the stack
			# (wherever the SP points to)
			self.write(f"@SP     ")
			self.write(f"A=M     ")
			self.write(f"M=D     ")
			self.increment_SP()

	def write_push_pop(self, command, segment, i):
		"""
		Writes the assembly code that implements
		the given command to the output file,
		where command is either C_PUSH or C_POP.

		:param command (C_PUSH or C_POP),
		:param segment (string),
		:param i for index (int)
		"""
		## 'push constant 2' ##
		# command: 'C_PUSH'   #
		# segment: 'constant' #
		# index: 2            #
		#######################
		if command == 'C_PUSH':
			if segment == 'constant':
				self.write(f"////////////////////")
				self.write(f"//push {segment} {i}")
				self.write(f"@{i}                ")
				self.write(f"D=A                 ")
				self.write(f"@SP                 ")
				self.write(f"A=M                 ")
				self.write(f"M=D   // *SP = {i}  ")
				self.increment_SP()
				return
			else:
				self.write(f"////////////////////")
				self.write(f"//push {segment} {i}")
				self.write(f"@{segment}          ")
				self.write(f"D=M                 ")
				self.write(f"@{i}                ")
				self.write(f"D=D+A //D=segment+i ")
				self.write(f"                    ")
				self.write(f"@SP                 ")
				self.write(f"A=M                 ")
				self.write(f"M=D    // *SP = D   ")
				self.increment_SP()
				return
		elif command == 'C_POP':
			self.write(f"////////////////////")
			self.write(f"//pop {segment} {i} ")
			self.pop_stack_into_D()
			self.write(f"@R13                ")
			self.write(f"M=D   // M[13]=D    "
			           f"// store popped value"
			            " temporarily in R13 ")
			# LOCAL => '@LCL' => '@1'
			self.write(f"@{self.addresses[segment]}")
			self.write(f"D=M   // baseAddr of"
			           f" {segment}          ")
			self.write(f"@{i}                ")
			self.write(f"D=D+A  //D = address of"
			           f" '{segment} {i}'    ")
			self.write(f"@R14                ")
			self.write(f"M=D                 ")
			self.write(f"@R13                ")
			self.write(f"D=M                 ")
			self.write(f"@R14                ")
			self.write(f"A=M                 ")
			self.write(f"M=D                 ")
		else:
			self.raise_unknown(command)

	def close(self):
		self.file.close()

	### END API
	###########
	def write(self, command):
		self.file.write(command + '\n')

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

	def increment_SP(self):
		self.write("             ")
		self.write("@SP          ")
		self.write("M=M+1  //SP++")
		self.write("             ")

	def decrement_SP(self):
		self.write("             ")
		self.write("@SP          ")
		self.write("M=M-1  //SP--")
		self.write("             ")

	def pop_stack_into_D(self):
		"""Decrements @SP;
		pop from stack into D
		"""
		self.write("@SP          ")
		self.write("M=M-1  //SP--")
		self.write(f"A=M         ")
		self.write(f"D=M  //D=*SP")

	def push_from_D_to_stack(self):
		"""Push the value of D to the stack;
		increment SP
		"""
		self.write(f"@SP        ")
		self.write(f"A=M        ")
		self.write(f"M=D //*SP=D")
		self.increment_SP()

	def pop_stack_twice(self):
		"""
		Decrement SP;
		Pop from stack into @R13;
		Decrement SP;
		Pop from stack into D;
		________ :RESULT: _________
		RAM[13] = top    stack value
		D       = second stack value
		"""
		self.decrement_SP()
		self.write(f"@SP         ")
		self.write(f"A=M         ")
		self.write(f"D=M  //D=*SP")
		self.write(f"@R13        ")
		self.write(f"M=D         ")
		self.decrement_SP()
		self.write(f"@SP         ")
		self.write(f"A=M         ")
		self.write(f"D=M  //D=*SP")
