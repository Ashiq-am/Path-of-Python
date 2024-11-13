# Python 3 code to demonstrate
# removing empty strings
# using list comprehension

# initializing list
test_list = ["", "GeeksforGeeks", "", "is", "best", ""]

# Printing original list
print("Original list is : " + str(test_list))

# using list comprehension to
# perform removal
test_list = [i for i in test_list if i]

# Printing modified list
print("Modified list is : " + str(test_list))
