data = [('a', 1), ('b', 2), ('c', 3), ('a', 4)]
dynamic_dict = {}
# looping through data to populate the dictionary

for key, value in data:
    if key in dynamic_dict:
        # aggregates values if key already exists
        dynamic_dict[key] += value
    else:
        # creates new key if not existing
        dynamic_dict[key] = value

print(dynamic_dict)
