# Python code to demonstrate working of
# Consecutive Pair Minimums
# zip() + list comprehension + min()

# initializing list
test_list = [4, 5, 8, 9, 10, 17]

# printing list
print("The original list : " + str(test_list))

# Consecutive Pair Minimums
# zip() + list comprehension + min()
res = [min(i, j) for i, j in zip(test_list, test_list[1:])[::2]]

# Printing result
print("Pair minimum of list : " + str(res))
