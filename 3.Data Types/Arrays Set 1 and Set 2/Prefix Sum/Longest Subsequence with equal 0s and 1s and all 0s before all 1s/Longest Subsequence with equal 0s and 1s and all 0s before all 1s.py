# Python3 code to implement the approach
# Function to find the length
# of the longest subsequence
def longestGoodString(s):
    # Size of the string
    n = len(s)

    # The pre is used to store the count of 0s
    # encountered from start to i index

    # The post is used to store the count of 1s
    # encountered from n-1 index to i index
    pre = []
    post = []

    for i in range(n):
        pre.append(0)
    post.append(0)

    if (s[0] is '0'):
        pre[0] = 1

    # Loop to calculate the value of pre[i]
    for i in range(1, n):
        if (s[i] is '0'):
            pre[i] = pre[i - 1] + 1
        else:
            pre[i] = pre[i - 1]

    if (s[n - 1] is '1'):
        post[n - 1] = 1

    # Loop to calculate the value of post[i]
    for i in range(n - 2, -1, -1):
        if (s[i] is '1'):
            post[i] = 1 + post[i + 1]
        else:
            post[i] = post[i + 1]

    # Picking up the maximum possible length
    ans = 0
    for i in range(n):
        ans = max(ans, 2 * min(pre[i], post[i]))

    # Return the maximum length as answer
    return ans


# Driver code
S = "0011001111"

# Function call
print(longestGoodString(S))

# This code is contributed by akashish__
