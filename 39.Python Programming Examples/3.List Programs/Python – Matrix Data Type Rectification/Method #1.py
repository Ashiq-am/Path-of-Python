# Python3 code to demonstrate
# Matrix Data Type Rectification
# using isdigit() + list comprehension

# Initializing list
test_list = [['5', 'GFG'], ['1', '3'], ['is', '11'], ['1', 'best']]

# printing original list
print("The original list is : " + str(test_list))

# Matrix Data Type Rectification
# using isdigit() + list comprehension
res = [[int(ele) if ele.isdigit() else ele for ele in sub] for sub in test_list]

# printing result
print ("The rectified Matrix is : " + str(res))
