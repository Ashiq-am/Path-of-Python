# Python code to demonstrate
# Alternate elements Minimimum
# using enumerate() + min()

# initializing list
test_list = [1, 4, 6, 7, 9, 3, 5]

# printing original list
print ("The original list : " + str(test_list))

# using enumerate() + min()
# Alternate elements Minimimum
res = min([i for j, i in enumerate(test_list) if j % 2 != 0])

# printing result
print ("The alternate element list minimum is : " + str(res))
