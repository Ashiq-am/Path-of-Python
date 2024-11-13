# Python3 code to demonstrate working of
# Frequency grouping of list elements
# using loop

# initialize list
test_list = [1, 3, 3, 1, 4, 4]

# printing original list
print("The original list : " + str(test_list))

# Frequency grouping of list elements
# using loop
res = []
temp = dict()
for ele in test_list:
    if ele in temp:
        temp[ele] = temp[ele] + 1
    else:
        temp[ele] = 1
for key in temp:
    res.append((key, temp[key]))

# printing result
print("Frequency of list elements : " + str(res))
