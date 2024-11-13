# Python3 code to demonstrate working of
# Replace duplicates in tuple
# using groupby() + loop
from itertools import groupby

# initialize tuple
test_tup = (1, 1, 4, 4, 4, 5, 5, 6, 7, 7)

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Replace duplicates in tuple
# using groupby() + loop
res = tuple()
for key, ele in groupby(test_tup):
	res = res + ((key, ) + ('gfg', ) * (len(list(ele))-1))

# printing result
print("Tuple after replacing values : " + str(res))
