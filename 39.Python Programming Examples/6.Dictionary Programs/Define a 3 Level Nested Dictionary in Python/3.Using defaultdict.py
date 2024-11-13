from collections import defaultdict

# Using defaultdict
nested_dict = defaultdict(lambda: defaultdict(dict))
nested_dict['first_level_key1']['second_level_key1']['third_level_key1'] = 'value1'
nested_dict['first_level_key1']['second_level_key1']['third_level_key2'] = 'value2'

# Example
print(nested_dict['first_level_key1']['second_level_key1']['third_level_key1'])
