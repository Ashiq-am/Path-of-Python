# Python3 code to demonstrate
# String Split including spaces
# using zip() + chain() + cycle()
from itertools import chain, cycle

# initializing string
test_string = "GfG is Best"

# printing original string
print("The original string : " + str(test_string))

# using zip() + chain() + cycle()
# String Split including spaces
res = list(chain(*zip(test_string.split(), cycle(' '))))[:-1]

# print result
print("The list without omitting spaces : " + str(res))
