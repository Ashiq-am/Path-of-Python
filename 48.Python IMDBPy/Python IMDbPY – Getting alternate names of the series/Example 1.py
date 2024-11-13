# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "0903747"

# getting information
series = ia.get_movie(code)

# getting alternate names of the series
names = series.data['akas']

# printing the object i.e name
print(series)

# print the series names
print(names)
