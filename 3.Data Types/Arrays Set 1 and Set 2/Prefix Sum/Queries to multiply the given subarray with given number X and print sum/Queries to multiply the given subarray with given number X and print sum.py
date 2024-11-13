# Python3 implementation to multiply
# the given subarray by the x
# for multiple queries of the Q

# Function to answer each query
def query(pre_sum, n, l, r, val):
    ans = 0
    temp = 0
    if (l > 0):
        temp = pre_sum[l - 1]

    ans = val * (pre_sum[r] - temp)
    return ans


# Function to multiply the subarray
# by the x for multiple Queries
def multiplyArray(arr, q, n):
    pre_sum = []
    s = 0

    # Loop to compute the prefix
    # sum of the array
    for i in range(n):
        s += arr[i]
        pre_sum.append(s)

    # Loop to answer each query
    for i in q:
        print(query(pre_sum, n, i[0][0], i[0][1], i[1]))


# Driver Code
if __name__ == '__main__':
    # Array
    arr = [2, 3, 4, 2, 5, 1]
    n = 6
    q = []
    q.append([[2, 4], 5])
    q.append([[1, 1], 4])
    q.append([[1, 3], -2])

    # Function Call
    multiplyArray(arr, q, n)


