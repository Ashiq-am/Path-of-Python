# Python3 code to demonstrate working of
# Consecutive String Comparison
# using zip() + list comprehension

# initialize list
test_list = ['gfg', 'gfg', 'is', 'best', 'best', 'for', 'geeks', 'geeks']

# printing original list
print("The original list : " + str(test_list))

# Consecutive String Comparison
# using zip() + list comprehension
res = [i for (i, j) in zip(test_list, test_list[1:]) if i == j]

# printing result
print("List of Consecutive similar elements : " + str(res))
