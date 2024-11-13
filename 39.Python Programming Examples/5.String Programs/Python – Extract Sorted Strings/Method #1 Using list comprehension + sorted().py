# Python3 code to demonstrate working of
# Extract sorted strings
# Using list comprehension + sorted()

# initializing list
test_list = ["hint", "geeks", "fins", "Gfg"]

# printing original list
print("The original list is : " + str(test_list))

# sorted(), converts to sorted version and compares with
# original string
res = [sub for sub in test_list if ''.join(sorted(sub)) == sub]

# printing result
print("Sorted Strings : " + str(res))
