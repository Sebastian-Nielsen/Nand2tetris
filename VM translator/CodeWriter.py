class CodeWriter:
	def __init__(self, outFile="outFile.asm"):
		self.file = open(outFile, 'w')
		self.addresses = self.address_dict()
		self.boolean_count = 0

	#######
	### API
	def writeArithmetic(self, command: str):
		"""
		Writes the assembly code that is the
		translation of the given arithmetic cmd.
		:param command (string),
		"""
		self.write(f"////////////////////")
		self.write(f"//{command}")

		self.pop_stack_into_D()  # Top value of stack (y) (D)
		if command not in ('neg', 'not'):
			self.pop_stack_into_A()  # Second value of stack (x) (A)

		if command == 'add':  # Arithmetic operators
			self.write("D=A+D")
		elif command == 'sub':
			self.write('D=A-D')
		elif command == 'neg':
			self.write('D=-D')

		elif command in ('lt', 'eq', 'gt'):  # Boolean operators
			############# Remember #############
			# Top    value of stack (y) or (D) #
			# Second value of stack (x) or (A) #
			self.write("D=A-D")

			i = self.boolean_count
			self.write(f"@Bool_{i}_TRUE")

			if command == 'lt':  # (x < y) aka (x-y < 0)
				self.write("D;JLT")
			elif command == 'eq':  # (x==y) aka (x-y==0)
				self.write("D;JEQ")
			elif command == 'gt':  # (x > y) aka (x-y > 0)
				self.write("D;JGT")

			self.write(f"D=0             ")
			self.write(f"@Bool_{i}_FALSE ")
			self.write(f"0;JMP           ")
			self.write(f"(Bool_{i}_TRUE) ")
			self.write(f"D=-1            ")
			self.write(f"(Bool_{i}_FALSE)")
			self.boolean_count += 1

		elif command == 'and':
			self.write('D=A&D')
		elif command == 'or':
			self.write('D=A|D')
		elif command == 'not':
			self.write('D=!D')

		# 'self.push_from_D_to_stack()' also
		# takes care of incrementing SP
		self.push_from_D_to_stack()

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
				self.write(f"@{self.addresses[segment]}")

				self.resolve_address(segment)

				self.write(f"@{i}                ")
				self.write(f"A=D+A //D=segment+i ")  # D=300
				self.write(f"D=M                 ")  # D= R[300]
				self.write(f"                    ")
				self.write(f"@SP                 ")
				self.write(f"A=M                 ")
				self.write(f"M=D    // *SP = D   ")
				self.increment_SP()
				return
		elif command == 'C_POP':
			self.write(f"////////////////////")
			self.write(f"//pop {segment} {i} ")

			# SP--; D=*SP
			self.pop_stack_into_D()

			self.write(f"@R13                ")
			self.write(f"M=D                 "
			           "// store popped value"
			           " temporarily in R13  ")

			self.write(f"@{self.addresses[segment]}"
			           f"  //eg. LOCAL=>@LCL=>@1   ")

			self.resolve_address(segment)

			self.write(f"@{i}                ")
			self.write(f"D=D+A  //D = address of '{segment} {i}'")
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
	def resolve_address(self, segment):
		"""Given 'segment' and 'i';
		- if the value of the segment is a
		pointer to another address -->
		:return *(segment+i)    // this might not be
		- if not,               // accurate don't believe it
		:return RAM[segment+i]

		___________Explanation_____________
		Not all of the first 16 reservered
		addresses in the RAM stores a pointer
		to the base address of their associated
		memory segment; only the first five:
		('SP', 'LCL', 'ARG', 'THIS', 'THAT'), aka.
		('R0', 'R1' , 'R2' , 'R3'  , 'R4'  ).

		The rest ('R5', ..., 'R15') does not.

		When getting a command like:
		'push segment i'

		We need to be aware of whether the segment
		stores a pointer (like the first five) or
		not (like the last 11 reserved addresses).
		"""
		# TODO We haven't handled "pointer" -- I don't know what that is. Look it up in address_dict
		if segment in ('local', 'argument', 'this', 'that'):
			self.write(f"D=M   // baseAddr of {segment}")
		else:
			self.write(f"D=A   // baseAddr of {segment}")

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

	def write(self, command):
		self.file.write(command + '\n')

	def raise_unknown(self, command):
		raise ValueError(f"{command} is an invalid argument")

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

	def pop_stack_into_A(self):
		"""Decrements @SP;
		pop from stack into A
		"""
		self.write("@SP          ")
		self.write("M=M-1  //SP--")
		self.write(f"A=M         ")
		self.write(f"A=M  //A=*SP")

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
