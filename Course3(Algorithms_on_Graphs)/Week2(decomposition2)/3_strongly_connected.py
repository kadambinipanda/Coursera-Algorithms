#Uses python3

import sys

sys.setrecursionlimit(200000)


class Graph:

    def __init__(self, adj=[]):
        self.vertices = len(adj)
        self.edges = sum([len(e) for e in adj])
        self.adj = adj

    def read(self):
        n, m = list(map(int, input().split()))
        self.vertices = n
        self.edges = m

        edges = []
        for _ in range(m):
            u, v = list(map(int, input().split()))
            edges.append((u, v))

        self.adj = [[] for _ in range(n)]
        for (a, b) in edges:
            self.adj[a - 1].append(b - 1)

    def dfs(self, u, ordered=True):
        for v in self.adj[u]:
            if self.visited[v] is not True:
                self.visited[v] = True
                self.dfs(v, ordered=ordered)
        if ordered:
            self.order.insert(0, u)

    def toposort(self):
        self.visited = [False] * self.vertices
        self.order = []

        for v in range(self.vertices):
            if self.visited[v] is not True:
                self.visited[v] = True
                self.dfs(v)
        return self.order

    def get_transpose_graph(self):
        adj_t = [[] for _ in range(self.vertices)]

        for u, l in enumerate(self.adj):
            for v in l:
                adj_t[v].append(u)

        return Graph(adj_t)

    def num_of_scc(self):
        scc = 0
        self.visited = [False] * self.vertices

        graph_t = self.get_transpose_graph()
        order = graph_t.toposort()

        for v in order:
            if self.visited[v] is not True:
                self.dfs(v, ordered=False)
                scc += 1

        return scc


if __name__ == '__main__':
    graph = Graph()
    graph.read()

    print(graph.num_of_scc())
