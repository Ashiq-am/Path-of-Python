# Python3 code to demonstrate working of
# String List to Column Character Matrix
# Using zip() + map()

# initializing list
test_list = ["123", "456", "789"]

# printing original list
print("The original list is : " + str(test_list))

# String List to Column Character Matrix
# Using zip() + map()
res = list(map(list, zip(*test_list)))

# printing result
print("The Character Matrix : " + str(res))
