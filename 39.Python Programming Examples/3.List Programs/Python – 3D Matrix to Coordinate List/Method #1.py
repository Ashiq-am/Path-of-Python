# Python3 code to demonstrate working of
# 3D Matrix to Coordinate List
# Using loop + zip()

# initializing list
test_list = [[[5, 6, 7], [2, 4, 6]], [[9, 2], [10, 3]], [[13, 6], [19, 7]]]

# printing original list
print("The original list is : " + str(test_list))

res = []
for sub1, sub2 in test_list:

    # zip() used to form pairing
    for ele in zip(sub1, sub2):
        res.append(ele)

# printing result
print("Constructed Pairs : " + str(res))
