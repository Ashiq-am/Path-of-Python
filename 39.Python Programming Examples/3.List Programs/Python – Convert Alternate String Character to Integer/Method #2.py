# Python 3 code to demonstrate
# Alternate String to Integer Conversion
# using list comprehension

# initializing list
test_list = ['1', '4', '3', '6', '7']

# Printing original list
print("Original list is : " + str(test_list))

# using list comprehension to
# perform conversion
test_list = [int(ele) if idx % 2 else ele for idx, ele in enumerate(test_list)]

# Printing modified list
print("Modified list is : " + str(test_list))
