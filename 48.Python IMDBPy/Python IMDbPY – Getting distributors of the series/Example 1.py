# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6468322"

# getting information
series = ia.get_movie(code)

# getting distributors companies of the series
distributors = series.data['distributors']

# printing the object i.e name
print(series)

# print the distributors
print(distributors)
