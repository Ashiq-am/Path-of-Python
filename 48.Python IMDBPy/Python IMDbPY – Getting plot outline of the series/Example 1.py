# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6077448"

# getting information
series = ia.get_movie(code)

# getting plot outline of the series
outline = series.data['plot outline']

# printing the object i.e name
print(series)

# print the outline
print(outline)
