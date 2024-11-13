# Python3 code to demonstrate working of
# Sort Matrix by row sum
# Using sorted() + sum() + lambda

# initializing list
test_list = [[4, 5], [2, 5, 7], [2, 1], [4, 6, 1]]

# printing original list
print("The original list is : " + str(test_list))

# using lambda fnction preventing fnc. call
res = sorted(test_list, key=lambda row: sum(row))

# printing result
print("Sum sorted Matrix : " + str(res))
