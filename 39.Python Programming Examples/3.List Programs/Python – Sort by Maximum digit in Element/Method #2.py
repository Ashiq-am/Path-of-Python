# Python3 code to demonstrate working of
# Sort by Maximum digit in Element
# Using sorted() + lambda + max()

# initializing list
test_list = [234, 92, 15, 8, 721]

# printing original list
print("The original list is : " + str(test_list))

# lambda fnc. used to get maximum Element logic
res = sorted(test_list, key = lambda ele : max(str(ele)))

# printing result
print("Sorted List " + str(res))
