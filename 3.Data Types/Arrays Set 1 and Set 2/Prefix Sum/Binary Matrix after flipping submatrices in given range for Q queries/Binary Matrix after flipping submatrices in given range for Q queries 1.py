# Python3 program to implement
# the above approach

# Function to modify dp[][] array by
# generating prefix sum
def modifyDP(matrix, dp):
    for j in range(1, len(matrix) + 1):

        for k in range(1, len(matrix[0]) + 1):

            # Update the tabular data
            dp[j][k] = dp[j][k] + dp[j - 1][k] \
                       + dp[j][k - 1] - dp[j - 1][k - 1]

            # If the count of flips is even
            if dp[j][k] % 2 != 0:
                matrix[j - 1][k - 1] = int(matrix[j - 1][k - 1]) ^ 1


# Function to update dp[][] matrix
# for each query
def queries_fxn(matrix, queries, dp):
    for q in queries:
        x1, y1, x2, y2 = q

        # Update the table
        dp[x1][y1] += 1
        dp[x2 + 1][y2 + 1] += 1
        dp[x1][y2 + 1] -= 1
        dp[x2 + 1][y1] -= 1

    modifyDP(matrix, dp)


# Driver Code
matrix = [[0, 1, 0], [1, 1, 0]]
queries = [[1, 1, 2, 3],
           [1, 1, 1, 1],
           [1, 2, 2, 3]]

# Initialize dp table
dp = [[0 for i in range(len(matrix[0]) + 2)]
      for j in range(len(matrix) + 2)]

queries_fxn(matrix, queries, dp)
print(matrix)
