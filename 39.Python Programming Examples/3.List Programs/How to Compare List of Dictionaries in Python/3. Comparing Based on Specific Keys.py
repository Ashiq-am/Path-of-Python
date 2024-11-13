# code
list1 = [{'id': 1, 'name': 'Ram'}, {'id': 2, 'name': 'Mohan'}]
list2 = [{'id': 2, 'name': 'Sohan'}, {'id': 3, 'name': 'Shyam'}]

ids_list1 = {item['id'] for item in list1}
ids_list2 = {item['id'] for item in list2}

common_ids = ids_list1.intersection(ids_list2)
print("Common IDs:", common_ids)
