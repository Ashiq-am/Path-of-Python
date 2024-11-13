# Python3 code to demonstrate working of
# All Position Character Combination
# Using list comprehension
import itertools

# initializing strings
test_str = 'abc'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = "$"

# one liner to perform this task
res = ["".join(chr if ele else K for chr, ele in zip(test_str, sub)) \
	for sub in itertools.product((True, False), repeat = len(test_str))]

# printing result
print("The required Combinations : " + str(res))
