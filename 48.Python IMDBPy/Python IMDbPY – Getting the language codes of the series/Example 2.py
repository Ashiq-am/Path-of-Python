# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6468322"

# getting information
series = ia.get_movie(code)

# getting language codes of the series
codes = series.data['language codes']

# printing the object i.e name
print(series)

# print the language codes
print(codes)
