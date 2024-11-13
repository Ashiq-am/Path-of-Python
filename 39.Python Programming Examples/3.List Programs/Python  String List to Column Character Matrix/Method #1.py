# Python3 code to demonstrate working of
# String List to Column Character Matrix
# Using list comprehension

# initializing list
test_list = ["123", "456", "789"]

# printing original list
print("The original list is : " + str(test_list))

# String List to Column Character Matrix
# Using list comprehension
res = [[sub[idx] for sub in test_list] for idx in range(len(test_list[0]))]

# printing result
print("The Character Matrix : " + str(res))
