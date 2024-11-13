# Python3 code to demonstrate working of
# Preceding Tuple elements in list
# using zip() + list comprehension

# initialize list
test_list = [1, 4, 'gfg', 7, 8, 'gfg', 9, 'gfg']

# printing original list
print("The original list is : " + str(test_list))

# initialize ele
ele = 'gfg'

# Preceding Tuple elements in list
# using zip() + list comprehension
res = [(x, y) for x, y in zip(test_list, test_list[1 : ]) if y == ele]

# printing result
print("Tuple list with desired Preceding elements " + str(res))
