# Python 3 Program to check if array
# can be split into K contiguous
# subarrays each having equal sum

# function returns true to it is possible to
# create K contiguous partitions each having
# equal sum, otherwise false
def KpartitionsPossible(arr, n, K):
    # Creating and filling prefix sum array
    prefix_sum = [0 for i in range(n)]
    prefix_sum[0] = arr[0]
    for i in range(1, n, 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    # return false if total_sum is not
    # divisible by K
    total_sum = prefix_sum[n - 1]
    if (total_sum % K != 0):
        return False

    # a temporary variable to check
    # there are exactly K partitions
    temp = 0

    pos = -1
    for i in range(0, n, 1):

        # find suitable i for which first
        # partition have the required sum
        # and then find next partition and so on
        if (pos == -1):
            sub = 0
        else:
            sub = prefix_sum[pos]
        if (prefix_sum[i] - sub == total_sum / K):
            pos = i
            temp += 1

        # if it becomes greater than
        # required sum break out
        elif (prefix_sum[i] -
              prefix_sum[pos] > total_sum / K):
            break

    # check if temp has reached to K
    return (temp == K)


# Driver Code
if __name__ == '__main__':
    arr = [4, 4, 3, 5, 6, 2]
    n = len(arr)

    K = 3
    if (KpartitionsPossible(arr, n, K)):
        print("Yes")
    else:
        print("No")
