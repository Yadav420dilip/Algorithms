"""Kruskal's algorithm finds a minimum spanning forest of an undirected edge-weighted graph. If the graph is
connected, it finds a minimum spanning tree. It is a greedy algorithm in graph theory as in each step it adds the
next lowest-weight edge that will not form a cycle to the minimum spanning forest. """


class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = []

    # add edges to the graph
    def add_edge(self, parent, child, weight):
        self.graph.append([parent, child, weight])

    # return the graph
    def get_graph(self):
        return self.graph

    #   find the parent  of the node
    def find(self, parent, x):
        if parent[x] < 0:
            return x
        return self.find(parent, parent[x])

    # perform the union of the two node of different parent using disjoint set data structure
    def union(self, parent, x, y):
        if abs(parent[x]) > abs(parent[y]):  # if node x has weight greater than node y then
            parent[y] = x   # assign the x index to y node as parent
            parent[x] -= 1  # and increment the node x weight negatively to know it is parent node

        elif abs(parent[x]) < abs(parent[y]):   # if node y has weight greater than node y then
            parent[x] = y   # assign the y index to x node as parent
            parent[y] -= 1    # and increment the node y weight negatively to know it is parent node

        else:   # if both the condition is false then
            parent[y] = x  # assign the first node as parent of the y
            parent[x] -= 1  # and increment weight of the first node

    # performing the main method kruskal's algorithm
    def kruskal_algo(self):
        self.graph.sort(key=lambda w: w[2])     # sort the graph based on the weight of the edge
        result = []
        parent = [-1 for _ in range(self.vertex)] # create list in which each node is parent of itself which is
        # indicated by negative 1 value
        for edge in self.graph:
            x = self.find(parent, edge[0])
            y = self.find(parent, edge[1])
            if x != y:  # if the parent of the 2 node is not equal mean they belong to different set therefore they
                # not create cycle
                result.append(edge)     # append the result
                self.union(parent, x, y)    # union these node in same set

        return result


# First example of graph
g = Graph(6)
g.add_edge(0, 1, 7)
g.add_edge(1, 2, 6)
g.add_edge(0, 3, 8)
g.add_edge(1, 3, 3)
g.add_edge(3, 2, 4)
g.add_edge(3, 4, 3)
g.add_edge(2, 4, 2)
g.add_edge(2, 5, 5)
g.add_edge(4, 5, 2)

#  Second Example of graph
# g = Graph(5)
# g.add_edge(3,4,1)
# g.add_edge(3,2,2)
# g.add_edge(2,0,3)
# g.add_edge(1,3,4)
# g.add_edge(2,4,6)
# g.add_edge(1,2,10)

print(g.get_graph())
mst = g.kruskal_algo()
for mst_edge in mst:
    print("{0} ----  {1} =  {2}".format(mst_edge[0], mst_edge[1], mst_edge[2]))
