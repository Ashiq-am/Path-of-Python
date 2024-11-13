# Python3 program for the above approach

# Function to find the minimum sum
# for each query after removing
# element from either ends till each
# value Q[i]
def minOperations(arr, N, Q, M):
    # Stores the prefix sum from
    # both the ends of the array
    m1 = {}
    m2 = {}
    front = 0
    rear = 0

    # Traverse the array from front
    for i in range(N):
        front += arr[i]

        # Insert it into the map m1
        m1[arr[i]] = front

    # Traverse the array in reverse
    for i in range(N - 1, -1, -1):
        rear += arr[i]

        # Insert it into the map m2
        m2[arr[i]] = rear

    # Traverse the query array
    for i in range(M):
        # Print the minimum of the
        # two values as the answer
        print(min(m1[Q[i]], m2[Q[i]]), end=" ")


# Driver Code
arr = [2, 3, 6, 7, 4, 5, 1]
N = len(arr)
Q = [7, 6]
M = len(Q)

# Function Call
minOperations(arr, N, Q, M)

# This code is contributed by avanitrachhadiya2155
