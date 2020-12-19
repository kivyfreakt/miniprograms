class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def BellmanFord(self, src):
        dist = [9999999]*self.V
        dist[src] = 0
        for k in range(1, self.V):
            x = -1
            for i in range(len(self.graph)):
                if (dist[self.graph[i][0]] < 9999999):
                    if dist[self.graph[i][0]] + self.graph[i][2] < dist[self.graph[i][1]]:
                        dist[self.graph[i][1]] = dist[self.graph[i][0]] + self.graph[i][2]
                        x = self.graph[i][1]
        if x == -1:
            for i in range(self.V):
                print(i, dist[i])
        else:
            print(-1)
