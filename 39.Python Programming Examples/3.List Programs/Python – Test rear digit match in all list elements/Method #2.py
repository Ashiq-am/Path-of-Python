# Python3 code to demonstrate
# Test rear digit match
# using all() + list comprehension

# initializing list
test_list = [45, 545, 2345, 8765]

# printing original list
print("The original list : " + str(test_list))

# using all() + list comprehension
# Test rear digit match
res = all(str(i)[-1] == str(test_list[-1])[-1] for i in test_list)

# print result
print("Does each element end with same digit ? " + str(res))
