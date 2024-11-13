# initializing list
test_list = [[3], [1, 7], [10, 2, 4], [8, 6, 5, 1, 4]]

# printing original list
print("The original list is : " + str(test_list))

# checking for truth for all rows in matrix
res = all(len(test_list[idx + 1]) > len(test_list[idx]) for idx in range(len(test_list) - 1))

# printing result
print("Are rows of increasing lengths ? : " + str(res))
