# Python3 code to demonstrate working of
# Variance of List
# using loop + formula

# initialize list
test_list = [6, 7, 3, 9, 10, 15]

# printing original list
print("The original list is : " + str(test_list))

# Variance of List
# using loop + formula
mean = sum(test_list) / len(test_list)
res = sum((i - mean) ** 2 for i in test_list) / len(test_list)

# printing result
print("The variance of list is : " + str(res))
