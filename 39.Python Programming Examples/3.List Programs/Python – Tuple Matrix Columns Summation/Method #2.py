# Python3 code to demonstrate working of
# Tuple Matrix Columns Summation
# Using map() + list comprehension + zip()

# initializing lists
test_list = [[(4, 5), (3, 2)], [(2, 2), (4, 6)], [(3, 2), (4, 5)]]

# printing original list
print("The original list is : " + str(test_list))

# Tuple Matrix Columns Summation
# Using map() + list comprehension + zip()
res = [tuple(map(sum, zip(*ele))) for ele in zip(*test_list)]

# printing result
print("Tuple matrix columns summation : " + str(res))
