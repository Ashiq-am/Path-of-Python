# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "0903747"

# getting information
series = ia.get_movie(code)

# getting series year of the series
years = series.data['series years']

# printing the object i.e name
print(series)

# print the series year
print(years)
