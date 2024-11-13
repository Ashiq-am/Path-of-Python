# Python3 code to demonstrate working of
# Remove front column from Matrix
# Using loop + del + list slicing

# initialize list
test_list = [[1, 3, 4], [2, 4, 6], [3, 8, 1]]

# printing original list
print("The original list : " + str(test_list))

# Remove front column from Matrix
# Using loop + del + list slicing
for ele in test_list: del ele[0]

# printing result
print("Matrix after removal of front column : " + str(test_list))
