def minSwaps(arr, n):
    # To store total number of ones
    totalCount = 0

    # count total no of ones
    for i in range(0, n):
        totalCount += arr[i]

    currCount = 0  # To store count of ones in current window
    maxCount = 0  # To store maximum count ones out of all windows
    i = 0  # start of window
    j = 0  # end of window

    while (j < n):
        currCount += arr[j]

        # update maxCount when reach window size i.e. total count of ones in array
        if ((j - i + 1) == totalCount):
            maxCount = max(maxCount, currCount)
            if (arr[i] == 1):
                currCount -= 1

            # decrease current count if first element of window is 1
            i += 1  # slide window
        j += 1

    return totalCount - maxCount  # return total no of ones in array - maximum count of ones out of all windows


# Driver Code
a = [1, 0, 1, 0, 1, 1]
n = len(a)
print(minSwaps(a, n))

# this code is contributed by shivanisighss2110
