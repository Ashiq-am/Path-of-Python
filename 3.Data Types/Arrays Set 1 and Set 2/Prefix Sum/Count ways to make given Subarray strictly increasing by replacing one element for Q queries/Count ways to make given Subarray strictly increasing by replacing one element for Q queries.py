# Python code to implement the approach

# list to store precomputed values
pre = [0] * 100005


# Function to fill pre array
def precompute(a, N):
    for i in range(N):
        if (i == 0):
            # First element can be replaced
            # with every element smaller than
            # next element except itself
            pre[i] = a[1] - 2
        else:

            # If this is not the last element
            if (i != N - 1):
                # Calculate possible values for
                # the current index that it can
                # be replaced with
                pre[i] = a[i + 1] - a[i - 1] - 2


    for i in range(1, N):
        # Calculating prefix sum
        pre[i] += pre[i - 1]


# Function to answer the queries
def solve(Q, Queries, K, a, N):
    # Precomputing values only if there is
    # more than one element
    if (N > 1):
        # Function call
        precompute(a, N)

    # Loop for answering queries
    for i in range(Q):
        # Taking L and R from Queries
        L = Queries[i][0]

        R = Queries[i][1]


        if (L == R):
            # if single element subarray then
            # it can be replaced with K - 1
            # elements
            print(K - 1, end=" ")

        else:
            ans = 0

            # Possible replacements for
            # element at index L
            left = a[L + 1] - 1
            ans += (left - 1)

            # Possible replacements for
            # element at index R
            right = a[R - 1] + 1
            ans += (K - right)

            # Possible replacements for
            # element in range [L + 1, R - 1]
            ans += (pre[R - 1] - pre[L])

            # Printing the answer
            print(ans, end=" ")

# Driver Code
A = [1, 2, 4, 5]
N = len(A)
Q = 2
K = 5
Queries = [[1, 2], [2, 3]]

# Function call
solve(Q, Queries, K, A, N)

# This code is contributed by Atul_kumar_shrivastava.
