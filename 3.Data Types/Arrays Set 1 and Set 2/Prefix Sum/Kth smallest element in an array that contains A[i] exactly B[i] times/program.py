# Python3 program for the above approach

# Function to find the Kth smallest element
# that contains A[i] exactly B[i] times
def KthSmallest(A, B, N, K):
    M = 0

    # Traverse the given array
    for i in range(N):
        M = max(A[i], M)

    # Stores the frequency
    # of every elements
    freq = [0] * (M + 1)

    # Traverse the given array
    for i in range(N):
        freq[A[i]] += B[i]

    # Initialize a variable to
    # store the prefix sums
    sum = 0

    # Iterate over the range [0, M]
    for i in range(M + 1):

        # Increment sum by freq[i]
        sum += freq[i]

        # If sum is greater
        # than or equal to K
        if (sum >= K):
            # Return the current
            # element as answer
            return i

    # Return -1
    return -1


# Driver Code
if __name__ == "__main__":
    # Given Input
    A = [3, 4, 5]
    B = [2, 1, 3]
    N = len(A)
    K = 4

    # Function call
    print(KthSmallest(A, B, N, K))
