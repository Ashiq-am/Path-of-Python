# Without dict.get(key)
my_dict = {'a': 1, 'b': 2}
try:
    value = my_dict['c']
except KeyError:
    value = 0

# Using dict.get(key)
value = my_dict.get('c', 0)
print(value)
