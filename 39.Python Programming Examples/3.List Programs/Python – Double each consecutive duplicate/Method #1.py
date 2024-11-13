# Python3 code to demonstrate
# Double each consecutive duplicate
# using loop

# Initializing list
test_list = [1, 2, 4, 2, 4, 1, 2]

# printing original list
print("The original list is : " + str(test_list))

# Double each consecutive duplicate
# using loop
temp = {}
res = []
for ele in test_list:
    temp[ele] = temp1 = temp.get(ele, 0) + ele
    res.append(temp1)

# printing result
print("The list after manipulation is : " + str(res))
