def DFS(G, start, end):
    n = len(G)
    visited = [False] * n
    S = []
    S.append(start)
    visited[start] = True    
    dist = [0] * n
       
    while (S != []):
        v = S[-1]
        S.pop()
        for i in G[v]:
            if i != end:
                 if (visited[i] == False):
                     S.append(i)
                     visited[i] = True
                     dist[i] = dist[v] + 1
            else:
                return dist[v] + 1
    return 0

G = [
[1, 2, 3],
[0, 4, 5],
[0, 6, 7],
[0, 8, 9],
[1, 10, 11, 12],
[1, 13, 14],
[2, 15],
[2, 16, 17],
[3],
[3, 18],
[4],
[4],
[4, 19, 20],
[5],
[5],
[6, 21, 22, 23],
[7, 24, 25],
[7, 26, 27],
[9, 28, 29],
[12],
[12],
[15],
[15],
[15],
[16],
[16],
[17],
[17],
[18],
[18]
]

start, end = map(int, input().split())
print(DFS(G, start, end))
