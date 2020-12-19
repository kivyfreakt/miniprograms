class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def minDistance(self, dist, visited):
        min_item = 9999
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_item and not visited[v]:
                min_item = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, source):
        dist = [9999]*self.V
        visited = [False]*self.V

        dist[source] = 0
        v = source

        while v != -1:
            for u in range(self.V):
                if not visited[u] and self.graph[v][u]:
                    if dist[v] + self.graph[v][u] < dist[u]:
                        dist[u] = dist[v] + self.graph[v][u]
            visited[v] = True
            v = self.minDistance(dist, visited)

            for i in range(self.V):
                print(i, dist[i])
            print("\n")

g = Graph(12)
g.graph = [[9999, 9999, 9999, 9999, 3, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
[2, 9999, 10 ,9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
[9999, 9999, 9999, 9999, 9999, 9999, 7, 9999, 9999, 9999, 9999, 9999],
[9999, 9999, 9999, 9999, 9999, 9999, 9999, 9, 9999, 9999, 9999, 9999],

[3, 6, 9999, 9999, 9999, 4, 9999, 9999, 9999, 9999, 9999, 9999],
[9999, 4, 9999, 9999, 4, 9999, 1, 9999, 6, 9999, 9999, 9999],
[9999, 1, 7, 9999, 9999, 9999, 9999, 9999, 9999, 3, 7, 9999],
[9999, 9999, 9999, 9, 9999, 9999, 4, 9999, 9999, 9999, 4, 5],

[9999, 9999, 9999, 9999, 5, 9999, 9999, 9999, 9999, 6, 9999, 9999],
[9999, 9999, 9999, 9999, 9999, 6, 9999, 9999, 6, 9999, 1, 9999],
[9999, 9999, 9999, 9999, 9999, 9999, 7, 4, 9999, 1, 9999, 7],
[9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 7, 9999]]
g.dijkstra(0)
