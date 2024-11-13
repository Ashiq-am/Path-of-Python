# Python3 code to demonstrate
# Clearing a tuple
# using list() + tuple() + clear()

# initializing tuple
test_tup = (1, 5, 3, 6, 8)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Clearing a tuple
# using list() + tuple() + clear()
temp = list(test_tup)
temp.clear()
test_tup = tuple(temp)

# print result
print("The tuple after clearing values : " + str(test_tup))
