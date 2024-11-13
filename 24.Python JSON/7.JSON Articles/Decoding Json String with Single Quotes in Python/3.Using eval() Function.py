json_string = "{'name': 'Ragu','age': 30,'salary':30000,'address': { 'street': 'Gradenl','city': 'Pune'}}"
# converting the json singe quote string to dictionary
my_dict = eval(json_string)

print("Decoding Using single quotes:")
print("The address of %s is" % my_dict["name"], my_dict["address"])