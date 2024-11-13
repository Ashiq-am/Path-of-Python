# Method 3: Using the sort() Method with a Custom Comparator
list_of_dicts = [{'name': 'tarjan', 'height': 30}, {'name': 'blon', 'height': 89}, {'name': 'starc', 'height': 75}]
list_of_dicts.sort(key=lambda x: x['height'], reverse=True)


#Display the list of dictionaries
print(list_of_dicts)
