from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfsSort(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfsSort(i, visited, stack)
        stack.appendleft(v)  # Add to front after exploring

    def topologicalSort(self):
        visited = [False] * self.V
        stack = deque()

        for i in range(self.V):
            if not visited[i]:
                self.dfsSort(i, visited, stack)

        print(stack)


def main():
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    g.topologicalSort()


if __name__ == "__main__":
    main()
