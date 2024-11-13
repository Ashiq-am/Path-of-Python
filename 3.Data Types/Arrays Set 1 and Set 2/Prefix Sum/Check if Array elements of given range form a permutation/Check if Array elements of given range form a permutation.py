# Python code to implement the approach

# Function to check if the given range
# of queries form an Permutation or not
# in the given array arr[]
def findPermutation(arr, N, Q, M):
    # Precomputation array
    # stores the sum of all ranges
    # for any L to R
    prefix = [0] * (N + 1)

    # Iterates over the range [1, N]
    for i in range(1, N + 1):
        # Finding prefix sum of
        # given array
        prefix[i] = prefix[i - 1] + arr[i - 1]

    # Traverse the given queries
    for i in range(0, M):

        # Stores range L to R for
        # each query
        L = Q[i][0]
        R = Q[i][1]

        # Size variable stores size of
        # [L, R] range
        size = R - L + 1

        # Stores total from 1 to size of
        # range [L, R]
        total_From_1_To_Size = size * (size + 1) // 2

        # Stores total sum from L to R
        # of Array
        total_From_L_To_R = prefix[R] - prefix[L - 1]

        # If total from 1 to size is equal
        # to total from L to R then print
        # yes
        if (total_From_L_To_R == total_From_1_To_Size):
            print("YES")

        else:
            print("NO")


# Driver Code
if __name__ == "__main__":
    arr = [6, 4, 1, 2, 3, 5, 7]
    Q = [[3, 5], [1, 5], [2, 6]]
    N = len(arr)
    M = len(Q)

    # Function Call
    findPermutation(arr, N, Q, M)

    # This code is contributed by sanjoy_62.