"""A Multistage graph is a directed graph in which the nodes can be divided into a set of stages such that all edges
are from a stage to next stage only (In other words there is no edge between vertices of same stage and from a vertex
of current stage to previous stage). """

total_nodes = 12
total_stages = 5
graph = [[0, 9, 7, 3, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 4, 2, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 2, 7, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 11, 8, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

cost = [0] * total_nodes
d = [0] * total_nodes

for node in range(total_nodes - 1, -1, -1):
    minimum = float('INF')
    for j in range(total_nodes):
        if graph[node][j] != 0 and graph[node][j] + cost[j] < minimum:  # select the minimum edges which go forward  from current vertex
            minimum = graph[node][j] + cost[j]  # cost of current node is cost of edge from current vertex to the next vertext + cost of next stage vertex
            d[node] = j
    if minimum == float('INF'):
        cost[node] = 0
        d[node] = node

    else:
        cost[node] = minimum

print(cost)
print(d)

# Find the path
path = [0]*total_stages
path[0] = 0
for k in range(1, total_stages):
    path[k] = d[path[k-1]]

print("Minimum cost path from source vertex to destination vertex", path)
