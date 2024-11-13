# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# name of the company
name = "Universal Studios Hollywood"

# searching the name of the company
search = ia.search_company(name)

# printing the search
print(search)

# printing the name
for i in range(len(search)):
	print(search[i]['name'])
