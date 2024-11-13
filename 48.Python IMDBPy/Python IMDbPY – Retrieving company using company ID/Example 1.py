# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# ID
code = "0051941"

# searching the Id
search = ia.get_company(code)

# printing the search
print(search)
