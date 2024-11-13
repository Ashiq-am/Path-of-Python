# Append Tuple To A Set With Tuples
my_set = {(1, 2), (3, 4), (5, 6)}
new_tuple = (7, 8)

updated_set = my_set.union({new_tuple})
print("Updated Set:", updated_set)
