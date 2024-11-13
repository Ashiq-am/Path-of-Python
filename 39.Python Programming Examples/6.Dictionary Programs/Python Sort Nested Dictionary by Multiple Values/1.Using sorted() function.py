nested_dict = {'A': {'score': 85, 'age': 25},
               'B': {'score': 92, 'age': 30},
               'C': {'score': 78, 'age': 27}}

sorted_nested_dict = dict(sorted(nested_dict.items(), key=lambda x: (x[1]['score'])))

print(sorted_nested_dict)
