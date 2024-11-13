# Python3 code to demonstrate working of
# Elements Frequency in Mixed Nested Tuple
# Using recursion + Counter()
from collections import Counter

# helper_fnc
def flatten(test_tuple):
	for tup in test_tuple:
		if isinstance(tup, tuple):
			yield from flatten(tup)
		else:
			yield tup

# initializing tuple
test_tuple = (5, 6, (5, 6), 7, (8, 9), 9)

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Elements Frequency in Mixed Nested Tuple
# Using recursion + Counter()
res = dict(Counter(flatten(test_tuple)))

# printing result
print("The elements frequency : " + str(res))
