# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# name
name = "Success story"

# searching the name
movies = ia.search_movie(name)

movie = movies[0]

# getting more information
ia.update(movie, info=['plot'])

# printing plot
print(movie['plot'])
