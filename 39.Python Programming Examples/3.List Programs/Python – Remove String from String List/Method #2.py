# Python 3 code to demonstrate
# Remove K String from String List
# using list comprehension

# initializing list
test_list = ["bad", "GeeksforGeeks", "bad", "is", "best", "bad"]

# Printing original list
print("Original list is : " + str(test_list))

# initializing K
K = "bad"

# using list comprehension to
# Remove K String from String List
test_list = [i for i in test_list if i != K]

# Printing modified list
print("Modified list is : " + str(test_list))
