# Python3 code to demonstrate working of
# Remove Columns of Duplicate Elements
# Using list comprehension + set() +
# chain.from_iterable() + generator + loop
from itertools import chain


def dup_idx(sub):

	memo = set()
	for idx, ele in enumerate(sub):

		# adding element if not there
		if ele not in memo:
			memo.add(ele)
		else:

			# return index is Duplicate
			yield idx


# initializing list
test_list = [[4, 3, 5, 2, 3], [6, 4, 2, 1, 1],
			[4, 3, 9, 3, 9], [5, 4, 3, 2, 1]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# passing each row to generator function
# flattening indices at end
temp_idxs = set(chain.from_iterable(dup_idx(sub) for sub in test_list))

# extracting columns with only non-duplicate indices values
res = [[ele for idx, ele in enumerate(
	sub) if idx not in temp_idxs] for sub in test_list]

# printing result
print("The filtered Matrix : " + str(res))
