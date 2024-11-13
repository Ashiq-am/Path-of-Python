# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# ID
code = "1187043"

# searching the Id
movie = ia.get_movie(code)

# getting default info
info = movie.default_info

# printing movie title
print(movie['title'])

# printing the info
print(info)
