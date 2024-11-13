# Python3 code to demonstrate working of
# Extend tuples by count in list
# using loop + chain()
from itertools import chain

# initialize list of tuple
test_list = [('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', )]

# printing original tuples list
print("The original list : " + str(test_list))

# Extend tuples by count in list
# using loop + chain()
res = []
for sub in range(len(test_list)):
	res.append([test_list[sub]]*len(test_list[sub]))
res1 = chain(*res)
res = list(res1)

# printing result
print("The modified and extended list is : " + str(res))
