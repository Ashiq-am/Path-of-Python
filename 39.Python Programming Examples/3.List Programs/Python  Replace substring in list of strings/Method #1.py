# Python3 code to demonstrate
# Replace substring in list of strings
# using list comprehension + replace()

# initializing list
test_list = ['4', 'kg', 'butter', 'for', '40', 'bucks']

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + replace()
# Replace substring in list of strings
res = [sub.replace('4', '1') for sub in test_list]

# print result
print("The list after substring replacement : " + str(res))
