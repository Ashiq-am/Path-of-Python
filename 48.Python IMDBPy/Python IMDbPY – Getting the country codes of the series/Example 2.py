# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6077448"

# getting information
series = ia.get_movie(code)

# getting countries of the series
country_codes = series.data['country codes']

# printing the object i.e name
print(series)

# print the country codes
print(country_codes)
