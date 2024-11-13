# Python3 code to demonstrate working of
# Strings Frequency (Case Insensitive)
# Using defaultdict() + lower()
from collections import defaultdict

# initializing list
test_list = ["Gfg", "Best", "best", "gfg", "GFG", "is", "IS", "BEST"]

# printing original list
print("The original list is : " + str(test_list))

res = defaultdict(int)
for ele in test_list:
    # lowercasing to cater for Case Insensitivity
    res[ele.lower()] += 1

# printing result
print("Strings Frequency : " + str(dict(res)))
