# Python code to demonstrate
# converting list of dictionary to list of tuples

# initialising list of dictionary
ini_list = [{'a':[1, 2, 3], 'b':[4, 5, 6]},
			{'c':[7, 8, 9], 'd':[10, 11, 12]}]

# converting to list of tuples
dict_list = [(key, )+tuple(val) for dic in ini_list
					for key, val in dic.items()]

# printing result
print ("Resultant list of tuples: {}".format(dict_list))
