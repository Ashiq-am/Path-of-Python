# Python3 code to demonstrate working of
# Empty String to None Conversion
# Using str()

# initializing list of strings
test_list = ["Geeks", '', "CS", '', '']

# printing original list
print("The original list is : " + str(test_list))

# using str()
# Empty String to None Conversion
res = [str(i or None) for i in test_list]

# printing result
print("The list after conversion of Empty Strings : " + str(res))
