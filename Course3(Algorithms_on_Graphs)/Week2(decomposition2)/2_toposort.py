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


if __name__ == '__main__':
    graph = Graph()
    graph.read()

    order = graph.toposort()
    print(' '.join([str(x+1) for x in order]))
