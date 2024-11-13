from collections import defaultdict

# Example using lambda and defaultdict
my_dict = defaultdict(lambda: 0)
my_dict['apple'] = 5
my_dict['banana'] = 3

# Accessing a key that doesn't exist
value = my_dict['grape']
print("value of the key", value)
