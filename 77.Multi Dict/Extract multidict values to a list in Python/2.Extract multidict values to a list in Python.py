# Import module 'Multidict'
import multidict

# create a multidict
d = multidict.MultiDict([('a', 1), ('b', 2),
                         ('b', 3), ('c', 5),
                         ('d', 4), ('c', 7)])

# create two blank lists to store
# the values
list_for_values_of_multidict = []

# Loop through the multidict structure
# using "items" method Use append method
# of list to add respective keys and
# values of multidict
for k, v in d.items():
    # place the values in separate list
    list_for_values_of_multidict.append(v)

# print the lists
print("List of values of multidict:", list_for_values_of_multidict)
