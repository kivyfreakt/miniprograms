class Queue:
    def __init__ (self):
        self.elements = []
    def empty(self):
        return self.elements == []
    def push(self, element):
        if element not in self.elements:
            self.elements.append(element)
    def top(self):
        return min(self.elements)
    def pop(self):
        return self.element.pop(self.element.index(self.top()))


def prime_alg(n, matrix):
    queue = Queue()
    t


n = int(input())
matrix = [list(map(int, input().split()) for i in range(n)]
