# Python3 code to demonstrate working of
# Column Product in List of Lists
# using loop + zip()

# getting Product
def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res


# initialize list
test_list = [[5, 6, 7],
             [9, 10, 2],
             [10, 3, 4]]

# printing original list
print("The original list is : " + str(test_list))

# initialize K
K = 2

# Column Product in List of Lists
# using loop + zip()
res = [prod(idx) for idx in zip(*test_list)][K]

# printing result
print("Product of Kth column is : " + str(res))
