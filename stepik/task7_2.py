def prim(n, G):
    visited = [False]*n
    no_edge = 0
    visited[6] = True

    sum = 0

    while (no_edge < n-1):
        min = 101
        y = 0

        for i in range(n):
            if (visited[i]):
                for j in range(n):
                    if (not visited[j] and G[i][j]):
                        if min > G[i][j]:
                            min = G[i][j]
                            y = j

        if min == 101:
            return -1
        sum += min
        visited[y] = True
        no_edge += 1
    return sum

n = int(input())
G = [list(map(int, input().split())) for i in range(n)]

s = prim(n, G)

if s == -1:
    print("NON-CONNECTED")
else:
    print(s)
