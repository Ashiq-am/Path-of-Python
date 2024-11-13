# Python3 code to demonstrate working of
# Consecutive element deletion strings
# Using list comprehension + enumerate()

# initializing string
test_str = 'Geeks4Geeks'

# printing original string
print("The original string is : " + str(test_str))

# Consecutive element deletion strings
# Using list comprehension + enumerate()
res = [test_str[:idx] + test_str[idx + 1:]
		for idx, _ in enumerate(test_str)]

# printing result
print("Consecutive Elements removal list : " + str(res))
