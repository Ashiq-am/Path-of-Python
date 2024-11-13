# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# keyword
keyword = "Delhi"

# searching keyword
search = ia.search_keyword(keyword)

# printing the search
print(search)
