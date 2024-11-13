# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# name
name = "Al Pacino"

# searching the name
search = ia.search_person(name)

# loop for printing the name and id
for i in range(len(search)):
    # getting the id
    id = search[i].personID

    # printing it
    print(search[i]['name'] + " : " + id)
