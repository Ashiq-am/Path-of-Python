# row sum util.
def row_sum(row):
	return sum(row)


# initializing list
test_list = [[3, 4, 5, 6], [1, 4, 6], [199], [2, 3, 4, 5, 6], [7, 3, 1]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# sort() used to sort
# K rows extracted using slicing
test_list.sort(key=row_sum, reverse=True)
res = test_list[:K]

# printing result
print("The filtered rows : " + str(res))
