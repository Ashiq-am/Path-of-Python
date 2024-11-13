# Python3 code to demonstrate working of
# Test if any set element exists in List
# Using any()

# initializing set
test_set = {6, 4, 2, 7, 9, 1}

# printing original set
print("The original set is : " + str(test_set))

# initializing list
test_list = [6, 8, 10]

# any() checking for any set element in check list
res = any(ele in test_set for ele in test_list)

# printing result
print("Any set element is in list ? : " + str(res))
