# Python3 code to demonstrate working of
# Check if any element in list satisfies a condition
# Using list comprehension

# initializing list
test_list = [4, 5, 8, 9, 10, 17]

# printing list
print("The original list : " + str(test_list))

# Check if any element in list satisfies a condition
# Using list comprehension
res = True in (ele > 10 for ele in test_list)

# Printing result
print("Does any element satisfy specified condition ? : " + str(res))
