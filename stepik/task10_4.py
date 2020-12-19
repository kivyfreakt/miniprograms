inf = 9999

def FloydWarshall(graph):
    W = graph
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                W[i][j] = min(W[i][j], W[i][k]+W[k][j])
        for i in range(n):
            for j in range(n):
                print(W[i][j], end = " ")
            print("")
        print("\n\n")

graph =[[0, inf, inf, inf, 11],
[13, 0, inf, 4, inf],
[2, 5, 0, 15, inf],
[12, inf, inf, 0, 11],
[inf, 9, 9, inf, 0]
]

FloydWarshall(graph)
