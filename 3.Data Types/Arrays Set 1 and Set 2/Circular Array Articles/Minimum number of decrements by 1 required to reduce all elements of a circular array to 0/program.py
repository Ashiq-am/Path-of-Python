# Python3 program for the above approach

# Function to find minimum operation
# require to make all elemnts 0
def minimumOperations(arr, N):
    # Stores the maximum element and
    # its position in the array
    mx = 0
    pos = 0

    # Traverse the array
    for i in range(N):

        # Update the maximum element
        # and its index
        if (arr[i] >= mx):
            mx = arr[i]
            pos = i

    # Print the minimum number of
    # operations required
    print((mx - 1) * N + pos + 1)


# Driver Code
if __name__ == '__main__':
    arr = [2, 0, 2]
    N = len(arr)

    minimumOperations(arr, N)
