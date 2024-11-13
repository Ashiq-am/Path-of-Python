# Python code to check if two lists
# have any element in common

# Initialization of list
list1 = [1, 3, 4, 55]
list2 = [90, 22]

flag = 0

# Using in to check element of
# second list into first list
for elem in list2:
	if elem in list1:
		flag = 1

# checking condition
if flag == 1:
	print("True")
else :
	print("False")
