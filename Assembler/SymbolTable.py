class SymbolTable:
	"""Keeps a correspondance between
	symbolic and numeric addresses"""
	def __init__(self):
		# Initialize the symbol table
		# with predefined symbols
		self.symbolTable = {
			'SP': 0,   # Stack Pointer
			'LCL': 1,  # Local (variable)
			'ARG': 2,  # Argument (variable)
			'THIS': 3,
			'THAT': 4,
			'SCREEN': 16384,
			'KBD': 24576
		}
		for i in range(16):
			self.symbolTable[f"R{i}"] = i

		self.variablesEncountered = 0

	def add_entry(self, symbol: str, address: int):
		"""Adds the pair (symbol, address)
		to the symbol table.
		"""
		self.symbolTable[symbol] = address

	def contains(self, symbol: str) -> bool:
		"""Does the symbol table contain
		the given symbol?
		"""
		try:
			self.symbolTable[symbol]
			return True
		except KeyError:
			return False

	def getAddress(self, symbol: str) -> int:
		return self.symbolTable[symbol]
