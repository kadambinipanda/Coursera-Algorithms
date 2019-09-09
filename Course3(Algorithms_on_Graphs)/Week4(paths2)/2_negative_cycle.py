#Uses python3

import sys
import queue


class Graph:

    def read(self):
        n, m = list(map(int, input().split()))
        self.vertices = n
        self.edges = m

        self.adj = [[] for _ in range(self.vertices)]
        self.weight = [[] for _ in range(self.vertices)]
        for _ in range(m):
            u, v, w = list(map(int, input().split()))
            self.adj[u - 1].append(v - 1)
            self.weight[u - 1].append(w)

    def has_negative_cycle(self):
        self.distances = [0] * self.vertices

        for i in range(self.vertices):
            for u in range(self.vertices):
                for v_idx, v in enumerate(self.adj[u]):
                    new_cost = self.distances[u] + self.weight[u][v_idx]

                    if self.distances[v] > new_cost:
                        self.distances[v] = new_cost
                        if i == self.vertices - 1:
                            return 1
        return 0

if __name__ == '__main__':
    graph = Graph()
    graph.read()
    print(graph.has_negative_cycle())