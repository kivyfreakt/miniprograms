def DFS(v, c):
    color[v] = c
    
    for u in G[v]:
        if (not color[u]):
            DFS(u, invert(c))
        elif color[u] == c:
            print("NO")
            exit()

def invert(c):
    if c == 1:
        return 2
    else:
        return 1


n = int(input())

G = [[] for i in range(101)]
color = [0]*101

for i in range(n):
    a, b = map(int, input().split())
    G[a].append(b)

for i in range(1, 101):
    if color[i] == 0:
        DFS(i, 1)

print("YES")
