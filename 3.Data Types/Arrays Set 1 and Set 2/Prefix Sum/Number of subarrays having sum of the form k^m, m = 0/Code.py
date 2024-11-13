# Python3 implementation of
# the above approach
from collections import defaultdict

MAX = 100005


def partial_sum(prefix_sum,arr, n):
    for i in range(1, n + 1):
        prefix_sum[i] = (prefix_sum[i - 1] + arr[i - 1])
    return prefix_sum


# Function to count number of
# sub-arrays whose sum is k^p
# where p>=0
def countSubarrays(arr, n, k):
    prefix_sum = [0] * MAX
    prefix_sum[0] = 0

    prefix_sum = partial_sum(prefix_sum,
                             arr, n)
    if (k == 1):
        sum = 0
        m = defaultdict(int)

        for i in range(n, -1, -1):

            # If m[a+b] = c, then add
            # c to the current sum.
            if ((prefix_sum[i] + 1) in m):
                sum += m[prefix_sum[i] + 1]

            # Increase count of prefix sum.
            m[prefix_sum[i]] += 1

        return sum

    if (k == -1):
        sum = 0
        m = defaultdict(int)

        for i in range(n, -1, -1):

            # If m[a+b] = c, then add c
            # to the current sum.
            if ((prefix_sum[i] + 1) in m):
                sum += m[prefix_sum[i] + 1]

            if ((prefix_sum[i] - 1) in m):
                sum += m[prefix_sum[i] - 1]

            # Increase count of prefix sum.
            m[prefix_sum[i]] += 1

        return sum

    sum = 0

    # b = k^p, p>=0
    m = defaultdict(int)

    for i in range(n, -1, -1):
        b = 1
        while (True):

            # k^m can be maximum equal
            # to 10^14.
            if (b > 100000000000000):
                break

            # If m[a+b] = c, then add c
            # to the current sum.
            if ((prefix_sum[i] + b) in m):
                sum += m[prefix_sum[i] + b]

            b *= k

        # Increase count of prefix
        # sum.
        m[prefix_sum[i]] += 1
    return sum


# Driver code
if __name__ == "__main__":
    arr = [2, 2, 2, 2]
    n = len(arr)
    k = 2
    print(countSubarrays(arr, n, k))


