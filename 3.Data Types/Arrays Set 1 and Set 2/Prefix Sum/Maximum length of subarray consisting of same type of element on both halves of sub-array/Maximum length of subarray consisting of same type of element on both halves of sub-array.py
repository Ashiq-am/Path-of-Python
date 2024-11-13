# Python3 program for the above approach

# Function that finds the maximum
# length of the sub-array that
# contains equal element on both
# halves of sub-array
def maxLengthSubArray(A, N):
    # To store continuous occurence
    # of the element
    forward = [0] * N
    backward = [0] * N

    # To store continuous
    # forward occurence
    for i in range(N):
        if i == 0 or A[i] != A[i - 1]:
            forward[i] = 1
        else:
            forward[i] = forward[i - 1] + 1

    # To store continuous
    # backward occurence
    for i in range(N - 1, -1, -1):
        if i == N - 1 or A[i] != A[i + 1]:
            backward[i] = 1
        else:
            backward[i] = backward[i + 1] + 1

    # To store the maximum length
    ans = 0

    # Find maximum length
    for i in range(N - 1):
        if (A[i] != A[i + 1]):
            ans = max(ans,min(forward[i],backward[i + 1]) * 2)

        # Print the result
    print(ans)


# Driver Code

# Given array
arr = [1, 2, 3, 4, 4, 4, 6, 6, 6, 9]

# Size of the array
N = len(arr)

# Function call
maxLengthSubArray(arr, N)
