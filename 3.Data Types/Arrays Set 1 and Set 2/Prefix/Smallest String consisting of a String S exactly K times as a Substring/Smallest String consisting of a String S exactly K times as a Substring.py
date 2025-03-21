# Python3 program to implement
# the above approach

# KMP algorithm
def kmp(s):
    n = len(s)
    lps = [None] * n
    lps[0] = 0

    i, Len = 1, 0

    while (i < n):

        if (s[i] == s[Len]):
            Len += 1
            lps[i] = Len
            i += 1

        else:
            if (Len != 0):
                Len = lps[Len - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


# Function to return the required string
def findString(s, k):
    n = len(s)

    # Finding the longest proper prefix
    # which is also suffix
    lps = kmp(s)

    # ans string
    ans = ""

    suff = s[0: n - lps[n - 1]: 1]

    for i in range(k - 1):
        # Update ans appending the
        # substring K - 1 times
        ans += suff

    # Append the original string
    ans += s

    # Returning min length string
    # which contain exactly k
    # substring of given string
    return ans


# Driver code
k = 3

s = "geeksforgeeks"

print(findString(s, k))

# This code is contributed by divyeshrabadiya07
