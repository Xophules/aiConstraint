import json
from collections import defaultdict


class country:
    def __init__(self, number, color, point, neighbors):
        self.number = number
        self.color = color
        self.point = point
        self.neighbors = neighbors
        self.colors = {"yellow", "blue", "red", "green"}

    def printCounty(self):
        print(self.number, self.color, self.point, self.neighbors)

    def nbg(self):
        for x in self.neighbors:
            yield x


class Map:
    data = {}
    dic = defaultdict(list)
    points = {}
    countries = defaultdict(list)

    def __init__(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)

        for x in data['edges']:
            # print(x[0], x[1])
            self.dic[x[0]].append(x[1])

        self.points = data['points']
        self.data = data

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

    def printColors(self):
        for x in self.countries:
            print(x, self.countries[x][0].color, list(self.nbColor(x)))

    def printDomain(self):
        for x in self.countries:
            print(x, self.domain(x))

    def nbColor(self, u):
        for x in self.countries[u][0].nbg():
            # print(self.countries[x][0].color)
            yield self.countries[x][0].color

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

    def arcConstraint(self, u, v):
        if u is v:
            return False
        return True

    def changeColor(self, u, color):
        self.countries[u][0].color = color

    def domain(self, node):
        return self.countries[node][0].colors

    def forwardDomain(self, node):
        c = self.countries[node][0].colors
        n = list(self.nbColor(node))
        return [item for item in c if item not in n]

    def ac3(self):
        q = self.data['edges']

        while q:
            curArc = q.pop()
            if self.revise(curArc[0], curArc[1]):
                if self.domain(curArc[0]) is None:
                    return False
                l = list(self.countries[curArc[0]][0].nbg())
                l.remove(curArc[1]) # removing the wrong thing
                for xk in l:
                    q.append([xk, curArc[0]])

        return True

    def revise(self, xi, xj):
        revised = False
        for color in list(self.domain(xi)):
            for y in list(self.domain(xj)):
                if not self.arcConstraint(color, y):  # Posiably very wrong
                    self.countries[xi][0].colors.remove(color)
                    revised = True

        return revised


def recBacktrack(map):
    if map.complete():
        return map
    else:
        for node in range(0, len(map.countries)):
            # print(node, map.countries[node][0].color, "blank")
            if map.countries[node][0].color is "blank":
                for val in map.forwardDomain(node):
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


if __name__ == '__main__':
    Graph = Map('gcp.json')
    Solve = Graph
    Solve.countries[0][0].colors ={'red'}
    Solve.printDomain()
    Solve.ac3()
    Solve.printDomain()



