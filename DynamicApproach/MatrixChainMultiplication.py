n = 5
dimension = [3, 2, 4, 2, 5]
cost = [[0 for _ in range(0, n)] for _ in range(0, n)]
partition = [[0 for _ in range(0, n)] for _ in range(0, n)]

for d in range(1, n - 1):
    for i in range(1, n - d):
        j = i + d
        min_val = float('INF')
        for k in range(i, j):
            c = cost[i][k] + cost[k + 1][j] + dimension[i - 1] * dimension[k] * dimension[j]
            if c < min_val:
                min_val = c
                partition[i][j] = k
        cost[i][j] = min_val

print(partition)
print(cost)
