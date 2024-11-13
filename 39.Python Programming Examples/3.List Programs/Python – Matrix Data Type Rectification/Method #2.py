# Python3 code to demonstrate
# Matrix Data Type Rectification
# using map() + isdigit()

# Initializing list
test_list = [['5', 'GFG'], ['1', '3'], ['is', '11'], ['1', 'best']]

# printing original list
print("The original list is : " + str(test_list))

# Matrix Data Type Rectification
# using map() + isdigit()
res = [list(map(lambda ele: int(ele) if ele.isdigit() else ele, sub)) for sub in test_list]

# printing result
print ("The rectified Matrix is : " + str(res))
