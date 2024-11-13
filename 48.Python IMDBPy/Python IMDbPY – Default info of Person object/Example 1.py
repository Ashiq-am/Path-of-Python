# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# ID
code = "2690647"

# searching the Id
person = ia.get_person(code)

# getting default info
info = person.default_info

# printing name
print(person['name'])

# printing the info
print(info)
