# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# person id
code = "1372788"

# getting person oject
actor = ia.get_person(code)

# printing object it prntts its name
print(actor)

# getting birth place
place = actor['birth info']['birth place']

# printing the place
print(place)
