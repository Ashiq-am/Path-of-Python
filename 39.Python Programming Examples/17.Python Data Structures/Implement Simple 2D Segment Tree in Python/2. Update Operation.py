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
