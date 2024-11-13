# Python3 code to demonstrate
# Custom Multiplication in list of lists
# Using list comprehension + enumerate()

# initializing list
test_list = [[5, 6, 8], [7, 4, 3], [8, 10, 12]]

# initializing multiply list
mult_list = [10, 20, 30]

# printing original list
print("The original list : " + str(test_list))

# printing multiply list
print("The original multiply list : " + str(mult_list))

# using list comprehension + enumerate()
# Custom Multiplication in list of lists
res = [[mult_list[i] * j for j in sub]
	for i, sub in enumerate(test_list)]

# print result
print("The list after multiply : " + str(res))
