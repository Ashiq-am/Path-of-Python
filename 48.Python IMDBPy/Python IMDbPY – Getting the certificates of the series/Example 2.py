# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6077448"

# getting information
series = ia.get_movie(code)

# getting certificates of the series
certificate = series.data['certificates']

# printing the object i.e name
print(series)

# print the certificate
print(certificate)
