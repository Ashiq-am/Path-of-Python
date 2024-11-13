# Python program to demonstrate
# dynamic dictionary creation


# Key to be added
key_ref = 'More Nested Things'
my_dict = {
    'Nested Things': [{'name', 'thing one'}, {'name', 'thing two'}]
}

# Value to be added
my_list_of_things = [{'name', 'thing three'}, {'name', 'thing four'}]

# try-except to take care of errors
# while adding key-value pair
try:
    my_dict[key_ref].append(my_list_of_things)

except KeyError:
    my_dict = {**my_dict, **{key_ref: my_list_of_things}}

print(my_dict)
