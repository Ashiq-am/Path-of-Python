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
