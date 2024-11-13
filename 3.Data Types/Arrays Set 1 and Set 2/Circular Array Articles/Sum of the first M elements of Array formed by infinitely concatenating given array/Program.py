# Python3 program for the above approach

# Function to find the sum of first
# M numbers formed by the infinite
# concatenation of the array A[]
def sumOfFirstM(A, N, M):
    # Stores the resultant sum
    sum = 0

    # Iterate over the range [0, M - 1]
    for i in range(M):
        # Add the value A[i%N] to sum
        sum = sum + A[i % N]

    # Return the resultant sum
    return sum


# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 3]
    M = 5
    N = len(arr)

    print(sumOfFirstM(arr, N, M))
