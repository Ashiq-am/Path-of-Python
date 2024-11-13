# Python3 code to demonstrate working of
# Product and Inter Summation dictionary values
# Using map() + reduce() + lambda + zip() + sum() + generator expression
from functools import reduce

# initializing dictionary
test_dict = {'gfg' : [4, 5, 6], 'is' : [1, 3, 4], 'best' : [7, 8, 9]}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Product and Inter Summation dictionary values
# Using map() + reduce() + lambda + zip() + sum() + generator expression
res = sum(map(lambda ele: reduce(lambda x, y: int(x) * int(y), ele),
										zip(*test_dict.values())))

# printing result
print("The summations of product : " + str(res))
