# Python3 code to demonstrate
# alternate elements summation
# using list comprehension + list slicing

# initializing list
test_list = [2, 1, 5, 6, 8, 10]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + list slicing
# alternate elements summation
res = [sum(test_list[i : : 2])
	for i in range(len(test_list)//(len(test_list)//2))]

# print result
print("The alternate elements summation list : " + str(res))
