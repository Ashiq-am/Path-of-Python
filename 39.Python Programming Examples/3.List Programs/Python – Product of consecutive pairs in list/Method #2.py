# Python code to demonstrate working of
# List consecutive pair Product
# Using zip() + list comprehension

# initializing list
test_list = [5, 8, 3, 5, 9, 10]

# printing list
print("The original list : " + str(test_list))

# List consecutive pair Product
# zip() + list comprehension
res = [i * j for i, j in zip(test_list, test_list[1:])[::2]]

# Printing result
print("Pair product of list : " + str(res))
