# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6468322"

# getting information
series = ia.get_movie(code)

# getting votes of the series
votes = series.data['votes']

# printing the object i.e name
print(series)

# print the votes
print(votes)
