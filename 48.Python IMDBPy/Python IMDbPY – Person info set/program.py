# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# getting the person info set of data base
info = ia.get_person_infoset()

# printing the list
for element in info:
	print(element)
