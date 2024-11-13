import json

class CustomDecoder(json.JSONDecoder):
    def decode(self, s, _w=json.decoder.WHITESPACE.match):
        obj = super().decode(s, _w)
        # Custom logic: Convert all string values to uppercase
        for key in obj:
            if isinstance(obj[key], str):
                obj[key] = obj[key].upper()
        return obj

# JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Create a CustomDecoder object
decoder = CustomDecoder()

# Decode the JSON string using the custom decoder
python_obj = decoder.decode(json_string)

print(python_obj)
