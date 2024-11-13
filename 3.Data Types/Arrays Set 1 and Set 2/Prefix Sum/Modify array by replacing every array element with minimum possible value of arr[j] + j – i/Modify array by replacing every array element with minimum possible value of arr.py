# Python3 program for the above approach

# Function to find minimum value of
# arr[j] + |j - i| for every array index
def minAtEachIndex(n, arr):
    # Stores minimum of a[j] + |i - j|
    # upto position i
    dp1 = [0] * n

    # Stores minimum of a[j] + |i-j|
    # upto position i from the end
    dp2 = [0] * n

    i = 0

    dp1[0] = arr[0]

    # Traversing and storing minimum
    # of a[j]+|i-j| upto i
    for i in range(1, n):
        dp1[i] = min(arr[i], dp1[i - 1] + 1)

    dp2[n - 1] = arr[n - 1]

    # Traversing and storing minimum
    # of a[j]+|i-j| upto i from the end
    for i in range(n - 2, -1, -1):
        dp2[i] = min(arr[i], dp2[i + 1] + 1)

    v = []

    # Traversing from [0, N] and storing minimum
    # of a[j] + |i - j| from starting and end
    for i in range(0, n):
        v.append(min(dp1[i], dp2[i]))

    # Print the required array
    for x in v:
        print(x, end=" ")


# Driver code
if __name__ == '__main__':
    # Given array arr
    arr = [1, 4, 2, 5, 3]

    # Size of the array
    N = len(arr)

    # Function Call
    minAtEachIndex(N, arr)
