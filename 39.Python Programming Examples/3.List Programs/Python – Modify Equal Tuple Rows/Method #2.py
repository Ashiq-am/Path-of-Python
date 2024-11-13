# Python3 code to demonstrate working of
# Modify Equal Tuple Rows
# Using list comprehension

# initializing list
test_list = [[(12, 5), (13, 6)], [(12, 2), (13, 2)]]

# printing original list
print("The original list is : " + str(test_list))

# initializing check row
test_row = [(12, 2), (13, 2)]

# Modify Equal Tuple Rows
# Using list comprehension
# multiple y coordinate by 4
res = [[(sub[0], sub[1] * 4) for sub in ele] if ele == test_row else ele for ele in test_list]

# printing result
print("List after modification : " + str(res))
