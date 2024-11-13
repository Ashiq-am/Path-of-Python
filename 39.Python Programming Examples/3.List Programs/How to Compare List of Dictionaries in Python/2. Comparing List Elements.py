# code
list1 = [{'id': 1, 'name': 'Ram'}, {'id': 2, 'name': 'Mohan'}]
list2 = [{'id': 2, 'name': 'Sohan'}, {'id': 3, 'name': 'Shyam'}]

common_dicts = [dict1 for dict1 in list1 if dict1 in list2]
print("Common dictionaries:", common_dicts)
