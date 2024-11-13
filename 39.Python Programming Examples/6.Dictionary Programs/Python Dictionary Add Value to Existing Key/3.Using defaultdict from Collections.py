from collections import defaultdict

my_dict = defaultdict(int, {'a': 1, 'b': 2})

# Add 3 to the value of key 'a'
my_dict['a'] += 3

print(my_dict)
