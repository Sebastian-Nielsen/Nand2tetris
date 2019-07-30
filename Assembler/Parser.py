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
import re
from Code import compDict, destDict, jumpDict

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
		self.curr_cmd is updated
		:return True
		2. There are no more commands;
		self.curr_cmd is None
		:return False
		"""
		self.next_cmd = self.getNextCmd()
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
		return self.curr_cmd

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
		"""
		:return
		"""

	def get_dest_bin(self, c_instr: str) -> str:
		"""Takes a >CLEAN< c-instruction (no 
		whitespace and stripped()) as input
		and returns the binary machine language
		equivalent of the dest part. Example:
		c_instr:       |'M=D+1'  |'M-1;JGT'|
		dest_part:     |'M'      |'null'   |
		dest_part_bin: |'001'    |'000'    |
		"""
		if ('=' in c_instr):
			dest_part = c_instr.split('=')[0]
		else:
			dest_part = 'null'

		# Look up the binary representation of
		# the dest_part.
		dest_part_bin = destDict[dest_part]
		return dest_part_bin

	def get_comp_bin(self, c_instr: str) -> str:
		"""Takes a >CLEAN< c-instruction (no 
		whitespace and stripped()) as input
		and returns the binary machine language
		equivalent of the comp part. Example:
		c_instr:        |'M=D+1'  |'M-1;JGT'|
		comp_part:      |'D+1'    |'M-1'    |
		comp_part_bin:  |'0011111'|'1110010'|
		"""
		matches = re.search(
			r'(?:(.*= *)?)([\w+-]*)((?: *;.*)?)',
			c_instr
		)
		# We only care about the second capture,
		# group, namely, the comp_part.
		comp_part = matches.group(2)
		# Look up the binary representation of
		# the comp_part
		comp_part_bin = compDict[comp_part]
		return comp_part_bin

	def get_jump_bin(self, c_instr: str) -> str:
		"""Takes a >CLEAN< c-instruction (no 
		whitespace and stripped()) as input
		and returns the binary machine language
		equivalent of the jump part. Example:
		c_instr:       |'M=D+1'  |'M-1;JGT'|
		jump_part:     |'null'   |'JGT'    |
		jump_part_bin: |'000'    |'001'    |
		"""
		if (';' in c_instr):
			jump_part = c_instr.split(';')[1]
		else:
			jump_part = 'null'

		# Look up the binary representation of
		# the jump_part.
		jump_part_bin = jumpDict[jump_part]
		return jump_part_bin

	def hasMoreLabels(self):
		"""
		1. There are more labels;
		self.curr_label is updated
		:return True
		2. There are no more labels;
		self.curr_label is None
		:return False
		"""
		self.next_label = self.getNextCmd()
		return bool(self.next_cmd)

	def getNextLabel(self, ):
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

			# The 'cleaned line' must
			# a command by now
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



"""
	0 1 2 3 4 5 6 7 8 9 1 1 2 3 4 5  (index)
	1 1 1 a c c c c c c d d d j j j
	^     \_____ _____/\_ __/\__ _/
	opcode    comp      dest  jump
"""