# Python code to demonstrate working of
# Pair summation of list
# zip() + list comprehension

# initializing list
test_list = [4, 5, 8, 9, 10, 17]

# printing list
print("The original list : " + str(test_list))

# Pair summation of list
# zip() + list comprehension
res = [i + j for i, j in zip(test_list, test_list[1:])[::2]]

# Printing result
print("Pair summation of list : " + str(res))
