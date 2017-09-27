def selectUnAssignedVar(self):
    for x in self.countries:
        if self.countries[x][0].color is "blank":
            return self.countries[x][0].number


def orderDomainValue(self):
    print(var, assign)
    for x in self.countries:
        yield x


def backtrackV2(self, assign):
    if self.complete():
        return assign
    var = self.selectUnAssignedVar()

    for val in self.orderDomainValue():
        print("hello")


def dfsBacktrackV3(self, start):
    visited, toVisit = [], []
    toVisit.append(start)
    popNum = 0
    while not self.complete():

        cn = toVisit.pop(popNum % len(toVisit))

        if cn in visited:
            continue

        if self.countries[cn][0].color in self.nbColor(cn):
            self.countries[cn][0].color = self.assignNcolor(cn)

        if self.countries[cn][0].color is None:
            popNum += 1
            toVisit.append(cn)
            print("Backtrack", (popNum % len(toVisit)), )
            continue

        visited.append(cn)
        toVisit.extend(self.countries[cn][0].neighbors)
        yield cn


def dfsBacktrackV2(self, s):
    S, Q = [], []
    Q.append(s)
    while Q:
        u = Q.pop(0)
        # print(u, Q)
        if u in S:
            continue
        if self.countries[u][0].color in self.nbColor(u):
            self.countries[u][0].color = self.assignNcolor(u)
            if self.countries[u][0].color is None:
                print("backtrack")
                Q.append(u)
                S.pop()
                continue
        S.append(u)
        Q.extend(self.countries[u][0].neighbors)
        yield u


def dfsBacktrack(self, start, S=set(), first=0):
    if first is 0:
        Q = []
        Q.append(start)
        while Q:
            u = Q.pop()
            # print("u = ", u)
            # print("Q = ", Q)
            # print("S = ", S)
            if self.countries[u][0].color in self.nbColor(u):
                # print(u, "Same color as my neighbor: ", self.countries[u][0].color)
                self.countries[u][0].color = self.assignNcolor(u)
                if self.countries[u][0].color is None:
                    Q.append(u)
                    print("Backtrack/None", S)
                    return self.dfsBacktrack(u, S, 1)

            if u in S: continue
            S.add(u)
            Q.extend(self.countries[u][0].neighbors)
            # self.countries[u][0].color = "yellow"
            yield u
    else:
        return 0


def backtrakingSearch(self):
    s = {}
    return self.backtrack(s)


def backtrack(self, assign):
    print(assign)


# if assign is self.complete:
# return assign
# u = 1
# self.countries[u][0].color = self.assignNcolor(u)
# for val in self.orderDV():
# if val is consistent(assign):
# assign.add(var = val)
# infernces = self.inferences(var,val)
# if inferences not 0:
# add inferences assign
# result = self.backtrack(assign)
# if result not 0:
# return result
# remove{var = val} and inferences from assign
# return 0

def dfsRecV2(self, start, visited=None):
    print("dfsRecV2Start", start)
    if visited is None:
        visited = []

    fail = 0
    visited.append(start)
    for curNode in self.dic[start]:
        if curNode in visited:
            continue

        if self.countries[curNode][0].color in self.nbColor(curNode):
            # print(u, "Same color as my neighbor: ", self.countries[u][0].color)
            self.countries[curNode][0].color = self.assignNcolor(curNode)
            if self.countries[curNode][0].color is None:
                print("Backtrack")
                self.dic[visited[-2]].remove(visited[-1])
                fail = 1

        if fail is 1:
            self.dfsRecV2(curNode, visited[:-1])
        else:
            self.dfsRecV2(curNode, visited)
    return visited

    def assignNcolor(self, u):
        for x in self.colors:
            print(x, list(self.nbColor(u)))
            if x not in self.nbColor(u):
                # print("Node:", u, "will be assigned: ", x)
                return x

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