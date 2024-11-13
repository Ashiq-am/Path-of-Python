# Python3 program for
# the above approach

# Function to calculate
# the sum between the
# given range as per value
# of m
def range_sum(arr, a, b):
    # Stores the sum
    sum = 0

    # Condition for a to
    # print the sum between
    # ranges [a, b]
    if (a - 2 < 0):
        sum = arr[b - 1]
    else:
        sum = (arr[b - 1] -
               arr[a - 2])

    # Return sum
    return sum


# Function to precalculate
# the sum of both the vectors
def precompute_sum(arr, brr):
    N = len(arr)

    # Make Prefix sum array
    for i in range(1, N):
        arr[i] = arr[i] + arr[i - 1]
        brr[i] = brr[i] + brr[i - 1]


# Function to compute
# the result for each query
def find_sum(arr, q, Queries):
    # Take a dummy vector
    # and copy the element
    # of arr in brr
    brr = arr.copy()

    N = len(arr)

    # Sort the dummy vector
    brr.sort()

    # Compute prefix sum of
    # both vectors
    precompute_sum(arr, brr)

    # Performs operations
    for i in range(q):

        m = Queries[i][0]
        a = Queries[i][1]
        b = Queries[i][2]

        if (m == 1):

            # Function Call to
            # find sum
            print(range_sum(arr,
                            a, b),
                  end=' ')

        elif (m == 2):

            # Function Call to
            # find sum
            print(range_sum(brr,
                            a, b),
                  end=' ')


# Driver Code
if __name__ == "__main__":
    # Given arr[]
    arr = [0, 6, 4,
           2, 7, 2, 7]

    # Number of queries
    Q = 1

    # Given queries
    Queries = [[2, 3, 6]]

    # Function Call
    find_sum(arr, Q, Queries)
