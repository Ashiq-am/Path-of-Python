# Python3 code to demonstrate working of
# Column Minimum in Tuple list
# using list comprehension + min() + zip()

# initialize list
test_list = [(1, 2, 3), (6, 7, 6), (1, 6, 8)]

# printing original list
print("The original list : " + str(test_list))

# Column Minimum in Tuple list
# using list comprehension + min() + zip()
res = [min(ele) for ele in zip(*test_list)]

# printing result
print("The Cummulative column minimum is : " + str(res))
