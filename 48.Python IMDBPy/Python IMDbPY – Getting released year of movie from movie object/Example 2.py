# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# getting the movie with name
search = ia.search_movie("Dil Se")

# getting movie year
year = search[0]['year']

# printing movie name and year
print(search[0]['title'] + " : " + str(year))
