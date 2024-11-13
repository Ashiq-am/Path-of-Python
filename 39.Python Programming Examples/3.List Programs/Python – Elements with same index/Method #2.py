# Python3 code to demonstrate working of
# Elements with same index
# Using list comprehension + enumerate()

# initializing list
test_list = [3, 1, 2, 5, 4, 10, 6, 9]

# printing original list
print("The original list is : " + str(test_list))

# enumerate to get index and element
res = [ele for idx, ele in enumerate(test_list) if idx == ele]

# printing result
print("Filtered elements : " + str(res))
