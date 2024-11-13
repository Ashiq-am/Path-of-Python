# Python3 program to implement
# the above approach

# Function to prthe cost
# to move all 1s to each index
def costMove1s(arr, N):
    # cost[i] Stores cost to move
    # all 1s at index i
    cost = [0] * N

    # Stores count of 1s on
    # the left side of index i
    cntLeft = 0

    # Stores cost to move all 1s
    # from the left side of index i
    # to index i
    costLeft = 0

    # Traverse the array from
    # left to right.
    for i in range(N):

        # Update cost to move
        # all 1s from left side
        # of index i to index i
        costLeft += cntLeft

        # Update cost[i] to cntLeft
        cost[i] += costLeft

        # If current element is 1.
        if (arr[i] == 1):
            cntLeft += 1

    # Stores count of 1s on
    # the right side of index i
    cntRight = 0

    # Stores cost to move all 1s
    # from the right of index i
    # to index i
    costRight = 0

    # Traverse the array from
    # right to left.
    for i in range(N - 1, -1, -1):

        # Update cost to move
        # all 1s from right side
        # of index i to index i
        costRight += cntRight

        # Update cost[i]
        # to costRight
        cost[i] += costRight

        # If current element
        # is 1.
        if (arr[i] == 1):
            cntRight += 1

    # Print cost to move all 1s
    for i in range(N):
        print(cost[i], end=" ")


# Driver Code
if __name__ == '__main__':
    arr = [0, 1, 0, 1]
    N = len(arr)

    costMove1s(arr, N)


