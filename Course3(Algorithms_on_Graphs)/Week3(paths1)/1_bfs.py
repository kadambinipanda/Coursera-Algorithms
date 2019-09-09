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

    def compute_distance(self, u, v):
        distances = [None] * self.vertices
        processing = Queue(self.vertices)

        distances[u] = 0
        processing.put(u)

        while not processing.empty():
            vertex = processing.get()

            if vertex == v:
                break

            for neighbor in self.adj[vertex]:
                if distances[neighbor] is None:
                    processing.put(neighbor)
                    distances[neighbor] = distances[vertex] + 1

        return distances[v] if distances[v] is not None else -1


if __name__ == '__main__':
    graph = Graph()
    graph.read()

    u, v = list(map(int, input().split()))
    u, v = u-1, v-1
    print(graph.compute_distance(u, v))
