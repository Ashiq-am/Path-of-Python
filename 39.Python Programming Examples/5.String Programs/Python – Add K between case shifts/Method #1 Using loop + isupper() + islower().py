# Python3 code to demonstrate working of
# Add K between case shifts
# Using loop + isupper() + islower()
import re

# initializing string
test_str = 'GeeKSforGeEKs'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = '^'

res = ""
for idx in range(0, len(test_str) - 1):
	# checking for case shift
	if test_str[idx].isupper() and test_str[idx + 1].islower() or test_str[idx].islower() and test_str[idx + 1].isupper():
		res = res + test_str[idx] + K
	else:
		res = res + test_str[idx]
res = res + test_str[-1]

# printing result
print("String after alteration : " + str(res))
