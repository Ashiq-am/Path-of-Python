# Python code to check if two lists
# have any element in common

# Initialization of list
list1 = [1, 2, 3, 4, 55]
list2 = [2, 3, 90, 22]

# using any function
out = any(check in list1 for check in list2)

# Checking condition
if out:
	print("True")
else :
	print("False")
