# Python3 code to demonstrate working of
# Remove Initial K column elements
# Using loop + del + list slicing

# initialize list
test_list = [[1, 3, 4], [2, 4, 6], [3, 8, 1]]

# printing original list
print("The original list : " + str(test_list))

# initialize K
K = 2

# Remove Initial K column elements
# Using loop + del + list slicing
for sub in test_list: del sub[:K]

# printing result
print("Matrix after removal of front elements from rows : " + str(test_list))
