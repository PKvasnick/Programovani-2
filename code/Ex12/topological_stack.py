from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = deque()
        working_stack = deque()

        for i in range(self.V):
            if not visited[i]:
                working_stack.append(i)
                while working_stack:
                    v = working_stack[-1]
                    visited[v] = True
                    daughters = [
                        next_v for next_v in self.graph[v] if not visited[next_v]
                    ]
                    if daughters:
                        working_stack.extend(daughters)
                    else:
                        stack.appendleft(v)
                        working_stack.pop()

        return stack


def main():
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    print(g.topologicalSort())


if __name__ == "__main__":
    main()
