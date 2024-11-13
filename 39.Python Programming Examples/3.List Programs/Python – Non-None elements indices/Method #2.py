# Python3 code to demonstrate
# Non-None elements indices
# using list comprehension + enumerate

# initializing list
test_list = [1, None, 4, None, None, 5]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + enumerate
# Non-None elements indices
res = [i for i, val in enumerate(test_list) if val != None]

# print result
print("The Non None indices list is : " + str(res))
