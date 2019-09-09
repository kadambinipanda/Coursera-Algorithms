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

    def find_shortest_paths(self, s):
        distances = [float('inf')] * self.vertices
        distances[s] = 0
        last_changed = []

        for i in range(self.vertices):
            for u in range(self.vertices):
                for v_idx, v in enumerate(self.adj[u]):
                    new_cost = distances[u] + self.weight[u][v_idx]

                    if distances[v] > new_cost:
                        distances[v] = new_cost
                        if i == self.vertices - 1:
                            last_changed.append(v)

        visited = [False] * self.vertices
        bfs_visited = last_changed.copy()
        while bfs_visited:
            vertex = bfs_visited.pop()
            visited[vertex] = True

            for neighbor in self.adj[vertex]:
                if visited[neighbor] != True:
                    bfs_visited.append(neighbor)
        
        for i in range(len(visited)):
            if visited[i] is True:
                distances[i] = float('-inf')

        return distances

if __name__ == '__main__':

    graph = Graph()
    graph.read()

    vertex = int(input())
    distances = graph.find_shortest_paths(vertex-1)
    for d in distances:
        if d == float('inf'):
            print('*')
        elif d == float('-inf'):
            print('-')
        else:
            print(d)