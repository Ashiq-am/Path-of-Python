# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# name
name = "3 idiots"

# searching the name
movies = ia.search_movie(name)

movie = movies[0]

# getting more information
ia.update(movie, info=['taglines'])

# printing tagline
print(movie['taglines'])
