# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# person id
code = "1372788"

# getting person object
actor = ia.get_person(code)

# printing object it prints its name
print(actor)

# getting alternate names
alternate = actor['akas']

# printing
print(alternate)
