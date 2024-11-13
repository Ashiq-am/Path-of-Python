# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# name of the person
name = "Neil Nitin mukesh"

# searching the name of the person
search = ia.search_person(name)

# printing the name
for i in range(len(search)):
	print(search[i]['name'])
