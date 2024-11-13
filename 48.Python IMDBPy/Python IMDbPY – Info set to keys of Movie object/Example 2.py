# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# ID
code = "4434004"

# searching the Id and getting info set
movie = ia.get_movie(code, info=['plot'])

# making infoset to use as keys
movie.infoset2keys

# printing movie plot
print(movie['plot'])
