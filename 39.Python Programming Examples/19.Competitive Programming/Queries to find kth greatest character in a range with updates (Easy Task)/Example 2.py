# Python3 Program to implement
# the above approach
# Function to find the kth greatest
# character from the string
def find_kth_largest(strr, k):
    # Sorting the in
    # non-increasing Order
    strr = sorted(strr)
    strr = strr[:: -1]
    return strr[k - 1]


# Function to print the K-th character
# from the subS[l] .. S[r]
def printCharacter(strr, l, r, k):
    # 0-based indexing
    l = l - 1
    r = r - 1

    # Subof strr from the
    # indices l to r.
    temp = strr[l: r - l + 1]

    # Extract kth Largest character
    ans = find_kth_largest(temp, k)

    return ans


# Function to replace character at
# pos of strr by the character s
def updateString(strr, pos, s):
    # Index of S to be updated.
    index = pos - 1
    c = s

    # Character to be replaced
    # at index in S
    strr[index] = c


# Driver Code
if __name__ == '__main__':
    # Given string
    strr = "abcddef"
    strr = [i for i in strr]

    # Count of queries
    Q = 3

    # Queries
    print(printCharacter(strr, 1, 2, 2))
    updateString(strr, 4, 'g')
    print(printCharacter(strr, 1, 5, 4))

# This code is contributed by Mohit Kumar 29
