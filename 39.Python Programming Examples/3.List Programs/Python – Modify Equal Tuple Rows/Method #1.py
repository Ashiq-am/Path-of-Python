# Python3 code to demonstrate working of
# Modify Equal Tuple Rows
# Using loop + enumerate()

# initializing list
test_list = [[(12, 5), (13, 6)], [(12, 2), (13, 2)]]

# printing original list
print("The original list is : " + str(test_list))

# initializing check row
test_row = [(12, 2), (13, 2)]

# Modify Equal Tuple Rows
# Using loop + enumerate()
# multiple y coordinate by 4
for idx, val in enumerate(test_list):
    if val == test_row:
        temp = []
        for sub in val:
            ele = (sub[0], sub[1] * 4)
            temp.append(ele)
        test_list[idx] = temp

# printing result
print("List after modification : " + str(test_list))
