# Python3 code to demonstrate working of
# Remove last element from each row in Matrix
# Using loop + del + list slicing

# initialize list
test_list = [[1, 3, 4], [2, 4, 6], [3, 8, 1]]

# printing original list
print("The original list : " + str(test_list))

# Remove last element from each row in Matrix
# Using loop + del + list slicing
for ele in test_list: del ele[-1]

# printing result
print("Matrix after removal of rear element from rows : " + str(test_list))
