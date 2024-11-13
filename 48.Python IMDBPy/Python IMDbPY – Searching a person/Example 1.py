# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# name of the person
name = "Akshay Kumar"

# searchning the name of the person
search = ia.search_person(name)

# printing the result
for i in search :
	print(i)
