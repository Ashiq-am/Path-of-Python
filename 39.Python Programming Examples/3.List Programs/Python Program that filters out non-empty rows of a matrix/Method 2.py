# initializing list
test_list = [[4, 5, 6, 7], [], [], [9, 8, 1], []]

# printing original lists
print("The original list is : " + str(test_list))

# checking for row lengths using len()
# filtering using filter() + lambda
res = list(filter(lambda row: len(row) > 0, test_list))

# printing result
print("Filtered Matrix " + str(res))
