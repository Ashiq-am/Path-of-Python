# Python3 code to demonstrate
# Merge Range Characters in List
# using join() + list slicing

# initializing list
test_list = ['I', 'L', 'O', 'V', 'E', 'G', 'F', 'G']

# printing original list
print ("The original list is : " + str(test_list))

# initializing Range, i, j
i, j = 3, 7

# using join() + list slicing
# Merge Range Characters in List
test_list[i : j] = [''.join(test_list[i : j])]

# printing result
print ("The list after merging elements : " + str(test_list))
