# Python3 code to demonstrate
# Even Front digits Test in List
# using all() + list comprehension

# initializing list
test_list = [25, 6, 828829, 432]

# printing original list
print("The original list : " + str(test_list))

# using all() + list comprehension
# Even Front digits Test in List
res = all(not int(str(i)[0]) % 2 for i in test_list)

# print result
print("Does each element start with even digit ? " + str(res))
