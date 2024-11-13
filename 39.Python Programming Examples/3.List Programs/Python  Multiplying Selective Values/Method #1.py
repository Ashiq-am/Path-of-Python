# Python3 code to demonstrate
# Multiplying Selective Values
# using list comprehension + loop

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

# using list comprehension + loop to
# Multiplying Selective Values
res_list = [test_list[i] for i in index_list]
res = prod(res_list)

# printing result
print("Resultant product : " + str(res))
