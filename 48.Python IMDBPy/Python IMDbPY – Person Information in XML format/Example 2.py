# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "2690647"

# getting information
person = ia.get_person(code)

# printing name
print(person['name'])

print("--------------------------------")

# converting person object into XML file
xml_file = person.asXML()

# printing some part of the XML file
print(xml_file[:250])
