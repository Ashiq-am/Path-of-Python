# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# name of the movie
name = "Jab Taare Utare Zameen Par"

# searching the name of the movie
search = ia.search_movie(name)

# prinitng whole list
print(search)

# printing the movies
for i in range(len(search)):
	print(search[i]['title'])
