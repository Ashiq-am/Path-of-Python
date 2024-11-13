# python 3 program for the above approach
MAX = 100005

from math import sqrt


# Fuction to check wheather a number
# is perfect Number
def isPerfect(N):
    # Stores sum of divisors
    sum = 1

    # Itearate over the range[2, sqrt(N)]
    for i in range(2, int(sqrt(N)) + 1, 1):
        if (N % i == 0):
            if (i * i != N):
                sum = sum + i + N // i
            else:
                sum = sum + i

    # If sum of divisors is equal to
    # N, then N is a perfect number
    if (sum == N and N != 1):
        return True

    return False


# Function to find count of perfect
# numbers in a given range
def Query(arr, N):
    # Stores the count of perfect Numbers
    # upto a every number less than MAX
    prefix = [0 for i in range(MAX + 1)]

    # Iterate over the range [1, MAX]
    for i in range(2, MAX + 1, 1):
        prefix[i] = prefix[i - 1] + isPerfect(i)

    # Traverse the array arr[]
    for i in range(N):
        # Print the count of perfect numbers
        # in the range [arr[i][0], arr[i][1]]
        print(prefix[arr[i][1]] - prefix[arr[i][0] - 1], end=" ")


# Driver Code
if __name__ == '__main__':
    arr = [[1, 1000], [1000, 2000], [2000, 3000]]
    N = len(arr)
    Query(arr, N)
