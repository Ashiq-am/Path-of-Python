# Python program for above approach
# import the module
import sys


# Function to minimize the sum
def minimumCost(A, B, N):
    minimuPrice = sys.maxint

    # Checking and comparing for
    # all the possibilities
    for i in range(N):
        for j in range(i, N):
            currentPrice = A[i] + B[j]
            minimuPrice = min(minimuPrice,
                              currentPrice)

    # Return the minimum price found
    return minimuPrice;


# Driver Code
if __name__ == "__main__":
    A = [34, 12, 45, 10, 86, 39, 77]
    B = [5, 42, 29, 63, 30, 33, 20]

    N = len(A)

    # Function Call
    print(minimumCost(A, B, N))

# This code is contributed by hrithikgarg03188.
