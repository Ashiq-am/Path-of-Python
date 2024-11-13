# Sample List of Tuples
list_of_tuples = [(1, 'apple'), (2, 'banana'), (3, 'cherry'), (4, 'date')]

# Conditional Slicing with List Comprehension
sliced_result = [tup for tup in list_of_tuples if tup[0] % 2 == 0]
print(sliced_result)
