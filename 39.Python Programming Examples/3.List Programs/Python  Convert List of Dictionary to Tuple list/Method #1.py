# Python code to demonstrate
# converting list of dictionary to list of tuples

# initialising list of dictionary
ini_list = [{'a':[1, 2, 3], 'b':[4, 5, 6]},
			{'c':[7, 8, 9], 'd':[10, 11, 12]}]

# converting to list of tuples
temp_dict = {}
result = []
for ini_dict in ini_list:
	for key in ini_dict.keys():
		if key in temp_dict:
			temp_dict[key] += ini_dict[key]
		else:
			temp_dict[key] = ini_dict[key]

for key in temp_dict.keys():
	result.append(tuple([key] + temp_dict[key]))

# printing result
print ("Resultant list of tuples: {}".format(result))
