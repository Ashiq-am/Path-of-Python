# create dictionary dynamically using the zip() function
keys = ['a', 'b', 'c']
values = [1, 2, 3]

# creating a dictionary by zipping keys and values together
dynamic_dict = dict(zip(keys, values))
print(dynamic_dict)
