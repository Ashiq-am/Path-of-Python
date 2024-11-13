my_dict = {'name': 'geeks', 'age': 21, 'country': 'india'}

key_to_remove = 'age'
updated_dict = {k: v for k, v in my_dict.items() if k != key_to_remove}

print(f"Item with key '{key_to_remove}' removed. Updated dictionary: {updated_dict}")
