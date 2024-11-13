# Python3 code to demonstrate
# checking unique values in matrix
# set() + list comprehension

# initializing matrix
test_matrix = [[1, 3, 1], [4, 5, 3], [1, 2, 4]]

# printing the original matrix
print ("The original matrix is : " + str(test_matrix))

# using set() + list comprehension
# for checking unique values in matrix
res = list(set(i for j in test_matrix for i in j))

# printing result
print ("Unique values in matrix are : " + str(res))
