# Python3 program to implement
# the above approachf
from bisect import bisect_left


# Function to find the smallest index
# of an array element whose value is
# less than or equal to Q[i]
def minimumIndex(arr, Q):
    # Stores size of array
    N = len(arr)

    # Stores coun of queries
    M = len(Q)

    # Store array elements along
    # with the index
    storeArrIdx = []

    # Store smallest index of an array
    # element whose value is greater
    # than or equal to i
    minIdx = [0] * (N)

    # Traverse the array
    for i in range(N):
        # Insert {arr[i], i} into
        # storeArrIdx[]
        storeArrIdx.append([arr[i], i])

    # Sort the array
    arr = sorted(arr)

    # Sort the storeArrIdx
    storeArrIdx = sorted(storeArrIdx)

    # Stores index of arr[N - 1] in
    # sorted order
    minIdx[N - 1] = storeArrIdx[N - 1][1]

    # Traverse the array storeArrIdx[]
    for i in range(N - 2, -1, -1):
        # Update minIdx[i]
        minIdx[i] = min(minIdx[i + 1], storeArrIdx[i][1])

    # Traverse the array Q[]
    for i in range(M):

        # Store the index of
        # lower_bound of Q[i]
        pos = bisect_left(arr, Q[i])

        # If no index found whose value
        # greater than or equal to arr[i]
        if (pos == N):
            print(-1, end=" ")
            continue

        # Prsmallest index whose value
        # greater than or equal to Q[i]
        print(minIdx[pos], end=" ")


# Driver Code
if __name__ == '__main__':
    arr = [1, 9]
    Q = [7, 10, 0]
    minimumIndex(arr, Q)
