# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6468322"

# getting information
series = ia.get_movie(code)

# getting languages of the series
languages = series.data['languages']

# printing the object i.e name
print(series)

# print the languages
print(languages)
