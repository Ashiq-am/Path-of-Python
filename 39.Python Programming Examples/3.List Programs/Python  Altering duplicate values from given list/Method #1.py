# Python3 code to demonstrate
# Altering duplicated
# using list comprehension + enumerate()

# initializing list
test_list = [2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + enumerate()
# Altering duplicated
res = [False if (ele in test_list[ :idx]) else ele
			for idx, ele in enumerate(test_list)]

# print result
print("The altered duplicate list is : " + str(res))
