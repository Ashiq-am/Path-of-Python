# Python3 code to demonstrate
# Contiguous Boolean Ranging
# using sum() + accumulate() + groupby()
from itertools import accumulate, groupby

# initializing list
test_list = [True, True, False, False, False,
			True, True, True, False, False]

# printing the original list
print ("The original list is : " + str(test_list))

# using sum() + accumulate() + groupby()
# for Contiguous Boolean Ranging
res = [0] + list(accumulate(sum(1 for i in j)
			for i, j in groupby(test_list)))

# printing result
print ("The boolean range list is : " + str(res))
