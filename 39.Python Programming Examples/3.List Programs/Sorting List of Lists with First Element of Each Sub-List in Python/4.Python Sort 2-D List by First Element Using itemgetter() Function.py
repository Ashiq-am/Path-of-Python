# Using the itemgetter Function from the operator Module
from operator import itemgetter
list_of_lists = [[3, 'b'], [1, 'a'], [2, 'c']]
sorted_list= sorted(list_of_lists, key=itemgetter(0))

# Display sorted list
print(sorted_list)
