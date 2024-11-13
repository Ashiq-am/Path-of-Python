# Without dict.get(key)
my_dict = {'a': 1, 'b': 2}
if 'c' in my_dict:
    value = my_dict['c']
else:
    value = 0

# Using dict.get(key)
value = my_dict.get('c', 0)  # Simplifies the code
print(value)
