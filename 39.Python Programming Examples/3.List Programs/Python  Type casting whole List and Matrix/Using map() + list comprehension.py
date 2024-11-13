# Python3 code to demonstrate working of
# Type casting whole List and Matrix
# using map() + list comprehension

# helper function to type cast list
def cast_list(test_list, data_type):
    return list(map(data_type, test_list))


# helper function to type cast Matrix
def cast_matrix(test_matrix, data_type):
    return list(map(lambda sub: list(map(data_type, sub)), test_matrix))


# initialize list
test_list = [1, 4, 9, 10, 19]

# initialize Matrix
test_matrix = [[5, 6, 8], [8, 5, 3], [9, 10, 3]]

# printing original list
print("The original list is : " + str(test_list))

# printing original matrix
print("The original Matrix is : " + str(test_matrix))

# Type casting whole List and Matrix
# using map() + list comprehension
res_list = cast_list(test_list, str)
res_matrix = cast_matrix(test_matrix, str)

# printing result
print("The List after type casting is : " + str(res_list))
print("The Matrix after type casting is : " + str(res_matrix))
