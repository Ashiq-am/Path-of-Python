# Python3 program for
# the above approach

# Function to find whether the path
# exists with all element even or not
def answerQueries(n, q, a, b, Queries):
    # Add 0 to beginning to make
    # 1-based-indexing
    # a[0]=0;
    # b[0]=0;
    # Change elements based on parity
    # and take prefix sum
    # 1 is odd and 0 is even
    # Traverse the array R
    for i in range(1, n + 1):

        # Taking & to check parity
        if ((a[i] & 1) != 0):
            a[i] = 1
        else:
            a[i] = 0

        # Build prefix sum array
        a[i] += a[i - 1]

    # Traverse the array C
    for i in range(1, n + 1):

        # Taking & to check parity
        if ((b[i] & 1) != 0):
            b[i] = 1
        else:
            b[i] = 0

        # Build prefix sum array
        b[i] += b[i - 1]

    # Traverse the matrix Queries
    for i in range(0, q):
        ra = Queries[i][0]
        ca = Queries[i][1]
        rb = Queries[i][2]
        cb = Queries[i][3]

        r2 = max(ra, rb)
        r1 = min(ra, rb)
        c2 = max(ca, cb)
        c1 = min(ca, cb)

        # Check if all numbers are of
        # same parity between (r1 to r2)
        if ((a[r2] - a[r1 - 1] == 0) or
                (a[r2] - a[r1 - 1] == r2 - r1 + 1)):

            # Check if all numbers are of
            # same parity between (r1 to r2)
            if ((b[c2] - b[c1 - 1] == 0) or
                    (b[c2] - b[c1 - 1] == c2 - c1 + 1)):
                # Path exists
                print("Yes", end=" ")
                continue

        # No path exists
        print("No", end=" ")


# Driver Code
if __name__ == '__main__':
    # Given N, Q
    N = 5
    Q = 3

    # Given array R and C
    R = [0, 6, 2, 7, 8, 3]
    C = [0, 3, 4, 8, 5, 1]

    # Given queries
    Queries = [[2, 2, 1, 3],
               [4, 2, 4, 3],
               [5, 1, 3, 4]]

    # Function call
    answerQueries(N, Q, R, C, Queries)


