# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# ID
code = "4731677"

# searching the Id
search = ia.get_person(code)

# printing the search
print(search)
