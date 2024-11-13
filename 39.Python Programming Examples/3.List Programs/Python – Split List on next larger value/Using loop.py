# Python3 code to demonstrate working of
# Split List on next larger value
# Using loop

# initializing list
test_list = [4, 2, 3, 7, 5, 9, 3, 4, 11, 2]

# printing original list
print("The original list is : " + str(test_list))

# starting value as ref.
curr = test_list[0]
temp = []
res = []
for ele in test_list:

    # if curr value greater than split
    if ele > curr:
        res.append(temp)
        curr = ele
        temp = []
    temp.append(ele)
res.append(temp)

# printing results
print("Split List : " + str(res))
