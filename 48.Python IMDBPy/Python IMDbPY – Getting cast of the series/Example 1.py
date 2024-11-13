# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "0903747"

# getting information
series = ia.get_movie(code)

# getting cast of the series
cast = series.data['cast']

# printing the object i.e name
print(series)

# print the cast person at index 0
print(cast[0])
