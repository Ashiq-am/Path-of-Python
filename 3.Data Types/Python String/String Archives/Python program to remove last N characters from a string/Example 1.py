# Python3 code for the above approach

# Function to remove last N
# characters from string
def removeLastN(S, N):
    # Stores the resultant string
    res = ''

    # Traverse the string
    for i in range(len(S) - N):
        # Insert current character
        res += S[i]

    # Return the string
    return res


# Driver Code

# Input
S = "GeeksForGeeks"
N = 5

print(removeLastN(S, N))
