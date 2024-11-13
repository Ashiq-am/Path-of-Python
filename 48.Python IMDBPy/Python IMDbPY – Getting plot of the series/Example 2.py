# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6468322"

# getting information
series = ia.get_movie(code)

# getting plot of the series
plot = series.data['plot']

# printing the object i.e name
print(series)

# print the plot
print(plot)
