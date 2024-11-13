import json

# Example JSON data with bytes encoded using different encodings
json_data_utf16 = b'\xff\xfe{\x00"\x00n\x00a\x00m\x00e\x00"\x00:\x00 \x00"\x00A\x00n\x00i\x00l\x00"\x00,\x00 \x00"\x00a\x00g\x00e\x00"\x00:\x00 \x002\x005\x00,\x00 \x00"\x00c\x00i\x00t\x00y\x00"\x00:\x00 \x00"\x00N\x00e\x00w\x00 \x00Y\x00o\x00r\x00k\x00"\x00}\x00'

# Decode bytes with different encodings
decoded_data_utf16 = json_data_utf16.decode('utf-16')
parsed_json_utf16 = json.loads(decoded_data_utf16)

# Accessing values from parsed JSON
name_utf16 = parsed_json_utf16['name']
age_utf16 = parsed_json_utf16['age']
city_utf16 = parsed_json_utf16['city']

# Printing parsed values
print("Name (UTF-16):", name_utf16)
print("Age (UTF-16):", age_utf16)
print("City (UTF-16):", city_utf16)
