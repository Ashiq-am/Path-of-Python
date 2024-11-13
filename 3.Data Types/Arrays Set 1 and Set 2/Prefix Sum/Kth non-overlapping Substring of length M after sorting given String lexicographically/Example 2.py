# Python program for the above approach:

## Function to get the kth substring
def getKthString(N, M, K, str):
    a = [0] * 26

    ## Storing the frequency of all the characters
    for i in range(N):
        a[ord(str[i]) - ord('a')] += 1

    ## Prefix array
    prefix = [0] * 26
    prefix[0] = a[0]
    for i in range(1, 26):
        prefix[i] = prefix[i - 1] + a[i]

    ## Get the starting index of the kth
    ## lexicographically string
    startingIndex = (K - 1) * M
    var = 0

    ## To track the size of string
    size = 0

    kthString = ""

    for i in range(26):

        ## Prefix array is smaller than
        ## startingIndex or element is not present
        if (prefix[i] < startingIndex or a[i] == 0):
            continue
        ## This case is when prefix array
        ## exceeds the startingIndex for
        ## the first time
        elif (var == 0):
            var = prefix[i] - startingIndex;
            for j in range(var):
                kthString += chr(97 + i)
                size += 1
                if (size == M):
                    break
        ## Prefix array exceeding startingIndex
        ## other than first time
        else:
            for j in range(prefix[i] - prefix[i - 1]):
                kthString += chr(97 + i);
                size += 1
                if (size == M):
                    break
        ## Breaking from the loop if we
        ## get the string of M size
        if (size == M):
            break

    ## Return the resultant string
    return kthString


## Driver code
if __name__ == '__main__':
    N = 6;
    M = 3
    K = 1
    string = "xeabck"

    ## Function call
    print(getKthString(N, M, K, string))

# This code is contributed by entertain2022.
