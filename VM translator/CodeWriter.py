class CodeWriter:
	def __init__(self, outFile="outFile"):
		self.file = open(f"{outFile}.asm", 'w')
		self.addresses = self.address_dict()
		self.filename = None  # filename of vm file that is being translated
		self.bool_count = 0
		self.returnAddr_count = 0 # number of return addresses created so far
		self.DEBUG_lineNumber = 0  # Solely for debugging purposes


	def set_vmFilename(self, filename: str):
		"""Before running any of the CodeWriter's API methods,
		the filename of the currently focused .vm file that is
		about to get translated into .asm should be set.
		This is important, as the filename of the .vm file is
		used when creating unique labels.
		"""
		self.write(f"/////////////////////////////////////////////")
		self.write(f"// FILE: {filename}                          ")
		self.filename = filename

	#######
	### API
	def writeInit(self):
		"""
		The first VM function that starts executing
		should be sys.init.
		1. Initialize the stack pointer to addr 256
		2. Starts executing (the translated code of) sys.init
		"""
		self.write('@256')
		self.write('D=A')
		self.write('@SP')
		self.write('M=D')
		self.writeCall('Sys.init', numArgs=0)

	def writeArithmetic(self, cmd: str):
		"""
		Writes the assembly code that is the
		translation of the given arithmetic cmd.
		:param cmd (string),
		"""
		self.write(f"////////////////////")
		self.write(f"//{cmd}")

		self.pop_stack_into_D()  # Top value of stack (y) (D)
		if cmd not in ('neg', 'not'):
			self.pop_stack_into_A()  # Second value of stack (x) (A)

		if cmd == 'add':  # Arithmetic operators
			self.write("D=A+D")
		elif cmd == 'sub':
			self.write('D=A-D')
		elif cmd == 'neg':
			self.write('D=-D')

		elif cmd in ('lt', 'eq', 'gt'):  # Boolean operators
			############# Remember #############
			# Top    value of stack (y) or (D) #
			# Second value of stack (x) or (A) #
			self.write("D=A-D")

			i = self.bool_count
			self.write(f"@Bool_{i}_TRUE")

			if cmd == 'lt':  # (x < y) aka (x-y < 0)
				self.write("D;JLT")
			elif cmd == 'eq':  # (x==y) aka (x-y==0)
				self.write("D;JEQ")
			elif cmd == 'gt':  # (x > y) aka (x-y > 0)
				self.write("D;JGT")

			self.write(f"D=0             ")
			self.write(f"@Bool_{i}_FALSE ")
			self.write(f"0;JMP           ")
			self.write(f"(Bool_{i}_TRUE) ")
			self.write(f"D=-1            ")
			self.write(f"(Bool_{i}_FALSE)")
			self.bool_count += 1

		elif cmd == 'and':
			self.write('D=A&D')
		elif cmd == 'or':
			self.write('D=A|D')
		elif cmd == 'not':
			self.write('D=!D')

		# 'self.push_D_to_stack()' also
		# takes care of incrementing SP
		self.push_D_to_stack()

	def writePushPop(self, command, segment, i):
		"""
		Writes the assembly code that implements
		the given command to the output file,
		where command is either C_PUSH or C_POP.

		:param command (C_PUSH or C_POP),
		:param segment (string),
		:param i for index (int)
		________Example_________
		## 'push constant 2' ##
		# command: 'C_PUSH'   #
		# segment: 'constant' #
		# index: 2            #
		#######################
		"""
		self.write(f"////////////////////")
		self.write(f"//{command} {segment} {i}")

		self.resolve_address(segment, i)
		# The A-register is now resolved to hold
		# the address that corresponds to that of
		# the given {segment} and {i}.

		if command == 'C_PUSH':
			if segment == 'constant':
				# The >A-register< holds a constant.
				self.write('D=A')
				self.push_D_to_stack()
				return
			else:
				# The >A-register< holds the address that holds
				# the value we want to push to the stack.
				self.write('D=M')
				self.push_D_to_stack()
				return

		elif command == 'C_POP':
			# The >A-register< holds the address to which we
			# want to store the current top value of the stack.

			# Store the address that is in the A-register in a
			# temporariy memory location: R13
			self.write('D=A')
			self.write('@R13')
			self.write('M=D')

			# Pop the top value of the stack
			self.pop_stack_into_D()

			self.write('@R13')
			self.write('A=M')
			self.write('M=D')
			return
		else:
			self.raise_unknown(command)

	def writeLabel(self, cmd):
		"""Given a vm cmd, like:
		cmd = 'label LOOP_START'
		write the assembly equivalent
		to the asm file:
		(LOOP_START)
		"""
		args = cmd.split(' ')
		labelName = args[1]
		self.write(f"////////////////////")
		self.write(f"// {cmd}")
		self.write(f"({self.filename}${labelName})")

	def writeGoto(self, cmd):
		"""
		'goto returnAddress'
		"""
		args = cmd.split(' ')
		labelName = args[1]
		self.write(f'////////////////////')
		self.write(f'// {cmd}')
		self.write(f'@{self.filename}${labelName}')
		self.write('0;JMP')

	def writeIfgoto(self, cmd):
		"""The stacks topmost value is popped; if the
		value is not zero, execution continues from the
		location marked by the label; otherwise, execution
		continues from the next command in the program.
		"""
		args = cmd.split(' ')
		labelName = args[1]
		self.write(f'////////////////////')
		self.write(f'// {cmd}')
		self.pop_stack_into_D()
		self.write(f'@{self.filename}${labelName}')
		self.write('D;JNE')

	def writeFunction(self, functionName: str, numLocals: int):
		"""Given a command like:
		function Foo.main 4
		function {functionName} {numLocals}
		"""
		self.write(f"////////////////////")
		self.write(f"// function {functionName} {numLocals}")
		# Declaress a label for the function entry
		self.write(f"({functionName})")  
		# nVars = number of local variables
		# Initializes the local variables to 0
		for _ in range(numLocals):
			self.write('D=0')  # 'Push 0'
			self.push_D_to_stack()

	def writeReturn(self):
		"""We need to restore the state of the caller.
		This involves changing the SP, LCL, ARG, THIS, THAT
		to what it were before the currently running function
		were called.
		_____________________
		endFrame=LCL
		retAddr=*(endFrame-5)
		*ARG=pop()
		SP=ARG+1
		THAT=*(endFrame-1)
		THIS=*(endFrame-2)
		ARG =*(endFrame-3)
		LCL =*(endFrame-4)
		goto retAddr
		"""
		self.write(f"////////////////////")
		self.write(f"// return")
		endFrame = 'R13'
		RET = 'R14'

		### endFrame=LCL
		self.write(f"@LCL")
		self.write(f"D=M")
		self.write(f"@{endFrame}")
		self.write(f"M=D")  # endFrame=M[@LCL]

		### retAddr = *(endFrame-5)
		# Get the return-address
		self.write(f"@{endFrame}")
		self.write(f"D=M")
		self.write(f"@5")
		self.write(f"A=D-A")  # A=(endFrame-5)
		self.write(f"D=M")  # D=M[(endFrame-5)]
		# NOTE: D is now equal to the line number of the
		# return-label that is positioned just after the
		# call cmd to the currently executing function.
		# This is the place we want to jump to, when we
		# are done restoring the state of the caller.
		self.write(f"@{RET}")
		self.write(f"M=D")

		### *ARG=pop()
		self.pop_stack_into_D()
		self.write('@ARG')
		self.write('A=M')
		self.write('M=D')

		### SP=ARG+1
		self.write('@ARG')
		self.write('D=M')
		self.write('@SP')
		self.write('M=D+1')

		i = 1
		for addr in ('@THAT', '@THIS', '@ARG', '@LCL'):
			### {addr}=*(endFrame-{i})
			# Restore {addr} of the caller
			self.write(f"@{endFrame}")
			self.write(f"D=M")
			self.write(f"@{i}")
			self.write(f"D=D-A")  # D=(endFrame-{i})
			self.write(f"A=D")  # A=(endFrame-{i})
			self.write(f"D=M")  # D=*(endFrame-{i})
			self.write(addr)
			self.write(f"M=D")  # RAM[{addr}]=*(endFrame-{i})
			i += 1

		self.write(f"@{RET}")
		self.write(f"A=M")
		self.write(f"0;JMP")

	def writeCall(self, functionName: str, numArgs: int):
		"""
		# The argument {numArgs} informs us that
		# n arguments have been pushed onto the stack.
		# So, we know how many values on the stack should
		# be treated as arguments.
	
		call Bar.mult 2
		call {functionName} {numArgs}
		"""
		self.write(f"////////////////////")
		self.write(f"// call {functionName} {numArgs}")
		
		# Unique return label
		a = self.filename
		b = self.returnAddr_count
		rtrnAddrLabel = f"{a}.RET_{b}"
		# '@rtrnAddrLabel' = '{lineAtWhichLabel: (rtrnAddrLabel) was declared}'
		# eg.    '@rtrnAddrLabel' = '@4'  (declared at line 4)

		self.returnAddr_count += 1

		# Push returnAddressLabel
		self.write(f"@{rtrnAddrLabel}")  # A is equal to the
		self.write(f"D=A")  # line number of the (rtrnAddrLabel)
		self.push_D_to_stack()

		# Save the caller's state
		# Saves LCL, ARG, ..., of the caller
		for addr in ('@LCL', '@ARG', '@THIS', '@THAT'):
			self.write(addr)
			self.write('D=M')
			self.push_D_to_stack()

		# Reposition ARG
		self.write(f'@SP       ')
		self.write(f'D=M       ')  # D=RAM[SP]
		self.write(f'@5        ')
		self.write(f'D=D-A     ')  # D-=5
		self.write(f'@{numArgs}')
		self.write(f'D=D-A     ')  # D-={numArgs}
		self.write(f'@ARG      ')
		self.write(f'M=D       ')  # RAM[ARG]=D

		# Reposition LCL
		self.write('@SP ')
		self.write('D=M ')
		self.write('@LCL')
		self.write('M=D ')  # RAM[LCL]=RAM[SP]

		# Transfer control to the called function (goto {functionName})
		# (It is important not to call "self.writeGoto", as it will prepend
		# {self.filename}$, which we do not want!)
		self.write(f"@{functionName}")
		self.write(f"0;JMP")

		# Declare a label for the return-address
		self.write(f"({rtrnAddrLabel})")

	def close(self):
		self.file.close()

	### END API
	###########
	def resolve_address(self, segment, index):
		"""Given 'segment' and 'index' (i);
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
		# Get the predefined address string or
		# the associated address baseAddr number
		# of the segment.
		address = self.addresses.get(segment)

		if segment == 'constant':
			self.write(f"@{index}")
			return

		elif segment in ('local', 'argument', 'this', 'that'):
			# {address} is as string
			self.write(f"@{address}")
			self.write(f'D=M       //baseAddr of {segment} ')
			self.write(f'@{index}                          ')
			self.write('A=D+A                              ')
			return

		elif segment in ('pointer', 'temp'):
			# {address} is an int
			self.write(f"@{address + int(index)}")
			self.write(f'D=A   // baseAddr of {segment}')
			return

		elif segment in ('static'):
			self.write(f'@{self.filename}.{index}')
			return

		else:
			self.raise_unknown(segment)

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
		if command.strip().startswith('//') or command.strip() == '':
			self.file.write(command + '\n')
			return

		self.file.write(command + '//' + str(self.DEBUG_lineNumber) + '\n')
		if not command.startswith('('):
			self.DEBUG_lineNumber += 1

	def raise_unknown(self, command):
		raise ValueError(f"{command} is an invalid argument")

	def increment_SP(self):
		self.write("@SP          ")
		self.write("M=M+1  //SP++")

	def decrement_SP(self):
		self.write("@SP          ")
		self.write("M=M-1  //SP--")

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

	def push_D_to_stack(self):
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
		Pop from stack into @R5;
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
		self.write(f"@R5        ")
		self.write(f"M=D         ")
		self.decrement_SP()
		self.write(f"@SP         ")
		self.write(f"A=M         ")
		self.write(f"D=M  //D=*SP")
