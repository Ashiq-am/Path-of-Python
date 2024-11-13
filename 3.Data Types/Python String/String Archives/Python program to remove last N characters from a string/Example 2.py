# Python3 code for the above approach

# Function to remove last N
# characters from string S
def removeLastN(S, N):
    # Stores resultant string
    res = ''

    # Reversing S
    S = S[::-1]

    # Removing last N characters
    res = S.replace(S[:N], '', 1)

    # Reversing back res
    res = res[::-1]

    # Return the string
    return res


# Driver Code

# Input
S = "GeeksForGeeks"
N = 5

print(removeLastN(S, N))
