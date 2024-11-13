# Python3 code to demonstrate working of
# Sort by Factor count
# Using sort() + len() + list comprehension


def factor_count(ele):

	# getting factors count
	return len([ele for idx in range(1, ele) if ele % idx == 0])


# initializing list
test_list = [12, 100, 360, 22, 200]

# printing original list
print("The original list is : " + str(test_list))

# performing sort
test_list.sort(key=factor_count)

# printing result
print("Sorted List : " + str(test_list))
