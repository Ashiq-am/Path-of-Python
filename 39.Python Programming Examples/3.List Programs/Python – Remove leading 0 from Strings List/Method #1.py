# Python3 code to demonstrate
# Remove leading 0 from Strings List
# using lstrip() + list comprehension

# Initializing list
test_list = ['012', '03', '044', '09']

# printing original list
print("The original list is : " + str(test_list))

# Remove leading 0 from Strings List
# using lstrip() + list comprehension
res = [ele.lstrip('0') for ele in test_list]

# printing result
print ("The string list after leading 0 removal : " + str(res))
