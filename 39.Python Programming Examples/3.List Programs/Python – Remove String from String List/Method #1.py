# Python 3 code to demonstrate
# Remove K String from String List
# using remove()

# initializing list
test_list = ["bad", "GeeksforGeeks", "bad", "is", "best", "bad"]

# Printing original list
print("Original list is : " + str(test_list))

# initializing K
K = "bad"

# using remove() to
# Remove K String from String List
while (K in test_list):
    test_list.remove(K)

# Printing modified list
print("Modified list is : " + str(test_list))
