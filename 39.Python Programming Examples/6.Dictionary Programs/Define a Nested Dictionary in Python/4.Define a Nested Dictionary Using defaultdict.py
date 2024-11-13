from collections import defaultdict

nested_dict = defaultdict(dict)
nested_dict['outer_key']['inner_key1'] = 'value1'
nested_dict['outer_key']['inner_key2'] = 'value2'
print(dict(nested_dict))
