# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# person id
person_id = "0000206"

# getting person details
search = ia.get_person(person_id)

# printing the search
# printing name and birth date
print(search['name'] + " " +search['birth date'])
