# Python3 code to program to find occurrence
# to each character in given string
from collections import Counter

# initializing string
in_str = "GeeksforGeeks"

# using collections.Counter() to get
# count of each element in string
oup = Counter(in_str)

# printing result
print("Occurrence of all characters in GeeksforGeeks is :\n " + str(oup))
