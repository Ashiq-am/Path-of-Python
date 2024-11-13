# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "0903747"

# getting information
series = ia.get_movie(code)

# getting synopsis of the series
synopsis = series.data['synopsis']

# printing the object i.e name
print(series)

# print the synopsis
print(synopsis)
