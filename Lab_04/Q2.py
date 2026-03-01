distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_Cost = 9999
best_Path = []

for b in range(1, 4):
    for c in range(1, 4):
        for d in range(1, 4):

            if b != c and c != d and b != d:

                cost = 0
                cost = cost + distance[0][b]
                cost = cost + distance[b][c]
                cost = cost + distance[c][d]
                cost = cost + distance[d][0]

                if cost < min_Cost:
                    min_Cost = cost
                    best_Path = [0, b, c, d, 0]
print("Shortest Path:", best_Path)
print("Minimum Cost:", min_Cost)