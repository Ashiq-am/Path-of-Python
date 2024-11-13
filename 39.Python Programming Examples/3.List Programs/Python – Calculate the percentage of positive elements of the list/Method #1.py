# Python3 code to demonstrate working of
# Positive values percentage
# Using len() + list comprehension

# initializing list
test_list = [4, 6, -2, 3, -8, 0, -1, 8, 9, 1]

# printing original list
print("The original list is : " + str(test_list))

# getting filtered list using comprehension and
# division to get fraction
res = (len([ele for ele in test_list if ele > 0]) / len(test_list)) * 100

# printing result
print("Positive elements percentage : " + str(res))
