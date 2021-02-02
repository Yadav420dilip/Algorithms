class Stack:
    """Stack data structure"""
    def __init__(self):
        self.stack = []

    def add(self, vertex):
        self.stack.insert(0, vertex)

    def pop(self):
        return self.stack.pop(0)

    def __call__(self, *args, **kwargs):
        return self.stack


def dfs(graph, source):
    visited = []
    stack = Stack()
    visited.append(source)
    stack.add(source)

    while stack():
        v = stack.pop()

        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.add(v)
                stack.add(neighbour)
                break

    return visited


graph = {1: [4, 2],
         2: [3, 5, 7, 8],
         3: [2, 4, 9, 10],
         4: [1, 3],
         5: [2, 6, 7, 8],
         6: [5],
         7: [2, 5, 8],
         8: [2, 5, 7],
         9: [3],
         10: [3]}

t = dfs(graph, 1)
print(t)
