def BFS(G, start, end):
    n = len(G)
    nodes = []
    visited = [False]*n
    nodes.append(start)
    visited[start] = True
    current_node = 0
    path = [0]*n

    while (current_node < len(nodes)):
        v = nodes[current_node]
        current_node += 1
        for i in G[v]:
            if(not visited[i]):
                nodes.append(i)
                visited[i] = True
                path[i] = path[v] + 1


    v = end
    p = [v]
    while (v != start):
        for i in G[v]:
            if path[i] + 1 == path[v]:
                v = i
                p.append(i)
                break
    return p[::-1]

G = [
[1, 4, 5],
[0, 6],
[5, 3],
[2, 7],
[0, 5, 9],
[0, 2, 4, 9, 10],
[1, 11],
[3, 10],
[9, 13],
[4, 5, 8, 10, 12],
[5, 9, 15],
[6, 14],
[9],
[8, 14],
[11, 13],
[10]
]


start, end = map(int, input().split())
print(*BFS(G, start, end))
