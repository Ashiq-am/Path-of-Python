# Iterative Approach
array_of_sets = []
for i in range(0, 10, 3):
    new_set = set(range(i, i + 3))
    array_of_sets.append(new_set)

print(array_of_sets)
