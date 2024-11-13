# Python program to illustrate union
# Without repetition
def Union(lst1, lst2):
	final_list = list(set(lst1) | set(lst2))
	return final_list

# Driver Code
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst1, lst2))
