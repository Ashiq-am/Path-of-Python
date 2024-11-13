# Python3 code to demonstrate working of
# Test for nested list
# using any() + isinstance()

# initialize list
test_list = [[5, 6], 6, [7], 8, 10]

# printing original list
print("The original list is : " + str(test_list))

# Test for nested list
# using any() + isinstance()
res = any(isinstance(sub, list) for sub in test_list)

# printing result
print("Does list contain nested list ? : " + str(res))
