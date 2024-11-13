# Python code to demonstrate working of
# Consecutive Pair Maximum
# Using zip() + list comprehension + max()

# initializing list
test_list = [5, 8, 3, 5, 9, 10]

# printing list
print("The original list : " + str(test_list))

# Consecutive Pair Maximum
# zip() + list comprehension + max()
res = [max(i, j) for i, j in zip(test_list, test_list[1:])[::2]]

# Printing result
print("Pair maximum of list : " + str(res))
