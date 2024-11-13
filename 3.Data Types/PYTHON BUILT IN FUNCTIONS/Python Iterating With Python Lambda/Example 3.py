# Iterating With Python Lambdas

# list of numbers
l1 = [4, 2, 13, 21, 5]

# list of square of odd numbers
# lambda function is used to iterate over list l1
# filter is used to find odd numbers
l2 = list(map(lambda v: v ** 2, filter(lambda u: u % 2, l1)))

# print list
print(l2)
