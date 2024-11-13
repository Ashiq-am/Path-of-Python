# Using the sorted() Function with Itemgetter
from operator import itemgetter
list_of_dicts = [{'class': '5', 'section': 3}, {'Class': 'Five', 'section':7}, {'Class': 'Five', 'section': 2}]
sorted_list = sorted(list_of_dicts, key=itemgetter('section'), reverse=True)

#Display the list of dictionaries
print(sorted_list)
