# Python3 code to demonstrate working of
# Sort Strings by Maximum Character
# Using sorted() + lambda + max()

# initializing list
test_list = ["geeksforgeeks", "is", "best", "for", "cs"]

# printing original lists
print("The original list is : " + str(test_list))

# performing sorting using sorted()
# lambda function provides logic
res = sorted(test_list, key=lambda sub: ord(max(sub)))

# printing result
print("Sorted List : " + str(res))
