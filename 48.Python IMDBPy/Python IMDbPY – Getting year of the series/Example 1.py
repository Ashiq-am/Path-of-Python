# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6468322"

# getting information
series = ia.get_movie(code)

# getting year of the series
year = series.data['year']

# printing the object i.e name
print(series)

# print the year
print(year)
