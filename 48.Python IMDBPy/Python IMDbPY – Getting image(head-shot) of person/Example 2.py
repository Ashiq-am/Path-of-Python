# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# person id
code = "1596350"

# getting person oject
actor = ia.get_person(code)

# printing object it prntts its name
print(actor)

# getting image
image = actor['headshot']

# printing the place
print(image)
