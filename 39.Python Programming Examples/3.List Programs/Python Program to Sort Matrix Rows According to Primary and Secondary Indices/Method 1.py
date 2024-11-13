# initializing list
test_list = [[2, 5, 7, 4], [8, 1, 3, 10], [9, 1, 9, 4], [10, 1, 1, 4]]

# printing original list
print("The original list is : " + str(test_list))

# initializing pri, sec
pri, sec = 3, 2

# inplace sorting using sort()
test_list.sort(key=lambda ele: (ele[pri], ele[sec]))

# printing result
print("Matrix after sorting : " + str(test_list))
