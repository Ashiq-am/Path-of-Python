# Python3 code to demonstrate
# Split list into lists by particular value
# Using list comprehension + zip() + slicing + enumerate()

# initializing list
test_list = [1, 4, 5, 6, 4, 5, 6, 5, 4]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + zip() + slicing + enumerate()
# Split list into lists by particular value
size = len(test_list)
idx_list = [idx + 1 for idx, val in
			enumerate(test_list) if val == 5]


res = [test_list[i: j] for i, j in
		zip([0] + idx_list, idx_list +
		([size] if idx_list[-1] != size else []))]

# print result
print("The list after splitting by a value : " + str(res))
