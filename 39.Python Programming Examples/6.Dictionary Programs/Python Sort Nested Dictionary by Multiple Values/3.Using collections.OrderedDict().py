from collections import OrderedDict

nested_dict = {'A': {'score': 85, 'age': 25},
               'B': {'score': 92, 'age': 30},
               'C': {'score': 78, 'age': 22}}

sorted_nested_dict = OrderedDict(sorted(nested_dict.items(), key=lambda x: (x[1]['score'], x[1]['age'])))

print(sorted_nested_dict)
