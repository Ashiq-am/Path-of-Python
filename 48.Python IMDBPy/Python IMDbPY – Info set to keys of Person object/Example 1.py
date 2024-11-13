# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# ID
code = "4731677"

# searching the Id and getting info set
person = ia.get_person(code, info=['biography'])

# making infoset to use as keys
person.infoset2keys

# printing bio graphy
print(person['biography'])
