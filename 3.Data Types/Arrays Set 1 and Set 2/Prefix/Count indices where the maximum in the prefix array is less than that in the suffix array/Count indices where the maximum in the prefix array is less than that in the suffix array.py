# Python program for the above approach

# Function to print the count of indices
# in which the maximum in prefix arrays
# is less than that in the suffix array
def count(a, n):
    # If size of array is 1
    if (n == 1):
        print(0)
        return

    # pre[]: Prefix array
    # suf[]: Suffix array
    pre = [0] * (n - 1)
    suf = [0] * (n - 1)
    max = a[0]

    # Stores the required count
    ans = 0

    pre[0] = a[0]

    # Find the maximum in prefix array
    for i in range(n - 1):

        if (a[i] > max):
            max = a[i]

        pre[i] = max

    max = a[n - 1]
    suf[n - 2] = a[n - 1]

    # Find the maximum in suffix array
    for i in range(n - 2, 0, -1):

        if (a[i] > max):
            max = a[i]

        suf[i - 1] = max

    # Traverse the array
    for i in range(n - 1):

        # If maximum in prefix array
        # is less than maximum in
        # the suffix array
        if (pre[i] < suf[i]):
            ans += 1

    # Print the answer
    print(ans)


# Driver Code

arr = [2, 3, 4, 8, 1, 4]
N = len(arr)

# Function Call
count(arr, N)

# This code is contributed by code_hunt.
