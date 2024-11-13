import json
from datetime import datetime
def custom_decoder(dict_data):
    if 'date' in dict_data:
        dict_data['date'] = datetime.strptime(dict_data['date'], '%Y-%m-%d')
    return dict_data

json_data = '{"name": "Alice", "date": "2021-08-01"}'
decoder = json.JSONDecoder(object_hook=custom_decoder)
data = decoder.decode(json_data)
print(data)
