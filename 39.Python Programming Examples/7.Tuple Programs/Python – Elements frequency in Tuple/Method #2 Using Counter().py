# Python3 code to demonstrate working of
# Elements frequency in Tuple
# Using Counter()
from collections import Counter

# initializing tuple
test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# converting result back from defauldict to dict
res = dict(Counter(test_tup))

# printing result
print("Tuple elements frequency is : " + str(res))
