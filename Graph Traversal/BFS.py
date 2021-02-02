class Queue:
    def __init__(self):
        self.queue = []

    def add(self, vertex):
        self.queue.append(vertex)

    def remove(self):
        return self.queue.pop(0)

    def __call__(self, *args, **kwargs):
        return self.queue


def bfs(graph, source):
    visited = []
    queue = Queue()
    queue.add(source)
    visited.append(source)
    
    # If not visited, mark it as visited, and
    # enqueue it

    while queue():
        v = queue.remove()

        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.add(neighbour)

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

t = bfs(graph, 1)
print(t)
