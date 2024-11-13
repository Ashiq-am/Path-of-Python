# Python3 program to find the sum of
# the addition of all possible subsets.

# Function that answers all the queries
def solveQueries(Str, query):
    # Length of the String
    ll = len(Str)

    # Number of queries
    Q = len(query)

    # Prefix array
    pre = [[0 for i in range(256)]
           for i in range(ll)]
    # memset(pre, 0, sizeof pre)

    # Iterate for all the characters
    for i in range(ll):

        # Increase the count of the character
        pre[i][ord(Str[i])] += 1

        # Presum array for
        # all 26 characters
        if (i):

            # Update the prefix array
            for j in range(256):
                pre[i][j] += pre[i - 1][j]

    # Answer every query
    for i in range(Q):

        # Range
        l = query[i][0]
        r = query[i][1]
        maxi = 0
        c = 'a'

        # Iterate for all characters
        for j in range(256):

            # Times the lowercase character
            # j occurs till r-th index
            times = pre[r][j]

            # Subtract the times it occurred
            # till (l-1)th index
            if (l):
                times -= pre[l - 1][j]

            # Max times it occurs
            if (times > maxi):
                maxi = times
                c = chr(j)

        # Print the answer
        print("Query ", i + 1, ": ", c)


# Driver Code
Str = "striver"
query = [[0, 1], [1, 6], [5, 6]]
solveQueries(Str, query)

# This code is contributed by Mohit Kumar
