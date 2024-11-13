# Python3 code to demonstrate working of
# Uppercase selective indices
# Using list comprehension + upper() + join()

# initializing string
test_str = 'geeksgeeksisbestforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing indices list
idx_list = [5, 7, 3, 2, 6, 9]

# one-liner way to solve this problem
res = ''.join([test_str[idx].upper() if idx in idx_list else test_str[idx]
			for idx in range(0, len(test_str))])

# printing result
print("Transformed String : " + str(res))
