# Python3 program for the above approach

# Function to find the NGE for the
# given circular array arr[]
def printNGE(arr, n):
    # create stack list
    s = []

    # Initialize nge[] array to -1
    nge = [-1] * n

    i = 0

    # Traverse the array
    while (i < 2 * n):

        # If stack is not empty and
        # current element is greater
        # than top element of the stack
        while (len(s) != 0 and arr[i % n] > arr[s[-1]]):
            # Assign next greater element
            # for the top element of the stack
            nge[s[-1]] = arr[i % n]

            # Pop the top element
            # of the stack
            s.pop()

        s.append(i % n)
        i += 1

    # Print the nge[] array
    for i in range(n):
        print(nge[i], end=" ")


# Driver Code
if __name__ == "__main__":
    arr = [4, -2, 5, 8]
    N = len(arr)

    # Function Call
    printNGE(arr, N)


