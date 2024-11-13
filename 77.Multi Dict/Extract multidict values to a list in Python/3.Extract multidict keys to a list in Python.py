# Import module 'Multidict'
import multidict

# create a multidict
d = multidict.MultiDict([('a', 1), ('b', 2),
                         ('b', 3), ('c', 5),
                         ('d', 4), ('c', 7)])

# create two blank lists to store the keys
list_for_key_of_multidict = []

# Loop through the multidict structure
# using "items" method Use append method
# of list to add respective keys and
# values of multidict
for k, v in d.items():
    # place the keys in separate list
    list_for_key_of_multidict.append(k)

# print the lists
print("List of keys of multidict:", list_for_key_of_multidict)
