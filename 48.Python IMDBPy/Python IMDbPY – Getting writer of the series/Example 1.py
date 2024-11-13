# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6468322"

# getting information
series = ia.get_movie(code)

# getting wruters of the series
writer = series.data['writer']

# printing the object i.e name
print(series)

# print the writers
print(writer)
