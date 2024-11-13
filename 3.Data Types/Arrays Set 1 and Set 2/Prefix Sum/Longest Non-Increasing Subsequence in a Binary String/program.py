# Python3 program for the above approach

# Function to find the length of the
# longest non-increasing subsequence
def findLength(str, n):
    # Stores the prefix and suffix
    # count of 1s and 0s respectively
    pre = [0] * n
    post = [0] * n

    # Store the number of '1's
    # up to current index i in pre
    for i in range(n):

        # Find the prefix sum
        if (i != 0):
            pre[i] += pre[i - 1]

        # If the current element
        # is '1', update the pre[i]
        if (str[i] == '1'):
            pre[i] += 1

    # Store the number of '0's over
    # the range [i, N - 1]
    for i in range(n - 1, -1, -1):

        # Find the suffix sum
        if (i != (n - 1)):
            post[i] += post[i + 1]

        # If the current element
        # is '0', update post[i]
        if (str[i] == '0'):
            post[i] += 1

    # Stores the maximum length
    ans = 0

    # Find the maximum value of
    # pre[i] + post[i]
    for i in range(n):
        ans = max(ans, pre[i] + post[i])

    # Return the answer
    return ans


# Driver Code
S = "0101110110100001011"
n = len(S)

print(findLength(S, n))


