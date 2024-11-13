import json

json_data = '{"name": "Bob", "age": 25, "city": "Los Angeles"}'

# Custom function to convert JSON to a custom object
def custom_decoder(dct):
    if 'name' in dct:
        dct['name'] = dct['name'].upper()
    return dct

decoder = json.JSONDecoder(object_hook=custom_decoder)
python_obj = decoder.decode(json_data)

print(python_obj)
