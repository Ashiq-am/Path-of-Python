# Python3 code to demonstrate working of
# Construct Cartesian Product Tuple list
# using list comprehension

# initialize list and tuple
test_list = [1, 4, 6, 7]
test_tup = (1, 3)

# printing original list and tuple
print("The original list : " + str(test_list))
print("The original tuple : " + str(test_tup))

# Construct Cartesian Product Tuple list
# using list comprehension
res = [(a, b) for a in test_tup for b in test_list]

# printing result
print("The Cartesian Product is : " + str(res))
