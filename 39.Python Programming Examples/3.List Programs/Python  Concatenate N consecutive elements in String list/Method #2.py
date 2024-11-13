# Python3 code to demonstrate working of
# Consecutive N concatenation in String list
# using starmap() + zip() + iter() + format()
from itertools import starmap

# initialize list
test_list = ['gfg', 'is', 'good', 'for', 'geek', 'people']

# printing original list
print("The original list : " + str(test_list))

# initialize N
N = 3

# Consecutive N concatenation in String list
# using starmap() + zip() + iter() + format()
temp = '{} ' * N
res = list(starmap(temp.format, zip(*[iter(test_list)] * N)))

# printing result
print("List after N concatenation of String : " + str(res))
