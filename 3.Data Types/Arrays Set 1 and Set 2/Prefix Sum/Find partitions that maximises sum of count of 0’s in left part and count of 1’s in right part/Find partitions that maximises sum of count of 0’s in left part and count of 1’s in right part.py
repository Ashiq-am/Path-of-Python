# Python program to find partitions
# that maximizes sum of count of 0's
# in left part and count
# of 1's in right part

# Function to find all possible
# max sum partitions
def findPartitions(A):
    N = len(A)
    mx = 0

    # Prefix sum array
    sum = []
    for i in range(0, N + 1):
        sum.append(0)
    ans = []
    for i in range(0, N):
        sum[i + 1] = sum[i] + A[i];

    # Find the partitions
    # with maximum prefix sum
    for i in range(0, N + 1):

        # Calculate score for
        # the current index
        score = i - sum[i] + sum[N] - sum[i]

        # Compare current score
        # with previous max
        if (score > mx):
            ans.clear()
            ans.append(i)
            mx = score

        # If current score
        # is greater than
        # previous then push
        # in the ans array.
        elif (score == mx):
            ans.append(i)

    # Returning the resultant
    # array of indices
    return ans


# Driver code
res = []
arr = [0, 0, 0, 1, 0, 1, 1]
res = findPartitions(arr)
print(res)

# This code is contributed by Samim Hossain Mondal
