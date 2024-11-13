# Python3 code to demonstrate working of
# Filter unique valued tuples
# Using list comprehension

# initializing list
test_list = [(3, 5, 6, 7), (3, 2, 4, 3), (9, 4), (2, 3, 2)]

# printing original list
print("The original list is : " + str(test_list))

# list comprehension used to filter
res = [sub for sub in test_list if len(set(sub)) == len(sub)]

# printing results
print("Filtered tuples : " + str(res))
