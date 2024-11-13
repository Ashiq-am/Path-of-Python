# Python3 code to demonstrate working of
# Extract sorted strings
# Using filter() + lambda + sorted() + join()

# initializing list
test_list = ["hint", "geeks", "fins", "Gfg"]

# printing original list
print("The original list is : " + str(test_list))

# sorted(), converts to sorted version and compares with
# original string
res = list(filter(lambda sub : ''.join(sorted(sub)) == sub, test_list))

# printing result
print("Sorted Strings : " + str(res))
