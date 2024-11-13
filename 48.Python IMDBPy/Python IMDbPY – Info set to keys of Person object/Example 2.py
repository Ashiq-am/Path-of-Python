# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# ID
code = "2690647"

# searching the Id and getting info set
person = ia.get_person(code, info=['filmography'])

# making infoset to use as keys
person.infoset2keys

# printing filmo graphy
print(person['filmography'])
