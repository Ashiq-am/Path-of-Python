# Python3 code to demonstrate working of
# Move Word to Rear end
# Using string slicing and find()

# initializing string
test_str = 'Geeksforgeeks is best for geeks '

# printing original string
print("The original string is : " + str(test_str))

# initializing Substring
sub_str = 'best'

# Move Word to Rear end
# Using string slicing and find()
res = test_str[:test_str.find(sub_str)] + test_str[test_str.find(sub_str) + len(sub_str):] + sub_str

# printing result
print("The string after word removal : " + str(res))
