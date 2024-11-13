# Python3 code to demonstrate working of
# Bigrams Frequency in String
# Using Counter() + zip() + map() + join
from collections import Counter

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# Bigrams Frequency in String
# Using Counter() + zip() + map() + join
res = Counter(map(''.join, zip(test_str, test_str[1:])))

# printing result
print("The Bigrams Frequency is : " + str(dict(res)))
