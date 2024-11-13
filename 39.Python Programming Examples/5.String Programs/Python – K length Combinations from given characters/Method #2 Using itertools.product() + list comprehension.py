# Python3 code to demonstrate working of
# K length Combinations from given characters shorthand
# Using itertools.product() + join() + map()
from itertools import product

# initializing string
test_str = 'gfg'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 2

# list comprehension + join() used to change return data type
res = [''.join(ele) for ele in product(test_str, repeat=K)]

# printing result
print("The generated Combinations : " + str(res))
