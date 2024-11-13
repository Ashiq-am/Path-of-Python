# Python3 code for the above approach

# Function to remove last N
# characters from string S
def removeLastN(S, N):
    S = S[:len(S) - N]

    # Return the string
    return S


# Driver Code

# Input
S = "GeeksForGeeks"
N = 5

print(removeLastN(S, N))
