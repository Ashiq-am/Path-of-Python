# Python3 code to implement the approach

# Function to get the kth substring
def getKthString(N, M, K, str):
    # Sort the entire string
    # We do this by converting the string to a list,
    # then sorting the list
    # then joining the list back
    # into a string
    str = "".join(sorted(list(str)))

    # Get the starting index of the kth
    # lexicographically string
    startingIndex = (K - 1) * M

    kthString = ""

    # To track the size of string
    size = 0
    i = startingIndex

    # Run a loop till size is not equal to M
    while (i < N and size < M):
        # Add the current character to the
        # resulting string
        kthString += str[i]

        # Increase the size by 1
        size += 1
        i += 1

    # Return the resultant string
    return kthString


# Driver Function
N = 6
M = 3
K = 1
str = "xeabcks"

# Function Call
print(getKthString(N, M, K, str))

# This code is contributed by phasing17.
