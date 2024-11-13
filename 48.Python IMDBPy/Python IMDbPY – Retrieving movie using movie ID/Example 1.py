# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# ID
code = "1187043"

# searching the Id
search = ia.get_movie(code)

# printing the search
print(search)
