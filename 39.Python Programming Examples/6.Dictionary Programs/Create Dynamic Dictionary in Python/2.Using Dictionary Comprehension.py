# create two lists for keys and values
keys = ['a', 'b', 'c']
values = [1, 2, 3]

# using dictionary comprehension to create a dictionary
dynamic_dict = {keys[i]: values[i] for i in range(len(keys))}
print(dynamic_dict)
