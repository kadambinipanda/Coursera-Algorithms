#Uses python3
import sys
import math


class Edge:

    def __init__(self, u, v, x1, y1, x2, y2):
        self.u = u
        self.v = v
        self.dist = ((x1-x2)**2 + (y1-y2)**2)**0.5

    def __lt__(self, other):
        return self.dist - other.dist


def union(sets, u, v):
    new_val = min(sets[u], sets[v])
    old_val = max(sets[u], sets[v])
    return [new_val if v == old_val else v for v in sets]

def get_edges(x, y):
    edges = []
    for i, pair in enumerate(zip(x, y)):
        for j, pair2 in enumerate(zip(x[i:], y[i:])):
            if pair != pair2:
                edges.append(Edge(i, i+j, pair[0], pair[1], pair2[0], pair2[1]))
    return edges

def clustering(x, y, k):
    sets = list(range(len(x)))

    edges = get_edges(x, y)
    edges_copy = edges.copy()
    edges.sort(key=lambda edge: edge.dist)

    num_of_sets = len(x)
    while num_of_sets > k:
        edge = edges.pop(0)

        if sets[edge.u] != sets[edge.v]:
            sets = union(sets, edge.u, edge.v)
            num_of_sets -= 1

    d = float('inf')
    for edge in edges_copy:
        if sets[edge.u] != sets[edge.v] and edge.dist < d:
            d = edge.dist
    return d


if __name__ == '__main__':
    n = int(input())

    x = []
    y = []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        x.append(a)
        y.append(b)
    k = int(input())
    print("{0:.9f}".format(clustering(x, y, k)))