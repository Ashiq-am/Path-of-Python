# Function to find k'th non repeating character
# in string
from collections import OrderedDict


def kthRepeating(input, k):
    # OrderedDict returns a dictionary data
    # structure having characters of input
    # string as keys in the same order they
    # were inserted and 0 as their default value
    dict = OrderedDict.fromkeys(input, 0)

    # now traverse input string to calculate
    # frequency of each character
    for ch in input:
        dict[ch] += 1

    # now extract list of all keys whose value
    # is 1 from dict Ordered Dictionary
    nonRepeatDict = [key for (key, value) in dict.items() if value == 1]

    # now return (k-1)th character from above list
    if len(nonRepeatDict) < k:
        return 'Less than k non-repeating characters in input.'
    else:
        return nonRepeatDict[k - 1]

    # Driver function


if __name__ == "__main__":
    input = "geeksforgeeks"
    k = 3
    print(kthRepeating(input, k))
