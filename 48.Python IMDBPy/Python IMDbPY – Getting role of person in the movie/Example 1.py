# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "1187043"

# getting information
movie = ia.get_movie(code)

# printing movie name
cast = movie['cast']

# printing actor name
print(cast[0])

# getting role
role = cast[0].currentRole

# printig role
print(role)
