# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# name
name = "Robert Downey"

# searching the name
persons = ia.search_person(name)

person = persons[0]

# getting more information
ia.update(person, info=['other works'])

# printing other works
print(person['other works'])
