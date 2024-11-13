# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6473300"

# getting information
series = ia.get_movie(code)

# getting countries of the series
countries = series.data['countries']

# printing the object i.e name
print(series)

# print the countries
print(countries)
