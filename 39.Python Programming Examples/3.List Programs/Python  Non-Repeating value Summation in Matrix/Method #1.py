# Python3 code to demonstrate
# Non-Repeating value Summation in Matrix
# set() + list comprehension + sum()

# initializing matrix
test_matrix = [[1, 3, 1], [4, 5, 3], [1, 2, 4]]

# printing the original matrix
print ("The original matrix is : " + str(test_matrix))

# using set() + list comprehension + sum()
# Non-Repeating value Summation in Matrix
res = sum(list(set(i for j in test_matrix for i in j)))

# printing result
print ("Unique values summation in matrix are : " + str(res))
