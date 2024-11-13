# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# person id
code = "0001098"

# printing person name
print(ia.get_person(code))

# getting information
actor_results = ia.get_person_filmography(code)

# printing movie name
for index in range(5):
	movie_name = actor_results['data']['filmography'][0]['actor'][index]
	print(movie_name)
