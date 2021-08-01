# ---------------------- GRAPH - SETS / DICTIONARY -------------------------- #
class Graph:
    def __init__(self):
        # self.v = v
        self.graph = dict()
 
    def addEdge(self, a, b):
        if a not in self.graph:
            self.graph[a] = {b}
        else:
            self.graph[a].add(b)

        if b not in self.graph:
            self.graph[b] = {a}
        else:
            self.graph[b].add(a)

# -------------------------------- INPUT ------------------------------------ #
data = input().split()
n = int(data[0])
m = int(data[1])

g = Graph()

for i in range(m):
    seq = input().split()
    num = int(seq[0])
    for j in range(1, num):
        for k in range(j+1, num+1):
            g.addEdge(seq[j], seq[k])

group_one = g.graph.get("1")
infected = []
if group_one:
    for i in group_one:
        infected.append(i)

# ----------------------------------- BFS ------------------------------------ #
visited = []
possible = []
visited.append("1")
for i in infected:
    possible.append(i)

while possible:
    s = possible.pop()
    neighbours = g.graph.get(s)

    if s not in visited:
        visited.append(s)

    for p in neighbours:
        if (p not in visited) and (p not in possible):
            possible.append(p)
            visited.append(p)

visited = [int(x) for x in visited]
visited.sort()
print(len(visited))
print(' '.join(str(x) for x in visited))