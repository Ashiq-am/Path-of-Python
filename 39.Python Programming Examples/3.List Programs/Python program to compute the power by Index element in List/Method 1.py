# Python3 code to demonstrate working of
# Index Power List
# Using ** operator + loop + enumerate()

# initializing list
test_list = [6, 9, 1, 8, 4, 7]

# printing original list
print("The original list is : " + str(test_list))

# ** does task of getting power
res = []
for idx, ele in enumerate(test_list):
    res.append(ele ** idx)

# printing result
print("Powered elements : " + str(res))
