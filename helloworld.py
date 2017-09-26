import json
from collections import defaultdict


class country:
	def __init__(self, number, color, point, neighbors):
		self.number = number
		self.color = color
		self.point = point
		self.neighbors = neighbors

	def printCounty(self):
		print(self.number, self.color, self.point, self.neighbors)

	def nbg(self):
		for x in self.neighbors:
			yield x


class Map:
	dic = defaultdict(list)
	points = {}
	countries = defaultdict(list)
	colors = {"yellow", "blue", "red", "green"}

	def __init__(self, filename):
		with open(filename, 'r') as f:
			data = json.load(f)

		for x in data['edges']:
			# print(x[0], x[1])
			self.dic[x[0]].append(x[1])

		self.points = data['points']

		for x in range(0, len(self.points)):
			c = country(x, "blank", self.points[str(x)], self.dic[x])
			self.countries[x].append(c)
			# self.countries[x][0].printCounty()

	def printEdges(self):
		# print(self.countries.items())
		print(self.dic.items())

	def printPoints(self):
		for x in range(0, len(self.points)):
			print(x, self.points[str(x)])

	def printCounties(self):
		for x in range(0, len(self.countries)):
			self.countries[x][0].printCounty()

	def iterDfs(self, s):
		S = set()
		Q = []
		Q.append(s)
		while Q:
			u = Q.pop()
			# print("u = ", u)
			# print("Q = ", Q)
			# print("S = ", S)
			if u in S:
				continue
			# if self.countries[u][0].color =
			S.add(u)
			Q.extend(self.countries[u][0].neighbors)
			self.countries[u][0].color = 1
			yield u

	def printColors(self):
		for x in self.countries:
			print(x, self.countries[x][0].color, list(self.nbColor(x)))

	def nbColor(self, u):
		for x in self.countries[u][0].nbg():
			# print(self.countries[x][0].color)
			yield self.countries[x][0].color

	def assignNcolor(self, u):
		for x in self.colors:
			# print(x, list(self.nbColor(u)))
			if x not in self.nbColor(u):
				# print("Node:", u, "will be assigned: ", x)
				return x

	def complete(self):
		for x in self.countries:
			# print(self.countries[x][0].color, list(self.nbColor(x)))
			if self.countries[x][0].color in self.nbColor(x):
				return False
			elif self.countries[x][0].color is None:
				return False
			elif self.countries[x][0].color is "blank":
				return False

		return True

	def constraint(self, u):
		if self.countries[u][0].color in self.nbColor(u):
			return False
		elif self.countries[u][0].color is "blank":
			return False
		elif self.countries[u][0].color is None:
			return False
		else:
			return True

	def changeColor(self, u, color):
		self.countries[u][0].color = color

	def domain(self):
		return self.colors


def recBacktrack(map):
	if map.complete():
		return map
	else:
		for node in range(0, len(map.countries)):
			# print(node, map.countries[node][0].color, "blank")
			if map.countries[node][0].color is "blank":
				for val in map.domain():
					# print(val, self.countries[node][0].color, self.constraint(node))
					if not map.constraint(node):
						map.countries[node][0].color = val
						posNewMap = recBacktrack(map)
						# print(node, map.countries[node][0].color, posNewMap)
						# print(posNewMap)
						if posNewMap is not None:
							# posNewMap.printCounties()
							return posNewMap
						else:
							map.countries[node][0].color = "blank"
				return None


def iter_dfs(G, s):
	S, Q = set(), []
	Q.append(s)
	while Q:
		u = Q.pop()
		if u in S:
			continue
		S.add(u)
		Q.extend(G[u])
		yield u


if __name__ == '__main__':
	Graph = Map('gcp.json')
	# Graph.printEdges()
	# Graph.printPoints()
	# Graph.printCounties()

	# c = country(0, 0, [0.0, 0.0], [1, 2, 3])
	# c.printCounty()

	# for i in Graph.dfsBacktrackV3(8):
	#   print(i)
	# print(Graph.dfsRecV2(8))
	Sol = recBacktrack(Graph)
	Sol.printCounties()
