# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# ID
code = "4434004"

# getting movie
movie = ia.get_movie(code)

# printing movie object
print(movie)

print("===============")

# getting cast
cast = movie['art department']

# printing actors name from caste
print(cast[0])
