# Python3 code to demonstrate
# Extracting numbers from list of strings
# using list comprehension + split()

# initializing list
test_list = ['Rs. 24', 'Rs. 18', 'Rs. 8', 'Rs. 21']

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + split()
# Extracting numbers from list of strings
res = [int(sub.split('.')[1]) for sub in test_list]

# print result
print("The list after Extracting numbers : " + str(res))
