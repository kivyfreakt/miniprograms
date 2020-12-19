def DFS(G, start):
    n = len(G)
    S = []
    S.append(start)
    visited = [False]*n
    visited[start] = True

    while (S != []):
        v = S[-1]
        S.pop()
        for i in G[v]:
            if i != -1:
                if (not visited[i]):
                    visited[i] = True
                    S.append(i)
            else:
                return visited

    return visited

def count_conn_comp(G):
    n = len(G)
    visited = [False]*n
    count = 0

    for i in range(0, n):
        if not visited[i]:
            visited[i] = True;
            v = DFS(G, i);
            count += 1
            for i in range(len(v)):
                if visited[i] == False and v[i] == True:
                     visited[i] = True;

    return count

n = int(input())
G = []
for i in range(n):
    G.append(list(map(int, input().split())))

print(count_conn_comp(G))
