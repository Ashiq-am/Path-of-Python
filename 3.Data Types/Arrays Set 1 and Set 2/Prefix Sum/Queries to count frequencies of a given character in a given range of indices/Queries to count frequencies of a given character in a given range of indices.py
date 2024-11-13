# Python3 program for the above approach

# Function to prcount of char
# y present in the range [l, r]
def noOfChars(s, queries):
    # Length of the string
    n = len(s)

    # Stores the precomputed results
    dp = [[0 for i in range(26)]
          for i in range(n + 1)]

    # Iterate the given string
    for i in range(n):

        # Increment dp[i][y-'a'] by 1
        dp[i + 1][ord(s[i]) - ord('a')] += 1

        # Pre-compute
        for j in range(26):
            dp[i + 1][j] += dp[i][j]

    # Number of queries
    q = len(queries)

    # Traverse each query
    for i in range(q):
        l = queries[i][0]
        r = queries[i][1]
        c = ord(queries[i][2]) - ord('a')

        # Print the result for
        # each query
        print(dp[r] - dp[l - 1], end=" ")


# Driver Code
if __name__ == '__main__':
    # Given string
    S = "aabv"

    # Given Queries
    queries = [[1, 2, 'a'],
               [2, 3, 'b']]

    # Function Call
    noOfChars(S, queries)


