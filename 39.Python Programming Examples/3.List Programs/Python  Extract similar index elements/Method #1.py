# Python3 code to demonstrate working of
# Extracting similar index elements
# using loop + zip()

# initialize lists
test_list1 = ["a", "b", "c", "d"]
test_list2 = ["g", "b", "s", "d"]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Extracting similar index elements
# using loop + zip()
res = []
for i, j in zip(test_list1, test_list2):
	if i == j:
		res.append(i)

# printing result
print("Similar index elements in lists : " + str(res))
