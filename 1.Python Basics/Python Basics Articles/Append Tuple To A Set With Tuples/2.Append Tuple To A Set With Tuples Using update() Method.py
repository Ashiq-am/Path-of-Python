# Append Tuple To A Set With Tuples
my_set = {(1, 2), (3, 4), (5, 6)}
new_tuples = {(7, 8), (9, 10), (11, 12)}

my_set.update(new_tuples)
print("Updated Set:", my_set)
