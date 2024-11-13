# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# name of the company
name = "Walt Disney"

# searching the name of the company
search = ia.search_company(name)


# printing the name
for i in range(len(search)):
	print(search[i]['name'])
