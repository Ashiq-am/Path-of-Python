import orjson

# Non-existent JSON file path
json_file = 'a.json'

try:
    # Reading JSON data from file
    with open(json_file, 'r') as f:
        json_data = f.read()

    # Parsing JSON data using orjson.loads()
    data = orjson.loads(json_data)

    # Displaying the parsed data
    print(data)
except FileNotFoundError:
    print("File not found:", json_file)
except orjson.JSONDecodeError as e:
    print("Error parsing JSON:", e)
