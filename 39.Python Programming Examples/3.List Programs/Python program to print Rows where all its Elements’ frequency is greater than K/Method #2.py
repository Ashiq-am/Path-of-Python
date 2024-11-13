# Python3 code to demonstrate working of
# Rows with all Elements frequency greater than K
# Using filter() + lambda + all() + count()

def freq_greater_K(row, K):
    # checking for all elements occurrence greater than K
    return all(row.count(ele) > K for ele in row)


# initializing list
test_list = [[1, 1, 2, 3, 2, 3], [4, 4, 5, 6, 6], [1, 1, 1, 1], [4, 5, 6, 8]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 1

# checking for each row
res = list(filter(lambda ele: freq_greater_K(ele, K), test_list))

# printing result
print("Filtered rows : " + str(res))
