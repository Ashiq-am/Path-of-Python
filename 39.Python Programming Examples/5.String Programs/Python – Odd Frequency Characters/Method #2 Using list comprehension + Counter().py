# Python3 code to demonstrate working of
# Odd Frequency Characters
# Using list comprehension + Counter()
from collections import Counter

# initializing string
test_str = 'geekforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# Odd Frequency Characters
# Using list comprehension + Counter()
res = [ chr for chr, count in Counter(test_str).items() if count & 1 ]

# printing result
print("The Odd Frequency Characters are : " + str(res))
