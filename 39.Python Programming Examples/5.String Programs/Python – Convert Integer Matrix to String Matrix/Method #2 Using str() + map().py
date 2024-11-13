# Python3 code to demonstrate working of
# Convert Integer Matrix to String Matrix
# Using str() + map()

# initializing list
test_list = [[4, 5, 7], [10, 8, 3], [19, 4, 6], [9, 3, 6]]

# printing original list
print("The original list : " + str(test_list))

# using map() to extend all elements as string
res = [list(map(str, sub)) for sub in test_list]

# printing result
print("The data type converted Matrix : " + str(res))
