from operator import itemgetter

# Sample list of dictionaries
list_of_dicts = [{'key1': 10, 'key2': 20}, {'key1': 30, 'key2': 40}, {'key1': 50, 'key2': 60}]

# Key to extract values from
desired_key = 'key1'

# Using itemgetter
result = list(map(itemgetter(desired_key), list_of_dicts))

print(result)
