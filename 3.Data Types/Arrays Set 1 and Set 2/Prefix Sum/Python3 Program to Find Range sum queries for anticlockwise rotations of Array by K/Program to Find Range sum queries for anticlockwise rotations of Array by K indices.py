# Python3 program to calculate range sum
# queries for anticlockwise
# rotations of the array by K

# Function to execute the queries
def rotatedSumQuery(arr, n, query, Q):
    # Construct a new array
    # of size 2*N to store
    # prefix sum of every index
    prefix = [0] * (2 * n)

    # Copy elements to the new array
    for i in range(n):
        prefix[i] = arr[i]
        prefix[i + n] = arr[i]

    # Calculate the prefix sum
    # for every index
    for i in range(1, 2 * n):
        prefix[i] += prefix[i - 1]

    # Set start pointer as 0
    start = 0

    for q in range(Q):

        # Query to perform
        # anticlockwise rotation
        if (query[q][0] == 1):
            k = query[q][1]
            start = (start + k) % n

        # Query to answer range sum
        elif (query[q][0] == 2):
            L = query[q][1]
            R = query[q][2]

            # If pointing to 1st index
            if (start + L == 0):

                # Display the sum upto start + R
                print(prefix[start + R])

            else:

                # Subtract sum upto start + L - 1
                # from sum upto start + R
                print(prefix[start + R] -
                      prefix[start + L - 1])


# Driver code
arr = [1, 2, 3, 4, 5, 6]

# Number of query
Q = 5

# Store all the queries
query = [[2, 1, 3],
         [1, 3],
         [2, 0, 3],
         [1, 4],
         [2, 3, 5]]

n = len(arr)
rotatedSumQuery(arr, n, query, Q)


