# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# getting the movie with id
search = ia.get_movie("0111161")

# getting movie year
year = search['year']

# printing movie name and year
print(search['title'] + " : " + str(year))
