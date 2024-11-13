# Python3 code to demonstrate
# K Character Split String
# using zip() + chain() + cycle()
from itertools import chain, cycle

# initializing string
test_string = "GfG_is_Best"

# printing original string
print("The original string : " + str(test_string))

# initializing K
K = "_"

# using zip() + chain() + cycle()
# K Character Split String
res = list(chain(*zip(test_string.split(K), cycle(K))))[:-1]

# print result
print("The list without omitting character : " + str(res))
