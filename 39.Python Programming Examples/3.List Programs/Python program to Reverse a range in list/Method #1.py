# Python3 code to demonstrate working of
# Reversing a range
# Using reverse() + loop

# initializing list
test_list = [6, 3, 1, 8, 9, 2, 10, 12, 7, 4, 11]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
strt, end = 3, 9

# reversing list and assigning the range
temp = test_list[strt:end]
temp.reverse()
for idx in range(strt, end):
    test_list[idx] = temp[idx - strt]

# printing result
print("Range reversed range list : " + str(test_list))
