## Python program for the above approach:

## Define the prefix sum arrays globally
prefix_sum_row = [[0] * 51 for _ in range(50)]
prefix_sum_col = [[0] * 50 for _ in range(51)]


def is_valid(r, c, size, grid):
    r_end = r + size
    c_end = c + size

    ## Diagonal sum
    sum = 0;
    j = c
    for i in range(r, r_end):
        sum += grid[i][j];
        j += 1

    ## Check each row
    for i in range(r, r_end):
        if ((prefix_sum_row[i][c_end] - prefix_sum_row[i]) != sum):
            return False

    ## Check each column
    for i in range(c, c_end):
        if ((prefix_sum_col[r_end][i] - prefix_sum_col[r][i]) != sum):
            return False

    ## Check anti-diagonal
    ad_sum = 0;
    j = c_end - 1
    for i in range(r, r_end):
        ad_sum += grid[i][j]
        j -= 1

    return (ad_sum == sum)


def largestSquareValidMatrix(grid):
    ## Store the size of the given grid
    m = len(grid)
    n = len(grid[0])

    ## Compute the prefix sum for the rows
    for i in range(0, m):
        for j in range(1, n + 1):
            prefix_sum_row[i][j] = prefix_sum_row[i][j - 1] + grid[i][j - 1];

    ## Compute the prefix sum for the columns
    for i in range(1, m + 1):
        for j in range(0, n):
            prefix_sum_col[i][j] = prefix_sum_col[i - 1][j] + grid[i - 1][j]

    ## Check for all possible square submatrix
    for size in range(min(m, n), 1, -1):
        for i in range(0, m - size + 1):
            for j in range(0, n - size + 1):
                if (is_valid(i, j, size, grid)):
                    return size

    return 1


## Driver code
if __name__ == '__main__':
    grid = [[7, 1, 4, 5, 6],
            [2, 5, 1, 6, 4],
            [1, 5, 4, 3, 2],
            [1, 2, 7, 3, 4]
            ]

    print(largestSquareValidMatrix(grid))

# This code is contributed by subhamgoyal2014.
