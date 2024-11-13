from operator import itemgetter

def sort_nested_dict(nested_dict, *keys):
    sorted_items = sorted(nested_dict.items(), key=lambda x: itemgetter(*keys)(x[1]))
    return {k: v for k, v in sorted_items}

nested_dict = {'A': {'score': 85, 'age': 25},
               'B': {'score': 92, 'age': 30},
               'C': {'score': 78, 'age': 22}}

sorted_nested_dict = sort_nested_dict(nested_dict, 'score', 'age')

print(sorted_nested_dict)
# Nikunj Sonigara
