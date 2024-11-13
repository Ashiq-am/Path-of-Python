# Python3 code to demonstrate
# checking for first digit in elements
# using all() + list comprehension

# initializing list
test_list = [45, 4, 428829, 432]

# printing original list
print("The original list : " + str(test_list))

# using all() + list comprehension
# checking for first digit in elements
res = all(str(i)[0] == str(test_list[0])[0] for i in test_list)

# print result
print("Does each element start with same digit ? " + str(res))
