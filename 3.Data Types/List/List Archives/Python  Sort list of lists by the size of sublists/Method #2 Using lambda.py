# Python code to demonstrate
# sort list of list
# on the basis of size of sublist

ini_list = [[1, 2, 3], [1, 2], [1, 2, 3, 4],
				[1, 2, 3, 4, 5], [2, 4, 6]]

# printing initial ini_list
print ("initial list", str(ini_list))

# sorting on bais of size of list
ini_list.sort(key = lambda x:len(x))

# printing final result
print("final list", str(ini_list))
