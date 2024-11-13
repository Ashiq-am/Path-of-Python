# Python3 program for the above approach

# Function to find the minimum number
# of days required to work to at least
# arr[i] points for every array element
def minDays(P, arr):
    # Traverse the array P[]
    for i in range(1, len(P)):
        # Find the prefix sum
        P[i] += P[i] + P[i - 1]

    # Traverse the array arr[]
    for i in range(len(arr)):

        # Find the minimum index of
        # the array having value
        # at least arr[i]
        index = binarySeach(P, arr[i])

        # If the index is not -1
        if (index != -1):
            print(index + 1, end=" ")
        # Otherwise
        else:
            print(-1, end=" ")


# Function to find the lower bound
# of N using binary search
def binarySeach(P, N):
    # Stores the lower bound
    i = 0

    # Stores the upper bound
    j = len(P) - 1

    # Stores the minimum index
    # having value is at least N
    index = -1

    # Iterater while i<=j
    while (i <= j):

        # Stores the mid index
        # of the range [i, j]
        mid = i + (j - i) // 2

        # If P[mid] is at least N
        if (P[mid] >= N):

            # Update the value of
            # mid to index
            index = mid

            # Update the value of j
            j = mid - 1

        # Update the value of i
        else:
            i = mid + 1

    # Return the resultant index
    return index


# Driver Code
if __name__ == '__main__':
    arr = [400, 200, 700, 900, 1400]
    P = [100, 300, 400, 500, 600]
    minDays(P, arr)
