# Python3 program for the above approach

# Function to print the circular array
def printCircularArray(arr, n):
    # Print the array
    for i in range(n):
        print(arr[i], end=" ")


# Function to sort m elements of diven
# circular array starting from index k
def sortCircularArray(arr, n, k, m):
    # Traverse M elements
    for i in range(m):

        # Iterate from index k to k + m - 1
        for j in range(k, k + m - 1):

            # Check if the next element
            # in the circular array is
            # less than the current element
            if (arr[j % n] > arr[(j + 1) % n]):
                # Swap current element
                # with the next element
                arr[j % n], arr[(j + 1) % n] = (arr[(j + 1) % n],
                                                arr[j % n])

    # Print the circular array
    printCircularArray(arr, n)


# Driver Code
if __name__ == "__main__":
    arr = [4, 1, 6, 5, 3]
    K = 2
    M = 3
    N = len(arr)

    # Function Call
    sortCircularArray(arr, N, K, M)
