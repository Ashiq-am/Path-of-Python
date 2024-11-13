# Python3 code to demonstrate working of
# Tuple Matrix Columns Summation
# Using list comprehension + zip() + sum()

# initializing lists
test_list = [[(4, 5), (3, 2)], [(2, 2), (4, 6)], [(3, 2), (4, 5)]]

# printing original list
print("The original list is : " + str(test_list))

# Tuple Matrix Columns Summation
# Using list comprehension + zip() + sum()
res = [tuple(sum(ele) for ele in zip(*i)) for i in zip(*test_list)]

# printing result
print("Tuple matrix columns summation : " + str(res))
