# Python3 code to demonstrate swapping
# sublist using slice() + itertools.chain.from_iterable()
import itertools

# initializing list
test_list = [1, 4, 5, 8, 3, 10, 6, 7, 11, 14, 15, 2]

# printing the original list
print ("The original list is : " + str(test_list))

# using slice() + itertools.chain.from_iterable()
# swapping sublist
slice_1 = test_list[1 : 3]
slice_2 = test_list[6 : 8]
slice_temp = [slice(0, 1), slice(6, 8), slice(3, 6),
			slice(1, 3), slice(8, len(test_list))]

res = list(itertools.chain.from_iterable([test_list[i]
								for i in slice_temp]))

# printing result
print ("The list after sublist swapping : " + str(res))
