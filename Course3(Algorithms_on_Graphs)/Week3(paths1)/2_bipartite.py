#Uses python3

import sys
from queue import Queue

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
            self.adj[b - 1].append(a - 1)

    def is_bipartite(self):
        colors = [None] * self.vertices
        colors[0] = 0

        processing = Queue(self.vertices)
        processing.put(0)

        while not processing.empty():
            vertex = processing.get()

            new_color = abs(colors[vertex] - 1)
            for neighbor in self.adj[vertex]:
                if colors[neighbor] is None:
                    colors[neighbor] = new_color
                    processing.put(neighbor)
                elif colors[neighbor] != new_color:
                    return 0
        return 1


if __name__ == '__main__':
    graph = Graph()
    graph.read()
    print(graph.is_bipartite())
