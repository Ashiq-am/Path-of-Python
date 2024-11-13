# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# name
name = "Amir khan"

# searching the name
persons = ia.search_person(name)

person = persons[0]

# getting more information
ia.update(person, info=['biography'])

# printing biography
print(person['biography'])
