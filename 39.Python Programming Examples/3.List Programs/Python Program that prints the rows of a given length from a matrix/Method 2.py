# initializing list
test_list = [[3, 4, 5, 6], [1, 4, 6], [2], [2, 3, 4, 5, 6], [7, 3, 1]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# filter() + lambda to filter out rows of len K
res = list(filter(lambda sub: len(sub) == K, test_list))

# printing result
print("The filtered rows : " + str(res))
