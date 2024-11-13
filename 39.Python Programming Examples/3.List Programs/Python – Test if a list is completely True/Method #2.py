# Python3 code to demonstrate
# Pure List Test
# using all()

# initializing list
test_list = [True, True, True, True]

# printing original list
print ("The original list is : " + str(test_list))

flag = 0

# using all()
# Pure List Test
res = all(i for i in test_list)

# printing result
print ("Is List completely True ? : " + str(res))
