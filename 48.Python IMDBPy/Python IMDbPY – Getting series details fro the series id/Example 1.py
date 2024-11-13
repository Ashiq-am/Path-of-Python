# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6473300"

# getting information
series = ia.get_movie(code)

# printing title
print(series.data['title'])

# printing writer name
print(series.data['writer'])
