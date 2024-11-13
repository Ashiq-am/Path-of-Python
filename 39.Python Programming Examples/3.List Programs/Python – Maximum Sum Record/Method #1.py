# Python3 code to demonstrate working of
# Maximum Sum Record
# Using list comprehension + max()

# initialize list
test_list = [(3, 5), (1, 7), (10, 3), (1, 2)]

# printing original list
print("The original list : " + str(test_list))

# Maximum Sum Record
# Using list comprehension + max()
temp = [b + a for a, b in test_list]
res = max(temp)

# printing result
print("Maximum sum among pairs : " + str(res))
