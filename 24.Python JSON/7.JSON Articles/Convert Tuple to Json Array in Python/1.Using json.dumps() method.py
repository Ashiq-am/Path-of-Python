import json
physics_tuple = ('Class 9', 'Physics', 'Laws of Motion', 'Introduction', 'Newton First Law')

# Convert tuple to JSON
json_data = json.dumps(physics_tuple)

# Display the result
print(type(json_data))
print(json_data)
