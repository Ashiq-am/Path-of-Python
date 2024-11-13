# Python3 code to demonstrate working of
# Sucessive row difference in Matrix
# Using set.difference + loop

# initializing list
test_list = [[5, 6, 3, 1], [7, 5, 3, 1],
             [3, 2], [7, 3, 3, 2],
             [2, 3], [9, 8, 1]]

# printing original list
print("The original list is : " + str(test_list))

res = []
prev = set(test_list[0])
for ele in test_list:
    # appending difference set diff with previous
    # element
    res.append(list(set(ele).difference(prev)))

    # updating prev. for comparison
    prev = set(ele)

# printing result
print("Sucessive Row difference : " + str(res))
