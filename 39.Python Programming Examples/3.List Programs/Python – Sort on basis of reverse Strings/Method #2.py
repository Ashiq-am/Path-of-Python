# Python3 code to demonstrate working of
# Sort on basis of reverse Strings
# Using list slicing + sort()

# initializing list
test_list = ["gfg", "is", "best", "for", "geeks"]

# printing original list
print("The original list : " + str(test_list))

# [::-1] to reverse each string
# sort() to sort
test_list.sort(key = lambda sub: sub[::-1])

# printing result
print("List after sorting on reversed strings : " + str(test_list))
