# Python3 code to demonstrate working of
# Consecutive Similar elements ranges
# Using loop

# initializing list
test_list = [2, 3, 3, 3, 8, 8, 6, 7, 7]

# printing original list
print("The original list is : " + str(test_list))

res = []
idx = 0
while idx < (len(test_list)):
    strt_pos = idx
    val = test_list[idx]

    # getting last pos.
    while (idx < len(test_list) and test_list[idx] == val):
        idx += 1
    end_pos = idx - 1

    # appending in format [ele, strt_pos, end_pos]
    res.append((val, strt_pos, end_pos))

# printing result
print("Elements with range : " + str(res))
