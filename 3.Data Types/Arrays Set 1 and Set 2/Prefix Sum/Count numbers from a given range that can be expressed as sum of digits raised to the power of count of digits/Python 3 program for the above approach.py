# Python 3 program for the above approach
R = 100005
arr = [0 for i in range(R)]


# Function to check if a number N can be
# expressed as sum of its digits raised
# to the power of the count of digits
def canExpress(N):
    temp = N

    # Stores the number of digits
    n = 0
    while (N != 0):
        N //= 10
        n += 1

    # Stores the resultant number
    N = temp
    sum = 0
    while (N != 0):
        sum += pow(N % 10, n)
        N //= 10

    # Return true if both the
    # numbers are same
    return (sum == temp)


# Function to precompute and store
# for all numbers whether they can
# be expressed
def precompute():
    # Mark all the index which
    # are plus perfect number
    for i in range(1, R, 1):

        # If true, then update the
        # value at this index
        if (canExpress(i)):
            arr[i] = 1

    # Compute prefix sum of the array
    for i in range(1, R, 1):
        arr[i] += arr[i - 1]


# Function to count array elements that
# can be expressed as the sum of digits
# raised to the power of count of digits
def countNumbers(queries, N):
    # Precompute the results
    precompute()

    # Traverse the queries
    for i in range(N):
        L1 = queries[i][0]
        R1 = queries[i][1]

        # Print the resultant count
        print((arr[R1] - arr[L1 - 1]), end=" ")


# Driver Code
if __name__ == '__main__':
    queries = [[1, 400], [1, 9]]
    N = len(queries)
    countNumbers(queries, N)


