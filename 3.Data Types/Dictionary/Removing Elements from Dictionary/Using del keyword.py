"""In Python Dictionary, deletion of keys can be done by using the del keyword.
Using del keyword, specific values from a dictionary as well as whole dictionary can be deleted.
Items in a Nested dictionary can also be deleted by using del keyword and providing specific nested key and
particular key to be deleted from that nested Dictionary.

Note- del Dict will delete the entire dictionary and hence printing it after deletion will raise an Error."""





# Initial Dictionary
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',
		'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
		'B' : {1 : 'Geeks', 2 : 'Life'}}
print("Initial Dictionary: ")
print(Dict)

# Deleting a Key value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)

# Deleting a Key from
# Nested Dictionary
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)
