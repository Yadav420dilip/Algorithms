"""Dijkstra's algorithm (or Dijkstra's Shortest Path First algorithm, SPF algorithm)[4] is an algorithm for finding
the shortest paths between nodes in a graph, which may represent, for example, road networks. """


class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0 for _ in range(vertex)] for __ in range(vertex)]

    def find_min_distance(self, value, visited_node):  # find the minimum distance
        min_dis = float('INF')
        for i in range(self.vertex):
            if value[i] < min_dis and visited_node[i] is False:
                min_dis = value[i]
                min_index = i
        return min_index


    def representing_graph(self, parent, value):
        for i in range(len(parent)):
            if parent[i] == -1:
                print("{}   ---------   {}  =   {}".format(i, i, value[i]))
            else:
                print("{}   ---------   {}  =   {}".format(parent[i], i, value[i]))

    def dijktras(self, source):
        value = [float('INF')] * self.vertex
        parent = [-1] * self.vertex
        processed = [False] * self.vertex
        value[source] = 0

        while any(flag is False for flag in processed):  # check each node is visited or not
            min_index = self.find_min_distance(value, processed)
            processed[min_index] = True

            for v in range(self.vertex):
                if self.graph[min_index][v] > 0 and processed[v] is False and value[v] > self.graph[min_index][v] + \
                        value[min_index]:  # check the adjacent node should be greater than 0 and node is not visited
                    # and distance from the parent node should be less
                    value[v] = self.graph[min_index][v] + value[min_index]
                    parent[v] = min_index
        self.representing_graph(parent, value)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijktras(0)
