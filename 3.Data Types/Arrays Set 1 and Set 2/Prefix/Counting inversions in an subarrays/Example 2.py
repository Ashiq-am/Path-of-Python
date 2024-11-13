# Python3 program for the above approach

# Function to count the number of
# inversions in all the sub-arrays
def findSubarrayInversions(arr, n):
    # Initializing the arrays to 0
    greater = [[0 for i in range(n)]
               for j in range(n)]
    prefix = [[0 for i in range(n)]
              for j in range(n)]
    inversions = [[0 for i in range(n)]
                  for j in range(n)]

    # For each pair of indices i and j
    # calculating the number of elements
    # from i to j inclusive which are
    # greater than arr[i]
    for i in range(0, n):
        for j in range(i + 1, n):
            greater[i][j] = greater[i][j - 1]

            if (arr[i] > arr[j]):
                greater[i][j] += 1

    # Building the prefix table.
    # Prefix[i][j] denotes the sum of
    # greater[0][j], greater[1][j] ... greater[i][j]
    for j in range(0, n):
        prefix[0][j] = greater[0][j]
        for i in range(1, n):
            prefix[i][j] = (prefix[i - 1][j] +
                            greater[i][j])

    # Calculating the inversion count for
    # each subarray using the prefix table
    for i in range(0, n):
        for j in range(i, n):
            if (i == 0):
                inversions[i][j] = prefix[j][j]
            else:
                inversions[i][j] = (prefix[j][j] -
                                    prefix[i - 1][j])

    # Printing the values of the number
    # of inversions in each subarray
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
