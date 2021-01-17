# for detail information click on the below given link
# https://www.youtube.com/watch?v=nLmhmB6NzcM&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=54
price = [0, 1, 2, 5, 6]
weight = [0, 2, 3, 4, 5]
col, row = 8, 4
K = [[float('INF') for _ in range(0, col + 1)] for _ in range(0, row + 1)]
print(K)

for i in range(0, row + 1):
    for j in range(0, col + 1):
        if i == 0 or j == 0:
            K[i][j] = 0

        elif weight[i] <= j:
            K[i][j] = max(price[i] + K[i - 1][j - weight[i]], K[i - 1][j])

        else:
            K[i][j] = K[i - 1][j]

print(K)

max = K[row][col]
while row > 0:
    if max in K[row - 1]:
        print("{} == 0".format(row))
        row -= 1
    else:
        print("{} == 1".format(row))
        max = max - price[row]
        row -= 1
