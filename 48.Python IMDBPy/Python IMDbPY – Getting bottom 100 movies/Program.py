# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# getting top 250 movies
search = ia.get_bottom100_movies()

# printing only last 10 movies title
for i in range(90, 100):
	print(search[i]['title'])
