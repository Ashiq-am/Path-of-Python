# Python code to filter even values from a list

# Initialisation of list
lis1 = [1,2,3,4,5]

is_even = lambda x: x % 2 == 0

# using filter
lis2 = list(filter(is_even, lis1))

# Printing output
print(lis2)
