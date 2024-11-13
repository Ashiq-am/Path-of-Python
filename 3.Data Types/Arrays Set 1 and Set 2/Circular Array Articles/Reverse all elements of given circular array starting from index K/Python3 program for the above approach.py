# Python3 program for the above approach

# Function to prthe array arr[]
def printArray(arr, N):
    # Print the array
    for i in range(N):
        print(arr[i], end=" ")


# Function to reverse elements of given
# circular array starting from index k
def reverseCircularArray(arr, N, K):
    # Initialize two variables as
    # start = k and end = k-1
    start, end = K, K - 1

    # Initialize count = N/2
    count = N // 2

    # Loop while count > 0
    while (count):

        # Swap the elements at index
        # (start%N) and (end%N)
        temp = arr[start % N]
        arr[start % N] = arr[end % N]
        arr[end % N] = temp

        # Update the start and end
        start += 1
        end -= 1

        # If end equals to -1
        # set end = N-1
        if (end == -1):
            end = N - 1

        count -= 1

    # Print the circular array
    printArray(arr, N)


# Driver Code
if __name__ == '__main__':
    arr = [3, 5, 2, 4, 1]
    K = 2
    N = len(arr)

    # Function Call
    reverseCircularArray(arr, N, K)
