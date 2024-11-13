# importing module
from operator import mul

# initializing string
test_str = '5x6, 9x10, 7x8'

# printing original string
print("The original string is : " + str(test_str))

# sum() is used to sum the product of each computation
res = sum(mul(*map(int, ele.split('x'))) for ele in test_str.split(', '))

# printing result
print("The computed summation of products : " + str(res))
