# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# ID
code = "4434004"

# getting movie
movie = ia.get_movie(code)

# person id
code2 = "1372788"

# getting person
person = ia.get_person(code2)

# printing movie object
print(movie)

# printing person object
print(person)

print("===============")

# checking if person is in the movie or not
if person in movie:
    print("Yes !!")

else:
    print("No !!")
