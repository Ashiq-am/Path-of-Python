# Python3 code to demonstrate working of
# Maximum of Tuple List Similar Indices
# using max() + zip() + map()

# initialize lists
test_list1 = [(2, 4), (6, 7), (5, 1)]
test_list2 = [(5, 4), (8, 10), (8, 14)]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Maximum of Tuple List Similar Indices
# using max() + zip() + map()
res = [tuple(map(max, zip(a, b)))
	for a, b in zip(test_list1, test_list2)]

# printing result
print("The Maximum across lists is : " + str(res))
