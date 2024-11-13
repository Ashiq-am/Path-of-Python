# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6077448"

# getting information
series = ia.get_movie(code)

# getting gerne of the series
genre = series.data['genres']

# printing the object i.e name
print(series)

# print the gerne
print(genre)
