# initializing list
test_list = [[3, 4, 5, 6], [1, 4, 6], [199], [2, 3, 4, 5, 6], [7, 3, 1]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# sorted gets reverse sorted matrix by sum
# K rows extracted using slicing
res = sorted(test_list, key=lambda row: sum(row), reverse=True)[:K]

# printing result
print("The filtered rows : " + str(res))
