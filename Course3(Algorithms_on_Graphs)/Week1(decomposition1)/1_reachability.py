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
        self.visited = [False] * self.vertices


    def reachable(self, x, y):

        if x == y:
            return 1
        else:
            self.visited[x] = True

            for v in self.adj[x]:
                if self.visited[v] is not True:
                    if self.reachable(v, y) == 1:
                        return 1
        return 0


if __name__ == '__main__':

    graph = Graph()
    graph.read()

    x, y = list(map(int, input().split()))
    x, y = x-1, y-1
    print(graph.reachable(x, y))