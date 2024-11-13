# Using List Comprehension with Sorted
list_of_dicts = [{'word': 'Geeks', 'letter': 1}, {'word': 'Geeks', 'letter':3}, {'word': 'for', 'letter': 2}]
sorted_list = [x for x in sorted(list_of_dicts, key=lambda x: x['letter'], reverse=True)]

#Display sorted list
print(sorted_list)
