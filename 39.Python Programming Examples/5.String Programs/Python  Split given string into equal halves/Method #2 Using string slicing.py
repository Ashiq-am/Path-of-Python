# Python3 code to demonstrate working of
# Splitting string into equal halves
# Using string slicing

# initializing string
test_str = "GeeksforGeeks"

# printing original string
print("The original string is : " + test_str)

# Using string slicing
# Splitting string into equal halves
res_first, res_second = test_str[:len(test_str)//2], test_str[len(test_str)//2:]

# printing result
print("The first part of string : " + res_first)
print("The second part of string : " + res_second)
