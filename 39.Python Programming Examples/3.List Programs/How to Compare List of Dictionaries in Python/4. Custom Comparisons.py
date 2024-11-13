# code
def compare_dicts(dict1, dict2):
    return dict1['id'] == dict2['id'] and dict1['name'].lower() == dict2['name'].lower()

list1 = [{'id': 1, 'name': 'Ram'}, {'id': 2, 'name': 'Mohan'}]
list2 = [{'id': 2, 'name': 'sohan'}, {'id': 3, 'name': 'Shyam'}]

common_dicts = [d1 for d1 in list1 for d2 in list2 if compare_dicts(d1, d2)]
print("Common dictionaries with custom comparison:", common_dicts)
