# Python3 code to demonstrate working of
# Pair Kth character with each element
# Using join() + zip() + cycle()
from itertools import cycle

# initializing string
test_str = "geeksforgeeks"

# printing original string
print("The original string is : " + test_str)

# initializing K
K = 4

# Pair Kth character with each element
# Using join() + zip() + cycle()
res = list(map(''.join, zip(cycle(test_str[K]), test_str)))

# printing result
print("List after pairing : " + str(res))
