# Python code to demonstrate
# sum of list of list using
# zip and list comprehension

# Declaring initial list of list
List = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

# Printing list of list
print("Initial List - ", str(List))

# Using list comprehension
res = [sum(i) for i in zip(*List)]

# printing result
print("final list - ", str(res))
