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

    def update(self, row, col, val):
        # Update the value at (row, col) to val
        r, c = row + self.n, col + self.m
        self.tree[r][c] = val

        # Update columns
        while c > 1:
            c //= 2
            self.tree[r][c] = self.tree[r][2 * c] + self.tree[r][2 * c + 1]

        # Update rows
        while r > 1:
            r //= 2
            c = col + self.m
            while c >= 1:
                self.tree[r][c] = self.tree[2 * r][c] + self.tree[2 * r + 1][c]
                c //= 2

    def sum_region(self, row1, col1, row2, col2):
        # Get the sum of the elements in the submatrix [(row1, col1), (row2, col2)]
        res = 0
        r1, r2 = row1 + self.n, row2 + self.n + 1
        while r1 < r2:
            if r1 % 2 == 1:
                res += self.sum_col(r1, col1, col2)
                r1 += 1
            if r2 % 2 == 1:
                r2 -= 1
                res += self.sum_col(r2, col1, col2)
            r1 //= 2
            r2 //= 2
        return res

    def sum_col(self, row, col1, col2):
        res = 0
        c1, c2 = col1 + self.m, col2 + self.m + 1
        while c1 < c2:
            if c1 % 2 == 1:
                res += self.tree[row][c1]
                c1 += 1
            if c2 % 2 == 1:
                c2 -= 1
                res += self.tree[row][c2]
            c1 //= 2
            c2 //= 2
        return res


# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

st = SegmentTree2D(matrix)
print(st.sum_region(0, 0, 1, 1))  # Sum of submatrix from (0,0) to (1,1)
st.update(1, 1, 10)
print(st.sum_region(0, 0, 1, 1))  # Sum of submatrix from (0,0) to (1,1) after update
