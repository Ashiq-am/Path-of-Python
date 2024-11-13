# Python3 program for the above approach

# Function to find the maximum length
# of a subarray of 1s after removing
# at most one 0
def longestSubarray(a, n):
    # Stores the count of consecutive
    # 1's from left
    l = [0] * (n)

    # Stores the count of consecutive
    # 1's from right
    r = [0] * (n)

    count = 0

    # Traverse left to right
    for i in range(n):

        # If cell is non-empty
        if (a[i] == 1):

            # Increase count
            count += 1

        # If cell is empty
        else:

            # Store the count of
            # consecutive 1's
            # till (i - 1)-th index
            l[i] = count
            count = 0

    count = 0
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        if (a[i] == 1):
            count += 1

        else:

            # Store the count of
            # consecutive 1s
            # till (i + 1)-th index
            r[i] = count
            count = 0

    # Stores the length of
    # longest subarray
    ans = -1
    for i in range(n):
        if (a[i] == 0):
            # Store the maximum
            ans = max(ans, l[i] + r[i])

    # If array a contains only 1s
    # return n else return ans
    return ans < 0 and n or ans


# Driver code
arr = [0, 1, 1, 1, 0, 1, 0, 1, 1]

n = len(arr)

print(longestSubarray(arr, n))

# This code is contributed by sanjoy_62
