# Python3 code to demonstrate working of
# Remove K length words in String
# Using filter() + lambda + split() + len() + join()

# initializing string
test_str = 'Gfg is best for all geeks'

# printing original string
print("The original string is : " + (test_str))

# initializing K
K = 3

# getting splits
temp = test_str.split()

# omitting K lengths
# filtering using filter() and lambda
res = list(filter(lambda ele: len(ele) != K, temp))

# joining result
res = ' '.join(res)

# printing result
print("Modified String : " + (res))
