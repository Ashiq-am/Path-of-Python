# using set comprehension
set_of_sets = {frozenset(range(i, i+3)) for i in range(1, 10, 3)}

#printing result
print(type(set_of_sets))
print(set_of_sets)
