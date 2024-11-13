# Python3 program for the above approach

# Size of a column
m = 5


# Function to find the count of
# submatrix whose sum is X
def countSubsquare(arr, n, X):
    dp = [[0 for x in range(m + 1)]
          for y in range(n + 1)]

    # Copying arr to dp and making
    # it indexed 1
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = arr[i][j]

        # Precalculate and store the sum
    # of all rectangles with upper
    # left corner at (0, 0);
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Calculating sum in
            # a 2d grid
            dp[i][j] += (dp[i - 1][j] +
                         dp[i][j - 1] -
                         dp[i - 1][j - 1])

        # Stores the answer
    cnt = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            # Fix upper left corner
            # at {i, j} and perform
            # binary search on all
            # such possible squares

            # Minimum length of square
            lo = 1

            # Maximum length of square
            hi = min(n - i, m - j) + 1

            # Flag to set if sub-square
            # with sum X is found
            found = False

            while (lo <= hi):
                mid = (lo + hi) // 2

                # Calculate lower right
                # index if upper right
                # corner is at {i, j}
                ni = i + mid - 1
                nj = j + mid - 1

                # Calculate the sum of
                # elements in the submatrix
                # with upper left column
                # {i, j} and lower right
                # column at {ni, nj};
                sum = (dp[ni][nj] -
                       dp[ni][j - 1] -
                       dp[i - 1][nj] +
                       dp[i - 1][j - 1])

                if (sum >= X):

                    # If sum X is found
                    if (sum == X):
                        found = True

                    hi = mid - 1

                # If sum > X, then size of
                # the square with sum X
                # must be less than mid
                else:

                    # If sum < X, then size of
                    # the square with sum X
                    # must be greater than mid
                    lo = mid + 1

            # If found, increment
            # count by 1;
            if (found == True):
                cnt += 1
    return cnt


# Driver Code
if __name__ == "__main__":
    N, X = 4, 10

    # Given matrix arr[][]
    arr = [[2, 4, 3, 2, 10],
           [3, 1, 1, 1, 5],
           [1, 1, 2, 1, 4],
           [2, 1, 1, 1, 3]]

    # Function call
    print(countSubsquare(arr, N, X))
