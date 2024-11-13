# Initialize the dictionary
multi_value_dict = {}

# Function to add a key-value pair
def add_to_dict(key, value):
    if key not in multi_value_dict:
        multi_value_dict[key] = {}
    if value in multi_value_dict[key]:
        multi_value_dict[key][value] += 1
    else:
        multi_value_dict[key][value] = 1

# Add values to the dictionary
add_to_dict('Platform', 'GeeksForGeeks')
add_to_dict('Courses', 'MERN')
add_to_dict('Courses', 'DSA')
add_to_dict('Courses', 'DSA')


# Print the dictionary
print(multi_value_dict)
