# Python3 code to demonstrate working of
# Rotate dictionary by K
# Using list comprehension + items() + dictionary comprehension

# initializing dictionary
test_dict = {1: 6, 8: 1, 9: 3, 10: 8, 12: 6, 4: 9}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 2

# converting to tuples list
test_dict = list(test_dict.items())

# performing rotate
res = [test_dict[(i - K) % len(test_dict)]
	for i, x in enumerate(test_dict)]

# reconverting to dictionary
res = {sub[0]: sub[1] for sub in res}

# printing result
print("The required result : " + str(res))
