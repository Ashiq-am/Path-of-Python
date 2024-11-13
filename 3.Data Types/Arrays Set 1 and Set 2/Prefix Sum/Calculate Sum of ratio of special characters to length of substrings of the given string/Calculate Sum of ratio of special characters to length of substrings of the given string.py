# Python3 program to implement
# the above approach
N = 100005

# Stores frequency of special
# characters in the array
prefix = [0] * N

# Stores prefix sum
sum = [0] * N


# Function to check whether a character
# is special or not
def isSpecial(c, special):
    for i in special:

        # If current character
        # is special
        if (i == c):
            return True

    # Otherwise
    return False


# Function to find sum of ratio of
# count of special characters and
# length of substrings
def countRatio(s, special):
    n = len(s)
    for i in range(n):

        # Calculate the prefix sum of
        # special nodes
        prefix[i] = int(isSpecial(s[i],
                                  special))
        if (i > 0):
            prefix[i] += prefix[i - 1]

    for i in range(n):

        # Generate prefix sum array
        sum[i] = prefix[i]
        if (i > 0):
            sum[i] += sum[i - 1]

    ans = 0
    for i in range(1, n + 1):

        # Calculate ratio for substring
        if i > 1:
            count = sum[n - 1] - sum[i - 2]
        else:
            count = sum[n - 1]
        if i < n:
            count -= sum[n - i - 1]

        ans += count / i

    return ans


# Driver Code
if __name__ == "__main__":
    s = "abcd"
    special = ['b', 'c']

    ans = countRatio(s, special)

    print('%.6f' % ans)
