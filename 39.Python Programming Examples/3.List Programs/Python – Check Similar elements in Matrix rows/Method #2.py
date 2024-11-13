# Python3 code to demonstrate working of
# Similar all elements as List in Matrix rows
# Using all() + generator expression

# initializing Matrix
test_list = [[1, 1, 1], [4, 4],
             [3, 3, 3], [5, 5, 5, 5]]

# printing original list
print("The original list is : " + str(test_list))

# initializing tar_list
tar_list = [1, 4, 3, 5]

# nested all() used to check each element and rows
res = all(all(ele == tar_list[idx] for ele in test_list[idx])
          for idx in range(len(test_list)))

# printing result
print("Are row index element\
	similar to list index element ? : " + str(res))
