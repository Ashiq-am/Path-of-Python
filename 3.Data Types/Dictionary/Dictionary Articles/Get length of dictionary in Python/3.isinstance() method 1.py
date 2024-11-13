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
            'Street':
                {
                    'st_number': 4,
                    'st_name': 'Rockins Road'
                },
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

        # add the length of inner dictionary
        length += len(i)

        # check whether th inner dictionary
        # is further nested
        for j in i.values():

            if isinstance(j, dict):
                length += len(j)

print("The total length of the dictionary is ", length)
