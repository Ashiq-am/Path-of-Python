# Python3 program for the above approach

# Function to count the number of
# inversions in all the sub-arrays
def findSubarrayInversions(arr, n):
    inversions = [[0 for i in range(n)]
                  for j in range(n)]

    # Initializing the inversion count
    # of each subarray to 0
    # inversions[i][j] will denote
    # the number of inversions
    # from index i to index j inclusive
    # Generating all subarray
    for i in range(0, n):
        for j in range(0, n):
            ans = 0

            # Counting the number of inversions
            # for a subarray
            for x in range(i, j + 1):
                for y in range(x, j + 1):
                    if (arr[x] > arr[y]):
                        ans += 1

            # Print(ans)
            inversions[i][j] = ans

    # Printing the number of inversions
    # of all subarrays
    for i in range(0, n):
        for j in range(0, n):
            print(inversions[i][j], end=" ")

        print()


# Driver Code

# Given Input
n = 7
arr = [3, 6, 1, 6, 5, 3, 9]

# Function Call
findSubarrayInversions(arr, n)

# This code is contributed by amreshkumar3
