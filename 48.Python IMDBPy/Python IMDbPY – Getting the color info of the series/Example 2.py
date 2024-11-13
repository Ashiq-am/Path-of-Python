# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6077448"

# getting information
series = ia.get_movie(code)

# getting color info of the series
info = series.data['color info']

# printing the object i.e name
print(series)

# print the color info
print(info)
