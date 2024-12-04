nested_dict = {'person': {'name': 'Alice', 'age': 25}, 'address': {'city': 'New York'}}
try:
    value = nested_dict['person']['salary']
except KeyError:
    print("Key not found!")