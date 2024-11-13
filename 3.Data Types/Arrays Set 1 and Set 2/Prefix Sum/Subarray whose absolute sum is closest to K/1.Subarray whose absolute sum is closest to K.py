# Python Code to find sub-array whose
# sum shows the minimum deviation

def getSubArray(arr, n, K):
    i = -1
    j = -1
    currSum = 0
    # starting index, ending index, Deviation
    result = [i, j, abs(K - abs(currSum))]

    # iterate i and j to get all subarrays
    for i in range(0, n):

        currSum = 0

        for j in range(i, n):
            currSum += arr[j]
            currDev = abs(K - abs(currSum))

            # found sub-array with less sum
            if (currDev < result[2]):
                result = [i, j, currDev]

            # exactly same sum
            if (currDev == 0):
                return result
    return result


# Driver Code
def main():
    arr = [15, -3, 5, 2, 7, 6, 34, -6]

    n = len(arr)

    K = 50

    [i, j, minDev] = getSubArray(arr, n, K)

    if (i == -1):
        print("The empty array shows minimum Deviation")
        return 0

    for i in range(i, j + 1):
        print(arr[i])


main()
