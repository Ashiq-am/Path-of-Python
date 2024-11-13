# Python3 code to demonstrate working of
# Bigrams Frequency in String
# Using Counter() + generator expression
from collections import Counter

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# Bigrams Frequency in String
# Using Counter() + generator expression
res = Counter(test_str[idx: idx + 2] for idx in range(len(test_str) - 1))

# printing result
print("The Bigrams Frequency is : " + str(dict(res)))
