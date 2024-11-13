# Python3 code to demonstrate working of
# Possible Substring count from String
# Using Counter() + list comprehension
from collections import Counter

# initializing string
test_str = "gekseforgeeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing arg string
arg_str = "geeks"

# using Counter to get character frequencies
temp1 = Counter(test_str)
temp2 = Counter(arg_str)
res = min(temp1[char] // temp2[char] for char in temp2.keys())

# printing result
print("Possible substrings count : " + str(res))
