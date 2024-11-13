# create a list of 10 elements
data = [10, 2, 3, 4, 56, 32, 56, 32, 21, 59]

# filter data using comprehension
# to get even numbers
print([x for x in data if x % 2 == 0])

# filter data using comprehension
# to get odd numbers
print([x for x in data if x % 2 != 0])
