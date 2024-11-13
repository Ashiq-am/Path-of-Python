# initializing list
test_list = [7, 6, -3, -4, -7, 8, 3, -6, 7, 8]

# printing original list
print("The original list is : " + str(test_list))

# list comprehension to provide one liner alternative
res = [idx for idx in range(0, len(test_list) - 1) if test_list[idx] >
	0 and test_list[idx + 1] < 0 or test_list[idx] < 0 and test_list[idx + 1] > 0]

# printing result
print("Sign shift indices : " + str(res))
