# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6077448"

# getting information
series = ia.get_movie(code)

# getting number of seasons in the series
count = series.data['number of seasons']

# printing the object i.e name
print(series)

# print the count
print(count)
