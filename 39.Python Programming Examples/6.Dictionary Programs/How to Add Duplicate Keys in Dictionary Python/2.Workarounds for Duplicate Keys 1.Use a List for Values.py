# Initialize the dictionary
duplicate_dict = {}

# Function to add a key-value pair
def add_to_dict(key, value):
    if key in duplicate_dict:
        duplicate_dict[key].append(value)
    else:
        duplicate_dict[key] = [value]

# Add values to the dictionary
add_to_dict('Platform', 'GeeksForGeeks')
add_to_dict('Courses', 'MERN')
add_to_dict('Courses', 'DSA')

print(duplicate_dict)
