def count_bridges(u, parent, curr_h, G, visited, h, f):
    curr_h += 1
    h[u] = curr_h
    f[u] = h[u]
    visited[u] = True
    count = 0
    for i in G[u]:
        if i == parent:
            continue
        if visited[i] == False:
            count += count_bridges(i, u, curr_h, G, visited, h, f)
            f[u] = min(f[u], f[i])
            if f[i] > h[u]:
                count += 1
        else:
            f[u] = min(f[u], h[i])
    return count



n = int(input())
G = []
for i in range(n):
    G.append(list(map(int, input().split())))

print(count_bridges(0, -1, 0, G, [0]*n, [0]*n, [0]*n))
