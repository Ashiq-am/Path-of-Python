# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# keyword
keyword = "marvel"

# searching keyword
search = ia.get_keyword(keyword)

# printing the search
print(len(search))
print(search[0])
