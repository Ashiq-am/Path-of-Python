# Python3 code to demonstrate
# Elements with Frequency equal K
# using naive method

# initializing list
test_list = [9, 4, 5, 4, 4, 5, 9, 5]

# printing original list
print("Original list : " + str(test_list))

# initializing K
K = 3

# using naive method to
# get most frequent element
res = []
for i in test_list:
    freq = test_list.count(i)
    if freq == K and i not in res:
        res.append(i)

# printing result
print("Elements with count K are : " + str(res))
