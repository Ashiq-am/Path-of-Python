# Python 3 code to demonstrate
# removing empty strings
# using filter()

# initializing list
test_list = ["", "GeeksforGeeks", "", "is", "best", ""]

# Printing original list
print("Original list is : " + str(test_list))

# using filter() to
# perform removal
test_list = list(filter(None, test_list))

# Printing modified list
print("Modified list is : " + str(test_list))
