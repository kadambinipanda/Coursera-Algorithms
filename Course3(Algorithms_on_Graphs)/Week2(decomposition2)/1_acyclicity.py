#Uses python3

import sys

class Graph:

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

    def explore(self, u):
        self.visited[u] = True
        self.rec_stack[u] = True

        for v in self.adj[u]:
            if self.visited[v] is not True:
                if self.explore(v) == 1:
                    return 1
            elif self.rec_stack[v] is True:
                return 1
        self.rec_stack[u] = False
        return 0

    def acyclic(self):
        self.visited = [False] * self.vertices
        self.rec_stack = [False] * self.vertices

        for v in range(self.vertices):
            if self.visited[v] is not True:
                if self.explore(v) == 1:
                    return 1
        return 0


if __name__ == '__main__':
    graph = Graph()
    graph.read()

    print(graph.acyclic())
