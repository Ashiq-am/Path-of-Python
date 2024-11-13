# Python3 code to demonstrate working of
# Successive element pairing
# using zip() + list comprehension

# initialize list
test_list = [1, 4, 'gfg', 7, 8, 'gfg', 9, 'gfg', 10]

# printing original list
print("The original list is : " + str(test_list))

# initialize ele
ele = 'gfg'

# Successive element pairing
# using zip() + list comprehension
res = [(x, y) for x, y in zip(test_list, test_list[1 : ]) if x == ele]

# printing result
print("Tuple list with desired Successive elements " + str(res))
