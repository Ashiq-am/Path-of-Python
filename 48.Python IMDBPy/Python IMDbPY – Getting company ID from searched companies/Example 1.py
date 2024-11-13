# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# name
name = "Marvel"

# searching the name
search = ia.search_company(name)

# loop for printing the name and id
for i in range(len(search)):
    # getting the id
    id = search[i].companyID

    # printing it
    print(search[i]['name'] + " : " + id)
