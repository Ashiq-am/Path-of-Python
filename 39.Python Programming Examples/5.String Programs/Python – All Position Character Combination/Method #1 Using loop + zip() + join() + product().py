# Python3 code to demonstrate working of
# All Position Character Combination
# Using loop + zip() + join() + product()
import itertools

# initializing strings
test_str = 'gfg'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = "$"

res = []

# True and false represent Character from String and K respectively.
for sub in itertools.product((True, False), repeat = len(test_str)):
	res.append("".join(chr if ele else K for chr, ele in zip(test_str, sub)))

# printing result
print("The required Combinations : " + str(res))
