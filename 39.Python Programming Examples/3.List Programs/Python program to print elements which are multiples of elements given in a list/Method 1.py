# initializing List
test_list = [4, 24, 8, 10, 12, 23]

# printing original list
print("The original list is : " + str(test_list))

# initializing divisor list
div_list = [6, 4]

# using all() to test for all elements
res = [ele for ele in test_list if all(ele % j == 0 for j in div_list)]

# printing result
print("All elements multiple of divisor list : " + str(res))
