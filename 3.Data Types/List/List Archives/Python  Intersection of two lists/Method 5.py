# Python program to illustrate the intersection
# of two lists, sublists and use of filter()
def intersection(lst1, lst2):
	lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2]
	return lst3

# Driver Code
lst1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
lst2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]
print(intersection(lst1, lst2))
