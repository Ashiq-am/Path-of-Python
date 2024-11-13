# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6468322"

# getting information
series = ia.get_movie(code)

# printing title
print(series.data['title'])

print("--------------------------------")

# converting series object's CAST into XML file
xml_cast = series.getAsXML('cast')

# printing some part of the XML file
print(xml_cast[:100])
