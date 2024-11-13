# Python3 code to demonstrate
# appending single value
# using list comprehension

# initializing list of lists
test_list = [[1, 3], [3, 4], [6, 5], [4, 5]]

# printing original list
print("The original list : " + str(test_list))

# declaring element to be inserted
K = "GFG"

# using list comprehension
# appending single value
res = [[i, j, K ] for i, j in test_list]

# printing result
print("The list after adding element : " + str(res))
