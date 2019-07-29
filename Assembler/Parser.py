"""
The main function of the parser is to
break each assembly command into its
underlying componets (fields and symbols).
The APIs is as follows.

PARSER: Encapsulates access to the input code.
Reads an assembly language command, parses it,
and provides convient access to the command's
components (fields and symbols). In addition,
removes all white space and comments.

List of instructions
http://f.javier.io/rep/books/The%20Elements%20of%20Computing%20Systems.pdf
GOTO p. 138
"""

class Parser:
	def __init__(self, inFile="inFile.vm"):
		self.file = open(inFile, 'r')
		self.curr_cmd = None
		self.next_cmd = None

	#######
	### API

	def hasMoreCommands(self) -> bool:
		"""
		1. There are more commands;
		self.curr_cmd have been updated
		:return True
		2. There are no more commands;
		self.curr_cmd is None
		:return False
		"""
		# print(f'Before next_cmd: {self.next_cmd}')
		self.next_cmd = self.getNextCmd()
		# print(f'After next_cmd: {self.next_cmd}')
		return bool(self.next_cmd)

	def advance(self):
		"""Reads the next cmd from the
		input and makes it the current
		command. Should be called only
		if hasMoreCommands() is true.
		Initially there is no current cmd.
		"""
		self.curr_cmd = self.next_cmd
		self.next_cmd = None

	def commandType(self, cmd: str):
		"""Types:
		1. 'A_COMMAND' for @xxx where
		xxx is either a symbol or a
		decimal number.
		2. 'C_COMMAND' for dest=comp;jump
		3. 'L_COMMAND' (actually, pseudo-
		command) for (xxx) where xxx is a
		symbol.
		:return command type [str]
		"""
		if cmd.startswith('@'):
			return 'A_COMMAND'
		elif cmd.startswith('('):
			return 'L_COMMAND'
		elif ('=' in cmd) or (';' in cmd):
			return 'C_COMMAND'
		else:
			raise ValueError('Unknown cmd encountered')

	def symbol(self):
		...

	### API END
	###########
	def getNextCmd(self):
		"""
		Who calls this method?
		-> hasMoreCommands(self)
		_______DESCRIP________
		Read lines continuesly until
		a cmd is found or the end of
		the file is reached.
		______________________
		If cmd found:
			self.next_cmd = cmd
			:return cmd
		else:
			# End of file reached
			self.next_cmd = None
			:return None
		"""
		while True:
			line = self.getNextLine()

			if line is None:
				# We have reached the
				# end of the file
				return None

			line_cleaned = self.removeCommentsAndStrip(line)

			if line_cleaned == '':
				# The line doesn't contain any cmd
				# Repeat the loop -> get a new line
				continue

			# The 'cleaned line' must be a command
			command = line_cleaned
			return command

	def getNextLine(self) -> str:
		line = self.file.readline()
		if line == '':
			# We have reached the
			# end of the file
			return None
		else:
			return line

	def removeCommentsAndStrip(self, line: str) -> str:
		"""Removes all comments on a line,
		and strip() the line.
		:return line [str]
		"""
		line = line.split('//')[0] #Remove inline comment
		line = line.strip()
		return line



if __name__ == '__main__':
	x = Parser()
	while x.hasMoreCommands():
		x.advance()
		print(x.curr_cmd)

