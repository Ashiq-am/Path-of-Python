# create a list of tuples.
test = [(1, 2), (1, 4), (3, 5), (5, 7)]

# create a empty dictionary name new_dict
new_dict = {}

# a for loop to iterate the list of tuples
for i in test:

    # checking whether the dictionary
    # has the key already.
    # If it returns No, a new Key is created.
    # If the key is not present the first
    # value of the tuple is made as the key
    if new_dict.get(i[0], 'No') == 'No':

        # THe remaining element is made
        # as values of the key
        new_dict[i[0]] = i[1:]
    else:
        # If the key is already present assign
        # the remaining element as values to
        # the corresponding key
        new_dict[i[0]] = new_dict.get(i[0]) + i[1:]
print(new_dict)
