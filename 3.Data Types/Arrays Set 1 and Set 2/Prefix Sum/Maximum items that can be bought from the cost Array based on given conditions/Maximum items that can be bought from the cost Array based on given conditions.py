# Python3 program to find the maximum
# number of items that can be bought
# from the given cost array

# Function to find the maximum
# number of items that can be
# bought from the given cost array
def number(a, n, p, k):
    # Sort the given array
    a.sort()

    # Variables to store the prefix
    # sum, answer and the counter
    # variables
    pre = []
    for i in range(n):
        pre.append(0)

    ans = 0
    val = 0
    i = 0
    j = 0

    # Initializing the first element
    # of the prefix array
    pre[0] = a[0]

    # If we can buy at least one item
    if pre[0] <= p:
        ans = 1

    # Iterating through the first
    # K items and finding the
    # prefix sum
    for i in range(1, k - 1):
        pre[i] = pre[i - 1] + a[i]

        # Check the number of items
        # that can be bought
        if pre[i] <= p:
            ans = i + 1

    pre[k - 1] = a[k - 1]

    # Finding the prefix sum for
    # the remaining elements
    for i in range(k - 1, n):
        if i >= k:
            pre[i] += pre[i - k] + a[i]

        # Check the number of iteams
        # that can be bought
        if pre[i] <= p:
            ans = i + 1

    return ans


# Driver code
n = 5
arr = [2, 4, 3, 5, 7]
p = 11
k = 2

print(number(arr, n, p, k))
