# For a given array arr[], returns the
# maximum j – i such that arr[j] > arr[i]
def maxIndexDiff(arr, n):
    rightMax = [0] * n
    rightMax[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], arr[i])

    # rightMax[i] = max arr[i...(n-1]
    maxDist = -2 ** 31
    i = 0
    j = 0

    while (i < n and j < n):
        if (rightMax[j] >= arr[i]):
            maxDist = max(maxDist, j - i)
            j += 1

        else:

            # if(rightMax[j] < leftMin[i])
            i += 1

    return maxDist


# Driver Code
arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
n = len(arr)
maxDiff = maxIndexDiff(arr, n)

print(maxDiff)

# This code is contributed by Shubham Singh
