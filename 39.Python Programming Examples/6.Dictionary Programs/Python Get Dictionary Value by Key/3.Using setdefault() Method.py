# Creating a sample dictionary
sample_dict = {'name': 'geeks', 'age': 21, 'place': 'India'}

# Using setdefault() method
name_value = sample_dict.setdefault('name', 'Default Name')
print("Name:", name_value)

# Using setdefault() for a key not present in the dictionary
country_value = sample_dict.setdefault('country', 'Unknown')
print("Country:", country_value)
