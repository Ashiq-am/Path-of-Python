# Python code to demonstrate
# to construct alternate element list
# using Slice notation

# initializing list
test_list = [1, 4, 6, 7, 9, 3, 5]

# printing original list
print ("The original list : " + str(test_list))

# using Slice notation
# to construct alternate element list
res = test_list[1::2]

# printing result
print ("The alternate element list is : " + str(res))
