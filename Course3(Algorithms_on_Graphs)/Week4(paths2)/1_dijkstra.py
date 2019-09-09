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

    def get_next_vertex(self):
        vertex = -1
        min_value = float('inf')

        for idx, dist in enumerate(self.distances):
            if dist < min_value and self.visited[idx] == False:
                min_value = dist
                vertex = idx
        return vertex

    def compute_distance(self, u, v):
        self.distances = [float('inf')] * self.vertices
        self.visited = [False] * self.vertices
        self.distances[u] = 0

        for _ in range(self.vertices - 1):
            vertex = self.get_next_vertex()

            if vertex == -1:
                break
            self.visited[vertex] = True
            dist = self.distances[vertex]

            for idx in range(len(self.adj[vertex])):
                neighbor = self.adj[vertex][idx]
                weight = self.weight[vertex][idx]

                if self.visited[neighbor] == False and\
                 self.distances[neighbor] > dist + weight:
                    self.distances[neighbor] = dist + weight
        return self.distances[v] if self.distances[v] != float('inf') else -1

if __name__ == '__main__':
    graph = Graph()
    graph.read()

    u, v = list(map(int, input().split()))
    u, v = u - 1, v - 1
    print(graph.compute_distance(u, v))
