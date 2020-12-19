def path_find(n, G, path, x, y):
    if x > n or y > n or G[x][y] == 0:
        return -1
    path[x][y] = 1
    if x == n and y == n:
        for i in range(n+1):
            for j in range(n+1):
                print(path[i][j], end = " ")
            print("")
        return 1
    a = path_find(n, G, path, x+1, y)
    b = path_find(n, G, path, x, y+1)
    path[x][y] = 0
    return max(a, b)

n = int(input())
G = [list(map(int, input().split())) for i in range(n)]

path = [[0]*n for i in range(n)]
c = path_find(n-1, G, path, 0, 0)
if c == -1:
    print(c)
