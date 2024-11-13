# Python3 progrma of
# simple approach to
# find maximum value
# after m range increments.
import sys


# Function to find the
# maximum element after
# m operations
def findMax(n, a, b, k, m):


    arr = [0] * n

    # Start performing m operations
    for i in range(m):
        # Store lower and upper
        # index i.e. range
        lowerbound = a[i]
        upperbound = b[i]

        # Add 'k[i]' value at
        # this operation to whole range
        for j in range(lowerbound,upperbound + 1):
            arr[j] += k[i]

            # Find maximum value after
            # all operations and return
            res = -sys.maxsize - 1


            for i in range(n):
                res = max(res, arr[i])
                return res

# Driver code
if __name__ == "__main__":
    # Number of values
    n = 5
    a = [0, 1, 2]
    b = [1, 4, 3]

    # Value of k to be added
    # at each operation
    k = [100, 100, 100]


    m = len(a)


    print("Maximum value after 'm' operations is ",findMax(n, a, b, k, m))
