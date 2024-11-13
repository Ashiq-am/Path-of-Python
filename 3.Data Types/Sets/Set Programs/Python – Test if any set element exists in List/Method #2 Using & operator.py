# Python3 code to demonstrate working of
# Test if any set element exists in List
# Using & operator

# initializing set
test_set = {6, 4, 2, 7, 9, 1}

# printing original set
print("The original set is : " + str(test_set))

# initializing list
test_list = [6, 8, 10]

# & operator checks for any common element
res = bool(test_set & set(test_list))

# printing result
print("Any set element is in list ? : " + str(res))
