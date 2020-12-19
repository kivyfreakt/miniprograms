class set_union():
    def __init__(self, n):
        self.n = n # количество элементов в множестве
        self.parent = [0] # родительский элемент
        self.size = [0] # количество элементов в поддереве
        for i in range(1, n+1):
            self.parent.append(i)
            self.size.append(1)

    def find(self, v):
        if (self.parent[v] == v):
            return v
        else:
            return self.find(self.parent[v])

    def union(self, v, u):
        r1 = self.find(v) # корни подмножеств
        r2 = self.find(u)

        if r1 == r2:
            return # уже находятся в этом множестве

        if self.size[r1] >= self.size[r2]:
            self.size[r1] += self.size[r2]
            self.parent[r2] = r1
        else:
            self.size[r2] += self.size[r1]
            self.parent[r1] = r2

    def is_same_component(self, v, u):
        return self.find(v) == self.find(u)


def weight_compare(arr):
    return arr[2]

def kruskal(n, m, G):
    count = 0
    s = set_union(n)
    G.sort(key = weight_compare)
    for i in range(m):
        if not s.is_same_component(G[i][0], G[i][1]):
            print(G[i][0], G[i][1])
            count += G[i][2]
            s.union(G[i][0], G[i][1])
    return count

n, m = map(int, input().split())
G = [] # массив ребер

for i in range(m):
    v, u, w = map(int, input().split())
    G.append((v, u, w))

print(kruskal(n, m, G))
