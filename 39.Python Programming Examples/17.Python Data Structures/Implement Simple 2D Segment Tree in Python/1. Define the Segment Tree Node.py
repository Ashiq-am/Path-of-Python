class SegmentTree2D:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return

        self.n = len(matrix)
        self.m = len(matrix[0])
        self.tree = [[0] * (2 * self.m) for _ in range(2 * self.n)]
        self.build(matrix)

    def build(self, matrix):
        # Build the segment tree
        for i in range(self.n):
            for j in range(self.m):
                self.tree[i + self.n][j + self.m] = matrix[i][j]

        # Build columns
        for i in range(self.n):
            for j in range(self.m - 1, 0, -1):
                self.tree[i + self.n][j] = self.tree[i + self.n][2 * j] + self.tree[i + self.n][2 * j + 1]

        # Build rows
        for i in range(self.n - 1, 0, -1):
            for j in range(2 * self.m):
                self.tree[i][j] = self.tree[2 * i][j] + self.tree[2 * i + 1][j]
