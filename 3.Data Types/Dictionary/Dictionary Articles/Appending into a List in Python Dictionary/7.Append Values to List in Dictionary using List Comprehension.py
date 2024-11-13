Details = {"Age": [18, 20, 25, 29, 30]}
extra_values = [35, 40]

# Using List Comprehension to append values to the existing list
Details["Age"] = [x for x in Details["Age"]] + extra_values

print(Details)
