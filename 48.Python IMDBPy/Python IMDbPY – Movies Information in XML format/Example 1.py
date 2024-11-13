# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "1187043"

# getting information
movie = ia.get_movie(code)

# printing movie name
print(movie['title'])

print("--------------------------------")

# converting movie object into XML file
xml_file = movie.asXML()

# printing some part of the XML file
print(xml_file[:150])
