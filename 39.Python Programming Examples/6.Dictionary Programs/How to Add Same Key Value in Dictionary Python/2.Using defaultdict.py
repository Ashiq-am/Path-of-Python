# import collection module
from collections import defaultdict

# function to add key vales
def add_pairs(dictionary, key, value):
    dictionary[key].append(value)

# initialize dictionary
my_dict = defaultdict(list)

# key value pair 1
add_pairs(my_dict, 'a', 1)
add_pairs(my_dict, 'a', 1)

# key value pair 2
add_pairs(my_dict, 'b', 2)
add_pairs(my_dict, 'b', 2)

print(my_dict)
