# Python 3 program for the above approach

# Function to perform the given queries
# in the given empty array of size N
def updateQuery(queries, N):
    # Initialize an array a[]
    a = [0 for i in range(N + 1)]

    # Stores the size of the array
    n = N + 1

    q = len(queries)

    # Traverse the queries
    for i in range(q):

        # Starting index
        l = queries[i][0]

        # Ending index
        r = queries[i][1]

        # Increment each index from L to
        # R in a[] by (j - l + 1)
        for j in range(l, r + 1, 1):
            a[j] += (j - l + 1)

    # Print the modified array
    for i in range(1, N + 1, 1):
        print(a[i], end=" ")


# Driver Code
if __name__ == '__main__':
    N = 7
    queries = [[1, 7], [3, 6], [4, 5]]

    # Function Call
    updateQuery(queries, N)
