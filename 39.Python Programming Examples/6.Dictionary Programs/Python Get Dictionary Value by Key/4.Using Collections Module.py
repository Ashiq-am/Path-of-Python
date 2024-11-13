from collections import defaultdict

# Creating a defaultdict with a default value of 'Unknown'
sample_dict = defaultdict(lambda: 'Unknown', {'name': 'geeks', 'age': 21, 'place': 'India'}
)

# Accessing value using bracket notation
country_value = sample_dict['place']
print("Country:", country_value)
