# Python3 code to demonstrate working of
# Smallest K elements indices
# using sorted() + lambda + list slicing

# initialize list
test_list = [5, 6, 10, 4, 7, 1, 19]

# printing original list
print("The original list is : " + str(test_list))

# initialize K
K = 3

# Smallest K elements indices
# using sorted() + lambda + list slicing
res = sorted(range(len(test_list)), key = lambda sub: test_list[sub])[:K]

# printing result
print("Indices list of min K elements is : " + str(res))
