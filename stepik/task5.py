def DFS_T(node, G, visited, time_order):
    if node == -1:
        return
    visited[node] = True
    for i in range(len(G[node])):
        if not visited[G[node][i]]:
            DFS_T(G[node][i], G, visited, time_order)
    time_order.append(node)

def DFS_C(node, G_T, component, res):
    if node == -1:
        return
    component[node] = res
    for i in range(len(G_T[node])):
        if component[G_T[node][i]] == 0:
            DFS_C(G_T[node][i], G_T, component, res)


def kos_sharir_alg(G, G_T):
    time_order = []
    visited1 = [False]*len(G)
    c = [0]*len(G)
    res = 1
    for i in range(len(G)):
        if not visited1[i]:
            DFS_T(i, G, visited1, time_order)
    
    print(time_order)    

    for i in range(len(G)):
        v = time_order[len(G)-i-1]
        if c[v] == 0:
            DFS_C(v, G_T, c, res)
            res += 1
    return c

n = int(input())

G = [list(map(int, input().split())) for i in range(n)]
G_T = [[] for i in range(n)]

for i in range(len(G)):
    for j in G[i]:
        if(j != -1):
            G_T[j].append(i)
for i in range(len(G_T)):
    if(len(G_T[i]) == 0):
        G_T[i].append(-1)

print(kos_sharir_alg(G, G_T))
