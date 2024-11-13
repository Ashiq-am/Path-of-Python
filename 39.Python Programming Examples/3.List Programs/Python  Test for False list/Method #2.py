# Python3 code to demonstrate
# to check for False list
# using all()

# initializing list
test_list = [False, False, False, False]

# printing original list
print ("The original list is : " + str(test_list))

flag = 0

# using all()
# to check for False list
res = all(not i for i in test_list)

# printing result
print ("Is List completely false ? : " + str(res))
