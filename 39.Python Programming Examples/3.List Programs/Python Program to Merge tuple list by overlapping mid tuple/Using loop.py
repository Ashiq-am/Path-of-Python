# Python3 code to demonstrate working of
# Merge tuple list by overlapping mid tuple
# Using loop


# initializing lists
test_list1 = [(4, 8), (19, 22), (28, 30), (91, 98)]
test_list2 = [(10, 22), (23, 26), (15, 20), (52, 58)]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

idx = 0
j = 0
res = list()

# iterating till anyone of list exhausts.
while j < len(test_list2):

	# checking for mid tuple and appending
	if test_list2[j][0] > test_list1[idx][0]\
	and test_list2[j][1] < test_list1[idx + 1][1]:

		# appending the range element from 2nd list which
		# fits consecution along with original elements
		# from 1st list.
		res.append((test_list1[idx], test_list2[j], test_list1[idx + 1]))
		j += 1
		idx = 0
	else:

		# if not, the 1st list is iterated and next two
		# ranges are compared for a fit.
		idx += 1

	# restart indices once limits are checked.
	if idx == len(test_list1) - 1:
		idx = 0
		j += 1

# printing result
print("Merged Tuples : " + str(res))
