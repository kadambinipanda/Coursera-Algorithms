# python3

import sys
import threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:

    def __init__(self, key, p=None):
        self.key = key
        self.p = p
        self.children = []


class Tree:

        def read(self):
            self.n = int(sys.stdin.readline())
            
            parents = list(map(int, sys.stdin.readline().split()))
            nodes = [Node(i, p) for i, p in enumerate(parents)]

            for node in nodes:
                if node.p != -1:
                    nodes[node.p].children.append(node)
                    node.p = nodes[node.p]
                else:
                    self.root = node

        def compute_height(self):
            return self.height_improve(self.root)

        def height_improve(self, root):
            if root == None:
                return 0
            else:
                if root.children:
                    return 1 + max([self.height_improve(c)
                                   for c in root.children])
                else:
                    return 1


def main():
  tree = Tree()
  tree.read()   
  print(tree.compute_height())

threading.Thread(target=main).start()
