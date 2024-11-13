# Consider same previous example.

# Initialize using star operator.
star_list = [[0]] * 5

# Initialize using list Comprehension.
range_list = [[0] for i in range(5)]

star_list[0] = 8  # Expected output will come.
range_list[0] = 8  # Expected output.

''' 
Output: 
	star_list = [8, [0], [0], [0], [0]] 
	range_list = [8, [0], [0], [0], [0]] 
'''

# Unexpected output will come.
star_list[2].append(8)
''' 
	Since star_list[2] = [0]. so it will find for all 
	[0] in list and append '8' to each occurrence of 
	[0]. And will not affect "non [0]" items is list.'''

range_list[2].append(8)  # expected output.

print("Star list : ", star_list)
print("Range list : ", range_list)
