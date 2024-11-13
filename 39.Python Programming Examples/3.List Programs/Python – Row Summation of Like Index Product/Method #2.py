# Python3 code to demonstrate working of
# Row Summation of Like Index Product
# Using map() + sum() + zip() + lambda

# initializing list
test_list = [[3, 4, 5], [1, 7, 5], [8, 1, 2]]

# printing original list
print("The original list is : " + str(test_list))

# initializing mul list
mul_list = [5, 2, 3]

# Using map() + sum() + zip() + lambda
# Performing product in inner map, by zipping with elements list, and sum at outer map() used.
res = list(map(sum, (map(lambda ele: ([x * y for x, y in zip(
							ele, mul_list)]), test_list))))

# printing result
print("List after multiplication : " + str(res))
