# Python3 code to demonstrate working of
# Incremental slice partition in list
# Using enumerate() + slice() + next() + iter() + count()
from itertools import islice, count

# initializing list
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# printing original list
print("The original list is : " + str(test_list))

# Incremental slice partition in list
# Using enumerate() + slice() + next() + iter() + count()
res = {key : val for key, val in enumerate(iter(lambda i = iter(test_list),
						c = count(1): list(islice(i, next(c))), []), 1)}

# printing result
print("The partitioned dictionary from list is : " + str(res))
