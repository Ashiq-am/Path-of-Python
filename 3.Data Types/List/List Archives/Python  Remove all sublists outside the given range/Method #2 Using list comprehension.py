# Python code to remove all the
# sublist outside the given range

# Initialisation of list of list
list = [[11, 12, 15, 17, 3],
		[3, 1, 4, 5.2, 9, 19],
		[2, 4, 6, 7.2, 8.9]]

# Defining range
left = 1
right = 9

# Using list comprehension
Output = [i for i in list if (min(i)>=left and max(i)<=right)]

# Printing output
print (Output)
