# Python code to demonstrate
# converting 2d list into 1d list
# using sum

ini_list = [[1, 2, 3],
			[3, 6, 7],
			[7, 5, 4]]

# printing initial list
print ("initial list ", str(ini_list))

# converting 2d list into 1d
flatten_list = sum(ini_list, [])

# printing flatten_list
print ("final_result", str(flatten_list))

# This code is contributed by
# Mayank Chaudhary - chaudhary_19
