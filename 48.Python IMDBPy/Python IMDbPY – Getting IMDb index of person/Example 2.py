# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# person id
code = "0262635"

# getting person oject
actor = ia.get_person_filmography(code)

# printing object name
print(actor['data']['name'])

# getting index
index = actor['data']['imdbIndex']

# printing
print(index)
