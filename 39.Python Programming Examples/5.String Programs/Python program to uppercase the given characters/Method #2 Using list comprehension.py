# Python3 code to demonstrate working of
# Uppercase custom characters
# Using list comprehension

# initializing string
test_str = 'gfg is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing upperlist
upper_list = ['g', 'e', 'b', 'k']

# one-liner used to solve problem
res = "".join([ele.upper() if ele in upper_list else ele for ele in test_str])

# printing result
print("String after reconstruction : " + str(res))
