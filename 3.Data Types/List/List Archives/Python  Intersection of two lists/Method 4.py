# Python program to illustrate the intersection
# of two lists
def intersection(lst1, lst2):

	# Use of hybrid method
	temp = set(lst2)
	lst3 = [value for value in lst1 if value in temp]
	return lst3

# Driver Code
lst1 = [9, 9, 74, 21, 45, 11, 63]
lst2 = [4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
print(intersection(lst1, lst2))
