# Python3 code to demonstrate
# to check for False list
# using any()

# initializing list
test_list = [False, False, False, False]

# printing original list
print ("The original list is : " + str(test_list))

# using any()
# to check for False list
res = not any(test_list)

# printing result
print ("Is List completely false ? : " + str(res))
