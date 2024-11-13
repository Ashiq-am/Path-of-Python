from functools import reduce
from operator import mul

# generator function


def sliced_prod(sub, K):
	for idx in range(len(sub) - K + 1):

		# slicing and returning intermediate product
		sliced = sub[idx: idx + K]
		yield reduce(mul, sliced)

# generator function


# initializing lists
test_list = [5, 6, 2, 1, 7, 5, 3]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# calling fnc.
res = list(sliced_prod(test_list, K))

# printing result
print("Computed Products : " + str(res))
