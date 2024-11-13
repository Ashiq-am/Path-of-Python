# Python3 program for the above approach

# Function that creates a difference
# array D[] for A[]
def initializeDiffArray(A):
    N = len(A)

    # Stores the difference array
    D = [0] * (N + 1)

    D[0] = A[0]
    D[N] = 0

    # Update difference array D[]
    for i in range(1, N):
        D[i] = A[i] - A[i - 1]

    # Return difference array
    return D


# Function that performs the range
# update queries
def update(D, l, r, x):
    # Update the ends of the range
    D[l] += x
    D[r + 1] -= x


# Function that perform all query
# once with modified update Call
def UpdateDiffArray(DiffArray, Start,
                    End, Val, Freq):
    # For range update, difference
    # array is modified
    update(DiffArray, Start - 1,
           End - 1, Val * Freq)


# Function to take queries
def queriesInput(DiffArray, Q, M):
    # Traverse the query
    for i in range(M):
        # Function Call for updates
        UpdateDiffArray(DiffArray, Q[i][0],
                        Q[i][1], Q[i][2],
                        Q[i][3])


# Function to updates the array
# using the difference array
def UpdateArray(A, D):
    # Traverse the array A[]
    for i in range(len(A)):

        # 1st Element
        if (i == 0):
            A[i] = D[i]

        # A[0] or D[0] decides values
        # of rest of the elements
        else:
            A[i] = D[i] + A[i - 1]


# Function that prints the array
def PrintArray(A):
    # Print the element
    for i in range(len(A)):
        print(A[i], end=" ")

    return


# Function that prthe array
# after performing all queries
def printAfterUpdate(A, Q, M):
    # Create and fill difference
    # array for range updates
    DiffArray = initializeDiffArray(A)

    queriesInput(DiffArray, Q, M)

    # Now update Array A using
    # Difference Array
    UpdateArray(A, DiffArray)

    # Prupdated Array A
    # after M queries
    PrintArray(A)


# Driver Code
if __name__ == '__main__':
    # N = Array size, M = Queries
    N = 3
    M = 3

    # Given array A[]
    A = [1, 2, 3]

    # Queries
    Q = [[1, 2, 1, 4],
         [1, 3, 2, 3],
         [2, 3, 4, 5]]

    # Function call
    printAfterUpdate(A, Q, M)
