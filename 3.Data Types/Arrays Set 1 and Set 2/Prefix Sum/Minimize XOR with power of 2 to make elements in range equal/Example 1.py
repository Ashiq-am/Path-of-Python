# Python code to implement the approach

# Function to calculate minimum operation
def MinimumOperations(N, A, Q, query):
    # List to store ans of all queries
    ans = []

    # Loop to calculate the minimum number
    # of operations for each query
    for i in range(Q):
        l = query[i][0]
        r = query[i][1]

        # To store answer for current query
        y = 0
        n = r - l + 1

        # loop for calculating at
        # number of setbits from
        # 0th to 31st bit
        for j in range(32):
            setbitcount = 0
            for i in range(l, r + 1):
                mask = 2 ** j
                if (A[i] & mask):
                    setbitcount = setbitcount + 1
            y = y + min(setbitcount, n - setbitcount)

        ans.append(y)

    return ans


# Driver code

A = [2, 3, 1, 7]
N = len(A)
query = [[0, 2]]

# Function call
v = MinimumOperations(N, A, 1, query)
for i in range(len(v)):
    print(v[i], end=" ")

# This code is contributed by Pushpesh Raj.
