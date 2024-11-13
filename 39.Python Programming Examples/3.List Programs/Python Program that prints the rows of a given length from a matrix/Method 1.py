# initializing list
test_list = [[3, 4, 5, 6], [1, 4, 6], [2], [2, 3, 4, 5, 6], [7, 3, 1]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# list comprehension is used for extracting K len rows
res = [sub for sub in test_list if len(sub) == K]

# printing result
print("The filtered rows : " + str(res))
