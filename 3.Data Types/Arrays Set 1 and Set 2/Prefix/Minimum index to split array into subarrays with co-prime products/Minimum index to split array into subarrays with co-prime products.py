# Python3 program for the
# above approach

# Function to find the
# GCD of 2 numbers
def GCD(a, b):
    # Base Case
    if (b == 0):
        return a

    # Find the GCD recursively
    return GCD(b, a % b)


# Function to find the minimum
# partition index K s.t. product
# of both subarrays around that
# partition are co-prime
def findPartition(nums, N):
    # Stores the prefix and
    # suffix array product
    prefix = [0] * N
    suffix = [0] * N

    prefix[0] = nums[0]

    # Update the prefix
    # array
    for i in range(1, N):
        prefix[i] = (prefix[i - 1] *
                     nums[i])

    suffix[N - 1] = nums[N - 1]

    # Update the suffix array
    for i in range(N - 2, -1, -1):
        suffix[i] = (suffix[i + 1] *
                     nums[i])

    # Iterate the given array
    for k in range(N - 1):

        # Check if prefix[k] and
        # suffix[k+1] are co-prime
        if (GCD(prefix[k],
                suffix[k + 1]) == 1):
            return k

    # If no index for partition
    # exists, then return -1
    return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 5]
    N = len(arr)

    # Function call
    print(findPartition(arr, N))

# This code is contributed by Mohit Kumar 29
