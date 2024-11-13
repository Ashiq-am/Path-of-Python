# Python3 implementation of the approach

# Function to return the
# count of sub-strings starting
# from startIndex that are
# also the prefixes of string
def subStringsStartingHere(string, n,
                           startIndex):
    count = 0
    i = startIndex + 1

    while (i <= n):
        if string.startswith(
                string[startIndex: i]):
            count += 1
        else:
            break

        i += 1

    return count


# Function to return the
# count of all possible sub-strings
# of string that are also
# the prefixes of string
def countSubStrings(string, n):
    count = 0

    for i in range(n):

        # If current character is equal to
        # the starting character of str
        if string[i] == string[0]:
            count += subStringsStartingHere(
                string, n, i)

    return count


# Driver Code
if __name__ == "__main__":
    string = "ababc"
    n = len(string)
    print(countSubStrings(string, n))

# this code is contributed by Ryuga
