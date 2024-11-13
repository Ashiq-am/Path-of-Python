# Python3 code to demonstrate
# Product of Index values
# using map() + __getitem__ + loop

# getting Product
def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res


# initializing lists
test_list = [9, 4, 5, 8, 10, 14]
index_list = [1, 3, 4]

# printing original lists
print("Original list : " + str(test_list))
print("Original index list : " + str(index_list))

# using map() + __getitem__ + loop to
# Product of Index values
res_list = prod(list(map(test_list.__getitem__, index_list)))

# printing result
print("Resultant list : " + str(res_list))
