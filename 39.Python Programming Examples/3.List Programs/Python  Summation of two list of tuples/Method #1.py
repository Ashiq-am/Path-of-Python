# Python3 code to demonstrate working of
# Summation of two list of tuples
# using list comprehension + zip()

# initialize lists
test_list1 = [(2, 4), (6, 7), (5, 1)]
test_list2 = [(5, 4), (8, 10), (8, 14)]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# Summation of two list of tuples
# using list comprehension + zip()
res = [(x[0] + y[0], x[1] + y[1]) for x, y in zip(test_list1, test_list2)]

# printing result
print("The Summation across lists is : " + str(res))
