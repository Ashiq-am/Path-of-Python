import json

json_string = "{'name': 'Ragu','age': 30,'salary':30000,'address': { 'street': 'Gradenl','city': 'Pune'}}"
my_dict = json.loads(json_string.replace("'", "\""))

print("Decoding Using single quotes:")
print("The address of %s is" % my_dict['name'], my_dict['address'])