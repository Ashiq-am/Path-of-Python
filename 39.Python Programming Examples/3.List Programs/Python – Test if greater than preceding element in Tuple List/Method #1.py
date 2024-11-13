# Python3 code to demonstrate working of
# Test if greater than preceding element in Tuple List
# Using list comprehension + enumerate()

# initializing list
test_list = [(3, 5, 1), (7, 4, 9), (1, 3, 5)]

# printing original list
print("The original list : " + str(test_list))

# Test if greater than preceding element in Tuple List
# Indices checked using enumerate() and True and false
# values assigned in list comprehension
res = [[True if idx > 0 and j > i[idx - 1] else False
		for idx, j in enumerate(i)] for i in test_list]

# printing result
print("Filtered values : " + str(res))
