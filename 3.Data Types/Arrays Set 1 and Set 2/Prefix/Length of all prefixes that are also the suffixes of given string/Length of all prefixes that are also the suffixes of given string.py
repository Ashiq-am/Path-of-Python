# Python3 program for the above approach

# Function to find the length of all
# prefixes of the given that
# are also suffixes of the same string
def countSamePrefixSuffix(s, n):
    # Stores the prefix string
    prefix = ""

    # Traverse the S
    for i in range(n - 1):

        # Add the current character
        # to the prefix string
        prefix += s[i]

        # Store the suffix string
        suffix = s[n - 1 - i: 2 * n - 2 - i]

        # Check if both the strings
        # are equal or not
        if (prefix == suffix):
            print(len(prefix), end=" ")


# Driver Code
if __name__ == '__main__':
    S = "ababababab"
    N = len(S)

    countSamePrefixSuffix(S, N)

# This code is contributed by mohit kumar 29
