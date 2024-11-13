# Python3 code to demonstrate working of
# Absolute Tuple Summation
# Using list comprehension + sum() + map()

# initializing list
test_list = [(7, -8), (-5, -6), (-7, 2), (6, 8)]

# printing original list
print("The original list is : " + str(test_list))

# Absolute Tuple Summation
# Using list comprehension + sum() + map()
res = [sum(map(abs, ele)) for ele in test_list]

# printing result
print("The absolute sum list: " + str(res))
