import json
import math
import sys
from collections import defaultdict


class Board:
	data = {}

	def __init__(self, filename):
		with open(filename, 'r') as f:
			data = json.load(f)
		self.data = data
		self.printBoard()

	def printBoard(self):
		for x in self.data:
			print(x)
		# print(type(x[0]))

	def dupCol(self, dx):
		seen = set()
		for col in self.data:
			if col[dx] in seen:
				return True
			seen.add(col[dx])
			#print(col[dx])

		return False

	def dupRow(self, dy):
		seen = set()
		for col in self.data[dy]:
			if col in seen:
				return True
			seen.add(col)
			#1print(col)

		return False

	def dubSquare(self, dx, dy):
		square = []
		for x in range(0, 3):
			for y in range(0, 3):
				square.append(self.data[math.floor(dx / 3) * 3 + x][math.floor(dy / 3) * 3 + y])

		seen = set()
		for x in square:
			if x in seen:
				return True
			seen.add(x)
		# 1print(col)

		return False

	def constraints(self, dx, dy):
		if self.data[dx][dy] is 0:
			return False
		if self.dupCol(dx):
			return False
		if self.dupRow(dy):
			return False
		if self.dubSquare(dx, dy):
			return False

		return True

	def complete(self):
		dx, dy = -1, -1
		for x in self.data:
			dx = dx + 1
			dy = -1
			# print("X", x)
			for node in x:
				dy = dy + 1
				if node is 0:
					#print("There's a 0")
					return False
				if not self.constraints(dx, dy):
					#print("There's a conflict")
					return False
		return True


def recBacktrack(self):
	if self.complete():
		#print("Complete")
		return self
	else:
		dx, dy = -1, -1
		for node in self.data:
			dx = dx + 1
			dy = -1
			for x in node:
				dy = dy + 1
				if x is 0:
					for val in (1, 2, 3, 4, 5, 6, 7, 8, 9):
						if not self.constraints(dx, dy):
							# print(node)

							self.data[dx][dy] = val
							# print(node)
							#print("X is:", x, "The value of data @",dx,dy,"is",self.data[dx][dy])
							newBoard = recBacktrack(self)
							#print(newBoard)
							if newBoard is not None:
								#b1.printBoard()
								return newBoard
							else:
								self.data[dx][dy] = 0

					return None


if __name__ == '__main__':
	# sys.setrecursionlimit(1500)
	b1 = Board('sudoku.json')

	print("Space")

	b1 = recBacktrack(b1)
	b1.printBoard()
	#print(b1.dupRow(0))