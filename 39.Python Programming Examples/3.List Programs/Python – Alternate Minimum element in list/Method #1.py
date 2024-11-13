# Python code to demonstrate
# Alternate elements Minimimum
# using list comprehension + min()

# initializing list
test_list = [1, 4, 6, 7, 9, 3, 5]

# printing original list
print ("The original list : " + str(test_list))

# using list comprehension + min()
# Alternate elements Minimimum
res = min([test_list[i] for i in range(len(test_list)) if i % 2 != 0])

# printing result
print ("The alternate element list minimum is : " + str(res))
