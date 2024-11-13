# function to add key vales
def add_pair(dictionary, key, value):
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]

# initialize dictionary
my_dict = {}

# key value pair 1
add_pair(my_dict, 'a', 1)
add_pair(my_dict, 'a', 1)

# key value pair 2
add_pair(my_dict, 'b', 2)
add_pair(my_dict, 'b', 2)

print(my_dict)
