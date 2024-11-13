class KaryHeap:
    def __init__(self, k):
        self.k = k
        self.heap = []

    def parent(self, i):
        return (i - 1) // self.k

    def child(self, i, j):
        return self.k * i + j + 1
