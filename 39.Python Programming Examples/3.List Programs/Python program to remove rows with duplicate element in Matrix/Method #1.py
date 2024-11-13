# initializing list
test_list = [[4, 3, 2], [7, 6, 7], [2, 4, 5], [8, 9, 9]]

# printing original list
print("The original list is : " + str(test_list))

# set() removing all elements
# list comprehension used to filter
res = [sub for sub in test_list if len(set(sub)) == len(sub)]

# printing result
print("Rows after removal : " + str(res))
