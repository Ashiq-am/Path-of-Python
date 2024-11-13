# Python3 code to demonstrate
# removing multiple spaces
# using list comprehension + zip() + list slicing

# initializing list of lists
test_list = ["GfG", "", "", "", "", "is", "", "", "best"]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + zip() + list slicing
# removing multiple spaces
res = test_list[ : 1] + [j for i, j in
	zip(test_list, test_list[1 : ]) if i or j]

# printing result
print("The list after removing additional spaces : " + str(res))
