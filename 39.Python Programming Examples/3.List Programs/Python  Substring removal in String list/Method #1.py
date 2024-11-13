# Python3 code to demonstrate
# Substring removal in String list
# using list comprehension + replace()

# initializing list
test_list = ['4', 'kg', 'butter', 'for', '40', 'bucks']

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + replace()
# Substring removal in String list
res = [sub.replace('4', '') for sub in test_list]

# print result
print("The list after substring removal : " + str(res))
