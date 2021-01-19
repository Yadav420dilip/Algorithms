"""In computer science, an optimal binary search tree, sometimes called a weight-balanced binary tree, is a binary
search tree which provides the smallest possible search time for a given sequence of accesses. """

# To understand the concept please watch this video
# https://www.youtube.com/watch?v=wAy6nDMPYAE&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=57

node = [0, 10, 20, 30, 40]
p = [0, 3, 3, 1, 1]
q = [2, 3, 1, 1, 1]
n = 5
weight = [[0 for _ in range(5)] for _ in range(5)]
cost = [[0 for _ in range(5)] for _ in range(5)]
K = [[0 for _ in range(5)] for _ in range(5)]

for d in range(0, n):
    for i in range(0, n - d):
        j = i + d
        if i == j:
            weight[i][j] = q[j]
            cost[i][j] = 0
            K[i][j] = 0

        else:
            weight[i][j] = weight[i][j - 1] + p[j] + q[j]  # wieght[i][j] = weight[i][j-1]+p[j]+q[j]
            minimum = float('INF')
            for k in range(i + 1, j + 1):
                c = cost[i][k - 1] + cost[k][j]  # cost[i][j] = min of {c[i, k-1]+c[k, j] where i<k<=j} + weight[i][j]
                if c < minimum:
                    minimum = c
                    K[i][j] = k

            cost[i][j] = minimum + weight[i][j]

print(weight)
print(cost)
print(K)


def graph(m, n, message):
    k = K[m][n]
    if k == 0:
        return 0
    else:
        print(message, node[k])
        graph(m, k - 1, "LEFT")
        graph(k, n, "RIGHT")


graph(0, n - 1, "Parent Node")
