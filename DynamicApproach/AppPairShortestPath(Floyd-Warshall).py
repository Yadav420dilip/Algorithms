"""The all pair shortest path algorithm is also known as Floyd-Warshall algorithm is used to find all pair shortest
path problem from a given weighted graph. As a result of this algorithm, it will generate a matrix, which will
represent the minimum distance from any node to all other nodes in the graph. """

"""For better understanding watch the video https://www.youtube.com/watch?v=oNI0rf2P9gE"""
inf = float('INF')
vertices = 4
graph = [[0, 3, inf, 7],
         [8, 0, 2, inf],
         [5, inf, 0, 1],
         [2, inf, inf, 0]]

for k in range(vertices):
    for i in range(vertices):
        for j in range(vertices):
            if graph[i][j] != 0:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    print(graph)
