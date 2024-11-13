# Python3 implementation of the approach
import sys

# Set to store all the strings
# from the given array
uSet = set()

# To store the required count
minCnt = sys.maxsize


# Recursive function to find the count of
# substrings that can be splitted starting
# from the index start such that all
# the substrings are present in the map
def findSubStr(string, cnt, start):
    global minCnt

    # All the chosen substrings
    # are present in the map
    if (start == len(string)):
        # Update the minimum count
        # of substrings
        minCnt = min(cnt, minCnt)

    # Starting from the substrings of length 1
    # that start with the given index
    for length in range(1, len(string) - start + 1):

        # Get the substring
        subStr = string[start: start + length]

        # If the substring is present in the set
        if subStr in uSet:
            # Recursive call for the
            # rest of the string
            findSubStr(string, cnt + 1, start + length)


# Function that inserts all the strings
# from the given array in a set and calls
# the recursive function to find the
# minimum count of substrings str can be
# splitted into that satisfy the given condition
def findMinSubStr(arr, n, string):
    # Insert all the strings from
    # the given array in a set
    for i in range(n):
        uSet.add(arr[i])

    # Find the required count
    findSubStr(string, 0, 0)


# Driver code
if __name__ == "__main__":
    string = "123456"
    arr = ["1", "12345", "2345",
           "56", "23", "456"]

    n = len(arr)

    findMinSubStr(arr, n, string)

    print(minCnt)

# This code is contributed by AnkitRai01
