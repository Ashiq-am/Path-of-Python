# Python3 code to demonstrate
# removing empty strings
# using join() + split()

# initializing list
test_list = ["", "GeeksforGeeks", "", "is", "best", ""]

# Printing original list
print("Original list is : " + str(test_list))

# using join() + split() to
# perform removal
test_list = ' '.join(test_list).split()

# Printing modified list
print("Modified list is : " + str(test_list))
