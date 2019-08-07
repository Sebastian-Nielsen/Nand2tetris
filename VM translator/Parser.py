import re
class Parser:
	"""
	Handles the parsing of a single .vm file,
	and encapsulates access to the input code.
	It reads VM commands, parses them, and
	provides convenient access to their
	components. In addition, it removes all
	white spaces and comments.
	"""

	def __init__(self, inFile="inFile"):
		self.file = open(f"{inFile}.vm", 'r')
		self.commands = self.commands_dict()

		self.curr_cmd = None
		self.next_cmd = self.getNextCmd()

	#######
	### API
	def hasMoreCommands(self) -> bool:
		return bool(self.next_cmd)

	def advance(self):
		"""The next cmd is now the current.
		Should be called only if hasMoreCommands()
		is true.
		Initially there is no current cmd.
		"""
		self.curr_cmd = self.next_cmd
		self.next_cmd = self.getNextCmd()
		return self.curr_cmd

	def removeCommentsAndStrip(self, line: str) -> str:
		"""Remove all comments in the given line;
		strip() the line.
		:return line [str]
		"""
		line = line.split('//')[0] #Remove inline comment
		line = line.strip()
		return line

	def commandType(self, cmd: str):
		"""Types:
		1. Arithmetic commands - Perform
		arithmetic and logical operations
		on the stack.
		2. Memory access commands - transfer
		data between the stack and virtual
		memory segments.
		3. Label commands -
		4. NOT_YET_ADDED
		http://f.javier.io/rep/books/The%20Elements%20of%20Computing%20Systems.pdf
		page 138
		"""
		cmd_arg0 = self.getArg0(cmd)
		cmd_type = self.commands[cmd_arg0]
		return cmd_type

	### END API
	###########
	def getArg0(self, cmd: str) -> str:
		"""Returns the first argument of the cmd.
	  __________Example___________
		cmd = 'push segment i'
			then,
		return 'push'
		____________________________
		"""
		capture_groups = re.search(r'([\w-]+) *', cmd)
		arg0 = capture_groups.group(1)
		return arg0

	def getArg1(self, cmd: str) -> str:
		"""Returns the second argument of the
		current program.
		________Example________
		cmd = 'push segment i'
			then,
		return 'segment'
		_______________________
		Method should only be called if the
		cmdType of the cmd argument is either
		C_PUSH, C_POP, C_FUNCTION or C_CALL.
		"""
		capture_groups = re.search(r'\w+ *(\w+)', cmd)
		arg1 = capture_groups.group(1)
		return arg1

	def getNextCmd(self):
		"""Read lines from file until
		a cmd is found or the end of
		the file is reached.
		______________________
		If cmd found:
			:return cmd
		else: # End of file reached
			:return None
		"""
		while True:
			line = self.file.readline()

			if line == '':
				# End of the file reached
				return None

			line_cleaned = self.removeCommentsAndStrip(line)

			if line_cleaned == '':
				# The line doesn't contain any cmd.
				# Repeat the loop -> Get a new line.
				continue

			# The 'cleaned line' contains a cmd
			cmd = line_cleaned
			return cmd

	def commands_dict(self):
		return {
			'add': 'C_ARITHMETIC',
			'sub': 'C_ARITHMETIC',
			'neg': 'C_ARITHMETIC',
			'eq': 'C_ARITHMETIC',
			'gt': 'C_ARITHMETIC',
			'lt': 'C_ARITHMETIC',
			'and': 'C_ARITHMETIC',
			'or': 'C_ARITHMETIC',
			'not': 'C_ARITHMETIC',
			'push': 'C_PUSH',
			'pop': 'C_POP',
			'label': 'C_LABEL',
			'goto': 'C_GOTO',
			'if-goto': 'C_IF',
			'function': 'C_FUNCTION',
			'return': 'C_RETURN',
			'call': 'C_CALL'
		}
