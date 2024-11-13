# Python3 code to demonstrate working of
# Test if any list element returns true for condition
# Using any() + list comprehension

# initializing list
test_list = [6, 4, 8, 9, 10]

# printing list
print("The original list : " + str(test_list))

# Test if any list element returns true for condition
# Using any() + list comprehension
res = any(x % 5 for x in test_list)

# Printing result
print("Does list contain any element divisible by 5? : " + str(res))
