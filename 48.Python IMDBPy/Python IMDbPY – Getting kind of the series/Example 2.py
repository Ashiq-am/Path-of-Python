# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6468322"

# getting information
series = ia.get_movie(code)

# getting kind of the series
kind = series.data['kind']

# printing the object i.e name
print(series)

# print the kind
print(kind)
