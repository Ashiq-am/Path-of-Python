# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "6468322"

# getting information
series = ia.get_movie(code)

# getting production companies of the series
companies = series.data['production companies']

# printing the object i.e name
print(series)

# print the companies
print(companies)
