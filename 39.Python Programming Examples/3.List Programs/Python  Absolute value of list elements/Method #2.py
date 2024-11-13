# Python3 code to demonstrate working of
# Absolute value of list elements
# using map() + abs()

# initialize list
test_list = [5, -6, 7, -8, -10]

# printing original list
print("The original list is : " + str(test_list))

# Absolute value of list elements
# using map() + abs()
res = list(map(abs, test_list))

# printing result
print("Absolute value list : " + str(res))
