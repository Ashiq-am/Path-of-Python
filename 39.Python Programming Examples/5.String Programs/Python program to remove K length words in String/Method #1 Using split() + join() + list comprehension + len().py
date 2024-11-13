# Python3 code to demonstrate working of
# Remove K length words in String
# Using split() + join() + list comprehension + len()

# initializing string
test_str = 'Gfg is best for all geeks'

# printing original string
print("The original string is : " + (test_str))

# initializing K
K = 3

# getting splits
temp = test_str.split()

# omitting K lengths
res = [ele for ele in temp if len(ele) != K]

# joining result
res = ' '.join(res)

# printing result
print("Modified String : " + (res))
