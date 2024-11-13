# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# getting the company info set of data base
info = ia.get_company_infoset()

# printing the list
for element in info:
	print(element)
