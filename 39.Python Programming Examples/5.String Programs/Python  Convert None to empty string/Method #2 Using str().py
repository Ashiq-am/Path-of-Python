# Python3 code to demonstrate working of
# Converting None to empty string
# Using str()

# initializing list of strings
test_list = ["Geeks", None, "CS", None, None]

# printing original list
print("The original list is : " + str(test_list))

# using str()
# Converting None to empty string
res = [str(i or '') for i in test_list]

# printing result
print("The list after conversion of None values : " + str(res))
