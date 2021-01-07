"""Prim's algorithm to find minimum cost spanning tree (as Kruskal's algorithm) uses the greedy approach. Prim's
algorithm shares a similarity with the shortest path first algorithms.
"""
# https://static.javatpoint.com/ds/images/prim-algorithm-example.png
# graph = [[0, 7, 0, 8, 0, 0],
#          [7, 0, 6, 3, 0, 0],
#          [0, 6, 0, 4, 2, 5],
#          [8, 3, 4, 0, 3, 0],
#          [0, 0, 2, 3, 0, 2],
#          [0, 0, 5, 0, 2, 0]]

# graph = [[0, 2, 0, 6, 0],
#          [2, 0, 3, 8, 5],
#          [0, 3, 0, 0, 7],
#          [6, 8, 0, 0, 9],
#          [0, 5, 7, 9, 0]]

# https://www.javatpoint.com/prim-algorithm
graph = [[0, 0, 3, 0, 0],
         [0, 0, 10, 4, 0],
         [3, 10, 0, 2, 6],
         [0, 4, 2, 0, 1],
         [0, 0, 6, 1, 0]]

check = []
for i in range(len(graph)):  # iterating the outer matrix
    min_val = float('INF')
    min_index = 0
    for j in range(len(graph[i])):  # iterating the inner element
        if 0 < graph[i][j] <= min_val:
            min_val = graph[i][j]
            min_index = j

    # print(i, min_index)
    if (i, min_index) in check or (min_index, i) in check:  # check for reversible path which previously consider
        continue
    else:
        check.append((i, min_index))  # append the new path
        print("{} - {} = {}".format(i, min_index, min_val))
