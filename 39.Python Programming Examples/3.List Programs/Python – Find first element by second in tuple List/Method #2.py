# Python3 code to demonstrate working of
# Find first element by second in tuple List
# Using next() + generator expression

# initializing list
test_list = [(4, 5), (5, 6), (1, 3), (6, 9)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 6

# Find first element by second in tuple List
# Using next() + generator expression
res = next((x for x, y in test_list if y == K), None)

# printing result
print("The key from value : " + str(res))
