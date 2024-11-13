# Python program to find
# length of nested dictionary


# nested dictionary
dict2 = {
    'Name':
        {
            'first_name': 'Steve',
            'Last_name': 'Jobs'
        },
    'Age': 30,
    'Designation': 'Programmer',
    'address':
        {
            'Street': 'Rockins Road',
            'City': 'Bangalore',
            'Country': 'India'
        }
}

# storing the outer dictionary length
length = len(dict2)

# iterating to find the length
# of all inner dictionaries
for i in dict2.values():

    # checking whether the value is a dictionary
    if isinstance(i, dict):
        length += len(i)

print("The length of the dictionary is", length)
