# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6077448"

# getting information
series = ia.get_movie(code)

# printing title
print(series.data['title'])

print("--------------------------------")

# converting series object's RUN TIMES into XML file
xml = series.getAsXML('runtimes')

# printing the XML file
print(xml)
