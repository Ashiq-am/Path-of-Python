# initializing list
test_list = [[4, 3, 2], [7, 6, 7], [2, 4, 5], [8, 9, 9]]

# printing original list
print("The original list is : " + str(test_list))

# set() removing all elements
# filter() used to filter
res = list(filter(lambda ele: len(set(ele)) == len(ele), test_list))

# printing result
print("Rows after removal : " + str(res))
