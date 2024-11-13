# Importing required modules
import json
import datetime

# Create a datetime object
dt = datetime.datetime.now()

# Convert the datetime object to a string in a specific format
dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")

# Serialize the string using the json module
json_data = json.dumps(dt_str)
print(json_data)
