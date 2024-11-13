# Python3 code to demonstrate
# increasing alternate element pattern
# using list comprehension + enumerate()

# initializing list
test_list = [1, 2, 3, 4, 5]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + enumerate()
# increasing alternate element pattern
res = [j for sub in ((i, '*' * k)
	for k, i in enumerate(test_list, 1))
	for j in sub]

# print result
print("The increasing element pattern list : " + str(res))
