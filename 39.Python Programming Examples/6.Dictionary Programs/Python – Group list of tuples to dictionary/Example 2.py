# create a list of tuples
test = [(1, 2, 3, 4, 5, 6), (1, 4),
        (3, 5, 3, 4, 5, 6), (5, 7),
        (5, 6), (4, 4)]

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

        # THe remaining element is
        # made as values of the key
        new_dict[i[0]] = i[1:]
    else:

        # If the key is already present assign
        # the remaining element as values to
        # the corresponding key
        # add the values to the tuples and them
        # convert them to list using list() function
        new_dict[i[0]] = list(new_dict.get(i[0]) + i[1:])

# if the length of value is 1,
# it would be still as tuple,
# so conver them as list using list() function
for k, v in new_dict.items():
    if len(v) == 1:
        new_dict[k] = list(v)
print(new_dict)
