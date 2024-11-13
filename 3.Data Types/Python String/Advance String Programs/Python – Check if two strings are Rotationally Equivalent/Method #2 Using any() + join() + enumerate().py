# Python3 code to demonstrate working of
# Check if two strings are Rotationally Equivalent
# Using any() + join() + enumerate()

# initializing strings
test_str1 = 'geeks'
test_str2 = 'eksge'

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# Check if two strings are Rotationally Equivalent
# Using any() + join() + enumerate()
res = any(''.join([test_str2[idx2 - idx1]
		for idx2, val2 in enumerate(test_str2)]) == test_str1
		for idx1, val1 in enumerate(test_str1))

# printing result
print("Are two strings Rotationally equal ? : " + str(res))
