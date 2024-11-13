# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6468322"

# getting information
series = ia.get_movie(code)

# getting rating of the series
rating = series.data['rating']

# printing the object i.e name
print(series)

# print the rating
print(rating)
