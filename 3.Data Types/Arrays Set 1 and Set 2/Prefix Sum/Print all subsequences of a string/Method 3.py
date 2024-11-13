# Python program to generate power set in lexicographic order.

# str: Stores input string
# n: Length of str.
# curr: Stores current permutation
# index: Index in current permutation, curr
def printSubSeqRec(str, n, index=-1, curr=""):
    # base case
    if (index == n):
        return
    if (len(curr) > 0):
        print(curr)

    i = index + 1

    while (i < n):
        curr = curr + str[i]
        printSubSeqRec(str, n, i, curr)
        curr = curr[0:-1]
        i = i + 1


# Generates power set in lexicographic order.
# function
def printSubSeq(str):
    printSubSeqRec(str, len(str))


# // Driver code
str = "cab"
printSubSeq(str)

# This code is contributed by shinjanpatra
