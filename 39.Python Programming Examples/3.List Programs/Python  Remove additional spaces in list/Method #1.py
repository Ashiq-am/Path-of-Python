# Python3 code to demonstrate
# removing multiple spaces
# using list comprehension + enumerate()

# initializing list of lists
test_list = ["GfG", "", "", "", "", "is", "", "", "best"]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + enumerate()
# removing multiple spaces
res = [val for idx, val in enumerate(test_list)
	if val or (not val and test_list[idx - 1])]

# printing result
print("The list after removing additional spaces : " + str(res))
