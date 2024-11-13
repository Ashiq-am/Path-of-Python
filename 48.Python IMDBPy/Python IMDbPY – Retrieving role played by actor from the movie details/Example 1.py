# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# ID
code = "1187043"

# getting movie
movie = ia.get_movie(code)

# printing movie object
print(movie)

print("===============")

# getting cast
cast = movie['cast']

# actor name from caste
actor = cast[35]
print(actor)

# role played
role = actor.notes

print(role)
