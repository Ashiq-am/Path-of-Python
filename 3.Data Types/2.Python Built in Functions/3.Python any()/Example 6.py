# Python3 code to demonstrate working of any()
# To Check if any element in list satisfies a condition

# initializing list
test_list = [4, 5, 8, 9, 10, 17]

# printing list
print("The original list : ", test_list)

# Check if any element in list satisfies a condition
# Using any()
res = any(ele > 10 for ele in test_list)

# Printing result
print("Does any element satisfy specified condition ? : ", res)
