# Python3 code to Find the smallest
# window in a string containing all
# characters of another string
from collections import defaultdict
import sys


def min_window(str, pattern):
    # Function to check validity of source and
    # destination
    def isValid(i, j):
        for item in j:
            if item not in i or i[item] < j[item]:
                return False
        return True

    source = defaultdict(int)
    target = defaultdict(int)

    # Target consist pattern elements and 1
    # as key:value pair
    for e in pattern:
        target[e] += 1

    # Minimum length for window
    minLen = sys.maxsize
    n = len(str)
    ans, j = '', 0
    for i in range(n):

        # Update source for valid source - target pair
        while j < n and (isValid(source, target) == False):
            source[str[j]] += 1
            j += 1

        # Checking validity of source-target pair
        if isValid(source, target):
            if minLen > j - i + 1:
                minLen = j - i + 1
                ans = str[i:j]
        source[str[i]] -= 1
    return ans


# Driver Code
string = "geekforgeeks"
pattern = "gks"
print(min_window(string, pattern))
