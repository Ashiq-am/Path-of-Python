# Python3 program for the above approach

# Function to calculate the sum
# between the given range as per
# value of m
def range_sum(v, a, b):
    # Stores the sum
    Sum = 0

    # Loop to calculate the sum
    for i in range(a - 1, b):
        Sum += v[i]

    # Return sum
    return Sum


# Function to find the sum of elements
# for each query
def findSum(v1, q, Queries):
    # Take a dummy vector
    v2 = []

    # Size of vector
    n = len(v1)

    # Copying the elements into
    # dummy vector
    for i in range(n):
        v2.append(v1[i])

    # Sort the dummy vector
    v2.sort()

    # Performs operations
    for i in range(q):
        m = Queries[i][0]
        a = Queries[i][1]
        b = Queries[i][2]

        if (m == 1):

            # Function call to find sum
            print(range_sum(v1, a, b), end=" ")

        elif (m == 2):

            # Function call to find sum
            print(range_sum(v2, a, b), end=" ")


# Driver code

# Given arr[]
arr = [6, 4, 2, 7, 2, 7]

Q = 1

# Given Queries
Queries = [[2, 3, 6]]

# Function call
findSum(arr, Q, Queries)
