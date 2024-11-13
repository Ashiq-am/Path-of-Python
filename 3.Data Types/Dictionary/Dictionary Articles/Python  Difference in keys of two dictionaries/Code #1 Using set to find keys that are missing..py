# Python code to find the difference in
# keys in two dictionary

# Initialising dictionary
dict1= {'key1':'Geeks', 'key2':'For', 'key3':'geeks'}
dict2= {'key1':'Geeks', 'key2:':'Portal'}

diff = set(dict2) - set(dict1)

# Printing difference in
# keys in two dictionary
print(diff)
