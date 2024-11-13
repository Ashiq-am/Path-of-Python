import json

json_data = '{"price": 12.34, "discount": 0.1}'

# Custom float parsing function
def parse_custom_float(value):
    return round(float(value), 1)

decoder = json.JSONDecoder(parse_float=parse_custom_float)
python_obj = decoder.decode(json_data)

print(python_obj)
