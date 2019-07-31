import re

COMMENT = '//'


class Parser:
	def __init__(self, inFile="inFile.asm"):
		self.inFile = open(inFile, 'r')

		self.lines = (instr for instr in self.inFile.readlines())
		self.commands = self.commands_dict()

	#######
	### API
	def get_nextIstr(self):
		"""
		Return: next instruction
		if no 'next instruction':
			raise 'StopIteration Error'
		"""
		# Get next line
		nextLine = next(self.lines)
		# Remove comments and strip()
		# We are either left with nothing '' or
		# an instruction eg. 'push constant 7'
		clean_nextLine = self.removeComments(line=nextLine)

		while (clean_nextLine == ''):
			nextLine = next(self.lines)
			clean_nextLine = self.removeComments(line=nextLine)

		# We are now left with an instruction
		nextInstr = clean_nextLine
		return nextInstr

	def fileContainsAnInstr(self):
		"""
		return: True,  if file contains an instr
		return: False, if file doesn't contain an instr
		"""
		try:
			print(f"File is not empty, it contains "
			      f"the instr: {self.get_nextIstr()}\n____")
			#Reset file reader pointer
			self.inFile.seek(0)
			return False
		except StopIteration:
			return True

	def removeCommentsAndStrip(self, line: str) -> str:
		"""Removes label and all comments on a line,
		and strip() the line.
		:return line [str]
		"""
		if line.startswith('('):
			# The line contains a label
			return ''

		line = line.split('//')[0] #Remove inline comment
		line = line.strip()
		return line

	### END API
	###########
	def removeComments(self, line):
		line = line.split(COMMENT)[0].strip()
		return line

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


if __name__ == '__main__':
	parser = Parser()





