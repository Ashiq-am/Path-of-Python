# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6468322"

# getting information
series = ia.get_movie(code)

# getting seasons of the series
season = series.data['seasons']

# printing the object i.e name
print(series)

# print the seasons
print(season)
