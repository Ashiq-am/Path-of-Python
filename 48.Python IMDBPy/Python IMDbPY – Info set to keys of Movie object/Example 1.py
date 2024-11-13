# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# ID
code = "0094226"

# searching the Id and getting info set
movie = ia.get_movie(code, info=['taglines', 'plot'])

# making infoset to use as keys
movie.infoset2keys

# printing movie tagline
print(movie['taglines'])
