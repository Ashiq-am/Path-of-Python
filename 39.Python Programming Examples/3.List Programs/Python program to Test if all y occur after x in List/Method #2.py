# Python3 code to demonstrate working of
# Test if y occurs after x in List
# Using all() + index()

# initializing list
test_list = [4, 5, 6, 2, 4, 5, 2, 9]

# printing original lists
print("The original list is : " + str(test_list))

# initializing x, y
x, y = 6, 2

# getting index of x
xidx = test_list.index(x)

# checking for all indices of y in list
res = all(idx > xidx for idx, ele in enumerate(test_list) if ele == y)

# printing result
print("Do all y occur after x : " + str(res))
