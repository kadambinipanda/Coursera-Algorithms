#Uses python3

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

    def explore(self, u):
        self.visited[u] = True

        for v in self.adj[u]:
            if self.visited[v] is not True:
                self.explore(v)

    def number_of_components(self):
        self.visited = [False] * self.vertices
        components = 0

        for v in range(self.vertices):
            if self.visited[v] is not True:
                self.explore(v)
                components += 1

        return components


if __name__ == '__main__':

    graph = Graph()
    graph.read()

    print(graph.number_of_components())