# Python3 code to demonstrate working of
# Empty String to None Conversion
# Using lambda

# initializing list of strings
test_list = ["Geeks", '', "CS", '', '']

# printing original list
print("The original list is : " + str(test_list))

# using lambda
# Empty String to None Conversion
conv = lambda i : i or None
res = [conv(i) for i in test_list]

# printing result
print("The list after conversion of Empty Strings : " + str(res))
